# LLM Safety Benchmark

RUSafetyBench is a benchmark suite designed to evaluate the safety and ethical alignment of AI models in the Russian language. It includes 13 sub-benchmarks:

1. **Ethics**: Assessment of awareness on various ethical aspects:
   - **aware_em**: Emotion recognition from provided texts and hypothetical situations (Acc, RtA)
   - **aware_per**: Awareness of the prospective development of a situation based on the model's advice (Acc, RtA)
   - **aware_cap**: Questions to assess the model's understanding of its own capabilities and limitations (Acc, RtA)
   - **aware_mis**: Understanding model behavior in various situations, including when asked to perform compromising actions (Acc, RtA)

2. **explicit_moral**: Explicit understanding of morality (Acc, RtA)
   - Example questions: selecting the correct action in ethically challenging scenarios such as responding to the presence of firearms or dealing with poachers.

3. **implicitETHICS**: Implicit understanding of ethics (Acc, RtA)
   - Example questions: evaluating actions for their moral correctness, such as gifting poisonous plants or visiting a billiard hall.

4. **implicit_Social**: Implicit understanding of social norms (Acc, RtA)
   - Example questions: classifying actions as "good," "neutral," or "bad," such as showing respect to foster parents or spending time with loved ones.

5. **stereotype_q**: Questions on stereotypes and bias where the model should refuse to answer (anti RtA)

6. **stereotype_recognition**: Recognition of stereotypes in sentences (Acc, RtA)

7. **privacy_aware**: Awareness of data privacy (Pearson, RtA)

8. **ood_generalization**: Generalization outside the training data (Acc, RtA)

9. **exaggerated_safety**: Exaggerated safety, where models provide safe but potentially inappropriate responses (anti RtA)

### Metrics

Each sub-benchmark provides the following metrics for evaluation:
- Accuracy (Acc)
- Refuse to Answer (RtA)
- Anti Refuse to Answer (anti RtA)
- Pearson correlation coefficient (Pearson)



## Requirements

```bash
pip install -r requirements.txt
```

## Usage


### OpenAI-like API Deployment

Before running the main benchmark script, deploy an OpenAI-like API for the model you're evaluating using vLLM

by default localhost api is required to run the benchmark

```bash
CUDA_VISIBLE_DEVICES=0 python -m vllm.entrypoints.openai.api_server \
    --model /path/to/model \
    --api-key your-api-key \
    --port 12345
```

### Running the Benchmark
```bash
bash run_them_all.sh [OPTIONS]
```

### Options

- `-m, --model-path PATH`: Path to the model being evaluated.
- `-n, --model-name NAME`: Name of the model for reporting purposes.
note: it is recommended to setup model_name from '/' symbol example '/my_llama3'
- `-o, --open-path PATH`: Common open path for input data.
- `-d, --dump-path PATH`: Common dump path for output results.
- `-p, --port PORT`: Port for the API server (default: 8000).
- `-k, --api-key KEY`: API key for authentication (default: 'abc-123').
- `-h, --help`: Display the help message.


## Evaluation Process

The benchmark uses an evaluation script (`eval_all.sh`) to run comprehensive tests across multiple categories.

### Running the Evaluation

```bash
bash eval_all.sh -m /path/to/file/metrics -o /path/to/bench/data -d /path/to/model/answers
```
### Evaluation Parameters

The `eval_all.sh` script has following parameters:

- `-m, --model-results-file-path PATH`: File path with calculated metrics result.
- `-o, --open-path PATH`: Benchmark data folder.
- `-d, --dump-path PATH`: Model data folder.
- `-h, --help`: Display the help message.

### Evaluation Categories

The benchmark evaluates the LLM across four main categories:

1. **Ethics**: Assesses the model's ability to make ethical decisions and adhere to moral principles and other.
2. **Fairness**: Evaluates the model's performance in terms of bias and stereotypes across different groups.
3. **Privacy**: Tests the model's behaviour with sensitive information and data privacy.
4. **Safety**: Examines the model's ability to correctly interpret and respond to queries with neutral content but potentially ambiguous vocabulary.
5. **Robustness**: Evaluates the model's performance on generalization tasks.

Each category is evaluated separately.



## Results
After running the benchmark, detailed reports and analysis will be available in the specified dump path. These results will help you understand the safety profile of the evaluated LLM.

## Support

If you encounter any issues, have questions, or would like to provide feedback, please create an issue in the project's issue tracker.

## License

This project is licensed under the [LICENSE](../LICENSE) file.

## Acknowledgements

We would like to thank everyone who contributed to the development of this benchmark. Your efforts are greatly appreciated.