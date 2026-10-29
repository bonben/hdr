# Edge AI for Health: EEG Processing on Microcontrollers

## Context: The Strategic Choice of EEG
The decoding of Electroencephalographic (EEG) signals is moving from clinical setups to portable, wearable devices. Beyond the scientific challenges, focusing on EEG represents a strategic positioning for our research team. 
First, we have established a strong dynamic in this domain, highlighted by recent publications at NeurIPS, such as **REVE (A Foundation Model for EEG -- Adapting to Any Setup with Large-Scale Pretraining on 25,000 Subjects)**. 
Second, EEG analysis is an ideal target because the underlying neural models are significantly lighter compared to those required for high-resolution vision or complex text processing. This makes it a perfect match for institutions with constrained computing clusters, allowing us to remain highly competitive.
Finally, the transition of EEG processing to embedded systems is a mature and highly relevant field, as demonstrated by the literature (e.g., **Benini et al., \textit{EEGformer: Transformer-Based Epilepsy Detection on Raw EEG Traces for Low-Channel-Count Wearable Continuous Monitoring Devices}**). These devices operate under extreme energy constraints, typically relying on low-power microcontrollers (MCUs) like ARM Cortex-M or RISC-V equivalents, yet they must process multichannel time-series data with high temporal resolution.

## State of the Art: The Limits of CNNs
Currently, **Convolutional Neural Networks (CNNs)** like **EEGNet**~\cite{Lawhern2018} represent the state of the art for embedded EEG classification.
*   **Strengths**: They are compact and efficient at extracting local temporal and spatial features.
*   **Limitations**: CNNs struggle to capture *long-range dependencies* (global context) essential for identifying complex biomarkers (e.g., seizure onset patterns spanning several seconds).
*   **The Transformer Promise**: Transformer architectures (like the aforementioned EEGformer), with their **Self-Attention** mechanism, theoretically solve this by modeling global relationships. However, the computational complexity of the Attention map is quadratic $O(N^2)$ with the sequence length $N$. For an EEG sequence of just a few seconds ($N > 1000$), calculating and storing this matrix exceeds the limited SRAM of standard MCUs (often < 512KB).

## Methodology: Efficient Attention for Embedded Targets
Our research objective is to make Transformers feasible on microcontrollers by breaking the $O(N^2)$ barrier and optimizing memory geometry.
*   **Linear Attention Mechanisms**: We are exploring **Linear Attention** variants and State Space Models (SSMs) like **Bidirectional Mamba (FEMBA)**~\cite{tegon2025}, which reduce complexity to $O(N)$. This allows processing long sequences without a memory explosion.
*   **Hardware-Software Co-design**:
    *   **Quantization**: Implementing aggressive post-training quantization (int8) specifically validated for EEG dynamic ranges.
    *   **Tiling & Vectorization**: Adapting neural operators to utilize MCU-specific SIMD instructions (e.g., ARM CMSIS-NN) and designing memory-tiling strategies that keep the attention computation within the L1 cache or SRAM limits.
*   **Collaboration**: This work involves a close collaboration with **Giulia Lioi** (IMT Atlantique) to validate these architectures on clinically relevant datasets, ensuring that "efficient" does not mean "medically irrelevant".

## Long Term Goal
The ultimate goal is to enable a new class of **"Always-On" Neuro-Wearables**: autonomous headsets capable of detecting neurological events in real-time and locally, without transmitting raw privacy-sensitive data to the cloud.
