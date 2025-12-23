## 1. Statement of the Hardy–Weinberg law

**Hardy–Weinberg equilibrium (HWE)** states that:

> In a randomly mating population with no evolutionary forces,  
> genotype frequencies are completely determined by allele frequencies  
> and remain constant across generations.

Formally, for a biallelic locus with allele frequencies:  
$$
p = \text{freq}(A), \quad q = 1 - p  
$$

the genotype frequencies are:  
$$
AA : p^2,\quad Aa : 2pq,\quad aa : q^2  
$$

---

## 2. What Hardy–Weinberg is _really_ about 

Hardy–Weinberg is **not** primarily a formula.  
It is a **reference state**.

In the language of dynamics:

> **Hardy–Weinberg equilibrium is the fixed point of the genetic system when all evolutionary forces are absent.**

It defines:

- the _null model_ of population genetics
    
- the _baseline state_ against which all deviations are interpreted
    

---

## 3. Assumptions (as modeling constraints)

Hardy–Weinberg equilibrium holds under the following assumptions:

- random mating
    
- infinite population size
    
- no selection
    
- no mutation
    
- no migration
    
- no genetic drift
    
- no population structure
    
- no inbreeding
    

These assumptions are **not meant to be realistic**, but **diagnostic**.

> Each violation of an assumption corresponds to a specific evolutionary process.

---

## 4. Hardy–Weinberg as a fixed point

From a dynamical perspective:

- Allele frequencies $p$ are state variables
    
- Genotype frequencies are functions of $p$
    

If no evolutionary forces act:  
$$
\frac{dp}{dt} = 0  
$$

and the system remains at:

$$
(p^2,\,2pq,\,q^2)  
$$

Thus, Hardy–Weinberg represents a **neutral equilibrium state** of the system.

---

## 5. Separation of timescales
A key theoretical insight is that:

> **Genotype frequencies relax to Hardy–Weinberg equilibrium faster than allele frequencies change.**

This allows population genetics to operate on two levels:

1. **Fast dynamics**
    
    - random mating
        
    - restoration of HWE each generation
        
2. **Slow dynamics**
    
    - mutation
        
    - selection
        
    - migration
        
    - drift
        

This separation justifies:

- working primarily with allele frequencies
    
- treating genotype frequencies as quasi-equilibrated
    

---

## 6. Hardy–Weinberg as a null model

Hardy–Weinberg equilibrium functions as the **null hypothesis** in population genetics.

Observed deviation from HWE implies the presence of at least one process:

- selection
    
- inbreeding
    
- population structure
    
- assortative mating
    
- genetic drift
    
- genotyping error (in applied contexts)
    

However:

> **Deviation from HWE is not inherently a problem — it is information.**

---

## 7. What Hardy–Weinberg does NOT assume

Clarifications to avoid common misconceptions:

- HWE does **not** assume equal fitness
    
- HWE does **not** imply absence of evolution forever
    
- HWE does **not** describe adaptive dynamics
    

It simply describes the genetic composition of a population **at a reference state**.

---

## 8. Relationship to evolutionary forces

Hardy–Weinberg equilibrium is the baseline upon which evolutionary forces act:

| Process    | Effect relative to HWE          |
| ---------- | ------------------------------- |
| Mutation   | shifts allele frequencies       |
| Migration  | mixes allele pools              |
| Selection  | biases genotype survival        |
| Drift      | introduces stochastic deviation |
| Inbreeding | alters genotype proportions     |

All subsequent models can be written as:  
$$
\text{HWE} + \text{perturbation}  
$$

---

## 9. Role in population genetics theory

Hardy–Weinberg equilibrium provides:

- the starting point of frequency dynamics
    
- the reference frame for selection models
    
- the baseline for drift and diffusion theory
    
- the foundation for LD and haplotype theory
    
- the statistical null for GWAS quality control
    

Without HWE, population genetics loses its coordinate system.

---

## 10. Conceptual summary

> **Hardy–Weinberg equilibrium is not a law of nature,  
> but a reference state of genetic systems in the absence of evolutionary forces.  
> It defines the zero point of population genetics.**

---

## Links

- [[Allele_frequency]]
    
- [[Frequency dynamics]]
    
- [[Variance dynamics]]
    
- [[Selection(general)]]
    
- [[Mutation]]
    
- [[Migration]]
    
- [[Genetic drift]]
    
- [[Linkage_disequilibrium]]
    
