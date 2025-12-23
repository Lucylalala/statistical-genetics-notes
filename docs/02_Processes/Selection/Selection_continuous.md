## 1. Motivation: why continuous time?

Classical population genetics is often formulated in **discrete generations**:

$$
p_{t+1} = f(p_t)  
$$

However, for understanding:

- stability,
    
- local behavior near boundaries,
    
- dominance effects at low frequency,
    
- and the geometric structure of selection,
    

it is useful to consider a **continuous-time approximation**.

The continuous-time limit does not replace the discrete model;  
it provides a **local, first-order description** of allele-frequency change under weak selection.

---

## 2. Assumptions of the continuous-time limit

The derivation relies on three key assumptions:

1. **Weak selection**  
    $$
    s \ll 1  
    $$
    
2. **Small per-generation change**  
    $$ 
    |p_{t+1} - p_t| \ll 1  
    $$
    
3. **Time measured in generations can be treated continuously**
    

Under these conditions, the finite difference can be approximated by a derivative:

$$  
p_{t+1} - p_t \;\approx\; \frac{dp}{dt}  
$$

---

## 3. Starting point: discrete selection dynamics

Consider a single-locus, two-allele system under viability selection with dominance:

$$  
\begin{aligned}  
w_{AA} &= 1 \\  
w_{Aa} &= 1 - hs \\  
w_{aa} &= 1 - s  
\end{aligned}  
$$

Let $(p)$ be the frequency of allele ($A$), and ($q = 1 - p$).

A general identity for allele-frequency change under selection is:

$$
\Delta p  
= p_{t+1} - p_t  
= \frac{pq}{\bar w}\,(w_A - w_a)  
$$

where:

- ($w_A$) and ($w_a$) are the **average fitnesses of alleles**,
    
- ($\bar w$) is the mean population fitness.
    

---

## 4. Allelic fitness difference

Under the above fitness scheme, the difference in allelic fitness is:

$$
w_A - w_a  
= s\Big[(1-h) + (2h-1)p\Big]  
$$

This term encodes the **dominance structure** of selection.

---

## 5. Weak-selection approximation

Under weak selection:

$$
\bar w = 1 - \mathcal{O}(s)  
\quad\Rightarrow\quad  
\frac{1}{\bar w} \approx 1  
$$

Thus, to first order in (s):

$$
\Delta p  
\approx  
s\,p(1-p)\Big[(1-h) + (2h-1)p\Big]  
$$

---

## 6. Continuous-time selection equation

Replacing the finite difference by a derivative yields the continuous-time model:

$$
\boxed{  
\frac{dp}{dt}=
s\,p(1-p)\Big[(1-h) + (2h-1)p\Big]  
}  
$$

This equation defines a **one-dimensional nonlinear dynamical system** on the interval ($p \in [0,1]$).

---

## 7. Interpretation of the terms

### 7.1 The factor ($p(1-p)$)

- Selection requires genetic variation
    
- When ($p = 0$) or ($p = 1$), no variation exists
    
- Therefore, boundary points are always equilibria
    

This structure is **independent of the fitness scheme**.

---

### 7.2 Dominance and low-frequency behavior

As ($p \to 0$):

$$
\frac{dp}{dt} \approx s(1-h)\,p  
$$

Consequences:

- ($h < 1$): selection is effective at low frequency
    
- ($h = 1$): selection is invisible when rare
    

**Recessive beneficial alleles behave nearly neutrally at low frequency.**

---

### 7.3 High-frequency behavior

As ($p \to 1$):

$$
\frac{dp}{dt} \approx s h (1-p)  
$$

Dominance effects diminish near fixation.

---

## 8. Fixed points and stability

The fixed points satisfy:

$$
\frac{dp}{dt} = 0  
$$

For directional selection (($0 \le h \le 1$)):

- ($p^* = 0$) — unstable
    
- ($p^* = 1$) — stable
    

Interpretation:

- Instability of (p=0) means loss of robustness to perturbation
    
- It does **not** imply population extinction
    

---

## 9. Phase-line interpretation

The continuous equation defines a **force field** on allele-frequency space.

For ($0 < p < 1$) and ($0 \le h \le 1$):
$$
\frac{dp}{dt} > 0  
$$

Thus:

- trajectories flow monotonically from ($p=0$) to ($p=1$)
    
- selection produces **fixation dynamics**
    

The phase line summarizes this behavior geometrically.

---

## 10. Conceptual significance

The continuous-time limit reveals that:

- selection acts as a **deterministic force**
    
- dominance controls **visibility**, not direction
    
- fixation is a global property of the force field
    
- mutation or drift are required to generate interior equilibria
    

This formulation provides the natural foundation for:

- mutation–selection balance
    
- diffusion approximations
    
- fitness landscapes and potential functions
    

---

## Links

- [[Selection(general)]]
    
- [[Fitness_scheme]]
    
- [[Allele_frequency]]
    
- [[Frequency dynamics]]
    
- [[Mutation_selection_balance]]
    
