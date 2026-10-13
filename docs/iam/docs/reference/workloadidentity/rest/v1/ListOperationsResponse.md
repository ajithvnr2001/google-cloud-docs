---
url: https://docs.cloud.google.com/iam/docs/reference/workloadidentity/rest/v1/ListOperationsResponse/
title: ListOperationsResponse \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:39:22.526799+00:00
---

# ListOperationsResponse  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/workloadidentity/rest/v1/ListOperationsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  ListOperationsResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The response message for `[Operations.ListOperations](https://docs.cloud.google.com/iam/docs/reference/workloadidentity/rest/v1/projects.locations.operations/list#google.longrunning.Operations.ListOperations)`.

JSON representation  
---  
      
    
    {
      "operations": [
        {
          object ([Operation](https://docs.cloud.google.com/iam/docs/reference/workloadidentity/rest/v1/folders.locations.operations#Operation))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`operations[]` |  `object (`[Operation](https://docs.cloud.google.com/iam/docs/reference/workloadidentity/rest/v1/folders.locations.operations#Operation)`)` A list of operations that matches the specified filter in the request.  
`nextPageToken` |  `string` The standard List next-page token.  
`unreachable[]` |  `string` Unordered list. Unreachable resources. Populated when the request sets `ListOperationsRequest.return_partial_success` and reads across collections. For example, when attempting to list all resources across all supported locations.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
