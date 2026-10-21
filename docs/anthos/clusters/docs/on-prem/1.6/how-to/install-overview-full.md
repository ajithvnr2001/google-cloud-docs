---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/install-overview-full/
title: Overview of advanced installation topics \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:57:29.698473+00:00
---

# Overview of advanced installation topics  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/install-overview-full/

**Version 1.6**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.6 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6)



Send feedback 

#  Overview of advanced installation topics Stay organized with collections  Save and categorize content based on your preferences. 

The Google Distributed Cloud documentation provides an [initial installation journey](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/install-overview-basic) that makes several choices to keep the experience easy and straightforward. When you complete the initial installation journey, you have an admin cluster and a small user cluster.

This section of the documentation has a collection of advanced topics related to setting up your vSphere environment and installing Google Distributed Cloud.

For example, in the initial installation journey, you create a user cluster that has three nodes. Given that the cluster has only three nodes, the documentation can list simple CPU, RAM, and storage requirements for your vSphere environment. Going forward, you might want to create a user cluster that has more than three nodes. In that case, you should read [CPU, RAM, and storage requirements](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/cpu-ram-storage), which gives detailed instructions on how to calculate your resource requirements depending on your cluster size and the types of workloads you intend to run.

The initial installation journey used the F5 BIG-IP load balancer along with integrated load balancing mode. For an overview of load balancing modes and instructions on how to manually configure some alternatives to F5 BIG-IP, see [Setting up your load balancer](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/setup-load-balance).

For information on how to use [OpenID Connect](https://developers.google.com/identity/protocols/OpenIDConnect) for authenticating clients of your user clusters, see [Authenticating with OIDC](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/oidc).

Use the following topics to learn how to configure and install Google Distributed Cloud with all options, including how to configure a private Docker registry:

  * Static IPs: 
    * [Creating an admin workstation with a static IP address](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-workstation-static-ip)
    * [Installing using static IP addresses](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/install-static-ips)
  * DHCP: 
    * [Creating an admin workstation using DHCP](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/admin-workstation-dhcp)
    * [Installing using DHCP](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/install-dhcp)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
