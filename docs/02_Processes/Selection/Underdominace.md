## 1. Definition of underdominance

**Underdominance** (heterozygote disadvantage) occurs when the heterozygote has lower fitness than both homozygotes:

$$
\boxed{  
w_{Aa} < w_{AA}, \quad w_{Aa} < w_{aa}  
}  
$$

In contrast to overdominance, the heterozygote represents a **fitness minimum**, not a maximum.

Underdominance produces **threshold dynamics** and an **unstable internal equilibrium**.

---

## 2. Canonical fitness scheme

A commonly used symmetric parameterization is:

$$  
\begin{aligned}  
w_{AA} &= 1 \\  
w_{Aa} &= 1 - s \\  
w_{aa} &= 1  
\end{aligned}  
\quad (s>0)  
$$

Here:

- both homozygotes have equal fitness,
    
- the heterozygote is selected against.
    

An asymmetric generalization is:

$$
\begin{aligned}  
w_{AA} &= 1 \\  
w_{Aa} &= 1 - s \\  
w_{aa} &= 1 - t  
\end{aligned}  
$$

with ($s,t>0$).

---

## 3. Allele-frequency dynamics

Under random mating and viability selection, allele-frequency change follows:

$$ 
\Delta p
=
\frac{pq}{\bar w}(w_A - w_a)  
$$

In the weak-selection, continuous-time limit, the dynamics take the form:

$$ 
\boxed{  
\frac{dp}{dt}
=
p(1-p)\,G(p)  
}  
$$

where ($G(p)$) changes sign at an internal point, reflecting frequency-dependent selection.

---

## 4. Fixed points

The system has three equilibria:

- ($p = 0$)
    
- ($p = 1$)
    
- an internal equilibrium ($p^*$) (typically ($p^* = 1/2)$ in the symmetric case)
    

---

## 5. Stability structure

### Boundary equilibria

- ($p=0$): **stable**
    
- ($p=1$): **stable**
    

Both pure states are attractors.

---

### Internal equilibrium

The internal equilibrium satisfies:

- if ($p < p^*$): ($\frac{dp}{dt} < 0$)
    
- if ($p > p^*$): ($\frac{dp}{dt} > 0$)
    

Thus:
$$
\boxed{  
p^* \text{ is an unstable equilibrium}  
}  
$$

It acts as a **separatrix** dividing the state space into two basins of attraction.

---

## 6. Phase-line interpretation

The phase-line structure is:

```
0  ———→  ○  ←———  1
      unstable
```

Interpretation:

- initial conditions determine the evolutionary outcome,
    
- trajectories diverge away from the internal equilibrium,
    
- the system evolves toward one of two alternative fixations.
    

---

## 7. Mechanistic interpretation (core insight)

The key mechanism underlying underdominance is:

> **When an allele is rare, it predominantly occurs in heterozygotes,  
> which have the lowest fitness.**

Consequences:

- rare alleles are penalized,
    
- majority alleles are favored,
    
- selection amplifies initial asymmetries.
    

This produces **positive frequency-dependent selection**.

---

## 8. Threshold dynamics

Underdominance introduces a **critical frequency threshold**:

- if ($p_0 < p^*$) → allele ($A$) is eliminated
    
- if ($p_0 > p^*$) → allele ($A$) fixes
    

Thus, evolutionary fate depends on initial conditions.

---

## 9. Comparison with overdominance

| Feature                 | Overdominance | Underdominance |
| ----------------------- | ------------- | -------------- |
| Fitness of heterozygote | highest       | lowest         |
| Frequency dependence    | negative      | positive       |
| Internal equilibrium    | stable        | unstable       |
| Maintains polymorphism  | yes           | no             |
| Dynamics                | convergence   | divergence     |

These two cases represent **topologically opposite selection regimes**.

---

## 10. Biological relevance

Underdominance arises in contexts such as:

- chromosomal rearrangements (e.g. inversions, translocations)
    
- hybrid incompatibilities
    
- engineered gene drives with release thresholds
    
- tension zones between diverging populations
    

It plays a key role in:

- speciation theory
    
- maintenance of sharp clines
    
- bistable evolutionary systems
    

---

## 11. Conceptual role in population genetics

Underdominance demonstrates that:

- selection can be bistable,
    
- polymorphism is not always maintained,
    
- equilibrium structure depends on frequency dependence,
    
- history and initial conditions matter.
    

It is the canonical model of **threshold selection**.

---

## Links

- [[Dominance_selection]]
    
- [[Overdominance]]
    
- [[Selection(general)]]
    
- [[Selection_continuous]]
    
- [[Genetic drift]]
    
- [[Balancing_selection]]
    
- [[Speciation]]
    

---

> **Underdominance creates an unstable internal equilibrium because rare alleles are confined to low-fitness heterozygotes, leading to positive frequency-dependent selection and threshold dynamics.**
---

