def count_vowels(text: str) -> int:
    vowel_count = 0
    vowel = ["a", "e", "i", "o", "u"]
    text = text.lower()
    for char in text:
        if char in vowel:
            vowel_count += 1
    return vowel_count
