---
url: https://docs.cloud.google.com/alloydb/docs/using-query-insights/
title: Improve query performance using query insights \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:15.261314+00:00
---

# Improve query performance using query insights  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/using-query-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Improve query performance using query insights Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use the query insights dashboard to detect and analyze performance problems. For an overview of this feature, see [Query insights overview](https://docs.cloud.google.com/alloydb/docs/query-insights-overview).

You can use Gemini Cloud Assist to help you monitor and troubleshoot your AlloyDB resources. For more information, see [Monitor and troubleshoot with Gemini assistance](https://docs.cloud.google.com/alloydb/docs/monitor-troubleshoot-with-gemini).

## Before you begin

If you or other users need to view the query plan or perform end-to-end tracing, you need specific Identity and Access Management (IAM) permissions to do so. You can create a custom role and add the necessary IAM permissions to it. Then, you can add this role to each user account that uses query insights to troubleshoot an issue. See [Create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role).

The custom role needs to have the following IAM permission: `cloudtrace.traces.get`.

## Open the query insights dashboard

To open the query insights dashboard, do the following steps:

  1. From the list of clusters and instances, click an instance.
  2. Either click **Go to Query insights for more in-depth info on queries and performance** below the metrics graph on the cluster Overview page or select the **Query insights** tab in the left navigation panel. 



On the subsequent page, you can use the following options to filter the results:

  1. **Instance selector.** Lets you select either the primary instance or read pool instances in the cluster. By default, the primary instance is selected. The details shown are aggregated for all connected read pool instances and their nodes.
  2. **Database.** Filters query load on a specific database or all databases.
  3. **User.** Filters query load from specific user accounts.
  4. **Client address.** Filters query load from a specific IP address.
  5. **Time range.** Filters query load by time ranges, such as hour, day, week, or a custom range.

![The query insights dashboard provides an instance selector and
            drop-down menus for databases, users, and addresses. To the right
            of the drop-down menus, there's a filter for setting a time range.](https://docs.cloud.google.com/alloydb/images/adb-insights-edit-conf.png)**Note:** If you [enable Gemini Cloud Assist](https://docs.cloud.google.com/database-center/docs/set-up-database-center#enable-gemini), the data retention policy for query metrics is 30 days.

## Edit the query insights configuration

Query insights are enabled by default on AlloyDB instances. You can edit the default query insights configuration.

To edit the query insights configuration for an AlloyDB instance, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. Click **Query insights** in the left navigation panel.

  4. Select **Primary** or **Read pool** from the **Query insights** list, and then click **Edit**.

  5. Edit the **Query insights** fields:

     1. To change the default limit of 1024 bytes on query lengths for AlloyDB to analyze, in the **Query lengths** field, enter a number from 256 to 4500.

The instance restarts after you edit this field.

**Note** : Higher query-length limits require more memory.

     2. To customize your query insights feature sets, adjust the following options:

        * **Query plan sampling** : Select this checkbox to visualize the operations used to complete a sample of a query. The sampling rate determines the maximum number of queries that AlloyDB can sample per minute for the instance per node.

In the **Maximum sampling rate** field, enter a number from one to 20. By default, the sampling rate is set to 5. To disable sampling, clear the **Query plan sampling** checkbox.

        * **Store client IP addresses** : Select this checkbox to know from where your queries are originating, and to group that information to run metrics.

        * **Store application tags** : Select this checkbox to know which tagged applications are making requests, and to group that information to run metrics. For more information about application tags, see [the specification](https://google.github.io/sqlcommenter/spec/).

  6. Click **Update instance**.




### gcloud

To enable query insights for an AlloyDB instance using Google Cloud CLI commands, do the following:

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI.
  2. To [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI, run the following command: 
         
         gcloud init
         

  3. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login
         

You don't need to do this if you're using Cloud Shell.

For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development).




Here's an example:
    
    
    gcloud alloydb instances update INSTANCE \
    --cluster=CLUSTER \
    --project=PROJECT \
    --region=REGION \
    --insights-config-query-string-length=QUERY_LENGTH \
    --insights-config-query-plans-per-minute=QUERY_PLANS \
    --insights-config-record-application-tags \
    --insights-config-record-client-address

Replace the following:

  * `INSTANCE`: the ID of the instance to update
  * `CLUSTER`: the ID of the instance's cluster
  * `PROJECT`: the ID of the cluster's project
  * `REGION`: the cluster's region—for example, `us-central1`
  * `QUERY_LENGTH`: the length of the query that ranges from 256 to 4500
  * `QUERY_PLANS`: the number of query plans to configure per minute.



Also, use one or more of the following optional flags:

  * `--insights-config-query-string-length`: Sets the default query length limit to a specified value from 256 to 4500 bytes. The default query length is 1024 bytes. Higher query lengths are more useful for analytical queries, but they also require more memory. Changing the query length requires you to [restart the instance](https://docs.cloud.google.com/alloydb/docs/instance-restart). You can still add tags to queries that exceed the length limit.
  * `--insights-config-query-plans-per-minute`: By default, a maximum of five executed query plan samples are captured per minute across all databases on the instance. Change this value to a number from 1 to 20. To disable sampling, enter 0. Increasing the sampling rate is likely to give you more data points but might add a performance overhead.
  * `--insights-config-record-client-address`: Stores the client IP addresses where queries are coming from and helps you group that data to run metrics against it. Queries come from more than one host. Reviewing graphs for queries from client IP addresses can help identify the source of a problem. If you don't want to store client IP addresses, use `--no-insights-config-record-client-address`.
  * `--insights-config-record-application-tags`: Stores application tags that help you determine the APIs and model-view-controller (MVC) routes that are making requests and group the data to run metrics against it. This option requires you to comment queries with a specific set of tags. If you don't want to store application tags, use `--no-insights-config-record-application-tags`.



### Terraform

**Warning:** To keep your Terraform state consistent, update configurations directly in your Terraform files. If you make manual changes using the Google Cloud console, gcloud CLI, or REST API, the following issues can occur: 

  * API errors
  * Perpetual diffs
  * Overwritten changes during `terraform apply`



To use Terraform to configure query insights, use the [`google_alloydb_instance` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/alloydb_instance).

Here's an example:
    
    
      query_insights_config {
        query_string_length = QUERY_STRING_LENGTH_VALUE
        record_application_tags = RECORD_APPLICATION_TAG_VALUE
        record_client_address = RECORD_CLIENT_ADDRESS_VALUE
        query_plans_per_minute = QUERY_PLANS_PER_MINUTE_VALUE5
      }
      

Replace the following:

  * `QUERY_STRING_LENGTH_VALUE`: query string length. The default value is `1024`. Any integer between 256 and 4500 is valid.
  * `RECORD_APPLICATION_TAG_VALUE`: record application tag for an instance. The default value is `true`.
  * `RECORD_CLIENT_ADDRESS_VALUE`: record client address for an instance. The default value is `true`.
  * `QUERY_PLANS_PER_MINUTE_VALUE`: the number of query execution plans captured by Insights per minute for all queries combined. The default value is `5`. Any integer between 0 and 20 is valid.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://cloud.google.com/docs/terraform/basic-commands).

The sample instance configuration with the added query insights configuration should appear as follows:
        
        resource "google_alloydb_instance" "instance_name" {
        provider = "google-beta"
        cluster       = google_alloydb_cluster.default.name
        instance_id   = "instance_id"
        instance_type = "PRIMARY"
        
        machine_config {
         cpu_count = 8
        }
        
        query_insights_config {
        query_string_length = 1024
        record_application_tags = false
        record_client_address = false
        query_plans_per_minute = 5
        }
        
        depends_on = [google_alloydb_instance.default]
        }
        




###  REST v1 

This example configures observability settings on your AlloyDB instance. For a complete list of parameters for this call, see [Method: projects.locations.clusters.instances.patch](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances/patch).

To configure query insights settings, modify optional fields as needed. For a complete list of fields for this call, see [QueryInsightsInstanceConfig](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#QueryInsightsInstanceConfig).

Before you use any of the request data, make the following replacements:

  * `CLUSTER_ID`: the ID of the cluster that you create. It must begin with a lowercase letter and can contain lowercase letters, numbers, and hyphens.
  * `PROJECT_ID`: the ID of the project where you want the cluster placed.
  * `LOCATION_ID`: the ID of the cluster's region.
  * `INSTANCE_ID`: the name of the primary instance that you want to create.



To modify your instance configuration, use the following [`PATCH`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/projects.locations.clusters.instances/patch) request:
    
    
    PATCH https://alloydb.googleapis.com/v1beta/{instance.name=projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID?updateMask=observabilityConfig.enabled}
    

The request JSON body that configures all observability fields looks as follows:
    
    
    {
      "queryStringLength": integer,
      "recordApplicationTags": boolean,
      "recordClientAddress": boolean,
      "queryPlansPerMinute": integer
    }
    

## Improve query performance

Query insights troubleshoot AlloyDB queries to look for performance issues. The query insights dashboard shows the _query load_ based on factors that you select. Query load is a measurement of the total work for all the queries in the instance in the selected time range.

Query insights help you detect and analyze query performance problems. To troubleshoot queries with query insights, follow these steps:

  * View the database load for all queries.
  * Identify a problematic query or tag.
  * Examine the query or tag to identify issues.
  * Examine a trace generated by a sample query.



### View the database load for all queries

The top-level query insights dashboard shows the **Database load — all top queries** graph using filtered data. Database query load is a measure of the work (in CPU seconds) that the executed queries in your selected database perform over time. Each running query is either using or waiting for CPU resources, IO resources, or lock resources. Database query load is the ratio of the amount of time taken by all the queries that are completed in a given time window to the wall clock time.

![Shows the database load graph with a load for CPU capacity, CPU and
         CPU wait, IO Wait, and Lock Wait.](https://docs.cloud.google.com/alloydb/images/adb-insights-db-all.png)

Colored lines in the graph show the query load, split into four categories:

  * **CPU capacity** : The number of CPUs available on the instance.
  * **CPU and CPU Wait** : The ratio of the time taken by queries in an active state to wall clock time. IO and Lock waits do not block queries that are in an active state. This metric might mean that the query is either using the CPU or waiting for the Linux scheduler to schedule the server process running the query while other processes are using the CPU.

**Note** : CPU load accounts for both the runtime and the time waiting for the Linux scheduler to schedule the server process that is running. As a result, the CPU load can go beyond the maximum core line.

  * **IO Wait** : The ratio of time taken by queries that are waiting for IO to wall clock time. IO wait includes Read IO Wait and Write IO Wait. See the PostgreSQL [event table](https://www.postgresql.org/docs/current/monitoring-stats.html#WAIT-EVENT-TABLE). If you want a breakdown of information for IO waits, you can see it in Cloud Monitoring. For more information, see [metrics charts](https://docs.cloud.google.com/alloydb/docs/monitor-instance#metrics-pg).

  * **Lock Wait** : The ratio of time taken by queries that are waiting for Locks to wall clock time. It includes Lock Waits, LwLock Waits, and Buffer pin Lock waits. If you want a breakdown of information for lock waits, you can see it in Cloud Monitoring. For more information, see [metrics charts](https://docs.cloud.google.com/alloydb/docs/monitor-instance#metrics-pg).




Next, review the graph and use the filtering options to answer these questions:

  1. **Is the query load high?** Is the graph spiking or elevated over time? If you don't see a high load, then the problem isn't with your queries.
  2. **How long has the load been high?** Is it only high now? Or has it been high for a long time? Use the range selection to select various time periods to find out how long the problem has occurred. Or you can zoom in to view a time window where query load spikes are observed. You can zoom out to view up to one week of the timeline.
  3. **What is causing the high load?** You can select options to look at the CPU capacity, CPU and CPU wait, lock wait, or IO wait. The graph for each of these options is a different color so that you can see which one has the highest load. The dark blue line on the graph shows the max CPU capacity of the system. It lets you compare the query load with the max CPU system capacity. This comparison helps you know whether an instance is running out of CPU resources.
  4. **Which database is experiencing the load?** Select different databases from the Databases drop-down menu to find the databases with the highest loads.
  5. **Are specific users or IP addresses causing higher loads?** Select different users and addresses from the drop-down menus to compare which ones are causing higher loads.



### Filter the database load

The **Queries and tags** sections lets you filter or sort the query load for either a selected query or a SQL query tag.

#### Filter by queries

The **QUERIES** table provides an overview of the queries that cause the most query load. The table shows all the normalized queries for the time window and options selected on the query insights dashboard.

By default, the table sorts queries by the total execution time within the time window you selected.

![Shows the database load graph with a load for queries, with
         filters selected for CPU capacity, CPU and
         CPU wait, IO Wait, and Lock Wait.](https://docs.cloud.google.com/alloydb/images/adb-insights-top-queries.png)

To filter the table, select a property from **Filter queries**. To sort the table, select a column heading. The table shows the following properties:

  * **Query string.** The normalized query string. query insights only shows 1024 characters in the query string by default.

Queries labeled `UTILITY COMMAND` usually include `BEGIN`, `COMMIT`, and `EXPLAIN` commands or wrapper commands.

  * **Database.** The database that the query was run against.

  * **Load by total time/Load by CPU/Load by IO wait/Load by lock wait.** These options let you filter specific queries to find the largest load for each option.

  * **Avg execution time (ms).** The total time that all sub-tasks take across all parallel workers to complete the query. For more information, see Average execution time and duration.

  * **Times called.** The number of times the query was called by the application.

  * **Avg rows fetched.** The average number of rows fetched for the query.




Query insights display normalized queries, that is, $1, $2, and so on replace the literal constant values. For example:
    
    
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
    

The constant's value is ignored so that query insights can aggregate similar queries and remove any PII information that the constant might show.

#### Filter by query tags

To troubleshoot an application, you must first add tags to your SQL queries.

Query insights provide application-centric monitoring to diagnose performance problems for applications built using ORMs.

If you're responsible for the entire application stack, Query insights provide query monitoring from an application view. Query tagging helps you find issues at higher-level constructs, such as using the business logic, a microservice, or some other construct. You might tag queries by the business logic, for example, using the payment, inventory, business analytics, or shipping tags. You can then find the query load that the various types of business logic are created. For example, you might find unexpected events, such as spikes for a business analytics tag at 1 PM. Or you might see unexpected growth for a payment service trending over the previous week.

Query load tags provide a breakdown of the query load of the selected tag over time.

To calculate the **Database Load for Tag** , query insights use the amount of time taken by every query that uses the tag you select. Query insights calculate the completion time at the minute boundary using wall clock time.

On the query insights dashboard, select **TAGS** to view the tags table. The **TAGS** table sorts tags by their total load by total time.

![Figure 5 shows the query insights dashboard, with load for tags.
         Below the graph is a list of tags.](https://docs.cloud.google.com/alloydb/images/adb-insights-top-tags.png)

You can sort the table by selecting a property from **Filter queries** , or by clicking a column heading. The table shows the following properties:

  * **Action, Controller, Framework, Route, Application, DB Driver.** Each property that you added to your queries is shown as a column. At least one of these properties must be added if you want to filter by tags.
  * **Load by total time/Load by CPU/Load by IO wait/Load by lock wait.** These options let you filter specific queries to find the largest load for each option.
  * **Avg execution time (ms).** The total time that all sub-tasks take across all parallel workers to complete the query. For more information, see Average execution time and duration.
  * **Times called.** The number of times the query was called by the application.
  * **Avg rows fetched.** The average number of rows fetched for the query.
  * **Database.** The database that the query was run against.



### Examine a specific query or tag

To determine if a query or a tag is the root cause of the problem, do the following from the **Queries** tab or **Tags** tab, respectively:

  1. Click the **Load by total time** header to sort the list in descending order.
  2. Click the query or tag that looks like it has the highest load and is taking a longer time than the others.



A dashboard opens showing the details of the selected query or tag.

If you selected a query, an overview of the selected query is shown:

![Shows a truncated version of the selected query.](https://docs.cloud.google.com/alloydb/images/adb-query-insights-details.png)

If you selected a tag, an overview of the selected tag is shown.

#### Examine the load for a specific query or tag

The **Database load — specific query** graph shows a measure of the work (in CPU seconds) that your selected normalized query has performed in your selected query over time. To calculate load, it uses the amount of time taken by the normalized queries that are completed at the minute boundary to the wall clock time. At the top of the table, the first 1024 characters of the normalized query (where literals are removed for aggregation and PII reasons) are displayed. As with the total queries graph, you can filter the load for a specific query by **Database** , **User** , and **Client Address**. Query load is split into **CPU capacity** , **CPU and CPU Wait** , **IO Wait** , and **Lock Wait.**

![Shows the database load and latency graphs for a
         specific query.](https://docs.cloud.google.com/alloydb/images/adb-insights-specific-query-graph.png)

The **Database load — specific tags** graph shows a measure of the work (in CPU seconds) that queries matching your selected tags have performed in your selected database over time. As with the total queries graph, you can filter the load for a specific tag by **Database** , **User** , and **Client Address**.

![Shows the database load and latency graphs for a
         specific query.](https://docs.cloud.google.com/alloydb/images/adb-insights-specific-tag-graph.png)

#### Examine the latency

You use the **Latency** graph to examine latency on the query or tag. _Latency_ is the time taken for the normalized query to complete, in wall clock time. The latency dashboard shows 50th, 95th, and 99th percentile latency to find outlier behaviors.

![Shows the query latency graph for a specific
         query with filters selected for CPU capacity, CPU and CPU wait,
         IO Wait, and Lock Wait.](https://docs.cloud.google.com/alloydb/images/adb-insights-latency.png)

The latency of [Parallel Queries](https://www.postgresql.org/docs/10/parallel-query.html) is measured in wall clock time even though query load can be higher for the query due to multiple cores being used to run part of the query.

Try to narrow down the problem by looking at the following:

  1. **What is causing the high load?** Select options to look at the CPU capacity, CPU and CPU wait, lock wait, or IO wait.
  2. **How long has the load been high? Is it only high now? Or has it been high for a long time?** Change the time ranges to find the date and time that the load started performing poorly.
  3. **Were there spikes in latency?** You can change the time window to study the historical latency for the normalized query.



When you find the areas and times for the highest load, you can drill down further.

#### Examine the latency across a cluster

You use the **P99 latency on the same query across the cluster** graph to examine P99 latency on the query or tag across instances in the cluster.

![Shows the query latency graph for a specific
         query with filters selected for CPU capacity, CPU and CPU wait,
         IO Wait, and Lock Wait.](https://docs.cloud.google.com/alloydb/images/adb-insights-latency-cluster.png)

#### Examine operations in a sampled query plan

A query plan takes a sample of your query and breaks it down into individual operations. It explains and analyzes each operation in the query. The **Query plan samples** graph shows all the query plans running at particular times and the amount of time each plan took to run.

![Shows a graph for sample query plans, with the time when they
         were run at the bottom of the graph \(x axis\), and the number of seconds
         they ran on the right \(y axis\).](https://docs.cloud.google.com/alloydb/images/adb-query-samples.png)

To see details for the sample query plan, click the dots on the **Sample query plans** graph. There is a view of executed sample [query plans](https://en.wikipedia.org/wiki/Query_plan) for most, but not all, queries. Note that AlloyDB for PostgreSQL samples queries automatically. The more a query is run, the more likely it is to be sampled. If you need to view more sample query plans, follow the instructions in edit the query insights configuration to increase the **Maximum sampling rate**.

When you view a query plan's expanded details, you see a model of all the operations within that plan. Each operation shows the latency, rows returned, and the cost for that operation. When you select an operation, you can see more details, such as shared hit blocks, the type of schema, the actual loops, plan rows, and more.

![The query plan shows the latency and cost for each operation
         run for the query.](https://docs.cloud.google.com/alloydb/images/adb-insights-plan-details.png)

Try to narrow down the problem by looking at the following questions:

  1. What is the resource consumption?
  2. How does it relate to other queries?
  3. Does consumption change over time?



#### Examine a trace generated by a sample query

In addition to viewing the sample query plan, you can use query insights to view an in-context, end-to-end application trace for a sample query. This trace can help you identify the source of a problematic query by displaying database activity for a specific request. Also, log entries that the application sends to Cloud Logging during the request are linked to the trace, which helps you with your investigation.

To view the in-context trace, do the following:

  1. In the **Sample Query** pane, click the **End-to-end Trace** tab. This tab displays a Gantt chart that details the spans, which are records of individual operations, for the trace generated by the query.

  2. To view more details about each span, such as attributes and metadata, click the span.




You can also view the trace in the **Trace Explorer** page. To do so, click **View in Cloud Trace**. For details about how to use the **Trace Explorer** page to explore your trace data, see [Find and explore traces](https://docs.cloud.google.com/trace/docs/finding-traces).

## Add tags to SQL queries

Tagging SQL queries simplifies application troubleshooting. You can use sqlcommenter to add tags to your SQL queries either automatically by using Object-relational mapping (ORM) or manually.

### Use sqlcommenter with ORM

When ORM is used instead of directly writing SQL queries, you might not find application code that is causing performance challenges. You might also have trouble analyzing how your application code impacts query performance. To tackle that pain point, Query insights provide an open source library called sqlcommenter, an ORM instrumentation library. This library is useful for developers using [ORMs](https://en.wikipedia.org/wiki/Object-relational_mapping) and administrators to detect which application code is causing performance problems.

If you're using ORM and sqlcommenter together, the tags are auto created without requiring you to change or add custom code to your application.

You can install sqlcommenter on the application server. The instrumentation library allows application information related to your MVC framework to be propagated to the database along with the queries as a SQL comment. The database picks up these tags and starts recording and aggregating statistics by tags, which are orthogonal with statistics aggregated by normalized queries. Query insights show the tags so that you know which application is causing the query load. This information helps you find which application code is causing performance problems.

When you examine results in SQL database logs, they appear as follows:
    
    
    SELECT * from USERS /*action='run+this',
    controller='foo%3',
    traceparent='00-01',
    tracestate='rojo%2'*/
    

Supported tags include the controller name, route, framework, and action.

The set of ORMs in sqlcommenter is supported for various programming languages:

Python | 

  * Django
  * psycopg2
  * Sqlalchemy
  * Flask

  
---|---  
Java | 

  * Hibernate
  * Spring

  
Ruby | 

  * Rails

  
Node.js | 

  * Knex.js
  * Sequelize.js
  * Express.js

  
  
For more information about sqlcommenter and how to use it sqlcommenter in your ORM framework, see the sqlcommenter documentation in [GitHub](https://google.github.io/sqlcommenter/spec/).

### Use sqlcommenter to add tags manually

If you're not using ORM, you must manually add sqlcommenter tags to your SQL queries. In your query, you must augment each SQL statement with a comment containing a serialized key-value pair. Use at least one of the following keys:

  * `action=''`
  * `controller=''`
  * `framework=''`
  * `route=''`
  * `application=''`
  * `db driver=''`



Query insights drop all other keys. See the [sqlcommenter documentation](https://google.github.io/sqlcommenter/spec/#format) for the correct SQL comment format.

## Execution time and duration

Query insights provide an **Avg execution time (ms)** metric, which reports the total time that all sub-tasks take across all parallel workers to complete the query. This metric can help you optimize the aggregate resource utilization of databases by finding and optimizing queries that create the highest CPU overhead.

To view the elapsed time, you can measure the duration of a query by running the `\timing` command on the `psql` client. It measures the time that elapses between receiving the query and the PostgreSQL server sending a response. This metric can help you analyze why a given query is taking too long, and decide whether to optimize it to run faster.

If a query is completed single-threaded by a single task, the duration and average execution time remain the same.

## Enable advanced query insights features for AlloyDB

The advanced query insights features for AlloyDB dashboard is integrated within the standard query insights dashboard. For more information about enabling advanced query insights features, see [Improve query performance using advanced query insights features](https://docs.cloud.google.com/alloydb/docs/using-advanced-query-insights).

## What's next

  * [Query insights overview](https://docs.cloud.google.com/alloydb/docs/query-insights-overview)
  * [Improve query performance using advanced query insights features for AlloyDB](https://docs.cloud.google.com/alloydb/docs/using-advanced-query-insights)
  * [AlloyDB metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-alloydb)
  * [SQL Commenter blog: Introducing Sqlcommenter: An open source ORM auto-instrumentation library](https://cloud.google.com/blog/topics/developers-practitioners/introducing-sqlcommenter-open-source-orm-auto-instrumentation-library)
  * [How-to blog: Enable query tagging with Sqlcommenter](https://cloud.google.com/blog/topics/developers-practitioners/enable-query-tagging-sqlcommenter-understand-application-impact-database-performance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
