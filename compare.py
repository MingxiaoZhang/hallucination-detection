from model import SentenceModel, WordModel
from sentence_transformers import util
import torch

def compare(ground_truth, llm_output): 
    word_model = WordModel('bert-large-cased')
    ground_truth_word_embedding = word_model.encode(ground_truth)
    llm_output_word_embedding = word_model.encode(llm_output)
    
    sentence_model = SentenceModel('stsb-bert-large')
    ground_truth_sentence_embedding = sentence_model.encode(ground_truth)
    llm_output_sentence_embedding = sentence_model.encode(llm_output)

    word_similarity = util.pytorch_cos_sim(ground_truth_word_embedding, llm_output_word_embedding).item()
    sentence_similarity = util.pytorch_cos_sim(ground_truth_sentence_embedding, llm_output_sentence_embedding).item()

    similarity = 0.3 * word_similarity + 0.7 * sentence_similarity

    if similarity > 0.85: 
        semantic_relationship = "Strong"
    elif similarity > 0.6:
        semantic_relationship = "Neutral"
    else:
        semantic_relationship = "Weak"

    return word_similarity, sentence_similarity, similarity, semantic_relationship