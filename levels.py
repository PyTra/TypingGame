def calc_error(missed: int, total: int) -> float:
    return missed/total


def calc_wpm(words: [str], time: float) -> float:

    char_count = 0
    for w in words:
        char_count += len(w)
    if time == 0:
        return (char_count / 5)

    return round((char_count / 5) / (time / 60))




def level(e_rate: float, wpm: float, level: int) -> int:
    result = level
    if e_rate > 0.3 and level > 1:
        result -= 1
    elif e_rate <= 0.3 and level < 4 and wpm > 45:
        result += 1
    return result

    