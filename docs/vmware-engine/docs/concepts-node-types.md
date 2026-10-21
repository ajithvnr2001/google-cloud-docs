---
url: https://docs.cloud.google.com/vmware-engine/docs/concepts-node-types/
title: VMware Engine node types \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:23.266607+00:00
---

# VMware Engine node types  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/concepts-node-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# VMware Engine node types

A Google Cloud VMware Engine private cloud is a collection of vSphere clusters created with a set of dedicated isolated bare metal hardware nodes in a region. These nodes provide the compute, memory, and storage required to run VMware ESXi, and are the basic unit of consumption of Google Cloud VMware Engine. This document details the node types, their resource capacity and availability in the regions.

VMware Engine supports private clouds with mixed node families (`ve1` and `ve2`) in some regions. While a private cloud can contain mixed node families, each cluster within that private cloud must contain nodes of the same type. For more information, see Region availability. To create a new cluster of a different node family, contact Cloud Customer Care.

A vSphere cluster must have nodes with identical storage. Google Cloud VMware Engine allows creation of a cluster with a mix of hyperconverged infrastructure (HCI) and storage only node types from the same node family. You can create a cluster with `ve2-standard-128` and `ve2-standard-so` node types, but not mix two different HCI node types in the same cluster.

## Node types

The following sections list node types that are available when creating a VMware Engine private clouds or clusters.

### Hyperconverged node types

The following table lists HCI node types that are available when creating a VMware Engine private cloud or a cluster.

Node type | vCPUs/Node§ | Memory/Node (GiB) | Storage/Node (TB)*  
---|---|---|---  
ve1-standard-72 | 72 | 768 | 19.2  
ve2-mega-128† | 128 | 2048 | 51.2  
ve2-mega-112† | 112 | 2048 | 51.2  
ve2-mega-96† | 96 | 2048 | 51.2  
ve2-mega-80† | 80 | 2048 | 51.2  
ve2-mega-64† | 64 | 2048 | 51.2  
ve2-large-128† | 128 | 2048 | 38.4  
ve2-large-112† | 112 | 2048 | 38.4  
ve2-large-96† | 96 | 2048 | 38.4  
ve2-large-80† | 80 | 2048 | 38.4  
ve2-large-64† | 64 | 2048 | 38.4  
ve2-standard-128† | 128 | 2048 | 25.5  
ve2-standard-112† | 112 | 2048 | 25.5  
ve2-standard-96† | 96 | 2048 | 25.5  
ve2-standard-80† | 80 | 2048 | 25.5  
ve2-standard-64† | 64 | 2048 | 25.5  
ve2-small-128† | 128 | 2048 | 12.8  
ve2-small-112† | 112 | 2048 | 12.8  
ve2-small-96† | 96 | 2048 | 12.8  
ve2-small-80† | 80 | 2048 | 12.8  
ve2-small-64† | 64 | 2048 | 12.8  
  
### Storage-only node types

The following table lists storage-only node types that are available when creating a VMware Engine private cloud or cluster.

Node type | Storage/Node (TB)*  
---|---  
ve1-standard-so | 19.2  
ve2-mega-so† | 51.2  
ve2-large-so† | 38.4  
ve2-standard-so† | 25.5  
ve2-small-so† | 12.8  
  
* Raw storage excluding cache.  
† Available in select regions.  
§ vCPU refers to a logical thread, with 2 threads per physical core.

## Region availability

The following table lists the regional availability of Google Cloud VMware Engine node types.

Region | Zones | Private cloud types | Node types  
---|---|---|---  
`asia-northeast1` (Tokyo) | `asia-northeast1-a` | Standard, Single-Node | ve1, ve2  
`asia-northeast2` (Osaka) | `asia-northeast2-a` | Standard, Single-Node | ve2  
`asia-south1` (Mumbai) | `asia-south1-a`, `asia-south1-b` | Standard, Stretched, Single-Node | ve1  
`asia-south2` (Delhi) | `asia-south2-a` | Standard, Single-Node | ve1  
`asia-southeast1` (Singapore) | `asia-southeast1-a`, `asia-southeast1-b` | Standard, Single-Node | ve1  
`australia-southeast1` (Sydney) | `australia-southeast1-a`, `australia-southeast1-b` | Standard, Stretched, Single-Node | ve1, ve2‡  
`australia-southeast2` (Melbourne) | `australia-southeast2-a`, `australia-southeast2-b` | Standard, Stretched, Single-Node | ve2  
`europe-west2` (London) | `europe-west2-a`, `europe-west2-b` | Standard, Stretched, Single-Node | ve1, ve2‡  
`europe-west3` (Frankfurt) | `europe-west3-a`, `europe-west3-b` | Standard, Stretched, Single-Node | ve1, ve2‡  
`europe-west4` (Netherlands) | `europe-west4-a` | Standard, Single-Node | ve1, ve2  
`europe-west6` (Zurich) | `europe-west6-a` | Standard, Single-Node | ve1  
`europe-west8` (Milan) | `europe-west8-a`, `europe-west8-b` | Standard, Stretched, Single-Node | ve1, ve2  
`europe-west9` (Paris) | `europe-west9-b` | Standard, Single-Node | ve1, ve2  
`europe-west12` (Turin) | `europe-west12-a` | Standard, Single-Node | ve1  
`europe-southwest1` (Madrid) | `europe-southwest1-a` | Standard, Single-Node | ve2  
`me-central1` (Doha) | `me-central1-a` | Standard, Single-Node | ve2  
`me-central2` (Dammam) | `me-central2-c` | Standard, Single-Node | ve2  
`me-west1` (Tel Aviv) | `me-west1-a`, `me-west1-b` | Standard, Single-Node | ve1  
`northamerica-northeast1` (Montréal) | `northamerica-northeast1-a` | Standard, Single-Node | ve1, ve2‡  
`northamerica-northeast2` (Toronto) | `northamerica-northeast2-a` | Standard, Single-Node | ve1, ve2  
`northamerica-south1` (Mexico City) | `northamerica-south1-a` | Standard, Single-Node | ve2  
`southamerica-east1` (São Paulo) | `southamerica-east1-a`, `southamerica-east1-c` | Standard, Stretched, Single-Node | ve1, ve2‡  
`southamerica-west1` (Santiago) | `southamerica-west1-a`, `southamerica-west1-b` | Standard, Stretched, Single-Node | ve1, ve2‡  
`us-central1` (Iowa) | `us-central1-a` | Standard, Single-Node | ve1, ve2‡  
`us-east4` (North Virginia) | `us-east4-a`, `us-east4-b` | Standard, Single-Node | ve1, ve2‡  
`us-south1` (Dallas) | `us-south1-b` | Standard, Single-Node | ve1, ve2‡  
`us-west2` (Los Angeles) | `us-west2-a`, `us-west2-b` | Standard, Single-Node | ve1, ve2  
  
‡ Supports private clouds with mixed `ve1` and `ve2` node types.

## Node identification

Each VMware Engine private cloud has a `nodeTypeId` that's available as soon as you create a VMware Engine private cloud. Retrieve the `nodeTypeId` with the [`projects.locations.nodeTypes.get`](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.nodeTypes/get) REST request.

## Node billing

There are two options for paying for VMware Engine nodes: On-demand and commitment. When you provision a VMware Engine node, you control the VMs on that host. For more information about pricing, see [VMware Engine pricing](https://cloud.google.com/vmware-engine/pricing).

### Node commitments

You can purchase VMware Engine nodes with a one- or three-year [committed use discount](https://docs.cloud.google.com/vmware-engine/docs/cud) (CUD) where you make a fixed monthly payment, or you can pay for nodes as you use them. Once you purchase a CUD, you can't cancel it. For more information about pricing, see [VMware Engine pricing](https://cloud.google.com/vmware-engine/pricing).

### Purchasing nodes as CAPEX or OPEX

Google does not provide guidance about accounting. Review the details about the VMware Engine node product and seek guidance from your Controllership team and auditors before you make any accounting decisions regarding CAPEX or OPEX.

## Node maintenance

If a node fails, VMware Engine immediately and automatically adds a new node to the affected VMware cluster to restore service operability. VMware Engine also sends an email to the primary address notifying you about the replacement of the failed node and the name of the private cloud. For more information about maintenance, see [Private cloud maintenance and updates](https://docs.cloud.google.com/vmware-engine/docs/concepts-maintenance-updates).

## What's next

  * Learn about [bringing images with existing licenses to Google Cloud](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/microsoft-licensing#bring-licenses).
  * Learn about [VLANs and subnets](https://docs.cloud.google.com/vmware-engine/docs/concepts-vlans-subnets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
