from group_anagrams import group_anagrams

def normalize(groups):
    return sorted(sorted(g) for g in groups)

def test_example():
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert normalize(result) == normalize([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])

def test_single_word():
    assert normalize(group_anagrams(["abc"])) == [["abc"]]

def test_empty_string():
    assert normalize(group_anagrams([""])) == [[""]]

def test_no_anagrams():
    assert normalize(group_anagrams(["ab", "cd", "ef"])) == [["ab"], ["cd"], ["ef"]]

def test_duplicates_stay():
    assert normalize(group_anagrams(["ab", "ba", "ab"])) == [["ab", "ab", "ba"]]

def test_empty_list():
    assert group_anagrams([]) == []
