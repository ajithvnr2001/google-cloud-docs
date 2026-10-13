---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ComponentParameters/
title: ComponentParameters \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:58.025810+00:00
---

# ComponentParameters  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ComponentParameters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  ComponentParameters Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Information about the component level parameters for an application.

JSON representation  
---  
      
    
    {
      "component": string,
      "parameters": [
        {
          object ([Parameter](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Parameter))
        }
      ],
      "connectionsParameters": [
        {
          object ([ConnectionParameters](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ConnectionParameters))
        }
      ],
      "state": enum (State),
      "componentParameterSchema": [
        {
          object ([ComponentParameterSchema](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ComponentParameterSchema))
        }
      ],
      "applicationInfo": {
        object ([ComponentApplicationInfo](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ComponentApplicationInfo))
      },
      "effectiveApplicationInfo": {
        object ([ComponentApplicationInfo](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ComponentApplicationInfo))
      }
    }  
  
Fields  
---  
`component` |  `string` Required. The name of the component parameter.  
`parameters[]` |  `object (`[Parameter](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Parameter)`)` Optional. A list of parameters associated with the component.  
`connectionsParameters[]` |  `object (`[ConnectionParameters](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ConnectionParameters)`)` Output only. A list of connections associated with the component.  
`state` |  `enum (`State`)` Output only. Deployment state of the component.  
`componentParameterSchema[]` |  `object (`[ComponentParameterSchema](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ComponentParameterSchema)`)` Output only. The component parameter schema, which includes possible parameter values.  
`applicationInfo` |  `object (`[ComponentApplicationInfo](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ComponentApplicationInfo)`)` Optional. The application associated with the component.  
`effectiveApplicationInfo` |  `object (`[ComponentApplicationInfo](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/ComponentApplicationInfo)`)` Output only. The effective application associated with the component. This is the server set application field.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
