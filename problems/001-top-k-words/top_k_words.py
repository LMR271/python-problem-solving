import re
def top_k_words(text: str, k: int) -> list[tuple[str, int]]:
    if k <= 0:
        return []
    result = {}
    words = re.findall(r"[a-z']+", text.lower())
    for word in words:
        result[word] = result.get(word, 0 ) + 1
    pairs = sorted(result.items()) # sort alphabetically
    pairs = sorted(pairs, key=lambda pair: pair[1], reverse=True)[:k] # sort based on count
    return pairs
    '''return sorted(result.items(), key=lambda x: (-x[1], x[0]))[:k]'''
