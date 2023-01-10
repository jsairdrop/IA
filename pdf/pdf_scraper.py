import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

import pdf.pdf_utils
import model.text_processing


def tokenize_pdfs():
    root = tk.Tk()  # Criar a janela principal
    root.withdraw()  # Esconder a janela principal

    pdf_paths = tk.filedialog.askopenfilenames(filetypes=[('Arquivos PDF', '*.pdf')])
    if not pdf_paths:
        return

    data = []
    for pdf_path in pdf_paths:
        text = pdf.pdf_utils.extract_text_from_pdf(pdf_path)  # Adicionar o prefixo "pdf."
        data.append(model.text_processing.preprocess_text(text))

    save_location = tk.filedialog.asksaveasfilename(defaultextension='.txt')
    if not save_location:
        return

    # Verificar se o arquivo de saída já existe
    if os.path.exists(save_location):
        # Se o arquivo já existe, perguntar se o utilizador deseja adicionar as novas tokenizações ao final do arquivo
        # existente
        choice = tk.messagebox.askyesno('Arquivo existente',
                                        'O arquivo de saída já existe. Deseja adicionar as novas tokenizações ao '
                                        'final do arquivo existente?')
        if choice:
            # Abrir o arquivo em modo de adição ("a") para adicionar as novas tokenizações ao final do arquivo
            with open(save_location, "a") as f:
                # Adicionar as novas tokenizações ao arquivo
                for text in data:
                    f.write(' '.join(text))  # Transforma a lista em uma ‘string’ e escreve no arquivo
                    f.write('\n')
        else:
            # Se o utilizador não deseja adicionar as novas tokenizações ao arquivo existente, pedir para ele escolher
            # um novo nome para o arquivo
            save_location = filedialog.asksaveasfilename(defaultextension='.txt')
            # Criar o novo arquivo e adicionar as tokenizações
            with open(save_location, "w") as f:
                for text in data:
                    f.write(' '.join(text))  # Transforma a lista em uma string e escreve no arquivo
                    f.write('\n')
