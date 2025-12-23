## 1. Assumptions
- Infinite population
- Random mating
- No mutation, no migration
- Viability selection
## 2. Fitness scheme
In a viability selection model, fitness represents relative survival from zygote to adulthood, not absolute survival probability. Genotypes with lower fitness contribute proportionally fewer individuals to the next generation.
Let genotype fitnesses be:
- $w_{AA} = 1$
- $w_{Aa} = 1$
- $w_{aa} = 1 - s$
## 3. Update rule
Let $p_t$ be allele $A$ frequency at generation $t$.

After selection:
$$
p_{t+1} = \frac{p_t}{1 - s(1 - p_t)^2}
$$
## 4. Fixed points
Solve $p_{t+1} = p_t$:
- $p = 0$
- $p = 1$
## 5. Stability
- $p = 1$ is stable
- $p = 0$ is unstable (if $s > 0$)
$p = 0$ is an unstable fixed point under positive selection, meaning that any introduction of the beneficial allele will drive the system away from this state.
## 6. Interpretation
Selection drives allele frequency toward fixation of the beneficial allele.

## Links
- [[Allele_frequency]]
- [[Frequency dynamics]]

Extensions:
- [[Dominance_selection]]
- [[Overdominance]]
