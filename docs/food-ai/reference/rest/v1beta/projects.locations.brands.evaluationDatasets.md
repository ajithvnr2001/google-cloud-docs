---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasets
title: REST Resource: projects.locations.brands.evaluationDatasets \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:57:38.689739+00:00
---

# REST Resource: projects.locations.brands.evaluationDatasets  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasets

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)



Send feedback 

#  REST Resource: projects.locations.brands.evaluationDatasets Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: EvaluationDataset
    * JSON representation
  * Methods



## Resource: EvaluationDataset

A dataset of evaluation cases.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "evaluationCases": [
        string
      ],
      "evaluationContext": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the evaluation dataset. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationDatasets/{evaluationDataset}  
`displayName` |  `string` Required. The human-readable name of the evaluation dataset.  
`description` |  `string` Optional. The description of the evaluation dataset.  
`evaluationCases[]` |  `string` Optional. The list of evaluation cases references for this dataset. Each case with the following format: projects/{project}/locations/{location}/brands/{brand}/evaluationCases/{evaluationCase}  
`evaluationContext` |  `string` Optional. Optional evaluation context to use for the evaluation dataset. If set, this overrides the evaluation context set in the individual evaluation cases. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationContexts/{evaluationContext}  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasets/create)`

|  Creates an EvaluationDataset.  
  
### `[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasets/delete)`

|  Deletes the specified EvaluationDataset.  
  
### `[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasets/get)`

|  Gets an EvaluationDataset.  
  
### `[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasets/list)`

|  Lists EvaluationDatasets.  
  
### `[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasets/patch)`

|  Updates the specified EvaluationDataset.  
  
### `[run](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasets/run)`

|  Runs an evaluation dataset.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-21 UTC."],[],[]] 
