def run(points: str) -> str:
    points_a = 0
    points_b = 0
    a_sets = 0
    b_sets = 0
    a_games = 0
    b_games = 0
    TIE_BREAK_CONDITION = 6
    result = ''
    for point in points:
        if point == 'A':
            points_a += 1
        else:
            points_b += 1
        # COMPROBACIÓN DE SET PARA A
        if points_a >= 4 and points_a - points_b >= 2:
            points_a = 0
            points_b = 0
            a_sets += 1
        # COMPROBACIÓN DE SET PARA B
        elif points_b >= 4 and points_b - points_a >= 2:
            points_b = 0
            points_a = 0
            b_sets += 1
        # COMPROBACIÓN DE JUEGO PARA A
        if a_sets >= 6 and a_sets - b_sets >= 2:
            a_games += 1
            result += f'{a_sets}-{b_sets} '
            a_sets = 0
            b_sets = 0
            points_a = 0
            points_b = 0
        # COMPROBACIÓN DE JUEGO PARA B
        elif b_sets >= 6 and a_sets - b_sets >= 2:
            b_games += 1
            result += f'{a_sets}-{b_sets} '
            b_sets = 0
            a_sets = 0
            points_a = 0
            points_b = 0
        # COMPROBACIÓN DE EMPATE
        elif a_sets == TIE_BREAK_CONDITION and b_sets == a_sets:
            if point == 'A':
                points_a += 1
            else:
                points_b += 1
            if points_a >= 7 and points_a - points_b >= 2:
                a_sets += 1
                points_a = 0
                points_b = 0
            elif points_b >= 7 and points_b - points_a >= 2:
                b_sets += 1
                points_a = 0
                points_b = 0
        # COMPROBACIÓN DE PARTIDO
        if a_games == 2 or b_games == 2:
            break
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
