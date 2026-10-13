---
url: https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/ExecuteIntegrationsResponse/
title: ExecuteIntegrationsResponse \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:46:55.943727+00:00
---

# ExecuteIntegrationsResponse  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/ExecuteIntegrationsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Reference ](https://docs.cloud.google.com/application-integration/docs/quotas)



Send feedback 

#  ExecuteIntegrationsResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The response for executing an integration.

JSON representation  
---  
      
    
    {
      "executionId": string,
      "outputParameters": {
        object
      },
      "parameters": {
        string: {
          object ([ValueType](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/ValueType))
        },
        ...
      }
    }  
  
Fields  
---  
`executionId` |  `string` The id of the execution corresponding to this run of integration.  
`outputParameters` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` OUTPUT parameters in format of Map<Key,Value>. Where Key is the name of the parameter. Note: name of the system generated parameters are wrapped by backtick(`) to distinguish them from the user defined parameters.  
`parameters` |  `map (key: string, value: object (`[ValueType](https://docs.cloud.google.com/application-integration/docs/reference/rest/v1/ValueType)`))` Optional. OUTPUT parameters from integration execution.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-22 UTC."],[],[]] 
