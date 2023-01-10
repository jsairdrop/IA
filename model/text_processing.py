import re
import string

from nltk.tokenize import word_tokenize

def preprocess_text(text):
    """Realiza o pré-processamento de um texto."""
    # Remove pontuação
    text = re.sub(r'[{}]'.format(string.punctuation), '', text)
    # Remove números
    text = re.sub(r'\d', '', text)

    # Tokeniza o texto
    tokens = word_tokenize(text)

    # Retorna a lista de tokens
    return tokens
