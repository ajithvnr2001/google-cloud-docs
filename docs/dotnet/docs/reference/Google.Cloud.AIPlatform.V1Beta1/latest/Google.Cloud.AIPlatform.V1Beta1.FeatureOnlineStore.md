---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore
title: Vertex AI v1beta1 API - Class FeatureOnlineStore (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:47.944811+00:00
---

# Vertex AI v1beta1 API - Class FeatureOnlineStore (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class FeatureOnlineStore (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class FeatureOnlineStore : IMessage<FeatureOnlineStore>, IEquatable<FeatureOnlineStore>, IDeepCloneable<FeatureOnlineStore>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class FeatureOnlineStore.

Vertex AI Feature Online Store provides a centralized repository for serving ML features and embedding indexes at low latency. The Feature Online Store is a top-level container.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > FeatureOnlineStore

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### FeatureOnlineStore()
    
    
    public FeatureOnlineStore()

### FeatureOnlineStore(FeatureOnlineStore)
    
    
    public FeatureOnlineStore(FeatureOnlineStore other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore)`  
  
  
## Properties 

### Bigtable
    
    
    public FeatureOnlineStore.Types.Bigtable Bigtable { get; set; }

Contains settings for the Cloud Bigtable instance that will be created to serve featureValues for all FeatureViews under this FeatureOnlineStore.

**Property Value**  
---  
**Type** | **Description**  
`[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore.Types)[Bigtable](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore.Types.Bigtable)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Timestamp when this FeatureOnlineStore was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DedicatedServingEndpoint
    
    
    public FeatureOnlineStore.Types.DedicatedServingEndpoint DedicatedServingEndpoint { get; set; }

Optional. The dedicated serving endpoint for this FeatureOnlineStore, which is different from common Vertex service endpoint.

**Property Value**  
---  
**Type** | **Description**  
`[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore.Types)[DedicatedServingEndpoint](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore.Types.DedicatedServingEndpoint)` |   
  
### EmbeddingManagement
    
    
    [Obsolete]
    public FeatureOnlineStore.Types.EmbeddingManagement EmbeddingManagement { get; set; }

Optional. Deprecated: This field is no longer needed anymore and embedding management is automatically enabled when specifying Optimized storage type.

**Property Value**  
---  
**Type** | **Description**  
`[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore.Types)[EmbeddingManagement](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore.Types.EmbeddingManagement)` |   
  
### EncryptionSpec
    
    
    public EncryptionSpec EncryptionSpec { get; set; }

Optional. Customer-managed encryption key spec for data storage. If set, online store will be secured by this key.

**Property Value**  
---  
**Type** | **Description**  
`[EncryptionSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.EncryptionSpec)` |   
  
### Etag
    
    
    public string Etag { get; set; }

Optional. Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### FeatureOnlineStoreName
    
    
    public FeatureOnlineStoreName FeatureOnlineStoreName { get; set; }

[FeatureOnlineStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStoreName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore#Google_Cloud_AIPlatform_V1Beta1_FeatureOnlineStore_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[FeatureOnlineStoreName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStoreName)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Optional. The labels with user-defined metadata to organize your FeatureOnlineStore.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See <https://goo.gl/xmQnxf> for more information on and examples of labels. No more than 64 user labels can be associated with one FeatureOnlineStore(System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. Name of the FeatureOnlineStore. Format: `projects/{project}/locations/{location}/featureOnlineStores/{featureOnlineStore}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Optimized
    
    
    public FeatureOnlineStore.Types.Optimized Optimized { get; set; }

Contains settings for the Optimized store that will be created to serve featureValues for all FeatureViews under this FeatureOnlineStore. When choose Optimized storage type, need to set [PrivateServiceConnectConfig.enable_private_service_connect][google.cloud.aiplatform.v1beta1.PrivateServiceConnectConfig.enable_private_service_connect] to use private endpoint. Otherwise will use public endpoint by default.

**Property Value**  
---  
**Type** | **Description**  
`[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore.Types)[Optimized](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore.Types.Optimized)` |   
  
### SatisfiesPzi
    
    
    public bool SatisfiesPzi { get; set; }

Output only. Reserved for future use.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### SatisfiesPzs
    
    
    public bool SatisfiesPzs { get; set; }

Output only. Reserved for future use.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### State
    
    
    public FeatureOnlineStore.Types.State State { get; set; }

Output only. State of the featureOnlineStore.

**Property Value**  
---  
**Type** | **Description**  
`[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore.Types.State)` |   
  
### StorageTypeCase
    
    
    public FeatureOnlineStore.StorageTypeOneofCase StorageTypeCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[FeatureOnlineStore](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore)[StorageTypeOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStore.StorageTypeOneofCase)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. Timestamp when this FeatureOnlineStore was last updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
