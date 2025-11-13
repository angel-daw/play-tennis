def run(points: str) -> str:
    points_a = 0
    points_b = 0
    a_sets = 0
    b_sets = 0
    for i in points:
        if i == 'A':
            points_a += 1
        else:
            points_b += 1
        if points_a >= 4 and points_a - points_b >= 2:
            points_a = 0
            points_b = 0
            a_sets += 1
        elif points_b >= 4 and points_b - points_a >= 2:
            points_b = 0
            points_a = 0
            b_sets += 1
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
