---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.CreateModelRequest
title: Financial Services v1 API - Class CreateModelRequest (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:48:18.717446+00:00
---

# Financial Services v1 API - Class CreateModelRequest (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.CreateModelRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Financial Services v1 API - Class CreateModelRequest (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta02 
    
    
    public sealed class CreateModelRequest : IMessage<CreateModelRequest>, IEquatable<CreateModelRequest>, IDeepCloneable<CreateModelRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Financial Services v1 API class CreateModelRequest.

Request for creating a Model resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateModelRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.CreateModelRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.CreateModelRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.CreateModelRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.FinancialServices.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1)

## Assembly

Google.Cloud.FinancialServices.V1.dll

## Constructors 

### CreateModelRequest()
    
    
    public CreateModelRequest()

### CreateModelRequest(CreateModelRequest)
    
    
    public CreateModelRequest(CreateModelRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.CreateModelRequest)`  
  
  
## Properties 

### Model
    
    
    public Model Model { get; set; }

Required. The Model that will be created.

**Property Value**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.Model)` |   
  
### ModelId
    
    
    public string ModelId { get; set; }

Required. The resource id of the Model

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The parent of the Model is the Instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsInstanceName
    
    
    public InstanceName ParentAsInstanceName { get; set; }

[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.InstanceName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.CreateModelRequest#Google_Cloud_FinancialServices_V1_CreateModelRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.FinancialServices.V1/latest/Google.Cloud.FinancialServices.V1.InstanceName)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
