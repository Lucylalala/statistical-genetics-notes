## 1. Assumptions

- Single locus, two alleles $A$ and $a$
- Forward mutation rate: $μ (A → a)$
- Back mutation rate: $ν (a → A)$
- Infinite population (no drift)

## 2. Update rule

Let $p_t$ be the frequency of allele $A$ at generation $t$.

Then:
$$
p_{t+1} = p_t (1 - \mu) + (1 - p_t)\nu
$$

## 3. Interpretation

- First term: $A$ alleles that do not mutate
- Second term: a alleles that mutate into $A$

## 4. Fixed point

Solve:
$$
p_{t+1} = p_t
$$

Result:
$$
p^* = \frac{\nu}{\mu + \nu}
$$
The mutation–mutation equilibrium is determined by balance of allele fluxes rather than fitness optimization.

## 5. Dynamics

- Linear map
- Globally stable equilibrium
- No fixation unless μ = 0 or ν = 0

## Links

- [[Allele_frequency]]
- [[Frequency dynamics]]

