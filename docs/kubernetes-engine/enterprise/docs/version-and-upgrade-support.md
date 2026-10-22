---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/version-and-upgrade-support/
title: Version and upgrade support \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:22:34.719076+00:00
---

# Version and upgrade support  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/version-and-upgrade-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)



Send feedback 

#  Version and upgrade support Stay organized with collections  Save and categorize content based on your preferences. 

This document shows which versions of Google Kubernetes Engine and GKE-related products1 are compatible with each other and with each cluster type. This information is updated after these products have been tested with the latest minor version of each cluster type. To learn about the features available for each cluster type, see [Deployment options](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/deployment-options).

To avoid compatibility issues and ensure support, we encourage you to maintain your cluster environment with the product's latest major or minor release.

  * _What versions are recommended?_

To ensure a proper upgrade path, recommended patch versions are proven against our highest standard for production use. When available, upgrade to the recommended patch version. Learn about the recommended patch versions in the following table.

In addition to meeting rigorous qualification requirements, a patch release must satisfy the following criteria for it to be designated as recommended:

    * It's not the initial (1.x.**0**) patch release of a minor version.
    * It's been available for at least two weeks.
    * It's free of major defects.
  * _Where do I find information for cluster types that don't have a recommended version?_
    * For details on GKE recommended versions, see [Current versions](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#current_versions).
    * Attached clusters supports the latest minor versions listed in the tables. For details about recommended versions, see [Amazon EKS platform versions](https://docs.aws.amazon.com/eks/latest/userguide/platform-versions.html) and [Supported Kubernetes versions in Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/supported-kubernetes-versions?tabs=azure-cli).



## GKE

GKE on Google Cloud  
---  
Cluster  
Version | Recommended  
Patch | Kubernetes  
Version | Config Sync | Policy Controller | Cloud Service Mesh  
1.36 | - | 1.36 | 1.25  
1.24  
1.23 | 1.24 | 1.30  
1.29  
1.28  
1.35 | - | 1.35 | 1.25  
1.24  
1.23 | 1.24  
1.23 | 1.30  
1.29  
1.28  
1.34 | - | 1.34 | 1.24  
1.23  
1.22 | 1.24  
1.23  
1.22 | 1.30  
1.29  
1.28  
  
## Google Distributed Cloud

On bare metal  
---  
Cluster  
Version | Recommended  
Patch | Kubernetes  
Version | Config Sync | Policy Controller | Cloud Service Mesh  
1.36 | - | 1.36 | 1.24  
1.23  
1.22 | 1.24 | 1.31  
1.30  
1.29  
1.28  
1.35 | 1.35.600-gke.141 | 1.35 | 1.24  
1.23  
1.22 | 1.24  
1.23 | 1.31  
1.30  
1.29  
1.28  
1.34 | 1.34.900-gke.135 | 1.34 | 1.24  
1.23  
1.22 | 1.24  
1.23  
1.22 | 1.31  
1.30  
1.29  
1.28  
On VMware  
---  
Cluster  
Version | Recommended  
Patch | Kubernetes  
Version | Config Sync | Policy Controller | Cloud Service Mesh  
1.36 | - | 1.36 | 1.24  
1.23  
1.22 | 1.24 | 1.31  
1.30  
1.29  
1.28  
1.35 | 1.35.600-gke.141 | 1.35 | 1.24  
1.23  
1.22 | 1.24  
1.23 | 1.31  
1.30  
1.29  
1.28  
1.34 | 1.34.900-gke.135 | 1.34 | 1.24  
1.23  
1.22 | 1.24  
1.23  
1.22 | 1.31  
1.30  
1.29  
1.28  
  
## GKE Multi-Cloud

**Important:** GKE on AWS and GKE on Azure are now in maintenance mode. No new functionality will be added except as needed to fix bugs.On AWS  
---  
Cluster  
Version | Recommended  
Patch | Kubernetes  
Version | Config Sync | Policy Controller | Cloud Service Mesh  
1.35 | 1.35.3-gke.300 | 1.35 | 1.24  
1.23  
1.22 | 1.24  
1.23  
1.22 | 1.28  
1.27  
1.26  
1.34 | 1.34.6-gke.200 | 1.34 | 1.24  
1.23  
1.22 | 1.24  
1.23  
1.22 | 1.28  
1.27  
1.26  
1.33 | 1.33.10-gke.200 | 1.33 | 1.24  
1.23  
1.22 | 1.24  
1.23  
1.22 | 1.27  
1.26  
1.25  
On Azure  
---  
Cluster  
Version | Recommended  
Patch | Kubernetes  
Version | Config Sync | Policy Controller | Cloud Service Mesh  
1.35 | 1.35.3-gke.300 | 1.35 | 1.24  
1.23  
1.22 | 1.24  
1.23  
1.22 | 1.28  
1.27  
1.26  
1.34 | 1.34.6-gke.200 | 1.34 | 1.24  
1.23  
1.22 | 1.24  
1.23  
1.22 | 1.28  
1.27  
1.26  
1.33 | 1.33.10-gke.200 | 1.33 | 1.24  
1.23  
1.22 | 1.24  
1.23  
1.22 | 1.27  
1.26  
1.25  
GKE attached clusters: Amazon Elastic Kubernetes Service (EKS)  
---  
Cluster  
Version | Recommended  
Patch | Kubernetes  
Version | Config Sync | Policy Controller | Cloud Service Mesh  
1.35 | - | 1.35 | 1.24  
1.23  
1.22 | 1.24  
1.23  
1.22 | 1.28  
1.27  
1.26  
1.34 | - | 1.34 | 1.24  
1.23  
1.22 | 1.24  
1.23  
1.22 | 1.28  
1.27  
1.26  
1.33 | - | 1.33 | 1.24  
1.23  
1.22 | 1.24  
1.23  
1.22 | 1.27  
1.26  
1.25  
GKE attached clusters: Azure Kubernetes Service (AKS)  
---  
Cluster  
Version | Recommended  
Patch | Kubernetes  
Version | Config Sync | Policy Controller | Cloud Service Mesh  
1.35 | - | 1.35 | 1.24  
1.23  
1.22 | 1.24  
1.23  
1.22 | 1.28  
1.27  
1.26  
1.34 | - | 1.34 | 1.24  
1.23  
1.22 | 1.24  
1.23  
1.22 | 1.28  
1.27  
1.26  
1.33 | - | 1.33 | 1.24  
1.23  
1.22 | 1.24  
1.23  
1.22 | 1.27  
1.26  
1.25  
  
**1** Connect, Cloud Logging, and Cloud Monitoring are supported on all cluster types.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
