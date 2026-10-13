---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection
title: Package com.google.cloud.spanner.connection (2.46.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:40:28.677282+00:00
---

# Package com.google.cloud.spanner.connection (2.46.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Package com.google.cloud.spanner.connection (2.46.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.46.0 (latest)  2.42.0  2.41.0  2.40.0  2.38.0  2.35.4  2.34.0  2.33.2  2.32.3  2.31.2  2.30.4  2.28.0  2.27.1  2.26.1  2.25.1  2.24.1  2.23.0  2.22.1  2.21.0  2.20.2  2.19.3  2.18.1  2.17.0  2.16.1  2.15.5  2.14.6  2.13.4  2.11.4  2.10.0  2.9.16  2.8.0  2.7.12  2.6.4  2.5.11 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/google-cloud-java/google-cloud-spanner-jdbc/src/main/java/com/google/cloud/spanner/connection)  
---  
  
## This package is not the recommended entry point to using this client library!

For this library, we recommend using [com.google.cloud.spanner.jdbc](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.jdbc) for new applications.

## Classes

Class |  Description  
---|---  
[com.google.cloud.spanner.connection.AbstractStatementParser](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.AbstractStatementParser) |   
[com.google.cloud.spanner.connection.AbstractStatementParser.ParametersInfo](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.AbstractStatementParser.ParametersInfo) |   
[com.google.cloud.spanner.connection.AbstractStatementParser.ParsedStatement](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.AbstractStatementParser.ParsedStatement) |   
[com.google.cloud.spanner.connection.Connection.InternalMetadataQuery](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.Connection.InternalMetadataQuery) |   
[com.google.cloud.spanner.connection.ConnectionOptions](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.ConnectionOptions) |   
[com.google.cloud.spanner.connection.ConnectionOptions.Builder](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.ConnectionOptions.Builder) |   
[com.google.cloud.spanner.connection.ConnectionOptionsHelper](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.ConnectionOptionsHelper) |   
[com.google.cloud.spanner.connection.ConnectionProperties](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.ConnectionProperties) |   
[com.google.cloud.spanner.connection.ConnectionProperty](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.ConnectionProperty) |   
[com.google.cloud.spanner.connection.DirectedReadOptionsUtil](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.DirectedReadOptionsUtil) |   
[com.google.cloud.spanner.connection.PartitionId](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.PartitionId) |   
[com.google.cloud.spanner.connection.PostgreSQLStatementParser](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.PostgreSQLStatementParser) |   
[com.google.cloud.spanner.connection.ReadOnlyStalenessUtil](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.ReadOnlyStalenessUtil) |   
[com.google.cloud.spanner.connection.SpannerPool](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.SpannerPool) |   
[com.google.cloud.spanner.connection.SpannerStatementParser](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.SpannerStatementParser) |   
[com.google.cloud.spanner.connection.TransactionRetryListenerImpl](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.TransactionRetryListenerImpl) |   
  
## Interfaces

Interface |  Description  
---|---  
[com.google.cloud.spanner.connection.AsyncStatementResult](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.AsyncStatementResult) |   
[com.google.cloud.spanner.connection.Connection](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.Connection) |   
[com.google.cloud.spanner.connection.Connection.TransactionCallable](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.Connection.TransactionCallable) |   
[com.google.cloud.spanner.connection.ConnectionOptions.ExternalChannelProvider](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.ConnectionOptions.ExternalChannelProvider) |   
[com.google.cloud.spanner.connection.PartitionedQueryResultSet](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.PartitionedQueryResultSet) |   
[com.google.cloud.spanner.connection.StatementResult](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.StatementResult) |   
[com.google.cloud.spanner.connection.TransactionRetryListener](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.TransactionRetryListener) |   
  
## Enums

Enum |  Description  
---|---  
[com.google.cloud.spanner.connection.AbstractStatementParser.StatementType](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.AbstractStatementParser.StatementType) |   
[com.google.cloud.spanner.connection.AutocommitDmlMode](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.AutocommitDmlMode) |   
[com.google.cloud.spanner.connection.ConnectionProperty.Context](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.ConnectionProperty.Context) |   
[com.google.cloud.spanner.connection.DdlInTransactionMode](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.DdlInTransactionMode) |   
[com.google.cloud.spanner.connection.SavepointSupport](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.SavepointSupport) |   
[com.google.cloud.spanner.connection.StatementResult.ClientSideStatementType](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.StatementResult.ClientSideStatementType) |   
[com.google.cloud.spanner.connection.StatementResult.ResultType](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.StatementResult.ResultType) |   
[com.google.cloud.spanner.connection.TransactionMode](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.TransactionMode) |   
[com.google.cloud.spanner.connection.TransactionRetryListener.RetryResult](https://cloud.google.com/java/docs/reference/google-cloud-spanner-jdbc/latest/com.google.cloud.spanner.connection.TransactionRetryListener.RetryResult) |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
