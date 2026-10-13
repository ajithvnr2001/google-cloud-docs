---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.MoveObjectRequestOrBuilder
title: Interface MoveObjectRequestOrBuilder (2.75.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:27:22.781744+00:00
---

# Interface MoveObjectRequestOrBuilder (2.75.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.MoveObjectRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface MoveObjectRequestOrBuilder (2.75.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.75.0 (latest)  2.71.0  2.70.0  2.69.0  2.67.0  2.64.0  2.63.0  2.62.1  2.60.0  2.59.0  2.58.1  2.57.0  2.56.0  2.55.0  2.54.0  2.53.3  2.52.3  2.50.0  2.49.0  2.48.2  2.47.0  2.46.0  2.45.0  2.44.1  2.43.2  2.42.0  2.41.0  2.40.1  2.39.0  2.38.0  2.37.0  2.36.1  2.34.0  2.33.0  2.32.1  2.30.1  2.29.1  2.28.0  2.27.1  2.24.0  2.23.0  2.22.6  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.0  2.15.1  2.14.0  2.13.1  2.12.0  2.11.3  2.10.0  2.9.3  2.8.1  2.7.1  2.6.1  2.5.1  2.4.5  2.3.0  2.2.3  2.1.10 
    
    
    public interface MoveObjectRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBucket()
    
    
    public abstract String getBucket()

Required. Name of the bucket in which the object resides.

` string bucket = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The bucket.  
  
### getBucketBytes()
    
    
    public abstract ByteString getBucketBytes()

Required. Name of the bucket in which the object resides.

` string bucket = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for bucket.  
  
### getDestinationObject()
    
    
    public abstract String getDestinationObject()

Required. Name of the destination object.

`string destination_object = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The destinationObject.  
  
### getDestinationObjectBytes()
    
    
    public abstract ByteString getDestinationObjectBytes()

Required. Name of the destination object.

`string destination_object = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for destinationObject.  
  
### getIfGenerationMatch()
    
    
    public abstract long getIfGenerationMatch()

Optional. Makes the operation conditional on whether the destination object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object. `if_generation_match` and `if_generation_not_match` conditions are mutually exclusive: it's an error for both of them to be set in the request.

`optional int64 if_generation_match = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The ifGenerationMatch.  
  
### getIfGenerationNotMatch()
    
    
    public abstract long getIfGenerationNotMatch()

Optional. Makes the operation conditional on whether the destination object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object. `if_generation_match` and `if_generation_not_match` conditions are mutually exclusive: it's an error for both of them to be set in the request.

`optional int64 if_generation_not_match = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The ifGenerationNotMatch.  
  
### getIfMetagenerationMatch()
    
    
    public abstract long getIfMetagenerationMatch()

Optional. Makes the operation conditional on whether the destination object's current metageneration matches the given value. `if_metageneration_match` and `if_metageneration_not_match` conditions are mutually exclusive: it's an error for both of them to be set in the request.

`optional int64 if_metageneration_match = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The ifMetagenerationMatch.  
  
### getIfMetagenerationNotMatch()
    
    
    public abstract long getIfMetagenerationNotMatch()

Optional. Makes the operation conditional on whether the destination object's current metageneration does not match the given value. `if_metageneration_match` and `if_metageneration_not_match` conditions are mutually exclusive: it's an error for both of them to be set in the request.

` optional int64 if_metageneration_not_match = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The ifMetagenerationNotMatch.  
  
### getIfSourceGenerationMatch()
    
    
    public abstract long getIfSourceGenerationMatch()

Optional. Makes the operation conditional on whether the source object's current generation matches the given value. `if_source_generation_match` and `if_source_generation_not_match` conditions are mutually exclusive: it's an error for both of them to be set in the request.

`optional int64 if_source_generation_match = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The ifSourceGenerationMatch.  
  
### getIfSourceGenerationNotMatch()
    
    
    public abstract long getIfSourceGenerationNotMatch()

Optional. Makes the operation conditional on whether the source object's current generation does not match the given value. `if_source_generation_match` and `if_source_generation_not_match` conditions are mutually exclusive: it's an error for both of them to be set in the request.

` optional int64 if_source_generation_not_match = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The ifSourceGenerationNotMatch.  
  
### getIfSourceMetagenerationMatch()
    
    
    public abstract long getIfSourceMetagenerationMatch()

Optional. Makes the operation conditional on whether the source object's current metageneration matches the given value. `if_source_metageneration_match` and `if_source_metageneration_not_match` conditions are mutually exclusive: it's an error for both of them to be set in the request.

` optional int64 if_source_metageneration_match = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The ifSourceMetagenerationMatch.  
  
### getIfSourceMetagenerationNotMatch()
    
    
    public abstract long getIfSourceMetagenerationNotMatch()

Optional. Makes the operation conditional on whether the source object's current metageneration does not match the given value. `if_source_metageneration_match` and `if_source_metageneration_not_match` conditions are mutually exclusive: it's an error for both of them to be set in the request.

` optional int64 if_source_metageneration_not_match = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The ifSourceMetagenerationNotMatch.  
  
### getSourceObject()
    
    
    public abstract String getSourceObject()

Required. Name of the source object.

`string source_object = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The sourceObject.  
  
### getSourceObjectBytes()
    
    
    public abstract ByteString getSourceObjectBytes()

Required. Name of the source object.

`string source_object = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for sourceObject.  
  
### hasIfGenerationMatch()
    
    
    public abstract boolean hasIfGenerationMatch()

Optional. Makes the operation conditional on whether the destination object's current generation matches the given value. Setting to 0 makes the operation succeed only if there are no live versions of the object. `if_generation_match` and `if_generation_not_match` conditions are mutually exclusive: it's an error for both of them to be set in the request.

`optional int64 if_generation_match = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the ifGenerationMatch field is set.  
  
### hasIfGenerationNotMatch()
    
    
    public abstract boolean hasIfGenerationNotMatch()

Optional. Makes the operation conditional on whether the destination object's current generation does not match the given value. If no live object exists, the precondition fails. Setting to 0 makes the operation succeed only if there is a live version of the object. `if_generation_match` and `if_generation_not_match` conditions are mutually exclusive: it's an error for both of them to be set in the request.

`optional int64 if_generation_not_match = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the ifGenerationNotMatch field is set.  
  
### hasIfMetagenerationMatch()
    
    
    public abstract boolean hasIfMetagenerationMatch()

Optional. Makes the operation conditional on whether the destination object's current metageneration matches the given value. `if_metageneration_match` and `if_metageneration_not_match` conditions are mutually exclusive: it's an error for both of them to be set in the request.

`optional int64 if_metageneration_match = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the ifMetagenerationMatch field is set.  
  
### hasIfMetagenerationNotMatch()
    
    
    public abstract boolean hasIfMetagenerationNotMatch()

Optional. Makes the operation conditional on whether the destination object's current metageneration does not match the given value. `if_metageneration_match` and `if_metageneration_not_match` conditions are mutually exclusive: it's an error for both of them to be set in the request.

` optional int64 if_metageneration_not_match = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the ifMetagenerationNotMatch field is set.  
  
### hasIfSourceGenerationMatch()
    
    
    public abstract boolean hasIfSourceGenerationMatch()

Optional. Makes the operation conditional on whether the source object's current generation matches the given value. `if_source_generation_match` and `if_source_generation_not_match` conditions are mutually exclusive: it's an error for both of them to be set in the request.

`optional int64 if_source_generation_match = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the ifSourceGenerationMatch field is set.  
  
### hasIfSourceGenerationNotMatch()
    
    
    public abstract boolean hasIfSourceGenerationNotMatch()

Optional. Makes the operation conditional on whether the source object's current generation does not match the given value. `if_source_generation_match` and `if_source_generation_not_match` conditions are mutually exclusive: it's an error for both of them to be set in the request.

` optional int64 if_source_generation_not_match = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the ifSourceGenerationNotMatch field is set.  
  
### hasIfSourceMetagenerationMatch()
    
    
    public abstract boolean hasIfSourceMetagenerationMatch()

Optional. Makes the operation conditional on whether the source object's current metageneration matches the given value. `if_source_metageneration_match` and `if_source_metageneration_not_match` conditions are mutually exclusive: it's an error for both of them to be set in the request.

` optional int64 if_source_metageneration_match = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the ifSourceMetagenerationMatch field is set.  
  
### hasIfSourceMetagenerationNotMatch()
    
    
    public abstract boolean hasIfSourceMetagenerationNotMatch()

Optional. Makes the operation conditional on whether the source object's current metageneration does not match the given value. `if_source_metageneration_match` and `if_source_metageneration_not_match` conditions are mutually exclusive: it's an error for both of them to be set in the request.

` optional int64 if_source_metageneration_not_match = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the ifSourceMetagenerationNotMatch field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
