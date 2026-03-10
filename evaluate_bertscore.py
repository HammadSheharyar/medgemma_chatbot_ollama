import pandas as pd
from bert_score import score

df = pd.read_csv("generated_answers.csv")

P, R, F1 = score(
    df["answer"].tolist(),
    df["reference_answer"].tolist(),
    lang="en"
)

print("BERTScore F1:", F1.mean().item())











