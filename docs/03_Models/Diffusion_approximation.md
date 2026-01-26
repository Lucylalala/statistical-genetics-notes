## 1. Conceptual motivation

The Wright–Fisher model provides an exact, discrete-time description of allele frequency evolution in a finite population.  
However, its discrete state space and generation-based dynamics make analytical treatment and inference difficult.

The diffusion approximation addresses this by asking:

> _What is the continuous-time limit of Wright–Fisher dynamics when population size is large and per-generation changes are small?_

The answer is a **stochastic differential equation (SDE)** describing allele frequency evolution as a diffusion process.

---

## 2. Fundamental idea

> **Diffusion approximation is the large-population, long-time, weak-change limit of the Wright–Fisher model.**

Three ingredients are essential:

1. Finite population size introduces randomness (genetic drift)
    
2. Allele frequency changes per generation are small
    
3. Random effects accumulate over many generations
    

Under these conditions, discrete binomial sampling converges to continuous stochastic motion.

---

## 3. Wright–Fisher moments as the starting point

Let $p_t$ denote the allele frequency at generation $t$.

Under the Wright–Fisher model:
$$
X_{t+1} \mid p_t \sim \mathrm{Binomial}(2N, p_t)  
\quad\text{and}\quad  
p_{t+1} = \frac{X_{t+1}}{2N}  
$$

The first two conditional moments are:

### Conditional mean
$$
\mathbb{E}[p_{t+1} - p_t \mid p_t] = M(p_t)  
$$

### Conditional variance
$$
\mathrm{Var}(p_{t+1} - p_t \mid p_t) = V(p_t)  
$$

For **neutral drift**:  
$$
M(p) = 0, \qquad V(p) = \frac{p(1-p)}{2N}  
$$

These two quantities completely determine the diffusion limit.

---

## 4. Time rescaling

As $N \to \infty$, the per-generation variance goes to zero.  
To observe non-trivial stochastic behavior, time must be rescaled.

Define continuous time:  
$$
t = \frac{\tau}{2N}  
$$

Interpretation:

- Each generation contributes a fluctuation of order $1/N$
- Over $O(N)$ generations, these fluctuations accumulate
    
This rescaling is essential and not optional.

---

## 5. Diffusion limit

Under the rescaling above, the allele frequency process converges to a stochastic differential equation:
$$
\boxed{  
dp(t) = M(p)\,dt + \sqrt{V(p)}\,dW_t  
}  
$$

where:

- $W_t$ is standard Brownian motion
- $M(p)$ is the deterministic drift term
- $V(p)$ is the diffusion (variance) term
    
---

## 6. Wright–Fisher diffusion (neutral case)

For pure genetic drift:
$$
\boxed{  
dp(t) = \sqrt{p(1-p)}\,dW_t  
}  
$$

Key properties:

- No deterministic trend
- State-dependent noise
- Absorbing boundaries at $p=0$ and $p=1$
    
This process is known as the **Wright–Fisher diffusion**.

---

## 7. Selection + drift: unified dynamics

When selection is present, the deterministic term becomes non-zero.

For genic selection with coefficient ( s ):
$$
\boxed{  
dp
=
s\,p(1-p)\,dt  
+  
\sqrt{\frac{p(1-p)}{2N}}\,dW_t  
}  
$$

Interpretation:

- Selection determines the **direction** of change
- Drift determines the **uncertainty** around that direction
    
This decomposition formalizes the orthogonality of selection and drift.

---

## 8. Fokker–Planck (forward Kolmogorov) equation

Instead of tracking individual trajectories, one may study the probability density ( f(p,t) ).

The corresponding Fokker–Planck equation is:
$$
\frac{\partial f}{\partial t}
=
-\frac{\partial}{\partial p}[M(p)f]  
+  
\frac{1}{2}\frac{\partial^2}{\partial p^2}[V(p)f]  
$$

For neutral drift:
$$
\frac{\partial f}{\partial t}
=
\frac{1}{2}  
\frac{\partial^2}{\partial p^2}\big[p(1-p)f\big]  
$$

This formulation underlies many results in population genetics, including fixation times and frequency spectra.

---

## 9. Boundary behavior and fixation

In the diffusion framework:

- $p=0$ and $p=1$ are absorbing boundaries
- Fixation probability under neutrality:  
$$
    P_{\mathrm{fix}}(p_0) = p_0  
    $$
- Expected fixation time scales with effective population size
    

Diffusion theory reproduces all classical Wright–Fisher fixation results in continuous time.

---

## 10. Conceptual interpretation

Diffusion approximation shows that:

- Genetic drift is not an ad hoc noise term
- It emerges naturally from finite sampling
- Its strength is inversely proportional to effective population size
    

From this perspective:

> **Genetic drift is the diffusion component of allele frequency dynamics arising from finite reproduction.**

---

## 11. Position in the population genetics framework

Diffusion approximation occupies a central position:

```
Wright–Fisher model
        ↓
Diffusion approximation
        ↓
Coalescent theory
        ↓
SFS / LD / GWAS
```

It forms the bridge between:

- Forward-time stochastic dynamics
- Backward-time genealogical processes
    

---

## 12. What diffusion approximation enables

Only within the diffusion framework can one:

- Derive continuous-time fixation statistics
- Construct likelihood-based inference
- Incorporate time-varying population size
- Connect allele frequencies to coalescent genealogies
- Interpret GWAS kinship matrices as covariance structures
    

---

## 13. Limitations

Diffusion approximation assumes:

- Large effective population size
- Small per-generation changes
- Weak selection, mutation, and migration
    

It is an approximation, but a **controlled and principled one**.

---

## 14. Summary

> **Diffusion approximation provides a continuous-time stochastic description of allele frequency evolution that preserves the essential effects of genetic drift while enabling analytical and inferential tractability.**

It is the mathematical backbone of modern population genetics.

---

## Links

- [[Wright_Fisher_model]]
- [[Genetic drift]]
- [[Selection_continuous]]
- [[Coalescent_theory]]
- [[Population_structure]]
- [[GWAS_K_matrix]]
    
---
