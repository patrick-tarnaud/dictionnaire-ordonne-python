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
            self.key_list = list(kwargs.keys())
            self.value_list = list(kwargs.values())
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

    def __getitem__(self, key):
        # recherche de la key dans key_list pour obtenir l'index
        try:
            index = self.key_list.index(key)
        except ValueError as e:
            # la ValueError de la liste se transforme en KeyError car l'instance doit se comporter comme un dictionnaire
            raise KeyError(f"{key} is not in the ordered dictionnary")
        return self.value_list[index]
        # renvoie de la valeur dans value_list pour l'index

    def __setitem__(self, key, value):
        # si la clé existe dejà : on remplace la valeur simplement au même index que dans key_list
        # si la clé n'existe pas : on ajoute la clé et la valeur aux 2 listes
        if key in self.key_list:
            self.value_list[self.key_list.index(key)] = value
        else:
            self.key_list.append(key)
            self.value_list.append(value)
