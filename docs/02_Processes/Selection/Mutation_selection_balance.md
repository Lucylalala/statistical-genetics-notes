## 1. Conceptual overview

**Mutation–selection balance** describes the long-term equilibrium that arises when:

- **selection** removes deleterious alleles, and
    
- **mutation** continuously introduces them.
    

Rather than leading to fixation or loss, the system settles at an **internal stable equilibrium**, where opposing evolutionary forces balance.

> Selection is a directional force.  
> Mutation is a restorative force.  
> Their competition defines a stable allele-frequency attractor.

---

## 2. Why selection alone is insufficient

In a pure selection model:

- boundary states (($p=0, p=1$)) are the only equilibria,
    
- advantageous alleles fix,
    
- deleterious alleles are eliminated.
    

However, empirical populations show:

- persistent deleterious variation,
    
- incomplete purging,
    
- stable polymorphism at low frequency.
    

**Mutation is required to maintain genetic variation.**

---

## 3. Continuous-time formulation

Let:

- ($p$): frequency of allele ($A$)
    
- ($\mu$): mutation rate ($A \to a$)
    
- ($\nu$): mutation rate ($a \to A$)
    

### Mutation contribution

$$
\left.\frac{dp}{dt}\right|_{\text{mutation}}
=
\nu(1-p) - \mu p  
$$

This term:

- increases ($p$) via back-mutation,
    
- decreases ($p$) via forward mutation.
    

---

## 4. Selection term (from continuous limit)

From `Selection_continuous.md`, under viability selection with dominance:

$$
\left.\frac{dp}{dt}\right|_{\text{selection}}

=s\,p(1-p)\Big[(1-h)+(2h-1)p\Big]  
$$

---

## 5. Full mutation–selection dynamics

By superposition of forces:

$$  
\boxed{  
\frac{dp}{dt}

=s\,p(1-p)\Big[(1-h)+(2h-1)p\Big]  
+  
\nu(1-p) - \mu p  
}  
$$

This is a **one-dimensional nonlinear dynamical system** with mutation and selection acting simultaneously.

---

## 6. Classical case: recessive deleterious allele

This is the **canonical textbook model** underlying purifying selection.

### Assumptions

- allele ($a$) is deleterious
    
- allele ($A$) is wild type
    
- complete recessivity: ($h = 0$)
    
- no back-mutation: ($\nu = 0$)
    

Fitness scheme:

$$
w_{AA} = 1\,\quad  
w_{Aa} = 1\,\quad  
w_{aa} = 1 - s  
$$

---

## 7. Dynamical equation

Under these assumptions:

### Selection term

$$
\left.\frac{dp}{dt}\right|_{\text{selection}}

s,p(1-p)^2  
$$

### Mutation term

$$
\left.\frac{dp}{dt}\right|_{\text{mutation}}
=
-\mu p  
$$

### Combined system

$$
\boxed{  
\frac{dp}{dt}
=
s\,p(1-p)^2 - \mu p  
}  
$$

---

## 8. Solving for the equilibrium

At equilibrium ($p^*$):

$$
\frac{dp}{dt} = 0  
$$

Assuming ($p^* \neq 0$):

$$
s(1-p^*)^2 = \mu  
$$

Solving:
$$
\boxed{  
p^*
=
1 - \sqrt{\frac{\mu}{s}}  
}  
]
$$
This is the **mutation–selection balance frequency**.

---

## 9. Interpretation of the equilibrium

### 9.1 Persistence of deleterious alleles

Even with strong selection (($s \gg \mu$)):

- deleterious alleles are not eliminated,
    
- they persist at low frequency.
    

Selection reduces frequency,  
mutation prevents extinction.

---

### 9.2 Dependence on ($\mu/s$)

The equilibrium depends only on:

$$
\frac{\mu}{s}  
$$

- independent of population size,
    
- independent of initial frequency,
    
- determined by force balance.
    

---

### 9.3 Stability

The equilibrium ($p^*$) is **stable**:

- if ($p > p^*$): selection dominates → ($p$) decreases
    
- if ($p < p^*$): mutation dominates → ($p$) increases
    

Thus, ($p^*$) is a genuine **attractor** in allele-frequency space.

---

## 10. Phase-line interpretation

The force field now has a new topology:

```
p=0      p*                  p=1
|  → → →  ●  ← ← ←           |
        stable
```

- boundary fixation is prevented,
    
- an internal equilibrium emerges,
    
- long-term polymorphism is maintained.
    

This marks a **qualitative transition** from pure selection dynamics.

---

## 11. Conceptual significance

Mutation–selection balance shows that:

- evolution does not necessarily optimize fitness,
    
- equilibrium can occur away from fitness maxima,
    
- genetic load is an inevitable consequence of mutation.
    

> Purifying selection does not eliminate deleterious alleles —  
> it confines them to a low-frequency equilibrium.

---

## 12. Extensions and generalizations

This framework naturally extends to:

- partial dominance (($h \neq 0$))
    
- back-mutation (($\nu > 0$))
    
- multiple loci (background selection)
    
- diffusion approximations with drift
    

Mutation–selection balance forms the theoretical backbone of:

- genetic load theory,
    
- nearly neutral evolution,
    
- low-frequency variant architecture in GWAS.
    

---

## Links

- [[Selection(general)]]
    
- [[Selection_continuous]]
    
- [[Fitness_scheme]]
    
- [[Mutation]]
    
- [[Allele_frequency]]
    
- [[Background_selection]]
    

