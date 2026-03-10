import pandas as pd
from rouge_score import rouge_scorer

df = pd.read_csv("generated_answers.csv")

scorer = rouge_scorer.RougeScorer(['rouge1','rougeL'], use_stemmer=True)

scores = []

for i,row in df.iterrows():

    ref = row["reference_answer"]
    ans = row["answer"]

    score = scorer.score(ref, ans)

    scores.append(score["rouge1"].fmeasure)

print("Average ROUGE-1:", sum(scores)/len(scores))