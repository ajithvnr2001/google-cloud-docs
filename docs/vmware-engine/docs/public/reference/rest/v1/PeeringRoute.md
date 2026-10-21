---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/PeeringRoute/
title: PeeringRoute \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:23.388984+00:00
---

# PeeringRoute  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/PeeringRoute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  PeeringRoute Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Type
  * Direction



Exchanged network peering route.

JSON representation  
---  
      
    
    {
      "destRange": string,
      "type": enum ([Type](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/PeeringRoute#Type)),
      "nextHopRegion": string,
      "priority": string,
      "imported": boolean,
      "direction": enum ([Direction](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/PeeringRoute#Direction))
    }  
  
Fields  
---  
`destRange` |  `string` Output only. Destination range of the peering route in CIDR notation.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/PeeringRoute#Type)`)` Output only. Type of the route in the peer VPC network.  
`nextHopRegion` |  `string` Output only. Region containing the next hop of the peering route. This field only applies to dynamic routes in the peer VPC network.  
`priority` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The priority of the peering route.  
`imported` |  `boolean` Output only. True if the peering route has been imported from a peered VPC network; false otherwise. The import happens if the field `NetworkPeering.importCustomRoutes` is true for this network, `NetworkPeering.exportCustomRoutes` is true for the peer VPC network, and the import does not result in a route conflict.  
`direction` |  `enum (`[Direction](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/PeeringRoute#Direction)`)` Output only. Direction of the routes exchanged with the peer network, from the VMware Engine network perspective:

  * Routes of direction `INCOMING` are imported from the peer network.
  * Routes of direction `OUTGOING` are exported from the intranet VPC network of the VMware Engine network.

  
  
## Type

The type of the peering route.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified peering route type. This is the default value.  
`DYNAMIC_PEERING_ROUTE` | Dynamic routes in the peer network.  
`STATIC_PEERING_ROUTE` | Static routes in the peer network.  
`SUBNET_PEERING_ROUTE` | Created, updated, and removed automatically by Google Cloud when subnets are created, modified, or deleted in the peer network.  
  
## Direction

The direction of the exchanged routes.

Enums  
---  
`DIRECTION_UNSPECIFIED` | Unspecified exchanged routes direction. This is default.  
`INCOMING` | Routes imported from the peer network.  
`OUTGOING` | Routes exported to the peer network.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
