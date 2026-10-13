---
url: https://docs.cloud.google.com/channel/docs/reference/rest/Shared.Types/ListOperationsRequest/
title: ListOperationsRequest \u00a0|\u00a0 Channel Services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:10:03.299482+00:00
---

# ListOperationsRequest  |  Channel Services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/channel/docs/reference/rest/Shared.Types/ListOperationsRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Channel Services ](https://docs.cloud.google.com/channel/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/channel/docs/reference/libraries)



Send feedback 

#  ListOperationsRequest Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The request message for `[Operations.ListOperations](https://docs.cloud.google.com/channel/docs/reference/rest/v1/operations/list#google.longrunning.Operations.ListOperations)`.

JSON representation  
---  
      
    
    {
      "name": string,
      "filter": string,
      "pageSize": integer,
      "pageToken": string,
      "returnPartialSuccess": boolean
    }  
  
Fields  
---  
`name` |  `string` The name of the operation's parent resource.  
`filter` |  `string` The standard list filter.  
`pageSize` |  `integer` The standard list page size.  
`pageToken` |  `string` The standard list page token.  
`returnPartialSuccess` |  `boolean` When set to `true`, operations that are reachable are returned as normal, and those that are unreachable are returned in the `[ListOperationsResponse.unreachable](https://docs.cloud.google.com/channel/docs/reference/rest/Shared.Types/ListOperationsResponse#FIELDS.unreachable)` field.When reading across collections, such as when `parent` is set to `"projects/example/locations/-"`, this must be `true`.This field isn't supported by default and results in an `UNIMPLEMENTED` error if set, unless explicitly documented otherwise in documentation specific to a service or product.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-03 UTC."],[],[]] 
