#!/bin/bash

# Function to print usage information
usage() {
    echo "Usage: $0 [OPTIONS]"
    echo "Options:"
    echo "  -m, --model-path PATH     Set the model path"
    echo "  -n, --model-name NAME     Set the model name"
    echo "  -o, --open-path PATH      Set the common open path"
    echo "  -d, --dump-path PATH      Set the common dump path"
    echo "  -p, --port PORT           Set the port (default: 8000)"
    echo "  -k, --api-key KEY         Set the API key (default: 'abc-123')"
    echo "  -h, --help                Display this help message"
}

# Default values
MODEL_PATH="/home/results/LLMbench/llm_models_hf/Vikhr_7B_instruct_0.4"
MODEL_NAME="/Vikhr_7B_instruct_0.4"
COMMON_PATH_OPEN="/home/results/LLMbench/data/TrLLM"
COMMON_PATH_DUMP="/home/results/LLMbench/data/results"
PORT=8000
API_KEY='abc-123'

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -m|--model-path)
            MODEL_PATH="$2"
            shift 2
            ;;
        -n|--model-name)
            MODEL_NAME="$2"
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
        -p|--port)
            PORT="$2"
            shift 2
            ;;
        -k|--api-key)
            API_KEY="$2"
            shift 2
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            usage
            exit 1
            ;;
    esac
done

# files to run
FILES=(
    "ethics_answers_aware_cap.py"
    "ethics_answers_aware_em.py"
    "ethics_answers_aware_mis.py"
    "ethics_answers_aware_per.py"
    "ethics_answers_explicit_moralchoice.py"
    "ethics_answers_implicit_ETHICS.py"
    "ethics_answers_implicit_SocialChemistry.py"
    "fairness_answers_stereotype_query_test.py"
    "fairness_answers_stereotype_recognition.py"
    "privacy_answers.py"
    "robustness_answers.py"
    "safety_answers.py"
)

# run all files
for FILE in "${FILES[@]}"
do
    echo "run $FILE..."
    python $FILE \
        --model2test "$MODEL_PATH" \
        --model_name "$MODEL_NAME" \
        --common_path_open "$COMMON_PATH_OPEN" \
        --common_path_dump "$COMMON_PATH_DUMP" \
        --port "$PORT" \
        --api_key "$API_KEY"
    echo "$FILE done!"
done
echo "all done!"