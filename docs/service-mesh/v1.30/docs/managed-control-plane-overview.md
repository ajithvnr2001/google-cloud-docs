---
url: https://docs.cloud.google.com/service-mesh/v1.30/docs/managed-control-plane-overview/
title: Managed control plane \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:28:51.973755+00:00
---

# Managed control plane  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.30/docs/managed-control-plane-overview/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.30/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Managed control plane

**Caution:** managed Cloud Service Mesh with the `ISTIOD` control plane implementation is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). You must modernize all managed `ISTIOD` fleets to the `TRAFFIC_DIRECTOR` implementation. 

This document explains the architectural differences between the deprecated `ISTIOD` control plane implementation and Google's modern `TRAFFIC_DIRECTOR` control plane implementation, and outlines your next steps if your clusters still use a deprecated control plane.

## Control plane overview

In service meshes, the control plane provides traffic management, proxy management when the Envoy proxy is in use, and other networking capabilities.

Cloud Service Mesh using Istio APIs on GKE clusters provides a fully supported implementation of the [Istio APIs](https://docs.cloud.google.com/service-mesh/v1.30/docs/onboarding/api-support). The APIs are implemented and supported by the fully managed and Cloud Networking integrated `TRAFFIC_DIRECTOR` control plane. Previously, two additional control plane implementations were supported:

  * The [deprecated](https://docs.cloud.google.com/service-mesh/deprecations) **managed`ISTIOD` implementation**, which runs a single-cluster dedicated control plane.
  * The [deprecated](https://docs.cloud.google.com/service-mesh/deprecations) **in-cluster`ISTIOD` implementation**, which runs customer-managed control plane components inside your cluster.



## Operational characteristics of the `TRAFFIC_DIRECTOR` control plane

Cloud Service Mesh with the `TRAFFIC_DIRECTOR` control plane uses Google Cloud's managed networking infrastructure rather than per-cluster control plane instances.

The Istio APIs (CRDs) and the xDS configuration sent to Envoy sidecars remain compatible, but you should expect the following operational characteristics:

  * **Policy and service configuration propagation:** When you create new services or update routing and security policies, configuration is validated and propagated across Google Cloud systems before taking effect on sidecars. As a result, initial policy and service propagation takes longer than with in-cluster or `ISTIOD` control planes. For guidance on optimizing deployment workflows, see [Configuration propagation](https://docs.cloud.google.com/service-mesh/v1.30/docs/operate-and-maintain/scalability-best-practices#configuration_propagation).
  * **Pod scaling and endpoint updates:** Changes to workload endpoints—such as new Pods created by horizontal Pod autoscaling or Pods restarting with new IP addresses—are propagated directly by the control plane without the latency associated with policy updates. Existing Pods fetching existing configuration start without delay.
  * **Multi-cluster endpoint discovery:** In multi-cluster meshes, clusters share their endpoints directly through Google Cloud rather than synchronizing them point-to-point between each combination of clusters. This ensures cross-cluster endpoint state converges more quickly and consistently as your mesh scales.



## How does this affect you?

Your next steps depend on which Cloud Service Mesh [control plane implementation](https://docs.cloud.google.com/service-mesh/v1.30/docs/check-control-plane-implementation) your clusters use:

  * **Managed control plane (`TRAFFIC_DIRECTOR` implementation):**
    * You are already using the current, globally scalable architecture (whether configured using Istio APIs, Gateway API, or Google Cloud APIs).
    * No action is required.
  * **Managed control plane (`ISTIOD` implementation):**
    * This implementation is **[deprecated](https://docs.cloud.google.com/service-mesh/deprecations)**.
    * You must take action to inspect your fleet for compatibility blockers, update your configuration, and complete [managed control plane modernization](https://docs.cloud.google.com/service-mesh/v1.30/docs/modernization), or [uninstall managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.30/docs/uninstall-managed).
  * **In-cluster control plane:**
    * The in-cluster control plane on GKE is **[deprecated](https://docs.cloud.google.com/service-mesh/deprecations)**.
    * In-cluster installations cannot be modernized in-place. You must take action to [migrate from in-cluster to the managed control plane on a new cluster](https://docs.cloud.google.com/service-mesh/v1.30/docs/tutorials/migrate-in-cluster-to-managed-on-new-cluster) or [uninstall Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.30/docs/uninstall).



## Control plane modernization for managed Cloud Service Mesh with the ISTIOD implementation

All managed fleets running the deprecated `ISTIOD` implementation must complete modernization to the `TRAFFIC_DIRECTOR` implementation before the end-of-support deadline specified in the [deprecation notice](https://docs.cloud.google.com/service-mesh/deprecations). You can modernize your fleet using either **customer-triggered modernization** (recommended for per-cluster control and staged traffic shifting) or **Google-driven modernization** (automated rollouts for eligible fleets).

For step-by-step instructions, see [Managed control plane modernization](https://docs.cloud.google.com/service-mesh/v1.30/docs/modernization).

### Check control plane compatibility

To evaluate your fleet against supported features and identify configuration blockers before modernization, see:

  * [Understanding Cloud Service Mesh compatibility](https://docs.cloud.google.com/service-mesh/v1.30/docs/migrate/eligibility)
  * [Configuration updates for modernization](https://docs.cloud.google.com/service-mesh/v1.30/docs/migrate/modernization-configuration-updates)



## Appendix: Control plane rollout and deprecation timeline

The transition from `ISTIOD` control planes to the managed `TRAFFIC_DIRECTOR` control plane implementation has followed this timeline:

  * [**May 23, 2024**](https://docs.cloud.google.com/service-mesh/v1.30/docs/release-notes#May_23_2024): Anthos Service Mesh and Traffic Director converged into **Cloud Service Mesh** , introducing the `TRAFFIC_DIRECTOR` control plane implementation for Istio APIs.
  * [**July 1, 2024**](https://docs.cloud.google.com/service-mesh/v1.30/docs/release-notes#July_01_2024): New fleets onboarded to managed Cloud Service Mesh began receiving the `TRAFFIC_DIRECTOR` implementation by default.
  * **September 8, 2024:** Provisioning of the `ISTIOD` implementation for new fleets ended for general availability (with temporary exceptions for specific organizations in an allowlist).
  * [**September 28, 2026**](https://docs.cloud.google.com/service-mesh/v1.30/docs/release-notes#September_28_2026): Formal deprecation announced for both the managed `ISTIOD` control plane implementation and the in-cluster control plane on GKE.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
