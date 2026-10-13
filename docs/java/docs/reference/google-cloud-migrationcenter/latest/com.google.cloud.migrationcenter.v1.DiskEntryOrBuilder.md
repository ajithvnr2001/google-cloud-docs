---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DiskEntryOrBuilder
title: Interface DiskEntryOrBuilder (0.81.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:56.025078+00:00
---

# Interface DiskEntryOrBuilder (0.81.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DiskEntryOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DiskEntryOrBuilder (0.81.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.81.0 (latest)  0.77.0  0.76.0  0.75.0  0.73.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.62.0  0.60.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.52.0  0.50.0  0.49.0  0.46.0  0.45.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface DiskEntryOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCapacityBytes()
    
    
    public abstract long getCapacityBytes()

Disk capacity.

`int64 capacity_bytes = 1;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The capacityBytes.  
  
### getDiskLabel()
    
    
    public abstract String getDiskLabel()

Disk label.

`string disk_label = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The diskLabel.  
  
### getDiskLabelBytes()
    
    
    public abstract ByteString getDiskLabelBytes()

Disk label.

`string disk_label = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for diskLabel.  
  
### getDiskLabelType()
    
    
    public abstract String getDiskLabelType()

Disk label type (e.g. BIOS/GPT)

`string disk_label_type = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The diskLabelType.  
  
### getDiskLabelTypeBytes()
    
    
    public abstract ByteString getDiskLabelTypeBytes()

Disk label type (e.g. BIOS/GPT)

`string disk_label_type = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for diskLabelType.  
  
### getFreeBytes()
    
    
    public abstract long getFreeBytes()

Disk free space.

`int64 free_bytes = 2;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The freeBytes.  
  
### getHwAddress()
    
    
    public abstract String getHwAddress()

Disk hardware address (e.g. 0:1 for SCSI).

`string hw_address = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The hwAddress.  
  
### getHwAddressBytes()
    
    
    public abstract ByteString getHwAddressBytes()

Disk hardware address (e.g. 0:1 for SCSI).

`string hw_address = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for hwAddress.  
  
### getInterfaceType()
    
    
    public abstract DiskEntry.InterfaceType getInterfaceType()

Disks interface type.

`.google.cloud.migrationcenter.v1.DiskEntry.InterfaceType interface_type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[DiskEntry.InterfaceType](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DiskEntry.InterfaceType)` | The interfaceType.  
  
### getInterfaceTypeValue()
    
    
    public abstract int getInterfaceTypeValue()

Disks interface type.

`.google.cloud.migrationcenter.v1.DiskEntry.InterfaceType interface_type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for interfaceType.  
  
### getPartitions()
    
    
    public abstract DiskPartitionList getPartitions()

Partition layout.

`.google.cloud.migrationcenter.v1.DiskPartitionList partitions = 6;`

**Returns**  
---  
**Type** | **Description**  
`[DiskPartitionList](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DiskPartitionList)` | The partitions.  
  
### getPartitionsOrBuilder()
    
    
    public abstract DiskPartitionListOrBuilder getPartitionsOrBuilder()

Partition layout.

`.google.cloud.migrationcenter.v1.DiskPartitionList partitions = 6;`

**Returns**  
---  
**Type** | **Description**  
`[DiskPartitionListOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DiskPartitionListOrBuilder)` |   
  
### getPlatformSpecificCase()
    
    
    public abstract DiskEntry.PlatformSpecificCase getPlatformSpecificCase()

**Returns**  
---  
**Type** | **Description**  
`[DiskEntry.PlatformSpecificCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.DiskEntry.PlatformSpecificCase)` |   
  
### getVmware()
    
    
    public abstract VmwareDiskConfig getVmware()

VMware disk details.

`.google.cloud.migrationcenter.v1.VmwareDiskConfig vmware = 20;`

**Returns**  
---  
**Type** | **Description**  
`[VmwareDiskConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.VmwareDiskConfig)` | The vmware.  
  
### getVmwareOrBuilder()
    
    
    public abstract VmwareDiskConfigOrBuilder getVmwareOrBuilder()

VMware disk details.

`.google.cloud.migrationcenter.v1.VmwareDiskConfig vmware = 20;`

**Returns**  
---  
**Type** | **Description**  
`[VmwareDiskConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.VmwareDiskConfigOrBuilder)` |   
  
### hasPartitions()
    
    
    public abstract boolean hasPartitions()

Partition layout.

`.google.cloud.migrationcenter.v1.DiskPartitionList partitions = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the partitions field is set.  
  
### hasVmware()
    
    
    public abstract boolean hasVmware()

VMware disk details.

`.google.cloud.migrationcenter.v1.VmwareDiskConfig vmware = 20;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the vmware field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
