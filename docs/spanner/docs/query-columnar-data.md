---
url: https://docs.cloud.google.com/spanner/docs/query-columnar-data/
title: Query columnar data \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:29.322834+00:00
---

# Query columnar data  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/query-columnar-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Query columnar data Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This feature is available with the Spanner Enterprise edition and Enterprise Plus edition. For more information, see the [Spanner editions overview](https://docs.cloud.google.com/spanner/docs/editions-overview). 

This page describes how to run queries against columnar data.

## Query columnar data

Spanner query engine analyzes queries and automatically selects the columnar format if it is beneficial. However, several classes of queries might still need the query hint to use the columnar format. The following are examples of how to use the `@{scan_method=columnar}` query hint:

### GoogleSQL

  * `@{scan_method=columnar} SELECT COUNT(*) FROM Singers;`
  * `SELECT COUNT(*) FROM Singers @{scan_method=columnar};`
  * `@{scan_method=columnar} SELECT MsgBlob FROM Messages WHERE id='1234';`



### Postgres

  * `/*@ scan_method=columnar */ SELECT COUNT(*) FROM "Singers";`
  * `SELECT COUNT(*) FROM "Singers" /*@ scan_method=columnar*/;`
  * `/*@ scan_method=columnar */ SELECT "MsgBlob" FROM "Messages" WHERE id ='1234';`



In addition, you can disable the automatic selection of columnar explicitly by using the query hint `@{scan_method=no_columnar}`.

## Query Spanner columnar data using BigQuery federated queries

To read Spanner columnar data from BigQuery, you can either create an [external dataset](https://docs.cloud.google.com/bigquery/docs/spanner-external-datasets#create_an_external_dataset) or use the [`EXTERNAL_QUERY`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/federated_query_functions#external_query) function.

When you query external datasets, columnar data is automatically used if it's available and suitable for your query.

If you use the `EXTERNAL_QUERY` function, Spanner automatically uses the columnar data if it's available and appropriate for the workload. You can also include the `@{scan_method=columnar}` hint in the nested Spanner query.

In the following example for using the query hint:

  * The first argument to `EXTERNAL_QUERY` specifies the external connection and dataset, `my-project.us.albums`.
  * The second argument is a SQL query that selects `MarketingBudget` from the `AlbumInfo` table where `MarketingBudget` is less than 500,000.
  * The `@{scan_method=columnar}` hint optimizes the external query for columnar scanning.
  * The outer `SELECT` statement calculates the sum of the `MarketingBudget` values returned by the external query.
  * The `AS total_marketing_spend` clause assigns an alias to the calculated sum.


    
    
    SELECT SUM(MarketingBudget) AS total_marketing_spend
    FROM
      EXTERNAL_QUERY(
        'my-project.us.albums',
        '@{scan_method=columnar} SELECT AlbumInfo.MarketingBudget FROM AlbumInfo WHERE AlbumInfo.MarketingBudget < 500000;');
    

## What's next

  * Learn about [columnar engine](https://docs.cloud.google.com/spanner/docs/columnar-engine).
  * Learn how to [enable columnar engine](https://docs.cloud.google.com/spanner/docs/configure-columnar-engine).
  * Learn how to [monitor columnar engine](https://docs.cloud.google.com/spanner/docs/monitor-columnar-engine).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
