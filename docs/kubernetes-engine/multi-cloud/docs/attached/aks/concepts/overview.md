---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/concepts/overview/
title: GKE attached clusters overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:19.599799+00:00
---

# GKE attached clusters overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/concepts/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE attached clusters ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/concepts/overview)



Send feedback 

#  GKE attached clusters overview Stay organized with collections  Save and categorize content based on your preferences. 

GKE attached clusters lets you register, or _attach_ , Kubernetes clusters that you've created yourself to the Google Kubernetes Engine management environment. GKE attached clusters supports attaching any [conformant Kubernetes cluster](https://www.cncf.io/certification/software-conformance/), with support for Amazon EKS clusters and Azure AKS clusters.

Attaching a cluster gives you management and control over it, along with access to a suite of additional Google Cloud configuration and control tools such as connect gateway, fleets, Config Sync, and Cloud Service Mesh.

By leveraging GKE management and control capabilities, you can:

  * Automate policy and security across all clusters within your fleet through [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller).
  * Deploy cluster configurations across your fleet through [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview).
  * Monitor and manage a reliable fleet-wide service mesh through [Cloud Service Mesh](https://docs.cloud.google.com/anthos/service-mesh).
  * Authenticate and access all your clusters through a single interface, regardless of where they are, through [Connect Gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway).



You can control and monitor an attached cluster through the Google Cloud CLI or the Google Cloud console.

## GKE attached clusters architecture

![Anthos Attached Clusters architecture](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/attached/aks/images/AAC-architecture.svg)

**Figure 1: GKE attached clusters architecture**

GKE attached clusters represents your external Kubernetes cluster in the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) as an _AttachedCluster_ resource within the GKE Multi-Cloud API.

This resource lets you centrally operate configuration and control tools, including the Config Sync, Policy Controller, and Cloud Service Mesh products.

When you install GKE attached clusters, a new attached cluster resource is created within your Google project as a regional resource. All metadata associated with the cluster is stored in the Google Cloud region associated with your attached cluster resource. This permits compliance with data residency requirements.

GKE attached clusters deploys a workload called the Connect Agent in your cluster. This agent connects back to the Connect API service on Google Cloud to create a secure link to Google Cloud. GKE attached clusters uses this secure tunnel to manage additional features for your clusters.

## What's next

  * Read an [overview of GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview).
  * Learn about [GKE cluster options](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
