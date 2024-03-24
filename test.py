from time import sleep
from manim import *

class alg(Scene):
    def construct(self):
        # Define an algebraic operation in LaTeX
        equation = MathTex(r"x^2 + y^2 = z^2")
        
        # Display the equation on the screen
        self.play(Write(equation))
        
        # Wait a bit so the viewer can see the equation
        self.wait(2)

        # To update or transform the equation to a new one
        new_equation = MathTex(r"x^3 + y^3 = z^3")
        self.play(Transform(equation, new_equation))
        
        # Keep the new equation on screen for a while
        self.wait(2)
