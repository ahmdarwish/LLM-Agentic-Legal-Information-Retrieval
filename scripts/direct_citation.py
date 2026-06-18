import re
from collections import defaultdict

def extract_direct_citations_from_query(query, law_citations, article_index, known_law_codes):
    query = str(query)
    citations = []

    law_code_pattern = "|".join(re.escape(code) for code in known_law_codes)
    article_pattern = re.compile(
        rf"Art\.?\s*(?P<article>\d+[a-zA-Z]?)"
        rf"(?:\s*Abs\.?\s*(?P<abs>\d+))?"
        rf"\s+(?P<code>{law_code_pattern})\b",
        flags=re.IGNORECASE
    )

    for m in article_pattern.finditer(query):
        article = m.group("article")
        abs_no = m.group("abs")
        code = m.group("code")  # normalized outside in main notebook
        citations.append(f"Art. {article} {code}")
        if abs_no is not None:
            citations.append(f"Art. {article} Abs. {abs_no} {code}")

    # Remove duplicates
    return list(dict.fromkeys(citations))
