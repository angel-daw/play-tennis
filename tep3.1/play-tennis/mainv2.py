def run(points: str) -> str:
    a_points = 0
    b_points = 0
    a_games = 0
    b_games = 0
    a_sets = 0
    b_sets = 0
    tiebreak_condition = False
    result = ''
    for point in points:
        if a_games == 6 and b_games == 6:
            tiebreak = True
        if point == 'A':
            points_a += 1
        else:
            points_b += 1
        # COMPROBACIÓN DE EMPATE
        # COMPROBACIÓN DE SET PARA A
        if a_points >= 4 and a_points - b_points >= 2:
            a_games += 1
            a_points = 0
            b_points = 0
        # COMPROBACIÓN DE SET PARA B
        elif b_points >= 4 and b_points - a_points >= 2:
            b_games += 1
            a_points = 0
            b_points = 0
        # COMPROBACIÓN DE JUEGO PARA A
        if a_games >= 6 and a_games - b_games >= 2:
            a_sets += 1
            result += f'{a_games}-{b_games} '
            a_games = 0
            b_games = 0
        # COMPROBACIÓN DE JUEGO PARA B
        elif b_games >= 6 and b_games - a_games >= 2:
            b_sets += 1
            result += f'{a_games}-{b_games} '
            b_games = 0
            a_games = 0
        # COMPROBACIÓN DE PARTIDO
        if a_sets == 2 or b_sets == 2:
            break
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
