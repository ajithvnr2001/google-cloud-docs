---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.MachineDetailsOrBuilder
title: Interface MachineDetailsOrBuilder (0.81.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:17:56.601416+00:00
---

# Interface MachineDetailsOrBuilder (0.81.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.MachineDetailsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface MachineDetailsOrBuilder (0.81.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.81.0 (latest)  0.77.0  0.76.0  0.75.0  0.73.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.62.0  0.60.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.52.0  0.50.0  0.49.0  0.46.0  0.45.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface MachineDetailsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getArchitecture()
    
    
    public abstract MachineArchitectureDetails getArchitecture()

Architecture details (vendor, CPU architecture).

`.google.cloud.migrationcenter.v1.MachineArchitectureDetails architecture = 7;`

**Returns**  
---  
**Type** | **Description**  
`[MachineArchitectureDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.MachineArchitectureDetails)` | The architecture.  
  
### getArchitectureOrBuilder()
    
    
    public abstract MachineArchitectureDetailsOrBuilder getArchitectureOrBuilder()

Architecture details (vendor, CPU architecture).

`.google.cloud.migrationcenter.v1.MachineArchitectureDetails architecture = 7;`

**Returns**  
---  
**Type** | **Description**  
`[MachineArchitectureDetailsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.MachineArchitectureDetailsOrBuilder)` |   
  
### getCoreCount()
    
    
    public abstract int getCoreCount()

Number of CPU cores in the machine. Must be non-negative.

`int32 core_count = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The coreCount.  
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Machine creation time.

`.google.protobuf.Timestamp create_time = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Machine creation time.

`.google.protobuf.Timestamp create_time = 3;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDisks()
    
    
    public abstract MachineDiskDetails getDisks()

Disk details.

`.google.cloud.migrationcenter.v1.MachineDiskDetails disks = 10;`

**Returns**  
---  
**Type** | **Description**  
`[MachineDiskDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.MachineDiskDetails)` | The disks.  
  
### getDisksOrBuilder()
    
    
    public abstract MachineDiskDetailsOrBuilder getDisksOrBuilder()

Disk details.

`.google.cloud.migrationcenter.v1.MachineDiskDetails disks = 10;`

**Returns**  
---  
**Type** | **Description**  
`[MachineDiskDetailsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.MachineDiskDetailsOrBuilder)` |   
  
### getGuestOs()
    
    
    public abstract GuestOsDetails getGuestOs()

Guest OS information.

`.google.cloud.migrationcenter.v1.GuestOsDetails guest_os = 8;`

**Returns**  
---  
**Type** | **Description**  
`[GuestOsDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.GuestOsDetails)` | The guestOs.  
  
### getGuestOsOrBuilder()
    
    
    public abstract GuestOsDetailsOrBuilder getGuestOsOrBuilder()

Guest OS information.

`.google.cloud.migrationcenter.v1.GuestOsDetails guest_os = 8;`

**Returns**  
---  
**Type** | **Description**  
`[GuestOsDetailsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.GuestOsDetailsOrBuilder)` |   
  
### getMachineName()
    
    
    public abstract String getMachineName()

Machine name.

`string machine_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The machineName.  
  
### getMachineNameBytes()
    
    
    public abstract ByteString getMachineNameBytes()

Machine name.

`string machine_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for machineName.  
  
### getMemoryMb()
    
    
    public abstract int getMemoryMb()

The amount of memory in the machine. Must be non-negative.

`int32 memory_mb = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The memoryMb.  
  
### getNetwork()
    
    
    public abstract MachineNetworkDetails getNetwork()

Network details.

`.google.cloud.migrationcenter.v1.MachineNetworkDetails network = 9;`

**Returns**  
---  
**Type** | **Description**  
`[MachineNetworkDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.MachineNetworkDetails)` | The network.  
  
### getNetworkOrBuilder()
    
    
    public abstract MachineNetworkDetailsOrBuilder getNetworkOrBuilder()

Network details.

`.google.cloud.migrationcenter.v1.MachineNetworkDetails network = 9;`

**Returns**  
---  
**Type** | **Description**  
`[MachineNetworkDetailsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.MachineNetworkDetailsOrBuilder)` |   
  
### getPlatform()
    
    
    public abstract PlatformDetails getPlatform()

Platform specific information.

`.google.cloud.migrationcenter.v1.PlatformDetails platform = 11;`

**Returns**  
---  
**Type** | **Description**  
`[PlatformDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.PlatformDetails)` | The platform.  
  
### getPlatformOrBuilder()
    
    
    public abstract PlatformDetailsOrBuilder getPlatformOrBuilder()

Platform specific information.

`.google.cloud.migrationcenter.v1.PlatformDetails platform = 11;`

**Returns**  
---  
**Type** | **Description**  
`[PlatformDetailsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.PlatformDetailsOrBuilder)` |   
  
### getPowerState()
    
    
    public abstract MachineDetails.PowerState getPowerState()

Power state of the machine.

`.google.cloud.migrationcenter.v1.MachineDetails.PowerState power_state = 6;`

**Returns**  
---  
**Type** | **Description**  
`[MachineDetails.PowerState](https://docs.cloud.google.com/java/docs/reference/google-cloud-migrationcenter/latest/com.google.cloud.migrationcenter.v1.MachineDetails.PowerState)` | The powerState.  
  
### getPowerStateValue()
    
    
    public abstract int getPowerStateValue()

Power state of the machine.

`.google.cloud.migrationcenter.v1.MachineDetails.PowerState power_state = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for powerState.  
  
### getUuid()
    
    
    public abstract String getUuid()

Machine unique identifier.

`string uuid = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The uuid.  
  
### getUuidBytes()
    
    
    public abstract ByteString getUuidBytes()

Machine unique identifier.

`string uuid = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for uuid.  
  
### hasArchitecture()
    
    
    public abstract boolean hasArchitecture()

Architecture details (vendor, CPU architecture).

`.google.cloud.migrationcenter.v1.MachineArchitectureDetails architecture = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the architecture field is set.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Machine creation time.

`.google.protobuf.Timestamp create_time = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasDisks()
    
    
    public abstract boolean hasDisks()

Disk details.

`.google.cloud.migrationcenter.v1.MachineDiskDetails disks = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the disks field is set.  
  
### hasGuestOs()
    
    
    public abstract boolean hasGuestOs()

Guest OS information.

`.google.cloud.migrationcenter.v1.GuestOsDetails guest_os = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the guestOs field is set.  
  
### hasNetwork()
    
    
    public abstract boolean hasNetwork()

Network details.

`.google.cloud.migrationcenter.v1.MachineNetworkDetails network = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the network field is set.  
  
### hasPlatform()
    
    
    public abstract boolean hasPlatform()

Platform specific information.

`.google.cloud.migrationcenter.v1.PlatformDetails platform = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the platform field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
