---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/network-basic/
title: vSphere network \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:04:52.523821+00:00
---

# vSphere network  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/how-to/network-basic/

**Version 1.9**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.9 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.9/overview)



Send feedback 

#  vSphere network Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.9 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/network)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/network)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This page explains the networking requirements for an initial installation of Google Distributed Cloud.

In your initial installation of Google Distributed Cloud, you create these virtual machines (VMs):

  * One VM for an admin workstation
  * Four VMs for an admin cluster
  * Three VMs for a user cluster



In your vSphere environment, you must have a network that can support the creation of those eight VMs. Your network must also be able to support a vCenter Server and must be able to support the load balancer mode that you choose for your configuration.

Your network needs to support outbound traffic to the internet so that your admin workstation and your cluster nodes can fetch Google Distributed Cloud components and call certain Google services.

If you want external clients to call services in your Google Distributed Cloud clusters, your network must support inbound traffic from the internet.

The following diagram shows one possible network topology:

[ ![Diagram of network topology](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.9/images/vsphere-network.svg)](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.9/images/vsphere-network.svg) Network topology (click to enlarge)

The preceding diagram has the following features:

  * The admin workstation is on a private network.
  * vCenter Server is on a public network.
  * The cluster nodes are on a private network.
  * The F5 BIG-IP load balancer is on three private networks.
  * The F5 BIG-IP load balancer is configured with Virtual IPs (VIPs) that have private addresses. External clients must use public IP addresses configured in the network address translation (NAT) device. The NAT device uses static NAT to convert the public addresses to the internal VIPs configured on the load balancer.



## Network Time Protocol

All the VMs that are part of your Google Distributed Cloud infrastructure must use the same [Network Time Protocol (NTP)](http://www.ntp.org/ntpfaq/NTP-s-def.htm) server.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
