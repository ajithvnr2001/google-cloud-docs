---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsErrorInfo
title: Artifact Registry v1beta2 API - Class ImportYumArtifactsErrorInfo (2.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:18:21.892593+00:00
---

# Artifact Registry v1beta2 API - Class ImportYumArtifactsErrorInfo (2.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsErrorInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Artifact Registry v1beta2 API - Class ImportYumArtifactsErrorInfo (2.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsErrorInfo)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/2.0.0-beta05/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsErrorInfo)
  * [ 1.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/1.0.0-beta06/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsErrorInfo)


    
    
    public sealed class ImportYumArtifactsErrorInfo : IMessage<ImportYumArtifactsErrorInfo>, IEquatable<ImportYumArtifactsErrorInfo>, IDeepCloneable<ImportYumArtifactsErrorInfo>, IBufferMessage, IMessage

Reference documentation and code samples for the Artifact Registry v1beta2 API class ImportYumArtifactsErrorInfo.

Error information explaining why a package was not imported.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ImportYumArtifactsErrorInfo

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ImportYumArtifactsErrorInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsErrorInfo), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ImportYumArtifactsErrorInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsErrorInfo), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ImportYumArtifactsErrorInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsErrorInfo), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ArtifactRegistry.V1Beta2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2)

## Assembly

Google.Cloud.ArtifactRegistry.V1Beta2.dll

## Constructors 

### ImportYumArtifactsErrorInfo()
    
    
    public ImportYumArtifactsErrorInfo()

### ImportYumArtifactsErrorInfo(ImportYumArtifactsErrorInfo)
    
    
    public ImportYumArtifactsErrorInfo(ImportYumArtifactsErrorInfo other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ImportYumArtifactsErrorInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsErrorInfo)`  
  
  
## Properties 

### Error
    
    
    public Status Error { get; set; }

The detailed error status.

**Property Value**  
---  
**Type** | **Description**  
`[Status](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Status.html)` |   
  
### GcsSource
    
    
    public ImportYumArtifactsGcsSource GcsSource { get; set; }

Google Cloud Storage location requested.

**Property Value**  
---  
**Type** | **Description**  
`[ImportYumArtifactsGcsSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsGcsSource)` |   
  
### SourceCase
    
    
    public ImportYumArtifactsErrorInfo.SourceOneofCase SourceCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ImportYumArtifactsErrorInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsErrorInfo)[SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ArtifactRegistry.V1Beta2/latest/Google.Cloud.ArtifactRegistry.V1Beta2.ImportYumArtifactsErrorInfo.SourceOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
