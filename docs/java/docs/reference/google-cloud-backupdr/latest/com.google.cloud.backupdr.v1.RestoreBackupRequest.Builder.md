---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder
title: Class RestoreBackupRequest.Builder (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:34:59.288002+00:00
---

# Class RestoreBackupRequest.Builder (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RestoreBackupRequest.Builder (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class RestoreBackupRequest.Builder extends GeneratedMessage.Builder<RestoreBackupRequest.Builder> implements RestoreBackupRequestOrBuilder

Request message for restoring from a Backup.

Protobuf type `google.cloud.backupdr.v1.RestoreBackupRequest`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > RestoreBackupRequest.Builder

## Implements

[RestoreBackupRequestOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequestOrBuilder)

## Inherited Members

[AbstractMessage.Builder.findInitializationErrors()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_findInitializationErrors__)

[AbstractMessage.Builder.getInitializationErrorString()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_getInitializationErrorString__)

[AbstractMessage.Builder.internalMergeFrom(AbstractMessageLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_internalMergeFrom_com_google_protobuf_AbstractMessageLite_)

[AbstractMessage.Builder.mergeFrom(byte[])](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_byte___)

[AbstractMessage.Builder.mergeFrom(byte[],ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_byte___com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessage.Builder.mergeFrom(byte[],int,int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_byte___int_int_)

[AbstractMessage.Builder.mergeFrom(byte[],int,int,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_byte___int_int_com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessage.Builder.mergeFrom(ByteString)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_ByteString_)

[AbstractMessage.Builder.mergeFrom(ByteString,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_ByteString_com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessage.Builder.mergeFrom(CodedInputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_)

[AbstractMessage.Builder.mergeFrom(CodedInputStream,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessage.Builder.mergeFrom(Message)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

[AbstractMessage.Builder.mergeFrom(InputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_java_io_InputStream_)

[AbstractMessage.Builder.mergeFrom(InputStream,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_java_io_InputStream_com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessage.Builder.newUninitializedMessageException(Message)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_newUninitializedMessageException_com_google_protobuf_Message_)

[AbstractMessage.Builder.toString()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_toString__)

[AbstractMessageLite.Builder.<T>addAll(Iterable<T>,Collection<? super T>)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html#com_google_protobuf_AbstractMessageLite_Builder__T_addAll_java_lang_Iterable_T__java_util_Collection___super_T__)

[AbstractMessageLite.Builder.<T>addAll(Iterable<T>,List<? super T>)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html#com_google_protobuf_AbstractMessageLite_Builder__T_addAll_java_lang_Iterable_T__java_util_List___super_T__)

[AbstractMessageLite.Builder.internalMergeFrom(MessageType)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html#com_google_protobuf_AbstractMessageLite_Builder_internalMergeFrom_MessageType_)

[AbstractMessageLite.Builder.mergeDelimitedFrom(InputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html#com_google_protobuf_AbstractMessageLite_Builder_mergeDelimitedFrom_java_io_InputStream_)

[AbstractMessageLite.Builder.mergeDelimitedFrom(InputStream,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html#com_google_protobuf_AbstractMessageLite_Builder_mergeDelimitedFrom_java_io_InputStream_com_google_protobuf_ExtensionRegistryLite_)

[AbstractMessageLite.Builder.mergeFrom(MessageLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html#com_google_protobuf_AbstractMessageLite_Builder_mergeFrom_com_google_protobuf_MessageLite_)

[AbstractMessageLite.Builder.newUninitializedMessageException(MessageLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html#com_google_protobuf_AbstractMessageLite_Builder_newUninitializedMessageException_com_google_protobuf_MessageLite_)

[GeneratedMessage.Builder.addRepeatedField(Descriptors.FieldDescriptor,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_addRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_java_lang_Object_)

[GeneratedMessage.Builder.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

[GeneratedMessage.Builder.clearField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clearField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.Builder.clearOneof(Descriptors.OneofDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clearOneof_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessage.Builder.clone()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clone__)

[GeneratedMessage.Builder.getAllFields()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getAllFields__)

[GeneratedMessage.Builder.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

[GeneratedMessage.Builder.getField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.Builder.getFieldBuilder(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getFieldBuilder_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.Builder.getOneofFieldDescriptor(Descriptors.OneofDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getOneofFieldDescriptor_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessage.Builder.getParentForChildren()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getParentForChildren__)

[GeneratedMessage.Builder.getRepeatedField(Descriptors.FieldDescriptor,int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_int_)

[GeneratedMessage.Builder.getRepeatedFieldBuilder(Descriptors.FieldDescriptor,int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getRepeatedFieldBuilder_com_google_protobuf_Descriptors_FieldDescriptor_int_)

[GeneratedMessage.Builder.getRepeatedFieldCount(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getRepeatedFieldCount_com_google_protobuf_Descriptors_FieldDescriptor_)

com.google.protobuf.GeneratedMessage.Builder.getUnknownFieldSetBuilder()

[GeneratedMessage.Builder.getUnknownFields()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getUnknownFields__)

[GeneratedMessage.Builder.hasField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_hasField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.Builder.hasOneof(Descriptors.OneofDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_hasOneof_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessage.Builder.internalGetFieldAccessorTable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_internalGetFieldAccessorTable__)

[GeneratedMessage.Builder.internalGetMapField(int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_internalGetMapField_int_)

com.google.protobuf.GeneratedMessage.Builder.internalGetMapFieldReflection(int)

[GeneratedMessage.Builder.internalGetMutableMapField(int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_internalGetMutableMapField_int_)

com.google.protobuf.GeneratedMessage.Builder.internalGetMutableMapFieldReflection(int)

[GeneratedMessage.Builder.isClean()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_isClean__)

[GeneratedMessage.Builder.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_isInitialized__)

[GeneratedMessage.Builder.markClean()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_markClean__)

[GeneratedMessage.Builder.mergeUnknownFields(UnknownFieldSet)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_mergeUnknownFields_com_google_protobuf_UnknownFieldSet_)

com.google.protobuf.GeneratedMessage.Builder.mergeUnknownLengthDelimitedField(int,com.google.protobuf.ByteString)

com.google.protobuf.GeneratedMessage.Builder.mergeUnknownVarintField(int,int)

[GeneratedMessage.Builder.newBuilderForField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_newBuilderForField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.Builder.onBuilt()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_onBuilt__)

[GeneratedMessage.Builder.onChanged()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_onChanged__)

com.google.protobuf.GeneratedMessage.Builder.parseUnknownField(com.google.protobuf.CodedInputStream,com.google.protobuf.ExtensionRegistryLite,int)

[GeneratedMessage.Builder.setField(Descriptors.FieldDescriptor,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_setField_com_google_protobuf_Descriptors_FieldDescriptor_java_lang_Object_)

[GeneratedMessage.Builder.setRepeatedField(Descriptors.FieldDescriptor,int,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_setRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_int_java_lang_Object_)

com.google.protobuf.GeneratedMessage.Builder.setUnknownFieldSetBuilder(com.google.protobuf.UnknownFieldSet.Builder)

[GeneratedMessage.Builder.setUnknownFields(UnknownFieldSet)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_setUnknownFields_com_google_protobuf_UnknownFieldSet_)

com.google.protobuf.GeneratedMessage.Builder.setUnknownFieldsProto3(com.google.protobuf.UnknownFieldSet)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Methods 

### getDescriptor()
    
    
    public static final Descriptors.Descriptor getDescriptor()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
  
## Methods 

### build()
    
    
    public RestoreBackupRequest build()

**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest)` |   
  
### buildPartial()
    
    
    public RestoreBackupRequest buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest)` |   
  
### clear()
    
    
    public RestoreBackupRequest.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearClearOverridesFieldMask()
    
    
    public RestoreBackupRequest.Builder clearClearOverridesFieldMask()

Optional. A field mask used to clear server-side default values for fields within the `instance_properties` oneof.

When a field in this mask is cleared, the server will not apply its default logic (like inheriting a value from the source) for that field.

The most common current use case is clearing default encryption keys.

Examples of field mask paths:

  * Compute Instance Disks: `compute_instance_restore_properties.disks.*.disk_encryption_key`
  * Single Disk: `disk_restore_properties.disk_encryption_key`



` optional .google.protobuf.FieldMask clear_overrides_field_mask = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### clearComputeInstanceRestoreProperties()
    
    
    public RestoreBackupRequest.Builder clearComputeInstanceRestoreProperties()

Compute Engine instance properties to be overridden during restore.

` .google.cloud.backupdr.v1.ComputeInstanceRestoreProperties compute_instance_restore_properties = 4; `

**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### clearComputeInstanceTargetEnvironment()
    
    
    public RestoreBackupRequest.Builder clearComputeInstanceTargetEnvironment()

Compute Engine target environment to be used during restore.

` .google.cloud.backupdr.v1.ComputeInstanceTargetEnvironment compute_instance_target_environment = 3; `

**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### clearDiskRestoreProperties()
    
    
    public RestoreBackupRequest.Builder clearDiskRestoreProperties()

Disk properties to be overridden during restore.

`.google.cloud.backupdr.v1.DiskRestoreProperties disk_restore_properties = 7;`

**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### clearDiskTargetEnvironment()
    
    
    public RestoreBackupRequest.Builder clearDiskTargetEnvironment()

Disk target environment to be used during restore.

`.google.cloud.backupdr.v1.DiskTargetEnvironment disk_target_environment = 5;`

**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### clearInstanceProperties()
    
    
    public RestoreBackupRequest.Builder clearInstanceProperties()

**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### clearName()
    
    
    public RestoreBackupRequest.Builder clearName()

Required. The resource name of the Backup instance, in the format 'projects/*/locations/*/backupVaults/*/dataSources/*/backups/'.

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` | This builder for chaining.  
  
### clearRegionDiskTargetEnvironment()
    
    
    public RestoreBackupRequest.Builder clearRegionDiskTargetEnvironment()

Region disk target environment to be used during restore.

` .google.cloud.backupdr.v1.RegionDiskTargetEnvironment region_disk_target_environment = 6; `

**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### clearRequestId()
    
    
    public RestoreBackupRequest.Builder clearRequestId()

Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

` string request_id = 2 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` | This builder for chaining.  
  
### clearTargetEnvironment()
    
    
    public RestoreBackupRequest.Builder clearTargetEnvironment()

**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### getClearOverridesFieldMask()
    
    
    public FieldMask getClearOverridesFieldMask()

Optional. A field mask used to clear server-side default values for fields within the `instance_properties` oneof.

When a field in this mask is cleared, the server will not apply its default logic (like inheriting a value from the source) for that field.

The most common current use case is clearing default encryption keys.

Examples of field mask paths:

  * Compute Instance Disks: `compute_instance_restore_properties.disks.*.disk_encryption_key`
  * Single Disk: `disk_restore_properties.disk_encryption_key`



` optional .google.protobuf.FieldMask clear_overrides_field_mask = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)` | The clearOverridesFieldMask.  
  
### getClearOverridesFieldMaskBuilder()
    
    
    public FieldMask.Builder getClearOverridesFieldMaskBuilder()

Optional. A field mask used to clear server-side default values for fields within the `instance_properties` oneof.

When a field in this mask is cleared, the server will not apply its default logic (like inheriting a value from the source) for that field.

The most common current use case is clearing default encryption keys.

Examples of field mask paths:

  * Compute Instance Disks: `compute_instance_restore_properties.disks.*.disk_encryption_key`
  * Single Disk: `disk_restore_properties.disk_encryption_key`



` optional .google.protobuf.FieldMask clear_overrides_field_mask = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html)` |   
  
### getClearOverridesFieldMaskOrBuilder()
    
    
    public FieldMaskOrBuilder getClearOverridesFieldMaskOrBuilder()

Optional. A field mask used to clear server-side default values for fields within the `instance_properties` oneof.

When a field in this mask is cleared, the server will not apply its default logic (like inheriting a value from the source) for that field.

The most common current use case is clearing default encryption keys.

Examples of field mask paths:

  * Compute Instance Disks: `compute_instance_restore_properties.disks.*.disk_encryption_key`
  * Single Disk: `disk_restore_properties.disk_encryption_key`



` optional .google.protobuf.FieldMask clear_overrides_field_mask = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FieldMaskOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMaskOrBuilder.html)` |   
  
### getComputeInstanceRestoreProperties()
    
    
    public ComputeInstanceRestoreProperties getComputeInstanceRestoreProperties()

Compute Engine instance properties to be overridden during restore.

` .google.cloud.backupdr.v1.ComputeInstanceRestoreProperties compute_instance_restore_properties = 4; `

**Returns**  
---  
**Type** | **Description**  
`[ComputeInstanceRestoreProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ComputeInstanceRestoreProperties)` | The computeInstanceRestoreProperties.  
  
### getComputeInstanceRestorePropertiesBuilder()
    
    
    public ComputeInstanceRestoreProperties.Builder getComputeInstanceRestorePropertiesBuilder()

Compute Engine instance properties to be overridden during restore.

` .google.cloud.backupdr.v1.ComputeInstanceRestoreProperties compute_instance_restore_properties = 4; `

**Returns**  
---  
**Type** | **Description**  
`[ComputeInstanceRestoreProperties.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ComputeInstanceRestoreProperties.Builder)` |   
  
### getComputeInstanceRestorePropertiesOrBuilder()
    
    
    public ComputeInstanceRestorePropertiesOrBuilder getComputeInstanceRestorePropertiesOrBuilder()

Compute Engine instance properties to be overridden during restore.

` .google.cloud.backupdr.v1.ComputeInstanceRestoreProperties compute_instance_restore_properties = 4; `

**Returns**  
---  
**Type** | **Description**  
`[ComputeInstanceRestorePropertiesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ComputeInstanceRestorePropertiesOrBuilder)` |   
  
### getComputeInstanceTargetEnvironment()
    
    
    public ComputeInstanceTargetEnvironment getComputeInstanceTargetEnvironment()

Compute Engine target environment to be used during restore.

` .google.cloud.backupdr.v1.ComputeInstanceTargetEnvironment compute_instance_target_environment = 3; `

**Returns**  
---  
**Type** | **Description**  
`[ComputeInstanceTargetEnvironment](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ComputeInstanceTargetEnvironment)` | The computeInstanceTargetEnvironment.  
  
### getComputeInstanceTargetEnvironmentBuilder()
    
    
    public ComputeInstanceTargetEnvironment.Builder getComputeInstanceTargetEnvironmentBuilder()

Compute Engine target environment to be used during restore.

` .google.cloud.backupdr.v1.ComputeInstanceTargetEnvironment compute_instance_target_environment = 3; `

**Returns**  
---  
**Type** | **Description**  
`[ComputeInstanceTargetEnvironment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ComputeInstanceTargetEnvironment.Builder)` |   
  
### getComputeInstanceTargetEnvironmentOrBuilder()
    
    
    public ComputeInstanceTargetEnvironmentOrBuilder getComputeInstanceTargetEnvironmentOrBuilder()

Compute Engine target environment to be used during restore.

` .google.cloud.backupdr.v1.ComputeInstanceTargetEnvironment compute_instance_target_environment = 3; `

**Returns**  
---  
**Type** | **Description**  
`[ComputeInstanceTargetEnvironmentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ComputeInstanceTargetEnvironmentOrBuilder)` |   
  
### getDefaultInstanceForType()
    
    
    public RestoreBackupRequest getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getDiskRestoreProperties()
    
    
    public DiskRestoreProperties getDiskRestoreProperties()

Disk properties to be overridden during restore.

`.google.cloud.backupdr.v1.DiskRestoreProperties disk_restore_properties = 7;`

**Returns**  
---  
**Type** | **Description**  
`[DiskRestoreProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DiskRestoreProperties)` | The diskRestoreProperties.  
  
### getDiskRestorePropertiesBuilder()
    
    
    public DiskRestoreProperties.Builder getDiskRestorePropertiesBuilder()

Disk properties to be overridden during restore.

`.google.cloud.backupdr.v1.DiskRestoreProperties disk_restore_properties = 7;`

**Returns**  
---  
**Type** | **Description**  
`[DiskRestoreProperties.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DiskRestoreProperties.Builder)` |   
  
### getDiskRestorePropertiesOrBuilder()
    
    
    public DiskRestorePropertiesOrBuilder getDiskRestorePropertiesOrBuilder()

Disk properties to be overridden during restore.

`.google.cloud.backupdr.v1.DiskRestoreProperties disk_restore_properties = 7;`

**Returns**  
---  
**Type** | **Description**  
`[DiskRestorePropertiesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DiskRestorePropertiesOrBuilder)` |   
  
### getDiskTargetEnvironment()
    
    
    public DiskTargetEnvironment getDiskTargetEnvironment()

Disk target environment to be used during restore.

`.google.cloud.backupdr.v1.DiskTargetEnvironment disk_target_environment = 5;`

**Returns**  
---  
**Type** | **Description**  
`[DiskTargetEnvironment](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DiskTargetEnvironment)` | The diskTargetEnvironment.  
  
### getDiskTargetEnvironmentBuilder()
    
    
    public DiskTargetEnvironment.Builder getDiskTargetEnvironmentBuilder()

Disk target environment to be used during restore.

`.google.cloud.backupdr.v1.DiskTargetEnvironment disk_target_environment = 5;`

**Returns**  
---  
**Type** | **Description**  
`[DiskTargetEnvironment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DiskTargetEnvironment.Builder)` |   
  
### getDiskTargetEnvironmentOrBuilder()
    
    
    public DiskTargetEnvironmentOrBuilder getDiskTargetEnvironmentOrBuilder()

Disk target environment to be used during restore.

`.google.cloud.backupdr.v1.DiskTargetEnvironment disk_target_environment = 5;`

**Returns**  
---  
**Type** | **Description**  
`[DiskTargetEnvironmentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DiskTargetEnvironmentOrBuilder)` |   
  
### getInstancePropertiesCase()
    
    
    public RestoreBackupRequest.InstancePropertiesCase getInstancePropertiesCase()

**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.InstancePropertiesCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.InstancePropertiesCase)` |   
  
### getName()
    
    
    public String getName()

Required. The resource name of the Backup instance, in the format 'projects/*/locations/*/backupVaults/*/dataSources/*/backups/'.

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

Required. The resource name of the Backup instance, in the format 'projects/*/locations/*/backupVaults/*/dataSources/*/backups/'.

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getRegionDiskTargetEnvironment()
    
    
    public RegionDiskTargetEnvironment getRegionDiskTargetEnvironment()

Region disk target environment to be used during restore.

` .google.cloud.backupdr.v1.RegionDiskTargetEnvironment region_disk_target_environment = 6; `

**Returns**  
---  
**Type** | **Description**  
`[RegionDiskTargetEnvironment](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RegionDiskTargetEnvironment)` | The regionDiskTargetEnvironment.  
  
### getRegionDiskTargetEnvironmentBuilder()
    
    
    public RegionDiskTargetEnvironment.Builder getRegionDiskTargetEnvironmentBuilder()

Region disk target environment to be used during restore.

` .google.cloud.backupdr.v1.RegionDiskTargetEnvironment region_disk_target_environment = 6; `

**Returns**  
---  
**Type** | **Description**  
`[RegionDiskTargetEnvironment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RegionDiskTargetEnvironment.Builder)` |   
  
### getRegionDiskTargetEnvironmentOrBuilder()
    
    
    public RegionDiskTargetEnvironmentOrBuilder getRegionDiskTargetEnvironmentOrBuilder()

Region disk target environment to be used during restore.

` .google.cloud.backupdr.v1.RegionDiskTargetEnvironment region_disk_target_environment = 6; `

**Returns**  
---  
**Type** | **Description**  
`[RegionDiskTargetEnvironmentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RegionDiskTargetEnvironmentOrBuilder)` |   
  
### getRequestId()
    
    
    public String getRequestId()

Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

` string request_id = 2 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The requestId.  
  
### getRequestIdBytes()
    
    
    public ByteString getRequestIdBytes()

Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

` string request_id = 2 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for requestId.  
  
### getTargetEnvironmentCase()
    
    
    public RestoreBackupRequest.TargetEnvironmentCase getTargetEnvironmentCase()

**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.TargetEnvironmentCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.TargetEnvironmentCase)` |   
  
### hasClearOverridesFieldMask()
    
    
    public boolean hasClearOverridesFieldMask()

Optional. A field mask used to clear server-side default values for fields within the `instance_properties` oneof.

When a field in this mask is cleared, the server will not apply its default logic (like inheriting a value from the source) for that field.

The most common current use case is clearing default encryption keys.

Examples of field mask paths:

  * Compute Instance Disks: `compute_instance_restore_properties.disks.*.disk_encryption_key`
  * Single Disk: `disk_restore_properties.disk_encryption_key`



` optional .google.protobuf.FieldMask clear_overrides_field_mask = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the clearOverridesFieldMask field is set.  
  
### hasComputeInstanceRestoreProperties()
    
    
    public boolean hasComputeInstanceRestoreProperties()

Compute Engine instance properties to be overridden during restore.

` .google.cloud.backupdr.v1.ComputeInstanceRestoreProperties compute_instance_restore_properties = 4; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the computeInstanceRestoreProperties field is set.  
  
### hasComputeInstanceTargetEnvironment()
    
    
    public boolean hasComputeInstanceTargetEnvironment()

Compute Engine target environment to be used during restore.

` .google.cloud.backupdr.v1.ComputeInstanceTargetEnvironment compute_instance_target_environment = 3; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the computeInstanceTargetEnvironment field is set.  
  
### hasDiskRestoreProperties()
    
    
    public boolean hasDiskRestoreProperties()

Disk properties to be overridden during restore.

`.google.cloud.backupdr.v1.DiskRestoreProperties disk_restore_properties = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the diskRestoreProperties field is set.  
  
### hasDiskTargetEnvironment()
    
    
    public boolean hasDiskTargetEnvironment()

Disk target environment to be used during restore.

`.google.cloud.backupdr.v1.DiskTargetEnvironment disk_target_environment = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the diskTargetEnvironment field is set.  
  
### hasRegionDiskTargetEnvironment()
    
    
    public boolean hasRegionDiskTargetEnvironment()

Region disk target environment to be used during restore.

` .google.cloud.backupdr.v1.RegionDiskTargetEnvironment region_disk_target_environment = 6; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the regionDiskTargetEnvironment field is set.  
  
### internalGetFieldAccessorTable()
    
    
    protected GeneratedMessage.FieldAccessorTable internalGetFieldAccessorTable()

**Returns**  
---  
**Type** | **Description**  
`[FieldAccessorTable](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.FieldAccessorTable.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.internalGetFieldAccessorTable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_internalGetFieldAccessorTable__)

### isInitialized()
    
    
    public final boolean isInitialized()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_isInitialized__)

### mergeClearOverridesFieldMask(FieldMask value)
    
    
    public RestoreBackupRequest.Builder mergeClearOverridesFieldMask(FieldMask value)

Optional. A field mask used to clear server-side default values for fields within the `instance_properties` oneof.

When a field in this mask is cleared, the server will not apply its default logic (like inheriting a value from the source) for that field.

The most common current use case is clearing default encryption keys.

Examples of field mask paths:

  * Compute Instance Disks: `compute_instance_restore_properties.disks.*.disk_encryption_key`
  * Single Disk: `disk_restore_properties.disk_encryption_key`



` optional .google.protobuf.FieldMask clear_overrides_field_mask = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### mergeComputeInstanceRestoreProperties(ComputeInstanceRestoreProperties value)
    
    
    public RestoreBackupRequest.Builder mergeComputeInstanceRestoreProperties(ComputeInstanceRestoreProperties value)

Compute Engine instance properties to be overridden during restore.

` .google.cloud.backupdr.v1.ComputeInstanceRestoreProperties compute_instance_restore_properties = 4; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ComputeInstanceRestoreProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ComputeInstanceRestoreProperties)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### mergeComputeInstanceTargetEnvironment(ComputeInstanceTargetEnvironment value)
    
    
    public RestoreBackupRequest.Builder mergeComputeInstanceTargetEnvironment(ComputeInstanceTargetEnvironment value)

Compute Engine target environment to be used during restore.

` .google.cloud.backupdr.v1.ComputeInstanceTargetEnvironment compute_instance_target_environment = 3; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ComputeInstanceTargetEnvironment](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ComputeInstanceTargetEnvironment)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### mergeDiskRestoreProperties(DiskRestoreProperties value)
    
    
    public RestoreBackupRequest.Builder mergeDiskRestoreProperties(DiskRestoreProperties value)

Disk properties to be overridden during restore.

`.google.cloud.backupdr.v1.DiskRestoreProperties disk_restore_properties = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DiskRestoreProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DiskRestoreProperties)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### mergeDiskTargetEnvironment(DiskTargetEnvironment value)
    
    
    public RestoreBackupRequest.Builder mergeDiskTargetEnvironment(DiskTargetEnvironment value)

Disk target environment to be used during restore.

`.google.cloud.backupdr.v1.DiskTargetEnvironment disk_target_environment = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DiskTargetEnvironment](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DiskTargetEnvironment)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### mergeFrom(RestoreBackupRequest other)
    
    
    public RestoreBackupRequest.Builder mergeFrom(RestoreBackupRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RestoreBackupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public RestoreBackupRequest.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public RestoreBackupRequest.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeRegionDiskTargetEnvironment(RegionDiskTargetEnvironment value)
    
    
    public RestoreBackupRequest.Builder mergeRegionDiskTargetEnvironment(RegionDiskTargetEnvironment value)

Region disk target environment to be used during restore.

` .google.cloud.backupdr.v1.RegionDiskTargetEnvironment region_disk_target_environment = 6; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[RegionDiskTargetEnvironment](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RegionDiskTargetEnvironment)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### setClearOverridesFieldMask(FieldMask value)
    
    
    public RestoreBackupRequest.Builder setClearOverridesFieldMask(FieldMask value)

Optional. A field mask used to clear server-side default values for fields within the `instance_properties` oneof.

When a field in this mask is cleared, the server will not apply its default logic (like inheriting a value from the source) for that field.

The most common current use case is clearing default encryption keys.

Examples of field mask paths:

  * Compute Instance Disks: `compute_instance_restore_properties.disks.*.disk_encryption_key`
  * Single Disk: `disk_restore_properties.disk_encryption_key`



` optional .google.protobuf.FieldMask clear_overrides_field_mask = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### setClearOverridesFieldMask(FieldMask.Builder builderForValue)
    
    
    public RestoreBackupRequest.Builder setClearOverridesFieldMask(FieldMask.Builder builderForValue)

Optional. A field mask used to clear server-side default values for fields within the `instance_properties` oneof.

When a field in this mask is cleared, the server will not apply its default logic (like inheriting a value from the source) for that field.

The most common current use case is clearing default encryption keys.

Examples of field mask paths:

  * Compute Instance Disks: `compute_instance_restore_properties.disks.*.disk_encryption_key`
  * Single Disk: `disk_restore_properties.disk_encryption_key`



` optional .google.protobuf.FieldMask clear_overrides_field_mask = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### setComputeInstanceRestoreProperties(ComputeInstanceRestoreProperties value)
    
    
    public RestoreBackupRequest.Builder setComputeInstanceRestoreProperties(ComputeInstanceRestoreProperties value)

Compute Engine instance properties to be overridden during restore.

` .google.cloud.backupdr.v1.ComputeInstanceRestoreProperties compute_instance_restore_properties = 4; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ComputeInstanceRestoreProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ComputeInstanceRestoreProperties)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### setComputeInstanceRestoreProperties(ComputeInstanceRestoreProperties.Builder builderForValue)
    
    
    public RestoreBackupRequest.Builder setComputeInstanceRestoreProperties(ComputeInstanceRestoreProperties.Builder builderForValue)

Compute Engine instance properties to be overridden during restore.

` .google.cloud.backupdr.v1.ComputeInstanceRestoreProperties compute_instance_restore_properties = 4; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ComputeInstanceRestoreProperties.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ComputeInstanceRestoreProperties.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### setComputeInstanceTargetEnvironment(ComputeInstanceTargetEnvironment value)
    
    
    public RestoreBackupRequest.Builder setComputeInstanceTargetEnvironment(ComputeInstanceTargetEnvironment value)

Compute Engine target environment to be used during restore.

` .google.cloud.backupdr.v1.ComputeInstanceTargetEnvironment compute_instance_target_environment = 3; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ComputeInstanceTargetEnvironment](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ComputeInstanceTargetEnvironment)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### setComputeInstanceTargetEnvironment(ComputeInstanceTargetEnvironment.Builder builderForValue)
    
    
    public RestoreBackupRequest.Builder setComputeInstanceTargetEnvironment(ComputeInstanceTargetEnvironment.Builder builderForValue)

Compute Engine target environment to be used during restore.

` .google.cloud.backupdr.v1.ComputeInstanceTargetEnvironment compute_instance_target_environment = 3; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ComputeInstanceTargetEnvironment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.ComputeInstanceTargetEnvironment.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### setDiskRestoreProperties(DiskRestoreProperties value)
    
    
    public RestoreBackupRequest.Builder setDiskRestoreProperties(DiskRestoreProperties value)

Disk properties to be overridden during restore.

`.google.cloud.backupdr.v1.DiskRestoreProperties disk_restore_properties = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DiskRestoreProperties](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DiskRestoreProperties)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### setDiskRestoreProperties(DiskRestoreProperties.Builder builderForValue)
    
    
    public RestoreBackupRequest.Builder setDiskRestoreProperties(DiskRestoreProperties.Builder builderForValue)

Disk properties to be overridden during restore.

`.google.cloud.backupdr.v1.DiskRestoreProperties disk_restore_properties = 7;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[DiskRestoreProperties.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DiskRestoreProperties.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### setDiskTargetEnvironment(DiskTargetEnvironment value)
    
    
    public RestoreBackupRequest.Builder setDiskTargetEnvironment(DiskTargetEnvironment value)

Disk target environment to be used during restore.

`.google.cloud.backupdr.v1.DiskTargetEnvironment disk_target_environment = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DiskTargetEnvironment](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DiskTargetEnvironment)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### setDiskTargetEnvironment(DiskTargetEnvironment.Builder builderForValue)
    
    
    public RestoreBackupRequest.Builder setDiskTargetEnvironment(DiskTargetEnvironment.Builder builderForValue)

Disk target environment to be used during restore.

`.google.cloud.backupdr.v1.DiskTargetEnvironment disk_target_environment = 5;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[DiskTargetEnvironment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.DiskTargetEnvironment.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### setName(String value)
    
    
    public RestoreBackupRequest.Builder setName(String value)

Required. The resource name of the Backup instance, in the format 'projects/*/locations/*/backupVaults/*/dataSources/*/backups/'.

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public RestoreBackupRequest.Builder setNameBytes(ByteString value)

Required. The resource name of the Backup instance, in the format 'projects/*/locations/*/backupVaults/*/dataSources/*/backups/'.

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` | This builder for chaining.  
  
### setRegionDiskTargetEnvironment(RegionDiskTargetEnvironment value)
    
    
    public RestoreBackupRequest.Builder setRegionDiskTargetEnvironment(RegionDiskTargetEnvironment value)

Region disk target environment to be used during restore.

` .google.cloud.backupdr.v1.RegionDiskTargetEnvironment region_disk_target_environment = 6; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[RegionDiskTargetEnvironment](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RegionDiskTargetEnvironment)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### setRegionDiskTargetEnvironment(RegionDiskTargetEnvironment.Builder builderForValue)
    
    
    public RestoreBackupRequest.Builder setRegionDiskTargetEnvironment(RegionDiskTargetEnvironment.Builder builderForValue)

Region disk target environment to be used during restore.

` .google.cloud.backupdr.v1.RegionDiskTargetEnvironment region_disk_target_environment = 6; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[RegionDiskTargetEnvironment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RegionDiskTargetEnvironment.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` |   
  
### setRequestId(String value)
    
    
    public RestoreBackupRequest.Builder setRequestId(String value)

Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

` string request_id = 2 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_info) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The requestId to set.  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` | This builder for chaining.  
  
### setRequestIdBytes(ByteString value)
    
    
    public RestoreBackupRequest.Builder setRequestIdBytes(ByteString value)

Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

` string request_id = 2 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_info) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for requestId to set.  
**Returns**  
---  
**Type** | **Description**  
`[RestoreBackupRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RestoreBackupRequest.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
