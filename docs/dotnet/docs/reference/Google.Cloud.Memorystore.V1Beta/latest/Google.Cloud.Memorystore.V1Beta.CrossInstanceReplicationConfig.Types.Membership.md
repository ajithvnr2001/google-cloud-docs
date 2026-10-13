---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.CrossInstanceReplicationConfig.Types.Membership
title: Memorystore v1beta API - Class CrossInstanceReplicationConfig.Types.Membership (1.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:36.990624+00:00
---

# Memorystore v1beta API - Class CrossInstanceReplicationConfig.Types.Membership (1.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.CrossInstanceReplicationConfig.Types.Membership

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Memorystore v1beta API - Class CrossInstanceReplicationConfig.Types.Membership (1.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta07 (latest)  1.0.0-beta06 
    
    
    public sealed class CrossInstanceReplicationConfig.Types.Membership : IMessage<CrossInstanceReplicationConfig.Types.Membership>, IEquatable<CrossInstanceReplicationConfig.Types.Membership>, IDeepCloneable<CrossInstanceReplicationConfig.Types.Membership>, IBufferMessage, IMessage

Reference documentation and code samples for the Memorystore v1beta API class CrossInstanceReplicationConfig.Types.Membership.

An output only view of all the member instances participating in the cross instance replication.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CrossInstanceReplicationConfig.Types.Membership

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CrossInstanceReplicationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.CrossInstanceReplicationConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.CrossInstanceReplicationConfig.Types)[Membership](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.CrossInstanceReplicationConfig.Types.Membership), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CrossInstanceReplicationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.CrossInstanceReplicationConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.CrossInstanceReplicationConfig.Types)[Membership](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.CrossInstanceReplicationConfig.Types.Membership), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CrossInstanceReplicationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.CrossInstanceReplicationConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.CrossInstanceReplicationConfig.Types)[Membership](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.CrossInstanceReplicationConfig.Types.Membership), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Memorystore.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta)

## Assembly

Google.Cloud.Memorystore.V1Beta.dll

## Constructors 

### Membership()
    
    
    public Membership()

### Membership(Membership)
    
    
    public Membership(CrossInstanceReplicationConfig.Types.Membership other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CrossInstanceReplicationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.CrossInstanceReplicationConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.CrossInstanceReplicationConfig.Types)[Membership](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.CrossInstanceReplicationConfig.Types.Membership)`  
  
  
## Properties 

### PrimaryInstance
    
    
    public CrossInstanceReplicationConfig.Types.RemoteInstance PrimaryInstance { get; set; }

Output only. The primary instance that acts as the source of replication for the secondary instances.

**Property Value**  
---  
**Type** | **Description**  
`[CrossInstanceReplicationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.CrossInstanceReplicationConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.CrossInstanceReplicationConfig.Types)[RemoteInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.CrossInstanceReplicationConfig.Types.RemoteInstance)` |   
  
### SecondaryInstances
    
    
    public RepeatedField<CrossInstanceReplicationConfig.Types.RemoteInstance> SecondaryInstances { get; }

Output only. The list of secondary instances replicating from the primary instance.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[CrossInstanceReplicationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.CrossInstanceReplicationConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.CrossInstanceReplicationConfig.Types)[RemoteInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memorystore.V1Beta/latest/Google.Cloud.Memorystore.V1Beta.CrossInstanceReplicationConfig.Types.RemoteInstance)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
