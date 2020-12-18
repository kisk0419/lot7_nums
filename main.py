from typing import List
from random import randint

SET_NUM = 10295472
BUY_NUM = 2


def get_numbers(min: int = 1, max: int = 37) -> List[int]:
    """
    ランダムに番号を7つ取得する
    """

    return [randint(min, max) for _ in range(7)]


def is_correct_numbers(numbers: List[int]) -> bool:
    """
    番号に重複がない正しい数列かチェックする
    """
    d = {}
    for number in numbers:
        if number in d:
            return False
        d[number] = True
    return True


def main(set_num: int = SET_NUM, buy_num: int = BUY_NUM):
    for _ in range(buy_num):
        correct_num_cnt = 0
        lastest_nums = None
        while set_num > correct_num_cnt:
            nums = get_numbers()
            if is_correct_numbers(nums):
                correct_num_cnt += 1
                lastest_nums = nums
        print(sorted(lastest_nums))


if __name__ == '__main__':
    main(buy_num=1)

