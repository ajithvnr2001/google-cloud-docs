---
url: https://docs.cloud.google.com/looker/docs/system-activity-dashboards/
title: Admin settings - System Activity dashboards \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:40.889009+00:00
---

# Admin settings - System Activity dashboards  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/system-activity-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - System Activity dashboards Stay organized with collections  Save and categorize content based on your preferences. 

The **System Activity** section of the **Admin** menu displays built-in dashboards that show usage and performance information about your Looker instance. You can [download](https://docs.cloud.google.com/looker/docs/viewing-legacy-dashboards#downloading_your_dashboard), [schedule](https://docs.cloud.google.com/looker/docs/viewing-legacy-dashboards#scheduling_dashboard_data_delivery), [set alerts on](https://docs.cloud.google.com/looker/docs/alerts-overview), and [drill into](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores#drilling_down_into_the_data) metrics and elements just like on any other dashboard. Data in the System Activity dashboards is updated and cached every 12 hours.

> Before enabling System Activity on a customer-hosted Looker deployment with [MySQL backend](https://docs.cloud.google.com/looker/docs/migrating-looker-backend-db-to-mysql), verify that you have properly set up the user for the backend database. Specifically, you must perform the step to `grant all on looker_tmp.* to '<DB_username>'@'%';` before enabling the System Activity feature. See the procedure on the [Migrating the Looker backend database to MySQL](https://docs.cloud.google.com/looker/docs/migrating-looker-backend-db-to-mysql#mysql_create_db) documentation page.
> 
> Because the [permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#schedule_look_emails) to [deliver](https://docs.cloud.google.com/looker/docs/scheduling) content to email destinations is model specific, to send or schedule System Activity dashboards to email destinations, users must have **All** models selected in the **Model Set** specified for their role.

The System Activity dashboards connect to the underlying application database of your Looker instance. They show information about your instance, including Looks and dashboards, user information, historical query information, and performance statistics. Both the granularity and retention of System Activity data are subject to system constraints. System Activity is designed for collecting high-volume data, and aggregating it can be used to supplement your business logs.

> This data can be useful for supplementing monitoring and auditing activities, but is not intended to replace your current compliance strategy.

By default, System Activity data is stored in the internal database of your Looker instance. In this configuration, Looker stores a maximum of 90 days of historical query and event data.

> The text in filters run by users is accessible in System Activity and can be viewed by any user who has permission to view the System Activity model.
> 
> **Take action** : Modify who has view access to the System Activity model. Admins have access to this model by default. Non-admin users can be granted access to the System Activity model if they are given the `see_system_activity` permission.
> 
> System Activity dashboards and Explores are restricted in the number of concurrent queries that can be run. This restriction may increase loading times for System Activity dashboards.
> 
> **Chat Team Tip** : Time-based data in System Activity is stored using the **System time zone**. See the [Using time zone settings](https://docs.cloud.google.com/looker/docs/using-time-zone-settings#system_time_zone) documentation page for more information.

## System Activity dashboards

**Note:** If your Looker admin has [enabled the Looker reports feature](https://docs.cloud.google.com/looker/docs/enabling-looker-reports), System Activity also shows information about reports on your instance. For more information, see [Monitoring Looker reports with System Activity](https://docs.cloud.google.com/looker/docs/system-activity-for-looker-reports).

These are the System Activity dashboards:

  * User Activity
  * Content Activity
  * Database Performance
  * Instance Performance
  * Performance Recommendations
  * Errors and Broken Content
  * Dashboard Diagnostics
  * Conversational Analytics
  * Query History



## User Activity dashboard

The **User Activity** dashboard shows information about your users and their usage of your Looker instance.

![](https://docs.cloud.google.com/static/looker/docs/images/sa-user-activity-2414.png)

The **User Activity** dashboard includes tiles that show the following information:

  * The total number of users on your Looker instance.
  * The number of users of each type on your Looker instance, including:

    * [Developer, Standard, and Viewer users](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permissions_and_looker_licenses).
    * [Embedded Standard and Viewer users](https://docs.cloud.google.com/looker/docs/signed-embedding).
    * [Disabled users](https://docs.cloud.google.com/looker/docs/admin-panel-users-users#disabling_users).
    * [Googlers who work on Looker](https://docs.cloud.google.com/looker/docs/admin-panel-general-support-access#Granting).
  * The total number of users on your Looker instance over time.

  * The percentage of users who have issued at least one query on your Looker instance in the last 7 days.

  * A snapshot of user login activity over the past 90 days.

  * The average minutes of activity and average number of queries per user each week for the previous 6 weeks.

  * The number of users who have issued at least one query in the previous 7 days, grouped by query source.

  * A list of users who have spent the most time using your Looker instance in the previous 7 days.

  * A list of users who have created the most new dashboards on your Looker instance in the previous 7 days.

  * A list of users who have triggered the most Git events from your Looker instance over all time.

  * A list of users who have not logged in to your Looker instance in the last 90 days.

  * A text tile with links to Looker education and training resources.

  * A list of the most recent login failures, with the following information for each failure:

    * The time of the login attempt.
    * The user ID.
    * The authentication method that was used.
    * Any error messages that were returned.



## Content Activity dashboard

The **Content Activity** dashboard shows information about which dashboards, Looks, and Explores are being viewed and scheduled on your Looker instance.

![](https://docs.cloud.google.com/static/looker/docs/images/sa-content-activity-2102.png)

The **Content Activity** dashboard includes tiles that show the following data:

  * The number of dashboards that have not been deleted.
  * The number of Looks that have not been deleted.
  * The number of scheduled plans.
  * The percentage of dashboards that were queried in the previous 30 days.
  * The percentage of Looks that were queried in the previous 30 days.
  * The number of scheduled jobs for each day in the previous 7 days.
  * The number of Explore queries that were issued in the previous 30 days.
  * A list of all dashboards and Looks that have been accessed in the last 30 days, sortable by the number of views in the Looker UI, number of times viewed in an embed, number of times viewed through the API, number of times the content was made a favorite, and number of times the content was delivered through a scheduled job.
  * A list of Explores created in the previous 30 days, showing the number of times the Explore was run and the number of users running the Explore.
  * A list of dashboards and Looks that have not been accessed in the last 30 days, showing the content's number of views in the last 90 days in the Looker UI, in an embed, and through the API; and in the last 90 days the number of times the content was made a favorite, and the number of times the content was delivered through a scheduled job.
  * A list of Explores created in the previous 90 days that have not been queried in the previous 30 days, showing the length of time since the Explore was last run, the number of times the Explore was run in the previous 90 days, the date the Explore was last run, and the date the Explore was first run.



## Database Performance dashboard

The **Database Performance** dashboard shows information about the performance of content and PDTs on your Looker instance. You can filter the entire dashboard by **Connection Name**. The dashboard includes insights into query runtimes, concurrency, and PDT builds, and lists the number of query errors and PDT build failures.

![](https://docs.cloud.google.com/static/looker/docs/images/sa-database-performance-2514.png)

The **Database Performance** dashboard includes tiles that show the following data:

  * **Query Latency** : A breakdown of the average time that it takes for a query to be executed on the database. This helps distinguish between latency caused by Looker and latency caused by the database itself. If you observe that "Average Time Spent Running Queries" or "Average Time Spent Initializing and Connecting" are consistently high, it may suggest that your database is under-provisioned and that upsizing its resources could lead to significant improvements.
  * **Query Concurrency** : A view of the average number of simultaneous queries, categorized by source. For an effective analysis, you can filter by a single connection and unhide the **Max Connections** series to compare your query load against the connection's limit. If concurrency is consistently high, you can adjust the [**Max Connections**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max_concurrent_queries_for_this_connection) setting on the Connections admin page to prevent overloading your database.
  * The percentage of queries that were returned from the cache.
  * All queries that were run over the previous 30 days, grouped by query source, with query runtimes aggregated into tiers, and with each runtime tier shown as a percentage of all queries.
  * A table of the top 15 users that shows the number of queries that were run for the previous 7 days.
  * A table of the top 10 query sources that shows the number of queries that were run for the previous 7 days.
  * The number of queries that were run, the number of active users, and the percentage of queries that were returned from the cache for each hour of the day.
  * The number of scheduled jobs and scheduled plans for each hour of the day.
  * The number of PDT builds for each connection for each hour of the day.
  * The average runtime for each Explore over the previous 7 days, sorted by the longest runtime.
  * The average runtime for each Look over the previous 7 days, sorted by the longest runtime.
  * The average runtime for each dashboard over the previous 7 days, sorted by the longest runtime.
  * A list of all PDTs that were built in the previous 7 days, showing the number of trigger failures, create failures, and successful builds.
  * The average build time for each PDT in the previous 7 days, sorted by the longest average build time.



## Instance Performance dashboard

The **Instance Performance** dashboard shows information about the load and performance of the Scheduler and performance-intensive content.

![](https://docs.cloud.google.com/static/looker/docs/images/sa-instance-performance-2514.png)

The **Instance Performance** dashboard includes tiles that show the following data:

  * **Dashboard Review** : The **Taxing Dashboards** tile helps identify dashboards that may be straining your instance. You can sort the table to see which dashboards have the lowest refresh intervals, highest number of tiles, or a high count of merge queries. For more details on these settings, you can navigate to the [**Content Guardrails**](https://docs.cloud.google.com/looker/docs/admin-panel-performance-center-content-guardrails) page to proactively manage content and improve instance performance.
  * A heatmap that shows the number of scheduled jobs and their average time in the queue for each hour of each day of the week, showing you which hours or days have the heaviest impact on the Scheduler.
  * The number of queries and query average runtime for days where the average runtime exceeds 1.5 times the standard deviation for all days, showing you which days have exceptionally heavy impact on the Scheduler.
  * The number of scheduled jobs for each Explore.
  * The most frequently scheduled content for the previous 14 days, showing the number of times that each content item was scheduled each day.
  * A list of queries that were downloaded or scheduled with the [All Results](https://docs.cloud.google.com/looker/docs/downloading#all_results) option.
  * **Optimization Resources** : A set of buttons that link to Best Practices pages and documentation about optimizing your instance.



## Performance Recommendations dashboard

The **Performance Recommendations** dashboard surfaces opportunities to improve performance on your Looker instance.

![](https://docs.cloud.google.com/static/looker/docs/images/sa-performance-recommendations-2206.png)

The **Performance Recommendations** dashboard includes tiles that show the following information:

  * **Dashboard Recommendations**: A list of possibly non-performant dashboards and recommendations to improve performance.
  * **Explore Recommendations**: A list of possibly non-performant Explores and recommendations to improve performance.



The following sections explain the tiles in more detail.

### Dashboard Recommendations

The **Dashboard Recommendations** tile surfaces dashboards that may cause performance strains on either your Looker instance or your database. The tile provides recommendations from the [Considerations when building performant Looker dashboards](https://docs.cloud.google.com/looker/docs/best-practices/considerations-when-building-performant-dashboards) Best Practices page. You can apply these recommendations at the dashboard level to help improve performance. The following are possible warnings that you may see:

Warning | Recommendation  
---|---  
`The number of queries generated by this dashboard is <X>, which is higher than recommended (<25).` | Reduce the number of query tiles or create a second dashboard.  
`The number of merge queries generated by this dashboard is <X>, which is higher than recommended (<=4).` | Reduce the number of merge result tiles.  
`The auto-refresh interval of this dashboard is <X>, which is lower than recommended (>=15 min).` | Increase or disable the auto-refresh interval setting to avoid overloading the database.  
  
### Explore Recommendations

The **Explore Recommendations** tile surfaces Explores that may cause performance strains on either your Looker instance or your database.

The tile compares average values of each Explore's [query performance metrics](https://docs.cloud.google.com/looker/docs/query-performance-metrics) against benchmarks for healthy instance performance. The severity listed next to each Explore indicates how far the Explore's metrics exceed these benchmarks.

Based on which metrics exceed the benchmarks, the tile provides targeted troubleshooting strategies to help improve performance. The following are warnings and recommendations that you may see.

Query Step | Warning | Recommendations  
---|---|---  
`Model Init: Computed` | `The average model init: computed time is <X>, which is above the recommended benchmark.` | Remove unnecessary views from the [`include` parameter](https://docs.cloud.google.com/looker/docs/reference/param-model-include) of the LookML model. Ensure that LookML production code is changed infrequently, ideally at times when users aren't running many queries.  
`Explore Init: From Cache` | `The average explore init: from cache (marshalled cache load) time is <X>, which is above the recommended benchmark.` | Move [custom fields](https://docs.cloud.google.com/looker/docs/custom-fields) and [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) into LookML wherever possible.  
`Explore Init: Computed` | `The average explore init: computed time is <X>, which is above the recommended benchmark.` | Remove unnecessary [joins](https://docs.cloud.google.com/looker/docs/reference/param-explore-join) from the LookML `explore` file. Use the [`fields` LookML parameter](https://docs.cloud.google.com/looker/docs/reference/param-explore-fields) to exclude unnecessary fields from the Explore. Ensure that LookML production code is changed infrequently, ideally at times when users aren't running many queries.  
`Prepare` | `The average prepare time is <X>, which is above the recommended benchmark.` | Enable the [New LookML Runtime](https://docs.cloud.google.com/looker/docs/reference/param-manifest-new-lookml-runtime) feature to decrease preparation time. Move [custom fields](https://docs.cloud.google.com/looker/docs/custom-fields) and [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) into LookML wherever possible.  
`Acquire Connection` | `The average connection acquisition time is <X>, which is above the recommended benchmark.` | Configure the [max connection limit](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max_connections) in the connection settings panel. Set a limit no less than the max number of queries needed to run concurrently at peak traffic.  
`Execute Main Query` | `The average main query execution time is <X>, which is above the recommended benchmark.` | Avoid complex SQL logic such as window functions, CTEs, join conditions on date fields, or large join chains. Put complex SQL logic into [persistent derived tables (PDTs)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_tables_pdts) to reduce query times. Use [aggregate awareness](https://docs.cloud.google.com/looker/docs/aggregate_awareness) when possible.  
`Postprocessing` | `The average postprocessing time is <X>, which is above the recommended benchmark.` | Simplify [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) and move them to LookML when possible. Remove complex pivots, sorts, or value formatting.  
`Stream to Cache` | `The average stream to cache time is <X>, which is above the recommended benchmark.` | Simplify [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) and move them to LookML when possible. Remove complex pivots, sorts, or value formatting.  
  
## Errors and Broken Content dashboard

The **Errors and Broken Content** dashboard shows the dashboards, Looks, schedules, and PDTs that produce query errors, along with the number of errors for each query source.

This dashboard displays only errors that occur at query runtime. For example, if you remove a LookML field from a view, any Looks and dashboards that use that field will display warnings, but the **Errors and Broken Content** dashboard will not display these warnings. Use the [Content Validator](https://docs.cloud.google.com/looker/docs/content-validation) to check for LookML reference issues in your Looks and dashboards.

![](https://docs.cloud.google.com/static/looker/docs/images/sa-errors-and-broken-content-2102.png)

The **Errors and Broken Content** dashboard includes tiles that show the following data:

  * A list of dashboards that are producing errors, including the errors given, the issuer of each dashboard query, and the number of users who have run queries using each dashboard.
  * A list of scheduled jobs that are producing errors, including the errors given and the creator of each schedule.
  * A list of scheduled jobs that have warnings for partial data delivery. For each job, the list includes the name of the dashboard, status details that explain why the delivery was incomplete, the schedule creator and schedule creation date, and links to the content and folder.
  * A list of Looks that are producing errors, including the errors given and the issuer of each Look query.
  * A list of PDTs that are producing errors, including the PDT actions that created the error log entry, any data related to the PDT action, number of times the PDT produced a "create cancelled error" action, and the number of times the PDT produced a "trigger value error".
  * The number of errors from each query source for the previous 10 days.



## Dashboard Diagnostics

The **Dashboard Diagnostics** dashboard surfaces opportunities to improve performance on an individual dashboard.

You can access the **Dashboard Diagnostics** dashboard from any dashboard by clicking the **Dashboard actions** [three-dot menu](https://docs.cloud.google.com/looker/docs/viewing-dashboards#three-dot_dashboard_menu) and selecting **Dashboard Performance Summary**.

![](https://docs.cloud.google.com/static/looker/docs/images/sa-dashboard-performance-2514.png)

Some tiles, such as **Query Runtime by Hour** and **Query Runtime by Tile** , break down the query runtime by query stage. The query stages are as follows:

  * **In Queue:** This is the amount of time, in seconds, that the query spent in the Looker queue. Looker queues queries when the connection's [Max connections per node](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max_connections_per_node) limit has been reached, or when the [per-user limit](https://docs.cloud.google.com/looker/docs/startup-options) (which has a default value of 15 concurrent queries) has been reached.
  * **Query Initialization:** This is the amount of time, in seconds, that Looker spent building the query from the source LookML, and connecting to the database. If this stage is taking a long time, this may indicate that LookML model complexity or database connectivity is impacting the query runtime.
  * **Running Query:** This is the amount of time, in seconds, that Looker spent waiting for query results while the query runs on the database. This includes the main query and any needed additional queries including calculating totals and building PDTs. This is the most common cause of long dashboard runtime, and can be improved by [optimizing query performance](https://docs.cloud.google.com/looker/docs/best-practices/how-to-optimize-looker-server-performance#optimize-query-performance).
  * **Processing Results:** This is the time, in seconds, that Looker spent formatting the results, calculating table calculations, and caching the result set.



The **Dashboard Diagnostics** dashboard includes tiles that show the following information:

  * The title of the dashboard.
  * The numbers of users who have run this dashboard in the selected timeframe.
  * The number of times this dashboard has been run in the selected timeframe.
  * The percentage of queries from this dashboard that were run from cache. 
    * If the cache percentage is low, use [caching strategies](https://docs.cloud.google.com/looker/docs/caching-and-datagroups) to reduce database load.
  * The average query time per tile.
  * The users who have most frequently run this dashboard.
  * The average query time per hour. 
    * If there are spikes in this tile, ensure there are not several [scheduled plans](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-schedule) being sent at the same time.
  * The number of tiles with at least one merged results query.
  * The number of merged results queries in the dashboard.
  * **Dashboard Recommendations**: A list of possible performance issues and recommendations to improve performance for this dashboard.



## Conversational Analytics

The **Conversational Analytics** dashboard surfaces usage and telemetry data for [Conversational Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview) features in Looker. This dashboard refreshes every 24 hours.

The **Conversational Analytics** dashboard is organized into these tabs:

  * **Engagement**
  * **Token usage**



If the **End User Conversational Analytics (CA) Query Review** [preview feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#ca-user-feedback) is enabled, the **Conversational Analytics** dashboard displays additional information about the users' Conversational Analytics queries. The **Conversational Analytics** dashboard is organized into these tabs:

  * **Engagement**
  * **Token usage**
  * **Responses & feedback**



Feedback information and query responses are collected starting when thisfeature is enabled.

### Conversational Analytics engagement

Conversational Analytics usage data is displayed in the **Engagement** tab.

The section about users and conversations shows the following data:

  * **Total Users** : The number of users who have asked questions using Conversational Analytics.
  * **Active % of Total Users (last 7 days)** : The percentage of active users who have asked questions using Conversational Analytics.
  * **Total Agents** : The number of data agents that have been used in conversations.
  * **Total Conversations** : The number of conversations in which a user asked at least one question.
  * **Users by Type** : A comparison of users by user type, according to their [Looker license type](https://cloud.google.com/terms/looker/legal/customers/licensing).
  * **Conversations by Type** : A comparison of the number of conversations with data agents and with Explores.
  * **Weekly Users** : The number of weekly users.
  * **Weekly Conversations** : The weekly breakdown of the number of conversations with a data agent or with a Looker Explore.
  * **Users Active in Last 7 Days** : The number of active users in the last 7 days.
  * **Weekly Average Queries per User** : The weekly average of queries per user.



The **Top Agents, Explores, and Users** section shows the following data:

  * **Top Explores** : The most heavily used Explores, sorted by Explores with the most users, the most conversations, and the most queries.
  * **Agents Not Used in Last 30 Days** : The IDs for agents that have not been used in the last 30 days.
  * **Top Users** : The most active users, sorted by users with the most conversations and the most queries.



The **Dashboard Agents Deep Dive** section shows the following data:

  * **Total Conversations (Dashboard Agents)** : The number of conversations in which a user asked at least one question of a data agent from a dashboard.
  * **Total Users (Dashboard Agents)** : The number of users who have asked questions of a data agent from a dashboard.
  * **Dashboards with Questions** : The number of dashboards with a data agent that users have asked at least one question.
  * **Dashboard Views vs Questions (Last Week)** : A comparison of a dashboard's views and the number of questions that were asked of the data agents that are associated with that dashboard.
  * **Dashboard Questions Timeline** : A chart of how many questions have been asked of a dashboard's data agent over time.
  * **Top Agents** : The most heavily used data agents, sorted by agents with the most users, the most conversations, and the most queries.



The **Queries** section shows the following data:

  * **Longest Running Queries** : The longest-running queries, sorted by queries that have taken the longest to run.
  * **Queries by Runtime Tier** : Queries broken down by runtime tiers in seconds.



### Conversational Analytics token usage

**Note:** To enable token usage observability for Looker (Google Cloud core) instances, a Looker admin must turn on the [**Conversational Analytics Agent Token usage**](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#ca-agent-token-usage) preview feature.

Conversational Analytics token usage is displayed in the **Token usage** tab. Usage is measured in _data tokens_ , which are basic units of text and data processed by a Large Language Model (LLM). All interactions with Conversational Analytics in Looker are measured in data tokens. This includes the questions that are asked, the context that's provided to the model, and the answers that are sent back. These interactions are broken down into two types: _input data tokens_ and _output data tokens_.

_Input data tokens_ are the data tokens that are sent to the model for processing. Input data tokens may include the following text or data:

  * The question that is typed into the chat.
  * The conversational history of a session.
  * Any relevant data context, like metadata and agent instructions.



_Output data tokens_ are the data tokens that the model generates and sends back as part of a response. Output data tokens may include the following text or data:

  * The natural language response to a question.
  * The API call or SQL query that is generated to retrieve data.
  * Any other text that is generated by the model as part of the response.
  * The visualization that is created by the model.



The **Token usage** tab shows the following data:

  * **Total Estimated Input Tokens** : The total number of input data tokens that are estimated to be used in Conversational Analytics.
  * **Total Estimated Output Tokens** : The total number of output data tokens that are estimated to be used in Conversational Analytics.
  * **Daily Estimated Token Usage** : A visualization showing the estimated daily use of input and output tokens over time.
  * **Daily Token Utilization** : A visualization showing the estimated daily token utilization over time.
  * **Top Agents by Token Usage** : A visualization showing the input tokens that are sent by the agent and the output token responses. The **Conversation Surface** column denotes the type of data agent, and includes these options: 
    * [**Conversational Analytics**](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data): A data agent that queries one or more Looker Explores.
    * [**Conversational Analytics API**](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview): A data agent that was created using the [Looker API's `ConversationalAnalytics` methods](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest).
    * [**Conversational Analytics Embed**](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-embedding): A data agent that queries an embedded Looker Explore.
    * [**Dashboard Agents**](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-dashboards): A data agent that queries a Looker dashboard.
    * [**Dashboard Agents Embed**](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-embedding): A data agent that queries an embedded Looker dashboard.
    * [**Explore Insight Assistant**](https://docs.cloud.google.com/looker/docs/gemini-insight-asst): An Insight Assistant agent.
    * [**Gemini Enterprise**](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents#publish-data-agents): A data agent that was published to Gemini Enterprise. This option appears only for Looker (original) instances.
  * **Top Users by Token Usage** : A table that shows the users with the highest token usage.
  * **Top Conversations by Token Usage** : A table that shows the conversations with the highest token usage.



Admins can use page-level filters on the **Token usage** tab to filter token usage counts by the following attributes:

  * **Created Date**
  * **Agent ID**
  * **Conversation Surface**
  * **User ID**
  * **Conversation ID**

**Notes:**

  * Conversation surfaces and linked conversations appear in the dashboard only after an actual conversation is completed. For example, **Dashboard Agent** appears in the **Conversation Surface** filter list only after a user has completed their first conversation with a dashboard agent.
  * Token usage is tagged with conversation surfaces starting when the tagging feature is enabled in Looker 26.14. There is no retroactive tagging for past usage; token usage from Looker 26.12 or from Looker 26.14 before the feature was enabled won't be tagged with the conversation surface.
  * Token usage data has a sync latency of six hours.



For more information about pricing based on token usage, see the [Looker pricing](https://cloud.google.com/looker/pricing) page.

### Responses & feedback

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** User query feedback for Conversational Analytics is in preview with limited support. We encourage you to share your feedback to help us improve. To report bugs or issues about user query feedback, reach out to [ca-user-queries-feedback@google.com](mailto:ca-user-queries-feedback@google.com). In your email, include the following details: 

  * A clear description of the problem and the expected behavior.
  * Steps to reproduce the issue.
  * Any additional relevant details.



The **Responses & feedback** tab reports information about Conversational Analytics user behavior for users who have [consented to revealing their query data](https://docs.cloud.google.com/looker/docs/user-account#conversational-analytics) to their Looker admins.

The **Responses & feedback** tab shows the following data:

  * **Overall Answer Success** : A chart that shows the percentage of user queries that resulted in a successful response (**Success**), an error (**Error**), or a timeout (**Timeout**). You can drill into a result type to view, download, or explore the queries that returned that result.
  * **Rating Distribution** : A chart that shows the count of each user rating of how well Conversational Analytics responded to their question. User ratings include **Thumbs up** , **Thumbs down** , **Unrated** , and **Removed rating**. You can drill into a rating type to view, download, and explore the queries for which users provided that rating.
  * **User Feedback** : A table that lists the user ratings and optional written comments submitted by users about the quality of the responses they received. It displays the following information:

    * **Question** : The query as written by the user, truncated if necessary. When you drill into the question, the user's conversation opens in a separate panel.
    * **Agent** : A unique identifier for the Conversational Analytics agent.
    * **Dashboard** : For dashboard data agents, the dashboard that contains the data that the agent is querying.
    * **Model** : For Explore data agents, the underlying model of the Explore that the agent is querying.
    * **Explore** : For Explore data agents, the Explore that the agent is querying.
    * **Rating** : The user's rating of the response.
    * **Answer Success** : The answer success result.
    * **Latency** : The end-to-end duration, in seconds, of a single conversation turn from the moment a user submits a query to when the final response is delivered.
    * **User** : The name of the user who is chatting with the agent.
    * **Timestamp** : The YYYY-MM-DD HH:MM:SS timestamp for when user submitted the query.



## Query History

The **Query History** dashboard is available from the [Explore **Performance** panel](https://docs.cloud.google.com/looker/docs/query-tracker#explore_performance_panel), and shows current and historical performance data for both the query and the Explore that was used to create the query.

![](https://docs.cloud.google.com/static/looker/docs/images/sa-dashboard-query-history-2418.png)

The **Query History** dashboard includes tiles that show the following data:

  * The average time it took for the query to run and return results.
  * The total number of times that the query was run.
  * The average time that the query spent in each of the [three query phases](https://docs.cloud.google.com/looker/docs/query-tracker).
  * Detailed metrics about the query.
  * The number of queries that were run from the Explore that was used to create the initial query, broken down in five-second runtime increments.
  * The total number of queries run that are based on the Explore that was used to create the initial query.
  * The average time it took for queries based on the Explore that was used to create the initial query to run and return results.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
