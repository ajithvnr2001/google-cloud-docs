---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators
title: REST Resource: projects.generators \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:17.375662+00:00
---

# REST Resource: projects.generators  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  REST Resource: projects.generators Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Generator
    * JSON representation
    * FreeFormContext
      * JSON representation
    * AgentCoachingContext
      * JSON representation
    * AgentCoachingInstruction
      * JSON representation
    * DuplicateCheckResult
      * JSON representation
    * DuplicateSuggestion
      * JSON representation
    * TriggerEvent
    * SummarizationContext
      * JSON representation
    * SummarizationSection
      * JSON representation
    * Type
    * FewShotExample
      * JSON representation
    * ConversationContext
      * JSON representation
    * SummarizationSectionList
      * JSON representation
    * GeneratorSuggestion
      * JSON representation
    * FreeFormSuggestion
      * JSON representation
    * SummarySuggestion
      * JSON representation
    * AgentCoachingSuggestion
      * JSON representation
    * AgentActionSuggestion
      * JSON representation
    * Sources
      * JSON representation
    * DuplicateCheckResult
      * JSON representation
    * DuplicateSuggestion
      * JSON representation
    * SampleResponse
      * JSON representation
    * ToolCallInfo
      * JSON representation
    * ToolCall
      * JSON representation
    * State
    * ToolCallResult
      * JSON representation
    * Error
      * JSON representation
    * InferenceParameter
      * JSON representation
    * SuggestionDedupingConfig
      * JSON representation
    * CesAppSpec
      * JSON representation
  * Methods



## Resource: Generator

LLM generator.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "inferenceParameter": {
        object ([InferenceParameter](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.InferenceParameter))
      },
      "triggerEvent": enum ([TriggerEvent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/TriggerEvent)),
      "createTime": string,
      "updateTime": string,
      "tools": [
        string
      ],
      "suggestionDedupingConfig": {
        object ([SuggestionDedupingConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.SuggestionDedupingConfig))
      },
      "toolsetTools": [
        {
          object ([ToolsetTool](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ToolsetTool))
        }
      ],
      "cesToolSpecs": [
        {
          object ([CesToolSpec](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/CesToolSpec))
        }
      ],
      "cesAppSpecs": [
        {
          object ([CesAppSpec](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.CesAppSpec))
        }
      ],
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "freeFormContext": {
        object ([FreeFormContext](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.FreeFormContext))
      },
      "agentCoachingContext": {
        object ([AgentCoachingContext](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.AgentCoachingContext))
      },
      "summarizationContext": {
        object ([SummarizationContext](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.SummarizationContext))
      }
      // End of mutually exclusive fields.
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "publishedModel": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The resource name of the generator. Format: `projects/<Project ID>/locations/<Location ID>/generators/<Generator ID>`  
`description` |  `string` Optional. Human readable description of the generator.  
`inferenceParameter` |  `object (`[InferenceParameter](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.InferenceParameter)`)` Optional. Inference parameters for this generator.  
`triggerEvent` |  `enum (`[TriggerEvent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/TriggerEvent)`)` Optional. The trigger event of the generator. It defines when the generator is triggered in a conversation.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time of this generator.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update time of this generator.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`tools[]` |  `string` Optional. Resource names of the tools that the generator can choose from. Format: `projects/<Project ID>/locations/<Location ID>/tools/<tool ID>`.  
`suggestionDedupingConfig` |  `object (`[SuggestionDedupingConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.SuggestionDedupingConfig)`)` Optional. Configuration for suggestion deduping. This is only applicable to AI Coach feature.  
`toolsetTools[]` |  `object (`[ToolsetTool](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ToolsetTool)`)` Optional. List of CES toolset specs that the generator can choose from.  
`cesToolSpecs[]` |  `object (`[CesToolSpec](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/CesToolSpec)`)` Optional. List of CES tool specs that the generator can choose from.  
`cesAppSpecs[]  
**(deprecated)**` |  `object (`[CesAppSpec](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.CesAppSpec)`)` This item is deprecated!Optional. Deprecated: Use `cesToolSpecs` instead. List of CES app specs that the generator can choose from.  
Required. Input context of the generator. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`freeFormContext` |  `object (`[FreeFormContext](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.FreeFormContext)`)` Input of free from generator to LLM.  
`agentCoachingContext` |  `object (`[AgentCoachingContext](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.AgentCoachingContext)`)` Input of prebuilt Agent Coaching feature.  
`summarizationContext` |  `object (`[SummarizationContext](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.SummarizationContext)`)` Input of prebuilt Summarization feature.  
End of mutually exclusive fields.  
The foundation model to use for generating suggestions. If a foundation model isn't specified here, a model specifically tuned for the feature type (and version when applicable) will be used. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`publishedModel` |  `string` Optional. The published Large Language Model name. * To use the latest model version, specify the model name without version number. Example: `text-bison` * To use a stable model version, specify the version number as well. Example: `text-bison@002`.  
End of mutually exclusive fields.  
  
### FreeFormContext

Free form generator context that customer can configure.

JSON representation  
---  
      
    
    {
      "text": string
    }  
  
Fields  
---  
`text` |  `string` Optional. Free form text input to LLM.  
  
### AgentCoachingContext

Agent Coaching context that customer can configure.

JSON representation  
---  
      
    
    {
      "overarchingGuidance": string,
      "instructions": [
        {
          object ([AgentCoachingInstruction](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.AgentCoachingInstruction))
        }
      ],
      "version": string,
      "outputLanguageCode": string
    }  
  
Fields  
---  
`overarchingGuidance` |  `string` Optional. The overarching guidance for the agent coaching. This should be set only for v1.5 and later versions.  
`instructions[]` |  `object (`[AgentCoachingInstruction](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.AgentCoachingInstruction)`)` Optional. Customized instructions for agent coaching.  
`version` |  `string` Optional. Version of the feature. If not set, default to latest version. Current candidates are ["1.2"].  
`outputLanguageCode` |  `string` Optional. Output language code.  
  
### AgentCoachingInstruction

Agent Coaching instructions that customer can configure.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "displayDetails": string,
      "condition": string,
      "agentAction": string,
      "systemAction": string,
      "duplicateCheckResult": {
        object ([DuplicateCheckResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.DuplicateCheckResult))
      },
      "triggeringEvent": enum ([TriggerEvent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.TriggerEvent))
    }  
  
Fields  
---  
`displayName` |  `string` Optional. Display name for the instruction.  
`displayDetails` |  `string` Optional. The detailed description of this instruction.  
`condition` |  `string` Optional. The condition of the instruction. For example, "the customer wants to cancel an order". If the users want the instruction to be triggered unconditionally, the condition can be empty.  
`agentAction` |  `string` Optional. The action that human agent should take. For example, "apologize for the slow shipping". If the users only want to use agent coaching for intent detection, agentAction can be empty  
`systemAction` |  `string` Optional. The action that system should take. For example, "call GetOrderTime with order_number={order number provided by the customer}". If the users don't have plugins or don't want to trigger plugins, the systemAction can be empty  
`duplicateCheckResult` |  `object (`[DuplicateCheckResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.DuplicateCheckResult)`)` Output only. Duplication check for the AgentCoachingInstruction.  
`triggeringEvent` |  `enum (`[TriggerEvent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.TriggerEvent)`)` Optional. The event that should trigger this instruction. If UNSPECIFIED, the instruction triggering will be same as the generator's triggerEvent.  
  
### DuplicateCheckResult

Duplication check for the suggestion.

JSON representation  
---  
      
    
    {
      "duplicateSuggestions": [
        {
          object ([DuplicateSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.DuplicateSuggestion))
        }
      ]
    }  
  
Fields  
---  
`duplicateSuggestions[]` |  `object (`[DuplicateSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.DuplicateSuggestion)`)` Output only. The duplicate suggestions.  
  
### DuplicateSuggestion

The duplicate suggestion details.

JSON representation  
---  
      
    
    {
      "answerRecord": string,
      "suggestionIndex": integer,
      "similarityScore": number
    }  
  
Fields  
---  
`answerRecord` |  `string` Output only. The answer record id of the past duplicate suggestion.  
`suggestionIndex` |  `integer` Output only. The index of the duplicate suggestion in the past suggestion list.  
`similarityScore` |  `number` Output only. The similarity score of between the past and current suggestion.  
  
### TriggerEvent

The event that should trigger this instruction.

Enums  
---  
`TRIGGER_EVENT_UNSPECIFIED` | Default value for TriggerEvent.  
`END_OF_UTTERANCE` | Triggers when each chat message or voice utterance ends.  
`MANUAL_CALL` | Triggers on the conversation manually by API calls.  
`CUSTOMER_MESSAGE` | Triggers after each customer message.  
`AGENT_MESSAGE` | Triggers after each agent message.  
`TOOL_CALL_COMPLETION` | Triggers on tool call completion.  
  
### SummarizationContext

Summarization context that customer can configure.

JSON representation  
---  
      
    
    {
      "summarizationSections": [
        {
          object ([SummarizationSection](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.SummarizationSection))
        }
      ],
      "fewShotExamples": [
        {
          object ([FewShotExample](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.FewShotExample))
        }
      ],
      "version": string,
      "outputLanguageCode": string
    }  
  
Fields  
---  
`summarizationSections[]` |  `object (`[SummarizationSection](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.SummarizationSection)`)` Optional. List of sections. Note it contains both predefined section sand customer defined sections.  
`fewShotExamples[]` |  `object (`[FewShotExample](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.FewShotExample)`)` Optional. List of few shot examples.  
`version` |  `string` Optional. Version of the feature. If not set, default to latest version. Current candidates are ["1.0"].  
`outputLanguageCode` |  `string` Optional. The target language of the generated summary. The language code for conversation will be used if this field is empty. Supported 2.0 and later versions.  
  
### SummarizationSection

Represents the section of summarization.

JSON representation  
---  
      
    
    {
      "key": string,
      "definition": string,
      "type": enum ([Type](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.Type))
    }  
  
Fields  
---  
`key` |  `string` Optional. Name of the section, for example, "situation".  
`definition` |  `string` Optional. Definition of the section, for example, "what the customer needs help with or has question about."  
`type` |  `enum (`[Type](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.Type)`)` Optional. Type of the summarization section.  
  
### Type

Type enum of the summarization sections.

Enums  
---  
`TYPE_UNSPECIFIED` | Undefined section type, does not return anything.  
`SITUATION` | What the customer needs help with or has question about. Section name: "situation".  
`ACTION` | What the agent does to help the customer. Section name: "action".  
`RESOLUTION` | Result of the customer service. A single word describing the result of the conversation. Section name: "resolution".  
`REASON_FOR_CANCELLATION` | Reason for cancellation if the customer requests for a cancellation. "N/A" otherwise. Section name: "reason_for_cancellation".  
`CUSTOMER_SATISFACTION` | "Unsatisfied" or "Satisfied" depending on the customer's feelings at the end of the conversation. Section name: "customer_satisfaction".  
`ENTITIES` | Key entities extracted from the conversation, such as ticket number, order number, dollar amount, etc. Section names are prefixed by "entities/".  
`CUSTOMER_DEFINED` | Customer defined sections.  
`SITUATION_CONCISE` | Concise version of the situation section. This type is only available if type SITUATION is not selected.  
`ACTION_CONCISE` | Concise version of the action section. This type is only available if type ACTION is not selected.  
  
### FewShotExample

Providing examples in the generator (i.e. building a few-shot generator) helps convey the desired format of the LLM response.

JSON representation  
---  
      
    
    {
      "conversationContext": {
        object ([ConversationContext](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.ConversationContext))
      },
      "extraInfo": {
        string: string,
        ...
      },
      "output": {
        object ([GeneratorSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.GeneratorSuggestion))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "summarizationSectionList": {
        object ([SummarizationSectionList](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.SummarizationSectionList))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`conversationContext` |  `object (`[ConversationContext](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.ConversationContext)`)` Optional. Conversation transcripts.  
`extraInfo` |  `map (key: string, value: string)` Optional. Key is the placeholder field name in input, value is the value of the placeholder. E.g. instruction contains "@price", and ingested data has <"price", "10">An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`output` |  `object (`[GeneratorSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.GeneratorSuggestion)`)` Required. Example output of the model.  
Instruction list of this few_shot example. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`summarizationSectionList` |  `object (`[SummarizationSectionList](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.SummarizationSectionList)`)` Summarization sections.  
End of mutually exclusive fields.  
  
### ConversationContext

Context of the conversation, including transcripts.

JSON representation  
---  
      
    
    {
      "messageEntries": [
        {
          object ([MessageEntry](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/MessageEntry))
        }
      ]
    }  
  
Fields  
---  
`messageEntries[]` |  `object (`[MessageEntry](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/MessageEntry)`)` Optional. List of message transcripts in the conversation.  
  
### SummarizationSectionList

List of summarization sections.

JSON representation  
---  
      
    
    {
      "summarizationSections": [
        {
          object ([SummarizationSection](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.SummarizationSection))
        }
      ]
    }  
  
Fields  
---  
`summarizationSections[]` |  `object (`[SummarizationSection](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.SummarizationSection)`)` Optional. Summarization sections.  
  
### GeneratorSuggestion

Suggestion generated using a Generator.

JSON representation  
---  
      
    
    {
      "toolCallInfo": [
        {
          object ([ToolCallInfo](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.ToolCallInfo))
        }
      ],
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "freeFormSuggestion": {
        object ([FreeFormSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.FreeFormSuggestion))
      },
      "summarySuggestion": {
        object ([SummarySuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.SummarySuggestion))
      },
      "agentCoachingSuggestion": {
        object ([AgentCoachingSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.AgentCoachingSuggestion))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`toolCallInfo[]` |  `object (`[ToolCallInfo](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.ToolCallInfo)`)` Optional. List of request and response for tool calls executed.  
The suggestion could be one of the many types The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`freeFormSuggestion` |  `object (`[FreeFormSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.FreeFormSuggestion)`)` Optional. Free form suggestion.  
`summarySuggestion` |  `object (`[SummarySuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.SummarySuggestion)`)` Optional. Suggested summary.  
`agentCoachingSuggestion` |  `object (`[AgentCoachingSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.AgentCoachingSuggestion)`)` Optional. Suggestion to coach the agent.  
End of mutually exclusive fields.  
  
### FreeFormSuggestion

Suggestion generated using free form generator.

JSON representation  
---  
      
    
    {
      "response": string
    }  
  
Fields  
---  
`response` |  `string` Required. Free form suggestion.  
  
### SummarySuggestion

Suggested summary of the conversation.

JSON representation  
---  
      
    
    {
      "summarySections": [
        {
          object ([SummarySection](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/SummarySection))
        }
      ]
    }  
  
Fields  
---  
`summarySections[]` |  `object (`[SummarySection](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/SummarySection)`)` Required. All the parts of generated summary.  
  
### AgentCoachingSuggestion

Suggestion for coaching agents.

JSON representation  
---  
      
    
    {
      "applicableInstructions": [
        {
          object ([AgentCoachingInstruction](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.AgentCoachingInstruction))
        }
      ],
      "agentActionSuggestions": [
        {
          object ([AgentActionSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.AgentActionSuggestion))
        }
      ],
      "sampleResponses": [
        {
          object ([SampleResponse](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.SampleResponse))
        }
      ]
    }  
  
Fields  
---  
`applicableInstructions[]` |  `object (`[AgentCoachingInstruction](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.AgentCoachingInstruction)`)` Optional. Instructions applicable based on the current context.  
`agentActionSuggestions[]` |  `object (`[AgentActionSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.AgentActionSuggestion)`)` Optional. Suggested actions for the agent to take.  
`sampleResponses[]` |  `object (`[SampleResponse](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.SampleResponse)`)` Optional. Sample response for the Agent.  
  
### AgentActionSuggestion

Actions suggested for the agent. This is based on applicable instructions.

JSON representation  
---  
      
    
    {
      "agentAction": string,
      "sources": {
        object ([Sources](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.Sources))
      },
      "duplicateCheckResult": {
        object ([DuplicateCheckResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.DuplicateCheckResult_1))
      }
    }  
  
Fields  
---  
`agentAction` |  `string` Optional. The suggested action for the agent.  
`sources` |  `object (`[Sources](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.Sources)`)` Output only. Sources for the agent action suggestion.  
`duplicateCheckResult` |  `object (`[DuplicateCheckResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.DuplicateCheckResult_1)`)` Output only. Duplicate check result for the agent action suggestion.  
  
### Sources

Sources for the suggestion.

JSON representation  
---  
      
    
    {
      "instructionIndexes": [
        integer
      ]
    }  
  
Fields  
---  
`instructionIndexes[]` |  `integer` Output only. Source instruction indexes for the suggestion. This is the index of the applicableInstructions field.  
  
### DuplicateCheckResult

Duplication check for the suggestion.

JSON representation  
---  
      
    
    {
      "duplicateSuggestions": [
        {
          object ([DuplicateSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.DuplicateSuggestion_1))
        }
      ]
    }  
  
Fields  
---  
`duplicateSuggestions[]` |  `object (`[DuplicateSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.DuplicateSuggestion_1)`)` Output only. The duplicate suggestions.  
  
### DuplicateSuggestion

The duplicate suggestion details. Keeping answerRecord and sources together as they are identifiers for duplicate suggestions.

JSON representation  
---  
      
    
    {
      "answerRecord": string,
      "sources": {
        object ([Sources](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.Sources))
      },
      "suggestionIndex": integer,
      "similarityScore": number
    }  
  
Fields  
---  
`answerRecord` |  `string` Output only. The answer record id of the past duplicate suggestion.  
`sources` |  `object (`[Sources](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.Sources)`)` Output only. Sources for the suggestion.  
`suggestionIndex` |  `integer` Output only. The index of the duplicate suggestion in the past suggestion list.  
`similarityScore` |  `number` Output only. The similarity score of between the past and current suggestion.  
  
### SampleResponse

Sample response that the agent can use. This could be based on applicable instructions and ingested data from other systems.

JSON representation  
---  
      
    
    {
      "responseText": string,
      "sources": {
        object ([Sources](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.Sources))
      },
      "duplicateCheckResult": {
        object ([DuplicateCheckResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.DuplicateCheckResult_1))
      }
    }  
  
Fields  
---  
`responseText` |  `string` Optional. Sample response for Agent in text.  
`sources` |  `object (`[Sources](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.Sources)`)` Output only. Sources for the Sample Response.  
`duplicateCheckResult` |  `object (`[DuplicateCheckResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.DuplicateCheckResult_1)`)` Output only. Duplicate check result for the sample response.  
  
### ToolCallInfo

Request and response for a tool call.

JSON representation  
---  
      
    
    {
      "toolCall": {
        object ([ToolCall](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.ToolCall))
      },
      "toolCallResult": {
        object ([ToolCallResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.ToolCallResult))
      }
    }  
  
Fields  
---  
`toolCall` |  `object (`[ToolCall](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.ToolCall)`)` Required. Request for a tool call.  
`toolCallResult` |  `object (`[ToolCallResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.ToolCallResult)`)` Required. Response for a tool call.  
  
### ToolCall

Represents a call of a specific tool's action with the specified inputs.

JSON representation  
---  
      
    
    {
      "toolDisplayName": string,
      "toolDisplayDetails": string,
      "action": string,
      "inputParameters": {
        object
      },
      "createTime": string,
      "answerRecord": string,
      "state": enum ([State](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.State)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "tool": string,
      "cesTool": string,
      "cesToolset": string,
      "cesApp": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`toolDisplayName` |  `string` Optional. A human readable short name of the tool, to be shown on the UI.  
`toolDisplayDetails` |  `string` Optional. A human readable description of the tool.  
`action` |  `string` Optional. The name of the tool's action associated with this call.  
`inputParameters` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The action's input parameters.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create time of the tool call.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`answerRecord` |  `string` Optional. The answer record associated with this tool call.  
`state` |  `enum (`[State](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.State)`)` Output only. State of the tool call.  
Specifies the source of this tool call. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`tool` |  `string` Optional. The `[tool](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.tools#Tool)` associated with this call. Format: `projects/<ProjectID>/locations/<LocationID>/tools/<ToolID>`.  
`cesTool` |  `string` Optional. CES tool name for this call. Format: `projects/<ProjectID>/locations/<LocationID>/apps/<AppID>/tools/<ToolID>`.  
`cesToolset` |  `string` Optional. CES toolset name for this call. Format: `projects/<ProjectID>/locations/<LocationID>/apps/<AppID>/toolsets/ToolsetID>`.  
`cesApp` |  `string` Optional. CES app name for this call. Format: `projects/<ProjectID>/locations/<LocationID>/apps/<AppID>`.  
End of mutually exclusive fields.  
  
### State

Tool call states.

Enums  
---  
`STATE_UNSPECIFIED` | Default value.  
`TRIGGERED` | The tool call has been triggered.  
`NEEDS_CONFIRMATION` | The tool call requires confirmation from a human.  
  
### ToolCallResult

The result of calling a tool's action.

JSON representation  
---  
      
    
    {
      "action": string,
      "createTime": string,
      "answerRecord": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "tool": string,
      "cesToolset": string,
      "cesTool": string,
      "cesApp": string
      // End of mutually exclusive fields.
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "error": {
        object ([Error](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.Error))
      },
      "rawContent": string,
      "content": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`action` |  `string` Optional. The name of the tool's action associated with this call.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create time of the tool call result.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`answerRecord` |  `string` Optional. The answer record associated with this tool call result.  
Specifies the source of this tool call. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`tool` |  `string` Optional. The `[tool](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.tools#Tool)` associated with this call. Format: `projects/<ProjectID>/locations/<LocationID>/tools/<ToolID>`.  
`cesToolset` |  `string` Optional. CES toolset name for this call. Format: `projects/<ProjectID>/locations/<LocationID>/apps/<AppID>/toolsets/ToolsetID>`.  
`cesTool` |  `string` Optional. CES tool name for this call. Format: `projects/<ProjectID>/locations/<LocationID>/apps/<AppID>/tools/<ToolID>`.  
`cesApp` |  `string` Optional. CES app name for this call. Format: `projects/<ProjectID>/locations/<LocationID>/apps/<AppID>`.  
End of mutually exclusive fields.  
The tool call's result. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`error` |  `object (`[Error](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators#Generator.Error)`)` Optional. The tool call's error.  
`rawContent` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. Only populated if the response content is not utf-8 encoded. (by definition byte fields are base64 encoded).A base64-encoded string.  
`content` |  `string` Optional. Only populated if the response content is utf-8 encoded.  
End of mutually exclusive fields.  
  
### Error

An error produced by the tool call.

JSON representation  
---  
      
    
    {
      "message": string,
      "retryable": boolean
    }  
  
Fields  
---  
`message` |  `string` Optional. The error message of the function.  
`retryable` |  `boolean` Optional. Specifies whether the tool call is retryable.  
  
### InferenceParameter

The parameters of inference.

JSON representation  
---  
      
    
    {
      "maxOutputTokens": integer,
      "temperature": number,
      "topK": integer,
      "topP": number
    }  
  
Fields  
---  
`maxOutputTokens` |  `integer` Optional. Maximum number of the output tokens for the generator.  
`temperature` |  `number` Optional. Controls the randomness of LLM predictions. Low temperature = less random. High temperature = more random. If unset (or 0), uses a default value of 0.  
`topK` |  `integer` Optional. Top-k changes how the model selects tokens for output. A top-k of 1 means the selected token is the most probable among all tokens in the model's vocabulary (also called greedy decoding), while a top-k of 3 means that the next token is selected from among the 3 most probable tokens (using temperature). For each token selection step, the top K tokens with the highest probabilities are sampled. Then tokens are further filtered based on topP with the final token selected using temperature sampling. Specify a lower value for less random responses and a higher value for more random responses. Acceptable value is [1, 40], default to 40.  
`topP` |  `number` Optional. Top-p changes how the model selects tokens for output. Tokens are selected from most K (see topK parameter) probable to least until the sum of their probabilities equals the top-p value. For example, if tokens A, B, and C have a probability of 0.3, 0.2, and 0.1 and the top-p value is 0.5, then the model will select either A or B as the next token (using temperature) and doesn't consider C. The default top-p value is 0.95. Specify a lower value for less random responses and a higher value for more random responses. Acceptable value is [0.0, 1.0], default to 0.95.  
  
### SuggestionDedupingConfig

Config for suggestion deduping. NEXT_ID: 3

JSON representation  
---  
      
    
    {
      "enableDeduping": boolean,
      "similarityThreshold": number
    }  
  
Fields  
---  
`enableDeduping` |  `boolean` Optional. Whether to enable suggestion deduping.  
`similarityThreshold` |  `number` Optional. The threshold for similarity between two suggestions. Acceptable value is [0.0, 1.0], default to 0.8  
  
### CesAppSpec

This item is deprecated!

Deprecated: Use `CesToolSpec` instead. Spec of CES app that the generator can choose from.

JSON representation  
---  
      
    
    {
      "cesApp": string,
      "confirmationRequirement": enum ([ConfirmationRequirement](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ConfirmationRequirement)),
      "proactiveEnabled": boolean,
      "reactiveEnabled": boolean
    }  
  
Fields  
---  
`cesApp` |  `string` Optional. Format: `projects/<Project ID>/locations/<Location ID>/apps/<app ID>`.  
`confirmationRequirement` |  `enum (`[ConfirmationRequirement](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ConfirmationRequirement)`)` Optional. Indicates whether the app requires human confirmation.  
`proactiveEnabled` |  `boolean` Optional. Only applicable for CompanionAgent. Indicates whether the ces app is enabled in proactive mode. At least one of `proactiveEnabled` or `reactiveEnabled` should be true; otherwise, the ces app will be ignored.  
`reactiveEnabled` |  `boolean` Optional. Only applicable for CompanionAgent. Indicates whether the ces app is enabled in reactive mode. At least one of `proactiveEnabled` or `reactiveEnabled` should be true; otherwise, the ces app will be ignored.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators/create)`

|  Creates a generator.  
  
### `[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.generators/list)`

|  Lists generators.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
