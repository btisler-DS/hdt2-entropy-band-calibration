from typing import List
import numpy as np


def shannon_entropy_bits(probs: np.ndarray) -> float:
    """
    Compute Shannon entropy in bits for a 1D probability vector.

    probs: np.ndarray of shape [k], already normalized.
    """
    probs = np.asarray(probs, dtype=float)
    mask = probs > 0
    p = probs[mask]
    return float(-(p * np.log2(p)).sum())


def compute_token_entropies(topk_probs: List[np.ndarray]) -> List[float]:
    """
    Compute entropy per token from a list of top-k probability arrays.

    topk_probs: list of np.ndarray[k], each representing renormalized top-k probabilities.
    """
    return [shannon_entropy_bits(p) for p in topk_probs]
