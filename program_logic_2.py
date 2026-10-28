"""程式邏輯題目二：球從 100 公分落下，每次反彈到前一次高度的一半。

求第 10 次落地時總共經過多少公分，以及第 10 次反彈的高度。
"""


def bounce(height: float, landings: int) -> tuple[float, float]:
    """Return (total distance at the given landing, height of the bounce after it)."""
    distance = 0.0
    current = height
    for landing in range(1, landings + 1):
        distance += current  # falling down
        current /= 2  # the ball bounces back to half the height
        if landing < landings:
            distance += current  # going back up before the next landing
    return distance, current


def main() -> None:
    distance, rebound = bounce(100, 10)
    print(f"第 10 次落地時共經過 {distance:g} 公分")
    print(f"第 10 次反彈高度 {rebound:g} 公分")


if __name__ == "__main__":
    main()
