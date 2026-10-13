---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.AlloyDbSettings
title: Database Migration v1 API - Class AlloyDbSettings (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:24.809714+00:00
---

# Database Migration v1 API - Class AlloyDbSettings (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.AlloyDbSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Database Migration v1 API - Class AlloyDbSettings (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.AlloyDbSettings)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.5.0/Google.Cloud.CloudDms.V1.AlloyDbSettings)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.4.0/Google.Cloud.CloudDms.V1.AlloyDbSettings)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.3.0/Google.Cloud.CloudDms.V1.AlloyDbSettings)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.2.0/Google.Cloud.CloudDms.V1.AlloyDbSettings)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.1.0/Google.Cloud.CloudDms.V1.AlloyDbSettings)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/2.0.0/Google.Cloud.CloudDms.V1.AlloyDbSettings)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/1.2.0/Google.Cloud.CloudDms.V1.AlloyDbSettings)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/1.1.0/Google.Cloud.CloudDms.V1.AlloyDbSettings)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/1.0.0/Google.Cloud.CloudDms.V1.AlloyDbSettings)


    
    
    public sealed class AlloyDbSettings : IMessage<AlloyDbSettings>, IEquatable<AlloyDbSettings>, IDeepCloneable<AlloyDbSettings>, IBufferMessage, IMessage

Reference documentation and code samples for the Database Migration v1 API class AlloyDbSettings.

Settings for creating an AlloyDB cluster.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AlloyDbSettings

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AlloyDbSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.AlloyDbSettings), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AlloyDbSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.AlloyDbSettings), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AlloyDbSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.AlloyDbSettings), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudDms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1)

## Assembly

Google.Cloud.CloudDms.V1.dll

## Constructors 

### AlloyDbSettings()
    
    
    public AlloyDbSettings()

### AlloyDbSettings(AlloyDbSettings)
    
    
    public AlloyDbSettings(AlloyDbSettings other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AlloyDbSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.AlloyDbSettings)`  
  
  
## Properties 

### EncryptionConfig
    
    
    public AlloyDbSettings.Types.EncryptionConfig EncryptionConfig { get; set; }

Optional. The encryption config can be specified to encrypt the data disks and other persistent data resources of a cluster with a customer-managed encryption key (CMEK). When this field is not specified, the cluster will then use default encryption scheme to protect the user data.

**Property Value**  
---  
**Type** | **Description**  
`[AlloyDbSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.AlloyDbSettings)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.AlloyDbSettings.Types)[EncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.AlloyDbSettings.Types.EncryptionConfig)` |   
  
### InitialUser
    
    
    public AlloyDbSettings.Types.UserPassword InitialUser { get; set; }

Required. Input only. Initial user to setup during cluster creation. Required.

**Property Value**  
---  
**Type** | **Description**  
`[AlloyDbSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.AlloyDbSettings)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.AlloyDbSettings.Types)[UserPassword](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.AlloyDbSettings.Types.UserPassword)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Labels for the AlloyDB cluster created by DMS. An object containing a list of 'key', 'value' pairs.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PrimaryInstanceSettings
    
    
    public AlloyDbSettings.Types.PrimaryInstanceSettings PrimaryInstanceSettings { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[AlloyDbSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.AlloyDbSettings)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.AlloyDbSettings.Types)[PrimaryInstanceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudDms.V1/latest/Google.Cloud.CloudDms.V1.AlloyDbSettings.Types.PrimaryInstanceSettings)` |   
  
### VpcNetwork
    
    
    public string VpcNetwork { get; set; }

Required. The resource link for the VPC network in which cluster resources are created and from which they are accessible via Private IP. The network must belong to the same project as the cluster. It is specified in the form: "projects/{project_number}/global/networks/{network_id}". This is required to create a cluster.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
