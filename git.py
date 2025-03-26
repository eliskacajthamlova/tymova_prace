while True:
    print("zadejte dve cisla")
    cislo1 = float(input("zadej prvni cislo:"))
    cislo2 = float(input("zadej druhe cislo:"))
    operace = input("zadej operace + - * /")

    if operace == "+":
        soucet = cislo1 + cislo2
        print(soucet)
    elif operace == "-":
        rozdil = cislo1 - cislo2
        print(rozdil)
    elif operace == "*":
        soucin = cislo1 * cislo2
        print(soucin)
    elif operace == "/":
        podil = cislo1 / cislo2
        print(podil)
        opakovani = input("Pokud nechcete opakovat program napište exit")
    if opakovani == "exit":
        break
 


