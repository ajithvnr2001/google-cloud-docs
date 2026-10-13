---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Match/
title: Match \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:35.884939+00:00
---

# Match  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Match/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  Match Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * MatchType



Represents one match result of [MatchIntent][].

JSON representation  
---  
      
    
    {
      "intent": {
        object ([Intent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents#Intent))
      },
      "event": string,
      "parameters": {
        object
      },
      "resolvedInput": string,
      "matchType": enum ([MatchType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Match#MatchType)),
      "confidence": number
    }  
  
Fields  
---  
`intent` |  `object (`[Intent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents#Intent)`)` The `[Intent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents#Intent)` that matched the query. Some, not all fields are filled in this message, including but not limited to: `name` and `displayName`. Only filled for `[`INTENT`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Match#MatchType)` match type.  
`event` |  `string` The event that matched the query. Filled for `[`EVENT`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Match#MatchType)`, `[`NO_MATCH`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Match#MatchType)` and `[`NO_INPUT`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Match#MatchType)` match types.  
`parameters` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The collection of parameters extracted from the query.Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs:

  * MapKey type: string
  * MapKey value: parameter name
  * MapValue type: If parameter's entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map.
  * MapValue value: If parameter's entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value.

  
`resolvedInput` |  `string` Final text input which was matched during MatchIntent. This value can be different from original input sent in request because of spelling correction or other processing.  
`matchType` |  `enum (`[MatchType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Match#MatchType)`)` Type of this `[Match](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Match)`.  
`confidence` |  `number` The confidence of this match. Values range from 0.0 (completely uncertain) to 1.0 (completely certain). This value is for informational purpose only and is only used to help match the best intent within the classification threshold. This value may change for the same end-user expression at any time due to a model retraining or change in implementation.  
  
## MatchType

Type of a Match.

Enums  
---  
`MATCH_TYPE_UNSPECIFIED` | Not specified. Should never be used.  
`INTENT` | The query was matched to an intent.  
`DIRECT_INTENT` | The query directly triggered an intent.  
`PARAMETER_FILLING` | The query was used for parameter filling.  
`NO_MATCH` | No match was found for the query.  
`NO_INPUT` | Indicates an empty query.  
`EVENT` | The query directly triggered an event.  
`KNOWLEDGE_CONNECTOR` | The query was matched to a Knowledge Connector answer.  
`PLAYBOOK` | The query was handled by a `[`Playbook`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks#Playbook)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
