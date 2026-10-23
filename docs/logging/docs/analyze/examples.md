---
url: https://docs.cloud.google.com/logging/docs/analyze/examples/
title: Sample SQL queries \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:28.149664+00:00
---

# Sample SQL queries  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/analyze/examples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Sample SQL queries Stay organized with collections  Save and categorize content based on your preferences. 

You can use sample [SQL](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators) queries in Observability Analytics to analyze log entries, extract payload fields, and aggregate log data across your services. You run these queries from the **Observability Analytics** page in the Google Cloud console on [log buckets that are upgraded to use Observability Analytics](https://docs.cloud.google.com/logging/docs/log-analytics). For more samples, see the [`logging-analytics-samples`](https://github.com/GoogleCloudPlatform/logging-analytics-samples) and [`security-analytics`](https://github.com/GoogleCloudPlatform/security-analytics/tree/main/backends/log_analytics/sql) GitHub repositories. For information about SQL syntax or how to route and store log entries, see the What's next section.

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

If you include a `timestamp` field in the `WHERE` clause, then the time-range selector setting isn't used. The following example illustrates how to filter by timestamp:
    
    
    -- Matches log entries whose timestamp is within the most recent 1 hour.
    WHERE timestamp > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 HOUR)

For more information about how to filter by time, see [Time functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#time_functions) and [Timestamp functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators#timestamp_functions).

## Before you begin

This section describes steps that you must complete before you can use Observability Analytics.

### Configure log buckets

Ensure that your log buckets have been upgraded to use Observability Analytics:

  1. In the Google Cloud console, go to the **Logs Storage** page: 

[Go to **Logs Storage**](https://console.cloud.google.com/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. For each log bucket that has a log view that you want to query, ensure that the **Observability Analytics available** column displays **Open**. If **Upgrade** is shown, then click **Upgrade** and complete the dialog.



### Configure IAM roles and permissions

This section describes the IAM roles or permissions that are required to use Observability Analytics:

  * To get the permissions that you need to use Observability Analytics and query log views, ask your administrator to grant you the following IAM roles on your project: 

    * To query the `_Required` and `_Default` log buckets: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) 
    * To query all log views in a project: [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`) 

You can restrict a principal to a specific log view either by adding an IAM condition to the Logs View Accessor role grant made at the project level, or by adding an IAM binding to the policy file of the log view. For more information, see [Control access to a log view](https://docs.cloud.google.com/logging/docs/logs-views#about-iam-policies).

These are the same permissions that you need to view log entries on the **Logs Explorer** page. For information about additional roles that you need to query views on user-defined buckets or to query the `_AllLogs` view of the `_Default` log bucket, see [Cloud Logging roles](https://docs.cloud.google.com/logging/docs/access-control#considerations).

  * To get the permissions that you need to query analytics views, ask your administrator to grant you the [Observability Analytics User ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`) IAM role on your project. 




## How to use the queries on this page

  1. In the Google Cloud console, go to the _manage_search_ **Observability Analytics** page: 

[Go to **Observability Analytics**](https://console.cloud.google.com/logs/analytics)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. In the **Query** pane, click the _code_ **SQL** , and then copy and paste a query into the SQL query pane.

Before you copy a query, in the `FROM` clause, replace the following fields

     * PROJECT_ID: The identifier of the project.
     * LOCATION: The location of the log view or the analytics view.
     * BUCKET_ID: The name or ID of the log bucket.
     * LOG_VIEW_ID: The identifier of the log view, which is limited to 100 characters and can include only letters, digits, underscores, and hyphens.

The following shows the format of the `FROM` clause for a [log view](https://docs.cloud.google.com/logging/docs/logs-views):
    
    FROM `PROJECT_ID.LOCATION.BUCKET_ID.LOG_VIEW_ID`

The log samples on this page query a log view. To query an [analytics view](https://docs.cloud.google.com/logging/docs/analyze/about-analytics-views), use the following path format: ``analytics_view.PROJECT_ID.LOCATION.ANALYTICS_VIEW_ID``. In the previous expression, `PROJECT_ID` is the ID of your project, and `LOCATION` and `ANALYTICS_VIEW_ID`, are the location and name of your analytics view.

**Note:** The delimiters for the path are period characters, `(.)`. If a path element like the Google Cloud project contains a period character, then ensure every path field is wrapped by single backquotes, `(`)`.



To use the queries shown in this document on the **BigQuery Studio** page or to use the [bq command-line tool](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference), then edit the `FROM` clause and enter the [path to the linked BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#table_path). For example, to query the `_AllLogs` view on the linked BigQuery dataset named `mydataset` that is in the project `myproject`, the path is `myproject.mydataset._AllLogs`.

## Common use cases

This section lists several common use cases that might help you create your custom queries.

### Show log entries in the default log bucket

To query the `_Default` bucket, run the following query:
    
    
    SELECT
      timestamp, severity, resource.type, log_name, text_payload, proto_payload, json_payload
    FROM
      `PROJECT_ID.LOCATION._Default._AllLogs`
    -- Limit to 1000 entries
    LIMIT 1000
    

### Extract field value by regular expression

To extract a value from a string by using a regular expression, use the function [`REGEXP_EXTRACT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/string_functions#regexp_extract):
    
    
    SELECT
      -- Display the timestamp, and the part of the name that begins with test.
      timestamp, REGEXP_EXTRACT(JSON_VALUE(json_payload.jobName), r".*(test.*)$") AS name,
    FROM
      `PROJECT_ID.LOCATION.BUCKET_ID.LOG_VIEW_ID`
    WHERE
      -- Get the value of jobName, which is a subfield in a JSON structure.
      JSON_VALUE(json_payload.jobName) IS NOT NULL
    ORDER BY timestamp DESC
    LIMIT 20
    

For more information, see the [`REGEXP_EXTRACT` documentation](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/string_functions#regexp_extract).

For substring matches, like the previous query, use of the [`CONTAINS_SUBSTR`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/string_functions#contains_substr) function results in a more efficient query.

## Filter log entries

To apply a filter to your query, add a `WHERE` clause. The syntax that you use in this clause depends on the data type of the field. This section provides several examples for different data types.

### Filter log entries by payload type

Log entries can have one of three payload types. To filter log entries by the payload type, use one of the following clauses:

  * Text payloads
        
        -- Matches log entries that have a text payload.
        WHERE text_payload IS NOT NULL
        

  * JSON payloads
        
        -- Matches log entries that have a JSON payload.
        WHERE json_payload IS NOT NULL
        

  * Proto payloads
        
        -- Matches log entries that have a proto payload.
        -- Because proto_payload has a data type of RECORD, this statement tests
        -- whether a mandatory subfield exists.
        WHERE proto_payload.type IS NOT NULL
        




In the query results, both the `json_payload` and `proto_payload` fields are rendered in JSON, which you can navigate through.

### Filter log data by timestamp

To filter log entries by their timestamp, we recommend that you use the time-range selector. However, you can also specify the `timestamp` in the `WHERE` clause:
    
    
    -- Matches log entries whose timestamp is within the most recent hour
    WHERE timestamp > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 HOUR)
    

For more information about how to filter by time, see [Time functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/time_functions) and [Timestamp functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/timestamp_functions).

**Note:** If you include a `timestamp` field in the `WHERE` clause, then the time-range selector setting isn't used.

### Filter by resource

To filter your log data by resource, add a `resource.type` statement to the `WHERE` clause:
    
    
    -- Matches log entries whose resource type is gce_instance
    WHERE resource.type = "gce_instance"
    

### Filter by severity

To filter your log data by a severity, add a `severity` statement to the `WHERE` clause:
    
    
    -- Matches log entries whose severity is INFO or ERROR
    WHERE severity IS NOT NULL AND severity IN ('INFO', 'ERROR')
    

You can also filter your log entries by the `severity_number`, which is an integer. For example, the following clause matches all log entries whose severity level is at least `NOTICE`:
    
    
    -- Matches log entries whose severity level is at least NOTICE
    WHERE severity_number IS NOT NULL AND severity_number > 200
    

For information about the enumerated values, see [`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity).

### Filter by log name

To filter your log data by a log name, add a `log_name` or `log_id` statement to the `WHERE` clause:

  * Log name specifies the resource path:
        
        -- Matches log entries that have the following log ID.
        WHERE log_name="projects/cloud-logs-test-project/logs/cloudaudit.googleapis.com%2Factivity"
        

  * Log ID omits the resource path:
        
        -- Matches log entries that have the following log id.
        WHERE log_id = "cloudaudit.googleapis.com/data_access"
        




### Filter log entries by resource label

Resource labels are stored as a JSON structure. To filter by the value of a field within a JSON structure, use the function [`JSON_VALUE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/json_functions#json_value):
    
    
    SELECT
      timestamp, JSON_VALUE(resource.labels.zone) AS zone, json_payload, resource, labels
    FROM
      `PROJECT_ID.LOCATION.BUCKET_ID.LOG_VIEW_ID`
    WHERE
      -- Matches log entries whose resource type is gce_instance and whose zone is
      -- us-central1-f. Because resource has data type JSON, you must use JSON_VALUE
      -- to get the value for subfields, like zone.
      resource.type = "gce_instance" AND
      JSON_VALUE(resource.labels.zone) = "us-central1-f"
    ORDER BY timestamp ASC
    

The previous query relies on the format of resource labels, as they are stored in a log entry. The following is an example of the resource field:
    
    
    {
       type: "gce_instance"
       labels: {
          instance_id: "1234512345123451"
          project_id: "my-project"
          zone: "us-central1-f"
       }
    }
    

For information about all functions that can retrieve and transform JSON data, see [JSON functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/json_functions).

### Filter by HTTP request

To only query log entries that have an HTTP request field, use the following clause:
    
    
    -- Matches log entries that have a HTTP request_method field.
    -- Don't compare http_request to NULL. This field has a data type of RECORD.
    WHERE http_request.request_method IS NOT NULL
    

You can also use the `IN` statement:
    
    
    -- Matches log entries whose HTTP request_method is GET or POST.
    WHERE http_request.request_method IN ('GET', 'POST')
    

### Filter by HTTP status

To only query log entries that have an HTTP status, use the following clause:
    
    
    -- Matches log entries that have an http_request.status field.
    WHERE http_request.status IS NOT NULL
    

### Filter by a field within a JSON data type

To only query log entries when the subfield of a field with a JSON data type has a specific value, extract the value by using the function [`JSON_VALUE`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/json_functions#json_value):
    
    
    -- Compare the value of the status field to NULL.
    WHERE JSON_VALUE(json_payload.status) IS NOT NULL
    

The previous clause is subtly different than the following clause:
    
    
    -- Compare the status field to NULL.
    WHERE json_payload.status IS NOT NULL
    

The first clause tests whether the value of the status field is `NULL`. The second clause tests whether the status field exists. Suppose a log view contains two log entries. For one log entry, the `json_payload` field has the following form:
    
    
    {
        status: {
            measureTime: "1661517845"
        }
    }
    

For the other log entry, the `json_payload` field has a different structure:
    
    
    {
        @type: "type.googleapis.com/google.cloud.scheduler.logging.AttemptFinished"
        jobName: "projects/my-project/locations/us-central1/jobs/test1"
        relativeUrl: "/food=cake"
        status: "NOT_FOUND"
        targetType: "APP_ENGINE_HTTP"
    }
    

The clause `WHERE json_payload.status IS NOT NULL` matches both log entries. However, the clause `WHERE JSON_VALUE(json_payload.status) IS NOT NULL` only matches the second log entry.

## Group and aggregate log entries

This section builds upon the previous samples and illustrates how you can group and aggregate log entries. If you don't specify a grouping but do specify an aggregation, one result is printed because SQL treats all rows that satisfy the `WHERE` clause as one group.

Every `SELECT` expression must be included in the group fields or be aggregated.

### Group log entries by timestamp

To group data by timestamp, use the function [`TIMESTAMP_TRUNC`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/timestamp_functions#timestamp_trunc), which truncates a timestamp to a specified granularity like `HOUR`:
    
    
    SELECT
      -- Truncate the timestamp by hour.
      TIMESTAMP_TRUNC(timestamp, HOUR) AS hour,
      JSON_VALUE(json_payload.status) AS status,
      -- Count the number log entries in each group.
      COUNT(*) AS count
    FROM
      `PROJECT_ID.LOCATION.BUCKET_ID.LOG_VIEW_ID`
    WHERE
      -- Matches log entries that have a status field whose value isn't NULL.
      json_payload IS NOT NULL AND JSON_VALUE(json_payload.status) IS NOT NULL
    GROUP BY
      -- Group by hour and status
      hour,status
    ORDER BY hour ASC
    

For more information, see [`TIMESTAMP_TRUNC` documentation](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/timestamp_functions#timestamp_trunc) and [Datetime functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/datetime_functions).

### Group log entries by resource

The following query shows how to group log entries by the resource type, and then count the number of log entries in each group:
    
    
    SELECT
       -- Count the number of log entries for each resource type
       resource.type, COUNT(*) AS count
    FROM
      `PROJECT_ID.LOCATION.BUCKET_ID.LOG_VIEW_ID`
    GROUP BY resource.type
    LIMIT 100
    

### Group log entries by severity

The following query shows how to group log entries by the severity, and then count the number of log entries in each group:
    
    
    SELECT
      -- Count the number of log entries for each severity.
      severity, COUNT(*) AS count
    FROM
      `PROJECT_ID.LOCATION.BUCKET_ID.LOG_VIEW_ID`
    WHERE
      severity IS NOT NULL
    GROUP BY severity
    ORDER BY severity
    LIMIT 100
    

### Group log entries by their `log_id`

The following query shows how to group log entries by the log ID, and then count the number of log entries in each group:
    
    
    SELECT
      -- Count the number of log entries for each log ID.
      log_id, COUNT(*) AS count
    FROM
      `PROJECT_ID.LOCATION.BUCKET_ID.LOG_VIEW_ID`
    GROUP BY log_id
    ORDER BY count DESC
    LIMIT 100
    

### Compute average latency of HTTP requests per URL

The following query illustrates how to group log entries by the HTTP request URL and location, and then count the number of log entries in each group:
    
    
    SELECT
      -- Compute the average latency for each group. Because the labels field has a
      -- data type of JSON, use JSON_VALUE to get the value of checker_location.
      JSON_VALUE(labels.checker_location) AS location,
      AVG(http_request.latency.seconds) AS secs, http_request.request_url
    FROM
      `PROJECT_ID.LOCATION.BUCKET_ID.LOG_VIEW_ID`
    WHERE
      -- Matches log entries when the request_method field is GET.
      http_request IS NOT NULL AND http_request.request_method IN ('GET')
    GROUP BY
      -- Group by request URL and location
      http_request.request_url, location
    ORDER BY location
    LIMIT 100
    

### Compute average bytes sent for a subnetwork test

The following query shows how to group log entries by the location specified in the resource labels, and then compute the number of log entries in each group:
    
    
    SELECT
      -- Compute the average number of bytes sent per location. Because labels has
      -- a data type of JSON, use JSON_VALUE to get the value of the location field.
      -- bytes_sent is a string. Must cast to a FLOAT64 before computing average.
      JSON_VALUE(resource.labels.location) AS location,
      AVG(CAST(JSON_VALUE(json_payload.bytes_sent) AS FLOAT64)) AS bytes
    FROM
      `PROJECT_ID.LOCATION.BUCKET_ID.LOG_VIEW_ID`
    WHERE
      resource.type = "gce_subnetwork" AND json_payload IS NOT NULL
    GROUP BY
      -- Group by location
      location
    LIMIT 100
    

For more information, see [JSON functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/json_functions) and [Conversion functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/conversion_functions).

### Count the log entries with a field that matches a pattern

To return the substring that matches a regular expression, use the function [`REGEXP_EXTRACT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/string_functions#regexp_extract):
    
    
    SELECT
      -- Extract the value that begins with test.
      -- Count the number of log entries for each name.
      REGEXP_EXTRACT(JSON_VALUE(json_payload.jobName), r".*(test.*)$") AS name,
      COUNT(*) AS count
    FROM
      `PROJECT_ID.LOCATION.BUCKET_ID.LOG_VIEW_ID`
    WHERE
      json_payload.jobName IS NOT NULL
    GROUP BY name
    ORDER BY count
    LIMIT 20
    

For additional examples, see the [`REGEXP_EXTRACT` documentation](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/string_functions#regexp_extract).

## Cross-column search

This section describes two approaches that you can use to search multiple columns of the view that you are querying:

  * Token-based searches: You specify the search location, a search query, and then use the [`SEARCH`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/search_functions) function. Because the `SEARCH` function has specific rules on how the data is searched, we recommend that you read the [`SEARCH` documentation](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/search_functions).

  * Substring-based searches: You provide the search location, a string literal, and then use the function [`CONTAINS_SUBSTR`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/string_functions#contains_substr). The system performs a case-insensitive test to determine whether the string literal exists in an expression. The `CONTAINS_SUBSTR` function returns `TRUE` when the string literal exists and `FALSE` otherwise. The search value must be a `STRING` literal, but not the literal `NULL`.




### Token-based search on a log view

The following query retains only those rows that have a field that exactly matches "35.193.12.15":
    
    
    SELECT
      timestamp, log_id, proto_payload, severity, resource.type, resource, labels
    FROM
      `PROJECT_ID.LOCATION.BUCKET_ID.LOG_VIEW_ID` AS t
    WHERE
      -- Search data access audit logs for the IP address that matches 35.193.12.15.
      -- The use of backticks prevents the string from being tokenized.
      proto_payload IS NOT NULL AND
      log_id = "cloudaudit.googleapis.com/data_access" AND
      SEARCH(t,"`35.193.12.15`")
    ORDER BY timestamp ASC
    LIMIT 20
    

When backticks are omitted in the query string, the query string is split based on rules defined in the [`SEARCH` documentation](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/search_functions). For example, when the following statement is run, the query string is split into four tokens: "35", "193", "12", and "15":
    
    
      SEARCH(t,"35.193.12.15")
    

The previous `SEARCH` statement matches a row when a single field matches all four tokens. The order of the tokens doesn't matter.

You can include multiple `SEARCH` statements in a query. For example, in the previous query, you could replace the filter on the log ID with a statement like the following:
    
    
      SEARCH(t,"`cloudaudit.googleapis.com/data_access`")
    

The previous statement searches every field of the log entries in the log view while the original statement searches only the `log_id` field of the log entries.

To perform multiple searches on multiple fields, separate the individual strings with a space. For example, the following statement matches rows where a field contains "Hello World", "happy", and "days":
    
    
      SEARCH(t,"`Hello World` happy days")
    

Lastly, you can search specific fields instead of searching an entire table. For example, the following statement only searches the columns named `text_payload` and `json_payload`:
    
    
       SEARCH((text_payload, json_payload) ,"`35.222.132.245`")
    

For information about how the parameters of the `SEARCH` function are processed, see the BigQuery reference page [Search functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/search_functions).

### Substring search on a log view

For example, the following query fetches all Data Access audit log entries with a specific IP address whose timestamps are in a specific time range. Lastly, the query sorts the results and then displays the 20 oldest results:
    
    
    SELECT
      timestamp, log_id, proto_payload, severity, resource.type, resource, labels
    FROM
      `PROJECT_ID.LOCATION.BUCKET_ID.LOG_VIEW_ID` AS t
    WHERE
      -- Search data access audit logs for the IP address that matches 35.193.12.15.
      -- CONTAINS_SUBSTR performs a contains-test.
      proto_payload IS NOT NULL AND
      log_id = "cloudaudit.googleapis.com/data_access" AND
      CONTAINS_SUBSTR(t,"35.193.12.15")
    ORDER BY timestamp ASC
    LIMIT 20
    

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




### Join two log views by the trace ID

To combine information from two tables, use one of the [join](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#join_types) operators:
    
    
    SELECT
      -- Do an inner join on two tables by using the span ID and trace ID.
      -- Don't join only by span ID, as this field isn't globally unique.
      -- From the first view, show the timestamp, severity, and JSON payload.
      -- From the second view, show the JSON payload.
      a.timestamp, a.severity, a.json_payload, b.json_payload, a.span_id, a.trace
    FROM  `PROJECT_ID.LOCATION.BUCKET_ID.LOG_VIEW_1` a
    JOIN  `PROJECT_ID.LOCATION.BUCKET_ID.LOG_VIEW_2` b
    ON
      a.span_id = b.span_id AND
      a.trace = b.trace
    LIMIT 100
    

### Query two log views with a union statement

To combine the results of two or more `SELECT` statements and discard duplicate rows, use the [`UNION`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#union) operator. To retain duplicate rows, use the `UNION ALL` operator:
    
    
    SELECT
      timestamp, log_name, severity, json_payload, resource, labels
    -- Create a union of two log views
    FROM(
      SELECT * FROM `PROJECT_ID.LOCATION.BUCKET_ID.LOG_VIEW_1`
      UNION ALL
      SELECT * FROM `PROJECT_ID.LOCATION.BUCKET_ID.LOG_VIEW_2`
    )
    -- Sort the union by timestamp.
    ORDER BY timestamp ASC
    LIMIT 100
    

## Remove duplicate log entries

Observability Analytics doesn't remove duplicate log entries before a query is run. This behavior is different than when you query log entries by using the Logs Explorer, which removes duplicate entries by comparing the log names, timestamps, and insert ID fields.

You can use row-level validation to remove duplicate log entries.

**Note:** Queries that perform row-level validation are slower than those that don't. Don't deduplicate log entries unless the query is sensitive to duplicate log entries or the query result must not contain duplicate entries.

For more information, see [Troubleshoot: There are duplicate log entries in my Observability Analytics results](https://docs.cloud.google.com/logging/docs/analyze/troubleshoot#duplicate-analytics).

## What's next

For information about how to route and store log entries, see the following documents:

  * [Create a log bucket](https://docs.cloud.google.com/logging/docs/buckets#create_bucket)
  * [Upgrade a bucket to use Observability Analytics](https://docs.cloud.google.com/logging/docs/buckets#upgrade-bucket)
  * [Link a log bucket to a BigQuery dataset](https://docs.cloud.google.com/logging/docs/buckets#link-bq-dataset)
  * [Configure and manage sinks](https://docs.cloud.google.com/logging/docs/export/configure_export_v2)



For SQL reference documentation, see the following documents:

  * [Functions, operators, and conditionals](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators)
  * [Search functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/search_functions)
  * [Query syntax](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
