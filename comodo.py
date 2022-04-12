class Comodo:
    __largura: float  #adicionar __ deixa-o como privado, não sendo possível alterar o que está armazenado no main.py
    __profundidade: float
    __altura: float

    def __init__(self, largura, profundidade):
        self.largura = largura #não é mais necessário passar a conversão para float aqui nem na linha 8
        self.profundidade = profundidade
        self.__altura = 2.9

    @property  #o decorator property indica que esse método é uma propriedade de um atributo
    def largura(self):
        return self.__largura

    @property # utilizamos propriedades (property) para controlar o acesso a atributos privados
    def profundidade(self):
        return self.__profundidade

    @property
    def altura(self):
        return self.__altura

    @largura.setter
    def largura(self, largura):
        try: #estrutura para tratar erros, no caso: verificar se largura é float; caso contrário, o print abaixo é exibido
            self.__largura = float(largura) #fez o tratamento de dados de entrada e converteu string para float (go to linha 7)
        except Exception:
            print('O valor informado para largura é inválido! Insira corretamente')
            exit()

    @profundidade.setter
    def profundidade(self, profundidade):
        try:
           self.__profundidade = float(profundidade) #fez o tratamento de dados de entrada e converteu string para float (go to linha 7)
        except Exception:
            print('O valor informado para profundidade é inválido! Insira corretamente')
            exit()