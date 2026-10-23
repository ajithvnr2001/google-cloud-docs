---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/inference/
title: About AI/ML model inference on GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:01.013292+00:00
---

# About AI/ML model inference on GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/inference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  About AI/ML model inference on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes the key concepts, benefits, and steps for running generative AI/ML model inference workloads on Google Kubernetes Engine (GKE), using GKE Gen AI capabilities. 

Inference serving is critical in deploying your generative AI models to real-world applications. GKE provides a robust and scalable platform for managing your containerized workloads, making it a compelling choice for serving your models in development or production. With GKE, you can use Kubernetes' capabilities for orchestration, scaling, and high availability to efficiently deploy and manage your inference services.

Recognizing the specific demands of AI/ML inference, Google Cloud has introduced **GKE Gen AI capabilities** —a suite of features specifically designed to enhance and optimize inference serving on GKE. For more information about specific features, see GKE Gen AI capabilities.

If you are new to GKE, expand the following section to get an overview of GKE and Kubernetes fundamentals:

  * **GKE clusters and nodes:** All Kubernetes workloads run on _nodes_. In GKE, a node is a Compute Engine virtual machine (VM). On other Kubernetes platforms, a node could be either a physical or virtual machine. Each node is managed by the Kubernetes control plane and has all the necessary components to run Pods. A _cluster_ is a set of nodes that can be treated together as a single entity, on which you deploy a containerized application.
  * **Pods and Deployments:**
    * In Kubernetes, containerized applications run inside a _Pod_. A Pod is the smallest deployable unit of computing that you can create and manage in Kubernetes. A Pod has one or more _containers_.
    * A _Deployment_ is a Kubernetes API object that lets you run multiple replicas of Pods that are distributed among the nodes in a cluster.
  * **GKE modes of operation:**
    * **Autopilot:** in this mode, GKE fully manages the cluster's nodes, including configuration, scaling, and security. You don't need to provision or manage the node infrastructure; you focus on deploying your applications (Pods).
    * **Standard:** this mode provides complete control over node configuration. You create and manage groups of nodes called node pools. Autopilot simplifies operations and is suitable for many inference workloads, as it supports accelerators. Standard mode might be preferred if you need fine-grained control over node types or specific configurations to optimize performance or cost, beyond what Autopilot offers.



## Get started with AI/ML model inference on GKE

You can start exploring AI/ML model inference on GKE in minutes. You can use GKE's [free tier](https://cloud.google.com/kubernetes-engine/pricing#cluster_management_fee_and_free_tier), which lets you get started with Kubernetes without incurring costs for cluster management.

  1. [Go to the GKE AI/ML page in Google Cloud console](https://console.cloud.google.com/kubernetes/aiml/overview)

  2. Try the [Deploy Models](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart#console) steps to deploy a containerized model and model server.
  3. Read [Overview of inference best practices on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference), which has guidance and resources for planning and running your inference workloads on GKE.



## Terminology

This page uses the following terminology related to inference on GKE:

  * **Inference** : the process of running a generative AI model, such as a large language model or diffusion model, within a GKE cluster to generate text, embeddings, or other outputs from input data. Model inference on GKE leverages accelerators to efficiently handle complex computations for real-time or batch processing.
  * **Model** : a generative AI model that has learned patterns from data and is used for inference. Models vary in size and architecture, from smaller domain-specific models to massive multi-billion parameter neural networks that are optimized for diverse language tasks.
  * **Model server** : a containerized service responsible for receiving inference requests and returning inferences. This service might be a Python app, or a more robust solution like [vLLM](https://docs.vllm.ai/en/latest/), [JetStream](https://github.com/AI-Hypercomputer/JetStream), [TensorFlow Serving](https://github.com/tensorflow/serving), or [Triton Inference Server](https://github.com/triton-inference-server/server). The model server handles loading models into memory, and executes computations on accelerators to return inferences efficiently.
  * **Accelerator** : specialized hardware, such as [Graphics Processing Units](https://cloud.google.com/gpu) (GPUs) from NVIDIA and [Tensor Processing Units](https://cloud.google.com/tpu) (TPUs) from Google, that can be attached to GKE nodes to speed up computations, particularly for training and inference tasks.
  * **Quantization** : a technique used to reduce the size of AI/ML models and improve inference speed by converting model weights and activations from higher-precision data types to lower-precision data types.



## Benefits of GKE for inference

Inference serving on GKE provides several benefits:

  * **Efficient price-performance:** get value and speed for your inference serving needs. GKE lets you choose from a [range of powerful accelerators (GPUs and TPUs)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/inference#obtainability), so you only pay for the performance you need.
  * **Faster deployment** : accelerate your time to market with tailored best practices, qualifications, and best practices provided by GKE Gen AI capabilities.
  * **Scalable performance** : scale out performance with prebuilt monitoring by using [GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway), [Horizontal Pod Autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) (HPA), and custom metrics. You can run a range of pre-trained or custom models, from 8 billion parameters up to 671 billion parameters.
  * **Full portability** : benefit from full portability with open standards. Google contributes to key Kubernetes APIs, including [Gateway](https://gateway-api.sigs.k8s.io/) and [LeaderWorkerSet](https://github.com/kubernetes-sigs/lws), and all APIs are portable with Kubernetes distributions.
  * **Ecosystem support** : build on GKE's robust ecosystem which supports tools like [Kueue](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/kueue-intro) for advanced resource queuing and management, and [Ray](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/concepts/overview) for distributed computing, to facilitate scalable and efficient model training and inference.



## How inference on GKE works

This section describes, at a high-level, the steps to use GKE for inference serving:

  1. **Containerize your model** : To _containerize_ an application is to create a _container image_ , which is an executable package that includes everything needed to run the application: code, runtime, system tools, system libraries, and settings. A simple application can be containerized as a single unit, while a more complex application can be broken up into multiple, containerized components. Deploy a model by containerizing the model server (such as vLLM), and loading model weights from Cloud Storage or a repository like Hugging Face. When you use [GKE Inference Quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart), the containerized image is automatically managed in the manifest for you.

  2. **Create a GKE cluster** : create a [GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/learn/get-started-with-kubernetes#nodes) to host your deployment. Choose Autopilot for a managed experience or Standard for customization. Configure the cluster size, node types, and accelerators. For an optimized configuration, use [Inference Quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart).

  3. **Deploy your model as a Kubernetes Deployment** : create a [Kubernetes Deployment](https://docs.cloud.google.com/kubernetes-engine/docs/learn/get-started-with-kubernetes#controllers) to manage your inference service. A _Deployment_ is a Kubernetes API object that lets you run multiple replicas of Pods that are distributed among the nodes in a cluster. Specify the Docker image, replicas, and settings. Kubernetes pulls the image and runs your containers on the GKE cluster nodes. Configure the Pods with your model server and model, including [LoRA](https://arxiv.org/abs/2106.09685) adapters if needed.

  4. **Expose your inference service** : make your inference service accessible by creating a [Kubernetes Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) to provide a network endpoint for your Deployment. Use [Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway) for intelligent load balancing and routing that's specifically tailored for generative AI inference workloads, or see the [comparison of load balancing strategies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/choose-lb-strategy) to choose the best option for your needs.

  5. **Handle inference requests** : send data from your application clients to your Service's endpoint, in the expected format (JSON, gRPC). If you are using a load balancer, it distributes requests to model replicas. The model server processes the request, runs the model, and returns the inference.

  6. **Scale and monitor your inference deployment** : scale inference with HPA to automatically adjust replicas based on CPU or latency. The Horizontal Pod Autoscaler (HPA) is a Kubernetes controller that automatically increases or decreases the number of Pods in a workload (such as a Deployment) based on observed metrics like CPU utilization or custom metrics. Use [Inference Quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart) to get auto-generated scaling recommendations. To track performance, use Cloud Monitoring and Cloud Logging with prebuilt observability, including dashboards for popular model servers like [vLLM](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/vllm).




For detailed examples that use specific models, model servers, and accelerators, see Inference examples.

## GKE Gen AI capabilities

You can use these capabilities together or individually to address key challenges in serving generative AI models and improving resource utilization within your GKE environment, at no additional cost.

Name | Description | Benefits  
---|---|---  
[GKE Inference Quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart) |  Analyze the performance and cost-efficiency of your inference workloads. Specify your business needs and get tailored best practices for the combination of accelerators, scaling and storage configurations, and model servers that best meets your needs. You can access this service with the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) and Google Cloud console. For more information, see [Analyze model serving performance and costs with GKE Inference Quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart). | 

  * Saves time by automating the initial steps of choosing and configuring your infrastructure.
  * Lets you maintain full control over your Kubernetes setup for further tuning.

  
[GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway) | Get routing based on metrics, like KV cache utilization, for better latency. For more information, see [About GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway) | 

  * Share fined-tuned models that use LoRA files, with affinity-based endpoint picking for cost-efficiency.
  * Achieve high availability by dynamically accessing GPU and TPU capacity across regions.
  * Enhance the security of your models with Model Armor add-on policies.

  
[Model weight loading accelerators](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/storage-overview) | Access data in Cloud Storage quickly using [Cloud Storage FUSE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cloud-storage-fuse-csi-driver) with [caching and parallel downloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf). For more information about using Cloud Storage FUSE for AI/ML workloads, see the [reference architecture](https://docs.cloud.google.com/architecture/optimize-ai-ml-workloads-cloud-storage-fuse). [Google Cloud Managed Lustre](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managed-lustre) is a high performance, fully managed parallel file system optimized for AI that can attach to 10,000 or more Pods. For more information about using Managed Lustre for AI/ML workloads, see the [reference architecture](https://docs.cloud.google.com/architecture/optimize-ai-ml-workloads-managed-lustre). [Google Cloud Hyperdisk ML](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/hyperdisk-ml) is a network-attached disk that can be attached to up to 2,500 Pods. | 

  * Optimize inference startup time by minimizing weight loading model latency on GKE.
  * For deployments with limited node scaling, consider using Cloud Storage FUSE to mount model weights.
  * For inference workloads that demand consistent scale out performance, Google Cloud Managed Lustre supports high-throughput and low-latency file access from multiple Pods simultaneously.
  * For massive-scale scenarios demanding consistent, low latency access to large model weights, Google Cloud Hyperdisk ML offers a dedicated block storage solution.

  
  
## Inference performance metrics

To optimize your inference workloads, it's important to understand how to measure their performance. The following table describes the key metrics for benchmarking inference performance on GKE.

Benchmark indicators | Metric (unit) | Description  
---|---|---  
Latency | Time to First Token (TTFT) (ms) | Time it takes to generate the first token for a request.  
Normalized Time Per Output Token (NTPOT) (ms) | Request latency normalized by the number of output tokens, measured as `request_latency / total_output_tokens`.  
Time Per Output Token (TPOT) (ms) | Time it takes to generate one output token, measured as `(request_latency - time_to_first_token) / (total_output_tokens - 1)`.  
Inter-token latency (ITL) (ms) | Measures latency between two output token generations. Unlike TPOT, which measures latency across the entire request, ITL measures the time to generate each individual output token. These individual measurements are then aggregated to produce mean, median, and percentile values such as p90.  
Request latency (ms) | End-to-end time to complete a request.  
Throughput | Requests per second | Total number of requests that you serve per second. Note that this metric might not be a reliable way to measure LLM throughput because it can vary widely for different context lengths.  
Output tokens per second | A common metric that is measured as `total_output_tokens_generated_by_server / elapsed_time_in_seconds`.  
Input tokens per second | Measured as `total_input_tokens_generated_by_server / elapsed_time_in_seconds`.  
Tokens per second | Measured as `total_tokens_generated_by_server / elapsed_time_in_seconds`. This metric counts both input and output tokens, helping you compare workloads with high prefill versus high decode times.  
  
## Planning for inference

A successful inference deployment requires careful planning across several key areas, including cost-efficiency, performance, and flexibility, efficiency, and availability of accelerator capacity. For detailed recommendations on how to build a scalable, performant, and cost-effective inference platform, see [Overview of inference best practices on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference).

## Try inference examples

Find GKE deployment examples for generative AI models, accelerators, and model servers. If you are just getting started, we recommend exploring the [Serve Gemma open models using GPUs on GKE with vLLM](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-gpu-vllm) tutorial.

**Tip:** For production deployments on GKE, we strongly recommend using [Inference Quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart).

GPUsTPUsvLLMMaxDiffusionRay ServeTorchServeTGI

Or, search for a tutorial by keyword:

Accelerator | Model Server | Tutorial  
---|---|---  
GPUs | vLLM |  [Serve LLMs like DeepSeek-R1 671B or Llama 3.1 405B on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-multihost-gpu)  
GPUs | vLLM |  [Serve Gemma open models using GPUs on GKE with vLLM](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-gpu-vllm)  
GPUs | vLLM |  [Serve an LLM with GKE Inference Gateway ](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-with-gke-inference-gateway)  
GPUs | vLLM |  [Serve open LLMs on GKE with a pre-configured architecture ](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-open-models-terraform)  
GPUs | Ray Serve |  [Serve an LLM on L4 GPUs with Ray ](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/serve-llm-l4-ray)  
GPUs | TGI |  [Serve an LLM with multiple GPUs in GKE ](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-multiple-gpu)  
GPUs | TorchServe |  [Serve T5 on GKE with TorchServe ](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scalable-ml-models-torchserve)  
TPUs | vLLM |  [Serve an LLM using TPU Trillium on GKE with vLLM](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-vllm-tpu)  
TPUs | vLLM |  [Serve an LLM using TPUs on GKE with KubeRay ](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-lllm-tpu-ray)  
TPUs | MaxDiffusion |  [Serve Stable Diffusion XL (SDXL) using TPUs on GKE with MaxDiffusion](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-sdxl-tpu)  
TPUs | vLLM |  [Serve LLMs using multi-host TPUs on GKE with JetStream and Pathways](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-multihost-tpu-jetstream)  
TPUs | vLLM |  [Serve open LLMs on TPUs with a pre-configured architecture ](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-open-models-tpu-terraform)  
  
## What's next

  * Visit the [AI/ML orchestration on GKE portal](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra) to explore our official guides, tutorials, and use cases for running AI/ML workloads on GKE.
  * Explore experimental samples for leveraging GKE to accelerate your AI/ML initiatives in [GKE AI Labs](https://gke-ai-labs.dev/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
