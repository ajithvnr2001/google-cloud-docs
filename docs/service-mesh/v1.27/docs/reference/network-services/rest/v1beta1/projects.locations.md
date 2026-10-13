---
url: https://docs.cloud.google.com/service-mesh/v1.27/docs/reference/network-services/rest/v1beta1/projects.locations
title: REST Resource: projects.locations \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:32:08.959472+00:00
---

# REST Resource: projects.locations  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.27/docs/reference/network-services/rest/v1beta1/projects.locations

You are viewing v1.27 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.27/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview)



Send feedback 

#  REST Resource: projects.locations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Location
    * JSON representation
  * Methods



## Resource: Location

A resource that represents a Google Cloud location.

JSON representation  
---  
      
    
    {
      "name": string,
      "locationId": string,
      "displayName": string,
      "labels": {
        string: string,
        ...
      },
      "metadata": {
        "@type": string,
        field1: ...,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Resource name for the location, which may vary between implementations. For example: `"projects/example-project/locations/us-east1"`  
`locationId` |  `string` The canonical id for this location. For example: `"us-east1"`.  
`displayName` |  `string` The friendly name for this location, typically a nearby city name. For example, "Tokyo".  
`labels` |  `map (key: string, value: string)` Cross-service attributes for the location. For example
    
    
    {"cloud.googleapis.com/region": "us-east1"}
    

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`metadata` |  `object` Service-specific metadata. For example the available capacity at the given location.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/service-mesh/v1.27/docs/reference/network-services/rest/v1beta1/projects.locations/get)`

|  Gets information about a location.  
  
### `[list](https://docs.cloud.google.com/service-mesh/v1.27/docs/reference/network-services/rest/v1beta1/projects.locations/list)`

|  Lists information about the supported locations for this service.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-13 UTC."],[],[]] 
