def calculate_final_score(scores):
    max_score = len(scores) * 3  # maximum score if all variables scored 3
    total_score = sum(scores)
    percentage_score = (total_score / max_score) * 100
    return percentage_score


