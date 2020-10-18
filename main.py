from dictionnaire_ordonne import *


def main():
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


if __name__ == '__main__':
    main()
