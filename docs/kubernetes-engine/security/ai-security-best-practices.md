---
url: https://docs.cloud.google.com/kubernetes-engine/security/ai-security-best-practices/
title: Best practices for AI workload security on GKE \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:26:24.391156+00:00
---

# Best practices for AI workload security on GKE  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/security/ai-security-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Best practices for AI workload security on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document provides best practices for platform teams, security engineers, and cloud architects who deploy AI workloads on Google Kubernetes Engine (GKE). You can use GKE to protect proprietary intellectual property (IP) such as model weights, safeguard brand reputation by filtering content, and improve regulatory compliance.

Implement these best practices in addition to other GKE and AI workload security best practices like the following:

  * [Generative AI security best practices](https://docs.cloud.google.com/docs/security/genai-security-bps)
  * [Best practices for hardening cluster security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster)



## Understand your security responsibilities

The security posture of your AI workloads depends on various layers of your environment, such as your Google Cloud infrastructure and the models that you use. The following table describes these layers, who's responsible for securing each layer, and the security responsibilities for that layer:

Layer | Description | Responsibilities  
---|---|---  
Infrastructure | The underlying infrastructure, such as virtual machines (VMs), networking components, and storage hardware that your AI workloads run on. Google Cloud owns the infrastructure and provides a strong security baseline. | Platform administrators in your organization implement controls to improve security in the following areas:

  * Defense against prompt injection attacks
  * Data encryption
  * User and workload authentication and authorization
  * Output safety
  * Hardware and tenant isolation for multi-tenant environments
  * Rate limiting in multi-tenant environments
  * Log and metric collection

  
Model | The model, model weights, the training pipeline, and safety properties. If you run models that you trained or fine-tuned, then you're responsible for securing the model layer. If you run managed models from third-party providers (such as Gemini), then the provider is responsible for model security. | At the model layer, the model owner is responsible for security in the following areas:

  * Model integrity
  * Model weight protection
  * Model safety properties

  
Application | The prompts, code, system instructions, and end-user experience. Application operators and platform administrators in your organization are responsible for security at the application layer. | At the application layer, application operators, developers, and platform administrators are responsible for security in the following areas:

  * Defense against prompt injection attacks
  * Application data handling
  * Application-layer content safety
  * Workload isolation and sandboxing

  
  
You apply controls to secure the layers that you're responsible for. The following examples show common deployment types for GKE customers and the corresponding security responsibilities for those deployments:

  * **You run a managed model, such as Gemini** : you apply controls at the infrastructure and application layers. Even when you use a managed model that has built-in safety filters, you still own the prompt injection defenses required to protect your specific application logic.
  * **You run your own model** : if you run a fine-tuned model, an open-source model, or a model that you trained, then you're responsible for security at every layer.
  * **You're a multi-tenant AI service provider** : if you provide AI services to your own end-users by running your model on GKE and exposing inference endpoints to multiple tenants, then you're responsible for additional controls. These multi-tenant controls include logical and physical tenant isolation (such as dedicated node pools, namespaces, and network policies), per-tenant rate limiting, and the encryption of tenant data at rest by using distinct Customer-Managed Encryption Keys (CMEK).



## Improve security at the infrastructure layer

At the infrastructure layer, Google Cloud and GKE provide a baseline security posture that implements various security controls by default. To improve the security of your infrastructure for AI workloads, you configure additional security controls based on the type of AI workloads that you run and the specific security goals that you want to achieve. The following sections describe the products and services that you can use to protect various components of your AI infrastructure.

### Protect GKE nodes

Use the following services to protect sensitive data, such as inference workloads that process prompts and responses or training workloads that access proprietary models:

  * **Encrypt sensitive data in-use with hardware attestation** : run your inference workloads on [Confidential Google Kubernetes Engine Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes), extending hardware-level memory encryption to accelerators including GPUs and TPUs, in addition to AMD SEV-SNP or Intel TDX CPUs. Use Confidential GKE Nodes for regulated deployments and sensitive inference workloads. Confidential GKE Nodes don't protect workloads from application-level exploits or authorized users who have node-level access.

For providers whose customers have strict isolation requirements (such as sovereign workloads), [GKE Hypercluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/hypercluster-overview) provides cryptographic attestation that even the underlying infrastructure operator, Google Cloud, can't inspect tenant data.

  * **Reduce the risk of node impersonation** : run workloads on [ Shielded GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes), which provide verifiable node integrity and identity attestations. Use Shielded GKE Nodes for all workload types.

  * **Eliminate the use of static credentials for workloads** : use [ Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to access Google Cloud services from your application code by using short-lived, federated credentials and prevent non-essential Compute Engine metadata from being exposed to applications. Use Workload Identity Federation for GKE in all production clusters, especially when you need to access data that's in services outside of the cluster.




### Implement network controls

You can use the following features and products to improve network security for AI workloads:

  * **Use alias IP address ranges** : [VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips) use alias IP address ranges to route traffic between Pods instead of using static routes in the VPC network. Always use VPC-native clusters.

  * **Restrict network access to nodes** : use [private nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation) to prevent traffic between your nodes and the public internet by default. Inference endpoints that need to be exposed should have a managed service like Google Cloud Armor between the endpoints and the internet.

  * **Deny in-cluster traffic by default** : use [Kubernetes NetworkPolicies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) to deny traffic between Pods, between namespaces, and egress traffic to the internet. Allow network traffic only for applications that require specific access.

  * **Add edge protection to internet endpoints** : you can use [Google Cloud Armor](https://cloud.google.com/security/products/armor) to protect inference endpoints that are exposed to the internet by implementing rate limiting, DDoS protection, geo-based access control, and Layer 7 attack mitigation. If you have public-facing AI APIs, use Cloud Armor to handle volumetric and application-layer attacks before the attacks reach your compute infrastructure. Combine Cloud Armor with private nodes to optimize the security of inference endpoints.

  * **Prevent data exfiltration during an attack** : use [VPC Service Controls](https://cloud.google.com/security/vpc-service-controls) to create a security perimeter around your Google Cloud resources. Even if credentials are compromised, attackers can't take data outside of the perimeter. Use VPC Service Controls for regulated workloads.




### Manage identity and access

To identify users and to control access to clusters and workloads, use the following authorization mechanisms:

  * **Control access to Google Cloud resources** : use [Google Cloud Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) access policies to control which principals can interact with GKE clusters and nodes.

  * **Control access to Kubernetes resources in clusters** : use [Kubernetes role-based access control (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) policies to control what various principals can do to the Kubernetes API resources inside each cluster.

  * **Configure zero-trust access to inference endpoints and admin interfaces** : use a service like [Chrome Enterprise Premium](https://cloud.google.com/beyondcorp) to configure user access based on identity and device posture instead of network topology.




### Manage keys and secrets

Keep all of your encryption keys and sensitive data, such as API keys and credentials, outside of the cluster. The following products can help you to store these resources:

  * **Manage encryption keys** : use [Cloud Key Management Service](https://cloud.google.com/security/products/security-key-management) to manage all encryption keys. You can also create Customer-Managed Encryption Keys (CMEKs) in Cloud KMS to encrypt data with keys that you control, which is often a requirement in regulated industries.

  * **Store sensitive application data** : use [Secret Manager](https://cloud.google.com/security/products/secret-manager) to store sensitive data that's used by workloads, such as application secrets, API keys, and credentials. To read this data from Pods, use [ Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) to give specific workload identities access to only the resources that the Pods need.




### Improve supply chain security

The following Google Cloud services can help you to improve security throughout the software supply chain:

  * **Scan for container image vulnerabilities** : store your container images in [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) repositories that have vulnerability scanning enabled by default. Enable continuous CVE detection on every image in your registry.
  * **Allow only verified images to reach production** : use [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs) to enforce policy-based authorization of container image signatures at deploy time. Only attested images reach production.

  * **Configure security detection and posture management** : use [Security Command Center](https://cloud.google.com/security/products/security-command-center) to view AI-specific threat detection and posture management findings, such as misconfigured Gemini Enterprise Agent Platform endpoints or exposed training data buckets. Security Command Center integrates these AI findings with Artifact Registry vulnerabilities and IAM analysis for a comprehensive view of your fleet.

  * **Track AI artifacts** : use bill-of-materials tooling that's built for Kubernetes AI workloads, such as [`k8s-aibom`](https://github.com/GoogleCloudPlatform/k8s-aibom), to generate comprehensive inventories of your models, datasets, and frameworks.




## Improve security at the model layer

If you run models that you trained or fine-tuned, or you run open source models that you configured, then you should configure various controls to improve the security of the model. If you run managed models from third-party providers, then this layer doesn't apply to you. The following sections describe what you can do to improve the integrity, confidentiality, and security of your models.

### Improve model integrity

Improve the integrity of your models so that you can find evidence of tampering before the model is accessible at an inference endpoint. The following guidelines can help you to improve model integrity:

  * **Sign your model artifacts** : cryptographically sign model weights before you publish the weights to your registry. When you deploy the model, verify the signature by using [Binary Authorization attestations](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestations). Signing and verifying your model artifacts helps you to identify whether models were tampered with during storage or transit and gives you a verifiable chain of custody for production models.
  * **Find post-training modifications** : the open source [Activation Model Scanner (AMS)](https://github.com/GoogleCloudPlatform/activation-model-scanner) detects models that have been modified after training (for example, to add backdoors, weight perturbations, or unauthorised fine-tunes) by analysing the model's activation signatures against a baseline. Run a scanner like AMS as part of your CI/CD pipeline before you publish your models to production registries. For high-value or regulated models, schedule periodic AMS scans against production artefacts to detect tampering that occurs after initial publication.



### Protect model confidentiality

If you have sensitive model weights, such as proprietary fine-tunes, models trained on regulated data, or competitive intellectual property, use the following guidelines to protect the weights:

  * **Encrypt weights at rest** : store weights in encrypted object storage, such as in Cloud Storage buckets, with restricted IAM access. Cloud Storage encrypts customer content at rest by default. You can optionally use CMEKs to encrypt the data with keys that you control, which is often a requirement in regulated industries. For more information, in the Cloud Storage documentation, see [Data encryption options](https://docs.cloud.google.com/storage/docs/encryption).

  * **Protect weights in use** : run models on Confidential GKE Nodes to ensure that weights are encrypted in memory during inference. Confidential GKE Nodes can help you to protect your intellectual property from hypervisor-level compromise and unauthorized access by the infrastructure operator. Confidential GKE Nodes doesn't protect against application-level exploits or authorized users with node-level access.

  * **Control all access to weights** : log all access to model artifacts in storage. Use IAM access policies to restrict access to specific service accounts and humans that have a documented access need. Strictly restrict administrative access to the cluster, including shell access to containers, SSH access to node VMs, or node-level debugging, by using Kubernetes RBAC policies and Chrome Enterprise Premium. These measures can help you to protect model weights from users who have node-level access, which isn't covered by Confidential GKE Nodes.




### Improve model safety properties

You can implement various safety settings for models during training. If you're training or fine-tuning your own model, then invest in safety training that's relevant to the model use case. Safety properties for models include refusal behavior, alignment training, and resistance to jailbreaks. If you use a pre-trained model, choose a model that has safety properties that match your application requirements.

Application developers and operators can implement various controls at the application layer to improve security in areas that the model can't cover.

## Improve security at the application layer

The application layer is where operators and developers have the most control over AI-specific security configurations. At the application layer, you can implement security controls that protect data, create well-formed requests, and protect prompts and responses. These controls are typically useful for inference workloads, which handle user prompts, sessions, and responses. The following sections describe various controls, products, and services that might help you to achieve specific security goals at the application layer.

### Defend against content-layer threats

Inspect all prompts and responses for security issues like prompt injection, sensitive data exposure, and harmful content. Because GKE nodes are designed to have no access to content, deploy [Model Armor](https://cloud.google.com/security/products/model-armor) between your application and the inference endpoint. Model Armor has specific [data handling and storage principles](https://docs.cloud.google.com/model-armor/overview#data-handling) that are designed to improve the privacy of your data during scanning.

### Protect system prompts

Filter outputs for prompt leakage and configure Model Armor data exfiltration detection to catch extraction patterns. For highly sensitive instructions, process the instructions in an invocation that doesn't return text to the user.

### Manage sessions and routing

When you expose inference endpoints to end-users, use [ GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway). Inference Gateway extends the Gateway API to route traffic based on metrics and data that are specific to AI inference workloads. You can autoscale workloads to meet demand and integrate with Model Armor and Apigee for content filtering, session-level observability and quota enforcement.

### Improve AI agent security

If your AI workload is an agent, then you require additional application-layer controls like the following:

  * **Restrict access to Google Cloud APIs:** use Workload Identity Federation for GKE with IAM access policies to limit which APIs your agent workload Pods can access. Use a dedicated Kubernetes ServiceAccount for each agent, and grant that principal only the IAM permissions that the workload needs.
  * **Run code execution or untrusted tools in sandboxes** : run agents that execute generated code or interact with unverified third-party tools in sandboxed environments by using Agent Sandbox. Agent Sandbox uses an isolation mechanism like GKE Sandbox or Kata Containers to protect against container escapes.



## Configure observability and incident response

Collect logs and monitor various metrics to identify potential attacks early and limit the impact of exploits. The following sections provide guidelines that might help you to improve detection and response.

### Collect logs and metrics

To identify threats as quickly as possible, implement as many of the following observability best practices as possible:

  * Collect [GKE logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs).
  * Enable Data Access audit logs for sensitive operations, such as KMS key usage.
  * Don't log prompt or completion content unless your policy explicitly permits it. If you [collect multimodal prompt and response data](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managed-otel-gke#multimodal-prompts-responses) ([Preview](https://cloud.google.com/products#product-launch-stages)), then delete or restrict access to the stored data based on your security policies.
  * Collect [metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics) that matter to your SREs.
  * Configure [automatic application monitoring](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-automatic-application-monitoring) for specific types of AI model servers.
  * Aggregate logs in Cloud Logging or in your own Security Information and Event Management (SIEM) platform.
  * Use [log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics) to create metrics based on the content of logs.



### Detect AI-specific threats

Set up alerts in Logging and Cloud Monitoring to detect various AI-specific threats. The specific alerting policies that you set up depend on the types of logs that you collect and what your organization requires. For more information about the available alerting policies, see [Comparison of alerting options](https://docs.cloud.google.com/logging/docs/alerting/monitoring-logs#alert-diffs). Configure alerts for AI-specific threats such as the following:

AI-specific threats and signals  
---  
Prompt injection | [Model Armor logs](https://docs.cloud.google.com/model-armor/configure-logging) for prompt sanitization or denial  
System prompt extraction | Model Armor and cache hit anomalies  
Sensitive data exposure | Model Armor response logs  
Inference cost abuse | Session-level token usage from Inference Gateway metrics  
Session manipulation | Velocity of new sessions per tenant from Inference Gateway metrics  
Model fingerprinting | Capability probing patterns  
[Timing side-channel](https://en.wikipedia.org/wiki/Timing_attack) | Architectural mitigation (cache partitioning)  
  
### Establish an incident response process

How you respond to various incidents depends on your organizational structure and security requirements. The following guidelines describe what to do when you detect specific types of threats to your AI workloads:

  * **Content detections in Model Armor** : block the request, document the event, and set up an alert to notify you if the rate exceeds a threshold. Set up rate-limiting for users who have repeated violations.

  * **Inference detections** : throttle tenants by using Inference Gateway. Terminate sessions for confirmed abuse.

  * **Cross-layer correlation:** a Model Armor detection plus a token abuse pattern indicates coordinated abuse. Define correlation rules and identify a confidence threshold after which the risk of a false positive alert is low. Automate the termination of sessions that cross this threshold.




## Implement security across the deployment lifecycle

Optimize your AI deployments for security throughout the deployment lifecycle. During specific lifecycle stages, implement controls that protect one or more layers. The following sections provide guidelines for each stage of the lifecycle.

### Deploy infrastructure

When you create or design the infrastructure that runs your AI workloads, implement as many of the following controls as possible:

Category  
---  
GKE nodes | 

  * Enable Workload Identity Federation for GKE on all production clusters.
  * Set up Confidential GKE Nodes for sensitive inference workloads.
  * Enable Shielded GKE Nodes for all workloads.

  
Networking | 

  * Use VPC-native clusters.
  * Enable private nodes.
  * Deny cluster traffic by default by using NetworkPolicies.
  * Create VPC Service Controls perimeters for regulated workloads.
  * Deploy Model Armor for inference endpoints.
  * Configure Inference Gateway for load balancing and session management.

  
Identity and access management | 

  * Use Chrome Enterprise Premium for human administrative access.
  * Use IAM access policies and Kubernetes RBAC for authorization.

  
Sensitive data management | 

  * Store all secrets, such as API keys, in Secret Manager.
  * Store container images in Artifact Registry and enable vulnerability scanning.

  
Observability | 

  * Enable Security Command Center.
  * Set up logging and monitoring.
  * Establish an incident response process.

  
  
### Operate workloads and infrastructure

When you deploy your AI workloads and run a production system, implement as many of the following controls as possible:

Category  
---  
Workload security | 

  * Enforce container image policies with Binary Authorization.
  * Sign and verify model artifacts at deploy time.
  * Run AMS in the model CI pipeline.
  * Validate all structured outputs.
  * Isolate agents that run code in sandboxes.

  
Networking | 

  * Tune Model Armor profiles.
  * Tune Inference Gateway settings.

  
Sensitive data protection | Use CMEK to encrypt data with your own keys in regulated environments.  
Observability | 

  * Configure and aggregate audit logging.
  * Generate AI supply chain inventories.

  
  
### Govern deployments at scale

As your organization scales up, implement the following controls to automate security management:

  * Configure organization-level guardrails using Organization Policy Service.
  * Enforce admission-time policy using Kubernetes admission webhooks.
  * Automate first-response for high-confidence detections.
  * Establish cross-layer SIEM correlation and per-tenant behavioral baselines.



## Summary of best practices

The following table summarizes the best practices recommended in this document:

Topic  
---  
Improve security at the infrastructure layer | Protect GKE nodes, implement network controls, manage identity and access, manage keys and secrets, and improve supply chain security.  
Improve security at the model layer | Improve model integrity, protect model confidentiality, and improve model safety properties.  
Improve security at the application layer | Defend against content-layer threats, protect system prompts, manage sessions and routing, and improve AI agent security.  
Configure observability and incident response | Collect logs and metrics, detect AI-specific threats, and establish an incident response process.  
Implement security across the deployment lifecycle | Deploy infrastructure, operate workloads and infrastructure, and govern deployments at scale.  
  
## What's next

  * [Generative AI security best practices](https://docs.cloud.google.com/docs/security/genai-security-bps)
  * [Best practices for hardening cluster security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
