---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.DeleteBigQueryExportRequest
title: Security Command Center v2 API - Class DeleteBigQueryExportRequest (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:07:41.587840+00:00
---

# Security Command Center v2 API - Class DeleteBigQueryExportRequest (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.DeleteBigQueryExportRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Security Command Center v2 API - Class DeleteBigQueryExportRequest (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class DeleteBigQueryExportRequest : IMessage<DeleteBigQueryExportRequest>, IEquatable<DeleteBigQueryExportRequest>, IDeepCloneable<DeleteBigQueryExportRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Security Command Center v2 API class DeleteBigQueryExportRequest.

Request message for deleting a BigQuery export.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteBigQueryExportRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.DeleteBigQueryExportRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.DeleteBigQueryExportRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.DeleteBigQueryExportRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecurityCenter.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2)

## Assembly

Google.Cloud.SecurityCenter.V2.dll

## Constructors 

### DeleteBigQueryExportRequest()
    
    
    public DeleteBigQueryExportRequest()

### DeleteBigQueryExportRequest(DeleteBigQueryExportRequest)
    
    
    public DeleteBigQueryExportRequest(DeleteBigQueryExportRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteBigQueryExportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.DeleteBigQueryExportRequest)`  
  
  
## Properties 

### BigQueryExportName
    
    
    public BigQueryExportName BigQueryExportName { get; set; }

[BigQueryExportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.BigQueryExportName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.DeleteBigQueryExportRequest#Google_Cloud_SecurityCenter_V2_DeleteBigQueryExportRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[BigQueryExportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V2/latest/Google.Cloud.SecurityCenter.V2.BigQueryExportName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The name of the BigQuery export to delete. The following list shows some examples of the format:

\+ `organizations/{organization}/locations/{location}/bigQueryExports/{export_id}`

  * `folders/{folder}/locations/{location}/bigQueryExports/{export_id}`
  * `projects/{project}/locations/{location}/bigQueryExports/{export_id}`



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
