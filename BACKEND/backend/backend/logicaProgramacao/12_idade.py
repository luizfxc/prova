idade = int(input("Digite sua idade:"))

match idade:
    case idade if idade < 12:
        print("Ainda é juvenil")

    case idade if idade >= 12 and idade <18:
      print("Virou juvena")

    case idade if idade >= 18 and idade <60:
      print("Virou amador")

    case idade if idade >= 60 and idade <100:
      print("TU É Historico")

    case idade if idade >= 100:
      print("Morre não desgraça")
