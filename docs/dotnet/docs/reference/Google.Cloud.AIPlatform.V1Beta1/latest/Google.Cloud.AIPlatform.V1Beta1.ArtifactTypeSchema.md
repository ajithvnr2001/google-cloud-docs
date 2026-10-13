---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ArtifactTypeSchema
title: Vertex AI v1beta1 API - Class ArtifactTypeSchema (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:30:14.333929+00:00
---

# Vertex AI v1beta1 API - Class ArtifactTypeSchema (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ArtifactTypeSchema

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class ArtifactTypeSchema (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class ArtifactTypeSchema : IMessage<ArtifactTypeSchema>, IEquatable<ArtifactTypeSchema>, IDeepCloneable<ArtifactTypeSchema>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class ArtifactTypeSchema.

The definition of a artifact type in MLMD.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ArtifactTypeSchema

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ArtifactTypeSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ArtifactTypeSchema), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ArtifactTypeSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ArtifactTypeSchema), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ArtifactTypeSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ArtifactTypeSchema), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### ArtifactTypeSchema()
    
    
    public ArtifactTypeSchema()

### ArtifactTypeSchema(ArtifactTypeSchema)
    
    
    public ArtifactTypeSchema(ArtifactTypeSchema other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ArtifactTypeSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ArtifactTypeSchema)`  
  
  
## Properties 

### HasInstanceSchema
    
    
    public bool HasInstanceSchema { get; }

Gets whether the "instance_schema" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSchemaTitle
    
    
    public bool HasSchemaTitle { get; }

Gets whether the "schema_title" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSchemaUri
    
    
    [Obsolete]
    public bool HasSchemaUri { get; }

Gets whether the "schema_uri" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InstanceSchema
    
    
    public string InstanceSchema { get; set; }

Contains a raw YAML string, describing the format of the properties of the type.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### KindCase
    
    
    public ArtifactTypeSchema.KindOneofCase KindCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ArtifactTypeSchema](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ArtifactTypeSchema)[KindOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ArtifactTypeSchema.KindOneofCase)` |   
  
### SchemaTitle
    
    
    public string SchemaTitle { get; set; }

The name of the type. The format of the title must be: `<namespace>.<title>`. Examples:

  * `aiplatform.Model`
  * `acme.CustomModel` When this field is set, the type must be pre-registered in the MLMD store.



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SchemaUri
    
    
    [Obsolete]
    public string SchemaUri { get; set; }

Points to a YAML file stored on Cloud Storage describing the format. Deprecated. Use [PipelineArtifactTypeSchema.schema_title][] or [PipelineArtifactTypeSchema.instance_schema][] instead.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SchemaVersion
    
    
    public string SchemaVersion { get; set; }

The schema version of the artifact. If the value is not set, it defaults to the latest version in the system.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
