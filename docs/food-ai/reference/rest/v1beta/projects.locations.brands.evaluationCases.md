---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases
title: REST Resource: projects.locations.brands.evaluationCases \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:27:35.695139+00:00
---

# REST Resource: projects.locations.brands.evaluationCases  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)



Send feedback 

#  REST Resource: projects.locations.brands.evaluationCases Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: EvaluationCase
    * JSON representation
    * StaticTextTurnCase
      * JSON representation
    * TextTurn
      * JSON representation
    * DynamicTextTurnCase
      * JSON representation
  * Methods



## Resource: EvaluationCase

An individual evaluation case.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "evaluationContext": string,
      "evaluationMatchers": [
        string
      ],
    
      // Union field test_case can be only one of the following:
      "staticTextTurnCase": {
        object ([StaticTextTurnCase](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases#EvaluationCase.StaticTextTurnCase))
      },
      "dynamicTextTurnCase": {
        object ([DynamicTextTurnCase](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases#EvaluationCase.DynamicTextTurnCase))
      }
      // End of list of possible types for union field test_case.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the evaluation case. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationCases/{evaluationCase}  
`displayName` |  `string` Required. The human-readable name of the evaluation case.  
`description` |  `string` Optional. The description of the evaluation case.  
`evaluationContext` |  `string` Required. The resource name of the evaluation context this case is associated with. Format: projects/{project}/locations/{location}/brands/{brand}/evaluationContexts/{evaluationContext}  
`evaluationMatchers[]` |  `string` Optional. The list of evaluation matchers to use for the evaluation case. The evaluation is performed once at the end of the BidiProcessOrder session. Each matcher produces a boolean result indicating whether the evaluation matcher passed or failed.  
Union field `test_case`. The test case to use for the evaluation case. `test_case` can be only one of the following:  
`staticTextTurnCase` |  `object (`[StaticTextTurnCase](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases#EvaluationCase.StaticTextTurnCase)`)` Optional. A test case where the user and agent text turns are static.  
`dynamicTextTurnCase` |  `object (`[DynamicTextTurnCase](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases#EvaluationCase.DynamicTextTurnCase)`)` Optional. A test case where the user text inputs are dynamically generated using LLM with an ordering instruction.  
  
### StaticTextTurnCase

An evaluation case where the user inputs are static text inputs.

JSON representation  
---  
      
    
    {
      "textTurns": [
        {
          object ([TextTurn](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases#EvaluationCase.TextTurn))
        }
      ]
    }  
  
Fields  
---  
`textTurns[]` |  `object (`[TextTurn](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases#EvaluationCase.TextTurn)`)` Required. The list of text turns in the evaluation case.  
  
### TextTurn

A single text turn in the evaluation case, consisting of user input and agent response.

JSON representation  
---  
      
    
    {
      "userTextInput": string,
      "exampleAgentResponse": string
    }  
  
Fields  
---  
`userTextInput` |  `string` Required. The user text input for this turn.  
`exampleAgentResponse` |  `string` Optional. The example agent response for this turn. Note that this is not the actual agent response. The actual agent response may differ from this example response. The example response is NOT used for evaluation, but only for display purposes to make the evaluation case easier to understand.  
  
### DynamicTextTurnCase

An evaluation case where the user inputs are dynamically generated using LLM with an ordering instruction.

JSON representation  
---  
      
    
    {
      "orderingInstruction": string
    }  
  
Fields  
---  
`orderingInstruction` |  `string` Required. The ordering instruction for the user to interact with the Food Ordering Agent. LLM dynamically generates the user text inputs based on the ordering instruction. This may include the targeted items to order, the user's preferences and constraints, and specific actions to that the user should inform the ordering agent.  
  
## Methods  
  
---  
  
### `[batchCreate](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases/batchCreate)`

|  Batch creates EvaluationCases.  
  
### `[batchUpdate](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases/batchUpdate)`

|  Batch updates EvaluationCases.  
  
### `[create](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases/create)`

|  Creates an EvaluationCase.  
  
### `[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases/delete)`

|  Deletes the specified EvaluationCase.  
  
### `[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases/get)`

|  Gets an EvaluationCase.  
  
### `[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases/list)`

|  Lists EvaluationCases.  
  
### `[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases/patch)`

|  Updates the specified EvaluationCase.  
  
### `[run](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases/run)`

|  Runs an evaluation case.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-15 UTC."],[],[]] 
