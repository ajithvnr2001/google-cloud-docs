---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BareMetalNodePoolConfig/
title: BareMetalNodePoolConfig \u00a0|\u00a0 GKE On-Prem API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:17.944833+00:00
---

# BareMetalNodePoolConfig  |  GKE On-Prem API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BareMetalNodePoolConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ GKE On-Prem API ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview)



Send feedback 

#  BareMetalNodePoolConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * BareMetalNodeConfig
    * JSON representation
  * OperatingSystem
  * BareMetalKubeletConfig
    * JSON representation



BareMetalNodePoolConfig describes the configuration of all nodes within a given bare metal node pool.

JSON representation  
---  
      
    
    {
      "nodeConfigs": [
        {
          object ([BareMetalNodeConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BareMetalNodePoolConfig#BareMetalNodeConfig))
        }
      ],
      "operatingSystem": enum ([OperatingSystem](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BareMetalNodePoolConfig#OperatingSystem)),
      "taints": [
        {
          object ([NodeTaint](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/NodeTaint))
        }
      ],
      "labels": {
        string: string,
        ...
      },
      "kubeletConfig": {
        object ([BareMetalKubeletConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BareMetalNodePoolConfig#BareMetalKubeletConfig))
      }
    }  
  
Fields  
---  
`nodeConfigs[]` |  `object (`[BareMetalNodeConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BareMetalNodePoolConfig#BareMetalNodeConfig)`)` Required. The list of machine addresses in the bare metal node pool.  
`operatingSystem` |  `enum (`[OperatingSystem](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BareMetalNodePoolConfig#OperatingSystem)`)` Specifies the nodes operating system (default: LINUX).  
`taints[]` |  `object (`[NodeTaint](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/NodeTaint)`)` The initial taints assigned to nodes of this node pool.  
`labels` |  `map (key: string, value: string)` The labels assigned to nodes of this node pool. An object containing a list of key/value pairs.Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`kubeletConfig` |  `object (`[BareMetalKubeletConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/BareMetalNodePoolConfig#BareMetalKubeletConfig)`)` The modifiable kubelet configurations for the bare metal machines.  
  
## BareMetalNodeConfig

BareMetalNodeConfig lists machine addresses to access Nodes.

JSON representation  
---  
      
    
    {
      "nodeIp": string,
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`nodeIp` |  `string` The default IPv4 address for SSH access and Kubernetes node. Example: 192.168.0.1  
`labels` |  `map (key: string, value: string)` The labels assigned to this node. An object containing a list of key/value pairs. The labels here, unioned with the labels set on BareMetalNodePoolConfig are the set of labels that will be applied to the node. If there are any conflicts, the BareMetalNodeConfig labels take precedence.Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## OperatingSystem

The available Operating Systems to be run in a Node.

Enums  
---  
`OPERATING_SYSTEM_UNSPECIFIED` | No operating system runtime selected.  
`LINUX` | Linux operating system.  
  
## BareMetalKubeletConfig

KubeletConfig defines the modifiable kubelet configurations for bare metal machines.

Note: this list includes fields supported in GKE (see <https://cloud.google.com/kubernetes-engine/docs/how-to/node-system-config#kubelet-options)>.

JSON representation  
---  
      
    
    {
      "registryBurst": integer,
      "serializeImagePullsDisabled": boolean,
      "registryPullQps": integer
    }  
  
Fields  
---  
`registryBurst` |  `integer` The maximum size of bursty pulls, temporarily allows pulls to burst to this number, while still not exceeding registryPullQps.The value must not be a negative number. Updating this field may impact scalability by changing the amount of traffic produced by image pulls.Defaults to 10.  
`serializeImagePullsDisabled` |  `boolean` Prevents the Kubelet from pulling multiple images at a time.We recommend _not_ changing the default value on nodes that run docker daemon with version < 1.9 or an Another Union File System (Aufs) storage backend. Issue <https://github.com/kubernetes/kubernetes/issues/10959> has more details.  
`registryPullQps` |  `integer` The limit of registry pulls per second.Setting this value to 0 means no limit. Updating this field may impact scalability by changing the amount of traffic produced by image pulls.Defaults to 5.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
