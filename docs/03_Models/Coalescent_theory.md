## 1. What coalescent theory studies

Coalescent theory provides a **backward-time stochastic description** of how the genealogies of a finite sample of alleles are formed under genetic drift.

Instead of tracking allele frequencies forward in time, coalescent theory focuses on:

- the **ancestral relationships** among sampled alleles
- the **timing of common ancestry**
- the **randomness introduced by finite reproduction**

> Coalescent theory is a theory of **genealogies**, not of populations as a whole.

---

## 2. Motivation: why look backward in time?

### 2.1 Limitations of forward-time models

In forward-time models (e.g. Wright–Fisher):

- the number of individuals is $O(N)$ each generation
- tracking full population histories is intractable
- stochasticity accumulates across many generations

### 2.2 The backward-time advantage

When tracing ancestry backward:

- the number of ancestral lineages **only decreases**
- complexity scales with **sample size $n$**, not population size $N$
- genealogical structure becomes analytically tractable

> Time reversal collapses complexity.

---

## 3. Coalescence as a consequence of genetic drift

Genetic drift arises from **finite reproduction**.  
Coalescence is the **genealogical manifestation** of the same randomness.

Two sampled alleles may trace back to the **same ancestral allele** because:

- only a finite number of gene copies existed in the previous generation
- parental alleles are sampled randomly

Thus:

> **Coalescence is the backward-time signature of genetic drift.**

---

## 4. The basic coalescent event: two lineages

Consider two sampled alleles in a diploid population of size $N$.

- There are (2N) alleles in the parental generation
- Each sampled allele independently chooses a parent allele
- The probability that both choose the same parent allele is:

$$
P(\text{coalescence in previous generation}) = \frac{1}{2N}  
$$

This is the fundamental microscopic rule underlying coalescent theory.

---

## 5. Continuous-time limit and exponential waiting time

For large $N$:

- coalescence is a rare event per generation
- generations form independent Bernoulli trials

In the limit $N \to \infty$, waiting time to coalescence converges to an exponential distribution:

$$
T \sim \text{Exponential}!\left(\frac{1}{2N}\right)  
$$

with mean:

$$
\mathbb{E}[T] = 2N  
$$

This defines the **coalescent time scale**.

---

## 6. The Kingman coalescent (general case)

For a sample of (n) alleles, let (k) be the number of ancestral lineages at a given time.

### 6.1 Coalescence rate

Any pair of lineages can coalesce, so the total coalescence rate is:

$$ 
\lambda_k = \binom{k}{2} \cdot \frac{1}{2N}  
$$

### 6.2 Waiting time distribution

The waiting time until the next coalescent event is:

$$
T_k \sim \text{Exponential}(\lambda_k)  
$$

with expected value:

$$
\mathbb{E}[T_k] = \frac{2N}{\binom{k}{2}}  
$$

---

## 7. Definition: Kingman’s coalescent

> **Kingman’s coalescent** is a continuous-time Markov process describing the backward-time merging of ancestral lineages, in which:
> 
> - only pairwise mergers occur
> - all lineage pairs are exchangeable
> - coalescence rates are inversely proportional to population size

This process is the **universal neutral limit** of a wide class of population models.

---

## 8. Relationship to Wright–Fisher and diffusion

Coalescent theory is **not a separate model**. It is:

- the **backward-time limit** of the Wright–Fisher model
- mathematically dual to diffusion approximation

|Perspective|Object|Time|
|---|---|---|
|Wright–Fisher|allele counts|forward|
|Diffusion|allele frequencies|forward|
|Coalescent|genealogies|backward|

All three describe the same evolutionary randomness.

---

## 9. Mutation on the coalescent

Under neutrality:

> **Mutation does not affect genealogical structure.**

Therefore:

1. A coalescent tree is generated
2. Mutations occur along branches as a Poisson process
    

This separation allows analytical treatment of genetic variation.

---

## 10. Coalescent and genetic variation

Mutation on coalescent trees explains:

- single nucleotide polymorphisms (SNPs)
- haplotypes
- site frequency spectrum (SFS)
- linkage disequilibrium (LD) 

For example, the expected SFS under neutrality satisfies:

$$
\mathbb{E}[\xi_k] = \frac{\theta}{k}  
\quad (k=1,\dots,n-1)  
$$

where $\theta = 4N\mu$.

---

## 11. Effective population size in coalescent theory

The coalescent rate depends on **effective population size $N_e$**:

$$
\lambda_k = \binom{k}{2} \cdot \frac{1}{2N_e}  
$$

When population size varies through time:

$$  
\lambda_k(t) = \binom{k}{2} \cdot \frac{1}{2N_e(t)}  
$$

Time-varying $N_e(t)$ rescales coalescent time and shapes genealogical structure.

---

## 12. Extensions of the basic coalescent

The standard Kingman coalescent can be extended to include:

- **structured coalescent** (migration / population structure)
- **recombination** (ancestral recombination graph, ARG)
- **background selection**
- **linked selection**
- **demographic history**

Each extension modifies coalescent rates or lineage movement but preserves the core logic.

---

## 13. Why coalescent theory is central

Coalescent theory underlies:

- demographic inference (PSMC, MSMC)
- local ancestry inference
- haplotype-based analyses
- GWAS kinship matrices
- neutral null models for selection tests

It is the **genealogical backbone** of modern statistical genetics.

---

## 14. Conceptual summary

> **Coalescent theory provides a backward-time, sample-based description of genetic drift, transforming finite-population randomness into a tractable theory of genealogies.**

It completes the conceptual chain:

```
Finite reproduction
        ↓
Genetic drift
        ↓
Diffusion (forward-time)
        ↓
Coalescent (backward-time)
        ↓
Mutation on trees
        ↓
Observable genetic variation
```

---
## Links

- [[Wright_Fisher_model]]
- [[Genetic drift]]
- [[Diffusion_approximation]]
- [[Mutation_on_coalescent]]
- [[Site_Frequency_Spectrum]]
- [[Structured_coalescent]]
- [[Effective_population_size]]
- [[GWAS_K_matrix]]
---
