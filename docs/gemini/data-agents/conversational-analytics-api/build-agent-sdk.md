---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk/
title: Build a data agent using the Python SDK \u00a0|\u00a0 Conversational Analytics API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:02.246813+00:00
---

# Build a data agent using the Python SDK  |  Conversational Analytics API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Build a data agent using the Python SDK Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to use the Python SDK to make requests to the Conversational Analytics API. The sample Python code demonstrates how to complete the following tasks:

  * Authenticate and set up your environment
  * Configure settings and initialize clients
  * Connect to a Looker, BigQuery, or Data Studio data source
  * Set up context for stateful or stateless chat
  * Create a data agent
  * Create a conversation
  * Manage data agents and conversations
  * Use the API to ask questions
  * Create a stateless multi-turn conversation
  * Define helper functions

**Tip:** To run the code samples on this page in an interactive environment, see the [Conversational Analytics API SDK Colaboratory notebook](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/agents/gemini_data_analytics/intro_gemini_data_analytics_sdk.ipynb).

## Authenticate and set up your environment

To use the Python SDK for the Conversational Analytics API, follow the instructions in the [Conversational Analytics API SDK Colaboratory notebook](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/agents/gemini_data_analytics/intro_gemini_data_analytics_sdk.ipynb) to download and install the SDK. Note that the download method and the contents of the SDK Colab are subject to change.

After you've completed the setup instructions in the notebook, you can use the following code to import the required SDK libraries and authenticate your Google Account within a Colaboratory environment:
    
    
    from google.colab import auth
    auth.authenticate_user()
    
    from google.cloud import geminidataanalytics
    from google.api_core import client_options
    

## Configure settings and initialize clients

The following sample Python code defines the billing project, location, and system instructions that are used throughout your script, and initializes API clients with endpoint settings based on location:
    
    
    # Billing project
    billing_project = "my_project_name"
    location = "LOCATION"
    
    # System instructions
    system_instruction = "Help the user analyze their data."
    
    # Set client options based on location.
    if not location or location == "global":
      endpoint = "geminidataanalytics.googleapis.com"
    elif "-" in location:
      # Regional endpoints
      endpoint = f"geminidataanalytics-{location}.googleapis.com"
    else:
      # Multi-regional endpoints
      endpoint = f"geminidataanalytics.{location}.rep.googleapis.com"
    opts = client_options.ClientOptions(api_endpoint=endpoint)
    
    data_agent_client = geminidataanalytics.DataAgentServiceClient(client_options=opts)
    data_chat_client = geminidataanalytics.DataChatServiceClient(client_options=opts)
    

Replace the sample values as follows:

  * my_project_name: The ID of the Google Cloud project where you [enabled the required APIs](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/enable-the-api).
  * LOCATION: The location where your resources are stored. To use the global endpoint, specify `global`. To meet data residency requirements, specify a supported single region (such as `us-east4`) or multi-region (such as `eu` or `us`). For more information, see [Data residency](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-residency).

**Important:** The location in the request parent or resource name must match the location of the endpoint that you're calling. For example, if you configure the client to use the `geminidataanalytics.us.rep.googleapis.com` endpoint, specify `us` in your request parent (such as `projects/PROJECT_ID/locations/us`).
  * Help the user analyze their data.: System instructions to guide the agent's behavior and customize it for your data needs. For example, you can use system instructions to define business terms, control response length, or set data formatting. Ideally, define system instructions by using the recommended YAML format in [Write effective system instructions](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-system-instructions) to provide detailed and structured guidance.




## Connect to a data source

The following sections show how to define the connection details for your agent's data sources. Your agent can connect to data in the following ways:

  * Looker
  * BigQuery
  * Data Studio
  * AlloyDB
  * Cloud SQL for MySQL
  * Cloud SQL for PostgreSQL
  * Spanner data



### Connect to Looker data

The following code examples show how to define the details for a connection to a Looker Explore with either API keys or an access token. You can connect up to five Looker Explores at a time with the Conversational Analytics API.

When you connect to a Looker data source, note the following:

  * You can query any included Explore in a conversation.
  * An agent can only query one Explore at a time. It is not possible to perform queries across multiple Explores simultaneously.
  * An agent can query multiple Explores in the same conversation.
  * An agent can query multiple Explores in a conversation that includes questions with multiple parts, or in conversations that include follow-up questions.

For example: A user connects two Explores, one called `cat-explore` and one called `dog-explore`. The user inputs the question "What's greater: the count of cats or the count of dogs?" This would create two queries: one to count the number of cats in `cat-explore` and one to count the number of dogs in `dog-explore`. The agent compares the numbers from both queries after completing both queries.




The following sample code defines a connection to multiple Looker Explores. To improve agent performance, you can optionally provide golden queries as structured context for your Explores. For more information, see [Define data agent context for Looker data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-looker).

### API keys

You can establish a connection with a Looker instance with generated Looker API keys, as described in [Authenticate and connect to a data source](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/authentication#looker-api-keys).
    
    
    looker_client_id = "my_looker_client_id"
    looker_client_secret = "my_looker_client_secret"
    looker_instance_uri = "https://my_company.looker.com"
    lookml_model_1 = "my_model"
    explore_1 = "my_explore"
    lookml_model_2 = "my_model_2"
    explore_2 = "my_explore_2"
    
    looker_explore_reference = geminidataanalytics.LookerExploreReference()
    looker_explore_reference.looker_instance_uri = looker_instance_uri
    looker_explore_reference.lookml_model = "my_model"
    looker_explore_reference.explore = "my_explore"
    
    looker_explore_reference2 = geminidataanalytics.LookerExploreReference()
    looker_explore_reference2.looker_instance_uri = looker_instance_uri
    looker_explore_reference2.lookml_model = "my_model_2"
    looker_explore_reference2.explore = "my_explore_2"
    
    credentials = geminidataanalytics.Credentials()
    credentials.oauth.secret.client_id = looker_client_id
    credentials.oauth.secret.client_secret = looker_client_secret
    
    datasource_references = geminidataanalytics.DatasourceReferences()
    datasource_references.looker.explore_references = [looker_explore_reference, looker_explore_reference2]
    

Replace the sample values as follows:

  * my_looker_client_id: The client ID of your generated Looker API key.
  * my_looker_client_secret: The client secret of your generated Looker API key.
  * https://my_company.looker.com: The complete URL of your Looker instance.
  * my_model: The name of the LookML model that includes the Explore that you want to connect to.
  * my_explore: The name of the Looker Explore that you want the data agent to query.
  * my_model_2: The name of the second LookML model that includes the Explore that you want to connect to. You can repeat this variable for additional models for up to five Explores.
  * my_explore_2: The name of the additional Looker Explore that you want the data agent to query. You can repeat this variable to include up to five Explores.



### Access token

You can establish a connection with a Looker instance by using an access token, as described in [Authenticate and connect to a data source with the Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/authentication#looker-access-token).
    
    
    looker_access_token = "my_access_token"
    looker_instance_uri = "https://my_company.looker.com"
    lookml_model = "my_model"
    explore = "my_explore"
    lookml_model_2 = "my_model_2"
    explore_2 = "my_explore_2"
    
    looker_explore_reference = geminidataanalytics.LookerExploreReference()
    looker_explore_reference.looker_instance_uri = looker_instance_uri
    looker_explore_reference.lookml_model = "my_model"
    looker_explore_reference.explore = "my_explore"
    
    looker_explore_reference2 = geminidataanalytics.LookerExploreReference()
    looker_explore_reference2.looker_instance_uri = looker_instance_uri
    looker_explore_reference2.lookml_model = "my_model_2"
    looker_explore_reference2.explore = "my_explore_2"
    
    credentials = geminidataanalytics.Credentials()
    credentials.oauth.secret.client_id = looker_client_id
    credentials.oauth.secret.client_secret = looker_client_secret
    
    datasource_references = geminidataanalytics.DatasourceReferences()
    datasource_references.looker.explore_references = [looker_explore_reference, looker_explore_reference2]
    

Replace the sample values as follows:

  * my_access_token: The `access_token` value that you generate to authenticate to Looker.
  * https://my_company.looker.com: The complete URL of your Looker instance.
  * my_model: The name of the LookML model that includes the Explore that you want to connect to.
  * my_explore: The name of the Looker Explore that you want the data agent to query.
  * my_model_2: The name of the second LookML model that includes the Explore that you want to connect to. You can repeat this variable for additional models for up to five Explores.
  * my_explore_2: The name of the additional Looker Explore that you want the data agent to query. You can repeat this variable to include up to five Explores.



### Connect to BigQuery data

With the Conversational Analytics API, there are no hard limits on the number of BigQuery tables that you can connect to. However, connecting to a large number of tables can reduce accuracy or cause you to exceed the model's input token limit.

**Note:** Queries that require complex joins across multiple tables might result in less accurate responses.

The following sections show how to connect to BigQuery data by using table references, graph references, or both.

#### Connect to BigQuery tables

The following sample code defines a connection to multiple BigQuery tables and includes examples of optional structured context fields. To improve agent performance, you can optionally provide structured context for your BigQuery tables, such as table and column descriptions, synonyms, tags, example queries, and user-defined functions. For more information, see [Define data agent context for BigQuery data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-bq).

**Important:** Make sure you have the necessary Identity and Access Management (IAM) permissions to query any BigQuery tables that you specify.
    
    
    bigquery_table_reference_1 = geminidataanalytics.BigQueryTableReference()
    bigquery_table_reference_1.project_id = "PROJECT_ID_1"
    bigquery_table_reference_1.dataset_id = "DATASET_ID_1"
    bigquery_table_reference_1.table_id = "TABLE_ID_1"
    bigquery_table_reference_1.schema = geminidataanalytics.Schema()
    bigquery_table_reference_1.schema.description = "TABLE_DESCRIPTION"
    bigquery_table_reference_1.schema.fields = [
      geminidataanalytics.Field(
        name="COLUMN_NAME",
        description="COLUMN_DESCRIPTION"
      )
    ]
    
    bigquery_table_reference_2 = geminidataanalytics.BigQueryTableReference()
    bigquery_table_reference_2.project_id = "PROJECT_ID_2"
    bigquery_table_reference_2.dataset_id = "DATASET_ID_2"
    bigquery_table_reference_2.table_id = "TABLE_ID_2"
    
    bigquery_table_reference_3 = geminidataanalytics.BigQueryTableReference()
    bigquery_table_reference_3.project_id = "PROJECT_ID_3"
    bigquery_table_reference_3.dataset_id = "DATASET_ID_3"
    bigquery_table_reference_3.table_id = "TABLE_ID_3"
    
    # Connect to your data source
    datasource_references = geminidataanalytics.DatasourceReferences()
    datasource_references.bq.table_references = [bigquery_table_reference_1, bigquery_table_reference_2, bigquery_table_reference_3]
    

Replace the sample values as follows:

  * PROJECT_ID_1: The ID of the Google Cloud project that contains the BigQuery dataset and table that you want to connect to. To connect to a [public dataset](https://docs.cloud.google.com/bigquery/public-data), specify `bigquery-public-data`.
  * DATASET_ID_1: The ID of the BigQuery dataset. For example, `san_francisco`.
  * TABLE_ID_1: The ID of the BigQuery table. For example, `street_trees`.
  * TABLE_DESCRIPTION: An optional description of the table's content and purpose.
  * COLUMN_NAME: The name of a column in the table for which you are providing an optional description.
  * COLUMN_DESCRIPTION: An optional description of the column's content and purpose.



#### Connect to BigQuery Graph

You can also connect to graphs by using [BigQuery Graph](https://docs.cloud.google.com/bigquery/docs/graph-overview). Provide one or more graph references in the `property_graph_references` field.

For information about BigQuery edition requirements and graph query limitations, see [Connect to BigQuery Graph](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/connect-bigquery#connect-to-bq-graph).
    
    
    # BigQuery graph reference
    graph_reference = geminidataanalytics.BigQueryPropertyGraphReference()
    graph_reference.project_id = "GRAPH_PROJECT_ID"
    graph_reference.dataset_id = "GRAPH_DATASET_ID"
    graph_reference.property_graph_id = "GRAPH_ID"
    
    # Connect to your data source
    datasource_references = geminidataanalytics.DatasourceReferences()
    datasource_references.bq.property_graph_references = [graph_reference]
    

Replace the sample values as follows:

  * GRAPH_PROJECT_ID: The ID of the Google Cloud project that contains the BigQuery graph.
  * GRAPH_DATASET_ID: The ID of the BigQuery dataset that contains the graph.
  * GRAPH_ID: The ID of the BigQuery graph.



To query both tables and graphs with the same data agent, set both `table_references` and `property_graph_references` on `datasource_references.bq`.

### Connect to Data Studio data

The following sample code defines a connection to a Data Studio data source.
    
    
    studio_datasource_id = "my_datasource_id"
    
    studio_references = geminidataanalytics.StudioDatasourceReference()
    studio_references.datasource_id = studio_datasource_id
    
    ## Connect to your data source
    datasource_references.studio.studio_references = [studio_references]
    

In the previous example, replace my_datasource_id with the data source ID.

### Connect to AlloyDB data

The following sample code defines a connection to an AlloyDB database using the Python SDK.
    
    
    # Define the AlloyDB database reference
    alloydb_database_reference = geminidataanalytics.AlloyDbDatabaseReference()
    alloydb_database_reference.project_id = "PROJECT_ID"
    alloydb_database_reference.region = "REGION"
    alloydb_database_reference.cluster_id = "CLUSTER_ID"
    alloydb_database_reference.instance_id = "INSTANCE_ID"
    alloydb_database_reference.database_id = "DATABASE"
    alloydb_database_reference.table_ids = ["TABLE_1_ID", "TABLE_2_ID"]
    
    # Optional: Include this if you have created advanced context for the agent
    agent_context_reference = geminidataanalytics.AgentContextReference()
    agent_context_reference.context_set_id = f"projects/{billing_project}/locations/{location}/contextSets/your_context_set_id"
    
    # Add the AlloyDB reference to the DatasourceReferences object
    datasource_references = geminidataanalytics.DatasourceReferences()
    datasource_references.alloydb.database_reference = alloydb_database_reference
    # Optional:
    # datasource_references.alloydb.agent_context_reference = agent_context_reference
    

Replace the sample values as follows:

  * PROJECT_ID: The ID of the Google Cloud project that contains the AlloyDB cluster.
  * REGION: The region where the AlloyDB cluster resides—for example, `us-central1`.
  * CLUSTER_ID: The ID of the AlloyDB cluster.
  * INSTANCE_ID: The ID of the AlloyDB instance.
  * DATABASE: The name of the target database—for example, `financial`.
  * TABLE_1_ID, TABLE_2_ID: A list of the tables in the database that the data agent is suggested to use—for example, `"loan"`, `"client"`, `"disp"`.
  * your_context_set_id: If you created advanced context for the agent, the ID of your context set.



### Connect to Cloud SQL for MySQL data

To connect to a Cloud SQL for MySQL instance, you use the `CloudSqlReference` class from the `geminidataanalytics` SDK. This involves specifying the project, instance, database, and optionally, the specific tables that you want the agent to consider.

Before you connect to Cloud SQL for MySQL data, make sure that you authenticate to Cloud SQL for MySQL using Identity and Access Management (IAM). For more information, see [Authenticate to Cloud SQL for MySQL and Cloud SQL for PostgreSQL](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/authentication#connect-to-sql).

The following example defines a connection to a Cloud SQL for MySQL database using the Python SDK.
    
    
    # Import the necessary library
    from google.cloud import geminidataanalytics
    
    # Define the Cloud SQL database reference
    cloud_sql_database_reference = geminidataanalytics.CloudSqlDatabaseReference(
        project_id="PROJECT_ID",
        instance_id="INSTANCE_ID",
        database_id="DATABASE_ID",
        # Optional: Specify table IDs to guide the agent
        table_ids=["TABLE_1_ID", "TABLE_2_ID"]
    )
    
    # Create a CloudSqlReference object
    cloud_sql_reference = geminidataanalytics.CloudSqlReference(
        database_reference=cloud_sql_database_reference
        # Optional: Include this if you have created advanced context for the agent
        # agent_context_reference=geminidataanalytics.AgentContextReference(
        # context_set_id=f"projects/{billing_project}/locations/{location}/contextSets/your_context_set_id"
        # )
    )
    
    # Add the Cloud SQL reference to the DatasourceReferences object
    datasource_references = geminidataanalytics.[DatasourceReferences](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.DatasourceReferences.html)()
    datasource_references.cloud_sql = cloud_sql_reference
    

Replace the sample values as follows:

  * PROJECT_ID: The ID of the Google Cloud project containing the Cloud SQL for MySQL instance.
  * INSTANCE_ID: The ID of the Cloud SQL for MySQL instance.
  * DATABASE_ID: The name of the target database within the instance—for example, `financial`.
  * TABLE_1_ID, TABLE_2_ID: (Optional) A list of specific table names in the database that the data agent is suggested to use—for example, `"orders"` and `"customers"`.
  * your_context_set_id: If you created advanced context for the agent, the ID of your context set.



You can use the `datasource_references` object when you create or interact with the data agent.

### Connect to Cloud SQL for PostgreSQL data

To connect to a Cloud SQL for PostgreSQL instance, you use the `CloudSqlReference` class from the `geminidataanalytics` SDK. This involves specifying the project, instance, database, and optionally, the specific tables that you want the agent to consider.

Before you connect to Cloud SQL for PostgreSQL data, make sure that you authenticate to Cloud SQL for PostgreSQL using IAM. For more information, see [Authenticate to Cloud SQL for MySQL and Cloud SQL for PostgreSQL](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/authentication#connect-to-sql).

The following example defines a connection to a Cloud SQL for PostgreSQL database using the Python SDK.
    
    
    # Import the necessary library
    from google.cloud import geminidataanalytics
    
    # Define the Cloud SQL database reference
    cloud_sql_database_reference = geminidataanalytics.CloudSqlDatabaseReference(
        project_id="PROJECT_ID",
        instance_id="INSTANCE_ID",
        database_id="DATABASE_ID",
        # Optional: Specify table IDs to guide the agent
        table_ids=["TABLE_1_ID", "TABLE_2_ID"]
    )
    
    # Create a CloudSqlReference object
    cloud_sql_reference = geminidataanalytics.CloudSqlReference(
        database_reference=cloud_sql_database_reference
        # Optional: Include this if you have created advanced context for the agent
        # agent_context_reference=geminidataanalytics.AgentContextReference(
        # context_set_id=f"projects/{billing_project}/locations/{location}/contextSets/your_context_set_id"
        # )
    )
    
    # Add the Cloud SQL reference to the DatasourceReferences object
    datasource_references = geminidataanalytics.[DatasourceReferences](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.DatasourceReferences.html)()
    datasource_references.cloud_sql = cloud_sql_reference
    

Replace the sample values as follows:

  * PROJECT_ID: The ID of the Google Cloud project containing the Cloud SQL for PostgreSQL instance.
  * INSTANCE_ID: The ID of the Cloud SQL for PostgreSQL instance.
  * DATABASE_ID: The name of the target database within the instance—for example, `postgres`.
  * TABLE_1_ID, TABLE_2_ID: (Optional) A list of specific table names within the database that the data agent is suggested to use—for example, `"users"` and `"products"`.
  * your_context_set_id: If you created advanced context for the agent, the ID of your context set.



You can use the `datasource_references` object when you create or interact with the data agent.

### Connect to Spanner data

To connect to a Spanner instance, you use the `SpannerReference` class from the `geminidataanalytics` SDK. This involves specifying the project, instance, database, and optionally, the specific tables that you want the agent to consider.

Before you connect to Spanner data, make sure that the user or service account has the `spanner.databaseReader` IAM role. For more information, see [Apply IAM roles](https://docs.cloud.google.com/spanner/docs/grant-permissions).

The following sample Python code defines a connection to a Spanner database using the Python SDK.
    
    
    # Import the necessary library
    from google.cloud import geminidataanalytics
    
    # Define the Spanner database reference
    spanner_database_reference = geminidataanalytics.SpannerDatabaseReference(
        project_id="PROJECT_ID",
        instance_id="INSTANCE_ID",
        database_id="DATABASE_ID",
        # Optional: Specify table IDs to guide the agent
        table_ids=["TABLE_1_ID", "TABLE_2_ID"]
    )
    
    # Create a SpannerReference object
    spanner_reference = geminidataanalytics.SpannerReference(
        database_reference=spanner_database_reference
        # Optional: Include this if you have created advanced context for the agent
        # agent_context_reference=geminidataanalytics.AgentContextReference(
        # context_set_id=f"projects/{billing_project}/locations/{location}/contextSets/your_context_set_id"
        # )
    )
    
    # Add the Spanner reference to the DatasourceReferences object
    datasource_references = geminidataanalytics.[DatasourceReferences](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.DatasourceReferences.html)()
    datasource_references.spanner = spanner_reference
    

Replace the sample values as follows:

  * PROJECT_ID: The ID of the Google Cloud project containing the Spanner instance.
  * INSTANCE_ID: The ID of the Spanner instance.
  * DATABASE_ID: The name of the target database in the instance.
  * TABLE_1_ID, TABLE_2_ID: (Optional) A list of specific table names within the database that the data agent is suggested to use—for example, `"Singers"` and `"Albums"`.
  * your_context_set_id: If you created advanced context for the agent, the ID of your context set.



You can use the `datasource_references` object when creating or interacting with the data agent.

## Set up context for stateful or stateless chat

The Conversational Analytics API supports multi-turn conversations, which let users ask follow-up questions that build on previous context. The following sample Python code demonstrates how to set up context for either _stateful_ or _stateless_ chat:

  * **Stateful chat** : Google Cloud stores and manages the conversation history. Stateful chat is inherently multi-turn, as the API retains context from previous messages. You only need to send the current message for each turn.
  * **Stateless chat** : Your application manages the conversation history. You must include the entire conversation history with each new message. For detailed examples on how to manage multi-turn conversations in stateless mode, see Create a stateless multi-turn conversation.

**Note:** Whether you set up `published_context` for stateful chat or `inline_context` for stateless chat, you use the `system_instruction` variable that you defined in Configure settings and initialize clients to effectively guide the agent's responses. For details on the recommended YAML format for these instructions, see [Write effective system instructions](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-system-instructions).

### Stateful chat

The following code sample sets up context for stateful chat, where Google Cloud stores and manages the conversation history. You can also optionally enable advanced analysis with Python by including the line `published_context.options.analysis.python.enabled = True` in the following sample code.

**Warning:** The Python code that data agents return is designed to execute within a secure, Google-managed sandbox. Executing this code in a local or other unverified environment bypasses the sandbox's security protections and can expose your system to security risks, such as the execution of malicious code. For guidance on how to safely inspect and handle agent-generated Python code, see [How can I safely inspect and handle agent-generated Python code?](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/frequently-asked-questions#safe-python)
    
    
    # Set up context for stateful chat
    published_context = geminidataanalytics.Context()
    published_context.system_instruction = system_instruction
    published_context.datasource_references = datasource_references
    # Optional: To enable advanced analysis with Python, include the following line:
    published_context.options.analysis.python.enabled = True
    # Optional: To limit query costs to 100 MiB, include the following line:
    published_context.options.datasource.big_query_max_billed_bytes.value = 104857600
    

### Stateless chat

The following sample code sets up context for stateless chat, where you must send the entire conversation history with each message. You can also optionally enable advanced analysis with Python by including the line `inline_context.options.analysis.python.enabled = True` in the following sample code.

**Warning:** The Python code that data agents return is designed to execute within a secure, Google-managed sandbox. Executing this code in a local or other unverified environment bypasses the sandbox's security protections and can expose your system to security risks, such as the execution of malicious code. For guidance on how to safely inspect and handle agent-generated Python code, see [How can I safely inspect and handle agent-generated Python code?](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/frequently-asked-questions#safe-python)
    
    
    # Set up context for stateless chat
    inline_context = geminidataanalytics.Context()
    inline_context.system_instruction = system_instruction
    inline_context.datasource_references = datasource_references
    # Optional: To enable advanced analysis with Python, include the following line:
    inline_context.options.analysis.python.enabled = True
    # Optional: To limit query costs to 100 MiB, include the following line:
    inline_context.options.datasource.big_query_max_billed_bytes = 104857600
    

## Create a data agent

The following sample Python code makes an API request to create a data agent, which you can then use to have a conversation about your data. You can create an agent synchronously or asynchronously. The data agent is configured with the specified data source, system instructions, and context.

You can optionally protect the data agent with CMEK by setting the `kms_key` field when you create the data agent. For more information, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/cmek).

### Synchronous
    
    
      data_agent_id = "data_agent_1"
    
      # Optional: If using CMEK, replace the empty strings with your KMS key details.
      key_ring = ""    # KEY_RING_NAME
      key_name = ""    # KEY_NAME
      key_project = "" # KMS_PROJECT_ID (Defaults to billing_project if empty)
    
      data_agent = geminidataanalytics.DataAgent()
      data_agent.data_analytics_agent.published_context = published_context
      data_agent.name = f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}" # Optional
    
      # Optional: Add CMEK key if details are provided
      if key_ring and key_name:
        if not key_project:
          key_project = billing_project
        kms_key_data_agent = f"projects/{key_project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{key_name}"
        data_agent.kms_key = kms_key_data_agent # Add for CMEK
    
      request = geminidataanalytics.CreateDataAgentRequest(
        parent=f"projects/{billing_project}/locations/{location}",
        data_agent_id=data_agent_id, # Optional
        data_agent=data_agent,
      )
    
      try:
        response = data_agent_client.create_data_agent_sync(request=request)
        print("Data Agent created")
        print(response)
      except Exception as e:
        print(f"Error creating Data Agent: {e}")
    

### Asynchronous
    
    
      data_agent_id = "data_agent_1"
    
      # Optional: If using CMEK, replace the empty strings with your KMS key details.
      key_ring = ""    # KEY_RING_NAME
      key_name = ""    # KEY_NAME
      key_project = "" # KMS_PROJECT_ID (Defaults to billing_project if empty)
    
      data_agent = geminidataanalytics.DataAgent()
      data_agent.data_analytics_agent.published_context = published_context
      data_agent.name = f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}" # Optional
    
      # Optional: Add CMEK key if details are provided
      if key_ring and key_name:
        if not key_project:
          key_project = billing_project
        kms_key_data_agent = f"projects/{key_project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{key_name}"
        data_agent.kms_key = kms_key_data_agent # Add for CMEK
    
      request = geminidataanalytics.CreateDataAgentRequest(
        parent=f"projects/{billing_project}/locations/{location}",
        data_agent_id=data_agent_id, # Optional
        data_agent=data_agent,
      )
    
      try:
        data_agent_client.create_data_agent(request=request)
        print("Data Agent created")
      except Exception as e:
        print(f"Error creating Data Agent: {e}")
    

In the previous example, replace values as follows:

  * data_agent_1: A unique identifier for the data agent.
  * KEY_RING_NAME: If using CMEK, the name of your Cloud KMS key ring.
  * KEY_NAME: If using CMEK, the name of your Cloud KMS key.
  * KMS_PROJECT_ID: If using CMEK, the project ID where the key is hosted.



## Create a conversation

The following sample Python code makes an API request to create a conversation.

You can optionally protect the conversation with CMEK by setting the `kms_key` field when you create the conversation. For more information, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/cmek).
    
    
    # Initialize request arguments
    data_agent_id = "data_agent_1"
    conversation_id = "conversation_1"
    
    
    # Optional: If using CMEK, replace the empty strings with your KMS key details.
    key_ring = ""    # KEY_RING_NAME
    key_name = ""    # KEY_NAME
    key_project = "" # KMS_PROJECT_ID (Defaults to billing_project if empty)
    
    if key_project == "":
      key_project = billing_project
    kms_key_conversation = f"projects/{key_project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{key_name}"
    
    conversation = geminidataanalytics.Conversation()
    conversation.agents = [f'projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}']
    conversation.name = f"projects/{billing_project}/locations/{location}/conversations/{conversation_id}"
    
    # Optional: Add CMEK key if details are provided
    if key_ring and key_name:
      if not key_project:
        key_project = billing_project
      kms_key_conversation = f"projects/{key_project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{key_name}"
      conversation.kms_key = kms_key_conversation # Add for CMEK
    
    request = geminidataanalytics.CreateConversationRequest(
      parent=f"projects/{billing_project}/locations/{location}",
      conversation_id=conversation_id,
      conversation=conversation,
    )
    
    # Make the request
    response = data_chat_client.create_conversation(request=request)
    
    # Handle the response
    print(response)
    

Replace the sample values as follows:

  * data_agent_1: The ID of the data agent, as defined in the sample code block in Create a data agent.
  * conversation_1: A unique identifier for the conversation.
  * KEY_RING_NAME: If using CMEK, the name of your Cloud KMS key ring.
  * KEY_NAME: If using CMEK, the name of your Cloud KMS key.
  * KMS_PROJECT_ID: If using CMEK, the project ID where the key is hosted.



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

The following sample Python code demonstrates how to make an API request to retrieve a data agent that you previously created.
    
    
    # Initialize request arguments
    data_agent_id = "data_agent_1"
    request = geminidataanalytics.GetDataAgentRequest(
      name=f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}",
    )
    
    # Make the request
    response = data_agent_client.get_data_agent(request=request)
    
    # Handle the response
    print(response)
    

In the previous example, replace the value data_agent_1 with the unique identifier for the data agent that you want to retrieve.

### List data agents

The following code demonstrates how to list all the data agents for a given project by calling the `list_data_agents` method. To list all agents, you must have the `geminidataanalytics.dataAgents.list` permission on the project. For more information on which IAM roles include this permission, see the list of [predefined roles](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control#predefined-roles).
    
    
    billing_project = "YOUR-BILLING-PROJECT"
    location = "global"
    request = geminidataanalytics.ListDataAgentsRequest(
      parent=f"projects/{billing_project}/locations/{location}",
    )
    
    # Make the request
    page_result = data_agent_client.list_data_agents(request=request)
    
    # Handle the response
    for response in page_result:
      print(response)
    

Replace YOUR-BILLING-PROJECT with the ID of your billing project.

### List accessible data agents

The following code demonstrates how to list all the accessible data agents for a given project by calling the `list_accessible_data_agents` method.
    
    
    billing_project = "YOUR-BILLING-PROJECT"
    creator_filter = "YOUR-CREATOR-FILTER"
    location = "global"
    request = geminidataanalytics.ListAccessibleDataAgentsRequest(
      parent=f"projects/{billing_project}/locations/{location}",
      creator_filter=creator_filter
    )
    
    # Make the request
    page_result = data_agent_client.list_accessible_data_agents(request=request)
    
    # Handle the response
    for response in page_result:
      print(response)
    

Replace the sample values as follows:

  * YOUR-BILLING-PROJECT: The ID of your billing project.
  * YOUR-CREATOR-FILTER: The filter to apply based on the creator of the data agent. Possible values include `NONE` (default), `CREATOR_ONLY`, and `NOT_CREATOR_ONLY`.



### Update a data agent

The following sample code demonstrates how to update a data agent synchronously or asynchronously by calling the `update_data_agent_sync` or `update_data_agent` method on the data agent resource. The request requires a `DataAgent` object that includes the new values for the fields that you want to change, and an `update_mask` parameter that takes a `FieldMask` object to specify which fields to update.

To update a data agent, you must have the `geminidataanalytics.dataAgents.update` IAM permission on the agent. For more information on which IAM roles include this permission, see the list of [predefined roles](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control#predefined-roles).

### Synchronous
    
    
    data_agent_id = "data_agent_1"
    billing_project = "YOUR-BILLING-PROJECT"
    data_agent = geminidataanalytics.DataAgent()
    data_agent.data_analytics_agent.published_context = published_context
    data_agent.name = f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}"
    data_agent.description = "Updated description of the data agent."
    
    update_mask = field_mask_pb2.FieldMask(paths=['description', 'data_analytics_agent.published_context'])
    
    request = geminidataanalytics.UpdateDataAgentRequest(
      data_agent=data_agent,
      update_mask=update_mask,
    )
    
    try:
      # Make the request
      response = data_agent_client.update_data_agent_sync(request=request)
      print("Data Agent Updated")
      print(response)
    except Exception as e:
      print(f"Error updating Data Agent: {e}")
    

### Asynchronous
    
    
    data_agent_id = "data_agent_1"
    billing_project = "YOUR-BILLING-PROJECT"
    data_agent = geminidataanalytics.DataAgent()
    data_agent.data_analytics_agent.published_context = published_context
    data_agent.name = f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}"
    data_agent.description = "Updated description of the data agent."
    
    update_mask = field_mask_pb2.FieldMask(paths=['description', 'data_analytics_agent.published_context'])
    
    request = geminidataanalytics.UpdateDataAgentRequest(
      data_agent=data_agent,
      update_mask=update_mask,
    )
    
    try:
      # Make the request
      data_agent_client.update_data_agent(request=request)
      print("Data Agent Updated")
    except Exception as e:
      print(f"Error updating Data Agent: {e}")
    

Replace the sample values as follows:

  * data_agent_1: The ID of the data agent that you want to update.
  * YOUR-BILLING-PROJECT: The ID of your billing project.
  * Updated description of the data agent.: A description of the updated data agent.



### Get the IAM policy for a data agent

The following sample code demonstrates how to use the `get_iam_policy` method to fetch the IAM policy for a data agent. The request specifies the data agent resource path.
    
    
    billing_project = "YOUR-BILLING-PROJECT"
    location = "global"
    data_agent_id = "data_agent_1"
    
    resource = f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}"
    request = iam_policy_pb2.GetIamPolicyRequest(
          resource=resource,
        )
    try:
      response = data_agent_client.get_iam_policy(request=request)
      print("IAM Policy fetched successfully!")
      print(f"Response: {response}")
    except Exception as e:
      print(f"Error setting IAM policy: {e}")
    

Replace the sample values as follows:

  * YOUR-BILLING-PROJECT: The ID of your billing project.
  * data_agent_1: The ID of the data agent for which you want to get the IAM policy.



### Set the IAM policy for a data agent

To share an agent, you can use the `set_iam_policy` method to assign IAM roles to users on a specific agent. The request includes bindings that specify which roles should be assigned to which users.

**Important:** This API call overrides existing permissions for the resource. To preserve existing policies, call the `get_iam_policy` method to fetch the existing policy, and then pass the existing policy along with any additional changes in the call to `set_iam_policy`.
    
    
    billing_project = "YOUR-BILLING-PROJECT"
    location = "global"
    data_agent_id = "data_agent_1"
    role = "roles/geminidataanalytics.dataAgentEditor"
    users = "EMAIL_ADDRESS"
    
    resource = f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}"
    
    # Construct the IAM policy
    binding = policy_pb2.Binding(
      role=role,
      members= [f"user:{i.strip()}" for i in users.split(",")]
    )
    
    policy = policy_pb2.Policy(bindings=[binding])
    
    # Create the request
    request = iam_policy_pb2.SetIamPolicyRequest(
      resource=resource,
      policy=policy
    )
    
    # Send the request
    try:
      response = data_agent_client.set_iam_policy(request=request)
      print("IAM Policy set successfully!")
      print(f"Response: {response}")
    except Exception as e:
      print(f"Error setting IAM policy: {e}")
    

Replace the sample values as follows:

  * YOUR-BILLING-PROJECT: The ID of your billing project.
  * data_agent_1: The ID of the data agent for which you want to set the IAM policy.
  * EMAIL_ADDRESSES: A comma-separated list of user emails to which you want to grant the specified role.



### Delete a data agent

The following sample code demonstrates how to use the `delete_data_agent_sync` or `delete_data_agent` method to delete a data agent synchronously or asynchronously. When you delete a data agent, it enters a 30-day soft-deletion period where it cannot be recovered. For more information, see [Data retention and deletion](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/retention-deletion). The request specifies the data agent resource URL.

### Synchronous
    
    
    billing_project = "YOUR-BILLING-PROJECT"
    location = "global"
    data_agent_id = "data_agent_1"
    
    request = geminidataanalytics.DeleteDataAgentRequest(
      name=f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}",
    )
    
    try:
      # Make the request
      data_agent_client.delete_data_agent_sync(request=request)
      print("Data Agent Deleted")
    except Exception as e:
      print(f"Error deleting Data Agent: {e}")
    

### Asynchronous
    
    
    billing_project = "YOUR-BILLING-PROJECT"
    location = "global"
    data_agent_id = "data_agent_1"
    
    request = geminidataanalytics.DeleteDataAgentRequest(
      name=f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}",
    )
    
    try:
      # Make the request
      data_agent_client.delete_data_agent(request=request)
      print("Data Agent Deleted")
    except Exception as e:
      print(f"Error deleting Data Agent: {e}")
    

Replace the sample values as follows:

  * YOUR-BILLING-PROJECT: The ID of your billing project.
  * data_agent_1: The ID of the data agent that you want to delete.



### Get a conversation

The following sample code demonstrates how to use the `get_conversation` method to fetch information about an existing conversation. The request specifies the conversation resource path.
    
    
    billing_project = "YOUR-BILLING-PROJECT"
    location = "global"
    conversation_id = "conversation_1"
    
    request = geminidataanalytics.GetConversationRequest(
      name = f"projects/{billing_project}/locations/{location}/conversations/{conversation_id}"
    )
    
    # Make the request
    response = data_chat_client.get_conversation(request=request)
    
    # Handle the response
    print(response)
    

Replace the sample values as follows:

  * YOUR-BILLING-PROJECT: The ID of your billing project.
  * conversation_1: The ID of the conversation that you want to fetch.



### List conversations

The following sample code demonstrates how to list conversations for a given project by calling the `list_conversations` method. The request specifies the parent resource URL, which is the project and location (for example, `projects/my-project/locations/global`).

By default, this method returns the conversations that you created. Admins (users with the [`cloudaicompanion.topicAdmin` IAM role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.topicAdmin)) can see all conversations within the project.
    
    
    billing_project = "YOUR-BILLING-PROJECT"
    location = "global"
    request = geminidataanalytics.ListConversationsRequest(
      parent=f"projects/{billing_project}/locations/{location}",
    )
    
    # Make the request
    response = data_chat_client.list_conversations(request=request)
    
    # Handle the response
    print(response)
    

Replace YOUR-BILLING-PROJECT with the ID of the billing project where you've enabled the required APIs.

### List messages in a conversation

The following sample code demonstrates how to use the `list_messages` method to fetch all the messages in a conversation. The request specifies the conversation resource path.

To list messages, you must have the [`cloudaicompanion.topics.get` permission](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#gemini-for-google-cloud-api-roles) on the conversation.

**Note:** This list operation also supports pagination.
    
    
    billing_project = "YOUR-BILLING-PROJECT"
    location = "global"
    
    conversation_id = "conversation_1"
    
    request = geminidataanalytics.ListMessagesRequest(
      parent=f"projects/{billing_project}/locations/{location}/conversations/{conversation_id}",
    )
    
    # Make the request
    response = data_chat_client.list_messages(request=request)
    
    # Handle the response
    print(response)
    

Replace the sample values as follows:

  * YOUR-BILLING-PROJECT: The ID of your billing project.
  * conversation_1: The ID of the conversation for which you want to list messages.



### Delete a conversation

The following sample code demonstrates how to delete a conversation. Admins (users with the [cloudaicompanion.topicAdmin Identity and Access Management role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.topicAdmin)) or users with the [`cloudaicompanion.topics.delete` Identity and Access Management permission](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.topics.delete) can delete conversations within the project.
    
    
    billing_project = "YOUR-BILLING-PROJECT"
    location = "global"
    conversation_id = "conversation_1"
    
    request = geminidataanalytics.DeleteConversationRequest(
      name = f"projects/{billing_project}/locations/{location}/conversations/{conversation_id}"
    )
    
    # Make the request
    response = data_chat_client.delete_conversation(request=request)
    
    # Handle the response
    print(response)
    

Replace the sample values as follows:

  * YOUR-BILLING-PROJECT: The ID of your billing project.
  * conversation_1: The ID of the conversation for which you want to list messages.



## Use the API to ask questions

After you create a data agent and, for stateful chat, a conversation, you can send queries to the agent. The following code examples show how to call the `data_chat_client.chat` method. These examples use the context variables (such as data source and system instructions) that you configured in Set up context for stateful or stateless chat.

When you send a query, the API returns a stream of [`Message`](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/reference/rest/v1/Message) objects. This stream can contain different types of messages, including text, data tables, and charts. Text messages can provide insight into the agent's reasoning, report on its progress, or give the final answer. The purpose of each text message is indicated by its [`TextType`](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/reference/rest/v1/Message#TextType) value:

  * `THOUGHT`: Shows the agent's internal thought process as it plans how to answer your query. `THOUGHT` messages provide step-by-step insight into the agent's reasoning and decision-making process and contain two parts: `parts[0]` is the thought summary, which briefly summarizes the full thought text, and `parts[1]` is the full thought text.
  * `PROGRESS`: Reports the agent's progress on an action, such as data retrieval or a tool that's being invoked. This value is returned only for Looker data sources and contains two parts: `parts[0]` is the summary, and `parts[1]` is the full progress text.
  * `FINAL_RESPONSE`: Provides the final answer to your query.



The following code examples use the `show_message` helper function, defined in Define helper functions, to process and display each message in the stream. For guidance on how to render these messages in a user interface when you're using Looker data sources, see [Render agent responses for Looker data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/render-looker-data).

### Stateful chat

### Send a stateful chat request with a `Conversation` reference

You can send a stateful chat request to the data agent by referencing a `Conversation` resource that you previously created.

**Note:** If your agent uses a Looker data source, uncomment the line `credentials=credentials` in the chat request.
    
    
    # Create a request that contains a single user message (your question)
    question = "Which species of tree is most prevalent?"
    messages = [geminidataanalytics.Message()]
    messages[0].user_message.text = question
    
    data_agent_id = "data_agent_1"
    conversation_id = "conversation_1"
    
    # Create a conversation_reference
    conversation_reference = geminidataanalytics.ConversationReference()
    conversation_reference.conversation = f"projects/{billing_project}/locations/{location}/conversations/{conversation_id}"
    conversation_reference.data_agent_context.data_agent = f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}"
    
    # Form the request
    request = geminidataanalytics.ChatRequest(
        parent = f"projects/{billing_project}/locations/{location}",
        # credentials = credentials,
        messages = messages,
        conversation_reference = conversation_reference
    )
    
    # Make the request
    stream = data_chat_client.chat(request=request, timeout=300 #custom timeout up to 600s)
    
    # Handle the response
    for response in stream:
        show_message(response)
    

Replace the sample values as follows:

  * Which species of tree is most prevalent?: A natural language question to send to the data agent.
  * data_agent_1: The unique identifier for the data agent, as defined in Create a data agent.
  * conversation_1: The unique identifier for the conversation, as defined in Create a conversation.



### Stateless chat

The following code samples demonstrate how to send a query to the data agent when you've set up context for stateless chat. You can send stateless queries by referencing a previously defined `DataAgent` resource or by using inline context in the request.

### Send a stateless chat request with a `DataAgent` reference

You can send a query to the data agent by referencing a `DataAgent` resource that you previously created.

**Note:** If your agent uses a Looker data source, uncomment the line `credentials=credentials` in the chat request.
    
    
    # Create a request that contains a single user message (your question)
    question = "Which species of tree is most prevalent?"
    messages = [geminidataanalytics.Message()]
    messages[0].user_message.text = question
    
    data_agent_id = "data_agent_1"
    
    data_agent_context = geminidataanalytics.DataAgentContext()
    data_agent_context.data_agent = f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}"
    
    # Form the request
    request = geminidataanalytics.ChatRequest(
        parent=f"projects/{billing_project}/locations/{location}",
        # credentials=credentials,
        messages=messages,
        data_agent_context = data_agent_context
    )
    
    # Make the request
    stream = data_chat_client.chat(request=request, timeout=300 #custom timeout up to 600s)
    
    # Handle the response
    for response in stream:
        show_message(response)
    

Replace the sample values as follows:

  * Which species of tree is most prevalent?: A natural language question to send to the data agent.
  * data_agent_1: The unique identifier for the data agent, as defined in Create a data agent.



### Send a stateless chat request with inline context

The following sample code demonstrates how to use the `inline_context` parameter to provide context directly within your stateless chat request.

**Note:** If your agent uses a Looker data source, uncomment the credentials=credentials line in the chat request.
    
    
    # Create a request that contains a single user message (your question)
    question = "Which species of tree is most prevalent?"
    messages = [geminidataanalytics.Message()]
    messages[0].user_message.text = question
    
    request = geminidataanalytics.ChatRequest(
        inline_context=inline_context,
        parent=f"projects/{billing_project}/locations/{location}",
        # credentials=credentials,
        messages=messages,
    )
    
    # Make the request
    stream = data_chat_client.chat(request=request, timeout=300 #custom timeout up to 600s)
    
    # Handle the response
    for response in stream:
        show_message(response)
    

In the previous example, replace Which species of tree is most prevalent? with a natural language question to send to the data agent.

## Create a stateless multi-turn conversation

To ask follow-up questions in a stateless conversation, your application must manage the conversation's context by sending the entire message history with each new request. The following example shows how to create a multi-turn conversation by referencing a data agent or by using inline context to provide the data source directly.

The following code sample uses data agent context. To use inline context instead, uncomment the line `inline_context=inline_context`.

If your agent uses a Looker data source, uncomment the line `credentials = credentials` in the chat request.
    
    
    # List that is used to track previous turns and is reused across requests
    conversation_messages = []
    
    data_agent_id = "data_agent_1"
    
    # Use data agent context
    data_agent_context = geminidataanalytics.DataAgentContext()
    data_agent_context.data_agent = f"projects/{billing_project}/locations/{location}/dataAgents/{data_agent_id}"
    
    # Helper function for calling the API
    def multi_turn_Conversation(msg):
    
      message = geminidataanalytics.Message()
      message.user_message.text = msg
    
      # Send a multi-turn request by including previous turns and the new message
      conversation_messages.append(message)
    
      request = geminidataanalytics.ChatRequest(
        parent=f"projects/{billing_project}/locations/{location}",
        # credentials=credentials,
        messages=conversation_messages,
        # Use data agent context
        data_agent_context=data_agent_context,
        # Use inline context
        # inline_context=inline_context,
      )
    
      # Make the request
      stream = data_chat_client.chat(request=request, timeout=300 #custom timeout up to 600s)
    
      # Handle the response
      for response in stream:
        show_message(response)
        conversation_messages.append(response)
    
    # Send the first turn request
    multi_turn_Conversation("Which species of tree is most prevalent?")
    
    # Send follow-up turn request
    multi_turn_Conversation("Can you show me the results as a bar chart?")
    

In the previous example, replace the sample values as follows:

  * data_agent_1: The unique identifier for the data agent, as defined in the sample code block in Create a data agent.
  * Which species of tree is most prevalent?: A natural language question to send to the data agent.
  * Can you show me the results as a bar chart?: A follow-up question that builds on or refines the previous question.



## Define helper functions

The following sample code contains helper function definitions that are used in the previous code samples. These functions help to parse the response from the API and display the results.
    
    
    import json as json_lib
    import textwrap
    import time
    
    import altair as alt
    import IPython
    import pandas as pd
    import proto
    import requests
    
    from google.protobuf.json_format import MessageToDict, MessageToJson
    from IPython.display import display, HTML
    from pygments import highlight, lexers, formatters
    from google.protobuf import field_mask_pb2
    from google.iam.v1 import policy_pb2
    from google.iam.v1 import iam_policy_pb2
    
    def handle_text_response(resp):
      parts = resp.parts
      full_text = "".join(parts)
      if "\n" not in full_text and len(full_text) > 80:
        wrapped_text = textwrap.fill(full_text, width=80)
        print(wrapped_text)
      else:
        print(full_text)
    
    def display_schema(data):
      fields = getattr(data, "fields")
      df = pd.DataFrame({
        "Column": map(lambda field: getattr(field, 'name'), fields),
        "Type": map(lambda field: getattr(field, 'type'), fields),
        "Description": map(lambda field: getattr(field, 'description', '-'), fields),
        "Mode": map(lambda field: getattr(field, 'mode'), fields)
      })
      display(df)
    
    def display_section_title(text):
      display(HTML('<h2>{}</h2>'.format(text)))
    
    def format_looker_table_ref(table_ref):
      return 'lookmlModel: {}, explore: {}, lookerInstanceUri: {}'.format(table_ref.lookml_model, table_ref.explore, table_ref.looker_instance_uri)
    
    def format_bq_table_ref(table_ref):
      return '{}.{}.{}'.format(table_ref.project_id, table_ref.dataset_id, table_ref.table_id)
    
    def display_datasource(datasource):
      source_name = ''
      if 'studio_datasource_id' in datasource:
        source_name = getattr(datasource, 'studio_datasource_id')
      elif 'looker_explore_reference' in datasource:
        source_name = format_looker_table_ref(getattr(datasource, 'looker_explore_reference'))
      else:
        source_name = format_bq_table_ref(getattr(datasource, 'bigquery_table_reference'))
    
      print(source_name)
      display_schema(datasource.schema)
    
    def handle_schema_response(resp):
      if 'query' in resp:
        print(resp.query.question)
      elif 'result' in resp:
        display_section_title('Schema resolved')
        print('Data sources:')
        for datasource in resp.result.datasources:
          display_datasource(datasource)
    
    def handle_data_response(resp):
      if "query" in resp:
        query = resp.query
        display_section_title("Retrieval query")
        print(f"Query name: {query.name}")
        if "question" in query:
          print(f"Question: {query.question}")
        if "datasources" in query:
          print("Data sources:")
          for datasource in query.datasources:
            display_datasource(datasource)
      elif "generated_sql" in resp:
        display_section_title("SQL generated")
        print(resp.generated_sql)
      elif "result" in resp:
        display_section_title("Data retrieved")
    
        fields = [field.name for field in resp.result.schema.fields]
        d = {}
        for el in resp.result.data:
          for field in fields:
            if field in d:
              d[field].append(el[field])
            else:
              d[field] = [el[field]]
    
        display(pd.DataFrame(d))
    
    def handle_chart_response(resp):
      def _value_to_dict(v):
        if isinstance(v, proto.marshal.collections.maps.MapComposite):
          return _map_to_dict(v)
        elif isinstance(v, proto.marshal.collections.RepeatedComposite):
          return [_value_to_dict(el) for el in v]
        elif isinstance(v, (int, float, str, bool)):
          return v
        else:
          return MessageToDict(v)
    
      def _map_to_dict(d):
        out = {}
        for k in d:
          if isinstance(d[k], proto.marshal.collections.maps.MapComposite):
            out[k] = _map_to_dict(d[k])
          else:
            out[k] = _value_to_dict(d[k])
        return out
    
      if 'query' in resp:
        print(resp.query.instructions)
      elif 'result' in resp:
        vegaConfig = resp.result.vega_config
        vegaConfig_dict = _map_to_dict(vegaConfig)
        alt.Chart.from_json(json_lib.dumps(vegaConfig_dict)).display();
    
    def show_message(msg):
      m = msg.system_message
      if 'text' in m:
        handle_text_response(getattr(m, 'text'))
      elif 'schema' in m:
        handle_schema_response(getattr(m, 'schema'))
      elif 'data' in m:
        handle_data_response(getattr(m, 'data'))
      elif 'chart' in m:
        handle_chart_response(getattr(m, 'chart'))
      print('\n')
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
