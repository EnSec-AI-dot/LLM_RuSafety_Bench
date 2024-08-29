import json
from tqdm import tqdm
from openai import AsyncOpenAI
import time
import os
import argparse
import asyncio

"""
    python ethics_answers.py \
        --model2test /home/results/LLMbench/llm_models_hf/Phi_3_mini_4k_instruct \
        --model_name /Phi_3_mini_4k_instruct \
        --common_path_open /home/results/LLMbench/data/TrLLM \
        --common_path_dump /home/results/LLMbench/data/results \
        --port 8000 \
        --api_key 'abc-123'
"""
start_time = time.time()

parser = argparse.ArgumentParser(description="ethics_answers")
parser.add_argument("--model2test", type=str, required=True, help="Path to model2test")
parser.add_argument("--model_name", type=str, required=True, help="model_name")
parser.add_argument(
    "--common_path_open", type=str, required=True, help="Path to common_path_open"
)
parser.add_argument(
    "--common_path_dump", type=str, required=True, help="Path to common_path_dump"
)
parser.add_argument("--api_key", type=str, required=True, help="API key")
parser.add_argument("--port", type=int, required=False, default=8000, help="Port")

args = parser.parse_args()

model2test = args.model2test
model_name = args.model_name
common_path_open = args.common_path_open
common_path_dump = args.common_path_dump
api_key = args.api_key
port = args.port

# Rest of your code here
print(f"model2test: {model2test}")
print(f"model_name: {model_name}")
print(f"common_path_open: {common_path_open}")
print(f"common_path_dump: {common_path_dump}")
print(f"port: {port}")
print(f"api_key: {api_key}")

common_path_dump = common_path_dump + model_name
ethics_dump_path = common_path_dump + "/ethics"
if not os.path.exists(ethics_dump_path):
    os.makedirs(ethics_dump_path)


async def generate_answers(client, model_name, temperature, max_tokens, prompt):
    completion = await client.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return completion.choices[0].message.content


async def file_progon(data, model_name, temperature, max_tokens):

    client = AsyncOpenAI(
        base_url=f"http://localhost:{port}/v1",
        api_key=api_key,
    )
    tasks = []
    for _, prompt in tqdm(enumerate(data)):
        task = asyncio.create_task(
            generate_answers(client, model_name, temperature, max_tokens, prompt)
        )
        tasks.append(task)

    answers = await asyncio.gather(*tasks)
    return answers


# ---------- implicit_ETHICS.json ----------
# ---------- implicit_ETHICS.json ----------
# ---------- implicit_ETHICS.json ----------

print("---------- Start implicit_ETHICS.json ----------")

path2bench = common_path_open + "/ethics/implicit_ETHICS.json"

with open(path2bench, "r") as f:
    data = json.load(f)

prompts = [x["prompt"] for x in data]

outputs = []
outputs = asyncio.run(file_progon(prompts, model2test, temperature=0, max_tokens=100))


print("Finish prompt from implicit_ETHICS feedding into LLM: ", len(outputs))

dump_path = common_path_dump + "/ethics/implicit_ETHICS.json"

with open(dump_path, "w") as f:
    json.dump(outputs, f, indent=2)


end_time = time.time()
execution_time = end_time - start_time
print(f"Loop executed in {execution_time:.2f} seconds")
