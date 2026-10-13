---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ManagedInstancePropertiesFromFlexibilityPolicyOrBuilder
title: Interface ManagedInstancePropertiesFromFlexibilityPolicyOrBuilder (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:15:05.956821+00:00
---

# Interface ManagedInstancePropertiesFromFlexibilityPolicyOrBuilder (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ManagedInstancePropertiesFromFlexibilityPolicyOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ManagedInstancePropertiesFromFlexibilityPolicyOrBuilder (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public interface ManagedInstancePropertiesFromFlexibilityPolicyOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDisks(int index)
    
    
    public abstract AttachedDisk getDisks(int index)

List of disks to be attached to the instance.

`repeated .google.cloud.compute.v1.AttachedDisk disks = 95594102;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk)` |   
  
### getDisksCount()
    
    
    public abstract int getDisksCount()

List of disks to be attached to the instance.

`repeated .google.cloud.compute.v1.AttachedDisk disks = 95594102;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDisksList()
    
    
    public abstract List<AttachedDisk> getDisksList()

List of disks to be attached to the instance.

`repeated .google.cloud.compute.v1.AttachedDisk disks = 95594102;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[AttachedDisk](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDisk)>` |   
  
### getDisksOrBuilder(int index)
    
    
    public abstract AttachedDiskOrBuilder getDisksOrBuilder(int index)

List of disks to be attached to the instance.

`repeated .google.cloud.compute.v1.AttachedDisk disks = 95594102;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AttachedDiskOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AttachedDiskOrBuilder)` |   
  
### getDisksOrBuilderList()
    
    
    public abstract List<? extends AttachedDiskOrBuilder> getDisksOrBuilderList()

List of disks to be attached to the instance.

`repeated .google.cloud.compute.v1.AttachedDisk disks = 95594102;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.compute.v1.AttachedDiskOrBuilder>` |   
  
### getMachineType()
    
    
    public abstract String getMachineType()

Output only. The machine type to be used for this instance.

`optional string machine_type = 227711026;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The machineType.  
  
### getMachineTypeBytes()
    
    
    public abstract ByteString getMachineTypeBytes()

Output only. The machine type to be used for this instance.

`optional string machine_type = 227711026;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for machineType.  
  
### getMinCpuPlatform()
    
    
    public abstract String getMinCpuPlatform()

Name of the minimum CPU platform to be used by this instance. e.g. 'Intel Ice Lake'.

`optional string min_cpu_platform = 242912759;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The minCpuPlatform.  
  
### getMinCpuPlatformBytes()
    
    
    public abstract ByteString getMinCpuPlatformBytes()

Name of the minimum CPU platform to be used by this instance. e.g. 'Intel Ice Lake'.

`optional string min_cpu_platform = 242912759;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for minCpuPlatform.  
  
### hasMachineType()
    
    
    public abstract boolean hasMachineType()

Output only. The machine type to be used for this instance.

`optional string machine_type = 227711026;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the machineType field is set.  
  
### hasMinCpuPlatform()
    
    
    public abstract boolean hasMinCpuPlatform()

Name of the minimum CPU platform to be used by this instance. e.g. 'Intel Ice Lake'.

`optional string min_cpu_platform = 242912759;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the minCpuPlatform field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
