---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v1/ListOrgPoliciesResponse/
title: ListOrgPoliciesResponse \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:22.016301+00:00
---

# ListOrgPoliciesResponse  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v1/ListOrgPoliciesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  ListOrgPoliciesResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The response returned from the `projects.listOrgPolicies` method. It will be empty if no `Policies` are set on the resource.

JSON representation  
---  
      
    
    {
      "policies": [
        {
          object ([Policy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/Policy))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`policies[]` |  `object (`[Policy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/Policy)`)` The `Policies` that are set on the resource. It will be empty if no `Policies` are set.  
`nextPageToken` |  `string` Page token used to retrieve the next page. This is currently not used, but the server may at any point start supplying a valid token.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-11 UTC."],[],[]] 
