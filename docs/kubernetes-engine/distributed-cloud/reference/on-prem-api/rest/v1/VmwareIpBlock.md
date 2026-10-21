---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareIpBlock/
title: VmwareIpBlock \u00a0|\u00a0 GKE On-Prem API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:20.572386+00:00
---

# VmwareIpBlock  |  GKE On-Prem API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareIpBlock/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ GKE On-Prem API ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview)



Send feedback 

#  VmwareIpBlock Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * VmwareHostIp
    * JSON representation



Represents a collection of IP addresses to assign to nodes.

JSON representation  
---  
      
    
    {
      "netmask": string,
      "gateway": string,
      "ips": [
        {
          object ([VmwareHostIp](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareIpBlock#VmwareHostIp))
        }
      ]
    }  
  
Fields  
---  
`netmask` |  `string` The netmask used by the VMware user cluster.  
`gateway` |  `string` The network gateway used by the VMware user cluster.  
`ips[]` |  `object (`[VmwareHostIp](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/VmwareIpBlock#VmwareHostIp)`)` The node's network configurations used by the VMware user cluster.  
  
## VmwareHostIp

Represents VMware user cluster node's network configuration.

JSON representation  
---  
      
    
    {
      "ip": string,
      "hostname": string
    }  
  
Fields  
---  
`ip` |  `string` IP could be an IP address (like 1.2.3.4) or a CIDR (like 1.2.3.0/24).  
`hostname` |  `string` Hostname of the machine. VM's name will be used if this field is empty.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
