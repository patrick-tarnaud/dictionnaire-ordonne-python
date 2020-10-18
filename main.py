from dictionnaire_ordonne import *


def main():
    d0 = {'framboises': 20, 'fraise': 40, 'cerises': 50, 'figues': 200}

    d1 = DictionnaireOrdonne()
    print(d1)

    d_init = dict()
    d_init["pommes"] = 25
    d_init["poires"] = 30
    d_init["oranges"] = 100
    d2 = DictionnaireOrdonne(d_init)
    print(d2)

    d3 = DictionnaireOrdonne(framboises=20, fraise=40, cerises=50)
    print(d3)

    try:
        print(d2["pommes"])
        print(d2["bananes"])
    except KeyError as e:
        print(e)

    d2["bananes"] = 100
    d2["pommes"] = 50
    print(d2)

    print('d0', d0)
    del d0['framboises']
    print('d0', d0)

    try:
        del d2["bananes"]
        print('d2', d2)
        del d2["ananas"]
    except KeyError as e:
        print(e)

    print("pommes in d2", 'pommes' in d2)
    print("ananas in d2", 'ananas' in d2)


if __name__ == '__main__':
    main()
