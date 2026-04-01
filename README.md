# Hierarchical Triple Stability & Kozai-Lidov Calculator

An interactive web tool for visualizing and exploring the **dynamical stability of hierarchical triple-star systems** and computing their Kozai-Lidov timescales.

## What This Tool Does

This calculator helps you:

1. **Explore orbital stability** in hierarchical triples using the quadrupole-order stability criterion from [Mardling (2001)](#references)
2. **Visualize the stable region** as a 2D map in the outer-orbit parameter space (*a*<sub>out</sub> vs *e*<sub>out</sub>)
3. **Apply observational constraints** by comparing theoretical stable regions against the observed projected separation (*s*<sub>obs</sub>) of the outer companion
4. **Compute Kozai-Lidov timescales** including the effect of the inner-binary eccentricity, with timescale variations across the stable region

### Key Features

- **Interactive orbital diagram** showing the hierarchical geometry (inner binary + distant companion)
- **2D stability map** with color-coded regions:
  - 🔵 Blue: dynamically stable orbits
  - 🟨 Gold: stable orbits **also compatible** with the observed outer separation
- **Live Kozai-Lidov panel** displaying:
  - *t*<sub>KL</sub> at three outer-eccentricity cases: *e*<sub>out</sub> = 0, *e*<sub>max</sub>/2, *e*<sub>max</sub>
  - Inner and outer orbital periods
  - Maximum stable eccentricity at the observation
- **Customizable inputs**: masses, semi-major axes, eccentricities, and model parameters
- **Fully client-side**: no backend required, runs entirely in your browser

---

## Quick Start

### Option 1: Online (Simplest)

1. Clone or download this repository
2. Open `index.html` directly in your web browser
3. Start adjusting parameters immediately

### Option 2: Local Server

```bash
cd stability_3bodies
python3 -m http.server 8000
```

Then open `http://localhost:8000` in your browser.

### Option 3: Python Standalone

For non-interactive calculations:

```bash
python3 stability.py
```

---

## How It Works

### The Stability Criterion

The tool implements the **quadrupole-order hierarchical triple stability criterion** (Mardling 2001):

$$\frac{a_\mathrm{out}}{a_\mathrm{in}} = C_\mathrm{tr} \cdot \rho(e_\mathrm{out})^{-\alpha} \cdot \left(\frac{\Omega_\mathrm{in}}{\Omega_\mathrm{out}}\right)^{\alpha}$$

where:
- $\rho(e) = \frac{\sqrt{1+e}}{(1-e)^{3/2}}$ (Mardling stability function)
- $C_\mathrm{tr}$ and $\alpha$ are model parameters (default: 0.037 and 2.0)
- $\Omega_i$ are mean motions

For a given outer separation *s*<sub>obs</sub>, the tool solves for the **maximum stable outer eccentricity** *e*<sub>max</sub>.

### The Kozai-Lidov Timescale

The tool computes the quadrupole-order Kozai-Lidov timescale:

$$t_\mathrm{KL} = \frac{8}{15\pi} \cdot \frac{M_\mathrm{tot}}{M_\mathrm{out}} \cdot \frac{P_\mathrm{out}^2}{P_\mathrm{in}} \cdot \frac{(1-e_\mathrm{out}^2)^{3/2}}{j_\mathrm{in}}$$

where $j_\mathrm{in} = \sqrt{1 - e_\mathrm{in}^2}$ accounts for inner-binary eccentricity.

---

## Input Parameters

### System Masses

(Default example: inner WD + M-dwarf + outer WD)

| Parameter | Default | Description |
|-----------|---------|-------------|
| M₁ | 0.626 M_sun | Primary of inner binary |
| M₂ | 0.449 M_sun | Secondary of inner binary |
| M<sub>out</sub> | 0.565 M_sun | Outer companion |

### Orbital Geometry & Eccentricities

| Parameter | Default | Description |
|-----------|---------|-------------|
| a<sub>in</sub> | 4.6 AU | Inner semi-major axis |
| s<sub>obs</sub> | 123.0 AU | Observed outer projected separation |
| e<sub>in</sub> | 0.19 | Inner-binary eccentricity (affects KL timescale) |

### Stability Model

| Parameter | Default | Description |
|-----------|---------|-------------|
| C<sub>tr</sub> | 0.037 | Normalization constant (Mardling 2001) |
| α | 2.0 | Power-law exponent (Mardling 2001) |

---

## Output Interpretation

### The 2D Stability Map

- **X-axis**: outer semi-major axis *a*<sub>out</sub> (AU)
- **Y-axis**: outer eccentricity *e*<sub>out</sub>
- **Dashed line**: vertical line at *s*<sub>obs</sub>—the observed separation
- **Blue region**: orbits satisfying the stability criterion
- **Gold region**: stable orbits where *s*<sub>obs</sub> ≤ *a*<sub>out</sub> (1 + *e*<sub>out</sub>/2)
- **Dark line**: stability boundary (*e*<sub>max</sub> as a function of *a*<sub>out</sub>)

### The Kozai-Lidov Panel

Shows the KL timescale at three representative outer eccentricities along the observed-separation line, plus inner/outer periods for reference. Use to estimate secular timescales for orbital-alignment oscillations.

---

## References

**Primary Reference:**
- **Mardling, R. A.** 2001, *Stability in the General Three-Body Problem*, ASP Conference Series, Vol. 229, p. 101
  - [ADS Link](https://ui.adsabs.harvard.edu/abs/2001ASPC..229..101M/abstract)

The tool follows the results and conventions in the Mardling paper, using the quadrupole-order hierarchical stability criterion and Kozai-Lidov timescale formulas.

---

## Technical Notes

- **No dependencies**: Pure HTML, CSS, and JavaScript—runs entirely in the browser
- **Interactive updates**: Every input change immediately recomputes the stability map and KL timescales
- **Numerical robustness**: Handles edge cases (e.g., rho_limit < 1 → no stable outer orbit at that separation)
- **Client-side only**: No data is sent to any server

---

## Files

- `index.html` — Interactive web interface (everything in one file)
- `stability.py` — Standalone Python implementation for batch calculations
- `README.md` — This file

---

## License & Attribution

If you use this tool in research, please cite [Mardling (2001)](#references) and acknowledge the interactive calculator.

---

## Questions or Contributions?

Feel free to open an issue or submit a pull request with improvements, bug fixes, or feature suggestions.
