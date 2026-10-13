---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.BigQueryDestination.Types.PartitionKey
title: Capacity Planner v1beta API - Enum BigQueryDestination.Types.PartitionKey (1.0.0-beta02) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:21:20.239654+00:00
---

# Capacity Planner v1beta API - Enum BigQueryDestination.Types.PartitionKey (1.0.0-beta02)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.BigQueryDestination.Types.PartitionKey

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Capacity Planner v1beta API - Enum BigQueryDestination.Types.PartitionKey (1.0.0-beta02) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta02 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta.BigQueryDestination.Types.PartitionKey)
  * [ 1.0.0-beta01 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/1.0.0-beta01/Google.Cloud.CapacityPlanner.V1Beta.BigQueryDestination.Types.PartitionKey)


    
    
    public enum BigQueryDestination.Types.PartitionKey

Reference documentation and code samples for the Capacity Planner v1beta API enum BigQueryDestination.Types.PartitionKey.

This enum determines the partition key column for the BigQuery tables. Partitioning can improve query performance and reduce query cost by filtering partitions. Refer to <https://cloud.google.com/bigquery/docs/partitioned-tables> for details.

## Namespace

[Google.Cloud.CapacityPlanner.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CapacityPlanner.V1Beta/latest/Google.Cloud.CapacityPlanner.V1Beta)

## Assembly

Google.Cloud.CapacityPlanner.V1Beta.dll

## Fields   
  
---  
**Name** | **Description**  
`RequestTime` | The time when the request is received. If specified as partition key, the result table(s) is partitioned by the RequestTime column, an additional timestamp column representing when the request was received.  
`Unspecified` | Unspecified partition key. Tables won't be partitioned using this option.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
