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

    print('len(d2)', len(d2))

    print('d2 avant tri', d2)
    d2.sort()
    print('d2 après tri', d2)
    d2.reverse()
    print('d2 après reverse', d2)

    # for c in d0:
    #     print(c)
    #
    # for c in d0.keys():
    #     print(c)

    for k in d2:
        print(k)

    print('k in d2.keys()')
    for k in d2.keys():
        print(k)

    print('for v in d2.values()')
    for v in d2.values():
        print(v)

    for k, v in d2.items():
        print(f'({k}, {v})')


if __name__ == '__main__':
    main()
