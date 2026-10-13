---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents
title: REST Resource: projects.locations.agents.intents \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:13.268484+00:00
---

# REST Resource: projects.locations.agents.intents  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  REST Resource: projects.locations.agents.intents Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Intent
    * JSON representation
    * TrainingPhrase
      * JSON representation
    * Part
      * JSON representation
    * Parameter
      * JSON representation
  * Methods



## Resource: Intent

An intent represents a user's intent to interact with a conversational agent.

You can provide information for the Dialogflow API to use to match user input to an intent by adding training phrases (i.e., examples of user input) to your intent.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "trainingPhrases": [
        {
          object ([TrainingPhrase](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents#Intent.TrainingPhrase))
        }
      ],
      "parameters": [
        {
          object ([Parameter](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents#Intent.Parameter))
        }
      ],
      "priority": integer,
      "isFallback": boolean,
      "labels": {
        string: string,
        ...
      },
      "description": string,
      "dtmfPattern": string
    }  
  
Fields  
---  
`name` |  `string` The unique identifier of the intent. Required for the `[Intents.UpdateIntent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/patch#google.cloud.dialogflow.cx.v3.Intents.UpdateIntent)` method. `[Intents.CreateIntent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/create#google.cloud.dialogflow.cx.v3.Intents.CreateIntent)` populates the name automatically. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/intents/<IntentID>`.  
`displayName` |  `string` Required. The human-readable name of the intent, unique within the agent.  
`trainingPhrases[]` |  `object (`[TrainingPhrase](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents#Intent.TrainingPhrase)`)` The collection of training phrases the agent is trained on to identify the intent.  
`parameters[]` |  `object (`[Parameter](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents#Intent.Parameter)`)` The collection of parameters associated with the intent.  
`priority` |  `integer` The priority of this intent. Higher numbers represent higher priorities.

  * If the supplied value is unspecified or 0, the service translates the value to 500,000, which corresponds to the `Normal` priority in the console.
  * If the supplied value is negative, the intent is ignored in runtime detect intent requests.

  
`isFallback` |  `boolean` Indicates whether this is a fallback intent. Currently only default fallback intent is allowed in the agent, which is added upon agent creation. Adding training phrases to fallback intent is useful in the case of requests that are mistakenly matched, since training phrases assigned to fallback intents act as negative examples that triggers no-match event.  
`labels` |  `map (key: string, value: string)` The key/value metadata to label an intent. Labels can contain lowercase letters, digits and the symbols '-' and '_'. International characters are allowed, including letters from unicase alphabets. Keys must start with a letter. Keys and values can be no longer than 63 characters and no more than 128 bytes.Prefix "sys-" is reserved for Dialogflow defined labels. Currently allowed Dialogflow defined labels include: * sys-head * sys-contextual The above labels do not require value. "sys-head" means the intent is a head intent. "sys.contextual" means the intent is a contextual intent.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` Human readable description for better understanding an intent like its scope, content, result etc. Maximum character limit: 1000 characters.  
`dtmfPattern` |  `string` Optional. Matching DTMF pattern for the intent.  
  
### TrainingPhrase

Represents an example that the agent is trained on to identify the intent.

JSON representation  
---  
      
    
    {
      "id": string,
      "parts": [
        {
          object ([Part](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents#Intent.Part))
        }
      ],
      "repeatCount": integer
    }  
  
Fields  
---  
`id` |  `string` Output only. The unique identifier of the training phrase.  
`parts[]` |  `object (`[Part](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents#Intent.Part)`)` Required. The ordered list of training phrase parts. The parts are concatenated in order to form the training phrase.Note: The API does not automatically annotate training phrases like the Dialogflow Console does.Note: Do not forget to include whitespace at part boundaries, so the training phrase is well formatted when the parts are concatenated.If the training phrase does not need to be annotated with parameters, you just need a single part with only the `[Part.text](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents#Intent.Part.FIELDS.text)` field set.If you want to annotate the training phrase, you must create multiple parts, where the fields of each part are populated in one of two ways:

  * `Part.text` is set to a part of the phrase that has no parameters.
  * `Part.text` is set to a part of the phrase that you want to annotate, and the `parameterId` field is set.

  
`repeatCount` |  `integer` Indicates how many times this example was added to the intent.  
  
### Part

Represents a part of a training phrase.

JSON representation  
---  
      
    
    {
      "text": string,
      "parameterId": string
    }  
  
Fields  
---  
`text` |  `string` Required. The text for this part.  
`parameterId` |  `string` The `[parameter](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents#Intent.Parameter)` used to annotate this part of the training phrase. This field is required for annotated parts of the training phrase.  
  
### Parameter

Represents an intent parameter.

JSON representation  
---  
      
    
    {
      "id": string,
      "entityType": string,
      "isList": boolean,
      "redact": boolean
    }  
  
Fields  
---  
`id` |  `string` Required. The unique identifier of the parameter. This field is used by `[training phrases](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents#Intent.TrainingPhrase)` to annotate their `[parts](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents#Intent.Part)`.  
`entityType` |  `string` Required. The entity type of the parameter. Format: `projects/-/locations/-/agents/-/entityTypes/<SystemEntityTypeID>` for system entity types (for example, `projects/-/locations/-/agents/-/entityTypes/sys.date`), or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/entityTypes/<EntityTypeID>` for developer entity types.  
`isList` |  `boolean` Indicates whether the parameter represents a list of values.  
`redact` |  `boolean` Indicates whether the parameter content should be redacted in log. If redaction is enabled, the parameter content will be replaced by parameter name during logging. Note: the parameter content is subject to redaction if either parameter level redaction or `[entity type level redaction](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes#EntityType.FIELDS.redact)` is enabled.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/create)`

|  Creates an intent in the specified agent.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/delete)`

|  Deletes the specified intent.  
  
### `[export](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/export)`

|  Exports the selected intents.  
  
### `[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/get)`

|  Retrieves the specified intent.  
  
### `[import](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/import)`

|  Imports the specified intents into the agent.  
  
### `[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/list)`

|  Returns the list of all intents in the specified agent.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents/patch)`

|  Updates the specified intent.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
