## 1. What is dominance selection?

**Dominance selection** refers to selection in which the fitness of the heterozygote differs from that of both homozygotes.

It describes how the **phenotypic expression of alleles in heterozygotes** modulates the action of selection across allele frequencies.

Dominance does **not** change the direction of selection,  
but it profoundly alters its **dynamics**.

---

## 2. Fitness scheme with dominance

For a single locus with two alleles (A) and (a):

$$
\begin{aligned}  
w_{AA} &= 1 \\  
w_{Aa} &= 1 - hs \\  
w_{aa} &= 1 - s  
\end{aligned}  
$$

where:

- $s$ is the selection coefficient
- $h$ is the dominance coefficient
    

Special cases:

- $h = 0$: complete dominance of $A$
- $h = 1/2$: additive selection
- $h = 1$: complete recessivity of $A$
    

---

## 3. Discrete-time allele frequency change

Under random mating and viability selection:

$$
\Delta p
=
\frac{pq}{\bar w}(w_A - w_a)  
$$

# with:  
$$
w_A - w_a
=
s\big[(1-h) + (2h-1)p\big]  
$$

This expression shows that dominance introduces **frequency dependence** into selection.

---

## 4. Continuous-time approximation

Under weak selection, the continuous-time dynamics are:

$$
\boxed{  
\frac{dp}{dt}
=
s\,p(1-p)\Big[(1-h) + (2h-1)p\Big]  
}  
$$

This equation fully characterizes dominance selection as a nonlinear dynamical system.

---

## 5. Low-frequency behavior: visibility of selection

As $p \to 0$:

$$
\frac{dp}{dt}  
\approx  
s(1-h)\,p  
$$

Implications:

| Dominance | Low-frequency behavior           |
| --------- | -------------------------------- |
| $h < 1$   | Selection acts immediately       |
| $h = 1$   | Selection is effectively neutral |

> Recessive beneficial alleles are invisible to selection when rare.

This explains the slow initial spread of recessive advantageous mutations.

---

## 6. High-frequency behavior

As $p \to 1$:
$$
\frac{dp}{dt}  
\approx  
sh(1-p)  
$$

Dominance effects diminish near fixation.

Selection becomes efficient regardless of dominance once the allele is common.

---

## 7. Fixed points and phase-line structure

For ($0 \le h \le 1$):

- Fixed points: ($p=0$), ($p=1$)
- No internal equilibria

Phase-line interpretation:

- $p=0$: unstable
- $p=1$: stable

Dominance modifies the **speed**, not the **direction**, of evolution.

---

## 8. Dominance vs additive selection

Additive selection $h=1/2$ serves as a baseline:

- symmetric allele contribution
- linear phenotype–genotype relationship

Dominance introduces asymmetry:

- early dynamics differ
- fixation time depends strongly on $h$

---

## 9. Biological interpretation

Dominance reflects:

- gene regulation
- protein dosage
- metabolic buffering
- developmental thresholds
    

It connects molecular biology to population-level dynamics.

---

## 10. Conceptual role of dominance selection

Dominance selection shows that:

- selection strength is frequency dependent
- visibility matters more than ultimate advantage
- early stochastic effects (drift) interact strongly with dominance
    

This prepares the ground for:

- overdominance
- underdominance
- mutation–selection balance with dominance
    

---

## Links

- [[Selection(general)]]
- [[Fitness_scheme]]
- [[Selection_continuous]]
- [[Mutation_selection_balance]]
- [[Overdominance]]
- [[Underdominace]]
- [[Genetic drift]]

---

> **Dominance controls when selection becomes visible,  
> not where evolution ultimately goes.**

---

