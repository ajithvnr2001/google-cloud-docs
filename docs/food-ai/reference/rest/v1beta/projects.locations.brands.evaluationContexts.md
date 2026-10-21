---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationContexts
title: REST Resource: projects.locations.brands.evaluationContexts \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:47:09.337060+00:00
---

# REST Resource: projects.locations.brands.evaluationContexts  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationContexts

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)



Send feedback 

#  REST Resource: projects.locations.brands.evaluationContexts Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: EvaluationContext
    * JSON representation
    * MockClientExecution
      * JSON representation
  * Methods



## Resource: EvaluationContext

An evaluation context for an evaluation suite or case.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "store": string,
      "menu": string,
      "testSessionStartTime": string,
      "mockClientExecutions": [
        {
          object ([MockClientExecution](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationContexts#EvaluationContext.MockClientExecution))
        }
      ],
      "daypartId": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The full resource name of the evaluation context. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationContexts/{evaluationContext}  
`displayName` |  `string` Required. The human-readable name of the evaluation context.  
`description` |  `string` Optional. The description of the evaluation context.  
`store` |  `string` Required. The full resource name of the store to use for the evaluation case. Format: projects/{projectId}/locations/{location}/brands/{brandId}/stores/{storeId}  
`menu` |  `string` Optional. Optional menu to use for the evaluation context. If not provided, it will use the default menu for the store. Format: projects/{projectId}/locations/{location}/brands/{brandId}/menus/{menuId}  
`testSessionStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Optional injected start time of the Food Ordering session. If set, the evaluation session will assume the test session started at this time. This is for simulating ordering behavior at a specific time of day. If not set, the evaluation session will use the current time as the start time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`mockClientExecutions[]` |  `object (`[MockClientExecution](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationContexts#EvaluationContext.MockClientExecution)`)` Optional. Optional mocked client execution responses for client execution requests sent by the food ordering service during the evaluation session.  
`daypartId` |  `string` Optional. Optional daypart ID to use for the evaluation context. If provided, the agent will use this daypart ID when establishing the process order configuration.  
  
### MockClientExecution

Represents a mocked client execution request and response pair. If the requests sent by the food ordering service in an eval run matches the mock request, the mock response will be returned to the service. Note the request.execution_id will be ignored during matching since it's session specific.

JSON representation  
---  
      
    
    {
      "rawJsonRequest": {
        object
      },
      "rawJsonResponse": {
        object
      }
    }  
  
Fields  
---  
`rawJsonRequest` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The request for the mock client execution.  
`rawJsonResponse` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The response for the mock client execution.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationContexts/create)`

|  Creates an EvaluationContext.  
  
### `[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationContexts/delete)`

|  Deletes the specified EvaluationContext.  
  
### `[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationContexts/get)`

|  Gets an EvaluationContext.  
  
### `[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationContexts/list)`

|  Lists EvaluationContexts.  
  
### `[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationContexts/patch)`

|  Updates the specified EvaluationContext.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-09 UTC."],[],[]] 
