class DictionnaireOrdonne():
    def __init__(self, d: {} = None, **kwargs):
        """
        constructeur
        :param d: dictionnaire
        :param kwargs: clés/valeurs sous forme de paramètres nommés
        """
        # dictionnaire fourni
        if d is not None and isinstance(d, dict):
            self.key_list = list(d.keys())
            self.value_list = list(d.values())
        # clés/valeurs fournies par paramètre nommé
        elif len(kwargs) > 0:
            self.key_list = kwargs.keys()
            self.value_list = kwargs.values()
            pass
        # pas de données d'initialisation
        else:
            self.key_list = []
            self.value_list = []

    def __str__(self):
        to_str = '{'
        for i in range(len(self.key_list)):
            to_str += f"""'{self.key_list[i]}': {self.value_list[i]}"""
            if i != len(self.key_list) - 1:
                to_str += ','
        to_str += '}'
        return to_str

    def __repr__(self):
        return self.__str__()
