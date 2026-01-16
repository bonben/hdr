# Application of Deep Learning for GNSS Denoising in a Spatial Context

## Context: The Anti-Jamming Challenge
Following several works carried out within the framework of research contracts with the company Arkane, a central issue emerged: the persistent vulnerability of Global Navigation Satellite Systems (GNSS) to interference and intentional jamming. This vulnerability is critical for autonomous systems, specifically in space environments (launchers, satellites) where signal integrity ensures mission success.

## State of the Art: The Complexity of Matrix Inversion
The project focuses on **Controlled Reception Pattern Antennas (CRPA)**, which use an antenna array to spatially filter the signal. The classical gold standard for such processing is **Space-Time Adaptive Processing (STAP)**.
*   **Mechanism**: STAP involves estimating the covariance matrix of the incoming noise and inverting it to compute optimal beamforming weights.
*   **FPGA Implementation Challenges**: Matrix inversion is computationally expensive ($O(N^3)$ complexity). State-of-the-art FPGA implementations, such as the work by **Zhang et al.**~\cite{Zhang2021}, employ advanced techniques like **LDL factorization based on Cholesky decomposition** and deeply pipelined triangular matrix inversion to achieve high throughput.
*   **Limitation**: Despite these optimizations, the resource consumption (DSP slices) scales rapidly with the antenna array size ($N$). For highly dynamic environments (e.g., spinning launchers) requiring ultra-low latency updates, even optimized matrix inversions become prohibitive on constrained avionics FPGAs.

## Methodology: Deep Learning as an Alternative
To overcome these limitations, the proposed Ph.D. work (Elise Lagarde) explores the integration of Deep Learning to replace or augment the classical processing chain.
*   **The Trend**: Recent literature confirms the potential of Deep Learning for interference mitigation. Models like **LcxNet**~\cite{LcxNet2024} or LSTM-based approaches~\cite{Munina2020} demonstrate robust detection and classification of jamming signatures.
*   **Algorithmic Shift**: We propose to replace the iterative matrix inversion with a **quantized CNN**. The network learns the mapping between antenna inputs and optimal weights (or clean signal), transforming an optimization problem ($O(N^3)$) into a fixed-latency inference problem ($O(1)$).
*   **FPGA Co-design**: Unlike generic software models, our focus is on **Hardware-Aware Training**. We constrain the neural network design (power-of-two quantization, structured pruning) specifically to fit within the DSP limits of radiation-hardened FPGAs, bridging the gap between academic DL models and space-grade hardware.

## Risks and Challenges
*   **Generalization to Unknown Jammers**: A fundamental risk is the behavior of the neural network when facing a jamming signature widely different from its training set. Unlike analytical STAP, which relies on physics, a CNN might hallucinate a solution outside its distribution.
*   **Data Scarcity**: Real-world jammed GNSS data is rare and often classified. We must rely heavily on high-fidelity simulators, introducing a "Sim-to-Real" gap that must be bridged.

## Long Term Goal
The ultimate objective is to produce a hardened, autonomous anti-jamming IP block for space launchers. This module would be capable of self-reconfiguration to adapt to evolving threat landscapes, directly contributing to the sovereignty of navigation solutions.
