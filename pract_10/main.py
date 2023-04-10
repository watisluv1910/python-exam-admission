from functools import reduce


def composite_function(*func):
    def compose(f, g):
        return lambda x: f(g(x))

    return reduce(compose, func, lambda x: x)


def del_column(table, idx):
    for j in table:
        del j[idx]
    return table


def get_row_len(table):
    return len(table[0])


def del_none(table):
    table_clear, idx = [row[:] for row in table], 0

    while idx < get_row_len(table_clear):
        if table_clear[0][idx] is None:
            table_clear = del_column(table_clear, idx)
        else:
            idx += 1

    return table_clear


def del_duplicates(table):
    table_unique = []
    for row in table:
        if list(row) not in table_unique:
            table_unique.append(list(row))

    unique_elements = []
    for idx, elem in enumerate(table[0]):
        if elem not in unique_elements:
            unique_elements.append(elem)
        else:
            table_unique = del_column(table_unique, idx)

    return table_unique


def format_elements(table):
    table_formatted = [[] for _ in range(len(table))]

    for i, row in enumerate(table):
        for j, elem in enumerate(row):
            table_formatted[i].extend(
                format_name(elem) if '&' in elem else format_mail(elem)
            )

    return table_formatted


def format_name(name):
    return [
        str(int(float(name.split('&')[1]) * 100)) + '%',
        ' '.join(reversed(name.split('&')[0].split()))
    ] if '&' in name else [name]


def format_mail(mail):
    return [mail.split('@')[0]] if '@' in mail else [mail]


def print_table(table):
    for row in table:
        print(row)


def main(table):

    format_table = composite_function(
        format_elements,
        del_duplicates,
        del_none
    )

    return format_table(table)


if __name__ == "__main__":
    print(main([
        [None, 'Вадим Фемиди&0.1', 'femidi19@gmail.com', 'femidi19@gmail.com'],
        [None, 'Виктор Булетак&0.9', 'buletak72@gmail.com', 'buletak72@gmail.com'],
        [None, 'Виктор Булетак&0.9', 'buletak72@gmail.com', 'buletak72@gmail.com'],
        [None, 'Одиссей Гинуциди&0.3', 'ginuzidi68@gmail.com', 'ginuzidi68@gmail.com'],
        [None, 'Елисей Шораряк&0.7', 'sorarak52@mail.ru', 'sorarak52@mail.ru']]
    ))
