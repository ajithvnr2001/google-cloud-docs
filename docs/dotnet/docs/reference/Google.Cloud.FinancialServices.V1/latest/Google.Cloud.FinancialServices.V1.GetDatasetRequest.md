---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.GetDatasetRequest
title: Financial Services v1 API - Class GetDatasetRequest (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:22.622402+00:00
---

# Financial Services v1 API - Class GetDatasetRequest (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.GetDatasetRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Financial Services v1 API - Class GetDatasetRequest (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta02 
    
    
    public sealed class GetDatasetRequest : IMessage<GetDatasetRequest>, IEquatable<GetDatasetRequest>, IDeepCloneable<GetDatasetRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Financial Services v1 API class GetDatasetRequest.

Request for retrieving a specific Dataset resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetDatasetRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetDatasetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.GetDatasetRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetDatasetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.GetDatasetRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetDatasetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.GetDatasetRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.FinancialServices.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1)

## Assembly

Google.Cloud.FinancialServices.V1.dll

## Constructors 

### GetDatasetRequest()
    
    
    public GetDatasetRequest()

### GetDatasetRequest(GetDatasetRequest)
    
    
    public GetDatasetRequest(GetDatasetRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetDatasetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.GetDatasetRequest)`  
  
  
## Properties 

### DatasetName
    
    
    public DatasetName DatasetName { get; set; }

[DatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.DatasetName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.GetDatasetRequest#Google_Cloud_FinancialServices_V1_GetDatasetRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[DatasetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.DatasetName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The resource name of the Dataset

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
