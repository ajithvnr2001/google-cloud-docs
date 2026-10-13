---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.ConfigManagement.OciConfig
title: GKE Hub v1 API - Class OciConfig (2.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:59.777715+00:00
---

# GKE Hub v1 API - Class OciConfig (2.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.ConfigManagement.OciConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  GKE Hub v1 API - Class OciConfig (2.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.ConfigManagement.OciConfig)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.7.0/Google.Cloud.GkeHub.V1.ConfigManagement.OciConfig)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.6.0/Google.Cloud.GkeHub.V1.ConfigManagement.OciConfig)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.5.0/Google.Cloud.GkeHub.V1.ConfigManagement.OciConfig)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.4.0/Google.Cloud.GkeHub.V1.ConfigManagement.OciConfig)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.3.0/Google.Cloud.GkeHub.V1.ConfigManagement.OciConfig)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.2.0/Google.Cloud.GkeHub.V1.ConfigManagement.OciConfig)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.1.0/Google.Cloud.GkeHub.V1.ConfigManagement.OciConfig)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/2.0.0/Google.Cloud.GkeHub.V1.ConfigManagement.OciConfig)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/1.2.0/Google.Cloud.GkeHub.V1.ConfigManagement.OciConfig)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/1.1.0/Google.Cloud.GkeHub.V1.ConfigManagement.OciConfig)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/1.0.0/Google.Cloud.GkeHub.V1.ConfigManagement.OciConfig)


    
    
    public sealed class OciConfig : IMessage<OciConfig>, IEquatable<OciConfig>, IDeepCloneable<OciConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the GKE Hub v1 API class OciConfig.

OCI repo configuration for a single cluster

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > OciConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[OciConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.ConfigManagement.OciConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[OciConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.ConfigManagement.OciConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[OciConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.ConfigManagement.OciConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GkeHub.V1.ConfigManagement](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.ConfigManagement)

## Assembly

Google.Cloud.GkeHub.V1.dll

## Constructors 

### OciConfig()
    
    
    public OciConfig()

### OciConfig(OciConfig)
    
    
    public OciConfig(OciConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[OciConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GkeHub.V1/latest/Google.Cloud.GkeHub.V1.ConfigManagement.OciConfig)`  
  
  
## Properties 

### GcpServiceAccountEmail
    
    
    public string GcpServiceAccountEmail { get; set; }

The Google Cloud Service Account Email used for auth when secret_type is gcpServiceAccount.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PolicyDir
    
    
    public string PolicyDir { get; set; }

The absolute path of the directory that contains the local resources. Default: the root directory of the image.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SecretType
    
    
    public string SecretType { get; set; }

Type of secret configured for access to the Git repo.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SyncRepo
    
    
    public string SyncRepo { get; set; }

The OCI image repository URL for the package to sync from. e.g. `LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY_NAME/PACKAGE_NAME`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SyncWaitSecs
    
    
    public long SyncWaitSecs { get; set; }

Period in seconds between consecutive syncs. Default: 15.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
