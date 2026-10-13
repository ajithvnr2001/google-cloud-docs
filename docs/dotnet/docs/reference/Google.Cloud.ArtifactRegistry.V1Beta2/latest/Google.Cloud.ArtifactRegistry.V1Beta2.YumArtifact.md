---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.YumArtifact
title: Artifact Registry v1beta2 API - Class YumArtifact (2.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:18:28.167075+00:00
---

# Artifact Registry v1beta2 API - Class YumArtifact (2.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.YumArtifact

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Artifact Registry v1beta2 API - Class YumArtifact (2.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.YumArtifact)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/2.0.0-beta05/Google.Cloud.ArtifactRegistry.V1Beta2.YumArtifact)
  * [ 1.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/1.0.0-beta06/Google.Cloud.ArtifactRegistry.V1Beta2.YumArtifact)


    
    
    public sealed class YumArtifact : IMessage<YumArtifact>, IEquatable<YumArtifact>, IDeepCloneable<YumArtifact>, IBufferMessage, IMessage

Reference documentation and code samples for the Artifact Registry v1beta2 API class YumArtifact.

A detailed representation of a Yum artifact.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > YumArtifact

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[YumArtifact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.YumArtifact), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[YumArtifact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.YumArtifact), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[YumArtifact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.YumArtifact), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ArtifactRegistry.V1Beta2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2)

## Assembly

Google.Cloud.ArtifactRegistry.V1Beta2.dll

## Constructors 

### YumArtifact()
    
    
    public YumArtifact()

### YumArtifact(YumArtifact)
    
    
    public YumArtifact(YumArtifact other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[YumArtifact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.YumArtifact)`  
  
  
## Properties 

### Architecture
    
    
    public string Architecture { get; set; }

Output only. Operating system architecture of the artifact.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. The Artifact Registry resource name of the artifact.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PackageName
    
    
    public string PackageName { get; set; }

Output only. The yum package name of the artifact.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PackageType
    
    
    public YumArtifact.Types.PackageType PackageType { get; set; }

Output only. An artifact is a binary or source package.

**Property Value**  
---  
**Type** | **Description**  
`[YumArtifact](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.YumArtifact)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.YumArtifact.Types)[PackageType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.YumArtifact.Types.PackageType)` |   
  
### YumArtifactName
    
    
    public YumArtifactName YumArtifactName { get; set; }

[YumArtifactName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.YumArtifactName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.YumArtifact#Google_Cloud_ArtifactRegistry_V1Beta2_YumArtifact_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[YumArtifactName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.YumArtifactName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
