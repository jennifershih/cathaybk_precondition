def calculate_total_score(name, original_score):
    next_multiple_of_5 = ((original_score // 5) + 1) * 5
    if next_multiple_of_5 - original_score <= 3 and next_multiple_of_5 >= 40:
        return next_multiple_of_5
    else:
        return original_score

students = {
    '德瑞克': 33,
    '尚恩': 73,
    '傑夫': 63,
    '馬基': 39
}

for name, score in students.items():
    total_score = calculate_total_score(name, score)
    print(f'{name}: {total_score}')