from manim import *
import numpy as np

class magica(Scene):
    def construct(self):
        print('='*43 + "\n"*2 +  """    ▄   ▄███▄     ▄▄▄▄▀ ████▄ ████▄ █▄▄▄▄ 
     █  █▀   ▀ ▀▀▀ █    █   █ █   █ █  ▄▀ 
█     █ ██▄▄       █    █   █ █   █ █▀▀▌  
 █    █ █▄   ▄▀   █     ▀████ ▀████ █  █  
  █  █  ▀███▀    ▀                    █   
   █▐                                ▀    
   ▐                                      """ + "\n"*2 + """por: passeado -'bh é nois'""" +'\n'+ '='*43)
        
        # Valores exemplo, substitua pelos seus valores ou cálculos específicos
        vetor_inicial = np.array([2, 1, 0])
        matrix = [[1, 2], [3, 4]]

        # Calculando o vetor final
        vetor_final = np.dot(matrix, vetor_inicial[:2])  # Ajustado para usar só os 2 primeiros elementos
        vetor_final = np.append(vetor_final, 0)  # Adicionando a terceira dimensão de volta

        # Definindo e criando os vetores na cena
        initial_vector = Arrow(start=ORIGIN, end=vetor_inicial, color=BLUE, buff=0)
        final_vector = Arrow(start=ORIGIN, end=vetor_final, color=GREEN, buff=0)

        # Adicionando o vetor inicial à cena
        self.play(Create(initial_vector))
        self.wait(1)
        
        # Transformando o vetor inicial para o vetor final
        self.play(Transform(initial_vector, final_vector))
        self.wait(1)
