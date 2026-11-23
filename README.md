# Linear Algebra & Calculus (M3) — Internal Assessment (10%)
## Project Option 1: Mathematical Animation Video

[![Subject](https://img.shields.io/badge/Course-Linear%20Algebra%20%26%20Calculus%20(M3)-blue.svg)](#)
[![Topic](https://img.shields.io/badge/Topic-Eigenvalues%20%26%20Eigenvectors-gold.svg)](#)
[![Video Duration](https://img.shields.io/badge/Duration-5%3A14%20min%20(Target%205%20min)-success.svg)](#)
[![Resolution](https://img.shields.io/badge/Resolution-1080p%20(1920x1080)%2016%3A9-blueviolet.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](#)

> **Official Submission Deadline:** 25th November  
> **Repository Visibility:** Public  
> **Student Author:** Jiya  
> **Student ID / Roll No:** `[Enter Your Student ID Here]`  

---

## 📽️ Project Overview & Central Guiding Question

When we apply a linear transformation matrix $A$ to the two-dimensional Cartesian plane, the entire space deforms: coordinate grid lines tilt, unit squares stretch into parallelograms, and almost every vector rotates and gets knocked off its original span.

### The Central Question:
> **"Do *all* vectors rotate when space transforms? Or do special, invariant directions exist that stubbornly refuse to turn, changing only in scale?"**

This video teaches the concept of **Eigenvalues and Eigenvectors** from first principles, connecting the geometric intuition of invariant lines with the rigorous algebraic solution of the characteristic equation $\det(A - \lambda I) = 0$.

---

## 🎬 Video Specifications & Deliverables Checklist

| Requirement | Specification | Status |
|:---|:---|:---:|
| **Final Video File** | `_Video.mp4` in root directory | ✅ Complete |
| **Duration** | **5 minutes 14 seconds** (Strictly within 5 min target / 7 min max) | ✅ Complete |
| **Resolution & Format** | 1080p Full HD (1920×1080), 16:9 Landscape, 24 FPS, MP4 (H.264 / AAC) | ✅ Complete |
| **Audio & Narration** | Clear voice-over narration + subtle ambient background music (-22 dB) | ✅ Complete |
| **Opening Frame** | Title, Concept, Student Name, Course Code | ✅ Complete |
| **Closing Frame** | 3 Core Takeaways, Academic References, Music Credits, AI Disclosure | ✅ Complete |
| **Storyboard** | 6-Scene Storyboard in Markdown & High-Res PDF (`Storyboard/`) | ✅ Complete |
| **Source Code** | Turnkey Python 1080p rendering pipeline + idiomatic Manim scripts | ✅ Complete |
| **Mathematical Proofs** | Step-by-step derivations & paper verification (`Documentation/`) | ✅ Complete |
| **Viva / Q&A Prep** | 10 comprehensive examiner questions & answers for viva voce | ✅ Complete |

---

## 📁 Repository Directory Structure

```text
.
├── _Video.mp4                        # Master 1080p 16:9 MP4 video (5:14 min)
├── README.md                         # Project documentation and submission hub
├── _Code/
│   ├── render_video.py               # Complete 1080p anti-aliased video renderer
│   ├── eigenvalues_manim.py          # Idiomatic Manim Community Edition script
│   ├── generate_audio.py             # Scene-by-scene voice narration generator
│   ├── generate_bgm.py               # Ambient harmonic synthesizer script
│   └── requirements.txt              # Python package dependencies
├── Storyboard/
│   ├── Storyboard.pdf                # Submission-ready multi-page Storyboard PDF
│   ├── Storyboard.md                 # Complete 6-scene storyboard table & transcripts
│   └── generate_storyboard_pdf.py    # Python script to regenerate the PDF
└── Documentation/
    ├── Mathematical_Derivation_and_Verification.md   # Step-by-step proofs & checks
    ├── Viva_QnA_Preparation.md                       # Comprehensive oral exam guide
    └── AI_Disclosure_and_Credits.md                  # Policy compliance & disclosures
```

---

## 📐 Mathematical Core & Worked Example

The video explores the symmetric transformation matrix:

$$A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$$

### 1. The Fundamental Identity
$$A\vec{v} = \lambda\vec{v} \iff (A - \lambda I)\vec{v} = \mathbf{0}$$

### 2. Characteristic Determinant
For non-trivial solutions ($\vec{v} \neq \mathbf{0}$):
$$\det(A - \lambda I) = 0$$
$$\det\begin{pmatrix} 2 - \lambda & 1 \\ 1 & 2 - \lambda \end{pmatrix} = (2 - \lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = 0$$

Factoring gives the eigenvalues:
$$\mathbf{\lambda_1 = 3}, \quad \mathbf{\lambda_2 = 1}$$

### 3. Calculating Eigenspaces
- **For $\lambda_1 = 3$:**
  $$\begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies y = x \implies \mathbf{\vec{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}}$$
  *(Stretches $3\times$ along $y = x$ without rotating)*

- **For $\lambda_2 = 1$:**
  $$\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies y = -x \implies \mathbf{\vec{v}_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix}}$$
  *(Completely stationary: length and direction are 100% preserved)*

### 4. Direct Verification Check
$$A\vec{v}_1 = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 3 \\ 3 \end{pmatrix} = 3 \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \lambda_1 \vec{v}_1 \quad \checkmark$$
$$A\vec{v}_2 = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} -1 \\ 1 \end{pmatrix} = \begin{pmatrix} -1 \\ 1 \end{pmatrix} = 1 \begin{pmatrix} -1 \\ 1 \end{pmatrix} = \lambda_2 \vec{v}_2 \quad \checkmark$$
$$\vec{v}_1 \cdot \vec{v}_2 = (1)(-1) + (1)(1) = 0 \quad (\text{Orthogonal eigen-axes}) \quad \checkmark$$

---

## 🎞️ The 6-Scene Storyboard Summary

1. **Scene 1: Hook / Context (~40s)**  
   *Visual:* Coordinate grid warping as space deforms; radial vector fan rotating across quadrants.  
   *Question:* Do all vectors rotate, or do invariant axes exist?
2. **Scene 2: Concept Introduction (~47s)**  
   *Visual:* Color-coded reveal of $A\vec{v} = \lambda\vec{v}$ with term-by-term breakdown.  
   *Key Point:* Why $\vec{v} \neq \mathbf{0}$ is mandatory (triviality avoidance).
3. **Scene 3: Visual Intuition (~64s)**  
   *Visual:* Generic basis vector $[1, 0]^T$ visibly rotating $26.57^\circ$ vs Eigenvectors $[1, 1]^T$ and $[-1, 1]^T$ staying strictly on their lines.
4. **Scene 4: Step-by-Step Worked Example (~80s)**  
   *Visual:* Blackboard derivation of characteristic polynomial $\lambda^2 - 4\lambda + 3 = 0$, factoring, and solving homogeneous systems for eigenspaces.
5. **Scene 5: Geometric Interpretation & Applications (~50s)**  
   *Visual:* Vector decomposition $\vec{x} = c_1\vec{v}_1 + c_2\vec{v}_2$, repeated matrix powers $A^k\vec{x} = c_1(3^k)\vec{v}_1 + c_2(1^k)\vec{v}_2$, Google PageRank, structural vibrations, and machine learning PCA.
6. **Scene 6: Summary & Credits (~34s)**  
   *Visual:* 3 Core takeaways glowing on screen, followed by official student submission card, music credits, and AI disclosure.

---

## 🚀 How to Run and Re-Render

### Prerequisites
- Python 3.9+
- FFmpeg installed (`brew install ffmpeg`)
- Python packages: `pip install -r _Code/requirements.txt`

### Step 1: Generate Scene Voice Narration
```bash
python3 _Code/generate_audio.py
```

### Step 2: Synthesize Background Music
```bash
python3 _Code/generate_bgm.py
```

### Step 3: Render Final 1080p MP4 Video
```bash
python3 _Code/render_video.py
```
*(Produces the final `_Video.mp4` in root).*

### Step 4: Regenerate Storyboard PDF (Optional)
```bash
python3 Storyboard/generate_storyboard_pdf.py
```

---

## 📝 Submission Instructions for Evaluation

1. Ensure this GitHub repository visibility is set to **Public**.
2. To test visibility, open the GitHub URL in an **Incognito / Private Window**.
3. Verify that `_Video.mp4`, `_Code/`, `Storyboard/`, and `Documentation/` are visible and accessible.
4. Copy the public repository URL and paste it into the official M3 Google Submission Form once released.
