def reverse_string(text: str) -> str:
    result = ""
    if text == "":
        return ""
    else:
        for i in text:
            result = i + result
    return result

def reverse_string(text: str) -> str:
    if text == "":
        return ""
    else:
        return text[::-1]
