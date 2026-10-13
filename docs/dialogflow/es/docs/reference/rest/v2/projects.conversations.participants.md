---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants
title: REST Resource: projects.conversations.participants \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:23.619997+00:00
---

# REST Resource: projects.conversations.participants  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  REST Resource: projects.conversations.participants Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Participant
    * JSON representation
    * Role
    * AgentDesktopSource
  * Methods



## Resource: Participant

Represents a conversation participant (human agent, virtual agent, end-user).

JSON representation  
---  
      
    
    {
      "name": string,
      "role": enum ([Role](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants#Participant.Role)),
      "sipRecordingMediaLabel": string,
      "obfuscatedExternalUserId": string,
      "documentsMetadataFilters": {
        string: string,
        ...
      },
      "agentDesktopSource": enum ([AgentDesktopSource](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants#Participant.AgentDesktopSource))
    }  
  
Fields  
---  
`name` |  `string` Optional. The unique identifier of this participant. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`.  
`role` |  `enum (`[Role](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants#Participant.Role)`)` Immutable. The role this participant plays in the conversation. This field must be set during participant creation and is then immutable.  
`sipRecordingMediaLabel` |  `string` Optional. Label applied to streams representing this participant in SIPREC XML metadata and SDP. This is used to assign transcriptions from that media stream to this participant. This field can be updated.  
`obfuscatedExternalUserId` |  `string` Optional. Obfuscated user id that should be associated with the created participant.You can specify a user id as follows:

  1. If you set this field in `CreateParticipantRequest` or `UpdateParticipantRequest`, Dialogflow adds the obfuscated user id with the participant.
  2. If you set this field in `participants.analyzeContent` or `StreamingAnalyzeContent`, Dialogflow will update `[Participant.obfuscated_external_user_id](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants#Participant.FIELDS.obfuscated_external_user_id)`.

Dialogflow returns an error if you try to add a user id for a non-`[END_USER](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants#Participant.Role.ENUM_VALUES.END_USER)` participant.Dialogflow uses this user id for billing and measurement purposes. For example, Dialogflow determines whether a user in one conversation returned in a later conversation.Additionally, to link an escalated Virtual Agent conversation with its corresponding Agent Assist conversation for analytics, this field in Agent Assist conversations should be populated to indicate the user id of the `END_USER` participant in the escalated conversation.Note:

  * Please never pass raw user ids to Dialogflow. Always obfuscate your user id first.
  * Dialogflow only accepts a UTF-8 encoded string, e.g., a hex digest of a hash function like SHA-512.
  * The length of the user id must be <= 256 characters.

  
`documentsMetadataFilters` |  `map (key: string, value: string)` Optional. Key-value filters on the metadata of documents returned by article suggestion. If specified, article suggestion only returns suggested documents that match all filters in their `[Document.metadata](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.knowledgeBases.documents#Document.FIELDS.metadata)`. Multiple values for a metadata key should be concatenated by comma. For example, filters to match all documents that have 'US' or 'CA' in their market metadata values and 'agent' in their user metadata values will be
    
    
    documentsMetadataFilters {
      key: "market"
      value: "US,CA"
    }
    documentsMetadataFilters {
      key: "user"
      value: "agent"
    }
    

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`agentDesktopSource` |  `enum (`[AgentDesktopSource](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants#Participant.AgentDesktopSource)`)` Optional. For tracking the utilization of prebuilt Agent Assist integration modules. This field is only inscope for Integration type that include UI Modules, Backend Modules, and Agent Desktop connector, it is out of scope for CCaaS and Direct Integration. For each human agent, prebuilt UI Modules needs to trigger the participants.patch API to update this field. Both `CreateParticipantRequest` and `UpdateParticipantRequest` will be supported.  
  
### Role

Enumeration of the roles a participant can play in a conversation.

Enums  
---  
`ROLE_UNSPECIFIED` | Participant role not set.  
`HUMAN_AGENT` | Participant is a human agent.  
`AUTOMATED_AGENT` | Participant is an automated agent, such as a Dialogflow agent.  
`END_USER` | Participant is an end user that has called or chatted with Dialogflow services.  
  
### AgentDesktopSource

Enumeration of the Agent Desktop Source when using prebuilt Agent Assist integration modules.

Enums  
---  
`AGENT_DESKTOP_SOURCE_UNSPECIFIED` | Agent Desktop Source is not specified.  
`LIVE_PERSON` | Agent Desktop Source is Live Person.  
`GENESYS_CLOUD` | Agent Desktop Source is Genesys Cloud.  
`TWILIO` | Agent Desktop Source is Twilio.  
`SALESFORCE` | Agent Desktop Source is Salesforce.  
`OTHER` | UI Modules are in use but the desktop is either not currently released or setting this field to the applicable desktop.  
  
## Methods  
  
---  
  
### `[analyzeContent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants/analyzeContent)`

|  Adds a text (chat, for example), or audio (phone recording, for example) message from a participant into the conversation.  
  
### `[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants/create)`

|  Creates a new participant in a conversation.  
  
### `[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants/get)`

|  Retrieves a conversation participant.  
  
### `[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants/list)`

|  Returns the list of all participants in the specified conversation.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants/patch)`

|  Updates the specified participant.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-25 UTC."],[],[]] 
