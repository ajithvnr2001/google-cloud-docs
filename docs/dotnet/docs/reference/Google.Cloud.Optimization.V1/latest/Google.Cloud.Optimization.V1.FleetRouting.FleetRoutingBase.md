---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.FleetRouting.FleetRoutingBase
title: Cloud Optimization v1 API - Class FleetRouting.FleetRoutingBase (2.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:35:21.657135+00:00
---

# Cloud Optimization v1 API - Class FleetRouting.FleetRoutingBase (2.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.FleetRouting.FleetRoutingBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Optimization v1 API - Class FleetRouting.FleetRoutingBase (2.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.7.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.FleetRouting.FleetRoutingBase)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.6.0/Google.Cloud.Optimization.V1.FleetRouting.FleetRoutingBase)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.5.0/Google.Cloud.Optimization.V1.FleetRouting.FleetRoutingBase)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.4.0/Google.Cloud.Optimization.V1.FleetRouting.FleetRoutingBase)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.3.0/Google.Cloud.Optimization.V1.FleetRouting.FleetRoutingBase)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.2.0/Google.Cloud.Optimization.V1.FleetRouting.FleetRoutingBase)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.1.0/Google.Cloud.Optimization.V1.FleetRouting.FleetRoutingBase)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/2.0.0/Google.Cloud.Optimization.V1.FleetRouting.FleetRoutingBase)
  * [ 1.0.0-beta01 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/1.0.0-beta01/Google.Cloud.Optimization.V1.FleetRouting.FleetRoutingBase)


    
    
    [BindServiceMethod(typeof(FleetRouting), "BindService")]
    public abstract class FleetRouting.FleetRoutingBase

Reference documentation and code samples for the Cloud Optimization v1 API class FleetRouting.FleetRoutingBase.

Base class for server-side implementations of FleetRouting

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > FleetRouting.FleetRoutingBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Optimization.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1)

## Assembly

Google.Cloud.Optimization.V1.dll

## Methods 

### BatchOptimizeTours(BatchOptimizeToursRequest, ServerCallContext)
    
    
    public virtual Task<Operation> BatchOptimizeTours(BatchOptimizeToursRequest request, ServerCallContext context)

Optimizes vehicle tours for one or more `OptimizeToursRequest` messages as a batch.

This method is a Long Running Operation (LRO). The inputs for optimization (`OptimizeToursRequest` messages) and outputs (`OptimizeToursResponse` messages) are read/written from/to Cloud Storage in user-specified format. Like the `OptimizeTours` method, each `OptimizeToursRequest` contains a `ShipmentModel` and returns an `OptimizeToursResponse` containing `ShipmentRoute`s, which are a set of routes to be performed by vehicles minimizing the overall cost.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchOptimizeToursRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.BatchOptimizeToursRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### OptimizeTours(OptimizeToursRequest, ServerCallContext)
    
    
    public virtual Task<OptimizeToursResponse> OptimizeTours(OptimizeToursRequest request, ServerCallContext context)

Sends an `OptimizeToursRequest` containing a `ShipmentModel` and returns an `OptimizeToursResponse` containing `ShipmentRoute`s, which are a set of routes to be performed by vehicles minimizing the overall cost.

A `ShipmentModel` model consists mainly of `Shipment`s that need to be carried out and `Vehicle`s that can be used to transport the `Shipment`s. The `ShipmentRoute`s assign `Shipment`s to `Vehicle`s. More specifically, they assign a series of `Visit`s to each vehicle, where a `Visit` corresponds to a `VisitRequest`, which is a pickup or delivery for a `Shipment`.

The goal is to provide an assignment of `ShipmentRoute`s to `Vehicle`s that minimizes the total cost where cost has many components defined in the `ShipmentModel`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[OptimizeToursRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.OptimizeToursRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[OptimizeToursResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Optimization.V1/latest/Google.Cloud.Optimization.V1.OptimizeToursResponse)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
