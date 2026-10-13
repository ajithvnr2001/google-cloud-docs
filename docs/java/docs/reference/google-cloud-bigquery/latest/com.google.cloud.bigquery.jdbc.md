---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.jdbc
title: Package com.google.cloud.bigquery.jdbc (2.65.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:58:19.691304+00:00
---

# Package com.google.cloud.bigquery.jdbc (2.65.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.jdbc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Package com.google.cloud.bigquery.jdbc (2.65.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.73.0 (latest)  2.69.0  2.68.0  2.67.0  2.65.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.2  2.56.0  2.55.3  2.54.2  2.53.0  2.52.0  2.51.0  2.50.1  2.49.0  2.48.1  2.47.0  2.46.0  2.45.0  2.44.0  2.43.3  2.42.3  2.41.0  2.40.3  2.39.1  2.38.2  2.37.2  2.36.0  2.35.0  2.34.2  2.33.2 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/google-cloud-java/google-cloud-bigquery/src/main/java/com/google/cloud/bigquery/jdbc)  
---  
  
## This package is not the recommended entry point to using this client library!

For this library, we recommend using [com.google.cloud.bigquery](https://cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery) for new applications.

## Classes

Class |  Description  
---|---  
[com.google.cloud.bigquery.jdbc.BigQueryBaseResultSet](https://cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.jdbc.BigQueryBaseResultSet) |   
[com.google.cloud.bigquery.jdbc.BigQueryConnection](https://cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.jdbc.BigQueryConnection) |  An implementation of [java.sql.Connection](https://docs.oracle.com/javase/8/docs/api/java/sql/Connection.html) for establishing a connection with BigQuery and executing SQL statements See Also: BigQueryStatement  
[com.google.cloud.bigquery.jdbc.BigQueryDriver](https://cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.jdbc.BigQueryDriver) |  JDBC Driver implementation for BigQuery. Usage:   
[com.google.cloud.bigquery.jdbc.BigQueryStatement](https://cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.jdbc.BigQueryStatement) |  An implementation of [java.sql.Statement](https://docs.oracle.com/javase/8/docs/api/java/sql/Statement.html) for executing BigQuery SQL statement and returning the results it produces. See Also: BigQueryConnection#createStatement, ResultSet  
[com.google.cloud.bigquery.jdbc.DataSource](https://cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.jdbc.DataSource) |  BigQuery JDBC implementation of [javax.sql.DataSource](https://docs.oracle.com/javase/8/docs/api/javax/sql/DataSource.html) A factory for connections to the physical data source that this DataSource object represents. An alternative to the DriverManager facility, a DataSource object is the preferred means of  
[com.google.cloud.bigquery.jdbc.PooledConnectionDataSource](https://cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.jdbc.PooledConnectionDataSource) |   
[com.google.cloud.bigquery.jdbc.PooledConnectionListener](https://cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.jdbc.PooledConnectionListener) |   
  
## Interfaces

Interface |  Description  
---|---  
[com.google.cloud.bigquery.jdbc.BigQueryResultSet](https://cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.jdbc.BigQueryResultSet) |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
