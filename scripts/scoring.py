import math
from collections import Counter

def parse_citations(x):
    if x is None or str(x).strip() == "":
        return set()
    return set(c.strip() for c in str(x).split(";") if c.strip())

def f1_score_citations(gold, pred):
    gold = set(gold)
    pred = set(pred)
    if len(gold) == 0 and len(pred) == 0:
        return 1.0
    if len(gold) == 0 or len(pred) == 0:
        return 0.0
    tp = len(gold & pred)
    precision = tp / len(pred) if len(pred) > 0 else 0
    recall = tp / len(gold) if len(gold) > 0 else 0
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)

def citation_train_prior(citation, train_gold_counter, max_count):
    count = train_gold_counter.get(citation, 0)
    if count == 0:
        return 0.0
    return math.log1p(count) / math.log1p(max_count)
