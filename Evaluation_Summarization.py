from rouge import Rouge
ROUGE = Rouge()

print(ROUGE.get_scores(summary, abstract))
#print(abstract)
