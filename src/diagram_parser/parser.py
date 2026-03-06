from pathlib import Path
from typing import List, Optional, Tuple

import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class DiagramParser:
    """
    Interpreta um diagrama de arquitetura em imagem e extrai componentes.
    """

    def __init__(self, model_path: Optional[Path] = None):
        self.model_path = model_path
        try:
            pytesseract.get_tesseract_version()
        except pytesseract.TesseractNotFoundError:
            print(
                "Tesseract is not installed or it's not in your PATH. "
                "Please install it from the official website and add it to your PATH."
            )
            raise pytesseract.TesseractNotFoundError

    def parse(self, image_path: Path) -> List[dict]:
        """
        Analisa a imagem e retorna lista de componentes.

        Cada componente: {"type": str, "label": str, "bbox": (x1,y1,x2,y2) opcional}
        """
        if not image_path.exists():
            raise FileNotFoundError(f"Image not found at {image_path}")
        
        image = cv2.imread(str(image_path))
        # Aplica um filtro para reduzir o ruído, preservando as bordas
        image = cv2.bilateralFilter(image, 9, 75, 75)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Aplica thresholding adaptativo para binarizar a imagem
        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        
        # Extrai texto com Pytesseract
        results = pytesseract.image_to_data(thresh, output_type=pytesseract.Output.DICT)
        
        # Encontra contornos
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        components = []
        for i in range(len(results["text"])):
            text = results["text"][i]
            conf = int(results["conf"][i])
            
            if conf > 60 and text.strip() != "": # Filtra por confianca e texto nao vazio
                x, y, w, h = results["left"][i], results["top"][i], results["width"][i], results["height"][i]
                center_x = x + w / 2
                center_y = y + h / 2

                # Associa texto a um contorno
                for contour in contours:
                    if cv2.pointPolygonTest(contour, (center_x, center_y), False) >= 0:
                        x_c, y_c, w_c, h_c = cv2.boundingRect(contour)
                        components.append({
                            "type": "Component", # Placeholder
                            "label": text,
                            "bbox": (x_c, y_c, x_c + w_c, y_c + h_c)
                        })
                        break # Evita associar a múltiplos contornos
        
        return components
