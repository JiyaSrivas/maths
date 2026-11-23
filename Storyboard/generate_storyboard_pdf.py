import os
from PIL import Image, ImageDraw, ImageFont

def create_storyboard_pdf(output_pdf_path):
    print("Generating Storyboard PDF...")
    # Page settings: A4 Landscape at 150 DPI (1754 x 1240)
    page_width, page_height = 1754, 1240
    
    # Try finding high-quality system fonts
    font_paths = [
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf"
    ]
    font_file = None
    for p in font_paths:
        if os.path.exists(p):
            font_file = p
            break
            
    def get_font(size, bold=False):
        if font_file:
            return ImageFont.truetype(font_file, size)
        return ImageFont.load_default()

    font_title = get_font(38, bold=True)
    font_subtitle = get_font(24)
    font_h1 = get_font(28, bold=True)
    font_body = get_font(18)
    font_small = get_font(15)
    font_code = get_font(16)

    # PAGE 1: Overview & Scenes 1-3
    page1 = Image.new("RGB", (page_width, page_height), "#ffffff")
    draw1 = ImageDraw.Draw(page1)

    # Header banner
    draw1.rectangle([0, 0, page_width, 130], fill="#1e272e")
    draw1.text((60, 25), "LINEAR ALGEBRA & CALCULUS (M3) — ANIMATION STORYBOARD", fill="#00d2ff", font=font_title)
    draw1.text((60, 80), "Topic: Eigenvalues & Eigenvectors: Invariant Directions | Author: Jiya | Duration: 5:14 min (1080p)", fill="#d2dae2", font=font_subtitle)

    # Learning Objective Box
    draw1.rounded_rectangle([60, 150, page_width - 60, 220], radius=8, fill="#f1f2f6", outline="#747d8c", width=1)
    draw1.text((80, 162), "Core Learning Objective:", fill="#2f3542", font=get_font(20, bold=True))
    draw1.text((80, 190), "“By the end of this video, the viewer will be able to visualize invariant directions of linear transformations and calculate eigenvalues & eigenspaces algebraically.”", fill="#57606f", font=font_body)

    # 3 Column layout for Scenes 1, 2, 3
    col_width = (page_width - 120 - 40) // 3
    y_start = 245
    card_height = 930

    scenes_p1 = [
        {
            "num": "Scene 1: Hook / Context",
            "time": "0:00 - 0:45 (~45s)",
            "purpose": "Spark Curiosity & Motivate Invariance",
            "visuals": [
                "• Title card: Course, Topic, Author.",
                "• 2D Cartesian plane shown as elastic sheet.",
                "• Linear matrix warps grid lines into parallelograms.",
                "• Multiple arrows rotate across quadrants.",
                "• Central guiding question highlighted:",
                "  'Do ALL vectors rotate, or do some remain?'"
            ],
            "narration": "“Welcome to Linear Algebra. Imagine the 2D plane as a flexible rubber sheet. When we apply a linear transformation matrix, the entire plane warps. Grid lines tilt, and almost every vector rotates... But here is the central question: does every vector turn? Or are there special invariant directions?”",
            "math": "T: R^2 -> R^2,  x -> A x\nMatrix deforms space; search for invariant lines."
        },
        {
            "num": "Scene 2: Concept Introduction",
            "time": "0:45 - 1:30 (~45s)",
            "purpose": "Formal Definition & Learning Goal",
            "visuals": [
                "• Clean formula reveal: A v = λ v, v != 0.",
                "• Color coding: Matrix A (cyan), v (gold), λ (coral).",
                "• Side-by-side comparison diagram:",
                "  Left: Matrix multiplication (2D transformation)",
                "  Right: Scalar multiplication (1D stretch/shrink)",
                "• Emphasize non-triviality condition v != 0."
            ],
            "narration": "“Let us state the formal definition. Given an n-by-n square matrix A, a non-zero vector v is an eigenvector if multiplying A by v produces a simple scalar multiple: A v = λ v. Notice the power: multi-dimensional transformation collapses into simple 1D stretching or shrinking.”",
            "math": "A v = λ v,  where v != 0\nλ in R (Eigenvalue),  v in R^n (Eigenvector)"
        },
        {
            "num": "Scene 3: Visual Intuition",
            "time": "1:30 - 2:30 (~60s)",
            "purpose": "Geometric Contrast: Generic vs Invariant",
            "visuals": [
                "• Matrix A = [[2, 1], [1, 2]] displayed on grid.",
                "• Generic vector u = [1, 0]^T transforms to [2, 1]^T",
                "  (Clear angle arc showing rotation of 26.57°).",
                "• Invariant vector v1 = [1, 1]^T along y = x stretches",
                "  smoothly to [3, 3]^T (stays on line, λ = 3!).",
                "• Invariant vector v2 = [-1, 1]^T on y = -x stays",
                "  identical to [-1, 1]^T (stationary, λ = 1!)."
            ],
            "narration": "“To build intuition, consider matrix [[2,1],[1,2]]. Standard basis vector [1,0] maps to [2,1]—clearly rotating. But look at [1,1] along y = x: it stretches to [3,3] without turning! Lambda equals 3. Along y = -x, [-1,1] maps to [-1,1], unchanged! Lambda equals 1.”",
            "math": "u = [1,0]^T -> [2,1]^T (Rotates)\nv1 = [1,1]^T -> [3,3]^T = 3 v1 (λ=3)\nv2 = [-1,1]^T -> [-1,1]^T = 1 v2 (λ=1)"
        }
    ]

    for idx, sc in enumerate(scenes_p1):
        x0 = 60 + idx * (col_width + 20)
        x1 = x0 + col_width
        draw1.rounded_rectangle([x0, y_start, x1, y_start + card_height], radius=8, fill="#ffffff", outline="#dfe4ea", width=2)
        # Card header
        draw1.rounded_rectangle([x0, y_start, x1, y_start + 70], radius=8, fill="#2f3542")
        draw1.text((x0 + 15, y_start + 12), sc["num"], fill="#00d2ff", font=get_font(20, bold=True))
        draw1.text((x0 + 15, y_start + 42), sc["time"] + " | " + sc["purpose"], fill="#ced6e0", font=font_small)

        # Visuals Section
        draw1.text((x0 + 15, y_start + 85), "VISUAL PLAN:", fill="#2f3542", font=get_font(16, bold=True))
        y_text = y_start + 115
        for line in sc["visuals"]:
            draw1.text((x0 + 15, y_text), line, fill="#3742fa" if "•" in line and "Scene" in line else "#2f3542", font=font_small)
            y_text += 26

        # Narration Section
        y_narr = y_start + 450
        draw1.rounded_rectangle([x0 + 10, y_narr, x1 - 10, y_narr + 260], radius=6, fill="#f1f2f6")
        draw1.text((x0 + 20, y_narr + 10), "SPOKEN NARRATION EXCERPT:", fill="#ff4757", font=get_font(15, bold=True))
        # Simple word wrap for narration
        words = sc["narration"].split()
        curr_line = ""
        y_line = y_narr + 35
        for w in words:
            test_line = curr_line + " " + w if curr_line else w
            if len(test_line) * 9 > (col_width - 40):
                draw1.text((x0 + 20, y_line), curr_line, fill="#2f3542", font=font_small)
                y_line += 22
                curr_line = w
            else:
                curr_line = test_line
        if curr_line:
            draw1.text((x0 + 20, y_line), curr_line, fill="#2f3542", font=font_small)

        # Math plan box
        y_math = y_start + 725
        draw1.rounded_rectangle([x0 + 10, y_math, x1 - 10, y_start + card_height - 15], radius=6, fill="#2ed573", outline="#26af5f", width=1)
        draw1.text((x0 + 20, y_math + 10), "MATHEMATICAL ANCHOR:", fill="#ffffff", font=get_font(15, bold=True))
        for mline in sc["math"].split("\n"):
            draw1.text((x0 + 20, y_math + 35), mline, fill="#ffffff", font=font_small)
            y_math += 25

    # PAGE 2: Scenes 4-6 + Checklist & Sign-off
    page2 = Image.new("RGB", (page_width, page_height), "#ffffff")
    draw2 = ImageDraw.Draw(page2)

    # Header banner
    draw2.rectangle([0, 0, page_width, 130], fill="#1e272e")
    draw2.text((60, 25), "LINEAR ALGEBRA & CALCULUS (M3) — ANIMATION STORYBOARD", fill="#00d2ff", font=font_title)
    draw2.text((60, 80), "Part 2: Worked Calculations, Interpretation, Summary & Assessment Checklist", fill="#d2dae2", font=font_subtitle)

    scenes_p2 = [
        {
            "num": "Scene 4: Step-by-Step Worked Example",
            "time": "2:30 - 3:45 (~75s)",
            "purpose": "Rigorous Algebraic Derivation",
            "visuals": [
                "• Blackboard derivation of (A - λ I) v = 0.",
                "• Singularity condition: det(A - λ I) = 0.",
                "• Expand determinant: (2 - λ)^2 - 1 = 0.",
                "• Quadratic polynomial: λ^2 - 4λ + 3 = 0.",
                "• Factoring: (λ - 3)(λ - 1) = 0 -> λ1 = 3, λ2 = 1.",
                "• Finding eigenspaces for λ=3: y = x, v1 = [1, 1].",
                "• Finding eigenspaces for λ=1: y = -x, v2 = [-1, 1].",
                "• Green checkmarks verifying A v = λ v."
            ],
            "narration": "“How do we find these algebraically? We set (A - λ I)v = 0. For non-trivial solutions, det(A - λ I) must equal zero. Expanding gives λ^2 - 4λ + 3 = 0, giving eigenvalues 3 and 1. Substituting back yields eigenvectors [1, 1] and [-1, 1], matching our geometry perfectly!”",
            "math": "det(A - λ I) = λ^2 - 4λ + 3 = 0\nλ1 = 3 -> v1 = [1, 1]^T\nλ2 = 1 -> v2 = [-1, 1]^T"
        },
        {
            "num": "Scene 5: Geometric Interpretation",
            "time": "3:45 - 4:35 (~50s)",
            "purpose": "Connect Algebra Back to Geometry & Apps",
            "visuals": [
                "• Vector decomposition: x = c1 v1 + c2 v2.",
                "• Dynamic animation of applying matrix repeatedly:",
                "  A^k x = c1 (3^k) v1 + c2 (1^k) v2.",
                "• Space stretches along v1; v2 stays fixed.",
                "• Real-world applications illustrated:",
                "  1. Google PageRank (Dominant web eigenvector)",
                "  2. Resonance / Vibrations in skyscrapers & bridges",
                "  3. Principal Component Analysis (AI / PCA)"
            ],
            "narration": "“Because eigenvectors form a basis, any vector decomposes into c1 v1 + c2 v2. Repeatedly multiplying by A doesn't require matrix powers—it simplifies into scaling along the eigen-axes! This powers Google PageRank, predicts bridge vibration frequencies, and drives machine learning.”",
            "math": "x = c1 v1 + c2 v2\nA^k x = c1 (3^k) v1 + c2 (1^k) v2\nDiagonalization: A = P D P^(-1)"
        },
        {
            "num": "Scene 6: Summary & Credits",
            "time": "4:35 - 5:05 (~30s)",
            "purpose": "Reinforce Takeaways & Comply with Credits",
            "visuals": [
                "• 3 Key Takeaway cards glow on screen:",
                "  1. Invariance (No rotation, only scaling)",
                "  2. Characteristic Equation (det(A - λ I) = 0)",
                "  3. Decoupling (Eigenbasis diagonalizes action)",
                "• Closing frame with full formal credits:",
                "  Student: Jiya | Course: M3 | Submission 2026",
                "  Tools: Python, Pillow, NumPy, FFmpeg, Manim",
                "  Music & AI Disclosure statements."
            ],
            "narration": "“To summarize: Eigenvectors are invariant directions. Eigenvalues are the roots of det(A - λ I) = 0. And the eigenbasis turns complex matrix operations into parallel scalings. Produced for Linear Algebra & Calculus M3 by Jiya. Thank you for watching!”",
            "math": "Takeaway 1: A v = λ v\nTakeaway 2: det(A - λ I) = 0\nTakeaway 3: A = P D P^(-1)"
        }
    ]

    for idx, sc in enumerate(scenes_p2):
        x0 = 60 + idx * (col_width + 20)
        x1 = x0 + col_width
        draw2.rounded_rectangle([x0, y_start, x1, y_start + card_height], radius=8, fill="#ffffff", outline="#dfe4ea", width=2)
        # Card header
        draw2.rounded_rectangle([x0, y_start, x1, y_start + 70], radius=8, fill="#2f3542")
        draw2.text((x0 + 15, y_start + 12), sc["num"], fill="#00d2ff", font=get_font(20, bold=True))
        draw2.text((x0 + 15, y_start + 42), sc["time"] + " | " + sc["purpose"], fill="#ced6e0", font=font_small)

        # Visuals Section
        draw2.text((x0 + 15, y_start + 85), "VISUAL PLAN:", fill="#2f3542", font=get_font(16, bold=True))
        y_text = y_start + 115
        for line in sc["visuals"]:
            draw2.text((x0 + 15, y_text), line, fill="#2f3542", font=font_small)
            y_text += 26

        # Narration Section
        y_narr = y_start + 450
        draw2.rounded_rectangle([x0 + 10, y_narr, x1 - 10, y_narr + 260], radius=6, fill="#f1f2f6")
        draw2.text((x0 + 20, y_narr + 10), "SPOKEN NARRATION EXCERPT:", fill="#ff4757", font=get_font(15, bold=True))
        words = sc["narration"].split()
        curr_line = ""
        y_line = y_narr + 35
        for w in words:
            test_line = curr_line + " " + w if curr_line else w
            if len(test_line) * 9 > (col_width - 40):
                draw2.text((x0 + 20, y_line), curr_line, fill="#2f3542", font=font_small)
                y_line += 22
                curr_line = w
            else:
                curr_line = test_line
        if curr_line:
            draw2.text((x0 + 20, y_line), curr_line, fill="#2f3542", font=font_small)

        # Math plan box
        y_math = y_start + 725
        draw2.rounded_rectangle([x0 + 10, y_math, x1 - 10, y_start + card_height - 15], radius=6, fill="#2ed573", outline="#26af5f", width=1)
        draw2.text((x0 + 20, y_math + 10), "MATHEMATICAL ANCHOR:", fill="#ffffff", font=get_font(15, bold=True))
        for mline in sc["math"].split("\n"):
            draw2.text((x0 + 20, y_math + 35), mline, fill="#ffffff", font=font_small)
            y_math += 25

    # Save multi-page PDF
    page1.save(output_pdf_path, save_all=True, append_images=[page2], resolution=150)
    print(f"Successfully generated high-resolution Storyboard PDF at: {output_pdf_path}")

if __name__ == "__main__":
    out_pdf = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Storyboard", "Storyboard.pdf")
    create_storyboard_pdf(out_pdf)
