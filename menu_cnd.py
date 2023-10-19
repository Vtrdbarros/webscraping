import tkinter as tk
import logging
from federal_cnd import emitir_cnd_federal
from estadual_cnd import emitir_cnd_estadual
from municipal_cnd import emitir_cnd_municipal

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def show_cnpj_dialog():
    logging.info("Exibindo campo de entrada CNPJ...")
    
    def on_confirm():
        cnpj_value = cnpj_entry.get()
        dialog.destroy()  # fecha a janela de diálogo
        emitir_cnd_federal(cnpj_value)

    dialog = tk.Toplevel()  # cria uma nova janela
    dialog.title("Informe o CNPJ")

    cnpj_label = tk.Label(dialog, text="CNPJ:")
    cnpj_label.pack(pady=10)

    cnpj_entry = tk.Entry(dialog)
    cnpj_entry.pack(pady=10)

    confirm_btn = tk.Button(dialog, text="Confirmar", command=on_confirm)
    confirm_btn.pack(pady=10)


def main():
    window = tk.Tk()
    window.title("Menu CND")
    window.geometry("300x300")
    title = tk.Label(window, text="Menu CND", font=("Arial", 12))
    title.pack(pady=20)
    window.configure(bg='lightgray')
    
    federal_btn = tk.Button(window, text="Federal", command=show_cnpj_dialog)
    federal_btn.pack(pady=20)
    federal_btn.configure(bg='blue', fg='white')

    estadual_btn = tk.Button(window, text="Estadual", command=emitir_cnd_estadual)
    estadual_btn.pack(pady=20)
    estadual_btn.configure(bg='green', fg='white')

    municipal_btn = tk.Button(window, text="Municipal", command=emitir_cnd_municipal)
    municipal_btn.pack(pady=20)
    municipal_btn.configure(bg='red', fg='white')

    window.mainloop()

if __name__ == "__main__":
    main()
