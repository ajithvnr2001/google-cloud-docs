---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.Simulator.SimulatorBase
title: Policy Simulator v1 API - Class Simulator.SimulatorBase (1.4.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:40.398966+00:00
---

# Policy Simulator v1 API - Class Simulator.SimulatorBase (1.4.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.Simulator.SimulatorBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Policy Simulator v1 API - Class Simulator.SimulatorBase (1.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.Simulator.SimulatorBase)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/1.3.0/Google.Cloud.PolicySimulator.V1.Simulator.SimulatorBase)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/1.2.0/Google.Cloud.PolicySimulator.V1.Simulator.SimulatorBase)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/1.1.0/Google.Cloud.PolicySimulator.V1.Simulator.SimulatorBase)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/1.0.0/Google.Cloud.PolicySimulator.V1.Simulator.SimulatorBase)


    
    
    [BindServiceMethod(typeof(Simulator), "BindService")]
    public abstract class Simulator.SimulatorBase

Reference documentation and code samples for the Policy Simulator v1 API class Simulator.SimulatorBase.

Base class for server-side implementations of Simulator

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Simulator.SimulatorBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.PolicySimulator.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1)

## Assembly

Google.Cloud.PolicySimulator.V1.dll

## Methods 

### CreateReplay(CreateReplayRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateReplay(CreateReplayRequest request, ServerCallContext context)

Creates and starts a [Replay][google.cloud.policysimulator.v1.Replay] using the given [ReplayConfig][google.cloud.policysimulator.v1.ReplayConfig].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReplayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.CreateReplayRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### GetReplay(GetReplayRequest, ServerCallContext)
    
    
    public virtual Task<Replay> GetReplay(GetReplayRequest request, ServerCallContext context)

Gets the specified [Replay][google.cloud.policysimulator.v1.Replay]. Each `Replay` is available for at least 7 days.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReplayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.GetReplayRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Replay](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.Replay)` | The response to send back to the client (wrapped by a task).  
  
### ListReplayResults(ListReplayResultsRequest, ServerCallContext)
    
    
    public virtual Task<ListReplayResultsResponse> ListReplayResults(ListReplayResultsRequest request, ServerCallContext context)

Lists the results of running a [Replay][google.cloud.policysimulator.v1.Replay].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReplayResultsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.ListReplayResultsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListReplayResultsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.ListReplayResultsResponse)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
