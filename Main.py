from sympy import *
import PySimpleGUI as sG

#Interface Gráfica
layout = [
    [sG.Text('Expressão polinomial de uma variável:')],
    [sG.Text('Exemplo: (4000*x)-2*(x**2)')],
    [sG.Text('f (x) ='), sG.Input(key='polinomio')],
    [sG.Button('Enviar', size=(50,1), bind_return_key=True)], #Atribuindo a tecla de retorno ao botão enviar
    [sG.Output(size=(50,15), key='saida')]
]
#Janela
janela = sG.Window('Otimizador').layout(layout)

#Laço para manter a janela aberta
while True:
    janela.button, janela.values = janela.Read() #Leitura da insersão do usuário
    #Quando o usuário clicar para fechar a janela
    if janela.button == sG.WINDOW_CLOSED:
        break

    x = Symbol('x')
    polinomio = janela.values['polinomio']
    janela.FindElement('saida').Update('') #Limpeza da caixa de saída

    if 'x' in polinomio: #Checagem de formatação válida
        f = parse_expr(polinomio) #Transformação de string em expressão válida para a biblioteca

        #Calculando as derivadas
        f_prime = f.diff(x)
        f_second = f_prime.diff(x)

        #Resolvendo o ponto crítico
        ptoCritico = solve(f_prime, x)

        #Exibindo os resultados
        print('A derivada primeira é:')
        print(f_prime)
        print('O ponto crítico é:')
        print(ptoCritico)
        print('A derivada segunda é:')
        print(f_second)
        print('A análise da derivada segunda é:')
        print(solve(f_second, x))
    else:
        print('Polinômio inválido!') #Mensagem de erro

#Fim do programa
janela.close()
