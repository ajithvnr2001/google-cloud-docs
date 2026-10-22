---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/filtering/
title: Filter conversations \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:59.133158+00:00
---

# Filter conversations  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/filtering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Filter conversations Stay organized with collections  Save and categorize content based on your preferences. 

You can filter conversations based on information gleaned directly from their characteristics or from attributes of operations that those conversations have been through.

## Conversation filters

Conversations can be filtered on one or more of the characteristics in the following table. These filters are useful for narrowing down a search among large conversation data sets. The "Filtering" section of the [List Conversations](https://docs.cloud.google.com/gemini-enterprise-cx/insights/list-conversations-api#filtering) page lists the permissions you need to apply the following filters.

**Note:** When using the double quotes (") in a curl command or a URL, you should escape them with a backslash and no extra space after (").Filter term | Description | Reference code  
---|---|---  
Agent ID | String for a unique agent |  `agent_id="some agent_id"` `quality_metadata.agent_info.agent_id:"some agent_id"`  
Agent team | String for an agent team |  `agent_team="some agent_team"` `quality_metadata.agent_info.teams:"some agent_team"`  
Agent type | Human or automated agent |  `quality_metadata.agent_info.agent_type:"HUMAN_AGENT"` `quality_metadata.agent_info.agent_type="AUTOMATED_AGENT"`  
Analysis create time | Time when the analysis was created | `latest_analysis.create_time>"2023-12-31T16:00:10-08:00"`  
Analysis status | Whether the conversation has been analyzed |  Has been analyzed: `latest_analysis:"*"` Has not been analyzed: `-latest_analysis:"*"`  
Conversation channel | Medium of the conversation: PHONE_CALL or CHAT | `medium="PHONE_CALL"`  
Conversation create time | Time when the conversation was imported into CX Insights |  `create_time>"1969-12-31T16:00:10-08:00"` `create_time<="1969-12-31T16:00:20-08:00"`  
Conversation label | Label or tag assigned to a conversation |  `labels:"key_only"` `labels.key_1:"value_1"`  
Conversation start time | Time at which the conversation began |  `start_time>"1969-12-31T16:00:10-08:00"` `start_time>"1969-12-31T16:00:20-08:00"`  
Conversation update time | Time when the conversation was last updated |  `update_time>"1969-12-31T16:00:10-08:00"` `update_time<="1969-12-31T16:00:20-08:00"`  
CSAT score | Customer satisfaction score |  `quality_metadata.customer_satisfaction_rating>"1"` `quality_metadata.customer_satisfaction_rating<"5"`  
Custom highlight (also called Phrase matchers) | [Custom highlights](https://docs.cloud.google.com/gemini-enterprise-cx/insights/custom-highlights-ui) to help flag certain phrases |  `latest_analysis.analysis_result.call_analysis_metadata.phrase_matchers.id:"add_one_positive_custom_highlight"` `latest_analysis.analysis_result.call_analysis_metadata.phrase_matchers.id:"multiple positive custom highlights"` `-latest_analysis.analysis_result.call_analysis_metadata.phrase_matchers.id:"one_negative_custom_highlight"` `-latest_analysis.analysis_result.call_analysis_metadata.phrase_matchers.id:"multiple negative custom highlights"`  
Data source | Source of the conversation is Cloud Storage or Dialogflow, or has screen recordings |  `data_source.gcs_source: "*"` `data_source.dialogflow_source: "*"` `data_source.screen_recordings.video_uri: "*"`  
Dialogflow conversation | Conversation that took place through Dialogflow, using a virtual agent | `data_source.dialogflow_source.dialogflow_conversation="projects/123456789/locations/us-central1/conversations/some_dialogflow_conversation"`  
Dialogflow conversation profile ID | String for a unique Dialogflow conversation profile | `dialogflow_conversation_profile_id="some_dialogflow_conversation_profile_id"`  
Duration | Length of time conversation lasted | `duration<="20s"`  
Language | Spoken or typed language used in the conversation with language code in BCP-47 format and supported prefixes | `language_code: "some_language_code"`  
Latest analysis create time | Time at which the latest analysis was created |  `latest_analysis.create_time>"1969-12-31T16:00:10-08:00"` `latest_analysis.create_time<$eq;"1969-12-31T16:00:20-08:00"`  
Latest summary | Match a portion of the most recent summary |  `latest_summary.text:"phrase to match"` `latest_summary.text:"and another"` `-latest_summary.text:"exclude this"`  
Scorecard | All conversations analyzed by a particular scorecard | latest_analysis.analysis_result.call_analysis_metadata.qa_scorecard_results.qa_scorecard_revision_id=projects/PROJECT_ID/locations/us-central1/qaScorecards/SCORECARD_ID  
Scorecard question answer | Conversations analyzed by a particular scorecard and which yield a particular answer for a question | latest_analysis.analysis_result.call_analysis_metadata.qa_scorecard_results.qa_answers.contains((qa_question="projects/PROJECT_ID/locations/LOCATION_ID/qaScorecards/SCORECARD_ID/revisions/REVISION_ID/qaQuestions/QUESTION"),(answer_value.str_value="ANSWER"))  
Sentiment score | Average user sentiment score for the conversation |  `latest_analysis.analysis_result.call_analysis_metadata.sentiments.sentiment_data.score>"0.1"` `latest_analysis.analysis_result.call_analysis_metadata.sentiments.sentiment_data.score<"0.2"`  
Silence duration | Length of the silence time the conversation has |  `latest_analysis.analysis_result.call_analysis_metadata.silence.silence_duration>"10s"` `latest_analysis.analysis_result.call_analysis_metadata.silence.silence_duration<$eq;"20s"`  
Smart highlight | [Smart highlights](https://docs.cloud.google.com/gemini-enterprise-cx/insights/smart-highlights) to help flag certain phrases. |  `latest_analysis.analysis_result.call_analysis_metadata.intents.display_name:"one_positive_smart_highlight"` `latest_analysis.analysis_result.call_analysis_metadata.intents.display_name:"multiple positive smart highlights"` `-latest_analysis.analysis_result.call_analysis_metadata.intents.display_name:"one_negative_smart_highlight"` `-latest_analysis.analysis_result.call_analysis_metadata.intents.display_name:"multiple negative smart highlights"`  
Summary status | Whether a summary has been generated |  Has a summary: `latest_summary:"*"` No summary: `-latest_summary:"*"`  
Topic (also called Issue) | Topic or issue identified by Topic Modeling |  `latest_analysis.analysis_result.issues.issue="projects/123456789/locations/us-central1/issueModels/test_model/issues/issue_foo"` `latest_analysis.analysis_result.issue_model_id="projects/123456789/locations/us-central1/issueModels/test_model"`  
Transcript | Match text of the conversation |  `transcript.transcript_segments.text:"one_positive_term"` `transcript.transcript_segments.text:"multiple positive terms"` `-transcript.transcript_segments.text:"one_negative_term"` `-transcript.transcript_segments.text:"multiple negative terms"`  
Turn count | Number of conversation turns |  `turn_count>"10"` `turn_count<="20"`  
  
## Operation filters

You can also filter conversations based on the information available from operations that have been performed on them. You can filter a conversation dataset based on the following operation attributes.

Filter term | Description | Reference code  
---|---|---  
Create time | Time at which the operation was created |  `metadata.create_time>"1969-12-31T16:00:10-08:00"` `metadata.create_time<="1969-12-31T16:00:20-08:00"`  
Conversation ID | String for a specific conversation | `metadata.conversation_id="some_conversation_id"`  
Done | Final status of an operation |  Completed: `done="true"` Not completed: `done="false"`  
Operation Type | Type of operation performed on the dataset |  Operation type is: `metadata.operation_type="BulkAnalyzeConversations"` Operation type is not: `metadata.operation_type!="BulkAnalyzeConversations"`  
Status | Detailed status of the operation |  Completed successfully: `status_code="0"` Failed but not aborted: `status_code!="ABORTED"`  
  
To view the errors from running a bulk operation, you must use a curl command.

  * Bulk analyze operations: 
        
        curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" "https://contactcenterinsights.googleapis.com/v1/projects/$PROJECT/locations/$LOCATION/operations?filter=metadata.operation_type=\"BulkAnalyzeConversations\"&page_size=10"

  * Bulk ingest operations (transcript or audio): 
        
        curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8"  "https://contactcenterinsights.googleapis.com/v1/projects/$PROJECT/locations/$LOCATION/operations?filter=metadata.operation_type=\"IngestConversations\"&page_size=10"




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
