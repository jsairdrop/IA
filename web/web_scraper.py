import tkinter
from tkinter import filedialog
import tkinter.simpledialog
import tkinter as tk
import os
import requests
import model
from bs4 import BeautifulSoup


def search_web(num_results=None):
    search_term = tkinter.simpledialog.askstring('Pesquisar na web', 'Insira o termo de pesquisa:')
    if not search_term:
        return

    # Fazer a pesquisa no Google
    url = 'https://www.google.com/search?q={}'.format(search_term)
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError('Erro ao fazer a pesquisa: status code {}'.format(response.status_code))

    # Extrair os resultados da pesquisa da página HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div', class_='g')

    # Exibir os resultados da pesquisa em uma janela de seleção
    window = tk.Tk()
    window.title('Selecione os resultados da pesquisa')

    # Criar uma lista de caixas de seleção para cada resultado da pesquisa
    var_list = []
    for i, result in enumerate(results):
        title = result.find('h3').text  # Título do resultado da pesquisa
        url = result.find('cite').text  # URL do resultado da pesquisa

        # Criar uma caixa de seleção para o resultado da pesquisa
        var = tk.IntVar()
        checkbox = tk.Checkbutton(window, text=title, variable=var)
        checkbox.pack()
        var_list.append((var, url))

    # Criar um campo de input para o usuário inserir o número de resultados desejados
    num_results_label = tk.Label(window, text='Número de resultados:')
    num_results_label.pack()
    num_results_entry = tk.Entry(window)
    num_results_entry.pack()

    # Obter o número de resultados desejados pelo usuário
    try:
        num_results = int(num_results_entry.get())
    except ValueError:
        tk.messagebox.showerror('Erro', 'O número de resultados deve ser um número inteiro')
        return

    # Criar um botão de "Tokenizar"
    tokenize_button = tk.Button(window, text='Tokenizar', command=lambda: tokenize_selected(var_list))
    tokenize_button.pack()

    # Exibir a janela de seleção
    window.mainloop()

    def tokenize_selected(var_list):
            """Tokenizar os resultados da pesquisa selecionados pelo usuário."""
            data = []
            for var, url in var_list:
                if var.get() == 1:  # Se o resultado da pesquisa estiver selecionado
                    response = requests.get(url)
                if response.status_code != 200:
                    raise ValueError('Erro ao acessar o site: status code {}'.format(response.status_code))
                text = response.text
                data.append(model.text_processing.preprocess_text(text))

            save_location = filedialog.asksaveasfilename(defaultextension='.txt')
            if not save_location:
                return

            # Verificar se o arquivo de saída já existe
            if os.path.exists(save_location):
                # Se o arquivo já existe, perguntar ao usuário se deseja sobrescrevê-lo
                if not tk.messagebox.askyesno('Atenção', 'O arquivo já existe. Deseja sobrescrevê-lo?'):
                    return

            # Salvar os dados tokenizados em um arquivo de saída
            with open(save_location, 'w') as f:
                for text in data:
                    f.write(text + '\n')
                    f.write('\n')