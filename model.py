from transformers import AutoTokenizer, AutoModel
import torch
from sentence_transformers import SentenceTransformer, util
import gensim.downloader as api
import spacy
import numpy as np
from rake_nltk import Rake


class SentenceModel():
    def __init__(self, model_name):
        print("Loading sentence embedding model.")
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)
    
    def encode(self, text):
        print("Processing sentence encoding.")
        output = self.model.encode(text)
        output = torch.Tensor(output).unsqueeze(0)
        return output
    
class WordModel():
    def __init__(self, model_name):
        print("Loading word embedding model.")
        self.model_name = model_name
        self.word2vec = api.load("glove-wiki-gigaword-300")
    def encode(self, text):
        print("Processing word encoding.")
        r = Rake()
        r.extract_keywords_from_text(text)
        phrases = r.get_ranked_phrases_with_scores()
        
        mean = torch.zeros(300)
        sum = 0
        for phrase in phrases:
            embeddings = []
            for token in phrase[1].split():
                if token in self.word2vec:
                    embeddings.append(self.word2vec[token])
            if embeddings:
                embeddings = np.array(embeddings)
                mean_embedding = torch.tensor(embeddings).mean(dim=0)
                mean_embedding = torch.nn.functional.normalize(mean_embedding, p=2, dim=0)
                mean += mean_embedding * phrase[0]
                sum += phrase[0]
        mean = mean / sum
        return mean.unsqueeze(0)