---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.agent.intents
title: REST Resource: projects.locations.agent.intents \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:53:43.651573+00:00
---

# REST Resource: projects.locations.agent.intents  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.agent.intents

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  REST Resource: projects.locations.agent.intents Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Intent
    * JSON representation
  * Methods



## Resource: Intent

An intent categorizes an end-user's intention for one conversation turn. For each agent, you define many intents, where your combined intents can handle a complete conversation. When an end-user writes or says something, referred to as an end-user expression or end-user input, Dialogflow matches the end-user input to the best intent in your agent. Matching an intent is also known as intent classification.

For more information, see the [intent guide](https://cloud.google.com/dialogflow/docs/intents-overview).

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "webhookState": enum ([WebhookState](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.intents#Intent.WebhookState)),
      "priority": integer,
      "isFallback": boolean,
      "mlEnabled": boolean,
      "mlDisabled": boolean,
      "liveAgentHandoff": boolean,
      "endInteraction": boolean,
      "inputContextNames": [
        string
      ],
      "events": [
        string
      ],
      "trainingPhrases": [
        {
          object ([TrainingPhrase](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.intents#Intent.TrainingPhrase))
        }
      ],
      "action": string,
      "outputContexts": [
        {
          object ([Context](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.environments.users.sessions.contexts#Context))
        }
      ],
      "resetContexts": boolean,
      "parameters": [
        {
          object ([Parameter](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.intents#Intent.Parameter))
        }
      ],
      "messages": [
        {
          object ([Message](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/Message))
        }
      ],
      "defaultResponsePlatforms": [
        enum ([Platform](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/Platform))
      ],
      "rootFollowupIntentName": string,
      "parentFollowupIntentName": string,
      "followupIntentInfo": [
        {
          object ([FollowupIntentInfo](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.intents#Intent.FollowupIntentInfo))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Optional. The unique identifier of this intent. Required for `[Intents.UpdateIntent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.intents/patch#google.cloud.dialogflow.v2beta1.Intents.UpdateIntent)` and `[Intents.BatchUpdateIntents](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.intents/batchUpdate#google.cloud.dialogflow.v2beta1.Intents.BatchUpdateIntents)` methods. Supported formats:

  * `projects/<Project ID>/agent/intents/<Intent ID>`
  * `projects/<Project ID>/locations/<Location ID>/agent/intents/<Intent ID>`

  
`displayName` |  `string` Required. The name of this intent.  
`webhookState` |  `enum (`[WebhookState](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.intents#Intent.WebhookState)`)` Optional. Indicates whether webhooks are enabled for the intent.  
`priority` |  `integer` Optional. The priority of this intent. Higher numbers represent higher priorities.

  * If the supplied value is unspecified or 0, the service translates the value to 500,000, which corresponds to the `Normal` priority in the console.
  * If the supplied value is negative, the intent is ignored in runtime detect intent requests.

  
`isFallback` |  `boolean` Optional. Indicates whether this is a fallback intent.  
`mlEnabled  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Indicates whether Machine Learning is enabled for the intent. Note: If `mlEnabled` setting is set to false, then this intent is not taken into account during inference in `ML ONLY` match mode. Also, auto-markup in the UI is turned off. DEPRECATED! Please use `mlDisabled` field instead. NOTE: If both `mlEnabled` and `mlDisabled` are either not set or false, then the default value is determined as follows:

  * Before April 15th, 2018 the default is: mlEnabled = false / mlDisabled = true.
  * After April 15th, 2018 the default is: mlEnabled = true / mlDisabled = false.

  
`mlDisabled` |  `boolean` Optional. Indicates whether Machine Learning is disabled for the intent. Note: If `mlDisabled` setting is set to true, then this intent is not taken into account during inference in `ML ONLY` match mode. Also, auto-markup in the UI is turned off.  
`liveAgentHandoff` |  `boolean` Optional. Indicates that a live agent should be brought in to handle the interaction with the user. In most cases, when you set this flag to true, you would also want to set endInteraction to true as well. Default is false.  
`endInteraction` |  `boolean` Optional. Indicates that this intent ends an interaction. Some integrations (e.g., Actions on Google or Dialogflow phone gateway) use this information to close interaction with an end user. Default is false.  
`inputContextNames[]` |  `string` Optional. The list of context names required for this intent to be triggered. Formats:

  * `projects/<Project ID>/agent/sessions/-/contexts/<Context ID>`
  * `projects/<Project ID>/locations/<Location ID>/agent/sessions/-/contexts/<Context ID>`

  
`events[]` |  `string` Optional. The collection of event names that trigger the intent. If the collection of input contexts is not empty, all of the contexts must be present in the active user session for an event to trigger this intent. Event names are limited to 150 characters.  
`trainingPhrases[]` |  `object (`[TrainingPhrase](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.intents#Intent.TrainingPhrase)`)` Optional. The collection of examples that the agent is trained on.  
`action` |  `string` Optional. The name of the action associated with the intent. Note: The action name must not contain whitespaces.  
`outputContexts[]` |  `object (`[Context](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.environments.users.sessions.contexts#Context)`)` Optional. The collection of contexts that are activated when the intent is matched. Context messages in this collection should not set the parameters field. Setting the `lifespanCount` to 0 will reset the context when the intent is matched. Format: `projects/<Project ID>/agent/sessions/-/contexts/<Context ID>`.  
`resetContexts` |  `boolean` Optional. Indicates whether to delete all contexts in the current session when this intent is matched.  
`parameters[]` |  `object (`[Parameter](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.intents#Intent.Parameter)`)` Optional. The collection of parameters associated with the intent.  
`messages[]` |  `object (`[Message](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/Message)`)` Optional. The collection of rich messages corresponding to the `Response` field in the Dialogflow console.  
`defaultResponsePlatforms[]` |  `enum (`[Platform](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/Platform)`)` Optional. The list of platforms for which the first responses will be copied from the messages in PLATFORM_UNSPECIFIED (i.e. default platform).  
`rootFollowupIntentName` |  `string` Output only. The unique identifier of the root intent in the chain of followup intents. It identifies the correct followup intents chain for this intent.Format: `projects/<Project ID>/agent/intents/<Intent ID>`.  
`parentFollowupIntentName` |  `string` Optional. The unique identifier of the parent intent in the chain of followup intents. You can set this field when creating an intent, for example with `[intents.create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.intents/create#google.cloud.dialogflow.v2beta1.Intents.CreateIntent)` or `[intents.batchUpdate](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.intents/batchUpdate#google.cloud.dialogflow.v2beta1.Intents.BatchUpdateIntents)`, in order to make this intent a followup intent.It identifies the parent followup intent. Format: `projects/<Project ID>/agent/intents/<Intent ID>`.  
`followupIntentInfo[]` |  `object (`[FollowupIntentInfo](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.agent.intents#Intent.FollowupIntentInfo)`)` Output only. Information about all followup intents that have this intent as a direct or indirect parent. We populate this field only in the output.  
  
## Methods  
  
---  
  
### `[batchDelete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.agent.intents/batchDelete)`

|  Deletes intents in the specified agent.  
  
### `[batchUpdate](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.agent.intents/batchUpdate)`

|  Updates/Creates multiple intents in the specified agent.  
  
### `[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.agent.intents/create)`

|  Creates an intent in the specified agent.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.agent.intents/delete)`

|  Deletes the specified intent and its direct or indirect followup intents.  
  
### `[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.agent.intents/get)`

|  Retrieves the specified intent.  
  
### `[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.agent.intents/list)`

|  Returns the list of all intents in the specified agent.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.agent.intents/patch)`

|  Updates the specified intent.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
