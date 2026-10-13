---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1.CloudProductRegistryReadService.CloudProductRegistryReadServiceBase
title: Cloud Product Registry v1 API - Class CloudProductRegistryReadService.CloudProductRegistryReadServiceBase (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:03.266618+00:00
---

# Cloud Product Registry v1 API - Class CloudProductRegistryReadService.CloudProductRegistryReadServiceBase (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1.CloudProductRegistryReadService.CloudProductRegistryReadServiceBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Product Registry v1 API - Class CloudProductRegistryReadService.CloudProductRegistryReadServiceBase (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    [BindServiceMethod(typeof(CloudProductRegistryReadService), "BindService")]
    public abstract class CloudProductRegistryReadService.CloudProductRegistryReadServiceBase

Reference documentation and code samples for the Cloud Product Registry v1 API class CloudProductRegistryReadService.CloudProductRegistryReadServiceBase.

Base class for server-side implementations of CloudProductRegistryReadService

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CloudProductRegistryReadService.CloudProductRegistryReadServiceBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ProductRegistry.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1)

## Assembly

Google.Cloud.ProductRegistry.V1.dll

## Methods 

### GetLogicalProduct(GetLogicalProductRequest, ServerCallContext)
    
    
    public virtual Task<LogicalProduct> GetLogicalProduct(GetLogicalProductRequest request, ServerCallContext context)

Gets details of a LogicalProduct.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetLogicalProductRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1.GetLogicalProductRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LogicalProduct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1.LogicalProduct)` | The response to send back to the client (wrapped by a task).  
  
### GetLogicalProductVariant(GetLogicalProductVariantRequest, ServerCallContext)
    
    
    public virtual Task<LogicalProductVariant> GetLogicalProductVariant(GetLogicalProductVariantRequest request, ServerCallContext context)

Get details of a LogicalProductVariant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetLogicalProductVariantRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1.GetLogicalProductVariantRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LogicalProductVariant](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1.LogicalProductVariant)` | The response to send back to the client (wrapped by a task).  
  
### GetProductSuite(GetProductSuiteRequest, ServerCallContext)
    
    
    public virtual Task<ProductSuite> GetProductSuite(GetProductSuiteRequest request, ServerCallContext context)

Get details of a ProductSuite.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProductSuiteRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1.GetProductSuiteRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ProductSuite](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1.ProductSuite)` | The response to send back to the client (wrapped by a task).  
  
### ListLogicalProductVariants(ListLogicalProductVariantsRequest, ServerCallContext)
    
    
    public virtual Task<ListLogicalProductVariantsResponse> ListLogicalProductVariants(ListLogicalProductVariantsRequest request, ServerCallContext context)

Lists LogicalProductVariants matching given criteria.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListLogicalProductVariantsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1.ListLogicalProductVariantsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListLogicalProductVariantsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1.ListLogicalProductVariantsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListLogicalProducts(ListLogicalProductsRequest, ServerCallContext)
    
    
    public virtual Task<ListLogicalProductsResponse> ListLogicalProducts(ListLogicalProductsRequest request, ServerCallContext context)

Lists LogicalProducts matching given criteria.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListLogicalProductsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1.ListLogicalProductsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListLogicalProductsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1.ListLogicalProductsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListProductSuites(ListProductSuitesRequest, ServerCallContext)
    
    
    public virtual Task<ListProductSuitesResponse> ListProductSuites(ListProductSuitesRequest request, ServerCallContext context)

Lists ProductSuites.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProductSuitesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1.ListProductSuitesRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListProductSuitesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1.ListProductSuitesResponse)` | The response to send back to the client (wrapped by a task).  
  
### LookupEntity(LookupEntityRequest, ServerCallContext)
    
    
    public virtual Task<LookupEntityResponse> LookupEntity(LookupEntityRequest request, ServerCallContext context)

Look up entities.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupEntityRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1.LookupEntityRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[LookupEntityResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ProductRegistry.V1/latest/Google.Cloud.ProductRegistry.V1.LookupEntityResponse)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
