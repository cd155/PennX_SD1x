# Quiz 1.3

def quiz_one():
    scores = [88, 55, 71, 98, 93]
    decent_scores = []
    for num in range(0, len(scores)):
        if scores[num] > 90:
            decent_scores.append(num)
    print(decent_scores[1])

def quiz_two():
    array = [8, 5, 15, 23, 1, 7]
    for num in range(len(scores) -1 , 0, -1):
        array[num-1] = array[num]
    print(array[0])

print("Quiz one:")
# quiz_one()

print("Quiz two:")
# quiz_two()