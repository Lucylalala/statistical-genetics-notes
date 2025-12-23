## 1. What is migration?

**Migration** is the deterministic change in allele frequency caused by the movement of individuals (or gametes) between populations.

In population genetics, migration is modeled as a **mixing process** that alters allele frequencies by importing genetic material from other populations.

> Migration is a **force** acting on allele frequencies, not a stochastic process.

---

## 2. Migration as a deterministic force

Unlike genetic drift:

- migration does **not** arise from randomness
    
- it has a **direction and magnitude**
    
- it does **not** require finite population size ($N$)
    

Mathematically, migration defines a **deterministic mapping** on allele-frequency space.

This places migration in the same conceptual category as:

- mutation
    
- selection
    

---

## 3. The simplest model: one population receiving migrants

### Assumptions

- Focal population with allele frequency ($p_t$)
    
- Source population with allele frequency ($p_m$)
    
- Migration rate ($m$): fraction of individuals replaced by migrants each generation
    

### Update rule

$$
\boxed{  
p_{t+1}
=
(1-m)p_t + m p_m  
}  
$$

Interpretation:

- fraction ($1-m$): local reproduction
    
- fraction ($m$): migrant contribution
    

---

## 4. Continuous-time limit

For small (m), we can write the continuous-time approximation:

$$  
\boxed{  
\frac{dp}{dt}
=
m(p_m - p)  
}  
$$

This is a **linear differential equation** describing migration as a restoring force.

---

## 5. Fixed point and stability

### Fixed point
$$  
\frac{dp}{dt} = 0  
\quad\Rightarrow\quad  
p^* = p_m  
$$

The equilibrium allele frequency equals the source population frequency.

---

### Stability

- If ($p > p_m$): migration decreases ($p$)
    
- If ($p < p_m$): migration increases ($p$)
    

Thus:

$$  
p^* = p_m \quad \text{is globally stable}  
$$

Migration always homogenizes allele frequencies.

---

## 6. Migration as a force field

In force-field language:

$$  
\frac{dp}{dt} = -m(p - p_m)  
$$

- Direction: toward ($p_m$)
    
- Strength: proportional to distance from ($p_m$)
    
- Shape: linear (no nonlinearity)
    

Migration creates a **single attractor** in allele-frequency space.

---

## 7. Two-population symmetric migration (preview)

For two populations with symmetric migration rate (m):

$$  
\begin{aligned}  
\frac{dp_1}{dt} &= m(p_2 - p_1) \\  
\frac{dp_2}{dt} &= m(p_1 - p_2)  
\end{aligned}  
$$

Properties:

- difference ($p_1 - p_2$) decays exponentially
    
- populations converge to a common frequency
    
- total mean frequency is conserved
    

This introduces **population structure** without randomness.

---

## 8. Migration vs mutation (important comparison)

| Aspect           | Mutation                   | Migration               |
| ---------------- | -------------------------- | ----------------------- |
| Acts on          | alleles                    | individuals / gametes   |
| Typical rate     | very small                 | potentially large       |
| Source frequency | implicit ($0/1$)           | explicit ($p_m$)        |
| Effect           | creates new variation      | redistributes variation |
| Fixed point      | mutation–selection balance | source population       |

Migration can be seen as **frequency-dependent mutation** driven by other populations.

---

## 9. Migration vs selection

| Aspect                  | Migration               | Selection             |
| ----------------------- | ----------------------- | --------------------- |
| Direction               | toward source frequency | toward higher fitness |
| Depends on fitness?     | no                      | yes                   |
| Nonlinearity            | linear                  | generally nonlinear   |
| Creates adaptation?     | no                      | yes                   |
| Homogenizes populations | yes                     | no                    |

Migration does **not optimize fitness**; it optimizes similarity.

---

## 10. Migration–selection balance (conceptual preview)

When migration and selection act together:

- migration pulls allele frequencies toward the source
    
- selection pulls frequencies toward local optima
    

Balance occurs when:

$$  
\text{migration force} = \text{selection force}  
$$

This explains:

- local adaptation
    
- clines
    
- tension zones
    

(Details developed in later modules.)

---

## 11. What migration does NOT capture

Migration models intentionally ignore:

- stochastic sampling (drift)
    
- ancestry and genealogies
    
- haplotype structure
    
- linkage disequilibrium
    

These require:

- genetic drift
    
- recombination
    
- coalescent theory
    

---

## 12. Conceptual role of migration in population genetics

Migration:

- introduces population structure deterministically
    
- counteracts divergence
    
- sets the stage for drift-based differentiation
    
- provides the backbone for (F_{ST}) theory
    

Migration is the **last purely deterministic process** before entering stochastic population genetics.

---

## Links

- [[Allele_frequency]]
    
- [[Frequency dynamics]]
    
- [[Mutation]]
    
- [[Selection(general)]]
    
- [[Selection_continuous]]
    
- [[Genetic drift]]

- [[Population_structure]]
    

---


> **Migration is a deterministic homogenizing force that moves allele frequencies toward external sources, introducing population structure without stochasticity.**

---
