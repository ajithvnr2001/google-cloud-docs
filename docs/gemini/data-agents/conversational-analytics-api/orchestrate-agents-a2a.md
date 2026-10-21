---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/orchestrate-agents-a2a/
title: Orchestrate data agents with A2A \u00a0|\u00a0 Conversational Analytics API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:52.559996+00:00
---

# Orchestrate data agents with A2A  |  Conversational Analytics API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/orchestrate-agents-a2a/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Orchestrate data agents with A2A Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Conversational Analytics API in Google Cloud implements the open [Agent-to-Agent (A2A) protocol](https://a2a-protocol.org/), which lets agents in multi-agent workflows discover capabilities, delegate analytical queries, and stream structured responses, such as executable SQL queries and chart visualizations.

You can query data agents that are built into the Conversational Analytics API for BigQuery and Looker by passing dataset context in your API request, or you can query custom data agents that are configured with your organization's business logic.

To build and query data agents directly, see [Build a data agent using the Python SDK](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk) or [Build a data agent using HTTP](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http).

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

## How data agent orchestration works

When you integrate Conversational Analytics API data agents into an application or multi-agent system, the orchestration workflow follows these operations:

  * The orchestrator agent discovers a data agent's capabilities and skills by inspecting its agent card before delegating analytical queries.
  * The orchestrator agent sends a message to query either a built-in data agent (`agents/bigquery-ca` or `agents/looker-ca`) by specifying data sources in the request, or a custom data agent (`dataAgents/DATA_AGENT_ID`) that is configured with domain business logic.
  * The data agent processes the request, executes required queries, and returns the results—either as a complete response or by streaming reasoning progress and structured artifacts (such as executable SQL and Vega-Lite chart specifications).



## Before you begin

Before you begin, complete the following prerequisites:

  1. [Enable the Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/enable-the-api), BigQuery API, and Looker API in your Google Cloud project.
  2. Verify that you have the required IAM roles and permissions.
  3. [Authenticate against the Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/authentication) and install the client library or obtain an authorization token.



### Required roles

To get the permissions that you need to discover and query data agents over A2A, ask your administrator to grant you the following IAM roles on your project: 

  * [Gemini Data Analytics Data Agent User ](https://docs.cloud.google.com/iam/docs/roles-permissions/geminidataanalytics#geminidataanalytics.dataAgentUser) (`roles/geminidataanalytics.dataAgentUser`)
  * For stateless queries: [Gemini Data Analytics Data Agent Stateless User ](https://docs.cloud.google.com/iam/docs/roles-permissions/geminidataanalytics#geminidataanalytics.dataAgentStatelessUser) (`roles/geminidataanalytics.dataAgentStatelessUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To query underlying data sources, you must also have read permissions on your target BigQuery datasets (such as `roles/bigquery.dataViewer`) or Looker Explores.

## Discover agent capabilities

Before delegating queries to a data agent, an orchestrator agent or a client application can inspect the agent card to view its capabilities and configuration, such as its description, available skills, and supported extensions. You can retrieve agent cards by using the [`getCard`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/a2a.projects.locations.agents.v1/getCard) method for both built-in data agents (`agents/bigquery-ca` and `agents/looker-ca`) and custom data agents (`dataAgents/DATA_AGENT_ID`).

### Retrieve an agent card

The following code samples show how to retrieve an agent card. These samples use the built-in BigQuery data agent (`agents/bigquery-ca`) as an example, but you can retrieve the card for the built-in Looker agent (`agents/looker-ca`) or a custom data agent (`dataAgents/DATA_AGENT_ID`) by changing the agent resource name in your request:

### Python SDK
    
    
    from google.cloud import geminidataanalytics_v1
    
    client = geminidataanalytics_v1.DataA2AServiceClient()
    
    agent_name = "projects/PROJECT_ID/locations/LOCATION/agents/bigquery-ca"
    
    request = geminidataanalytics_v1.GetAgentCardRequest(tenant=agent_name)
    card = client.[get_agent_card](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.html#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_get_agent_card)(request=request)
    
    print(card)
    

In the previous sample, replace values as follows:

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the location of the agent resource (such as `us`, `us-east4`, `eu`, or `global`)



### HTTP
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      "https://geminidataanalytics.googleapis.com/v1/a2a/projects/PROJECT_ID/locations/LOCATION/agents/bigquery-ca/v1/card"
    

In the previous sample, replace values as follows:

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the location of the agent resource (such as `us`, `us-east4`, `eu`, or `global`)



### Understand the agent card structure

A successful request returns an agent card object that contains metadata, supported skills, and extensions:
    
    
    {
      "name": "BigQuery Conversational Analytics Agent",
      "description": "This agent can answer questions about your data using BigQuery.",
      "protocolVersion": "1.0",
      "skills": [
        {
          "id": "data-analysis",
          "name": "Data Analysis",
          "description": "Provides data analysis assistance",
          "examples": [
            "What is the total sales for the last 3 months?"
          ],
          "inputModes": [
            "text/plain"
          ],
          "outputModes": [
            "text/plain",
            "application/json"
          ]
        }
      ],
      "capabilities": {
        "streaming": true,
        "extensions": [
          {
            "uri": "https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/reference/a2a/extensions/bigquery_context/v1",
            "description": "Google Data Analytics BigQuery Context extension"
          }
        ]
      },
      "defaultInputModes": [
        "text/plain"
      ],
      "defaultOutputModes": [
        "text/plain",
        "application/json"
      ]
    }
    

The agent card includes the following fields:

  * `name`: the display name of the data agent
  * `description`: a summary of the data agent's analytical capabilities
  * `protocolVersion`: the version of the A2A protocol that is supported by the endpoint (such as `1.0`)
  * `skills`: the tasks that the data agent can perform, including sample prompts (`examples`) and supported data formats (`inputModes` and `outputModes`, such as `text/plain` or `application/json`)
  * `capabilities.streaming`: a boolean value that indicates whether the data agent supports real-time streaming over the `stream` method
  * `capabilities.extensions`: the A2A extensions that the data agent supports, such as `bigquery_context/v1`, `stateless/v1`, and `kms/v1`
  * `defaultInputModes` and `defaultOutputModes`: the default data formats (such as `text/plain` or `application/json`) for request and response payloads



## Send a message to a data agent

To send a message to a data agent, use the [`send`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/a2a.projects.locations.agents.v1.message/send) method. The data agent processes the request, generates and runs the required SQL queries against your data, and returns the natural language answer along with generated data artifacts.

### Send a message

When you send a message, specify the target data agent in the resource path:

  * For built-in data agents (`agents/bigquery-ca` or `agents/looker-ca`), pass target table or Explore references in the `metadata` field by using the `bigquery_context/v1` or `looker_context/v1` extension.
  * For custom data agents (`dataAgents/DATA_AGENT_ID`), omit the `metadata` field because context, schemas, and instructions are configured directly on the agent resource.



To process queries without storing conversation history in Google Cloud, include the `stateless/v1` extension in your request. To encrypt stored conversation data and metadata by using a customer-managed encryption key, pass the `kms/v1` extension with your Cloud KMS key name. For more information, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/cmek).

The following code samples show how to send a message to the built-in BigQuery data agent:

### Python SDK
    
    
    from google.cloud import geminidataanalytics_v1
    
    client = geminidataanalytics_v1.DataA2AServiceClient()
    
    agent_name = "projects/PROJECT_ID/locations/LOCATION/agents/bigquery-ca"
    
    request = geminidataanalytics_v1.SendMessageRequest(
        tenant=agent_name,
        message=geminidataanalytics_v1.[Message](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Message.html)(
            role="ROLE_USER",
            # Optional: Pass context_id to continue an existing conversation
            # context_id="projects/PROJECT_ID/locations/LOCATION/conversations/CONVERSATION_ID",
            parts=[
                geminidataanalytics_v1.Part(
                    text="What are the top 5 countries where our users are located?"
                )
            ],
        ),
        configuration=geminidataanalytics_v1.SendMessageConfiguration(
            return_immediately=False
        ),
        metadata={
            "https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/reference/a2a/extensions/bigquery_context/v1": {
                "datasource_references": {
                    "bq": {
                        "tableReferences": [
                            {
                                "projectId": "DATASET_PROJECT_ID",
                                "datasetId": "DATASET_ID",
                                "tableId": "TABLE_ID",
                            }
                        ]
                    }
                }
            },
            # Optional: Process queries without storing conversation history in Google Cloud
            # "https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/reference/a2a/extensions/stateless/v1": {},
            # Optional: Encrypt conversation history and metadata with a customer-managed encryption key (CMEK)
            # "https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/reference/a2a/extensions/kms/v1": {
            #     "kmsKey": "projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME"
            # },
        },
    )
    
    response = client.[send_message](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.html#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_send_message)(request=request)
    
    print(response)
    

In the previous sample, replace values as follows:

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the location of the agent resource (such as `us`, `us-east4`, `eu`, or `global`)
  * `CONVERSATION_ID`: (Optional) the ID of an existing conversation session to continue
  * `What are the top 5 countries where our users are located?`: the natural language question to ask the data agent
  * `DATASET_PROJECT_ID`: the ID of the Google Cloud project that contains the BigQuery dataset (for example, `bigquery-public-data`)
  * `DATASET_ID`: the ID of the BigQuery dataset (for example, `thelook_ecommerce`)
  * `TABLE_ID`: the ID of the BigQuery table (for example, `users`)
  * `KEY_RING`: (Optional) the name of the Cloud KMS key ring when using CMEK
  * `KEY_NAME`: (Optional) the name of the Cloud KMS crypto key when using CMEK



### HTTP
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "Content-Type: application/json; charset=utf-8" \
      -H "A2A-Extensions: https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/reference/a2a/extensions/bigquery_context/v1" \
      -d '{
        "message": {
          "role": "ROLE_USER",
          "parts": [
            {
              "text": "What are the top 5 countries where our users are located?"
            }
          ]
        },
        "configuration": {
          "return_immediately": false
        },
        "metadata": {
          "https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/reference/a2a/extensions/bigquery_context/v1": {
            "datasource_references": {
              "bq": {
                "tableReferences": [
                  {
                    "projectId": "DATASET_PROJECT_ID",
                    "datasetId": "DATASET_ID",
                    "tableId": "TABLE_ID"
                  }
                ]
              }
            }
          }
        }
      }' \
      "https://geminidataanalytics.googleapis.com/v1/a2a/projects/PROJECT_ID/locations/LOCATION/agents/bigquery-ca/v1/message:send"
    

In the previous sample, replace values as follows:

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the location of the agent resource (such as `us`, `us-east4`, `eu`, or `global`)
  * `What are the top 5 countries where our users are located?`: the natural language question to ask the data agent
  * `DATASET_PROJECT_ID`: the ID of the Google Cloud project that contains the BigQuery dataset (for example, `bigquery-public-data`)
  * `DATASET_ID`: the ID of the BigQuery dataset (for example, `thelook_ecommerce`)
  * `TABLE_ID`: the ID of the BigQuery table (for example, `users`)



### Understand the response structure

A successful request returns a `task` object that contains the final status, the conversation identifier, and generated artifacts:
    
    
    {
      "task": {
        "id": "ab12d1f2-e170-4c4f-aff4-be466c6beaaa",
        "contextId": "projects/my-project/locations/us/conversations/conv-67890",
        "status": {
          "state": "TASK_STATE_COMPLETED"
        },
        "artifacts": [
          {
            "artifactId": "synthetic-8a368e8e-378a-4b80-9f07-0b1a397c221d",
            "name": "Final response",
            "description": "Final response from the agent.",
            "parts": [
              {
                "text": "The top 5 countries where our users are located are China (33,783), the United States (22,701), Brasil (14,620), South Korea (5,302), and France (4,645)."
              }
            ]
          },
          {
            "artifactId": "synthetic-50483808-b231-4b30-a859-2c30d0355a8d",
            "name": "Generated SQL",
            "description": "Generated SQL from the agent.",
            "parts": [
              {
                "text": "SELECT country, COUNT(DISTINCT id) AS user_count FROM `bigquery-public-data.thelook_ecommerce.users` GROUP BY country ORDER BY user_count DESC LIMIT 5",
                "mediaType": "text/x-sql"
              }
            ]
          }
        ]
      }
    }
    

The response includes the following key fields:

  * `task.id`: the unique identifier for the execution task
  * `task.contextId`: the resource path of the conversation, which you pass in the `message.contextId` field of subsequent requests to continue the session
  * `task.status.state`: the execution state of the task (such as `TASK_STATE_COMPLETED`)
  * `task.artifacts[]`: structured assets that are generated by the data agent, such as the natural language answer (`Final response`), the executable SQL query (`Generated SQL`), and tabular result rows (`Data result`)



## Stream responses from a data agent

To receive real-time updates as the data agent reasons through a query, use the [`stream`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/a2a.projects.locations.agents.v1.message/stream) method. The response streams status updates (`status_update`) with intermediate thoughts and incremental artifacts (`artifact_update`), such as generated SQL queries and Vega-Lite chart specifications.

Streaming requests also support continuing conversations (`context_id`), stateless processing (`stateless/v1`), and customer-managed encryption keys (`kms/v1`).

### Send a streaming message

The following code samples show how to stream events from the built-in BigQuery data agent. To stream from a custom data agent (`dataAgents/DATA_AGENT_ID`), target the custom agent resource path and omit the `metadata` field:

### Python SDK
    
    
    from google.cloud import geminidataanalytics_v1
    
    client = geminidataanalytics_v1.DataA2AServiceClient()
    
    agent_name = "projects/PROJECT_ID/locations/LOCATION/agents/bigquery-ca"
    
    request = geminidataanalytics_v1.SendMessageRequest(
        tenant=agent_name,
        message=geminidataanalytics_v1.[Message](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Message.html)(
            role="ROLE_USER",
            parts=[
                geminidataanalytics_v1.Part(
                    text="What are the top 5 countries where our users are located? Please show a pie chart."
                )
            ],
        ),
        metadata={
            "https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/reference/a2a/extensions/bigquery_context/v1": {
                "datasource_references": {
                    "bq": {
                        "tableReferences": [
                            {
                                "projectId": "DATASET_PROJECT_ID",
                                "datasetId": "DATASET_ID",
                                "tableId": "TABLE_ID",
                            }
                        ]
                    }
                }
            },
            # Optional: Process queries without storing conversation history in Google Cloud
            # "https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/reference/a2a/extensions/stateless/v1": {},
            # Optional: Encrypt conversation history and metadata with a customer-managed encryption key (CMEK)
            # "https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/reference/a2a/extensions/kms/v1": {
            #     "kmsKey": "projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME"
            # },
        },
    )
    
    # Stream response events
    stream = client.[send_streaming_message](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_a2a_service.DataA2AServiceClient.html#google_cloud_geminidataanalytics_v1alpha_services_data_a2a_service_DataA2AServiceClient_send_streaming_message)(request=request)
    
    for chunk in stream:
      print(chunk)
    

In the previous sample, replace values as follows:

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the location of the agent resource (such as `us`, `us-east4`, `eu`, or `global`)
  * `What are the top 5 countries where our users are located? Please show a pie chart.`: the natural language question to ask the data agent
  * `DATASET_PROJECT_ID`: the ID of the Google Cloud project that contains the BigQuery dataset (for example, `bigquery-public-data`)
  * `DATASET_ID`: the ID of the BigQuery dataset (for example, `thelook_ecommerce`)
  * `TABLE_ID`: the ID of the BigQuery table (for example, `users`)
  * `KEY_RING`: (Optional) the name of the Cloud KMS key ring when using CMEK
  * `KEY_NAME`: (Optional) the name of the Cloud KMS crypto key when using CMEK



### HTTP
    
    
    curl -X POST \
      -N \
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "Content-Type: application/json; charset=utf-8" \
      -H "Accept: text/event-stream, application/json" \
      -H "A2A-Extensions: https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/reference/a2a/extensions/bigquery_context/v1" \
      -d '{
        "message": {
          "role": "ROLE_USER",
          "parts": [
            {
              "text": "What are the top 5 countries where our users are located? Please show a pie chart."
            }
          ]
        },
        "metadata": {
          "https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/reference/a2a/extensions/bigquery_context/v1": {
            "datasource_references": {
              "bq": {
                "tableReferences": [
                  {
                    "projectId": "DATASET_PROJECT_ID",
                    "datasetId": "DATASET_ID",
                    "tableId": "TABLE_ID"
                  }
                ]
              }
            }
          }
        }
      }' \
      "https://geminidataanalytics.googleapis.com/v1/a2a/projects/PROJECT_ID/locations/LOCATION/agents/bigquery-ca/v1/message:stream"
    

In the previous sample, replace values as follows:

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the location of the agent resource (such as `us`, `us-east4`, `eu`, or `global`)
  * `What are the top 5 countries where our users are located? Please show a pie chart.`: the natural language question to ask the data agent
  * `DATASET_PROJECT_ID`: the ID of the Google Cloud project that contains the BigQuery dataset (for example, `bigquery-public-data`)
  * `DATASET_ID`: the ID of the BigQuery dataset (for example, `thelook_ecommerce`)
  * `TABLE_ID`: the ID of the BigQuery table (for example, `users`)



### Understand the streaming response structure

When you send a streaming request, the server returns a stream of event objects (`StreamResponse`). Each event contains either a status update or an artifact update.

Status update events deliver intermediate progress notifications and thought messages as the data agent reasons through your query:
    
    
    {
      "statusUpdate": {
        "taskId": "f41cd8e3-e665-460c-aceb-7b337f1848ef",
        "status": {
          "state": "TASK_STATE_WORKING",
          "message": {
            "role": "ROLE_AGENT",
            "parts": [
              {
                "text": "Analyzing context"
              },
              {
                "text": "Retrieved context for 1 table."
              }
            ]
          }
        }
      }
    }
    

Artifact update events deliver structured output objects, such as executable SQL queries, natural language answers, or chart specifications:
    
    
    {
      "artifactUpdate": {
        "taskId": "f41cd8e3-e665-460c-aceb-7b337f1848ef",
        "artifact": {
          "artifactId": "synthetic-7ca98286-0a15-4ca0-a8bc-f14dc231b3ba",
          "name": "Chart result",
          "description": "Chart visualization generated by the data agent.",
          "parts": [
            {
              "data": {
                "title": "Top 5 Countries by User Population",
                "mark": "arc",
                "encoding": {
                  "color": {
                    "field": "country",
                    "type": "nominal"
                  },
                  "theta": {
                    "field": "user_count",
                    "type": "quantitative"
                  }
                },
                "data": {
                  "values": [
                    {
                      "country": "China",
                      "user_count": 33783
                    },
                    {
                      "country": "United States",
                      "user_count": 22701
                    },
                    {
                      "country": "Brasil",
                      "user_count": 14620
                    },
                    {
                      "country": "South Korea",
                      "user_count": 5302
                    },
                    {
                      "country": "France",
                      "user_count": 4645
                    }
                  ]
                }
              }
            }
          }
        },
        "lastChunk": true
      }
    }
    

The streaming response includes the following key fields:

  * `statusUpdate.status.state`: the intermediate or final state of the task (such as `TASK_STATE_WORKING` or `TASK_STATE_COMPLETED`)
  * `statusUpdate.status.message.parts[]`: thought or progress descriptions that are emitted during execution
  * `artifactUpdate.artifact`: the structured asset that is generated by the data agent, such as a Vega-Lite chart specification (`data`) or SQL query (`text`)
  * `artifactUpdate.lastChunk`: a boolean flag that indicates whether the artifact stream is complete



To render the returned Vega or Vega-Lite specification in Python or frontend applications, see [Render an agent response as a visualization](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/render-visualization).

## What's next

  * Learn how to [render agent responses as visualizations](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/render-visualization) by using Vega-Lite and Altair.
  * Learn how to [guide agent behavior with authored context](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-system-instructions) to configure business rules and verified queries.
  * Explore [architectural integration patterns](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/integration-patterns) for multi-agent systems.
  * Review the [Gemini Data Analytics API REST reference](https://docs.cloud.google.com/gemini/data-agents/reference/rest).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
