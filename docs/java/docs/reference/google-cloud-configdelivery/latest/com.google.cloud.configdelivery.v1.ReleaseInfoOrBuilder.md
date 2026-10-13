---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1.ReleaseInfoOrBuilder
title: Interface ReleaseInfoOrBuilder (0.33.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:16.797346+00:00
---

# Interface ReleaseInfoOrBuilder (0.33.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1.ReleaseInfoOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ReleaseInfoOrBuilder (0.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.33.0 (latest)  0.29.0  0.28.0  0.27.0  0.25.0  0.22.0  0.21.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.4.0  0.2.0  0.1.0 
    
    
    public interface ReleaseInfoOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsVariantOciImagePaths(String key)
    
    
    public abstract boolean containsVariantOciImagePaths(String key)

Optional. per-variant paths to the oci images the service uploads on package release creation

` map<string, string> variant_oci_image_paths = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getOciImagePath()
    
    
    public abstract String getOciImagePath()

Output only. path to the oci image the service uploads to on a `Release` creation.

`string oci_image_path = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The ociImagePath.  
  
### getOciImagePathBytes()
    
    
    public abstract ByteString getOciImagePathBytes()

Output only. path to the oci image the service uploads to on a `Release` creation.

`string oci_image_path = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for ociImagePath.  
  
### getVariantOciImagePaths() (deprecated)
    
    
    public abstract Map<String,String> getVariantOciImagePaths()

Use [#getVariantOciImagePathsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1.ReleaseInfoOrBuilder#com_google_cloud_configdelivery_v1_ReleaseInfoOrBuilder_getVariantOciImagePathsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getVariantOciImagePathsCount()
    
    
    public abstract int getVariantOciImagePathsCount()

Optional. per-variant paths to the oci images the service uploads on package release creation

` map<string, string> variant_oci_image_paths = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getVariantOciImagePathsMap()
    
    
    public abstract Map<String,String> getVariantOciImagePathsMap()

Optional. per-variant paths to the oci images the service uploads on package release creation

` map<string, string> variant_oci_image_paths = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getVariantOciImagePathsOrDefault(String key, String defaultValue)
    
    
    public abstract String getVariantOciImagePathsOrDefault(String key, String defaultValue)

Optional. per-variant paths to the oci images the service uploads on package release creation

` map<string, string> variant_oci_image_paths = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getVariantOciImagePathsOrThrow(String key)
    
    
    public abstract String getVariantOciImagePathsOrThrow(String key)

Optional. per-variant paths to the oci images the service uploads on package release creation

` map<string, string> variant_oci_image_paths = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
