from calculadora import Calculadora
from comodo import Comodo

calc = Calculadora()

comodo = Comodo(
    float(input('Qual a largura do comodo\n')),
    float(input('Qual a profundidade do comodo\n'))
)

print(f"A área das paredes é: {calc.calcular_area_paredes(comodo.largura, comodo.profundidade, comodo.altura)}")

print(f"A área do teto é: {calc.calcular_area_teto(comodo.largura, comodo.profundidade)}")

print(f"Serão necessários {calc.calcular_volume_tintas()} litros de tinta para pintar esse cômodo.")