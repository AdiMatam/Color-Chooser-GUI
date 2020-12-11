class TextManager(list):
    def __init__(self, text: str):
        self.set_text(text)

    def set_text(self, text):
        super().__init__(text)

    def __str__(self) -> str:
        return "".join(self)

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            return "".join(super().__getitem__(idx))
        else:
            return super().__getitem__(idx)


if __name__ == "__main__":
    text = TextManager("abddkjkasf")
