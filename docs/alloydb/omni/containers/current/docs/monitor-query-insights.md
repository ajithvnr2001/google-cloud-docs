---
url: https://docs.cloud.google.com/alloydb/omni/containers/current/docs/monitor-query-insights/
title: Monitor query performance using advanced query insights \u00a0|\u00a0 AlloyDB Omni using containers: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:54:34.712541+00:00
---

# Monitor query performance using advanced query insights  |  AlloyDB Omni using containers: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/current/docs/monitor-query-insights/

This page documents AlloyDB Omni version **18.4.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/overview)



Send feedback 

#  Monitor query performance using advanced query insights Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/monitor-query-insights)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/monitor-query-insights)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/monitor-query-insights)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/monitor-query-insights)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/monitor-query-insights)



Advanced query insights lets you detect, diagnose, and prevent query performance problems in your AlloyDB Omni database. It captures database telemetry, including normalized query statistics, wait events, client IP addresses, tags, and instance load, and retains historical metrics for 30 days.

You can use advanced query insights to perform the following tasks:

  * Identify high-latency and resource-intensive queries by analyzing execution time, I/O time, wait time, shared buffer activity, and row counts.
  * Troubleshoot bottlenecks by correlating slow queries with wait events and wait event classes.
  * Trace query performance to specific application components by tagging queries with [SQLCommenter](https://google.github.io/sqlcommenter/spec/) metadata.
  * Monitor active queries and open transactions in real time, and stop problematic sessions.



## Before you begin

**Caution:** Enabling the `google_insights_v2` extension for advanced query insights can introduce up to 5% performance overhead on your database instance.

Before you enable advanced query insights, verify the following requirements:

  * You are running a **standalone** AlloyDB Omni instance in a container. 

**Caution:** Don't use advanced query insights on a high availability (HA) instance.
  * You have `postgres` superuser access to the database instance and administrative access to restart the container. 

  * The `alloydbadmin` database exists on your instance. AlloyDB Omni creates this database by default during initialization.




## Enable advanced query insights

To enable advanced query insights, follow these steps:

  1. Connect to the `postgres` database as the `postgres` superuser:

### Docker
         
         docker exec -it CONTAINER_NAME psql -U postgres -d postgres
         

### Docker
         
         docker exec -it CONTAINER_NAME psql -U postgres -d postgres
         

### Podman
         
         podman exec -it CONTAINER_NAME psql -U postgres -d postgres
         

### Podman
         
         podman exec -it CONTAINER_NAME psql -U postgres -d postgres
         

Replace `CONTAINER_NAME` with the name of your AlloyDB Omni container, such as `my-omni-1`.

  2. Check the loaded libraries in `shared_preload_libraries`, add advanced query insights to the preload list, enable the extension, and exit `psql`:
         
         SHOW shared_preload_libraries;
         ALTER SYSTEM SET shared_preload_libraries = 'LIBRARY_1','LIBRARY_2','google_insights_v2';
         ALTER SYSTEM SET google_insights_v2.enabled = on;
         \q
         

Replace `LIBRARY_1`, `LIBRARY_2`, and any additional existing libraries with the library names returned by `SHOW shared_preload_libraries`. Enclose each individual library entry in single quotes, such as `'g_stats','google_columnar_engine','google_insights_v2'`, and include all existing libraries required by AlloyDB Omni so that you don't overwrite them.

  3. Restart the AlloyDB Omni server to apply the preload settings:

### Docker
         
         docker restart CONTAINER_NAME
         

### Docker
         
         docker restart CONTAINER_NAME
         

### Podman
         
         podman restart CONTAINER_NAME
         

### Podman
         
         podman restart CONTAINER_NAME
         

  4. Connect to the `alloydbadmin` database as the `postgres` superuser:

### Docker
         
         docker exec -it CONTAINER_NAME psql -U postgres -d alloydbadmin
         

### Docker
         
         docker exec -it CONTAINER_NAME psql -U postgres -d alloydbadmin
         

### Podman
         
         podman exec -it CONTAINER_NAME psql -U postgres -d alloydbadmin
         

### Podman
         
         podman exec -it CONTAINER_NAME psql -U postgres -d alloydbadmin
         

  5. Create the advanced query insights extension in the `alloydbadmin` database:
         
         CREATE EXTENSION IF NOT EXISTS google_insights_v2;
         

**Note:** Always create the extension in `alloydbadmin`, not in your application database. The extension captures activity across all databases on the instance and writes all telemetry to `alloydbadmin`.
  6. Verify that the library is loaded, the extension is enabled, and the `google_insights_v2` extension is installed in `alloydbadmin`:
         
         SHOW shared_preload_libraries;
         SHOW google_insights_v2.enabled;
         SELECT extname, extversion FROM pg_extension WHERE extname = 'google_insights_v2';
         

Confirm that `shared_preload_libraries` includes `google_insights_v2`, `google_insights_v2.enabled` returns `on`, and `pg_extension` returns a row for `google_insights_v2`.




## Dimensions and capability parameters

In AlloyDB Omni, advanced query insights records database telemetry into SQL tables, views, and functions in the `alloydbadmin` database across the following dimensions and capabilities:

  * Queries: use to identify slow or resource-intensive SQL statements when query latency increases.
  * Wait event types: use to determine whether CPU, disk I/O, or lock contention causes workload bottlenecks.
  * Wait events: use to identify the specific PostgreSQL wait event, such as `DataFileRead` or `WALWrite`, that delays query execution.
  * Databases: use to compare resource consumption across logical databases and isolate high-load databases on shared instances.
  * Users and client IP addresses: use to attribute query load to specific database roles or client IP addresses and identify problematic application clients.
  * Tags: use to correlate database load with specific application services, routes, or ORM actions tagged with [SQLCommenter](https://google.github.io/sqlcommenter/spec/).
  * Active queries: use to diagnose live performance spikes, blocked transactions, and long-running sessions in real time.



When you set `google_insights_v2.enabled` to `on`, AlloyDB Omni automatically collects metrics for queries, wait event types, wait events, databases, and users.

To update any `google_insights_v2.*` parameter at runtime without restarting the database server, run `ALTER SYSTEM SET` and reload the configuration:
    
    
    ALTER SYSTEM SET PARAMETER_NAME = VALUE;
    SELECT pg_reload_conf();
    

Replace the following:

  * `PARAMETER_NAME`: the name of the advanced query insights parameter to configure, such as `google_insights_v2.qi_track_active_queries`, `google_insights_v2.qi_track_tag`, or `google_insights_v2.qi_track_client_address`.
  * `VALUE`: the new value for the parameter, such as `on`.



For descriptions of each parameter, the corresponding observability views, and the metrics and columns that each view returns, see [Advanced query insights reference](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/reference/advanced-query-insights-reference).

## Time granularities

Each historical `observability_service_*` view is available at three time granularities:

  * Base views (`*_view`): 15-second flush intervals. Use these views to investigate recent spikes or incidents within the last 1 to 6 hours.
  * Coarse level 1 views (`*_coarse_1_view`): 5-minute aggregated intervals for the top 2,000 queries. Use these views to analyze performance trends across 6 to 24 hours.
  * Coarse level 2 views (`*_coarse_2_view`): 30-minute aggregated intervals for the top 2,000 queries. Use these views to analyze multi-day trends up to the 30-day retention limit.



The historical observability views store all execution, wait, and I/O time columns in microseconds, including `total_execution_time`, `total_wait_time`, `total_read_time`, `total_write_time`, and `time_spent`.

## Query historical performance metrics

Connect to the `alloydbadmin` database to run diagnostic queries against the historical observability views. For more information, see [Run and connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/run-connect).

The SQL statements in this section are example queries for common troubleshooting scenarios across the dimensions. You can customize these examples, such as changing the `recorded_on` time window, filtering by specific databases or roles, or querying `*_coarse_1_view` and `*_coarse_2_view` for multi-day analysis, to fit your workload.

### Identify high-latency queries

To find the top 10 normalized queries with the highest total execution time in the last hour, run the following example query against `google_insights_v2.observability_service_query_view`:
    
    
    SELECT
      query_id,
      database,
      username,
      left(query, 100) AS normalized_query,
      sum(count) AS total_executions,
      sum(total_execution_time) AS total_execution_time_us,
      round((sum(total_execution_time)::numeric / NULLIF(sum(count), 0)), 2) AS avg_execution_time_us,
      sum(total_rows) AS total_rows,
      sum(total_shared_blocks_hit) AS shared_blocks_hit,
      sum(total_shared_blocks_read) AS shared_blocks_read
    FROM google_insights_v2.observability_service_query_view
    WHERE recorded_on >= now() - INTERVAL '1 hour'
    GROUP BY query_id, database, username, left(query, 100)
    ORDER BY total_execution_time_us DESC
    LIMIT 10;
    

### Analyze wait events by query

To identify which wait event categories (`wait_class`) and granular wait events (`wait_event`) contribute the most wait time to a specific `query_id`, run the following example query against `google_insights_v2.observability_service_wait_event_stats_by_query_view`:
    
    
    SELECT
      query_id,
      database,
      username,
      wait_class,
      wait_event,
      sum(count) AS wait_occurrences,
      sum(time_spent) AS total_wait_time_us
    FROM google_insights_v2.observability_service_wait_event_stats_by_query_view
    WHERE recorded_on >= now() - INTERVAL '1 hour'
      AND query_id = QUERY_ID
    GROUP BY query_id, database, username, wait_class, wait_event
    ORDER BY total_wait_time_us DESC;
    

Replace `QUERY_ID` with the `query_id` value that `observability_service_query_view` returns.

### Analyze database, user, and client IP load

To compare total execution time, wait time, and query volume across logical databases and database roles in the last hour, run the following example query against `google_insights_v2.observability_service_db_load_conn_view`:
    
    
    SELECT
      database,
      username,
      sum(count) AS total_executions,
      sum(total_execution_time) AS total_execution_time_us,
      sum(total_wait_time) AS total_wait_time_us
    FROM google_insights_v2.observability_service_db_load_conn_view
    WHERE recorded_on >= now() - INTERVAL '1 hour'
    GROUP BY database, username
    ORDER BY total_execution_time_us DESC;
    

If you enable `google_insights_v2.qi_track_client_address`, you can also identify which connecting client IP addresses generate the most query time using the following example query against `google_insights_v2.observability_service_client_address_stats_by_query_view`:
    
    
    SELECT
      client_address,
      username,
      database,
      query_id,
      sum(count) AS total_executions,
      sum(time_spent) AS total_time_spent_us
    FROM google_insights_v2.observability_service_client_address_stats_by_query_view
    WHERE recorded_on >= now() - INTERVAL '1 hour'
    GROUP BY client_address, username, database, query_id
    ORDER BY total_time_spent_us DESC
    LIMIT 10;
    

### Trace query performance by tags

When `google_insights_v2.qi_track_tag` is set to `on` and your queries include [SQLCommenter](https://google.github.io/sqlcommenter/spec/) comments, run the following example query to aggregate execution time by application tag metadata using `google_insights_v2.observability_service_tag_view`:
    
    
    SELECT
      application,
      framework_name,
      framework_controller,
      framework_action,
      framework_route,
      database,
      username,
      sum(count) AS total_executions,
      sum(total_execution_time) AS total_execution_time_us,
      round((sum(total_execution_time)::numeric / NULLIF(sum(count), 0)), 2) AS avg_execution_time_us
    FROM google_insights_v2.observability_service_tag_view
    WHERE recorded_on >= now() - INTERVAL '1 hour'
    GROUP BY
      application,
      framework_name,
      framework_controller,
      framework_action,
      framework_route,
      database,
      username
    ORDER BY total_execution_time_us DESC
    LIMIT 10;
    

## Monitor active queries

When you set `google_insights_v2.qi_track_active_queries` to `on`, you can monitor running queries and open transactions in real time by querying `google_insights_v2.stat_activity` and `google_insights_v2.stat_activity_v3` in the `alloydbadmin` database.

These views expose active client connections, session and transaction durations, and current wait events while excluding background workers and `alloydbadmin` connections.

### Query active sessions and transaction durations

To identify which queries are actively running on the instance right now and which transactions have been running the longest, run the following example query in `alloydbadmin`:
    
    
    SELECT
      pid AS "Process ID",
      left(normalized_query, 40) AS "Query",
      state AS "Status",
      round(EXTRACT(EPOCH FROM (clock_timestamp() - backend_start))::numeric, 2) AS "Session duration (secs)",
      CASE
        WHEN xact_start IS NOT NULL
        THEN round(EXTRACT(EPOCH FROM (clock_timestamp() - xact_start))::numeric, 2)
        ELSE NULL
      END AS "Transaction duration (secs)",
      CASE
        WHEN query_start IS NOT NULL
        THEN round(EXTRACT(EPOCH FROM (clock_timestamp() - query_start))::numeric, 2)
        ELSE NULL
      END AS "Query duration (secs)",
      COALESCE(wait_event_type, '') AS "Wait event type",
      COALESCE(wait_event, '') AS "Wait event",
      database AS "Database",
      COALESCE(application_name, '') AS "Application name",
      username AS "Username",
      COALESCE(client_addr::text, '') AS "Client address"
    FROM google_insights_v2.stat_activity_v3
    WHERE state = 'active'
    ORDER BY query_start ASC;
    

### Stop a long-running query or transaction

To stop a long-running query or blocked transaction identified in `google_insights_v2.stat_activity_v3`, pass its process ID to `pg_terminate_backend`:
    
    
    SELECT pg_terminate_backend(PROCESS_ID);
    

Replace `PROCESS_ID` with the `Process ID` (`pid`) value returned by `google_insights_v2.stat_activity_v3`.

## Disable advanced query insights

To stop telemetry collection without restarting your AlloyDB Omni instance, set `google_insights_v2.enabled` to `off` and reload the configuration:
    
    
    ALTER SYSTEM SET google_insights_v2.enabled = off;
    SELECT pg_reload_conf();
    

To remove the extension objects and stored historical data from the `alloydbadmin` database, connect to `alloydbadmin` and drop the extension:
    
    
    DROP EXTENSION IF EXISTS google_insights_v2 CASCADE;
    

## What's next

  * [Advanced query insights reference](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/reference/advanced-query-insights-reference)
  * [Choose and install monitoring tools](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/choose-install-monitoring-tools)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
