

class DataStability:
    def __init__(self, list_to_sort):
        self.__name = "Stable sort algorithm"
        self.__description = "Retourner une liste des données triées selon la première valeur du pair.|| Return a list of data sorted by the first value of the peer  "
        self.list_to_sort = list_to_sort
        self.min_value_of_cx: int
        self.max_value_of_cx: int
        self.frequency_of_cx_from_provided_list_size: int
        self.frequency_of_cx_from_provided_list: list[int] 
        self.final_sorted_table = []
    
    # Attribuer les bonnes valeurs aux membres suivants: self.min_value_of_cx et self.max_value_of_cx 
    # Assign the correct values to the following members: self.min_value_of_cx and self.max_value_of_cx
    def find_cx_min_max_value(self):
        return NotImplemented

    # Compter les valeurs se trouvant dans la table des fréquences attribuer les les bonnes valeurs aux membres suivants :
    #  self.frequency_of_cx_from_provided_list_size , self.frequency_of_cx_from_provided_list
    # Count the values in the frequency table and assign the correct values to the following members :
    #  self.frequency_of_cx_from_provided_list_size , self.frequency_of_cx_from_provided_list
    def compt_frequency_of_cx_table(self):
        return NotImplemented

    # Appel les différentes methodes implémentées plus haut et retourne une liste de tuples triés. 
    # Retourne self.final_sorted_table
    # Calls the different methods implemented above and returns a list of sorted tuples.
    # Return self.final_sorted_table
    def perform_sort(self) -> list:
        return NotImplemented
