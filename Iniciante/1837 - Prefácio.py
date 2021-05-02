def divisao_euclidiana(a, b, direcao=1):
    ############################### 'a' e 'b' positivos  ###############################
    if direcao == 1:
        quociente_int = 1
        resto = 0
        while b * quociente_int < a:
            quociente_int += 1
            if b * quociente_int > a:
                quociente_int -= 1
                break
        while b * quociente_int + resto != a:
            resto += 1
        print(quociente_int, resto)
        ############################### 'a' e 'b' negativos ###############################
    elif direcao == 2:
        quociente_int = 1
        resto = -1
        while b * quociente_int > a:
            quociente_int += 1
            if b * quociente_int < a:
                quociente_int -= 1
                break
        while b * quociente_int + resto != a:
            resto -= 1
        print(quociente_int, resto)
        ############################### 'a' negativo e 'b' positivo ###############################
    elif direcao == 3:
        quociente_int = -1
        resto = 0
        while b * quociente_int > a:
            quociente_int -= 1
            if b * quociente_int <= a:
                quociente_int += 1
                break
        while b * quociente_int + resto != a:
            resto += -1
        print(quociente_int, abs(resto))
    ############################### 'a' positivo e 'b' negativo ###############################
    elif direcao == 4:
        quociente_int = -1
        resto = 0
        while b * quociente_int < a:
            quociente_int -= 1
            if b * quociente_int > a:
                quociente_int += 1
                break
        while b * quociente_int + resto != a:
            resto += 1
        print(quociente_int, resto)


a, b = map(int, input().split())

divisao_euclidiana(a, b, direcao=4)