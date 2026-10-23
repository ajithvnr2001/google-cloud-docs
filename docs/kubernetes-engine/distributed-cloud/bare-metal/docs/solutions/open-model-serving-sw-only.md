---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/open-model-serving-sw-only/
title: Open model serving on Distributed Cloud software only reference architecture \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:42.437778+00:00
---

# Open model serving on Distributed Cloud software only reference architecture  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/open-model-serving-sw-only/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Open model serving on Distributed Cloud software only reference architecture Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

This **Solution Reference Architecture (SRA)** defines the conceptual design, component topology, and technical boundaries for hosting, serving, and validating open-weight Large Language Models (LLMs) on Distributed Cloud software only standalone clusters.

Enterprise edge environments often require low-latency inference and strict data sovereignty. This Solution Reference Architecture provides a standardized, secure, and observable serving stack to deploy the **Gemma 4 31B** model on a single-node Distributed Cloud software only cluster equipped with a customer-sourced **NVIDIA RTX PRO 6000 GPU (96GB VRAM)**.

**Important:** SRA versus SRI Scope. This document focuses on the architectural design and structural decisions. For concrete deployment manifests and step-by-step execution instructions, refer to the [Solution Reference Implementation (SRI)](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/open-model-serving-sw-only-implementation).

### Features and capabilities

  * **Local Model Serving:** Exposes an industry-standard, OpenAI-compatible API locally within the Distributed Cloud software only cluster boundary.
  * **Support for Large Edge Models:** Optimized to run Gemma 4 31B in native precision (BF16) or quantized formats, fully utilizing the 96GB VRAM capacity.
  * **Observability:** Integrates with Distributed Cloud software only's monitoring infrastructure (Google Cloud Managed Service for Prometheus) using native `PodMonitoring` resources to export GPU telemetry and vLLM performance metrics, avoiding the need for a standalone local Prometheus server.
  * **Interactive Validation:** Deploys a Gradio-based web interface for immediate, visual verification of model responsiveness.



### Architectural principles

  * **Simplicity and Portability:** Standardizes on Kubernetes native constructs (Deployment, Service) rather than complex serving operators, ensuring ease of deployment and maintenance on single-node setups.
  * **Data Sovereignty:** All inference traffic and prompt and response data remain strictly within the local cluster boundary.
  * **Resource Isolation:** Dedicates the physical GPU accelerator to a single model serving instance to prevent resource contention and guarantee predictable latency.



## Architecture and design

### Components

The solution components consist of:

  * **Customer Namespace (Distributed Cloud software only Cluster):**
    * **vLLM Serving Engine:** Deployed as a Kubernetes Deployment running the vLLM container. Configured to load Gemma weights from persistent storage and expose an OpenAI-compatible API.
    * **Gradio Web UI:** Deployed as a Kubernetes Deployment providing the chat interface for verification (Optional: Can also run externally on a developer workstation or test runtime connected to the cluster's vLLM service).
  * **Persistent Volume Claim (PVC):** Backed by Distributed Cloud software only local shared storage (using the `local-shared` StorageClass) to host the model weights.
  * **Kubernetes Services:** ClusterIP service for vLLM API endpoint; NodePort or LoadBalancer service for Gradio UI to expose it to the customer network.
  * **Infrastructure (Customer Managed):**
    * **NVIDIA GPU Operator:** Orchestrates and exposes the physical GPU resources to Distributed Cloud software only Kubernetes worker nodes.
    * **NVIDIA RTX PRO 6000 GPU:** The underlying physical accelerator (96 GB GDDR7 memory architecture).
  * **Google Cloud Integration:**
    * **Google Cloud Monitoring & Logging:** Default Distributed Cloud software only agents collecting and forwarding system logs, container logs, and basic metrics to Google Cloud.



### High-level architecture overview

The following diagram illustrates the flow of requests and component interactions within the Distributed Cloud software only cluster:

![Open model serving on Distributed Cloud software only architecture diagram.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/images/open-model-serving-sw-only-diagram.png)

### Hardware constraints

The solution is designed for customer-sourced hardware equipped with the NVIDIA RTX PRO 6000 Blackwell GPU.

  * **GPU Specification:** NVIDIA RTX PRO 6000 (Blackwell Server or Workstation Edition).
  * **Memory Architecture:** 96 GB GDDR7 VRAM (with ECC)
  * **Model Selection Impact:**
    * The 96 GB of VRAM allows running the target Gemma 4 31B model in native BF16 precision (occupying ~**62 GB** of weights and leaving ~**34 GB** of VRAM headroom for the Key-Value (KV) cache).
    * When Blackwell hardware-accelerated FP8 quantization (`--quantization=fp8`) is enabled—as configured in the reference implementation—model weight memory is halved to ~**31 GB** , expanding the available KV cache to **~56.5 GiB** (`61,728` tokens) at `--gpu-memory-utilization=0.95` and enabling large context windows or high concurrent batch sizes without encountering Out-of-Memory (OOM) errors.



## Supportability matrix (responsibilities)

Component | Managed by | Notes  
---|---|---  
Physical Hardware & OS | Customer | Customer-sourced hardware (specifically server or workstation with NVIDIA RTX PRO 6000 Blackwell GPU).  
Distributed Cloud software only Cluster Install | Customer | Must follow standard Distributed Cloud software only installation documentation.  
GPU Drivers & Operator | Customer | Installation of NVIDIA GPU Operator and Helm charts. Google does not support NVIDIA operator deployment.  
vLLM Serving Manifests | Google (Solution) | Provided as part of this solution guide.  
Model Artifacts | Customer | Downloading and hosting the Gemma model weights.  
Gradio UI and App Code | Customer | Customer-owned application layer for validation and use.  
Cloud Logging and Cloud Monitoring | Joint | Google provides default integration; Customer configures.  
  
## Concepts and technologies

This section details the functional components, their responsibilities, and how they communicate within the system. It identifies the core services, data storage units, and networking interfaces required to support the target use case.

### Infrastructure and platform

  * **NVIDIA RTX PRO 6000 GPU:** Provides 96GB GDDR7 VRAM. The physical GPU is dedicated entirely to the model serving instance. GPU partitioning (MIG) is not enabled to ensure the model has exclusive access to the full VRAM and memory bandwidth, preventing resource contention.
  * **NVIDIA GPU Operator:** Customer-managed operator that orchestrates and exposes the physical GPU resources to Distributed Cloud software only Kubernetes worker nodes.
  * **Node-Local Storage (Persistent Volume Claim):** Backed by Distributed Cloud software only node-local storage to host and persist the model weights on the node. This ensures that once model weights are downloaded, they are persisted locally. Subsequent pod restarts or updates load weights from this local cache, reducing startup time and protecting against WAN outages.
  * **Shared Memory Segment (`/dev/shm`):** An `emptyDir` volume with `medium: Memory` is mounted at `/dev/shm` and allocated 16GiB to prevent segmentation faults during high-concurrency tensor operations in vLLM.



### Services and logic

  * **vLLM Serving Engine:** Deployed as a Kubernetes Deployment running the Vertex AI-qualified vLLM container, exposed via a `ClusterIP` service (port 8000). Key configuration parameters include: 
    * `--model`: Path or ID of the Gemma model (e.g., `google/gemma-4-31B-it`).
    * `--tensor-parallel-size`: Set to `1` (single GPU constraint).
    * `--dtype`: Set to `bfloat16` to leverage hardware-native precision for non-quantized layers and activations.
    * `--quantization`: Set to `fp8` in the reference implementation to leverage Blackwell FP8 weight quantization (~31 GB weights, ~56.5 GiB KV cache), or omitted if unquantized BF16 (~62 GB weights, ~34 GB KV cache) is preferred.
  * **Gradio Web UI:** Deployed as a Kubernetes Deployment providing a chat interface for validation, exposed via a `ClusterIP` service (port 8080). It connects to the vLLM service for prompt and response interaction.



### Observability and Google Cloud integration

  * **Cloud Logging:** Uses default Distributed Cloud software only logging agents to automatically capture and forward container logs (vLLM application logs and GPU diagnostics) to Cloud Logging.
  * **Cloud Monitoring (PodMonitoring):** Google Cloud Managed Service for Prometheus (GMP) resources target both the vLLM pod (for serving telemetry like token throughput and KV cache usage) and the GPU exporter pod (for GPU telemetry), exporting metrics to Cloud Monitoring.



## Considerations

### Scalability and performance

  * **GPU Dedication:** The NVIDIA RTX PRO 6000 GPU is dedicated entirely to the vLLM container. Sharing the GPU via MIG or time-slicing is not implemented in this architecture to ensure predictable inference latency and prevent OOMs. The Gemma 4 31B model also require most of the VRAM capacity for the model weights (~62GB) which doesn't leave a lot of memory for other models to run concurrently.
  * **Deployment Strategy:** Enforced as `Recreate`. Since we only have one GPU, we cannot run two instances of the vLLM pod concurrently during an update. The old pod must be terminated to release the GPU lock before the new pod can start.



### Resource management

  * **VRAM Headroom:** While the 96 GB NVIDIA RTX PRO 6000 fits the Gemma 4 31B model in unquantized BF16 precision (~62 GB for weights, leaving ~34 GB for the KV cache), the reference deployment enables Blackwell FP8 quantization (`--quantization=fp8`) to reduce weight memory to ~31 GB and expand the available KV cache to **~56.5 GiB** (`61,728` concurrent tokens).
  * **KV Cache Sizing:** The SRA assumes the default vLLM allocation (`--gpu-memory-utilization=0.95`), which maximizes VRAM usage for the engine.



### Availability and reliability

  * **Cache Warmth:** The use of node-local PVs is critical. If the node restarts, the cached weights on the host directory are reused.
  * **Image Caching:** Because the vLLM container image is large (>10GB), it is recommended to set `imagePullPolicy: IfNotPresent` to avoid registry pull delays on pod restart.



### Operational complexity

  * **Console Visibility:** Unlike GKE, Distributed Cloud software only does not support the console-based "AI/ML Models" view. All validation and monitoring must be performed via the `kubectl` CLI, port-forwarding, and direct Cloud Monitoring dashboards.



## Design decision

### Inference engine: vLLM versus Triton versus Ollama

  * **Selected Option:** **vLLM**
  * **Rationale:** vLLM offers the best performance out-of-the-box for LLMs via PagedAttention, supports OpenAI API parity, and has pre-qualified container images from Vertex AI.
  * **Alternatives Rejected:**
    * _Triton:_ Too complex to configure and compile for a single-model edge deployment.
    * _Ollama:_ Lacks the advanced telemetry endpoints and granular concurrency tuning required for production monitoring.



### Telemetry path: native GMP versus local Prometheus

**Selected Option:** **Native GMP (`PodMonitoring`)**

  * **Rationale:** Distributed Cloud software only supports native integration with Cloud Monitoring. We can route metrics directly to Google Cloud using Managed Prometheus, reducing on-cluster operational overhead.
  * **Alternatives Rejected:**
    * _Local Prometheus and Grafana Stack:_ Rejected to minimize control plane resource usage on the single-node cluster.



## Assumptions and limitations

### Assumptions

  * **GPU Operator Availability:** It is assumed the customer has successfully installed the NVIDIA GPU Operator and configured the `nvidia` RuntimeClass prior to deploying this solution.
  * **Hugging Face Access:** The deployment requires a valid Hugging Face token with access to the gated Gemma 4 repository, stored as a Kubernetes Secret.
  * **Network Path:** The cluster must have internet access (or an internal proxy) to download the container image and model weights during the initial setup.



### Limitations

  * **Single-GPU Boundary:** The Phase 1 architecture is bounded by the physical capacity of a single NVIDIA RTX PRO 6000 GPU. Models larger than ~31B (or high-concurrency workloads requiring multi-GPU tensor parallelism) are not supported in Phase 1.
  * **No Rolling Updates:** The `Recreate` strategy implies a temporary service downtime during model updates or configuration changes, as the GPU cannot be shared between the old and new pods.
  * **Performance Tuning Excluded:** Consistent with the project scope, node-level optimizations (CPU pinning, hugepages, `PerformanceTuningProfile`) are excluded from this architecture.



## What's next

  * [Solution Reference Implementation (SRI)](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/solutions/open-model-serving-sw-only-implementation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
