## 1. What the Wright–Fisher model is

The Wright–Fisher model is a **discrete-time stochastic population model** that describes how allele frequencies change across generations due to **random sampling of gametes** in a finite population.

It provides the **canonical mathematical foundation** for genetic drift.

> Genetic drift is the phenomenon;  
> the Wright–Fisher model is the formal mechanism.

---

## 2. Core assumptions

The classical Wright–Fisher model assumes:

1. **Finite population size**
    
    - Diploid population of constant size ( $N$ )
        
    - Total number of gene copies: ( $2N$ )
        
2. **Non-overlapping generations**
    
    - Entire population is replaced each generation
        
3. **Random mating**
    
    - No population structure
        
    - No assortative mating
        
4. **No selection, mutation, or migration**
    
    - All alleles are selectively neutral
        
    - Allele frequency changes are purely stochastic
        
5. **Sampling with replacement**
    
    - Each new gene copy is drawn independently from the parental generation
        

These assumptions define a **minimal neutral model**.

---

## 3. State variable

Let:

- ( $p_t$ ): frequency of allele ( $A$ ) at generation ( $t$ )
    

The **state space** is:

$$
p_t \in \{ 0, \frac{1}{2N}, \frac{2}{2N}, \dots, 1 \}  
$$

This discreteness is fundamental.

---
## 4. Transition rule (binomial sampling)

Given allele frequency ( $p_t$ ), the number of ( $A$ ) alleles in the next generation follows:

$$  
X_{t+1} \sim \mathrm{Binomial}(2N, p_t)  
$$

and therefore:

$$
p_{t+1} = \frac{X_{t+1}}{2N}  
$$

This single equation **fully defines the Wright–Fisher process**.

---

## 5. Expectation and variance

### Expectation

$$
\mathbb{E}[p_{t+1} \mid p_t] = p_t  
$$

➡️ Drift does **not** bias allele frequency on average.

---

### Variance

$$  
\mathrm{Var}(p_{t+1} \mid p_t) = \frac{p_t(1 - p_t)}{2N}  
$$

Key consequences:

- Drift strength increases when:
    
    -  $N$ is small
        
    - $p_t$ is intermediate
    
- Variance goes to zero at  $p = 0$ and  $p = 1$
    
---

## 6. Absorbing boundaries and fixation

- $p = 0$ : loss of allele $A$
    
- $p = 1$: fixation of allele $A$
    

These are **absorbing states**:

$$
p_t = 0 \Rightarrow p_{t+k} = 0 \quad \forall k > 0  
$$

Under pure drift:

- Fixation is inevitable
    
- Which allele fixes is random
    
---

## 7. Fixation probability

For a neutral allele:

$$
\Pr(\text{fixation} \mid p_0) = p_0  
$$

In particular:

- A new mutation appears at frequency ( $\frac{1}{2N}$ )
    
- Fixation probability:
    

$$
\Pr(\text{fixation}) = \frac{1}{2N}  
$$

This result is **one of the most important in population genetics**.

---

## 8. Time to fixation (order of magnitude)

- Expected time to fixation or loss:  
    $$
    \mathcal{O}(N)  
    $$
    
- Conditioning on fixation:  
    $$
    \mathcal{O}(4N)  
    $$

Drift is **slow in large populations, fast in small ones**.

---

## 9. Relation to genetic drift

Genetic drift is:

> The stochastic change in allele frequency caused by finite population sampling.

The Wright–Fisher model shows that drift is:

- Unbiased in expectation
    
- Inevitable in finite populations
    
- Strongly dependent on population size
    

---

## 10. From Wright–Fisher to diffusion approximation

Taking the limit:

-  $N \to \infty$
    
- Small changes per generation
    

leads to the **diffusion approximation**:

$$ 
dp = \sqrt{\frac{p(1-p)}{2N}} \, dW_t  
$$

This connects Wright–Fisher to:

- Stochastic differential equations
    
- Fokker–Planck equations
    
- Continuous-time allele frequency dynamics
    
---

## 11. Position in the dynamics framework

|Level|Role|
|---|---|
|Genetic drift|Evolutionary phenomenon|
|Wright–Fisher model|Discrete stochastic model|
|Diffusion approximation|Continuous limit|
|Coalescent theory|Backward-time dual|

---

## 12. What the Wright–Fisher model does _not_ include

- Selection → added via biased sampling
    
- Mutation → added via mutation matrices
    
- Migration → added via structured populations
    
- Linkage → single-locus only
    

These extensions define **new models**, not modifications of the core.

---

## 13. Conceptual summary

> The Wright–Fisher model is the simplest mathematically complete description of evolution under randomness alone.

It is the **probabilistic backbone** underlying:

- Genetic drift
    
- Neutral theory
    
- Diffusion theory
    
- Coalescent theory
    
- GWAS kinship modeling (via covariance structure)
    

---

## Links

- [[Genetic drift]]
    
- [[Allele_frequency]]
    
- [[Diffusion_approximation]]
    
- [[Coalescent_theory]]
    
- [[Site_frequency_spectrum]]
    
- [[GWAS_K_matrix]]
    
---
