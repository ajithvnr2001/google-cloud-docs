---
url: https://docs.cloud.google.com/service-mesh/v1.24/docs/troubleshooting/troubleshoot-scaling/
title: Resolving scaling issues in Cloud Service Mesh \u00a0|\u00a0 Cloud Service Mesh v1.24 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:59.326575+00:00
---

# Resolving scaling issues in Cloud Service Mesh  |  Cloud Service Mesh v1.24  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.24/docs/troubleshooting/troubleshoot-scaling/

You are viewing archived v1.24 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.24 ](https://docs.cloud.google.com/service-mesh/v1.24/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.24/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Resolving scaling issues in Cloud Service Mesh

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.24/docs/overview).

This section explains common Cloud Service Mesh problems and how to resolve them. If you need additional assistance, see [Getting support](https://docs.cloud.google.com/service-mesh/v1.24/docs/getting-support).

## Scaling factors

[Istiod](https://istio.io/v1.24/blog/2020/istiod/) sends configuration to each sidecar using a long-lived gRPC stream. It has several characteristics that affect scaling:

  * The size of the configuration to generate: 
    * Total number of services/pods & Istio resources
    * For large scale, adjust settings for the [Sidecar](https://istio.io/v1.24/docs/reference/config/networking/sidecar/) to reduce the configuration size.
  * The rate of change in the environment: 
    * When a new service is created or the Istio configuration is changed, full updates are sent to proxies.
    * Adding new endpoints is inexpensive for performance, because only incremental updates are sent.
  * The number of proxies for which configuration is generated: 
    * Affected by the number of gateways and pods with a sidecar.



## Scaling considerations

Istiod scales well vertically (large requests) and horizontally (more replicas). Ensure that your CPU limits are not too restrictive; if Istiod reaches the CPU limit, throttling may occur which will negatively affect configuration distribution. If you encounter performance issues, consider upgrading to the latest version of Cloud Service Mesh, as each version has performance optimizations.

For more guidance on scaling your mesh, see the [Scalability best practices guide](https://docs.cloud.google.com/service-mesh/v1.24/docs/operate-and-maintain/scalability-best-practices).

## Unbalanced load

Large changes in cluster size might cause a temporarily unbalanced load, due to the long-lived connections. This is mitigated by a 30 minute maximum connection age, which might result in error messages in Envoy, such as `gRPC config stream closed: 13`, which allows the load to naturally rebalance.

Mitigate this issue by having multiple replicas of Istiod (the default is 2 replicas), and pre-scaling if you expect extreme cluster scale-ups.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
