---
url: https://docs.cloud.google.com/service-mesh/docs/supported-platforms/
title: Supported platforms \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:13.023474+00:00
---

# Supported platforms  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/supported-platforms/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Supported platforms

Cloud Service Mesh supports a variety of infrastructures (GKE/Kubernetes, Compute Engine) and environments (on-premises, other clouds). This page describes the APIs and options for using Cloud Service Mesh across all of these options.

## On Google Cloud

There are two choices of APIs on Google Cloud based on which infrastructure you plan to use.

If your workloads are exclusively on GKE, use the Istio APIs.

  * Use the fleet API to install Cloud Service Mesh on clusters in the fleet.

  * Choose the CA you want to use, MeshCA or CAS. The clusters in the fleet will all use the same CA, establishing trust across the workloads running on the clusters.

  * The Service Mesh UI is enabled automatically.




### Managed control plane for GKE

The control plane provisioned for these clusters depends on whether you are adding clusters to an existing fleet or are provisioning a new fleet.

New fleets use the global, managed control plane. This control plane scales across the entire Google Cloud network and provides enhanced reliability and stability.

If you are adding clusters to an existing fleet, new clusters will use the same managed control plane implementation as existing clusters.

### Unmanaged Cloud Service Mesh

Using an unmanaged, in-cluster control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Do not use an in-cluster control plane for new deployments on GKE on Google Cloud. If you have an existing in-cluster control plane on GKE on Google Cloud, migrate to [managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/migrate/migrate-to-managed-csm).

### VMs, GKE and or Proxyless gRPC

If your workloads are a combination of VMs and GKE, or use proxyless gRPC, you should use the [Service Routing APIs](https://docs.cloud.google.com/service-mesh/docs/service-routing/service-routing-overview). These APIs let you define a mesh and configure the routing between services in that mesh.

## Off Google Cloud

Cloud Service Mesh supports GKE and attached clusters in a variety of environments. In this case, Cloud Service Mesh is part of GKE Enterprise on Google Cloud. In these environments Cloud Service Mesh is installed in-cluster using `asmcli`. The Istio APIs are installed in the cluster enabling the user to configure the service mesh for Kubernetes workloads.

Cloud Service Mesh supports the following environments:

  * Google Distributed Cloud (software only) for VMware
  * Google Distributed Cloud (software only) for bare metal



The following products are now deprecated and are in maintenance mode.

  * GKE on AWS will be shut down on March 17, 2027.
  * GKE on Azure will be shut down on March 17, 2027.
  * Cloud Service Mesh support for EKS Kubernetes clusters on AWS will end on March 17, 2027.
  * Cloud Service Mesh support for AKS Kubernetes clusters on Azure will end on March 17, 2027.



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
  
## 1.28.x

Only the following environments are supported for in-cluster Cloud Service Mesh 1.28.x. All other environments are unsupported.

Platform | Version  
---|---  
GKE on Google Cloud |  We recommend that you enroll GKE clusters on Google Cloud in a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). When enrolling, use the Regular release channel because other channels might be based on a GKE version that isn't supported. Cloud Service Mesh 1.28 supports the following GKE versions: 1.33-1.36.  For more information about the GKE versions included in each release channel see the following: 

  * [Release notes (Stable channel)](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-stable)
  * [Release notes (Regular channel)](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-regular)
  * [Release notes (Rapid channel)](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-rapid)

The GKE cluster must be Standard. GKE Autopilot cluster is not supported by the in-cluster control plane. In order to use the GKE Autopilot, you must choose [managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh).   
Google Distributed Cloud (software only) for VMware 1.34-1.36 | Kubernetes version 1.34-1.36  
Google Distributed Cloud (software only) ([deprecated](https://docs.cloud.google.com/service-mesh/deprecations)) for bare metal 1.34-1.36 | Kubernetes version 1.34-1.36  
GKE on AWS ([deprecated](https://docs.cloud.google.com/service-mesh/deprecations)) | Kubernetes version 1.33-1.35  
GKE on Azure ([deprecated](https://docs.cloud.google.com/service-mesh/deprecations)) | Kubernetes version 1.33-1.35  
GKE attached clusters ([deprecated](https://docs.cloud.google.com/service-mesh/deprecations)) | Amazon EKS on Kubernetes 1.33-1.35 and Microsoft AKS on Kubernetes 1.34-1.35  
  
For a list of environments that are supported for managed Cloud Service Mesh, see [managed Cloud Service Mesh Environments](https://docs.cloud.google.com/service-mesh/docs/managed/supported-features-mcp#environments).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
