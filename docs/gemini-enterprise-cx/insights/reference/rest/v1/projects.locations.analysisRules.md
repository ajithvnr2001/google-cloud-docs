---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.analysisRules
title: REST Resource: projects.locations.analysisRules \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:45:57.773352+00:00
---

# REST Resource: projects.locations.analysisRules  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.analysisRules

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  REST Resource: projects.locations.analysisRules Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AnalysisRule
    * JSON representation
  * Methods



## Resource: AnalysisRule

The CCAI Insights project wide analysis rule. This rule will be applied to all conversations that match the filter defined in the rule. For a conversation matches the filter, the annotators specified in the rule will be run. If a conversation matches multiple rules, a union of all the annotators will be run. One project can have multiple analysis rules.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "conversationFilter": string,
      "annotatorSelector": {
        object ([AnnotatorSelector](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/AnnotatorSelector))
      },
      "analysisPercentage": number,
      "active": boolean,
      "displayName": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the analysis rule. Format: projects/{project}/locations/{location}/analysisRules/{analysisRule}  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this analysis rule was created.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The most recent time at which this analysis rule was updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`conversationFilter` |  `string` Filter for the conversations that should apply this analysis rule. An empty filter means this analysis rule applies to all conversations. Refer to <https://cloud.google.com/gemini-enterprise-cx/insights/filtering> for details.  
`annotatorSelector` |  `object (`[AnnotatorSelector](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/AnnotatorSelector)`)` Selector of annotators to run and the phrase matchers to use for conversations that matches the conversationFilter. If not specified, NO annotators will be run.  
`analysisPercentage` |  `number` Percentage of conversations that we should apply this analysis setting automatically, between [0, 1]. For example, 0.1 means 10%. Conversations are sampled in a determenestic way. The original runtime_percentage & upload percentage will be replaced by defining filters on the conversation.  
`active` |  `boolean` If true, apply this rule to conversations. Otherwise, this rule is inactive and saved as a draft.  
`displayName` |  `string` Display Name of the analysis rule.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.analysisRules/create)`

|  Creates a analysis rule.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.analysisRules/delete)`

|  Deletes a analysis rule.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.analysisRules/get)`

|  Get a analysis rule.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.analysisRules/list)`

|  Lists analysis rules.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.analysisRules/patch)`

|  Updates a analysis rule.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
