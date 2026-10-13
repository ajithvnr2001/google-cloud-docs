---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination
title: Google Cloud Asset Inventory v1 API - Class IamPolicyAnalysisOutputConfig.Types.BigQueryDestination (3.14.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:44:06.438867+00:00
---

# Google Cloud Asset Inventory v1 API - Class IamPolicyAnalysisOutputConfig.Types.BigQueryDestination (3.14.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Asset Inventory v1 API - Class IamPolicyAnalysisOutputConfig.Types.BigQueryDestination (3.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.14.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination)
  * [ 3.13.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.13.0/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination)
  * [ 3.12.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.12.0/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination)
  * [ 3.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.11.0/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination)
  * [ 3.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.10.0/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination)
  * [ 3.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.9.0/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination)
  * [ 3.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.8.0/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination)
  * [ 3.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.7.0/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.6.0/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.5.0/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.4.0/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.3.0/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.2.0/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.1.0/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/3.0.0/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination)
  * [ 2.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/2.11.0/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/2.10.0/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/2.9.0/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/2.8.0/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/2.7.0/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination)


    
    
    public sealed class IamPolicyAnalysisOutputConfig.Types.BigQueryDestination : IMessage<IamPolicyAnalysisOutputConfig.Types.BigQueryDestination>, IEquatable<IamPolicyAnalysisOutputConfig.Types.BigQueryDestination>, IDeepCloneable<IamPolicyAnalysisOutputConfig.Types.BigQueryDestination>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Asset Inventory v1 API class IamPolicyAnalysisOutputConfig.Types.BigQueryDestination.

A BigQuery destination.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > IamPolicyAnalysisOutputConfig.Types.BigQueryDestination

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[IamPolicyAnalysisOutputConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types)[BigQueryDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[IamPolicyAnalysisOutputConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types)[BigQueryDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[IamPolicyAnalysisOutputConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types)[BigQueryDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Asset.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1)

## Assembly

Google.Cloud.Asset.V1.dll

## Constructors 

### BigQueryDestination()
    
    
    public BigQueryDestination()

### BigQueryDestination(BigQueryDestination)
    
    
    public BigQueryDestination(IamPolicyAnalysisOutputConfig.Types.BigQueryDestination other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[IamPolicyAnalysisOutputConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types)[BigQueryDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination)`  
  
  
## Properties 

### Dataset
    
    
    public string Dataset { get; set; }

Required. The BigQuery dataset in format "projects/projectId/datasets/datasetId", to which the analysis results should be exported. If this dataset does not exist, the export call will return an INVALID_ARGUMENT error.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PartitionKey
    
    
    public IamPolicyAnalysisOutputConfig.Types.BigQueryDestination.Types.PartitionKey PartitionKey { get; set; }

The partition key for BigQuery partitioned table.

**Property Value**  
---  
**Type** | **Description**  
`[IamPolicyAnalysisOutputConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types)[BigQueryDestination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination.Types)[PartitionKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Asset.V1/latest/Google.Cloud.Asset.V1.IamPolicyAnalysisOutputConfig.Types.BigQueryDestination.Types.PartitionKey)` |   
  
### TablePrefix
    
    
    public string TablePrefix { get; set; }

Required. The prefix of the BigQuery tables to which the analysis results will be written. Tables will be created based on this table_prefix if not exist:

  * <table_prefix>_analysis table will contain export operation's metadata.
  * <table_prefix>_analysis_result will contain all the [IamPolicyAnalysisResult][google.cloud.asset.v1.IamPolicyAnalysisResult]. When [partition_key] is specified, both tables will be partitioned based on the [partition_key].



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### WriteDisposition
    
    
    public string WriteDisposition { get; set; }

Optional. Specifies the action that occurs if the destination table or partition already exists. The following values are supported:

  * WRITE_TRUNCATE: If the table or partition already exists, BigQuery overwrites the entire table or all the partitions data.
  * WRITE_APPEND: If the table or partition already exists, BigQuery appends the data to the table or the latest partition.
  * WRITE_EMPTY: If the table already exists and contains data, an error is returned.



The default value is WRITE_APPEND. Each action is atomic and only occurs if BigQuery is able to complete the job successfully. Details are at <https://cloud.google.com/bigquery/docs/loading-data-local#appending_to_or_overwriting_a_table_using_a_local_file>.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
