from manim import *

class Vector3D(Scene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)
        vector_cat = Arrow3D(start = [0, 0, 0], end = [0.45281, -0.50108, -0.53714], color = RED)
        vector_dog = Arrow3D(start = [0, 0, 0], end = [0.11008,  -0.38781,  -0.57615], color = BLUE)
        vector_flower = Arrow3D(start = [0, 0, 0], end = [0.075439 , 1.2659,   -1.3179], color = GREEN)
        label_cat = MathTex(r"Cat", color = RED).next_to(vector_cat, UP)
        label_dog = MathTex(r"Dog", color = BLUE).next_to(vector_dog, UP)
        labal_flower = MathTex(r"Flower", color = GREEN).next_to(vector_flower, UP)
        self.play(Create(vector))




