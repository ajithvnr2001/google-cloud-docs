---
url: https://docs.cloud.google.com/agent-assist/docs/troubleshoot-ka/
title: Troubleshoot knowledge assist features \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:10:09.653024+00:00
---

# Troubleshoot knowledge assist features  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-assist/docs/troubleshoot-ka/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Troubleshoot knowledge assist features Stay organized with collections  Save and categorize content based on your preferences. 

Access detailed information regarding failures, feature usage behavior, and latency for both Generative knowledge assist (GKA) and Proactive generative knowledge assist (PGKA). Enable `enable_response_debug_info` to view these troubleshooting details within the `knowledge_assist_debug_info` object.

## Configure a conversation profile for troubleshooting

To access troubleshooting information for both GKA and PGKA, you must turn on the `enable_response_debug_info` field in the conversation profile. If this field is off, knowledge search gives you a `NotFound` error when a query yields no results and knowledge assist gives you an empty message. Turn on `enable_response_debug_info` to provide an `OK` response with details about the lack of results. This modification affects the API and existing integrations.

## Generative knowledge assist (GKA)

To get detailed troubleshooting information for your GKA queries, you must enable it in your conversation profile. When creating or updating a conversation profile, set the `enable_response_debug_info` field to `true` within the `human_agent_assistant_config`, as follows.
    
    
    parent:"projects/PROJECT_ID/locations/LOCATION-ID"
    conversation_profile {
      display_name: "DISPLAY-NAME"
      human_agent_assistant_config {
        human_agent_suggestion_config {
          feature_configs {
            suggestion_feature {
              type: KNOWLEDGE_SEARCH
            }
            query_config {
              dialogflow_query_source {
                human_agent_side_config {
                  agent: "projects/PROJECT_ID/locations/LOCATION-NAME/agents/AGENT-ID"
                }
              }
            }
            enable_response_debug_info: true
          }
        }
      }
    }
    

With the `enable_response_debug_info` field enabled, the generator returns the `knowledge_search_debug_info` object as part of the `SearchKnowledgeResponse` along with the generated answers. This information provides valuable insights into the performance and behavior of the knowledge search.

### Troubleshooting for PGKA V2

With the enabled `enable_response_debug_info field`, the `KnowledgeAssistDebugInfo` object includes several new fields specific for PGKA V2. To access this, `baseline_model_version` and `enable_response_debug_info` need to be set to 2.0. Following is the example of setup to access troubleshooting information in PGKA V2:
    
    
      "name": "projects/PROJECT_ID/locations/LOCATION/conversationProfiles/PROFILE_ID",
      "human_agent_assistant_config": {
        "human_agent_suggestion_config": {
          "feature_configs": [
            {
              "suggestion_feature": {
                "type": "KNOWLEDGE_ASSIST"
              },
              "query_config": {
                "dialogflow_query_source": {
                  "agent": "projects/PROJECT_ID/locations/LOCATION/agents/AGENT_ID"
                }
              },
              "conversation_model_config": {
                "baseline_model_version": "2.0"
              },
              "disable_query_search_context": true,
              "enable_response_debug_info": true,
                "suggestion_trigger_event": "END_OF_UTTERANCE",
            }
          ]
        }
      }
    

### Troubleshooting details

The `search_knowledge_debug_info` object contains several key pieces of information to help you troubleshoot and understand the search process for GKA.

#### Search failure or unhelpful answer

The `datastore_response_reason` field gives you a high-level status about the data serving or answer quality. It helps you quickly identify why a search might have failed or why the answer quality might be degraded.

Possible values include:

  * **`NONE`** : The request was processed without any specific issues to report.
  * **`SEARCH_OUT_OF_QUOTA`** : The search operation was blocked due to exceeding usage quota.
  * **`SEARCH_EMPTY_RESULTS`** : The search returned no documents from your Datastore.
  * **`ANSWER_GENERATION_GEN_AI_DISABLED`** : Generative AI features are disabled for your project.
  * **`ANSWER_GENERATION_OUT_OF_QUOTA`** : Answer generation was blocked due to exceeding usage quota. 
  * **`ANSWER_GENERATION_ERROR`** : An internal error occurred during answer generation.
  * **`ANSWER_GENERATION_NOT_ENOUGH_INFO`** : The retrieved documents lacked sufficient information to generate an answer.
  * **`ANSWER_GENERATION_RAI_FAILED`** : The generated answer was blocked by Responsible AI (RAI) filters.
  * **`ANSWER_GENERATION_NOT_GROUNDED`** : The grounding verification step determined the generated answer wasn't factually supported by the source documents and was therefore discarded.



### Active behaviors

The `search_knowledge_behavior` object tells you which specific behaviors were active during the GKA request.

  * **`answer_generation_rewriter_on`** : A `true` value indicates that the system rewrote the user's query to be more effective for searching the Datastore. A `false` value indicates that the generator didn't rewrite your query.
  * **`end_user_metadata_included`** : A `true` value indicates that `end_user_metadata` was passed along in the call to the data store agent. A `false` value indicates that `end_user_metadata` wasn't passed along to the data store agent.



### Troubleshooting information from ingested context

The `ingested_context_reference_debug_info` field provides troubleshooting information related to context that was ingested to aid the search.

  * **`project_not_allowlisted`** : A `true` value means the project isn't on the allowlist to use the ingested context reference feature. A `false` value means the project is on the allowlist.
  * **`context_reference_retrieved`** : Indicates whether the context reference was successfully retrieved from the database.
  * **`ingested_parameters_debug_info`** : A list of parameters ingested from the context reference and their status. For each parameter, you see a parameter name and one of the following ingestion statuses. 
    * `INGESTION_STATUS_SUCCEEDED`: The parameter was successfully ingested.
    * `INGESTION_STATUS_CONTEXT_NOT_AVAILABLE`: The parameter wasn't available for ingestion.
    * `INGESTION_STATUS_PARSE_FAILED`: The system failed to parse the parameter's content.
    * `INGESTION_STATUS_INVALID_ENTRY`: The context reference had an unexpected number of content entries (it should only have one).
    * `INGESTION_STATUS_INVALID_FORMAT`: The context content wasn't in the expected format (e.g., JSON).
    * `INGESTION_STATUS_LANGUAGE_MISMATCH`: The language of the context reference didn't match the conversation's language.



### Latency

  * The `service_latency` object breaks down the time spent in various internal services, helping you pinpoint performance bottlenecks.

  * **`internal_service_latencies`** : A list containing latency details for each internal step of the process. Each entry includes a name (`step`), amount of time it takes in milliseconds (`latency_ms`) and the start (`start_time`) and end (`complete_time`) time. Possible names for an internal process step are the following:

    * **`total_data_store_agent`** : Measures the total time taken to process the entire GKA request, from receiving the query to returning a final answer. It acts as an umbrella timer for all datastore search steps for agents.
    * **`query_rewrite`** : The time spent rewriting the user's initial query to be more effective for searching your knowledge documents.
    * **`search_query`** : The time taken by the data store agent to execute the search against your configured data stores, using the (potentially rewritten) query.
    * **`summarization`** : The time spent generating a concise, natural language answer from the search results retrieved from the Datastore (ReAct turn).
    * **`grounding`** : The time spent on the grounding verification process. This crucial step checks if the generated answer is factually supported by the source documents before it's returned.
    * **`query_generation`** : The time spent analyzing the ongoing conversation and proactively generating a relevant search query.
    * **`generated_query_rai`** : The time taken to perform a Responsible AI (RAI) safety check on the proactively generated query before it is used for a search.
    * **`query_categorization`** : The time spent categorizing the generated query using Agent Search, if this feature is configured.



### Example troubleshooting information response

The following is a comprehensive example of what the `search_knowledge_debug_info` object might look like in a JSON response. 

**Note:** The API omits fields set to their default value from a response, but you see them in the following examples for illustrative purposes only. For example, you wouldn't see `"project_not_allowlisted": false` in a real response, because false is the default.
    
    
    {
      "search_knowledge_debug_info": {
        "datastore_response_reason": "ANSWER_GENERATION_NOT_ENOUGH_INFO",
        "search_knowledge_behavior": {
          "answer_generation_rewriter_on": true,
          "end_user_metadata_included": true
        },
        "ingested_context_reference_debug_info": {
          "project_not_allowlisted": false,
          "context_reference_retrieved": true,
          "ingested_parameters_debug_info": [
            {
              "parameter": "order_id",
              "ingestion_status": "INGESTION_STATUS_SUCCEEDED"
            },
            {
              "parameter": "user_profile",
              "ingestion_status": "INGESTION_STATUS_INVALID_FORMAT"
            },
            {
              "parameter": "product_sku",
              "ingestion_status": "INGESTION_STATUS_CONTEXT_NOT_AVAILABLE"
            }
          ]
        },
        "service_latency": {
          "internal_service_latencies": [
            {
              "step": "total_data_store_agent",
              "latency_ms": 4125.781,
              "start_time": {
                "seconds": 1750969252,
                "nanos": 550649603
              },
              "complete_time": {
                "seconds": 1750969256,
                "nanos": 676430603
              }
            },
            {
              "step": "query_rewrite",
              "latency_ms": 412.0,
              "start_time": {
                "seconds": 1750969252,
                "nanos": 780119421
              },
              "complete_time": {
                "seconds": 1750969253,
                "nanos": 192119421
              }
            },
            {
              "step": "search_query",
              "latency_ms": 950.0,
              "start_time": {
                "seconds": 1750969253,
                "nanos": 192119421
              },
              "complete_time": {
                "seconds": 1750969254,
                "nanos": 142119421
              }
            },
            {
              "step": "summarization",
              "latency_ms": 721.0,
              "start_time": {
                "seconds": 1750969254,
                "nanos": 142119421
              },
              "complete_time": {
                "seconds": 1750969254,
                "nanos": 863119421
              }
            },
            {
                "step": "grounding",
                "latency_ms": 155.0,
                "start_time": {
                  "seconds": 1750969254,
                  "nanos": 863119421
                },
                "complete_time": {
                  "seconds": 1750969255,
                  "nanos": 18119421
                }
            }
          ]
        }
      }
    }
    

## Proactive generative knowledge assist (PGKA)

Troubleshooting provides deep insights into the query generation, categorization, and answer-retrieval processes. The `knowledge_assist_debug_info` object is part of the `knowledge_assist_answer` within your suggestion results.

When you create or update a conversation profile, set the `enable_response_debug_info` field to `true` for the `KNOWLEDGE_ASSIST` feature, as follows.
    
    
    parent: "projects/PROJECT_ID/locations/LOCATION-ID"
    conversation_profile {
      display_name: "DISPLAY-NAME"
      human_agent_assistant_config {
        human_agent_suggestion_config {
          feature_configs {
            suggestion_feature {
              type: KNOWLEDGE_ASSIST
            }
            query_config {
              dialogflow_query_source {
                agent: "projects/PROJECT_ID/locations/LOCATION-ID/agents/DATASTORE-AGENT-ID"
              }
            }
            enable_response_debug_info: true
          }
        }
      }
    }
    
    

### Troubleshooting details

The `knowledge_assist_debug_info` object contains the following fields to help you understand the end-to-end lifecycle of a proactive suggestion.

#### Failed to generate a query

The `query_generation_failure_reason` field explains why a conversation might not have generated a proactive search query.

  * **`QUERY_GENERATION_FAILED`** : An internal error occurred during query generation.
  * **`QUERY_GENERATION_NO_QUERY_GENERATED`** : The generator decided not to generate a query. This usually happens when the conversation topic hasn't changed or a similar query was recently suggested.
  * **`QUERY_GENERATION_RAI_FAILED`** : Responsible AI (RAI) filters blocked a potential query for safety reasons.
  * **`NOT_IN_ALLOWLIST`** : Filtering rules at the conversation profile or agent level blocked query generation.
  * **`QUERY_GENERATION_QUERY_REDACTED`** : The generator blocked the generated query because it contained sensitive information that was redacted.
  * **`QUERY_GENERATION_AGENT_LANGUAGE_MISMATCH`** : Query generation failed because the agent's language doesn't match the customer's language.
  * **`QUERY_GENERATION_TRANSLATION_LANGUAGE_MISMATCH`** : Query generation failed because the translated message's language doesn't match the conversation profile's language.
  * **`QUERY_GENERATION_TRANSLATED_MESSAGE_NOT_FOUND`** : The generator expected a translated message for query generation but didn't find one.
  * **`QUERY_GENERATION_EMPTY_CONVERSATION`** : The conversation has no messages. This is only available for PGKA V2.
  * **`QUERY_GENERATION_EMPTY_LAST_MESSAGE`** : The last message was empty or whitespace. This is only available for PGKA V2.
  * **`QUERY_GENERATION_TRIGGERING_EVENT_CONDITION_NOT_MET`** : The trigger event configuration (e.g. `AGENT_MESSAGE`) didn't match the role of the last message sender. This is only available for PGKA V2.
  * **`QUERY_GENERATION_LLM_RESPONSE_PARSE_FAILED`** : The system couldn't parse the structured JSON output from the model. This is only available for PGKA V2.



#### Failed to categorize a query

The `query_categorization_failure_reason` field explains why query categorization might have failed.

  * **`QUERY_CATEGORIZATION_INVALID_CONFIG`** : The Agent Search configuration provided for categorization is invalid, for example the search engine is empty.
  * **`QUERY_CATEGORIZATION_RESULT_NOT_FOUND`** : The result from Agent Search didn't include a categorization result.
  * **`QUERY_CATEGORIZATION_FAILED`** : The call to Agent Search for categorization failed.



#### Datastore search status

The `datastore_response_reason` field provides the status of the search against your Datastore after a query is generated.

  * **`NONE`** : Datastore processed the request without any specific issues to report.
  * **`SEARCH_OUT_OF_QUOTA`** : Agent Assist blocked the search operation due to exceeding the usage quota.
  * **`SEARCH_EMPTY_RESULTS`** : The search returned no documents from your Datastore.
  * **`ANSWER_GENERATION_GEN_AI_DISABLED`** : Generative AI features are disabled for your project.
  * **`ANSWER_GENERATION_OUT_OF_QUOTA`** : Agent Assist blocked answer generation due to exceeding the usage quota. 
  * **`ANSWER_GENERATION_ERROR`** : An internal error occurred during answer generation.
  * **`ANSWER_GENERATION_NOT_ENOUGH_INFO`** : The retrieved documents lacked sufficient information to generate an answer.
  * **`ANSWER_GENERATION_RAI_FAILED`** : RAI filters blocked the generated answer.
  * **`ANSWER_GENERATION_NOT_GROUNDED`** : The grounding verification step determined source documents didn't factually support the generated answer, so the answer was discarded.



#### Active configurations

The `knowledge_assist_behavior` object tells you which specific configurations were active for the request.

  * **`answer_generation_rewriter_on`** : `true` if the generator rewrote the query for better search results and `false` if it didn't.
  * **`end_user_metadata_included`** : `true` if the generator passed `end_user_metadata` to the Datastore and `false` if it didn't.
  * **`return_query_only`** : `true` if your profile is configured to only return the generated search query and `false` if your profile returns the full answer.
  * **`use_pubsub_delivery`** : `true` if your generator is configured to deliver results with Pub/Sub and `false` if not.
  * **`disable_sync_delivery`** : `true` if synchronous delivery of the response is disabled and `false` if synchronous response delivery is enabled.
  * **`previous_queries_included`** : `true` if the generator considered previously suggested queries during the query generation process and `false` if it didn't.
  * **`use_translated_message`** : `true` if a translated message was used for query generation and `false` if it wasn't.
  * **`use_custom_safety_filter_level`** : `true` if a custom safety filter level was applied. `false` if the generator used only the default safety filter levels.
  * **`multiple_queries_generated`** : A `true` value indicates that the model produced more than one query. This is available for PGKA V2.
  * **`query_contained_search_context`** : A `true` value indicates that the generated query included a search context. This is available for PGKA V2.
  * **`appended_search_context_count`** : This indicates the number of context items (e.g., "product", "OS") successfully used in the search. This is available for PGKA V2.



#### Information from ingested context

The `ingested_context_reference_debug_info` field provides debug information related to context that was ingested to aid the search.

  * **`project_not_allowlisted`** : A `true` value means the project isn't on the allowlist to use the ingested context reference feature. A `false` value means the project is on the allowlist.
  * **`context_reference_retrieved`** : Indicates whether the context reference was successfully retrieved from the database.
  * **`ingested_parameters_debug_info`** : A list of parameters ingested from the context reference and their status. For each parameter, you see a parameter name and one of the following possible ingestion statuses. 
    * `INGESTION_STATUS_SUCCEEDED`: The parameter was successfully ingested.
    * `INGESTION_STATUS_CONTEXT_NOT_AVAILABLE`: The parameter wasn't available for ingestion.
    * `INGESTION_STATUS_PARSE_FAILED`: The system failed to parse the parameter's content.
    * `INGESTION_STATUS_INVALID_ENTRY`: The context reference had an unexpected number of content entries (it should only have one).
    * `INGESTION_STATUS_INVALID_FORMAT`: The context content wasn't in the expected format.
    * `INGESTION_STATUS_LANGUAGE_MISMATCH`: The language of the context reference didn't match the conversation's language.



### Example troubleshooting response for PGKA V1

The following is a comprehensive example of what the `knowledge_assist_debug_info` object might look like in a response. 

**Note:** The API omits fields set to their default value from a response. These are included in the following examples for illustrative purposes only. For example, you wouldn't see `"return_query_only": false` in an API response, because `false` is the default.
    
    
    {
      "knowledge_assist_debug_info": {
        "query_generation_failure_reason": "QUERY_GENERATION_NO_QUERY_GENERATED",
        "query_categorization_failure_reason": "QUERY_CATEGORIZATION_FAILURE_REASON_UNSPECIFIED",
        "datastore_response_reason": "SEARCH_EMPTY_RESULTS",
        "knowledge_assist_behavior": {
          "answer_generation_rewriter_on": true,
          "end_user_metadata_included": false,
          "return_query_only": false,
          "use_pubsub_delivery": true,
          "disable_sync_delivery": true,
          "previous_queries_included": true,
          "use_translated_message": false,
          "use_custom_safety_filter_level": false
        },
        "ingested_context_reference_debug_info": {
          "project_not_allowlisted": false,
          "context_reference_retrieved": true,
          "ingested_parameters_debug_info": [
            {
              "parameter": "session_id",
              "ingestion_status": "INGESTION_STATUS_SUCCEEDED"
            }
          ]
        },
        "service_latency": {
          "internal_service_latencies": [
            {
              "step": "query_generation",
              "latency_ms": 680.5,
              "start_time": {
                "seconds": 1753123456,
                "nanos": 110220330
              },
              "complete_time": {
                "seconds": 1753123456,
                "nanos": 790720330
              }
            },
            {
              "step": "search_query",
              "latency_ms": 1050.1,
              "start_time": {
                "seconds": 1753123456,
                "nanos": 790720330
              },
              "complete_time": {
                "seconds": 1753123457,
                "nanos": 840820330
              }
            }
          ]
        }
      }
    }
    
    

### Example troubleshooting response for PGKA V2

The following are comprehensive examples for two scenarios.

#### Example 1: Successful suggestion with behavior flags

This scenario illustrates a response the model successfully generated multiple queries and enriched the primary query with search context. Following are the field explanations:

  * **`multiple_queries_generated`** : Indicates the model produced more than one relevant topic.
  * **`query_contained_search_context`** : Confirms the primary query was enriched with structured data.
  * **`appended_search_context_count`** : The exact number of key-value pairs (e.g., application name, OS) used to refine the search.


    
    
    {
      "message": {
        "name": "projects/PROJECT_ID/locations/LOCATION/conversations/CONVERSATION_ID/messages/MESSAGE_ID",
        "content": "My DesignApp is crashing on Mac. Also, how do I resolve the storage limit error?",
        "participant_role": "END_USER"
      },
      "human_agent_suggestion_results": [
        {
          "suggest_knowledge_assist_response": {
            "knowledge_assist_answer": {
              "suggested_query": {
                "query_text": "Troubleshoot application crashing",
                "search_contexts": [
                  { "key": "application name", "value": "DesignApp" },
                  { "key": "operating system", "value": "Mac" }
                ]
              },
              "suggested_query_answer": {
                "answer_text": "To troubleshoot the crash on Mac, ensure..."
              },
              "answer_record": "projects/PROJECT_ID/locations/LOCATION/answerRecords/ANSWER_RECORD_ID",
              "knowledge_assist_debug_info": {
                "knowledge_assist_behavior": {
                  "multiple_queries_generated": true,
                  "query_contained_search_context": true,
                  "appended_search_context_count": 2
                }
              }
            },
            "latest_message": "projects/PROJECT_ID/locations/LOCATION/conversations/CONVERSATION_ID/messages/MESSAGE_ID",
            "context_size": 20,
            "additional_suggested_query_results": [
              {
                "suggested_query": {
                  "query_text": "Resolve storage limit exceeded error",
                  "search_contexts": [
                    { "key": "storage plan", "value": "1TB" }
                  ]
                }
              }
            ]
          }
        }
      ]
    }
    

#### Example 2: Skipped suggestion with failure reason

In this scenario, the system determined that a suggestion shouldn't be triggered because the event condition wasn't met (e.g., the trigger was set to `AGENT_MESSAGE` but the last message was from the `END_USER`). Instead of an error, the system returns a successful status with the specific reason.
    
    
    {
      "message": {
        "name": "projects/PROJECT_ID/locations/LOCATION/conversations/CONVERSATION_ID/messages/MESSAGE_ID",
        "content": "I am having trouble with my account.",
        "participant_role": "END_USER"
      },
      "human_agent_suggestion_results": [
        {
          "suggest_knowledge_assist_response": {
            "knowledge_assist_answer": {
              "knowledge_assist_debug_info": {
                "query_generation_failure_reason": "QUERY_GENERATION_TRIGGERING_EVENT_CONDITION_NOT_MET"
              }
            },
            "latest_message": "projects/PROJECT_ID/locations/LOCATION/conversations/CONVERSATION_ID/messages/MESSAGE_ID",
            "context_size": 20
          }
        }
      ]
    }
    

Other common failure reasons include:

  * **`QUERY_GENERATION_EMPTY_CONVERSATION`** : Found no messages in conversation.
  * **`QUERY_GENERATION_EMPTY_LAST_MESSAGE`** : The last message was empty or only whitespace.
  * **`QUERY_GENERATION_LLM_RESPONSE_PARSE_FAILED`** : The system couldn't parse the structured output from the LLM.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
