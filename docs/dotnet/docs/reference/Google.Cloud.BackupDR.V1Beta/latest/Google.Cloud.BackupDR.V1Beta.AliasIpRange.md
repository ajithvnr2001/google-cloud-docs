---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.AliasIpRange
title: Backup and DR Service v1beta API - Class AliasIpRange (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:24.867092+00:00
---

# Backup and DR Service v1beta API - Class AliasIpRange (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.AliasIpRange

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Backup and DR Service v1beta API - Class AliasIpRange (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public sealed class AliasIpRange : IMessage<AliasIpRange>, IEquatable<AliasIpRange>, IDeepCloneable<AliasIpRange>, IBufferMessage, IMessage

Reference documentation and code samples for the Backup and DR Service v1beta API class AliasIpRange.

An alias IP range attached to an instance's network interface.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AliasIpRange

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AliasIpRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.AliasIpRange), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AliasIpRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.AliasIpRange), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AliasIpRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.AliasIpRange), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BackupDR.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta)

## Assembly

Google.Cloud.BackupDR.V1Beta.dll

## Constructors 

### AliasIpRange()
    
    
    public AliasIpRange()

### AliasIpRange(AliasIpRange)
    
    
    public AliasIpRange(AliasIpRange other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AliasIpRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1Beta/latest/Google.Cloud.BackupDR.V1Beta.AliasIpRange)`  
  
  
## Properties 

### HasIpCidrRange
    
    
    public bool HasIpCidrRange { get; }

Gets whether the "ip_cidr_range" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSubnetworkRangeName
    
    
    public bool HasSubnetworkRangeName { get; }

Gets whether the "subnetwork_range_name" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IpCidrRange
    
    
    public string IpCidrRange { get; set; }

Optional. The IP alias ranges to allocate for this interface.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SubnetworkRangeName
    
    
    public string SubnetworkRangeName { get; set; }

Optional. The name of a subnetwork secondary IP range from which to allocate an IP alias range. If not specified, the primary range of the subnetwork is used.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
