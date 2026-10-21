---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ExportModelOperationMetadata/
title: ExportModelOperationMetadata \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:51:00.400187+00:00
---

# ExportModelOperationMetadata  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ExportModelOperationMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  ExportModelOperationMetadata Stay organized with collections  Save and categorize content based on your preferences. 

Details of `[ModelService.ExportModel](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.models/export#google.cloud.aiplatform.v1beta1.ModelService.ExportModel)` operation.

Fields  
  
`genericMetadata` `object (`[GenericOperationMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/GenericOperationMetadata)`)` The common part of the operation metadata. | `outputInfo` `object (`[OutputInfo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ExportModelOperationMetadata#OutputInfo)`)` Output only. Information further describing the output of this Model export. | JSON representation  
---  
      
    
    {
      "genericMetadata": {
        object ([GenericOperationMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/GenericOperationMetadata))
      },
      "outputInfo": {
        object ([OutputInfo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ExportModelOperationMetadata#OutputInfo))
      }
    }  
  
## OutputInfo

Further describes the output of the ExportModel. Supplements `[ExportModelRequest.OutputConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.models/export#OutputConfig)`.

Fields  
  
`artifactOutputUri` `string` Output only. If the Model artifact is being exported to Google Cloud Storage this is the full path of the directory created, into which the Model files are being written to. | `imageOutputUri` `string` Output only. If the Model image is being exported to Google Artifact Registry this is the full path of the image created. | JSON representation  
---  
      
    
    {
      "artifactOutputUri": string,
      "imageOutputUri": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
