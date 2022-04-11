from calculadora import Calculadora

calc = Calculadora()

altura = float(input("Digite a altura da parede\n"))
profundidade = float(input("Digite a profundidade da parede\n"))
largura = float(input("Digite a largura da parede\n"))

print(f"A área das paredes é: {calc.calcular_area_paredes(largura, profundidade, altura)}")

print(f"A área do teto é: {calc.calcular_area_teto(largura, profundidade)}")

print(f"Serão necessários {calc.calcular_volume_tintas()} litros de tinta para pintar esse cômodo.")