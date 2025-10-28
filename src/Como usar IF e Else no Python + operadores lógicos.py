# Definindo as variáveis
variavel1 = "Felipe"  # Uma string
variavel2 = 25  # Um número inteiro
variavel3 = ["Felipe", "Lira", "Martins", "João" ]  # Uma lista de strings

# Primeiro loop: verifica se o nome é "Felipe"
for nome in variavel3:
    if nome == "Felipe":
        print("É o Felipe")  # Imprime se o nome for "Felipe"
    else:
        print("Não é o Felipe")  # Imprime se o nome não for "Felipe"

# Segundo loop: imprime números de 0 a variavel2 - 1
for i in range(variavel2):
    print(i)

# Definindo uma lista de strings numéricas
lista = ["98437538", "23094728", "57382910", "48273645", "19283746", "65748392", "29384756", "93847561", "58392047", "84756293"]

# Terceiro loop: verifica se o primeiro caractere do número é "9"
for numeros in lista:
    if  numeros[0] == "9":
        print(f"O número inicial é {numeros[0]}")  # Imprime se o primeiro caractere for "9"
    else:
        print("não é 9")  # Imprime se o primeiro caractere não for "9"

# Verifica se variavel1 é diferente de "Felipe"
if variavel1 != "Felipe":
    print("É diferente")

# Verifica se variavel2 é menor ou igual a 33
if variavel2 <= 33:
    print("É menor que 33" )

# Verifica se "a" está em variavel1
if "a" in variavel1:
    print("tem a")
else:
    print("Não tem a")

# Verifica se "Felipe" está em variavel3
if "Felipe" in variavel3:
    print("Tem Felipe na lista")

# Verifica se "Lorela" está em variavel3
if "Lorela" in variavel3:
    print("Tem Lorela na lista")
elif "Felipe" in variavel3:
    print("Sla vei")
else:
    print('Não tem Lorela na lista')

# Redefine variavel1 como True
variavel1 = True

# Verifica se variavel1 é True
if variavel1 is True:
    print("Receba")