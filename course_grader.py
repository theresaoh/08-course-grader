def course_grader(param):
    score_sum = 0
    for score in param:
        if score < 50:
            return "fail"
        score_sum += score
    avg = score_sum/len(param)
    if avg >= 70:
        return "pass"
    else:
        return "fail"
