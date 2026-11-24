# 6-Scene Storyboard Document

**Project**: M3 Internal Assessment — Animation Video  
**Topic**: Eigenvalues & Eigenvectors: Invariant Directions of Linear Transformations  
**Author**: Jiya | Course: Linear Algebra & Calculus (M3)  
**Target Duration**: ~5 Minutes (300 seconds) | Resolution: 1080p (1920×1080, 16:9)  

---

## Scene-by-Scene Storyboard Overview

| Scene # | Scene Title | Duration | Pedagogical Purpose | Core Math & Visual Focus |
|:---:|:---|:---:|:---|:---|
| **1** | Hook / Context | ~45s | Spark curiosity & motivate topic | Grid deformation, rotating vectors, search for invariant lines |
| **2** | Concept Introduction | ~45s | Formal definition & learning objective | $A\vec{v} = \lambda\vec{v}$, scaling vs rotation, $\vec{v} \neq \mathbf{0}$ |
| **3** | Visual Intuition | ~60s | Geometric contrast: generic vs invariant | Generic $\vec{u}$ rotating vs Eigenvectors $\vec{v}_1, \vec{v}_2$ stretching |
| **4** | Worked Example | ~75s | Rigorous step-by-step calculation | Matrix $A$, characteristic eq $\det(A - \lambda I) = 0$, finding $\lambda$ and $\vec{v}$ |
| **5** | Geometric Interpretation | ~50s | Connect algebra back to geometry | Vector decomposition, decoupled powers $A^k\vec{x}$, real-world impact |
| **6** | Summary & Credits | ~30s | Review 3 takeaways & formal credits | 3 core takeaways, references, AI disclosure, closing card |

---

## Detailed Scene Breakdown

### Scene 1: Hook / Context (0:00 - 0:45)
- **Visuals**:
  - Clean title card fades in: "LINEAR ALGEBRA & CALCULUS (M3)", "Eigenvalues & Eigenvectors: Invariant Directions", "Author: Jiya".
  - A bright Cartesian coordinate grid appears with multiple vectors radiating outwards.
  - As a matrix transformation acts on the space, the grid warps, squares become parallelograms, and almost every vector visibly rotates away from its original trajectory.
  - Pulsing highlight: But do *all* vectors rotate? Or are there special directions that stubbornly refuse to turn?
- **Narration Script**:
  > "Welcome to Linear Algebra. Imagine the two-dimensional plane as a flexible rubber sheet. When we apply a linear transformation matrix, the entire plane warps. Grid lines tilt, squares turn into parallelograms, and almost every vector rotates and gets knocked off its original span. But here is the central mystery: does *every* vector turn? Or are there special, invariant directions that stubbornly refuse to rotate, changing only in scale? In this video, we will discover eigenvalues and eigenvectors—the hidden geometric axes that define how matrices transform our world."
- **Key Equations & Notation**:
  - $T: \mathbb{R}^2 \to \mathbb{R}^2$
  - $\vec{x} \mapsto A\vec{x}$

---

### Scene 2: Concept Introduction (0:45 - 1:30)
- **Visuals**:
  - Clean card displaying the central equation: $A\vec{v} = \lambda\vec{v}$.
  - Color coding introduced: Matrix $A$ in cyan, Vector $\vec{v}$ in vibrant gold/yellow, Scalar $\lambda$ in energetic magenta.
  - Side-by-side comparison:
    - Left: Matrix-vector multiplication $A \times \vec{v}$ (multivariate operation).
    - Right: Scalar-vector multiplication $\lambda \times \vec{v}$ (simple 1D stretching/shrinking).
  - Callout box emphasizing why $\vec{v} \neq \mathbf{0}$.
- **Narration Script**:
  > "Let's state the formal definition. Given an n by n square matrix A, a non-zero vector v is an eigenvector if multiplying A by v yields a scalar multiple of v. That is, A times v equals lambda times v. The scalar lambda is called the eigenvalue. Notice the incredible power of this equation: on the left, A times v represents a complicated multi-dimensional transformation. But on the right, it simplifies into pure scalar multiplication—just stretching, shrinking, or reversing the vector along its existing line. We strictly require v to be non-zero, because the zero vector satisfies this trivially for every number. By the end of this video, you will be able to find these invariant directions geometrically and algebraically."
- **Key Equations & Notation**:
  - $A\vec{v} = \lambda\vec{v}, \quad \vec{v} \neq \mathbf{0}$
  - $\lambda \in \mathbb{R}$ (Eigenvalue)
  - $\vec{v} \in \mathbb{R}^n$ (Eigenvector)

---

### Scene 3: Visual Intuition (1:30 - 2:30)
- **Visuals**:
  - High-contrast 2D coordinate plane with transformation matrix $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.
  - Test Case 1 (Generic Vector): Standard basis vector $\vec{u} = [1, 0]^T$ (green). Under transformation, it maps to $[2, 1]^T$. A curved arc shows the angle change ($0^\circ \to 26.57^\circ$). It clearly rotated!
  - Test Case 2 (First Invariant Direction): Vector $\vec{v}_1 = [1, 1]^T$ on the dashed line $y = x$ (gold). As the grid deforms, $\vec{v}_1$ stretches smoothly to $[3, 3]^T$. It stays exactly on the dashed line! It scaled by exactly $\lambda_1 = 3$.
  - Test Case 3 (Second Invariant Direction): Vector $\vec{v}_2 = [-1, 1]^T$ on the dashed line $y = -x$ (cyan). Under transformation, it maps to $[-1, 1]^T$. It does not move or stretch at all ($\lambda_2 = 1$).
- **Narration Script**:
  > "To see this in action, let us observe the symmetric matrix with rows [2, 1] and [1, 2]. First, consider a standard unit vector along the x-axis, [1, 0]. When transformed, it maps to [2, 1]. Its line of action has clearly rotated by over twenty-six degrees. It is not an eigenvector. Now, look at a vector pointing at forty-five degrees, [1, 1]. As the grid transforms, watch closely: this vector never turns. It remains locked onto the line y equals x, stretching to three times its original length. Here, lambda equals three! Next, look at the perpendicular line, y equals minus x, with vector [-1, 1]. When transformed, it maps to [-1, 1]—unchanged in both length and direction. Its eigenvalue is one. These two invariant lines form the natural coordinate framework of the transformation."
- **Key Equations & Notation**:
  - $\vec{u} = \begin{pmatrix} 1 \\ 0 \end{pmatrix} \xrightarrow{A} \begin{pmatrix} 2 \\ 1 \end{pmatrix}$ (Rotates)
  - $\vec{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix} \xrightarrow{A} \begin{pmatrix} 3 \\ 3 \end{pmatrix} = 3\vec{v}_1$ ($\lambda_1 = 3$)
  - $\vec{v}_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix} \xrightarrow{A} \begin{pmatrix} -1 \\ 1 \end{pmatrix} = 1\vec{v}_2$ ($\lambda_2 = 1$)

---

### Scene 4: Step-by-Step Worked Example (2:30 - 3:45)
- **Visuals**:
  - Clean blackboard-style calculation view.
  - Step 1: $(A - \lambda I)\vec{v} = \mathbf{0}$.
  - Step 2: Determinant formula: $\det(A - \lambda I) = 0$.
  - Step 3: Expansion: $(2-\lambda)(2-\lambda) - 1 = \lambda^2 - 4\lambda + 3 = 0$.
  - Step 4: Factoring: $(\lambda - 3)(\lambda - 1) = 0 \implies \lambda_1 = 3, \lambda_2 = 1$.
  - Step 5: Eigenspace calculation for $\lambda = 3$:
    $$\begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies y = x \implies \vec{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$
  - Step 6: Eigenspace calculation for $\lambda = 1$:
    $$\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \implies y = -x \implies \vec{v}_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$$
  - Verification checkmark callouts for both eigenpairs.
- **Narration Script**:
  > "Now, how do we find these values mathematically without guessing? We start with A v equals lambda v. Subtracting lambda I v from both sides gives the system: (A minus lambda I) times v equals zero. For a non-zero vector v to satisfy this, the matrix (A minus lambda I) must have linearly dependent columns, meaning its determinant must be zero. Let us compute this for our matrix. The determinant of [2 minus lambda, 1; 1, 2 minus lambda] equals (2 minus lambda) squared minus one. Expanding gives lambda squared minus 4 lambda plus 3 equals zero. Factoring gives (lambda minus 3) times (lambda minus 1) equals zero, yielding our eigenvalues: lambda one equals 3, and lambda two equals 1. To find the eigenvectors, we substitute each eigenvalue back into our nullspace equation. For lambda equals 3, we get the equation minus x plus y equals zero, meaning y equals x, yielding the eigenvector [1, 1]. For lambda equals 1, we get x plus y equals zero, meaning y equals minus x, giving the eigenvector [-1, 1]. Both calculations perfectly match our visual observations!"
- **Key Equations & Notation**:
  - $(A - \lambda I)\vec{v} = \mathbf{0}$
  - $\det(A - \lambda I) = 0$
  - $\lambda^2 - 4\lambda + 3 = 0 \implies \lambda \in \{3, 1\}$
  - $E_3 = \text{span}\{[1, 1]^T\}, \quad E_1 = \text{span}\{[-1, 1]^T\}$

---

### Scene 5: Geometric Interpretation & Applications (3:45 - 4:35)
- **Visuals**:
  - Coordinate plane showing decomposition of an arbitrary vector into the two orthogonal eigenvectors:
    $\vec{x} = c_1 \vec{v}_1 + c_2 \vec{v}_2$.
  - Animation of applying $A$ repeatedly: $A^k \vec{x} = c_1 (3^k)\vec{v}_1 + c_2 (1^k)\vec{v}_2$. The component along $\vec{v}_1$ grows rapidly, dominating the space!
  - Real-world application cards:
    1. Google PageRank (Dominant eigenvector of web link transitions).
    2. Structural Engineering (Resonance modes of skyscrapers).
    3. Principal Component Analysis (Data compression and AI).
- **Narration Script**:
  > "What does this mean for mathematics and real-world engineering? Because our eigenvectors are linearly independent, any vector in the plane can be decomposed as a combination of these two invariant directions. When we multiply by A repeatedly, we do not need to perform painful matrix multiplications. We simply scale the first eigenvector by 3 to the power k, while the second component remains constant. This is matrix diagonalization: turning complex, coupled systems into independent, single-variable scalings. This single concept powers Google's PageRank algorithm to rank the internet, predicts vibrational frequencies to keep suspension bridges standing, and underpins Principal Component Analysis in modern machine learning."
- **Key Equations & Notation**:
  - $\vec{x} = c_1 \vec{v}_1 + c_2 \vec{v}_2$
  - $A^k\vec{x} = c_1 (\lambda_1)^k \vec{v}_1 + c_2 (\lambda_2)^k \vec{v}_2$
  - $A = P D P^{-1}$

---

### Scene 6: Summary, Takeaways & Credits (4:35 - 5:05)
- **Visuals**:
  - Three distinct takeaway summary boxes glow on screen.
  - Final credits frame:
    - Course: Linear Algebra and Calculus (M3)
    - Topic: Eigenvalues and Eigenvectors: Invariant Directions
    - Author: Jiya
    - Course: Linear Algebra and Calculus (M3)
    - Audio: High-Quality Narration & Royalty-Free Ambient Synthesizer Pad
    - AI Disclosure: Gemini AI assisted with code architecture and scene timing
- **Narration Script**:
  > "To summarize our three core takeaways: First, an eigenvector is a special direction that never rotates under a linear transformation, only scaling by lambda. Second, eigenvalues are found by setting the determinant of (A minus lambda I) to zero. And third, eigenvectors provide the natural coordinate basis that simplifies complex matrix operations into parallel scalings. Thank you for watching, and happy learning!"
- **Key Takeaways Displayed**:
  1. **Directional Invariance**: $A\vec{v} = \lambda\vec{v}$ (Vectors only scale, never rotate).
  2. **Characteristic Determinant**: $\det(A - \lambda I) = 0$ (Solves for invariant scaling factors).
  3. **Decoupling Power**: $A = PDP^{-1}$ (Transforms coupled systems into simple diagonal actions).
