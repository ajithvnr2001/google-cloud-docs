---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.engines.sessions.answers
title: REST Resource: projects.locations.collections.engines.sessions.answers \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:52.107905+00:00
---

# REST Resource: projects.locations.collections.engines.sessions.answers  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.engines.sessions.answers

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  REST Resource: projects.locations.collections.engines.sessions.answers Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Answer
    * JSON representation
  * Methods



## Resource: Answer

Defines an answer.

JSON representation  
---  
      
    
    {
      "name": string,
      "state": enum ([State](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.sessions.answers#Answer.State)),
      "answerText": string,
      "citations": [
        {
          object ([Citation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.sessions.answers#Answer.Citation))
        }
      ],
      "groundingSupports": [
        {
          object ([GroundingSupport](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.sessions.answers#Answer.GroundingSupport))
        }
      ],
      "references": [
        {
          object ([Reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.sessions.answers#Answer.Reference))
        }
      ],
      "blobAttachments": [
        {
          object ([BlobAttachment](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.sessions.answers#Answer.BlobAttachment))
        }
      ],
      "relatedQuestions": [
        string
      ],
      "steps": [
        {
          object ([Step](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.sessions.answers#Answer.Step))
        }
      ],
      "queryUnderstandingInfo": {
        object ([QueryUnderstandingInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.sessions.answers#Answer.QueryUnderstandingInfo))
      },
      "answerSkippedReasons": [
        enum ([AnswerSkippedReason](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.sessions.answers#Answer.AnswerSkippedReason))
      ],
      "createTime": string,
      "completeTime": string,
      "safetyRatings": [
        {
          object ([SafetyRating](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.sessions.answers#Answer.SafetyRating))
        }
      ],
      "groundingScore": number
    }  
  
Fields  
---  
`name` |  `string` Immutable. Fully qualified name `projects/{project}/locations/global/collections/{collection}/engines/{engine}/sessions/*/answers/*`  
`state` |  `enum (`[State](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.sessions.answers#Answer.State)`)` The State of the answer generation.  
`answerText` |  `string` The textual answer.  
`citations[]` |  `object (`[Citation](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.sessions.answers#Answer.Citation)`)` Citations.  
`groundingSupports[]` |  `object (`[GroundingSupport](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.sessions.answers#Answer.GroundingSupport)`)` Optional. Grounding supports.  
`references[]` |  `object (`[Reference](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.sessions.answers#Answer.Reference)`)` References.  
`blobAttachments[]` |  `object (`[BlobAttachment](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.sessions.answers#Answer.BlobAttachment)`)` Output only. List of blob attachments in the answer.  
`relatedQuestions[]` |  `string` Suggested related questions.  
`steps[]` |  `object (`[Step](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.sessions.answers#Answer.Step)`)` Answer generation steps.  
`queryUnderstandingInfo` |  `object (`[QueryUnderstandingInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.sessions.answers#Answer.QueryUnderstandingInfo)`)` Query understanding information.  
`answerSkippedReasons[]` |  `enum (`[AnswerSkippedReason](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.sessions.answers#Answer.AnswerSkippedReason)`)` Additional answer-skipped reasons. This provides the reason for ignored cases. If nothing is skipped, this field is not set.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Answer creation timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`completeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Answer completed timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`safetyRatings[]` |  `object (`[SafetyRating](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.sessions.answers#Answer.SafetyRating)`)` Optional. Safety ratings.  
`groundingScore` |  `number` A score in the range of [0, 1] describing how grounded the answer is by the reference chunks.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.engines.sessions.answers/get)`

|  Gets a Answer.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-21 UTC."],[],[]] 
