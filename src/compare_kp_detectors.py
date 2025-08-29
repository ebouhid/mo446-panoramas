# -*- coding: utf-8 -*-
"""
Script para Análise Comparativa de Detectores de Keypoints (SIFT vs. ORB vs. AKAZE).

Este script executa o pipeline de construção de panorama para os detectores SIFT, ORB e AKAZE,
coleta métricas de desempenho e robustez, e salva os resultados em um arquivo CSV
para análise científica, conforme solicitado no T1 de MO446/MC449.

Uso:
    python benchmark_detectors.py --input_dir <caminho_para_imagens> --output_csv <caminho_para_salvar.csv> \
        [--detectors SIFT,ORB,AKAZE]

Argumento --detectors (opcional) aceita lista separada por vírgulas para escolher subconjunto.

Dependências:
    - opencv-python
    - opencv-contrib-python (necessário para o SIFT)
    - numpy
    - pandas
"""
import cv2
import numpy as np
import os
import time
import pandas as pd
import argparse
from typing import List, Dict, Any, Optional
from main import load_images

def create_detector_and_matcher(detector_type: str, nfeatures: Optional[int]):
    """Cria o detector de características e o matcher correspondente.

    Parâmetros
    ----------
    detector_type : str
        Nome do detector (SIFT, ORB, AKAZE)
    nfeatures : int | None
        Número máximo de keypoints (relevante para SIFT e ORB). Ignorado para AKAZE.
    """
    dt = detector_type.upper()
    if dt == 'SIFT':
        detector = cv2.SIFT_create(nfeatures=nfeatures)
        FLANN_INDEX_KDTREE = 1
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)
        matcher = cv2.FlannBasedMatcher(index_params, search_params)
    elif dt == 'ORB':
        detector = cv2.ORB_create(nfeatures=nfeatures)
        matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)
    elif dt == 'AKAZE':
        # AKAZE gera descritores binários (MLDB); usar BFMatcher Hamming
        # nfeatures não é parâmetro; controlar nº de pontos via threshold se desejado (não exposto aqui)
        detector = cv2.AKAZE_create()
        matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)
    else:
        raise ValueError(f"Detector '{detector_type}' não suportado.")
    return detector, matcher

def evaluate_detector(images: List[np.ndarray], params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Executa o pipeline para um detector e coleta métricas.
    Retorna um dicionário com os resultados médios por par de imagens.
    """
    detector_type = params['detector_type']
    nfeatures = params.get('nfeatures')  # pode ser None para AKAZE
    ratio_thresh = params['ratio_thresh']
    ransac_thresh = params['ransac_thresh']

    detector, matcher = create_detector_and_matcher(detector_type, nfeatures)
    
    start_time = time.time()

    # 1. Detectar características
    dataset = []
    total_keypoints = 0
    for im in images:
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        kp, desc = detector.detectAndCompute(gray, None)
        dataset.append({'kp': kp, 'desc': desc})
        total_keypoints += len(kp)

    # 2. Fazer matching e estimar homografia para cada par
    total_good_matches = 0
    total_inliers = 0
    num_pairs = len(dataset) - 1

    for i in range(num_pairs):
        desc1, desc2 = dataset[i]['desc'], dataset[i+1]['desc']
        if desc1 is None or desc2 is None or len(desc1) < 2 or len(desc2) < 2:
            continue

        knn_matches = matcher.knnMatch(desc1, desc2, k=2)
        
        good_matches = []
        for m, n in knn_matches:
            if m.distance < ratio_thresh * n.distance:
                good_matches.append(m)
        
        total_good_matches += len(good_matches)
        
        if len(good_matches) >= 4:
            kpA, kpB = dataset[i]['kp'], dataset[i+1]['kp']
            ptsA = np.float32([kpA[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
            ptsB = np.float32([kpB[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
            
            _, inliers_mask = cv2.findHomography(ptsA, ptsB, method=cv2.RANSAC, ransacReprojThreshold=ransac_thresh)
            if inliers_mask is not None:
                total_inliers += int(inliers_mask.sum())

    end_time = time.time()
    
    # Calcular médias e resultados
    results = {
        'Detector': detector_type,
        'Nº Médio de Keypoints': round(total_keypoints / len(images), 2),
        'Nº Médio de Matches (Pós-Ratio Test)': round(total_good_matches / num_pairs, 2),
        'Nº Médio de Inliers (Pós-RANSAC)': round(total_inliers / num_pairs, 2),
        'Tempo Total de Execução (s)': round(end_time - start_time, 4)
    }
    
    return results

def main():
    """Função principal para executar a análise comparativa."""
    parser = argparse.ArgumentParser(description="Análise comparativa entre detectores SIFT e ORB.")
    parser.add_argument('--input_dir', type=str, required=True, help="Pasta com as imagens de entrada.")
    parser.add_argument('--output_csv', type=str, required=True, help="Arquivo CSV para salvar os resultados.")
    parser.add_argument('--detectors', type=str, default='SIFT,ORB,AKAZE',
                        help="Lista separada por vírgulas dos detectores a avaliar (ex: SIFT,ORB,AKAZE)")
    args = parser.parse_args()

    # Carrega as imagens
    images, _ = load_images(args.input_dir)

    # Parâmetros baseados no notebook fornecido
    params = {
        'nfeatures': 12000,
        'ratio_thresh': 0.75, # Usando um valor mais comum que o 0.25 do notebook, que é muito restritivo
        'ransac_thresh': 1.5
    }

    # Lista para armazenar os resultados de cada detector
    benchmark_results = []

    detectors_to_test = [d.strip().upper() for d in args.detectors.split(',') if d.strip()]

    for detector in detectors_to_test:
        print("-" * 50)
        print(f"Avaliando o detector: {detector}")
        current_params = params.copy()
        current_params['detector_type'] = detector
        
        try:
            result = evaluate_detector(images, current_params)
            benchmark_results.append(result)
            print(f"Resultados para {detector}: {result}")
        except Exception as e:
            print(f"ERRO ao avaliar {detector}: {e}")

    # Cria e salva o DataFrame com os resultados
    if benchmark_results:
        df = pd.DataFrame(benchmark_results)
        df.to_csv(args.output_csv, index=False)
        print("-" * 50)
        print(f"Análise concluída. Resultados salvos em: {args.output_csv}")
        print("\nConteúdo do CSV gerado:")
        print(df.to_string(index=False))
    else:
        print("Nenhuma análise foi concluída com sucesso.")

if __name__ == "__main__":
    main()
