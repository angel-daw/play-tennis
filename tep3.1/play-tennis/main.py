def run(points: str) -> str:
    points_a = 0
    points_b = 0
    a_sets = 0
    b_sets = 0
    a_games = 0
    b_games = 0
    TIE_BREAK_CONDITION = False
    result = ''
    for point in points:
        if point == 'A':
            points_a += 1
        else:
            points_b += 1
        # COMPROBACIÓN DE EMPATE
        if TIE_BREAK_CONDITION:
            if points_a >= 7 and points_a - points_b >= 2:
                a_games += 1
                result += '7-6 '
                a_sets = 0
                b_sets = 0
                points_a = 0
                points_b = 0
                continue
            if points_b >= 7 and points_b - points_a >= 2:
                b_games += 1
                result += '6-7 '
                a_sets = 0
                b_sets = 0
                points_a = 0
                points_b = 0
                continue
            TIE_BREAK_CONDITION = False
        # COMPROBACIÓN DE SET PARA A
        if points_a >= 4 and points_a - points_b >= 2:
            a_sets += 1
            points_a = 0
            points_b = 0
        # COMPROBACIÓN DE SET PARA B
        elif points_b >= 4 and points_b - points_a >= 2:
            b_sets += 1
            points_b = 0
            points_a = 0
        # COMPROBACIÓN DE JUEGO PARA A
        if a_sets >= 6 and a_sets - b_sets >= 2:
            a_games += 1
            result += f'{a_sets}-{b_sets} '
            a_sets = 0
            b_sets = 0
        # COMPROBACIÓN DE JUEGO PARA B
        elif b_sets >= 6 and b_sets - a_sets >= 2:
            b_games += 1
            result += f'{a_sets}-{b_sets} '
            b_sets = 0
            a_sets = 0
        if b_sets > 7 and a_sets > 7:
            b_sets = 0
            a_sets = 0
            points_a = 0
            points_b = 0
        # Para que cuando sea 6-6, en la siguiente iteranción
        # Hace que entre por lo de los tie breaks.
        if a_sets == 6 and b_sets == 6:
            TIE_BREAK_CONDITION = True
        # COMPROBACIÓN DE PARTIDO
        if a_games == 2 or b_games == 2:
            break
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
