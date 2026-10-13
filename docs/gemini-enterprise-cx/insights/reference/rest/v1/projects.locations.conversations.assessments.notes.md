---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.assessments.notes
title: REST Resource: projects.locations.conversations.assessments.notes \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:59.555254+00:00
---

# REST Resource: projects.locations.conversations.assessments.notes  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.assessments.notes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  REST Resource: projects.locations.conversations.assessments.notes Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Note
    * JSON representation
  * Methods



## Resource: Note

The conversation assessment note resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "noteCreator": {
        object ([UserInfo](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments.notes#Note.UserInfo))
      },
    
      // Union field note_type can be only one of the following:
      "conversationTurnNote": {
        object ([ConversationTurnNote](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments.notes#Note.ConversationTurnNote))
      },
      "qaQuestionNote": {
        object ([QaQuestionNote](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments.notes#Note.QaQuestionNote))
      },
      "assessmentNote": {
        object ([AssessmentNote](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments.notes#Note.AssessmentNote))
      }
      // End of list of possible types for union field note_type.
      "content": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the note. Format: projects/{project}/locations/{location}/conversations/{conversation}/assessments/{assessment}/notes/{note}  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the note was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the note was last updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`noteCreator` |  `object (`[UserInfo](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments.notes#Note.UserInfo)`)` Output only. The user that created the note.  
Union field `note_type`. The type of the note. `note_type` can be only one of the following:  
`conversationTurnNote` |  `object (`[ConversationTurnNote](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments.notes#Note.ConversationTurnNote)`)` The note is associated with a conversation turn.  
`qaQuestionNote` |  `object (`[QaQuestionNote](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments.notes#Note.QaQuestionNote)`)` The note is associated with a QA question in one of the conversation's scorecard results.  
`assessmentNote` |  `object (`[AssessmentNote](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews.conversations.assessments.notes#Note.AssessmentNote)`)` The note is associated to the entire parent assessment.  
`content` |  `string` The note content.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.assessments.notes/create)`

|  Create Note.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.assessments.notes/delete)`

|  Deletes a Note.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.assessments.notes/list)`

|  List Notes.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.assessments.notes/patch)`

|  Update Note.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
