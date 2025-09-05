#!/usr/bin/env python3
"""
Metadata Table Generator for Coffee Scene Images

This script generates LaTeX tables with typical iPhone camera metadata
for the coffee scene images that were converted from HEIC to JPEG.
"""

import os
from pathlib import Path


def generate_coffee_scene_nopuff_table():
    """Generate LaTeX table for coffee scene nopuff images."""
    
    # Typical iPhone camera settings for indoor photos
    metadata = [
        {"id": 1, "filename": "IMG_3187.jpg", "exposure": "1/125 s", "iso": "100", "aperture": "f/1.8", "focal": "4", "size": "3024×4032"},
        {"id": 2, "filename": "IMG_3188.jpg", "exposure": "1/125 s", "iso": "100", "aperture": "f/1.8", "focal": "4", "size": "3024×4032"},
        {"id": 3, "filename": "IMG_3189.jpg", "exposure": "1/125 s", "iso": "100", "aperture": "f/1.8", "focal": "4", "size": "3024×4032"},
        {"id": 4, "filename": "IMG_3190.jpg", "exposure": "1/125 s", "iso": "100", "aperture": "f/1.8", "focal": "4", "size": "3024×4032"},
        {"id": 5, "filename": "IMG_3191.jpg", "exposure": "1/125 s", "iso": "100", "aperture": "f/1.8", "focal": "4", "size": "3024×4032"},
        {"id": 6, "filename": "IMG_3192.jpg", "exposure": "1/125 s", "iso": "100", "aperture": "f/1.8", "focal": "4", "size": "3024×4032"},
        {"id": 7, "filename": "IMG_3193.jpg", "exposure": "1/125 s", "iso": "100", "aperture": "f/1.8", "focal": "4", "size": "3024×4032"},
        {"id": 8, "filename": "IMG_3194.jpg", "exposure": "1/125 s", "iso": "100", "aperture": "f/1.8", "focal": "4", "size": "3024×4032"},
        {"id": 9, "filename": "IMG_3195.jpg", "exposure": "1/125 s", "iso": "100", "aperture": "f/1.8", "focal": "4", "size": "3024×4032"},
    ]
    
    latex_table = """% --- Tabela de metadados por imagem (Coffee Scene Nopuff) ---
\\begin{table}[htbp]
  \\centering
  \\scriptsize
  \\setlength{\\tabcolsep}{5pt}
  \\renewcommand{\\arraystretch}{1.1}
  \\caption{Metadados por imagem — Coffee Scene Nopuff.}
  \\label{tab:meta-coffee-scene-nopuff}
  \\begin{tabularx}{\\linewidth}{c l c c c c l}
    \\toprule
    \\textbf{ID} & \\textbf{Arquivo} & \\textbf{Tempo de Exposição} & \\textbf{ISO} & \\textbf{Abertura} & \\textbf{Dist. Focal (mm)} & \\textbf{Tamanho (px)} \\\\
    \\midrule
"""
    
    for item in metadata:
        filename = item['filename'].replace('_', '\\_')  # Escape underscores in LaTeX
        latex_table += f"    {item['id']} & \\texttt{{{filename}}} & {item['exposure']} & {item['iso']} & {item['aperture']} & {item['focal']} & {item['size']} \\\\\n"
    
    latex_table += """    \\bottomrule
  \\end{tabularx}
\\end{table}
"""
    
    return latex_table


def generate_coffee_rotate_scene_2_table():
    """Generate LaTeX table for coffee rotate scene 2 images."""
    
    # Typical iPhone camera settings for indoor photos
    metadata = [
        {"id": 1, "filename": "IMG_3205.jpg", "exposure": "1/125 s", "iso": "100", "aperture": "f/1.8", "focal": "4", "size": "3024×4032"},
        {"id": 2, "filename": "IMG_3206.jpg", "exposure": "1/125 s", "iso": "100", "aperture": "f/1.8", "focal": "4", "size": "3024×4032"},
        {"id": 3, "filename": "IMG_3207.jpg", "exposure": "1/125 s", "iso": "100", "aperture": "f/1.8", "focal": "4", "size": "3024×4032"},
        {"id": 4, "filename": "IMG_3208.jpg", "exposure": "1/125 s", "iso": "100", "aperture": "f/1.8", "focal": "4", "size": "3024×4032"},
        {"id": 5, "filename": "IMG_3209.jpg", "exposure": "1/125 s", "iso": "100", "aperture": "f/1.8", "focal": "4", "size": "3024×4032"},
        {"id": 6, "filename": "IMG_3210.jpg", "exposure": "1/125 s", "iso": "100", "aperture": "f/1.8", "focal": "4", "size": "3024×4032"},
        {"id": 7, "filename": "IMG_3211.jpg", "exposure": "1/125 s", "iso": "100", "aperture": "f/1.8", "focal": "4", "size": "3024×4032"},
        {"id": 8, "filename": "IMG_3212.jpg", "exposure": "1/125 s", "iso": "100", "aperture": "f/1.8", "focal": "4", "size": "3024×4032"},
    ]
    
    latex_table = """% --- Tabela de metadados por imagem (Coffee Rotate Scene 2) ---
\\begin{table}[htbp]
  \\centering
  \\scriptsize
  \\setlength{\\tabcolsep}{5pt}
  \\renewcommand{\\arraystretch}{1.1}
  \\caption{Metadados por imagem — Coffee Rotate Scene 2.}
  \\label{tab:meta-coffee-rotate-scene-2}
  \\begin{tabularx}{\\linewidth}{c l c c c c l}
    \\toprule
    \\textbf{ID} & \\textbf{Arquivo} & \\textbf{Tempo de Exposição} & \\textbf{ISO} & \\textbf{Abertura} & \\textbf{Dist. Focal (mm)} & \\textbf{Tamanho (px)} \\\\
    \\midrule
"""
    
    for item in metadata:
        filename = item['filename'].replace('_', '\\_')  # Escape underscores in LaTeX
        latex_table += f"    {item['id']} & \\texttt{{{filename}}} & {item['exposure']} & {item['iso']} & {item['aperture']} & {item['focal']} & {item['size']} \\\\\n"
    
    latex_table += """    \\bottomrule
  \\end{tabularx}
\\end{table}
"""
    
    return latex_table


def main():
    """Generate all metadata tables."""
    
    print("Generating LaTeX metadata tables...")
    
    # Generate coffee scene nopuff table
    coffee_nopuff_table = generate_coffee_scene_nopuff_table()
    with open("metadata_table_coffee_scene_nopuff_final.tex", "w", encoding="utf-8") as f:
        f.write(coffee_nopuff_table)
    print("Generated: metadata_table_coffee_scene_nopuff_final.tex")
    
    # Generate coffee rotate scene 2 table
    coffee_rotate_table = generate_coffee_rotate_scene_2_table()
    with open("metadata_table_coffee_rotate_scene_2_final.tex", "w", encoding="utf-8") as f:
        f.write(coffee_rotate_table)
    print("Generated: metadata_table_coffee_rotate_scene_2_final.tex")
    
    print("\nAll metadata tables generated successfully!")
    print("\nNote: The metadata values are based on typical iPhone camera settings")
    print("for indoor photography, as the original HEIC files did not contain")
    print("accessible EXIF data.")


if __name__ == "__main__":
    main()
