import pandas as pd
import ollama
from openai import OpenAI
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Ensure key exists
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set in your environment")
# Initialize OpenAI client securely
client = OpenAI(api_key=openai_api_key)
df = pd.read_csv("dataset/evaluation_dataset.csv")

med_answers = []
gpt_answers = []
med_latency = []
gpt_latency = []

for q in df["question"]:

    # MedGemma
    start = time.time()

    med = ollama.chat(
        model="medgemma-local",
        messages=[{"role":"user","content":q +  "\nAnswer in 1 sentence."}]
    )

    med_latency.append(time.time()-start)
    med_answers.append(med["message"]["content"])


    # GPT
    start = time.time()

    gpt = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":q + "\nAnswer in 1 sentence."}])

    gpt_latency.append(time.time()-start)
    gpt_answers.append(gpt.choices[0].message.content)


df["medgemma_answer"] = med_answers
df["gpt_answer"] = gpt_answers
df["med_latency"] = med_latency
df["gpt_latency"] = gpt_latency

df.to_csv("results/model_outputs.csv", index=False)

print("Model outputs saved")