---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BfdPacket
title: Compute Engine v1 API - Class BfdPacket (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:04.575108+00:00
---

# Compute Engine v1 API - Class BfdPacket (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BfdPacket

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class BfdPacket (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class BfdPacket : IMessage<BfdPacket>, IEquatable<BfdPacket>, IDeepCloneable<BfdPacket>, IBufferMessage, IMessage

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BfdPacket

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BfdPacket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BfdPacket), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BfdPacket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BfdPacket), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BfdPacket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BfdPacket), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Constructors 

### BfdPacket()
    
    
    public BfdPacket()

### BfdPacket(BfdPacket)
    
    
    public BfdPacket(BfdPacket other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BfdPacket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BfdPacket)`  
  
  
## Properties 

### AuthenticationPresent
    
    
    public bool AuthenticationPresent { get; set; }

The Authentication Present bit of the BFD packet. This is specified in section 4.1 ofRFC5880

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### ControlPlaneIndependent
    
    
    public bool ControlPlaneIndependent { get; set; }

The Control Plane Independent bit of the BFD packet. This is specified in section 4.1 ofRFC5880

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Demand
    
    
    public bool Demand { get; set; }

The demand bit of the BFD packet. This is specified in section 4.1 ofRFC5880

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Diagnostic
    
    
    public string Diagnostic { get; set; }

The diagnostic code specifies the local system's reason for the last change in session state. This allows remote systems to determine the reason that the previous session failed, for example. These diagnostic codes are specified in section 4.1 ofRFC5880 Check the Diagnostic enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Final
    
    
    public bool Final { get; set; }

The Final bit of the BFD packet. This is specified in section 4.1 ofRFC5880

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasAuthenticationPresent
    
    
    public bool HasAuthenticationPresent { get; }

Gets whether the "authentication_present" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasControlPlaneIndependent
    
    
    public bool HasControlPlaneIndependent { get; }

Gets whether the "control_plane_independent" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasDemand
    
    
    public bool HasDemand { get; }

Gets whether the "demand" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasDiagnostic
    
    
    public bool HasDiagnostic { get; }

Gets whether the "diagnostic" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasFinal
    
    
    public bool HasFinal { get; }

Gets whether the "final" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasLength
    
    
    public bool HasLength { get; }

Gets whether the "length" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMinEchoRxIntervalMs
    
    
    public bool HasMinEchoRxIntervalMs { get; }

Gets whether the "min_echo_rx_interval_ms" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMinRxIntervalMs
    
    
    public bool HasMinRxIntervalMs { get; }

Gets whether the "min_rx_interval_ms" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMinTxIntervalMs
    
    
    public bool HasMinTxIntervalMs { get; }

Gets whether the "min_tx_interval_ms" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMultiplier
    
    
    public bool HasMultiplier { get; }

Gets whether the "multiplier" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMultipoint
    
    
    public bool HasMultipoint { get; }

Gets whether the "multipoint" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMyDiscriminator
    
    
    public bool HasMyDiscriminator { get; }

Gets whether the "my_discriminator" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasPoll
    
    
    public bool HasPoll { get; }

Gets whether the "poll" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasState
    
    
    public bool HasState { get; }

Gets whether the "state" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasVersion
    
    
    public bool HasVersion { get; }

Gets whether the "version" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasYourDiscriminator
    
    
    public bool HasYourDiscriminator { get; }

Gets whether the "your_discriminator" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Length
    
    
    public uint Length { get; set; }

The length of the BFD Control packet in bytes. This is specified in section 4.1 ofRFC5880

**Property Value**  
---  
**Type** | **Description**  
`[uint](https://learn.microsoft.com/dotnet/api/system.uint32)` |   
  
### MinEchoRxIntervalMs
    
    
    public uint MinEchoRxIntervalMs { get; set; }

The Required Min Echo RX Interval value in the BFD packet. This is specified in section 4.1 ofRFC5880

**Property Value**  
---  
**Type** | **Description**  
`[uint](https://learn.microsoft.com/dotnet/api/system.uint32)` |   
  
### MinRxIntervalMs
    
    
    public uint MinRxIntervalMs { get; set; }

The Required Min RX Interval value in the BFD packet. This is specified in section 4.1 ofRFC5880

**Property Value**  
---  
**Type** | **Description**  
`[uint](https://learn.microsoft.com/dotnet/api/system.uint32)` |   
  
### MinTxIntervalMs
    
    
    public uint MinTxIntervalMs { get; set; }

The Desired Min TX Interval value in the BFD packet. This is specified in section 4.1 ofRFC5880

**Property Value**  
---  
**Type** | **Description**  
`[uint](https://learn.microsoft.com/dotnet/api/system.uint32)` |   
  
### Multiplier
    
    
    public uint Multiplier { get; set; }

The detection time multiplier of the BFD packet. This is specified in section 4.1 ofRFC5880

**Property Value**  
---  
**Type** | **Description**  
`[uint](https://learn.microsoft.com/dotnet/api/system.uint32)` |   
  
### Multipoint
    
    
    public bool Multipoint { get; set; }

The multipoint bit of the BFD packet. This is specified in section 4.1 ofRFC5880

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### MyDiscriminator
    
    
    public uint MyDiscriminator { get; set; }

The My Discriminator value in the BFD packet. This is specified in section 4.1 ofRFC5880

**Property Value**  
---  
**Type** | **Description**  
`[uint](https://learn.microsoft.com/dotnet/api/system.uint32)` |   
  
### Poll
    
    
    public bool Poll { get; set; }

The Poll bit of the BFD packet. This is specified in section 4.1 ofRFC5880

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### State
    
    
    public string State { get; set; }

The current BFD session state as seen by the transmitting system. These states are specified in section 4.1 ofRFC5880 Check the State enum for the list of possible values.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Version
    
    
    public uint Version { get; set; }

The version number of the BFD protocol, as specified in section 4.1 ofRFC5880.

**Property Value**  
---  
**Type** | **Description**  
`[uint](https://learn.microsoft.com/dotnet/api/system.uint32)` |   
  
### YourDiscriminator
    
    
    public uint YourDiscriminator { get; set; }

The Your Discriminator value in the BFD packet. This is specified in section 4.1 ofRFC5880

**Property Value**  
---  
**Type** | **Description**  
`[uint](https://learn.microsoft.com/dotnet/api/system.uint32)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
