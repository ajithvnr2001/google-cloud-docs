---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.AssetOrBuilder
title: Interface AssetOrBuilder (0.56.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:16:20.024653+00:00
---

# Interface AssetOrBuilder (0.56.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.AssetOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AssetOrBuilder (0.56.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.56.0 (latest)  0.52.0  0.51.0  0.50.0  0.48.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.37.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.27.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface AssetOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAssetGcsSource()
    
    
    public abstract AssetSource.AssetGcsSource getAssetGcsSource()

Output only. The original cloud storage source uri that is associated with this asset.

` .google.cloud.visionai.v1.AssetSource.AssetGcsSource asset_gcs_source = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AssetSource.AssetGcsSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.AssetSource.AssetGcsSource)` | The assetGcsSource.  
  
### getAssetGcsSourceOrBuilder()
    
    
    public abstract AssetSource.AssetGcsSourceOrBuilder getAssetGcsSourceOrBuilder()

Output only. The original cloud storage source uri that is associated with this asset.

` .google.cloud.visionai.v1.AssetSource.AssetGcsSource asset_gcs_source = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AssetSource.AssetGcsSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-visionai/latest/com.google.cloud.visionai.v1.AssetSource.AssetGcsSourceOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Resource name of the asset. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/assets/{asset_id}`

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Resource name of the asset. Format: `projects/{project_number}/locations/{location_id}/corpora/{corpus_id}/assets/{asset_id}`

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getTtl()
    
    
    public abstract Duration getTtl()

The duration for which all media assets, associated metadata, and search documents can exist. If not set, then it will using the default ttl in the parent corpus resource.

`.google.protobuf.Duration ttl = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The ttl.  
  
### getTtlOrBuilder()
    
    
    public abstract DurationOrBuilder getTtlOrBuilder()

The duration for which all media assets, associated metadata, and search documents can exist. If not set, then it will using the default ttl in the parent corpus resource.

`.google.protobuf.Duration ttl = 2;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### hasAssetGcsSource()
    
    
    public abstract boolean hasAssetGcsSource()

Output only. The original cloud storage source uri that is associated with this asset.

` .google.cloud.visionai.v1.AssetSource.AssetGcsSource asset_gcs_source = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the assetGcsSource field is set.  
  
### hasTtl()
    
    
    public abstract boolean hasTtl()

The duration for which all media assets, associated metadata, and search documents can exist. If not set, then it will using the default ttl in the parent corpus resource.

`.google.protobuf.Duration ttl = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the ttl field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
