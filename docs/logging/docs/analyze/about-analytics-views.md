---
url: https://docs.cloud.google.com/logging/docs/analyze/about-analytics-views/
title: About analytics views \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:12.562590+00:00
---

# About analytics views  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/analyze/about-analytics-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  About analytics views Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Analytics views in Observability Analytics let you define a SQL query with a custom schema over your observability data so that you can simplify and reuse complex transformations. Whereas you can only rerun a saved query, you can reference an analytics view as a data source in the `FROM` clause of other SQL queries.

## Overview

An _analytics view_ is a resource you can query. That is, after you define an analytics view, you can write queries where you specify your analytics view in the `FROM` clause.

The primary benefit of using analytics views is that you aren't constrained to querying the data in the format an API or system defines. An analytics view lets you define a schema, which lets you simplify your queries or reduce the time you spend writing queries. The query in an analytics view can do things like retain only specific fields, rename fields, move nested fields to a top-level column, and perform grouping and aggregation.

Analytics views aren't [materialized views](https://docs.cloud.google.com/bigquery/docs/materialized-views-intro). An analytics view isn't a precomputed view that periodically caches query results. Therefore, querying an analytics view is equivalent to querying the views that are listed in the analytics view's query.

Analytics views are more powerful than saved queries, which are queries that you run on the **Observability Analytics** page and then save. You can rerun a saved query, but you can't query the results of a saved query.

### Types of analytics views

There are two types of analytics views: user-defined and system-defined:

  * _User-defined analytics views_ are any analytics views that you create. You can query, edit, and delete user-defined analytics views.

  * _System-defined analytics views_ are analytics views created by Google Cloud services. You can query system-defined analytics views. However, you can't edit or delete them.




For information about listing the analytics views in your Google Cloud project, see [List analytics views](https://docs.cloud.google.com/logging/docs/analyze/create-and-manage-analytics-views#list).

### Location of analytics views

The location of an analytics view is determined by the location of the resources it queries. For example, if an analytics view queries a log view that is in the `global` location, then the location of the analytics view must also be `global`. When you use the Google Cloud console to create an analytics view, the location is set automatically.

## Example use cases

The following examples illustrate how you can use analytics views to simplify and reuse queries.

### Query for network details

You want to analyze network performance by using VPC Flow Logs. You need to analyze the overall networking performance and identify specific networks, IP addresses, and hosts. This information is stored within nested fields in the `json_payload` field of a log entry.

To simplify your analysis queries, you create the following analytics view and name it `network_details`:
    
    
    SELECT
      -- Create a column for each network field.
      JSON_VALUE(resource.labels.subnetwork_name) subnetwork_name,
      JSON_VALUE(json_payload.src_instance.vm_name) vm_name,
      JSON_VALUE(json_payload.connection.src_ip) as src_ip,
      JSON_VALUE(json_payload.connection.src_port) as src_port,
      JSON_VALUE(json_payload.connection.dest_ip) as dest_ip,
      JSON_VALUE(json_payload.connection.dest_port) as dest_port,
      CAST(JSON_VALUE(json_payload.bytes_sent) as INT64) as bytes_sent,
      CAST(JSON_VALUE(json_payload.packets_sent) as INT64) as packets_sent
    FROM
      -- Query one log view.
      `PROJECT_ID.LOCATION.BUCKET_ID.LOG_VIEW_ID`
    WHERE
      -- Only query the VPC Flow Logs log.
      log_id = "compute.googleapis.com/vpc_flows"
      AND SEARCH(json_payload.reporter, "SRC")
    

Before you use the query, set the values of the following variables:

  * PROJECT_ID: The identifier of the project.
  * LOCATION: The location of the log view.
  * BUCKET_ID: The name or ID of the log bucket.
  * LOG_VIEW_ID: The identifier of the log view, which is limited to 100 characters and can include only letters, digits, underscores, and hyphens.



When you want to analyze the network performance, you query your analytics view. For example, if you are only interested in the name of the instance and the amount of data sent, then you might write the following query:
    
    
    SELECT vm_name, bytes_sent, packets_sent,
    FROM `analytics_view.my_project.global.network_details`
    ORDER BY bytes_sent DESC
    LIMIT 100
    

### Base query for API latency analysis

Several teams need weekly performance data to complete their analysis. Instead of each team generating the weekly data, you create an analytics view that extracts the weekly data. Other teams can query the analytics view and then perform their analysis.

The following query illustrates how to use SQL to compute the minimum, maximum, and average request latency:
    
    
    SELECT week, MIN(took_ms) as min, MAX(took_ms) AS max, AVG(took_ms) AS avg
    FROM (
      SELECT TIMESTAMP_TRUNC(timestamp, WEEK) AS week,
      CAST( JSON_VALUE(json_payload, '$."http.resp.took_ms"') AS INT64) as took_ms
      FROM
        -- Query one log view.
        `PROJECT_ID.LOCATION.BUCKET_ID.LOG_VIEW_ID`
      WHERE json_payload IS NOT NULL
        AND SEARCH(labels,"frontend")
        AND JSON_VALUE(json_payload.message) = "request complete"
      ORDER BY took_ms DESC, timestamp ASC
    )
    GROUP BY week ORDER BY week
    

## Limitations

The following limitations apply to analytics views:

  * An analytics view can only query log views.
  * The parent resource of an analytics view must be a Google Cloud project.
  * You can only query an analytics view by using the **Observability Analytics** page, and only when you use the **Observability Analytics (default)** query engine.
  * All views that an analytics view queries must be in the same location.
  * You must use the Google Cloud console to create or manage your analytics views.
  * You can create at most 100 analytics views per Google Cloud project.
  * You can create at most 50 analytics views per region.
  * Per Google Cloud project, at most 10 regions can contain an analytics view.



## What's next

  * [Create, query, and manage analytics views](https://docs.cloud.google.com/logging/docs/analyze/create-and-manage-analytics-views)
  * [Query and analyze logs overview](https://docs.cloud.google.com/logging/docs/log-analytics)
  * [Save and share a SQL query](https://docs.cloud.google.com/logging/docs/analyze/save-share-query)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
