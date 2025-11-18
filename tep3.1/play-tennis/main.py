def run(points: str) -> str:
    MIN_POINTS_REQUIRED = 4
    MIN_POINTS_REQUIRED_TIEBREAK = 7
    MIN_GAMES_REQUIRED = 6
    SETS_TO_WIN = 2
    MIN_ADVANTAGE_REQUIRED = 2
    A_SCORE_CHECK = 'A'
    GAMES_TIEBREAK_CONDITION = 6

    a_points = 0
    b_points = 0
    a_games = 0
    b_games = 0
    a_sets = 0
    b_sets = 0
    tiebreak = False
    result = ''

    for point in points:
        # COMPROBACIÓN DE EMPATE
        if a_games == GAMES_TIEBREAK_CONDITION and b_games == GAMES_TIEBREAK_CONDITION:
            tiebreak = True
        if point == A_SCORE_CHECK:
            a_points += 1
        else:
            b_points += 1
        # COMPROBACIÓN DE JUEGOS PARA A
        if (
            a_points >= MIN_POINTS_REQUIRED
            and a_points - b_points >= MIN_ADVANTAGE_REQUIRED
            and not tiebreak
        ):
            a_games += 1
            a_points = 0
            b_points = 0
        # COMPROBACIÓN DE JUEGOS PARA B
        elif (
            b_points >= MIN_POINTS_REQUIRED
            and b_points - a_points >= MIN_ADVANTAGE_REQUIRED
            and not tiebreak
        ):
            b_games += 1
            a_points = 0
            b_points = 0
        # RESOLUCIÓN TIEBREAK
        if tiebreak:
            if (
                a_points >= MIN_POINTS_REQUIRED_TIEBREAK
                and a_points - b_points >= MIN_ADVANTAGE_REQUIRED
            ):
                a_games += 1
                result += f'{a_games}-{b_games} '
                a_points = 0
                b_points = 0
                a_games = 0
                b_games = 0
                tiebreak = False
            elif (
                b_points >= MIN_POINTS_REQUIRED_TIEBREAK
                and b_points - a_points >= MIN_ADVANTAGE_REQUIRED
            ):
                b_games += 1
                result += f'{a_games}-{b_games} '
                a_points = 0
                b_points = 0
                a_games = 0
                b_games = 0
                tiebreak = False
        # COMPROBACIÓN DE SETS PARA A
        if a_games >= MIN_GAMES_REQUIRED and a_games - b_games >= MIN_ADVANTAGE_REQUIRED:
            a_sets += 1
            result += f'{a_games}-{b_games} '
            a_games = 0
            b_games = 0
            continue
        # COMPROBACIÓN DE SETS PARA B
        elif b_games >= MIN_GAMES_REQUIRED and b_games - a_games >= MIN_ADVANTAGE_REQUIRED:
            b_sets += 1
            result += f'{a_games}-{b_games} '
            b_games = 0
            a_games = 0
            continue
        # COMPROBACIÓN DE PARTIDO
        if a_sets == SETS_TO_WIN or b_sets == SETS_TO_WIN:
            break
    return result


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
