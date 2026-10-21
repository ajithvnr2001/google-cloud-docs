---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationMatchers
title: REST Resource: projects.locations.brands.evaluationMatchers \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:45:12.407290+00:00
---

# REST Resource: projects.locations.brands.evaluationMatchers  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationMatchers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)



Send feedback 

#  REST Resource: projects.locations.brands.evaluationMatchers Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: EvaluationMatcher
    * JSON representation
    * OrderResultMatcher
      * JSON representation
    * AgentUtteranceStringMatcher
      * JSON representation
    * LLMJudgementMatcher
      * JSON representation
  * Methods



## Resource: EvaluationMatcher

An evaluation matcher.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
    
      // Union field matcher can be only one of the following:
      "orderResultMatcher": {
        object ([OrderResultMatcher](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationMatchers#EvaluationMatcher.OrderResultMatcher))
      },
      "agentUtteranceStringMatcher": {
        object ([AgentUtteranceStringMatcher](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationMatchers#EvaluationMatcher.AgentUtteranceStringMatcher))
      },
      "llmJudgementMatcher": {
        object ([LLMJudgementMatcher](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationMatchers#EvaluationMatcher.LLMJudgementMatcher))
      }
      // End of list of possible types for union field matcher.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the evaluation matcher.  
`displayName` |  `string` Required. The human-readable name of the evaluation matcher.  
`description` |  `string` Optional. The description of the evaluation matcher.  
Union field `matcher`. The matcher to use for the evaluation matcher. The matcher must produce a boolean result indicating whether the evaluation matcher passed or not. `matcher` can be only one of the following:  
`orderResultMatcher` |  `object (`[OrderResultMatcher](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationMatchers#EvaluationMatcher.OrderResultMatcher)`)` Optional. An evaluation matcher for an order result.  
`agentUtteranceStringMatcher` |  `object (`[AgentUtteranceStringMatcher](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationMatchers#EvaluationMatcher.AgentUtteranceStringMatcher)`)` Optional. An evaluation matcher for an agent utterance string.  
`llmJudgementMatcher` |  `object (`[LLMJudgementMatcher](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationMatchers#EvaluationMatcher.LLMJudgementMatcher)`)` Optional. An evaluation matcher using LLM judgement.  
  
### OrderResultMatcher

An evaluation matcher for an order result.

JSON representation  
---  
      
    
    {
      "expectedOrder": {
        object ([Order](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/Order))
      },
      "expectedLegacyOrder": {
        object
      }
    }  
  
Fields  
---  
`expectedOrder` |  `object (`[Order](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/Order)`)` Required. The expected order to match against. The actual order must match this expected order after normalization. The evaluation passes if all fields and quantities match. Default quantities of 1 are ignored during comparison to handle field omission consistently.  
`expectedLegacyOrder` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The expected legacy order state to match against. Used when the evaluation context has useLegacyOrderState set to true.  
  
### AgentUtteranceStringMatcher

An evaluation matcher for an agent utterance string.

JSON representation  
---  
      
    
    {
      "invert": boolean,
    
      // Union field match_pattern can be only one of the following:
      "contains": string,
      "regex": string
      // End of list of possible types for union field match_pattern.
    }  
  
Fields  
---  
`invert` |  `boolean` Optional. If true, the match condition is inverted (e.g., "does not contain" or "does not match").  
Union field `match_pattern`.`match_pattern` can be only one of the following:  
`contains` |  `string` Optional. The agent utterance should contain this substring.  
`regex` |  `string` Optional. The agent utterance should match this regex.  
  
### LLMJudgementMatcher

An evaluation matcher using LLM judgement with the following prompt: "You are a helpful assistant that helps users place food orders at a restaurant. You will be given user inputs and agent responses. Your task is to determine if the agent response satisfies the following criteria: {criteria}"

JSON representation  
---  
      
    
    {
      "criteria": string,
      "invert": boolean
    }  
  
Fields  
---  
`criteria` |  `string` Required. The criteria for the LLM to consider if an agent response passes the check.  
`invert` |  `boolean` Optional. If true, the match condition is inverted (e.g., "does not contain").  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationMatchers/create)`

|  Creates an EvaluationMatcher.  
  
### `[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationMatchers/delete)`

|  Deletes the specified EvaluationMatcher.  
  
### `[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationMatchers/get)`

|  Gets an EvaluationMatcher.  
  
### `[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationMatchers/list)`

|  Lists EvaluationMatchers.  
  
### `[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationMatchers/patch)`

|  Updates the specified EvaluationMatcher.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-21 UTC."],[],[]] 
