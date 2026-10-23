---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/known-limitations/
title: Conversational Analytics API known limitations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:26.713898+00:00
---

# Conversational Analytics API known limitations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/known-limitations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Conversational Analytics API known limitations Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Conversational Analytics API has the following known limitations on the number of data sources, style of visualizations, and size of datasets.

## Data source limitations

This section describes the constraints and behaviors of the Conversational Analytics API when you connect to and query Looker and database sources— AlloyDB for PostgreSQL, Cloud SQL for MySQL, Cloud SQL for PostgreSQL, and Spanner.

### Looker data source limitations

When you connect to a Looker data source, note the following:

  * You can query any included Explore in a conversation.
  * An agent can only query one Explore at a time. It is not possible to perform queries across multiple Explores simultaneously.
  * An agent can query multiple Explores in the same conversation.
  * An agent can query multiple Explores in a conversation that includes questions with multiple parts, or in conversations that include follow-up questions.

For example: A user connects two Explores, one called `cat-explore` and one called `dog-explore`. The user inputs the question "What's greater: the count of cats or the count of dogs?" This would create two queries: one to count the number of cats in `cat-explore` and one to count the number of dogs in `dog-explore`. The agent compares the number from both queries after completing both queries.

  * The `QueryData` method does not support BigQuery or Looker data sources.




### Database data source limitations

When you connect to an AlloyDB, Cloud SQL for MySQL, Cloud SQL for PostgreSQL, or Spanner data sources, consider the following:

  * Data agents access the data using the credential of the user who is interacting with the data agent. If a user accesses a shared data agent for which they don't have access to the agent's configured tables, then the data agent can't access those tables.

  * The table selection for the data agent guides your agent about which tables to focus on. Table selection isn't a security setting. Even if you specify that the data source can only pull information from certain tables—like `table1` and `table2`—the system might still return data from an unintended table (`table3`) if the user running the query has general permissions to view the content of `table3` in the same database.




## Visualization limitations

The following visualization types are supported:

  * Area
  * Bar
  * Geoshape
  * Heatmap
  * Line (Time series)
  * Pie
  * Scatter

**Note:** Charts with tooltips are partially supported and may exhibit unexpected behavior.

## Data processing limitations

  * For Looker data sources, the Conversational Analytics API can return a maximum of **5,000 rows** per query.
  * For BigQuery data sources, the Conversational Analytics API limits data queries to 500 GB of bytes processed.
  * For AlloyDB, Cloud SQL for MySQL, Cloud SQL for PostgreSQL, and Spanner data sources, the Conversational Analytics API can return a maximum of 1,000 rows per query.
  * The Conversational Analytics API's Python-based reasoning and content retrieval capabilities can accommodate time complexities of up to `O(100k)` rows.
  * Querying large amounts of data can cause reduced reasoning accuracy in data agents.
  * The Conversational Analytics API has a maximum token output length of **8,192 tokens**. Querying large amounts of data can return a `MAX_TOKENS` error.
  * The data returned within the `DataResult` field of a system message is subject to a size limit. Data results are truncated to a maximum of 3,000,000 bytes. This truncation process keeps as many full rows as possible within this size constraint.



## Query limitations

  * BigQuery's flexible column names feature isn't supported.
  * Structs in BigQuery are supported but may sometimes fail.
  * For Looker data sources, the API can't set the value of a filter-only field that is defined by using the LookML `parameter` parameter.
  * Using the Conversational Analytics API to connect to a private IP Looker (Google Cloud core) instance using Data Studio Pro when that Looker (Google Cloud core) instance is inside a VPC Service Controls perimeter isn't a supported configuration and doesn't meet VPC Service Controls compliance requirements.
  * For connections to [Looker (Google Cloud core) instances with private IP configurations](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections), the Conversational Analytics API doesn't support Looker (Google Cloud core) instances that are [configured to use CMEK](https://docs.cloud.google.com/looker/docs/looker-core-cmek) or VPC Service Controls.
  * The Conversational Analytics API doesn't work well with Data Studio data sources that have [field editing in reports](https://docs.cloud.google.com/looker/docs/studio/edit-fields-in-your-reports) disabled because this setting prevents Conversational analytics from creating calculated fields.
  * When a failure occurs during query validation or execution, the Conversational Analytics API may automatically retry the operation by generating a corrected query. This kind of retry will be attempted a maximum of three times per request.

If a query fails because of permission or authentication issues, the Conversational Analytics API won't retry the query. Retries are non-deterministic; if the error message suggests that a query is unrecoverable, then the Conversational Analytics API won't try the query again, even if it's still below the limit of three errors per request.




## Quota limitations

  * The Conversational Analytics API has the following limits for overall requests (including both chat and non-chat requests): 
    * A maximum rate of 30 queries per second (QPS), which is 1,800 queries per minute (QPM) per project.
    * A maximum rate of 10 QPS, which is 600 QPM per user per project.
  * As an exception, chat requests have more restrictive limits: 
    * A maximum rate of 30 QPM per project.
    * A maximum rate of 30 QPM per user per project.
    * Each chat request counts as 8 quota units, rather than the standard of 1 unit. As a result, the Google Cloud console [Quotas](https://console.cloud.google.com/apis/api/geminidataanalytics.googleapis.com/quotas) page displays limits that are 8 times the actual request limits. For example, a limit of 240 units represents 30 chat requests.
  * Agent-to-Agent (A2A) requests have a maximum rate of 10 QPS, which is 600 QPM per project per agent.
  * Conversational Analytics API for AlloyDB, Cloud SQL for MySQL, Cloud SQL for PostgreSQL, and Spanner has a 50 QPM limit per project. To increase these limits, contact [Google Cloud Customer Care](https://cloud.google.com/support?e=48754805).



## Question types limitations

  * The Conversational Analytics API supports questions that can be answered by a single visualization, for example:

    * Metric trends over time
    * Breakdown or distribution of a metric by dimension
    * Unique values for one or more dimensions
    * Single metric values
    * The top dimension values by metric
  * The Conversational Analytics API doesn't yet support questions that can only be answered with the following types of complicated visualizations:

    * Prediction and forecasting
    * Advanced statistical analysis, including correlation and anomaly detection



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
