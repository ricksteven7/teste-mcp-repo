import math

class Calculadora:
    def __init__(self):
        self.historico = []
    
    def somar(self, a, b):
        """Realiza a operação de adição"""
        resultado = a + b
        self.historico.append(f"{a} + {b} = {resultado}")
        return resultado
    
    def subtrair(self, a, b):
        """Realiza a operação de subtração"""
        resultado = a - b
        self.historico.append(f"{a} - {b} = {resultado}")
        return resultado
    
    def multiplicar(self, a, b):
        """Realiza a operação de multiplicação"""
        resultado = a * b
        self.historico.append(f"{a} x {b} = {resultado}")
        return resultado
    
    def dividir(self, a, b):
        """Realiza a operação de divisão"""
        if b == 0:
            raise ValueError("Erro: Divisão por zero não é permitida!")
        resultado = a / b
        self.historico.append(f"{a} / {b} = {resultado}")
        return resultado
    
    def potencia(self, a, b):
        """Calcula a potência de a elevado a b"""
        resultado = a ** b
        self.historico.append(f"{a}^{b} = {resultado}")
        return resultado
    
    def raiz_quadrada(self, a):
        """Calcula a raiz quadrada de a"""
        if a < 0:
            raise ValueError("Erro: Não é possível calcular raiz quadrada de número negativo!")
        resultado = math.sqrt(a)
        self.historico.append(f"sqrt({a}) = {resultado}")
        return resultado
    
    def modulo(self, a, b):
        """Calcula o resto da divisão de a por b"""
        if b == 0:
            raise ValueError("Erro: Divisão por zero não é permitida!")
        resultado = a % b
        self.historico.append(f"{a} mod {b} = {resultado}")
        return resultado
    
    def mostrar_historico(self):
        """Exibe o histórico de operações"""
        if not self.historico:
            print("Nenhuma operação realizada ainda.")
            return
        
        print("\n=== HISTÓRICO DE OPERAÇÕES ===")
        for i, operacao in enumerate(self.historico, 1):
            print(f"{i}. {operacao}")
        print("=" * 30)
    
    def limpar_historico(self):
        """Limpa o histórico de operações"""
        self.historico.clear()
        print("Histórico limpo!")

def obter_numero(mensagem):
    """Função auxiliar para obter um número válido do usuário"""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Por favor, digite um número válido!")

def menu_principal():
    """Exibe o menu principal da calculadora"""
    print("\n" + "="*50)
    print("           CALCULADORA SIMPLES")
    print("="*50)
    print("1. Adicao (+)")
    print("2. Subtracao (-)")
    print("3. Multiplicacao (x)")
    print("4. Divisao (/)")
    print("5. Potencia (^)")
    print("6. Raiz Quadrada (sqrt)")
    print("7. Modulo (mod)")
    print("8. Ver Historico")
    print("9. Limpar Historico")
    print("0. Sair")
    print("="*50)

def main():
    """Função principal que executa a calculadora"""
    calc = Calculadora()
    
    while True:
        menu_principal()
        
        try:
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "0":
                print("Obrigado por usar a calculadora! Até logo!")
                break
            
            elif opcao == "1":  # Adição
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                resultado = calc.somar(a, b)
                print(f"Resultado: {a} + {b} = {resultado}")
            
            elif opcao == "2":  # Subtração
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                resultado = calc.subtrair(a, b)
                print(f"Resultado: {a} - {b} = {resultado}")
            
            elif opcao == "3":  # Multiplicação
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                resultado = calc.multiplicar(a, b)
                print(f"Resultado: {a} x {b} = {resultado}")
            
            elif opcao == "4":  # Divisão
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                try:
                    resultado = calc.dividir(a, b)
                    print(f"Resultado: {a} / {b} = {resultado}")
                except ValueError as e:
                    print(e)
            
            elif opcao == "5":  # Potência
                a = obter_numero("Digite a base: ")
                b = obter_numero("Digite o expoente: ")
                resultado = calc.potencia(a, b)
                print(f"Resultado: {a}^{b} = {resultado}")
            
            elif opcao == "6":  # Raiz Quadrada
                a = obter_numero("Digite o número: ")
                try:
                    resultado = calc.raiz_quadrada(a)
                    print(f"Resultado: sqrt({a}) = {resultado}")
                except ValueError as e:
                    print(e)
            
            elif opcao == "7":  # Módulo
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                try:
                    resultado = calc.modulo(a, b)
                    print(f"Resultado: {a} mod {b} = {resultado}")
                except ValueError as e:
                    print(e)
            
            elif opcao == "8":  # Ver Histórico
                calc.mostrar_historico()
            
            elif opcao == "9":  # Limpar Histórico
                calc.limpar_historico()
            
            else:
                print("Opção inválida! Por favor, escolha uma opção de 0 a 9.")
        
        except KeyboardInterrupt:
            print("\n\nOperação cancelada pelo usuário.")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()