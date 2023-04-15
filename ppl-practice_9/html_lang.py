deep = 0


class Body:
    def __init__(self, text_list: list):
        self.text_list = text_list

    def __enter__(self):
        global deep

        self.text_list.append(" " * deep + "<body>\n")
        deep += 1

    def __exit__(self, *args):
        global deep

        deep -= 1
        self.text_list.append(" " * deep + "</body>\n")


class Div:
    def __init__(self, text_list: list):
        self.text_list = text_list

    def __enter__(self):
        global deep

        self.text_list.append(" " * deep + "<div>\n")
        deep += 1

    def __exit__(self, *args):
        global deep

        deep -= 1
        self.text_list.append(" " * deep + "</div>\n")


class HTML:
    def __init__(self):
        self.text_list = []

    def p(self, text):
        self.text_list.append(" " * deep + f"<p>{text}</p>\n")

    def body(self):
        return Body(self.text_list)

    def div(self):
        return Div(self.text_list)

    def get_code(self):
        return "".join(self.text_list)


html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
    html.p('Вторая строка.')
    with html.div():
        html.p('Третья строка.')

print(html.get_code())
