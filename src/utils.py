from tkinter import messagebox

def copy_to_clipboard(root, text):
    """Copia texto para o clipboard"""
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()
    messagebox.showinfo("Sucesso", "Texto copiado para a área de transferência!")