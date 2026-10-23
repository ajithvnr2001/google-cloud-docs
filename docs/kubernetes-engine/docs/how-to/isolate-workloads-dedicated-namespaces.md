---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/isolate-workloads-dedicated-namespaces/
title: Isolate your workloads using namespaces \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:19.791785+00:00
---

# Isolate your workloads using namespaces  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/isolate-workloads-dedicated-namespaces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Isolate your workloads using namespaces Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to improve the reliability and performance of your clusters by identifying workloads that are running in the default namespace and moving those workloads to dedicated namespaces.

## About namespaces

In Kubernetes, [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) let you isolate groups of resources within a single cluster. Resource names must be unique within a namespace, but not across namespaces.

### About the default namespace

Kubernetes creates a namespace named `default` when you create a cluster and uses this namespace for all resources by default. We don't recommend using the `default` namespace for your workloads for a production cluster.

If you deploy workloads to the `default` namespace, you expose them to the following risks:

  * Degraded workload performance caused by [noisy neighbor](https://en.wikipedia.org/wiki/Cloud_computing_issues#Performance_interference_and_noisy_neighbors) problems or resource exhaustion due to shared resources (CPU, memory) and network.
  * Disruptions caused by accidental naming collisions and interactions between environments.
  * Weaker security posture due to insufficient isolation of access permissions and network.
  * Inefficient cluster resource use caused by overcrowding the `default` namespace over time and the difficulty of isolated cleanup.



## Why deploy workloads to dedicated namespaces?

The benefits of deploying workloads to dedicated namespaces include the following:

  * **Increased reliability and performance stability** achieved by resource isolation with namespace-bound memory and CPU [resource quotas](https://kubernetes.io/docs/tasks/administer-cluster/manage-resources/quota-memory-cpu-namespace/), lowering the risk of the noisy neighbor problem and resource exhaustion.
  * **Enhanced security** with namespace-scoped [access controls](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/restrict-resources-access-by-namespace) that adhere to the principle of least privilege using [RBAC authorization](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#define-and-assign), and with namespace-scoped [network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) that isolate network communication between applications.
  * **Simplified management and operations** by doing the following:

    * Reduce naming collisions between different workloads or teams that share the same cluster.
    * Isolate observability.
    * Narrow down troubleshooting and debugging.
    * Attribute and optimize cost.
    * Target operations to a specific namespace without affecting the rest of the cluster.
  * **Multi-tenancy** for organizing and isolating cluster resources and policies by applications, environments and teams.




## Inspect the `default` namespace of a specific cluster

To check for workloads running in the `default` namespace of a specific cluster, inspect the `default` namespace for a cluster:

  1. Go to the **Workloads** page.

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload/overview)

  2. In the **Cluster** field, enter the name of the cluster.

  3. In the **Namespace** field, enter `default`.




## Migrate a workload to a dedicated namespace

After you identify workloads running in the `default` namespace, migrate them to a dedicated namespace to achieve higher reliability, more stable performance, and enhanced security.

## What's next

  * [Sync objects to multiple namespaces](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/namespace-scoped-objects)
  * [Managing a GKE Multi-tenant Cluster with Namespaces](https://www.cloudskillsboost.google/focuses/14861?parent=catalog)
  * [Enable access and view cluster resources by namespace](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/restrict-resources-access-by-namespace)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
