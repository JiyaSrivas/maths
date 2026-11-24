"""
Linear Algebra and Calculus (M3) - Internal Assessment: Animation Video
Topic: Eigenvalues & Eigenvectors: Invariant Directions of Linear Transformations
Author: Jiya
Code: Manim Community Edition Scene Scripts
"""

from manim import *
import numpy as np

class EigenvaluesAndEigenvectors(Scene):
    """
    Comprehensive 6-Scene Manim Animation covering:
    1. Hook & Context (Transforming rubber sheet / rotating vectors)
    2. Concept Introduction (A v = lambda v, scalar vs matrix multiplication)
    3. Visual Intuition (Generic rotating vector vs Invariant eigenvectors for A = [[2,1],[1,2]])
    4. Step-by-Step Worked Example (det(A - lambda I) = 0, roots lambda=3, 1, finding eigenspaces)
    5. Geometric Interpretation (Decoupled vector decomposition and repeated powers A^k v)
    6. Summary & Credits (3 Key takeaways, author card, and credits)
    """

    def construct(self):
        self.camera.background_color = "#0f111a"
        self.play_scene_1_hook()
        self.play_scene_2_concept()
        self.play_scene_3_visual_intuition()
        self.play_scene_4_worked_example()
        self.play_scene_5_interpretation()
        self.play_scene_6_summary_credits()

    def play_scene_1_hook(self):
        # Opening Title Frame
        course_title = Text("LINEAR ALGEBRA & CALCULUS (M3)", font_size=28, color="#00d2ff")
        course_title.to_edge(UP, buff=0.8)
        
        main_title = Text("Eigenvalues & Eigenvectors", font_size=44, weight=BOLD, color=WHITE)
        subtitle = Text("The Invariant Directions of Linear Transformations", font_size=26, color="#fbc531")
        author_text = Text("Author: Jiya  |  Internal Assessment", font_size=22, color=GRAY)
        
        title_group = VGroup(course_title, main_title, subtitle, author_text)
        title_group.arrange(DOWN, buff=0.35)
        
        self.play(FadeIn(title_group, shift=UP*0.5), run_time=2.0)
        self.wait(2.0)
        self.play(FadeOut(title_group), run_time=1.5)

        # Motivating Question / Grid Warping
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-4, 4, 1],
            background_line_style={"stroke_color": "#2f3640", "stroke_width": 1.5}
        )
        self.play(Create(grid), run_time=1.5)

        question = Text("When space warps, do ALL vectors rotate?", font_size=32, color="#e84118")
        question.to_edge(UP, buff=0.6)
        self.play(Write(question), run_time=1.5)

        # Show arbitrary vectors rotating under a shear / stretch transformation
        vec1 = Arrow(start=ORIGIN, end=[2, 0, 0], color=GREEN, buff=0)
        vec2 = Arrow(start=ORIGIN, end=[0, 2, 0], color=YELLOW, buff=0)
        vec3 = Arrow(start=ORIGIN, end=[-1.5, 1.5, 0], color=PURPLE, buff=0)
        
        self.play(GrowArrow(vec1), GrowArrow(vec2), GrowArrow(vec3), run_time=1.5)
        self.wait(1.0)

        # Apply transformation matrix [[2, 1], [1, 2]]
        matrix_a = [[2, 1], [1, 2]]
        self.play(
            grid.animate.apply_matrix(matrix_a),
            vec1.animate.put_start_and_end_on(ORIGIN, [2, 1, 0]),
            vec2.animate.put_start_and_end_on(ORIGIN, [1, 2, 0]),
            vec3.animate.put_start_and_end_on(ORIGIN, [-1.5, 1.5, 0]),
            run_time=3.0
        )
        self.wait(1.5)
        self.play(FadeOut(grid), FadeOut(vec1), FadeOut(vec2), FadeOut(vec3), FadeOut(question))

    def play_scene_2_concept(self):
        scene_heading = Text("SCENE 2: The Core Definition", font_size=28, color="#00d2ff").to_edge(UP)
        self.play(Write(scene_heading))

        eq = MathTex(
            r"A \vec{v} = \lambda \vec{v}, \quad \vec{v} \neq \mathbf{0}",
            font_size=52
        )
        eq.set_color_by_tex(r"A", "#00d2ff")
        eq.set_color_by_tex(r"\vec{v}", "#fbc531")
        eq.set_color_by_tex(r"\lambda", "#e84118")
        
        self.play(Write(eq), run_time=2.0)
        self.wait(1.0)

        explanation = VGroup(
            Text("A : Transformation Matrix (multi-dimensional action)", font_size=24, color="#00d2ff"),
            Text("v : Eigenvector (Invariant direction, non-zero)", font_size=24, color="#fbc531"),
            Text("λ : Eigenvalue (Pure 1D scalar stretch/shrink factor)", font_size=24, color="#e84118"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(eq, DOWN, buff=0.8)

        self.play(FadeIn(explanation, shift=UP*0.3), run_time=2.0)
        self.wait(2.5)
        self.play(FadeOut(scene_heading), FadeOut(eq), FadeOut(explanation))

    def play_scene_3_visual_intuition(self):
        scene_heading = Text("SCENE 3: Visual Intuition", font_size=28, color="#00d2ff").to_edge(UP)
        matrix_label = MathTex(r"A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}", font_size=34).next_to(scene_heading, DOWN, buff=0.2)
        
        grid = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            background_line_style={"stroke_color": "#2f3640", "stroke_width": 1.2}
        )
        self.play(Write(scene_heading), Write(matrix_label), Create(grid))

        # Vector 1: Generic vector [1, 0]^T rotating to [2, 1]^T
        u_label = MathTex(r"\vec{u} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \to A\vec{u} = \begin{pmatrix} 2 \\ 1 \end{pmatrix} \text{ (Rotates!)}", font_size=24, color="#4cd137")
        u_label.to_corner(UL, buff=1.0)
        u_arrow = Arrow(ORIGIN, [1.5, 0, 0], color="#4cd137", buff=0)
        self.play(GrowArrow(u_arrow), Write(u_label))
        self.wait(1.0)
        self.play(u_arrow.animate.put_start_and_end_on(ORIGIN, [3.0, 1.5, 0]), run_time=2.0)
        self.wait(1.0)
        self.play(FadeOut(u_arrow), FadeOut(u_label))

        # Vector 2: Eigenvector [1, 1]^T stretching to [3, 3]^T (factor 3)
        v1_line = DashedLine([-3, -3, 0], [3, 3, 0], color="#fbc531", stroke_width=2)
        v1_label = MathTex(r"\vec{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix} \to A\vec{v}_1 = 3\vec{v}_1 \quad (\lambda_1 = 3)", font_size=26, color="#fbc531")
        v1_label.to_corner(UL, buff=1.0)
        v1_arrow = Arrow(ORIGIN, [1.0, 1.0, 0], color="#fbc531", buff=0)

        self.play(Create(v1_line), GrowArrow(v1_arrow), Write(v1_label))
        self.wait(1.0)
        self.play(v1_arrow.animate.put_start_and_end_on(ORIGIN, [3.0, 3.0, 0]), run_time=2.5)
        self.wait(1.5)

        # Vector 3: Second Eigenvector [-1, 1]^T (eigenvalue 1)
        v2_line = DashedLine([3, -3, 0], [-3, 3, 0], color="#00d2ff", stroke_width=2)
        v2_label = MathTex(r"\vec{v}_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix} \to A\vec{v}_2 = 1\vec{v}_2 \quad (\lambda_2 = 1)", font_size=26, color="#00d2ff")
        v2_label.next_to(v1_label, DOWN, buff=0.3, aligned_edge=LEFT)
        v2_arrow = Arrow(ORIGIN, [-1.0, 1.0, 0], color="#00d2ff", buff=0)

        self.play(Create(v2_line), GrowArrow(v2_arrow), Write(v2_label))
        self.wait(1.5)
        self.play(FadeOut(grid), FadeOut(v1_line), FadeOut(v1_arrow), FadeOut(v1_label),
                  FadeOut(v2_line), FadeOut(v2_arrow), FadeOut(v2_label),
                  FadeOut(scene_heading), FadeOut(matrix_label))

    def play_scene_4_worked_example(self):
        scene_heading = Text("SCENE 4: Step-by-Step Algebraic Derivation", font_size=28, color="#00d2ff").to_edge(UP)
        self.play(Write(scene_heading))

        steps = VGroup(
            MathTex(r"(A - \lambda I)\vec{v} = \mathbf{0} \implies \det(A - \lambda I) = 0", font_size=32),
            MathTex(r"\det\begin{pmatrix} 2 - \lambda & 1 \\ 1 & 2 - \lambda \end{pmatrix} = (2 - \lambda)^2 - 1 = 0", font_size=32),
            MathTex(r"\lambda^2 - 4\lambda + 3 = 0 \implies (\lambda - 3)(\lambda - 1) = 0", font_size=32),
            MathTex(r"\text{Eigenvalues: } \lambda_1 = 3, \quad \lambda_2 = 1", font_size=34, color="#fbc531"),
            MathTex(r"\text{For } \lambda_1 = 3: \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix}\vec{v} = \mathbf{0} \implies y = x \implies \vec{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}", font_size=28, color="#fbc531"),
            MathTex(r"\text{For } \lambda_2 = 1: \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}\vec{v} = \mathbf{0} \implies y = -x \implies \vec{v}_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix}", font_size=28, color="#00d2ff")
        ).arrange(DOWN, buff=0.35).next_to(scene_heading, DOWN, buff=0.4)

        for step in steps:
            self.play(Write(step), run_time=1.8)
            self.wait(0.8)
        self.wait(2.0)
        self.play(FadeOut(steps), FadeOut(scene_heading))

    def play_scene_5_interpretation(self):
        scene_heading = Text("SCENE 5: Decoupling & Diagonalization", font_size=28, color="#00d2ff").to_edge(UP)
        self.play(Write(scene_heading))

        eq1 = MathTex(r"\vec{x} = c_1 \vec{v}_1 + c_2 \vec{v}_2", font_size=36)
        eq2 = MathTex(r"A^k \vec{x} = c_1 (\lambda_1)^k \vec{v}_1 + c_2 (\lambda_2)^k \vec{v}_2", font_size=38, color="#fbc531")
        eq3 = MathTex(r"A = P D P^{-1} \quad \text{where } D = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}", font_size=34, color="#00d2ff")
        
        math_grp = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.4).next_to(scene_heading, DOWN, buff=0.5)
        self.play(Write(math_grp), run_time=3.0)
        self.wait(1.5)

        apps = VGroup(
            Text("• Google PageRank (Dominant web link eigenvector)", font_size=22),
            Text("• Structural Resonance (Vibration eigenmodes of bridges/towers)", font_size=22),
            Text("• Principal Component Analysis (Dimensionality reduction in AI)", font_size=22)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(math_grp, DOWN, buff=0.5)

        self.play(FadeIn(apps, shift=UP*0.3), run_time=2.0)
        self.wait(2.5)
        self.play(FadeOut(scene_heading), FadeOut(math_grp), FadeOut(apps))

    def play_scene_6_summary_credits(self):
        title = Text("Key Takeaways & Credits", font_size=34, color="#00d2ff").to_edge(UP, buff=0.6)
        self.play(Write(title))

        takeaways = VGroup(
            Text("1. Invariance: Eigenvectors only scale by λ without rotating.", font_size=24, color=WHITE),
            Text("2. Characteristic Equation: det(A - λI) = 0 computes the scaling factors.", font_size=24, color=WHITE),
            Text("3. Decoupling: The eigenbasis turns matrix operations into simple scalings.", font_size=24, color=WHITE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).next_to(title, DOWN, buff=0.5)

        credits = VGroup(
            Text("Course: Linear Algebra & Calculus (M3)", font_size=20, color=GRAY),
            Text("Student Author: Jiya", font_size=20, color="#fbc531"),
            Text("Tools: Python, Pillow, NumPy, FFmpeg, Manim", font_size=18, color=GRAY),
            Text("Audio: Apple Voice Daniel (Narration) | Royalty-Free Ambient Synthesizer", font_size=18, color=GRAY),
            Text("AI Tools Disclosure: Gemini Assistant utilized for code architecture & layout", font_size=16, color="#e84118")
        ).arrange(DOWN, buff=0.2).next_to(takeaways, DOWN, buff=0.6)

        self.play(FadeIn(takeaways, shift=UP*0.3), run_time=2.0)
        self.play(FadeIn(credits, shift=UP*0.3), run_time=2.0)
        self.wait(4.0)
