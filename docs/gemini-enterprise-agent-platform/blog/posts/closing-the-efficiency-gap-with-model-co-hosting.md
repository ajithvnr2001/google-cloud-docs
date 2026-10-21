---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/blog/posts/closing-the-efficiency-gap-with-model-co-hosting/
title: Closing the efficiency gap in LLM serving with model co-hosting with Vertex AI \u00a0|\u00a0 Cloud AI Engineering Blog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:49:12.420099+00:00
---

# Closing the efficiency gap in LLM serving with model co-hosting with Vertex AI  |  Cloud AI Engineering Blog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/blog/posts/closing-the-efficiency-gap-with-model-co-hosting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud AI Engineering Blog ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/blog)



Send feedback 

#  Closing the efficiency gap in LLM serving with model co-hosting with Vertex AI Stay organized with collections  Save and categorize content based on your preferences. 

March 19, 2026 

**Authors:** Ivan Nardini, Kathy Yu, and Jiuqiang Tang 

**Editor:** Elisa Bandy 

**TL;DR:** In the evolving landscape of large language models (LLMs), the "one model per machine" deployment pattern is becoming a significant bottleneck for LLM serving cost efficiency in enterprises. **Model co-hosting** addresses this efficiency gap by enabling multiple model instances to share the same virtual machine and GPU resources. This technical blog details Vertex AI Engineering's process in bringing model co-hosting to a production-ready cloud service. 

![](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/blog/posts/closing-the-efficiency-gap-with-model-co-hosting/images/fig2.svg)

Time to read: 11 minutes 

In the evolving landscape of [large language models (LLMs)](https://cloud.google.com/ai/llms?e=48754805), the "one model per machine" deployment pattern is becoming a significant bottleneck for **LLM serving** cost efficiency in enterprises. LLMs often require substantial hardware reservations, such as full [8x H100 GPU nodes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/predictions/configure-compute), to manage peak loads. However, during standard operations, these expensive resources often sit underutilized, leading to high total cost of ownership (TCO).

![Diagram representing the one model per machine pattern. Eight rectangles are
encapsulated in a larger box representing the machine. The last six rectangles
are greyed out and have a dashed outline. These represent the underutilized
resources. The first two rectangles have a solid outline. The second rectangle
is also greyed out, while the first rectangle has a blue background and is
labeled "Model A". These two rectangles represent the resources being used by
Model A.](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/blog/posts/closing-the-efficiency-gap-with-model-co-hosting/images/fig1.svg)

[Click to enlarge image](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/blog/posts/closing-the-efficiency-gap-with-model-co-hosting/images/fig1.svg)

**Model co-hosting** addresses this efficiency gap by enabling multiple model instances to share the same virtual machine and GPU resources. This includes entirely different models, such as [Llama 3.3](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/llama) and [Gemma 3](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/open-models/use-gemma). By utilizing sub-GPU memory slicing and intelligent resource partitioning, [Vertex AI Model Garden](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models) transforms static hardware reservations into flexible, high-density compute pools.

![Diagram representing the model co-hosting pattern. Three blue rectangles are
encapsulated in a larger box representing the high-density compute pool. The
boxes are labeled "Llama 3.3", "Gemma 3" and "Mistral 7B".](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/blog/posts/closing-the-efficiency-gap-with-model-co-hosting/images/fig2.svg)

[Click to enlarge image](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/blog/posts/closing-the-efficiency-gap-with-model-co-hosting/images/fig2.svg)

This technical blog details Vertex AI Engineering's process in bringing model co-hosting to a production-ready cloud service. We'll share our methodology for our container-level implementation strategies, identifying optimal serving configurations, and key findings from our extensive multi-model benchmark study, enabling you to maximize your LLM serving cost efficiency.

## Understanding model co-hosting: concept and architecture

Model co-hosting is a high-density serving strategy that enables multiple large language model (LLM) instances or different model architectures to share the same physical hardware resources within a single virtual machine (VM). Unlike traditional deployment models that dedicate a full VM or GPU to a single model, co-hosting utilizes granular resource partitioning to maximize hardware ROI and improve utilization of memory and computational resources.

Our implementation focuses on a container-level solution that allows for the simultaneous serving of multiple models with independent configurations. This architecture operates through several integrated technical mechanisms, starting with the deployment of multiple independent model server instances within a single container. Each of these instances serves as a full, independent copy of the model server, which enables simultaneous request processing across the virtual machine. To manage this traffic, we implemented an instance routing layer within the container that efficiently distributes incoming requests among the active instances.

This design provides granular parallelism by allowing each co-hosted model to utilize a dedicated serving configuration, featuring unique settings for _Tensor Parallelism (TP)_ , _Pipeline Parallelism (PP)_ , and the specific number of model instances. This is complemented by resource slicing, where specific GPU memory partitions are assigned to each model—such as a 0.4 GPU memory partition per model—to ensure that diverse workloads coexist on the same accelerator without starving one another of critical memory resources. This architectural approach transforms a static hardware reservation, such as a full 8x H100 GPU node, into a flexible compute pool capable of serving a diverse portfolio—ranging from large reasoning models to small, low-latency chat models.

![Flowchart depicting the instance routing implementation. Incoming requests are
directed into a container, where the requests are processed by an "Instance
Routing" component. This component then routes the requests to one of three
"VLLM Server \(Model\)" components: Model A, Model B, or Model C. Below the VLLM
servers, the diagram shows how GPU memory is partitioned. There are three GPU
memory portions: "Partition A \(40%\)", "Partition B \(30%\)", and "Partition C
\(30%\)".](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/blog/posts/closing-the-efficiency-gap-with-model-co-hosting/images/fig3.svg)

[Click to enlarge image](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/blog/posts/closing-the-efficiency-gap-with-model-co-hosting/images/fig3.svg)

## Prototyping and benchmark study

Before developing our production-ready orchestrator, we conducted a comprehensive benchmark study to validate the theoretical efficiency of model co-hosting. This phase aimed to thoroughly test [vLLM](https://github.com/vllm-project/vllm)'s native parallelism and precisely quantify the degree of "interference" when models share the same silicon.

### Parallelism investigation: Finding the "crossover point"

Our initial analysis focused on vLLM's native [Tensor Parallelism (TP)](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/features/parallelisms.html#tensor-parallelism) and Vertex implementation of model instances as multiple vLLM server instances to determine how these strategies interact with varying user loads. We discovered that the optimal configuration is highly dependent on concurrency; at lower concurrencies, a high Tensor Parallelism (e.g., TP=8) provides the lowest latency for individual requests by distributing layers across all available accelerators. However, as concurrent traffic increases, the bottleneck shifts. To maximize throughput under high-load conditions, the optimal configuration transitions from TP=8 to TP=4, TP=2, and eventually TP=1, while simultaneously increasing the number of independent model instances. This transition defines a "crossover point" where the benefits of reduced inter-GPU communication latency in low-TP setups outweigh the raw speed of high-TP execution. In the following, you have a crossover point chart with the Gemma 2 9B IT model.

![Line graph entitled "Gemma 2 9B IT Request Throughput, Light to Heavy
Traffic". The y-axis, labeled "Request throughput \(requests/sec\)," ranges from
0.000 to 100.000, with increments of 25.000. The x-axis is labeled "Concurrency"
and ranges from 1 to 1024. The graph displays five data series, each
representing different parallelization configurations: One line is for "TP=1,
DP=8". One line is for "TP=1, DP=1, 8 server instances". One line is for "TP=4,
DP 1, 2 server instances". One line is for "TP=2, DP=1, 4 server instances". One
line is for "TP=8, DP=1". All data series show similar logarithmic growth trends
to varying severities.](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/blog/posts/closing-the-efficiency-gap-with-model-co-hosting/images/fig7.svg)

[Click to enlarge image](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/blog/posts/closing-the-efficiency-gap-with-model-co-hosting/images/fig7.svg)

### Optimal scaling: Single-model, multi-replica

To establish a rigorous baseline for scalability, we benchmarked serving multiple instances of the same model on a single node. Under saturating traffic conditions (2048 concurrent requests per GPU), launching eight independent vLLM server instances on an 8xH100 node yielded an approximate **7.8 times throughput improvement** with virtually zero latency regression compared to a single-GPU baseline.

### Infrastructure comparison: Container vs. pod co-scheduling

We further evaluated our container-level orchestration against native infrastructure-level solutions, specifically [_Pod co-scheduling_](https://docs.cloud.google.com/vertex-ai/docs/predictions/configure-compute). While both solutions delivered comparable performance for multi-replica serving, we ultimately selected the container-level approach for our Minimum Viable Product (MVP). This decision was driven by the superior flexibility the container-level solution offers for _heterogeneous co-hosting_ , allowing developers to serve different model architectures side-by-side with granular, software-defined memory partitions that are not restricted by underlying Kubernetes scheduling constraints. In addition to that, the container-level orchestration allows iterating much faster and it is easier to customize and innovate.

### The interference test: Co-hosting different models

The final prototyping milestone was the "Interference Test," where we co-hosted Gemma-3n-E2B-it and Llama-3.1-8B-Instruct on the same VM. With each model assigned a 0.4 GPU memory partition, serving performance remained almost identical to single-model benchmarks. For example, Gemma-3n reached 30.21 reqs in a co-hosted environment compared to 30.96 reqs in isolation. These results confirm that there is little to no compute interference between co-hosted models, even under heavy traffic, provided that memory resources are appropriately partitioned to prevent [KV cache](https://huggingface.co/blog/not-lain/kv-caching) starvation.

## MVP container implementation

The transition from a validated benchmark to a production-ready system necessitated the engineering of a robust, containerized orchestrator. This development phase centered on building a high-level software layer capable of managing the complexities of multiple model lifecycles while ensuring deterministic resource isolation.

### Model co-hosting server design

The core of our implementation is the `model_cohost_server`, a custom entry point designed to act as a master orchestrator within the container. Deviating from the standard single-process model, this server implements sub-process management, facilitating the concurrent execution of multiple independent model server instances—such as vLLM—as isolated sub-processes. To manage incoming traffic, the orchestrator employs high-level request routing, identifying requests by their unique model identifiers via arguments such as `--served-model-name` and directing them to the corresponding internal server instance. Beyond routing, the server provides comprehensive **lifecycle orchestration** , managing the initialization, health monitoring, and termination of all co-hosted instances. This centralized management provides a single, unified endpoint for external traffic while maintaining the distinct operational boundaries of each sub-process.

![Flow diagram that illustrates the process for an incoming request through a
model co-host server. The process starts with an "Incoming request" which is
directed to the "Model Co-hosting Server". From there, the request goes to the
"Lifecycle Orchestration" component and then to "Model Co-hosting Router". The
router performs a "Model identifier check" and then directs the request to one
of three independent model server instances: "Independent Model Server Instance
\(Llama 3.3\)", "Independent Model Server Instance \(Gemma 3.0\)", or "Independent
Model Server Instance \(Mistral 7.0\)".](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/blog/posts/closing-the-efficiency-gap-with-model-co-hosting/images/fig4.svg)

[Click to enlarge image](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/blog/posts/closing-the-efficiency-gap-with-model-co-hosting/images/fig4.svg)

### GPU resource partitioning: Deterministic slicing

To eliminate the risk of a single model's workload triggering an Out-of-Memory (OOM) error across the co-hosted environment, we implemented a strict resource slicing mechanism. This is operationalized through the `gpu-memory-partition` argument, which allows developers to define explicit memory ratios (e.g., 0.4, 0.4) to reserve a fixed percentage of the total GPU memory of a node for each individual model instance.

To guide this allocation, we adopt a _"Pre-allocated vs. Transient" memory model_ , which distinguishes between static and dynamic resource requirements. "Pre-allocated" memory consists of memory used for the model weights and KV cache. The amount of memory used for the model weights depends on the model's parameter count and precision. For instance, an 8B parameter model in BF16 requires approximately 16GB of static storage. The amount of memory used for the KV cache depends on the model dimensions, precision, context length and number of sequences. **"Transient" memory** consists of intermediate computations and inference working memory. The `gpu-memory-partition` argument accounts for the "pre-allocated" memory. We recommend leaving buffer room for "transient" memory by setting the sum of `gpu-memory-partition`s to be smaller than 1.0.

![Diagram illustrating GPU memory partitions, divided into three sections. The
first section is labeled "Partition A \(0.40\)" and contains subsections for two
types of memory: "Pre-allocated Memory \(Model parameters, KV cache\)" and
"Transient Memory \(Working memory\)." The section section is labeled "Partition B
\(0.4\)" and contains two subsections similar to the first partition. The final
section is labeled "System/Overhead \(0.2\)."](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/blog/posts/closing-the-efficiency-gap-with-model-co-hosting/images/fig5.svg)

[Click to enlarge image](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/blog/posts/closing-the-efficiency-gap-with-model-co-hosting/images/fig5.svg)

## Productization

The productization phase of model co-hosting with Vertex AI was dedicated to establishing a seamless, production-ready environment for both single-model multi-replica and multi-model serving configurations. This transition effectively translated empirical benchmark findings into simplified deployment workflows and deeply integrated infrastructure support structures.

### Simplified deployment workflows

To lower the barrier to entry for high-density serving, we standardized co-hosting configurations using custom container arguments that integrate natively with existing [Vertex AI APIs](https://docs.cloud.google.com/vertex-ai/docs/reference/rest). For full-shape virtual machines, such as an 8x H100 node, we developed a [benchmark util](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_model_cohost.ipynb) to customize the best recipes for your specific use cases. These benchmark util would allow you to find the configuration which automatically balances Tensor Parallelism (TP), [Pipeline Parallelism (PP)](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/features/parallelisms.html#pipeline-parallelism), and the number of model instances based on the specific parameter count and precision of the model. This is complemented by robust Deployment API support, allowing developers to specify these granular parameters—including exact GPU memory partitions—directly within a standard [deployModel](https://docs.cloud.google.com/vertex-ai/docs/general/deployment) request and deploy models.

## Dynamic multi-model serving

A significant advancement in our technical journey was the transition from static configurations to a dynamic serving architecture. This capability is critical for production environments characterized by rapidly shifting traffic patterns, as the ability to load or unload models without a full container restart is essential for maintaining infrastructure agility and high availability.

### The Dynamic Update API (`update_models`)

To address the inherent limitations of immutable deployments, we implemented a specialized model update API within the Vertex Model Garden vLLM model co-hosting container. This API facilitates _hot re-loading_ , enabling the server to adjust its portfolio of hosted models on-the-fly based on a centralized configuration file stored in a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs).

The update process is initiated via a POST request to the `update_models` endpoint, which includes the `model_config_path` pointing to the Cloud Storage YAML file. Upon receiving this request, the server executes a multi-stage orchestration sequence optimized for minimal downtime:

  * **Graceful unloading** : The system identifies models absent from the new configuration and terminates their sub-processes first, immediately reclaiming GPU memory and compute resources.
  * **Intelligent loading and re-use** : The server then initializes new model instances. Crucially, if a model's parallelism settings—such as Tensor Parallelism (TP) or Pipeline Parallelism (PP)—and its allocated memory partition remain unchanged, the orchestrator re-uses the existing running instance. This optimization bypasses the costly re-initialization phase, ensuring that active services remain uninterrupted during configuration shifts.



![Flow diagram depicting dynamic multi-model serving. The top-most node is
labeled "Post /update_models API Request \(with 'model_config_path'\)" and flows
into a node labeled "Read Cloud Storage YAML Config." The "Read Cloud Storage YAML Config" node
flows into a node labeled "Server Orchestration," which flows into two nodes to
the left and right. The left node is labeled "Graceful unloading \(removed
models\)," and the right node is labeled "Intelligent loading \(new/changed
models, reuse unchanged instances\)." Both nodes flow into a node labeled
"Updated models active."](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/blog/posts/closing-the-efficiency-gap-with-model-co-hosting/images/fig6.svg)

[Click to enlarge image](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/blog/posts/closing-the-efficiency-gap-with-model-co-hosting/images/fig6.svg)

### Latency and performance analysis

Empirical analysis of these update strategies reveals that dynamic hot re-loading substantially mitigates the "cold start" penalty commonly associated with large-scale LLM serving.

## Conclusion

Model co-hosting with Vertex AI represents a fundamental paradigm shift, transitioning from rigid, hardware-heavy monolithic deployments to a fluid and efficient serving architecture. By evolving beyond the "one-model-per-VM" standard into a high-density compute pool model, organizations can significantly reduce their Total Cost of Ownership (TCO) while maintaining—and often improving—performance benchmarks.

Our engineering journey and extensive multi-model benchmark studies have established a definitive set of production guidelines for this architecture:

  1. There is no one-size-fits-all configuration. We advocate for finding the best serving recipe for a specific use case (model, hardware, traffic), and build tools for doing so.
  2. Scaling throughput with replicas.
  3. Improve resource utilization by breaking hardware boundaries and splitting memory at a more granular level.



To successfully implement a co-hosted architecture, we recommend the following technical workflow:

  1. **Explicit partitioning** : Employ the `--gpu-memory-partitions` argument to allocate memory resources for individual models.
  2. **Iterative benchmarking** : Utilize the provided Benchmark Utility to identify the specific "Concurrency Crossover" point for your workload—the "sweet spot" configuration of number of instances, TP and PP.



The implementation of co-hosting on Google Cloud Model Garden provides a scalable blueprint for building high-density AI applications. Developers are encouraged to explore these capabilities and reproduce our benchmarks using the provided [tutorial notebook](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_model_cohost.ipynb) to optimize serving configurations for their specific enterprise requirements.

## Thanks for reading

We welcome your feedback and questions about Vertex AI.

  * Ivan Nardini: [LinkedIn](https://www.linkedin.com/in/ivan-nardini/) and [X](https://twitter.com/IlNardo92)
  * Kathy Yu: [LinkedIn](https://www.linkedin.com/in/feiyang-kathy-yu-9818b7169)
  * Jiuqiang Tang: [LinkedIn](https://www.linkedin.com/in/jiuqiang-tang-51bb1665)



## Acknowledgements

We would like to express our sincere gratitude to the Google Cloud Vertex AI team. Specifically, we thank Bo Wu and Ting Yu for their leadership and guidance, as well as Deborah He, Shawn Ma, Desmond Liu, Yang Pan, Surya K G Tangatur, and Luis Rizo for their invaluable contributions, throughout this project.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
