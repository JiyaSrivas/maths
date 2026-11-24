# Mathematical Derivation and Verification

**Course**: Linear Algebra and Calculus (M3)  
**Topic**: Eigenvalues and Eigenvectors: Invariant Directions of Linear Transformations  
**Author**: Jiya  

---

## 1. Executive Summary & Core Definition

In linear algebra, a square matrix $A \in \mathbb{R}^{n \times n}$ acts as a linear map from $\mathbb{R}^n$ to $\mathbb{R}^n$:
$$\vec{x} \mapsto A\vec{x}$$

Geometrically, most non-zero vectors in $\mathbb{R}^n$ change both their **length** and their **spatial direction** (angle) when transformed by $A$. 

However, there exist special non-zero vectors $\vec{v} \in \mathbb{R}^n \setminus \{\mathbf{0}\}$ that do **not** rotate; they remain pinned to their original one-dimensional span (the line passing through the origin and $\vec{v}$). When $A$ operates on such a vector, the result is merely a scaled copy of the original vector:

$$A\vec{v} = \lambda\vec{v}$$

- $\vec{v}$ is called an **eigenvector** (from German *eigen*, meaning "own", "peculiar", or "characteristic").
- $\lambda \in \mathbb{R}$ (or $\mathbb{C}$) is the corresponding **eigenvalue**, representing the scalar factor by which $\vec{v}$ is stretched, shrunk, or flipped.

---

## 2. Theoretical Derivation: The Characteristic Equation

To determine the eigenpairs $(\lambda, \vec{v})$, we convert the visual condition into an algebraic nullspace problem:

$$A\vec{v} = \lambda\vec{v}$$

Since $\lambda$ is a scalar, we introduce the identity matrix $I_n$:
$$\lambda\vec{v} = \lambda (I_n \vec{v}) = (\lambda I_n)\vec{v}$$

Rearranging to one side:
$$A\vec{v} - (\lambda I_n)\vec{v} = \mathbf{0}$$
$$(A - \lambda I_n)\vec{v} = \mathbf{0}$$

### The Non-Triviality Condition
Equation $(A - \lambda I_n)\vec{v} = \mathbf{0}$ is a homogeneous linear system.
- If the matrix $(A - \lambda I_n)$ is invertible, multiplying both sides by $(A - \lambda I_n)^{-1}$ yields:
  $$\vec{v} = (A - \lambda I_n)^{-1} \mathbf{0} = \mathbf{0}$$
- But by definition, an eigenvector must be non-zero ($\vec{v} \neq \mathbf{0}$).
- Therefore, a non-zero solution $\vec{v}$ exists if and only if the matrix $(A - \lambda I_n)$ is **singular** (non-invertible).
- A square matrix is singular if and only if its determinant is zero:

$$\det(A - \lambda I_n) = 0$$

This scalar polynomial equation in $\lambda$ of degree $n$ is known as the **characteristic equation** of $A$. Its roots are the eigenvalues of $A$.

---

## 3. Step-by-Step Worked Example (Used in Video)

For our 5-minute animated exposition, we select a symmetric $2 \times 2$ matrix with clean integer eigenvalues and orthogonal invariant axes:

$$A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$$

### Step 3.1: Form the Characteristic Matrix
$$A - \lambda I_2 = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} - \begin{pmatrix} \lambda & 0 \\ 0 & \lambda \end{pmatrix} = \begin{pmatrix} 2 - \lambda & 1 \\ 1 & 2 - \lambda \end{pmatrix}$$

### Step 3.2: Compute the Determinant
$$\det(A - \lambda I_2) = (2 - \lambda)(2 - \lambda) - (1)(1)$$
$$\det(A - \lambda I_2) = (4 - 4\lambda + \lambda^2) - 1$$
$$p(\lambda) = \lambda^2 - 4\lambda + 3 = 0$$

### Step 3.3: Solve for Eigenvalues
Factoring the quadratic polynomial:
$$(\lambda - 3)(\lambda - 1) = 0$$

Roots:
$$\lambda_1 = 3, \quad \lambda_2 = 1$$

Both eigenvalues are real, distinct, and positive.

---

## 4. Eigenvector Calculations & Eigenspace Determinations

### Case 1: First Eigenvalue $\lambda_1 = 3$
Substitute $\lambda_1 = 3$ into $(A - \lambda I)\vec{v} = \mathbf{0}$:
$$\begin{pmatrix} 2 - 3 & 1 \\ 1 & 2 - 3 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$
$$\begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$

This yields the system of equations:
$$-x + y = 0$$
$$x - y = 0$$

Both rows are linearly dependent (multiples of each other).
Thus:
$$y = x$$

Choosing free variable $x = 1$, we obtain the basis eigenvector:
$$\vec{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$

**Eigenspace $E_{\lambda=3}$**:
$$E_3 = \text{span}\left\{ \begin{pmatrix} 1 \\ 1 \end{pmatrix} \right\} = \left\{ c \begin{pmatrix} 1 \\ 1 \end{pmatrix} \,\middle|\, c \in \mathbb{R} \right\}$$
Geometrically, this is the $45^\circ$ diagonal line $y = x$. Every vector along this line expands by a factor of $3$ without tilting.

---

### Case 2: Second Eigenvalue $\lambda_2 = 1$
Substitute $\lambda_2 = 1$ into $(A - \lambda I)\vec{v} = \mathbf{0}$:
$$\begin{pmatrix} 2 - 1 & 1 \\ 1 & 2 - 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$
$$\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$

This yields the system of equations:
$$x + y = 0$$
$$y = -x$$

Choosing free variable $x = -1$, we obtain the basis eigenvector:
$$\vec{v}_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$$

**Eigenspace $E_{\lambda=1}$**:
$$E_1 = \text{span}\left\{ \begin{pmatrix} -1 \\ 1 \end{pmatrix} \right\} = \left\{ c \begin{pmatrix} -1 \\ 1 \end{pmatrix} \,\middle|\, c \in \mathbb{R} \right\}$$
Geometrically, this is the line $y = -x$. Every vector along this line has eigenvalue $1$, meaning its length and orientation remain **completely unchanged** under the transformation!

---

## 5. Verification & Consistency Checks

### Direct Multiplication Verification:
1. **Testing $\vec{v}_1$ with $\lambda_1 = 3$**:
   $$A\vec{v}_1 = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 2(1) + 1(1) \\ 1(1) + 2(1) \end{pmatrix} = \begin{pmatrix} 3 \\ 3 \end{pmatrix} = 3 \begin{pmatrix} 1 \\ 1 \end{pmatrix} = \lambda_1 \vec{v}_1 \quad \checkmark$$

2. **Testing $\vec{v}_2$ with $\lambda_2 = 1$**:
   $$A\vec{v}_2 = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} -1 \\ 1 \end{pmatrix} = \begin{pmatrix} 2(-1) + 1(1) \\ 1(-1) + 2(1) \end{pmatrix} = \begin{pmatrix} -1 \\ 1 \end{pmatrix} = 1 \begin{pmatrix} -1 \\ 1 \end{pmatrix} = \lambda_2 \vec{v}_2 \quad \checkmark$$

3. **Trace and Determinant Invariants**:
   - $\text{Trace}(A) = 2 + 2 = 4$
     $\lambda_1 + \lambda_2 = 3 + 1 = 4 = \text{Trace}(A) \quad \checkmark$
   - $\det(A) = 2(2) - 1(1) = 3$
     $\lambda_1 \cdot \lambda_2 = 3 \cdot 1 = 3 = \det(A) \quad \checkmark$

4. **Orthogonality of Eigenvectors (Spectral Theorem)**:
   Because $A = A^T$ is symmetric, its eigenvectors corresponding to distinct eigenvalues must be orthogonal:
   $$\vec{v}_1 \cdot \vec{v}_2 = (1)(-1) + (1)(1) = -1 + 1 = 0 \quad \checkmark$$

5. **Comparison with a Generic Vector**:
   Let $\vec{u} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ (standard basis vector $\hat{i}$).
   $$A\vec{u} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} 2 \\ 1 \end{pmatrix}$$
   Notice that $\begin{pmatrix} 2 \\ 1 \end{pmatrix} \neq c \begin{pmatrix} 1 \\ 0 \end{pmatrix}$ for any scalar $c$. The angle has rotated from $0^\circ$ to $\arctan(1/2) \approx 26.57^\circ$. This clearly illustrates the contrast between arbitrary vectors and invariant eigenvectors.

---

## 6. Geometric Decoupling and Matrix Diagonalization

Since $\vec{v}_1$ and $\vec{v}_2$ are linearly independent, they form an eigenbasis for $\mathbb{R}^2$. Any arbitrary vector $\vec{x} \in \mathbb{R}^2$ can be expressed uniquely as:
$$\vec{x} = c_1 \vec{v}_1 + c_2 \vec{v}_2$$

Applying the linear transformation $A$ to $\vec{x}$:
$$A\vec{x} = A(c_1 \vec{v}_1 + c_2 \vec{v}_2) = c_1 A\vec{v}_1 + c_2 A\vec{v}_2 = c_1 \lambda_1 \vec{v}_1 + c_2 \lambda_2 \vec{v}_2$$

For repeated transformations $A^k$:
$$A^k \vec{x} = c_1 (\lambda_1)^k \vec{v}_1 + c_2 (\lambda_2)^k \vec{v}_2$$

In matrix form, defining modal matrix $P$ and diagonal eigenvalue matrix $D$:
$$P = \begin{pmatrix} \vec{v}_1 & \vec{v}_2 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}, \quad D = \begin{pmatrix} 3 & 0 \\ 0 & 1 \end{pmatrix}$$
$$A = P D P^{-1}$$

This turns coupled, complicated matrix operations into elementary parallel scalar multiplications, forming the mathematical backbone of differential equations, vibration modes, quantum mechanics, and machine learning.
