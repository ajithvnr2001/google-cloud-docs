---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ConfusionMatrix/
title: ConfusionMatrix \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:04:51.669726+00:00
---

# ConfusionMatrix  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ConfusionMatrix/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  ConfusionMatrix Stay organized with collections  Save and categorize content based on your preferences. 

Fields  
  
`annotationSpecs[]` `object (`[AnnotationSpecRef](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ConfusionMatrix#AnnotationSpecRef)`)` AnnotationSpecs used in the confusion matrix.For AutoML Text Extraction, a special negative AnnotationSpec with empty `id` and `displayName` of "NULL" will be added as the last element. | `rows[]` `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` rows in the confusion matrix. The number of rows is equal to the size of `annotationSpecs`. `rows[i][j]` is the number of DataItems that have ground truth of the `annotationSpecs[i]` and are predicted as `annotationSpecs[j]` by the Model being evaluated.For Text Extraction, when `annotationSpecs[i]` is the last element in `annotationSpecs`, i.e. the special negative AnnotationSpec, `rows[i][j]` is the number of predicted entities of `annoatationSpec[j]` that are not labeled as any of the ground truth AnnotationSpec. When annotationSpecs[j] is the special negative AnnotationSpec, `rows[i][j]` is the number of entities have ground truth of `annotationSpec[i]` that are not predicted as an entity by the Model. The value of the last cell, i.e. `row[i][j]` where i == j and `annotationSpec[i]` is the special negative AnnotationSpec, is always 0. | JSON representation  
---  
      
    
    {
      "annotationSpecs": [
        {
          object ([AnnotationSpecRef](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ConfusionMatrix#AnnotationSpecRef))
        }
      ],
      "rows": [
        array
      ]
    }  
  
## AnnotationSpecRef

Fields  
  
`id` `string` id of the AnnotationSpec. | `displayName` `string` Display name of the AnnotationSpec. | JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
