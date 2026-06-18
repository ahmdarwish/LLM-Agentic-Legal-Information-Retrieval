import re

# English → German legal dictionary
legal_dictionary = {
    "contract": "Vertrag Vereinbarung Obligation OR",
    "termination": "Kündigung Beendigung Auflösung OR",
    "marriage": "Ehe Ehegatte ZGB",
    "divorce": "Scheidung Ehe ZGB",
    "criminal": "strafbar Strafe Strafgesetzbuch StGB",
    # ... include all other entries from your dictionary
}

# Law area keywords
law_area_keywords = {
    "OR": ["contract", "agreement", "obligation", "liability", "damage", "termination"],
    "ZGB": ["marriage", "divorce", "child", "inheritance", "estate"],
    "StGB": ["criminal", "crime", "offence", "murder", "theft", "fraud"],
    # ... all other law areas
}

# Law code normalization
law_code_alias = {"CO": "OR", "LCC": "KKG", "CC": "ZGB", "SCC": "ZGB", "CP": "StGB"}

def normalize_law_code(code):
    code = str(code).strip()
    return law_code_alias.get(code, code)

def detect_target_laws(query, known_law_codes, keywords_map=law_area_keywords):
    query_lower = str(query).lower()
    target_laws = []
    for law_code, keywords in keywords_map.items():
        for kw in keywords:
            if kw in query_lower:
                target_laws.append(law_code)
                break
    query_upper = str(query).upper()
    for code in known_law_codes:
        if re.search(rf"\b{re.escape(code.upper())}\b", query_upper):
            target_laws.append(normalize_law_code(code))
    return list(set(target_laws))

def expand_query_dictionary(query, known_law_codes):
    query_lower = str(query).lower()
    extra_terms = []
    for eng, ger in legal_dictionary.items():
        if eng in query_lower:
            extra_terms.append(ger)
    target_laws = detect_target_laws(query, known_law_codes)
    extra_terms.extend(target_laws)
    expanded_query = str(query) + " " + " ".join(extra_terms)
    return expanded_query, target_laws
