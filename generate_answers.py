import pandas as pd
import ollama

df = pd.read_csv("evaluation_dataset.csv")

answers = []

for q in df["question"]:

    response = ollama.chat(
        model="medgemma-local",
        messages=[{"role":"user","content":q}]
    )

    answers.append(response["message"]["content"])

df["answer"] = answers

df.to_csv("generated_answers.csv", index=False)

print("Answers generated successfully")