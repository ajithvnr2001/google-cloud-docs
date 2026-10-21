---
url: https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/PatchBody/
title: PatchBody \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:06.550684+00:00
---

# PatchBody  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/PatchBody/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  PatchBody Stay organized with collections  Save and categorize content based on your preferences. 

The structure for the body of a PATCH request.

JSON representation  
---  
      
    
    {
      "schemas": [
        string
      ],
      "Operations": [
        {
          object ([Operation](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/PatchBody#Operation))
        }
      ]
    }  
  
Fields  
---  
`schemas[]` |  `string` Required. This attribute must contain the URI value of `urn:ietf:params:scim:api:messages:2.0:PatchOp`.  
`Operations[]` |  `object (`[Operation](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/PatchBody#Operation)`)` Required. Each operation represents a single action to be applied to the SCIM resource.  
  
## Operation

The operation to perform.

JSON representation  
---  
      
    
    {
      "op": string,
      "path": string,
      "value": value
    }  
  
Fields  
---  
`op` |  `string` Required. The type of operation to perform.  
`path` |  `string` Attribute path describing the target of the operation. Examples of valid paths: `"path":"members"` `"path":"name.familyName"` `"path":"emails[type eq \"work\"]"`  
`value` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Must be set for `add` or `replace` operations. Can be a single value, an object (containing sub-attributes of a complex attribute), or an array depending on the target path.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-08 UTC."],[],[]] 
