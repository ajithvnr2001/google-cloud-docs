---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1.DatasetUpdateResponse
title: BigQuery Audit Data Logging v1 API - Class DatasetUpdateResponse (1.4.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:12:55.258929+00:00
---

# BigQuery Audit Data Logging v1 API - Class DatasetUpdateResponse (1.4.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1.DatasetUpdateResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  BigQuery Audit Data Logging v1 API - Class DatasetUpdateResponse (1.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1.DatasetUpdateResponse)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/1.3.0/Google.Cloud.BigQuery.Logging.V1.DatasetUpdateResponse)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/1.2.0/Google.Cloud.BigQuery.Logging.V1.DatasetUpdateResponse)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/1.1.0/Google.Cloud.BigQuery.Logging.V1.DatasetUpdateResponse)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/1.0.0/Google.Cloud.BigQuery.Logging.V1.DatasetUpdateResponse)


    
    
    public sealed class DatasetUpdateResponse : IMessage<DatasetUpdateResponse>, IEquatable<DatasetUpdateResponse>, IDeepCloneable<DatasetUpdateResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the BigQuery Audit Data Logging v1 API class DatasetUpdateResponse.

Dataset update response.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DatasetUpdateResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DatasetUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1.DatasetUpdateResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DatasetUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1.DatasetUpdateResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DatasetUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1.DatasetUpdateResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BigQuery.Logging.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1)

## Assembly

Google.Cloud.BigQuery.Logging.V1.dll

## Constructors 

### DatasetUpdateResponse()
    
    
    public DatasetUpdateResponse()

### DatasetUpdateResponse(DatasetUpdateResponse)
    
    
    public DatasetUpdateResponse(DatasetUpdateResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DatasetUpdateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1.DatasetUpdateResponse)`  
  
  
## Properties 

### Resource
    
    
    public Dataset Resource { get; set; }

Final state of the updated dataset.

**Property Value**  
---  
**Type** | **Description**  
`[Dataset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.Logging.V1/latest/Google.Cloud.BigQuery.Logging.V1.Dataset)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
