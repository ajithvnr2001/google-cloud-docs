---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults
title: REST Resource: projects.locations.brands.evaluationCaseResults \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:03:04.207140+00:00
---

# REST Resource: projects.locations.brands.evaluationCaseResults  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)



Send feedback 

#  REST Resource: projects.locations.brands.evaluationCaseResults Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: EvaluationCaseResult
    * JSON representation
  * Status
  * MatcherResult
    * JSON representation
  * OrderResultMatcherResult
    * JSON representation
  * AgentUtteranceStringMatcherResult
    * JSON representation
  * LLMJudgementMatcherResult
    * JSON representation
  * Methods



## Resource: EvaluationCaseResult

An evaluation case result.

JSON representation  
---  
      
    
    {
      "name": string,
      "evaluationCase": {
        object ([EvaluationCase](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases#EvaluationCase))
      },
      "evaluationContext": {
        object ([EvaluationContext](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationContexts#EvaluationContext))
      },
      "evaluationDataset": string,
      "sessionRecord": string,
      "status": enum ([Status](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults#Status)),
      "matcherResults": [
        {
          object ([MatcherResult](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults#MatcherResult))
        }
      ],
      "createTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the evaluation case result. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationCaseResults/{evaluationCaseResult}  
`evaluationCase` |  `object (`[EvaluationCase](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases#EvaluationCase)`)` Output only. The evaluation case this result is associated with.  
`evaluationContext` |  `object (`[EvaluationContext](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationContexts#EvaluationContext)`)` Output only. The evaluation context this result is associated with.  
`evaluationDataset` |  `string` Output only. The evaluation dataset reference this result is associated with. If not set, it means the test case is run as a standalone test, not as part of an evaluation dataset. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationDatasets/{evaluationDataset}  
`sessionRecord` |  `string` Output only. The resource name of the session record this result is associated with. Format: projects/{project}/locations/{location}/brands/{brand}/sessionRecords/{sessionRecord}  
`status` |  `enum (`[Status](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults#Status)`)` Output only. The status of the evaluation case.  
`matcherResults[]` |  `object (`[MatcherResult](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults#MatcherResult)`)` Output only. The list of evaluation matcher results for the evaluation case. The results of the evaluation matchers.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The create time of the evaluation case result.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Status

The status of the evaluation case.

Enums  
---  
`STATUS_UNSPECIFIED` | Invalid status.  
`PASS` | All the evaluation matchers are satisfied.  
`FAIL` | At least one of the evaluation matchers is not satisfied.  
`ERROR` | There was an error that the BidiProcessOrder session terminated unexpectedly and the evaluation could not be completed.  
  
## MatcherResult

A result of an evaluation matcher.

JSON representation  
---  
      
    
    {
      "evaluationMatcher": {
        object ([EvaluationMatcher](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationMatchers#EvaluationMatcher))
      },
    
      // Union field result can be only one of the following:
      "orderResultMatcherResult": {
        object ([OrderResultMatcherResult](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults#OrderResultMatcherResult))
      },
      "agentUtteranceStringMatcherResult": {
        object ([AgentUtteranceStringMatcherResult](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults#AgentUtteranceStringMatcherResult))
      },
      "llmJudgementMatcherResult": {
        object ([LLMJudgementMatcherResult](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults#LLMJudgementMatcherResult))
      }
      // End of list of possible types for union field result.
    }  
  
Fields  
---  
`evaluationMatcher` |  `object (`[EvaluationMatcher](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationMatchers#EvaluationMatcher)`)` Output only. The evaluation matcher this result is associated with.  
Union field `result`. The result of the evaluation matcher. `result` can be only one of the following:  
`orderResultMatcherResult` |  `object (`[OrderResultMatcherResult](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults#OrderResultMatcherResult)`)` Output only. The result of an order result matcher.  
`agentUtteranceStringMatcherResult` |  `object (`[AgentUtteranceStringMatcherResult](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults#AgentUtteranceStringMatcherResult)`)` Output only. The result of an agent utterance string matcher.  
`llmJudgementMatcherResult` |  `object (`[LLMJudgementMatcherResult](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults#LLMJudgementMatcherResult)`)` Output only. The result of an agent utterance LLM judgement matcher.  
  
## OrderResultMatcherResult

A result of an order result matcher.

JSON representation  
---  
      
    
    {
      "match": boolean,
      "difference": string
    }  
  
Fields  
---  
`match` |  `boolean` Output only. Whether the order result matcher passed or not.  
`difference` |  `string` Output only. The pretty printed difference between the expected order and the actual order in the order result matcher in the (-want +got) format.  
  
## AgentUtteranceStringMatcherResult

A result of an agent utterance string matcher.

JSON representation  
---  
      
    
    {
      "match": boolean
    }  
  
Fields  
---  
`match` |  `boolean` Output only. Whether the agent utterance string matcher passed or not.  
  
## LLMJudgementMatcherResult

A result of an agent utterance LLM judgement matcher.

JSON representation  
---  
      
    
    {
      "match": boolean,
      "reasoning": string
    }  
  
Fields  
---  
`match` |  `boolean` Output only. Whether the agent utterance LLM judgement matcher passed or not.  
`reasoning` |  `string` Output only. Describes the reasoning on why the LLM judgement matched or failed.  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults/delete)`

|  Deletes the specified EvaluationCaseResult.  
  
### `[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults/get)`

|  Gets an EvaluationCaseResult.  
  
### `[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults/list)`

|  Lists EvaluationCaseResults.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-09 UTC."],[],[]] 
