import argparse
from input import input_text_from_command_line, input_text_from_file
from compare import compare

def main():
    parser = argparse.ArgumentParser(description="Semantic Similarity Detection System")
    parser.add_argument('--file', type=str, help="Path to the input json file")

    args = parser.parse_args()

    if args.file:
        ground_truth, llm_output = input_text_from_file(args.file)
    else:
        ground_truth, llm_output = input_text_from_command_line()
        
    word_similarity, sentence_similarity, similarity, semantic_relationship = compare(ground_truth, llm_output)
    print("Word similarity: ", word_similarity)
    print("Sentence similarity: ", sentence_similarity)
    print("Overall similarity:", similarity)
    print("Semantic relationship:", semantic_relationship)

if __name__ == "__main__":
    main()
