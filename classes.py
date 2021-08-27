class dictionary_entry:
    def __init__(self,hir,kan,com,jlp,mea,cla):
        self.hiragana = hir
        self.kanji = kan
        self.common = com
        self.jlpt = jlp
        self.meanings = mea
        self.classes = cla

    def JSON(self):
        return f"\t{{\n\t\t\"Hiragana\": \"{self.hiragana}\", \
            \n\t\t\"Kanji\": \"{self.kanji}\", \
            \n\t\t\"Common\": \"{self.common}\", \
            \n\t\t\"JLPT\": \"{self.jlpt}\", \
            \n\t\t\"Meanings\": \"{self.meanings}\", \
            \n\t\t\"Class(es)\": \"{self.classes}\"\n\t}}"