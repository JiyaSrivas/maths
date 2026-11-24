"""
LINEAR ALGEBRA & CALCULUS (M3) - ANIMATION VIDEO RENDERER
Topic: Eigenvalues and Eigenvectors: Invariant Directions of Linear Transformations
Author: Jiya
Resolution: 1080p (1920x1080), 24 FPS
"""

import os
import sys
import wave
import math
import subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# Dimensions & Settings
WIDTH, HEIGHT = 1920, 1080
FPS = 24

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUDIO_DIR = os.path.join(BASE_DIR, "audio_cache")
OUTPUT_MP4 = os.path.join(BASE_DIR, "_Video.mp4")

# Font configuration
def get_font(size, bold=False):
    font_paths = [
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/SFNS.ttf",
        "/Library/Fonts/Arial.ttf"
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

FONT_TITLE = get_font(44, bold=True)
FONT_SUBTITLE = get_font(26)
FONT_HEADING = get_font(32, bold=True)
FONT_CARD_TITLE = get_font(24, bold=True)
FONT_BODY = get_font(20)
FONT_MATH_LARGE = get_font(38, bold=True)
FONT_MATH_MED = get_font(26, bold=True)
FONT_SMALL = get_font(16)

# Colors
BG_COLOR = "#0c1017"
PANEL_BG = "#161b22"
BORDER_COLOR = "#30363d"
CYAN = "#00d2ff"
GOLD = "#fbc531"
CORAL = "#ff4757"
GREEN = "#2ed573"
PURPLE = "#a55eea"
WHITE = "#ffffff"
GRAY_TEXT = "#8b949e"
LIGHT_GRAY = "#c9d1d9"
GRID_COLOR = "#1b2331"
AXIS_COLOR = "#485460"

def ease_in_out(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3.0 - 2.0 * t)

def get_audio_duration(wav_path):
    with wave.open(wav_path, "rb") as wf:
        return wf.getnframes() / float(wf.getframerate())

def draw_arrow(draw, start, end, color, width=4, tip_len=18):
    x0, y0 = start
    x1, y1 = end
    dx = x1 - x0
    dy = y1 - y0
    length = math.hypot(dx, dy)
    if length < 1:
        return
    draw.line([(x0, y0), (x1, y1)], fill=color, width=width)
    ux = dx / length
    uy = dy / length
    vx = -uy
    vy = ux
    bx = x1 - tip_len * ux
    by = y1 - tip_len * uy
    tip_w = tip_len * 0.5
    p1 = (bx + tip_w * vx, by + tip_w * vy)
    p2 = (bx - tip_w * vx, by - tip_w * vy)
    draw.polygon([(x1, y1), p1, p2], fill=color)

def draw_grid_system(draw, origin, scale, matrix=None, grid_range=5):
    ox, oy = origin
    if matrix is None:
        m00, m01 = 1.0, 0.0
        m10, m11 = 0.0, 1.0
    else:
        m00, m01 = matrix[0]
        m10, m11 = matrix[1]

    def transform(x, y):
        tx = m00 * x + m01 * y
        ty = m10 * x + m11 * y
        return (ox + tx * scale, oy - ty * scale)

    for i in range(-grid_range, grid_range + 1):
        p1 = transform(i, -grid_range)
        p2 = transform(i, grid_range)
        draw.line([p1, p2], fill=GRID_COLOR, width=1)
        p3 = transform(-grid_range, i)
        p4 = transform(grid_range, i)
        draw.line([p3, p4], fill=GRID_COLOR, width=1)

    draw.line([transform(-grid_range, 0), transform(grid_range, 0)], fill=AXIS_COLOR, width=2)
    draw.line([transform(0, -grid_range), transform(0, grid_range)], fill=AXIS_COLOR, width=2)
    draw.ellipse([ox - 4, oy - 4, ox + 4, oy + 4], fill=WHITE)

def draw_top_bar(draw, scene_num, scene_title, progress):
    draw.rectangle([0, 0, WIDTH, 70], fill=PANEL_BG)
    draw.line([(0, 70), (WIDTH, 70)], fill=BORDER_COLOR, width=2)
    draw.text((40, 12), "LINEAR ALGEBRA & CALCULUS (M3)", fill=CYAN, font=FONT_SMALL)
    draw.text((40, 32), f"Scene {scene_num}: {scene_title}", fill=WHITE, font=FONT_CARD_TITLE)
    draw.text((WIDTH - 280, 24), "Jiya | Eigenvalues & Eigenvectors", fill=GRAY_TEXT, font=FONT_BODY)
    bar_w = int(WIDTH * progress)
    draw.rectangle([0, 68, bar_w, 72], fill=CYAN)

# ----------------- SCENE RENDERERS -----------------

def render_scene_1(frame_idx, total_frames, t_sec, total_sec):
    im = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(im)
    draw_top_bar(draw, 1, "Hook & Context: Do All Vectors Rotate?", frame_idx / total_frames)
    
    # Title card intro (first 8 seconds)
    if t_sec < 8.0:
        alpha = min(1.0, t_sec / 1.5)
        cy = HEIGHT // 2 - 40
        draw.rounded_rectangle([300, cy - 140, WIDTH - 300, cy + 180], radius=16, fill=PANEL_BG, outline=CYAN, width=2)
        draw.text((WIDTH // 2 - 280, cy - 100), "LINEAR ALGEBRA & CALCULUS", fill=CYAN, font=FONT_SUBTITLE)
        draw.text((WIDTH // 2 - 380, cy - 50), "Eigenvalues & Eigenvectors", fill=WHITE, font=FONT_TITLE)
        draw.text((WIDTH // 2 - 320, cy + 20), "The Invariant Directions of Linear Transformations", fill=GOLD, font=FONT_SUBTITLE)
        draw.text((WIDTH // 2 - 200, cy + 80), "Option 1: Mathematical Animation Video", fill=LIGHT_GRAY, font=FONT_BODY)
        draw.text((WIDTH // 2 - 140, cy + 120), "Student: Jiya | Assessment M3", fill=GRAY_TEXT, font=FONT_BODY)
        return im

    # 2D Grid with warping animation
    ox, oy = 720, 580
    scale = 90
    warp_progress = ease_in_out(max(0.0, min(1.0, (t_sec - 12.0) / 10.0)))
    
    # Target matrix A = [[2, 1], [1, 2]]
    m00 = 1.0 + (2.0 - 1.0) * warp_progress
    m01 = 0.0 + (1.0 - 0.0) * warp_progress
    m10 = 0.0 + (1.0 - 0.0) * warp_progress
    m11 = 1.0 + (2.0 - 1.0) * warp_progress
    mat = [[m00, m01], [m10, m11]]

    draw_grid_system(draw, (ox, oy), scale, matrix=mat, grid_range=4)

    # Radial fan of vectors
    angles = [0, 45, 90, 135, 180, 225, 270, 315]
    colors = [GREEN, GOLD, CYAN, PURPLE, GREEN, GOLD, CYAN, PURPLE]
    for i, ang in enumerate(angles):
        rad = math.radians(ang)
        vx = math.cos(rad) * 1.6
        vy = math.sin(rad) * 1.6
        tx = m00 * vx + m01 * vy
        ty = m10 * vx + m11 * vy
        end_pt = (ox + tx * scale, oy - ty * scale)
        draw_arrow(draw, (ox, oy), end_pt, colors[i], width=3)

    # Right side narrative cards
    rx = 1320
    draw.rounded_rectangle([rx, 140, WIDTH - 60, 460], radius=12, fill=PANEL_BG, outline=BORDER_COLOR, width=1)
    draw.text((rx + 25, 165), "THE TRANSFORMATION PUZZLE", fill=CYAN, font=FONT_CARD_TITLE)
    draw.text((rx + 25, 215), "Matrix A warps 2D space:", fill=LIGHT_GRAY, font=FONT_BODY)
    draw.text((rx + 45, 255), "• Grid lines tilt into diagonals", fill=WHITE, font=FONT_BODY)
    draw.text((rx + 45, 295), "• Unit squares stretch to parallelograms", fill=WHITE, font=FONT_BODY)
    draw.text((rx + 45, 335), "• Vectors rotate and tilt across quadrants", fill=WHITE, font=FONT_BODY)
    
    if t_sec > 24.0:
        draw.rounded_rectangle([rx, 500, WIDTH - 60, 880], radius=12, fill=PANEL_BG, outline=CORAL, width=2)
        draw.text((rx + 25, 525), "CENTRAL GUIDING QUESTION:", fill=CORAL, font=FONT_CARD_TITLE)
        draw.text((rx + 25, 580), "Do ALL vectors rotate?", fill=WHITE, font=FONT_HEADING)
        draw.text((rx + 25, 640), "Or are there special, invariant", fill=LIGHT_GRAY, font=FONT_BODY)
        draw.text((rx + 25, 675), "directions that stubbornly refuse", fill=LIGHT_GRAY, font=FONT_BODY)
        draw.text((rx + 25, 710), "to turn, changing ONLY in scale?", fill=GOLD, font=FONT_HEADING)
        draw.text((rx + 25, 780), "-> These are EIGENVECTORS.", fill=CYAN, font=FONT_CARD_TITLE)

    return im

def render_scene_2(frame_idx, total_frames, t_sec, total_sec):
    im = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(im)
    draw_top_bar(draw, 2, "Concept Introduction: The Core Equation", frame_idx / total_frames)

    # Master definition formula banner
    cy = 130
    draw.rounded_rectangle([180, cy, WIDTH - 180, cy + 180], radius=16, fill=PANEL_BG, outline=GOLD, width=2)
    draw.text((WIDTH // 2 - 380, cy + 30), "THE EIGENVALUE-EIGENVECTOR EQUATION", fill=GRAY_TEXT, font=FONT_SMALL)
    
    # Beautiful color-coded formula
    fx = WIDTH // 2 - 280
    fy = cy + 70
    draw.text((fx, fy), "A", fill=CYAN, font=FONT_MATH_LARGE)
    draw.text((fx + 50, fy), "v", fill=GOLD, font=FONT_MATH_LARGE)
    draw.text((fx + 100, fy), "=", fill=WHITE, font=FONT_MATH_LARGE)
    draw.text((fx + 150, fy), "λ", fill=CORAL, font=FONT_MATH_LARGE)
    draw.text((fx + 200, fy), "v", fill=GOLD, font=FONT_MATH_LARGE)
    draw.text((fx + 280, fy), ",    v  ≠  0", fill=WHITE, font=FONT_MATH_LARGE)

    # 3 Term Explanation Cards
    cards_y = 360
    card_w = (WIDTH - 180*2 - 40*2) // 3
    
    # Card 1: Matrix A
    c1_x = 180
    draw.rounded_rectangle([c1_x, cards_y, c1_x + card_w, cards_y + 360], radius=12, fill=PANEL_BG, outline=CYAN, width=2)
    draw.rectangle([c1_x, cards_y, c1_x + card_w, cards_y + 60], fill="#112d42")
    draw.text((c1_x + 20, cards_y + 15), "Matrix  A", fill=CYAN, font=FONT_CARD_TITLE)
    draw.text((c1_x + 20, cards_y + 85), "• n × n Transformation Matrix", fill=WHITE, font=FONT_BODY)
    draw.text((c1_x + 20, cards_y + 130), "• Represents multi-dimensional", fill=LIGHT_GRAY, font=FONT_BODY)
    draw.text((c1_x + 20, cards_y + 160), "  action on space", fill=LIGHT_GRAY, font=FONT_BODY)
    draw.text((c1_x + 20, cards_y + 210), "• In general, mixes and rotates", fill=LIGHT_GRAY, font=FONT_BODY)
    draw.text((c1_x + 20, cards_y + 240), "  vector components", fill=LIGHT_GRAY, font=FONT_BODY)

    # Card 2: Eigenvector v
    c2_x = c1_x + card_w + 40
    draw.rounded_rectangle([c2_x, cards_y, c2_x + card_w, cards_y + 360], radius=12, fill=PANEL_BG, outline=GOLD, width=2)
    draw.rectangle([c2_x, cards_y, c2_x + card_w, cards_y + 60], fill="#3d3314")
    draw.text((c2_x + 20, cards_y + 15), "Eigenvector  v", fill=GOLD, font=FONT_CARD_TITLE)
    draw.text((c2_x + 20, cards_y + 85), "• Invariant Direction", fill=WHITE, font=FONT_BODY)
    draw.text((c2_x + 20, cards_y + 130), "• Stays locked on its original line", fill=LIGHT_GRAY, font=FONT_BODY)
    draw.text((c2_x + 20, cards_y + 160), "  span(v)", fill=GOLD, font=FONT_BODY)
    draw.text((c2_x + 20, cards_y + 210), "• NEVER rotates under A", fill=GREEN, font=FONT_CARD_TITLE)
    draw.text((c2_x + 20, cards_y + 260), "• STRICTLY NON-ZERO (v ≠ 0)", fill=CORAL, font=FONT_BODY)

    # Card 3: Eigenvalue lambda
    c3_x = c2_x + card_w + 40
    draw.rounded_rectangle([c3_x, cards_y, c3_x + card_w, cards_y + 360], radius=12, fill=PANEL_BG, outline=CORAL, width=2)
    draw.rectangle([c3_x, cards_y, c3_x + card_w, cards_y + 60], fill="#3d181c")
    draw.text((c3_x + 20, cards_y + 15), "Eigenvalue  λ", fill=CORAL, font=FONT_CARD_TITLE)
    draw.text((c3_x + 20, cards_y + 85), "• 1D Scalar Scaling Factor", fill=WHITE, font=FONT_BODY)
    draw.text((c3_x + 20, cards_y + 130), "• λ > 1 : Stretches vector", fill=LIGHT_GRAY, font=FONT_BODY)
    draw.text((c3_x + 20, cards_y + 170), "• 0 < λ < 1 : Shrinks vector", fill=LIGHT_GRAY, font=FONT_BODY)
    draw.text((c3_x + 20, cards_y + 210), "• λ < 0 : Flips direction 180°", fill=LIGHT_GRAY, font=FONT_BODY)
    draw.text((c3_x + 20, cards_y + 250), "• λ = 0 : Collapses to origin", fill=LIGHT_GRAY, font=FONT_BODY)

    # Bottom Callout Box: Why non-zero?
    by = 770
    draw.rounded_rectangle([180, by, WIDTH - 180, by + 190], radius=12, fill=PANEL_BG, outline=BORDER_COLOR, width=1)
    draw.text((220, by + 25), "WHY DO WE MANDATE  v ≠ 0 ?", fill=GOLD, font=FONT_CARD_TITLE)
    draw.text((220, by + 70), "If v = 0 was allowed, then  A(0) = λ(0) = 0  would hold trivially for EVERY scalar λ in the universe.", fill=WHITE, font=FONT_BODY)
    draw.text((220, by + 110), "That would make the eigenvalue undefined. Hence, eigenvectors must be genuine non-zero directions.", fill=LIGHT_GRAY, font=FONT_BODY)
    draw.text((220, by + 145), "However, the eigenvalue λ itself CAN be zero (indicating a non-trivial nullspace / singular matrix).", fill=CYAN, font=FONT_BODY)

    return im

def render_scene_3(frame_idx, total_frames, t_sec, total_sec):
    im = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(im)
    draw_top_bar(draw, 3, "Visual Intuition: Generic vs Invariant Directions", frame_idx / total_frames)

    # Left / Center: Interactive Coordinate Canvas
    ox, oy = 660, 580
    scale = 110
    draw_grid_system(draw, (ox, oy), scale, grid_range=4)

    # Matrix card
    draw.rounded_rectangle([50, 95, 380, 210], radius=8, fill=PANEL_BG, outline=CYAN, width=1)
    draw.text((70, 108), "TRANSFORMATION MATRIX", fill=CYAN, font=FONT_SMALL)
    draw.text((70, 135), "A = [ [2, 1],", fill=WHITE, font=FONT_MATH_MED)
    draw.text((120, 168), "[1, 2] ]", fill=WHITE, font=FONT_MATH_MED)

    # Right Side Dashboard
    rx = 1260
    draw.rounded_rectangle([rx, 95, WIDTH - 50, 980], radius=12, fill=PANEL_BG, outline=BORDER_COLOR, width=1)
    draw.text((rx + 25, 120), "VECTOR BEHAVIOR TELEMETRY", fill=WHITE, font=FONT_CARD_TITLE)
    draw.line([(rx + 25, 160), (WIDTH - 75, 160)], fill=BORDER_COLOR, width=1)

    # PHASE 1: Generic vector [1, 0] (0 to 20s)
    if t_sec < 20.0:
        p = ease_in_out(min(1.0, max(0.0, (t_sec - 4.0) / 7.0)))
        ux = 1.0 + (2.0 - 1.0) * p
        uy = 0.0 + (1.0 - 0.0) * p
        draw_arrow(draw, (ox, oy), (ox + ux * scale, oy - uy * scale), GREEN, width=5)
        # Original span line
        draw.line([(ox, oy), (ox + 3 * scale, oy)], fill="#2ed57355", width=2)
        # Arc indicating rotation
        rot_ang = math.degrees(math.atan2(uy, ux))
        draw.text((ox + int(ux * scale) + 15, oy - int(uy * scale) - 20), f"u -> [{ux:.1f}, {uy:.1f}]", fill=GREEN, font=FONT_CARD_TITLE)

        draw.rounded_rectangle([rx + 20, 180, WIDTH - 70, 480], radius=10, fill="#1c2b22", outline=GREEN, width=2)
        draw.text((rx + 35, 205), "TEST 1: GENERIC VECTOR  u", fill=GREEN, font=FONT_CARD_TITLE)
        draw.text((rx + 35, 250), "Input:  u = [ 1, 0 ]^T", fill=WHITE, font=FONT_BODY)
        draw.text((rx + 35, 290), "Transformed: A u = [ 2, 1 ]^T", fill=WHITE, font=FONT_BODY)
        draw.text((rx + 35, 340), f"Rotation Angle: {rot_ang:.1f}°", fill=CORAL, font=FONT_HEADING)
        draw.text((rx + 35, 400), "VERDICT: NOT AN EIGENVECTOR", fill=CORAL, font=FONT_CARD_TITLE)
        draw.text((rx + 35, 435), "Vector was knocked off its span line!", fill=LIGHT_GRAY, font=FONT_BODY)

    # PHASE 2: Eigenvector 1 [1, 1] (20s to 42s)
    elif t_sec < 42.0:
        # Draw dashed line y = x
        draw.line([(ox - 3 * scale, oy + 3 * scale), (ox + 3.5 * scale, oy - 3.5 * scale)], fill="#fbc53166", width=2)
        draw.text((ox + 2.5 * scale, oy - 2.8 * scale), "Line: y = x", fill=GOLD, font=FONT_BODY)

        p = ease_in_out(min(1.0, max(0.0, (t_sec - 24.0) / 8.0)))
        vx = 1.0 + (3.0 - 1.0) * p
        vy = 1.0 + (3.0 - 1.0) * p
        draw_arrow(draw, (ox, oy), (ox + vx * scale, oy - vy * scale), GOLD, width=6)
        draw.text((ox + int(vx * scale) + 15, oy - int(vy * scale) - 15), f"v1 -> [{vx:.1f}, {vy:.1f}]", fill=GOLD, font=FONT_CARD_TITLE)

        draw.rounded_rectangle([rx + 20, 180, WIDTH - 70, 520], radius=10, fill="#382e16", outline=GOLD, width=2)
        draw.text((rx + 35, 205), "TEST 2: INVARIANT VECTOR  v1", fill=GOLD, font=FONT_CARD_TITLE)
        draw.text((rx + 35, 250), "Input:  v1 = [ 1, 1 ]^T", fill=WHITE, font=FONT_BODY)
        draw.text((rx + 35, 290), "Transformed: A v1 = [ 3, 3 ]^T", fill=WHITE, font=FONT_BODY)
        draw.text((rx + 35, 340), "Rotation Angle: 0.0° (NONE!)", fill=GREEN, font=FONT_HEADING)
        draw.text((rx + 35, 400), "Length: Stretched exactly  3 ×", fill=GOLD, font=FONT_HEADING)
        draw.text((rx + 35, 455), "EIGENVALUE:  λ1 = 3", fill=CYAN, font=FONT_HEADING)

    # PHASE 3: Eigenvector 2 [-1, 1] (42s to end)
    else:
        # Both invariant axes visible
        draw.line([(ox - 3 * scale, oy + 3 * scale), (ox + 3.5 * scale, oy - 3.5 * scale)], fill="#fbc53144", width=2)
        draw.line([(ox + 3 * scale, oy + 3 * scale), (ox - 3.5 * scale, oy - 3.5 * scale)], fill="#00d2ff66", width=2)
        draw.text((ox - 2.8 * scale, oy - 2.8 * scale), "Line: y = -x", fill=CYAN, font=FONT_BODY)

        # Show v1 locked
        draw_arrow(draw, (ox, oy), (ox + 3.0 * scale, oy - 3.0 * scale), GOLD, width=4)
        # Show v2
        draw_arrow(draw, (ox, oy), (ox - 1.0 * scale, oy - 1.0 * scale), CYAN, width=6)
        draw.text((ox - 1.0 * scale - 140, oy - 1.0 * scale - 20), "v2 = [-1, 1]", fill=CYAN, font=FONT_CARD_TITLE)

        draw.rounded_rectangle([rx + 20, 180, WIDTH - 70, 520], radius=10, fill="#122938", outline=CYAN, width=2)
        draw.text((rx + 35, 205), "TEST 3: ORTHOGONAL AXIS  v2", fill=CYAN, font=FONT_CARD_TITLE)
        draw.text((rx + 35, 250), "Input:  v2 = [ -1, 1 ]^T", fill=WHITE, font=FONT_BODY)
        draw.text((rx + 35, 290), "Transformed: A v2 = [ -1, 1 ]^T", fill=WHITE, font=FONT_BODY)
        draw.text((rx + 35, 340), "Rotation Angle: 0.0° (NONE!)", fill=GREEN, font=FONT_HEADING)
        draw.text((rx + 35, 400), "Length: 100% UNCHANGED (1 ×)", fill=CYAN, font=FONT_HEADING)
        draw.text((rx + 35, 455), "EIGENVALUE:  λ2 = 1", fill=GOLD, font=FONT_HEADING)

        draw.rounded_rectangle([rx + 20, 550, WIDTH - 70, 780], radius=10, fill=PANEL_BG, outline=BORDER_COLOR, width=1)
        draw.text((rx + 35, 575), "SPECTRAL THEOREM NOTE:", fill=GOLD, font=FONT_CARD_TITLE)
        draw.text((rx + 35, 620), "Because A is symmetric (A = A^T),", fill=LIGHT_GRAY, font=FONT_BODY)
        draw.text((rx + 35, 655), "its eigenvectors are ORTHOGONAL:", fill=WHITE, font=FONT_BODY)
        draw.text((rx + 35, 700), "v1 · v2 = (1)(-1) + (1)(1) = 0", fill=GREEN, font=FONT_HEADING)

    return im

def render_scene_4(frame_idx, total_frames, t_sec, total_sec):
    im = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(im)
    draw_top_bar(draw, 4, "Step-by-Step Worked Algebraic Derivation", frame_idx / total_frames)

    # 2 Column Blackboard View
    col1_x = 80
    col1_w = 860
    col2_x = 980
    col2_w = 860

    # Column 1: Finding Eigenvalues via det(A - λI) = 0
    draw.rounded_rectangle([col1_x, 100, col1_x + col1_w, 980], radius=14, fill=PANEL_BG, outline=BORDER_COLOR, width=1)
    draw.rectangle([col1_x, 100, col1_x + col1_w, 160], fill="#1c2433")
    draw.text((col1_x + 30, 118), "PART 1: THE CHARACTERISTIC EQUATION", fill=CYAN, font=FONT_CARD_TITLE)

    y = 190
    draw.text((col1_x + 30, y), "Step 1: Start with the core identity", fill=GRAY_TEXT, font=FONT_SMALL)
    y += 30
    draw.text((col1_x + 50, y), "A v = λ v  ==>  (A - λ I) v = 0", fill=WHITE, font=FONT_MATH_MED)

    y += 75
    draw.text((col1_x + 30, y), "Step 2: Condition for non-zero v", fill=GRAY_TEXT, font=FONT_SMALL)
    y += 30
    draw.text((col1_x + 50, y), "Matrix must be singular:  det(A - λ I) = 0", fill=GOLD, font=FONT_MATH_MED)

    y += 75
    draw.text((col1_x + 30, y), "Step 3: Construct the characteristic matrix", fill=GRAY_TEXT, font=FONT_SMALL)
    y += 30
    draw.text((col1_x + 50, y), "| 2 - λ      1    |", fill=LIGHT_GRAY, font=FONT_MATH_MED)
    y += 35
    draw.text((col1_x + 50, y), "|   1      2 - λ  |  =  0", fill=LIGHT_GRAY, font=FONT_MATH_MED)

    y += 75
    draw.text((col1_x + 30, y), "Step 4: Expand the 2×2 determinant", fill=GRAY_TEXT, font=FONT_SMALL)
    y += 30
    draw.text((col1_x + 50, y), "(2 - λ)(2 - λ) - (1)(1) = 0", fill=WHITE, font=FONT_MATH_MED)
    y += 40
    draw.text((col1_x + 50, y), "(4 - 4λ + λ²) - 1 = 0", fill=WHITE, font=FONT_MATH_MED)
    y += 40
    draw.text((col1_x + 50, y), "λ² - 4λ + 3 = 0", fill=CORAL, font=FONT_MATH_MED)

    y += 75
    draw.text((col1_x + 30, y), "Step 5: Factor to solve for eigenvalues", fill=GRAY_TEXT, font=FONT_SMALL)
    y += 30
    draw.text((col1_x + 50, y), "(λ - 3)(λ - 1) = 0", fill=WHITE, font=FONT_MATH_MED)
    y += 45
    draw.rounded_rectangle([col1_x + 40, y, col1_x + col1_w - 40, y + 65], radius=8, fill="#1c3328", outline=GREEN, width=2)
    draw.text((col1_x + 60, y + 15), "EIGENVALUES:   λ1 = 3,    λ2 = 1", fill=GREEN, font=FONT_HEADING)

    # Column 2: Finding Eigenvectors via Nullspace
    draw.rounded_rectangle([col2_x, 100, col2_x + col2_w, 980], radius=14, fill=PANEL_BG, outline=BORDER_COLOR, width=1)
    draw.rectangle([col2_x, 100, col2_x + col2_w, 160], fill="#1c2433")
    draw.text((col2_x + 30, 118), "PART 2: COMPUTING EIGENVECTORS", fill=GOLD, font=FONT_CARD_TITLE)

    y2 = 190
    draw.text((col2_x + 30, y2), "For λ1 = 3: Solve (A - 3 I) v = 0", fill=GOLD, font=FONT_CARD_TITLE)
    y2 += 40
    draw.text((col2_x + 50, y2), "[ [2-3, 1], [1, 2-3] ] [x, y]^T = [0, 0]^T", fill=LIGHT_GRAY, font=FONT_BODY)
    y2 += 40
    draw.text((col2_x + 50, y2), "[ [-1, 1], [1, -1] ] [x, y]^T = [0, 0]^T", fill=WHITE, font=FONT_MATH_MED)
    y2 += 45
    draw.text((col2_x + 50, y2), "Row equation: -x + y = 0  ==>  y = x", fill=WHITE, font=FONT_BODY)
    y2 += 40
    draw.rounded_rectangle([col2_x + 40, y2, col2_x + col2_w - 40, y2 + 65], radius=8, fill="#382e16", outline=GOLD, width=2)
    draw.text((col2_x + 60, y2 + 15), "EIGENVECTOR 1:   v1 = [ 1, 1 ]^T", fill=GOLD, font=FONT_HEADING)

    y2 += 120
    draw.text((col2_x + 30, y2), "For λ2 = 1: Solve (A - 1 I) v = 0", fill=CYAN, font=FONT_CARD_TITLE)
    y2 += 40
    draw.text((col2_x + 50, y2), "[ [2-1, 1], [1, 2-1] ] [x, y]^T = [0, 0]^T", fill=LIGHT_GRAY, font=FONT_BODY)
    y2 += 40
    draw.text((col2_x + 50, y2), "[ [1, 1], [1, 1] ] [x, y]^T = [0, 0]^T", fill=WHITE, font=FONT_MATH_MED)
    y2 += 45
    draw.text((col2_x + 50, y2), "Row equation: x + y = 0  ==>  y = -x", fill=WHITE, font=FONT_BODY)
    y2 += 40
    draw.rounded_rectangle([col2_x + 40, y2, col2_x + col2_w - 40, y2 + 65], radius=8, fill="#122938", outline=CYAN, width=2)
    draw.text((col2_x + 60, y2 + 15), "EIGENVECTOR 2:   v2 = [ -1, 1 ]^T", fill=CYAN, font=FONT_HEADING)

    y2 += 115
    draw.rounded_rectangle([col2_x + 40, y2, col2_x + col2_w - 40, y2 + 90], radius=8, fill="#1c2b22", outline=GREEN, width=1)
    draw.text((col2_x + 60, y2 + 15), "VERIFICATION: A v = λ v", fill=GREEN, font=FONT_CARD_TITLE)
    draw.text((col2_x + 60, y2 + 50), "A v1 = [3, 3] = 3 v1  [OK]  |  A v2 = [-1, 1] = 1 v2  [OK]", fill=WHITE, font=FONT_BODY)

    return im

def render_scene_5(frame_idx, total_frames, t_sec, total_sec):
    im = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(im)
    draw_top_bar(draw, 5, "Geometric Interpretation & Real-World Impact", frame_idx / total_frames)

    # Top Section: Decoupling and Repeated Matrix Powers
    draw.rounded_rectangle([80, 100, WIDTH - 80, 480], radius=14, fill=PANEL_BG, outline=BORDER_COLOR, width=1)
    draw.text((120, 130), "THE DECOUPLING POWER OF EIGENBASIS", fill=CYAN, font=FONT_CARD_TITLE)
    
    draw.text((120, 180), "1. Any vector x decomposes uniquely into the eigenbasis:", fill=LIGHT_GRAY, font=FONT_BODY)
    draw.text((160, 220), "x  =  c1 v1  +  c2 v2", fill=GOLD, font=FONT_MATH_LARGE)

    draw.text((120, 290), "2. Applying transformation A repeatedly k times avoids expensive matrix products:", fill=LIGHT_GRAY, font=FONT_BODY)
    draw.text((160, 335), "A^k x  =  c1 (λ1)^k v1  +  c2 (λ2)^k v2  =  c1 (3^k) v1  +  c2 (1^k) v2", fill=GREEN, font=FONT_MATH_LARGE)

    draw.text((120, 410), "3. Matrix Diagonalization:    A  =  P D P^(-1)    where D = diag(3, 1)", fill=WHITE, font=FONT_HEADING)

    # Bottom Section: 3 Real-World Applications
    app_y = 520
    app_w = (WIDTH - 80*2 - 40*2) // 3

    # App 1: Google PageRank
    a1_x = 80
    draw.rounded_rectangle([a1_x, app_y, a1_x + app_w, 980], radius=12, fill=PANEL_BG, outline=CYAN, width=2)
    draw.rectangle([a1_x, app_y, a1_x + app_w, app_y + 60], fill="#112d42")
    draw.text((a1_x + 20, app_y + 15), "1. Google PageRank", fill=CYAN, font=FONT_CARD_TITLE)
    draw.text((a1_x + 20, app_y + 85), "• The World Wide Web graph", fill=WHITE, font=FONT_BODY)
    draw.text((a1_x + 20, app_y + 125), "• Link probability matrix M", fill=LIGHT_GRAY, font=FONT_BODY)
    draw.text((a1_x + 20, app_y + 165), "• Stationary distribution is", fill=LIGHT_GRAY, font=FONT_BODY)
    draw.text((a1_x + 20, app_y + 195), "  dominant eigenvector (λ = 1)", fill=GOLD, font=FONT_BODY)
    draw.text((a1_x + 20, app_y + 245), "• Ranks billions of pages!", fill=GREEN, font=FONT_CARD_TITLE)

    # App 2: Structural Resonance
    a2_x = a1_x + app_w + 40
    draw.rounded_rectangle([a2_x, app_y, a2_x + app_w, 980], radius=12, fill=PANEL_BG, outline=CORAL, width=2)
    draw.rectangle([a2_x, app_y, a2_x + app_w, app_y + 60], fill="#3d181c")
    draw.text((a2_x + 20, app_y + 15), "2. Structural Resonance", fill=CORAL, font=FONT_CARD_TITLE)
    draw.text((a2_x + 20, app_y + 85), "• Bridges & skyscrapers", fill=WHITE, font=FONT_BODY)
    draw.text((a2_x + 20, app_y + 125), "• Mass & stiffness matrices M, K", fill=LIGHT_GRAY, font=FONT_BODY)
    draw.text((a2_x + 20, app_y + 165), "• Eigenvalues = Natural frequencies", fill=GOLD, font=FONT_BODY)
    draw.text((a2_x + 20, app_y + 205), "• Eigenvectors = Vibration shapes", fill=CYAN, font=FONT_BODY)
    draw.text((a2_x + 20, app_y + 250), "• Prevents catastrophic collapse!", fill=CORAL, font=FONT_CARD_TITLE)

    # App 3: Principal Component Analysis (PCA)
    a3_x = a2_x + app_w + 40
    draw.rounded_rectangle([a3_x, app_y, a3_x + app_w, 980], radius=12, fill=PANEL_BG, outline=GOLD, width=2)
    draw.rectangle([a3_x, app_y, a3_x + app_w, app_y + 60], fill="#3d3314")
    draw.text((a3_x + 20, app_y + 15), "3. Machine Learning (PCA)", fill=GOLD, font=FONT_CARD_TITLE)
    draw.text((a3_x + 20, app_y + 85), "• High-dimensional big data", fill=WHITE, font=FONT_BODY)
    draw.text((a3_x + 20, app_y + 125), "• Data covariance matrix Σ", fill=LIGHT_GRAY, font=FONT_BODY)
    draw.text((a3_x + 20, app_y + 165), "• Eigenvectors give principal axes", fill=GOLD, font=FONT_BODY)
    draw.text((a3_x + 20, app_y + 195), "  of maximum variance", fill=LIGHT_GRAY, font=FONT_BODY)
    draw.text((a3_x + 20, app_y + 245), "• Compresses data with minimal loss", fill=GREEN, font=FONT_CARD_TITLE)

    return im

def render_scene_6(frame_idx, total_frames, t_sec, total_sec):
    im = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(im)
    draw_top_bar(draw, 6, "Summary & Submission Credits", frame_idx / total_frames)

    # 3 Core Takeaway Cards
    draw.rounded_rectangle([120, 110, WIDTH - 120, 490], radius=14, fill=PANEL_BG, outline=GOLD, width=2)
    draw.text((160, 135), "THREE CORE MATHEMATICAL TAKEAWAYS", fill=GOLD, font=FONT_CARD_TITLE)

    # Takeaway 1
    draw.text((160, 185), "1. Directional Invariance:", fill=CYAN, font=FONT_HEADING)
    draw.text((540, 188), "Eigenvectors NEVER rotate under transformation A. They only stretch, shrink, or flip:  A v = λ v", fill=WHITE, font=FONT_BODY)

    # Takeaway 2
    draw.text((160, 275), "2. Characteristic Equation:", fill=CORAL, font=FONT_HEADING)
    draw.text((540, 278), "Eigenvalues are roots of  det(A - λ I) = 0, enforcing linear dependence for non-trivial nullspaces.", fill=WHITE, font=FONT_BODY)

    # Takeaway 3
    draw.text((160, 365), "3. Decoupling & Diagonalization:", fill=GREEN, font=FONT_HEADING)
    draw.text((540, 368), "Eigenbasis transforms coupled matrix systems into independent 1D scalings:  A = P D P^(-1)", fill=WHITE, font=FONT_BODY)

    # Closing Frame & Official Submission Credits
    cred_y = 530
    draw.rounded_rectangle([120, cred_y, WIDTH - 120, 990], radius=14, fill=PANEL_BG, outline=BORDER_COLOR, width=1)
    draw.text((160, cred_y + 25), "INTERNAL ASSESSMENT SUBMISSION DETAILS", fill=CYAN, font=FONT_CARD_TITLE)

    draw.text((160, cred_y + 80), "Course: Linear Algebra and Calculus (M3)", fill=WHITE, font=FONT_HEADING)
    draw.text((160, cred_y + 125), "Topic: Eigenvalues and Eigenvectors: Invariant Directions", fill=GOLD, font=FONT_BODY)
    draw.text((160, cred_y + 160), "Student Author: Jiya", fill=WHITE, font=FONT_BODY)

    draw.line([(160, cred_y + 210), (WIDTH - 160, cred_y + 210)], fill=BORDER_COLOR, width=1)

    draw.text((160, cred_y + 230), "Animation & Visual Engine: Custom Python 1080p Anti-Aliased Engine + Manim Scripts", fill=LIGHT_GRAY, font=FONT_BODY)
    draw.text((160, cred_y + 270), "Audio & Narration: High-Fidelity Speech Engine + Royalty-Free Ambient Pad Synthesizer", fill=LIGHT_GRAY, font=FONT_BODY)
    draw.text((160, cred_y + 310), "AI Tool Disclosure: Gemini Assistant utilized for code architecture & scene timing optimization", fill=CORAL, font=FONT_BODY)
    draw.text((160, cred_y + 360), "Thank you for watching! All code and storyboards available in the public repository.", fill=GREEN, font=FONT_CARD_TITLE)

    return im

SCENE_RENDERERS = [
    (1, "Hook & Context", "scene_1_hook.wav", render_scene_1),
    (2, "Concept Introduction", "scene_2_concept_introduction.wav", render_scene_2),
    (3, "Visual Intuition", "scene_3_visual_intuition.wav", render_scene_3),
    (4, "Worked Example", "scene_4_worked_example.wav", render_scene_4),
    (5, "Interpretation & Applications", "scene_5_interpretation.wav", render_scene_5),
    (6, "Summary & Credits", "scene_6_summary_credits.wav", render_scene_6),
]

def main():
    print("=" * 60)
    print("STARTING 1080p ANIMATION VIDEO RENDERING PIPELINE")
    print("=" * 60)

    # 1. Inspect audio files and durations
    scene_durations = []
    total_video_duration = 0.0
    audio_wav_paths = []

    for s_num, s_title, s_wav, _ in SCENE_RENDERERS:
        wav_path = os.path.join(AUDIO_DIR, s_wav)
        if not os.path.exists(wav_path):
            raise FileNotFoundError(f"Audio file missing: {wav_path}")
        dur = get_audio_duration(wav_path)
        scene_durations.append(dur)
        total_video_duration += dur
        audio_wav_paths.append(wav_path)
        print(f"Scene {s_num}: {s_title} -> {dur:.2f}s ({dur/60:.2f} min)")

    print(f"\nTotal video duration: {total_video_duration:.2f}s ({total_video_duration/60:.2f} min)")

    # 2. Concat narration audio files
    concat_list_path = os.path.join(AUDIO_DIR, "audio_concat_list.txt")
    with open(concat_list_path, "w") as f:
        for p in audio_wav_paths:
            f.write(f"file '{p}'\n")

    full_voice_wav = os.path.join(AUDIO_DIR, "full_voice.wav")
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", concat_list_path, "-c", "copy", full_voice_wav
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # 3. Mix narration voice with background music track
    bgm_wav = os.path.join(AUDIO_DIR, "ambient_bgm.wav")
    final_audio_wav = os.path.join(AUDIO_DIR, "final_soundtrack.wav")

    # Audio filter: voice at 1.0 volume, BGM at low subtle volume (-22dB, approx 0.08), mixed together
    subprocess.run([
        "ffmpeg", "-y",
        "-i", full_voice_wav,
        "-i", bgm_wav,
        "-filter_complex",
        "[1:a]volume=0.18[bgm];[0:a][bgm]amix=inputs=2:duration=first:dropout_transition=3[aout]",
        "-map", "[aout]",
        "-ar", "44100", "-ac", "2",
        final_audio_wav
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print(f"Final mixed audio track created at: {final_audio_wav}")

    # 4. Stream video frames directly into FFmpeg stdin
    print("\nRendering frames and encoding MP4 via FFmpeg pipe...")
    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{WIDTH}x{HEIGHT}",
        "-pix_fmt", "rgb24",
        "-r", str(FPS),
        "-i", "-", # stdin video
        "-i", final_audio_wav, # audio
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "19",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        OUTPUT_MP4
    ]

    proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    total_frames_rendered = 0
    for idx, (s_num, s_title, _, renderer) in enumerate(SCENE_RENDERERS):
        dur = scene_durations[idx]
        n_frames = int(round(dur * FPS))
        print(f"Rendering Scene {s_num}/6 ({n_frames} frames)...", end="", flush=True)

        for f in range(n_frames):
            t_sec = f / float(FPS)
            frame_img = renderer(f, n_frames, t_sec, dur)
            proc.stdin.write(frame_img.tobytes())
            total_frames_rendered += 1

        print(" Done!")

    proc.stdin.close()
    proc.wait()

    print("\n" + "=" * 60)
    print(f"SUCCESSFULLY RENDERED FINAL VIDEO:")
    print(f"Path: {OUTPUT_MP4}")
    file_size_mb = os.path.getsize(OUTPUT_MP4) / (1024 * 1024)
    print(f"Size: {file_size_mb:.2f} MB")
    print(f"Total Frames: {total_frames_rendered} @ {FPS} FPS")
    print(f"Duration: {total_frames_rendered / FPS:.2f} seconds ({total_frames_rendered / (FPS * 60):.2f} minutes)")
    print("=" * 60)

if __name__ == "__main__":
    main()
