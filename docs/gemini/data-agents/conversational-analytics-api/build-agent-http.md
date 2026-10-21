---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http/
title: Build a data agent using HTTP and Python \u00a0|\u00a0 Conversational Analytics API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:37.124723+00:00
---

# Build a data agent using HTTP and Python  |  Conversational Analytics API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Build a data agent using HTTP and Python Stay organized with collections  Save and categorize content based on your preferences. 

This page guides you through using Python to make HTTP requests to the Conversational Analytics API (accessed through `geminidataanalytics.googleapis.com`).

The sample Python code on this page shows how to complete the following tasks:

  * Configure initial settings and authentication.
  * Connect to a Looker, BigQuery, Data Studio, AlloyDB for PostgreSQL, Cloud SQL, or Spanner data source.
  * Create a data agent.
  * Create a conversation.
  * Manage data agents and conversations.
  * Use the API to ask questions.
  * Create a stateless multi-turn conversation.
  * Define helper functions.

**Tip:** You can run the code samples on this page in the interactive [Conversational Analytics API HTTP Colaboratory notebook](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/agents/gemini_data_analytics/intro_gemini_data_analytics_http.ipynb).

## Configure initial settings and authentication

The following sample Python code performs these tasks:

  * Imports required Python libraries.
  * Obtains an access token for HTTP authentication by using the Google Cloud CLI.
  * Defines variables for the billing project, location, and system instructions.
  * Sets the API endpoint based on the `location` variable.


    
    
    import json
    import json as json_lib
    import textwrap
    
    import altair as alt
    import google.auth
    from google.auth.transport.requests import Request
    import IPython
    from IPython.display import display, HTML
    import pandas as pd
    from pygments import highlight, lexers, formatters
    import requests
    
    from google.colab import auth
    auth.authenticate_user()
    
    access_token = !gcloud auth application-default print-access-token
    headers = {
            "Authorization": f"Bearer {access_token[0]}",
            "Content-Type": "application/json",
            "x-server-timeout": "300", # Custom timeout up to 600s
    }
    
    billing_project = "BILLING_PROJECT"
    location = "LOCATION"
    system_instruction = "SYSTEM_INSTRUCTIONS"
    
    # Set the base URL based on location.
    if not location or location == "global":
      base_url = "https://geminidataanalytics.googleapis.com"
    elif "-" in location:
      # Regional endpoints
      base_url = f"https://geminidataanalytics-{location}.googleapis.com"
    else:
      # Multi-regional endpoints
      base_url = f"https://geminidataanalytics.{location}.rep.googleapis.com"
    

Replace the sample values as follows:

  * BILLING_PROJECT: The ID of the Google Cloud project where you [enabled the required APIs](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/enable-the-api).
  * LOCATION: The location where your resources are stored. To use the global endpoint, specify `global`. To meet data residency requirements, specify a supported single region (such as `us-east4`) or multi-region (such as `eu` or `us`). For more information, see [Data residency](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-residency).

**Important:** The location in your request path must match the location of the endpoint that you're calling. For example, if you call the `geminidataanalytics.us.rep.googleapis.com` endpoint, specify `us` in your request path (such as `/locations/us`).
  * SYSTEM_INSTRUCTIONS: System instructions to guide the agent's behavior and customize it for your data needs. For example, you can use system instructions to define business terms, control response length, or set data formatting. Ideally, define system instructions by using the recommended YAML format in [Write effective system instructions](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-system-instructions) to provide detailed and structured guidance.




### Authenticate to Looker

If you plan to connect to a Looker data source, you will need to authenticate to the Looker instance.

### Using API keys

The following Python code sample demonstrates how to authenticate your agent to a Looker instance using API keys.
    
    
    looker_credentials = {
        "oauth": {
            "secret": {
                "client_id": "CLIENT_ID",
                "client_secret": "CLIENT_SECRET",
            }
        }
    }
    

Replace the sample values as follows:

  * CLIENT_ID: The client ID of your generated Looker API key.
  * CLIENT_SECRET: The client secret of your generated Looker API key.



### Using access tokens

The following Python code sample demonstrates how to authenticate your agent to a Looker instance using access tokens.
    
    
    looker_credentials = {
        "oauth": {
            "token": {
                "access_token": "ACCESS_TOKEN",
            }
        }
    }
    

Replace the sample values as follows:

  * ACCESS_TOKEN: The `access_token` value that you generate to authenticate to Looker.

**Tip:** Store the Looker access token (`access_token`) as an environment variable for improved security.

### Authenticate to AlloyDB for PostgreSQL

If you plan to connect to an AlloyDB data source, use the gcloud CLI to authenticate to the AlloyDB instance.

  1. Enable Identity and Access Management (IAM) authentication on AlloyDB by enabling the `alloydb.iam_authentication` flag on the AlloyDB instance.
  2. Grant IAM roles. The principal (user or service account) calling the Conversational Analytics API needs appropriate IAM permissions in your Google Cloud project. This typically includes roles like `alloydb.databaseUser`.
  3. Create a corresponding database user. Create an AlloyDB user that mirrors the IAM principal, using the user or service account email address as the username.



For more information, see [IAM database authentication](https://docs.cloud.google.com/alloydb/docs/database-users/iam-authentication).

### Authenticate to Cloud SQL for MySQL and Cloud SQL for PostgreSQL

If you plan to connect to a Cloud SQL for MySQL or Cloud SQL for PostgreSQL data source, you must authenticate to the Cloud SQL instance.

  1. Enable IAM database authentication. Make sure that the `cloudsql.iam_authentication` flag is set to `on` in your Cloud SQL for MySQL instance. You can add this when you create an instance or when you patch an existing instance.
         
         gcloud sql instances patch INSTANCE_NAME --database-flags
         cloudsql.iam_authentication=on
         

  2. Grant the required IAM roles.

The principal (user or service account) attempting to connect needs the `cloudsql.instances.login` and `cloudsql.instances.connect` IAM permissions on the project. To grant these roles and permissions, do one of the following:

     1. Grant the `roles/cloudsql.instanceUser`role. This includes permissions to sign into the instance (`cloudsql.instances.login`) and connect using the proxy (`cloudsql.instances.connect`).
     2. Alternatively, grant a custom role containing at least `cloudsql.instances.login` and `cloudsql.instances.connect`.
  3. Add the [IAM principal](https://docs.cloud.google.com/sql/docs/mysql/iam-authentication#iam-auth-concepts) as a database user. Create a user in the Cloud SQL instance that corresponds to the IAM principal's email address.

For a service account, run the following command:
         
         gcloud sql users create SERVICE_ACCOUNT_EMAIL --instance=INSTANCE_NAME
         --type=cloud_iam_service_account
         

For a user account, run the following command:
         
         gcloud sql users create USER_EMAIL --instance=INSTANCE_NAME
         --type=cloud_iam_user
         

  4. Grant database privileges. Connecting with IAM authenticates the user to the database, but it doesn't automatically grant permissions in the database. You need to use standard PostgreSQL commands—like `GRANT`—to give this new database user permissions on specific objects like tables and schemas.

  5. Connect as a superuser—like the default postgres user—and run the following commands:
         
         -- Example: Connect using psql as the 'postgres' user
         
         GRANT SELECT ON ALL TABLES IN SCHEMA public TO
         "user-or-service-account@example.com";
         

  6. Connect using IAM authentication.

Clients typically connect through the Cloud SQL Auth Proxy or a connector library, which handles the token exchange. The database username is the IAM principal's email. Passwords aren't used. An OAuth 2.0 token, usually handled automatically by the Cloud SQL Auth Proxy or by the Google Cloud CLI, is used instead.

The following example uses psql and the gcloud CLI to generate a token:
         
         PGPASSWORD=$(gcloud sql generate-login-token) psql --host=HOST_IP \
         --username=IAM_PRINCIPAL_EMAIL --dbname=DATABASE_NAME\
         

For more information, see [IAM authentication](https://docs.cloud.google.com/sql/docs/mysql/iam-authentication).

Replace the sample values as follows:

     * `INSTANCE_NAME`: the ID of the Cloud SQL instance that you want to patch to enable IAM database authentication.
     * `SERVICE_ACCOUNT_EMAIL`: the email address of the service account.
     * `USER_EMAIL`: the email address of the user account.
     * `HOST_IP`: the IP address of the Cloud SQL instance.
     * `IAM_PRINCIPAL_EMAIL`: the email address of the IAM principal—for example, service account or user.
     * `DATABASE_NAME`: the name of the database to connect to.



### Authenticate to Spanner

If you plan to connect to a Spanner data source, you need to authenticate to the Spanner instance.

  1. Grant IAM roles. The principal (user or service account) calling the Conversational Analytics API needs appropriate IAM permissions in your Google Cloud project. This typically includes roles like `databaseUser`.
  2. Create corresponding abstract database roles in Spanner using Data Definition Language (DDL).
  3. Use IAM policies to let IAM principals assume those database roles.



For more information, see [Fine-grained access control privileges](https://docs.cloud.google.com/spanner/docs/fgac-privileges).

## Connect to a data source

The following sections show how to define the connection details for your agent's data sources. Your agent can connect to data in the following ways:

  * Looker
  * Data Studio
  * BigQuery
  * AlloyDB data
  * Cloud SQL for MySQL data
  * Cloud SQL for PostgreSQL data
  * Spanner data



### Connect to Looker data

The following sample code defines a connection to a Looker Explore. To establish a connection with a Looker instance, verify that you've generated Looker API keys, as described in [Authenticate and connect to a data source](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/authentication#looker-api-keys). You can connect to up to five Looker Explores at a time with the Conversational Analytics API.

When you connect to a Looker data source, note the following:

  * You can query any included Explore in a conversation.
  * An agent can only query one Explore at a time. It is not possible to perform queries across multiple Explores simultaneously.
  * An agent can query multiple Explores in the same conversation.
  * An agent can query multiple Explores in a conversation that includes questions with multiple parts, or in conversations that include follow-up questions.

For example: A user connects two Explores, one called `cat-explore` and one called `dog-explore`. The user inputs the question "What's greater: the count of cats or the count of dogs?" This would create two queries: one to count the number of cats in `cat-explore` and one to count the number of dogs in `dog-explore`. The agent compares the number from both queries after completing both queries.




The following sample code defines a connection to multiple Looker Explores. To improve agent performance, you can optionally provide golden queries as structured context for your Explores. For more information, see [Define data agent context for Looker data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-looker).
    
    
    looker_instance_uri = "INSTANCE_URI"
    looker_data_source = {
        "looker": {
            "explore_references": [
                {
                    "looker_instance_uri": looker_instance_uri,
                    "lookml_model": "MODEL",
                    "explore": "EXPLORE",
                },
                {
                    "looker_instance_uri": looker_instance_uri,
                    "lookml_model": "MODEL_2",
                    "explore": "EXPLORE_2",
                },
                # Add up to 5 total Explore references
            ],
        }
    }
    

Replace the sample values as follows:

  * INSTANCE_URI: The complete URL of your Looker instance (for example, `https://mycompany.looker.com`).
  * MODEL: The name of the LookML model that includes the Explore that you want to connect to.
  * EXPLORE: The name of the Looker Explore that you want the data agent to query.
  * MODEL_2: The name of the second LookML model that includes the Explore that you want to connect to. You can repeat this variable for additional models for up to five Explores.
  * EXPLORE_2: The name of the additional Looker Explore that you want the data agent to query. You can repeat this variable to include up to five Explores.



### Connect to BigQuery data

With the Conversational Analytics API, there are no hard limits on the number of BigQuery tables that you can connect to. However, connecting to a large number of tables can reduce accuracy or cause you to exceed the model's input token limit.

**Note:** Queries that require complex joins across multiple tables might result in less accurate responses.

The following sections show how to connect to BigQuery data by using table references, graph references, or both.

#### Connect to BigQuery tables

The following sample code defines a connection to multiple BigQuery tables and includes examples of optional structured context fields. To improve agent performance, you can optionally provide structured context for your BigQuery tables, such as table and column descriptions, synonyms, tags, example queries, and user-defined functions. For more information, see [Define data agent context for BigQuery data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-bq).

**Important:** Make sure you have the necessary Identity and Access Management (IAM) permissions to query any BigQuery tables that you're connecting to.
    
    
    bigquery_data_sources = {
        "bq": {
            "tableReferences": [
                {
                    "projectId": "PROJECT_ID",
                    "datasetId": "DATASET_ID",
                    "tableId": "TABLE_ID",
                    "schema": {
                        "description": "TABLE_DESCRIPTION",
                        "fields": [{
                            "name": "COLUMN_NAME",
                            "description": "COLUMN_DESCRIPTION"
                        }]
                    }
                },
                {
                    "projectId": "PROJECT_ID_2",
                    "datasetId": "DATASET_ID_2",
                    "tableId": "TABLE_ID_2"
                },
                {
                    "projectId": "PROJECT_ID_3",
                    "datasetId": "DATASET_ID_3",
                    "tableId": "TABLE_ID_3"
                },
            ]
        }
    }
    

Replace the sample values as follows:

  * PROJECT_ID: The ID of the Google Cloud project that contains the BigQuery dataset and table that you want to connect to. To connect to a [public dataset](https://docs.cloud.google.com/bigquery/public-data), specify `bigquery-public-data`.
  * DATASET_ID: The ID of the BigQuery dataset.
  * TABLE_ID: The ID of the BigQuery table.
  * TABLE_DESCRIPTION: An optional description of the table's content and purpose.
  * COLUMN_NAME: The name of a column in the table for which you are providing an optional description.
  * COLUMN_DESCRIPTION: An optional description of the column's content and purpose.



#### Connect to BigQuery Graph

You can also connect to graphs by using [BigQuery Graph](https://docs.cloud.google.com/bigquery/docs/graph-overview). Provide one or more graph references in the `propertyGraphReferences` field.

For information about BigQuery edition requirements and graph query limitations, see [Connect to BigQuery Graph](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/connect-bigquery#connect-to-bq-graph).
    
    
    bigquery_data_sources = {
        "bq": {
            "propertyGraphReferences": [
              {
                "projectId": "GRAPH_PROJECT_ID",
                "datasetId": "GRAPH_DATASET_ID",
                "propertyGraphId": "GRAPH_ID"
              }
            ]
        }
    }
    

Replace the sample values as follows:

  * GRAPH_PROJECT_ID: The ID of the Google Cloud project that contains the BigQuery graph.
  * GRAPH_DATASET_ID: The ID of the BigQuery dataset that contains the graph.
  * GRAPH_ID: The ID of the BigQuery graph.



To query both tables and graphs with the same data agent, include both `tableReferences` and `propertyGraphReferences` in the `bq` object.

### Connect to Data Studio data

The following sample code defines a connection to a Data Studio data source.
    
    
    looker_studio_data_source = {
        "studio":{
            "studio_references": [
                {
                  "studio_datasource_id": "studio_datasource_id"
                }
            ]
        }
    }
    

Replace studio_datasource_id with the data source ID.

### Connect to AlloyDB data

The Conversational Analytics API uses a `database_reference` field in the `alloydb` field to connect to your AlloyDB cluster.

The following example defines a connection to an AlloyDB database.
    
    
    alloydb_data_source = {
        "alloydb": {
            "database_reference":
              {
                "project_id":"PROJECT_ID",
                "region":"REGION",
                "cluster_id":"CLUSTER_ID",
                "instance_id":"INSTANCE_ID",
                "database_id":"DATABASE",
                "table_ids":["TABLE_1_ID", "TABLE_2_ID"]
              }
              # Optional: Include this if you have pre-authored context for the agent
              # "agent_context_reference": {
              #     "context_set_id": f"projects/billing_project/locations/location/contextSets/your_context_set_id"
              # }
    
        }
    }
    

Replace the sample values as follows:

  * `PROJECT_ID`: The ID of the Google Cloud project that contains the AlloyDB cluster.
  * `REGION`: The region where the AlloyDB cluster resides—for example, `us-central1`.
  * `CLUSTER_ID`: The ID of the AlloyDB cluster.
  * `INSTANCE_ID`: The ID of the AlloyDB instance.
  * `DATABASE`: The name of the target database—for example, `financial`.
  * `TABLE_1_ID`, `TABLE_2_ID`: Optional. A list of the tables in the database that the data agent is suggested to use—for example, `"loan"`, `"client"`, `"disp"`.
  * `billing_project`: The ID of the billing project where you've enabled the required APIs.
  * `location`: The location where your context set resides—for example, `global`.
  * `your_context_set_id`: If you created advanced context for the agent, the ID of your context set.



### Connect to Cloud SQL for MySQL and Cloud SQL for PostgreSQL data

The Conversational Analytics API uses a `database_reference` field in the `sql` field to connect to your Cloud SQL instance.

The following example defines a connection to a Cloud SQL for MySQL or a Cloud SQL for PostgreSQL database.
    
    
    sql_data_source = {
        "cloud_sql_reference": {
            "database_reference":
              {
                "project_id":"PROJECT_ID",
                "region":"REGION",
                "cluster_id":"CLUSTER_ID",
                "instance_id":"INSTANCE_ID",
                "database_id":"DATABASE_ID",
                "table_ids":["TABLE_1_ID", "TABLE_2_ID"]
              }
              # Optional: Include this if you have pre-authored context for the agent
              # "agent_context_reference": {
              #     "context_set_id": f"projects/billing_project/locations/location/contextSets/your_context_set_id"
              # }
        }
    }
    

Replace the sample values as follows:

  * `PROJECT_ID`: The ID of the Google Cloud project that contains the Cloud SQL instance.
  * `REGION`: The region where the Cloud SQL instance resides—for example, `us-central1`.
  * `CLUSTER_ID`: The ID of the Cloud SQL cluster.
  * `INSTANCE_ID`: The ID of the Cloud SQL instance.
  * `DATABASE_ID`: The name of the target database—for example, `financial`.
  * `TABLE_1_ID`, `TABLE_2_ID`: Optional. A list of the tables in the database that the data agent is suggested to use—for example, `"loan"`, `"client"`, `"disp"`.
  * `billing_project`: The ID of the billing project where you've enabled the required APIs.
  * `location`: The location where your context set resides—for example, `global`.
  * `your_context_set_id`: If you created advanced context for the agent, the ID of your context set.



### Connect to Spanner data

The Conversational Analytics API uses a `database_reference` field in the `spanner` field to connect to your Spanner instance.

The following example defines a connection to a Spanner database.
    
    
    spanner_data_sources = {
        "spanner_reference": {
            "database_reference": {
                "project_id": "PROJECT_ID",
                "region": location,
                "engine": GOOGLE_SQL,
                "instance_id": "INSTANCE_ID",
                "database_id": "DATABASE",
                "table_ids":["TABLE_1_ID", "TABLE_2_ID"]
            },
            # Optional: Include this if you have pre-authored context for the agent
            # "agent_context_reference": {
            #     "context_set_id": f"projects/billing_project/locations/location/contextSets/your_context_set_id"
            # }
        }
    }
    

Replace the sample values as follows:

  * `PROJECT_ID`: The ID of the Google Cloud project that contains the Spanner instance.
  * `INSTANCE_ID`: The ID of the Spanner instance.
  * `DATABASE`: The name of the target database—for example, `financial`.
  * `TABLE_1_ID`, `TABLE_2_ID`: A list of the tables in the database that the data agent is suggested to use—for example, `"loan"`, `"client"`, `"disp"`.
  * `billing_project`: the ID of the billing project where you've enabled the required APIs.
  * `location`: the location where your context set resides—for example, `global`.
  * `your_context_set_id`: if you created advanced context for the agent, the ID of your context set.



## Create a data agent

The following sample code demonstrates how to create the data agent synchronously or asynchronously by sending an HTTP `POST` request to the data agent creation endpoint. The request payload includes the following details:

  * The full resource name for the agent. This value includes the project ID, location, and a unique identifier for the agent.
  * The data agent's description.
  * The data agent's context, including the system description (defined in Configure initial settings and authentication) and the data source that the agent uses (defined in Connect to a data source).



You can optionally protect the data agent with customer-managed encryption keys (CMEK) by including the `kms_key` field in the request payload when you create the data agent. For more information, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/cmek).

You can also optionally enable advanced analysis with Python by including the `options` parameter in the request payload. See the [REST Resource: projects.locations.dataAgents](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/reference/rest/v1/projects.locations.dataAgents#context) for more information about the `options` parameter and the options that you can configure for the conversation.

**Warning:** The Python code that data agents return is designed to execute within a secure, Google-managed sandbox. Executing this code in a local or other unverified environment bypasses the sandbox's security protections and can expose your system to security risks, such as the execution of malicious code. For guidance on how to safely inspect and handle agent-generated Python code, see [How can I safely inspect and handle agent-generated Python code?](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/frequently-asked-questions#safe-python)

The following example uses the `bigquery_data_sources` variable that was created in the section on connecting to BigQuery to configure the data agent to connect to a BigQuery table.

To use Looker data instead, replace `bigquery_data_sources` with `looker_data_source`.

To use Data Studio data instead, replace `bigquery_data_sources` with `looker_studio_data_source`.

To use AlloyDB data instead, replace `bigquery_data_sources` with `alloydb_data_source`.

To use Cloud SQL data instead, replace `bigquery_data_sources` with `sql_data_source`.

To use Spanner data instead, replace `bigquery_data_sources` with `spanner_data_sources`.

### Synchronous
    
    
    data_agent_url = f"https://geminidataanalytics.googleapis.com/v1beta/projects/{billing_project}/locations/{location}/dataAgents:createSync"
    
    data_agent_id = "DATA_AGENT_ID"
    
    # Optional: If using CMEK, replace the empty strings with your KMS key details.
    kms_project_id = ""  # KMS_PROJECT_ID (Defaults to billing_project if empty)
    key_ring_name = ""   # KEY_RING_NAME
    key_name = ""        # KEY_NAME
    
    data_agent_payload = {
          "name": f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}", # Optional
          "description": "This is the description of the data agent.", # Optional
          "data_analytics_agent": {
              "published_context": {
                  "datasource_references": bigquery_data_sources,
                  "system_instruction": system_instruction,
                  "options": {
                      # Optional: To enable advanced analysis with Python
                      "analysis": {
                          "python": {
                              "enabled": True
                          }
                      },
                      # Optional: To limit query costs to 100MiB
                      "datasource": {
                          "bigQueryMaxBilledBytes": "104857600"
                      }
                  }
              }
          }
      }
    
    # If key details are provided, construct and add the kms_key field.
    if key_ring_name and key_name:
      if not kms_project_id:
        kms_project_id = billing_project
      data_agent_payload["kms_key"] = f"projects/{kms_project_id}/locations/{location}/keyRings/{key_ring_name}/cryptoKeys/{key_name}"
    
    params = {"data_agent_id": data_agent_id} # Optional
    
    data_agent_response = requests.post(
        data_agent_url, params=params, json=data_agent_payload, headers=headers
    )
    
    if data_agent_response.status_code == 200:
        print("Data Agent created successfully!")
        print(json.dumps(data_agent_response.json(), indent=2))
    else:
        print(f"Error creating Data Agent: {data_agent_response.status_code}")
        print(data_agent_response.text)
    

### Asynchronous
    
    
    data_agent_url = f"{base_url}/v1/projects/{billing_project}/locations/{location}/dataAgents"
    
    data_agent_id = "DATA_AGENT_ID"
    
    # Optional: If using CMEK, replace the empty strings with your KMS key details.
    kms_project_id = ""  # KMS_PROJECT_ID (Defaults to billing_project if empty)
    key_ring_name = ""   # KEY_RING_NAME
    key_name = ""        # KEY_NAME
    
    data_agent_payload = {
          "name": f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}", # Optional
          "description": "This is the description of the data agent.", # Optional
          "data_analytics_agent": {
              "published_context": {
                  "datasource_references": bigquery_data_sources,
                  "system_instruction": system_instruction,
                  "options": {
                      # Optional: To enable advanced analysis with Python
                      "analysis": {
                          "python": {
                              "enabled": True
                          }
                      },
                      # Optional: To limit query costs to 100MiB
                      "datasource": {
                          "bigQueryMaxBilledBytes": "104857600"
                      }
                  }
              }
          }
      }
    
    # If key details are provided, construct and add the kms_key field.
    if key_ring_name and key_name:
      if not kms_project_id:
        kms_project_id = billing_project
      data_agent_payload["kms_key"] = f"projects/{kms_project_id}/locations/{location}/keyRings/{key_ring_name}/cryptoKeys/{key_name}"
    
    params = {"data_agent_id": data_agent_id} # Optional
    
    data_agent_response = requests.post(
        data_agent_url, params=params, json=data_agent_payload, headers=headers
    )
    
    if data_agent_response.status_code == 200:
        print("Data Agent created successfully!")
        print(json.dumps(data_agent_response.json(), indent=2))
    else:
        print(f"Error creating Data Agent: {data_agent_response.status_code}")
        print(data_agent_response.text)
    

Replace the sample values as follows:

  * DATA_AGENT_ID: A unique identifier for the data agent. This value is used in the agent's resource name and as the `data_agent_id` URL query parameter.
  * KMS_PROJECT_ID: If using CMEK, the project ID where the key is hosted. If not provided, this defaults to your billing project.
  * KEY_RING_NAME: If using CMEK, the name of your Cloud KMS key ring.
  * KEY_NAME: If using CMEK, the name of your Cloud KMS key.
  * This is the description of the data agent.: A description for the data agent.



## Create a conversation

The following sample code demonstrates how to create a conversation with your data agent.

You can optionally protect the conversation with CMEK by including the `kms_key` field in the request payload when you create the conversation. For more information, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/cmek).
    
    
    conversation_url = f"{base_url}/v1/projects/{billing_project}/locations/{location}/conversations"
    
    data_agent_id = "DATA_AGENT_ID"
    conversation_id = "CONVERSATION_ID"
    
    # Optional: If using CMEK, replace the empty strings with your KMS key details.
    kms_project_id = ""  # KMS_PROJECT_ID (Defaults to billing_project if empty)
    key_ring_name = ""   # KEY_RING_NAME
    key_name = ""        # KEY_NAME
    
    conversation_payload = {
        "agents": [
            f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}"
        ],
        "name": f"projects/{billing_project}/locations/{location}/conversations/{conversation_id}",
    }
    
    # If key details are provided, construct and add the kms_key field.
    if key_ring_name and key_name:
      if not kms_project_id:
        kms_project_id = billing_project
      conversation_payload["kms_key"] = f"projects/{kms_project_id}/locations/{location}/keyRings/{key_ring_name}/cryptoKeys/{key_name}"
    
    params = {
        "conversation_id": conversation_id
    }
    
    conversation_response = requests.post(conversation_url, headers=headers, params=params, json=conversation_payload)
    
    if conversation_response.status_code == 200:
        print("Conversation created successfully!")
        print(json.dumps(conversation_response.json(), indent=2))
    else:
        print(f"Error creating Conversation: {conversation_response.status_code}")
        print(conversation_response.text)
    

Replace the sample values as follows:

  * DATA_AGENT_ID: The ID of the data agent, as defined in the sample code block in Create a data agent.
  * CONVERSATION_ID: A unique identifier for the conversation.
  * KMS_PROJECT_ID: If using CMEK, the project ID where the key is hosted. If not provided, this defaults to your billing project.
  * KEY_RING_NAME: If using CMEK, the name of your Cloud KMS key ring.
  * KEY_NAME: If using CMEK, the name of your Cloud KMS key.



## Manage data agents and conversations

The following code samples show how to manage your data agents and conversations by using the Conversational Analytics API. You can perform the following tasks:

  * Get a data agent
  * List data agents
  * List accessible data agents
  * Update a data agent
  * Get the IAM policy for a data agent
  * Set the IAM policy for a data agent
  * Delete a data agent
  * Get a conversation
  * List conversations
  * List messages in a conversation



### Get a data agent

The following sample code demonstrates how to fetch an existing data agent by sending an HTTP `GET` request to the data agent resource URL.
    
    
    data_agent_id = "DATA_AGENT_ID"
    data_agent_url = f"{base_url}/v1/projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}"
    
    data_agent_response = requests.get(
        data_agent_url, headers=headers
    )
    
    if data_agent_response.status_code == 200:
        print("Fetched Data Agent successfully!")
        print(json.dumps(data_agent_response.json(), indent=2))
    else:
        print(f"Error: {data_agent_response.status_code}")
        print(data_agent_response.text)
    

In the previous example, replace DATA_AGENT_ID with the ID of the data agent that you want to fetch.

### List data agents

The following code demonstrates how to list all the data agents for a given project by sending an HTTP `GET` request to the `dataAgents` endpoint.

To list all agents, you must have the `geminidataanalytics.dataAgents.list` permission on the project. For more information on which IAM roles include this permission, see the list of [predefined roles](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control#predefined-roles).
    
    
    billing_project = "BILLING_PROJECT"
    data_agent_url = f"{base_url}/v1/projects/{billing_project}/locations/{location}/dataAgents"
    
    data_agent_response = requests.get(
        data_agent_url, headers=headers
    )
    
    if data_agent_response.status_code == 200:
        print("Data Agents Listed successfully!")
        print(json.dumps(data_agent_response.json(), indent=2))
    else:
        print(f"Error Listing Data Agents: {data_agent_response.status_code}")
    

Replace BILLING_PROJECT with the ID of your billing project.

### List accessible data agents

The following code demonstrates how to list all the accessible data agents for a given project by sending an HTTP `GET` request to the `dataAgents:listAccessible` endpoint.
    
    
    billing_project = "BILLING_PROJECT"
    creator_filter = "CREATOR_FILTER"
    data_agent_url = f"{base_url}/v1/projects/{billing_project}/locations/{location}/dataAgents:listAccessible"
    
    params = {
        "creator_filter": creator_filter
    }
    
    data_agent_response = requests.get(
        data_agent_url, headers=headers, params=params
    )
    
    if data_agent_response.status_code == 200:
        print("Accessible Data Agents Listed successfully!")
        print(json.dumps(data_agent_response.json(), indent=2))
    else:
        print(f"Error Listing Accessible Data Agents: {data_agent_response.status_code}")
    

Replace the sample values as follows:

  * BILLING_PROJECT: The ID of your billing project.
  * CREATOR_FILTER: The filter to apply based on the creator of the data agent. Possible values include `NONE` (default), `CREATOR_ONLY`, and `NOT_CREATOR_ONLY`.



### Update a data agent

The following sample code demonstrates how to update a data agent synchronously or asynchronously by sending an HTTP `PATCH` request to the data agent resource URL. The request payload includes the new values for the fields that you want to change, and the request parameters include an `updateMask` parameter, which specifies the fields to be updated.

### Synchronous
    
    
    data_agent_id = "DATA_AGENT_ID"
    billing_project = "BILLING_PROJECT"
    
    data_agent_url = f"{base_url}/v1/projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}:updateSync"
    
    payload = {
        "description": "Updated description of the data agent.",
        "data_analytics_agent": {
            "published_context": {
                "datasource_references": bigquery_data_sources,
                "system_instruction": system_instruction
            }
        },
    }
    
    fields = ["description", "data_analytics_agent"]
    params = {
        "updateMask": ",".join(fields)
    }
    
    data_agent_response = requests.patch(
        data_agent_url, headers=headers, params=params, json=payload
    )
    
    if data_agent_response.status_code == 200:
        print("Data Agent updated successfully!")
        print(json.dumps(data_agent_response.json(), indent=2))
    else:
        print(f"Error Updating Data Agent: {data_agent_response.status_code}")
        print(data_agent_response.text)
    

### Asynchronous
    
    
    data_agent_id = "DATA_AGENT_ID"
    billing_project = "BILLING_PROJECT"
    
    data_agent_url = f"{base_url}/v1/projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}"
    
    payload = {
        "description": "Updated description of the data agent.",
        "data_analytics_agent": {
            "published_context": {
                "datasource_references": bigquery_data_sources,
                "system_instruction": system_instruction
            }
        },
    }
    
    fields = ["description", "data_analytics_agent"]
    params = {
        "updateMask": ",".join(fields)
    }
    
    data_agent_response = requests.patch(
        data_agent_url, headers=headers, params=params, json=payload
    )
    
    if data_agent_response.status_code == 200:
        print("Data Agent updated successfully!")
        print(json.dumps(data_agent_response.json(), indent=2))
    else:
        print(f"Error Updating Data Agent: {data_agent_response.status_code}")
        print(data_agent_response.text)
    

Replace the sample values as follows:

  * DATA_AGENT_ID: The ID of the data agent that you want to update.
  * BILLING_PROJECT: The ID of your billing project.
  * Updated description of the data agent.: A new description for the data agent.



### Get the IAM policy for a data agent

The following sample code demonstrates how to fetch the IAM policy for a data agent by sending an HTTP `POST` request to the data agent URL. The request payload includes the data agent path.
    
    
    billing_project = "BILLING_PROJECT"
    data_agent_id = "DATA_AGENT_ID"
    
    data_agent_url = f"{base_url}/v1/projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}:getIamPolicy"
    
    # Request body
    payload = {
        "resource": f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}"
    }
    
    data_agent_response = requests.post(
        data_agent_url, headers=headers, json=payload
    )
    
    if data_agent_response.status_code == 200:
        print("IAM Policy fetched successfully!")
        print(json.dumps(data_agent_response.json(), indent=2))
    else:
        print(f"Error fetching IAM policy: {data_agent_response.status_code}")
        print(data_agent_response.text)
    

Replace the sample values as follows:

  * BILLING_PROJECT: The ID of your billing project.
  * DATA_AGENT_ID: The ID of the data agent for which you want to get the IAM policy.



### Set the IAM policy for a data agent

To share an agent, you can use the [`setIamPolicy` method](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/reference/rest/v1/projects.locations.dataAgents/setIamPolicy) to assign IAM roles to users on a specific agent. The following sample code demonstrates how to make a `POST` call to the data agent URL with a payload that includes bindings. The binding specifies which roles should be assigned to which users.

**Important:** The `setIamPolicy` API call overrides existing permissions for the resource. To preserve existing policies, call the Get IAM policy API to fetch the existing policy, and then pass the existing policy along with any additional changes in the call to `SetIamPolicy`.
    
    
    billing_project = "BILLING_PROJECT"
    data_agent_id = "DATA_AGENT_ID"
    role = "roles/geminidataanalytics.dataAgentEditor"
    users = "222larabrown@gmail.com, cloudysanfrancisco@gmail.com"
    
    data_agent_url = f"{base_url}/v1/projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}:setIamPolicy"
    
    # Request body
    payload = {
        "policy": {
            "bindings": [
                {
                    "role": role,
                    "members": [
                        f"user:{i.strip()}" for i in users.split(",")
                    ]
                }
            ]
        }
    }
    
    data_agent_response = requests.post(
        data_agent_url, headers=headers, json=payload
    )
    
    if data_agent_response.status_code == 200:
        print("IAM Policy set successfully!")
        print(json.dumps(data_agent_response.json(), indent=2))
    else:
        print(f"Error setting IAM policy: {data_agent_response.status_code}")
        print(data_agent_response.text)
    

Replace the sample values as follows:

  * BILLING_PROJECT: The ID of your billing project.
  * DATA_AGENT_ID: The ID of the data agent for which you want to set the IAM policy.
  * 222larabrown@gmail.com, cloudysanfrancisco@gmail.com: A comma-separated list of user emails to which you want to grant the specified role.



### Delete a data agent

The following sample code demonstrates how to delete a data agent synchronously or asynchronously by sending an HTTP `DELETE` request to the data agent resource URL. When you delete a data agent, it enters a 30-day soft-deletion period where it cannot be recovered. For more information, see [Data retention and deletion](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/retention-deletion).

### Synchronous
    
    
    billing_project = "BILLING_PROJECT"
    data_agent_id = "DATA_AGENT_ID"
    
    data_agent_url = f"{base_url}/v1/projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}:deleteSync"
    
    data_agent_response = requests.delete(
        data_agent_url, headers=headers
    )
    
    if data_agent_response.status_code == 200:
        print("Data Agent deleted successfully!")
        print(json.dumps(data_agent_response.json(), indent=2))
    else:
        print(f"Error Deleting Data Agent: {data_agent_response.status_code}")
        print(data_agent_response.text)
    

### Asynchronous
    
    
    billing_project = "BILLING_PROJECT"
    data_agent_id = "DATA_AGENT_ID"
    
    data_agent_url = f"{base_url}/v1/projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}"
    
    data_agent_response = requests.delete(
        data_agent_url, headers=headers
    )
    
    if data_agent_response.status_code == 200:
        print("Data Agent deleted successfully!")
        print(json.dumps(data_agent_response.json(), indent=2))
    else:
        print(f"Error Deleting Data Agent: {data_agent_response.status_code}")
        print(data_agent_response.text)
    

Replace the sample values as follows:

  * BILLING_PROJECT: The ID of your billing project.
  * DATA_AGENT_ID: The ID of the data agent that you want to delete.



### Get a conversation

The following sample code demonstrates how to fetch an existing conversation by sending an HTTP `GET` request to the conversation resource URL.
    
    
    billing_project = "BILLING_PROJECT"
    conversation_id = "CONVERSATION_ID"
    
    conversation_url = f"{base_url}/v1/projects/{billing_project}/locations/{location}/conversations/{conversation_id}"
    
    conversation_response = requests.get(conversation_url, headers=headers)
    
    # Handle the response
    if conversation_response.status_code == 200:
        print("Conversation fetched successfully!")
        print(json.dumps(conversation_response.json(), indent=2))
    else:
        print(f"Error while fetching conversation: {conversation_response.status_code}")
        print(conversation_response.text)
    

Replace the sample values as follows:

  * BILLING_PROJECT: The ID of your billing project.
  * CONVERSATION_ID: The ID of the conversation that you want to fetch.



### List conversations

The following sample code demonstrates how to list conversations for a given project by sending an HTTP `GET` request to the `conversations` endpoint.

By default, this method returns the conversations that you created. Admins (users with the [`cloudaicompanion.topicAdmin` IAM role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.topicAdmin)) can see all conversations within the project.
    
    
    billing_project = "BILLING_PROJECT"
    conversation_url = f"{base_url}/v1/projects/{billing_project}/locations/{location}/conversations"
    
    conversation_response = requests.get(conversation_url, headers=headers)
    
    # Handle the response
    if conversation_response.status_code == 200:
        print("Conversation fetched successfully!")
        print(json.dumps(conversation_response.json(), indent=2))
    else:
        print(f"Error while fetching conversation: {conversation_response.status_code}")
        print(conversation_response.text)
    

Replace BILLING_PROJECT with the ID of the billing project where you've enabled the required APIs.

### List messages in a conversation

The following sample code demonstrates how to list all the messages in a conversation by sending an HTTP `GET` request to the conversation's `messages` endpoint.

To list messages, you must have the [`cloudaicompanion.topics.get` permission](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#gemini-for-google-cloud-api-roles) on the conversation.

**Note:** This list operation also supports pagination.
    
    
    billing_project = "BILLING_PROJECT"
    
    conversation_id = "CONVERSATION_ID"
    
    conversation_url = f"{base_url}/v1/projects/{billing_project}/locations/{location}/conversations/{conversation_id}/messages"
    
    conversation_response = requests.get(conversation_url, headers=headers)
    
    # Handle the response
    if conversation_response.status_code == 200:
        print("Conversation fetched successfully!")
        print(json.dumps(conversation_response.json(), indent=2))
    else:
        print(f"Error while fetching conversation: {conversation_response.status_code}")
        print(conversation_response.text)
    

Replace the sample values as follows:

  * BILLING_PROJECT: The ID of your billing project.
  * CONVERSATION_ID: The ID of the conversation for which you want to list messages.



### Delete a conversation

The following sample code demonstrates how to delete a conversation by sending an HTTP `DELETE` request to the conversation resource URL. Admins (users with the [cloudaicompanion.topicAdmin Identity and Access Management role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.topicAdmin)) or users with the [`cloudaicompanion.topics.delete` Identity and Access Management permission](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.topics.delete) can delete conversations within the project.
    
    
    billing_project = "BILLING_PROJECT"
    conversation_id = "CONVERSATION_ID"
    
    conversation_url = f"{base_url}/v1/projects/{billing_project}/locations/{location}/conversations/{conversation_id}"
    
    conversation_response = requests.delete(conversation_url, headers=headers)
    
    # Handle the response
    if conversation_response.status_code == 200:
        print("Conversation deleted successfully!")
        print(json.dumps(conversation_response.json(), indent=2))
    else:
        print(f"Error while deleting conversation: {conversation_response.status_code}")
        print(conversation_response.text)
    

Replace the sample values as follows:

  * BILLING_PROJECT: The ID of your billing project.
  * CONVERSATION_ID: The ID of the conversation that you want delete.



## Use the API to ask questions

After you create a data agent and, for stateful chat, a conversation, you can send queries to the agent.

When you send a query, the API returns a stream of [`Message`](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/reference/rest/v1/Message) objects. This stream can contain different types of messages, including text, data tables, and charts. Text messages can provide insight into the agent's reasoning, report on its progress, or give the final answer. The purpose of each text message is indicated by its [`TextType`](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/reference/rest/v1/Message#TextType) value:

  * `THOUGHT`: Shows the agent's internal thought process as it plans how to answer your query. `THOUGHT` messages provide step-by-step insight into the agent's reasoning and decision-making process and contain two parts: `parts[0]` is the thought summary, which briefly summarizes the full thought text, and `parts[1]` is the full thought text.
  * `PROGRESS`: Reports the agent's progress on an action, such as data retrieval or a tool that's being invoked. This value is returned only for Looker data sources and contains two parts: `parts[0]` is the summary, and `parts[1]` is the full progress text.
  * `FINAL_RESPONSE`: Provides the final answer to your query.



The examples in the following section use the helper functions that are defined in Helper Python functions to stream chat responses to process and display each message in the API's streamed response. For guidance on how to render these messages in a user interface when you're using Looker data sources, see [Render agent responses for Looker data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/render-looker-data).

### Ask questions with stateful and stateless chat

You can interact with the API in the following primary modes:

  * **Stateful chat** : Google Cloud stores and manages the conversation history. Stateful chat is inherently multi-turn, as the API retains context from previous messages. You only need to send the current message for each turn.
  * **Stateless chat** : Your application manages the conversation history. You must include the relevant previous messages with each new message. For detailed examples of how to manage multi-turn conversations in stateless mode, see Create a stateless multi-turn conversation.



The following examples demonstrate how to use the API for stateful and stateless chat by making a `POST` request to the `:chat` endpoint.

**Caution:** The code samples in this section use the standard Python `requests` library to demonstrate HTTP streaming. Standard HTTP or REST clients cannot read HTTP/2 trailers. If a fatal error (such as a timeout) occurs while streaming, the API might return a generic error message, such as `503 Connection reset by peer` or `500 Internal Server Error`. For production applications, we strongly recommend using the [Python SDK](https://cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/), which uses gRPC to correctly parse these trailing errors. 

### Stateful chat

#### Send a stateful chat request with a conversation reference

The following sample code demonstrates how to ask the API questions using the conversation that you defined in previous steps. This sample uses a `get_stream` helper function to stream the response.

**Note:** If your agent uses a Looker data source, you must uncomment the `"credentials": looker_credentials` line.
    
    
    chat_url = f"{base_url}/v1/projects/{billing_project}/locations/{location}:chat"
    
    data_agent_id = "DATA_AGENT_ID"
    conversation_id = "CONVERSATION_ID"
    
    # Construct the payload
    chat_payload = {
        "parent": f"projects/{billing_project}/locations/{location}",
        # "credentials": looker_credentials,
        "messages": [
            {
                "userMessage": {
                    "text": "Make a bar graph for the top 5 states by the total number of airports"
                }
            }
        ],
        "conversation_reference": {
            "conversation": f"projects/{billing_project}/locations/{location}/conversations/{conversation_id}",
            "data_agent_context": {
                "data_agent": f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}",
            }
        }
    }
    
    # Call the get_stream function to stream the response
    get_stream(chat_url, chat_payload)
    
    

Replace the sample values as follows:

  * DATA_AGENT_ID: The ID of the data agent, as defined in the sample code block in Create a data agent.
  * CONVERSATION_ID: A unique identifier for the conversation.
  * `Make a bar graph for the top 5 states by the total number of airports` was used as the sample prompt.



### Stateless chat

The following examples show how to send stateless requests by using either a data agent reference or inline context.

#### Send a stateless chat request with a data agent reference

The following sample code demonstrates how to ask the API a stateless question by using the data agent that you defined in previous steps. This sample uses a `get_stream` helper function to stream the response.

**Note:** If your agent uses a Looker data source, you must uncomment the `"credentials": looker_credentials` line.
    
    
    chat_url = f"{base_url}/v1/projects/{billing_project}/locations/{location}:chat"
    
    data_agent_id = "DATA_AGENT_ID"
    
    # Construct the payload
    chat_payload = {
        "parent": f"projects/{billing_project}/locations/{location}",
        # "credentials": looker_credentials,
        "messages": [
            {
                "userMessage": {
                    "text": "Make a bar graph for the top 5 states by the total number of airports"
                }
            }
        ],
        "data_agent_context": {
            "data_agent": f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}",
        }
    }
    
    # Call the get_stream function to stream the response
    get_stream(chat_url, chat_payload)
    

Replace the sample values as follows:

  * DATA_AGENT_ID: The ID of the data agent, as defined in the sample code block in Create a data agent.
  * `Make a bar graph for the top 5 states by the total number of airports` was used as the sample prompt.



#### Send a stateless chat request with inline context

The following sample code demonstrates how to ask the API a stateless question by using inline context. This sample uses a `get_stream` helper function to stream the response and uses a BigQuery data source as an example.

**Note:** If your agent uses a Looker data source, you must uncomment the `"credentials": looker_credentials` line in the following code samples.

You can also optionally enable advanced analysis with Python by including the `options` parameter in the request payload. See the [REST Resource: projects.locations.dataAgents](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/reference/rest/v1/projects.locations.dataAgents#context) page for more information about the `options` parameter and the options that you can configure for the conversation.

**Warning:** The Python code that data agents return is designed to execute within a secure, Google-managed sandbox. Executing this code in a local or other unverified environment bypasses the sandbox's security protections and can expose your system to security risks, such as the execution of malicious code. For guidance on how to safely inspect and handle agent-generated Python code, see [How can I safely inspect and handle agent-generated Python code?](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/frequently-asked-questions#safe-python)
    
    
    chat_url = f"{base_url}/v1/projects/{billing_project}/locations/{location}:chat"
    
    # Construct the payload
    chat_payload = {
        "parent": f"projects/{billing_project}/locations/{location}",
        # "credentials": looker_credentials,
        "messages": [
            {
                "userMessage": {
                    "text": "Make a bar graph for the top 5 states by the total number of airports"
                }
            }
        ],
        "inline_context": {
            "datasource_references": bigquery_data_sources,
              # Optional: To enable advanced analysis with Python, include the following options block:
              "options": {
                  "analysis": {
                      "python": {
                          "enabled": True
                      }
                  }
              }
        }
    }
    
    # Call the get_stream function to stream the response
    get_stream(chat_url, chat_payload)
    

The following sample code demonstrates how to ask the API a stateless question by using inline context and an AlloyDB data source as an example.
    
    
    chat_url = f"https://geminidataanalytics.googleapis.com/v1/projects/{billing_project}/locations/{location}:chat"
    
    # The natural language question to ask the data agent
    user_prompt = "What is the average loan amount in the US?"  # Replace with your question
    
    # Construct the payload
    chat_payload = {
        "parent": f"projects/{billing_project}/locations/{location}",
        # "credentials": looker_credentials,
        "messages": [
            {
                "userMessage": {
                    "text": user_prompt
                }
            }
        ],
        "data_agent_context": {
              "data_agent": f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}",
        }
    }
    
    print(f"Sending prompt to :chat: '{user_prompt}'")
    print(f"Endpoint: {chat_url}")
    print(f"Payload: {json.dumps(chat_payload, indent=2)}")
    
    get_stream(chat_url, chat_payload)
    

## Create a stateless multi-turn conversation

To ask follow-up questions in a stateless conversation, your application must manage the conversation context by sending the entire message history with each new request. Multi-turn conversations let you send follow-up questions that build on previous conversation turns.

The following example defines and calls a `multi_turn_conversation` function to manage conversation context by storing messages in a list. The `multi_turn_conversation` function calls the `get_stream_multi_turn` function to parse the streaming API response and update the `conversation_messages` list. This process preserves the context for subsequent turns. For the code for `get_stream_multi_turn` and other required helper functions, see Streaming chat helper functions.

The following code sample uses a data agent reference. To use inline context instead, uncomment the `inline_context` block and comment out the `data_agent_context` block. The inline context sample uses a BigQuery data source.

If your agent uses a Looker data source, you must uncomment the `"credentials": looker_credentials` line.
    
    
    chat_url = f"{base_url}/v1/projects/{billing_project}/locations/{location}:chat"
    
    # List that is used to track previous turns and is reused across requests
    conversation_messages = []
    
    data_agent_id = "DATA_AGENT_ID"
    
    # Helper function for calling the API
    def multi_turn_conversation(msg):
    
      userMessage = {
          "userMessage": {
              "text": msg
          }
      }
    
      # Send a multi-turn request by including previous turns and the new message
      conversation_messages.append(userMessage)
    
      # Construct the payload
      chat_payload = {
          "parent": f"projects/{billing_project}/locations/{location}",
          # "credentials": looker_credentials,
          "messages": conversation_messages,
          # Use a data agent reference
          "data_agent_context": {
              "data_agent": f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}",
          },
          # Use inline context
          # "inline_context": {
          #     "datasource_references": bigquery_data_sources,
          # }
      }
    
      # Call the get_stream_multi_turn helper function to stream the response
      get_stream_multi_turn(chat_url, chat_payload, conversation_messages)
    

In the previous example, replace DATA_AGENT_ID with the ID of the data agent, as defined in the sample code block in Create a data agent.

You can call the `multi_turn_conversation` helper function for each turn of the conversation. The following sample code shows how to send an initial request and then a follow-up request that builds on the previous response:
    
    
    # Send first-turn request
    multi_turn_conversation("Which species of tree is most prevalent?")
    
    # Send follow-up-turn request
    multi_turn_conversation("Can you show me the results as a bar chart?")
    

In the previous example, replace the sample values as follows:

  * Which species of tree is most prevalent?: A natural language question to send to the data agent.
  * Can you show me the results as a bar chart?: A follow-up question that builds on or refines the previous question.



## Define helper functions

The following section contains helper function definitions that are used in the previous code samples to parse responses from the API and display the results.

### Streaming chat helper functions

The following functions parse and display the streaming response from the API for standard (single-turn) chat requests.

#### Show helper functions for streaming chat responses
    
    
        def is_json(str):
          try:
              json_object = json_lib.loads(str)
          except ValueError as e:
              return False
          return True
    
        def handle_text_response(resp):
          parts = resp['parts']
          full_text = "".join(parts)
          if "\n" not in full_text and len(full_text) > 80:
            wrapped_text = textwrap.fill(full_text, width=80)
            print(wrapped_text)
          else:
            print(full_text)
    
        def get_property(data, field_name, default = ''):
          return data[field_name] if field_name in data else default
    
        def display_schema(data):
          fields = data['fields']
          df = pd.DataFrame({
            "Column": map(lambda field: get_property(field, 'name'), fields),
            "Type": map(lambda field: get_property(field, 'type'), fields),
            "Description": map(lambda field: get_property(field, 'description', '-'), fields),
            "Mode": map(lambda field: get_property(field, 'mode'), fields)
          })
          display(df)
    
        def display_section_title(text):
          display(HTML('<h2>{}</h2>'.format(text)))
    
        def format_bq_table_ref(table_ref):
          return '{}.{}.{}'.format(table_ref['projectId'], table_ref['datasetId'], table_ref['tableId'])
    
        def format_looker_table_ref(table_ref):
          return 'lookmlModel: {}, explore: {}, lookerInstanceUri: {}'.format(table_ref['lookmlModel'], table_ref['explore'], table_ref['lookerInstanceUri'])
    
        def display_datasource(datasource):
          source_name = ''
    
          if 'studioDatasourceId' in datasource:
            source_name = datasource['studioDatasourceId']
          elif 'lookerExploreReference' in datasource:
            source_name = format_looker_table_ref(datasource['lookerExploreReference'])
          else:
            source_name = format_bq_table_ref(datasource['bigqueryTableReference'])
    
          print(source_name)
          display_schema(datasource['schema'])
    
        def handle_schema_response(resp):
          if 'query' in resp:
            print(resp['query']['question'])
          elif 'result' in resp:
            display_section_title('Schema resolved')
            print('Data sources:')
            for datasource in resp['result']['datasources']:
              display_datasource(datasource)
    
        def handle_data_response(resp):
          if 'query' in resp:
            query = resp['query']
            display_section_title('Retrieval query')
            print('Query name: {}'.format(query['name']))
            if 'question' in query:
              print('Question: {}'.format(query['question']))
            if 'datasources' in query:
              print('Data sources:')
              for datasource in query['datasources']:
                display_datasource(datasource)
          elif 'generatedSql' in resp:
            display_section_title('SQL generated')
            print(resp['generatedSql'])
          elif 'result' in resp:
            display_section_title('Data retrieved')
    
            fields = map(lambda field: get_property(field, 'name'), resp['result']['schema']['fields'])
            dict = {}
    
            for field in fields:
              dict[field] = map(lambda el: get_property(el, field), resp['result']['data'])
    
            display(pd.DataFrame(dict))
    
        def handle_chart_response(resp):
          if 'query' in resp:
            print(resp['query']['instructions'])
          elif 'result' in resp:
            vegaConfig = resp['result']['vegaConfig']
            alt.Chart.from_json(json_lib.dumps(vegaConfig)).display();
    
        def handle_error(resp):
          display_section_title('Error')
          print('Code: {}'.format(resp['code']))
          print('Message: {}'.format(resp['message']))
    
        def get_stream(url, json):
          s = requests.Session()
    
          acc = ''
    
          with s.post(url, json=json, headers=headers, stream=True) as resp:
            for line in resp.iter_lines():
              if not line:
                continue
    
              decoded_line = str(line, encoding='utf-8')
    
              if decoded_line == '[{':
                acc = '{'
              elif decoded_line == '}]':
                acc += '}'
              elif decoded_line == ',':
                continue
              else:
                acc += decoded_line
    
              if not is_json(acc):
                continue
    
              data_json = json_lib.loads(acc)
    
              if not 'systemMessage' in data_json:
                if 'error' in data_json:
                    handle_error(data_json['error'])
                continue
    
              if 'text' in data_json['systemMessage']:
                handle_text_response(data_json['systemMessage']['text'])
              elif 'schema' in data_json['systemMessage']:
                handle_schema_response(data_json['systemMessage']['schema'])
              elif 'data' in data_json['systemMessage']:
                handle_data_response(data_json['systemMessage']['data'])
              elif 'chart' in data_json['systemMessage']:
                handle_chart_response(data_json['systemMessage']['chart'])
              else:
                colored_json = highlight(acc, lexers.JsonLexer(), formatters.TerminalFormatter())
                print(colored_json)
                print('\n')
                acc = ''
    
        def get_stream_multi_turn(url, json, conversation_messages):
            s = requests.Session()
    
            acc = ''
    
            with s.post(url, json=json, headers=headers, stream=True) as resp:
                for line in resp.iter_lines():
                    if not line:
                        continue
    
                    decoded_line = str(line, encoding='utf-8')
    
                    if decoded_line == '[{':
                        acc = '{'
                    elif decoded_line == '}]':
                        acc += '}'
                    elif decoded_line == ',':
                        continue
                    else:
                        acc += decoded_line
    
                    if not is_json(acc):
                        continue
    
                    data_json = json_lib.loads(acc)
                    # Store the response that will be used in the next iteration
                    conversation_messages.append(data_json)
    
                    if not 'systemMessage' in data_json:
                        if 'error' in data_json:
                            handle_error(data_json['error'])
                        continue
    
                    if 'text' in data_json['systemMessage']:
                        handle_text_response(data_json['systemMessage']['text'])
                    elif 'schema' in data_json['systemMessage']:
                        handle_schema_response(data_json['systemMessage']['schema'])
                    elif 'data' in data_json['systemMessage']:
                        handle_data_response(data_json['systemMessage']['data'])
                    elif 'chart' in data_json['systemMessage']:
                        handle_chart_response(data_json['systemMessage']['chart'])
                    else:
                        colored_json = highlight(acc, lexers.JsonLexer(), formatters.TerminalFormatter())
                        print(colored_json)
                    print('\n')
                    acc = ''
        

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
