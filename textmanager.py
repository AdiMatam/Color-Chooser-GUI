class TextManager(list):
    def __init__(self, text: str):
        self.cursor = None
        self.set_text(text)

    def set_text(self, text):
        super().__init__(text)
        self.cursor = len(text)

    def delchar(self):
        loc = self.cursor - 1
        if loc == -1:
            return
        del self[loc]
        self.move(-1)

    def addchar(self, char: str):
        self.insert(self.cursor, char)
        self.move(1)

    def move(self, side: int):
        if side > 0:
            self.cursor = min(self.cursor + 1, len(self))
        else:
            self.cursor = max(self.cursor - 1, 0)

    def to_str(self, cursor=False) -> str:
        if cursor:
            out = self.copy()
            out.insert(self.cursor, "|")
            return "".join(out)
        else:
            return "".join(self)

    def __str__(self):
        return self.to_str(cursor=True)


if __name__ == "__main__":
    text = TextManager("abddkjkasf")
