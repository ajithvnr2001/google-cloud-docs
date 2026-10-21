---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/bigquery-v2-schema/
title: BigQuery V2 schema \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:54:44.151183+00:00
---

# BigQuery V2 schema  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/bigquery-v2-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  BigQuery V2 schema Stay organized with collections  Save and categorize content based on your preferences. 

Changelog:

  * New field `dialogflowConversationProfileId`
  * New field `sentences.annotations.annotationRecord`
  * New field `sentences.annotations.detailedFeedback`
  * Deprecated field `sentences.annotations.record`



Find the column definitions in the following table.

Name | Type | Definition  
---|---|---  
conversationName | STRING | Name of the conversation resource.  
audioFileUri | STRING | Location of the audio file on Google Cloud Storage.  
agentId | STRING | The user-provided identifier for the agent who handled the conversation.  
dialogflowConversationProfileId | STRING | The Dialogflow conversation profile ID of this conversation.  
startTimestampUtc | INTEGER | The time in seconds at which the conversation started.  
loadTimestampUtc | INTEGER | The time in seconds at which the conversation was loaded into Insights.  
year | INTEGER | Year date part of `loadTimestampUtc`.  
month | INTEGER | Month date part of `loadTimestampUtc`.  
day | INTEGER | Day date part of `loadTimestampUtc`.  
durationNanos | INTEGER | Conversation duration in nanoseconds.  
silenceNanos | INTEGER | Number of nanoseconds calculated to be in silence.  
silencePercentage | FLOAT | Percentage of the total conversation spent in silence.  
agentSpeakingPercentage | FLOAT | Percentage of the conversation with the agent speaking.  
clientSpeakingPercentage | FLOAT | Percentage of the conversation with the client speaking.  
agentSentimentScore | FLOAT | Agent sentiment score between -1.0 (negative) and 1.0 (positive).  
agentSentimentMagnitude | FLOAT | A non-negative number from zero to infinity that represents the absolute magnitude of the agent sentiment regardless of score.  
clientSentimentScore | FLOAT | Client sentiment score between -1.0 (negative) and 1.0 (positive).  
clientSentimentMagnitude | FLOAT | A non-negative number from zero to infinity that represents the absolute magnitude of client sentiment regardless of score.  
transcript | STRING | The complete text transcript of the conversation.  
turnCount | INTEGER | The number of turns taken in the conversation.  
languageCode | STRING | Language code of the conversation.  
medium | STRING | Medium of the conversation.  
issues | REPEATED RECORD | The list of all issues of the conversation.  
issues.name | STRING | The name of the issue.  
issues.score | FLOAT | Score indicating the likelihood of the issue assignment, between 0 and 1.0.  
entities | REPEATED RECORD | The list of all spoken entities.  
entities.name | STRING | Name of the entity.  
entities.type | STRING | Type of the entity.  
entities.sentimentScore | FLOAT | The entity sentiment score between -1.0 (negative) and 1.0 (positive).  
entities.sentimentMagnitude | FLOAT | A non-negative number from zero to infinity that represents the absolute magnitude of the entity sentiment regardless of score.  
entities.salience | FLOAT | Salience score of the entity.  
entities.speakerTag | INTEGER | The speaker that the entity mention originated from.  
labels | REPEATED RECORD | The list of all user-provided labels.  
labels.key | STRING | User-provided label key.  
labels.value | STRING | User-provided label value.  
words | REPEATED RECORD | The list of all spoken words.  
words.word | STRING | The transcribed word.  
words.startOffsetNanos | INTEGER | Time offset in nanoseconds of the start of this word relative to the beginning of the conversation.  
words.endOffsetNanos | INTEGER | Time offset in nanoseconds of the end of this word relative to the beginning of the conversation.  
words.speakerTag | INTEGER | The speaker that the word originated from.  
words.languageCode | STRING | Language code.  
sentences | REPEATED RECORD | The list of conversation sentences.  
sentences.sentence | STRING | The transcribed sentence.  
sentences.sentimentScore | FLOAT | The sentence sentiment score between -1.0 (negative) and 1.0 (positive).  
sentences.sentimentMagnitude | FLOAT | A non-negative number from zero to infinity that represents the absolute magnitude of the sentence sentiment regardless of score.  
sentences.speakerTag | INTEGER | The speaker that the sentence originated from.  
sentences.languageCode | STRING | Language code.  
sentences.startOffsetNanos | INTEGER | Time offset in nanoseconds of the start of this sentence relative to the beginning of the conversation.  
sentences.endOffsetNanos | INTEGER | Time offset in nanoseconds of the end of this sentence relative to the beginning of the conversation.  
sentences.createTimeNanos | INTEGER | Time in nanoseconds that the conversation message took place, if provided.  
sentences.participantId | STRING | Participant ID, if provided.  
sentences.participantRole | STRING | Participant role, if provided.  
sentences.obfuscatedExternalUserId | STRING | Obfuscated external user ID, if provided.  
sentences.isCoveredBySmartReplyAllowlist | BOOL | Whether the sentence is covered by [a configured smart reply allowlist](https://docs.cloud.google.com/agent-assist/docs/model-training#model_allowlist_management) in Agent Assist.  
sentences.annotations | REPEATED RECORD | The list of annotations from [Dialogflow Runtime Integration](https://docs.cloud.google.com/gemini-enterprise-cx/insights/enable-dialogflow-runtime-integration). See [full list](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations#runtimeannotation).  
sentences.annotations.annotationRecord | JSON | The annotation record returned from Dialogflow.  
sentences.annotations.createTimeNanos | INTEGER | The timestamp when the suggestion was generated.  
sentences.annotations.type | STRING | The type of suggestion.  
sentences.annotations.clicked | BOOL | Customer feedback on whether the suggestion was clicked.  
sentences.annotations.correctnessLevel | STRING | Customer feedback on the correctness level of the suggestion.  
sentences.annotations.displayed | BOOL | Customer feedback on whether the suggestion was displayed.  
sentences.annotations.detailedFeedback | JSON | The detailed feedback content returned from Dialogflow.  
sentences.intentMatchData | REPEATED RECORD | The list of matched intents for the sentence.  
sentences.intentMatchData.intentId | STRING | The unique ID of the matched intent.  
sentences.intentMatchData.displayName | STRING | The human readable name of the matched intent.  
sentences.phraseMatchData | REPEATED RECORD | The list of phrase match data for the sentence.  
sentences.phraseMatchData.phraseMatcherId | STRING | The unique ID of the phrase matcher.  
sentences.phraseMatchData.revisionId | STRING | Indicating the revision of the phrase matcher.  
sentences.phraseMatchData.displayName | STRING | The human readable name of the phrase matcher.  
sentences.highlightData | REPEATED RECORD | The list of highlighter data for the sentence.  
sentences.highlightData.highlighterName | STRING | The unique id of the highlighter.  
sentences.highlightData.displayName | STRING | The human readable name of the highlighter.  
sentences.highlightData.type | STRING | The type of the highlighter.  
sentences.dialogflowIntentMatchData | REPEATED RECORD | The list of Dialogflow intent match data for the sentence.  
sentences.dialogflowIntentMatchData.intentName | STRING | The resource name of the matched intent.  
sentences.dialogflowIntentMatchData.displayName | STRING | The human readable name of the matched intent.  
sentences.dialogflowIntentMatchData.maxConfidence | FLOAT | The confidence score for the intent match, between 0 and 1.0.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
