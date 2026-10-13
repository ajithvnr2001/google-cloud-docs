---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.PartitionSpec.Types.PartitionKey
title: Google Cloud Asset Inventory v1 API - Enum PartitionSpec.Types.PartitionKey (3.14.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:44:13.585185+00:00
---

# Google Cloud Asset Inventory v1 API - Enum PartitionSpec.Types.PartitionKey (3.14.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.PartitionSpec.Types.PartitionKey

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Asset Inventory v1 API - Enum PartitionSpec.Types.PartitionKey (3.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.14.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.PartitionSpec.Types.PartitionKey)
  * [ 3.13.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.13.0/Google.Cloud.Asset.V1.PartitionSpec.Types.PartitionKey)
  * [ 3.12.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.12.0/Google.Cloud.Asset.V1.PartitionSpec.Types.PartitionKey)
  * [ 3.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.11.0/Google.Cloud.Asset.V1.PartitionSpec.Types.PartitionKey)
  * [ 3.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.10.0/Google.Cloud.Asset.V1.PartitionSpec.Types.PartitionKey)
  * [ 3.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.9.0/Google.Cloud.Asset.V1.PartitionSpec.Types.PartitionKey)
  * [ 3.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.8.0/Google.Cloud.Asset.V1.PartitionSpec.Types.PartitionKey)
  * [ 3.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.7.0/Google.Cloud.Asset.V1.PartitionSpec.Types.PartitionKey)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.6.0/Google.Cloud.Asset.V1.PartitionSpec.Types.PartitionKey)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.5.0/Google.Cloud.Asset.V1.PartitionSpec.Types.PartitionKey)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.4.0/Google.Cloud.Asset.V1.PartitionSpec.Types.PartitionKey)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.3.0/Google.Cloud.Asset.V1.PartitionSpec.Types.PartitionKey)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.2.0/Google.Cloud.Asset.V1.PartitionSpec.Types.PartitionKey)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.1.0/Google.Cloud.Asset.V1.PartitionSpec.Types.PartitionKey)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.0.0/Google.Cloud.Asset.V1.PartitionSpec.Types.PartitionKey)
  * [ 2.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/2.11.0/Google.Cloud.Asset.V1.PartitionSpec.Types.PartitionKey)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/2.10.0/Google.Cloud.Asset.V1.PartitionSpec.Types.PartitionKey)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/2.9.0/Google.Cloud.Asset.V1.PartitionSpec.Types.PartitionKey)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/2.8.0/Google.Cloud.Asset.V1.PartitionSpec.Types.PartitionKey)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/2.7.0/Google.Cloud.Asset.V1.PartitionSpec.Types.PartitionKey)


    
    
    public enum PartitionSpec.Types.PartitionKey

Reference documentation and code samples for the Google Cloud Asset Inventory v1 API enum PartitionSpec.Types.PartitionKey.

This enum is used to determine the partition key column when exporting assets to BigQuery partitioned table(s). Note that, if the partition key is a timestamp column, the actual partition is based on its date value (expressed in UTC. see details in <https://cloud.google.com/bigquery/docs/partitioned-tables#date_timestamp_partitioned_tables>).

## Namespace

[Google.Cloud.Asset.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1)

## Assembly

Google.Cloud.Asset.V1.dll

## Fields   
  
---  
**Name** | **Description**  
`ReadTime` | The time when the snapshot is taken. If specified as partition key, the result table(s) is partitioned by the additional timestamp column, readTime. If [read_time] in ExportAssetsRequest is specified, the readTime column's value will be the same as it. Otherwise, its value will be the current time that is used to take the snapshot.  
`RequestTime` | The time when the request is received and started to be processed. If specified as partition key, the result table(s) is partitioned by the requestTime column, an additional timestamp column representing when the request was received.  
`Unspecified` | Unspecified partition key. If used, it means using non-partitioned table.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
