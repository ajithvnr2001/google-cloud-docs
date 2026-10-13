---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.Scheduling
title: Backup and DR Service v1 API - Class Scheduling (2.9.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:46:36.957104+00:00
---

# Backup and DR Service v1 API - Class Scheduling (2.9.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.Scheduling

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Backup and DR Service v1 API - Class Scheduling (2.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.9.0 (latest)  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.2.0  1.1.0  1.0.0-beta02 
    
    
    public sealed class Scheduling : IMessage<Scheduling>, IEquatable<Scheduling>, IDeepCloneable<Scheduling>, IBufferMessage, IMessage

Reference documentation and code samples for the Backup and DR Service v1 API class Scheduling.

Sets the scheduling options for an Instance.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Scheduling

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Scheduling](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.Scheduling), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Scheduling](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.Scheduling), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Scheduling](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.Scheduling), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BackupDR.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1)

## Assembly

Google.Cloud.BackupDR.V1.dll

## Constructors 

### Scheduling()
    
    
    public Scheduling()

### Scheduling(Scheduling)
    
    
    public Scheduling(Scheduling other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Scheduling](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.Scheduling)`  
  
  
## Properties 

### AutomaticRestart
    
    
    public bool AutomaticRestart { get; set; }

Optional. Specifies whether the instance should be automatically restarted if it is terminated by Compute Engine (not terminated by a user).

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasAutomaticRestart
    
    
    public bool HasAutomaticRestart { get; }

Gets whether the "automatic_restart" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasInstanceTerminationAction
    
    
    public bool HasInstanceTerminationAction { get; }

Gets whether the "instance_termination_action" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMinNodeCpus
    
    
    public bool HasMinNodeCpus { get; }

Gets whether the "min_node_cpus" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasOnHostMaintenance
    
    
    public bool HasOnHostMaintenance { get; }

Gets whether the "on_host_maintenance" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasPreemptible
    
    
    public bool HasPreemptible { get; }

Gets whether the "preemptible" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasProvisioningModel
    
    
    public bool HasProvisioningModel { get; }

Gets whether the "provisioning_model" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InstanceTerminationAction
    
    
    public Scheduling.Types.InstanceTerminationAction InstanceTerminationAction { get; set; }

Optional. Specifies the termination action for the instance.

**Property Value**  
---  
**Type** | **Description**  
`[Scheduling](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.Scheduling)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.Scheduling.Types)[InstanceTerminationAction](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.Scheduling.Types.InstanceTerminationAction)` |   
  
### LocalSsdRecoveryTimeout
    
    
    public SchedulingDuration LocalSsdRecoveryTimeout { get; set; }

Optional. Specifies the maximum amount of time a Local Ssd Vm should wait while recovery of the Local Ssd state is attempted. Its value should be in between 0 and 168 hours with hour granularity and the default value being 1 hour.

**Property Value**  
---  
**Type** | **Description**  
`[SchedulingDuration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.SchedulingDuration)` |   
  
### MinNodeCpus
    
    
    public int MinNodeCpus { get; set; }

Optional. The minimum number of virtual CPUs this instance will consume when running on a sole-tenant node.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### NodeAffinities
    
    
    public RepeatedField<Scheduling.Types.NodeAffinity> NodeAffinities { get; }

Optional. A set of node affinity and anti-affinity configurations. Overrides reservationAffinity.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Scheduling](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.Scheduling)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.Scheduling.Types)[NodeAffinity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.Scheduling.Types.NodeAffinity)` |   
  
### OnHostMaintenance
    
    
    public Scheduling.Types.OnHostMaintenance OnHostMaintenance { get; set; }

Optional. Defines the maintenance behavior for this instance.

**Property Value**  
---  
**Type** | **Description**  
`[Scheduling](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.Scheduling)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.Scheduling.Types)[OnHostMaintenance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.Scheduling.Types.OnHostMaintenance)` |   
  
### Preemptible
    
    
    public bool Preemptible { get; set; }

Optional. Defines whether the instance is preemptible.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### ProvisioningModel
    
    
    public Scheduling.Types.ProvisioningModel ProvisioningModel { get; set; }

Optional. Specifies the provisioning model of the instance.

**Property Value**  
---  
**Type** | **Description**  
`[Scheduling](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.Scheduling)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.Scheduling.Types)[ProvisioningModel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.Scheduling.Types.ProvisioningModel)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-31 UTC."],[],[]] 
