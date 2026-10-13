---
url: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/ProviderTag/
title: ProviderTag \u00a0|\u00a0 Network Intelligence Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:45.490809+00:00
---

# ProviderTag  |  Network Intelligence Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/ProviderTag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Reference ](https://docs.cloud.google.com/network-intelligence-center/docs/apis)



Send feedback 

#  ProviderTag Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ResourceType



Message describing the provider tag.

JSON representation  
---  
      
    
    {
      "category": string,
      "value": string,
      "resourceType": enum ([ResourceType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/ProviderTag#ResourceType))
    }  
  
Fields  
---  
`category` |  `string` Output only. The category of the provider tag.  
`value` |  `string` Output only. The value of the provider tag.  
`resourceType` |  `enum (`[ResourceType](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/ProviderTag#ResourceType)`)` Output only. The resource type of the provider tag.  
  
## ResourceType

Enum for the resource type of the provider tag.

Enums  
---  
`RESOURCE_TYPE_UNSPECIFIED` | The default value. This value is used if the status is omitted.  
`NETWORK_PATH` | Network path.  
`WEB_PATH` | Web path.  
`MONITORING_POLICY` | Monitoring policy.  
`MONITORING_POINT` | Monitoring point.  
`MONITORING_POINT_RULE` | Monitoring point rule.  
`MONITORING_POINT_RULE_AUTO` | Monitoring point rule automatic.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-17 UTC."],[],[]] 
