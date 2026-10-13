---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.generators
title: REST Resource: projects.locations.agents.generators \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:33:25.119971+00:00
---

# REST Resource: projects.locations.agents.generators  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.generators

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  REST Resource: projects.locations.agents.generators Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Generator
    * JSON representation
  * Phrase
    * JSON representation
  * Placeholder
    * JSON representation
  * ModelParameter
    * JSON representation
  * Methods



## Resource: Generator

Generators contain prompt to be sent to the LLM model to generate text. The prompt can contain parameters which will be resolved before calling the model. It can optionally contain banned phrases to ensure the model responses are safe.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "promptText": {
        object ([Phrase](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.generators#Phrase))
      },
      "placeholders": [
        {
          object ([Placeholder](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.generators#Placeholder))
        }
      ],
      "llmModelSettings": {
        object ([LlmModelSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/LlmModelSettings))
      },
      "modelParameter": {
        object ([ModelParameter](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.generators#ModelParameter))
      }
    }  
  
Fields  
---  
`name` |  `string` The unique identifier of the generator. Must be set for the `[Generators.UpdateGenerator](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.generators/patch#google.cloud.dialogflow.cx.v3.Generators.UpdateGenerator)` method. [Generators.CreateGenerate][] populates the name automatically. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/generators/<GeneratorID>`.  
`displayName` |  `string` Required. The human-readable name of the generator, unique within the agent. The prompt contains pre-defined parameters such as $conversation, $last-user-utterance, etc. populated by Dialogflow. It can also contain custom placeholders which will be resolved during fulfillment.  
`promptText` |  `object (`[Phrase](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.generators#Phrase)`)` Required. Prompt for the LLM model.  
`placeholders[]` |  `object (`[Placeholder](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.generators#Placeholder)`)` Optional. List of custom placeholders in the prompt text.  
`llmModelSettings` |  `object (`[LlmModelSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/LlmModelSettings)`)` The LLM model settings.  
`modelParameter` |  `object (`[ModelParameter](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.generators#ModelParameter)`)` Parameters passed to the LLM to configure its behavior.  
  
## Phrase

Text input which can be used for prompt or banned phrases.

JSON representation  
---  
      
    
    {
      "text": string
    }  
  
Fields  
---  
`text` |  `string` Required. Text input which can be used for prompt or banned phrases.  
  
## Placeholder

Represents a custom placeholder in the prompt text.

JSON representation  
---  
      
    
    {
      "id": string,
      "name": string
    }  
  
Fields  
---  
`id` |  `string` Unique ID used to map custom placeholder to parameters in fulfillment.  
`name` |  `string` Custom placeholder value in the prompt text.  
  
## ModelParameter

Parameters to be passed to the LLM. If not set, default values will be used.

JSON representation  
---  
      
    
    {
      "temperature": number,
      "maxDecodeSteps": integer,
      "topP": number,
      "topK": integer
    }  
  
Fields  
---  
`temperature` |  `number` The temperature used for sampling. Temperature sampling occurs after both topP and topK have been applied. Valid range: [0.0, 1.0] Low temperature = less random. High temperature = more random.  
`maxDecodeSteps` |  `integer` The maximum number of tokens to generate.  
`topP` |  `number` If set, only the tokens comprising the top topP probability mass are considered. If both topP and topK are set, topP will be used for further refining candidates selected with topK. Valid range: (0.0, 1.0]. Small topP = less random. Large topP = more random.  
`topK` |  `integer` If set, the sampling process in each step is limited to the topK tokens with highest probabilities. Valid range: [1, 40] or 1000+. Small topK = less random. Large topK = more random.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.generators/create)`

|  Creates a generator in the specified agent.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.generators/delete)`

|  Deletes the specified generators.  
  
### `[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.generators/get)`

|  Retrieves the specified generator.  
  
### `[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.generators/list)`

|  Returns the list of all generators in the specified agent.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.generators/patch)`

|  Update the specified generator.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
