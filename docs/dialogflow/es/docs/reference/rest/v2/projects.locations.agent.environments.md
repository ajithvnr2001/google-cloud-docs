---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments
title: REST Resource: projects.locations.agent.environments \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:34.619625+00:00
---

# REST Resource: projects.locations.agent.environments  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  REST Resource: projects.locations.agent.environments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Environment
    * JSON representation
  * Methods



## Resource: Environment

You can create multiple versions of your agent and publish them to separate environments.

When you edit an agent, you are editing the draft agent. At any point, you can save the draft agent as an agent version, which is an immutable snapshot of your agent.

When you save the draft agent, it is published to the default environment. When you create agent versions, you can publish them to custom environments. You can create a variety of custom environments for:

  * testing
  * development
  * production
  * etc.



For more information, see the [versions and environments guide](https://cloud.google.com/dialogflow/docs/agents-versions).

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "agentVersion": string,
      "state": enum ([State](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments#Environment.State)),
      "updateTime": string,
      "textToSpeechSettings": {
        object ([TextToSpeechSettings](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments#Environment.TextToSpeechSettings))
      },
      "fulfillment": {
        object ([Fulfillment](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments#Environment.Fulfillment))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. The unique identifier of this agent environment. Supported formats:

  * `projects/<Project ID>/agent/environments/<Environment ID>`
  * `projects/<Project ID>/locations/<Location ID>/agent/environments/<Environment ID>`

The environment ID for the default environment is `-`.  
`description` |  `string` Optional. The developer-provided description for this environment. The maximum length is 500 characters. If exceeded, the request is rejected.  
`agentVersion` |  `string` Optional. The agent version loaded into this environment. Supported formats:

  * `projects/<Project ID>/agent/versions/<Version ID>`
  * `projects/<Project ID>/locations/<Location ID>/agent/versions/<Version ID>`

  
`state` |  `enum (`[State](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments#Environment.State)`)` Output only. The state of this environment. This field is read-only, i.e., it cannot be set by create and update methods.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last update time of this environment. This field is read-only, i.e., it cannot be set by create and update methods.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`textToSpeechSettings` |  `object (`[TextToSpeechSettings](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments#Environment.TextToSpeechSettings)`)` Optional. Text to speech settings for this environment.  
`fulfillment` |  `object (`[Fulfillment](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments#Environment.Fulfillment)`)` Optional. The fulfillment settings to use for this environment.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments/create)`

|  Creates an agent environment.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments/delete)`

|  Deletes the specified agent environment.  
  
### `[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments/get)`

|  Retrieves the specified agent environment.  
  
### `[getHistory](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments/getHistory)`

|  Gets the history of the specified environment.  
  
### `[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments/list)`

|  Returns the list of all non-default environments of the specified agent.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.locations.agent.environments/patch)`

|  Updates the specified agent environment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-21 UTC."],[],[]] 
