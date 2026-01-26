Population structure describes the non-random distribution of allele frequencies
across individuals due to subdivision of a population into partially isolated
subpopulations.

It is the most fundamental deviation from the idealized assumptions of:
- Hardy–Weinberg equilibrium
- panmixia (random mating)
- a single, well-mixed population

Population structure is therefore a *state of the population*, not an evolutionary
process itself.

---

## 1. Why population structure matters

Population structure matters because most statistical genetic models implicitly
assume that all sampled individuals are drawn from a single, randomly mating population.

When this assumption is violated:
- allele frequencies vary across subpopulations,
- genotype frequencies deviate from Hardy–Weinberg expectations,
- loci may appear correlated even without physical linkage,
- spurious associations arise in GWAS.

Thus, population structure is the primary source of confounding in population
genetic inference.

> **Population structure transforms individual-level randomness into population-level bias.**
---

## 2. Formal definition (allele frequency perspective)


Consider a biallelic locus with alleles $A$ and $a$.

Let the population be subdivided into K subpopulations.
In subpopulation k, the allele A has frequency $p_k$.

Population structure exists if:
$p_1 ≠ p_2 ≠ ... ≠ p_K$

The fundamental object in population structure is not genotype,
but the distribution of allele frequencies across subpopulations.

---

## 3. Sampling from a structured population

Suppose a sample is drawn by pooling individuals from multiple subpopulations.

Let:
- $w_k$ be the proportion of samples from subpopulation $k$
- $p_k$ be the allele frequency in subpopulation $k$

The overall allele frequency in the pooled sample is:
$$
p = Σ_k w_k p_k
$$
---

## 4. Wahlund effect (loss of heterozygosity)


Even if each subpopulation is in Hardy–Weinberg equilibrium,
the pooled population generally is not.

Expected heterozygosity within subpopulations:
$H_within = Σ_k w_k 2 p_k (1 - p_k)$

Expected heterozygosity under pooled allele frequency:
$H_total = 2 p (1 - p)$

In structured populations:
$H_within > H_total$

**Wahlund effect**
Population structure creates an apparent deficit of heterozygotes,
not because of inbreeding or selection,
but because alleles are sampled from different frequency backgrounds.

---

## 5. Population structure as drift in parallel

Population structure arises naturally through genetic drift acting independently
in different subpopulations.

Starting from the same ancestral population:
- random drift causes allele frequencies to diverge,
- different populations explore different evolutionary trajectories.

Thus, population structure is the spatial imprint of genetic drift.

> **Population structure is drift observed across space rather than time.**

---

## 6. Differentiation and F-statistics (intuition only)

Genetic differentiation between populations is commonly summarized by F-statistics.

$F_ST$ measures the fraction of total genetic variance that is explained by
between-population differences in allele frequency.

Conceptually:
$F_ST = Var(p_k) / Var_total$

At the core level, F_ST quantifies how much allele frequency variation

---

## 7. Migration vs population structure

Population structure reflects a balance between two forces:
- genetic drift, which differentiates populations,
- migration, which homogenizes allele frequencies.

Strong drift + weak migration → strong structure
Weak drift + strong migration → weak structure

> **Migration erodes structure; drift builds it.**
---

## 8. Relation to other core concepts

Population structure directly affects:

- Hardy–Weinberg equilibrium (via Wahlund effect)
- Linkage disequilibrium (via admixture LD)
- Allele frequency dynamics
- Variance dynamics

Population structure provides the conceptual foundation for:
- GWAS K matrix
- Structured coalescent
- Local ancestry and haplotypes
---
## 9. What this chapter does NOT cover

This core chapter intentionally does not cover:
- inference methods (PCA, ADMIXTURE, STRUCTURE),
- structured coalescent theory,
- likelihood-based models.

These topics are treated in later Model-level notes.

---
## Links

- Hardy_Weinberg_equilibrium
- Genetic_drift
- Migration
- Linkage_disequilibrium
- GWAS_K_matrix
- Structured_coalescent
---