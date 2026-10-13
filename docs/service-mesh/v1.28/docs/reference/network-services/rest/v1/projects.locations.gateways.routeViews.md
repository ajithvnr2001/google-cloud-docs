---
url: https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.gateways.routeViews
title: REST Resource: projects.locations.gateways.routeViews \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:22.513825+00:00
---

# REST Resource: projects.locations.gateways.routeViews  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.gateways.routeViews

You are viewing v1.28 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.28/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.28/docs/overview)



Send feedback 

#  REST Resource: projects.locations.gateways.routeViews Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: GatewayRouteView
    * JSON representation
  * Methods



## Resource: GatewayRouteView

GatewayRouteView defines view-only resource for Routes to a Gateway

JSON representation  
---  
      
    
    {
      "name": string,
      "routeProjectNumber": string,
      "routeLocation": string,
      "routeType": string,
      "routeId": string
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. Full path name of the GatewayRouteView resource. Format: projects/{project_number}/locations/{location}/gateways/{gateway}/routeViews/{route_view}  
`routeProjectNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Project number where the route exists.  
`routeLocation` |  `string` Output only. Location where the route exists.  
`routeType` |  `string` Output only. Type of the route: HttpRoute,GrpcRoute,TcpRoute, or TlsRoute  
`routeId` |  `string` Output only. The resource id for the route.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.gateways.routeViews/get)`

|  Get a single RouteView of a Gateway.  
  
### `[list](https://docs.cloud.google.com/service-mesh/v1.28/docs/reference/network-services/rest/v1/projects.locations.gateways.routeViews/list)`

|  Lists RouteViews  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-28 UTC."],[],[]] 
