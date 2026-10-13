---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-functions/latest/com.google.cloud.functions.v1.OperationMetadataV1OrBuilder
title: Interface OperationMetadataV1OrBuilder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:06:28.349782+00:00
---

# Interface OperationMetadataV1OrBuilder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-functions/latest/com.google.cloud.functions.v1.OperationMetadataV1OrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface OperationMetadataV1OrBuilder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.83.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.4  2.4.3  2.3.6 
    
    
    public interface OperationMetadataV1OrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBuildId()
    
    
    public abstract String getBuildId()

The Cloud Build ID of the function created or updated by an API call. This field is only populated for Create and Update operations.

`string build_id = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The buildId.  
  
### getBuildIdBytes()
    
    
    public abstract ByteString getBuildIdBytes()

The Cloud Build ID of the function created or updated by an API call. This field is only populated for Create and Update operations.

`string build_id = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for buildId.  
  
### getBuildName()
    
    
    public abstract String getBuildName()

The Cloud Build Name of the function deployment. This field is only populated for Create and Update operations. `projects/<project-number>/locations/<region>/builds/<build-id>`.

`string build_name = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The buildName.  
  
### getBuildNameBytes()
    
    
    public abstract ByteString getBuildNameBytes()

The Cloud Build Name of the function deployment. This field is only populated for Create and Update operations. `projects/<project-number>/locations/<region>/builds/<build-id>`.

`string build_name = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for buildName.  
  
### getRequest()
    
    
    public abstract Any getRequest()

The original request that started the operation.

`.google.protobuf.Any request = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Any](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Any.html)` | The request.  
  
### getRequestOrBuilder()
    
    
    public abstract AnyOrBuilder getRequestOrBuilder()

The original request that started the operation.

`.google.protobuf.Any request = 3;`

**Returns**  
---  
**Type** | **Description**  
`[AnyOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AnyOrBuilder.html)` |   
  
### getSourceToken()
    
    
    public abstract String getSourceToken()

An identifier for Firebase function sources. Disclaimer: This field is only supported for Firebase function deployments.

`string source_token = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The sourceToken.  
  
### getSourceTokenBytes()
    
    
    public abstract ByteString getSourceTokenBytes()

An identifier for Firebase function sources. Disclaimer: This field is only supported for Firebase function deployments.

`string source_token = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for sourceToken.  
  
### getTarget()
    
    
    public abstract String getTarget()

Target of the operation - for example `projects/project-1/locations/region-1/functions/function-1`

`string target = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The target.  
  
### getTargetBytes()
    
    
    public abstract ByteString getTargetBytes()

Target of the operation - for example `projects/project-1/locations/region-1/functions/function-1`

`string target = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for target.  
  
### getType()
    
    
    public abstract OperationType getType()

Type of operation.

`.google.cloud.functions.v1.OperationType type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[OperationType](https://docs.cloud.google.com/java/docs/reference/google-cloud-functions/latest/com.google.cloud.functions.v1.OperationType)` | The type.  
  
### getTypeValue()
    
    
    public abstract int getTypeValue()

Type of operation.

`.google.cloud.functions.v1.OperationType type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for type.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

The last update timestamp of the operation.

`.google.protobuf.Timestamp update_time = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

The last update timestamp of the operation.

`.google.protobuf.Timestamp update_time = 5;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getVersionId()
    
    
    public abstract long getVersionId()

Version id of the function created or updated by an API call. This field is only populated for Create and Update operations.

`int64 version_id = 4;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The versionId.  
  
### hasRequest()
    
    
    public abstract boolean hasRequest()

The original request that started the operation.

`.google.protobuf.Any request = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the request field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

The last update timestamp of the operation.

`.google.protobuf.Timestamp update_time = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
