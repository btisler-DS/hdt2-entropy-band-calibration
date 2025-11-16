import numpy as np
from .entropy import shannon_entropy_bits, compute_token_entropies


def main() -> None:
    # Two simple toy distributions: one confident, one uncertain
    confident = np.array([0.95, 0.05], dtype=float)
    uncertain = np.array([0.5, 0.5], dtype=float)

    h_conf = shannon_entropy_bits(confident)
    h_unc = shannon_entropy_bits(uncertain)

    print("H(confident) =", h_conf, "bits")
    print("H(uncertain) =", h_unc, "bits")

    # Show list-style usage (like per-token entropies)
    topk_list = [confident, uncertain]
    entropies = compute_token_entropies(topk_list)
    print("Per-token entropies:", entropies)


if __name__ == "__main__":
    main()
