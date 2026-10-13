---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.PromoteClusterStatus.Types.State
title: AlloyDB v1beta API - Enum PromoteClusterStatus.Types.State (1.0.0-beta19) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:40.668914+00:00
---

# AlloyDB v1beta API - Enum PromoteClusterStatus.Types.State (1.0.0-beta19)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.PromoteClusterStatus.Types.State

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  AlloyDB v1beta API - Enum PromoteClusterStatus.Types.State (1.0.0-beta19) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta19 (latest)  1.0.0-beta18 
    
    
    public enum PromoteClusterStatus.Types.State

Reference documentation and code samples for the AlloyDB v1beta API enum PromoteClusterStatus.Types.State.

State contains all valid states of the database during promote cluster operation. This is used for status reporting through the LRO metadata.

## Namespace

[Google.Cloud.AlloyDb.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta)

## Assembly

Google.Cloud.AlloyDb.V1Beta.dll

## Fields   
  
---  
**Name** | **Description**  
`PromoteClusterAvailableForRead` | The database is only available for read.  
`PromoteClusterAvailableForWrite` | The database is available for both read and write. The promote operation is near completion.  
`PromoteClusterCompleted` | The promote operation is completed and the database is available for write.  
`Unspecified` | The state of the database is unknown.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
