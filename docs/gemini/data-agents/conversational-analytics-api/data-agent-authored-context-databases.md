---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-databases/
title: Define data agent context for database data sources \u00a0|\u00a0 Conversational Analytics API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:17:22.714976+00:00
---

# Define data agent context for database data sources  |  Conversational Analytics API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-databases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Define data agent context for database data sources Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Data agents**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/pJByTWfenZAWbaXo7). 

This page describes how to provide authored context for data agents that use database data sources.

[Authored context](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-system-instructions) is guidance that data agent owners can provide to shape the behavior of a data agent and to refine the API's responses. Effective authored context provides your Conversational Analytics API data agents with useful context for answering questions about your data sources.

For database data sources such as AlloyDB, GoogleSQL for Spanner, Cloud SQL for MySQL, and Cloud SQL for PostgreSQL, you provide authored context by first defining and storing the context in the database, and then referencing it in your data source reference. The examples on this page use the [`QueryData` method](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations/queryData).

Providing high-accuracy context enables the API to generate more accurate and relevant SQL queries and answers.

## Before you begin

  * You'll need a data agent with its agent context uploaded for the database that you want to query. For more information, see the data agent documentation for [AlloyDB](https://docs.cloud.google.com/alloydb/docs/ai/build-context-gemini-cli), [Spanner](https://docs.cloud.google.com/spanner/docs/build-context-gemini-cli), [Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql/build-context-gemini-cli), and [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/build-context-gemini-cli).
  * To create, upload, and manage context sets for database data sources, enable the [Knowledge Catalog API](https://console.cloud.google.com/apis/library/dataplex.googleapis.com) and grant the Dataplex Catalog Editor (`roles/dataplex.catalogEditor`) or Dataplex Catalog Admin (`roles/dataplex.catalogAdmin`) role to the IAM user or service account at the project level. For more information, see [Context sets permissions](https://docs.cloud.google.com/knowledge-catalog/docs/iam-permissions#context-set-permissions).
  * Enable the [Cloud SQL Data API for your instance](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/instances/execute-sql) as follows:
        
        gcloud beta sql instances patch INSTANCE_ID --data-api-access=ALLOW_DATA_API

Replace `INSTANCE_ID` with the ID of your Cloud SQL for MySQL or Cloud SQL for PostgreSQL instance.

You must also grant database privileges to an IAM user or service account. For more information, see [Grant database privileges to an individual IAM user or service account in Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#grant-db-privileges) and [Grant database privileges to an individual IAM user or service account in Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/add-manage-iam-users#grant-db-privileges).




## Providing context with `QueryData`

When calling the `QueryData` method, you provide the data source and context information within the `QueryDataRequest.context.datasourceReferences` field. For database data sources, you must use one of the following:

  * `alloydb` for AlloyDB for PostgreSQL
  * `spanner_reference` for GoogleSQL for Spanner
  * `cloud_sql_reference` for Cloud SQL for MySQL and Cloud SQL for PostgreSQL



Within these references, you specify the database and tables by using the `databaseReference` field. To include authored context, you must also provide an `agentContextReference` that points to a `context_set_id`.

### Example `QueryData` request with authored context

The following example shows a `QueryData` request that uses `alloydb`. The `agent_context_reference.context_set_id` field is used to link to pre-authored context stored in the database.

### AlloyDB
    
    
    {
     "parent": "projects/data-agents-project/locations/us-central1",
     "prompt": "How many accounts who have region in Prague are eligible for loans? A3 contains the data of region.",
     "context": {
       "datasource_references": [
         {
           "alloydb": {
             "database_reference": {
               "project_id": "data-agents-project",
               "region": "us-central1",
               "cluster_id": "sqlgen-magic",
               "instance_id": "data-agents-primary",
               "database_id": "financial"
             },
             "agent_context_reference": {
               "context_set_id": "projects/data-agents-project/locations/us-east1/contextSets/bdf_pg_all_templates"
             }
           }
         }
       ]
     },
     "generation_options": {
       "generate_query_result": true,
       "generate_natural_language_answer": true,
       "generate_disambiguation_question": true,
       "generate_explanation": true
     }
    }

### GoogleSQL for Spanner
    
    
    {
     "parent": "projects/data-agents-project/locations/us-central1",
     "prompt": "How many accounts who have region in Prague are eligible for loans? A3 contains the data of region.",
     "context": {
       "datasource_references": [
         {
           "spanner_reference" {
             "database_reference" {
               "engine": "GOOGLE_SQL"
               "project_id": "data-agents-project"
               "instance_id": "evalbench"
               "database_id": "financial"
             },
             "agent_context_reference": {
               "context_set_id": "projects/data-agents-project/locations/us-east1/contextSets/bdf_pg_all_templates"
             }
           }
         }
       ]
     },
     "generation_options": {
       "generate_query_result": true,
       "generate_natural_language_answer": true,
       "generate_disambiguation_question": true,
       "generate_explanation": true
     }
    }

### Cloud SQL for MySQL
    
    
    {
     "parent": "projects/data-agents-project/locations/us-central1",
     "prompt": "How many accounts who have region in Prague are eligible for loans? A3 contains the data of region.",
     "context": {
       "datasource_references": [
         {
           "cloud_sql_reference": {
             "database_reference": {
               "engine": "MYSQL"
               "project_id": "data-agents-project",
               "region": "us-central1",
               "instance_id": "data-agents-primary",
               "database_id": "financial"
             },
             "agent_context_reference": {
               "context_set_id": "projects/data-agents-project/locations/us-east1/contextSets/bdf_pg_all_templates"
             }
           }
         }
       ]
     },
     "generation_options": {
       "generate_query_result": true,
       "generate_natural_language_answer": true,
       "generate_disambiguation_question": true,
       "generate_explanation": true
     }
    }

### Cloud SQL for PostgreSQL
    
    
    {
     "parent": "projects/data-agents-project/locations/us-central1",
     "prompt": "How many accounts who have region in Prague are eligible for loans? A3 contains the data of region.",
     "context": {
       "datasource_references": [
         {
           "cloud_sql_reference": {
             "database_reference": {
               "engine": "POSTGRES"
               "project_id": "data-agents-project",
               "region": "us-central1",
               "instance_id": "data-agents-primary",
               "database_id": "financial"
             },
             "agent_context_reference": {
               "context_set_id": "projects/data-agents-project/locations/us-east1/contextSets/bdf_pg_all_templates"
             }
           }
         }
       ]
     },
     "generation_options": {
       "generate_query_result": true,
       "generate_natural_language_answer": true,
       "generate_disambiguation_question": true,
       "generate_explanation": true
     }
    }

The request body contains the following fields:

  * `prompt`: The natural language question from the end user.
  * `context`: Contains information about the data sources. 
    * `datasource_references`: Specifies the data source type. 
      * `alloydb`: Required when querying the database. This field changes based on the database you are querying. 
        * `database_reference`: Specifies information related to your database instance. 
          * `engine`: The database engine or SQL dialect. Optional for AlloyDB. For Spanner databases, set to `GOOGLE_SQL`. For Cloud SQL for MySQL instances, set to `MYSQL`. For Cloud SQL for PostgreSQL instances, set to `POSTGRESQL`.
          * `project_id`: The project ID of the database instance.
          * `region`: The region of the database instance.
          * `cluster_id`: The cluster ID of the database instance.
          * `instance_id`: The instance ID of the database.
          * `database_id`: The ID of the database.
        * `agent_context_reference`: Links to authored context in the database. 
          * `context_set_id`: The agent context ID stored in the database. For more information about how to find the context set ID, see the documentation for [AlloyDB](https://docs.cloud.google.com/alloydb/docs/ai/inspect-data-agent#find-agent-context-id), [Spanner](https://docs.cloud.google.com/spanner/docs/inspect-data-agent#find-agent-context-id), [Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql/inspect-data-agent#find-agent-context-id), and [Cloud SQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/inspect-data-agent#find-agent-context-id).
  * `generationOptions`: Configures the type of output to generate. 
    * `generate_query_result`: Set to true to generate and return the query results.
    * `generate_natural_language_answer`: Optional. If set to true, generates a natural language answer.
    * `generate_explanation`: Optional. If set to true, generates an explanation of the SQL query.
    * `generate_disambiguation_question`: Optional. If set to true, generates disambiguation questions if the query is ambiguous.



### Example `QueryData` Response

Here is an example of a successful response from a `QueryData` call:
    
    
    {
     "generated_query": "-- Count the number of accounts in Prague that are eligible for loans\nSELECT\n  COUNT(DISTINCT \"loans\".\"account_id\")\nFROM \"loans\"\nJOIN \"district\" -- Join based on district ID\n  ON \"loans\".\"district_id\" = \"district\".\"district_id\"\nWHERE\n  \"district\".\"A3\" = 'Prague'; -- Filter for the Prague region",
     "intent_explanation": "The question asks for the number of accounts eligible for loans in the Prague region. I need to join the `district` table with the `loans` table to filter by region and count the distinct accounts. The `A3` column in the `district` table contains the region information, and I'll filter for 'Prague'. The `loans` table contains information about loans, including the `account_id` and `district_id`. I will join these two tables on their respective district IDs.",
     "query_result": {
       "columns": [
         {
           "name": "count"
         }
       ],
       "rows": [
         {
           "values": [
             {
               "value": "2"
             }
           ]
         }
       ],
       "total_row_count": 1
     },
     "natural_language_answer": "There are 2 accounts in Prague that are eligible for loans."
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
