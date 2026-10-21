---
url: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/PipelineConfig/
title: PipelineConfig \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:30:33.212981+00:00
---

# PipelineConfig  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/PipelineConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Dataform ](https://docs.cloud.google.com/dataform)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  PipelineConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * PipelineType



Defines the pipeline type and path within the Git repository.

JSON representation  
---  
      
    
    {
      "pipelineType": enum ([PipelineType](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/PipelineConfig#PipelineType)),
      "path": string
    }  
  
Fields  
---  
`pipelineType` |  `enum (`[PipelineType](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/PipelineConfig#PipelineType)`)` Required. The type of the pipeline.  
`path` |  `string` Required. The relative path within the Git repository where the pipeline is defined. For example, for a Dataform pipeline, it is a path to the folder where `workflow_settings.yaml` or `dataform.json` is located.  
  
## PipelineType

The type of the pipeline. In case of `PIPELINE_TYPE_UNSPECIFIED`, an error is thrown.

Enums  
---  
`PIPELINE_TYPE_UNSPECIFIED` | Default value. This value is unused. If set, an error is thrown.  
`DATAFORM` | Regular Dataform pipeline.  
`SQL` | SQL single file asset.  
`NOTEBOOK` | Notebook single file asset.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-17 UTC."],[],[]] 
