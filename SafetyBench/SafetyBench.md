# LLM RuSafety Benchmark
RUSafetyBench is a benchmark designed to evaluate the safety of large language models (LLMs) in the Russian language across seven safety categories.

## Subcategories

### 1. Offensiveness
Evaluates the model's ability to identify and counteract threats, insults, profanity, sarcasm, and impoliteness.

### 2. Unfairness and Bias
Assesses the model's ability to identify and avoid expressions and actions that contain social biases related to race, gender, religion, and other attributes.

### 3. Physical Health
Tests the model's knowledge on maintaining and promoting physical health, including providing accurate medical information.

### 4. Mental Health
Measures the model's ability to recognize mental health issues, support emotional well-being, and suggest resources and practices for mental health maintenance.

### 5. Illegal Activities
Evaluates the model's ability to distinguish between legal and illegal actions, and to discourage discussions and encouragement of illegal activities.

### 6. Ethics and Morality
Assesses the model's adherence to high standards of ethics and morality, and its ability to counteract unethical behaviors and expressions.

### 7. Privacy and Property
Tests the model's understanding of privacy and property rights, and its ability to prevent breaches of privacy and loss of property.

## Testing Methods

The benchmark includes both 0-shot and 5-shot evaluations:

- 0-shot: The model receives no examples before performing the task.
- 5-shot: The model receives five examples before performing the task.


## Requirements

- Python 3.8+
- vllm API or OpenAI-format API

## Usage

1. Launch vllm API:
by default localhost api is required to run the benchmark

CUDAVISIBLEDEVICES=0 python -m vllm.entrypoints.openai.api_server \
    --model /path/to/model \
    --api-key your-api-key \
    --port 12345

2. Run benchmark:

note: it is recommended to setup model_name from '/' symbol example '/my_llama3'

python run_SafetyBench.py \
    --model2test /path/to/model \
    --model_name ModelName \
    --shot_type 'five' \
    --path2bench path/to/resultSB.json \
    --path2shots path/to/devru.json \
    --common_path_dump path/to/results \
    --api_key 'your-api-key' \
    --port 12345

3. Calculate metrics:
note: it is recommended to setup model_name from '/' symbol example '/my_llama3'
note: you have to run the eval script for each shot_type

python metricsSB.py \
    --model_name ModelName \
    --shots_type five \
    --path2results path/to/results/resultfive.json \
    --path2dump path/to/results

## Support
Create an issue for questions or problems.