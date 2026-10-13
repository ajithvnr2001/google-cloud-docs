---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PreviewFeatureOrBuilder
title: Interface PreviewFeatureOrBuilder (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:13.266281+00:00
---

# Interface PreviewFeatureOrBuilder (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PreviewFeatureOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PreviewFeatureOrBuilder (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public interface PreviewFeatureOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getActivationStatus()
    
    
    public abstract String getActivationStatus()

Specifies whether the feature is enabled or disabled. Check the ActivationStatus enum for the list of possible values.

`optional string activation_status = 71960379;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The activationStatus.  
  
### getActivationStatusBytes()
    
    
    public abstract ByteString getActivationStatusBytes()

Specifies whether the feature is enabled or disabled. Check the ActivationStatus enum for the list of possible values.

`optional string activation_status = 71960379;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for activationStatus.  
  
### getCreationTimestamp()
    
    
    public abstract String getCreationTimestamp()

Output only. [Output Only] Creation timestamp inRFC3339 text format.

`optional string creation_timestamp = 30525366;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The creationTimestamp.  
  
### getCreationTimestampBytes()
    
    
    public abstract ByteString getCreationTimestampBytes()

Output only. [Output Only] Creation timestamp inRFC3339 text format.

`optional string creation_timestamp = 30525366;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for creationTimestamp.  
  
### getDescription()
    
    
    public abstract String getDescription()

Output only. [Output Only] Description of the feature.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Output only. [Output Only] Description of the feature.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getId()
    
    
    public abstract long getId()

Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server.

`optional uint64 id = 3355;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The id.  
  
### getKind()
    
    
    public abstract String getKind()

Output only. [Output only] The type of the feature. Always "compute#previewFeature" for preview features.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kind.  
  
### getKindBytes()
    
    
    public abstract ByteString getKindBytes()

Output only. [Output only] The type of the feature. Always "compute#previewFeature" for preview features.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kind.  
  
### getName()
    
    
    public abstract String getName()

Name of the feature.

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Name of the feature.

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getRolloutOperation()
    
    
    public abstract PreviewFeatureRolloutOperation getRolloutOperation()

Rollout operation of the feature.

` optional .google.cloud.compute.v1.PreviewFeatureRolloutOperation rollout_operation = 486746201; `

**Returns**  
---  
**Type** | **Description**  
`[PreviewFeatureRolloutOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PreviewFeatureRolloutOperation)` | The rolloutOperation.  
  
### getRolloutOperationOrBuilder()
    
    
    public abstract PreviewFeatureRolloutOperationOrBuilder getRolloutOperationOrBuilder()

Rollout operation of the feature.

` optional .google.cloud.compute.v1.PreviewFeatureRolloutOperation rollout_operation = 486746201; `

**Returns**  
---  
**Type** | **Description**  
`[PreviewFeatureRolloutOperationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PreviewFeatureRolloutOperationOrBuilder)` |   
  
### getSelfLink()
    
    
    public abstract String getSelfLink()

Output only. [Output Only] Server-defined URL for the resource.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The selfLink.  
  
### getSelfLinkBytes()
    
    
    public abstract ByteString getSelfLinkBytes()

Output only. [Output Only] Server-defined URL for the resource.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for selfLink.  
  
### getStatus()
    
    
    public abstract PreviewFeatureStatus getStatus()

Output only. [Output only] Status of the feature.

`optional .google.cloud.compute.v1.PreviewFeatureStatus status = 181260274;`

**Returns**  
---  
**Type** | **Description**  
`[PreviewFeatureStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PreviewFeatureStatus)` | The status.  
  
### getStatusOrBuilder()
    
    
    public abstract PreviewFeatureStatusOrBuilder getStatusOrBuilder()

Output only. [Output only] Status of the feature.

`optional .google.cloud.compute.v1.PreviewFeatureStatus status = 181260274;`

**Returns**  
---  
**Type** | **Description**  
`[PreviewFeatureStatusOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PreviewFeatureStatusOrBuilder)` |   
  
### hasActivationStatus()
    
    
    public abstract boolean hasActivationStatus()

Specifies whether the feature is enabled or disabled. Check the ActivationStatus enum for the list of possible values.

`optional string activation_status = 71960379;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the activationStatus field is set.  
  
### hasCreationTimestamp()
    
    
    public abstract boolean hasCreationTimestamp()

Output only. [Output Only] Creation timestamp inRFC3339 text format.

`optional string creation_timestamp = 30525366;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the creationTimestamp field is set.  
  
### hasDescription()
    
    
    public abstract boolean hasDescription()

Output only. [Output Only] Description of the feature.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the description field is set.  
  
### hasId()
    
    
    public abstract boolean hasId()

Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server.

`optional uint64 id = 3355;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the id field is set.  
  
### hasKind()
    
    
    public abstract boolean hasKind()

Output only. [Output only] The type of the feature. Always "compute#previewFeature" for preview features.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the kind field is set.  
  
### hasName()
    
    
    public abstract boolean hasName()

Name of the feature.

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the name field is set.  
  
### hasRolloutOperation()
    
    
    public abstract boolean hasRolloutOperation()

Rollout operation of the feature.

` optional .google.cloud.compute.v1.PreviewFeatureRolloutOperation rollout_operation = 486746201; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rolloutOperation field is set.  
  
### hasSelfLink()
    
    
    public abstract boolean hasSelfLink()

Output only. [Output Only] Server-defined URL for the resource.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the selfLink field is set.  
  
### hasStatus()
    
    
    public abstract boolean hasStatus()

Output only. [Output only] Status of the feature.

`optional .google.cloud.compute.v1.PreviewFeatureStatus status = 181260274;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the status field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
