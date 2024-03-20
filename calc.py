import math 
class calculator :
    def s (self, x, y):
        return x + y

    def sub (self, x, y):
        return x - y

    def multi (self, x, y):
        return x * y

    def div (self, x, y):
        if x != 0:
            return x / y
        else:
            return "Erro"
    def p (self, valor , percentual ):
        return (valor * percentual ) / 100
    def raiz (self, x ) :
        return math.sqrt (x)
    def pot (self, b, e ) :
        return b ** e 

def main():
    calc = calculator ()

    operacoes = {
        '1': calc.s,
        '2': calc.sub,
        '3': calc.multi,
        '4': calc.div,
        '5': calc.p,
        '6': calc.raiz,
        '7': calc.pot,

    }

    op = ''
    while op != '5':
        print("Escolha a operação:")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. percentual")
        print("6. raiz quadrada")
        print("7. potencia")


        op = input("Digite o número da operação desejada: ")

        if op in operacoes:
            y = float(input("Digite o primeiro número: "))
            x = float(input("Digite o segundo número: "))
            r = operacoes[op](x, y)
            print("Resultado:", r)

if __name__ == "__main__":
    main()