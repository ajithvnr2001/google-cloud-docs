---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.feedbackLabels
title: REST Resource: projects.locations.conversations.feedbackLabels \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:03:07.497523+00:00
---

# REST Resource: projects.locations.conversations.feedbackLabels  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.feedbackLabels

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  REST Resource: projects.locations.conversations.feedbackLabels Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: FeedbackLabel
    * JSON representation
  * Methods



## Resource: FeedbackLabel

Represents a conversation, resource, and label provided by the user. Can take the form of a string label or a QaAnswer label. QaAnswer labels are used for Quality AI example conversations. String labels are used for Topic Modeling. AgentAssistSummary labels are used for Agent Assist Summarization.

JSON representation  
---  
      
    
    {
      "name": string,
      "labeledResource": string,
      "createTime": string,
      "updateTime": string,
    
      // Union field label_type can be only one of the following:
      "label": string,
      "qaAnswerLabel": {
        object ([AnswerValue](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/AnswerValue))
      }
      // End of list of possible types for union field label_type.
    }  
  
Fields  
---  
`name` |  `string` Immutable. Resource name of the FeedbackLabel. Format: projects/{project}/locations/{location}/conversations/{conversation}/feedbackLabels/{feedbackLabel}  
`labeledResource` |  `string` Name of the resource to be labeled. Supported resources are:

  * `projects/{project}/locations/{location}/qaScorecards/{scorecard}/revisions/{revision}/qaQuestions/{question}`
  * `projects/{project}/locations/{location}/issueModels/{issueModel}`
  * `projects/{project}/locations/{location}/generators/{generatorId}`

  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create time of the label.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update time of the label.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `label_type`. Label type. `label_type` can be only one of the following:  
`label` |  `string` String label used for Topic Modeling.  
`qaAnswerLabel` |  `object (`[AnswerValue](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/AnswerValue)`)` QaAnswer label used for Quality AI example conversations.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.feedbackLabels/create)`

|  Create feedback label.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.feedbackLabels/delete)`

|  Delete feedback label.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.feedbackLabels/get)`

|  Get feedback label.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.feedbackLabels/list)`

|  List feedback labels.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations.feedbackLabels/patch)`

|  Update feedback label.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
