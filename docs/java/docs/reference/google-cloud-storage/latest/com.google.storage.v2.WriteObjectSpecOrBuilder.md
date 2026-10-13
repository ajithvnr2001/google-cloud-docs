---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.WriteObjectSpecOrBuilder
title: Interface WriteObjectSpecOrBuilder (2.75.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:05:50.758425+00:00
---

# Interface WriteObjectSpecOrBuilder (2.75.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.WriteObjectSpecOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface WriteObjectSpecOrBuilder (2.75.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.75.0 (latest)  2.71.0  2.70.0  2.69.0  2.67.0  2.64.0  2.63.0  2.62.1  2.60.0  2.59.0  2.58.1  2.57.0  2.56.0  2.55.0  2.54.0  2.53.3  2.52.3  2.50.0  2.49.0  2.48.2  2.47.0  2.46.0  2.45.0  2.44.1  2.43.2  2.42.0  2.41.0  2.40.1  2.39.0  2.38.0  2.37.0  2.36.1  2.34.0  2.33.0  2.32.1  2.30.1  2.29.1  2.28.0  2.27.1  2.24.0  2.23.0  2.22.6  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.0  2.15.1  2.14.0  2.13.1  2.12.0  2.11.3  2.10.0  2.9.3  2.8.1  2.7.1  2.6.1  2.5.1  2.4.5  2.3.0  2.2.3  2.1.10 
    
    
    public interface WriteObjectSpecOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAppendable()
    
    
    public abstract boolean getAppendable()

If `true`, the object is created in appendable mode. This field might only be set when using `BidiWriteObject`.

`optional bool appendable = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The appendable.  
  
### getIfGenerationMatch()
    
    
    public abstract long getIfGenerationMatch()

Makes the operation conditional on whether the object's current generation matches the given value. Setting to `0` makes the operation succeed only if there are no live versions of the object.

`optional int64 if_generation_match = 3;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The ifGenerationMatch.  
  
### getIfGenerationNotMatch()
    
    
    public abstract long getIfGenerationNotMatch()

Makes the operation conditional on whether the object's live generation does not match the given value. If no live object exists, the precondition fails. Setting to `0` makes the operation succeed only if there is a live version of the object.

`optional int64 if_generation_not_match = 4;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The ifGenerationNotMatch.  
  
### getIfMetagenerationMatch()
    
    
    public abstract long getIfMetagenerationMatch()

Makes the operation conditional on whether the object's current metageneration matches the given value.

`optional int64 if_metageneration_match = 5;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The ifMetagenerationMatch.  
  
### getIfMetagenerationNotMatch()
    
    
    public abstract long getIfMetagenerationNotMatch()

Makes the operation conditional on whether the object's current metageneration does not match the given value.

`optional int64 if_metageneration_not_match = 6;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The ifMetagenerationNotMatch.  
  
### getObjectSize()
    
    
    public abstract long getObjectSize()

The expected final object size being uploaded. If this value is set, closing the stream after writing fewer or more than `object_size` bytes results in an `OUT_OF_RANGE` error.

This situation is considered a client error, and if such an error occurs you must start the upload over from scratch, this time sending the correct number of bytes.

`optional int64 object_size = 8;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The objectSize.  
  
### getPredefinedAcl()
    
    
    public abstract String getPredefinedAcl()

Optional. Apply a predefined set of access controls to this object. Valid values are `authenticatedRead`, `bucketOwnerFullControl`, `bucketOwnerRead`, `private`, `projectPrivate`, or `publicRead`.

`string predefined_acl = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The predefinedAcl.  
  
### getPredefinedAclBytes()
    
    
    public abstract ByteString getPredefinedAclBytes()

Optional. Apply a predefined set of access controls to this object. Valid values are `authenticatedRead`, `bucketOwnerFullControl`, `bucketOwnerRead`, `private`, `projectPrivate`, or `publicRead`.

`string predefined_acl = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for predefinedAcl.  
  
### getResource()
    
    
    public abstract Object getResource()

Required. Destination object, including its name and its metadata.

`.google.storage.v2.Object resource = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[Object](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.Object)` | The resource.  
  
### getResourceOrBuilder()
    
    
    public abstract ObjectOrBuilder getResourceOrBuilder()

Required. Destination object, including its name and its metadata.

`.google.storage.v2.Object resource = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ObjectOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.ObjectOrBuilder)` |   
  
### hasAppendable()
    
    
    public abstract boolean hasAppendable()

If `true`, the object is created in appendable mode. This field might only be set when using `BidiWriteObject`.

`optional bool appendable = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the appendable field is set.  
  
### hasIfGenerationMatch()
    
    
    public abstract boolean hasIfGenerationMatch()

Makes the operation conditional on whether the object's current generation matches the given value. Setting to `0` makes the operation succeed only if there are no live versions of the object.

`optional int64 if_generation_match = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the ifGenerationMatch field is set.  
  
### hasIfGenerationNotMatch()
    
    
    public abstract boolean hasIfGenerationNotMatch()

Makes the operation conditional on whether the object's live generation does not match the given value. If no live object exists, the precondition fails. Setting to `0` makes the operation succeed only if there is a live version of the object.

`optional int64 if_generation_not_match = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the ifGenerationNotMatch field is set.  
  
### hasIfMetagenerationMatch()
    
    
    public abstract boolean hasIfMetagenerationMatch()

Makes the operation conditional on whether the object's current metageneration matches the given value.

`optional int64 if_metageneration_match = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the ifMetagenerationMatch field is set.  
  
### hasIfMetagenerationNotMatch()
    
    
    public abstract boolean hasIfMetagenerationNotMatch()

Makes the operation conditional on whether the object's current metageneration does not match the given value.

`optional int64 if_metageneration_not_match = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the ifMetagenerationNotMatch field is set.  
  
### hasObjectSize()
    
    
    public abstract boolean hasObjectSize()

The expected final object size being uploaded. If this value is set, closing the stream after writing fewer or more than `object_size` bytes results in an `OUT_OF_RANGE` error.

This situation is considered a client error, and if such an error occurs you must start the upload over from scratch, this time sending the correct number of bytes.

`optional int64 object_size = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the objectSize field is set.  
  
### hasResource()
    
    
    public abstract boolean hasResource()

Required. Destination object, including its name and its metadata.

`.google.storage.v2.Object resource = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the resource field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
