---
url: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/reference/network/rest/v1/projects.locations
title: REST Resource: projects.locations \u00a0|\u00a0 Google Distributed Cloud connected \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:49:45.626687+00:00
---

# REST Resource: projects.locations  |  Google Distributed Cloud connected  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/reference/network/rest/v1/projects.locations

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.13.0 (Latest) ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/apis)



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
  
### `[get](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/reference/network/rest/v1/projects.locations/get)`

|  Gets information about a location.  
  
### `[list](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/reference/network/rest/v1/projects.locations/list)`

|  Lists information about the supported locations for this service.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
