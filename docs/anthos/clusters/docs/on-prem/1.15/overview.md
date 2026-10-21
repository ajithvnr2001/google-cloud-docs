---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview/
title: Distributed Cloud overview \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:50.109396+00:00
---

# Distributed Cloud overview  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Distributed Cloud overview Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/overview)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/overview)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



Google Distributed Cloud (GDC) is our solution that extends Google Cloud's infrastructure and services into your data center, with Google-provided software running on your own hardware. Distributed Cloud is built on [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview), with its own _Google Distributed Cloud_ package that extends GKE for use in an on-premises environment. With Google Distributed Cloud, you can create, manage, and upgrade Kubernetes clusters on your own premises while using Google Cloud features. You can deploy and operate containerized applications on your Google Distributed Cloud clusters at scale using Google's infrastructure.

Distributed Cloud is part of GKE Enterprise: an enterprise tier for GKE with powerful features for governing, managing, and operating containerized workloads at scale. You can find out more about GKE Enterprise and the features available for Google Distributed Cloud clusters in the [GKE Enterprise (Anthos) technical overview](https://docs.cloud.google.com/anthos/docs/concepts/overview).

Google Distributed Cloud runs on your premises in a [vSphere environment](https://docs.vmware.com/en/VMware-vSphere/index.html). vSphere is [VMware's](https://www.vmware.com/company.html) virtualization platform. The two main components of vSphere are [ESXi](https://www.vmware.com/products/esxi-and-esx.html) and [vCenter Server](https://www.vmware.com/products/vcenter-server.html).

This page provides an overview of how Google Distributed Cloud works, giving you the background you need before going on to a minimal or production installation.

## How it works

Google Distributed Cloud extends [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview) to let you create GKE clusters in a [vSphere environment](https://docs.vmware.com/en/VMware-vSphere/index.html) on your own premises, and manage them in Google Cloud along with regular Google Kubernetes Engine clusters and clusters in other environments as part of a [fleet](https://docs.cloud.google.com/anthos/fleet-management/docs).

Because Google Distributed Cloud runs in your data center rather than on Google Cloud, it requires you to install some admin and control plane software in addition to the GKE software itself. The software that runs in your data center is downloaded as part of the installation and upgrade processes.

The following diagram shows the simplified result of a completed installation.

[ ![Diagram of an admin cluster and a user cluster](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.15/images/diagram-overview.svg)](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.15/images/diagram-overview.svg) Google Distributed Cloud architecture with one user cluster (Click to enlarge)

### Key components

The following components make up a Google Distributed Cloud installation:

  * A user cluster is where the workloads that implement your applications run, like in GKE on Google Cloud. The nodes that run your workloads are called _worker nodes_. A user cluster also has one or more control plane nodes. In the preceding diagram, the user cluster has one control plane node.

  * The admin cluster manages one or more user clusters. In the preceding diagram, the admin cluster has three control plane nodes.

  * The admin workstation is a separate machine that includes the tools that cluster creators and developers need to manage Google Distributed Cloud:

    * Running `gkectl` from the admin workstation lets you create and update clusters and perform some other administrative tasks
    * Running `kubectl` from the admin workstation lets you interact with your admin and user clusters, including deploying and managing workloads
  * The Google Cloud console provides a web interface for your Google Cloud project, including Google Distributed Cloud. You can perform a subset of Google Distributed Cloud administrative tasks, including cluster creation, from the Google Cloud console as an alternative to running commands on the admin workstation.

  * Cluster admins and developers use `kubectl` and virtual IP addresses (VIPs) to access the control planes in the admin and user clusters. You configure VIPs during cluster creation. Users and developers calling workloads in your user clusters use Service and Ingress VIPs. Each node in the installation also has its own IP address. You can learn more about IP planning for Google Distributed Cloud in [Plan your IP addresses](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/plan-ip-addresses).




### Connecting to the fleet

All Google Distributed Cloud user clusters (and optionally admin clusters) are members of a [fleet](https://docs.cloud.google.com/anthos/fleet-management/docs): a logical grouping of Kubernetes clusters. Fleets let your organization uplevel management from individual clusters to entire groups of clusters, and can help your teams adopt similar best practices to those used at Google. You can view and manage fleet clusters together in the Google Cloud console, and use fleet-enabled GKE Enterprise features to help you manage, govern, and operate your workloads at scale. You can see a complete list of available fleet features for on-premises environments in [GKE Enterprise deployment options](https://docs.cloud.google.com/anthos/deployment-options#features_available_on_anthos_clusters_outside_of_google_cloud).

Each fleet cluster's connection to Google Cloud is managed by a Connect Agent, which is deployed as part of the Google Distributed Cloud installation process. You can learn more about how this agent works in the [Connect Agent overview](https://docs.cloud.google.com/anthos/fleet-management/docs/connect-agent).

Fleet membership is also used to manage Google Distributed Cloud pricing, as described in the next section.

For a deeper discussion of GKE Enterprise features and how they work together, see the [GKE Enterprise technical overview](https://docs.cloud.google.com/anthos/docs/concepts/overview).

## Purchasing Distributed Cloud

Enabling GKE Enterprise lets you use all GKE Enterprise features, including Google Distributed Cloud, for a single per-vCPU charge for fleet clusters. You enable the platform by enabling the [Anthos API](https://console.cloud.google.com/apis/library/anthos.googleapis.com) in your Google Cloud project.

For full pricing information, including how to contact sales, see [GKE pricing](https://cloud.google.com/kubernetes-engine/pricing).

## Versions

To learn about Google Distributed Cloud versions, see [Version history](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/version-history).

## Installing Google Distributed Cloud

Because Google Distributed Cloud runs in your own infrastructure, it is highly configurable to meet your particular organizational and use case needs: you can choose from a range of supported load balancing modes, vSphere configurations, IP addressing options, security features, connectivity options, and more. This means that setting up Google Distributed Cloud involves making decisions before and during installation in consultation with your networking, vSphere, and application teams to ensure that your installation meets your needs. This documentation set includes guides to help your team make these decisions.

However, if you just need to see Google Distributed Cloud in action, we also provide a simple installation path for a small test installation where we've made a lot of these choices for you, letting you quickly get a workload up and running.

In each case, the installation process is as follows:

  1. **Plan your installation**. Minimally this includes ensuring you can meet the resource and vSphere requirements for Google Distributed Cloud, as well as planning your IP addresses.
  2. **Set up your on-premises environment** to support Google Distributed Cloud, including setting up vSphere inventory objects and your connection to Google.
  3. **Set up Google Cloud resources** , including the Google Cloud project you will use when setting up and managing Google Distributed Cloud.
  4. **Create an admin workstation** with the resources and tools you need to create clusters.
  5. **Create an admin cluster** to create, manage, and update user clusters.
  6. **Create user clusters** to run your actual workloads.



## What's next?

  * To start a minimal proof-of-concept installation, see [Set up minimal infrastructure](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/minimal-infrastructure).
  * To review some of the considerations needed to plan a Google Distributed Cloud installation, start a production installation, or both, see the [installation overview](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/install-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
