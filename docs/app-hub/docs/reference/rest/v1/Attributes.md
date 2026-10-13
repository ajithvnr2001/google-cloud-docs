---
url: https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/Attributes/
title: Attributes \u00a0|\u00a0 App Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:36.842863+00:00
---

# Attributes  |  App Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/Attributes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Reference ](https://docs.cloud.google.com/app-hub/docs/apis)



Send feedback 

#  Attributes Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Criticality
    * JSON representation
  * Type
  * Environment
    * JSON representation
  * Type
  * ContactInfo
    * JSON representation



Consumer provided attributes.

JSON representation  
---  
      
    
    {
      "criticality": {
        object ([Criticality](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/Attributes#Criticality))
      },
      "environment": {
        object ([Environment](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/Attributes#Environment))
      },
      "developerOwners": [
        {
          object ([ContactInfo](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/Attributes#ContactInfo))
        }
      ],
      "operatorOwners": [
        {
          object ([ContactInfo](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/Attributes#ContactInfo))
        }
      ],
      "businessOwners": [
        {
          object ([ContactInfo](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/Attributes#ContactInfo))
        }
      ]
    }  
  
Fields  
---  
`criticality` |  `object (`[Criticality](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/Attributes#Criticality)`)` Optional. User-defined criticality information.  
`environment` |  `object (`[Environment](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/Attributes#Environment)`)` Optional. User-defined environment information.  
`developerOwners[]` |  `object (`[ContactInfo](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/Attributes#ContactInfo)`)` Optional. Developer team that owns development and coding.  
`operatorOwners[]` |  `object (`[ContactInfo](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/Attributes#ContactInfo)`)` Optional. Operator team that ensures runtime and operations.  
`businessOwners[]` |  `object (`[ContactInfo](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/Attributes#ContactInfo)`)` Optional. Business team that ensures user needs are met and value is delivered  
  
## Criticality

Criticality of the Application, Service, or Workload

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/Attributes#Type))
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/Attributes#Type)`)` Required. Criticality Type.  
  
## Type

Criticality Type.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`MISSION_CRITICAL` | Mission critical service, application or workload.  
`HIGH` | High impact.  
`MEDIUM` | Medium impact.  
`LOW` | Low impact.  
  
## Environment

Environment of the Application, Service, or Workload

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/Attributes#Type_1))
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/app-hub/docs/reference/rest/v1/Attributes#Type_1)`)` Required. Environment Type.  
  
## Type

Environment Type.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`PRODUCTION` | Production environment.  
`STAGING` | Staging environment.  
`TEST` | Test environment.  
`DEVELOPMENT` | Development environment.  
  
## ContactInfo

Contact information of stakeholders.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "email": string
    }  
  
Fields  
---  
`displayName` |  `string` Optional. Contact's name. Can have a maximum length of 63 characters.  
`email` |  `string` Required. Email address of the contacts.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-06 UTC."],[],[]] 
