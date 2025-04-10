base = int(input("Digite a base do triângulo :"))
lado1 = int(input("Digite o lado um do triângulo :"))
lado2 = int(input("Digite o lado dois do triângulo :"))

triangulo = base + lado1 >lado2 and base + lado2 > lado1 and lado1 +lado2 > base


if triangulo:
    print("É um triangulo")
if base == lado1 ==lado2:
    print("É um triangulo e quilatero")
elif base == lado1 or base == lado2 or lado1==lado2:
    print("É isoceles")
else:
    print("É escaleno")


