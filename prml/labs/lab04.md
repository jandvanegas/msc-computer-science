# Lab 04

## Description

- Computing probability densities and ML estimates.

## Multivariate Gaussian Density

MVG is defined as

$$ \mathcal{N}(x|\mu, \Sigma) = \dfrac{1}{(2\pi)^{\dfrac{M}{2}}|\Sigma|^(1/2)}e^{-1/2 (x-\mu)^T\Sigma^-1(x-\mu)} $$

- where $M$ is the size of $x$
- $|\Sigma|$ is the determinant of $\Sigma$

$$ log \mathcal{N}(x|\mu, \Sigma) = - \dfrac{M}{2}log 2\pi -\dfrac{1}{2}log|\Sigma|-\dfrac{1}{2}(x-\mu)^T\Sigma^{-1}(x-\mu)$$

Write logpdf_GAU_ND(x, mu, C)
