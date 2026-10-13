---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1.Instance
title: Cloud Data Fusion v1 API - Class Instance (2.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:58:03.252638+00:00
---

# Cloud Data Fusion v1 API - Class Instance (2.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1.Instance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Data Fusion v1 API - Class Instance (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1.Instance)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/2.4.0/Google.Cloud.DataFusion.V1.Instance)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/2.3.0/Google.Cloud.DataFusion.V1.Instance)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/2.2.0/Google.Cloud.DataFusion.V1.Instance)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/2.1.0/Google.Cloud.DataFusion.V1.Instance)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/2.0.0/Google.Cloud.DataFusion.V1.Instance)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/1.1.0/Google.Cloud.DataFusion.V1.Instance)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/1.0.0/Google.Cloud.DataFusion.V1.Instance)


    
    
    public sealed class Instance : IMessage<Instance>, IEquatable<Instance>, IDeepCloneable<Instance>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Data Fusion v1 API class Instance.

Represents a Data Fusion instance.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Instance

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1.Instance), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1.Instance), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1.Instance), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DataFusion.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1)

## Assembly

Google.Cloud.DataFusion.V1.dll

## Constructors 

### Instance()
    
    
    public Instance()

### Instance(Instance)
    
    
    public Instance(Instance other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1.Instance)`  
  
  
## Properties 

### Accelerators
    
    
    public RepeatedField<Accelerator> Accelerators { get; }

List of accelerators enabled for this CDF instance.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Accelerator](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1.Accelerator)` |   
  
### ApiEndpoint
    
    
    public string ApiEndpoint { get; set; }

Output only. Endpoint on which the REST APIs is accessible.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AvailableVersion
    
    
    public RepeatedField<Version> AvailableVersion { get; }

Available versions that the instance can be upgraded to using UpdateInstanceRequest.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Version](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1.Version)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. The time the instance was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### CryptoKeyConfig
    
    
    public CryptoKeyConfig CryptoKeyConfig { get; set; }

The crypto key configuration. This field is used by the Customer-Managed Encryption Keys (CMEK) feature.

**Property Value**  
---  
**Type** | **Description**  
`[CryptoKeyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1.CryptoKeyConfig)` |   
  
### DataprocServiceAccount
    
    
    public string DataprocServiceAccount { get; set; }

User-managed service account to set on Dataproc when Cloud Data Fusion creates Dataproc to run data processing pipelines.

This allows users to have fine-grained access control on Dataproc's accesses to cloud resources.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Description
    
    
    public string Description { get; set; }

A description of this instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DisabledReason
    
    
    public RepeatedField<Instance.Types.DisabledReason> DisabledReason { get; }

Output only. If the instance state is DISABLED, the reason for disabling the instance.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1.Instance.Types)[DisabledReason](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1.Instance.Types.DisabledReason)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Display name for an instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EnableRbac
    
    
    public bool EnableRbac { get; set; }

Option to enable granular role-based access control.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### EnableStackdriverLogging
    
    
    public bool EnableStackdriverLogging { get; set; }

Option to enable Stackdriver Logging.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### EnableStackdriverMonitoring
    
    
    public bool EnableStackdriverMonitoring { get; set; }

Option to enable Stackdriver Monitoring.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### GcsBucket
    
    
    public string GcsBucket { get; set; }

Output only. Cloud Storage bucket generated by Data Fusion in the customer project.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### InstanceName
    
    
    public InstanceName InstanceName { get; set; }

[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1.InstanceName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1.Instance#Google_Cloud_DataFusion_V1_Instance_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1.InstanceName)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

The resource labels for instance to use to annotate any related underlying resources such as Compute Engine VMs. The character '=' is not allowed to be used within the labels.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. The name of this instance is in the form of projects/{project}/locations/{location}/instances/{instance}.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NetworkConfig
    
    
    public NetworkConfig NetworkConfig { get; set; }

Network configuration options. These are required when a private Data Fusion instance is to be created.

**Property Value**  
---  
**Type** | **Description**  
`[NetworkConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1.NetworkConfig)` |   
  
### Options
    
    
    public MapField<string, string> Options { get; }

Map of additional options used to configure the behavior of Data Fusion instance.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### P4ServiceAccount
    
    
    public string P4ServiceAccount { get; set; }

Output only. P4 service account for the customer project.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PrivateInstance
    
    
    public bool PrivateInstance { get; set; }

Specifies whether the Data Fusion instance should be private. If set to true, all Data Fusion nodes will have private IP addresses and will not be able to access the public internet.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### ServiceAccount
    
    
    [Obsolete]
    public string ServiceAccount { get; set; }

Output only. Deprecated. Use tenant_project_id instead to extract the tenant project ID.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceEndpoint
    
    
    public string ServiceEndpoint { get; set; }

Output only. Endpoint on which the Data Fusion UI is accessible.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### State
    
    
    public Instance.Types.State State { get; set; }

Output only. The current state of this Data Fusion instance.

**Property Value**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1.Instance.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1.Instance.Types.State)` |   
  
### StateMessage
    
    
    public string StateMessage { get; set; }

Output only. Additional information about the current state of this Data Fusion instance if available.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TenantProjectId
    
    
    public string TenantProjectId { get; set; }

Output only. The name of the tenant project.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public Instance.Types.Type Type { get; set; }

Required. Instance type.

**Property Value**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1.Instance.Types)[Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DataFusion.V1/latest/Google.Cloud.DataFusion.V1.Instance.Types.Type)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. The time the instance was last updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Version
    
    
    public string Version { get; set; }

Current version of the Data Fusion. Only specifiable in Update.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Zone
    
    
    public string Zone { get; set; }

Name of the zone in which the Data Fusion instance will be created. Only DEVELOPER instances use this field.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
