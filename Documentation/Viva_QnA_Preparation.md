# Individual Viva / Q&A Preparation Guide

**Course**: Linear Algebra and Calculus (M3)  
**Topic**: Eigenvalues & Eigenvectors: Invariant Directions of Linear Transformations  
**Candidate**: Jiya  

This document serves as an exhaustive study guide to prepare for the oral examination (viva voce) following the animation video presentation.

---

## Table of Questions & Model Answers

### Question 1: What is the geometric definition of an eigenvector, and how does it differ from an algebraic definition?
**Answer**:
- **Geometric Definition**: An eigenvector of a linear transformation $T: V \to V$ is a non-zero vector whose direction remains invariant under $T$. The transformation acts on this vector solely by stretching, shrinking, or reversing it along the line it spans, without any rotation away from its 1D subspace.
- **Algebraic Definition**: An eigenvector is a non-zero vector $\vec{v} \in \mathbb{R}^n$ that satisfies $A\vec{v} = \lambda\vec{v}$ for some scalar $\lambda \in \mathbb{R}$ (or $\mathbb{C}$).

---

### Question 2: Why must an eigenvector be strictly non-zero ($\vec{v} \neq \mathbf{0}$)?
**Answer**:
If the zero vector were considered an eigenvector, the equation $A\mathbf{0} = \lambda\mathbf{0}$ would be true for **every scalar $\lambda \in \mathbb{C}$**, because $A\mathbf{0} = \mathbf{0}$ and $\lambda\mathbf{0} = \mathbf{0}$ always. This would make the eigenvalue $\lambda$ completely undefined and meaningless. Hence, we mandate $\vec{v} \neq \mathbf{0}$, while the eigenvalue $\lambda$ is allowed to be zero.

---

### Question 3: Can an eigenvalue be zero ($\lambda = 0$)? What does that signify geometrically and algebraically?
**Answer**:
Yes, $\lambda = 0$ is a valid eigenvalue.
- **Algebraically**: $A\vec{v} = 0\vec{v} = \mathbf{0}$. This means $\vec{v}$ belongs to the **null space** (or **kernel**) of $A$.
- **Determinant**: $\det(A) = \prod \lambda_i = 0$. Hence, the matrix $A$ is singular and non-invertible.
- **Geometrically**: The transformation collapses at least one dimension along the direction of $\vec{v}$ down to a single point at the origin.

---

### Question 4: How does $(A - \lambda I)\vec{v} = \mathbf{0}$ lead to $\det(A - \lambda I) = 0$?
**Answer**:
$(A - \lambda I)\vec{v} = \mathbf{0}$ is a homogeneous linear system. The fundamental theorem of linear algebra states that a homogeneous square linear system has non-trivial (non-zero) solutions if and only if the coefficient matrix has a non-trivial null space, which occurs if and only if its columns are linearly dependent, meaning the matrix is singular and its determinant is identically zero: $\det(A - \lambda I) = 0$.

---

### Question 5: Why did you choose the matrix $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$ for the animated worked example?
**Answer**:
This matrix was purposefully selected because:
1. It is **symmetric** ($A = A^T$), guaranteeing real eigenvalues and mutually orthogonal eigenvectors by the Real Spectral Theorem.
2. The arithmetic yields integer eigenvalues ($\lambda_1 = 3, \lambda_2 = 1$), eliminating distracting algebraic fractions and keeping the focus on geometric intuition.
3. The eigenvectors lie along the lines $y = x$ ($45^\circ$) and $y = -x$ ($135^\circ$), which are easily recognizable visually.
4. One eigenvalue is $\lambda_2 = 1$, which acts as an invariant stationary axis (lengths preserved), creating a dramatic visual comparison against $\lambda_1 = 3$ (stretched by $3\times$).

---

### Question 6: Can a real matrix have no real eigenvalues? Give a physical/geometric example.
**Answer**:
Yes. A 2D rotation matrix by angle $\theta$ (where $\theta \neq k\pi$):
$$R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$
Its characteristic equation is:
$$\lambda^2 - 2\lambda\cos\theta + 1 = 0 \implies \lambda = \cos\theta \pm i\sin\theta = e^{\pm i\theta}$$
Geometrically, every vector in $\mathbb{R}^2$ rotates by $\theta$, so no real vector remains on its original span. Its eigenvalues and eigenvectors are strictly complex.

---

### Question 7: What is the relationship between the trace and determinant of a matrix and its eigenvalues?
**Answer**:
For any $n \times n$ matrix $A$:
1. **Trace**: The sum of the eigenvalues equals the trace of the matrix:
   $$\sum_{i=1}^n \lambda_i = \text{tr}(A)$$
2. **Determinant**: The product of the eigenvalues equals the determinant of the matrix:
   $$\prod_{i=1}^n \lambda_i = \det(A)$$
For our matrix $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$:
- $\lambda_1 + \lambda_2 = 3 + 1 = 4 = 2 + 2 = \text{tr}(A)$
- $\lambda_1 \cdot \lambda_2 = 3 \cdot 1 = 3 = (2)(2) - (1)(1) = \det(A)$

---

### Question 8: What is matrix diagonalization, and how does it relate to eigenvectors?
**Answer**:
If an $n \times n$ matrix $A$ has $n$ linearly independent eigenvectors, we can construct matrix $P = [\vec{v}_1, \dots, \vec{v}_n]$ and diagonal matrix $D = \text{diag}(\lambda_1, \dots, \lambda_n)$.
Then:
$$AP = A[\vec{v}_1, \dots, \vec{v}_n] = [\lambda_1\vec{v}_1, \dots, \lambda_n\vec{v}_n] = PD$$
$$A = PDP^{-1}$$
This changes our coordinate system from standard Cartesian axes to the natural eigenbasis, uncoupling multivariate equations into independent single-variable problems.

---

### Question 9: What is the difference between algebraic multiplicity and geometric multiplicity?
**Answer**:
- **Algebraic Multiplicity ($AM$)**: The multiplicity of $\lambda$ as a root of the characteristic polynomial $\det(A - \lambda I) = 0$.
- **Geometric Multiplicity ($GM$)**: The dimension of the eigenspace corresponding to $\lambda$, i.e., $\text{nullity}(A - \lambda I)$.
- General theorem: $1 \le GM(\lambda) \le AM(\lambda)$. If $GM(\lambda) < AM(\lambda)$ for any eigenvalue, the matrix is **defective** (non-diagonalizable), such as a shear matrix $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$.

---

### Question 10: Where are eigenvalues and eigenvectors used in real-world engineering and computing?
**Answer**:
1. **Google PageRank**: Finds the dominant eigenvector ($\lambda = 1$) of the stochastic web hyperlink transition matrix.
2. **Principal Component Analysis (PCA)**: Finds the eigenvectors of covariance matrices to identify directions of maximum variance for machine learning dimensionality reduction.
3. **Structural Vibration & Resonance**: Eigenvalues represent natural resonance frequencies of buildings and bridges; eigenvectors represent structural deformation mode shapes.
4. **Quantum Mechanics**: Observable physical quantities (energy, momentum) correspond to eigenvalues of Hermitian operators acting on state wavefunctions (eigenstates).
