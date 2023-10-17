import tkinter as tk
from federal_cnd import emitir_cnd_federal
from estadual_cnd import emitir_cnd_estadual
from municipal_cnd import emitir_cnd_municipal

def main():
    window = tk.Tk()
    window.title("Menu CND")
    window.geometry("300x300")
    title = tk.Label(window, text="Menu CND", font=("Arial", 12))
    title.pack(pady=20)
    window.configure(bg='lightgray')



    federal_btn = tk.Button(window, text="Federal", command=emitir_cnd_federal)
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
