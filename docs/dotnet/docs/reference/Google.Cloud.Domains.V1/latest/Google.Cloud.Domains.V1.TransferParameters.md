---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.TransferParameters
title: Cloud Domains v1 API - Class TransferParameters (2.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:21:10.065036+00:00
---

# Cloud Domains v1 API - Class TransferParameters (2.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.TransferParameters

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Domains v1 API - Class TransferParameters (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.TransferParameters)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.4.0/Google.Cloud.Domains.V1.TransferParameters)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.3.0/Google.Cloud.Domains.V1.TransferParameters)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.2.0/Google.Cloud.Domains.V1.TransferParameters)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.1.0/Google.Cloud.Domains.V1.TransferParameters)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/2.0.0/Google.Cloud.Domains.V1.TransferParameters)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/1.0.0/Google.Cloud.Domains.V1.TransferParameters)


    
    
    public sealed class TransferParameters : IMessage<TransferParameters>, IEquatable<TransferParameters>, IDeepCloneable<TransferParameters>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Domains v1 API class TransferParameters.

Parameters required to transfer a domain from another registrar.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > TransferParameters

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[TransferParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.TransferParameters), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[TransferParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.TransferParameters), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[TransferParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.TransferParameters), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Domains.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1)

## Assembly

Google.Cloud.Domains.V1.dll

## Constructors 

### TransferParameters()
    
    
    public TransferParameters()

### TransferParameters(TransferParameters)
    
    
    public TransferParameters(TransferParameters other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[TransferParameters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.TransferParameters)`  
  
  
## Properties 

### CurrentRegistrar
    
    
    public string CurrentRegistrar { get; set; }

The registrar that currently manages the domain.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DomainName
    
    
    public string DomainName { get; set; }

The domain name. Unicode domain names are expressed in Punycode format.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NameServers
    
    
    public RepeatedField<string> NameServers { get; }

The name servers that currently store the configuration of the domain.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SupportedPrivacy
    
    
    public RepeatedField<ContactPrivacy> SupportedPrivacy { get; }

Contact privacy options that the domain supports.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ContactPrivacy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.ContactPrivacy)` |   
  
### TransferLockState
    
    
    public TransferLockState TransferLockState { get; set; }

Indicates whether the domain is protected by a transfer lock. For a transfer to succeed, this must show `UNLOCKED`. To unlock a domain, go to its current registrar.

**Property Value**  
---  
**Type** | **Description**  
`[TransferLockState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Domains.V1/latest/Google.Cloud.Domains.V1.TransferLockState)` |   
  
### YearlyPrice
    
    
    public Money YearlyPrice { get; set; }

Price to transfer or renew the domain for one year.

**Property Value**  
---  
**Type** | **Description**  
`[Money](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Type.Money.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
