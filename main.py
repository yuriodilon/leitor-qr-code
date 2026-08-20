# main.py - Arquivo na raiz do projeto
import sys
import os

# Adicionar src ao path se necessário
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from src.main import main
except ImportError:
    # Fallback se executar diretamente
    from src.qr_scanner import QRCodeScanner
    
    def main():
        app = QRCodeScanner()
        app.run()

if __name__ == "__main__":
    main()