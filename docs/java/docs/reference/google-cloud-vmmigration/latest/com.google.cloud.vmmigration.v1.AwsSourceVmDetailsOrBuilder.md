---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.AwsSourceVmDetailsOrBuilder
title: Interface AwsSourceVmDetailsOrBuilder (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:09.995544+00:00
---

# Interface AwsSourceVmDetailsOrBuilder (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.AwsSourceVmDetailsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AwsSourceVmDetailsOrBuilder (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.5  1.2.0  1.1.1  1.0.5 
    
    
    public interface AwsSourceVmDetailsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getArchitecture()
    
    
    public abstract VmArchitecture getArchitecture()

Output only. The VM architecture.

` .google.cloud.vmmigration.v1.VmArchitecture architecture = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[VmArchitecture](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.VmArchitecture)` | The architecture.  
  
### getArchitectureValue()
    
    
    public abstract int getArchitectureValue()

Output only. The VM architecture.

` .google.cloud.vmmigration.v1.VmArchitecture architecture = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for architecture.  
  
### getCommittedStorageBytes()
    
    
    public abstract long getCommittedStorageBytes()

Output only. The total size of the disks being migrated in bytes.

`int64 committed_storage_bytes = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The committedStorageBytes.  
  
### getDisks(int index)
    
    
    public abstract AwsSourceVmDetails.AwsDiskDetails getDisks(int index)

Output only. The disks attached to the source VM.

` repeated .google.cloud.vmmigration.v1.AwsSourceVmDetails.AwsDiskDetails disks = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AwsSourceVmDetails.AwsDiskDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.AwsSourceVmDetails.AwsDiskDetails)` |   
  
### getDisksCount()
    
    
    public abstract int getDisksCount()

Output only. The disks attached to the source VM.

` repeated .google.cloud.vmmigration.v1.AwsSourceVmDetails.AwsDiskDetails disks = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDisksList()
    
    
    public abstract List<AwsSourceVmDetails.AwsDiskDetails> getDisksList()

Output only. The disks attached to the source VM.

` repeated .google.cloud.vmmigration.v1.AwsSourceVmDetails.AwsDiskDetails disks = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[AwsDiskDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.AwsSourceVmDetails.AwsDiskDetails)>` |   
  
### getDisksOrBuilder(int index)
    
    
    public abstract AwsSourceVmDetails.AwsDiskDetailsOrBuilder getDisksOrBuilder(int index)

Output only. The disks attached to the source VM.

` repeated .google.cloud.vmmigration.v1.AwsSourceVmDetails.AwsDiskDetails disks = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AwsSourceVmDetails.AwsDiskDetailsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.AwsSourceVmDetails.AwsDiskDetailsOrBuilder)` |   
  
### getDisksOrBuilderList()
    
    
    public abstract List<? extends AwsSourceVmDetails.AwsDiskDetailsOrBuilder> getDisksOrBuilderList()

Output only. The disks attached to the source VM.

` repeated .google.cloud.vmmigration.v1.AwsSourceVmDetails.AwsDiskDetails disks = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.vmmigration.v1.AwsSourceVmDetails.AwsDiskDetailsOrBuilder>` |   
  
### getFirmware()
    
    
    public abstract AwsSourceVmDetails.Firmware getFirmware()

Output only. The firmware type of the source VM.

` .google.cloud.vmmigration.v1.AwsSourceVmDetails.Firmware firmware = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AwsSourceVmDetails.Firmware](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.AwsSourceVmDetails.Firmware)` | The firmware.  
  
### getFirmwareValue()
    
    
    public abstract int getFirmwareValue()

Output only. The firmware type of the source VM.

` .google.cloud.vmmigration.v1.AwsSourceVmDetails.Firmware firmware = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for firmware.  
  
### getVmCapabilitiesInfo()
    
    
    public abstract VmCapabilities getVmCapabilitiesInfo()

Output only. Information about VM capabilities needed for some Compute Engine features.

` .google.cloud.vmmigration.v1.VmCapabilities vm_capabilities_info = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[VmCapabilities](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.VmCapabilities)` | The vmCapabilitiesInfo.  
  
### getVmCapabilitiesInfoOrBuilder()
    
    
    public abstract VmCapabilitiesOrBuilder getVmCapabilitiesInfoOrBuilder()

Output only. Information about VM capabilities needed for some Compute Engine features.

` .google.cloud.vmmigration.v1.VmCapabilities vm_capabilities_info = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[VmCapabilitiesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.VmCapabilitiesOrBuilder)` |   
  
### hasVmCapabilitiesInfo()
    
    
    public abstract boolean hasVmCapabilitiesInfo()

Output only. Information about VM capabilities needed for some Compute Engine features.

` .google.cloud.vmmigration.v1.VmCapabilities vm_capabilities_info = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the vmCapabilitiesInfo field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
