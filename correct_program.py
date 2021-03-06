# Krystian Płatek - 05.03.2021

class Main:
    def __init__(self, elephants_quantity, weights, actual, expected):
        # liczba słoni
        self.elephants_quantity = elephants_quantity
        # wagi słoni
        self.elephants_weights = weights
        # aktualne oraz oczekiwane ustawienie słoni
        self.actual = actual
        self.expected =  expected
        # lista słoni z przyporządkowanymi do ich numerów wagami
        self.elephants_list = {}
        # kontener czasowo przechowujący numery słoni w cyklu
        self.container = []
        # słownik z kontenerami
        self.all_containers = {}
        # aktualny numer słonia używany przez funkcję DoIt
        self.this_now = "coś"
        # numer służący do zapisu numerów cyklu do słownika self.all_containers
        self.number = 1
        # wagi wszystkich słoni w danym cyklu
        self.weights_in_cycle = []
        # wynik końcowy
        self.result = 0
    
        # tworzenie słownika słoni, numery wraz z wagami
        for elephant in range(self.elephants_quantity):
            self.elephants_list[elephant + 1] = int(self.elephants_weights[elephant])
    
    # funkcja mająca na celu wyodrębnienie poszczególnych cykli
    def DoIt(self):
        while len(self.actual) != 0:
            if self.actual[0] == self.expected[0]:
                del self.actual[0]
                del self.expected[0]
            
            else:
                self.this_now = self.actual[0]
                while True:
                    if self.this_now in self.container:
                        self.all_containers[self.number] = self.container[:]
                        self.number +=1
                        self.container.clear()
                        break
                    
                    else:
                        self.container.append(self.this_now)

                        index_to_del = self.actual.index(self.this_now)

                        # nowy self.this_now - numer słonia do kolejnego wykonania pętli
                        new = self.expected[index_to_del]

                        self.this_now = new

                        # usunięcie pozycji w obu zbiorach
                        del self.actual[index_to_del]
                        del self.expected[index_to_del]

    # funkcja główna (Implementacja algorytmu) mająca na celu zwrócenie (najkorzystniejszego) wyniku
    def ReturnTheResult(self):
        for cycle in self.all_containers.values():
            # opróżnienie konterera czasowo przechowującego numery słoni w cyklu
            self.weights_in_cycle.clear()
            for num in cycle:
                self.weights_in_cycle.append(self.elephants_list[int(num)])

            # dane algorytmu       
            suma_c = 0
            c_lenght = len(cycle)
            min_c = min(self.weights_in_cycle)
            mini = min(self.elephants_list.values())

            # przypisanie wartości sumy wag słoni w cyklu
            for weight in self.weights_in_cycle:
                suma_c += weight

            # metoda 1
            c1 = suma_c + (c_lenght - 2) * min_c

            # metoda 2
            c2 = suma_c + min_c + (c_lenght + 1) * mini

            # dodanie do wyniku(rezultatu) lepszej z opcji(metod)
            self.result += min(c1, c2)
        
        # zwrócenie wyniku
        return self.result

# liczba słoni
elephants_quantity = int(input())
# wagi słoni
weights = input() 
weights = list(weights.split(" "))
# aktualne ustawienie słoni
actual = input() 
actual = list(actual.split(" "))
# oczekiwane ustawienie słoni
expected = input() 
expected = list(expected.split(" "))

# wywołanie klasy Main
main = Main(elephants_quantity, weights, actual, expected)

# wywołanie funkcji DoIt
main.DoIt()

# wywołanie funkcji ReturnTheResult oraz zwrócenie wyniku
result = main.ReturnTheResult()

# wydrukowanie wyniku
print(result)

# zatrzymanie programu w celu sprawdzenia wyniku
input()