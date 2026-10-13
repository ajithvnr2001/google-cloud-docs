---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ReceiveEventsRequest.Types.SetupRequest
title: Vision AI v1 API - Class ReceiveEventsRequest.Types.SetupRequest (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:08:25.893193+00:00
---

# Vision AI v1 API - Class ReceiveEventsRequest.Types.SetupRequest (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ReceiveEventsRequest.Types.SetupRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vision AI v1 API - Class ReceiveEventsRequest.Types.SetupRequest (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public sealed class ReceiveEventsRequest.Types.SetupRequest : IMessage<ReceiveEventsRequest.Types.SetupRequest>, IEquatable<ReceiveEventsRequest.Types.SetupRequest>, IDeepCloneable<ReceiveEventsRequest.Types.SetupRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Vision AI v1 API class ReceiveEventsRequest.Types.SetupRequest.

SetupRequest is the first message sent to the service to setup the RPC connection.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ReceiveEventsRequest.Types.SetupRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ReceiveEventsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ReceiveEventsRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ReceiveEventsRequest.Types)[SetupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ReceiveEventsRequest.Types.SetupRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ReceiveEventsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ReceiveEventsRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ReceiveEventsRequest.Types)[SetupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ReceiveEventsRequest.Types.SetupRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ReceiveEventsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ReceiveEventsRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ReceiveEventsRequest.Types)[SetupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ReceiveEventsRequest.Types.SetupRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.VisionAI.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1)

## Assembly

Google.Cloud.VisionAI.V1.dll

## Constructors 

### SetupRequest()
    
    
    public SetupRequest()

### SetupRequest(SetupRequest)
    
    
    public SetupRequest(ReceiveEventsRequest.Types.SetupRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ReceiveEventsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ReceiveEventsRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ReceiveEventsRequest.Types)[SetupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ReceiveEventsRequest.Types.SetupRequest)`  
  
  
## Properties 

### Cluster
    
    
    public string Cluster { get; set; }

The cluster name.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ControlledMode
    
    
    public ControlledMode ControlledMode { get; set; }

Controller mode configuration for receiving events from the server.

**Property Value**  
---  
**Type** | **Description**  
`[ControlledMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ControlledMode)` |   
  
### HeartbeatInterval
    
    
    public Duration HeartbeatInterval { get; set; }

The maximum duration of server silence before the client determines the server unreachable.

The client must either receive an `Event` update or a heart beat message before this duration expires; otherwise, the client will automatically cancel the current connection and retry.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### Receiver
    
    
    public string Receiver { get; set; }

A name for the receiver to self-identify.

This is used to keep track of a receiver's read progress.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Stream
    
    
    public string Stream { get; set; }

The stream name. The service will return the events for the given stream.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### WritesDoneGracePeriod
    
    
    public Duration WritesDoneGracePeriod { get; set; }

The grace period after which a `writes_done_request` is issued, that a `WritesDone` is expected from the client.

The server is free to cancel the RPC should this expire.

A system default will be chosen if unset.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
