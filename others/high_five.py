from collections import defaultdict
from typing import List


class HighFive:
    @staticmethod
    def high_five(input: List[list]):
        student_id_wise_scores = defaultdict(list)
        for each in input:
            student_id_wise_scores[each[0]].append(each[1])
        output = []
        for student_id, scores in student_id_wise_scores.items():
            scores = sorted(scores, reverse=True)[:5]
            output.append([student_id, sum(scores) // len(scores)])
        return output


obj = HighFive()
print(obj.high_five(
    [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]))
