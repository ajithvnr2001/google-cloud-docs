---
url: https://docs.cloud.google.com/trace/docs/analytics-samples/
title: Sample SQL queries for Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:29.346727+00:00
---

# Sample SQL queries for Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/analytics-samples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Sample SQL queries for Trace Stay organized with collections  Save and categorize content based on your preferences. 

You can use sample [SQL](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax) queries in Observability Analytics to analyze your Cloud Trace data, identify latency outliers, and calculate span performance percentiles across your services.

These examples demonstrate how to filter, group, and aggregate spans stored in the `_AllSpans` view. If you haven't written queries in Observability Analytics, then first see [Query and analyze traces](https://docs.cloud.google.com/trace/docs/analytics).

## SQL language support

Queries used in the **Observability Analytics** page support GoogleSQL functions with some exceptions.

The following SQL commands aren't supported for SQL queries issued by using the **Observability Analytics** page:

  * DDL and DML commands
  * Javascript user-defined functions
  * BigQuery ML functions
  * SQL variables



The following are supported only when you query a linked BigQuery dataset by using the **BigQuery Studio** and **Looker Studio** pages, or by using the [bq command-line tool](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference):

  * Javascript user-defined functions
  * BigQuery ML functions
  * SQL variables



## Best practices

To set the time range of your query, we recommend that you use the time-range selector. For example, to view the data for the past week, select **Last 7 days** from the time-range selector. You can also use the time-range selector to specify a start and end time, specify a time to view around, and change time zones.

If you include a `start_time` field in the `WHERE` clause, then the time-range selector setting isn't used. The following example illustrates how to filter by timestamp:
    
    
    -- Matches trace spans whose start_time is within the most recent 1 hour.
    WHERE start_time > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 HOUR)

For more information about how to filter by time, see [Time functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#time_functions) and [Timestamp functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#timestamp_functions).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Observability API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=observability.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Observability API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=observability.googleapis.com)

  8. To get the permissions that you need to load the **Observability Analytics** page, write, run, and save private queries on your trace data, ask your administrator to grant you the following IAM roles: 

     * [Observability View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.viewAccessor) (`roles/observability.viewAccessor`) on the observability views that you want to query. This role supports IAM conditions, which let you restrict the grant to a specific view. If you don't attach a condition to the role grant, then the principal can access all observability views.
     * [Observability Analytics User ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`) on your project. This role contains the permissions required to save and run private queries, and to run shared queries.

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## How to use the queries on this page

  1. In the Google Cloud console, go to the _manage_search_ **Observability Analytics** page: 

[Go to **Observability Analytics**](https://console.cloud.google.com/logs/analytics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. In the **Query** pane, click the _code_ **SQL** , and then copy and paste a query into the SQL query pane.

The following shows the format of the `FROM` cause for querying the `_AllSpans` view:
         
         FROM `PROJECT_ID.LOCATION._Trace.Spans._AllSpans`

The `FROM` clause contains the following fields:

     * PROJECT_ID: The identifier of the project.
     * LOCATION: The [location of the observability bucket](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).
     * `_Trace` is the name of the observability bucket
     * `Spans` is the name of the dataset.
     * `_AllSpans` is the name of the view.
**Note:** The delimiters for the path are period characters, `(.)`. If a path element like the Google Cloud project contains a period character, then ensure every path field is wrapped by single backquotes, `(`)`.



To use the queries shown in this document on the **BigQuery Studio** page or to use the [bq command-line tool](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference), then edit the `FROM` clause and enter the [path to the linked BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#table_path). For example, to query the `_AllSpans` view on the linked BigQuery dataset named `my_linked_dataset` that is in the project `myproject`, the path is ``myproject.my_linked_dataset._AllSpans``.

## Common use cases

This section lists several common use cases that might help you create your custom queries.

### Show all trace data

To query the `_AllSpans` view, run the following query:
    
    
    -- Display all data.
    SELECT *
    FROM `PROJECT_ID.LOCATION._Trace.Spans._AllSpans`
    -- Limit to 10 entries.
    LIMIT 10
    

### Show common span information

To show common span information, like the start time and duration, run the following query:
    
    
    SELECT
      start_time,
      -- Set the value of service name based on the first non-null value in the list.
      COALESCE(
        JSON_VALUE(resource.attributes, '$."service.name"'),
        JSON_VALUE(attributes, '$."service.name"'),
        JSON_VALUE(attributes, '$."g.co/gae/app/module"')) AS service_name,
      name AS span_name,
      duration_nano,
      status.code AS status,
      trace_id,
      span_id
    FROM
      `PROJECT_ID.LOCATION._Trace.Spans._AllSpans`
    LIMIT 10
    

To learn more, see [Conditional expressions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/conditional_expressions).

### Show 50th and 99th percentiles of the span latency

To show the 50th and 99th percentiles of the latency for each rpc service, run the following query:
    
    
    SELECT
      -- Compute 50th and 99th percentiles for each service
      STRING(attributes['rpc.service']) || '/' || STRING(attributes['rpc.method']) AS rpc_service_method,
      APPROX_QUANTILES(duration_nano, 100)[OFFSET(50)] AS duration_nano_p50,
      APPROX_QUANTILES(duration_nano, 100)[OFFSET(99)] AS duration_nano_p99
    FROM
      `PROJECT_ID.LOCATION._Trace.Spans._AllSpans`
    WHERE
      -- Matches spans whose kind field has a value of 2 (SPAN_KIND_SERVER).
      kind = 2
    GROUP BY rpc_service_method
    

For more information about the enumeration, see the [OpenTelemetry: SpanKind](https://github.com/open-telemetry/opentelemetry-proto/blob/main/opentelemetry/proto/trace/v1/trace.proto#L150) documentation.

To view the results graphically, you might create a chart with the dimension set to `rpc_service_method`. You might add two measures, one for the average of the `duration_nano_p50` value, and the other for the average of the `duration_nano_p99` field.

## Filter trace entries

To apply a filter to your query, add a `WHERE` clause. The syntax that you use in this clause depends on the data type of the field. This section provides several examples for different data types.

### Filter by string data types

The field `name` is stored as a `String`.

  * To analyze only those spans where `name` is specified, use the following clause:
        
        -- Matches spans that have a name field.
        WHERE name IS NOT NULL
        

  * To analyze only those spans where `name` has the value `"POST"`, use the following clause:
        
        -- Matches spans whose name is POST.
        WHERE STRPOS(name, "POST") > 0
        

  * To analyze only those spans where `name` contains the value `"POST"`, use the `LIKE` operator along with wildcards:
        
        -- Matches spans whose name contains POST.
        WHERE name LIKE "%POST%"
        




### Filter by integer data types

The field `kind` is an integer, which can take values between zero and five:

  * To analyze only those spans where `kind` is specified, use the following clause:
        
        -- Matches spans that have field named kind.
        WHERE kind IS NOT NULL
        

  * To analyze spans whose `kind` value is either one or two, use the following clause:
        
        -- Matches spans whose kind value is 1 or 2.
        WHERE kind IN (1, 2)
        




### Filter by RECORD data types

Some fields in the trace schema have a data type of `RECORD`. These fields can either store one or more data structures, or they store repeated entries of the same data structure.

#### Filter by status or status code

The `status` field is an example of a field whose data type is `RECORD`. This field stores one data structure, with members labeled `code` and `message`.

  * To only analyze spans when the `status.code` field has a value of `1`, add the following clause:
        
        -- Matches spans that have a status.code field that has a value of 1.
        WHERE status.code = 1
        

The `status.code` field is stored as an integer.

  * To analyze spans where the `status` field isn't `EMPTY`, add the following clause:
        
        -- Matches spans that have status field. When the status field exists, it
        -- must contain a subfield named code.
        -- Don't compare status to NULL, because this field has a data type of RECORD.
        WHERE status.code IS NOT NULL
        




#### Filter by events or links

The `events` and `links` fields are stored with a data type of `RECORD`, but these are repeated fields.

  * To match spans that have at least one event, use the following clause:
        
        -- Matches spans that have at least one event. Don't compare events to NULL.
        -- The events field has data type of RECORD and contains a repeated fields.
        WHERE ARRAY_LENGTH(events) > 0
        

  * To match spans that have an event whose `name` field has the value of `message`, use the following clause:
        
        WHERE
          -- Exists is true when any event in the array has a name field with the
          -- value of message.
          EXISTS(
            SELECT 1
            FROM UNNEST(events) AS ev
            WHERE ev.name = 'message'
          )
        




### Filter by JSON data types

The `attributes` field is of type `JSON`. Each individual attribute is a key-value pair.

  * To analyze only those spans where `attributes` is specified, use the following clause:
        
        -- Matches spans where at least one attribute is specified.
        WHERE attributes IS NOT NULL
        

  * To analyze only those spans where the attribute key named `component` has a value of `"proxy"`, use the following clause:
        
        -- Matches spans that have an attribute named component with a value of proxy.
        WHERE attributes IS NOT NULL
              AND JSON_VALUE(attributes, '$.component') = 'proxy'
        

You can also use a `LIKE` statement along with wildcards to perform a contains test:
        
        -- Matches spans that have an attribute named component whose value contains proxy.
        WHERE attributes IS NOT NULL
              AND JSON_VALUE(attributes, '$.component') LIKE '%proxy%'
        




## Group and aggregate trace data

This section illustrates how you can group and aggregate spans. If you don't specify a grouping but do specify an aggregation, one result is printed because SQL treats all entries that satisfy the `WHERE` clause as one group.

Every `SELECT` expression must be included in the group fields or be aggregated.

### Group spans by start time

To group data by start time, use the function [`TIMESTAMP_TRUNC`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/timestamp_functions#timestamp_trunc), which truncates a timestamp to a specified granularity like `HOUR`:
    
    
    SELECT
      -- Truncate the start time to the hour. Count the number of spans per group.
      TIMESTAMP_TRUNC(start_time, HOUR) AS hour,
      status.code AS code,
      COUNT(*) AS count
    FROM
      `PROJECT_ID.LOCATION._Trace.Spans._AllSpans`
    WHERE
      -- Matches spans shows start time is within the previous 12 hours.
      start_time > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 12 HOUR)
    GROUP BY
      -- Group by hour and status code.
      hour, code
    ORDER BY hour DESC
    

For more information, see [`TIMESTAMP_TRUNC` documentation](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/timestamp_functions#timestamp_trunc) and [Datetime functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/datetime_functions).

**Note:** If you include a `start_time` field in the `WHERE` clause, then the time-range selector setting isn't used.

### Count spans by status code

To display the count of spans with a specific status code, run the following query:
    
    
    SELECT
      -- Count the number of spans for each status code.
      status.code,
      COUNT(*) AS count
    FROM
      `PROJECT_ID.LOCATION._Trace.Spans._AllSpans`
    WHERE status.code IS NOT NULL
    GROUP BY status.code
    

If you replace `status.code` with `kind`, then the previous query reports the number of spans for each value of the `kind` enumeration. Similarly, if you replace `status.code` with `name`, then the query result lists the number of entries for each span name.

### Compute the average duration of all spans

To display the average duration, after grouping span data by span name, run the following query:
    
    
    SELECT
      -- Group by name, and then compute the average duration for each group.
      name,
      AVG(duration_nano) AS nanosecs,
    FROM
      `PROJECT_ID.LOCATION._Trace.Spans._AllSpans`
    GROUP BY name
    ORDER BY nanosecs DESC
    

### Compute average duration and percentiles per service name

The following query computes the span count and various statistics for each service:
    
    
    SELECT
      -- Set the service name by the first non-null value.
      COALESCE(
        JSON_VALUE(resource.attributes, '$."service.name"'),
        JSON_VALUE(attributes, '$."service.name"'),
        JSON_VALUE(attributes, '$."g.co/gae/app/module"')) AS service_name,
    
      -- Count the number spans for each service name. Also compute statistics.
      COUNT(*) AS span_count,
      AVG(duration_nano) AS avg_duration_nano,
      MIN(duration_nano) AS min_duration_nano,
      MAX(duration_nano) AS max_duration_nano,
    
      -- Calculate percentiles for duration
      APPROX_QUANTILES(duration_nano, 100)[OFFSET(50)] AS p50_duration_nano,
      APPROX_QUANTILES(duration_nano, 100)[OFFSET(95)] AS p95_duration_nano,
      APPROX_QUANTILES(duration_nano, 100)[OFFSET(99)] AS p99_duration_nano,
    
      -- Count the number of unique trace IDs. Also, collect up to 5 unique
      -- span names and status codes.
      COUNT(DISTINCT trace_id) AS distinct_trace_count,
      ARRAY_AGG(DISTINCT name IGNORE NULLS LIMIT 5) AS sample_span_names,
      ARRAY_AGG(DISTINCT status.code IGNORE NULLS LIMIT 5) AS sample_status_codes
    FROM
      `PROJECT_ID.LOCATION._Trace.Spans._AllSpans`
    GROUP BY service_name
    ORDER BY span_count DESC
    

## Cross-column search

This section describes two approaches that you can use to search multiple columns of the view that you are querying:

  * Token-based searches: You specify the search location, a search query, and then use the [`SEARCH`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/search_functions) function. Because the `SEARCH` function has specific rules on how the data is searched, we recommend that you read the [`SEARCH` documentation](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/search_functions).

  * Substring-based searches: You provide the search location, a string literal, and then use the function [`CONTAINS_SUBSTR`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/string_functions#contains_substr). The system performs a case-insensitive test to determine whether the string literal exists in an expression. The `CONTAINS_SUBSTR` function returns `TRUE` when the string literal exists and `FALSE` otherwise. The search value must be a `STRING` literal, but not the literal `NULL`.




## Query multiple views

Query statements scan one or more tables or expressions and return the computed result rows. For example, you can use query statements to merge the results of `SELECT` statements on different tables or datasets in a variety of ways and then select the columns from the combined data.

To join views, the following restrictions apply:

  1. The locations of the views satisfy one of the following:

     * All views have the same location.
     * All views are in either the `global` or `us` location.
  2. When storage resources use customer managed encryption keys (CMEK), one of the following is be true:

     * Storage resources that use CMEK use the same Cloud KMS key.
     * Storage resources that use CMEK have a common ancestor, and that ancestor specifies a default Cloud KMS key that is in the same location as the storage resources.

When one or more storage resources uses CMEK, the system encrypts temporary data generated by the join with either the common Cloud KMS key or the ancestor's default Cloud KMS key.




For example, suppose that you have two views that reside in the same location. Then you can join these views when any of the following are true:

  * The storage resources don't use CMEK.
  * One storage resource uses CMEK and the other doesn't.
  * Both storage resources use CMEK and both use the same Cloud KMS key.
  * Both storage resources use CMEK but they use different keys. However, the resources share an ancestor that specifies a default Cloud KMS key that is in the same location as the storage resources.

For example, suppose that the resource hierarchy for a log bucket and observability bucket includes the same organization. You can join views on those buckets when, for that organization, you've configured the [default resource settings for Cloud Logging](https://docs.cloud.google.com/logging/docs/default-settings) and for [observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets) with the same default Cloud KMS key for the storage location.




### Join trace and log data by using the trace ID

The following query joins log and trace data by using the span and trace IDs:
    
    
    SELECT
      T.trace_id,
      T.span_id,
      T.name,
      T.start_time,
      T.duration_nano,
      L.log_name,
      L.severity,
      L.json_payload
    FROM
      `PROJECT_ID.LOCATION._Trace.Spans._AllSpans` AS T
    JOIN
      `PROJECT_ID.LOCATION._Default._AllLogs` AS L
    ON
      -- Join log and trace data by both the span ID and trace ID.
      -- Don't join only on span ID, this field isn't globally unique.
      T.span_id = L.span_id
      -- A regular expression is required because the storage format of the trace ID
      -- differs between a log view and a trace view.
      AND T.trace_id = REGEXP_EXTRACT(L.trace, r'/([^/]+)$')
    WHERE T.duration_nano > 1000000
    LIMIT 10
    

The response of the query lists the trace and span ID, which let you query for them individually to gather more information. Additionally, the results list the severity of the log entry and the JSON payload.

## What's next

  * [Save and share a SQL query](https://docs.cloud.google.com/trace/docs/analytics-save-share-query)
  * [Chart SQL query results](https://docs.cloud.google.com/trace/docs/analytics-chart)
  * [Query a linked BigQuery dataset in BigQuery](https://docs.cloud.google.com/trace/docs/analytics-query-linked-dataset)



For SQL reference documentation or other examples, see the following documents:

  * [Functions, operators, and conditionals](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators)
  * [Search functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/search_functions)
  * [Query syntax](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)
  * [Sample SQL queries for Cloud Logging](https://docs.cloud.google.com/logging/docs/analyze/examples)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
