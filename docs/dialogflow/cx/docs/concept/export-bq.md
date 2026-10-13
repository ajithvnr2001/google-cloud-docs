---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/export-bq/
title: Conversation history export to BigQuery \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:52.236752+00:00
---

# Conversation history export to BigQuery  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/export-bq/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Conversation history export to BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

You can export [conversation history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-general) to [BigQuery](https://docs.cloud.google.com/bigquery/docs). Once configured, all live conversation history is written to your BigQuery table. This provides you with advanced analysis tools that can help you debug and improve your agent and to discover patterns in conversation data.

## Limitations

The following limitations apply:

  * A maximum of 500 turns can be exported for each conversation.



## Cross project permissions

If your Dialogflow agent and BigQuery data are not in the same project, the [service account](https://docs.cloud.google.com/dialogflow/cx/docs/quick/setup#sa) associated with your Dialogflow Google Cloud project must also have the `roles/bigquery.dataEditor` IAM permission for the BigQuery dataset in your BigQuery Google Cloud project. 

Service account format: `service-<dialogflow-project-number>@gcp-sa-dialogflow.iam.gserviceaccount.com`

The user configuring the export in Dialogflow must have permissions on the BigQuery project. If they don't, the BigQuery project won't appear as an option in the Dialogflow Console.

The minimum permission required on the BigQuery project in order for the user to see it in Dialogflow is `resourcemanager.projects.get`. Alternatively, you can assign one of the following Google Cloud predefined roles that include this permission but don't require the user to have access to the BigQuery dataset: `roles/browser` or `roles/bigquery.metadataViewer`.

## Table description

Each row of the table contains one conversational turn with the following columns:

Column | Type | Description  
---|---|---  
project_id | STRING | The project ID.  
agent_id | STRING | The agent ID.  
conversation_name | STRING | The fully qualified resource name for the session.  
turn_position | INTEGER | The conversational turn number.  
request_time | TIMESTAMP | The time of the conversational turn.  
language_code | STRING | The [language tag](https://docs.cloud.google.com/dialogflow/cx/docs/reference/language).  
request | JSON | The detect intent request.  
response | JSON | The detect intent response.  
partial_responses | JSON | [Partial responses](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#partial-response) if applicable.  
derived_data | JSON | Additional metadata for this conversational turn.  
conversation_signals | JSON | NLU related analytics data. See [ConversationSignals](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationSignals) for the JSON schema.  
bot_answer_feedback | JSON | [Answer feedback](https://docs.cloud.google.com/dialogflow/cx/docs/concept/answer-feedback) if provided.  
  
## Configuration

To configure conversation history export:

  1. Ensure that [conversation history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-general) is enabled.
  2. Follow the BigQuery [dataset creation guide](https://docs.cloud.google.com/bigquery/docs/datasets#create-dataset) to create a dataset. Note the dataset name, as you will need this in the next step.
  3. Follow the BigQuery [table creation guide](https://docs.cloud.google.com/bigquery/docs/tables) to create a table with a SQL schema definition. Use the following SQL statement for creation:
         
         CREATE TABLE <your_dataset_name>.dialogflow_bigquery_export_data(
           project_id STRING,
           agent_id STRING,
           conversation_name STRING,
           turn_position INTEGER,
           request_time TIMESTAMP,
           language_code STRING,
           request JSON,
           response JSON,
           partial_responses JSON,
           derived_data JSON,
           conversation_signals JSON,
           bot_answer_feedback JSON
         );
         

  4. Configure your [agent settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-general) to enable BigQuery export, and to provide the dataset and table names created above.

**Note:** If your agent is protected by a Customer Managed Encryption Key (CMEK), you will see a warning if the destination BigQuery table is not protected by CMEK.



[ Previous arrow_back  Cloud logging  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/logging)

[ Next Change history  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/change-history)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
