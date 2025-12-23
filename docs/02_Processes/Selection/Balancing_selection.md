## 1. Definition (dynamical perspective)

**Balancing selection** refers to a class of selective regimes in which **allele frequency dynamics admit a stable internal equilibrium**:

$$
0 < p^* < 1  
$$

In contrast to directional selection, balancing selection **prevents fixation or loss**, maintaining polymorphism over long evolutionary timescales.

From a dynamical systems perspective, balancing selection corresponds to a **stable fixed point inside the state space**.

---

## 2. State variable and dynamics

Let

- $p$ = frequency of allele $A$
    
- $p \in [0,1]$
    
Allele frequency dynamics are described by:

$$
\frac{dp}{dt} = f(p)  
$$

Under balancing selection:

- $f(p) > 0$  when $p < p^*$
    
- $f(p) < 0$  when $p > p^*$ 
    
Thus, trajectories are **attracted toward ( $p^*$ )**.

---
## 3. Phase portrait (topological view)

Balancing selection produces a **single internal attractor**:

```
0  ----->  p*  <-----  1
```

- $p = 0$, $p = 1$: unstable fixed points
    
- $p = p^*$: stable equilibrium
    

This topology sharply contrasts with directional selection, where only boundary equilibria exist.

---

## 4. Overdominance (heterozygote advantage)

### 4.1 Fitness scheme

The canonical form of balancing selection arises under **overdominance**:

$$
\begin{aligned}  
w_{AA} &= 1 - s_1 \\  
w_{Aa} &= 1 \\  
w_{aa} &= 1 - s_2  
\end{aligned}  
$$

where $s_1, s_2 > 0$.

### 4.2 Internal equilibrium

Solving$\frac{dp}{dt} = 0$ yields:
$$
p^* = \frac{s_2}{s_1 + s_2}  
$$

This equilibrium is **globally stable** under deterministic dynamics.

### 4.3 Interpretation

- Selection disfavors both homozygotes
    
- Rare alleles are protected
    
- Allele frequencies are “pulled back” toward the center
    

This is the **cleanest and most robust mechanism** for balancing selection.

---

## 5. Other mechanisms generating balancing selection

Balancing selection is a **dynamical outcome**, not a single biological mechanism.

### 5.1 Frequency-dependent selection

Fitness depends on allele frequency:

$$  
w_A = w_A(p), \quad \frac{dw_A}{dp} < 0  
$$

- Rare alleles enjoy higher fitness
    
- Common in host–pathogen interactions and mating systems
    

---

### 5.2 Spatial or temporal heterogeneity

Different environments favor different alleles:

- Migration + local selection
    
- Temporal environmental fluctuations
    

Averaging across space or time can generate a **stable internal equilibrium**.

---

## 6. Coalescent consequences

Balancing selection has **distinct genealogical signatures**:

- Extended coalescent times
    
- Deep genealogies near selected loci
    
- Maintenance of ancient allelic lineages
    

This contrasts sharply with background selection, which shortens coalescent times.

---

## 7. Statistical signatures

Balancing selection produces recognizable population-genetic patterns:

- Elevated nucleotide diversity (π)
    
- Excess of intermediate-frequency variants
    
- Positive Tajima’s D
    
- Long-range LD around selected sites
    

These signatures form the basis of **balancing-selection scans**.

---

## 8. Relation to drift

In finite populations:

- Balancing selection counteracts drift
    
- Strong enough selection stabilizes polymorphism
    
- Weak balancing selection may be overwhelmed by drift
    

Thus, persistence depends on the relative strength of:  
$$
N_e s  
$$

---

## 9. Conceptual contrast

|Regime|Outcome|Diversity|Fixed points|
|---|---|---|---|
|Directional selection|Fixation|↓|Boundary only|
|Balancing selection|Polymorphism|↑|Internal stable|
|Background selection|Loss of variation|↓↓|Boundary only|

---

## 10. Conceptual summary

> **Balancing selection acts as a restoring force in allele-frequency space.**

It maintains genetic variation by introducing **negative feedback** on allele frequencies, fundamentally altering both **dynamics** and **genealogies**.

---

## Links

- [[Overdominance]]
    
- [[Underdominace]]
    
- [[Selection_continuous]]
    
- [[Genetic drift]]
    
- [[Site_frequency_spectrum]]
    
- [[Coalescent_theory]]
    