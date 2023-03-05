def car_speed (speed):
    if speed < 0:
        return 'Invalid'
    elif speed >= 0 and speed < 40:
        return 'Low'
    elif speed >= 40 and speed < 120:
        return 'Normal'
    elif speed >= 120 and speed < 200:
        return 'High'
    elif speed >= 200 and speed < 220:
        return 'V.High'
    else :
        return 'Invalid'




def student_score(score):
    if score < 0:
        return 'Invalid'
    elif score >= 0 and score < 50:
        return 'Failed'
    elif score >= 50 and score < 65:
        return 'Passed'
    elif score >= 65 and score < 75:
        return 'Good'
    elif score >= 75 and score < 85:
        return 'V.Good'
    elif score >= 85 and score < 100:
        return 'Excellent'
    else:
        return 'Invalid'