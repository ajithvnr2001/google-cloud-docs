---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/analysis-rule/
title: Configure analysis rules \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:28.767784+00:00
---

# Configure analysis rules  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/analysis-rule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Configure analysis rules Stay organized with collections  Save and categorize content based on your preferences. 

Analysis rules are designed to provide more flexible and user-friendly automatic analysis of your contact center conversations. By defining rules, you can specify exactly which conversations to analyze and which types of analysis to perform. Customer Experience Insights adopts your specifications automatically when ingesting conversations, so that you can control the budget and focus on important conversations to analyze.

## Analysis rule capabilities

Analysis rules provide the following customization capabilities all in one place:

  * Use [filters](https://docs.cloud.google.com/gemini-enterprise-cx/insights/filtering) to choose which conversations to analyze.
  * Specify the percentage of your conversation dataset for CX Insights to analyze.
  * Designate different types of analysis for each portion of your dataset.



The existing [analysis configuration settings](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/Settings#analysisconfig) let you specify the percentage of conversations to analyze and designate the type of analysis to use on your full conversation dataset. However, with analysis rules, you can also filter your conversations, then specify both the percentage and analysis type to use for the filtered dataset. Analysis rules replace the analysis configuration settings.

**Note:** CX Insights denies any updates to the old [analysis configuration settings](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/Settings#analysisconfig), and that configuration is disregarded in favor of the analysis rules.

## On demand analysis

CX Insights uses analysis rules to determine which analyses to perform on the conversation, unless the user explicitly specifies the analysis types to use.

Note the following details for using analysis rules with an API.

  * [`CreateAnalysis` API](https://docs.cloud.google.com/gemini-enterprise-cx/insights/create-analyze-conversation-api) always analyzes the conversation when requested and disregards the percentage specified in the matching analysis rules.
  * [`BulkAnalyzeConversations` API](https://docs.cloud.google.com/gemini-enterprise-cx/insights/bulk-analyze-api) uses the percentage specified in the `BulkAnalyzeConversations` request over the one in the analysis rules.



## Automatic analysis

After you configure active analysis rules, the following changes occur:

  1. CX Insights matches conversations against all active analysis rules to decide what analysis to perform for the conversation.
  2. If a conversation does not fit any rules, then CX Insights does not automatically analyze the conversation.



CX Insights supports automatic analysis for conversations uploaded with the console or one of the following API methods:

  * [`UploadConversations` API](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations/upload)
  * [Dialogflow runtime Ingestion](https://docs.cloud.google.com/gemini-enterprise-cx/insights/dialogflow-runtime-integration) `AnalyzeContent` API
  * [`CreateAnalysis` API](https://docs.cloud.google.com/gemini-enterprise-cx/insights/create-analyze-conversation-api)



CX Insights does not support automatic analysis for conversations uploaded with the following methods:

  * [Dialogflow runtime ingestion](https://docs.cloud.google.com/gemini-enterprise-cx/insights/dialogflow-runtime-integration) `DetectIntent` API: This API does not have a notion of conversation completion, so CX Insights cannot determine when to analyze a conversation.
  * [`IngestConversations` API](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations/ingest): Also referred to as bulk upload.



To analyze these conversations, you can use the [`BulkAnalyzeConversations` API](https://docs.cloud.google.com/gemini-enterprise-cx/insights/bulk-analyze-api).

## Create a rule

When you create an analysis rule, you can use the following:

  * **Filters** : [Conversation filters](https://docs.cloud.google.com/gemini-enterprise-cx/insights/filtering) allow you to narrow down your conversation dataset and analyze a smaller number of related conversations. Analysis rules offer the ability to filter your conversation dataset before running any analyses. Crucially, the filtering criteria cannot depend on the analysis result. For example, a single conversation with a specific custom highlight cannot be a conversation filter.
  * **Conversation percentage** : With an analysis rule, you can also configure the percentage of conversations for CX Insights to automatically analyze. If an uploaded conversation passes a rule's filter, then CX Insights decides whether or not that conversation should be analyzed based on the percentage specified in the rule.



Follow these steps to create an analysis rule.

### Console

  1. Navigate to the CX Insights console, and sign in with your Google Account.

[CX Insights console](https://ccai.cloud.google.com/insights)

  2. Enter your project ID.

  3. Click settings > **Analysis rules** > **\+ Create**.

  4. Give the rule a name in **Rule Name**.

     * The name can contain a maximum of 100 characters.
  5. Keep the **Status** set to active.

  6. Select a conversation type from the **Filters** menu.

  7. For **Analysis percentage** , enter the percentage of your conversation dataset that you want CX Insights to analyze.

  8. Select the type of analysis you want to run for **Annotator selectors** and choose one of the required options. For additional details, see the following section.

  9. Click **Save**.




### API

Using the [`AnalysisRules` API](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.analysisRules), you can create an analysis rule with the `CreateAnalysisRule` command. You can define each aspect of a rule with parameter values. For example, you must give each rule a name using the `Display_name` parameter with a non-empty string value of less than 64 characters. You can also decide whether or not to use a rule for conversation analysis by setting the `Active` parameter with a boolean value.

The following code illustrates how to create a rule with `CreateAnalysisRule`:
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json; charset=utf-8" \
      -d "{ display_name: 'runtime' , conversation_filter: 'data_source.gcs_source: "*"', annotator_selector:{run_silence_annotator : true,  run_sentiment_annotator: true}, analysis_percentage:0.4, active:true}" \
      "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/analysisRules"
    

The following is an example JSON representation of an analysis rule:
    
    
    {
    "display_name": string , 
    "conversation_filter": string, 
    "annotator_selector": object (AnnotatorSelector), 
    "analysis_percentage": number, 
    "active": boolean
    }
    

### Filter conversations

Use the `Conversation_filter` parameter. The value must be an alphanumeric string. If the value is empty, the rule applies to all your conversations.

### Conversation percentage

Use the `Analysis_percentage` parameter. The value must be a number between 0 and 1, where 1 means 100%. You can only use this parameter in a rule to configure an automated analysis. In other words, this percentage does not apply to the `CreateAnalysis` or `BulkAnalysis` commands.

### Analysis types

Use the `Annotator_selector` parameter. The value must be an [`AnnotatorSelector`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.analyses#Analysis.AnnotatorSelector) object. This configuration specifies which annotators to run for a specific set of conversations. A valid active analysis rule must contain at least one enabled annotator.

You can also create multiple analysis rules in CX Insights. If a conversation matches multiple rules, CX Insights applies a combination of all the requirements specified in all the matching rules. However, if a conversation matches conflicting rules, CX Insights doesn't analyze that conversation.

### Analysis types

Customer Experience Insights offers a variety of analysis types to help you better understand your conversation data. With an analysis rule, you can apply different analysis types to each portion of your filtered or unfiltered conversation dataset.

CX Insights offers the following analysis types:

  * Custom and smart highlights
  * Entity extraction
  * Intent extraction
  * Interruptions
  * Sentiment
  * Silence
  * Quality AI
  * Summarization
  * Topic modeling



## Create a follow-up analysis

You can configure a follow-up analysis that depends on a previous analysis result. For example, if you have a separate rule that analyzes conversation group A, you can then analyze conversation group B based on one of the results from group A. The conversation percentage for a follow-up analysis is automatically set at 100%. Follow these steps to create a follow-up analysis.

  1. Navigate to the CX Insights console, and sign in with your Google Account.

[CX Insights console](https://ccai.cloud.google.com/insights)

  2. Enter your project ID.

  3. Click settings > **Analysis rules** > **\+ Create**.

  4. Give the rule a name in **Rule Name**.

     * The name can contain a maximum of 100 characters.
  5. Keep the **Status** set to active.

  6. For **Rule type** , choose **Follow-up analysis**.

  7. Enter a filter that uses previous analysis results.

  8. Select the type of analysis you want to run for **Annotator selectors** and choose one of the required options.

  9. Click **Save**.




## Additional operations

You can use the following additional API commands with analysis rules:

  * Find the rule used for a particular conversation with `GetAnalysisRule`.
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/analysisRules/ANALYSIS_RULE_ID"
        

  * List all of your rules with `ListAnalysisRules`.
        
        curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/analysisRules"
        

  * Edit a rule with `UpdateAnalysisRule`.
        
        curl -X PATCH \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        -d '{annotator_selector: {run_silence_annotator: true}}' \
        "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/analysisRules/ANALYSIS_RULE_ID?updateMask=annotator_selector"
        

  * Remove a rule with `DeleteAnalysisRule`.
        
        curl -X DELETE \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/analysisRules/ANALYSIS_RULE_ID"
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
