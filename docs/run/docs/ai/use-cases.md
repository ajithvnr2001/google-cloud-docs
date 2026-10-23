---
url: https://docs.cloud.google.com/run/docs/ai/use-cases/
title: AI use cases on Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:48.109817+00:00
---

# AI use cases on Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/ai/use-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  AI use cases on Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

Whether you're building agents, running inference models, or integrating with various AI services, Cloud Run provides the scalability, flexibility, and ease of use needed to bring your AI innovations to life.

This page highlights some high-level use cases for hosting, building, and deploying AI workloads on Cloud Run.

## Why use Cloud Run for AI workloads?

Cloud Run offers several advantages for ensuring your AI applications are scalable, flexible, and managable. Some highlights include:

  * **Flexible container support** : Package your app and its dependencies in a container, or use any supported language, library, or framework. Learn more about Cloud Run's [Container runtime contract](https://docs.cloud.google.com/run/docs/container-contract).
  * **HTTP endpoint** : After deploying a [Cloud Run service or instance](https://docs.cloud.google.com/run/docs/resource-model), receive an out of the box, secure [Cloud Run URL endpoint](https://docs.cloud.google.com/run/docs/triggering/https-request). Cloud Run provides streaming through supporting HTTP chunked transfer encoding, HTTP/2, and WebSockets.
  * **Automatic or manual scaling** : For Cloud Run services, Cloud Run [automatically scales](https://docs.cloud.google.com/run/docs/about-instance-autoscaling) your service based on demand. This ensures you only pay for what you use, making it ideal for unpredictable AI workloads. You can also set your service to manual scaling based on your traffic and CPU utilization needs. For Cloud Run instances, autoscaling is not applicable; they run as singletons that you start and stop manually.


  * **GPU Support** : Accelerate your AI models by configuring Cloud Run resources with GPUs. Cloud Run services with GPUs enabled can scale down to zero for cost savings when not in use.

  * **Integrated ecosystem** : Seamlessly [connect to other Google Cloud services](https://docs.cloud.google.com/run/docs/integrate/using-gcp-services), such as Vertex AI, BigQuery, Cloud SQL, Memorystore, Pub/Sub, AlloyDB for PostgreSQL, Cloud CDN, Secret Manager, and custom domains to build comprehensive end-to-end AI pipelines. Google Cloud Observability also provides built-in monitoring and logging tools to understand application performance and troubleshoot issues effectively.



  * **Enterprise ready** : Cloud Run offers [direct VPC connectivity](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc), granular security, and networking controls.



## Key AI use cases

Here are some ways you can use Cloud Run to power your AI applications:

### Host AI agents and bots

Cloud Run is an ideal platform for hosting the backend logic for AI agents, chatbots, and virtual assistants. These agents can orchestrate calls to AI models like Gemini on Vertex AI, manage state, and integrate with various tools and APIs.

  * **Microservices for agents** : Deploy individual agent capabilities as separate Cloud Run services or instances. See [Host AI agents](https://docs.cloud.google.com/run/docs/ai-agents) to learn more.


  * **Agent2Agent (A2A) communication** : Build collaborative agent systems using the A2A protocol. See [Host A2A agents](https://docs.cloud.google.com/run/docs/host-a2a-agents) to learn more.


  * **Model Context Protocol (MCP) servers** : Implement MCP servers to provide standardized context to LLMs from your tools and data sources. See [Host MCP servers](https://docs.cloud.google.com/run/docs/host-mcp-servers) to learn more.



### Secure AI agents

Cloud Run integrates with [Agent Platform](https://docs.cloud.google.com/run/docs/ai/agent-platform-features) to provide built-in capabilities for AI agents, MCP servers, and tools.

  * **Agent identities** : Assign system-managed [Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview) credentials to your Cloud Run workloads to authenticate to Google Cloud APIs, other agents, and MCP servers without static keys. See [Authenticate your agents](https://docs.cloud.google.com/run/docs/ai/authenticate-agents).
  * **Agent Registry** : Automatically register your agents and tools in your organization's [Agent Registry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-registry) to securely connect to other developers and agents. See [Configure Agent Platform features for Cloud Run](https://docs.cloud.google.com/run/docs/ai/agent-platform-features).
  * **MCP servers and tools** : Protect MCP servers deployed on Cloud Run with Identity-Aware Proxy authentication and fine-grained access controls. See [Authenticate MCP servers](https://docs.cloud.google.com/run/docs/ai/authenticate-mcp-servers).



### Serve AI/ML models for inference

Deploy your trained machine learning models as scalable HTTP endpoints.

  * **Real-time inference** : Serve predictions from models built with frameworks like TensorFlow, PyTorch, scikit-learn, or using open models like Gemma. See [Run Gemma 3 on Cloud Run](https://docs.cloud.google.com/run/docs/run-gemma-on-cloud-run) for an example.


  * **GPU acceleration** : Use NVIDIA GPUs to accelerate inference for more demanding models. See [Configure GPU for services](https://docs.cloud.google.com/run/docs/configuring/services/gpu) to learn more.
  * **Integrate with Vertex AI** : Serve models trained or deployed on Vertex AI, using Cloud Run as a scalable frontend.


  * **Decouple large model files from your container** : The Cloud Storage FUSE adapter lets you mount a Cloud Storage bucket, and makes it accessible as a local directory inside your Cloud Run container.



### Build Retrieval-Augmented Generation (RAG) systems

Build RAG applications by connecting Cloud Run services or instances to your data sources.

  * **Vector databases** : Connect to vector databases hosted on Cloud SQL (with `pgvector`), AlloyDB for PostgreSQL, Memorystore for Redis, or other specialized vector stores to retrieve relevant context for your LLMs. See an [infrastructure example](https://docs.cloud.google.com/architecture/gen-ai-rag-vertex-ai-vector-search) of using Cloud Run for hosting a a RAG-capable generative AI application and data processing using Vertex AI and Vector Search.
  * **Data access** : Fetch data from Cloud Storage, BigQuery, Firestore, or other APIs to enrich prompts.



### Host AI-powered APIs and backends

Create APIs and microservices that embed AI capabilities.

  * **Smart APIs** : Develop APIs that use LLMs for natural language understanding, sentiment analysis, translation, summarization, and so forth.
  * **Automated workflows** : Build services that trigger AI-driven actions based on events or requests.



### Prototype and experiment on ideas

Rapidly iterate on AI ideas.

  * **Rapid deployment** : Quickly move prototypes from environments like [Vertex AI Studio](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/deploy-vais-prompt), [Google AI studio](https://ai.google.dev/gemma/docs/core/deploy_to_cloud_run_from_ai_studio), or Jupyter notebooks to scalable deployments on Cloud Run with minimal configuration.


  * **Traffic splitting** : Use Cloud Run's [traffic splitting feature](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration) to A/B test different models, prompts, or configurations, and Google Cloud Observability for monitoring metrics (latency, error rate, cost) to measure the success of A/B testing.



## What's next

Depending on your familiarity with AI concepts and your AI use case, [explore the Cloud Run AI resources](https://docs.cloud.google.com/run/docs/ai/resources).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
