# HDT²: Entropy-Band Calibration for LLM Reasoning Stability

This repository accompanies the paper:

> Tisler, B. (2025). **HDT²: A Pilot Framework for Entropy-Band Calibration of LLM Reasoning Stability.**  
> Zenodo. https://doi.org/10.5281/zenodo.17621326

## Status

Public academic release. Code scaffold is being built to replicate:

- ψ* entropy-band definition
- UNSUP_H_ALIGN quantile alignment
- 7-gate validation protocol

## Install

pip install -r requirements.txt

## Layout (in progress)

- `src/hdt2/` – Python package for entropy, alignment, and gates  
- `paper/` – PDF(s) of the paper and supplementary artifacts  
- `examples/` – Notebooks showing how to run calibration and gates
