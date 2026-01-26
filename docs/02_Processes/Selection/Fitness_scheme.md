## 1. What is a fitness scheme?

A **fitness scheme** specifies how different **genotypes contribute to the next generation**.  
It translates biological assumptions about survival or reproduction into **relative weights**, which in turn define the **direction and strength of allele frequency dynamics**.

> Fitness schemes are not empirical measurements of survival probability,  
> but **relative fitness values** used to construct a dynamical system.

In population genetics, the fitness scheme acts as the **interface** between:

- biological assumptions
- mathematical formulation
- dynamical behavior of allele frequencies
---

## 2. Viability selection framework

In the **viability selection** model:

- selection acts between **zygote formation and adulthood**
- genotypes differ in their probability of surviving to reproduce
- population size is implicitly rescaled each generation
    

Let the genotype fitnesses be:

$$
w_{AA},; w_{Aa},; w_{aa}  
$$

These values are **relative**, meaning that multiplying all fitnesses by a constant does not change the dynamics.

---

## 3. Canonical parameterization (single-locus, two-allele)

A widely used and highly informative parameterization is:

$$
\begin{aligned}
w_{AA} &= 1 \\
w_{Aa} &= 1 - hs \\
w_{aa} &= 1 - s
\end{aligned}
$$


where:

- $s$ = **selection coefficient** (strength of selection)
- $h$ = **dominance coefficient** (how heterozygotes compare to homozygotes)

This parameterization captures most classical selection models by varying $h$.

---

## 4. Interpretation of parameters

### Selection coefficient $s$

- Measures the fitness disadvantage of genotype $aa$
- $s = 0$: no selection
- Larger $s$: stronger selection against $aa$

### Dominance coefficient $h$

Controls how the heterozygote compares to homozygotes:

| $h$ | Interpretation                             |
| --- | ------------------------------------------ |
| 0   | complete dominance of $A$                  |
| 1/2 | additive (codominant)                      |
| 1   | complete recessivity of $A$                |
| < 0 | overdominance (heterozygote advantage)     |
| > 1 | underdominance (heterozygote disadvantage) |

Thus, **($h$) determines the qualitative structure of the dynamics**, not just the speed.

---

## 5. Special cases and their biological meaning

### 5.1 Complete dominance (h = 0)

$$ 
w_{AA} = w_{Aa} = 1,\quad w_{aa} = 1 - s  
$$

- Heterozygotes express the beneficial allele
- Selection is effective even at low allele frequency
- ($dp/dt \propto sp$)
    

**Biological meaning:**  
The beneficial allele is visible to selection immediately.

---

### 5.2 Additive selection (h = 1/2)

$$
w_{Aa} = \frac{w_{AA} + w_{aa}}{2}  
$$

- Most commonly used textbook model
- Symmetric contribution of alleles
- Smooth allele frequency change
    

**Biological meaning:**  
Phenotype changes approximately linearly with allele dosage.

---

### 5.3 Complete recessivity (h = 1)

$$
w_{Aa} = w_{aa}  
$$

- Beneficial allele hidden in heterozygotes
- Very slow increase when rare
- ($dp/dt \propto sp^2$)
    

**Biological meaning:**  
Recessive advantageous mutations struggle to escape low frequency.

---

## 6. Fitness scheme as a force field

Once a fitness scheme is specified, allele frequency dynamics can be viewed as motion in a **force field**:

$$
\frac{dp}{dt} = F(p)  
$$

- ($p$): allele A frequency
- ($F(p)$): selection-induced force
    

Fixed points satisfy:  
$$
F(p) = 0  
$$

The **stability** of these points depends entirely on the fitness scheme.

> Fitness schemes define the **topology of the phase portrait**.

---

## 7. Fixed points and their meaning

For simple directional selection:

- $p = 0$: loss of allele A
- $p = 1$: fixation of allele A

Stability interpretation:

- **Stable**: system returns after perturbation
- **Unstable**: any perturbation drives system away

⚠️ Important clarification:  
An unstable fixed point (e.g. $p=0$) does **not** mean population extinction —  
it only means the allele frequency state is unstable.

---

## 8. What fitness schemes do NOT capture

Fitness schemes intentionally ignore:

- linkage and LD
- individual ancestry
- genotype phase
- finite population stochasticity

These effects are handled by:

- drift models
- multi-locus models
- coalescent theory

Thus, fitness schemes are **controlled abstractions**, not complete descriptions.

---

## 9. Role of fitness schemes in population genetics

Fitness schemes:

- define selection models
- determine equilibrium structure
- predict fixation vs polymorphism
- connect biology to dynamical systems

They are the **starting point** for:

- mutation–selection balance
- balancing selection
- selective sweeps
- phase-plane analysis

---

## Links

- [[Selection(general)]]
- [[Allele_frequency]]
- [[Frequency dynamics]]
- [[Mutation]]
- [[Mutation_selection_balance]]
    

