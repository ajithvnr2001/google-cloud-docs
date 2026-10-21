---
url: https://docs.cloud.google.com/looker/docs/conversational-analytics-overview/
title: Conversational Analytics in Looker overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:33:14.210535+00:00
---

# Conversational Analytics in Looker overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/conversational-analytics-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Conversational Analytics in Looker overview Stay organized with collections  Save and categorize content based on your preferences. 

Conversational analytics is a chat-with-your-data feature that is powered by [Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview). Grounded in the [Looker semantic modeling layer](https://docs.cloud.google.com/looker/docs/what-is-lookml), Conversational Analytics empowers users in your organization to ask data-related questions in regular, natural (conversational) language for governed, trusted self-service BI. This approach accelerates adoption of analytics across your organization by providing enterprise-grade governance and security.

Conversational analytics is available in both Looker (Google Cloud core) instances and in Looker (original) instances.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

## Key features

Conversational analytics includes the following key features:

  * **Query Explores in natural language** : Converse in natural language with an individual Explore or with a data agent that is querying as many as five Explores.
  * **Create a data agent to query Explores** : You can customize an AI-powered Explore-querying agent by providing context and instructions that are specific to your data, which helps the data agent generate more accurate and contextually relevant responses. You can also share your data agents with other users or publish them to other applications, like Gemini Enterprise, so that they can ask questions with the same context. You can connect this type of data agent to as many as five Explores. Add [verified queries](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents#define-verified-queries) to your data agent context to help improve the accuracy of responses from your Explore data agent.
  * **Query a dashboard by using a data agent** : Use Conversational Analytics to generate a dashboard data agent that can query a dashboard's underlying models. When dashboard agents are enabled, each dashboard provides a single, shared [default agent](https://docs.cloud.google.com/looker/docs/glossary#default-agent) that can query the dashboard and its query-linked tiles. Dashboard agents are available when the **Dashboard agents** setting is enabled on the **Gemini in Looker** page in the **Admin** panel. Additionally, dashboard creators can enable or disable dashboard agents at the individual dashboard level. Dashboard agents are available for user-defined dashboards and for LookML dashboards. 
  * **Advanced analytics** : The **Advanced Analytics** feature within Conversational Analytics translates your natural language questions into Python code and executes that code. Compared to standard SQL-based queries, the **Advanced Analytics** feature's use of Python enables more complex analysis and visualizations.
  * **Embedding** : You can embed Conversational Analytics in a website or an application by using an HTML iframe tag just as you can with other Looker content types. Conversational analytics supports both [private embedding](https://docs.cloud.google.com/looker/docs/private-embedding), where users are authenticated with their Looker login, and [signed embedding](https://docs.cloud.google.com/looker/docs/signed-embedding), where users are authenticated through your own application.
  * **User engagement and token usage** : Users with access to Looker [System Activity](https://docs.cloud.google.com/looker/docs/system-activity-dashboards#conversational-analytics) can monitor user engagement and the token usage of Conversational Analytics agents across the instance. The **Conversational Analytics** dashboard is available in the **System Activity** section of the **Admin** panel.
  * **User query responses and feedback** [[Preview](https://cloud.google.com/products#product-launch-stages)]: Users with access to Looker [System Activity](https://docs.cloud.google.com/looker/docs/system-activity-dashboards#conversational-analytics) content can monitor users' query data and feedback if [users have consented to sharing their query data](https://docs.cloud.google.com/looker/docs/user-account#conversational-analytics) and if a Looker admin has enabled the [**End User Conversational Analytics (CA) Query Review**](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#ca-user-feedback) preview feature. The **Conversational Analytics** dashboard is available in the **System Activity** section of the **Admin** panel.
  * **Triggered agentic workflows** [[Preview](https://cloud.google.com/products#product-launch-stages)]: Set up metric-based alerts and monitoring directly through natural language queries in direct chats with an Explore or with Explore data agents. Agentic workflows are available when the **Enable Trusted Tester Features** and **Agentic Workflows** settings are enabled on the **Gemini in Looker** page in the **Admin** panel, along with whichever Conversational Analytics setting corresponds to the content you are using (**Conversational Analytics (Conversations page)** for Explores or **Dashboard agents** for dashboards).
  * **Scheduled agentic workflows** [Preview](https://cloud.google.com/products#product-launch-stages): Set up recurring agentic workflows to monitor your data and send recurring reports. Scheduled agentic workflows are available when the **Agentic Workflows** setting is enabled on the **Gemini in Looker** page in the **Admin** panel, along with whichever Conversational Analytics setting corresponds to the content you are using (**Conversational Analytics (Conversations page)** for Explores or **Dashboard agents** for dashboards).



See the List of documentation section of this page for links to more detailed information about each feature.

**Tip:** In addition to the Conversational Analytics interface in Looker, you can accomplish many of the same tasks with the [Conversational Analytics API](https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/overview).

## List of documentation

  * [Set up Conversational Analytics in Looker](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-setup): Enable Conversational Analytics for a Looker instance and grant access to users.
  * [Recommended setup and rollout strategy for Conversational Analytics in Looker](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-rollout): Plan the rollout of Conversational Analytics to users of a Looker instance.
  * [Query an Explore in natural language](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data): Start a "conversation" to query the data on a single Looker Explore in natural language.
  * [Create and manage Explore data agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents): Create, edit, delete, share, and publish data agents that query Looker Explores.
  * [Query a user-defined dashboard with a dashboard agent](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-dashboards): Converse with an AI-powered data agent that can query user-defined dashboards and their underlying models.
  * [Create and manage data agents for LookML dashboards](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-lookml-dashboards): Use LookML to configure and manage version-controlled data agents for LookML dashboards.
  * [Best practices for configuring Conversational Analytics in Looker](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-best-practices): Explore strategies and best practices to help Looker administrators and LookML developers successfully configure and optimize Conversational Analytics.
  * [Enable and use Advanced Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-advanced-analytics): Enable and use Advanced Analytics, which translates your natural language questions into Python code and executes that code.
  * [Embedding Conversational Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-embedding): Embed Conversational Analytics in an HTML iframe.
  * [Use triggered agentic workflows to monitor data thresholds](https://docs.cloud.google.com/looker/docs/conversational-analytics-triggered-agentic-workflows) [[Preview](https://cloud.google.com/products#product-launch-stages)]: Set up workflows to notify you when data thresholds that you specify are met or exceeded. Monitor your workflows from the [**Manage Workflows** user page](https://docs.cloud.google.com/looker/docs/user-workflows). Looker admins can manage workflows from the entire instance from the [**Manage Workflows** admin page](https://docs.cloud.google.com/looker/docs/admin-panel-alert-schedules-workflows).
  * [System Activity: Conversational Analytics](https://docs.cloud.google.com/looker/docs/system-activity-dashboards#conversational-analytics) [[Preview](https://cloud.google.com/products#product-launch-stages)]: Learn more about how to monitor Conversational Analytics user engagement and token usage across the Looker instance.



## Data agents versus Conversations

Chatting with a **data agent** offers several key advantages over having a standard conversation with a single **Explore**. While starting a conversation from an Explore allows for quick natural language querying of that specific data source, a data agent functions as a specialized standalone analyst that can be customized and shared across your organization.

Data agents provide the following advantage over conversations with Explores:

  * **Chat with multiple Explores** : In a conversation with an Explore, you're limited to querying one Explore at a time. However, a data agent can connect to as many as _five distinct Explores_ , enabling users to perform cross-domain analysis and receive more comprehensive answers.
  * **Chat with a Looker dashboard** : When you chat with a dashboard, Conversational Analytics creates a dashboard data agent that you can use to query not only a dashboard but the dashboard's underlying Explores.
  * **Authored context** : You can provide your data agent with _custom instructions_ that are not available in a standard Explore conversation, including the following resources: 
    * **Business glossaries** : You can define organization-specific jargon or acronyms directly within the agent's instructions.
    * **Persona framework** : You can assign a specific role or expertise to the agent, setting a consistent tone and professional judgment for the conversation.
  * **Agent specialization** : Rather than using the single generic interface of a conversation, you can create specialized agents for different business units, such as a **Revenue Agent** or an **Ops Agent**. This allows for a more guided analysis experience, leading users toward the specific fields and filters most relevant to their needs.
  * **Collaboration and reuse** : Explore conversations are typically limited to one user, while data agents can be _shared_ with other members of your organization. Sharing ensures that multiple users can benefit from the same authored context and governance that was developed by an administrator or data expert.
  * **Custom behavior** : You can configure your agent to operate within strict requirements, such as using _default filters_ — for example, "always default to the last 6 months if no timeframe is mentioned." These guardrails ensure that the agent operates within your organization's specific governance and security standards. You can also hide fields in Explores to prevent the data agent from using them in queries.



The following table summarizes the key differences in these types of conversations and data agents:

Conversational Analytics feature | Key use cases | Entry point | Sharing capabilities | Limitations  
---|---|---|---|---  
**Explore conversations** | 

  * Standard natural language querying of a single Looker Explore.
  * Organizing related questions about a specific dataset into discrete sessions.
  * Utilizes **Fast** and **Thinking** question modes.

| 

  * From the Explore: Select **Start a conversation**.
  * From the Conversational Analytics page: Select the **Conversations** tab.

| Typically limited to one user (not shareable). | 

  * Limited to querying only one Explore at a time.
  * No custom authored context or instructions (for example, verified queries, personas, business glossaries).
  * No agent specialization for different business units of an organization.
  * The **Start a conversation** option isn't available when using the new Explore experience.

  
**Explore data agents** | 

  * Specialized, standalone data analytics agents that are designed for specific business units of an organization (for example, Revenue Agent, Ops Agent).
  * Cross-domain analysis that uses up to five connected Explores.
  * Authored context that includes custom instructions, verified queries, business glossaries, and persona frameworks to enforce guardrails and improve accuracy.
  * Advanced analytics that use Python code execution, if enabled.
  * Doesn't require explicit `explore` permissions.

| From the Conversational Analytics page: Select the **Agents** tab. | Can be shared with other users in the organization by granting content access (**View** or **Manager access; Edit**). Can also be published to external applications like Gemini Enterprise (Preview). | 

  * Requires `access_data` and other permissions on the models underlying the Explores (sharing the agent doesn't grant access to the Explores).
  * Doesn't support verified queries that contain pivots or custom fields.

  
**Dashboard agents** | 

  * Direct natural language querying of a specific Looker dashboard and its [query-linked tiles](https://docs.cloud.google.com/looker/docs/viewing-dashboards).
  * Curating and customizing agent behavior on dashboards with custom instructions.
  * Access is managed strictly through dashboard-level permissions (**Manage access; Edit** on the dashboard) and model permissions.
  * Can be enabled or disabled at the individual dashboard level for user-defined dashboards.

| From the dashboard: Select **Chat with this dashboard**. | Inherits the dashboard's sharing model. | 

  * Cannot be shared independently of the dashboard.
  * Don't appear on the Conversational Analytics page. Conversations with a dashboard agent are accessible only from the **Recent conversations** page, which is available from the dashboard menu.
  * Limited to the context of the dashboard and its query-linked tiles.
  * Customizing dashboard agent behavior with custom instructions isn't supported for LookML dashboards.
  * The **Advanced Analytics** feature isn't supported.

  
  
## How does Conversational Analytics work?

Conversational analytics uses Gemini for Google Cloud to interpret natural language questions and provide answers in Looker based on your data. It uses the Looker semantic model — the LookML definitions of your data — as its source of truth to ensure that responses are accurate and consistent. Conversational Analytics can interpret your business definitions for metrics like "revenue" or "churn" because they are defined in LookML, using these definitions to deliver accurate and consistent questions.

To ground its responses in your specific data and business context, Conversational Analytics uses several techniques:

  * **LookML schema** : At the beginning of a request, Conversational Analytics fetches the schema from the [Explores](https://docs.cloud.google.com/looker/docs/exploring-data) that are connected to it. Conversational analytics uses parameters from the LookML model in several ways: 
    * **Field identification** : Metadata from the schema helps Conversational Analytics focus on relevant fields. This metadata includes LookML parameters such as `name`, `label`, `description`, `type`, and `dimension_group`. These parameters help Conversational Analytics to map terms in user questions to the correct fields. For example, `description` can provide business-specific terminology or context for a field. Conversational Analytics ignores any fields that use the [`hidden` parameter](https://docs.cloud.google.com/looker/docs/reference/param-field-hidden).
    * **Response formatting** : Conversational analytics uses `label` parameters for user-friendly field naming and `value_format` parameters for formatting data in responses.
  * **Query generation** : Instead of querying your database directly, Conversational Analytics determines which fields, filters, sorts, and limits should be used in the query. Looker then composes and executes the query by using the underlying LookML model. This process is similar to how a user interacts with an Explore interface; Conversational Analytics doesn't need to understand complex join logic or field definitions because Looker handles query composition based on the LookML model. Query generation ensures that all queries adhere to the join logic, filtering, aggregation, and [data permissions](https://docs.cloud.google.com/looker/docs/access-control-and-permission-management) that are defined in your LookML model. To generate queries, Conversational Analytics must determine the correct values to use in filters. These values must be exact matches of values in the underlying data or more advanced filter expressions such as wildcards. To resolve discrepancies between what values the user includes in their natural language questions and the exact values that may be required by a filter, Conversational Analytics uses values that are defined with `allowed_value` in [`parameter`](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter) fields and can use tools to check for specific values in fields: 
    * **Sample data** : Returns up to 100 values from a field to help Conversational Analytics learn patterns or find an exact match for filter values.
    * **Fuzzy search** : Generates a set of search terms based on user input and checks for their presence in a dimension to find appropriate filter values. Both sample data and fuzzy search use Looker's suggestion API and are therefore influenced by LookML parameters such as [`suggestions`](https://docs.cloud.google.com/looker/docs/reference/param-field-suggestions), `suggest_explore`, and `suggest_dimension`.
  * **Analysis** : After Looker runs the queries, Conversational Analytics analyzes query results to answer user questions. Conversational analytics can analyze results in one or more of the following ways: 
    * It uses built-in Gemini capabilities to interpret and summarize results.
    * It uses Python code execution through [Advanced Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-advanced-analytics) to perform further analysis on the results.
    * It creates visualizations based on query results.



By leveraging the Looker semantic model, Conversational Analytics provides access to data from various platforms — such as BigQuery, AlloyDB, Redshift, Snowflake, and Databricks — without needing to understand the underlying data complexity, and it ensures that all responses are consistent and governed.

### How do Conversational Analytics data agents work?

**Note:** Conversational Analytics data agents use [Production Mode](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#production_mode) when they query dashboards or their query-linked tiles.

A Conversational Analytics data agent bases its responses on two primary inputs: your instance's LookML schema, which is defined by a Looker developer, and agent instructions, which you write when you create or edit the agent.

From your query, a data agent must determine which LookML fields to select and which filters, sorts, or limits to apply. To do this accurately, it maps the natural language in your query to its own agent instructions and the data's LookML schema in the following ways:

  1. **Mapping semantic terms** : Users often use business jargon in their questions. The agent uses your agent instructions and the LookML field metadata to interpret your query. For example, for the query "How much new business did we do?" a data agent would be able to map "new business" to a measure that calculates monthly recurring revenue. For the query "Who are our top customers?" a data agent would be able to map "top" to a usage count and "customers" to a dimension called **Customer Name**.
  2. **Mapping field values** : The agent looks for specific data points — for example, "California" or "Slim-fit Jeans" — using specialized tools to sample the data or perform fuzzy searches. For example, if a user asks for "jeans," the agent might trigger a fuzzy search across the **Product Name** field to find the exact string matches in your database. If a user asks for "NY," is that the **City** field or a **State** field? The agent may need to sample the data to see which field contains "NY" or ask a clarifying question.
  3. **Query examples** : You can provide specific question-and-answer examples, called verified queries and also known as _golden queries_ , in data agent context to improve accuracy for common or critical queries.



Looker then uses the LookML definitions of these fields and other logic that's defined in the Explore — including field definitions, [access grants](https://docs.cloud.google.com/looker/docs/reference/param-model-access-grant) or [user attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes), [user-defined dashboard filters](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards), or complex [Liquid](https://docs.cloud.google.com/looker/docs/reference/liquid-variable-reference) or join logic — to compose the query that's sent to the database. Since the agent isn't writing the whole SQL query, it doesn't need to "understand" the data and can operate more accurately and deterministically.

To learn more about how your agent uses LookML, see the [Best practices for configuring Conversational Analytics in Looker](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-best-practices#lookml-best-practices-for-conversational-analytics) documentation page.

## Known limitations

Conversational Analytics dashboard agents have the following known limitations:

  * [**Advanced Analytics**](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-advanced-analytics#suggested-questions) isn't supported for dashboard agents.
  * Dashboard agents inherit the dashboard's sharing model; access to the agent is governed by access to the underlying dashboard.
  * You cannot modify the context or instructions for LookML dashboard agents.



### Limitations on visualizations

Conversational Analytics leverages [Vega-lite](https://vega.github.io/vega-lite) for conversation chart generation. The following Vega chart types are fully supported:

  * Line chart (one or more series)
  * Area chart
  * Bar chart (horizontal, vertical, stacked)
  * Scatter plot (one or more groups)
  * Pie chart



The following Vega chart types are supported, but you may encounter unexpected behavior when rendering them:

  * Maps
  * Heatmaps
  * Charts with tooltips



Chart types that exist outside the Vega catalog are not supported. Any charts that are not specified in this section are considered unsupported.

### Limitations on data sources

Conversational Analytics has the following data source limitations:

  * Conversational Analytics can return a maximum of 50,000 rows per query.
  * Conversational Analytics cannot set the value of a filter-only field that is defined using the LookML [`parameter`](https://docs.cloud.google.com/looker/docs/reference/param-field-parameter) or [`filter`](https://docs.cloud.google.com/looker/docs/reference/param-field-filter) parameters.



### Limitations on questions

Conversational Analytics supports questions that can be answered by a single visualization, for example:

  * Metric trends over time
  * Breakdown or distribution of a metric by dimension
  * Unique values for one or more dimensions
  * Single metric values
  * The top dimension values by metric



Conversational Analytics doesn't yet support questions that can only be answered with the following types of complicated visualizations:

  * Prediction and forecasting
  * Advanced statistical analysis, including correlation and anomaly detection



## Understand the compliance capabilities of Gemini in Looker features

Conversational analytics is not yet included in [FedRAMP High or FedRAMP Medium](https://docs.cloud.google.com/assured-workloads/docs/control-packages#regulatory-data-boundaries) authorization boundaries. Before you enable the **Gemini in Looker** setting for your Looker instance, discuss with your authorizing body whether Gemini for Google Cloud's compliance offerings meet the needs of your organization.

For Looker (Google Cloud core) instances, each [Assured Workloads control package](https://docs.cloud.google.com/assured-workloads/docs/control-packages) that becomes available will add Gemini in Looker features to the default offerings as that package's change requirements and processes are met. Conversational analytics in Looker respects the compliance capabilities of the associated Looker (Google Cloud core) instance, with the following exception:

Data Residency (DRZ) support, specifically for data-at-rest, is available to all Looker customers. All data-at-rest that is associated with Conversational Analytics resides strictly within the Looker instance and is confined to a single region. Data in transit and machine learning (ML) are processed using a global service.

### Compliance in the European Union

Localized processing is available for European Union (EU)-based customers with Looker (original) or Looker (Google Cloud core) instances that are running Looker 26.10 or later. This option enables data processing within the EU jurisdiction and allows Looker's Conversational Analytics traffic to be routed through an EU multi-regional endpoint, which ensures EU customer data is processed within the EU.

Localized processing applies to all Conversational Analytics in Looker features and all Looker API Conversational Analytics endpoints. It doesn't apply to the Conversational Analytics API.

**Note:** The European Union multi-region endpoint covers data residency strictly within EU member states. Geographies outside the European Union political boundary, including the `europe-west2` (London, UK) and `europe-west6` (Zurich, Switzerland) regions, are excluded from this endpoint. Localized ML processing is also not supported for the `europe-west12` (Turin, Italy) region; this region continues to point to global endpoints.

## Provide feedback

You can provide feedback to Google about individual responses in Conversational Analytics by selecting one of the following options:

  * thumb_up **Good response** : Indicate that the response was helpful.
  * thumb_down **Bad response** : Indicate that the response was not helpful.



## Related resources

  * [Learn more about the Conversational Analytics API](https://docs.cloud.google.com/gemini/docs/conversational-analytics-api/overview).
  * Review Gemini in Looker feature [pricing](https://cloud.google.com/looker/pricing) information.
  * [Learn more about Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview).
  * [Learn more about Gemini in Looker](https://docs.cloud.google.com/looker/docs/gemini-overview-looker).
  * [LookML basics](https://docs.cloud.google.com/looker/docs/lookml-overview): Understand the Looker semantic layer that Conversational Analytics is built on.
  * [Exploring data in Looker](https://docs.cloud.google.com/looker/docs/exploring-data): Learn about the Explore interface for querying data, which Conversational Analytics complements.
  * [Access control and permission management](https://docs.cloud.google.com/looker/docs/access-control-and-permission-management): Understand how Looker manages user permissions and data access, which Conversational Analytics respects.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
