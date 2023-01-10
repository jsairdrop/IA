import gensim


def topic_model(data, num_topics=5, num_words=5):
    """Realiza a modelagem de tópicos em um conjunto de dados e retorna os tópicos e palavras mais relevantes."""
    dictionary = gensim.corpora.Dictionary(data)
    corpus = [dictionary.doc2bow(doc) for doc in data]
    model = gensim.models.LdaModel(corpus, num_topics=num_topics, id2word=dictionary)
    topics = model.print_topics(num_topics=num_topics, num_words=num_words)
    return topics
