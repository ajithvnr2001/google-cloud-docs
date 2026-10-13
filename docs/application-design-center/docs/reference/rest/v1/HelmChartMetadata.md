---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/HelmChartMetadata/
title: HelmChartMetadata \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:19.890329+00:00
---

# HelmChartMetadata  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/HelmChartMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  HelmChartMetadata Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * HelmChartOutput
    * JSON representation



Helm Chart metadata.

JSON representation  
---  
      
    
    {
      "helmInput": [
        {
          object ([HelmChartInput](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/HelmChartInput))
        }
      ],
      "helmOutput": [
        {
          object ([HelmChartOutput](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/HelmChartMetadata#HelmChartOutput))
        }
      ]
    }  
  
Fields  
---  
`helmInput[]` |  `object (`[HelmChartInput](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/HelmChartInput)`)` Output only. Helm Chart inputs.  
`helmOutput[]` |  `object (`[HelmChartOutput](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/HelmChartMetadata#HelmChartOutput)`)` Output only. Helm Chart outputs.  
  
## HelmChartOutput

Helm Chart outputs.

JSON representation  
---  
      
    
    {
      "value": value,
      "helmOutputVariable": string,
      "description": string
    }  
  
Fields  
---  
`value` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Output only. Type of output.  
`helmOutputVariable` |  `string` Output only. Output variable name present.  
`description` |  `string` Output only. Description of the variable.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
