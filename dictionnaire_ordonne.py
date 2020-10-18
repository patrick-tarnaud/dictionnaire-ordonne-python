class DictionnaireOrdonne():
    def __init__(self, d: {} = None, **kwargs):
        """
        constructeur
        :param d: dictionnaire
        :param kwargs: clés/valeurs sous forme de paramètres nommés
        """
        # dictionnaire fourni
        if d is not None and isinstance(d, dict):
            self._key_list = list(d.keys())
            self._value_list = list(d.values())
        # clés/valeurs fournies par paramètre nommé
        elif len(kwargs) > 0:
            self._key_list = list(kwargs.keys())
            self._value_list = list(kwargs.values())
        # pas de données d'initialisation
        else:
            self._key_list = []
            self._value_list = []

    def __str__(self):
        to_str = '{'
        for i in range(len(self._key_list)):
            to_str += f"""'{self._key_list[i]}': {self._value_list[i]}"""
            if i != len(self._key_list) - 1:
                to_str += ','
        to_str += '}'
        return to_str

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, key):
        # recherche de la key dans key_list pour obtenir l'index
        try:
            index = self._key_list.index(key)
        except ValueError as e:
            # la ValueError de la liste se transforme en KeyError car l'instance doit se comporter comme un dictionnaire
            raise KeyError(f"{key} is not in the ordered dictionnary")
        return self._value_list[index]
        # renvoie de la valeur dans value_list pour l'index

    def __setitem__(self, key, value):
        # si la clé existe dejà : on remplace la valeur simplement au même index que dans key_list
        # si la clé n'existe pas : on ajoute la clé et la valeur aux 2 listes
        if key in self._key_list:
            self._value_list[self._key_list.index(key)] = value
        else:
            self._key_list.append(key)
            self._value_list.append(value)

    def __delitem__(self, key):
        # en cas de suppression, il faut supprimer dans les 2 listes : key_list et value_list
        if key in self._key_list:
            ind = self._key_list.index(key)
            del self._value_list[ind]
            del self._key_list[ind]
        else:
            raise KeyError(f"KeyError : '{key}'")

    def __contains__(self, key):
        return key in self._key_list

    def __len__(self):
        return len(self._key_list)

    def sort(self):
        # on trie les clés dans un premier temps dans une nouvelle liste de clés
        # dans l'ancienne liste de clé on récupère la valeur
        # on crée une nouvelle liste de valeur dans l'ordre de la nouvelle liste de clé
        new_key_list = sorted(self._key_list)
        new_value_list = []
        for key in new_key_list:
            value = self[key]
            new_value_list.append(value)
        self._key_list = new_key_list
        self._value_list = new_value_list

    def reverse(self):
        self._key_list.reverse()
        self._value_list.reverse()

    def __iter__(self):
        return iter(self._key_list)

    def keys(self):
        return self._key_list

    def values(self):
        return self._value_list

    def items(self):
        for key in self._key_list:
            val = self[key]
            yield key, val
