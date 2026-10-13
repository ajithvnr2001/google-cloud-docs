---
url: https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/organizations.locations
title: REST Resource: organizations.locations \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:12:56.294878+00:00
---

# REST Resource: organizations.locations  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/organizations.locations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Reference ](https://docs.cloud.google.com/stackdriver/docs/reference/api-overview)



Send feedback 

#  REST Resource: organizations.locations Stay organized with collections  Save and categorize content based on your preferences. 

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
      
  
`metadata` |  `object` Service-specific metadata. For example the available capacity at the given location.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/organizations.locations/get)`

|  Gets information about a location.  
  
### `[getSettings](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/organizations.locations/getSettings)`

|  Get Settings  
  
### `[list](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/organizations.locations/list)`

|  Lists information about the supported locations for this service.  
  
### `[updateSettings](https://docs.cloud.google.com/stackdriver/docs/reference/observability/api/rest/v1/organizations.locations/updateSettings)`

|  Update Settings  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-26 UTC."],[],[]] 
