from manim import *

class Vector3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)
        vector_cat = Arrow3D(start = np.array([0, 0, 0]), end = np.array([0.45281, -0.50108, -0.53714]), color = RED)
        vector_dog = Arrow3D(start = np.array([0, 0, 0]), end = np.array([0.11008, -0.38781, -0.57615]), color = BLUE)
        vector_flower = Arrow3D(start = np.array([0, 0, 0]), end = np.array([0.075439, 1.2659, -1.3179]), color = GREEN)
        
        # vector_dog = Arrow3D(start = [0, 0, 0], end = [2,2,2], color = BLUE)
        # vector_flower = Arrow3D(start = [0, 0, 0], end = [3,3,3], color = GREEN)
        # label_cat = MathTex(r"Cat", color = RED).next_to(vector_cat, UP)
        # label_dog = MathTex(r"Dog", color = BLUE).next_to(vector_dog, UP)
        # labal_flower = MathTex(r"Flower", color = GREEN).next_to(vector_flower, UP)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(vector_cat, vector_dog, vector_flower)
        self.wait()
        self.move_camera(phi=-100 * DEGREES, theta=360 * DEGREES)
        self.wait()
        # self.play(Create(vector_cat))




