# Research Perspectives - Current State Review

**Document**: `hdr.tex`
**Chapter**: "Research Perspectives"
**Location**: Lines 2058 - 2110
**Total Content**: ~1200 words (approx. 4-5 pages in standard thesis format).

---

## 2.1 New Methods and Architectures for Channel Codes

### 2.1.1 Interest in Short Codes, Relevance of Polar Codes (2 paragraphs)
*   **Content**:
    *   Collaboration with ETS Montreal on the Generalized Restart Mechanism (GRM) for software polar decoders.
    *   Goal: Reduce execution time by 25-60% without error correction degradation using GRM on Successive-Cancellation Flip (SCF) and Fast-SCF.
    *   Extension to quantum polar codes (collaboration opportunities, SCL-C decoder adaptation).
    *   Mention of constructing polar codes adapted to SCF using deep learning (ISTC 2023 work).
*   **Volume**: ~190 words.

### 2.1.2 RISC-V Architectures for Channel Code Decoding (4 paragraphs)
*   **Content**:
    *   Motivation for RISC-V in embedded systems: open source, modularity, custom extensions.
    *   Plan for collaborative ANR (PRC) with Adrien Cassagne (LIP6) and Camille Leroux (Bordeaux INP).
    *   Goal: Design specialized RISC-V architectures with custom instructions for channel decoding acceleration.
*   **Volume**: ~190 words.

---

## 2.2 Network Specialization for Embedded Targets

### 2.2.1 Application of Deep Learning for GNSS Denoising (5 paragraphs)
*   **Content**:
    *   Context: Vulnerability of GNSS to jamming/interference.
    *   Project: CIFRE thesis (Elise Lagarde) with Arkane and Télécom Paris.
    *   Focus: Using Deep Learning (CNNs) to accelerate/simplify Controlled Reception Pattern Antennas (CRPA) spatiotemporal processing on FPGAs.
    *   Challenges: Real-time execution, model quantization, complexity reduction.
*   **Volume**: ~265 words.

### 2.2.2 Attention Layers on Microcontroller Targets for EEG Data Processing (3 paragraphs)
*   **Content**:
    *   Context: Processing EEG signals on embedded systems.
    *   Focus: Applying Transformers (Attention mechanisms) to EEG data on microcontrollers.
    *   Challenge: Long time sequences vs. limited resources.
    *   Plan: Hardware-software co-design, collaboration with Giulia Lioi (BRAIN team).
    *   Goal: Autonomous devices for neurotechnology/BCI.
*   **Volume**: ~175 words.

### 2.2.3 Co-design of Neural Networks and Embedded Hardware Architectures (4 paragraphs)
*   **Content**:
    *   Problem: Manual architecture design is suboptimal; standard NAS approaches using Zero-Cost Proxies (ZCPs) are biased towards large models.
    *   Proposed Solution: Pragmatic NAS techniques for lightweight architectures (Transformers/CNNs).
    *   Method: Sampling supernets guided by zero-shot metrics + parameter count constraints.
    *   Collaboration: Integration with "Stream" tool (MICAS team, KU Leuven) to model hardware suitability (mobility planned for Jérémy Morlier in 2025).
*   **Volume**: ~365 words.

---

## Expansion Strategy
To significantly lengthen this chapter (aiming to contribute to the 90-page goal), we should expand on the *methodology* and *preliminary analysis* for each section, rather than just stating the goals.

**Suggestion**:
1.  **Literature Review**: Add a paragraph in each section contextualizing the state-of-the-art more deeply.
2.  **Methodology**: Detail the specific steps (e.g., for RISC-V, which instructions? for NAS, which search space?).
3.  **Risk Analysis**: Discuss potential bottlenecks and fallback strategies.
4.  **Impact**: Elaborate on the societal/scientific impact.
