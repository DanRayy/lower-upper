class UpperLower:
    def __init__(self):
        self.str_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.str_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K" ,"L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.str_texto = input("Digite algo: ")

    def lower(self):
        for l in range(len(self.str_texto)):
            if self.str_texto[l] in self.str_upper:
                ind = self.str_upper.index(self.str_texto[l])
                self.str_texto = self.str_texto[:l] + self.str_lower[ind] + self.str_texto[l+1:]
        print(self.str_texto)

    def upper(self):
        for u in range(len(self.str_texto)):
            if self.str_texto[u] in self.str_lower:
                ind = self.str_lower.index(self.str_texto[u])
                self.str_texto = self.str_texto[:u] + self.str_upper[ind] + self.str_texto[u+1:]
        print(self.str_texto)

ul = UpperLower()
ul.upper()
ul.lower()