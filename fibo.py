"""
    ---------------------------------------------------------------------------
                                    Fibonacci
    ---------------------------------------------------------------------------
        Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o 
        próximo valor sempre será a soma dos 2 valores anteriores 
        (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
        escreva um programa na linguagem que desejar onde, 
        informado um número, ele calcule a sequência de Fibonacci e 
        retorne uma mensagem avisando se o número informado 
        pertence ou não a sequência.
    ---------------------------------------------------------------------------
                                Made with: python3
                                Made by: João Goulart
    ---------------------------------------------------------------------------
"""

# Fibonacci usando programação dinãmica
def fibo(n):
    
    f = []
    f.append(1)
    f.append(1)
    
    # Variavel de controle do calculo da sequencia
    i = 2
    
    while True:
        f.append(f[i - 1] + f[i - 2])
        # Se calcular o valor de n, achou o numero e retorna verdadeiro
        if f[i] == n:
            return True
        if f[i] > n:
            return False
        i = i + 1

def main():
    if fibo(10):
        print("O número foi encontrando na sequencia de fibonacci!")
    else:
        print("O número não foi encontrando na sequencia de fibonacci!")

main()