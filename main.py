class Main:
    def __init__(self, file_name):
        self.all_infos = []
        # ogólna liczba słoni
        self.elephants_quantity = 0
        # aktualne oraz oczekiwane ustawienie słoni
        self.actual =    []
        self.expected =  []
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

        self.file_name = file_name
    
    # funkcja mająca na celu pobranie wszystkich danych z pliku
    def DownloadDatas(self):
        # otwarcie pliku z danymi
        with open("test/" + self.file_name, "r") as file:
            datas = file.read().split("\n")
            for data in datas:
                self.all_infos.append(data)
        
        # zapisanie wartości odpowiadającej liczbie słoni
        self.elephants_quantity = int(self.all_infos[0])

        # utworzenie listy wag słoni
        elephants = self.all_infos[1].split(" ")
        elephants = list(elephants)
        # numer słonia
        elephant_number = 1

        # tworzenie słownika słoni, numery wraz z wagami
        for elephant in elephants:
            self.elephants_list[elephant_number] = int(elephant)
            elephant_number += 1

        # aktualne ustawienie słoni
        actuall_order = self.all_infos[2].split(" ")
        self.actual = list(actuall_order)

        # oczekiwane ustawienie słoni
        expected_order = self.all_infos[3].split(" ")
        self.expected = list(expected_order)
    
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

                        # nowy self.this_now
                        new = self.expected[index_to_del]

                        self.this_now = new

                        # usunięcie pozycji w obu zbiorach
                        del self.actual[index_to_del]
                        del self.expected[index_to_del]

    # funkcja główna (Implementacja algorytmu) mająca na celu zwrócenie (najkorzystniejszego) wyniku
    def ReturnTheResult(self):
        for cycle in self.all_containers.values():
            self.weights_in_cycle.clear()
            for num in cycle:
                self.weights_in_cycle.append(self.elephants_list[int(num)])
                           
            suma_c = 0
            c_lenght = len(cycle)
            min_c = min(self.weights_in_cycle)

            mini = min(self.elephants_list.values())

            for weight in self.weights_in_cycle:
                suma_c += weight

            c1 = suma_c + (c_lenght - 2) * min_c

            c2 = suma_c + min_c + (c_lenght + 1) * mini

            self.result += min(c1, c2)
        
        print(self.result)


file_name = input()

main = Main(file_name)

main.DownloadDatas()

main.DoIt()

main.ReturnTheResult()

input()