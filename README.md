Projeto Panoramas - Visão Computacional
Este repositório contém o desenvolvimento do trabalho da disciplina de Visão Computacional, focado na construção de imagens panorâmicas a partir de múltiplas fotos.

Objetivo
O objetivo geral do trabalho é aplicar conceitos de Visão Computacional para construir panoramas a partir de múltiplas imagens, desenvolvendo competências práticas em detecção de características, emparelhamento, estimação de homografia e blending.

Equipe
- Eduardo Bouhid (RA: 299223)
- Lucas Rodrigues (RA: xxxxxx)
- Marcelo Campos (RA: xxxxxx)
- Thiago Rodrigues (RA: xxxxxx)

Estrutura do Repositório
O projeto está organizado da seguinte forma para facilitar a colaboração e o desenvolvimento:

**OBS.:** Essa estrutura é uma sugestão inicial e provavelmente o resultado final será um pouco diferente.

```
.
├── .gitignore             # Ignora arquivos desnecessários (dados, venv, cache)
├── README.md              # Este arquivo de documentação
├── requirements.txt       # Lista de dependências Python para o projeto
├── main.py                # Placeholder, vamos incluir futuramente
|
├── data/                  # Contém as imagens de entrada.
│   ├── nossas_imagens/      # Imagens capturadas pela equipe
│   └──
│
├── notebooks/             # Notebooks Jupyter para demonstração e testes
│   └── keypoints.ipynb    # Demonstração/teste dos métodos de detecção de pontos-chave
│
├── src/                   # Todo o código-fonte modularizado
│   ├── keypoints.py       # Placeholder, vamos incluir futuramente
│   ├── emparelhamento.py  # Placeholder, vamos incluir futuramente
│   ├── homografia.py      # Placeholder, vamos incluir futuramente
│   ├── composicao.py      # Placeholder, vamos incluir futuramente
│   └── utils.py           # Placeholder, vamos incluir futuramente
│
├── results/               # Contém os resultados gerados. ESTA PASTA NÃO É VERSIONADA.
│   ├── panoramas_finais/  # Os panoramas finais gerados automaticamente
│   └── visualizacoes/     # Imagens intermediárias (keypoints, matches, alinhamentos)
│
└── docs/                  # Contém os entregáveis finais do projeto
    ├── relatorio.pdf      # Relatório técnico completo
    └── apresentacao.pptx  # Slides para a apresentação oral
```
## Configuração do Ambiente
Para executar este projeto, siga os passos abaixo:

1. Clone o repositório:

```
git clone <url_do_nosso_repo>
cd <nome_do_nosso_repo>
```
2. Crie e ative um ambiente virtual:
(Vamos definir a versão do python depois, vou deixar em branco por enquanto)

3. Instale as dependências:

```pip install -r requirements.txt```

4. Prepare os dados:
Crie a pasta data/ na raiz do projeto (se ela não existir) e adicione as subpastas com as imagens que serão usadas. Esta pasta é ignorada pelo Git para evitar o versionamento de arquivos grandes.

## Como Executar
O script principal main.py foi projetado para executar todo o processo de criação do panorama.

Para gerar um panorama, utilize o seguinte comando no terminal:

```python main.py --input-dir data/nossas_imagens --output-path results/panoramas_finais/panorama_final.jpg --detector orb```

Argumentos do script:
```
--input-dir: O caminho para a pasta que contém a sequência de imagens de entrada.

--output-path: O caminho completo onde o panorama final será salvo.

--detector: O detector de características a ser usado (sift, orb, ou akaze).
```
## Informações da Disciplina

Trabalho: Panoramas / T1

Professor: Prof. Anderson Rocha

Prazo de Entrega previsto: 31 de Agosto, 2025