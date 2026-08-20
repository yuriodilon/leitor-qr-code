import sys
import cv2
import numpy as np
from PIL import ImageGrab, Image
from pyzbar.pyzbar import decode
import tkinter as tk
from tkinter import messagebox
import time
from src.utils import copy_to_clipboard

class QRCodeScanner:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Leitor de QR Code - Captura de Tela")
        self.root.geometry("400x300")
        self.root.configure(bg='#2c3e50')
        
        # Variáveis para controle da seleção
        self.start_x = None
        self.start_y = None
        self.rect = None
        self.selection_window = None
        self.canvas = None
        
        self.setup_ui()
        
    def setup_ui(self):
        """Configura a interface do usuário"""
        # Título
        title_label = tk.Label(
            self.root, 
            text="📷 Leitor de QR Code", 
            font=("Arial", 18, "bold"),
            bg='#2c3e50',
            fg='white'
        )
        title_label.pack(pady=20)
        
        # Botão para capturar
        capture_btn = tk.Button(
            self.root,
            text="🔍 Capturar QR Code",
            command=self.start_capture,
            font=("Arial", 14),
            bg='#3498db',
            fg='white',
            padx=20,
            pady=10,
            relief='flat',
            cursor='hand2'
        )
        capture_btn.pack(pady=20)
        
        # Área para mostrar resultado
        self.result_frame = tk.Frame(
            self.root,
            bg='#34495e',
            padx=10,
            pady=10
        )
        self.result_frame.pack(pady=20, fill='both', expand=True)
        
        self.result_label = tk.Label(
            self.result_frame,
            text="Aguardando captura...",
            font=("Arial", 12),
            bg='#34495e',
            fg='white',
            wraplength=350
        )
        self.result_label.pack()
        
        # Botão para limpar resultado
        clear_btn = tk.Button(
            self.root,
            text="Limpar Resultado",
            command=self.clear_result,
            font=("Arial", 10),
            bg='#e74c3c',
            fg='white',
            padx=15,
            pady=5,
            relief='flat',
            cursor='hand2'
        )
        clear_btn.pack(pady=5)
        
        # Instruções
        instructions = tk.Label(
            self.root,
            text="Clique em 'Capturar QR Code' e selecione a área do QR Code",
            font=("Arial", 9),
            bg='#2c3e50',
            fg='#95a5a6'
        )
        instructions.pack(pady=10)
        
        # Vincular tecla ESC para fechar seleção
        self.root.bind('<Escape>', self.cancel_selection)
        
        # Centralizar janela
        self.center_window()
        
    def center_window(self):
        """Centraliza a janela principal na tela"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def start_capture(self):
        """Inicia o processo de captura de tela"""
        self.root.iconify()
        time.sleep(0.3)
        
        self.selection_window = tk.Toplevel(self.root)
        self.selection_window.attributes('-fullscreen', True)
        self.selection_window.attributes('-alpha', 0.3)
        self.selection_window.configure(bg='black')
        self.selection_window.attributes('-topmost', True)
        
        self.selection_window.focus_force()
        
        self.canvas = tk.Canvas(
            self.selection_window,
            highlightthickness=0,
            bg='black'
        )
        self.canvas.pack(fill='both', expand=True)
        
        self.canvas.bind('<ButtonPress-1>', self.on_mouse_down)
        self.canvas.bind('<B1-Motion>', self.on_mouse_drag)
        self.canvas.bind('<ButtonRelease-1>', self.on_mouse_up)
        self.canvas.bind('<Escape>', self.cancel_selection)
        
        self.start_x = None
        self.start_y = None
        self.rect = None
        
    def on_mouse_down(self, event):
        """Início da seleção"""
        self.start_x = event.x
        self.start_y = event.y
        
        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y,
            self.start_x, self.start_y,
            outline='white',
            width=2,
            fill='blue',
            stipple='gray50'
        )
        
    def on_mouse_drag(self, event):
        """Durante o arrastar do mouse"""
        if self.rect:
            self.canvas.coords(
                self.rect,
                self.start_x, self.start_y,
                event.x, event.y
            )
            
    def on_mouse_up(self, event):
        """Fim da seleção - capturar área"""
        if self.rect and self.start_x is not None:
            try:
                x1 = min(self.start_x, event.x)
                y1 = min(self.start_y, event.y)
                x2 = max(self.start_x, event.x)
                y2 = max(self.start_y, event.y)
                
                self.selection_window.destroy()
                self.selection_window = None
                
                self.capture_area(x1, y1, x2, y2)
                
            except Exception as e:
                print(f"Erro na seleção: {e}")
                self.cancel_selection(None)
        else:
            self.cancel_selection(None)
            
    def capture_area(self, x1, y1, x2, y2):
        """Captura a área selecionada da tela"""
        try:
            if x2 - x1 < 10 or y2 - y1 < 10:
                messagebox.showwarning(
                    "Área muito pequena",
                    "Selecione uma área maior para capturar o QR Code."
                )
                self.root.deiconify()
                return
                
            screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
            
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            
            qr_codes = self.read_qr_code(frame)
            
            if qr_codes:
                self.show_results(qr_codes)
            else:
                messagebox.showinfo(
                    "Nenhum QR Code encontrado",
                    "Não foi possível encontrar QR Code na área selecionada."
                )
                
            self.root.deiconify()
            self.root.lift()
            
        except Exception as e:
            print(f"Erro na captura: {e}")
            messagebox.showerror("Erro", f"Erro ao capturar área: {str(e)}")
            self.root.deiconify()
            
    def read_qr_code(self, image):
        """Lê QR Codes de uma imagem usando pyzbar"""
        try:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
            
            decoded_objects = decode(thresh)
            
            if not decoded_objects:
                decoded_objects = decode(image)
                
            results = []
            for obj in decoded_objects:
                data = obj.data.decode('utf-8')
                results.append(data)
                
            return results
            
        except Exception as e:
            print(f"Erro ao ler QR Code: {e}")
            return None
            
    def show_results(self, qr_codes):
        """Mostra os resultados na interface"""
        if qr_codes:
            result_window = tk.Toplevel(self.root)
            result_window.title("📋 QR Code Encontrado!")
            result_window.geometry("500x300")
            result_window.configure(bg='#ecf0f1')
            
            result_window.transient(self.root)
            result_window.grab_set()
            
            main_frame = tk.Frame(result_window, bg='#ecf0f1')
            main_frame.pack(fill='both', expand=True, padx=20, pady=20)
            
            title_label = tk.Label(
                main_frame,
                text="✅ QR Code Detectado!",
                font=("Arial", 16, "bold"),
                bg='#ecf0f1',
                fg='#2c3e50'
            )
            title_label.pack(pady=10)
            
            for i, qr_data in enumerate(qr_codes):
                info_frame = tk.Frame(main_frame, bg='#ffffff', relief='solid', bd=1)
                info_frame.pack(fill='x', pady=5)
                
                content_label = tk.Label(
                    info_frame,
                    text=f"QR Code {i+1}:",
                    font=("Arial", 10, "bold"),
                    bg='#ffffff'
                )
                content_label.pack(anchor='w', padx=10, pady=5)
                
                qr_text = tk.Text(
                    info_frame,
                    height=2,
                    wrap='word',
                    font=("Arial", 10),
                    bg='#f8f9fa'
                )
                qr_text.insert('1.0', qr_data)
                qr_text.config(state='disabled')
                qr_text.pack(fill='x', padx=10, pady=5)
                
                copy_btn = tk.Button(
                    info_frame,
                    text="📋 Copiar",
                    command=lambda d=qr_data: copy_to_clipboard(self.root, d),
                    bg='#3498db',
                    fg='white',
                    relief='flat',
                    cursor='hand2'
                )
                copy_btn.pack(anchor='e', padx=10, pady=5)
            
            close_btn = tk.Button(
                main_frame,
                text="Fechar",
                command=result_window.destroy,
                bg='#e74c3c',
                fg='white',
                relief='flat',
                padx=20,
                pady=5,
                cursor='hand2'
            )
            close_btn.pack(pady=10)
            
            self.result_label.config(
                text=f"✅ QR Code encontrado: {qr_codes[0][:50]}...",
                fg='#2ecc71'
            )
            
        else:
            self.result_label.config(
                text="❌ Nenhum QR Code encontrado",
                fg='#e74c3c'
            )
            
    def clear_result(self):
        """Limpa o resultado exibido"""
        self.result_label.config(
            text="Aguardando captura...",
            fg='white'
        )
        
    def cancel_selection(self, event):
        """Cancela a seleção atual"""
        if self.selection_window:
            self.selection_window.destroy()
            self.selection_window = None
        self.root.deiconify()
        self.root.lift()
        
    def run(self):
        """Inicia a aplicação"""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            print("Programa interrompido pelo usuário")
        except Exception as e:
            print(f"Erro na execução: {e}")
            messagebox.showerror("Erro", f"Erro na execução: {str(e)}")