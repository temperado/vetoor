from manim import * # coisa de aminacao matematica
from math import *  # importa todas as funcoes matematicas
import ast          # transforma string de codigo em codigo
from time import sleep # importa a funcao sleep

def calculate(expression):
    return eval(expression)

class grau90(Scene):
    def construct(self):

        # Cabeçalho
        print('='*43 + "\n"*2 +  """    ▄   ▄███▄     ▄▄▄▄▀ ████▄ ████▄ █▄▄▄▄ 
     █  █▀   ▀ ▀▀▀ █    █   █ █   █ █  ▄▀ 
█     █ ██▄▄       █    █   █ █   █ █▀▀▌  
 █    █ █▄   ▄▀   █     ▀████ ▀████ █  █  
  █  █  ▀███▀    ▀                    █   
   █▐                                ▀    
   ▐                                      """ + "\n"*2 + """por: passeado -'bh é nois'""" +'\n'+ '='*43)
        sleep(2)
        # inputs
        print("\033[H\033[J")
        input1 = calculate(input("vetor inicial:\n     ["))
        print("\033[H\033[J")
        input2 = calculate(input(f"vetor inicial:\n     [{input1}]\n     ["))
        print("\033[H\033[J")
        input3 = calculate(input(f"vetor inicial:\n     [{input1}]\n     [{input2}]\n\nMatriz:\n     ["))
        print("\033[H\033[J")
        input4 = calculate(input(f"vetor inicial:\n     [{input1}]\n     [{input2}]\n\nMatriz:\n     [{input3} "))
        print("\033[H\033[J")
        input5 = calculate(input(f"vetor inicial:\n     [{input1}]\n     [{input2}]\n\nMatriz:\n     [{input3} {input4}]\n     ["))
        print("\033[H\033[J")
        input6 = calculate(input(f"vetor inicial:\n     [{input1}]\n     [{input2}]\n\nMatriz:\n     [{input3} {input4}]\n     [{input5} "))
        print("\033[H\033[J")
        print(f"vetor inicial:\n     [{input1}]\n     [{input2}]\n\nMatriz:\n     [{input3} {input4}]\n     [{input5} {input6}]")

        #  processando os inputs 
        vetor_inicial = np.array([float(input1), float(input2), 0])
        matrix = np.array([[float(input3), float(input4), 0], [float(input5), float(input6), 0], [0, 0, 0]])

        
        #  feedback visual
        for i in range(1, 10):
            print("\033[H\033[J")
            print(f"vetor inicial:\n     [{input1}]\n     [{input2}]\n\nMatriz inicial:\n     [{input3} {input4}]\n     [{input5} {input6}]")
            print('processando.' + '.'*(i%3))
            sleep(0.2)
        

        # Fazendo a mathematicsss do bagulho
        vetor_final = np.dot(matrix, vetor_inicial)
        # print(f'vetor: {vetor_inicial}\n\nmatriz: {matrix}\n\nresultado: {vetor_final}')
        
        print("\033[H\033[J")
        print(f'você está multiplicando a matriz [{input3} {input4}] pelo vetor [{input1}]\n' +' '*33+ f'[{input5} {input6}]' +' '*(14-len(str(input5)+str(input6)))+ f'[{input2}]')

        input("enter <-")
        print(f'\nlogo, temos o vetor: [{input3}*{input1} + {input4}*{input2}]\n' +' '*21+ f'[{input5}*{input1} + {input6}*{input2}]')
        input("\nClique enter para gerar uma representaçao visutal desta tranformação <-")

        # Definindo os vetores
        initial_vector = vetor_inicial
        final_vector = vetor_final

        # Criando os vetores na cena
        initial_vector = Arrow(start=ORIGIN, end=initial_vector, color=GREEN, buff=0)
        final_vector = Arrow(start=ORIGIN, end=final_vector, color=RED, buff=0)

        # Adicionando os vetores à cena
        self.add(NumberPlane())
        self.play(Create(initial_vector))
        self.wait(1)
        
        # Transformação do vetor inicial para o vetor final
        self.play(Transform(initial_vector, final_vector))
        self.wait(1)
