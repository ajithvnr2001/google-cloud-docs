---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.models.evaluations.slices
title: REST Resource: projects.locations.models.evaluations.slices \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:29:07.478297+00:00
---

# REST Resource: projects.locations.models.evaluations.slices  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.models.evaluations.slices

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  REST Resource: projects.locations.models.evaluations.slices Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: ModelEvaluationSlice

A collection of metrics calculated by comparing Model's predictions on a slice of the test data against ground truth annotations.

Fields  
  
`name` `string` Output only. The resource name of the ModelEvaluationSlice. | `slice` `object (`[Slice](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.models.evaluations.slices#Slice)`)` Output only. The slice of the test data that is used to evaluate the Model. | `metricsSchemaUri` `string` Output only. Points to a YAML file stored on Google Cloud Storage describing the `[metrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.models.evaluations.slices#ModelEvaluationSlice.FIELDS.metrics)` of this ModelEvaluationSlice. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). | `metrics` `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Output only. Sliced evaluation metrics of the Model. The schema of the metrics is stored in `[metricsSchemaUri](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.models.evaluations.slices#ModelEvaluationSlice.FIELDS.metrics_schema_uri)` | `createTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. timestamp when this ModelEvaluationSlice was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `modelExplanation` `object (`[ModelExplanation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelExplanation)`)` Output only. Aggregated explanation metrics for the Model's prediction output over the data this ModelEvaluation uses. This field is populated only if the Model is evaluated with explanations, and only for tabular Models. | JSON representation  
---  
      
    
    {
      "name": string,
      "slice": {
        object ([Slice](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.models.evaluations.slices#Slice))
      },
      "metricsSchemaUri": string,
      "metrics": value,
      "createTime": string,
      "modelExplanation": {
        object ([ModelExplanation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ModelExplanation))
      }
    }  
  
## Slice

Definition of a slice.

Fields  
  
`dimension` `string` Output only. The dimension of the slice. Well-known dimensions are: * `annotationSpec`: This slice is on the test data that has either ground truth or prediction with `[AnnotationSpec.display_name](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.datasets.annotationSpecs#AnnotationSpec.FIELDS.display_name)` equals to `[value](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.models.evaluations.slices#Slice.FIELDS.value)`. * `slice`: This slice is a user customized slice defined by its SliceSpec. | `value` `string` Output only. The value of the dimension in this slice. | `sliceSpec` `object (`[SliceSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/SliceSpec)`)` Output only. Specification for how the data was sliced. | JSON representation  
---  
      
    
    {
      "dimension": string,
      "value": string,
      "sliceSpec": {
        object ([SliceSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/SliceSpec))
      }
    }  
  
## Methods  
  
---  
  
### `[batchImport](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.models.evaluations.slices/batchImport)`

|  Imports a list of externally generated EvaluatedAnnotations.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.models.evaluations.slices/get)`

|  Gets a ModelEvaluationSlice.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.models.evaluations.slices/list)`

|  Lists ModelEvaluationSlices in a ModelEvaluation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
