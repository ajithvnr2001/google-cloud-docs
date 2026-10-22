---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/nat-overview/
title: NAT Overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:32:51.649645+00:00
---

# NAT Overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/nat-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  NAT Overview Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

Network Address Translation (NAT) settings refer to configurations that control how instances with private Internet Protocol (IP) addresses can communicate with the internet or other networks. Google Distributed Cloud (GDC) air-gapped provides outgoing NAT configurations to both virtual machines and containerized workloads when accessing external networks.

## Types of NAT in Distributed Cloud

Google Distributed Cloud air-gapped supports two NAT implementations. One is a replacement for the other, and they cannot be used together.

### Project default egress NAT (deprecated)

Before Cloud NAT the only way to egress traffic was by using the **project default egress NAT configuration**. By default projects are created with a default Egress NAT configuration that allows endpoints from VMs or Pods with the the label `egress.networking.gke.io/enabled:true` to egress traffic using an egress IP automatically assigned to the Project they are in.

This egress solution is now deprecated. We recommend that users migrate to Cloud NAT. Cloud NAT is the main NAT solution in Google Distributed Cloud (GDC) air-gapped systems.

**Important:** The default egress NAT configuration from a project is not compatible with Cloud NAT. I.e. a pod or VM endpoint cannot be connected to a Cloud NAT gateway (via label selectors), and have assigned the label `egress.networking.gke.io/enabled:true`.

This egress solution is unsupported for workloads in [standard clusters](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#standard-cluster), which must use CloudNAT.

See [default project egress](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/default-egress) for information on how to use this solution, and how to migrate to the recommended solution, Cloud NAT.

### Cloud NAT

Cloud NAT lets you send traffic out of the Google Distributed Cloud (GDC) air-gapped deployment through Cloud NAT gateways. You can select which specific Internet Protocol (IP) addresses each gateway uses to send traffic out by specifying `leaf` subnets with the outgoing IP addresses to use in the gateway configuration. You can also select which Kubernetes Pod or virtual machine (VM) endpoints can send traffic out through each gateway by specifying label selectors in the gateway configuration. Cloud NAT gateways have project and zonal scope, so the subnets and endpoints you specify, as well as the outgoing traffic, must be in the same zone and project as the gateway. Cloud NAT is specifically for external (North-South) traffic and not for internal (East-West) traffic.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
