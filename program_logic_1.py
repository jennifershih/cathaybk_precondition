"""程式邏輯題目一：期末分數加分。

規則：
- 新分數小於 40 分，不予加分（保持原分數）。
- 原分數與「下一個 5 的倍數」的差在 3 以下（含 3）時，新分數為該 5 的倍數。
"""

STUDENTS = {"德瑞克": 33, "尚恩": 73, "傑夫": 63, "馬基": 39}


def round_grade(score: int) -> int:
    """Return the grade after rounding up to the next multiple of 5 when allowed."""
    next_multiple = (score // 5 + 1) * 5
    if next_multiple < 40:
        return score
    if next_multiple - score <= 3:
        return next_multiple
    return score


def main() -> None:
    total = 0
    for name, score in STUDENTS.items():
        new_score = round_grade(score)
        total += new_score
        print(f"{name}: {score} → {new_score}")
    print(f"總成績: {total}")


if __name__ == "__main__":
    main()
