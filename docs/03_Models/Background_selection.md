## 1. Definition

**Background selection** refers to the reduction of neutral genetic variation caused by **purifying selection acting on linked deleterious mutations**.

Key point:

> **Neutral alleles are lost not because they are bad, but because they are linked to bad alleles.**

Background selection is **not a force acting directly on neutral alleles**, but an emergent consequence of:

- negative (purifying) selection
    
- linkage
    
- finite recombination
    

---

## 2. Contrast with balancing selection (high-level intuition)

|Aspect|Balancing selection|Background selection|
|---|---|---|
|Effect on diversity|Maintains / increases|Reduces|
|Equilibrium|Internal stable|Boundary (loss)|
|Feedback|Negative (restoring)|One-sided (erosive)|
|Genealogies|Deep|Shallow|
|Long-term polymorphism|Yes|No|

These two regimes represent **opposite ends of selection’s effect on ancestry**.

---

## 3. Dynamical interpretation

### 3.1 State variables

At the focal neutral locus:

- allele frequency $p$
    

At linked loci:

- deleterious mutations with selection coefficient $s > 0$
    

The key insight:

> Neutral allele dynamics are **conditionally stochastic**, depending on the genetic background.

---

### 3.2 No restoring force

Unlike balancing selection, background selection does **not** generate:

$$  
\frac{dp}{dt} = f(p) \quad \text{with internal stable equilibrium}  
$$

Instead:

- deleterious backgrounds are continually purged
    
- neutral alleles on those backgrounds are lost with them
    

Thus, there is **no internal attractor** in allele-frequency space.

---

## 4. Effective population size reduction

Background selection acts by **reducing the effective population size**:

$$  
N_e^{\text{BGS}} < N_e  
$$

Classic approximation (Hudson & Kaplan):

$$
N_e^{\text{BGS}} \approx N_e \cdot e^{-U/s}  
$$

where:

- $U$ : deleterious mutation rate per region
    
- $s$ : selection coefficient
    

Interpretation:

> Background selection compresses ancestry into fewer surviving lineages.

---

## 5. Coalescent perspective (central insight)

### 5.1 Genealogical effect

Under background selection:

- lineages in bad backgrounds are quickly eliminated
    
- coalescent events occur faster
    
- trees are **shorter and more star-like**
    

Formally:  
$$
T_2^{\text{BGS}} < T_2^{\text{neutral}}  
$$

---

### 5.2 Comparison of genealogies

|Regime|Tree depth|Branch balance|
|---|---|---|
|Neutral|Moderate|Random|
|Balancing selection|Very deep|Structured|
|Background selection|Shallow|Star-like|

This is why background selection **mimics demographic bottlenecks**.

---

## 6. Linkage and recombination

Background selection is fundamentally a **linkage phenomenon**.

- Strong linkage → strong BGS
    
- High recombination → weak BGS
    

Spatial heterogeneity:

- Low recombination regions (centromeres, inversions): strong BGS
    
- High recombination regions: near-neutral behavior
    

Thus:

> Recombination decouples neutral alleles from deleterious fate.

---

## 7. Statistical signatures

Background selection produces characteristic population-genetic patterns:

- Reduced nucleotide diversity ($π$)
    
- Reduced heterozygosity
    
- Excess of rare variants
    
- Slightly negative $Tajima’s D$
    
- Elevated LD due to reduced effective population size
    

Critically:

> These patterns are **genome-wide and smooth**, not localized spikes.

---

## 8. Background selection vs selective sweeps

|Feature|Background selection|Selective sweep|
|---|---|---|
|Cause|Purifying selection|Positive selection|
|Time scale|Continuous|Episodic|
|Spatial pattern|Broad|Local|
|Genealogies|Persistently shallow|Temporarily shallow|
|Detectability|Hard|Easier|

This distinction is crucial in **population genomics inference**.

---

## 9. Role in nearly neutral theory

Background selection provides the **environment** in which nearly neutral evolution operates:

- Weakly deleterious mutations
    
- Drift + purifying selection
    
- Reduced effective population size amplifies drift
    

Thus:

> Background selection sets the baseline against which neutrality is tested.

---

## 10. Implications for GWAS and complex traits

Background selection explains:

- Depletion of common variants in low-recombination regions
    
- Enrichment of rare deleterious variants
    
- Confounding between selection and demography
    
- Apparent heritability differences across genomic regions
    

This links directly to:

- LD structure
    
- K-matrix interpretation
    
- polygenic architecture
    

---

## 11. Conceptual summary

> **Background selection is selection acting on ancestry, not on alleles.**

It:

- erodes variation
    
- shortens genealogies
    
- reduces effective population size
    
- reshapes the statistical baseline of the genome
    

Unlike balancing selection, it does **not** stabilize polymorphism — it silently removes it.

---

## 12. Position in the dynamics framework

Background selection belongs to:

- ❌ not pure frequency dynamics
    
- ❌ not classic force-balance
    
- ✅ ancestry-level dynamics
    
- ✅ coalescent-modified neutrality
    

It is the **bridge between selection and population genomics**.

---

## Links

- [[Balancing_selection]]
    
- [[Selection_continuous]]
    
- [[Genetic drift]]
    
- [[Coalescent_theory]]
    
- [[Site_frequency_spectrum]]
    
- [[Linkage_disequilibrium]]
    

---

