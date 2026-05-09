import re

def check_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password Should Be At Least 8 Characters Long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add Uppercase Letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add Lowercase Letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Include Numbers.")

    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        feedback.append("Include Special Characters (@, $, !, %, *, ?, &).")

    return score, feedback
