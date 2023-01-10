import os
import tempfile

import fitz

def extract_text_from_pdf(pdf_path):
    """Extrai o texto de um arquivo PDF."""
    if not os.path.exists(pdf_path):
        raise ValueError('Arquivo PDF não encontrado: {}'.format(pdf_path))

    with open(pdf_path, 'rb') as pdf_file:
        # Cria um objeto Document da PyMuPDF
        doc = fitz.open(pdf_file)

        # Inicializa uma string vazia para armazenar o texto extraído
        text = ""

        # Itera sobre as páginas do documento
        for page in doc:
            # Obtém o texto da página e adiciona à string de texto total
            text += page.get_text()

    return text
