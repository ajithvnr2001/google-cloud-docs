---
url: https://docs.cloud.google.com/trace/docs/trace-export-bigquery/
title: Export to BigQuery \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:07:08.969032+00:00
---

# Export to BigQuery  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/trace-export-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Export to BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

**Caution** : As of February 18, 2026, the export of span data to BigQuery by using Cloud Trace sinks is [deprecated](https://docs.cloud.google.com/stackdriver/docs/deprecations). Sinks used to export spans to BigQuery will be removed on or after February 18, 2027. You can't create or modify trace sinks. For information about how to view your span data in BigQuery, see [Migrate to Observability Analytics](https://docs.cloud.google.com/trace/docs/analytics-migrate). 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes some attributes of the BigQuery dataset that is created when a sink exports traces from Cloud Trace to BigQuery.

## Schema

The schema for your table that stores trace data is determined by the Trace V2 API definition of [Span](https://docs.cloud.google.com/trace/docs/reference/v2/rest/v2/projects.traces/batchWrite#Span).

Trace keeps track of your table columns and patches the table when a new span contains fields that can't be stored in the existing table. A patch operation is required when an arriving span contains entries not previously seen. For example, if an arriving span contains a new [Attribute](https://docs.cloud.google.com/trace/docs/reference/v2/rest/v2/Attributes), the table is patched.

## Data retention

You configure the data retention policies of your BigQuery tables. For information about managing tables and table data, see [Working with tables](https://docs.cloud.google.com/bigquery/docs/tables-intro).

## Table type

If you configure a sink to export traces to BigQuery, Trace configures an [ingestion-time partitioned table](https://docs.cloud.google.com/bigquery/docs/creating-partitioned-tables). For detailed information on partitioned tables, including how to create, managed, query, and delete these tables, see [Working with partitioned tables](https://docs.cloud.google.com/bigquery/docs/managing-partitioned-tables).

### Sample queries

In the following queries, DATASET is the name of the BigQuery dataset, and MY_TABLE is the name of a table in that dataset.

  * To display all columns in the table for the date of November 20, 2019 while limiting the result to 10 rows, run the query:
        
        SELECT
          *
        FROM
          `DATASET.MY_TABLE`
        WHERE
          DATE(_PARTITIONTIME) = "2019-11-20" LIMIT 10

  * To display all of the partitions available in the table, run the query:
        
        SELECT
          _PARTITIONTIME as pt
        FROM
          `DATASET.MY_TABLE`
        GROUP BY 1




### HipsterShop query

HipsterShop is a demo application available on [GitHub](https://github.com/GoogleCloudPlatform/microservices-demo).

The following is a sample query that illustrates how you can use BigQuery queries to gather information that isn't readily available using the Trace interface.

The inner query finds all spans that match the specified regular expression that were received on December 2, 2019. The outer query selects for display the following:

  * name
  * number of spans that match
  * number of distinct trace IDs
  * 50th, 90th, and 99th quantiles
  * HTTP path
  * Error message



and displays the results sorted by the trace counts:
    
    
    SELECT t0.span.displayName.value, count(t0.span.spanId) as spanCount, count(distinct traceId) as traceCount,
    APPROX_QUANTILES(milliseconds, 100)[OFFSET(50)] as p50,
    APPROX_QUANTILES(milliseconds, 100)[OFFSET(95)] as p95,
    APPROX_QUANTILES(milliseconds, 100)[OFFSET(99)] as p99,
    t0.span.attributes.attributeMap._http_path,
    t0.span.attributes.attributeMap._error_message
    FROM (
    SELECT *,
    REGEXP_EXTRACT(span.name, r"./traces/([a-f0-9]+).") as traceId,
    TIMESTAMP_DIFF(span.endTime,span.startTime, MILLISECOND) as milliseconds
    FROM `hipstershop-demo.Hipstershop_trace_export.cloud_trace`
    WHERE DATE(_PARTITIONTIME) = "2019-12-02") AS t0
    WHERE t0.span.parentSpanId is NULL
    GROUP by t0.span.displayName.value, t0.span.attributes.attributeMap._http_path,t0.span.attributes.attributeMap._error_message
    ORDER BY traceCount DESC
    LIMIT 1000
     

For one particular installation of this application, the query result is as shown:

![Display the response to the previous query.](https://docs.cloud.google.com/static/trace/images/show-quantiles-12-02.png)

## View trace data

To view your trace data by using the [BigQuery interface](https://docs.cloud.google.com/bigquery/docs/bigquery-web-ui), select the table with your exported traces.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
