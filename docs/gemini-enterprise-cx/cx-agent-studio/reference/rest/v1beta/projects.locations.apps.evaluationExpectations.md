---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationExpectations
title: REST Resource: projects.locations.apps.evaluationExpectations \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:47.506428+00:00
---

# REST Resource: projects.locations.apps.evaluationExpectations  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationExpectations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  REST Resource: projects.locations.apps.evaluationExpectations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: EvaluationExpectation
    * JSON representation
  * EvaluationExpectation.LlmCriteria
    * JSON representation
  * Methods



## Resource: EvaluationExpectation

An evaluation expectation represents a specific criteria to evaluate against.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "tags": [
        string
      ],
      "createTime": string,
      "updateTime": string,
      "etag": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "llmCriteria": {
        object ([EvaluationExpectation.LlmCriteria](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationExpectations#EvaluationExpectation.LlmCriteria))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of this evaluation expectation. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationExpectations/{evaluationExpectation}`  
`displayName` |  `string` Required. User-defined display name. Must be unique within the app.  
`tags[]` |  `string` Optional. User-defined tags for expectations. Can be used to filter expectations.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the evaluation expectation was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the evaluation expectation was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
The definition of the criteria used for evaluation. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`llmCriteria` |  `object (`[EvaluationExpectation.LlmCriteria](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationExpectations#EvaluationExpectation.LlmCriteria)`)` Optional. Evaluation criteria based on an LLM prompt.  
End of mutually exclusive fields.  
  
## EvaluationExpectation.LlmCriteria

Configuration for LLM-based evaluation criteria.

JSON representation  
---  
      
    
    {
      "prompt": string
    }  
  
Fields  
---  
`prompt` |  `string` Required. The prompt/instructions provided to the LLM judge.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationExpectations/create)`

|  Creates an evaluation expectation.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationExpectations/delete)`

|  Deletes an evaluation expectation.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationExpectations/get)`

|  Gets details of the specified evaluation expectation.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationExpectations/list)`

|  Lists all evaluation expectations in the given app.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.evaluationExpectations/patch)`

|  Updates an evaluation expectation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
