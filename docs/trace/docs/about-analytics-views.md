---
url: https://docs.cloud.google.com/trace/docs/about-analytics-views/
title: About analytics views \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:58.376256+00:00
---

# About analytics views  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/about-analytics-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



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




For information about listing the analytics views in your Google Cloud project, see [List analytics views](https://docs.cloud.google.com/trace/docs/create-and-manage-analytics-views#list).

### Location of analytics views

The location of an analytics view is determined by the location of the resources it queries. For example, if an analytics view queries a observability view that is in the `global` location, then the location of the analytics view must also be `global`. When you use the Google Cloud console to create an analytics view, the location is set automatically.

## Example use cases

The following examples illustrate how you can use analytics views to simplify and reuse queries.

### Extract trace service name

Suppose that you want to write queries that analyze your trace data, and you want to either display or group by a synthesized service name. The query for your analytics view determines the service name for a span by using the `COALESCE` function, which evaluates a list of expressions, in order, and returns the value for the first expression that doesn't evaluate to `NULL`:
    
    
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
      `PROJECT_ID.us._Trace.Spans._AllSpans`
    LIMIT 10
    

Before you use the query, replace PROJECT_ID with the ID of your Google Cloud project.

## Limitations

The following limitations apply to analytics views:

  * An analytics view can only query observability views.
  * The parent resource of an analytics view must be a Google Cloud project.
  * You can only query an analytics view by using the **Observability Analytics** page, and only when you use the **Observability Analytics (default)** query engine.
  * All views that an analytics view queries must be in the same location.
  * You must use the Google Cloud console to create or manage your analytics views.
  * You can create at most 100 analytics views per Google Cloud project.
  * You can create at most 50 analytics views per region.
  * Per Google Cloud project, at most 10 regions can contain an analytics view.



## What's next

  * [Create, query, and manage analytics views](https://docs.cloud.google.com/trace/docs/create-and-manage-analytics-views)
  * [Query and analyze traces](https://docs.cloud.google.com/trace/docs/analytics)
  * [Chart SQL query results](https://docs.cloud.google.com/trace/docs/analytics-chart)
  * [Save and share queries](https://docs.cloud.google.com/trace/docs/analytics-save-share-query)
  * [Sample SQL queries](https://docs.cloud.google.com/trace/docs/analytics-samples)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
