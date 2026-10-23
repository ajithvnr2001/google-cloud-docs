---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/bigquery-v13-schema/
title: BigQuery V13 schema \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:50.826991+00:00
---

# BigQuery V13 schema  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/bigquery-v13-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  BigQuery V13 schema Stay organized with collections  Save and categorize content based on your preferences. 

Changelog:

  * New field `aaSupervisorMonitoringStatus`



Find the column definitions in the following table.

Name | Type | Definition  
---|---|---  
conversationName | STRING | Name of the conversation resource.  
audioFileUri | STRING | Location of the audio file on Google Cloud Storage.  
dialogflowConversationProfileId | STRING | The Dialogflow conversation profile ID of this conversation.  
startTimestampUtc | INTEGER | The time in seconds at which the conversation started.  
startTimestamp | TIMESTAMP | The time at which the conversation started.  
loadTimestampUtc | INTEGER | The time in seconds at which the conversation was loaded into Insights.  
analysisTimestampUtc | INTEGER | The time in seconds at which the most recent analysis was performed.  
conversationUpdateTimestampUtc | INTEGER | The time in seconds at which the conversation was last updated.  
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
clientSentimentRationale | STRING | The rationale for the client sentiment score.  
transcript | STRING | The complete text transcript of the conversation.  
turnCount | INTEGER | The number of turns taken in the conversation.  
languageCode | STRING | Language code of the conversation.  
medium | STRING | Medium of the conversation.  
liveAgentHandoff | BOOL | Whether the conversation was handed off to a live agent.  
issues | REPEATED RECORD | The list of all issues of the conversation.  
issues.name | STRING | The name of the issue.  
issues.score | FLOAT | Score indicating the likelihood of the issue assignment, between 0 and 1.0.  
issues.issueModelId | STRING | ID of the issue model that generated the issue assignment.  
issues.issueId | STRING | ID of the assigned issue.  
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
sentences.annotations.userInput | JSON | The explicit user input used to generate this annotation.  
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
latestSummary | RECORD | The latest conversation summary.  
latestSummary.text | STRING | The summarization content that is concatenated into one string.  
latestSummary.textSections | REPEATED RECORD | The summarization content that is divided into sections. The key is the section's name and the value is the section's content. There is no specific format for the key or value.  
latestSummary.textSections.key | STRING | The name of the section.  
latestSummary.textSections.value | STRING | The content of the section.  
latestSummary.confidence | FLOAT | The confidence score of the summarization.  
latestSummary.metadata | REPEATED RECORD | A map that contains metadata about the summarization and the document from which it originates.  
latestSummary.metadata.key | STRING | The key of the metadata.  
latestSummary.metadata.value | STRING | The value of the metadata.  
latestSummary.answerRecord | STRING | The name of the answer record. Format: projects/{project}/locations/{location}/answerRecords/{answer_record}  
latestSummary.conversationModel | STRING | The name of the model that generates this summary. Format: projects/{project}/locations/{location}/conversationModels/{conversation_model}  
qaScorecardResults | REPEATED RECORD | All QaScorecardResult(s) available for the conversation.  
qaScorecardResults.qaScorecard | STRING | Fully qualified resource name of the scorecard. Format: projects/{project}/locations/{location}/qaScorecards/{qa_scorecard_id}  
qaScorecardResults.qaScorecardRevision | STRING | Fully qualified resource name of the scorecard revision. Format: projects/{project}/locations/{location}/qaScorecards/{qa_scorecard_id}/revisions/{revision_id}  
qaScorecardResults.qaScorecardResult | STRING | Fully qualified resource name of the scorecard result. Format: projects/{project}/locations/{location}/qaScorecards/{qa_scorecard_id}/revisions/{revision_id}/results/{result_id}  
qaScorecardResults.score | FLOAT | The score assigned to the conversation.  
qaScorecardResults.potentialScore | FLOAT | The potential score assigned to the conversation.  
qaScorecardResults.normalizedScore | FLOAT | Normalized score assigned for the conversation.  
qaScorecardResults.qaTagResults | REPEATED RECORD |   
qaScorecardResults.qaTagResults.tag | STRING | The tag assigned to question(s) in the scorecard.  
qaScorecardResults.qaTagResults.score | FLOAT | The score assigned to the tag for this conversation.  
qaScorecardResults.qaTagResults.potentialScore | FLOAT | The potential score assigned to the tag for this conversation.  
qaScorecardResults.qaTagResults.normalizedScore | FLOAT | Normalized score for the given tag for this conversation.  
qaScorecardResults.qaAnswers | REPEATED RECORD | The answers to the questions in the scorecard.  
qaScorecardResults.qaAnswers.qaQuestion | RECORD | A QaQuestion corresponding to the given QaAnswer.  
qaScorecardResults.qaAnswers.qaQuestion.qaQuestion | STRING | Resource name of the question. Format: projects/{project}/locations/{location}/qaScorecards/{qa_scorecard_id}/revisions/{revision_id}/qaQuestions/{qa_question_id}  
qaScorecardResults.qaAnswers.qaQuestion.questionBody | STRING | Question text. For examlpe, "Did the agent greet the customer?"  
qaScorecardResults.qaAnswers.qaAnswerStringValue | STRING |   
qaScorecardResults.qaAnswers.qaAnswerNumericValue | FLOAT |   
qaScorecardResults.qaAnswers.qaAnswerBoolValue | BOOL |   
qaScorecardResults.qaAnswers.qaAnswerNaValue | BOOL |   
qaScorecardResults.qaAnswers.score | FLOAT | The score assigned to the answer.  
qaScorecardResults.qaAnswers.potentialScore | FLOAT | The potential score assigned to the answer.  
qaScorecardResults.qaAnswers.normalizedScore | FLOAT | The normalized score assigned to the answer.  
qaScorecardResults.qaAnswers.qaAnswerRationale | RECORD | The rationale for the answer.  
qaScorecardResults.qaAnswers.qaAnswerRationale.rationale | STRING | The rationale for the answer.  
qaScorecardResults.qaAnswers.tags | REPEATED STRING | User defined list of arbitrary tags.  
qaScorecardResults.qaAnswers.scoreSources | REPEATED RECORD | List of all individual score sets. Each score set contains a score, potential score, normalized score, and a list of tag scores. This contains score per question.  
qaScorecardResults.qaAnswers.scoreSources.sourceType | STRING | The source of the score. Possible values are SOURCE_TYPE_UNSPECIFIED, SYSTEM_GENERATED_ONLY or INCLUDES_MANUAL_EDITS.  
qaScorecardResults.qaAnswers.scoreSources.score | FLOAT | The overall numerical score of the result.  
qaScorecardResults.qaAnswers.scoreSources.potentialScore | FLOAT | The maximum potential overall score of the scorecard. Any questions answered using `na_value` are excluded from this calculation.  
qaScorecardResults.qaAnswers.scoreSources.normalizedScore | FLOAT | The normalized score, which is the score divided by the potential score.  
qaScorecardResults.qaAnswers.scoreSources.qaTagResults | REPEATED RECORD | Collection of tags and their scores.  
qaScorecardResults.qaAnswers.scoreSources.qaTagResults.tag | STRING | The tag the score applies to.  
qaScorecardResults.qaAnswers.scoreSources.qaTagResults.score | FLOAT | The score the tag applies to.  
qaScorecardResults.qaAnswers.scoreSources.qaTagResults.potentialScore | FLOAT | The potential score the tag applies to.  
qaScorecardResults.qaAnswers.scoreSources.qaTagResults.normalizedScore | FLOAT | The normalized score the tag applies to.  
qaScorecardResults.qaAnswers.answerSources | REPEATED RECORD | List of all individual answer sources. Each answer source contains a source type and the answer for the question provided by the LLM if the source is SYSTEM_GENERATED. If the source is MANUAL_EDIT, this field will contain the answer provided by the user using manual edit.  
qaScorecardResults.qaAnswers.answerSources.sourceType | STRING | The source of the answer. Possible values are SOURCE_TYPE_UNSPECIFIED, SYSTEM_GENERATED or MANUAL_EDIT.  
qaScorecardResults.qaAnswers.answerSources.qaAnswerStringValue | STRING |   
qaScorecardResults.qaAnswers.answerSources.qaAnswerNumericValue | FLOAT |   
qaScorecardResults.qaAnswers.answerSources.qaAnswerBoolValue | BOOL |   
qaScorecardResults.qaAnswers.answerSources.qaAnswerNaValue | BOOL |   
qaScorecardResults.qaAnswers.answerSources.score | FLOAT | The score assigned to the answer.  
qaScorecardResults.qaAnswers.answerSources.potentialScore | FLOAT | The potential score assigned to the answer.  
qaScorecardResults.qaAnswers.answerSources.normalizedScore | FLOAT | The normalized score assigned to the answer.  
qaScorecardResults.qaAnswers.answerSources.qaAnswerRationale | RECORD |   
qaScorecardResults.qaAnswers.answerSources.qaAnswerRationale.rationale | STRING | The rationale for the answer.  
qaScorecardResults.scoreSources | REPEATED RECORD | List of all individual score sets.  
qaScorecardResults.scoreSources.sourceType | STRING | The source of the score. Possible values are SOURCE_TYPE_UNSPECIFIED, SYSTEM_GENERATED_ONLY or INCLUDES_MANUAL_EDITS.  
qaScorecardResults.scoreSources.score | FLOAT | The overall numerical score of the result.  
qaScorecardResults.scoreSources.potentialScore | FLOAT | The maximum potential overall score of the scorecard. Any questions answered using `na_value` are excluded from this calculation.  
qaScorecardResults.scoreSources.normalizedScore | FLOAT | The normalized score, which is the score divided by the potential score.  
qaScorecardResults.scoreSources.qaTagResults | REPEATED RECORD | Collection of tags and their scores.  
qaScorecardResults.scoreSources.qaTagResults.tag | STRING | The tag the score applies to.  
qaScorecardResults.scoreSources.qaTagResults.score | FLOAT | The score the tag applies to.  
qaScorecardResults.scoreSources.qaTagResults.potentialScore | FLOAT | The potential score the tag applies to.  
qaScorecardResults.scoreSources.qaTagResults.normalizedScore | FLOAT | The normalized score the tag applies to.  
agents | REPEATED RECORD | Metadata about the agent dimension.  
agents.agentId | STRING | A user-specified string representing the agent. This field replaces the `agent_id` field in the older export versions.  
agents.agentDisplayName | STRING | The agent's name  
agents.agentTeam | STRING | A user-specified string representing the agent's team.  
agents.agentType | STRING | The agent's type. Possible values are ROLE_UNSPECIFIED, HUMAN_AGENT, AUTOMATED_AGENT, END_USER, or ANY_AGENT.  
feedbackLabels | REPEATED RECORD |   
feedbackLabels.name | STRING | The resource name of the feedback label. Format: projects/{project}/locations/{location}/conversations/{conversation}/feedbackLabels/{feedback_label}  
feedbackLabels.labeledResource | STRING | Resource name of the resource to be labeled.  
feedbackLabels.label | STRING | String label.  
feedbackLabels.qaAnswerStringValue | STRING | Quality AI: feedback label of string type.  
feedbackLabels.qaAnswerNumericValue | FLOAT | Quality AI: feedback label of numeric type.  
feedbackLabels.qaAnswerBoolValue | BOOL | Quality AI: feedback label of boolean type.  
feedbackLabels.qaAnswerNaValue | BOOL | Quality AI: feedback label of not applicable (N/A) type.  
feedbackLabels.createTimestampUtc | INTEGER | The timestamp when the feedback label was created.  
feedbackLabels.updateTimestampUtc | INTEGER | The timestamp when the feedback label was last updated.  
aaSupervisorMonitoringStatus | RECORD | The status of the conversation's Agent Assist supervisor monitoring.  
aaSupervisorMonitoringStatus.monitored | BOOL | Whether the conversation was monitored by an AA supervisor.  
aaSupervisorMonitoringStatus.escalatedToSupervisor | BOOL | Whether the conversation was escalated to an AA supervisor.  
aaSupervisorMonitoringStatus.assignedSupervisor | STRING | The ID of the assigned AA supervisor.  
aaSupervisorMonitoringStatus.transferredToHumanAgent | BOOL | Whether the conversation was transferred to a human agent.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
