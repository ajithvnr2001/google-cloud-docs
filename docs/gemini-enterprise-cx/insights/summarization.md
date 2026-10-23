---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/summarization/
title: Enable summarization \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:55.447392+00:00
---

# Enable summarization  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/summarization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Enable summarization Stay organized with collections  Save and categorize content based on your preferences. 

The summarization annotator returns summaries of your Customer Experience Insights conversations. Summarization is an Agent Assist feature that can be used with CX Insights only or in conjunction with your pre-existing Agent Assist conversation profiles. This page shows you how to enable the summarization annotator.

## Billing

Customer Experience Insights uses [Agent Assist](https://docs.cloud.google.com/agent-assist) to generate conversation summaries. When you implement summarization for Customer Experience Insights analyses, you will see an additional line item on your bill for Agent Assist API usage. See the Agent Assist [pricing](https://cloud.google.com/agent-assist/pricing) page for details.

## AnnotatorSelector

Unlike other analysis annotators, the summarization annotator is disabled by default. Enable it by setting `AnnotatorSelector.run_summarization_annotator` to `true`.

If `AnnotatorSelector` is specified in your requests, CX Insights runs explicitly enabled annotators. To run annotators other than summarization, enable the annotators in your request. For available options, see [AnnotatorSelector](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.analyses#annotatorselector).

## Prerequisites

Enable the [**Dialogflow API** and **Customer Experience Insights API**](https://docs.cloud.google.com/gemini-enterprise-cx/insights/before-you-begin) for your Google Cloud project.

## Summarize conversations using CX Insights analysis

You can generate a summary of a CX Insights conversation by creating an analysis for that conversation. For details, see [Create and analyze a conversation using the API](https://docs.cloud.google.com/gemini-enterprise-cx/insights/create-analyze-conversation-api). When you create an analysis, summarization is enabled and configured using the [annotator selector](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations.analyses#annotatorselector).

Refer to the Agent Assist [language support documentation](https://docs.cloud.google.com/agent-assist/docs/languages) for a list of supported languages for each summarization model.

### Use a generator summarization model

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenterinsights.analyses.create`



Agent Assist also offers LLM-powered [summarization with custom sections](https://docs.cloud.google.com/agent-assist/docs/summarization-with-custom-sections) with the generator model. You can use a generator model with predefined sections, or you can define custom sections.

Follow these steps to automatically generate summaries using the LLM-powered generator model.

  1. Follow the Agent Assist instructions to [create a summarization generator](https://docs.cloud.google.com/agent-assist/docs/summarization-with-custom-sections#create_a_summarization_generator)
  2. Set `run_summarization_annotator` to `true`.
  3. Set `summarization_config` to `generator`.



For example:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        -d '{annotator_selector: {run_summarization_annotator: true, summarization_config: {generator: '"projects/PROJECT_ID/locations/global/generators/generator_id"}}}' \
        "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/conversations/CONVERSATION_ID/
    

### View summarization results

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenterinsights.conversations.get`



Creating the analysis returns an operation ID. [Poll the operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/create-analyze-conversation-api#poll_the_operation) to track its progress. After the analysis is complete, query the conversation to see the analysis results.
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/conversations/CONVERSATION_ID"
    

Summary data is populated in the response.

  * The summary is stored as a `runtimeAnnotation` with the `conversationSummarizationSuggestion` field populated.
  * The conversation `latestSummary` field is populated.



Subsequent analyses add new runtime annotations, and the latest summary is overwritten.
    
    
    {
      "name": "projects/694347961123/locations/us-east1/conversations/14849016801257151776",
      "createTime": "2023-03-07T23:00:00.243902Z",
      "updateTime": "2023-03-07T23:00:01.167050Z",
      …
      "runtimeAnnotations": [
        {
          "annotationId": "14849016801257150641",
          "createTime": "2023-03-07T23:00:01.167050Z",
          "conversationSummarizationSuggestion": {
            "text": "A summary of your conversation."
            "textSections": {
              "DEFAULT_SECTION": "A summary of your conversation."
            }
          }
        }
      ],
      "latestSummary": {
        "text": "A summary of your conversation."
        "textSections": {
          "DEFAULT_SECTION": "A summary of your conversation."
        }
      }
    }
    

## Summarize conversations by default

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `contactcenterinsights.settings.update`



Rather than specifying a summarization configuration every time you create an analysis, you can configure a default annotator selector in your project settings. The configuration you set is used for every analysis unless that analysis contains its own annotator selector. Be aware that each analysis incurs an additional charge.
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json; charset=utf-8" \
      -d '{analysis_config: {annotator_selector: {run_summarization_annotator: true}}}' \
      "https://contactcenterinsights.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/settings?updateMask=analysis_config"
    

## Dialogflow runtime integration

If you [enable Dialogflow runtime integration](https://docs.cloud.google.com/gemini-enterprise-cx/insights/enable-dialogflow-runtime-integration), any summaries created by Agent Assist can be viewed in CX Insights as well. As with other CX Insights summaries, summary content is available as a runtime annotation and in the latest summary field.
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION_ID/conversations/CONVERSATION_ID",
      "dataSource": {
        "dialogflowSource": {
          "dialogflowConversation": "projects/PROJECT_ID/locations/us/conversations/CONVERSATION_ID",
          "conversationDataItem": "projects/PROJECT_ID/locations/us/conversationDatasets/DATASET_ID/conversationDataItems/DATA_ITEM_ID"
        }
      },
      …
      "runtimeAnnotations": [
        {
          "annotationId": "projects/PROJECT_ID/locations/us/conversationDatasets/DATASET_ID/conversationDataItems/DATA_ITEM_ID/conversationAnnotations/ANNOTATION_ID",
          "createTime": "2023-03-20T19:49:01.929940Z",
          "startBoundary": {},
          "endBoundary": {
            "transcriptIndex": 1
          },
          "answerFeedback": {},
          "conversationSummarizationSuggestion": {
            "text": "The customer had a query about the service. Closed conversation prior to the resolution.",
            "textSections": {
              "DEFAULT_SECTION": "The customer had a query about the service. Closed conversation prior to the resolution."
            }
          }
        }
      ],
      "latestSummary": {
        "text": "The customer had a query about the service. Closed conversation prior to the resolution.",
        "textSections": {
          "DEFAULT_SECTION": "The customer had a query about the service. Closed conversation prior to the resolution."
        }
      }
    }
    

## Filter conversations by summary content

When you list conversations in CX Insights, you can filter them by summary content. See [list conversations](https://docs.cloud.google.com/gemini-enterprise-cx/insights/list-conversations-api) for general instructions.

CX Insights supports the following filters for summary content:

  * **With a summary** : `latest_summary:"*"`
  * **No summary** : `-latest_summary:"*"`
  * **With a summary that has a phrase** : `latest_summary.text:"match this text"`
  * **With a summary with no phrase** : `-latest_summary.text:"must not match this text"`



## View summaries in BigQuery

When you export your CX Insights data to BigQuery, summary data is also exported. For instructions on how to configure a BigQuery export, see [Export conversations to BigQuery](https://docs.cloud.google.com/gemini-enterprise-cx/insights/export).

Each conversation's latest summary is available in the `latest_summary` field:
    
    
    bq query --use_legacy_sql=false 'SELECT conversationName, latestSummary.text FROM DATASET.TABLE'
    

All summaries, including the latest and any past summaries, are available as sentence-level annotations:
    
    
    bq query --use_legacy_sql=false <<EOF
    SELECT
      conversationName,
      sen.sentence,
      JSON_QUERY(JSON_VALUE(ant.annotationRecord), '$.text') AS summary_text
    FROM
      DATASET.TABLE,
      UNNEST(`sentences`) AS sen,
      UNNEST(`sen.annotations`) AS ant
    WHERE ant.type = 'CONVERSATION_SUMMARIZATION_SUGGESTION'
    EOF
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
