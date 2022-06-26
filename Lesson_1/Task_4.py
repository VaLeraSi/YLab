from itertools import combinations


def bananas(s):
    word = "banana"
    if len(s) < len(word):
        return set()
    result = set()
    x = [i for i in range(len(s))]
    index = list(combinations(x, len(x) - len(word)))
    list_s = []
    for row in index:
        redact_s = list(s)
        for j in row:
            redact_s[j] = "-"
        list_s.append(redact_s)
    for row in list_s:
        lst_ = "".join(row)
        lst_clean = lst_.replace("-", "")
        if lst_clean == word:
            result.add(lst_)
    return result
