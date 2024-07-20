import json

def input_text_from_command_line():
    ground_truth = input("Enter the ground truth passage: ")
    llm_output = input("Enter the LLM output passage: ")
    return ground_truth, llm_output

def input_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        ground_truth = data["ground_truth"].strip()
        llm_output = data["llm_output"].strip()
    print("Input ground truth:", ground_truth)
    print("Input llm output:", llm_output)
    return ground_truth, llm_output
