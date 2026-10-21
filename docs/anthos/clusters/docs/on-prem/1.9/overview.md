---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/overview/
title: Google Distributed Cloud overview \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:40:43.555894+00:00
---

# Google Distributed Cloud overview  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/overview/

**Version 1.9**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.9 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/overview)



Send feedback 

#  Google Distributed Cloud overview Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.9 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/overview)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/overview)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



Google Distributed Cloud is software that brings [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) to on-premises data centers. With Google Distributed Cloud, you can create, manage, and upgrade Kubernetes clusters in your on-premises environment.

With [Connect](https://docs.cloud.google.com/anthos/multicluster-management/connect), you can view and sign in to your on-premises and on-cloud Kubernetes clusters from the same interface in the [Google Cloud console](https://docs.cloud.google.com/anthos/multicluster-management/console).

Google Distributed Cloud runs in your data center in a [vSphere environment](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/vsphere-requirements). vSphere is VMware's [server virtualization](https://www.vmware.com/topics/glossary/content/server-virtualization) software. Google Distributed Cloud uses VMware's [vCenter Server](https://www.vmware.com/products/vcenter-server.html) to manage your clusters.

## Getting Google Distributed Cloud

Google Distributed Cloud is a core component of [GKE Enterprise](https://docs.cloud.google.com/anthos).

  * [GKE Enterprise overview](https://docs.cloud.google.com/anthos/docs/concepts/overview)
  * [Contact sales](https://cloud.google.com/contact)



## Installing Google Distributed Cloud

Before you install Google Distributed Cloud, you create an admin workstation virtual machine (VM) instance in your vSphere environment. You then use the admin workstation to [install Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/install-overview-basic).

## Architecture

An Google Distributed Cloud installation includes an admin cluster, one or more user clusters, and an admin workstation. An Anthos clusters on VMware cluster's virtual machines (VMs) are all in the same [vSphere cluster](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-487C09CE-8BE2-4B89-BA30-0E4F7E3C66F7.html). Anthos clusters on VMware clusters can be in the same or different vSphere clusters.

[ ![Diagram describing Google Distributed Cloud's architecture when one user control plane is deployed](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.9/images/architecture_09302019.svg)](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.9/images/architecture_09302019.svg) Google Distributed Cloud architecture with one user control plane (click to enlarge)

### Admin cluster

The _admin cluster_ is the base layer of Google Distributed Cloud. It runs the following Google Distributed Cloud components:

  * **Admin cluster control plane.** The admin cluster's control plane includes the Kubernetes API server, the scheduler, and several controllers for the admin cluster.

  * **User cluster control planes.** For each user cluster, the admin cluster has a node that runs the control plane for the user cluster. The control plane includes the Kubernetes API server, the scheduler, and several controllers for the user cluster.

  * **Add-ons.** The admin cluster runs several Kubernetes add-ons, like Grafana, Prometheus, and Google Cloud Observability. Google Distributed Cloud launches add-ons on different admin cluster nodes than other control plane components.




Note that user control planes are managed by the admin cluster. They run on nodes in the admin cluster, not in the user clusters. In addition, nodes in the admin cluster run Google Distributed Cloud components. User workloads do not run in the admin cluster.

### User cluster

_User clusters_ are where you deploy and run your containerized workloads and services.

## Versioning

To learn about Google Distributed Cloud versions, see [Version history](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/version-history).

## Additional GKE Enterprise components

With Google Distributed Cloud, you can also use the following GKE Enterprise components:

  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/gke-on-prem-install)
  * [Config Management](https://docs.cloud.google.com/anthos-config-management/docs/overview)
  * [Knative serving](https://docs.cloud.google.com/anthos/run/docs)
  * [Connect](https://docs.cloud.google.com/anthos/multicluster-management/connect)



## What's next

  * [Google Distributed Cloud installation overview](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/install-overview-basic)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
