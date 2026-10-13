---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.ArtifactConfig
title: Developer Connect v1 API - Class ArtifactConfig (1.0.0-beta04) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:19.039049+00:00
---

# Developer Connect v1 API - Class ArtifactConfig (1.0.0-beta04)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.ArtifactConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Developer Connect v1 API - Class ArtifactConfig (1.0.0-beta04) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta04 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.ArtifactConfig)
  * [ 1.0.0-beta03 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/1.0.0-beta03/Google.Cloud.DeveloperConnect.V1.ArtifactConfig)


    
    
    public sealed class ArtifactConfig : IMessage<ArtifactConfig>, IEquatable<ArtifactConfig>, IDeepCloneable<ArtifactConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Developer Connect v1 API class ArtifactConfig.

The artifact config of the artifact that is deployed.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ArtifactConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ArtifactConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.ArtifactConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ArtifactConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.ArtifactConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ArtifactConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.ArtifactConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DeveloperConnect.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1)

## Assembly

Google.Cloud.DeveloperConnect.V1.dll

## Constructors 

### ArtifactConfig()
    
    
    public ArtifactConfig()

### ArtifactConfig(ArtifactConfig)
    
    
    public ArtifactConfig(ArtifactConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ArtifactConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.ArtifactConfig)`  
  
  
## Properties 

### ArtifactMetadataStorageCase
    
    
    public ArtifactConfig.ArtifactMetadataStorageOneofCase ArtifactMetadataStorageCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ArtifactConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.ArtifactConfig)[ArtifactMetadataStorageOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.ArtifactConfig.ArtifactMetadataStorageOneofCase)` |   
  
### ArtifactStorageCase
    
    
    public ArtifactConfig.ArtifactStorageOneofCase ArtifactStorageCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ArtifactConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.ArtifactConfig)[ArtifactStorageOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.ArtifactConfig.ArtifactStorageOneofCase)` |   
  
### GoogleArtifactAnalysis
    
    
    public GoogleArtifactAnalysis GoogleArtifactAnalysis { get; set; }

Optional. Set if the artifact metadata is stored in Artifact analysis.

**Property Value**  
---  
**Type** | **Description**  
`[GoogleArtifactAnalysis](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.GoogleArtifactAnalysis)` |   
  
### GoogleArtifactRegistry
    
    
    public GoogleArtifactRegistry GoogleArtifactRegistry { get; set; }

Optional. Set if the artifact is stored in Artifact registry.

**Property Value**  
---  
**Type** | **Description**  
`[GoogleArtifactRegistry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DeveloperConnect.V1/latest/Google.Cloud.DeveloperConnect.V1.GoogleArtifactRegistry)` |   
  
### Uri
    
    
    public string Uri { get; set; }

Required. Immutable. The URI of the artifact that is deployed. e.g. `us-docker.pkg.dev/my-project/my-repo/image`. The URI does not include the tag / digest because it captures a lineage of artifacts.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
