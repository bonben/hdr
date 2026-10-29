### 2.2.4 [NOUVEAU] Split-Processing and Event-Based Vision for Edge AI

**Note:** This section ties into the recent work on YOLO for event detection in Search and Rescue scenarios, and synthetic data generation using Unreal Engine. It also introduces the PARADIS framework for NAS.

Event cameras, which capture data as a continuous stream of asynchronous events rather than dense frames, offer significant advantages in terms of latency, dynamic range, and power consumption. These characteristics make them highly suitable for Edge AI applications, such as UAV-based Search and Rescue.

However, the sparsity and continuous nature of incoming event streams (e.g., in formats like HDF5) present a challenge for conventional neural networks. To address this, we propose exploring a **Split-Processing** architecture.

1. **Tiny Edge Network for Background Filtering:** A very small neural network placed as close to the event sensor as possible. Its primary role is to filter out background noise or irrelevant events, triggering the downstream processing only when "interesting" motion or changes are detected (potentially supplemented by IMU data). By only sending relevant data, we drastically reduce the bandwidth and processing requirements downstream.
2. **Main Processing Unit:** A larger, more capable network (e.g., on a beefier embedded target or big GPUs) that receives the sliced, relevant event data and performs the main task, such as object detection (e.g., E-LoLa-YOLO).

**Challenges and Research Directions:**

*   **Automated Design for the Edge (NAS):** Designing the tiny edge network is challenging due to extreme complexity constraints (silicon area, power vs. the sensor itself). This is an ideal application for Neural Architecture Search (NAS). Specifically, frameworks like **ParaDis** (Parameter Distribution Shift NAS), developed with Timotée Ly-Manson, which uses parameter distribution statistics to constrain zero-cost proxies (ZCPs) to suitable regions of the search space, can be adapted to enforce the strict hardware limits of this near-sensor network.
*   **Ecosystem and Tools:** To implement and test these concepts, an evaluation of existing event-based ecosystems (like Prophesee's Metavision or iniVation's DV) is necessary to determine the best fit for prototyping split-processing pipelines and evaluating latency and energy savings. Collaboration with researchers like Jovita Lukasik (University of Siegen) will also drive this perspective forward.
