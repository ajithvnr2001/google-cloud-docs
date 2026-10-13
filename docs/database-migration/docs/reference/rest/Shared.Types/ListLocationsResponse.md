---
url: https://docs.cloud.google.com/database-migration/docs/reference/rest/Shared.Types/ListLocationsResponse/
title: ListLocationsResponse \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:57.912938+00:00
---

# ListLocationsResponse  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/reference/rest/Shared.Types/ListLocationsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ APIs and reference ](https://docs.cloud.google.com/database-migration/docs/reference/mcp)



Send feedback 

#  ListLocationsResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Location
    * JSON representation



The response message for `[Locations.ListLocations](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations/list#google.cloud.location.Locations.ListLocations)`.

JSON representation  
---  
      
    
    {
      "locations": [
        {
          object ([Location](https://docs.cloud.google.com/database-migration/docs/reference/rest/Shared.Types/ListLocationsResponse#Location))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`locations[]` |  `object (`[Location](https://docs.cloud.google.com/database-migration/docs/reference/rest/Shared.Types/ListLocationsResponse#Location)`)` A list of locations that matches the specified filter in the request.  
`nextPageToken` |  `string` The standard List next-page token.  
  
## Location

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
`metadata` |  `object` Service-specific metadata. For example the available capacity at the given location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
