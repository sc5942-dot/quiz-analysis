def letter_grade(score):
    return "A" if score > 90 else "B"

def median_score(scores):
    s = sorted(scores)
    return s[len(s) // 2]