---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.CreateReplayRequest
title: Policy Simulator v1 API - Class CreateReplayRequest (1.4.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:21:58.280722+00:00
---

# Policy Simulator v1 API - Class CreateReplayRequest (1.4.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.CreateReplayRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Policy Simulator v1 API - Class CreateReplayRequest (1.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.CreateReplayRequest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/1.3.0/Google.Cloud.PolicySimulator.V1.CreateReplayRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/1.2.0/Google.Cloud.PolicySimulator.V1.CreateReplayRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/1.1.0/Google.Cloud.PolicySimulator.V1.CreateReplayRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/1.0.0/Google.Cloud.PolicySimulator.V1.CreateReplayRequest)


    
    
    public sealed class CreateReplayRequest : IMessage<CreateReplayRequest>, IEquatable<CreateReplayRequest>, IDeepCloneable<CreateReplayRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Policy Simulator v1 API class CreateReplayRequest.

Request message for [Simulator.CreateReplay][google.cloud.policysimulator.v1.Simulator.CreateReplay].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateReplayRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateReplayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.CreateReplayRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateReplayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.CreateReplayRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateReplayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.CreateReplayRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.PolicySimulator.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1)

## Assembly

Google.Cloud.PolicySimulator.V1.dll

## Constructors 

### CreateReplayRequest()
    
    
    public CreateReplayRequest()

### CreateReplayRequest(CreateReplayRequest)
    
    
    public CreateReplayRequest(CreateReplayRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateReplayRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.CreateReplayRequest)`  
  
  
## Properties 

### Parent
    
    
    public string Parent { get; set; }

Required. The parent resource where this [Replay][google.cloud.policysimulator.v1.Replay] will be created. This resource must be a project, folder, or organization with a location.

Example: `projects/my-example-project/locations/global`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Replay
    
    
    public Replay Replay { get; set; }

Required. The [Replay][google.cloud.policysimulator.v1.Replay] to create. Set `Replay.ReplayConfig` to configure the replay.

**Property Value**  
---  
**Type** | **Description**  
`[Replay](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicySimulator.V1/latest/Google.Cloud.PolicySimulator.V1.Replay)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
