def turbo_bmh(string, pattern):
    """
     Bad character heuristic, good suffix heuristic, turbo-shift heuristic implemented on Python
     """
    def _suffices_preprocessing(suffix):
        suffix[m - 1] = m
        g = m - 1

        for i in range(m - 2, -1, -1):
            if i > g and suffix[i + m - f - 1] < i - g:
                suffix[i] = suffix[i + m - 1 - f]
            else:
                if i < g:
                    g = i
                f = i
                while g >= 0 and pattern[g] == pattern[g + m - 1 - f]:
                    g -= 1
                suffix[i] = f - g

    def good_suffix_preprocessing():
        # nonlocal pattern, good_suf, m
        suffix = [0 for _ in range(m)]
        _suffices_preprocessing(suffix)
        for i in range(m):
            good_suf[i] = m
        for i in range(m - 1, -1, -1):
            if suffix[i] == i + 1:
                for j in range(m - 1 - i):
                    if good_suf[j] == m:
                        good_suf[j] = m - 1 - i

        for i in range(0, m - 1):
            good_suf[m - 1 - suffix[i]] = m - 1 - i

    n = len(string)
    m = len(pattern)
    good_suf = [0 for i in range(m)]
    bad_character = [m for _ in range(256)]
    for k in range(m - 1):
        bad_character[ord(pattern[k])] = m - k - 1
    bad_character = tuple(bad_character)
    answers = []

    good_suffix_preprocessing()

    j = 0
    while j <= n - m:
        i = m - 1
        while i >= 0 and pattern[i] == string[i + j]:
            i -= 1

        if i < 0:
            answers.append(j)
            j += good_suf[0]
        else:
            j += max(good_suf[i], bad_character[ord(string[i + j])] - m + 1 + i)

    return answers