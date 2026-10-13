---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.Instance.PerformanceConfigOrBuilder
title: Interface Instance.PerformanceConfigOrBuilder (1.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:56:58.144283+00:00
---

# Interface Instance.PerformanceConfigOrBuilder (1.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.Instance.PerformanceConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Instance.PerformanceConfigOrBuilder (1.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.100.0 (latest)  1.96.0  1.95.0  1.94.0  1.92.0  1.89.0  1.88.0  1.86.0  1.84.0  1.83.0  1.82.0  1.81.0  1.79.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.71.0  1.69.0  1.68.0  1.65.0  1.64.0  1.63.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.2.0 
    
    
    public static interface Instance.PerformanceConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getFixedIops()
    
    
    public abstract Instance.FixedIOPS getFixedIops()

Choose a fixed provisioned IOPS value for the instance, which will remain constant regardless of instance capacity. Value must be a multiple of 1000.

If the chosen value is outside the supported range for the instance's capacity during instance creation, instance creation will fail with an `InvalidArgument` error. Similarly, if an instance capacity update would result in a value outside the supported range, the update will fail with an `InvalidArgument` error.

`.google.cloud.filestore.v1.Instance.FixedIOPS fixed_iops = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Instance.FixedIOPS](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.Instance.FixedIOPS)` | The fixedIops.  
  
### getFixedIopsOrBuilder()
    
    
    public abstract Instance.FixedIOPSOrBuilder getFixedIopsOrBuilder()

Choose a fixed provisioned IOPS value for the instance, which will remain constant regardless of instance capacity. Value must be a multiple of 1000.

If the chosen value is outside the supported range for the instance's capacity during instance creation, instance creation will fail with an `InvalidArgument` error. Similarly, if an instance capacity update would result in a value outside the supported range, the update will fail with an `InvalidArgument` error.

`.google.cloud.filestore.v1.Instance.FixedIOPS fixed_iops = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Instance.FixedIOPSOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.Instance.FixedIOPSOrBuilder)` |   
  
### getIopsPerTb()
    
    
    public abstract Instance.IOPSPerTB getIopsPerTb()

Provision IOPS dynamically based on the capacity of the instance. Provisioned IOPS will be calculated by multiplying the capacity of the instance in TiB by the `iops_per_tb` value. For example, for a 2 TiB instance with an `iops_per_tb` value of 17000 the provisioned IOPS will be 34000.

If the calculated value is outside the supported range for the instance's capacity during instance creation, instance creation will fail with an `InvalidArgument` error. Similarly, if an instance capacity update would result in a value outside the supported range, the update will fail with an `InvalidArgument` error.

`.google.cloud.filestore.v1.Instance.IOPSPerTB iops_per_tb = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Instance.IOPSPerTB](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.Instance.IOPSPerTB)` | The iopsPerTb.  
  
### getIopsPerTbOrBuilder()
    
    
    public abstract Instance.IOPSPerTBOrBuilder getIopsPerTbOrBuilder()

Provision IOPS dynamically based on the capacity of the instance. Provisioned IOPS will be calculated by multiplying the capacity of the instance in TiB by the `iops_per_tb` value. For example, for a 2 TiB instance with an `iops_per_tb` value of 17000 the provisioned IOPS will be 34000.

If the calculated value is outside the supported range for the instance's capacity during instance creation, instance creation will fail with an `InvalidArgument` error. Similarly, if an instance capacity update would result in a value outside the supported range, the update will fail with an `InvalidArgument` error.

`.google.cloud.filestore.v1.Instance.IOPSPerTB iops_per_tb = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Instance.IOPSPerTBOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.Instance.IOPSPerTBOrBuilder)` |   
  
### getModeCase()
    
    
    public abstract Instance.PerformanceConfig.ModeCase getModeCase()

**Returns**  
---  
**Type** | **Description**  
`[Instance.PerformanceConfig.ModeCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-filestore/latest/com.google.cloud.filestore.v1.Instance.PerformanceConfig.ModeCase)` |   
  
### hasFixedIops()
    
    
    public abstract boolean hasFixedIops()

Choose a fixed provisioned IOPS value for the instance, which will remain constant regardless of instance capacity. Value must be a multiple of 1000.

If the chosen value is outside the supported range for the instance's capacity during instance creation, instance creation will fail with an `InvalidArgument` error. Similarly, if an instance capacity update would result in a value outside the supported range, the update will fail with an `InvalidArgument` error.

`.google.cloud.filestore.v1.Instance.FixedIOPS fixed_iops = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the fixedIops field is set.  
  
### hasIopsPerTb()
    
    
    public abstract boolean hasIopsPerTb()

Provision IOPS dynamically based on the capacity of the instance. Provisioned IOPS will be calculated by multiplying the capacity of the instance in TiB by the `iops_per_tb` value. For example, for a 2 TiB instance with an `iops_per_tb` value of 17000 the provisioned IOPS will be 34000.

If the calculated value is outside the supported range for the instance's capacity during instance creation, instance creation will fail with an `InvalidArgument` error. Similarly, if an instance capacity update would result in a value outside the supported range, the update will fail with an `InvalidArgument` error.

`.google.cloud.filestore.v1.Instance.IOPSPerTB iops_per_tb = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the iopsPerTb field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
