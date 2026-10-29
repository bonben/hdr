# Automated Neural/Hardware Architecture Search

## Context: The Design Bottleneck
The customization of RISC-V architectures and the design of Domain-Specific Architectures (DSA) for AI applications is a thriving field. Industrial tools and academic frameworks allow designers to map existing hot-spots of C code to custom instructions. However, these tools excel mainly at automating the *implementation* phase. They remain limited by human intuition: they optimize what the engineer explicitly expresses, but they do not *invent* new algorithmic primitives or discover non-intuitive architectural choices. As architectures become more complex, manual design space exploration by experts becomes a significant bottleneck.

## Methodology: Hardware Exploration Facilitated by Evolutionary Algorithms
Inspired by methods used to discover novel learning algorithms, we propose applying a "genetic exploration" methodology to the design of Domain-Specific Architectures. This approach aims to close the loop between generative agents (or algorithmic search methods) and rigorous simulation environments.

To realize this vision, our team has developed **MONET**, a tool designed to rapidly evaluate the performance of neural networks on specific hardware targets. The core principle of MONET is to decouple the software model (e.g., an ONNX representation of a neural network) from the hardware model (described flexibly in JSON). 
*   **Rapid Estimation**: MONET provides fast and accurate predictions of both latency and energy consumption for a given NN-to-Hardware mapping, without requiring full RTL synthesis or cycle-accurate simulations for every iteration.
*   **The Exploration Loop**: Building upon MONET, we aim to integrate this rapid estimator into an outer optimization loop—such as Genetic Algorithms, Bayesian Optimization, or Reinforcement Learning. 

## Vision: From Manual Design to Automated Invention
By using MONET as the "fitness function" within an automated search loop, the system can autonomously explore thousands of hardware configurations. 
*   **Genotype**: The search algorithm proposes variations in hardware architecture (e.g., MAC array sizes, memory hierarchy parameters, custom RISC-V instruction definitions).
*   **Evaluation**: MONET rapidly predicts the latency and energy of executing the target neural networks on this proposed hardware.
*   **Evolution**: The algorithm refines the hardware candidates, effectively navigating the non-convex design space of hardware acceleration.

This shifts the engineering effort from manual hardware design to defining the search space and the optimization constraints, paving the way for the discovery of truly innovative, non-intuitive hardware architectures that surpass human-designed baselines.
# Hardware Architectures for AI (PEPR CAMELIA)

## Context: The Shift to Transformers
Within the framework of the PEPR CAMELIA program (Composants pour l’Accélération Matérielle Et Logicielle de l’IA), our research focus is expanding towards the holistic design of hardware architectures specifically tailored for modern AI workloads. While Convolutional Neural Networks (CNNs) have long dominated embedded vision tasks, Transformer architectures are rapidly becoming the universal standard, not only for Natural Language Processing but also for vision (Vision Transformers) and audio processing.

## Objective: Co-designing Next-Generation Accelerators
The primary challenge of deploying Transformers on constrained hardware lies in the quadratic complexity of their Attention mechanism and their massive memory bandwidth requirements. To address this, I am establishing a new research axis targeting the hardware/software co-design of Transformer accelerators. This effort is supported by an incoming Ph.D. student (funded by the CEA) and a dedicated research engineer, both focusing on:
*   **Architectural Optimization**: Designing custom scalable processing elements and memory hierarchies that mitigate the memory wall associated with Large Language Models (LLMs) and Vision Transformers.
*   **Dataflow and Scheduling**: Developing new execution schedules that maximize data reuse (e.g., flash attention principles adapted for customized hardware) to improve energy efficiency.

This work aims to produce sovereign, high-performance hardware IPs capable of supporting the next generation of foundational models in embedded and edge environments.
