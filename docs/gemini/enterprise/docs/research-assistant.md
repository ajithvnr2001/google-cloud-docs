---
url: https://docs.cloud.google.com/gemini/enterprise/docs/research-assistant/
title: Get reports with Deep Research \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:42:39.531797+00:00
---

# Get reports with Deep Research  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/research-assistant/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Get reports with Deep Research Stay organized with collections  Save and categorize content based on your preferences. 

Deep Research is a Made by Google agent for users who need to gather, analyze, and understand internal and external information.

**Note:** Made by Google agents aren't available in the Gemini Enterprise Frontline edition.

## Overview

When you enter a prompt to Deep Research, such as "Compare Example Project competitors", Deep Research assesses whether the question is research related, generates a plan outlining the steps it takes to do the research, and streams questions and answers as it progresses in its research. It then generates a report of its findings with citations as well as an audio summary.

For research sources, Deep Research uses data that the app indexes. It can also use web results if web search is enabled for the app.

Here are some example prompts that Deep Research generates reports for:

  * How can we improve the user experience of our existing mobile banking app to make it more intuitive and user-friendly?
  * How can we reduce customer wait times during peak hours without compromising on the quality of support?
  * Analyze the economic situation of Central European countries.
  * Compare BigQuery with its competitors, and provide the results in table format.



## Use Deep Research

Your end users can access and use Deep Research through the app. Deep Research has access to data that the app has already indexed and, if enabled, web results.

You can get results from Deep Research from the app or using the API (Generally available with an allowlist).

### Console

To use Deep Research in the app, do the following:

  1. In the app navigation menu, go to **Deep Research**.

  2. Click **Sources** to select the sources that the agent must include to provide the most relevant data insights.

In the sources, in addition to your Gemini Enterprise sources, you can also choose to include Google Search results.

  3. Enter a prompt to Deep Research and click **Submit**. If the prompt isn't research-related, Deep Research generates an answer. If the prompt is determined to be research-related, then Deep Research outlines the topics that the agent plans to research in a research plan.

  4. Edit the agent's prompt, if necessary, to generate a new research plan that better suits your requirements.

  5. If the research plan is acceptable to you, click **Start Research**.

The agent starts researching based on the plan:

     * Streams the topics that it's researching as it progresses
     * Generates a report of findings with citations
     * Creates a 1-2 minute audio summary of the report



### REST

**Note:** Deep research using the API is Generally available with allowlist. You must be on the allowlist to work with this agent using the API.

To use Deep Research using the API, do the following:

  1. Send a request to the [`streamAssist`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistants/streamAssist) method.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/project_id/locations/global/collections/default_collection/engines/app_id/assistants/default_assistant:streamAssist" \
         -d '{
              "query": {
                "text": "QUERY"
              },
              "agentsSpec": {
                "agentSpecs": {
                  "agentId": "deep_research"
                }
              },
              "toolsSpec": {
                "vertexAiSearchSpec": {
                  "dataStoreSpecs": {
                    "dataStore": "projects/PROJECT_ID/locations/global/collections/default_collection/datastores/DATA_STORE_ID"
                  }
                },
                "webGroundingSpec": {}
              }
             }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `APP_ID`: the ID of the app.
     * `QUERY`: the query.
     * `DATA_STORE_ID`: the ID of the data store when an app has multiple data stores. When you specify this, the search is limited to the documents in the specified data store.

#### Response

If your request is successful, you receive a JSON response similar to the following response. Note the SESSION_ID. This is required to initiate the research process in the next step.
    
    [{
     "answer": {
       "name": "ANSWER_ASSIST_NAME",
       "state": "SUCCEEDED",
       "replies": [
         {
           "groundedContent": {
             "content": {
               "role": "model",
               "text": "INLINE_TEXT"
             }
           },
         },
         {
           "groundedContent": {
             "content": {
               "role": "model",
               "text": "INLINE_TEXT_WITH_RESEARCH_PLAN"
             },
             "contentMetadata": {
               "contentKind": "RESEARCH_PLAN"
             }
           },
         }
       ],
     },
     "sessionInfo": {
       "session": "SESSION_ID",
       "queryId": "QUERY_ID",
       "turnId": "TURN_ID"
     },
     "assistToken": "ASSIST_TOKEN"
    }
    ]
    

  2. Initiate the research for the query in the previous step. To do so, send another request to the [`streamAssist`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistants/streamAssist) method. In this request, set your query as `Start Research` and add the session information from the previous step.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/project_id/locations/global/collections/default_collection/engines/app_id/assistants/default_assistant:streamAssist" \
         -d '{
              "query": {
                "text": "Start Research"
              },
              "session": "SESSION_ID",
              "agentsSpec": {
                "agentSpecs": {
                  "agentId": "deep_research"
                }
              },
              "toolsSpec": {
                "vertexAiSearchSpec": {
                  "dataStoreSpecs": {
                    "dataStore": "projects/PROJECT_ID/locations/global/collections/default_collection/datastores/DATA_STORE_ID"
                  }
                },
                "webGroundingSpec": {}
              },
             }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `APP_ID`: the ID of the app.
     * `SESSION_ID`: the session ID from the previous step.
     * `DATA_STORE_ID`: the ID of the data store when an app has multiple data stores. When you specify this, the search is limited to the documents in the specified data store.

#### Response

If your request is successful, you receive a JSON response similar to the following truncated response.

The response contains an instance of the [`AssistAnswer`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.sessions.assistAnswers) resource.

This is a streaming response and, therefore, depending on the amount of data in the research response, it can take some time to fully stream it.
    
    [{
     "answer": {
       "state": "IN_PROGRESS",
       "replies": [
         {
           "groundedContent": {
             "content": {
               "role": "model",
               "text": "RESEARCH_QUESTION_1"
             },
             "contentMetadata": {
               "contentKind": "RESEARCH_QUESTION",
               "contentId": "ID0"
             }
           },
         }
       ]
     },
     "assistToken": "ASSIST_TOKEN"
    },
    {
     "answer": {
       "state": "IN_PROGRESS",
       "replies": [
         {
           "groundedContent": {
             "content": {
               "role": "model",
               "text": "RESEARCH_ANSWER_1_PART_1"
             },
             "contentMetadata": {
               "contentKind": "RESEARCH_ANSWER",
               "contentId": "ID0"
             }
           },
         }
       ]
     },
     "assistToken": "ASSIST_TOKEN"
    },
    {
     "answer": {
       "state": "IN_PROGRESS",
       "replies": [
         {
           "groundedContent": {
             "content": {
               "role": "model",
               "text": "RESEARCH_ANSWER_1_PART_2"
             },
             "contentMetadata": {
               "contentKind": "RESEARCH_ANSWER",
               "contentId": "ID0"
             }
           },
         }
       ]
     },
     "assistToken": "ASSIST_TOKEN"
    },
    {
     "answer": {
       "state": "IN_PROGRESS",
       "replies": [
         {
           "groundedContent": {
             "content": {
               "role": "model",
               "text": "INLINE_TEXT"
             },
             "textGroundingMetadata": {
               "references": [
                 {
                   "documentMetadata": {
                     "document": "DOCUMENT_ID",
                     "uri": "DOCUMENT_REDIRECT_URI",
                     "title": "DOCUMENT_TITLE",
                     "pageIdentifier": "",
                     "domain": "DOCUMENT_DOMAIN"
                   }
                 }
               ]
               "searchEntryPoints": [
                 {
                   "renderedContent": "GROUNDING_SEARCH_ENTRY_POINT"
                 }
               ]
              }
            }
          }
        ]
      }
    },
    {
     "answer": {
       "state": "IN_PROGRESS",
       "replies": [
         {
           "groundedContent": {
             "content": {
               "role": "model",
               "file": {
                 "fileId": "AUDIO_FILE_ID"
               }
             },
             "contentMetadata": {
               "contentKind": "RESEARCH_AUDIO_SUMMARY"
             }
           },
         }
       ]
     },
     "assistToken": "ASSIST_TOKEN"
    }
    {
     "answer": {
       "name": "ANSWER_ASSIST_NAME",
       "state": "SUCCEEDED"
       },
     "sessionInfo": {
       "session": "SESSION_ID",
       "queryId": "QUERY_ID",
       "turnId": "TURN_ID"
     },
    "assistToken": "ASSIST_TOKEN"
    }]
    




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
