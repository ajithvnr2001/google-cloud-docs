---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.feedbackEntries
title: REST Resource: projects.locations.reasoningEngines.feedbackEntries \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:05:04.802586+00:00
---

# REST Resource: projects.locations.reasoningEngines.feedbackEntries  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.feedbackEntries

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  REST Resource: projects.locations.reasoningEngines.feedbackEntries Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: FeedbackEntry

FeedbackEntry is a resource that represents a user's feedback on a conversation with an agent.

Fields  
  
`name` `string` Identifier. The resource name. Assigned by the server on create.Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoningEngine}/feedbackEntries/{feedbackEntry}` | `sessionId` `string` Required. The id of the session that the feedback relates to. | `eventId` `string` Required. The id of the event within the session that the feedback relates to. | `feedbackType` `enum (`[FeedbackType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.feedbackEntries#FeedbackType)`)` Required. The coarse-grained type of feedback provided by the user. Must be set to a value other than `FEEDBACK_TYPE_UNSPECIFIED`. | `feedbackLabels[]` `string` | `feedbackText` `string` Optional. Qualitative free-form comments provided by the user. | `userId` `string` Optional. A caller-supplied identifier for the user who provided the feedback. The semantics of this field (for example whether it is an opaque token, a hashed value, or a user-visible identifier) are determined by the calling application. | `source` `string` Optional. The surface that the feedback originated from. | `customMetadata` `map (key: string, value: string)` Optional. Additional key-value metadata associated with the feedback. | `createTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the entry was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `updateTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the entry was most recently updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | JSON representation  
---  
      
    
    {
      "name": string,
      "sessionId": string,
      "eventId": string,
      "feedbackType": enum ([FeedbackType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.feedbackEntries#FeedbackType)),
      "feedbackLabels": [
        string
      ],
      "feedbackText": string,
      "userId": string,
      "source": string,
      "customMetadata": {
        string: string,
        ...
      },
      "createTime": string,
      "updateTime": string
    }  
  
## FeedbackType

The coarse-grained type of feedback provided by the user.

The enum is not frozen; additional values may be added in the future, so clients should treat unknown values gracefully.

Enums  
---  
`FEEDBACK_TYPE_UNSPECIFIED` | This is the default value meaning the type has not been set.  
`THUMBS_UP` | Indicates positive feedback.  
`THUMBS_DOWN` | Indicates negative feedback.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.feedbackEntries/create)`

|  Creates a new FeedbackEntry.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.feedbackEntries/delete)`

|  Deletes a FeedbackEntry and its associated FeedbackContext.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.feedbackEntries/get)`

|  Retrieves a single FeedbackEntry by its resource name.  
  
### `[getFeedbackContext](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.feedbackEntries/getFeedbackContext)`

|  Retrieves the FeedbackContext associated with a FeedbackEntry.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.feedbackEntries/list)`

|  Lists FeedbackEntries in a ReasoningEngine.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.feedbackEntries/patch)`

|  Updates an existing FeedbackEntry.  
  
### `[updateFeedbackContext](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.reasoningEngines.feedbackEntries/updateFeedbackContext)`

|  Updates the FeedbackContext associated with a FeedbackEntry.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-07 UTC."],[],[]] 
