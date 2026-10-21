---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/archive/open-weight-llm-architecture/
title: Open-weight LLM reference architecture on GDC air-gapped \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:21:36.633721+00:00
---

# Open-weight LLM reference architecture on GDC air-gapped  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/archive/open-weight-llm-architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Open-weight LLM reference architecture on GDC air-gapped Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This guide is deprecated. For the updated architecture, see the [Open-weight models on GDC air-gapped reference architecture](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/open-weight-models/reference-architecture).

Organizations operating in air-gapped environments face a significant challenge: they require the transformative power of Large Language Models (LLMs) but are strictly prohibited from connecting to external cloud-based APIs due to rigorous security protocols. To bridge this gap, these customers need a robust, self-contained ecosystem capable of hosting and managing open-weight models directly on their Google Distributed Cloud (GDC) air-gapped infrastructure. This localized deployment is essential for maintaining absolute data sovereignty, ensuring that sensitive information never leaves the physical premises. By integrating secure execution environments with local inference engines, users can leverage advanced AI capabilities while retaining full administrative control over their data, model weights, and internal security posture.

While [Gemini on GDC](https://cloud.google.com/distributed-cloud-air-gapped?e=48754805) provides powerful, managed frontier capabilities, customers often deploy open-weight models like _Gemma 4_ or _Llama 4_ for greater _granularity and control_. Deploying open-weight models on air-gapped GDC environments offers significant cost advantages over managed proprietary services. By owning the model weights, organizations eliminate recurring _per-token API fees_ , which can become prohibitive for high-volume, automated workloads. Furthermore, open-source models enable _quantization_ (for example, 4-bit or 8-bit), allowing high-performance reasoning to run on smaller, cheaper hardware footprints at the edge. This vertical optimization, combined with the ability to share infrastructure across multiple internal applications without extra licensing costs, results in a significantly lower _Total Cost of Ownership (TCO)_ for sustained, large-scale inference operations.

**Proposed solution**

This document outlines the reference architecture for deploying and managing open weight Large Language Models (LLMs) on Google Distributed Cloud (GDC) air-gapped environments. Many customers, especially those in highly regulated sectors, cannot use cloud-based LLM APIs due to strict data sovereignty and security requirements. This architecture addresses the need to run powerful LLMs locally within their own secure GDC instance.

**What is included:** This architecture covers the deployment of open-source LLMs (such as Gemma, Llama, DeepSeek) using either the vLLM or Ollama serving backends. It includes the use of Kubernetes for orchestration, Harbor for artifact storage, persistent volumes for model weights, and project network policies for network security.

**What isn't included:** This architecture doesn't cover managed AI Gateway services, proprietary models like Google's Gemini, model fine-tuning processes, or GenAI models for other modalities like image generation. These features will be covered in separate guides.

**Audience:** The primary audience for this document includes Platform Administrators responsible for deploying and managing services on GDC, and technical architects designing AI solutions within the air-gapped environment. End-users and developers who will interact with the deployed models are secondary audiences who benefit from understanding the underlying structure.

## Reference architecture

![Open-weight LLM reference architecture diagram.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/solutions/images/open-weight-llm-architecture.png)

## Solution components

The solution leverages the following components:

Solution Component | Responsibilities | Data Flow | Interfaces  
---|---|---|---  
**GDC air-gapped customer zone** | Hosts the Kubernetes clusters, networking, and storage infrastructure | Foundational Platform | Infrastructure management interfaces for the IO. Kubernetes API for Platform Admins and users  
**Load Balancer** | Exposes the LLM serving pods (vLLM, Ollama) to traffic from outside the Kubernetes cluster, providing a stable IP address. | External client requests are sent to the LoadBalancer's External IP. The LoadBalancer distributes the requests across the healthy backend pods (vLLM or Ollama) based on the Service's selector | Kubernetes Service API. Automatically provisions a network load balancer within the GDC environment.  
**vLLM** | High-throughput LLM inference serving. Optimized for low latency using techniques like PagedAttention. Typically serves one model per instance. | Receives HTTP inference requests from clients. Loads model weights from the mounted PVC. Performs computations on attached GPUs. Returns HTTP responses with generated text. | OpenAI-compatible RESTful API for inference. Accepts JSON requests.  
**Ollama** | LLM inference serving, designed for ease of use and managing multiple models within a single instance (though only one is active at a time) | Receives HTTP inference requests. Loads models (often bundled within the container image or pulled on first use if not air-gapped). Performs computations on GPUs. Returns HTTP responses. Models are unloaded after a period of inactivity. | Ollama RESTful API Accepts JSON requests. Also has a CLI.  
**Nvidia GPUs / MIG** | Provide hardware acceleration for LLM inference. | The LLM backends (vLLM, Ollama) offload the intensive model computations (matrix multiplications, etc.) to the GPUs to accelerate inference. MIG allows partitioning a single GPU to be used by multiple smaller model instances. | Exposed as a resource type in Kubernetes (e.g., `nvidia.com/gpu`). Pods request these resources  
**Harbor** | Securely stores and manages container images for vLLM, Ollama, and any helper pods (like busybox) | Container images are pushed from a build environment (e.g., a workstation with internet access) to Harbor. Kubernetes nodes pull these images from Harbor to run containers. | Docker Registry API. Kubernetes nodes interface with Harbor to pull images during pod creation. Users interface with Docker CLI or Harbor UI to push images.  
**Persistent Volume Claims** | Provides persistent storage for LLM model weights, decoupled from pod lifecycles. | Model files are copied into the Persistent Volume (e.g., using a helper pod and `kubectl cp`). The vLLM server reads model weights from this mounted volume at startup. Ollama typically bundles models within the image, so PVCs are less common for Ollama model storage in this setup. | Kubernetes storage API. Defined in YAML and mounted into pods as volumes.  
**Project Network Policy** | Enforces network isolation and controls traffic flow at the project/namespace level. Ensures only authorized traffic can reach the LLM services. | Network traffic to and from pods within the namespace is inspected. The policy rules dictate whether connections to the LLM service ports (e.g., 8000 for vLLM, 11434 for Ollama) are allowed, typically based on source IP ranges or other labels. | Kubernetes networking.gdc.goog/v1 API. Defined in YAML.  
  
### Features and capabilities

This reference architecture provides the following core capabilities:

  * **Open Weight LLM Serving:** Enables hosting and inference of various open weight models (for example, Gemma, Llama, DeepSeek). 
    * _Components:_ LLM Serving Backends (vLLM, Ollama), Kubernetes Deployments/Pods.
    * _Responsibilities:_ Loading model weights, managing the inference process, executing models on hardware accelerators, and exposing endpoints.
    * _Interfaces:_ REST APIs (OpenAI-compatible for vLLM, built-in API for Ollama) for inference requests, typically using JSON.
  * **Bring Your Own Model (BYOM):** Users can import and deploy their chosen open weight LLMs into the air-gapped environment. 
    * _Components:_ Harbor, Persistent Volume Claims, Kubernetes.
    * _Responsibilities:_ Secure storage of container images and model weights. Mechanism to transfer models into the environment and make them accessible to the serving engines.
    * _Interfaces:_ Docker Registry API (for Harbor), Kubernetes API (for PVCs and volume mounts).
  * **Hardware Accelerated Inference:** Leverages NVIDIA GPUs within the GDC cluster to run LLM inferences efficiently. 
    * _Components:_ NVIDIA GPUs, Kubernetes, Device Plugins.
    * _Responsibilities:_ Scheduling pods on nodes with GPU resources. Exposing GPU hardware to the LLM backend containers. Supports Multi-Instance GPU (MIG) for partitioning.
    * _Interfaces:_ Kubernetes API (for requesting GPU resources like `nvidia.com/gpu`).
  * **Network Controlled Access:** Ensures that access to the LLM inference endpoints is controlled and isolated within the GDC environment. 
    * _Components:_ Kubernetes Services (LoadBalancer), ProjectNetworkPolicy.
    * _Responsibilities:_ Exposing inference services using a stable IP. Defining and enforcing network rules to allow or deny traffic to the LLM backends based on source, destination, and ports.
    * _Interfaces:_ Kubernetes API (for Services and ProjectNetworkPolicy).
  * **Scalable Serving:** Allows for adjusting capacity based on demand. 
    * _Components:_ Kubernetes Deployments.
    * _Responsibilities:_ Enabling horizontal scaling by increasing the number of replicas for the LLM backend pods. Vertical scaling by adjusting resource requests/limits.
    * _Interfaces:_ Kubernetes API (for managing Deployment replicas and resources).



### Architectural principles

  * **Security First** : All components and data reside within the GDC air-gapped boundary, ensuring maximum data security and control. Network access is restricted using ProjectNetworkPolicies.
  * **Data Sovereignty** : Customers retain full control over their models and data, with no external connectivity required for operation.
  * **Open & Flexible**: The architecture leverages open-source serving backends (vLLM, Ollama) and supports a variety of open weight LLMs, giving customers choice and avoiding vendor lock-in for the inference engine.
  * **Component Decoupling** : Key functions like model storage (PVCs), image management (Harbor), and inference serving (vLLM/Ollama pods) are distinct components, allowing for independent management and updates.
  * **Scalability & Performance**: Designed to scale both horizontally by increasing the number of pod replicas and vertically by adjusting CPU/GPU resources to meet performance demands. vLLM is chosen for high-throughput, low-latency scenarios.
  * **Resource Optimization** : Supports NVIDIA Multi-Instance GPU (MIG) to allow smaller models to share GPU resources efficiently, maximizing hardware utilization.
  * **Standard Interfaces** : Built upon Kubernetes standards for orchestration, deployment, and service exposure. Inference endpoints provide REST APIs, with vLLM offering OpenAI compatibility.
  * **Resilience** : Leverages Kubernetes health checks and replication to ensure service availability.



## Considerations

  * **Scalability and Performance:**
    * Horizontal scaling is achieved by increasing the number of replicas in the Kubernetes Deployment for both vLLM and Ollama.
    * Vertical scaling involves allocating more CPU/memory and larger GPU slices, up to full GPUs.
    * vLLM serves one model per instance, requiring new Deployments for additional models. Ollama can manage multiple models but only runs one at a time.
    * PVC size significantly impacts model load times; 500GiB+ is recommended for high IOPS.
  * **Resource Management:**
    * Careful planning of GPU resources is essential. NVIDIA MIG can be used to partition GPUs for smaller models, improving utilization.
    * Adequate CPU and memory must be allocated to handle both inference and model management overhead.
    * Sufficient storage must be provisioned for PVCs to accommodate model sizes and ensure performance.
  * **Availability and Reliability:**
    * Kubernetes Deployments provide self-healing and rolling update capabilities.
    * LoadBalancer Services distribute traffic across healthy pods, masking individual pod failures.
    * Storing model weights on PVCs ensures persistence across pod restarts.
  * **Operational Complexity:**
    * Managing container images for different backends and versions in Harbor.
    * Procedures for securely transferring model weights into the air-gapped environment.
    * Creating and managing Kubernetes manifests (Deployments, Services, PVCs, Network Policies) for each model and backend.
    * Monitoring GPU utilization, inference latency, and error rates.
  * **Security and Compliance:**
    * The entire solution operates within the GDC air-gapped security perimeter.
    * ProjectNetworkPolicies are mandatory to enforce strict network isolation and control access to the LLM endpoints.
    * Harbor robot accounts and Kubernetes image pull secrets ensure secure access to container images.
    * Data in transit can be protected by Kubernetes network policies and any platform-level encryption. Data at rest on PVCs relies on GDC storage encryption.



## Design decisions

The following key design decisions have been made for this reference architecture:

### Decision 1: Offering both vLLM and Ollama versus only offering one inferencing model

Context | Key Decision | Rationale  
---|---|---  
Offer only one of the two choices for inferencing layers: VLLM and Ollama or offer both. | We decided to offer both as different users and use cases have varying requirements for performance, API compatibility, and ease of model management. | vLLM provides high-throughput, low-latency serving and OpenAI API compatibility, suited for production applications. Ollama offers a simpler setup, easier management of multiple models, and a user-friendly interface, better for development and experimentation. Supporting both provides flexibility.  
  
### Decision 2: Utilizing persistent storage versus object storage for vLLM model storage

Context | Key Decision | Rationale  
---|---|---  
vLLM requires model weights to be present on the file system at runtime. In an air-gapped environment, models cannot be downloaded on demand. | Using Persistent Volume Claims ensures model availability and improves startup time after the initial load, however it requires an initial step to populate the PVC, typically involving a helper pod | Persistent Volume Claims provide a resilient and persistent storage layer for large model files, decoupled from the vLLM pod lifecycle. This allows models to be loaded quickly on pod start.  
  
### Decision 3: Bundling models within Ollama Docker images versus standalone images

Context | Key Decision | Rationale  
---|---|---  
Ollama can download models, but this requires internet access, which is not available in air-gapped environments | Decision was made to bundle the images so that it simplifies runtime operation in the air-gapped environment as no external calls are needed, however to update or add models, the Docker image must be rebuilt and repushed to Harbor. | Building the Docker image with the models pre-downloaded ensures Ollama starts with the necessary models available offline.  
  
### Decision 4: Exposing vLLM and Ollama with LoadBalancer services versus no load balancer

Context | Key Decision | Rationale  
---|---|---  
LLM APIs need to be accessible to applications within the GDC environment. | Decision was made to expose services using a load balancer as this is the Standard Kubernetes approach for service exposure however this approach relies on the GDC platform's LoadBalancer provisioning. | Kubernetes Services of type LoadBalancer provide a standard, reliable method to expose the LLM backends, providing a stable IP address and distributing load.  
  
### Decision 5: Enforcing mandatory ProjectNetworkPolicy

Context | Key Decision | Rationale  
---|---|---  
Security and isolation are critical in GDC air-gapped deployments. | It was decided to enforce the ProjectNetworkPolicy as it Significantly enhances the security posture of the deployed LLM services even though it Requires careful definition of network policies | ProjectNetworkPolicies provide a Kubernetes-native way to enforce network isolation at the namespace level, ensuring only authorized traffic can reach the LLM services.  
  
## Assumptions and limitations

  * GDC air-gapped 1.15.1+ environment is available
  * Sufficient hardware resources (especially GPUs) are present in the standard cluster.
  * Harbor instance is set up and accessible.
  * Users have the necessary permissions (Namespace Admin, Cluster Developer).
  * Models are compatible with the chosen serving backends (vLLM/Ollama).



## User flow (end to end steps)

The following is a comprehensive user flow for deploying open weight Large Language Models (LLMs) on Google Distributed Cloud (GDC) air-gapped environments. The flow is divided into common setup, two deployment paths (vLLM and Ollama), and final validation.

### 1\. Common setup: Image management

Before deploying any LLM, you must configure how the GDC environment will pull container images from your private Harbor registry.

  * **Create Harbor Robot Account:** Generate a robot account in the Harbor UI and grant it "pull" permissions.
  * **Authenticate Docker:** Use the robot account credentials to sign in to Harbor from a machine with network access.
  * **Create Kubernetes Secret:** Create a docker-registry secret in your GDC project namespace using `kubectl` to store these Harbor credentials for the cluster to use.



### 2\. Deployment path A: vLLM (high throughput)

This path is recommended for serving performance-oriented models like Gemma-3.

  * **Acquire Image:** Pull the vLLM Docker image from the internet, tag it for your local Harbor registry, and push it to Harbor.
  * **Prepare Model Storage:**
    * Create a 500 GiB Persistent Volume Claim (PVC) to store model weights.
    * Download weights from Hugging Face on an internet-connected machine.
    * Use a temporary "helper pod" and `kubectl cp` to transfer these weights into the PVC within the GDC environment.
  * **Deploy Backend:** Apply a Kubernetes Deployment manifest that references the vLLM image and mounts the model weight PVC.
  * **Expose Service:** Create a `LoadBalancer` service to provide an external IP for the vLLM API.
  * **Secure Network:** Apply a `ProjectNetworkPolicy` to allow ingress traffic on the service port (typically 8000).



### 3\. Deployment path B: Ollama (ease of use)

This path focuses on a simplified setup where model weights are bundled or pre-loaded into the image.

  * **Build Custom Image:** Create a Dockerfile that installs Ollama and uses a `RUN` command to "pre-pull" specific models (e.g., `gemma3`) into the image layers.
  * **Push to Harbor:** Build the image locally and push it to your private Harbor registry.
  * **Deploy & Expose:** Create an Ollama Deployment and a `LoadBalancer` service.
  * **Secure Network:** Apply a `ProjectNetworkPolicy` for the Ollama port (11434).



### 4\. Validation and testing

Once deployed, the final steps involve verifying that the services are functional.

  * **Check Status:** Verify that pods are "Running" and services have been assigned external IP addresses.
  * **Test Inference:**
    * **vLLM:** Send a `curl` request to the vLLM `LoadBalancer` IP address using the OpenAI-compatible `/v1/chat/completions` endpoint.
    * **Ollama:** Send a `curl` request to the Ollama `LoadBalancer` IP address to the `/v1/completions` endpoint.



### 5\. Operations and scaling

  * **Vertical Scaling:** Increase GPU slices or move to multi-GPU configurations for larger models.
  * **Horizontal Scaling:** Increase the number of replicas in the deployment to handle more concurrent user requests.
  * **Troubleshooting:** Monitor logs using `kubectl logs` and check for common issues like FIPS self-test failures or network policy restrictions.



## Additional materials

  * [Solution reference implementation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/open-weight-llm-impl)
  * [Solution user guide](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/solutions/open-weight-llm-guide)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
