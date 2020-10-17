from dictionnaire_ordonne import *

def main():
    d1 = DictionnaireOrdonne()
    print(d1)

    d_init = dict()
    d_init["pommes"] = 25
    d_init["poires"] = 30
    d_init["framboises"] = 100
    d2 = DictionnaireOrdonne(d_init)
    print(d2)


if __name__ == '__main__':
    main()
