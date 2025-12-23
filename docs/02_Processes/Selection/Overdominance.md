## 1. Definition of overdominance

**Overdominance** (heterozygote advantage) occurs when the heterozygote has higher fitness than both homozygotes:

$$
\boxed{  
w_{Aa} > w_{AA}, \quad w_{Aa} > w_{aa}  
}  
$$

This is a definition based on **fitness ranking**, not parameter values.

Overdominance represents a qualitative shift in selection dynamics:

- the fitness optimum lies **inside** allele-frequency space,
    
- not at the boundaries.
    

---

## 2. Canonical fitness scheme

A standard parameterization is:

$$  
\begin{aligned}  
w_{AA} &= 1 - s \\  
w_{Aa} &= 1 \\  
w_{aa} &= 1 - t  
\end{aligned}  
\quad (s>0,; t>0)  
$$

Here:

- both homozygotes are selected against,
    
- the heterozygote is optimal.
    

---

## 3. Allele-frequency dynamics

Under random mating and viability selection, the change in allele frequency is:

$$
\Delta p
=
\frac{pq}{\bar w}(w_A - w_a)  
$$

For the above fitness scheme, selection becomes **frequency dependent**.

In the weak-selection, continuous-time limit:

$$ 
\boxed{  
\frac{dp}{dt}
=
p(1-p)\big[t - (s+t)p\big]  
}  
$$

This nonlinear equation defines the overdominance dynamics.

---

## 4. Fixed points

Solving ($\frac{dp}{dt}=0$) yields three equilibria:

- ($p=0$)
    
- ($p=1$)
    
- internal equilibrium:  
    $$
    \boxed{  
    p^* = \frac{t}{s+t}  
    }  
    $$
    

The internal equilibrium lies strictly between 0 and 1.

---

## 5. Stability analysis

### Boundary points

- Near ($p=0$):  
    $$
    \frac{dp}{dt} \approx tp > 0  
    $$ 
    → ($p=0$) is **unstable**
    
- Near ($p=1$):  
    $$
    \frac{dp}{dt} \approx -s(1-p) < 0  
    $$ 
    → (p=1) is **unstable**
    

---

### Internal equilibrium

At ($p^*$):

- if ($p < p^*$): ($\frac{dp}{dt} > 0$)
    
- if ($p > p^*$): ($\frac{dp}{dt} < 0$)
    

Thus:

$$
\boxed{  
p^* \text{ is a stable internal equilibrium}  
}  
$$

---

## 6. Phase-line interpretation

The overdominance phase line has the structure:

```
0  ←———  ●  ———→  1
       stable
```

Interpretation:

- selection pushes allele frequencies away from boundaries,
    
- trajectories converge toward the internal attractor.
    

This is the first case where **selection alone maintains polymorphism**.

---

## 7. Mechanistic interpretation (key insight)

The core mechanism of overdominance is:

> **The rarer allele is more likely to occur in heterozygotes,  
> which have the highest fitness.**

Thus:

- when allele ($A$) is rare, it is favored;
    
- when allele ($a$) is rare, it is favored.
    

This creates **negative frequency-dependent selection**.

---

## 8. Comparison with dominance selection

| Feature                | Dominance selection | Overdominance |
| ---------------------- | ------------------- | ------------- |
| Fitness optimum        | boundary            | interior      |
| Direction of selection | unidirectional      | bidirectional |
| Internal equilibrium   | none                | stable        |
| Maintains polymorphism | no                  | yes           |
| Requires mutation      | no                  | no            |

Overdominance represents a **topological change** in the selection landscape.

---

## 9. Relation to mutation–selection balance

Important distinction:

- mutation–selection balance:  
    equilibrium arises from opposing forces
    
- overdominance:  
    equilibrium arises from selection alone
    

Thus, overdominance is an **intrinsic balancing selection** mechanism.

---

## 10. Biological relevance and examples

Classic examples include:

- sickle-cell polymorphism in malaria-endemic regions
    
- MHC diversity
    
- loci contributing to heterosis
    

Note:

> heterozygote advantage at the phenotypic level  
> does not always imply single-locus overdominance.

---

## 11. Conceptual role in population genetics

Overdominance demonstrates that:

- selection does not always eliminate variation,
    
- equilibrium does not necessarily correspond to fixation,
    
- frequency-dependent effects can stabilize diversity.
    

It is the canonical model of **balancing selection**.

---

## Links

- [[Dominance_selection]]
    
- [[Selection(general)]]
    
- [[Selection_continuous]]
    
- [[Mutation_selection_balance]]
    
- [[Underdominace]]
    
- [[Genetic drift]]
    
- [[Balancing_selection]]
    

---

> **Overdominance produces a stable internal equilibrium because the fitness maximum lies in heterozygotes, creating negative frequency-dependent selection that favors rare alleles.**

---
