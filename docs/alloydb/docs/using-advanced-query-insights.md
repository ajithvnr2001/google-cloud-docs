---
url: https://docs.cloud.google.com/alloydb/docs/using-advanced-query-insights/
title: Improve query performance using advanced query insights features for AlloyDB \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:47.894412+00:00
---

# Improve query performance using advanced query insights features for AlloyDB  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/using-advanced-query-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Improve query performance using advanced query insights features for AlloyDB Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use advanced query insights features for AlloyDB to detect and analyze query performance problems in near real time for both primary and read pool instances. For an overview of advanced query insights features for AlloyDB, see [Advanced query insights features for AlloyDB overview](https://docs.cloud.google.com/alloydb/docs/advanced-query-insights-overview).

To learn how to use standard query insights, see [Improve query performance by using query insights](https://docs.cloud.google.com/alloydb/docs/using-query-insights).

You can use Gemini Cloud Assist to help you monitor and troubleshoot your AlloyDB resources. For more information, see [Monitor and troubleshoot with Gemini assistance](https://docs.cloud.google.com/alloydb/docs/monitor-troubleshoot-with-gemini).

## Before you begin

To access the query insights dashboard, [enable access to AlloyDB for PostgreSQL in your Google Cloud project](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect).

### Required roles

To use advanced query insights features for AlloyDB, you need permissions to do the following:

  * To access advanced query insights features for AlloyDB, you need permissions to access the AlloyDB query insights dashboard.
  * To edit settings of advanced query insights features for AlloyDB, you need permissions to update AlloyDB instances.



To get these permissions, ask your administrator to grant you one of the following roles:

  * Basic viewer (`roles/viewer`)
  * Database insights viewer (`roles/databaseinsights.viewer`)



For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Enable advanced query insights features for AlloyDB

To enable the advanced query insights configuration for an AlloyDB instance, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. From the list of clusters and instances, click an instance.

  3. Click **Query insights**.

  4. Click either **Enable** or **Edit settings**.

  5. In the **Edit query insights settings** tab, select the **Enable advanced query insights features for AlloyDB** checkbox.

This entails the following configuration changes by default:

     * Turns on the **Wait event analysis** and **Active query analysis** checkboxes.
     * Increases the query length from 4500B to 100000B.
  6. Save your changes. This restarts your AlloyDB for PostgreSQL instance.


**Note:** The increased data storage may incur additional charges.

### gcloud
    
    
    gcloud alpha alloydb instances update INSTANCE \
    --cluster=CLUSTER \
    --project=PROJECT \
    --region=REGION \
    --observability-config-enabled

Replace the following:

  * `INSTANCE`: the ID of the instance to update.
  * `CLUSTER`: the ID of the instance's cluster.
  * `PROJECT`: the ID of the cluster's project.
  * `REGION`: the cluster's region—for example, `us-central1`.



The `--observability-config-enabled` flag enables collecting and analyzing data on an AlloyDB instance to monitor its performance and health. If you want to disable advanced query insights, use `--no-observability-config-enabled`.

### Terraform

**Warning:** To keep your Terraform state consistent, update configurations directly in your Terraform files. If you make manual changes using the Google Cloud console, gcloud CLI, or REST API, the following issues can occur: 

  * API errors
  * Perpetual diffs
  * Overwritten changes during `terraform apply`



To use Terraform to enable advanced query insights on your AlloyDB instance, set the `enabled` field to `true` in the `observability_config` block.

Here's an example:
    
    
      observability_config {
        enabled = true
      ...
      }
      

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://cloud.google.com/docs/terraform/basic-commands).

###  REST v1 

This example enables advanced query insights on your AlloyDB instance. For a complete list of parameters for this call, see [Method: projects.locations.clusters.instances.patch](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/projects.locations.clusters.instances/patch). For information about advanced query insights settings, see [Edit advanced query insights settings](https://docs.cloud.google.com/alloydb/docs/using-advanced-query-insights#edit-advanced-features-settings).

Before you use any of the request data, make the following replacements:

  * `CLUSTER_ID`: the ID of the cluster that you create. It must begin with a lowercase letter and can contain lowercase letters, numbers, and hyphens.
  * `PROJECT_ID`: the ID of the project where you want the cluster placed.
  * `LOCATION_ID`: the ID of the cluster's region.
  * `INSTANCE_ID`: the name of the primary instance that you want to create.



To enable your instance configuration, use the following [`PATCH`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/projects.locations.clusters.instances/patch) request:
    
    
    PATCH https://alloydb.googleapis.com/v1beta/{instance.name=projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID}?updateMask=observabilityConfig.enabled
    

The `updateMask=observabilityConfig.enabled` query parameter tells the API to update the `enabled` field within the `observabilityConfig` block.

The request JSON body looks as follows:
    
    
    {
     "observabilityConfig": {
       "enabled" : true
     }
    }
    

After advanced query insights are enabled, you can edit your advanced query insights settings.

**Note:** The query insights dashboard resets after you enable advanced query insights. However, you can still access the standard query insights metrics using the [Metrics explorer UI](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

## Edit advanced features settings

To edit the advanced query insights configuration for an AlloyDB instance, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. From the list of clusters and instances, click an instance.

  3. Click **Query insights**.

  4. Click **Edit settings** and then modify any of the following settings:

     * **Wait event analysis** Wait event analysis can help you to identify and resolve performance issues in your database. A _wait event_ is a component that causes a delay in processing a query related operation.
     * **Active query analysis** Track actively running queries.
     * **Store query comments** Learn about query context by seeing the comments associated with any query you investigate, as part of query length. No additional memory needed. If your comments contain sensitive information, be mindful of user access.
     * **Enable index advisor** Surface index creation recommendations on a cluster's query insights page.
     * In the **Select run frequency** field, you can define the update frequency for recommendations.
     * **Store client IP addresses** Enable to track client IP addresses and analyze that data.
     * **Store application tags** Enable to learn which APIs and model-view-controller routes are making requests, and group that data to run metrics against it.
     * **Query plan sampling** Query plans visualize the operations used to complete a sample of a query. The sampling rate determines how many query samples can be captured per minute across your databases. Higher rates require more memory.
     * In the **Query lengths** field, you can change the default limit on query lengths, from 256 bytes up to 100 KB. Higher query lengths require more memory. Changing query length requires instance restart.
  5. Save your changes.




### gcloud
    
    
    gcloud alpha alloydb instances update INSTANCE \
    --cluster=CLUSTER \
    --project=PROJECT \
    --region=REGION \
    --observability-config-enabled \
    --observability-config-preserve-comments \
    --observability-config-track-wait-events \
    --observability-config-max-query-string-length=QUERY_LENGTH \
    --observability-config-record-application-tags \
    --observability-config-query-plans-per-minute=QUERY_PLANS \
    --observability-config-track-active-queries \
    --observability-config-track-client-address \
    --observability-config-assistive-experiences-enabled

Replace the following:

  * `INSTANCE`: the ID of the instance to update.
  * `CLUSTER`: the ID of the instance's cluster.
  * `PROJECT`: the ID of the cluster's project.
  * `REGION`: the cluster's region—for example, `us-central1`.
  * `QUERY_LENGTH`: the length of the query that ranges from 1024 to 100000 bytes. The default query length is 10240 bytes. Higher query lengths are more useful for analytical queries, but they also require more memory. Changing the query length requires you to [restart the instance](https://docs.cloud.google.com/alloydb/docs/instance-restart). You can still add tags to queries that exceed the length limit.
  * `QUERY_PLANS`: the number of query plans to configure per minute. By default, a maximum of 20 executed query plan samples are captured per minute across all databases on the instance. Change this value to a number from 1 to 200. To disable sampling, enter 0. Increasing the sampling rate is likely to give you more data points but might negatively affect performance.



Use the following optional observability flags if needed:

  * `--observability-config-enabled`: enables collecting and analyzing data on an AlloyDB instance to monitor its performance and health. If you want to disable advanced query insights, use `--no-observability-config-enabled`.
  * `--observability-config-track-active-queries`: enables [tracking of active queries](https://docs.cloud.google.com/alloydb/docs/monitor-active-queries). If you want to disable the feature, use `--no-observability-config-track-active-queries`.
  * `--observability-config-track-client-address`: enables tracking of client addresses. If you want to disable tracking of client addresses, use `--no-observability-config-track-client-address`.
  * `--observability-config-assistive-experiences-enabled`: enables assistive experiences to collect enhanced telemetry for monitoring and troubleshooting. If you want to disable assistive experiences, use `--no-observability-config-assistive-experiences-enabled`.
  * `--observability-config-record-application-tags`: stores application tags that help you determine the APIs and model-view-controller (MVC) routes that make requests and group data to run metrics against it. This option requires you to comment queries with a specific set of tags. If you don't want to store application tags, use `--no-observability-config-record-application-tags`.
  * `--observability-config-preserve-comments`: keeps comments in query strings recorded by query insights. If you don't want to keep comments, use `--no-observability-config-preserve-comments`.
  * `--observability-config-track-wait-events`: enables tracking of wait events during query execution. If you don't want to track wait events, use `--no-observability-config-track-wait-events`.
  * `--observability-config-query-plans-per-minute=QUERY_PLANS`: the number of query plans to sample per minute. By default, a maximum of 20 executed query plan samples are captured per minute across all databases on the instance. Change this value to a number from 1 to 200. To disable sampling, enter 0. Increasing the sampling rate is likely to give you more data points but might negatively affect performance.
  * `--observability-config-max-query-string-length=QUERY_LENGTH`: the query string length in bytes to store. The default value is 10240 bytes. Any value from 1024 to 100000 is allowed. Changing the query length requires you to restart the instance.



### Terraform

**Warning:** To keep your Terraform state consistent, update configurations directly in your Terraform files. If you make manual changes using the Google Cloud console, gcloud CLI, or REST API, the following issues can occur: 

  * API errors
  * Perpetual diffs
  * Overwritten changes during `terraform apply`



To use Terraform to configure advanced query insights on your AlloyDB instance, use the [`google_alloydb_instance` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/alloydb_instance).

The following is an example:
    
    
      observability_config {
        enabled = ENABLED_VALUE
        preserve_comments = PRESERVE_COMMENTS_VALUE
        track_wait_events = TRACK_WAIT_EVENTS_VALUE
        max_query_string_length = MAX_QUERY_STRING_LENGTH_VALUE
        record_application_tags = RECORD_APPLICATION_TAGS_VALUE
        query_plans_per_minute = QUERY_PLANS_PER_MINUTE_VALUE
        track_active_queries = TRACK_ACTIVE_QUERIES_VALUE
        track_client_address = TRACK_CLIENT_ADDRESS_VALUE
        assistive_experiences_enabled = ASSISTIVE_EXPERIENCES_ENABLED_VALUE
      }
      

Replace the following:

  * `ENABLED_VALUE`: observability feature status for an instance. Set to `true` when you edit the settings and specify other flags as needed.
  * `PRESERVE_COMMENTS_VALUE`: preserve comments in the query string. The default value is `false`.
  * `TRACK_WAIT_EVENTS_VALUE`: record wait events during query execution for an instance. The default value is `true`.
  * `MAX_QUERY_STRING_LENGTH_VALUE`: query string length. The default value is `10240`. Any integer between 1024 and 100000 is valid.
  * `RECORD_APPLICATION_TAGS_VALUE`: record application tags for an instance. The default value is `true`.
  * `QUERY_PLANS_PER_MINUTE_VALUE`: the number of query execution plans captured by insights per minute for all queries combined. The default value is `20`. Any integer between 0 and 200 is valid.
  * `TRACK_ACTIVE_QUERIES_VALUE`: track actively running queries. The default value is `false`.
  * `TRACK_CLIENT_ADDRESS_VALUE`: record client IP addresses for an instance. The default value is `false`.
  * `ASSISTIVE_EXPERIENCES_ENABLED_VALUE`: enable assistive experiences. The default value is `false`.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://cloud.google.com/docs/terraform/basic-commands).




###  REST v1 

This example configures advanced query insights settings on your AlloyDB instance. For a complete list of parameters for this call, see [Method: projects.locations.clusters.instances.patch](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/projects.locations.clusters.instances/patch).

To configure advanced query insights settings, set the `enabled` field to `true` and modify other optional fields as needed. For a complete list of fields for this call, see [ObservabilityInstanceConfig](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/projects.locations.clusters.instances#observabilityinstanceconfig).

Before you use any of the request data, make the following replacements:

  * `CLUSTER_ID`: the ID of the cluster that you create. It must begin with a lowercase letter and can contain lowercase letters, numbers, and hyphens.
  * `PROJECT_ID`: the ID of the project where you want the cluster placed.
  * `LOCATION_ID`: the ID of the cluster's region.
  * `INSTANCE_ID`: the name of the primary instance that you want to create.



To modify your instance configuration, use the following [`PATCH`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/projects.locations.clusters.instances/patch) request:
    
    
    PATCH https://alloydb.googleapis.com/v1beta/{instance.name=projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID}?updateMask=observabilityConfig.enabled,observabilityConfig.preserveComments,observabilityConfig.trackWaitEvents,observabilityConfig.maxQueryStringLength,observabilityConfig.recordApplicationTags,observabilityConfig.queryPlansPerMinute,observabilityConfig.trackActiveQueries,observabilityConfig.trackClientAddress,observabilityConfig.assistiveExperiencesEnabled
    

The request JSON body that configures all advanced query insights fields looks as follows:
    
    
    {
     "observabilityConfig": {
       "enabled": true,
       "preserveComments": true,
       "trackWaitEvents": true,
       "maxQueryStringLength": 5000,
       "recordApplicationTags": true,
       "queryPlansPerMinute": 20,
       "trackActiveQueries": true,
       "trackClientAddress": true,
       "assistiveExperiencesEnabled": true
     }
    }
    

## Detect and diagnose query performance problems

You can use advanced query insights to detect and diagnose performance problems. The query insights dashboard displays the _database load_ , which is a measure of the work (in CPU seconds) that executed queries in your selected database perform over time. Each running query is either using or waiting for resources. The database load is the ratio of the amount of time taken by all the queries that are completed in a given time window, in elapsed real time.

### View the measure of work done by executed queries

The database load graph gives the measure of work done (in CPU seconds) by all executed queries in your database, sliced by the selected dimension. The database load is divided into the distribution data that you select from the chart drop-down.

You can break down the database load by any of the following dimensions:

  * Query
  * Wait event type
  * Wait event
  * Database
  * User



To view work completed by executed queries in your database, follow these steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. From the list of clusters and instances, click an instance.

  3. Click **Query insights**.

  4. Choose the database and user.

  5. Choose the total execution time for which you want to display data, for example, 1 or 6 hours, or a custom time.

  6. In the **Database Load by execution time** drop-down, choose the dimension you want to investigate. Depending on the dimension you choose, the graph displays how the chosen dimension contributes to the overall database load. For example, if you select the **Wait events** dimension from the database load chart drop-down, the breakdown of all wait events that occurred during the selected time range for the selected database and user is displayed in the database load chart.

The database load chart displays data for all nine wait event types and the wait events supported in PostgreSQL. Depending on the number of wait events and types, the top ten contributing wait events and types are displayed. If there are more than ten wait events, the top nine wait events are displayed, and the rest are grouped into the **Others** category. This approach also applies to other dimensions like Queries, Databases, and Users.




### View the top contributors to database load

Using the **Top dimensions by database load** table, you can view top contributors to the database load for the chosen time range and dimension selected in the **Database Load** chart. Depending on the dimension you choose in the **Top dimensions by database load** table, you can find the top values for the selected time window.

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. From the list of clusters and instances, click an instance.

  3. Click **Query insights**.

  4. Choose the database and user.

  5. Choose the total execution time for which you want to display data, for example, 1 or 6 hours, or a custom time.

  6. In the **Top dimensions by database load** table, you can click any of the following: 

**Dimension** | **Description**  
---|---  
Queries | The table displays the top normalized queries by total execution time. For each query, the data shown in columns are listed as follows:  

     * **Avg Exec Time (ms).** Average time for the query to execute.
     * **Total execution time (ms).** The total execution time taken by the specific query.
     * **Rows Returned.** The average number of rows fetched for the query.
     * **Times Called.** The number of times the query was called by the application.
     * **%load by chart dimension.** The pill chart depicts how the chart's dimension is distributed across for the specific query.   
Wait event types | The table displays the list of top wait event types that occurred during the selected time range.  

     * **Avg time spent in wait (ms).** Average time the queries spent in the specific wait event type.
     * **Total time spent in wait (ms).** The total execution time the queries spent in the specific wait event type.
     * **Wait event type count.** The number of times a specific wait event type occurred in the chosen time range.
     * **%load by chart dimension.** The pill chart depicts how the chart's dimension selected in the database load chart drop-down is distributed across the specific wait event type.   
Wait events | The table displays the list of top wait events that occurred during the selected time range.  

     * **Avg time spent in wait (ms).** Average time the queries spent in the specific wait event.
     * **Total time spent in wait (ms).** The total execution time the queries spent in the specific wait event.
     * **Wait event count.** The number of times a specific wait event occurred in the chosen time range.
     * **%load by chart dimension.** The pill chart depicts how the chart's dimension selected in the database load chart drop-down is distributed across the specific wait event.   
Database | The table shows the list of top databases that contributed to the load during the chosen time range across all executed queries.  

     * **Avg time spent in database (ms).** Average time the queries spent in the specific database. 
     * **Total time spent in database (ms).** The total execution time the queries spent in the specific database.
     * **%load by chart dimension.** The pill chart depicts how the chart's dimension selected in the database load chart drop-down is distributed across the specific database.  
User | The table shows the list of top users for the chosen time range across all executed queries.  

     * **Avg time spent in user (ms).** Average time the queries spent on the specific user. 
     * **Total time spent in user (ms).** The total execution time the queries spent in the specific user.
     * **%load by chart dimension.** The pill chart depicts how the chart's dimension selected in the database load chart drop-down is distributed across the specific user.  



### View query execution time

Advanced query insights features for AlloyDB display the top ten queries contributing to database load in the **Top dimensions by database load** table. The top query is the one that contributed the most database load for the selected time range. The subsequent queries are a percentage of the longest execution time.

To learn how the execution time of a parameter in the **Top dimensions by database load** is affected by different values of the selected chart dimension (queries, wait event types, wait events, databases, and users), follow these steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. From the list of clusters and instances, click an instance.

  3. Click **Query insights**.

  4. Choose the database and user.

  5. View **% load by chart dimension** in the **Top dimensions by database load** table to learn how a parameter in the table is impacted by parameters in the **Database Load** chart.

For example, when you select **All Queries** in the **Database Load** chart and you click the **Queries** tab in the **Top dimensions by database load** table, **% load by Queries** displays a list of the queries that contributed the most database load in the selected database during the given time period.




### View details about query execution time

You can view details about query execution time in **More details** , including the dimensions that you selected in the database load chart and table, the definition of each wait event, and data that is encapsulated in the **Others** category.

**More details** also displays details of complex information that isn't shown elsewhere in the query details screen. This information includes the definition of each wait event.

To view details about query execution time, follow these steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. From the list of clusters and instances, click an instance.

  3. Click **Query insights**.

  4. Choose the database and user.

  5. In the **Top dimensions by database load** table, click **More details** for a query.




Advanced query insights features for AlloyDB display normalized queries ($1, $2, and so on) to replace the literal constant values. For example:
    
    
    UPDATE
      "demo_customer"
    SET
      "customer_id" = $1::uuid,
      "name" = $2,
      "address" = $3,
      "rating" = $4,
      "balance" = $5,
      "current_city" = $6,
      "current_location" = $7
    WHERE
      "demo_customer"."id" = $8

The constant value is ignored so that advanced query insights can aggregate similar queries and remove any Personally Identifiable Information (PII) information that the constant might show.

### Determine database load for normalized queries

To display a measure of the time and resource usage by query execution (in CPU seconds) that your selected normalized query performed in the selected database over time, follow these steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. From the list of clusters and instances, click an instance.

  3. Click **Query insights**.

  4. Choose the database and user.

  5. Click **Queries** in the **Database Load** chart. To calculate database load, the **Database Load** chart uses the amount of time taken by the normalized queries that are completed in the minute boundary to the elapsed real time.




At the top of the **Database Load** chart, the first 10KB characters of normalized query are displayed, where literals are removed for aggregation and personally identifiable information (PII) reasons.

To help determine the distribution of time spent in each of these states, advanced query insights features for AlloyDB distribute per normalized query loads into wait events and wait event types.

You can study query latency using the **Latency** charts. _Latency_ is the time taken for the normalized query to complete in elapsed real time. Latency of parallel queries is measured in elapsed real time even though database load can be higher for the query due to multiple cores being used to run part of the query.

You can filter by percentile to view the 50th, 95th or 99th percentile to detect queries that don't adhere to the expected execution time. To analyze historical latency for the normalized query, change the time window.

### Analyze normalized queries

Query plans help you understand and analyze normalized queries by providing a breakdown of the different operations in a sample of your query.

The sample query plan provides an `EXPLAIN ANALYZE` view for the [query plan](https://en.wikipedia.org/wiki/Query_plan) samples that are related to the normalized query. These are executed query plans that provide a breakdown of the active time taken by each operation in the query plan.

To view a sample query plan, follow these steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. From the list of clusters and instances, click an instance.

  3. Click **Query insights**.

  4. Choose the database and user.

  5. Choose the total execution time for which you want to display data, for example, 1 or 6 hours, or a custom time.

  6. In the **Top dimensions by database load** table, click a query.

  7. In **Query plan samples** , click any of the dots on the chart to view a query plan for that query.




## Monitor and troubleshoot application performance using tags

Advanced query insights provide application-centric monitoring and simplifies performance diagnosis of applications built with object relational mapping (ORM). Query tagging helps you find issues at higher-level constructs, such as using the business logic, a microservice, or some other construct. You can use tags in your application to help you do the following:

  * Monitor database performance.
  * Use Sqlcommenter to identify performance issues caused by application code.
  * Analyze database load.
  * View the per-tag load.



To learn how to use tags in query insights, see [Improve query performance by using query insights](https://docs.cloud.google.com/alloydb/docs/using-query-insights).

## Troubleshoot applications at the database layer

Advanced query insights provide an in-context, end-to-end trace view to help you understand issues with the application at the database layer for a specific request. In-context end-to-end application traces help you determine the source of the problematic query, for example, by model, view, controllers, and route.

When you enable [OpenTelemetry](https://opentelemetry.io/), span information is sent to the database along with the tag information inside SQL comments. Traces from the application to Cloud Logging are linked with database query plan traces to identify the source of the problem.

To view an in-context trace, follow these steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. From the list of clusters and instances, click an instance.

  3. Click **Query insights**.

  4. Choose the database and user.

  5. Click any entry in the **Top dimensions by database load** table.

  6. In the **Query insights details** page, click **END to END**.




You can also use Cloud Trace to see end-to-end tracing for each step in the query plan. To access Cloud Trace, select **Operations > Trace**.

## Frequently Asked Questions

This section provides answers to frequently asked questions about advanced query insights features.

### Why is the query string truncated?

By default, advanced query insights displays 10 KB in query strings. You can increase the display to 100KB.

### Why is my CPU load above the max core line in the Database Load chart?

CPU load accounts for both run time and time waiting for the Linux scheduler to schedule the server process running, so as a result the CPU load can go beyond the max core line.

### Can I use standard query insights metrics?

Yes. Standard query insights generate counters that can be accessed through Stackdriver. These metrics are available using Cloud Monitoring API and the Metrics Explorer UI. For more information, see [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-alloydb).

**Note:** The query insights dashboard resets after you enable advanced query insights.

### What is the maximum query string length?

For the standard query insights plugin, the maximum query string length is limited to 4.5 KB characters. For advanced query insights, the default string length is 10KB and the maximum length is limited to 100KB.

### Can I use advanced query insights features with secondary clusters?

You can't enable advanced query insights on clusters with secondary instances. Before creating a secondary instance on a cluster, you must disable advanced query insights on all the instances in the cluster.

## What's next

  * [Advanced query insights features for AlloyDB overview](https://docs.cloud.google.com/alloydb/docs/advanced-query-insights-overview)
  * [AlloyDB metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-alloydb)
  * [How-to blog: Enable query tagging with Sqlcommenter](https://cloud.google.com/blog/topics/developers-practitioners/enable-query-tagging-sqlcommenter-understand-application-impact-database-performance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
