---
url: https://docs.cloud.google.com/service-mesh/v1.19/docs/supported-platforms/
title: Supported platforms \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:42.241016+00:00
---

# Supported platforms  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.19/docs/supported-platforms/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Supported platforms

## 1.31.x

Only the following environments are supported for in-cluster Cloud Service Mesh 1.31.x. All other environments are unsupported.

Platform | Version  
---|---  
GKE on Google Cloud |  We recommend that you enroll GKE clusters on Google Cloud in a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). When enrolling, use the Regular release channel because other channels might be based on a GKE version that isn't supported. Cloud Service Mesh 1.31 supports the following GKE versions: 1.33-1.36.  For more information about the GKE versions included in each release channel see the following: 

  * [Release notes (Stable channel)](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-stable)
  * [Release notes (Regular channel)](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-regular)
  * [Release notes (Rapid channel)](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-rapid)

The GKE cluster must be Standard. GKE Autopilot cluster is not supported by the in-cluster control plane. In order to use the GKE Autopilot, you must choose [managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh).   
Google Distributed Cloud (software only) for bare metal 1.34-1.36 | Kubernetes version 1.34-1.36  
Google Distributed Cloud (software only) for VMware 1.34-1.36 | Kubernetes version 1.34-1.36  
  
## 1.30.x

Only the following environments are supported for in-cluster Cloud Service Mesh 1.30.x. All other environments are unsupported.

Platform | Version  
---|---  
GKE on Google Cloud |  We recommend that you enroll GKE clusters on Google Cloud in a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). When enrolling, use the Regular release channel because other channels might be based on a GKE version that isn't supported. Cloud Service Mesh 1.30 supports the following GKE versions: 1.33-1.36.  For more information about the GKE versions included in each release channel see the following: 

  * [Release notes (Stable channel)](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-stable)
  * [Release notes (Regular channel)](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-regular)
  * [Release notes (Rapid channel)](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-rapid)

The GKE cluster must be Standard. GKE Autopilot cluster is not supported by the in-cluster control plane. In order to use the GKE Autopilot, you must choose [managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh).   
Google Distributed Cloud (software only) for VMware 1.34-1.36 | Kubernetes version 1.34-1.36  
Google Distributed Cloud (software only) ([deprecated](https://docs.cloud.google.com/service-mesh/deprecations)) for bare metal 1.34-1.36 | Kubernetes version 1.34-1.36  
GKE on AWS ([deprecated](https://docs.cloud.google.com/service-mesh/deprecations)) | Kubernetes version 1.33-1.35  
GKE on Azure ([deprecated](https://docs.cloud.google.com/service-mesh/deprecations)) | Kubernetes version 1.33-1.35  
GKE attached clusters ([deprecated](https://docs.cloud.google.com/service-mesh/deprecations)) | Amazon EKS on Kubernetes 1.33-1.35 and Microsoft AKS on Kubernetes 1.34-1.35  
  
## 1.29.x

Only the following environments are supported for in-cluster Cloud Service Mesh 1.29.x. All other environments are unsupported.

Platform | Version  
---|---  
GKE on Google Cloud |  We recommend that you enroll GKE clusters on Google Cloud in a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). When enrolling, use the Regular release channel because other channels might be based on a GKE version that isn't supported. Cloud Service Mesh 1.29 supports the following GKE versions: 1.33-1.36.  For more information about the GKE versions included in each release channel see the following: 

  * [Release notes (Stable channel)](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-stable)
  * [Release notes (Regular channel)](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-regular)
  * [Release notes (Rapid channel)](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-rapid)

The GKE cluster must be Standard. GKE Autopilot cluster is not supported by the in-cluster control plane. In order to use the GKE Autopilot, you must choose [managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh).   
Google Distributed Cloud (software only) for VMware 1.34-1.36 | Kubernetes version 1.34-1.36  
Google Distributed Cloud (software only) ([deprecated](https://docs.cloud.google.com/service-mesh/deprecations)) for bare metal 1.34-1.36 | Kubernetes version 1.34-1.36  
GKE on AWS ([deprecated](https://docs.cloud.google.com/service-mesh/deprecations)) | Kubernetes version 1.33-1.35  
GKE on Azure ([deprecated](https://docs.cloud.google.com/service-mesh/deprecations)) | Kubernetes version 1.33-1.35  
GKE attached clusters ([deprecated](https://docs.cloud.google.com/service-mesh/deprecations)) | Amazon EKS on Kubernetes 1.33-1.35 and Microsoft AKS on Kubernetes 1.34-1.35  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
