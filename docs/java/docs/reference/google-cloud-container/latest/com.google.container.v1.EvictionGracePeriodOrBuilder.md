---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.EvictionGracePeriodOrBuilder
title: Interface EvictionGracePeriodOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:42:20.401544+00:00
---

# Interface EvictionGracePeriodOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.EvictionGracePeriodOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface EvictionGracePeriodOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public interface EvictionGracePeriodOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getImagefsAvailable()
    
    
    public abstract String getImagefsAvailable()

Optional. Grace period for eviction due to imagefs available signal. Sample format: "10s". Must be >= 0. See <https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/#eviction-signals>

`string imagefs_available = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The imagefsAvailable.  
  
### getImagefsAvailableBytes()
    
    
    public abstract ByteString getImagefsAvailableBytes()

Optional. Grace period for eviction due to imagefs available signal. Sample format: "10s". Must be >= 0. See <https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/#eviction-signals>

`string imagefs_available = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for imagefsAvailable.  
  
### getImagefsInodesFree()
    
    
    public abstract String getImagefsInodesFree()

Optional. Grace period for eviction due to imagefs inodes free signal. Sample format: "10s". Must be >= 0. See <https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/#eviction-signals>

`string imagefs_inodes_free = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The imagefsInodesFree.  
  
### getImagefsInodesFreeBytes()
    
    
    public abstract ByteString getImagefsInodesFreeBytes()

Optional. Grace period for eviction due to imagefs inodes free signal. Sample format: "10s". Must be >= 0. See <https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/#eviction-signals>

`string imagefs_inodes_free = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for imagefsInodesFree.  
  
### getMemoryAvailable()
    
    
    public abstract String getMemoryAvailable()

Optional. Grace period for eviction due to memory available signal. Sample format: "10s". Must be >= 0. See <https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/#eviction-signals>

`string memory_available = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The memoryAvailable.  
  
### getMemoryAvailableBytes()
    
    
    public abstract ByteString getMemoryAvailableBytes()

Optional. Grace period for eviction due to memory available signal. Sample format: "10s". Must be >= 0. See <https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/#eviction-signals>

`string memory_available = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for memoryAvailable.  
  
### getNodefsAvailable()
    
    
    public abstract String getNodefsAvailable()

Optional. Grace period for eviction due to nodefs available signal. Sample format: "10s". Must be >= 0. See <https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/#eviction-signals>

`string nodefs_available = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nodefsAvailable.  
  
### getNodefsAvailableBytes()
    
    
    public abstract ByteString getNodefsAvailableBytes()

Optional. Grace period for eviction due to nodefs available signal. Sample format: "10s". Must be >= 0. See <https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/#eviction-signals>

`string nodefs_available = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nodefsAvailable.  
  
### getNodefsInodesFree()
    
    
    public abstract String getNodefsInodesFree()

Optional. Grace period for eviction due to nodefs inodes free signal. Sample format: "10s". Must be >= 0. See <https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/#eviction-signals>

`string nodefs_inodes_free = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nodefsInodesFree.  
  
### getNodefsInodesFreeBytes()
    
    
    public abstract ByteString getNodefsInodesFreeBytes()

Optional. Grace period for eviction due to nodefs inodes free signal. Sample format: "10s". Must be >= 0. See <https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/#eviction-signals>

`string nodefs_inodes_free = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nodefsInodesFree.  
  
### getPidAvailable()
    
    
    public abstract String getPidAvailable()

Optional. Grace period for eviction due to pid available signal. Sample format: "10s". Must be >= 0. See <https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/#eviction-signals>

`string pid_available = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pidAvailable.  
  
### getPidAvailableBytes()
    
    
    public abstract ByteString getPidAvailableBytes()

Optional. Grace period for eviction due to pid available signal. Sample format: "10s". Must be >= 0. See <https://kubernetes.io/docs/concepts/scheduling-eviction/node-pressure-eviction/#eviction-signals>

`string pid_available = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pidAvailable.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
