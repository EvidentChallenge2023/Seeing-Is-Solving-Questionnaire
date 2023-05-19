# classe pour décripté le message

class Decryptor:
    def __init__(self, data):
        self.data = data

    def decrypt_data(self):
        sorted_message = sorted(self.data.split(), key=lambda i: sorted(i))

        resultat_sans_chiffre = ""
        for word in sorted_message:
            filtered_message = "".join(filter(lambda x: not x.isdigit(), word))
            resultat_sans_chiffre += filtered_message + " "

        return resultat_sans_chiffre.strip()
