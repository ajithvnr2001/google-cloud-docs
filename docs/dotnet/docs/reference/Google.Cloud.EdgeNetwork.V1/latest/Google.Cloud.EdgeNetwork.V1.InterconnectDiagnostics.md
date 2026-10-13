---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectDiagnostics
title: Distributed Cloud Edge Network v1 API - Class InterconnectDiagnostics (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:32:20.718172+00:00
---

# Distributed Cloud Edge Network v1 API - Class InterconnectDiagnostics (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectDiagnostics

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Distributed Cloud Edge Network v1 API - Class InterconnectDiagnostics (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectDiagnostics)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/1.5.0/Google.Cloud.EdgeNetwork.V1.InterconnectDiagnostics)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/1.4.0/Google.Cloud.EdgeNetwork.V1.InterconnectDiagnostics)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/1.3.0/Google.Cloud.EdgeNetwork.V1.InterconnectDiagnostics)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/1.2.0/Google.Cloud.EdgeNetwork.V1.InterconnectDiagnostics)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/1.1.0/Google.Cloud.EdgeNetwork.V1.InterconnectDiagnostics)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/1.0.0/Google.Cloud.EdgeNetwork.V1.InterconnectDiagnostics)


    
    
    public sealed class InterconnectDiagnostics : IMessage<InterconnectDiagnostics>, IEquatable<InterconnectDiagnostics>, IDeepCloneable<InterconnectDiagnostics>, IBufferMessage, IMessage

Reference documentation and code samples for the Distributed Cloud Edge Network v1 API class InterconnectDiagnostics.

Diagnostics information about interconnect, contains detailed and current technical information about Google's side of the connection.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > InterconnectDiagnostics

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[InterconnectDiagnostics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectDiagnostics), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[InterconnectDiagnostics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectDiagnostics), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[InterconnectDiagnostics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectDiagnostics), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.EdgeNetwork.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1)

## Assembly

Google.Cloud.EdgeNetwork.V1.dll

## Constructors 

### InterconnectDiagnostics()
    
    
    public InterconnectDiagnostics()

### InterconnectDiagnostics(InterconnectDiagnostics)
    
    
    public InterconnectDiagnostics(InterconnectDiagnostics other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[InterconnectDiagnostics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectDiagnostics)`  
  
  
## Properties 

### LinkLayerAddresses
    
    
    public RepeatedField<LinkLayerAddress> LinkLayerAddresses { get; }

A list of LinkLayerAddress, describing the ip address and corresponding link-layer address of the neighbors for this interconnect.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[LinkLayerAddress](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.LinkLayerAddress)` |   
  
### Links
    
    
    public RepeatedField<InterconnectDiagnostics.Types.LinkStatus> Links { get; }

A list of LinkStatus objects, used to describe the status for each link on the Interconnect.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[InterconnectDiagnostics](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectDiagnostics)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectDiagnostics.Types)[LinkStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.EdgeNetwork.V1/latest/Google.Cloud.EdgeNetwork.V1.InterconnectDiagnostics.Types.LinkStatus)` |   
  
### MacAddress
    
    
    public string MacAddress { get; set; }

The MAC address of the Interconnect's bundle interface.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
