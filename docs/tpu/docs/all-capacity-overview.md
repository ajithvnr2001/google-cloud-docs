---
url: https://docs.cloud.google.com/tpu/docs/all-capacity-overview/
title: All Capacity mode overview \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:26.503342+00:00
---

# All Capacity mode overview  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/all-capacity-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# All Capacity mode overview

**Caution:** The [Compute Engine Service Level Agreement (SLA)](https://cloud.google.com/compute/sla) doesn't apply to All Capacity mode TPUs.

TPU capacity is available in two modes: managed capacity mode and All Capacity mode. For a detailed comparison between these modes, see [TPU capacity modes](https://docs.cloud.google.com/tpu/docs/capacity-modes).

All Capacity mode provides physically co-located TPU capacity and direct, reservation-based control over your hardware for optimal performance and workload scheduling.

Key features of All Capacity mode include:

  * **Full capacity access** : Access your entire reserved capacity with zero holdbacks.
  * **Full topology visibility** : View the host topology, health, and utilization status of your reservation, blocks, sub-blocks, and hosts.
  * **Granular maintenance control** : Target specific VMs, sub-blocks, blocks, or entire reservations to schedule and start maintenance.
  * **Direct failure management** : Identify and report faulty hosts directly to initiate hardware repair workflows.



## Supported TPU versions

All Capacity mode is available on TPU v6e (Trillium) and TPU7x (Ironwood). All Capacity mode is not supported for older TPU versions.

## All Capacity mode terminology

All Capacity mode topology consists of four levels: _cluster_ , _block_ , _sub-block_ , and _host_. A cluster is a deployment unit of physical TPU capacity within one zone. A TPU reservation in All Capacity mode is always within one cluster.

The following tables show how TPU topology concepts map to physical components:

**TPU v6e**

Topology concept | Physical component | Cores | Chips | Hosts  
---|---|---|---|---  
N/A | Chip | 1 | 1 | N/A  
Host | Host | 8 | 8 | 1  
Sub-block | TPU v6e Pod | 256 | 256 | 32  
Block | Multiple TPU v6e Pods (up to 16) in a reservation | Up to 4096 | Up to 4096 | Up to 512  
  
A reservation can have one or more blocks, and each block can have 1 to 16 TPU v6e Pods.

For more information about supported slice sizes, see [TPU v6e supported configurations](https://docs.cloud.google.com/tpu/docs/v6e#configurations).

**TPU7x**

Topology concept | Physical component | Cores | Chips | Hosts  
---|---|---|---|---  
N/A | Chip | 2 | 1 | N/A  
Host | Host | 8 | 4 | 1  
Sub-block | Cube | 128 | 64 | 16  
Block | Multiple TPU7x cubes up to a full Pod | Up to 18,432 | Up to 9,216 (144 cubes) | Up to 2,304  
  
A reservation can have one or more TPU7x cubes, up to a full Pod.

For more information about supported slice sizes, see [TPU7x supported configurations](https://docs.cloud.google.com/tpu/docs/tpu7x#configurations).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
