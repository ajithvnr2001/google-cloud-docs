---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasetResults
title: REST Resource: projects.locations.brands.evaluationDatasetResults \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:41:58.026547+00:00
---

# REST Resource: projects.locations.brands.evaluationDatasetResults  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasetResults

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)



Send feedback 

#  REST Resource: projects.locations.brands.evaluationDatasetResults Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: EvaluationDatasetResult
    * JSON representation
  * Methods



## Resource: EvaluationDatasetResult

An evaluation dataset result.

JSON representation  
---  
      
    
    {
      "name": string,
      "evaluationDataset": string,
      "evaluationCaseResults": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the evaluation dataset result. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationDatasetResults/{evaluation_dataset_result}  
`evaluationDataset` |  `string` Output only. The evaluation dataset reference this result is associated with. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationDatasets/{evaluationDataset}  
`evaluationCaseResults[]` |  `string` Output only. The list of evaluation case results for the evaluation dataset. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationCaseResults/{evaluationCaseResult}  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasetResults/delete)`

|  Deletes the specified EvaluationDatasetResult.  
  
### `[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasetResults/get)`

|  Gets an EvaluationDatasetResult.  
  
### `[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasetResults/list)`

|  Lists EvaluationDatasetResults.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-09 UTC."],[],[]] 
