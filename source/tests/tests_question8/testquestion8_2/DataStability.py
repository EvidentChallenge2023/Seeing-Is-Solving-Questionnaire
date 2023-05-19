

class DataStability:
    def __init__(self, list_to_sort):
        self.__name = "Satble sort algorithm"
        self.__description = "Retourner une liste des données triées selon la première valeur du pair. "
        self.list_to_sort = list_to_sort
        self.min_value_of_cx: int
        self.max_value_of_cx: int
        self.frequency_of_cx_from_provided_list_size: int
        self.frequency_of_cx_from_provided_list: list[int] 
        self.final_sorted_table = []
    
    def find_min_max_value(self):
        self.min_value_of_cx = self.list_to_sort[0][0]
        self.max_value_of_cx = self.list_to_sort[0][0]

        for p in self.list_to_sort:
            if p[0] < self.min_value_of_cx:
                self.min_value_of_cx = p[0]
            if p[0] > self.max_value_of_cx:
                self.max_value_of_cx = p[0]
    
    def comput_frequency_stable(self):
        self.frequency_of_cx_from_provided_list_size = (self.max_value_of_cx - self.min_value_of_cx) + 1
        self.frequency_of_cx_from_provided_list = [0] * self.frequency_of_cx_from_provided_list_size

        for i in self.list_to_sort:
            valueOfA = i[0]
            self.frequency_of_cx_from_provided_list[valueOfA - self.min_value_of_cx] += 1
        for j in range(1, self.frequency_of_cx_from_provided_list_size):
            self.frequency_of_cx_from_provided_list[j] = self.frequency_of_cx_from_provided_list[j - 1] + self.frequency_of_cx_from_provided_list[j]
    
    def perform_sort(self):
        assert len(self.list_to_sort) > 0
        self.find_min_max_value()
        self.comput_frequency_stable()
        self.final_sorted_table = [(0, None)] * len(self.list_to_sort)

        for i in reversed(self.list_to_sort):
            valueOfABoucle4 = i[0]
            valeur_second = i[1]
            j = valueOfABoucle4 - self.min_value_of_cx
            valeurDeJBecomeIndice = self.frequency_of_cx_from_provided_list[j] - 1
            self.final_sorted_table[valeurDeJBecomeIndice] = (valueOfABoucle4, valeur_second)
            self.frequency_of_cx_from_provided_list[j] -= 1

        self.list_to_sort[:] = self.final_sorted_table
