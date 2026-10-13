---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource
title: Vertex AI v1beta1 API - Class MigratableResource (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:34:07.231975+00:00
---

# Vertex AI v1beta1 API - Class MigratableResource (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class MigratableResource (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class MigratableResource : IMessage<MigratableResource>, IEquatable<MigratableResource>, IDeepCloneable<MigratableResource>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class MigratableResource.

Represents one resource that exists in automl.googleapis.com, datalabeling.googleapis.com or ml.googleapis.com.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > MigratableResource

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[MigratableResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[MigratableResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[MigratableResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### MigratableResource()
    
    
    public MigratableResource()

### MigratableResource(MigratableResource)
    
    
    public MigratableResource(MigratableResource other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[MigratableResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource)`  
  
  
## Properties 

### AutomlDataset
    
    
    public MigratableResource.Types.AutomlDataset AutomlDataset { get; set; }

Output only. Represents one Dataset in automl.googleapis.com.

**Property Value**  
---  
**Type** | **Description**  
`[MigratableResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource.Types)[AutomlDataset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource.Types.AutomlDataset)` |   
  
### AutomlModel
    
    
    public MigratableResource.Types.AutomlModel AutomlModel { get; set; }

Output only. Represents one Model in automl.googleapis.com.

**Property Value**  
---  
**Type** | **Description**  
`[MigratableResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource.Types)[AutomlModel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource.Types.AutomlModel)` |   
  
### DataLabelingDataset
    
    
    public MigratableResource.Types.DataLabelingDataset DataLabelingDataset { get; set; }

Output only. Represents one Dataset in datalabeling.googleapis.com.

**Property Value**  
---  
**Type** | **Description**  
`[MigratableResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource.Types)[DataLabelingDataset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource.Types.DataLabelingDataset)` |   
  
### LastMigrateTime
    
    
    public Timestamp LastMigrateTime { get; set; }

Output only. Timestamp when the last migration attempt on this MigratableResource started. Will not be set if there's no migration attempt on this MigratableResource.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### LastUpdateTime
    
    
    public Timestamp LastUpdateTime { get; set; }

Output only. Timestamp when this MigratableResource was last updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### MlEngineModelVersion
    
    
    public MigratableResource.Types.MlEngineModelVersion MlEngineModelVersion { get; set; }

Output only. Represents one Version in ml.googleapis.com.

**Property Value**  
---  
**Type** | **Description**  
`[MigratableResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource.Types)[MlEngineModelVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource.Types.MlEngineModelVersion)` |   
  
### ResourceCase
    
    
    public MigratableResource.ResourceOneofCase ResourceCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[MigratableResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource)[ResourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigratableResource.ResourceOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
