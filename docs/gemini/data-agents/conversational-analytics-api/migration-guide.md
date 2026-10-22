---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/migration-guide/
title: Migrate from the Data QnA API to the Conversational Analytics API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:55.068276+00:00
---

# Migrate from the Data QnA API to the Conversational Analytics API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/migration-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Migrate from the Data QnA API to the Conversational Analytics API Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes key differences and steps for migrating your applications from the Data QnA API (`dataqna.googleapis.com`) to the Conversational Analytics API (`geminidataanalytics.googleapis.com`).

**Note:** If you haven't previously enabled the Data QnA API (`dataqna.googleapis.com`), you can skip this page and go directly to the documentation on [setup and authentication](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/enable-the-api).

## Provide feedback

If you encounter any discrepancies during the migration process, contact [`conversational-analytics-api-feedback@google.com`](mailto:conversational-analytics-api-feedback@google.com).

## Overview of key changes

The Conversational Analytics API introduces changes to the API endpoint, the service that the API uses, and the structure of API requests. The following table summarizes the key differences between the Data QnA API and the Conversational Analytics API and lists the required steps for migration.

**Data QnA API** | **Conversational Analytics API** | **Required change**  
---|---|---  
`dataqna.googleapis.com` endpoint | `geminidataanalytics.googleapis.com` endpoint | Update the API endpoint in your requests.  
`DataQuestionService` service | `DataChatService` service | Update the service name in your requests.  
`project` field in the `AskQuestionRequest` message | `parent` field in the `ChatRequest` message | Replace the `project` field with the `parent` field in your requests. For more information, see Replace `project` with `parent` for request routing.  
`datasource_ids` field | `studio_references` field | Replace the `datasource_ids` field with the `studio_references` field in your requests. For more information, see Update references to Data Studio data source IDs.  
`AgentConfig` object | `ConversationOptions` object | Replace the `AgentConfig` object with the `ConversationOptions` object in your requests. For more information, see Enable Python analysis with `ConversationOptions`.  
`context` field in the `AskQuestionRequest` message | `inline_context` field in the `ChatRequest` message | Replace the `context` field with the `inline_context` field in your requests. For more information, see Replace `context` with `inline_context`.  
  
For examples of how to update your API request structures, see Examples: Update your API request structures.

### Replace `project` with `parent` for request routing

In the Data QnA API, you use the `project` field within the `AskQuestionRequest` message to specify the Google Cloud project. In the Conversational Analytics API, the `project` field is deprecated within the `ChatRequest` message. Instead, you use the `parent` field to specify both the project and the location.

The following example shows the format for specifying the `parent` field:
    
    
    parent: "projects/PROJECT_NAME/locations/global"
    

In the previous example, replace `PROJECT_NAME` with the name of your Google Cloud project.

### Update references to Data Studio data source IDs

In the Data QnA API, you use the `datasource_ids` field to provide a list of Data Studio data source IDs. In the Conversational Analytics API, you use the `studio_references` field to provide a list of `StudioDatasourceReference` objects, each containing a single data source ID. For more information, see [`StudioDatasourceReference`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#studiodatasourcereferences).

### Enable Python analysis with `ConversationOptions`

The `AgentConfig` object, which is used in the Data QnA API to enable tools, is not used by the `DataChatService` service in the Conversational Analytics API. To enable features such as Python analysis in the Conversational Analytics API, use the `ConversationOptions` object when you create or configure a data agent. For more information, see [`ConversationOptions`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#conversationoptions).

### Replace `context` with `inline_context`

In the Data QnA API, the `AskQuestionRequest` message includes a `context` field for inline contextual information. In the Conversational Analytics API, the `context` field is renamed to `inline_context` in the `ChatRequest` message. This change helps to distinguish inline context from other types of context that can be provided through data agents.

## Examples: Update your API request structures

The following examples show how to adapt your requests to the new API structure when you migrate from the Data QnA API to the Conversational Analytics API. These examples cover BigQuery, Looker, and Data Studio data sources.

### BigQuery data source

This section provides an example of how to update your API requests for BigQuery data sources. The example shows how to update a request that asks for a bar graph that shows the top five states by the total number of airports.

The following code sample shows the request structure for the Data QnA API:
    
    
    project: "projects/PROJECT_NAME"
    messages {
      user_message {
        text: "Create a bar graph showing the top 5 states by the total number of airports."
      }
    }
    context {
      datasource_references {
        bq {
          table_references {
            project_id: "PROJECT_ID"
            dataset_id: "DATASET_ID"
            table_id: "TABLE_ID"
          }
        }
      }
    }
    

The following code sample shows the updated request structure for the Conversational Analytics API:
    
    
    messages {
      user_message {
        text: "Create a bar graph showing the top 5 states by the total number of airports."
      }
    }
    parent: "projects/PROJECT_NAME/locations/global"
    inline_context {
      datasource_references {
        bq {
          table_references {
            project_id: "PROJECT_ID"
            dataset_id: "DATASET_ID"
            table_id: "TABLE_ID"
          }
        }
      }
    

For the previous examples, you can replace the sample values as follows:

  * `PROJECT_NAME`: The name of your Google Cloud project.
  * `PROJECT_ID`: The ID of your BigQuery project. To connect to a [public dataset](https://docs.cloud.google.com/bigquery/public-data), specify `bigquery-public-data`.
  * `DATASET_ID`: The ID of the BigQuery dataset. For example, `faa`.
  * `TABLE_ID`: The ID of the BigQuery table. For example, `us_airports`.



### Looker data source

This section provides an example of how to update your API requests for Looker data sources. The example shows how to update a request that asks for the count of orders by order status.

The following code sample shows the request structure for the Data QnA API:
    
    
    project: "projects/PROJECT_NAME"
    messages {
      user_message {
        text: "Show the count of orders by order status."
      }
    }
    context {
      datasource_references {
        looker {
          explore_references {
            looker_instance_uri: "INSTANCE_URI"
            lookml_model: "MODEL_NAME"
            explore: "EXPLORE_NAME"
          }
          credentials {
            oauth {
              secret {
                client_id: "CLIENT_ID"
                client_secret: "CLIENT_SECRET"
              }
            }
          }
        }
      }
    }
    
    

The following code sample shows the updated request structure for the Conversational Analytics API:
    
    
    messages {
      user_message {
        text: "Show the count of orders by order status."
      }
    }
    parent: "projects/PROJECT_NAME/locations/global"
    credentials {
      oauth {
        secret {
          client_id: "CLIENT_ID"
          client_secret: "CLIENT_SECRET"
        }
      }
    }
    inline_context {
      datasource_references {
        looker {
          explore_references {
            lookml_model: "MODEL_NAME"
            explore: "EXPLORE_NAME"
            looker_instance_uri: "INSTANCE_URI"
          }
        }
      }
    }
    

For the previous examples, you can replace the sample values as follows:

  * `PROJECT_NAME`: The name of your Google Cloud project.
  * `CLIENT_ID`: The client ID of your generated Looker API key.
  * `CLIENT_SECRET`: The client secret of your generated Looker API key.
  * `MODEL_NAME`: The name of your LookML model.
  * `EXPLORE_NAME`: The name of your LookML Explore.
  * `INSTANCE_URI`: The URI of your Looker instance.



### Data Studio data source

This section provides an example of how to update your API requests for Data Studio data sources. The example shows how to update a request that asks for a bar graph that shows the top five carriers.

The following code sample shows the request structure for the Data QnA API:
    
    
    project: "projects/PROJECT_NAME"
    messages {
      user_message {
        text: "Create a bar graph showing the top 5 carriers."
      }
    }
    context {
      datasource_references {
        studio {
          datasource_ids: "DATA_SOURCE_ID"
        }
      }
    }
    

The following code sample shows the updated request structure for the Conversational Analytics API:
    
    
    messages {
      user_message {
        text: "Create a bar graph showing the top 5 carriers."
      }
    }
    parent: "projects/PROJECT_NAME/locations/global"
    inline_context {
      datasource_references {
        studio {
          datasource_ids: "DATA_SOURCE_ID"
        }
      }
    }
    

For the previous examples, you can replace the sample values as follows:

  * `PROJECT_NAME`: The name of your Google Cloud project.
  * `DATA_SOURCE_ID`: The ID of your Data Studio data source.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
