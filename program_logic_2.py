def calculate_bouncing_distance(height, num_bounces):
    bounce_height = height

    # 模擬球的自由落下和反彈過程
    for _ in range(num_bounces):
        height += bounce_height
        bounce_height /= 2

    total_distance = height
    bounce_height /= 2

    return total_distance, bounce_height


total_distance, tenth_bounce_height = calculate_bouncing_distance(100, 9)
print("總共 %.9f" % total_distance)
print("第十次 %.9f" % tenth_bounce_height)
