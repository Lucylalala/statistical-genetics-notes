## 0. Conceptual position

Genetic drift marks the **transition from deterministic population genetics to stochastic population genetics**.

Before drift:

- allele-frequency dynamics are deterministic
    
- evolution is described by forces (selection, mutation, migration)
    
With drift:

- evolution becomes a **random process**
    
- population size (N) becomes essential
    
- fixation and loss become inevitable outcomes
    
---
## 1. Definition (rigorous and minimal)

**Genetic drift** is the **stochastic fluctuation** of allele frequencies caused by random sampling of gametes in finite populations.

Key points:

- drift is **not a force**
    
- drift has **no direction**
    
- drift arises solely from **finite population size**
    
---
## 2. Why drift exists: probability vs frequency

In infinite populations:
- allele frequency = probability
    
In finite populations:
- allele frequency = outcome of random sampling
    

Thus:

> Even if the expected frequency is unchanged, the realized frequency fluctuates.

This sampling noise is genetic drift.

---

## 3. The Wright–Fisher model (axiomatic foundation)

### 3.1 Model assumptions

- diploid population of constant size ($N$)
    
- non-overlapping generations
    
- random mating
    
- no selection, mutation, or migration
    
- all gametes sampled independently
    

This is the **pure drift model**.

---

### 3.2 Random sampling rule

Let:

- ($p_t$) = frequency of allele ($A$) at generation ($t$)
    
- ($X_{t+1}$) = number of ($A$) alleles in generation ($t+1$)
    

Then:
$$
\boxed{  
X_{t+1} \sim \text{Binomial}(2N, p_t)  
}  
$$

and

$$  
p_{t+1} = \frac{X_{t+1}}{2N}  
$$

This is not an approximation — it is the **definition** of drift.

---

## 4. Expectation and variance (core properties)

### 4.1 Mean behavior (no directional change)

$$
\mathbb{E}[p_{t+1} \mid p_t] = p_t  
$$

Interpretation:

- drift is neutral
    
- no allele is systematically favored
    

---

### 4.2 Variance (strength of drift)

$$
\mathrm{Var}(p_{t+1} \mid p_t)
=
\frac{p_t(1-p_t)}{2N}  
$$

Implications:

- drift strength ($\propto 1/N$)
    
- strongest at intermediate frequencies
    
- zero at fixation boundaries
    

This variance term is the **engine of all stochastic effects**.

---

## 5. Drift as a random walk in allele-frequency space

Under drift:

- allele frequencies perform a **random walk**
    
- boundaries ($p=0$) and ($p=1$) are absorbing
    

Unlike selection:

- there is no restoring force
    
- fluctuations accumulate over time
    

---

## 6. Absorbing states and inevitability of fixation

### 6.1 Absorbing boundaries

Once:

- ($p=0$) → allele lost forever
    
- ($p=1$) → allele fixed forever
    

These states are **absorbing**, not merely stable.

---

### 6.2 Fixation is inevitable

In the absence of mutation and migration:

$$  
\boxed{  
\text{Fixation or loss occurs with probability } 1  
}  
$$

This is a theorem, not a tendency.

---

## 7. Fixation probability (fundamental result)

For a neutral allele with initial frequency ($p_0$):

$$
\boxed{  
\mathbb{P}(\text{fixation}) = p_0  
}  
$$

Special cases:

- single new mutation: ($p_0 = \frac{1}{2N}$)
    
- fixation probability is extremely small in large populations
    

Interpretation:

> Drift preserves expected frequencies, but destroys variation.

---

## 8. Time to fixation

Expected fixation time (neutral drift):

- scales with population size ($N$)
    
- larger populations drift more slowly
    
- smaller populations drift rapidly
    

Approximate results:

- time to fixation $\sim \mathcal O(N)$ to $\mathcal O(4N)$ generations

Thus:

- drift is weak but persistent
    
- long-term consequences are unavoidable
    

---

## 9. Drift vs selection (conceptual contrast)

|Aspect|Selection|Drift|
|---|---|---|
|Nature|deterministic force|stochastic process|
|Direction|yes|no|
|Depends on fitness|yes|no|
|Depends on (N)|no|yes|
|Outcome|optimization|fixation by chance|

Key insight:

> Selection determines _which_ alleles tend to increase,  
> drift determines _whether_ they survive at all.

---

## 10. Drift as the source of population structure

Because drift acts independently in different populations:

- allele frequencies diverge
    
- genetic differentiation accumulates
    
- relatedness emerges
    

This underlies:

- $F_{ST}
    
- kinship matrices (K in GWAS)
    
- PCA structure
    
- ancestry inference
    

---

## 11. Connection to diffusion approximation (preview)

In the continuous limit:

$$
dp
=
\underbrace{M(p)\,dt}_{\text{forces}}  
+  
\underbrace{\sqrt{\frac{p(1-p)}{2N}}\,dW_t}_{\text{drift}}  
$$

Where:

- $M(p)$: selection + mutation + migration
    
- $dW_t$: Wiener process
    
This connects:

- Wright–Fisher → diffusion → coalescent
    
---

## 12. What drift explains (and what it does not)

### Explains:

- loss of variation
    
- random fixation
    
- population differentiation
    
- neutral evolution
    
- background for selection
    

### Does not explain:

- adaptation
    
- fitness optimization
    
- directionality
    

Drift is **the default evolutionary background**.

---

> **Genetic drift is not an evolutionary force but the unavoidable stochastic consequence of finite population size, converting deterministic frequency dynamics into probabilistic evolutionary outcomes.**

---

---

> **Selection and genetic drift are orthogonal components of evolutionary dynamics: selection determines the deterministic direction of allele frequency change, while drift governs the stochastic variability around that direction.**

---

## Links

- [[Hardy_Weinberg_equilibrium]]
    
- [[Allele_frequency]]
    
- [[Frequency dynamics]]
    
- [[Selection(general)]]
    
- [[Mutation]]
    
- [[Migration]]
    
- [[Diffusion_approximation]]
    
- [[Coalescent_theory]]
    
- [[Population_structure]]
    
- [[GWAS_K_matrix]]
    

---