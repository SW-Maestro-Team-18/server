from typing import List

choice_score = [
    [
        [1,1,0,0,0,1,0,1,1],
        [0,0,1,1,1,0,1,0,0],
    ],
    [
        [0,1,0,0,1,1,0,1,1],
        [1,0,1,1,0,0,1,0,0]
    ],
    [
        [1,0,0,1,0,0,2,0,0],
        [0,0,2,0,1,0,0,0,1],
        [0,1,0,0,0,1,0,1,0]
    ],
    [
        [1,0,0,0,1,1,0,2,0],
        [0,1,2,2,0,0,1,0,1],
    ],
    [
        [2,1,0,0,0,0,0,1,1],
        [0,0,1,1,2,0,1,0,0],
        [0,0,0,0,0,3,0,0,0]
    ],
    [
        [0,0,0,0,0,0,1,0,1],
        [2,0,0,0,2,0,0,0,0]
    ],
    [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ],
    [
        [0,0,2,0,1,0,0,0,3],
        [1,0,0,2,0,0,1,0,0],
        [0,2,0,0,0,0,0,2,0]
    ],
    [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
]


def get_mbti(choices: List[int]) -> int:
    num_of_mbti = 9
    mbti_score = [0 for _ in range(num_of_mbti)]

    for choice, score in zip(choices, choice_score):
        for i in range(num_of_mbti):
            mbti_score[i] += score[choice][i]

    max_score = max(mbti_score)
    max_score_index = mbti_score.index(max_score)

    return max_score_index+1


if __name__ == "__main__":
    print(get_mbti([0,0,0,0,1,1,0,1,0]))