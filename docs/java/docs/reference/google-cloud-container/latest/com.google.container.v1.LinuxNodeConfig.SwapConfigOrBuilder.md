---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.SwapConfigOrBuilder
title: Interface LinuxNodeConfig.SwapConfigOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:42:35.238135+00:00
---

# Interface LinuxNodeConfig.SwapConfigOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.SwapConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface LinuxNodeConfig.SwapConfigOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public static interface LinuxNodeConfig.SwapConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBootDiskProfile()
    
    
    public abstract LinuxNodeConfig.SwapConfig.BootDiskProfile getBootDiskProfile()

Swap on the node's boot disk.

`.google.container.v1.LinuxNodeConfig.SwapConfig.BootDiskProfile boot_disk_profile = 3; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.SwapConfig.BootDiskProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.SwapConfig.BootDiskProfile)` | The bootDiskProfile.  
  
### getBootDiskProfileOrBuilder()
    
    
    public abstract LinuxNodeConfig.SwapConfig.BootDiskProfileOrBuilder getBootDiskProfileOrBuilder()

Swap on the node's boot disk.

`.google.container.v1.LinuxNodeConfig.SwapConfig.BootDiskProfile boot_disk_profile = 3; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.SwapConfig.BootDiskProfileOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.SwapConfig.BootDiskProfileOrBuilder)` |   
  
### getDedicatedLocalSsdProfile()
    
    
    public abstract LinuxNodeConfig.SwapConfig.DedicatedLocalSsdProfile getDedicatedLocalSsdProfile()

Provisions a new, separate local NVMe SSD exclusively for swap.

` .google.container.v1.LinuxNodeConfig.SwapConfig.DedicatedLocalSsdProfile dedicated_local_ssd_profile = 5; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.SwapConfig.DedicatedLocalSsdProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.SwapConfig.DedicatedLocalSsdProfile)` | The dedicatedLocalSsdProfile.  
  
### getDedicatedLocalSsdProfileOrBuilder()
    
    
    public abstract LinuxNodeConfig.SwapConfig.DedicatedLocalSsdProfileOrBuilder getDedicatedLocalSsdProfileOrBuilder()

Provisions a new, separate local NVMe SSD exclusively for swap.

` .google.container.v1.LinuxNodeConfig.SwapConfig.DedicatedLocalSsdProfile dedicated_local_ssd_profile = 5; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.SwapConfig.DedicatedLocalSsdProfileOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.SwapConfig.DedicatedLocalSsdProfileOrBuilder)` |   
  
### getEnabled()
    
    
    public abstract boolean getEnabled()

Optional. Enables or disables swap for the node pool.

`optional bool enabled = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enabled.  
  
### getEncryptionConfig()
    
    
    public abstract LinuxNodeConfig.SwapConfig.EncryptionConfig getEncryptionConfig()

Optional. If omitted, swap space is encrypted by default.

` optional .google.container.v1.LinuxNodeConfig.SwapConfig.EncryptionConfig encryption_config = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.SwapConfig.EncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.SwapConfig.EncryptionConfig)` | The encryptionConfig.  
  
### getEncryptionConfigOrBuilder()
    
    
    public abstract LinuxNodeConfig.SwapConfig.EncryptionConfigOrBuilder getEncryptionConfigOrBuilder()

Optional. If omitted, swap space is encrypted by default.

` optional .google.container.v1.LinuxNodeConfig.SwapConfig.EncryptionConfig encryption_config = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.SwapConfig.EncryptionConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.SwapConfig.EncryptionConfigOrBuilder)` |   
  
### getEphemeralLocalSsdProfile()
    
    
    public abstract LinuxNodeConfig.SwapConfig.EphemeralLocalSsdProfile getEphemeralLocalSsdProfile()

Swap on the local SSD shared with pod ephemeral storage.

` .google.container.v1.LinuxNodeConfig.SwapConfig.EphemeralLocalSsdProfile ephemeral_local_ssd_profile = 4; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.SwapConfig.EphemeralLocalSsdProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.SwapConfig.EphemeralLocalSsdProfile)` | The ephemeralLocalSsdProfile.  
  
### getEphemeralLocalSsdProfileOrBuilder()
    
    
    public abstract LinuxNodeConfig.SwapConfig.EphemeralLocalSsdProfileOrBuilder getEphemeralLocalSsdProfileOrBuilder()

Swap on the local SSD shared with pod ephemeral storage.

` .google.container.v1.LinuxNodeConfig.SwapConfig.EphemeralLocalSsdProfile ephemeral_local_ssd_profile = 4; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.SwapConfig.EphemeralLocalSsdProfileOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.SwapConfig.EphemeralLocalSsdProfileOrBuilder)` |   
  
### getPerformanceProfileCase()
    
    
    public abstract LinuxNodeConfig.SwapConfig.PerformanceProfileCase getPerformanceProfileCase()

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.SwapConfig.PerformanceProfileCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.LinuxNodeConfig.SwapConfig.PerformanceProfileCase)` |   
  
### hasBootDiskProfile()
    
    
    public abstract boolean hasBootDiskProfile()

Swap on the node's boot disk.

`.google.container.v1.LinuxNodeConfig.SwapConfig.BootDiskProfile boot_disk_profile = 3; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bootDiskProfile field is set.  
  
### hasDedicatedLocalSsdProfile()
    
    
    public abstract boolean hasDedicatedLocalSsdProfile()

Provisions a new, separate local NVMe SSD exclusively for swap.

` .google.container.v1.LinuxNodeConfig.SwapConfig.DedicatedLocalSsdProfile dedicated_local_ssd_profile = 5; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the dedicatedLocalSsdProfile field is set.  
  
### hasEnabled()
    
    
    public abstract boolean hasEnabled()

Optional. Enables or disables swap for the node pool.

`optional bool enabled = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the enabled field is set.  
  
### hasEncryptionConfig()
    
    
    public abstract boolean hasEncryptionConfig()

Optional. If omitted, swap space is encrypted by default.

` optional .google.container.v1.LinuxNodeConfig.SwapConfig.EncryptionConfig encryption_config = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the encryptionConfig field is set.  
  
### hasEphemeralLocalSsdProfile()
    
    
    public abstract boolean hasEphemeralLocalSsdProfile()

Swap on the local SSD shared with pod ephemeral storage.

` .google.container.v1.LinuxNodeConfig.SwapConfig.EphemeralLocalSsdProfile ephemeral_local_ssd_profile = 4; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the ephemeralLocalSsdProfile field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
