---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkCreateDataTableRowsRequest
title: Chronicle v1 API - Class BulkCreateDataTableRowsRequest (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:06:42.622485+00:00
---

# Chronicle v1 API - Class BulkCreateDataTableRowsRequest (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkCreateDataTableRowsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class BulkCreateDataTableRowsRequest (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class BulkCreateDataTableRowsRequest : IMessage<BulkCreateDataTableRowsRequest>, IEquatable<BulkCreateDataTableRowsRequest>, IDeepCloneable<BulkCreateDataTableRowsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Chronicle v1 API class BulkCreateDataTableRowsRequest.

Request to create data table rows in bulk.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BulkCreateDataTableRowsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BulkCreateDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkCreateDataTableRowsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BulkCreateDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkCreateDataTableRowsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BulkCreateDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkCreateDataTableRowsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1)

## Assembly

Google.Cloud.Chronicle.V1.dll

## Constructors 

### BulkCreateDataTableRowsRequest()
    
    
    public BulkCreateDataTableRowsRequest()

### BulkCreateDataTableRowsRequest(BulkCreateDataTableRowsRequest)
    
    
    public BulkCreateDataTableRowsRequest(BulkCreateDataTableRowsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BulkCreateDataTableRowsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkCreateDataTableRowsRequest)`  
  
  
## Properties 

### Parent
    
    
    public string Parent { get; set; }

Required. The resource id of the data table. Format: /projects/{project}/locations/{location}/instances/{instance}/dataTables/{data_table}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsDataTableName
    
    
    public DataTableName ParentAsDataTableName { get; set; }

[DataTableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.BulkCreateDataTableRowsRequest#Google_Cloud_Chronicle_V1_BulkCreateDataTableRowsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[DataTableName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableName)` |   
  
### Requests
    
    
    public RepeatedField<CreateDataTableRowRequest> Requests { get; }

Required. Data table rows to create. A maximum of 1000 rows (for sync requests) or 2000 rows (for async requests) can be created in a single request. Total size of the rows should be less than 4MB.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[CreateDataTableRowRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.CreateDataTableRowRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
