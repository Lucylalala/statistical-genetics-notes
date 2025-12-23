Study of how allele frequencies change across generations
due to evolutionary forces.
Core components:
- [[Allele_frequency]] (state variable)
- [[Selection(general)]], [[Genetic drift]], [[Mutation]], [[Migration]] (drivers)
- [[Wright_Fisher_model]] (population model)
- [[Coalescent_theory]] (time perspective)
- [[Site_frequency_spectrum]] (statistical consequence)

See also [[What_is_statistical_genetics_about]].

## 1. State variable
- Allele frequency $p$
- Genotype frequencies ($p², 2pq, q²$)
- Multiallelic extension
→ [[Hardy_Weinberg_equilibrium]]
→ [[Allele_frequency]]

## 2. Time
- Discrete generations
- Continuous-time approximation
- Scaling with Nₑ
## 3. Update rules
General form:
$$
p_{t+1} = f(p_t; \theta)
$$

where θ includes:
- Selection coefficients
- Mutation rates
- Migration rates
- Drift (stochasticity)
## 4. Deterministic vs stochastic dynamics
- Infinite population limit
- Finite population (sampling noise)
