def count_find_num(primesL, limit):
    base = eval('*'.join(map(str, primesL)))

    if base > limit:
        return []

    results = [base]

    for p in primesL:
        for num in results:
            num *= p
            while num not in results and num <= limit:
                results += [num]
                num *= p

    return [len(results), max(results)]
