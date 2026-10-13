---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-infra-manager/latest/com.google.cloud.config.v1.LockInfoOrBuilder
title: Interface LockInfoOrBuilder (0.76.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:11.878262+00:00
---

# Interface LockInfoOrBuilder (0.76.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-infra-manager/latest/com.google.cloud.config.v1.LockInfoOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface LockInfoOrBuilder (0.76.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.76.0 (latest)  0.72.0  0.71.0  0.70.0  0.68.0  0.65.0  0.64.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.55.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.47.0  0.45.0  0.44.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.1.0 
    
    
    public interface LockInfoOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Time that the lock was taken.

`.google.protobuf.Timestamp create_time = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Time that the lock was taken.

`.google.protobuf.Timestamp create_time = 6;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getInfo()
    
    
    public abstract String getInfo()

Extra information to store with the lock, provided by the caller.

`string info = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The info.  
  
### getInfoBytes()
    
    
    public abstract ByteString getInfoBytes()

Extra information to store with the lock, provided by the caller.

`string info = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for info.  
  
### getLockId()
    
    
    public abstract long getLockId()

Unique ID for the lock to be overridden with generation ID in the backend.

`int64 lock_id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The lockId.  
  
### getOperation()
    
    
    public abstract String getOperation()

Terraform operation, provided by the caller.

`string operation = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The operation.  
  
### getOperationBytes()
    
    
    public abstract ByteString getOperationBytes()

Terraform operation, provided by the caller.

`string operation = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for operation.  
  
### getVersion()
    
    
    public abstract String getVersion()

Terraform version

`string version = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The version.  
  
### getVersionBytes()
    
    
    public abstract ByteString getVersionBytes()

Terraform version

`string version = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for version.  
  
### getWho()
    
    
    public abstract String getWho()

user@hostname when available

`string who = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The who.  
  
### getWhoBytes()
    
    
    public abstract ByteString getWhoBytes()

user@hostname when available

`string who = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for who.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Time that the lock was taken.

`.google.protobuf.Timestamp create_time = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
