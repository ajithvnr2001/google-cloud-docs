---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.UpdateFolderIntelligenceConfigRequestOrBuilder
title: Interface UpdateFolderIntelligenceConfigRequestOrBuilder (2.75.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:10:36.182719+00:00
---

# Interface UpdateFolderIntelligenceConfigRequestOrBuilder (2.75.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.UpdateFolderIntelligenceConfigRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface UpdateFolderIntelligenceConfigRequestOrBuilder (2.75.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.75.0 (latest)  2.71.0  2.70.0  2.69.0  2.67.0  2.64.0  2.63.0  2.62.1  2.60.0  2.59.0  2.58.1  2.57.0  2.56.0  2.55.0  2.54.0  2.53.3  2.52.3  2.50.0  2.49.0  2.48.2  2.47.0  2.46.0  2.45.0  2.44.1  2.43.2  2.42.0  2.41.0  2.40.1  2.39.0  2.38.0  2.37.0  2.36.1  2.34.0  2.33.0  2.32.1  2.30.1  2.29.1  2.28.0  2.27.1  2.24.0  2.23.0  2.22.6  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.0  2.15.1  2.14.0  2.13.1  2.12.0  2.11.3  2.10.0  2.9.3  2.8.1  2.7.1  2.6.1  2.5.1  2.4.5  2.3.0  2.2.3  2.1.10 
    
    
    public interface UpdateFolderIntelligenceConfigRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getIntelligenceConfig()
    
    
    public abstract IntelligenceConfig getIntelligenceConfig()

Required. The `IntelligenceConfig` resource to be updated.

` .google.storage.control.v2.IntelligenceConfig intelligence_config = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[IntelligenceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.IntelligenceConfig)` | The intelligenceConfig.  
  
### getIntelligenceConfigOrBuilder()
    
    
    public abstract IntelligenceConfigOrBuilder getIntelligenceConfigOrBuilder()

Required. The `IntelligenceConfig` resource to be updated.

` .google.storage.control.v2.IntelligenceConfig intelligence_config = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[IntelligenceConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.IntelligenceConfigOrBuilder)` |   
  
### getRequestId()
    
    
    public abstract String getRequestId()

Optional. The ID that uniquely identifies the request, preventing duplicate processing.

` string request_id = 3 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The requestId.  
  
### getRequestIdBytes()
    
    
    public abstract ByteString getRequestIdBytes()

Optional. The ID that uniquely identifies the request, preventing duplicate processing.

` string request_id = 3 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for requestId.  
  
### getUpdateMask()
    
    
    public abstract FieldMask getUpdateMask()

Required. The `update_mask` that specifies the fields within the `IntelligenceConfig` resource that should be modified by this update. Only the listed fields are updated.

`.google.protobuf.FieldMask update_mask = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)` | The updateMask.  
  
### getUpdateMaskOrBuilder()
    
    
    public abstract FieldMaskOrBuilder getUpdateMaskOrBuilder()

Required. The `update_mask` that specifies the fields within the `IntelligenceConfig` resource that should be modified by this update. Only the listed fields are updated.

`.google.protobuf.FieldMask update_mask = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[FieldMaskOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMaskOrBuilder.html)` |   
  
### hasIntelligenceConfig()
    
    
    public abstract boolean hasIntelligenceConfig()

Required. The `IntelligenceConfig` resource to be updated.

` .google.storage.control.v2.IntelligenceConfig intelligence_config = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the intelligenceConfig field is set.  
  
### hasUpdateMask()
    
    
    public abstract boolean hasUpdateMask()

Required. The `update_mask` that specifies the fields within the `IntelligenceConfig` resource that should be modified by this update. Only the listed fields are updated.

`.google.protobuf.FieldMask update_mask = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateMask field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
