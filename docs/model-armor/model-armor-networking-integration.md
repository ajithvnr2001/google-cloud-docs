---
url: https://docs.cloud.google.com/model-armor/model-armor-networking-integration/
title: Integrate with Google Cloud networking services \u00a0|\u00a0 Model Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:09.781313+00:00
---

# Integrate with Google Cloud networking services  |  Model Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/model-armor/model-armor-networking-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Guides ](https://docs.cloud.google.com/model-armor/overview)



Send feedback 

#  Integrate with Google Cloud networking services Stay organized with collections  Save and categorize content based on your preferences. 

Model Armor integrates with Google Cloud networking services to provide inline security for AI applications at the network level. This integration allows Model Armor to inspect and filter prompts and responses without requiring modifications to the application code itself.

The mechanism for this integration is through [Service Extensions](https://docs.cloud.google.com/service-extensions/docs/overview). Service Extensions enable you to plug in custom logic, like Model Armor's security checks, into the data path of various Google Cloud networking services.

## Before you begin

Ensure that you have met all the [prerequisites](https://docs.cloud.google.com/service-extensions/docs/configure-extensions-to-google-services#before_you_begin).

## Integration points

Model Armor integrates with the following networking services.

Networking service | Description | Reference  
---|---|---  
[Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) | Use Model Armor with Service Extensions to filter traffic passing through Layer 7 load balancers. This is useful for protecting web applications and APIs that leverage LLMs. | [ Configure a traffic extension to call the Model Armor service](https://docs.cloud.google.com/service-extensions/docs/configure-extensions-to-google-services#configure-traffic-ma)  
[ GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway) | Use Model Armor with Service Extensions associated with the GKE Inference Gateway, for containerized AI applications or LLMs running on Google Kubernetes Engine, to inspect and enforce policies on traffic entering or leaving the GKE clusters. | [ Configure AI security and safety checks using GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-gke-inference-gateway-configurations#ai-safety-checks)  
[Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview) | Use Model Armor with Secure Web Proxy to inspect and secure egress traffic from your VPC to AI applications, MCP servers, or LLMs. | [ Configure a traffic extension](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions)  
  
## How it works

Service Extensions enable Google Cloud networking products to call out to Model Armor during data transiting.

  1. When traffic to or from your AI applications, MCP servers, or models passes through a configured network service, for example, a load balancer, Service Extensions forward the request or response content to Model Armor for inspection.
  2. Model Armor applies a set of filters based on your preconfigured template settings. These filters can identify and block prompt injections, jailbreak detection attempts, sensitive data leakage, malicious URLs, and harmful or inappropriate content, such as hate speech and harassment.
  3. Based on the scan results and your policy, Model Armor instructs the networking service to either allow, block, or modify the traffic, ensuring only safe and compliant interactions reach or leave your AI applications, MCP servers, or models.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
