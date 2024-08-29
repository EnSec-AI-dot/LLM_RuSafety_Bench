#!/bin/bash

# Function to display usage
usage() {
    echo "Usage: $0 [OPTIONS]"
    echo "Options:"
    echo "  -m, --model-results-file-path PATH     Set the results file path"
    echo "  -o, --open-path PATH      Set the common open path"
    echo "  -d, --dump-path PATH      Set the common dump path"
    echo "  -h, --help                Display this help message"
    exit 1
}

# Default values
COMMON_PATH_OPEN="LLMbench/data/TrLLM"
COMMON_PATH_DUMP="LLMbench/data/results"
MODEL_RESULTS_DUMP_FILE_PATH = "LLMbench/model_results_dump_file.json"

# Parse command line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -m|--model-results-file-path)
            MODEL_RESULTS_DUMP_FILE_PATH="$2"
            shift 2
            ;;
        -o|--open-path)
            COMMON_PATH_OPEN="$2"
            shift 2
            ;;
        -d|--dump-path)
            COMMON_PATH_DUMP="$2"
            shift 2
            ;;
        -h|--help)
            usage
            ;;
        *)
            echo "Unknown option: $1"
            usage
            ;;
    esac
done

files=("ethics.py" "fairness.py" "privacy.py" "robustness.py" "safety.py")


for file in "${files[@]}"; do
    echo "Running $file with arguments:"
    echo "  --model_results_dump_file_path $MODEL_RESULTS_DUMP_FILE_PATH"
    echo "  --common_path_bench $COMMON_PATH_OPEN"
    echo "  --common_path_results $COMMON_PATH_DUMP"
    
    python $file \
        --common_path_bench "$COMMON_PATH_OPEN" \
        --common_path_results "$COMMON_PATH_DUMP" \
        --model_results_dump_file_path "$MODEL_RESULTS_DUMP_FILE_PATH"
    
    if [ $? -ne 0 ]; then
        echo "Error: $file failed to run."
        exit 1
    fi
done

echo "All scripts ran successfully."