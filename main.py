# primeiro grau

grau = int(input("Digite o grau da equação: "))

if grau < 1 or grau > 2:
    print("Grau inválido")

if grau == 1:
    print("A equação é do primeiro grau")
    a = int(input("Digite o valor de a: "))
    if a == 0:
        print("Valor de a inválido")
    else:
        b1 = int(input("Digite o valor de b: "))    
        x = (-b1/a) 
        print(f"o valor de X é {x:.2f}")

# segundo grau  

if grau == 2:
    print("A equação é do segundo grau")
    a = int(input("Digite o valor de a: "))
    if a == 0:
        print("Valor de a inválido")
    else:
        b = int(input("Digite o valor de b: "))
        c = int(input("Digite o valor de c: "))
        b2_4ac = (b**2) - (4*a*c) 
        if b2_4ac < 0 : 
            print("A equação não possui raízes reais") 
        elif b2_4ac == 0: 
            print("A equação possui uma raiz real") 
            uma_raiz = (-(b) + b2_4ac**0.5) / (2*a) 
            print(f"{uma_raiz:.2f}") 
        elif b2_4ac > 0: 
            print("A equação possui duas raízes reais")
          
            raiz_pos = (-(b) + b2_4ac**0.5) / (2*a) 
            raiz_neg = (-(b) - b2_4ac**0.5) / (2*a) 
            
            if raiz_pos > raiz_neg: 
                print(f"{raiz_neg:.2f}") 
                print(f"{raiz_pos:.2f}") 
            else: 
                print(f"{raiz_pos:.2f}") 
                print(f"{raiz_neg:.2f}")