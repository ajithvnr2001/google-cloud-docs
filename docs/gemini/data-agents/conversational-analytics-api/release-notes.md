---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/release-notes/
title: Conversational Analytics API release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:59.365522+00:00
---

# Conversational Analytics API release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Conversational Analytics API release notes Stay organized with collections  Save and categorize content based on your preferences. 

These release notes are for updates to the [Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview).

## October 16, 2026

**Conversational Analytics API updates:**

Feature

The Conversational Analytics API now supports the following regional endpoints in Canada for BigQuery data sources:

  * `northamerica-northeast1` (Montréal)
  * `northamerica-northeast2` (Toronto)



These endpoints support data residency for data at rest and jurisdictional machine learning (ML) processing for data in use. For more information, see [Locations](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/locations) and [Data residency](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-residency).

## October 13, 2026

**Conversational Analytics API updates:**

Feature

If [`thinkingMode`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations/chat#thinkingmode) is left unspecified in the data agent configuration, data agents that use Looker data sources now default to `FAST`, rather than `THINKING`.

## September 30, 2026

**Conversational Analytics API updates:**

Feature

Connections to [BigQuery Graph](https://docs.cloud.google.com/bigquery/docs/graph-overview) in the Conversational Analytics API are now generally available (GA). You can configure a data agent to query one or more graphs or to combine tables and graphs in the same data source configuration.

Depending on your graph schema and the question that is being asked, the Conversational Analytics API queries a graph by using either Graph Query Language (GQL) or the [`GRAPH_EXPAND`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/graph-sql-queries#graph_expand) table-valued function in SQL. GQL queries require a [BigQuery Enterprise or Enterprise Plus edition](https://docs.cloud.google.com/bigquery/docs/editions-intro) reservation, while `GRAPH_EXPAND` queries can run with on-demand pricing. For requirements and limitations, see [Connect to BigQuery Graph](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/connect-bigquery#connect-to-bq-graph).

## September 3, 2026

**Conversational Analytics API updates:**

Feature

The Conversational Analytics API now supports agent observability. You can monitor performance, latency, and token usage in the Google Cloud console or by using Cloud Monitoring and Cloud Trace. For more information, see [Create data agents](https://docs.cloud.google.com/bigquery/docs/create-data-agents#monitor_agents_and_conversations).

Feature

The Conversational Analytics API now supports Deep Dive thinking mode for BigQuery data sources in [Preview](https://docs.cloud.google.com/products#product-launch-stages). Deep Dive mode lets data agents break down complex questions, investigate sub-questions, and synthesize findings into a detailed report.

This feature is gated by an allowlist. To request access and the user guide, submit the [Conversational Analytics Preview features interest form](https://docs.google.com/forms/d/e/1FAIpQLSfSz-AnPwi-Dk2DJB7614gRcsKF_tUTXj1DOMCDbce_I0EyRQ/viewform) and select the **Deep Dives** option.

Deep Dive mode has the following requirements and limitations during Preview:

  * Deep Dive supports only BigQuery data sources.
  * Deep Dive isn't supported with `LATEST_GA_MODEL`.
  * Queries typically take 3 to 5 minutes to complete. Because the service deadline is 5 minutes, set your client timeout to match.
  * Multi-turn conversations aren't supported. Conversation history is cleared during the solve phase.



Feature

The Conversational Analytics API is now HIPAA compliant. For more information, see [HIPAA compliance on Google Cloud](https://cloud.google.com/security/compliance/hipaa).

Feature

The Conversational Analytics API now supports [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview) and [Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview) for `DataAgent` and `Conversation` resources.

## June 23, 2026

**Conversational Analytics API updates:**

Announcement

**The Conversational Analytics API is generally available (GA) for BigQuery and Looker.**

For information on pricing, see [Data Cloud Agent Pricing and Free Trial](https://cloud.google.com/products/data-agents/pricing).

Feature

The Conversational Analytics API supports `v1` REST endpoints.

Feature

Data residency is now supported for the Conversational Analytics API. You can control the physical location of `DataAgent` and `Conversation` resources by using regional and multi-regional endpoints. These endpoints provide commitments for data at rest and, depending on your data source, jurisdictional machine learning (ML) processing for data in use. For more information, see [Data residency](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-residency) and [Locations](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/locations).

Feature

The Conversational Analytics API supports the following enterprise security and compliance features:

  * [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/cmek) to protect data agents and conversations
  * [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) to protect resources within a service perimeter
  * [Cloud Audit Logs](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/audit-logging) to log admin activity and data access
  * [Data retention and deletion](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/retention-deletion) to support enterprise data wipeout and retention policies



Feature

The Conversational Analytics API now supports the agent-to-agent (A2A) protocol in [Preview](https://docs.cloud.google.com/products#product-launch-stages). You can use new API methods, such as [`SendMessage`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/a2a.projects.locations.dataAgents.v1.message/send), [`SendStreamingMessage`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/a2a.projects.locations.dataAgents.v1.message/stream), and [`GetAgentCard`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/a2a.projects.locations.dataAgents.v1/getCard), to orchestrate multiple agents. For an example of how to use these methods, see the [A2A SDK sample notebook](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/gemini_data_analytics/a2a_sdk_sample.ipynb).

Feature

The Conversational Analytics API now supports filtering and sorting for list methods. Use the `[filter](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents/list#body.QUERY_PARAMETERS.filter)` field to narrow results for data agents, conversations, and messages. Use the `[orderBy](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1/projects.locations.dataAgents/list#body.QUERY_PARAMETERS.order_by)` field to sort data agents by name or creation time.

  * For data agents, you can filter by name, creation time, and labels.
  * For conversations, you can filter by associated agents and labels.
  * For messages, you can filter by creation time.
  * Wildcard support is available for string filters that include the has (`:`) operator and a trailing asterisk (`*`). Examples: `filter=display_name:"*"` or `filter=display_name:"foo*"`.
  * Conversations and messages are returned in order of most recent activity; custom sorting is not supported for these resources.



Feature

This release includes the following features and improvements for BigQuery data sources:

  * You can now use the `big_query_max_billed_bytes` field in your agent's configuration to [limit the bytes billed](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/manage-costs) for BigQuery jobs that the agent initiates.
  * Data agents can now [cite sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/key-concepts#how-data-agents-work), such as glossary terms or example queries, that are used to generate a response.
  * You can now [provide custom BigQuery user-defined functions (UDFs)](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-bq#user-functions) that the agent can use to answer questions.
  * If a user's question sufficiently matches a defined [example query](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-bq#example-queries), the agent might execute that query directly rather than generating a new one. When this occurs, the API response includes a `matchedQuery` object to indicate that a verified query was used.



Feature

The Conversational Analytics API now [supports chat with BigQuery Graph](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/authentication#connect-to-bigquery). This feature is in [Preview](https://docs.cloud.google.com/products#product-launch-stages).

Changed

The following changes and deprecations are in effect for the `v1` API:

  * SVG and PNG formats for charts aren't supported in the `v1` version. The `options.chart` field in `ChartOptions` is restricted to `v1alpha` and `v1beta` versions.
  * The `credentials` field under the `context` field (for example, `dataAgentContext.credentials`) is deprecated. For authentication, provide credentials directly in the `ChatRequest` object.
  * System-generated clarification messages (`systemMessage.clarification`) are deprecated. Use `TextMessage` with the `FINAL_RESPONSE` text type instead.



## April 16, 2026

**Conversational Analytics API updates:**

Feature

The Conversational Analytics API now supports querying Lakehouse tables that connect to the Apache Iceberg REST catalog or are federated to an external catalog. If you are using Lakehouse tables, use the four-part `project.catalog.namespace.table` (P.C.N.T) syntax. For more information, see [Authenticate and connect to a data source](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/authentication#connect-to-bigquery).

## March 30, 2026

**Conversational Analytics API updates:**

Feature

The Conversational Analytics API now supports AlloyDB for PostgreSQL, Cloud SQL for MySQL, Cloud SQL for PostgreSQL, and Spanner as data sources. This feature lets users query their operational data using natural language and translates complex human dialog into precise database queries to provide actionable insights. This feature is in [Preview](https://docs.cloud.google.com/products#product-launch-stages). For more information, see the following:

  * [Conversational analytics for AlloyDB overview](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/alloydb)
  * [Conversational analytics for Cloud SQL for MySQL overview](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-mysql)
  * [Conversational analytics for Cloud SQL for PostgreSQL overview](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/sql-postgres)
  * [Conversational analytics for Spanner overview](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics/spanner)



Feature

Updates to the Conversational Analytics API for BigQuery data sources include the following features and improvements:

  * The Conversational Analytics API now integrates with Cloud Storage through [ObjectRef functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/objectref_functions). This enables the API to answer questions about unstructured data in Cloud Storage buckets, such as images and PDFs, by referencing ObjectRef columns in any table.
  * The API now supports a set of BigQuery ML functions, including [`AI.FORECAST`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-forecast), [`AI.DETECT_ANOMALIES`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-detect-anomalies), and [`AI.GENERATE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate). The API can use these functions to answer a broader range of questions, such as for forecasting, anomaly detection, and generative AI tasks.
  * The Conversational Analytics API can now use BigQuery table partitioning. The API can optimize SQL queries by using partitioned columns, such as date ranges, on a date-partitioned table, which can improve query performance and reduce costs.
  * BigQuery jobs that are initiated by the Conversational Analytics API now include labels that allow you to identify them within your [BigQuery Job History](https://docs.cloud.google.com/bigquery/docs/managing-jobs#view-job) in the Google Cloud console. These labels can help with monitoring costs, auditing agent activity, and analyzing query performance. Because these labels are not directly visible in the BigQuery Studio job history table, you can identify them by querying `INFORMATION_SCHEMA.JOBS` for labels that are similar to `{'ca-bq-job': 'true'}`:
        
        SELECT
          COUNT(*) AS job_count
        FROM
          `PROJECT_ID`.`region-LOCATION`.INFORMATION_SCHEMA.JOBS
        WHERE
          EXISTS (
            SELECT 1
            FROM UNNEST(labels) AS label
            WHERE label.key = 'ca-bq-job' AND label.value = 'true'
          );

In the sample query, you would replace the sample values as follows:

    * `PROJECT_ID`: your Google Cloud project ID.
    * `LOCATION`: the location of your BigQuery jobs.



Feature

For data agents that use Looker or BigQuery data sources, you can now specify a [`thinkingMode`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations/chat#ThinkingMode) value of `FAST` in your chat request to enable "Fast" thinking mode. Fast thinking can help improve latency by decreasing the overall thinking time. However, this mode makes answers less transparent as no messages with a [`TextType` value of `THOUGHT`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/Message#TextType) are emitted in the response stream. Additionally, using this mode may impact the accuracy of responses.

Feature

For data agents that use Looker data sources, the agent can now ask follow-up questions to clarify ambiguities in a query, such as when there are multiple similarly named fields. These questions are returned as a `TextMessage` response with a `Clarification needed:` prefix. For more information, see [Ask effective questions](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/ask-effective-questions#ask-general-questions).

Feature

For data agents that use BigQuery data sources, the agent can now ask follow-up questions to clarify ambiguities in a query, such as when there are multiple fields with similar names. These questions are returned as a `TextMessage` response.

Changed

For data agents that use Looker data sources, several improvements have been made to reduce latency, including parallel tool calls and better use of the Looker cache.

## March 26, 2026

**Conversational Analytics API updates:**

Feature

For the Conversational Analytics API with Looker data sources, you can use customer-managed encryption keys (CMEK) to help protect `DataAgent` and `Conversation` resources at rest. CMEK in the Conversational Analytics API is available in Preview. For more information, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/cmek).

## February 11, 2026

**Conversational Analytics API updates:**

Feature

Chat requests with BigQuery data sources now provide more insight into the agent's reasoning process. Although the API schema is unchanged, you will observe the following new behaviors in the response stream:

  * The API response stream now includes additional [`systemMessage.text`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/Message#SystemMessage) messages with [`textType = THOUGHT`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/Message#texttype). These messages provide step-by-step insight into the agent's reasoning and decision-making process.
  * After the `THOUGHT` messages, the API returns the answer as a sequence of messages, such as query, job, text, data result, and chart messages. For more information about message types, see [`SystemMessage`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/Message#SystemMessage).
  * Schema messages are no longer included in the response stream for BigQuery data sources.



Feature

Synchronous agent management methods are available. These methods allow you to create, update, and delete data agents synchronously as an alternative to existing asynchronous methods:

  * `CreateDataAgentSync`
  * `UpdateDataAgentSync`
  * `DeleteDataAgentSync`



Changed

The Python analysis option (`options.analysis.python.enabled`) is no longer supported for BigQuery data sources.

## February 6, 2026

**Conversational Analytics API updates:**

Feature

For data agents that use Looker data sources, you can now define [golden Looker queries](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-looker#define-golden-query-looker) as structured context.

## January 26, 2026

**Conversational Analytics API updates:**

Feature

Improved reasoning transparency, which provides step-by-step insight into the agent's reasoning and decision-making process with `textType = THOUGHT` messages, no longer requires an allowlist and is available to all users for Looker data sources.

Feature

Granular data retrieval for Looker data sources, which provides updates on data value searches with `textType = PROGRESS` messages, no longer requires an allowlist and is available to all users.

## December 15, 2025

**Conversational Analytics API updates:**

Feature

The API response stream for Looker data sources includes additional `systemMessage.text` messages with [`textType = THOUGHT`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/Message#texttype). These messages provide step-by-step insight into the agent's reasoning and decision-making process as it works to answer your query. To run chat examples that demonstrate this reasoning, see the [HTTP](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/agents/gemini_data_analytics/intro_gemini_data_analytics_http.ipynb#scrollTo=mQ1G8_UnKQjT) and [Python SDK](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/agents/gemini_data_analytics/intro_gemini_data_analytics_sdk.ipynb#scrollTo=t6453RzShYWB) Colaboratory notebooks. For guidance on rendering `THOUGHT` messages with Looker data sources, see [Render agent responses for Looker data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/render-looker-data). This is an early announcement of an experimental feature that is available upon request. To request access to this feature, send an email to [conversational-analytics-api-feedback@google.com](mailto:conversational-analytics-api-feedback@google.com).

**Note:** As of January 26, 2026, this feature no longer requires an allowlist and is available to all users for Looker data sources; see entry for January 26, 2026.

Feature

For Looker data sources, agents use more granular methods to retrieve Explore schemas and data values. When the agent searches for specific data values, the API stream also includes `systemMessage.text` messages with [`textType = PROGRESS`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/Message#texttype), providing updates on search status and results. For guidance on rendering `PROGRESS` messages, see [Render agent responses for Looker data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/render-looker-data). This is an early announcement of an experimental feature that is available upon request. To request access to this feature, send an email to [conversational-analytics-api-feedback@google.com](mailto:conversational-analytics-api-feedback@google.com).

**Note:** As of January 26, 2026, this feature no longer requires an allowlist and is available to all users for Looker data sources; see entry for January 26, 2026.

Feature

The integration of the Conversational Analytics API with VPC Service Controls is in Preview. This integration is ready for broader testing and use, but is not fully supported for production environments. For more details, see the [supported products list](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_conversational_analytics).

Fixed

An issue with `[big_query_max_billed_bytes](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#datasourceoptions)` not being correctly applied has been fixed.

Fixed

Issues with how the API handles Looker data sources have been fixed, including the following:

  * Better value formatting in text responses
  * Better filtering for exact matches
  * Improved period-over-period (PoP) measure support
  * Improved `always_filter` support



**Client library updates:**

Feature

The following client libraries have been added:

  * [Node.js (v1beta)](https://www.npmjs.com/package/@google-cloud/geminidataanalytics)
  * [Java (v1beta)](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/overview)
  * [Go (v1beta)](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/geminidataanalytics/latest/apiv1beta)
  * [Ruby (v1beta)](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest)



## October 21, 2025

**Conversational Analytics API updates:**

Feature

Support for the [`deleteConversation` API method](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.conversations/delete) has been added to the REST APIs and SDK.

## September 25, 2025

**Conversational Analytics API updates:**

Feature

A new API, `ListAccessibleDataAgents`, is now available to list data agents that are accessible to a user in a project. A data agent is considered accessible if the user who invokes the API has the `get` permission on the agent. You can use the `creator_filter` field to manage which agents this method returns:

  * `NONE` (default): Returns all data agents that are accessible to the user, regardless of the creator.
  * `CREATOR_ONLY`: Returns only the data agents that were created by the user.
  * `NOT_CREATOR_ONLY`: Returns only the data agents that were created by other users.



Feature

The `systemMessage.text.textType` enum is now available with `FINAL_RESPONSE` and `THOUGHT` values, which helps clients distinguish between different types of text messages. The Conversational Analytics API now uses `systemMessage.text` messages with `textType = THOUGHT` to produce thinking steps.

Feature

The API now supports up to five Looker Explore data sources in context. Chat requests generate queries on the most relevant Explore. For more information, see the documentation on connecting to Looker data [with HTTP](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http#connect-to-looker-data) and [with the Python SDK](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk#connect-to-looker-data).

Changed

The `systemMessage.data.generatedLookerQuery` field is now `systemMessage.data.query.looker`.

## August 25, 2025

Announcement

**The Conversational Analytics API is now available in Public Preview.**

**Client library updates:**

Feature

The following client libraries are now available for multiple languages:

  * [PHP (v1beta)](https://docs.cloud.google.com/php/docs/reference/cloud-geminidataanalytics/latest)
  * [DotNet (v1beta)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GeminiDataAnalytics.V1Beta/latest)
  * [Python (v1beta)](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest)



**Conversational Analytics API updates:**

Feature

Support for `v1beta` endpoints for [HTTP REST](https://docs.cloud.google.com/gemini/data-agents/reference/rest) is now available.

Feature

Support for [`GetLocation`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations/get) and [`ListLocations`](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations/list) API methods has been added to the REST APIs and SDK.

Feature

You can now share data agents using the [`GetIamPolicy` and `SetIamPolicy` API methods](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview#key_api_operations).

Feature

You can now build data agents from Looker data sources that are based on Looker (Google Cloud core) instances that use private IP networks. (The Conversational Analytics API doesn't support data sources based on Looker (Google Cloud core) instances that are inside Virtual Private Cloud perimeters.)

Feature

[Structured context for BigQuery data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-bq) is now available. This includes the ability to add example question/query pairs, table descriptions, synonyms, and tags at the table and field levels using the API.

Changed

[Location and operation APIs](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.operations) are now supported. `DataAgentCreator` and `DataAgentEditor` Identity and Access Management roles will now have permissions for operation APIs.

Changed

An enhancement has been made for the automatic storage of `Last Published Context` in the server layer whenever a data agent's published context is updated.

Changed

The display names for Identity and Access Management roles have been updated to "Gemini Data Analytics Stateless Chat User" and "Gemini Data Analytics Data Agent Creator". For more information about the Identity and Access Management roles that are used with the API, see the [Grant Conversational Analytics API Identity and Access Management roles and permissions](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control) documentation page. 

Changed

Colaboratory version 1.1 is now available.

Fixed

Updates to error handling have been made to handle conversation-related 500 internal errors for stateful chat.

Fixed

Better exception handling messages have been implemented for 400 client errors.

**Documentation updates:**

Feature

You can now use the new [Streamlit Quickstart Application on GitHub](https://github.com/looker-open-source/ca-api-quickstarts) to set up a demo of the Conversational Analytics API in minutes.

Feature

The [Conversational Analytics API Golden Demo](https://github.com/looker-open-source/ca-demos-and-tools/blob/main/ca-api-golden-demo/README.md) is now available on GitHub. With the Conversational Analytics API Golden Demo, you can view examples to integrate the Conversational Analytics API into web applications as well as a full production demo in TypeScript. This project is intended for demonstration purposes only. It is not intended for use in a production environment.

Feature

Request payload code samples have been added for the [REST APIs](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http#manage-data-agents-and-conversations) and [SDK](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk#manage-data-agents-and-conversations).

Feature

[Conversational Analytics API architecture, workflows, and roles](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/key-concepts): Learn more about key concepts for using the Conversational Analytics API, including how data agents work, typical data agent workflows, conversation modes, Identity and Access Management roles, and how to design systems that use multiple data agents.

Feature

[Conversational Analytics API known limitations](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/known-limitations): Learn more about limitations on the number of data sources, style of visualizations, and size of datasets.

Feature

[Troubleshoot Conversational Analytics API errors](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/troubleshoot-ca-errors): Learn more about potential issues or errors with the Conversational Analytics API, as well as proposed solutions.

Feature

[Monitor and manage BigQuery costs for your Conversational Analytics API agents](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/manage-costs): Learn more about how to implement cost controls for your Conversational Analytics API agents.

Feature

`SetIAMPolicy` and `GetIAMPolicy` methods are available on the [Conversational Analytics API overview](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview#key_api_operations) documentation page for use in sharing data agents.

Feature

A new documentation page containing [answers to frequently asked questions about the Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/frequently-asked-questions) is now available.

Feature

[Define data agent context for BigQuery data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-bq): Learn more about how to write system instructions for BigQuery data sources.

Feature

[Define data agent context for Looker data sources](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-authored-context-looker): Learn more about how to write system instructions for Looker data sources.

## July 15, 2025

Feature

You can now invite users to collaborate on specific data agents by assigning predefined IAM roles. For details, see [Conversational Analytics API IAM roles and permissions](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control).

Feature

A new best practices guide helps you provide effective business and data context to your agents. For more information, see [Guide agent behavior with authored context](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-agent-system-instructions).

**SDK updates:**

Feature

You can now install the Python SDK from the [Python Package Index (PyPI)](https://pypi.org/project/google-cloud-geminidataanalytics/).

## June 25, 2025

**API updates:**

Feature

New predefined IAM roles control access for creating, managing, and interacting with data agents:

  * `geminidataanalytics.dataAgentCreator`
  * `geminidataanalytics.dataAgentOwner`
  * `geminidataanalytics.dataAgentEditor`
  * `geminidataanalytics.dataAgentUser`
  * `geminidataanalytics.dataAgentViewer`
  * `geminidataanalytics.dataAgentStatelessUser`



For a full list of roles and their permissions, see the [Grant Conversational Analytics API IAM roles and permissions](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/access-control).

## June 5, 2025

Announcement

The initial Private Preview of the Conversational Analytics API introduced capabilities for creating and interacting with data agents.

Feature

The following interactive Colaboratory notebooks are available for getting started with both REST and the Python SDK:

  * [HTTP Colab notebook](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/agents/gemini_data_analytics/intro_gemini_data_analytics_http.ipynb)
  * [Python SDK Colab notebook](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/agents/gemini_data_analytics/intro_gemini_data_analytics_sdk.ipynb)



**API updates:**

Feature

The [**Data Agent Service**](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents) lets you programmatically create, configure, and manage persistent, context-aware AI agents with Looker, Looker Studio, and BigQuery.

Feature

The [**Data Chat Service**](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations/chat) lets you engage in conversations with your agent by using multiple chat modes. These modes include a stateful mode where Google manages the conversation history, a stateful option where your application manages the conversation, and a stateless mode where your application provides the full context with each request.

Feature

The API supports [advanced analysis using Python](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations.dataAgents#python) and automatically retries failed queries.

Changed

The Conversational Analytics API (`geminidataanalytics.googleapis.com`) replaces the deprecated Data QnA API (`dataqna.googleapis.com`). This includes the migration from `DataQuestionService` to the new `DataChatService`. For detailed instructions on how to update your requests, see the [migration guide](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/migration-guide).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
