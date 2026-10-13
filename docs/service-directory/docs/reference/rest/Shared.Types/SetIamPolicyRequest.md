---
url: https://docs.cloud.google.com/service-directory/docs/reference/rest/Shared.Types/SetIamPolicyRequest/
title: SetIamPolicyRequest \u00a0|\u00a0 Service Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:36.406110+00:00
---

# SetIamPolicyRequest  |  Service Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-directory/docs/reference/rest/Shared.Types/SetIamPolicyRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Service Directory ](https://docs.cloud.google.com/service-directory/docs)
  * [ Reference ](https://docs.cloud.google.com/service-directory/docs/apis)



Send feedback 

#  SetIamPolicyRequest Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Request message for `SetIamPolicy` method.

JSON representation  
---  
      
    
    {
      "resource": string,
      "policy": {
        object ([Policy](https://docs.cloud.google.com/service-directory/docs/reference/rest/Shared.Types/Policy))
      }
    }  
  
Fields  
---  
`resource` |  `string` REQUIRED: The resource for which the policy is being specified. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.  
`policy` |  `object (`[Policy](https://docs.cloud.google.com/service-directory/docs/reference/rest/Shared.Types/Policy)`)` REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Google Cloud services (such as Projects) might reject them.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
