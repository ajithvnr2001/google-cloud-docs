---
url: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/MulticastResourceState/
title: MulticastResourceState \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:29:12.315384+00:00
---

# MulticastResourceState  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/MulticastResourceState/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Reference ](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest)



Send feedback 

#  MulticastResourceState Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * StateEnum



The multicast resource's state.

JSON representation  
---  
      
    
    {
      "state": enum ([StateEnum](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/MulticastResourceState#StateEnum))
    }  
  
Fields  
---  
`state` |  `enum (`[StateEnum](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/MulticastResourceState#StateEnum)`)` Optional. The state of the multicast resource.  
  
## StateEnum

Enum value of the multicast resource's state.

Enums  
---  
`STATE_ENUM_UNSPECIFIED` | The resource is in unspecified state.  
`CREATING` | The resource is being created.  
`ACTIVE` | The resource is in a normal state and ready to use.  
`DELETING` | The resource is being deleted.  
`DELETE_FAILED` | The resource is failed to be deleted.  
`UPDATING` | The resource is being updated.  
`UPDATE_FAILED` | The resource is failed to be updated.  
`INACTIVE` | The multicast consumer resource that is deactivated by the multicast administrator.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-22 UTC."],[],[]] 
