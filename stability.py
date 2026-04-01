#!/usr/bin/env python3
"""Triple-system stability criterion helper.

Implements the equations written in the manuscript subsection
"Dynamical Stability Criteria for Hierarchical Triple Systems".
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class StabilityResult:
    m_in: float
    rho_trial: float
    rho_limit: float
    e_crit: float | None
    stable: bool


def rho_of_e(e_out: float) -> float:
    if not (0.0 <= e_out < 1.0):
        raise ValueError("e_out must satisfy 0 <= e_out < 1")
    return math.sqrt(1.0 + e_out) / ((1.0 - e_out) ** 1.5)


def e_from_rho(rho_target: float, tol: float = 1e-10) -> float | None:
    if rho_target < 1.0:
        return None

    lo, hi = 0.0, 1.0 - 1e-12
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if rho_of_e(mid) < rho_target:
            lo = mid
        else:
            hi = mid
        if hi - lo < tol:
            break
    return 0.5 * (lo + hi)


def rho_limit_from_params(
    a_in: float,
    a_out: float,
    m_in: float,
    m_out: float,
    c_tr: float,
    alpha: float,
) -> float:
    if any(x <= 0 for x in [a_in, a_out, m_in, m_out, c_tr, alpha]):
        raise ValueError("all parameters must be positive")

    r = a_out / a_in
    m_tot = m_in + m_out

    # a_out/a_in = C_tr * rho(e_out)^(-alpha) * (Omega_in/Omega_out)^alpha
    # Omega_in/Omega_out = (a_out/a_in)^(3/2) * (M_in/M_tot)^(1/2)
    # -> rho_limit^alpha = C_tr * (M_in/M_tot)^(alpha/2) * (a_out/a_in)^(3*alpha/2 - 1)
    rhs = c_tr * (m_in / m_tot) ** (alpha / 2.0) * r ** (1.5 * alpha - 1.0)
    return rhs ** (1.0 / alpha)


def compute_stability(
    m1: float = 0.626,
    m2: float = 0.449,
    m_out: float = 0.565,
    a_in: float = 4.0,
    a_out: float = 123.0,
    e_out: float = 0.5,
    c_tr: float = 0.037,
    alpha: float = 2.0,
) -> StabilityResult:
    m_in = m1 + m2
    rho_trial = rho_of_e(e_out)
    rho_limit = rho_limit_from_params(a_in, a_out, m_in, m_out, c_tr, alpha)
    e_crit = e_from_rho(rho_limit)
    stable = rho_trial <= rho_limit

    return StabilityResult(
        m_in=m_in,
        rho_trial=rho_trial,
        rho_limit=rho_limit,
        e_crit=e_crit,
        stable=stable,
    )


if __name__ == "__main__":
    res = compute_stability()
    print(f"m_in      = {res.m_in:.6f} M_sun")
    print(f"rho(e_out)= {res.rho_trial:.6f}")
    print(f"rho_limit = {res.rho_limit:.6f}")
    print(f"e_crit    = {res.e_crit:.6f}" if res.e_crit is not None else "e_crit    = no solution (rho_limit < 1)")
    print(f"status    = {'STABLE' if res.stable else 'UNSTABLE'}")
