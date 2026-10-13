---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.StateTimeline
title: Network Connectivity v1beta API - Class StateTimeline (1.0.0-beta02) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:28.999952+00:00
---

# Network Connectivity v1beta API - Class StateTimeline (1.0.0-beta02)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.StateTimeline

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Connectivity v1beta API - Class StateTimeline (1.0.0-beta02) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta02 (latest)  1.0.0-beta01 
    
    
    public sealed class StateTimeline : IMessage<StateTimeline>, IEquatable<StateTimeline>, IDeepCloneable<StateTimeline>, IBufferMessage, IMessage

Reference documentation and code samples for the Network Connectivity v1beta API class StateTimeline.

The timeline of the pending states for a resource.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > StateTimeline

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[StateTimeline](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.StateTimeline), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[StateTimeline](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.StateTimeline), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[StateTimeline](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.StateTimeline), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkConnectivity.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta)

## Assembly

Google.Cloud.NetworkConnectivity.V1Beta.dll

## Constructors 

### StateTimeline()
    
    
    public StateTimeline()

### StateTimeline(StateTimeline)
    
    
    public StateTimeline(StateTimeline other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[StateTimeline](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.StateTimeline)`  
  
  
## Properties 

### States
    
    
    public RepeatedField<StateTimeline.Types.StateMetadata> States { get; }

Output only. The state and activation time details of the resource state.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[StateTimeline](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.StateTimeline)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.StateTimeline.Types)[StateMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.StateTimeline.Types.StateMetadata)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
