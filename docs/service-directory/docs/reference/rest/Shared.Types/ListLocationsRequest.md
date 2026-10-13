---
url: https://docs.cloud.google.com/service-directory/docs/reference/rest/Shared.Types/ListLocationsRequest/
title: ListLocationsRequest \u00a0|\u00a0 Service Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:53:36.809060+00:00
---

# ListLocationsRequest  |  Service Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-directory/docs/reference/rest/Shared.Types/ListLocationsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Service Directory ](https://docs.cloud.google.com/service-directory/docs)
  * [ Reference ](https://docs.cloud.google.com/service-directory/docs/apis)



Send feedback 

#  ListLocationsRequest Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The request message for `[Locations.ListLocations](https://docs.cloud.google.com/service-directory/docs/reference/rest/v1/projects.locations/list#google.cloud.location.Locations.ListLocations)`.

JSON representation  
---  
      
    
    {
      "name": string,
      "filter": string,
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`name` |  `string` The resource that owns the locations collection, if applicable.  
`filter` |  `string` A filter to narrow down results to a preferred subset. The filtering language accepts strings like `"displayName=tokyo"`, and is documented in more detail in [AIP-160](https://google.aip.dev/160).  
`pageSize` |  `integer` The maximum number of results to return. If not set, the service selects a default.  
`pageToken` |  `string` A page token received from the `nextPageToken` field in the response. Send that page token to receive the subsequent page.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
