---
url: https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListPoliciesResponse/
title: ListPoliciesResponse \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:00:43.352424+00:00
---

# ListPoliciesResponse  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/reference/rest/v2/ListPoliciesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Reference ](https://docs.cloud.google.com/organization-policy/apis)



Send feedback 

#  ListPoliciesResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The response returned from the `[ListPolicies](https://docs.cloud.google.com/organization-policy/reference/rest/v2/projects.policies/list#google.cloud.orgpolicy.v2.OrgPolicy.ListPolicies)` method. It will be empty if no policies are set on the resource.

JSON representation  
---  
      
    
    {
      "policies": [
        {
          object ([Policy](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`policies[]` |  `object (`[Policy](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy)`)` All policies that exist on the resource. It will be empty if no policies are set.  
`nextPageToken` |  `string` Page token used to retrieve the next page. This is not used, but the server may at any point start supplying a valid token.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-18 UTC."],[],[]] 
