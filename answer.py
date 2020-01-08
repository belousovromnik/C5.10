def answer():
    import random
    import sayings

    rand_answer = []
    rand_answer.append(random.choice(sayings.beginnings))
    rand_answer.append(random.choice(sayings.subjects))
    rand_answer.append(random.choice(sayings.verbs))
    rand_answer.append(random.choice(sayings.actions))
    rand_answer.append(random.choice(sayings.ends))

    return ' '.join(rand_answer)


def answer_api(cnt = 1):
    itog_arr = {}
    if cnt == 1:
        itog_arr = {"message": answer()}
    else:
        strt = []
        for _ in range(cnt):
            strt.append(answer())
        itog_arr = {"messages": strt}

    return itog_arr

# print(answer_api(5))