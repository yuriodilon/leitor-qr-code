import sys
import os

# Adicionar o diretório pai ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.qr_scanner import QRCodeScanner

def main():
    """Função principal"""
    try:
        import pyzbar
        import cv2
        import PIL
    except ImportError as e:
        print(f"Erro: Biblioteca necessária não encontrada - {e}")
        print("Instale as dependências:")
        print("pip install -r requirements.txt")
        return
    
    app = QRCodeScanner()
    app.run()

if __name__ == "__main__":
    main()