---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/DeployedResourceResponse/
title: DeployedResourceResponse \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:24.592068+00:00
---

# DeployedResourceResponse  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/DeployedResourceResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  DeployedResourceResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * UnregisteredResource
    * JSON representation



Common response message for the resource registration methods.

JSON representation  
---  
      
    
    {
      "apphubApplication": string,
      "registeredResources": [
        string
      ],
      "unregisteredResources": [
        {
          object ([UnregisteredResource](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/DeployedResourceResponse#UnregisteredResource))
        }
      ]
    }  
  
Fields  
---  
`apphubApplication` |  `string` The App Hub application name.  
`registeredResources[]` |  `string` The list of successfully registered GCP resources.  
`unregisteredResources[]` |  `object (`[UnregisteredResource](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/DeployedResourceResponse#UnregisteredResource)`)` The list of unregistered GCP resources with error details.  
  
## UnregisteredResource

UnregisteredResource represents a GCP resource that failed to register and apphub was not able to discover.

JSON representation  
---  
      
    
    {
      "deployedResource": {
        object ([DeployedResource](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/DeployedResource))
      },
      "reason": string
    }  
  
Fields  
---  
`deployedResource` |  `object (`[DeployedResource](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/DeployedResource)`)` Output only. The deployed GCP resource that failed to register.  
`reason` |  `string` Output only. The reason for the failure of registration.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
