---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Attributes/
title: Attributes \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:39.916691+00:00
---

# Attributes  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Attributes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  Attributes Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Criticality
    * JSON representation
  * Environment
    * JSON representation
  * ContactInfo
    * JSON representation
  * Channel
    * JSON representation



Consumer provided attributes.

JSON representation  
---  
      
    
    {
      "criticality": {
        object ([Criticality](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Attributes#Criticality))
      },
      "environment": {
        object ([Environment](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Attributes#Environment))
      },
      "developerOwners": [
        {
          object ([ContactInfo](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Attributes#ContactInfo))
        }
      ],
      "operatorOwners": [
        {
          object ([ContactInfo](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Attributes#ContactInfo))
        }
      ],
      "businessOwners": [
        {
          object ([ContactInfo](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Attributes#ContactInfo))
        }
      ]
    }  
  
Fields  
---  
`criticality` |  `object (`[Criticality](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Attributes#Criticality)`)` Optional. User-defined criticality information.  
`environment` |  `object (`[Environment](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Attributes#Environment)`)` Optional. User-defined environment information.  
`developerOwners[]` |  `object (`[ContactInfo](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Attributes#ContactInfo)`)` Optional. Developer team that owns development and coding.  
`operatorOwners[]` |  `object (`[ContactInfo](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Attributes#ContactInfo)`)` Optional. Operator team that ensures runtime and operations.  
`businessOwners[]` |  `object (`[ContactInfo](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Attributes#ContactInfo)`)` Optional. Business team that ensures user needs are met and value is delivered  
  
## Criticality

Criticality of the Application, Service, or Workload

JSON representation  
---  
      
    
    {
      "level": string,
      "missionCritical": boolean,
      "type": enum ([Type](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Type))
    }  
  
Fields  
---  
`level  
**(deprecated)**` |  `string` This item is deprecated!Optional. Criticality level. Can contain only lowercase letters, numeric characters, underscores, and dashes. Can have a maximum length of 63 characters. Deprecated: Please refer to type instead.  
`missionCritical  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Indicates mission-critical Application, Service, or Workload. Deprecated: Please refer to type instead.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Type)`)` Required. Criticality Type.  
  
## Environment

Environment of the Application, Service, or Workload

JSON representation  
---  
      
    
    {
      "environment": string,
      "type": enum (Type)
    }  
  
Fields  
---  
`environment  
**(deprecated)**` |  `string` This item is deprecated!Optional. Environment name. Can contain only lowercase letters, numeric characters, underscores, and dashes. Can have a maximum length of 63 characters. Deprecated: Please refer to type instead.  
`type` |  `enum (`Type`)` Required. Environment Type.  
  
## ContactInfo

Contact information of stakeholders.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "email": string,
      "channel": {
        object ([Channel](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Attributes#Channel))
      }
    }  
  
Fields  
---  
`displayName` |  `string` Optional. Contact's name. Can have a maximum length of 63 characters.  
`email` |  `string` Required. Email address of the contacts.  
`channel` |  `object (`[Channel](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Attributes#Channel)`)` Optional. Communication channel of the contacts.  
  
## Channel

Separate message to accommodate custom formats across IRC and Slack.

JSON representation  
---  
      
    
    {
      "uri": string
    }  
  
Fields  
---  
`uri` |  `string` Required. URI of the channel.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
