nota = int(input("Digite sua nota :"))

match nota:

    case 10:
        print("Parabens pela nota maxima")
    
    case 7|8|9:
        print("Passou na prova")
    
    case 0|1|2|3|5|6:
        print("burro do carai")

    case __:
        print("nota que nem existe")
