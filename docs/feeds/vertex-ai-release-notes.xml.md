---
url: https://docs.cloud.google.com/feeds/vertex-ai-release-notes.xml
title: Vertex AI - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:45.650443+00:00
---

# Vertex AI - Release notes

> Source: https://docs.cloud.google.com/feeds/vertex-ai-release-notes.xml

tag:google.com,2016:vertex-ai-release-notesVertex AI - Release notesGoogle Cloud Platform2026-03-16T00:00:00-07:00March 16, 2026tag:google.com,2016:vertex-ai-release-notes#March_16_20262026-03-16T00:00:00-07:00Deprecated 

Vertex Explainable AI is deprecated. For details, see [Vertex AI deprecations](https://docs.cloud.google.com/vertex-ai/docs/deprecations).

]]> March 05, 2026tag:google.com,2016:vertex-ai-release-notes#March_05_20262026-03-05T00:00:00-08:00Announcement 

**Vector Search 2.0 is generally available (GA)**

Vector Search 2.0 is generally available ([GA](https://cloud.google.com/products/#product-launch-stages)).

Vector Search 2.0 is a retrieval engine designed to streamline AI development and serve as the knowledge core for AI applications.

Available features:

  * [Collections](https://docs.cloud.google.com/vertex-ai/docs/vector-search-2/collections/collections) unifying data and vectors.
  * Auto-embeddings for populating vector fields automatically.
  * Hybrid search and ranking combining vector, full-text, and built-in semantic re-ranking in a single parallel query.
  * Private Service Connect (PSC), Private Google Accesss (PGA), and VPC Service Controls support.



For more information, see the [Vector Search 2.0 documentation](https://docs.cloud.google.com/vertex-ai/docs/vector-search-2/overview).

]]> February 17, 2026tag:google.com,2016:vertex-ai-release-notes#February_17_20262026-02-17T00:00:00-08:00Deprecated 

Vertex AI Feature Store Optimized online serving is deprecated. For details, see [Vertex AI deprecations](https://docs.cloud.google.com/vertex-ai/docs/deprecations).

### Deprecated

Vertex AI Feature Store (Legacy/V1) is deprecated. For details, see [Vertex AI deprecations](https://docs.cloud.google.com/vertex-ai/docs/deprecations).

]]> September 30, 2025tag:google.com,2016:vertex-ai-release-notes#September_30_20252025-09-30T00:00:00-07:00Feature 

[DeepSeek-V3.2-Exp](https://console.cloud.google.com/vertex-ai/publishers/deepseek-ai/model-garden/deepseek-v3-2) is available through Model Garden.

]]> September 22, 2025tag:google.com,2016:vertex-ai-release-notes#September_22_20252025-09-22T00:00:00-07:00Feature 

[DeepSeek-V3.1-Terminus](https://console.cloud.google.com/vertex-ai/publishers/deepseek-ai/model-garden/deepseek-v3-1;publisherModelVersion=deepseek-v3-1-terminus) is available through Model Garden.

]]> September 15, 2025tag:google.com,2016:vertex-ai-release-notes#September_15_20252025-09-15T00:00:00-07:00Feature 

**Vector Search indexes optimized for storage (Preview)**

Storage-optimized Vector Search offers a cost-effective solution for searching massive datasets. This new tier is ideal for large-scale RAG and semantic search applications, and simplifies development with a new auto-tuning feature that eliminates the need to manage the underlying index configuration. This feature is available in Preview.

For more information, see [Storage-optimized Vector Search](https://docs.cloud.google.com/vertex-ai/docs/vector-search/storage-optimized-vector-search).

]]> September 10, 2025tag:google.com,2016:vertex-ai-release-notes#September_10_20252025-09-10T00:00:00-07:00Breaking 

**Vertex AI Agent Engine**

In version `v1.112.0` of the Vertex AI SDK for Python, the `agent_engines` module has been refactored to a [client-based design](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview#migration). For information about updating your existing code to the new design, see the [Migration guide](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/deprecations/agent-engine-migration).

### Feature

**Vertex AI Agent Engine**

Agent Engine now supports the following features:

  * Agent Engine **Code Execution** , now in Preview, lets your agent run code in an isolated sandbox environment. For more information, see [Code Execution](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/code-execution/overview).

  * You can now develop, deploy, and use agents that support the **Agent-to-Agent (A2A) protocol** on Agent Engine. For more information, see [Develop an Agent2Agent agent](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/develop/a2a).

  * Agent Engine now supports **bidirectional streaming**. For more information, see [Bidirectional streaming](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/bidirectional-streaming).

  * The [Vertex AI Agent Engine page](https://console.cloud.google.com/vertex-ai/agents/agent-engines) in the Google Cloud console has a **Memory Bank** tab for displaying and managing memories.


]]> September 09, 2025tag:google.com,2016:vertex-ai-release-notes#September_09_20252025-09-09T00:00:00-07:00Feature 

[EmbeddingGemma](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/embeddinggemma) and [DeepSeek-V3.1](https://console.cloud.google.com/vertex-ai/publishers/deepseek-ai/model-garden/deepseek-v3-1) models are available through Model Garden.

### Feature

[AI Singapore's SEA-LION V4 models](https://console.cloud.google.com/vertex-ai/publishers/aisingapore/model-garden/gemma-sea-lion-v4) are available through Model Garden. They are open models for Southeast Asian languages, built by leveraging Vertex AI training clusters for enhanced training efficiency and model accuracy.

]]> August 21, 2025tag:google.com,2016:vertex-ai-release-notes#August_21_20252025-08-21T00:00:00-07:00Feature 

**Vertex AI Agent Engine**

Agent Engine now supports the following enterprise security features:

  * You can now deploy your agents in a private VPC environment, configuring a Private Service Connect interface, to ensure data privacy and meet security and compliance requirements. For more information, see [Configure Private Service Connect interface](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/deploy#psc-i).

  * You can now use your own [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/manage/access#cmek) to protect data at rest.

  * You can now specify [customized resource controls](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/deploy#customized-resource-controls), such as the minimum and maximum number of application instances, resource limits for each container, and concurrency for each container.

  * As a part of Vertex AI, Vertex AI Agent Engine supports [HIPAA](https://cloud.google.com/security/compliance/hipaa) workloads.




For more information, see [Agent Engine overview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview#enterprise_security).

]]> August 14, 2025tag:google.com,2016:vertex-ai-release-notes#August_14_20252025-08-14T00:00:00-07:00Feature 

[Gemma 3 270M](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/gemma3;publisherModelVersion=gemma-3-270m-it), [Wan 2.2](https://console.cloud.google.com/vertex-ai/publishers/wan-ai/model-garden/wan2-2) and [Wan 2.1](https://console.cloud.google.com/vertex-ai/publishers/wan-ai/model-garden/wan2-1) models are available through Model Garden.

]]> August 13, 2025tag:google.com,2016:vertex-ai-release-notes#August_13_20252025-08-13T00:00:00-07:00Feature 

[Qwen3 Coder](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/maas/qwen/qwen3-coder) and [Qwen3 235B](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/maas/qwen/qwen3-235b) are available as Model as a Service (MaaS) models in Model Garden.

### Feature

OpenAI's [gpt-oss-120b](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/maas/openai/gpt-oss-120b) and [gpt-oss-20b](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/maas/openai/gpt-oss-20b) are available as Model as a Service (MaaS) models in Model Garden.

]]> August 06, 2025tag:google.com,2016:vertex-ai-release-notes#August_06_20252025-08-06T00:00:00-07:00Feature 

[OpenAI's gpt-oss](https://console.cloud.google.com/vertex-ai/publishers/openai/model-garden/gpt-oss) models are available through Model Garden.

]]> July 16, 2025tag:google.com,2016:vertex-ai-release-notes#July_16_20252025-07-16T00:00:00-07:00Feature 

Added [Gemma 3](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/community/model_garden/model_garden_axolotl_gemma3_finetuning.ipynb) fine-tuning notebook using Axolotl docker with support for 1b, 4b, 12b, and 27b variants.

]]> July 14, 2025tag:google.com,2016:vertex-ai-release-notes#July_14_20252025-07-14T00:00:00-07:00Feature 

[Multimodal MedGemma 27B IT](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/medgemma;publisherModelVersion=medgemma-27b-it), [MedSigLIP](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/medsiglip), and [T5Gemma](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/t5gemma) models are available through Model Garden.

]]> July 11, 2025tag:google.com,2016:vertex-ai-release-notes#July_11_20252025-07-11T00:00:00-07:00Feature 

To reduce the cost of running your inference jobs, you can use flex-start VMs, which are powered by [Dynamic Workload Scheduler](https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler). Flex-start VMs offer significant discounts and are well-suited for short-duration workloads. This feature is available in [Preview](https://cloud.google.com/products/#product-launch-stages).

For more information, see [Use DWS flex-start VMs with inference](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-flex-start-vms).

]]> July 01, 2025tag:google.com,2016:vertex-ai-release-notes#July_01_20252025-07-01T00:00:00-07:00Feature 

The global endpoint is generally available (GA) for Anthropic's Claude Opus 4. For details, see [Global endpoint](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/locations#global-endpoint).

]]> June 30, 2025tag:google.com,2016:vertex-ai-release-notes#June_30_20252025-06-30T00:00:00-07:00Deprecated 

Mistral Nemo, which is offered as a Model as a Service (MaaS) model in Model Garden, is deprecated. For details, see [Model as a Service (MaaS) deprecations](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/deprecations/partner-models).

### Deprecated

Anthropic's Claude 3 Opus, which is offered as a Model as a Service (MaaS) model in Model Garden, is deprecated. For details, see [Model as a Service (MaaS) deprecations](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/deprecations/partner-models).

### Feature

Vertex AI now offers GA support of Private Service Connect Interface and includes Private DNS Peering. For more information, see [Use Private Service Connect interface for Vertex AI Training](https://docs.cloud.google.com/vertex-ai/docs/training/psc-i-egress).

### Feature

Private Service Connect interface (PSC-I) support for ML pipeline runs in Vertex AI Pipelines is now [generally available](https://cloud.google.com/products#product-launch-stages). PSC-I is recommended for private connectivity because it reduces the chance of IP exhaustion, allows for transitive peering, and includes Private DNS Peering.

For more information, see [Configure Private Service Connect interface for a pipeline](https://docs.cloud.google.com/vertex-ai/docs/pipelines/configure-private-service-connect).

### Feature

Vertex AI online inference now offers Preview support of PSC service automation that can automatically create PSC endpoints for dedicated private endpoints. For more information, see [Create the online inference endpoint with PSC automation](https://docs.cloud.google.com/vertex-ai/docs/predictions/private-service-connect#create-endpoint-with-automation).

]]> June 27, 2025tag:google.com,2016:vertex-ai-release-notes#June_27_20252025-06-27T00:00:00-07:00Feature 

[Gemma 3n](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/gemma3n) models are available through Model Garden.

]]> June 24, 2025tag:google.com,2016:vertex-ai-release-notes#June_24_20252025-06-24T00:00:00-07:00Deprecated 

The Generative AI module in the Vertex AI SDK is deprecated. For information about migrating to the Google Gen AI SDK, see the [migration guide](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/deprecations/genai-vertexai-sdk).

]]> June 10, 2025tag:google.com,2016:vertex-ai-release-notes#June_10_20252025-06-10T00:00:00-07:00Feature 

**Vector Search custom constraints with Organization Policy**

You can use custom constraints with the Organization Policy Service to provide more granular control over specific fields for indexes and index endpoints in Vector Search.

For more information, see [Create custom constraints for Vector Search](https://docs.cloud.google.com/vertex-ai/docs/vector-search/custom-constraints).

]]> May 15, 2025tag:google.com,2016:vertex-ai-release-notes#May_15_20252025-05-15T00:00:00-07:00Announcement 

Vertex AI custom training supports the following accelerators:

  * A3 Ultra
  * A4



Vertex AI online prediction supports the following accelerators:

  * A3 Mega
  * A4



For regional availability of accelerators, see [Using accelerators](https://docs.cloud.google.com/vertex-ai/docs/general/locations#accelerators).

]]> April 16, 2025tag:google.com,2016:vertex-ai-release-notes#April_16_20252025-04-16T00:00:00-07:00Announcement 

[Persistent resources](https://docs.cloud.google.com/vertex-ai/docs/training/persistent-resource-overview) for custom training is generally available ([GA](https://cloud.google.com/products#product-launch-stages)) and supports rebooting.

]]> March 27, 2025tag:google.com,2016:vertex-ai-release-notes#March_27_20252025-03-27T00:00:00-07:00Feature 

**Generally available** : To reduce the cost of running your training and prediction jobs, you can use Spot VMs. Spot VMs are virtual machine (VM) instances that are excess Compute Engine capacity. Spot VMs have significant discounts, but Compute Engine might preemptively stop or delete Spot VMs to reclaim the capacity at any time.

For more information, see [Use Spot VMs with training](https://docs.cloud.google.com/vertex-ai/docs/training/use-spot-vms) and [Use Spot VMs with prediction](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-spot-vms).

]]> March 26, 2025tag:google.com,2016:vertex-ai-release-notes#March_26_20252025-03-26T00:00:00-07:00Feature 

**Generally available** : You can consume reservations of VMs that have GPUs attached with your custom training jobs or prediction jobs. Reservations of Compute Engine zonal resources help you gain a high level of assurance that your jobs have the necessary resources to run. For more information, see the following:

  * [Use reservations with training](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations)

  * [Use reservations with prediction](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations)


]]> January 31, 2025tag:google.com,2016:vertex-ai-release-notes#January_31_20252025-01-31T00:00:00-08:00Feature 

[Dedicated Public Endpoints ](https://docs.cloud.google.com/vertex-ai/docs/general/deployment#deploy_a_model_to_an_endpoint)and [Private Service Connect Endpoints (PSC-E)](https://docs.cloud.google.com/vertex-ai/docs/predictions/private-service-connect) for Vertex AI Prediction are generally available (GA).

]]> December 20, 2024tag:google.com,2016:vertex-ai-release-notes#December_20_20242024-12-20T00:00:00-08:00Feature 

**Vector Search hybrid search and sparse embeddings are generally available (GA)**

Vector Search hybrid search and sparse embeddings are generally available ([GA](https://cloud.google.com/products/#product-launch-stages)). Hybrid search uses both dense and sparse embeddings, which lets you search based on a combination of keyword search and semantic search. For more information about hybrid search, see [About hybrid search](https://docs.cloud.google.com/vertex-ai/docs/vector-search/about-hybrid-search).

]]> December 17, 2024tag:google.com,2016:vertex-ai-release-notes#December_17_20242024-12-17T00:00:00-08:00Feature 

You can copy tuned Gemini 1.5 Pro 002 and Gemini 1.5 Flash 002 adapter models across projects. For details, see [Copy a model in Vertex AI Model Registry](https://docs.cloud.google.com/vertex-ai/docs/model-registry/copy-model).

]]> December 02, 2024tag:google.com,2016:vertex-ai-release-notes#December_02_20242024-12-02T00:00:00-08:00Feature 

**[Preview](https://cloud.google.com/products/#product-launch-stages)** : You can consume reservations of VMs that have GPUs attached with your custom training jobs or prediction jobs. Reservations of Compute Engine zonal resources help you gain a high level of assurance that your jobs have the necessary resources to run. For more information, see the following:

  * [Use reservations with training](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations)

  * [Use reservations with prediction](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations)


]]> October 31, 2024tag:google.com,2016:vertex-ai-release-notes#October_31_20242024-10-31T00:00:00-07:00Feature 

PSC-I Egress is supported for Ray clusters Vertex AI. PSC-I is recommended for private connectivity since it reduces the chance of IP exhaustion, and allows for transitive peering. Check out [Private Service Connect interface for Ray on Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/open-source/ray-on-vertex-ai/create-cluster#use-psc-i-egress). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

### Feature

Private Service Connect interface (PSC-I) is now supported for ML pipeline runs in Vertex AI Pipelines. PSC-I is recommended for private connectivity, since it reduces the chance of IP exhaustion, and allows for transitive peering.

For more information, see [Configure Private Service Connect interface for a pipeline](https://docs.cloud.google.com/vertex-ai/docs/pipelines/configure-private-service-connect). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

]]> October 08, 2024tag:google.com,2016:vertex-ai-release-notes#October_08_20242024-10-08T00:00:00-07:00Feature 

**Vector Search Private Service Connect automation**

Deploying an index with Private Service Connect automation is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). You can set up a service connection policy so that you don't have to manually create a compute address and forwarding rule after each index deployment. 

For more information, see [Set up Vector Search with Private Service Connect](https://docs.cloud.google.com/vertex-ai/docs/vector-search/setup/private-service-connect).

]]>
