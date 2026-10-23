---
url: https://docs.cloud.google.com/architecture/networking-for-ai-inference/
title: Networking for AI inference model serving on all backends \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:15:24.333877+00:00
---

# Networking for AI inference model serving on all backends  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/networking-for-ai-inference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Networking for AI inference model serving on all backends Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-05-20 UTC

This document provides a reference architecture to create a unified frontend for multiple AI models that are hosted on-premises or by any provider, including third-party and Google Cloud. If all of your inference servers are hosted in Google Kubernetes Engine (GKE), then see [Networking for AI inference model serving on GKE](https://docs.cloud.google.com/architecture/networking-for-ai-inference-gke).

This architecture is designed to enable your developers to select models without having to specify individual IP addresses for each model. Instead, developers send [OpenAI API](https://developers.openai.com/api/reference/overview) requests that include the name of the model to the frontend endpoint. The system in the architecture routes the requests to the backend that hosts the specified model. The frontend load balancer in the architecture provides the following centralized administrative functions:

  * Single frontend endpoint for all of the model calls regardless of how you host the models.
  * API management functionality.
  * Checkpoint for AI guardrails.
  * [Service Extensions](https://docs.cloud.google.com/service-extensions/docs/overview) insertion point for future extensibility.



This document is for network administrators and administrators of generative AI applications who want to place new or existing generative AI models behind a single inference endpoint. This document doesn't provide guidance about how to design an application or deploy an individual generative AI model. For guidance about how to deploy a model, see [Build and deploy generative AI and machine learning models in an enterprise](https://docs.cloud.google.com/architecture/blueprints/genai-mlops-blueprint). This architecture works with application networking architectures such as [Cross-Cloud Network for distributed applications](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design) and with other designs.

## Architecture

The following diagram shows an architecture with an endpoint in a consumer network that points to a regional internal Application Load Balancer frontend. This load balancer uses the name of the specified model to route requests to model replica sets that are hosted on-premises or by any provider. The frontend load balancer provides consolidated services for all of the hosted models.

![High-level overview of networking for AI inference.](https://docs.cloud.google.com/static/architecture/images/networking-for-ai-inference-architecture.svg)![](https://docs.cloud.google.com/static/architecture/images/networking-for-ai-inference-architecture.svg)

The architecture in the diagram includes the following components:

  * **Private Service Connect inference endpoint** : A unified endpoint for all of the hosted models. The end user sends inference requests to the endpoint IP address. The diagram shows a Private Service Connect endpoint in a single consumer Virtual Private Cloud (VPC) network. You can host endpoints in several VPC networks or in a shared-services VPC network.
  * **Regional internal Application Load Balancer** : In this architecture, the frontend load balancer is a regional internal Application Load Balancer. The frontend load balancer routes traffic to replica pools based on the model name specified in the request. In this architecture, the customer application makes [OpenAI API](https://developers.openai.com/api/reference/overview) calls to the load balancer. If the backend inference server is compatible with the OpenAI API, then things work transparently. If the inference server isn't compatible with the OpenAI API, then you must implement an API translator by using [Service Extensions](https://docs.cloud.google.com/service-extensions/docs/overview). This reference architecture doesn't include the implementation of an API translator.
  * **Service Extensions callouts** : You can use callouts to add additional processing to an Application Load Balancer. The architecture in this design uses the following callouts: 
    * [**Inference Payload Processor**](https://github.com/llm-d/llm-d-inference-payload-processor) (previously the body-based router): The Inference Payload Processor is deployed in Cloud Run. It reads the model name from the body of the OpenAI API request and writes it to an `X-Gateway-Model-Name` field in the header. The load balancer URL map uses the field to forward the request to the appropriate backend service. The Terraform deployment that's provided with this reference architecture includes the Inference Payload Processor configuration.
    * [**Apigee**](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee): An API manager that provides for API authentication, security, rate limiting, quota tracking, and other API management services. This architecture uses Apigee, but the architecture supports other options. To call Apigee from the load balancer, the architecture and the Terraform deployment use a [Service Extensions traffic extension](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions) to call the [Apigee Extension Processor](https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-overview).
    * [**Model Armor**](https://docs.cloud.google.com/model-armor/overview): An AI guardrails system that performs safety checks on inference prompts before they get to the inference server. It then performs safety checks on the outgoing responses. This architecture uses Model Armor for AI guardrails, but it also supports other options such as [NVIDIA NeMo Guardrails](https://docs.nvidia.com/nemo/microservices/latest/set-up/deploy-as-microservices/guardrails/gcp-installation.html). The Terraform deployment that's provided with this reference architecture includes a basic Model Armor configuration.
  * **Backend services** : The load balancer routes requests to backend services based on the name of the model in the request. The backend service contains a [network endpoint group (NEG)](https://docs.cloud.google.com/load-balancing/docs/negs).
  * **Model replica sets** : A [model replica](https://developers.google.com/machine-learning/glossary#replica) is a copy of an inference server that is deployed to one or more GPUs or TPUs. A model replica can be single-node or multi-node. A _replica set_ is a uniform group of model replicas that is fronted by a load balancer. In the architecture, model replicas are contained in a Google Kubernetes Engine (GKE) cluster behind a GKE Inference Gateway, in Gemini Enterprise Agent Platform, in Cloud Run, in an on-premises or other-cloud data center, and behind an endpoint on the internet.



### Model replica set configurations

In the architecture, the frontend load balancer directs traffic to a particular backend service based on the model name. The inference servers for the specified model can be hosted in one of the configurations that's described in the following table.

Replica set type | Description | Replica load balancing  
---|---|---  
Agent Platform | The model replicas run in Agent Platform. You publish a Agent Platform endpoint as a Private Service Connect Network Endpoint Group (NEG). The frontend load balancer uses Private Service Connect NEGs as backends for each distinct model, with each model structured as a backend service. | Agent Platform scales and load balances internally. Agent Platform performs metric-based weighted load balancing and prefix cache-based routing, which optimizes resource utilization and accelerates inference. For more information, see [Deploy a model to an endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/deployment).  
GKE | Inference servers run as Pods in a GKE cluster in the GKE replica set VPC network. Multiple model replicas within GKE collectively form a singular backend behind an Inference Gateway. The Inference Gateway publishes a Private Service Connect endpoint that the frontend load balancer accesses using a Private Service Connect NEG. | The [Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway#overview) provides model-aware load balancing for inference backends in a GKE cluster. The Inference Gateway uses prefix matching when applicable. If there isn't a prefix match, the Inference Gateway distributes requests based on GPU or TPU metrics. This configuration supports Horizontal Pod Autoscaling.  
Cloud Run | Inference servers run in Cloud Run. Cloud Run publishes an endpoint that the frontend load balancer accesses using a [Serverless NEG](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal-serverless). | Cloud Run [automatically scales](https://docs.cloud.google.com/run/docs/about-instance-autoscaling) the number of replicas based on traffic. It's limited to single-node replicas only.  
Hybrid | Inference servers run on-premises or in another cloud. You configure a [regional internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-hybrid) in a routing VPC network. This load balancer publishes a Private Service Connect endpoint that the frontend load balancer accesses using a Private Service Connect NEG. The internal load balancer in the routing VPC network in turn has a hybrid NEG backend that points to the IP address of an on-premises or other-cloud load balancer in front of the on-premises inference servers. | The load balancing mechanism of the external load balancer is configured by the administrators of the external facility.  
Internet | Inference servers that are accessible from public internet IP addresses. The frontend load balancer has an [internet NEG](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts) backend that points to the IP address of a model hosted on the internet. | The managed service provider handles scaling.  
  
### Request flow

The system routes inference requests as follows:

  1. An end user sends an OpenAI API request to the Private Service Connect endpoint. This request contains the following: 
     * The prompt.
     * The model name, which must match the model name of one of the hosted inference servers.
  2. The Private Service Connect endpoint forwards the request to the frontend internal Application Load Balancer.
  3. The load balancer forwards the request to Service Extensions.
  4. The Service Extensions [Inference Payload Processor code](https://github.com/llm-d/llm-d-inference-payload-processor) reads the model name from the request body and writes it to an `X-Gateway-Model-Name` header.
  5. The load balancer uses the Service Extensions traffic extension callout to send the request to the API management system for any API management services that are needed.
  6. The load balancer uses a Service Extensions traffic extension callout to send the prompt to Model Armor for screening. 
     * If the prompt contains sensitive information that can't be redacted, the prompt is blocked and Model Armor returns a response to indicate that a policy violation was found.
     * If the prompt contains sensitive information that can be redacted, or if the prompt has no issues at all, Model Armor redacts any sensitive information and forwards the prompt along.
  7. If the request is allowed by Model Armor, the load balancer consults the URL map and forwards the request to a backend service based on the model name custom header. If necessary, the URL map rewrites the URL and path of the request to match what the backend needs.
  8. The backend service forwards the request to its associated replica set load balancer.
  9. The load balancer for the specific inference service assigns the request to one of its replicas.
  10. The replica processes the request and sends back a response.
  11. The frontend regional internal Application Load Balancer sends the response to Model Armor for screening.
  12. The Application Load Balancer sends the response back to the Private Service Connect endpoint and on to the end user.



The following diagram shows a routing view of a sample deployment:

![Flow of prompts to sample replica sets.](https://docs.cloud.google.com/static/architecture/images/networking-for-ai-inference-flow.svg)![](https://docs.cloud.google.com/static/architecture/images/networking-for-ai-inference-flow.svg)

In this example, prompts are handled depending on the model that the user selects:

  * **Gemma** : All prompts are routed to the replica set that hosts the Gemma model.
  * **Llama** : The system load balances these prompts equally between two replica sets that both host the Llama model. These two replica sets don't have to be hosted in the same way. For example, one replica set could be hosted in Agent Platform and the other replica set could be hosted in GKE.
  * **LoRA-1-gemma or LoRA-2-gemma** : The system sends all of the prompts to the same replica set, which can handle both models.



## Products used

The reference architecture in this document uses the following Google Cloud products:

  * [ Cloud Load Balancing](https://cloud.google.com/load-balancing): A portfolio of high performance, scalable, global and regional load balancers. 
  * [ Virtual Private Cloud (VPC)](https://cloud.google.com/vpc): A virtual system that provides global, scalable networking functionality for your Google Cloud workloads. VPC includes VPC Network Peering, Private Service Connect, private services access, and Shared VPC.
  * [ Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect): A feature that lets consumers access managed services privately from inside their VPC network.
  * [ Cloud Run](https://cloud.google.com/run): A serverless compute platform that lets you run containers directly on top of Google's scalable infrastructure.
  * [ Apigee](https://cloud.google.com/apigee): An API management tool that gives you granular control over how your APIs are accessed and used. It provides security, rate limiting, quota enforcement, and analytics. 
  * [ Model Armor](https://cloud.google.com/security/products/model-armor): A service that provides protection for your generative and agentic AI resources against prompt injection, sensitive data leaks, and harmful content.



## Design alternatives

This section describes alternatives to some of the base assumptions of this architecture.

### AI guardrails

We recommend that you use Model Armor for AI guardrails. To centralize administration, we recommend that you call it directly from the load balancer, as in this architecture. You can also implement Model Armor in these alternative ways:

  * Use an API management policy to call Model Armor.
  * Deploy Model Armor at the replica only.



If you implement AI guardrails other than at the model endpoint, then you can turn off Model Armor at the frontend load balancer if you don't need it. If you don't want to use Model Armor, you can use [traffic extensions](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions) to deploy other guardrail offerings such as [NVIDIA NeMo Guardrails](https://docs.nvidia.com/nemo/microservices/latest/set-up/deploy-as-microservices/guardrails/gcp-installation.html).

### API management

The architecture in this document uses Apigee for API management, which is deployed using a load balancer Service Extension. If Apigee doesn't meet your needs, you can use Service Extensions to deploy a different API management service.

If deploying API management using Service Extensions doesn't meet your needs, then you might need to deploy a client-facing network and an API-facing network. In this scenario, the API management service acts as a bridge between the two networks. For information about how to deploy this for Apigee, see [Apigee networking options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options).

### Connecting to other networks

The architecture in this document uses a single consumer VPC network. However, you can share the Private Service Connect endpoint with many other networks by using a services-access VPC network in a [Cross-Cloud Network deployment](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design/connectivity).

## Design considerations

When you build the architecture for your workload, consider best practices and recommendations in the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework).

### Security, privacy, and compliance

  * To add distributed denial-of-service attack (DDoS) protection, Web Application Firewall (WAF) functionality, and IP address inspection to your deployment, add [Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview) to your frontend regional internal Application Load Balancer.
  * To add a common authentication layer to all of the backends, implement [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/how-to) to verify identity and enforce authorization policies.
  * When you route traffic from a web application to a Agent Platform model, you must choose an identity model for [authentication](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview#auth-models): 
    * Service account identity (recommended for general web apps): The application authenticates the end-user through [IAP](https://docs.cloud.google.com/iap/docs/how-to), but it calls Agent Platform using services workload identity (such as [Cloud Run,](https://docs.cloud.google.com/run/docs/configuring/services/service-identity) [GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity), or using a [third party identity](https://docs.cloud.google.com/iam/docs/workload-identity-federation)). This implementation abstracts Identity and Access Management (IAM) from the end-user, but it requires application-level logging to track which user generated which prompt.
    * End-user identity passthrough (recommended for strict auditability): The application captures the end-user's Google OAuth access token and passes it directly to Agent Platform in the `Authorization: Bearer` header. This implementation provides built-in Cloud Audit Logs logging of user actions, but it requires that every [end-user is provisioned](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control) with Google Cloud IAM permissions (such as `roles/aiplatform.user`).



### Reliability

To guard against regional failures, replicate your deployment to a second region using the [Google Cloud multi-regional deployment archetype](https://docs.cloud.google.com/architecture/deployment-archetypes/multiregional).

### Operational efficiency

  * To monitor traffic flows so that you can identify and remediate problems quickly, use [Cloud Logging logs](https://docs.cloud.google.com/load-balancing/docs/l7-internal/monitoring#how_to_view_logs) for your regional internal Application Load Balancer.
  * To facilitate discovery of the models that your organization supports, implement a list that can be queried to return available models. For example, you can create a list on a server that responds to the [list models API call](https://developers.openai.com/api/reference/resources/models/methods/list).



### Performance optimization

  * **Cloud Run** : To support faster instance starts, you can [Store model weights in the container image](https://docs.cloud.google.com/run/docs/tutorials/gpu-gemma-with-ollama#store-model-weights).
  * **GKE** : Follow the recommendations in the [Overview of inference best practices on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference).



## Deployment

To deploy a sample implementation of this architecture, use the [Networking for AI Inference Model Serving](https://github.com/GoogleCloudPlatform/cloud-networking-solutions/tree/main/reference-architectures/networking-for-ai-inference) code sample that's available in GitHub.

For information about how to deploy AI models, see the following resources:

  * [Deploy generative AI models on Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/deploy/overview).
  * [Deploying Open Models on GKE](https://codelabs.developers.google.com/codelabs/production-ready-ai-with-gc/5-deploying-agents/deploying-open-models-gke).



## What's next

  * For information on adding retrieval-augmented generation to your deployment, see [Private connectivity for RAG-capable generative AI applications](https://docs.cloud.google.com/architecture/private-connectivity-rag-capable-gen-ai).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Victor Moreno](https://www.linkedin.com/in/vimoreno) | Product Manager, Cloud Networking

Other contributors: 

  * [Mark Schlagenhauf](https://www.linkedin.com/in/mark-schlagenhauf-63b98) | Technical Writer, Networking
  * [James Duncan](https://www.linkedin.com/in/jdun) | Solutions Product Manager
  * [Ammett Williams](https://www.linkedin.com/in/ammett) | Developer Relations Engineer



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-20 UTC."],[],[]] 
