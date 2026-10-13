---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ComputeEngineTargetDetailsOrBuilder
title: Interface ComputeEngineTargetDetailsOrBuilder (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:52.849715+00:00
---

# Interface ComputeEngineTargetDetailsOrBuilder (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ComputeEngineTargetDetailsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ComputeEngineTargetDetailsOrBuilder (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.5  1.2.0  1.1.1  1.0.5 
    
    
    public interface ComputeEngineTargetDetailsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

A map of labels to associate with the VM.

`map<string, string> labels = 10;`

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

The metadata key/value pairs to assign to the VM.

`map<string, string> metadata = 16;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAdaptationModifiers(int index)
    
    
    public abstract AdaptationModifier getAdaptationModifiers(int index)

Optional. Modifiers to be used as configuration of the OS adaptation process.

` repeated .google.cloud.vmmigration.v1.AdaptationModifier adaptation_modifiers = 23 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdaptationModifier](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.AdaptationModifier)` |   
  
### getAdaptationModifiersCount()
    
    
    public abstract int getAdaptationModifiersCount()

Optional. Modifiers to be used as configuration of the OS adaptation process.

` repeated .google.cloud.vmmigration.v1.AdaptationModifier adaptation_modifiers = 23 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAdaptationModifiersList()
    
    
    public abstract List<AdaptationModifier> getAdaptationModifiersList()

Optional. Modifiers to be used as configuration of the OS adaptation process.

` repeated .google.cloud.vmmigration.v1.AdaptationModifier adaptation_modifiers = 23 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[AdaptationModifier](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.AdaptationModifier)>` |   
  
### getAdaptationModifiersOrBuilder(int index)
    
    
    public abstract AdaptationModifierOrBuilder getAdaptationModifiersOrBuilder(int index)

Optional. Modifiers to be used as configuration of the OS adaptation process.

` repeated .google.cloud.vmmigration.v1.AdaptationModifier adaptation_modifiers = 23 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AdaptationModifierOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.AdaptationModifierOrBuilder)` |   
  
### getAdaptationModifiersOrBuilderList()
    
    
    public abstract List<? extends AdaptationModifierOrBuilder> getAdaptationModifiersOrBuilderList()

Optional. Modifiers to be used as configuration of the OS adaptation process.

` repeated .google.cloud.vmmigration.v1.AdaptationModifier adaptation_modifiers = 23 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.vmmigration.v1.AdaptationModifierOrBuilder>` |   
  
### getAdditionalLicenses(int index)
    
    
    public abstract String getAdditionalLicenses(int index)

Additional licenses to assign to the VM.

`repeated string additional_licenses = 17;`

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

Additional licenses to assign to the VM.

`repeated string additional_licenses = 17;`

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

Additional licenses to assign to the VM.

`repeated string additional_licenses = 17;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of additionalLicenses.  
  
### getAdditionalLicensesList()
    
    
    public abstract List<String> getAdditionalLicensesList()

Additional licenses to assign to the VM.

`repeated string additional_licenses = 17;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the additionalLicenses.  
  
### getAppliedLicense()
    
    
    public abstract AppliedLicense getAppliedLicense()

The OS license returned from the adaptation module report.

`.google.cloud.vmmigration.v1.AppliedLicense applied_license = 12;`

**Returns**  
---  
**Type** | **Description**  
`[AppliedLicense](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.AppliedLicense)` | The appliedLicense.  
  
### getAppliedLicenseOrBuilder()
    
    
    public abstract AppliedLicenseOrBuilder getAppliedLicenseOrBuilder()

The OS license returned from the adaptation module report.

`.google.cloud.vmmigration.v1.AppliedLicense applied_license = 12;`

**Returns**  
---  
**Type** | **Description**  
`[AppliedLicenseOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.AppliedLicenseOrBuilder)` |   
  
### getBootConversion()
    
    
    public abstract BootConversion getBootConversion()

Optional. By default the virtual machine will keep its existing boot option. Setting this property will trigger an internal process which will convert the virtual machine from using the existing boot option to another.

` .google.cloud.vmmigration.v1.BootConversion boot_conversion = 20 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BootConversion](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.BootConversion)` | The bootConversion.  
  
### getBootConversionValue()
    
    
    public abstract int getBootConversionValue()

Optional. By default the virtual machine will keep its existing boot option. Setting this property will trigger an internal process which will convert the virtual machine from using the existing boot option to another.

` .google.cloud.vmmigration.v1.BootConversion boot_conversion = 20 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for bootConversion.  
  
### getBootOption()
    
    
    public abstract ComputeEngineBootOption getBootOption()

The VM Boot Option, as set in the source VM.

`.google.cloud.vmmigration.v1.ComputeEngineBootOption boot_option = 15;`

**Returns**  
---  
**Type** | **Description**  
`[ComputeEngineBootOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ComputeEngineBootOption)` | The bootOption.  
  
### getBootOptionValue()
    
    
    public abstract int getBootOptionValue()

The VM Boot Option, as set in the source VM.

`.google.cloud.vmmigration.v1.ComputeEngineBootOption boot_option = 15;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for bootOption.  
  
### getComputeScheduling()
    
    
    public abstract ComputeScheduling getComputeScheduling()

Compute instance scheduling information (if empty default is used).

`.google.cloud.vmmigration.v1.ComputeScheduling compute_scheduling = 13;`

**Returns**  
---  
**Type** | **Description**  
`[ComputeScheduling](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ComputeScheduling)` | The computeScheduling.  
  
### getComputeSchedulingOrBuilder()
    
    
    public abstract ComputeSchedulingOrBuilder getComputeSchedulingOrBuilder()

Compute instance scheduling information (if empty default is used).

`.google.cloud.vmmigration.v1.ComputeScheduling compute_scheduling = 13;`

**Returns**  
---  
**Type** | **Description**  
`[ComputeSchedulingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ComputeSchedulingOrBuilder)` |   
  
### getDiskReplicaZones(int index)
    
    
    public abstract String getDiskReplicaZones(int index)

Optional. Additional replica zones of the target regional disks. If this list is not empty a regional disk will be created. The first supported zone would be the one stated in the zone field. The rest are taken from this list. Please refer to the [regional disk creation API](https://cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources) for further details about regional vs zonal disks. If not specified, a zonal disk will be created in the same zone the VM is created.

`repeated string disk_replica_zones = 24 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The diskReplicaZones at the given index.  
  
### getDiskReplicaZonesBytes(int index)
    
    
    public abstract ByteString getDiskReplicaZonesBytes(int index)

Optional. Additional replica zones of the target regional disks. If this list is not empty a regional disk will be created. The first supported zone would be the one stated in the zone field. The rest are taken from this list. Please refer to the [regional disk creation API](https://cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources) for further details about regional vs zonal disks. If not specified, a zonal disk will be created in the same zone the VM is created.

`repeated string disk_replica_zones = 24 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the diskReplicaZones at the given index.  
  
### getDiskReplicaZonesCount()
    
    
    public abstract int getDiskReplicaZonesCount()

Optional. Additional replica zones of the target regional disks. If this list is not empty a regional disk will be created. The first supported zone would be the one stated in the zone field. The rest are taken from this list. Please refer to the [regional disk creation API](https://cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources) for further details about regional vs zonal disks. If not specified, a zonal disk will be created in the same zone the VM is created.

`repeated string disk_replica_zones = 24 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of diskReplicaZones.  
  
### getDiskReplicaZonesList()
    
    
    public abstract List<String> getDiskReplicaZonesList()

Optional. Additional replica zones of the target regional disks. If this list is not empty a regional disk will be created. The first supported zone would be the one stated in the zone field. The rest are taken from this list. Please refer to the [regional disk creation API](https://cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources) for further details about regional vs zonal disks. If not specified, a zonal disk will be created in the same zone the VM is created.

`repeated string disk_replica_zones = 24 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the diskReplicaZones.  
  
### getDiskType()
    
    
    public abstract ComputeEngineDiskType getDiskType()

The disk type to use in the VM.

`.google.cloud.vmmigration.v1.ComputeEngineDiskType disk_type = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ComputeEngineDiskType](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ComputeEngineDiskType)` | The diskType.  
  
### getDiskTypeValue()
    
    
    public abstract int getDiskTypeValue()

The disk type to use in the VM.

`.google.cloud.vmmigration.v1.ComputeEngineDiskType disk_type = 9;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for diskType.  
  
### getEnableIntegrityMonitoring()
    
    
    public abstract boolean getEnableIntegrityMonitoring()

Optional. Defines whether the instance has integrity monitoring enabled.

`bool enable_integrity_monitoring = 22 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableIntegrityMonitoring.  
  
### getEnableVtpm()
    
    
    public abstract boolean getEnableVtpm()

Optional. Defines whether the instance has vTPM enabled.

`bool enable_vtpm = 21 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableVtpm.  
  
### getEncryption()
    
    
    public abstract Encryption getEncryption()

Optional. The encryption to apply to the VM disks.

` .google.cloud.vmmigration.v1.Encryption encryption = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Encryption](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.Encryption)` | The encryption.  
  
### getEncryptionOrBuilder()
    
    
    public abstract EncryptionOrBuilder getEncryptionOrBuilder()

Optional. The encryption to apply to the VM disks.

` .google.cloud.vmmigration.v1.Encryption encryption = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EncryptionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.EncryptionOrBuilder)` |   
  
### getHostname()
    
    
    public abstract String getHostname()

The hostname to assign to the VM.

`string hostname = 18;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The hostname.  
  
### getHostnameBytes()
    
    
    public abstract ByteString getHostnameBytes()

The hostname to assign to the VM.

`string hostname = 18;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for hostname.  
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ComputeEngineTargetDetailsOrBuilder#com_google_cloud_vmmigration_v1_ComputeEngineTargetDetailsOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

A map of labels to associate with the VM.

`map<string, string> labels = 10;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

A map of labels to associate with the VM.

`map<string, string> labels = 10;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

A map of labels to associate with the VM.

`map<string, string> labels = 10;`

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

A map of labels to associate with the VM.

`map<string, string> labels = 10;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLicenseType()
    
    
    public abstract ComputeEngineLicenseType getLicenseType()

The license type to use in OS adaptation.

`.google.cloud.vmmigration.v1.ComputeEngineLicenseType license_type = 11;`

**Returns**  
---  
**Type** | **Description**  
`[ComputeEngineLicenseType](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ComputeEngineLicenseType)` | The licenseType.  
  
### getLicenseTypeValue()
    
    
    public abstract int getLicenseTypeValue()

The license type to use in OS adaptation.

`.google.cloud.vmmigration.v1.ComputeEngineLicenseType license_type = 11;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for licenseType.  
  
### getMachineType()
    
    
    public abstract String getMachineType()

The machine type to create the VM with.

`string machine_type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The machineType.  
  
### getMachineTypeBytes()
    
    
    public abstract ByteString getMachineTypeBytes()

The machine type to create the VM with.

`string machine_type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for machineType.  
  
### getMachineTypeSeries()
    
    
    public abstract String getMachineTypeSeries()

The machine type series to create the VM with.

`string machine_type_series = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The machineTypeSeries.  
  
### getMachineTypeSeriesBytes()
    
    
    public abstract ByteString getMachineTypeSeriesBytes()

The machine type series to create the VM with.

`string machine_type_series = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for machineTypeSeries.  
  
### getMetadata() (deprecated)
    
    
    public abstract Map<String,String> getMetadata()

Use [#getMetadataMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.ComputeEngineTargetDetailsOrBuilder#com_google_cloud_vmmigration_v1_ComputeEngineTargetDetailsOrBuilder_getMetadataMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getMetadataCount()
    
    
    public abstract int getMetadataCount()

The metadata key/value pairs to assign to the VM.

`map<string, string> metadata = 16;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMetadataMap()
    
    
    public abstract Map<String,String> getMetadataMap()

The metadata key/value pairs to assign to the VM.

`map<string, string> metadata = 16;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getMetadataOrDefault(String key, String defaultValue)
    
    
    public abstract String getMetadataOrDefault(String key, String defaultValue)

The metadata key/value pairs to assign to the VM.

`map<string, string> metadata = 16;`

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

The metadata key/value pairs to assign to the VM.

`map<string, string> metadata = 16;`

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

List of NICs connected to this VM.

`repeated .google.cloud.vmmigration.v1.NetworkInterface network_interfaces = 7;`

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

List of NICs connected to this VM.

`repeated .google.cloud.vmmigration.v1.NetworkInterface network_interfaces = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getNetworkInterfacesList()
    
    
    public abstract List<NetworkInterface> getNetworkInterfacesList()

List of NICs connected to this VM.

`repeated .google.cloud.vmmigration.v1.NetworkInterface network_interfaces = 7;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[NetworkInterface](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmmigration/latest/com.google.cloud.vmmigration.v1.NetworkInterface)>` |   
  
### getNetworkInterfacesOrBuilder(int index)
    
    
    public abstract NetworkInterfaceOrBuilder getNetworkInterfacesOrBuilder(int index)

List of NICs connected to this VM.

`repeated .google.cloud.vmmigration.v1.NetworkInterface network_interfaces = 7;`

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

List of NICs connected to this VM.

`repeated .google.cloud.vmmigration.v1.NetworkInterface network_interfaces = 7;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.vmmigration.v1.NetworkInterfaceOrBuilder>` |   
  
### getNetworkTags(int index)
    
    
    public abstract String getNetworkTags(int index)

A list of network tags to associate with the VM.

`repeated string network_tags = 6;`

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

A list of network tags to associate with the VM.

`repeated string network_tags = 6;`

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

A list of network tags to associate with the VM.

`repeated string network_tags = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of networkTags.  
  
### getNetworkTagsList()
    
    
    public abstract List<String> getNetworkTagsList()

A list of network tags to associate with the VM.

`repeated string network_tags = 6;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the networkTags.  
  
### getProject()
    
    
    public abstract String getProject()

The Google Cloud target project ID or project name.

`string project = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The project.  
  
### getProjectBytes()
    
    
    public abstract ByteString getProjectBytes()

The Google Cloud target project ID or project name.

`string project = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for project.  
  
### getSecureBoot()
    
    
    public abstract boolean getSecureBoot()

Defines whether the instance has Secure Boot enabled. This can be set to true only if the VM boot option is EFI.

`bool secure_boot = 14;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The secureBoot.  
  
### getServiceAccount()
    
    
    public abstract String getServiceAccount()

The service account to associate the VM with.

`string service_account = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serviceAccount.  
  
### getServiceAccountBytes()
    
    
    public abstract ByteString getServiceAccountBytes()

The service account to associate the VM with.

`string service_account = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serviceAccount.  
  
### getStoragePool()
    
    
    public abstract String getStoragePool()

Optional. The storage pool used for the VM disks. If specified this will be the storage pool in which the disk is created. This is the full path of the storage pool resource, for example: "projects/my-project/zones/us-central1-a/storagePools/my-storage-pool". The storage pool must be in the same project and zone as the target disks. The storage pool's type must match the disk type.

`string storage_pool = 25 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The storagePool.  
  
### getStoragePoolBytes()
    
    
    public abstract ByteString getStoragePoolBytes()

Optional. The storage pool used for the VM disks. If specified this will be the storage pool in which the disk is created. This is the full path of the storage pool resource, for example: "projects/my-project/zones/us-central1-a/storagePools/my-storage-pool". The storage pool must be in the same project and zone as the target disks. The storage pool's type must match the disk type.

`string storage_pool = 25 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for storagePool.  
  
### getVmName()
    
    
    public abstract String getVmName()

The name of the VM to create.

`string vm_name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The vmName.  
  
### getVmNameBytes()
    
    
    public abstract ByteString getVmNameBytes()

The name of the VM to create.

`string vm_name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for vmName.  
  
### getZone()
    
    
    public abstract String getZone()

The zone in which to create the VM.

`string zone = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The zone.  
  
### getZoneBytes()
    
    
    public abstract ByteString getZoneBytes()

The zone in which to create the VM.

`string zone = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for zone.  
  
### hasAppliedLicense()
    
    
    public abstract boolean hasAppliedLicense()

The OS license returned from the adaptation module report.

`.google.cloud.vmmigration.v1.AppliedLicense applied_license = 12;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the appliedLicense field is set.  
  
### hasComputeScheduling()
    
    
    public abstract boolean hasComputeScheduling()

Compute instance scheduling information (if empty default is used).

`.google.cloud.vmmigration.v1.ComputeScheduling compute_scheduling = 13;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the computeScheduling field is set.  
  
### hasEncryption()
    
    
    public abstract boolean hasEncryption()

Optional. The encryption to apply to the VM disks.

` .google.cloud.vmmigration.v1.Encryption encryption = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the encryption field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
