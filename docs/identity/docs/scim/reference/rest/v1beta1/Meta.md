---
url: https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/Meta/
title: Meta \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:06.147104+00:00
---

# Meta  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/Meta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Meta Stay organized with collections  Save and categorize content based on your preferences. 

Resource metadata assigned by the service provider.

JSON representation  
---  
      
    
    {
      "resourceType": string,
      "created": string,
      "location": string
    }  
  
Fields  
---  
`resourceType` |  `string` The resource type of the resource. This attribute has a mutability of `readOnly` and `caseExact` as `true`.  
`created` |  `string` The `DateTime` that the resource was added to the service provider. This attribute MUST be a `DateTime` as defined in [RFC 7643 Section 2.3.5](https://datatracker.ietf.org/doc/html/rfc7643#section-2.3.5). Example: 2008-01-23T04:56:22Z.  
`location` |  `string` The URI of the resource being returned.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-08 UTC."],[],[]] 
