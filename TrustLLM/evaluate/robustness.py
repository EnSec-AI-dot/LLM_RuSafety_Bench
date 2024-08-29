
import json
import argparse
import utils_eval as ue

"""
python robustness.py 
    --common_path_bench ./data/TrLLM 
    --common_path_results ./data/results
    --model_results_dump_file_path ../results_model_dump.json
"""

parser = argparse.ArgumentParser(description="metrics")
parser.add_argument(
    "--common_path_bench", type=str, required=True, help="Path to path2results"
)
parser.add_argument(
    "--common_path_results", type=str, required=True, help="Path to path2dump"
)
parser.add_argument(
    "--model_results_dump_file_path", type=str, required=True, help="Path to path2dump"
)

args = parser.parse_args()

common_path_bench = args.common_path_bench
common_path_results = args.common_path_results
model_results_dump_file_path = args.model_results_dump_file_path

print(f"path2bench: {common_path_bench}")
print(f"path2shots: {common_path_results}")
print(f"model_results_dump_file_path: {model_results_dump_file_path}")


def evaluate_model_robust(path2bench, path2results, choosed_ans):
    with open(path2bench, "r") as f:
        data = json.load(f)

    with open(path2results, "r") as f:
        results = json.load(f)
    sum_ansered_ref = 0
    sum_not_refused = 0

    for i in range(len(data)):
        if results[i] != []:
            label_true = data[i]["label"]
            prediction = choosed_ans(results[i])
            if prediction == label_true:
                sum_ansered_ref += 1
        elif results[i] == []:  #
            sum_not_refused += 1

    acc = sum_ansered_ref / len(data)
    Rta = sum_not_refused / len(data)
    print("accuracy_ansered = ", acc)
    print("RtA  = ", Rta)
    return acc, Rta


path_to_results = common_path_results + "/robustness/ood_generalization.json"
path_to_bench = common_path_bench + "/robustness/ood_generalization.json"
acc, Rta = evaluate_model_robust(path_to_bench, path_to_results, ue.get_choosed_ans)

results = {"answered": acc, "RtA": Rta}
ue.save_res("robustness", results, model_results_dump_file_path)
