MUST_HAVE = {'и': (1, 5)}
MUST_HAVE_VAL = list(MUST_HAVE.values())[0][1]
SURVIVAL_POINTS = 15
HEIGHT = 3
WIDTH = 3

def get_area_and_value(stuffdict):
    area = [stuffdict[item][0] for item in stuffdict]
    value = [stuffdict[item][1] for item in stuffdict]
    return area, value


def get_memtable(stuffdict, A=8):
    area, value = get_area_and_value(stuffdict)
    n = len(value)

    V = [[0 for a in range(A + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for a in range(A + 1):
            if i == 0 or a == 0:
                V[i][a] = 0
            elif area[i - 1] <= a:
                V[i][a] = max(value[i - 1] + V[i - 1][a - area[i - 1]], V[i - 1][a])
            else:
                V[i][a] = V[i - 1][a]
    print(value)
    return V, area, value


def get_selected_items_list(stuffdict, A=8):
    V, area, value = get_memtable(stuffdict)
    n = len(value)
    res = V[n][A]
    a = A
    items_list = []
    total_value = 0

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == V[i - 1][a]:
            continue
        else:
            items_list.append((area[i - 1], value[i - 1]))
            total_value += value[i - 1]

            res -= value[i - 1]
            a -= area[i - 1]

    selected_stuff = []

    for search in items_list:
        for key, val in stuffdict.items():
            if val == search and (key, val[0]) not in selected_stuff:
                selected_stuff.append((key, val[0]))
                break
    selected_stuff += [(list(MUST_HAVE.keys())[0], list(MUST_HAVE.values())[0][0])]
    total_survival_points = SURVIVAL_POINTS - sum(value) - MUST_HAVE_VAL + 2 * (total_value + MUST_HAVE_VAL)

    return selected_stuff, total_survival_points


def beautiful_output(height, width):
    stuff, total_value = get_selected_items_list(stuffdict)
    matrix = []
    for i in stuff:
        x = i[0]
        val = i[1]
        for _ in range(val):
            matrix.append([x])
    index = 0
    for i in range(height):
        for j in range(width):
            print(matrix[index], end=' ')
            index += 1
        print()
    print(f'Очки выживания:{total_value}')


stuffdict = {
    'в': (3, 25),
    'п': (2, 15),
    'б': (2, 15),
    'а': (2, 20),
    'н': (1, 15),
    'т': (3, 20),
    'о': (1, 25),
    'ф': (1, 15),
    'д': (1, 10),
    'к': (2, 20),
    'р': (2, 20),
}

beautiful_output(HEIGHT, WIDTH)
