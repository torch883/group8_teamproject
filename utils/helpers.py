from datetime import datetime

def get_today():
    today = datetime.now()
    return today.strftime("%Y-%m-%d")

def is_valid_date(date_str):
    valid = True
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        valid = False
    return valid

def is_valid_score(score_str):
    result = True
    try:
        value = int(score_str)
        if value < 0:
            result = False
    except ValueError:
        result = False
    return result