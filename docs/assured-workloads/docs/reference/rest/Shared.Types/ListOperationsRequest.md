---
url: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ListOperationsRequest/
title: ListOperationsRequest \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:38:32.382062+00:00
---

# ListOperationsRequest  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ListOperationsRequest/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Reference ](https://docs.cloud.google.com/assured-workloads/docs/apis)



Send feedback 

#  ListOperationsRequest Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The request message for `[Operations.ListOperations](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.operations/list#google.longrunning.Operations.ListOperations)`.

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
`returnPartialSuccess` |  `boolean` When set to `true`, operations that are reachable are returned as normal, and those that are unreachable are returned in the `[ListOperationsResponse.unreachable](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/ListOperationsResponse#FIELDS.unreachable)` field.This can only be `true` when reading across collections. For example, when `parent` is set to `"projects/example/locations/-"`.This field is not supported by default and will result in an `UNIMPLEMENTED` error if set unless explicitly documented otherwise in service or product specific documentation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-27 UTC."],[],[]] 
