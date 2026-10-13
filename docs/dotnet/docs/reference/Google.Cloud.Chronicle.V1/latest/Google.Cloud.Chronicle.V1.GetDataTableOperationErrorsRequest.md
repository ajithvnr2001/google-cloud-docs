---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDataTableOperationErrorsRequest
title: Chronicle v1 API - Class GetDataTableOperationErrorsRequest (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:31.823918+00:00
---

# Chronicle v1 API - Class GetDataTableOperationErrorsRequest (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDataTableOperationErrorsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class GetDataTableOperationErrorsRequest (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class GetDataTableOperationErrorsRequest : IMessage<GetDataTableOperationErrorsRequest>, IEquatable<GetDataTableOperationErrorsRequest>, IDeepCloneable<GetDataTableOperationErrorsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Chronicle v1 API class GetDataTableOperationErrorsRequest.

The request message for GetDataTableOperationErrors.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetDataTableOperationErrorsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetDataTableOperationErrorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDataTableOperationErrorsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetDataTableOperationErrorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDataTableOperationErrorsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetDataTableOperationErrorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDataTableOperationErrorsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1)

## Assembly

Google.Cloud.Chronicle.V1.dll

## Constructors 

### GetDataTableOperationErrorsRequest()
    
    
    public GetDataTableOperationErrorsRequest()

### GetDataTableOperationErrorsRequest(GetDataTableOperationErrorsRequest)
    
    
    public GetDataTableOperationErrorsRequest(GetDataTableOperationErrorsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetDataTableOperationErrorsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDataTableOperationErrorsRequest)`  
  
  
## Properties 

### DataTableOperationErrorsName
    
    
    public DataTableOperationErrorsName DataTableOperationErrorsName { get; set; }

[DataTableOperationErrorsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableOperationErrorsName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.GetDataTableOperationErrorsRequest#Google_Cloud_Chronicle_V1_GetDataTableOperationErrorsRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[DataTableOperationErrorsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.DataTableOperationErrorsName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. Resource name for the data table operation errors. Format: projects/{project}/locations/{location}/instances/{instance}/dataTableOperationErrors/{data_table_operation_errors}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
