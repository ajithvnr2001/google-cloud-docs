---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.DisksMigrationVmTargetDefaultsOrBuilder
title: Interface DisksMigrationVmTargetDefaultsOrBuilder (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:42:38.882915+00:00
---

# Interface DisksMigrationVmTargetDefaultsOrBuilder (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.DisksMigrationVmTargetDefaultsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DisksMigrationVmTargetDefaultsOrBuilder (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.5  1.2.0  1.1.1  1.0.5 
    
    
    public interface DisksMigrationVmTargetDefaultsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Optional. A map of labels to associate with the VM.

`map<string, string> labels = 13 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsMetadata(String key)
    
    
    public abstract boolean containsMetadata(String key)

Optional. The metadata key/value pairs to assign to the VM.

`map<string, string> metadata = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAdditionalLicenses(int index)
    
    
    public abstract String getAdditionalLicenses(int index)

Optional. Additional licenses to assign to the VM.

`repeated string additional_licenses = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The additionalLicenses at the given index.  
  
### getAdditionalLicensesBytes(int index)
    
    
    public abstract ByteString getAdditionalLicensesBytes(int index)

Optional. Additional licenses to assign to the VM.

`repeated string additional_licenses = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the additionalLicenses at the given index.  
  
### getAdditionalLicensesCount()
    
    
    public abstract int getAdditionalLicensesCount()

Optional. Additional licenses to assign to the VM.

`repeated string additional_licenses = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of additionalLicenses.  
  
### getAdditionalLicensesList()
    
    
    public abstract List<String> getAdditionalLicensesList()

Optional. Additional licenses to assign to the VM.

`repeated string additional_licenses = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the additionalLicenses.  
  
### getBootDiskDefaults()
    
    
    public abstract BootDiskDefaults getBootDiskDefaults()

Optional. Details of the boot disk of the VM.

` .google.cloud.vmmigration.v1.BootDiskDefaults boot_disk_defaults = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BootDiskDefaults](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.BootDiskDefaults)` | The bootDiskDefaults.  
  
### getBootDiskDefaultsOrBuilder()
    
    
    public abstract BootDiskDefaultsOrBuilder getBootDiskDefaultsOrBuilder()

Optional. Details of the boot disk of the VM.

` .google.cloud.vmmigration.v1.BootDiskDefaults boot_disk_defaults = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BootDiskDefaultsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.BootDiskDefaultsOrBuilder)` |   
  
### getComputeScheduling()
    
    
    public abstract ComputeScheduling getComputeScheduling()

Optional. Compute instance scheduling information (if empty default is used).

` .google.cloud.vmmigration.v1.ComputeScheduling compute_scheduling = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ComputeScheduling](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ComputeScheduling)` | The computeScheduling.  
  
### getComputeSchedulingOrBuilder()
    
    
    public abstract ComputeSchedulingOrBuilder getComputeSchedulingOrBuilder()

Optional. Compute instance scheduling information (if empty default is used).

` .google.cloud.vmmigration.v1.ComputeScheduling compute_scheduling = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ComputeSchedulingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ComputeSchedulingOrBuilder)` |   
  
### getEnableIntegrityMonitoring()
    
    
    public abstract boolean getEnableIntegrityMonitoring()

Optional. Defines whether the instance has integrity monitoring enabled.

`bool enable_integrity_monitoring = 17 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableIntegrityMonitoring.  
  
### getEnableVtpm()
    
    
    public abstract boolean getEnableVtpm()

Optional. Defines whether the instance has vTPM enabled.

`bool enable_vtpm = 16 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableVtpm.  
  
### getEncryption()
    
    
    public abstract Encryption getEncryption()

Optional. The encryption to apply to the VM.

` .google.cloud.vmmigration.v1.Encryption encryption = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Encryption](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.Encryption)` | The encryption.  
  
### getEncryptionOrBuilder()
    
    
    public abstract EncryptionOrBuilder getEncryptionOrBuilder()

Optional. The encryption to apply to the VM.

` .google.cloud.vmmigration.v1.Encryption encryption = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EncryptionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.EncryptionOrBuilder)` |   
  
### getHostname()
    
    
    public abstract String getHostname()

Optional. The hostname to assign to the VM.

`string hostname = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The hostname.  
  
### getHostnameBytes()
    
    
    public abstract ByteString getHostnameBytes()

Optional. The hostname to assign to the VM.

`string hostname = 12 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for hostname.  
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.DisksMigrationVmTargetDefaultsOrBuilder#com_google_cloud_vmmigration_v1_DisksMigrationVmTargetDefaultsOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Optional. A map of labels to associate with the VM.

`map<string, string> labels = 13 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Optional. A map of labels to associate with the VM.

`map<string, string> labels = 13 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Optional. A map of labels to associate with the VM.

`map<string, string> labels = 13 [(.google.api.field_behavior) = OPTIONAL];`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLabelsOrThrow(String key)
    
    
    public abstract String getLabelsOrThrow(String key)

Optional. A map of labels to associate with the VM.

`map<string, string> labels = 13 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMachineType()
    
    
    public abstract String getMachineType()

Required. The machine type to create the VM with.

`string machine_type = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The machineType.  
  
### getMachineTypeBytes()
    
    
    public abstract ByteString getMachineTypeBytes()

Required. The machine type to create the VM with.

`string machine_type = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for machineType.  
  
### getMachineTypeSeries()
    
    
    public abstract String getMachineTypeSeries()

Optional. The machine type series to create the VM with. For presentation only.

`string machine_type_series = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The machineTypeSeries.  
  
### getMachineTypeSeriesBytes()
    
    
    public abstract ByteString getMachineTypeSeriesBytes()

Optional. The machine type series to create the VM with. For presentation only.

`string machine_type_series = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for machineTypeSeries.  
  
### getMetadata() (deprecated)
    
    
    public abstract Map<String,String> getMetadata()

Use [#getMetadataMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.DisksMigrationVmTargetDefaultsOrBuilder#com_google_cloud_vmmigration_v1_DisksMigrationVmTargetDefaultsOrBuilder_getMetadataMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getMetadataCount()
    
    
    public abstract int getMetadataCount()

Optional. The metadata key/value pairs to assign to the VM.

`map<string, string> metadata = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMetadataMap()
    
    
    public abstract Map<String,String> getMetadataMap()

Optional. The metadata key/value pairs to assign to the VM.

`map<string, string> metadata = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getMetadataOrDefault(String key, String defaultValue)
    
    
    public abstract String getMetadataOrDefault(String key, String defaultValue)

Optional. The metadata key/value pairs to assign to the VM.

`map<string, string> metadata = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMetadataOrThrow(String key)
    
    
    public abstract String getMetadataOrThrow(String key)

Optional. The metadata key/value pairs to assign to the VM.

`map<string, string> metadata = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getNetworkInterfaces(int index)
    
    
    public abstract NetworkInterface getNetworkInterfaces(int index)

Optional. NICs to attach to the VM.

` repeated .google.cloud.vmmigration.v1.NetworkInterface network_interfaces = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.NetworkInterface)` |   
  
### getNetworkInterfacesCount()
    
    
    public abstract int getNetworkInterfacesCount()

Optional. NICs to attach to the VM.

` repeated .google.cloud.vmmigration.v1.NetworkInterface network_interfaces = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getNetworkInterfacesList()
    
    
    public abstract List<NetworkInterface> getNetworkInterfacesList()

Optional. NICs to attach to the VM.

` repeated .google.cloud.vmmigration.v1.NetworkInterface network_interfaces = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.NetworkInterface)>` |   
  
### getNetworkInterfacesOrBuilder(int index)
    
    
    public abstract NetworkInterfaceOrBuilder getNetworkInterfacesOrBuilder(int index)

Optional. NICs to attach to the VM.

` repeated .google.cloud.vmmigration.v1.NetworkInterface network_interfaces = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkInterfaceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.NetworkInterfaceOrBuilder)` |   
  
### getNetworkInterfacesOrBuilderList()
    
    
    public abstract List<? extends NetworkInterfaceOrBuilder> getNetworkInterfacesOrBuilderList()

Optional. NICs to attach to the VM.

` repeated .google.cloud.vmmigration.v1.NetworkInterface network_interfaces = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.vmmigration.v1.NetworkInterfaceOrBuilder>` |   
  
### getNetworkTags(int index)
    
    
    public abstract String getNetworkTags(int index)

Optional. A list of network tags to associate with the VM.

`repeated string network_tags = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The networkTags at the given index.  
  
### getNetworkTagsBytes(int index)
    
    
    public abstract ByteString getNetworkTagsBytes(int index)

Optional. A list of network tags to associate with the VM.

`repeated string network_tags = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the networkTags at the given index.  
  
### getNetworkTagsCount()
    
    
    public abstract int getNetworkTagsCount()

Optional. A list of network tags to associate with the VM.

`repeated string network_tags = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of networkTags.  
  
### getNetworkTagsList()
    
    
    public abstract List<String> getNetworkTagsList()

Optional. A list of network tags to associate with the VM.

`repeated string network_tags = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the networkTags.  
  
### getSecureBoot()
    
    
    public abstract boolean getSecureBoot()

Optional. Defines whether the instance has Secure Boot enabled. This can be set to true only if the VM boot option is EFI.

`bool secure_boot = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The secureBoot.  
  
### getServiceAccount()
    
    
    public abstract String getServiceAccount()

Optional. The service account to associate the VM with.

`string service_account = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serviceAccount.  
  
### getServiceAccountBytes()
    
    
    public abstract ByteString getServiceAccountBytes()

Optional. The service account to associate the VM with.

`string service_account = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serviceAccount.  
  
### getVmName()
    
    
    public abstract String getVmName()

Required. The name of the VM to create.

`string vm_name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The vmName.  
  
### getVmNameBytes()
    
    
    public abstract ByteString getVmNameBytes()

Required. The name of the VM to create.

`string vm_name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for vmName.  
  
### hasBootDiskDefaults()
    
    
    public abstract boolean hasBootDiskDefaults()

Optional. Details of the boot disk of the VM.

` .google.cloud.vmmigration.v1.BootDiskDefaults boot_disk_defaults = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bootDiskDefaults field is set.  
  
### hasComputeScheduling()
    
    
    public abstract boolean hasComputeScheduling()

Optional. Compute instance scheduling information (if empty default is used).

` .google.cloud.vmmigration.v1.ComputeScheduling compute_scheduling = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the computeScheduling field is set.  
  
### hasEncryption()
    
    
    public abstract boolean hasEncryption()

Optional. The encryption to apply to the VM.

` .google.cloud.vmmigration.v1.Encryption encryption = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the encryption field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
