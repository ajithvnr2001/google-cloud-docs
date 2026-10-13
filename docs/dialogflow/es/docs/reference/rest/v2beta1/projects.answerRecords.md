---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords
title: REST Resource: projects.answerRecords \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:50:48.234534+00:00
---

# REST Resource: projects.answerRecords  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  REST Resource: projects.answerRecords Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AnswerRecord
    * JSON representation
    * AnswerFeedback
      * JSON representation
    * CorrectnessLevel
    * AgentAssistantFeedback
      * JSON representation
    * AnswerRelevance
    * DocumentCorrectness
    * DocumentEfficiency
    * SummarizationFeedback
      * JSON representation
    * KnowledgeSearchFeedback
      * JSON representation
    * KnowledgeAssistFeedback
      * JSON representation
    * CompanionFeedback
    * AgentAssistantRecord
      * JSON representation
    * ArticleAnswer
      * JSON representation
    * FaqAnswer
      * JSON representation
    * DialogflowAssistAnswer
      * JSON representation
    * QueryResult
      * JSON representation
    * SentimentAnalysisResult
      * JSON representation
    * Sentiment
      * JSON representation
    * KnowledgeAnswers
      * JSON representation
    * Answer
      * JSON representation
    * MatchConfidenceLevel
    * IntentSuggestion
      * JSON representation
    * CompanionSuggestion
      * JSON representation
    * Guidance
      * JSON representation
    * KnowledgeSource
      * JSON representation
    * GroundingMetadata
      * JSON representation
    * SearchEntryPoint
      * JSON representation
    * GroundingChunk
      * JSON representation
    * Web
      * JSON representation
    * RetrievedContext
      * JSON representation
    * GroundingSupport
      * JSON representation
    * Segment
      * JSON representation
    * ToolCallSuggestion
      * JSON representation
    * ReactiveModeResponse
      * JSON representation
  * Methods



## Resource: AnswerRecord

Answer records are records to manage answer history and feedbacks for Dialogflow.

Currently, answer record includes:

  * human agent assistant article suggestion
  * human agent assistant faq article



It doesn't include:

  * `DetectIntent` intent matching
  * `DetectIntent` knowledge



Answer records are not related to the conversation history in the Dialogflow Console. A Record is generated even when the end-user disables conversation history in the console. Records are created when there's a human agent assistant suggestion generated.

A typical workflow for customers provide feedback to an answer is:

  1. For human agent assistant, customers get suggestion via suggestions.list API. Together with the answers, `[AnswerRecord.name](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.FIELDS.name)` are returned to the customers.
  2. The customer uses the `[AnswerRecord.name](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.FIELDS.name)` to call the [answerRecords.patch][] method to send feedback about a specific answer that they believe is wrong.

JSON representation  
---  
      
    
    {
      "name": string,
      "answerFeedback": {
        object ([AnswerFeedback](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.AnswerFeedback))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "agentAssistantRecord": {
        object ([AgentAssistantRecord](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.AgentAssistantRecord))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` The unique identifier of this answer record. Required for `[AnswerRecords.UpdateAnswerRecord](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords/patch#google.cloud.dialogflow.v2beta1.AnswerRecords.UpdateAnswerRecord)` method. Format: `projects/<Project ID>/locations/<Location ID>/answerRecords/<Answer Record ID>`.  
`answerFeedback` |  `object (`[AnswerFeedback](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.AnswerFeedback)`)` Optional. The AnswerFeedback for this record. You can set this with `[AnswerRecords.UpdateAnswerRecord](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords/patch#google.cloud.dialogflow.v2beta1.AnswerRecords.UpdateAnswerRecord)` in order to give us feedback about this answer.  
Output only. The record for this answer. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`agentAssistantRecord` |  `object (`[AgentAssistantRecord](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.AgentAssistantRecord)`)` Output only. The record for human agent assistant.  
End of mutually exclusive fields.  
  
### AnswerFeedback

Represents feedback the customer has about the quality & correctness of a certain answer in a conversation.

JSON representation  
---  
      
    
    {
      "correctnessLevel": enum ([CorrectnessLevel](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.CorrectnessLevel)),
      "clicked": boolean,
      "clickTime": string,
      "displayed": boolean,
      "displayTime": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "agentAssistantDetailFeedback": {
        object ([AgentAssistantFeedback](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.AgentAssistantFeedback))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`correctnessLevel` |  `enum (`[CorrectnessLevel](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.CorrectnessLevel)`)` The correctness level of the specific answer.  
`clicked` |  `boolean` Indicates whether the answer/item was clicked by the human agent or not. Default to false. For knowledge search, the answer record is considered to be clicked if the answer was copied or any URI was clicked.  
`clickTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time when the answer/item was clicked.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`displayed` |  `boolean` Indicates whether the answer/item was displayed to the human agent in the agent desktop UI. Default to false.  
`displayTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time when the answer/item was displayed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Normally, detail feedback is provided when answer is not fully correct. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`agentAssistantDetailFeedback` |  `object (`[AgentAssistantFeedback](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.AgentAssistantFeedback)`)` Optional. Detail feedback of agent assistant suggestions.  
End of mutually exclusive fields.  
  
### CorrectnessLevel

The correctness level of an answer.

Enums  
---  
`CORRECTNESS_LEVEL_UNSPECIFIED` | Correctness level unspecified.  
`NOT_CORRECT` | Answer is totally wrong.  
`PARTIALLY_CORRECT` | Answer is partially correct.  
`FULLY_CORRECT` | Answer is fully correct.  
  
### AgentAssistantFeedback

Detail feedback of Agent Assistant result.

JSON representation  
---  
      
    
    {
      "answerRelevance": enum ([AnswerRelevance](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.AnswerRelevance)),
      "documentCorrectness": enum ([DocumentCorrectness](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.DocumentCorrectness)),
      "documentEfficiency": enum ([DocumentEfficiency](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.DocumentEfficiency)),
      "summarizationFeedback": {
        object ([SummarizationFeedback](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.SummarizationFeedback))
      },
      "knowledgeSearchFeedback": {
        object ([KnowledgeSearchFeedback](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.KnowledgeSearchFeedback))
      },
      "knowledgeAssistFeedback": {
        object ([KnowledgeAssistFeedback](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.KnowledgeAssistFeedback))
      },
      "companionFeedback": {
        object ([CompanionFeedback](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.CompanionFeedback))
      }
    }  
  
Fields  
---  
`answerRelevance` |  `enum (`[AnswerRelevance](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.AnswerRelevance)`)` Optional. Whether or not the suggested answer is relevant.For example:

  * Query: "Can I change my mailing address?"
  * Suggested document says: "Items must be returned/exchanged within 60 days of the purchase date."
  * `[answerRelevance](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.AgentAssistantFeedback.FIELDS.answer_relevance)`: `[AnswerRelevance.IRRELEVANT](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.AnswerRelevance.ENUM_VALUES.IRRELEVANT)`

  
`documentCorrectness` |  `enum (`[DocumentCorrectness](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.DocumentCorrectness)`)` Optional. Whether or not the information in the document is correct.For example:

  * Query: "Can I return the package in 2 days once received?"
  * Suggested document says: "Items must be returned/exchanged within 60 days of the purchase date."
  * Ground truth: "No return or exchange is allowed."
  * `[documentCorrectness](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.AgentAssistantFeedback.FIELDS.document_correctness)`: `[INCORRECT](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.DocumentCorrectness.ENUM_VALUES.INCORRECT)`

  
`documentEfficiency` |  `enum (`[DocumentEfficiency](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.DocumentEfficiency)`)` Optional. Whether or not the suggested document is efficient. For example, if the document is poorly written, hard to understand, hard to use or too long to find useful information, `[documentEfficiency](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.AgentAssistantFeedback.FIELDS.document_efficiency)` is `[DocumentEfficiency.INEFFICIENT](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.DocumentEfficiency.ENUM_VALUES.INEFFICIENT)`.  
`summarizationFeedback` |  `object (`[SummarizationFeedback](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.SummarizationFeedback)`)` Feedback for conversation summarization.  
`knowledgeSearchFeedback` |  `object (`[KnowledgeSearchFeedback](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.KnowledgeSearchFeedback)`)` Optional. Feedback for knowledge search.  
`knowledgeAssistFeedback` |  `object (`[KnowledgeAssistFeedback](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.KnowledgeAssistFeedback)`)` Optional. Feedback for knowledge assist.  
`companionFeedback` |  `object (`[CompanionFeedback](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.CompanionFeedback)`)` Optional. Feedback for companion agent.  
  
### AnswerRelevance

Relevance of an answer.

Enums  
---  
`ANSWER_RELEVANCE_UNSPECIFIED` | Answer relevance unspecified.  
`IRRELEVANT` | Answer is irrelevant to query.  
`RELEVANT` | Answer is relevant to query.  
  
### DocumentCorrectness

Correctness of document.

Enums  
---  
`DOCUMENT_CORRECTNESS_UNSPECIFIED` | Document correctness unspecified.  
`INCORRECT` | Information in document is incorrect.  
`CORRECT` | Information in document is correct.  
  
### DocumentEfficiency

Efficiency of document.

Enums  
---  
`DOCUMENT_EFFICIENCY_UNSPECIFIED` | Document efficiency unspecified.  
`INEFFICIENT` | Document is inefficient.  
`EFFICIENT` | Document is efficient.  
  
### SummarizationFeedback

Feedback for conversation summarization.

JSON representation  
---  
      
    
    {
      "startTimestamp": string,
      "submitTimestamp": string,
      "summaryText": string,
      "textSections": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`startTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when composing of the summary starts.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`submitTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp when the summary was submitted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`summaryText` |  `string` Text of actual submitted summary.  
`textSections` |  `map (key: string, value: string)` Optional. Actual text sections of submitted summary.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### KnowledgeSearchFeedback

Feedback for knowledge search.

JSON representation  
---  
      
    
    {
      "answerCopied": boolean,
      "clickedUris": [
        string
      ]
    }  
  
Fields  
---  
`answerCopied` |  `boolean` Whether the answer was copied by the human agent or not. If the value is set to be true, `[AnswerFeedback.clicked](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.AnswerFeedback.FIELDS.clicked)` will be updated to be true.  
`clickedUris[]` |  `string` The URIs clicked by the human agent. The value is appended for each UpdateAnswerRecordRequest. If the value is not empty, `[AnswerFeedback.clicked](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.AnswerFeedback.FIELDS.clicked)` will be updated to be true.  
  
### KnowledgeAssistFeedback

Feedback for knowledge assist.

JSON representation  
---  
      
    
    {
      "answerCopied": boolean,
      "clickedUris": [
        string
      ]
    }  
  
Fields  
---  
`answerCopied` |  `boolean` Whether the suggested answer was copied by the human agent. If the value is set to be true, `[AnswerFeedback.clicked](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.AnswerFeedback.FIELDS.clicked)` will be updated to be true.  
`clickedUris[]` |  `string` The URIs clicked by the human agent. The value is appended for each `UpdateAnswerRecordRequest`. If the value is not empty, `[AnswerFeedback.clicked](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.AnswerFeedback.FIELDS.clicked)` will be updated to be true.  
  
### CompanionFeedback

This type has no fields.

Feedback for companion agent.

### AgentAssistantRecord

Represents a record of a human agent assistant answer.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "articleSuggestionAnswer": {
        object ([ArticleAnswer](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.ArticleAnswer))
      },
      "faqAnswer": {
        object ([FaqAnswer](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.FaqAnswer))
      },
      "dialogflowAssistAnswer": {
        object ([DialogflowAssistAnswer](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.DialogflowAssistAnswer))
      },
      "generatorSuggestion": {
        object ([GeneratorSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/GeneratorSuggestion))
      },
      "companionSuggestion": {
        object ([CompanionSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.CompanionSuggestion))
      },
      "reactiveCompanionSuggestion": {
        object ([ReactiveModeResponse](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.ReactiveModeResponse))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Output only. The agent assistant answer. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`articleSuggestionAnswer` |  `object (`[ArticleAnswer](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.ArticleAnswer)`)` Output only. The article suggestion answer.  
`faqAnswer` |  `object (`[FaqAnswer](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.FaqAnswer)`)` Output only. The FAQ answer.  
`dialogflowAssistAnswer` |  `object (`[DialogflowAssistAnswer](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.DialogflowAssistAnswer)`)` Output only. The Dialogflow assist answer.  
`generatorSuggestion` |  `object (`[GeneratorSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/GeneratorSuggestion)`)` Output only. The generator suggestion.  
`companionSuggestion` |  `object (`[CompanionSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.CompanionSuggestion)`)` Output only. The companion suggestion.  
`reactiveCompanionSuggestion` |  `object (`[ReactiveModeResponse](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.ReactiveModeResponse)`)` Output only. The reactive companion suggestion.  
End of mutually exclusive fields.  
  
### ArticleAnswer

Represents article answer.

JSON representation  
---  
      
    
    {
      "title": string,
      "uri": string,
      "snippets": [
        string
      ],
      "metadata": {
        string: string,
        ...
      },
      "answerRecord": string
    }  
  
Fields  
---  
`title` |  `string` The article title.  
`uri` |  `string` The article URI.  
`snippets[]` |  `string` Output only. Article snippets.  
`metadata` |  `map (key: string, value: string)` A map that contains metadata about the answer and the document from which it originates.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`answerRecord` |  `string` The name of answer record, in the format of "projects//locations//answerRecords/"  
  
### FaqAnswer

Represents answer from "frequently asked questions".

JSON representation  
---  
      
    
    {
      "answer": string,
      "confidence": number,
      "question": string,
      "source": string,
      "metadata": {
        string: string,
        ...
      },
      "answerRecord": string
    }  
  
Fields  
---  
`answer` |  `string` The piece of text from the `source` knowledge base document.  
`confidence` |  `number` The system's confidence score that this Knowledge answer is a good match for this conversational query, range from 0.0 (completely uncertain) to 1.0 (completely certain).  
`question` |  `string` The corresponding FAQ question.  
`source` |  `string` Indicates which Knowledge Document this answer was extracted from. Format: `projects/<Project ID>/locations/<Location ID>/agent/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>`.  
`metadata` |  `map (key: string, value: string)` A map that contains metadata about the answer and the document from which it originates.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`answerRecord` |  `string` The name of answer record, in the format of "projects//locations//answerRecords/"  
  
### DialogflowAssistAnswer

Represents a Dialogflow assist answer.

JSON representation  
---  
      
    
    {
      "answerRecord": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "queryResult": {
        object ([QueryResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.QueryResult))
      },
      "intentSuggestion": {
        object ([IntentSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.IntentSuggestion))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`answerRecord` |  `string` The name of answer record, in the format of "projects//locations//answerRecords/"  
Result from DetectIntent for one matched intent. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`queryResult` |  `object (`[QueryResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.QueryResult)`)` Result from v2 agent.  
`intentSuggestion` |  `object (`[IntentSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.IntentSuggestion)`)` An intent suggestion generated from conversation.  
End of mutually exclusive fields.  
  
### QueryResult

Represents the result of conversational query or event processing.

JSON representation  
---  
      
    
    {
      "queryText": string,
      "languageCode": string,
      "speechRecognitionConfidence": number,
      "action": string,
      "parameters": {
        object
      },
      "allRequiredParamsPresent": boolean,
      "cancelsSlotFilling": boolean,
      "fulfillmentText": string,
      "fulfillmentMessages": [
        {
          object ([Message](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/Message))
        }
      ],
      "webhookSource": string,
      "webhookPayload": {
        object
      },
      "outputContexts": [
        {
          object ([Context](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.environments.users.sessions.contexts#Context))
        }
      ],
      "intent": {
        object ([Intent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.intents#Intent))
      },
      "intentDetectionConfidence": number,
      "diagnosticInfo": {
        object
      },
      "sentimentAnalysisResult": {
        object ([SentimentAnalysisResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.SentimentAnalysisResult))
      },
      "knowledgeAnswers": {
        object ([KnowledgeAnswers](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.KnowledgeAnswers))
      }
    }  
  
Fields  
---  
`queryText` |  `string` The original conversational query text:

  * If natural language text was provided as input, `queryText` contains a copy of the input.
  * If natural language speech audio was provided as input, `queryText` contains the speech recognition result. If speech recognizer produced multiple alternatives, a particular one is picked.
  * If automatic spell correction is enabled, `queryText` will contain the corrected user input.

  
`languageCode` |  `string` The language that was triggered during intent detection. See [Language Support](https://cloud.google.com/dialogflow/docs/reference/language) for a list of the currently supported language codes.  
`speechRecognitionConfidence` |  `number` The Speech recognition confidence between 0.0 and 1.0. A higher number indicates an estimated greater likelihood that the recognized words are correct. The default of 0.0 is a sentinel value indicating that confidence was not set.This field is not guaranteed to be accurate or set. In particular this field isn't set for StreamingDetectIntent since the streaming endpoint has separate confidence estimates per portion of the audio in StreamingRecognitionResult.  
`action` |  `string` The action name from the matched intent.  
`parameters` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The collection of extracted parameters.Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs:

  * MapKey type: string
  * MapKey value: parameter name
  * MapValue type: If parameter's entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map.
  * MapValue value: If parameter's entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value.

  
`allRequiredParamsPresent` |  `boolean` This field is set to:

  * `false` if the matched intent has required parameters and not all of the required parameter values have been collected.
  * `true` if all required parameter values have been collected, or if the matched intent doesn't contain any required parameters.

  
`cancelsSlotFilling` |  `boolean` Indicates whether the conversational query triggers a cancellation for slot filling. For more information, see the [cancel slot filling documentation](https://cloud.google.com/dialogflow/es/docs/intents-actions-parameters#cancel).  
`fulfillmentText` |  `string` The text to be pronounced to the user or shown on the screen. Note: This is a legacy field, `fulfillmentMessages` should be preferred.  
`fulfillmentMessages[]` |  `object (`[Message](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/Message)`)` The collection of rich messages to present to the user.  
`webhookSource` |  `string` If the query was fulfilled by a webhook call, this field is set to the value of the `source` field returned in the webhook response.  
`webhookPayload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` If the query was fulfilled by a webhook call, this field is set to the value of the `payload` field returned in the webhook response.  
`outputContexts[]` |  `object (`[Context](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.environments.users.sessions.contexts#Context)`)` The collection of output contexts. If applicable, `outputContexts.parameters` contains entries with name `<parameter name>.original` containing the original parameter values before the query.  
`intent` |  `object (`[Intent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.intents#Intent)`)` The intent that matched the conversational query. Some, not all fields are filled in this message, including but not limited to: `name`, `displayName`, `endInteraction` and `isFallback`.  
`intentDetectionConfidence` |  `number` The intent detection confidence. Values range from 0.0 (completely uncertain) to 1.0 (completely certain). This value is for informational purpose only and is only used to help match the best intent within the classification threshold. This value may change for the same end-user expression at any time due to a model retraining or change in implementation. If there are `multiple knowledgeAnswers` messages, this value is set to the greatest `knowledgeAnswers.match_confidence` value in the list.  
`diagnosticInfo` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Free-form diagnostic information for the associated detect intent request. The fields of this data can change without notice, so you should not write code that depends on its structure. The data may contain:

  * webhook call latency
  * webhook errors

  
`sentimentAnalysisResult` |  `object (`[SentimentAnalysisResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.SentimentAnalysisResult)`)` The sentiment analysis result, which depends on the `sentimentAnalysisRequestConfig` specified in the request.  
`knowledgeAnswers` |  `object (`[KnowledgeAnswers](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.KnowledgeAnswers)`)` The result from Knowledge Connector (if any), ordered by decreasing `KnowledgeAnswers.match_confidence`.  
  
### SentimentAnalysisResult

The result of sentiment analysis. Sentiment analysis inspects user input and identifies the prevailing subjective opinion, especially to determine a user's attitude as positive, negative, or neutral. For [Participants.DetectIntent][], it needs to be configured in `[DetectIntentRequest.query_params](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.sessions/detectIntent#body.request_body.FIELDS.query_params)`. For [Participants.StreamingDetectIntent][], it needs to be configured in `StreamingDetectIntentRequest.query_params`. And for `[Participants.AnalyzeContent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversations.participants/analyzeContent#google.cloud.dialogflow.v2beta1.Participants.AnalyzeContent)` and `Participants.StreamingAnalyzeContent`, it needs to be configured in `[ConversationProfile.human_agent_assistant_config](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.conversationProfiles#ConversationProfile.FIELDS.human_agent_assistant_config)`

JSON representation  
---  
      
    
    {
      "queryTextSentiment": {
        object ([Sentiment](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.Sentiment))
      }
    }  
  
Fields  
---  
`queryTextSentiment` |  `object (`[Sentiment](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.Sentiment)`)` The sentiment analysis result for `queryText`.  
  
### Sentiment

The sentiment, such as positive/negative feeling or association, for a unit of analysis, such as the query text. See: <https://cloud.google.com/natural-language/docs/basics#interpreting_sentiment_analysis_values> for how to interpret the result.

JSON representation  
---  
      
    
    {
      "score": number,
      "magnitude": number
    }  
  
Fields  
---  
`score` |  `number` Sentiment score between -1.0 (negative sentiment) and 1.0 (positive sentiment).  
`magnitude` |  `number` A non-negative number in the [0, +inf) range, which represents the absolute magnitude of sentiment, regardless of score (positive or negative).  
  
### KnowledgeAnswers

Represents the result of querying a Knowledge base.

JSON representation  
---  
      
    
    {
      "answers": [
        {
          object ([Answer](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.Answer))
        }
      ]
    }  
  
Fields  
---  
`answers[]` |  `object (`[Answer](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.Answer)`)` A list of answers from Knowledge Connector.  
  
### Answer

An answer from Knowledge Connector.

JSON representation  
---  
      
    
    {
      "source": string,
      "faqQuestion": string,
      "answer": string,
      "matchConfidenceLevel": enum ([MatchConfidenceLevel](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.MatchConfidenceLevel)),
      "matchConfidence": number
    }  
  
Fields  
---  
`source` |  `string` Indicates which Knowledge Document this answer was extracted from. Format: `projects/<Project ID>/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>`.  
`faqQuestion` |  `string` The corresponding FAQ question if the answer was extracted from a FAQ Document, empty otherwise.  
`answer` |  `string` The piece of text from the `source` knowledge base document that answers this conversational query.  
`matchConfidenceLevel` |  `enum (`[MatchConfidenceLevel](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.MatchConfidenceLevel)`)` The system's confidence level that this knowledge answer is a good match for this conversational query. NOTE: The confidence level for a given `<query, answer>` pair may change without notice, as it depends on models that are constantly being improved. However, it will change less frequently than the confidence score below, and should be preferred for referencing the quality of an answer.  
`matchConfidence` |  `number` The system's confidence score that this Knowledge answer is a good match for this conversational query. The range is from 0.0 (completely uncertain) to 1.0 (completely certain). Note: The confidence score is likely to vary somewhat (possibly even for identical requests), as the underlying model is under constant improvement. It may be deprecated in the future. We recommend using `matchConfidenceLevel` which should be generally more stable.  
  
### MatchConfidenceLevel

Represents the system's confidence that this knowledge answer is a good match for this conversational query.

Enums  
---  
`MATCH_CONFIDENCE_LEVEL_UNSPECIFIED` | Not specified.  
`LOW` | Indicates that the confidence is low.  
`MEDIUM` | Indicates our confidence is medium.  
`HIGH` | Indicates our confidence is high.  
  
### IntentSuggestion

Represents an intent suggestion.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "description": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "intentV2": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`displayName` |  `string` The display name of the intent.  
`description` |  `string` Human readable description for better understanding an intent like its scope, content, result etc. Maximum character limit: 140 characters.  
The name of the intent. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`intentV2` |  `string` The unique identifier of this `[intent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.intents#Intent)`. Format: `projects/<Project ID>/locations/<Location ID>/agent/intents/<Intent ID>`.  
End of mutually exclusive fields.  
  
### CompanionSuggestion

Represents a companion suggestion answer.

JSON representation  
---  
      
    
    {
      "guidances": [
        {
          object ([Guidance](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.Guidance))
        }
      ]
    }  
  
Fields  
---  
`guidances[]` |  `object (`[Guidance](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.Guidance)`)` List of guidances generated by the Companion Agent.  
  
### Guidance

Represents guidance for companion suggestion.

JSON representation  
---  
      
    
    {
      "suggestedReply": string,
      "suggestedAction": string,
      "instructionSource": {
        object ([GuidanceInstruction](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/GuidanceInstruction))
      },
      "knowledgeSources": [
        {
          object ([KnowledgeSource](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.KnowledgeSource))
        }
      ],
      "explanation": string,
      "toolCalls": [
        {
          object ([ToolCallSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.ToolCallSuggestion))
        }
      ],
      "triggeringToolCallAnswerRecords": [
        string
      ],
      "groundingMetadata": {
        object ([GroundingMetadata](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.GroundingMetadata))
      }
    }  
  
Fields  
---  
`suggestedReply` |  `string` Suggested reply for the agent to respond to the customer.  
`suggestedAction` |  `string` Suggested action to human agent. For example, "Ask the customer for their shipping address" or "Create a new case for the customer".  
`instructionSource` |  `object (`[GuidanceInstruction](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/GuidanceInstruction)`)` Guidance instruction source.  
`knowledgeSources[]` |  `object (`[KnowledgeSource](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.KnowledgeSource)`)` Knowledge sources.  
`explanation` |  `string` Optional. A brief explanation of why the action is suggested.  
`toolCalls[]` |  `object (`[ToolCallSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.ToolCallSuggestion)`)` Optional. Rich structured tool calls and their associated citations delivered directly as suggestions.  
`triggeringToolCallAnswerRecords[]` |  `string` Optional. The AnswerRecords of the tool calls that triggered this guidance. Format: `projects/<Project ID>/locations/<Location ID>/answerRecords/<Answer Record ID>`.  
`groundingMetadata` |  `object (`[GroundingMetadata](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.GroundingMetadata)`)` Optional. Grounding metadata for the generated guidance.  
  
### KnowledgeSource

Represents a knowledge source for the guidance.

JSON representation  
---  
      
    
    {
      "knowledgeArticleUrl": string,
      "knowledgeArticleTitle": string,
      "knowledgeSnippet": string
    }  
  
Fields  
---  
`knowledgeArticleUrl` |  `string` URL of the knowledge article.  
`knowledgeArticleTitle` |  `string` Knowledge article title.  
`knowledgeSnippet` |  `string` Knowledge snippet.  
  
### GroundingMetadata

Grounding metadata contains sources, citations, and search entry points used to ground a generated answer or suggestion.

JSON representation  
---  
      
    
    {
      "webSearchQueries": [
        string
      ],
      "searchEntryPoint": {
        object ([SearchEntryPoint](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.SearchEntryPoint))
      },
      "groundingChunks": [
        {
          object ([GroundingChunk](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.GroundingChunk))
        }
      ],
      "groundingSupports": [
        {
          object ([GroundingSupport](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.GroundingSupport))
        }
      ]
    }  
  
Fields  
---  
`webSearchQueries[]` |  `string` Optional. The web search queries that were used to generate the content.  
`searchEntryPoint` |  `object (`[SearchEntryPoint](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.SearchEntryPoint)`)` Optional. A web search entry point that can be used to display search results.  
`groundingChunks[]` |  `object (`[GroundingChunk](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.GroundingChunk)`)` Optional. A list of supporting references retrieved from the grounding source.  
`groundingSupports[]` |  `object (`[GroundingSupport](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.GroundingSupport)`)` Optional. A list of grounding supports that connect the generated content to the grounding chunks.  
  
### SearchEntryPoint

Google search entry point.

JSON representation  
---  
      
    
    {
      "renderedContent": string
    }  
  
Fields  
---  
`renderedContent` |  `string` Optional. An HTML snippet that can be embedded in a web page or an application's webview. This snippet displays a search result, including the title, URL, and a brief description of the search result.  
  
### GroundingChunk

A piece of evidence that supports a claim made by the model.

This is used to show a citation for a claim made by the model. It contains a reference to the source of the information.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "web": {
        object ([Web](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.Web))
      },
      "retrievedContext": {
        object ([RetrievedContext](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.RetrievedContext))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The source of the grounding chunk. Currently we only support web search. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`web` |  `object (`[Web](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.Web)`)` Optional. A grounding chunk from a web page, typically from web search. See the `Web` message for details.  
`retrievedContext` |  `object (`[RetrievedContext](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.RetrievedContext)`)` Optional. A grounding chunk from a data source retrieved by a data store tool.  
End of mutually exclusive fields.  
  
### Web

A `Web` chunk is a piece of evidence that comes from a web page. It contains the URI of the web page, the title of the page, and the domain of the page. This is used to provide the user with a link to the source of the information.

JSON representation  
---  
      
    
    {
      "uri": string,
      "title": string,
      "domain": string
    }  
  
Fields  
---  
`uri` |  `string` Output only. The URI of the web page that contains the evidence.  
`title` |  `string` Output only. The title of the web page that contains the evidence.  
`domain` |  `string` Output only. The domain of the web page that contains the evidence. This can be used to filter out low-quality sources.  
  
### RetrievedContext

Context retrieved from a data source to ground the model's response. This is used when a retrieval tool fetches information from a user-provided corpus or a public dataset.

JSON representation  
---  
      
    
    {
      "uri": string,
      "title": string,
      "text": string
    }  
  
Fields  
---  
`uri` |  `string` Output only. The URI of the retrieved data source.  
`title` |  `string` Output only. The title of the retrieved data source.  
`text` |  `string` Output only. The content of the retrieved data source.  
  
### GroundingSupport

A collection of supporting references for a segment or part of the model's response.

JSON representation  
---  
      
    
    {
      "segment": {
        object ([Segment](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.Segment))
      },
      "groundingChunkIndices": [
        integer
      ]
    }  
  
Fields  
---  
`segment` |  `object (`[Segment](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.Segment)`)` Optional. Segment of the content this support belongs to.  
`groundingChunkIndices[]` |  `integer` Optional. A list of indices into `groundingChunks` field specifying the citations associated with the claim. For instance [1, 3] means that groundingChunks[1] and groundingChunks[3] are the retrieved contents attributed to the claim.  
  
### Segment

A segment of the content.

JSON representation  
---  
      
    
    {
      "startIndex": integer,
      "endIndex": integer,
      "text": string
    }  
  
Fields  
---  
`startIndex` |  `integer` Output only. The start index of the segment, measured in bytes. This marks the beginning of the segment and is inclusive, meaning the byte at this index is the first byte of the segment.  
`endIndex` |  `integer` Output only. The end index of the segment, measured in bytes. This marks the end of the segment and is exclusive, meaning the segment includes content up to, but not including, the byte at this index.  
`text` |  `string` Output only. The text of the segment.  
  
### ToolCallSuggestion

Structured wrapper that pairs tool execution details with strongly-typed citations.

JSON representation  
---  
      
    
    {
      "toolCallInfo": {
        object ([ToolCallInfo](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/ToolCallInfo))
      },
      "textUpdate": string
    }  
  
Fields  
---  
`toolCallInfo` |  `object (`[ToolCallInfo](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/ToolCallInfo)`)` Optional. Tool execution request/response details.  
`textUpdate` |  `string` Optional. The conversational text update generated by the agent accompanying this tool call (e.g. "The status of your order 12345 is currently being retrieved..."). This is a status update emitted alongside in-flight tool execution and is not accumulated into the final response.  
  
### ReactiveModeResponse

The complete response generated by the reactive mode capturing the entire accumulated streaming response, grounding metadata, and tool calls.

JSON representation  
---  
      
    
    {
      "response": string,
      "groundingMetadata": {
        object ([GroundingMetadata](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.GroundingMetadata))
      },
      "toolCalls": [
        {
          object ([ToolCallSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.ToolCallSuggestion))
        }
      ]
    }  
  
Fields  
---  
`response` |  `string` Optional. The full reactive suggestion generated by the Companion Agent. After the last streaming chunk is sent, this is the final response concatenating all the streaming response chunks together to represent the full reactive suggestion.  
`groundingMetadata` |  `object (`[GroundingMetadata](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.GroundingMetadata)`)` Optional. Grounding metadata for the generated response.  
`toolCalls[]` |  `object (`[ToolCallSuggestion](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords#AnswerRecord.ToolCallSuggestion)`)` Optional. Captures all the rich structured tool calls and their associated citations used by the reactive agent to generate the reactive suggestion.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords/get)   
**(deprecated)**`

|  Deprecated.  
  
### `[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords/list)`

|  Returns the list of all answer records in the specified project in reverse chronological order.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.answerRecords/patch)`

|  Updates the specified answer record.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
