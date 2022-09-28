# Sukurkite filmų klasę "Movie", kuri:
# * Turės klasės lygio 'docstring' tipo komentarą, trumpai aprašantį, kas tai
#   per klasė.
# * Turės 'docstring' tipo komentarą prie kiekvieno metodo, trumpai aprašantį,
#   ką tas metodas atlieka.
# * Gebės sukurti objektus su 3 savybėmis ir 1 metodu.

# Naudojant šią klasę sukurkite bent du skirtingus filmų objektus.

# Savybės:
# * title (str)
# * director (str)
# * budget (int)

# Metodas:
# * was_expensive() - jeigu filmo "budget" yra daugiau nei 100 mln. USD,
#   grąžins True, kitu atveju - False.

class Movie:
    def __init__(self, title, director, budget):
        self.title=str(title)
        self.director=str(director)
        self.budget=int(budget)

    def wasExpensive(self):
        '''si funkcija ivertina filmo verte'''
        if self.budget>100000000:
           return True
        else:
            return False


filmas1=Movie('pats', "petraitis", 150000)
filmas2=Movie('baisiausias', 'petras', 1500000000)
print(filmas1.wasExpensive())
print(filmas2.wasExpensive())
