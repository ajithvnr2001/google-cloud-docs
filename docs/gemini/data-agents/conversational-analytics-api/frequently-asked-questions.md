---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/frequently-asked-questions/
title: Frequently asked questions about the Conversational Analytics API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:37.184738+00:00
---

# Frequently asked questions about the Conversational Analytics API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/frequently-asked-questions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Frequently asked questions about the Conversational Analytics API Stay organized with collections  Save and categorize content based on your preferences. 

This page answers frequently asked questions about the Conversational Analytics API.

## Can the Conversational Analytics API alter or delete my data?

The Conversational Analytics API is designed with safeguards to prevent altering or deleting your data.

Here's how data safety is handled for different data sources:

  * **BigQuery** : The API blocks Data Definition Language (DDL) and Data Manipulation Language (DML) statements. Specifically, the system performs a test run on generated SQL and only permits `SELECT` type queries.
  * **Looker** : The API interacts with Looker by using methods like `run_inline_query`, which are restricted to read operations such as selections, filters, and limits. These methods don't support DDL or DML operations and don't include delete or drop operations.
  * **Data Studio (for CSVs and Google Sheets)** : Data Studio uses a structured format to define and fetch data for visualizations and reports. Any queries that are executed with this method are read-only and don't support data mutations.
  * **Databases** : The system only permits `SELECT` type queries. To prevent data alteration or deletion, make sure that the service account or user interacting with the Conversational Analytics API has read-only permissions to your database.



The Conversational Analytics API is designed to be read-only across these data sources. For more information about the security of the Conversational Analytics API, see the [Chat with confidence: Unpacking security in Looker Conversational Analytics](https://cloud.google.com/blog/products/business-intelligence/understanding-looker-conversational-analytics-security?e=48754805) blog post.

## How do I handle authentication and permission errors?

**Note:** See our [Troubleshoot Conversational Analytics API errors](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/troubleshoot-ca-errors) guide for more information about errors and potential solutions.

Here are some common authentication and permission errors you might encounter when using the Conversational Analytics API:

  1. **Error** : `PERMISSION_DENIED` or `403 Write access to project ... was denied`

     * **Likely Cause** : This message often indicates issues with Google Cloud IAM roles. The user or service account that is attempting to use the API lacks the necessary permissions on the Google Cloud project.
     * **Troubleshooting** : 
       * The Google Cloud project owner must ensure that the user or service account has the correct IAM roles assigned in the Google Cloud project. Roles like `Project Editor` might be needed for certain operations, such as enabling the API or testing its functions.
       * If you encounter a 403 error like `Write access to project 'us-gcp-project-name' was denied` when switching regions, verify your project's IAM configuration.
  2. **Error** : `500 Internal Server Error` when a Looker user with a **User** role tries to chat with a data agent.

     * **Likely Cause** : The Looker user might not have sufficient permissions.
     * **Troubleshooting** : Make sure that users are [granted the appropriate roles in IAM and in Looker](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control) to chat with a data agent. See the answer to What are the Looker requirements for using the Conversational Analytics API? in this FAQ for more information.



## Why do I see 503 or 500 errors when streaming responses?

If you use a basic HTTP or REST client (such as the Python `requests` library) to call the streaming `:chat` endpoint, the API might return a generic error message, such as `503 Connection reset by peer` or `500 Internal error`.

These generic errors occur because the streaming API sends an HTTP `200 OK` header as soon as the stream opens. If the data agent encounters a fatal error during the stream (such as a timeout for a long-running query or a sudden permission denial), it terminates the stream and includes the specific error code in the HTTP/2 trailers. Standard HTTP or REST clients cannot parse these trailing headers and instead interpret the abrupt termination as a socket crash.

To handle errors that occur during a stream, we strongly recommend using the official Google Cloud client libraries (SDKs), such as the Python SDK. These gRPC-based SDKs parse HTTP/2 trailers and return the specific error code, such as `DEADLINE_EXCEEDED` or `PERMISSION_DENIED`) instead of a generic network error.

## What are the Looker requirements for using the Conversational Analytics API?

To use the Conversational Analytics API, you need appropriate permissions both in Google Cloud IAM and within Looker, depending on the data source and the actions that you want to perform:

  1. **Google Cloud IAM roles** :

     * You need sufficient IAM roles on your Google Cloud project to interact with the `geminidataanalytics.googleapis.com` API. Misconfigured IAM roles often lead to `PERMISSION_DENIED` errors.
     * The specific roles required can depend on the actions, but general roles like **Project Editor** might be necessary for certain operations.
  2. **Looker permissions and roles** :

     * **Model level permissions** : To use Conversational Analytics and the Conversational Analytics API, a Looker user must be assigned a [Looker role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) that contains the `gemini_in_looker` permission for the models that they interact with.



To learn more about the permissions and roles that are required to use the Conversational Analytics API, see the [Grant Conversational Analytics API IAM roles and permissions](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control) documentation page for more information.

Additionally, your Looker instance must meet specific requirements:

  * [Looker (original)](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil#before_you_begin)
  * [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini#before_you_begin)



To use the Conversational Analytics API with Data Studio Pro, your Pro subscription must be outside of a VPC-SC perimeter.

## What are the database requirements for using the Conversational Analytics API?

To use the Conversational Analytics API with databases like AlloyDB for PostgreSQL, GoogleSQL for Spanner, Cloud SQL for MySQL, and Cloud SQL for PostgreSQL, you need to ensure proper IAM authentication and enablement:

  1. **Google Cloud IAM roles** :

     * The service account or user must have the necessary IAM roles to connect to and query the specific database. This typically involves roles with read access to the database.
  2. **API Enablement** :

     * Ensure that the Cloud AI Companion API is enabled in your Google Cloud project.



For more information about how to enable IAM authentication, see the documentation for each database:

  * AlloyDB: [Manage IAM authentication](https://docs.cloud.google.com/alloydb/docs/database-users/manage-iam-auth).
  * Spanner: [Authenticate to Spanner](https://docs.cloud.google.com/spanner/docs/authentication).
  * Cloud SQL for MySQL: [IAM authentication](https://docs.cloud.google.com/sql/docs/mysql/iam-authentication).
  * Cloud SQL for PostgreSQL: [IAM authentication](https://docs.cloud.google.com/sql/docs/postgres/iam-authentication).



## How do I migrate from the Data QnA API to the Conversational Analytics API?

If you used the older, experimental version of the Data QnA API (`dataqna.googleapis.com`), see the [migration guide](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/migration-guide) for how to migrate to the new, official endpoint for the Conversational Analytics API (`geminidataanalytics.googleapis.com`).

## What is the difference between a data agent's name and its ID?

The data agent's ID, which is defined as the value for `data_agent_id`, is the unique identifier for the data agent. The data agent's name, `data_agent.name`, is derived automatically from the `data_agent_id` as a fully qualified name (FQN), taking the form `projects/<project>/locations/<location>/dataAgents/<data_agent_id>`.

When creating a data agent, any value that you may have entered for `data_agent.name` is ignored. When performing `get`, `update`, or `delete` operations, the full `data_agent.name` is treated as the unique identifier of the data agent.

When using the Conversational Analytics API to create data agents, the following scenarios apply:

  * If you don't define `data_agent_id`, a unique ID is generated automatically.
  * If you define `data_agent_id` as, for example, `TestID`, any value that you may have entered for `data_agent.name` is overwritten with `projects/<project>/locations/<location>/dataAgents/TestID`.
  * If you define `data_agent_id` with a FQN, you receive a "malformed name" error.



## What is the accepted format for an ID in Create Agent or Create Conversation?

For data agents:

`projects/{project}/locations/{location}/dataAgents/{data_agent_id}`

`{data_agent}` is the resource ID. It should be 63 characters or fewer and must match the format that's described in <https://google.aip.dev/122#resource-id-segments>.

Example: `projects/1234567890/locations/us-central1/dataAgents/my-agent`

We recommend that you skip setting this field during agent creation as it will be inferred automatically and overwritten with `{parent}/dataAgents/{data_agent_id}`.

For conversations:

`projects/{project}/locations/{location}/conversations/{conversation_id}`

`{conversation_id}` is the resource ID and should be 63 characters or less and must match the format described in <https://google.aip.dev/122#resource-id-segments>.

Example: `projects/1234567890/locations/us-central1/conversations/my-conversation`.

We recommend that you skip setting this field during conversation creation because Conversational Analytics will automatically identify and then overwrite it with `{parent}/conversations/{conversation_id}`.

## How do I use `updateMask`?

In the [data agent `patch` method](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents/patch), the `updateMask` parameter takes a [`FieldMask` format string](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask) that specifies which `dataAgent` fields will be overwritten in the `dataAgent` resource by the update. The `updateMask` parameter is a required field and is validated as follows:

  * If `updateMask` is empty, a `BadRequestException` will be thrown and no fields will be updated.
  * If all of the fields in the `updateMask` are valid `dataAgent` fields, only those fields will be updated.
  * If a mix of valid and invalid fields is provided, the invalid fields will be ignored, and only the valid ones will be updated.



## How do I use `getIAMPolicy` and `setIAMPolicy` to set the IAM policy for a data agent?

You can use the [`getIamPolicy` method](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents/getIamPolicy) and [`setIamPolicy` method](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents/setIamPolicy) to assign IAM roles to users for a specific agent.

**Important:** The `setIamPolicy` method overrides existing permissions for the agent. To preserve existing policies, call the `getIAMPolicy` method first to fetch the existing policy, and then pass the existing policy along with any additional changes in the call to `setIamPolicy`.

The following code samples demonstrate how to fetch the IAM policy for a data agent:

  * [`getIAMPolicy` using HTTP](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http#get-iam-policy-for-data-agent)
  * [`getIAMPolicy` using the Python SDK](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk#get-iam-policy-for-data-agent)



The following code samples demonstrate how to assign IAM to a data agent:

  * [`setIAMPolicy` using HTTP](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http#set-iam-policy-for-data-agent)
  * [`setIAMPolicy` using the Python SDK](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk#set-iam-policy-for-data-agent)



## What are the Conversational Analytics API data agent's memory capabilities?

  * **Within a single session** : The Conversational Analytics API supports multi-turn conversations, meaning it can reference earlier parts of the _current_ conversation.
  * **Across multiple sessions** : The Conversational Analytics API includes features for managed conversation history, allowing users to chat over multiple sessions. It also supports stateful agents with Google-managed multi-turn conversations.
  * **Long-term memory** : Conversational Analytics API data agents don't support explicit long-term memory capabilities.

**Note:** Your messages may not be persisted in conversations with your data agent if the Conversational Analytics API returns anything other than a success response.

## Will a Conversational Analytics API data agent give me the same answer every time I ask the same question?

  * **Natural language responses** from the Conversational Analytics API data agent aren't deterministic, so the natural language answer provided by the agent may vary even for an identically worded question.
  * **Data query responses** : However, for a specific data-seeking question, the underlying generated query (SQL or Looker query) is expected to be deterministic. The data that's retrieved should be the same, assuming that the underlying data hasn't changed.



## How can I improve the accuracy of the responses from a Conversational Analytics API data agent?

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

One way to improve the accuracy of data agent responses is to provide the data agent with robust contextual information. You can add context in the following ways:

  * In Looker's semantic layer, you can provide context within the LookML definitions. For more information and examples, see the [Guide agent behavior with authored context in Looker](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-looker) documentation page.
  * For BigQuery data sources, you can provide authored context through structured context fields — such as table-level and column-level descriptions, synonyms, tags, and example queries — and through system instructions. Providing this context also helps to improve response accuracy and can enable agents to cite sources in their responses. For more information, see [Define data agent context for BigQuery data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-bq).
  * In AlloyDB for PostgreSQL, Cloud SQL for MySQL, Cloud SQL for PostgreSQL, and Spanner data sources, you can provide context by adding table, column, schema descriptions, and constraints as guidance for the data and how to interpret that data.
  * When you create a data agent, you can provide system instructions, verified queries, and advanced context:

    * System instructions, which are user-defined guidance that can shape the behavior of a data agent. This guidance includes business-specific logic, response formatting, or data presentation.
    * You can provide _verified queries_ (also referred to as _golden queries_ depending on the data source), which are sample natural language questions that are paired with their correct SQL or Looker queries.
    * For AlloyDB, Cloud SQL for MySQL, Cloud SQL for PostgreSQL, and Spanner data sources, you can provide advanced context, which helps you optimize your agents' data understanding and accuracy.

For more information, see [Guide agent behavior with authored context](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-system-instructions).




See the [Ask effective questions](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/ask-effective-questions) page for guidance about asking questions for more effective and accurate responses.

## How can I safely inspect and handle agent-generated Python code?

If you have enabled advanced analysis with Python, your data agent might return Python code. The Python code that data agents return is designed to execute within a secure, Google-managed sandbox. Executing this code in a local or other unverified environment bypasses the sandbox's security protections and can expose your system to security risks, such as the execution of malicious code.

To safely inspect and handle agent-generated Python code, follow these guidelines:

  * Manually inspect the generated code before running it. Look for suspicious patterns such as unexpected network requests (for example, `socket`, `requests`, or `urllib`), system-level commands (for example, `os.system` or `subprocess`), or heavily obfuscated string literals and variables.
  * Never run unverified code directly on a local machine or within a production environment. Use a secure, isolated sandbox — such as a Colaboratory notebook, an ephemeral Docker container, or a virtual machine — that doesn't have access to sensitive credentials, internal networks, or local file systems.
  * Where possible, before you run the code, you should run static analysis tools or linters on the code to flag potentially unsafe operations or known malicious patterns.



## Can I integrate the Conversational Analytics API with third-party applications?

Integrating the Conversational Analytics API with third-party applications allows users to interact with their data directly within the tools that they use daily.

Any third-party application that interacts with the `geminidataanalytics.googleapis.com` API endpoints must be able to send user messages from the application to the agent and display the responses.

To build an integration, see the [Conversational Analytics Quickstarts repository](https://github.com/looker-open-source/ca-api-quickstarts) for examples or libraries. You can also visit the [Google Developer Forums](https://discuss.google.dev/) to search for examples from other users.

## How much does the Conversational Analytics API cost?

The Conversational Analytics API is in General Availability (GA). For more information about pricing, see the [pricing guide](https://cloud.google.com/products/data-agents/pricing).

Additionally, queries that data agents execute against data sources such as BigQuery might incur costs from those services. For BigQuery, you can [manage costs](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/manage-costs) by setting quotas or limiting bytes billed per query by using the `bigquery_max_billed_bytes` parameter.

## What data sources does the Conversational Analytics API support?

**Note:** The `QueryData` method supports only database data sources.

The Conversational Analytics API supports the following data sources:

  * BigQuery (including tables and graphs with [BigQuery Graph](https://docs.cloud.google.com/bigquery/docs/graph-overview))
  * Looker Explores
  * Data Studio
  * AlloyDB for PostgreSQL
  * GoogleSQL for Spanner
  * Cloud SQL for MySQL and Cloud SQL for PostgreSQL



You can also connect to sources like SAP and Salesforce through BigQuery, and to CSVs and Google Sheets through Data Studio.

## What are the known limitations of the Conversational Analytics API?

To learn more about the known limitations of the Conversational Analytics API, see the [Conversational Analytics API known limitations](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/known-limitations) documentation page.

## What quotas do I need to be aware of for Google Cloud projects?

There are no restrictions on Google Cloud project selection or location. You can create data agents to query supported data sources that belong to any project or region.

## Does the Conversational Analytics API support data residency?

Yes, the Conversational Analytics API supports data residency. To control where your data is processed and stored, specify a regional or multi-regional service endpoint when making API requests. For detailed information about specific location support and configuration details, see [Data residency](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-residency).

## Does the Conversational Analytics API support languages other than English?

The only officially supported language for the Conversational Analytics API is **English**. Although the underlying Gemini models support many languages, and some users have reported anecdotal success with non-English queries, the Conversational Analytics API doesn't officially support languages other than English.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
