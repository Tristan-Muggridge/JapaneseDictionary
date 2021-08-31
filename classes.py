class DictionaryEntry:
    def __init__(self, hir, kan, com, jlp, mea, cla):
        self.hiragana = hir
        self.kanji = kan
        self.common = com
        self.jlpt = jlp
        self.meanings = mea
        self.classes = cla
        self.filtered_kanji = self.filtered_kanji(kan)

    def __str__(self):
        return f"{self.hiragana}|{self.kanji}|{self.common}|{self.jlpt}|{self.meanings}|{self.classes}\n"

    def JSON(self):
        return f'\t{{\n\t\t"Hiragana": "{self.hiragana}", \
            \n\t\t"Kanji": "{self.kanji}", \
            \n\t\t"Common": "{self.common}", \
            \n\t\t"JLPT": "{self.jlpt}", \
            \n\t\t"Meanings": "{self.meanings}", \
            \n\t\t"Class(es)": "{self.classes}"\n\t}}'

    def filtered_kanji(self, kan):
        list_ = list()
        hiragana = {
            "あ",
            "い",
            "う",
            "え",
            "お",
            "き",
            "か",
            "く",
            "け",
            "こ",
            "が",
            "ぎ",
            "ぐ",
            "げ",
            "ご",
            "さ",
            "し",
            "す",
            "せ",
            "そ",
            "ざ",
            "じ",
            "ず",
            "ぜ",
            "ぞ",
            "た",
            "ち",
            "つ",
            "て",
            "と",
            "だ",
            "ぢ",
            "づ",
            "で",
            "ど",
            "な",
            "に",
            "ぬ",
            "ね",
            "の",
            "は",
            "ひ",
            "ふ",
            "へ",
            "ほ",
            "ば",
            "び",
            "ぶ",
            "べ",
            "ぼ",
            "ぱ",
            "ぴ",
            "ぷ",
            "ぺ",
            "ぽ",
            "ま",
            "み",
            "む",
            "め",
            "も",
            "や",
            "ゆ",
            "よ",
            "ら",
            "り",
            "る",
            "れ",
            "ろ",
            "わ",
            "を",
            "ん",
            "っ",
            "ゃ",
            "ゅ",
            "ょ",
        }

        for character in kan:
            if character not in hiragana:
                list_.append(character)
        return "".join(list_)
