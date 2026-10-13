---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder
title: Class BackupConfigDetails.Builder (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:34:22.906533+00:00
---

# Class BackupConfigDetails.Builder (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BackupConfigDetails.Builder (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class BackupConfigDetails.Builder extends GeneratedMessage.Builder<BackupConfigDetails.Builder> implements BackupConfigDetailsOrBuilder

BackupConfigDetails has information about how the resource is configured for backups and about the most recent backup taken for this configuration.

Protobuf type `google.cloud.backupdr.v1.BackupConfigDetails`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > BackupConfigDetails.Builder

## Implements

[BackupConfigDetailsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetailsOrBuilder)

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

### addAllBackupLocations(Iterable<? extends BackupLocation> values)
    
    
    public BackupConfigDetails.Builder addAllBackupLocations(Iterable<? extends BackupLocation> values)

The locations where the backups are to be stored.

`repeated .google.cloud.backupdr.v1.BackupLocation backup_locations = 12;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.backupdr.v1.BackupLocation>`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### addBackupLocations(BackupLocation value)
    
    
    public BackupConfigDetails.Builder addBackupLocations(BackupLocation value)

The locations where the backups are to be stored.

`repeated .google.cloud.backupdr.v1.BackupLocation backup_locations = 12;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BackupLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupLocation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### addBackupLocations(BackupLocation.Builder builderForValue)
    
    
    public BackupConfigDetails.Builder addBackupLocations(BackupLocation.Builder builderForValue)

The locations where the backups are to be stored.

`repeated .google.cloud.backupdr.v1.BackupLocation backup_locations = 12;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[BackupLocation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupLocation.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### addBackupLocations(int index, BackupLocation value)
    
    
    public BackupConfigDetails.Builder addBackupLocations(int index, BackupLocation value)

The locations where the backups are to be stored.

`repeated .google.cloud.backupdr.v1.BackupLocation backup_locations = 12;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[BackupLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupLocation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### addBackupLocations(int index, BackupLocation.Builder builderForValue)
    
    
    public BackupConfigDetails.Builder addBackupLocations(int index, BackupLocation.Builder builderForValue)

The locations where the backups are to be stored.

`repeated .google.cloud.backupdr.v1.BackupLocation backup_locations = 12;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[BackupLocation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupLocation.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### addBackupLocationsBuilder()
    
    
    public BackupLocation.Builder addBackupLocationsBuilder()

The locations where the backups are to be stored.

`repeated .google.cloud.backupdr.v1.BackupLocation backup_locations = 12;`

**Returns**  
---  
**Type** | **Description**  
`[BackupLocation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupLocation.Builder)` |   
  
### addBackupLocationsBuilder(int index)
    
    
    public BackupLocation.Builder addBackupLocationsBuilder(int index)

The locations where the backups are to be stored.

`repeated .google.cloud.backupdr.v1.BackupLocation backup_locations = 12;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupLocation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupLocation.Builder)` |   
  
### build()
    
    
    public BackupConfigDetails build()

**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails)` |   
  
### buildPartial()
    
    
    public BackupConfigDetails buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails)` |   
  
### clear()
    
    
    public BackupConfigDetails.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearApplicableResource()
    
    
    public BackupConfigDetails.Builder clearApplicableResource()

Output only. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the resource that is applicable for the backup configuration. Example: "//compute.googleapis.com/projects/{project}/zones/{zone}/instances/{instance}"

`string applicable_resource = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` | This builder for chaining.  
  
### clearBackupConfigSource()
    
    
    public BackupConfigDetails.Builder clearBackupConfigSource()

Output only. The full resource name of the backup config source resource. For example, "//backupdr.googleapis.com/v1/projects/{project}/locations/{region}/backupPlans/{backupplanId}" or "//compute.googleapis.com/projects/{project}/locations/{region}/resourcePolicies/{resourcePolicyId}".

`string backup_config_source = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` | This builder for chaining.  
  
### clearBackupConfigSourceDisplayName()
    
    
    public BackupConfigDetails.Builder clearBackupConfigSourceDisplayName()

Output only. The display name of the backup config source resource.

` string backup_config_source_display_name = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` | This builder for chaining.  
  
### clearBackupDrPlanConfig()
    
    
    public BackupConfigDetails.Builder clearBackupDrPlanConfig()

Google Cloud Backup and DR's Backup Plan specific data.

`.google.cloud.backupdr.v1.BackupDrPlanConfig backup_dr_plan_config = 10;`

**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### clearBackupDrTemplateConfig()
    
    
    public BackupConfigDetails.Builder clearBackupDrTemplateConfig()

Google Cloud Backup and DR's Template specific data.

`.google.cloud.backupdr.v1.BackupDrTemplateConfig backup_dr_template_config = 11;`

**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### clearBackupLocations()
    
    
    public BackupConfigDetails.Builder clearBackupLocations()

The locations where the backups are to be stored.

`repeated .google.cloud.backupdr.v1.BackupLocation backup_locations = 12;`

**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### clearBackupVault()
    
    
    public BackupConfigDetails.Builder clearBackupVault()

Output only. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the backup vault that will store the backups generated through this backup configuration. Example: "//backupdr.googleapis.com/v1/projects/{project}/locations/{region}/backupVaults/{backupvaultId}"

`string backup_vault = 8 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` | This builder for chaining.  
  
### clearLatestSuccessfulBackupTime()
    
    
    public BackupConfigDetails.Builder clearLatestSuccessfulBackupTime()

Output only. Timestamp of the latest successful backup created via this backup configuration.

` .google.protobuf.Timestamp latest_successful_backup_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### clearPitrSettings()
    
    
    public BackupConfigDetails.Builder clearPitrSettings()

Output only. Point in time recovery settings of the backup configuration resource.

` .google.cloud.backupdr.v1.PitrSettings pitr_settings = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### clearPlanSpecificConfig()
    
    
    public BackupConfigDetails.Builder clearPlanSpecificConfig()

**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### clearState()
    
    
    public BackupConfigDetails.Builder clearState()

Output only. The state of the backup config resource.

` .google.cloud.backupdr.v1.BackupConfigDetails.State state = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` | This builder for chaining.  
  
### clearType()
    
    
    public BackupConfigDetails.Builder clearType()

Output only. The type of the backup config resource.

` .google.cloud.backupdr.v1.BackupConfigDetails.Type type = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` | This builder for chaining.  
  
### getApplicableResource()
    
    
    public String getApplicableResource()

Output only. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the resource that is applicable for the backup configuration. Example: "//compute.googleapis.com/projects/{project}/zones/{zone}/instances/{instance}"

`string applicable_resource = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The applicableResource.  
  
### getApplicableResourceBytes()
    
    
    public ByteString getApplicableResourceBytes()

Output only. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the resource that is applicable for the backup configuration. Example: "//compute.googleapis.com/projects/{project}/zones/{zone}/instances/{instance}"

`string applicable_resource = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for applicableResource.  
  
### getBackupConfigSource()
    
    
    public String getBackupConfigSource()

Output only. The full resource name of the backup config source resource. For example, "//backupdr.googleapis.com/v1/projects/{project}/locations/{region}/backupPlans/{backupplanId}" or "//compute.googleapis.com/projects/{project}/locations/{region}/resourcePolicies/{resourcePolicyId}".

`string backup_config_source = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The backupConfigSource.  
  
### getBackupConfigSourceBytes()
    
    
    public ByteString getBackupConfigSourceBytes()

Output only. The full resource name of the backup config source resource. For example, "//backupdr.googleapis.com/v1/projects/{project}/locations/{region}/backupPlans/{backupplanId}" or "//compute.googleapis.com/projects/{project}/locations/{region}/resourcePolicies/{resourcePolicyId}".

`string backup_config_source = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for backupConfigSource.  
  
### getBackupConfigSourceDisplayName()
    
    
    public String getBackupConfigSourceDisplayName()

Output only. The display name of the backup config source resource.

` string backup_config_source_display_name = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The backupConfigSourceDisplayName.  
  
### getBackupConfigSourceDisplayNameBytes()
    
    
    public ByteString getBackupConfigSourceDisplayNameBytes()

Output only. The display name of the backup config source resource.

` string backup_config_source_display_name = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for backupConfigSourceDisplayName.  
  
### getBackupDrPlanConfig()
    
    
    public BackupDrPlanConfig getBackupDrPlanConfig()

Google Cloud Backup and DR's Backup Plan specific data.

`.google.cloud.backupdr.v1.BackupDrPlanConfig backup_dr_plan_config = 10;`

**Returns**  
---  
**Type** | **Description**  
`[BackupDrPlanConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDrPlanConfig)` | The backupDrPlanConfig.  
  
### getBackupDrPlanConfigBuilder()
    
    
    public BackupDrPlanConfig.Builder getBackupDrPlanConfigBuilder()

Google Cloud Backup and DR's Backup Plan specific data.

`.google.cloud.backupdr.v1.BackupDrPlanConfig backup_dr_plan_config = 10;`

**Returns**  
---  
**Type** | **Description**  
`[BackupDrPlanConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDrPlanConfig.Builder)` |   
  
### getBackupDrPlanConfigOrBuilder()
    
    
    public BackupDrPlanConfigOrBuilder getBackupDrPlanConfigOrBuilder()

Google Cloud Backup and DR's Backup Plan specific data.

`.google.cloud.backupdr.v1.BackupDrPlanConfig backup_dr_plan_config = 10;`

**Returns**  
---  
**Type** | **Description**  
`[BackupDrPlanConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDrPlanConfigOrBuilder)` |   
  
### getBackupDrTemplateConfig()
    
    
    public BackupDrTemplateConfig getBackupDrTemplateConfig()

Google Cloud Backup and DR's Template specific data.

`.google.cloud.backupdr.v1.BackupDrTemplateConfig backup_dr_template_config = 11;`

**Returns**  
---  
**Type** | **Description**  
`[BackupDrTemplateConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDrTemplateConfig)` | The backupDrTemplateConfig.  
  
### getBackupDrTemplateConfigBuilder()
    
    
    public BackupDrTemplateConfig.Builder getBackupDrTemplateConfigBuilder()

Google Cloud Backup and DR's Template specific data.

`.google.cloud.backupdr.v1.BackupDrTemplateConfig backup_dr_template_config = 11;`

**Returns**  
---  
**Type** | **Description**  
`[BackupDrTemplateConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDrTemplateConfig.Builder)` |   
  
### getBackupDrTemplateConfigOrBuilder()
    
    
    public BackupDrTemplateConfigOrBuilder getBackupDrTemplateConfigOrBuilder()

Google Cloud Backup and DR's Template specific data.

`.google.cloud.backupdr.v1.BackupDrTemplateConfig backup_dr_template_config = 11;`

**Returns**  
---  
**Type** | **Description**  
`[BackupDrTemplateConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDrTemplateConfigOrBuilder)` |   
  
### getBackupLocations(int index)
    
    
    public BackupLocation getBackupLocations(int index)

The locations where the backups are to be stored.

`repeated .google.cloud.backupdr.v1.BackupLocation backup_locations = 12;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupLocation)` |   
  
### getBackupLocationsBuilder(int index)
    
    
    public BackupLocation.Builder getBackupLocationsBuilder(int index)

The locations where the backups are to be stored.

`repeated .google.cloud.backupdr.v1.BackupLocation backup_locations = 12;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupLocation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupLocation.Builder)` |   
  
### getBackupLocationsBuilderList()
    
    
    public List<BackupLocation.Builder> getBackupLocationsBuilderList()

The locations where the backups are to be stored.

`repeated .google.cloud.backupdr.v1.BackupLocation backup_locations = 12;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupLocation.Builder)>` |   
  
### getBackupLocationsCount()
    
    
    public int getBackupLocationsCount()

The locations where the backups are to be stored.

`repeated .google.cloud.backupdr.v1.BackupLocation backup_locations = 12;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBackupLocationsList()
    
    
    public List<BackupLocation> getBackupLocationsList()

The locations where the backups are to be stored.

`repeated .google.cloud.backupdr.v1.BackupLocation backup_locations = 12;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[BackupLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupLocation)>` |   
  
### getBackupLocationsOrBuilder(int index)
    
    
    public BackupLocationOrBuilder getBackupLocationsOrBuilder(int index)

The locations where the backups are to be stored.

`repeated .google.cloud.backupdr.v1.BackupLocation backup_locations = 12;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupLocationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupLocationOrBuilder)` |   
  
### getBackupLocationsOrBuilderList()
    
    
    public List<? extends BackupLocationOrBuilder> getBackupLocationsOrBuilderList()

The locations where the backups are to be stored.

`repeated .google.cloud.backupdr.v1.BackupLocation backup_locations = 12;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.backupdr.v1.BackupLocationOrBuilder>` |   
  
### getBackupVault()
    
    
    public String getBackupVault()

Output only. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the backup vault that will store the backups generated through this backup configuration. Example: "//backupdr.googleapis.com/v1/projects/{project}/locations/{region}/backupVaults/{backupvaultId}"

`string backup_vault = 8 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The backupVault.  
  
### getBackupVaultBytes()
    
    
    public ByteString getBackupVaultBytes()

Output only. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the backup vault that will store the backups generated through this backup configuration. Example: "//backupdr.googleapis.com/v1/projects/{project}/locations/{region}/backupVaults/{backupvaultId}"

`string backup_vault = 8 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for backupVault.  
  
### getDefaultInstanceForType()
    
    
    public BackupConfigDetails getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getLatestSuccessfulBackupTime()
    
    
    public Timestamp getLatestSuccessfulBackupTime()

Output only. Timestamp of the latest successful backup created via this backup configuration.

` .google.protobuf.Timestamp latest_successful_backup_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The latestSuccessfulBackupTime.  
  
### getLatestSuccessfulBackupTimeBuilder()
    
    
    public Timestamp.Builder getLatestSuccessfulBackupTimeBuilder()

Output only. Timestamp of the latest successful backup created via this backup configuration.

` .google.protobuf.Timestamp latest_successful_backup_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getLatestSuccessfulBackupTimeOrBuilder()
    
    
    public TimestampOrBuilder getLatestSuccessfulBackupTimeOrBuilder()

Output only. Timestamp of the latest successful backup created via this backup configuration.

` .google.protobuf.Timestamp latest_successful_backup_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getPitrSettings()
    
    
    public PitrSettings getPitrSettings()

Output only. Point in time recovery settings of the backup configuration resource.

` .google.cloud.backupdr.v1.PitrSettings pitr_settings = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[PitrSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.PitrSettings)` | The pitrSettings.  
  
### getPitrSettingsBuilder()
    
    
    public PitrSettings.Builder getPitrSettingsBuilder()

Output only. Point in time recovery settings of the backup configuration resource.

` .google.cloud.backupdr.v1.PitrSettings pitr_settings = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[PitrSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.PitrSettings.Builder)` |   
  
### getPitrSettingsOrBuilder()
    
    
    public PitrSettingsOrBuilder getPitrSettingsOrBuilder()

Output only. Point in time recovery settings of the backup configuration resource.

` .google.cloud.backupdr.v1.PitrSettings pitr_settings = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[PitrSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.PitrSettingsOrBuilder)` |   
  
### getPlanSpecificConfigCase()
    
    
    public BackupConfigDetails.PlanSpecificConfigCase getPlanSpecificConfigCase()

**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.PlanSpecificConfigCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.PlanSpecificConfigCase)` |   
  
### getState()
    
    
    public BackupConfigDetails.State getState()

Output only. The state of the backup config resource.

` .google.cloud.backupdr.v1.BackupConfigDetails.State state = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.State)` | The state.  
  
### getStateValue()
    
    
    public int getStateValue()

Output only. The state of the backup config resource.

` .google.cloud.backupdr.v1.BackupConfigDetails.State state = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getType()
    
    
    public BackupConfigDetails.Type getType()

Output only. The type of the backup config resource.

` .google.cloud.backupdr.v1.BackupConfigDetails.Type type = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Type)` | The type.  
  
### getTypeValue()
    
    
    public int getTypeValue()

Output only. The type of the backup config resource.

` .google.cloud.backupdr.v1.BackupConfigDetails.Type type = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for type.  
  
### hasBackupDrPlanConfig()
    
    
    public boolean hasBackupDrPlanConfig()

Google Cloud Backup and DR's Backup Plan specific data.

`.google.cloud.backupdr.v1.BackupDrPlanConfig backup_dr_plan_config = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the backupDrPlanConfig field is set.  
  
### hasBackupDrTemplateConfig()
    
    
    public boolean hasBackupDrTemplateConfig()

Google Cloud Backup and DR's Template specific data.

`.google.cloud.backupdr.v1.BackupDrTemplateConfig backup_dr_template_config = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the backupDrTemplateConfig field is set.  
  
### hasLatestSuccessfulBackupTime()
    
    
    public boolean hasLatestSuccessfulBackupTime()

Output only. Timestamp of the latest successful backup created via this backup configuration.

` .google.protobuf.Timestamp latest_successful_backup_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the latestSuccessfulBackupTime field is set.  
  
### hasPitrSettings()
    
    
    public boolean hasPitrSettings()

Output only. Point in time recovery settings of the backup configuration resource.

` .google.cloud.backupdr.v1.PitrSettings pitr_settings = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pitrSettings field is set.  
  
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

### mergeBackupDrPlanConfig(BackupDrPlanConfig value)
    
    
    public BackupConfigDetails.Builder mergeBackupDrPlanConfig(BackupDrPlanConfig value)

Google Cloud Backup and DR's Backup Plan specific data.

`.google.cloud.backupdr.v1.BackupDrPlanConfig backup_dr_plan_config = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BackupDrPlanConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDrPlanConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### mergeBackupDrTemplateConfig(BackupDrTemplateConfig value)
    
    
    public BackupConfigDetails.Builder mergeBackupDrTemplateConfig(BackupDrTemplateConfig value)

Google Cloud Backup and DR's Template specific data.

`.google.cloud.backupdr.v1.BackupDrTemplateConfig backup_dr_template_config = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BackupDrTemplateConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDrTemplateConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### mergeFrom(BackupConfigDetails other)
    
    
    public BackupConfigDetails.Builder mergeFrom(BackupConfigDetails other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BackupConfigDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public BackupConfigDetails.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public BackupConfigDetails.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeLatestSuccessfulBackupTime(Timestamp value)
    
    
    public BackupConfigDetails.Builder mergeLatestSuccessfulBackupTime(Timestamp value)

Output only. Timestamp of the latest successful backup created via this backup configuration.

` .google.protobuf.Timestamp latest_successful_backup_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### mergePitrSettings(PitrSettings value)
    
    
    public BackupConfigDetails.Builder mergePitrSettings(PitrSettings value)

Output only. Point in time recovery settings of the backup configuration resource.

` .google.cloud.backupdr.v1.PitrSettings pitr_settings = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PitrSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.PitrSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### removeBackupLocations(int index)
    
    
    public BackupConfigDetails.Builder removeBackupLocations(int index)

The locations where the backups are to be stored.

`repeated .google.cloud.backupdr.v1.BackupLocation backup_locations = 12;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### setApplicableResource(String value)
    
    
    public BackupConfigDetails.Builder setApplicableResource(String value)

Output only. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the resource that is applicable for the backup configuration. Example: "//compute.googleapis.com/projects/{project}/zones/{zone}/instances/{instance}"

`string applicable_resource = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The applicableResource to set.  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` | This builder for chaining.  
  
### setApplicableResourceBytes(ByteString value)
    
    
    public BackupConfigDetails.Builder setApplicableResourceBytes(ByteString value)

Output only. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the resource that is applicable for the backup configuration. Example: "//compute.googleapis.com/projects/{project}/zones/{zone}/instances/{instance}"

`string applicable_resource = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for applicableResource to set.  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` | This builder for chaining.  
  
### setBackupConfigSource(String value)
    
    
    public BackupConfigDetails.Builder setBackupConfigSource(String value)

Output only. The full resource name of the backup config source resource. For example, "//backupdr.googleapis.com/v1/projects/{project}/locations/{region}/backupPlans/{backupplanId}" or "//compute.googleapis.com/projects/{project}/locations/{region}/resourcePolicies/{resourcePolicyId}".

`string backup_config_source = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The backupConfigSource to set.  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` | This builder for chaining.  
  
### setBackupConfigSourceBytes(ByteString value)
    
    
    public BackupConfigDetails.Builder setBackupConfigSourceBytes(ByteString value)

Output only. The full resource name of the backup config source resource. For example, "//backupdr.googleapis.com/v1/projects/{project}/locations/{region}/backupPlans/{backupplanId}" or "//compute.googleapis.com/projects/{project}/locations/{region}/resourcePolicies/{resourcePolicyId}".

`string backup_config_source = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for backupConfigSource to set.  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` | This builder for chaining.  
  
### setBackupConfigSourceDisplayName(String value)
    
    
    public BackupConfigDetails.Builder setBackupConfigSourceDisplayName(String value)

Output only. The display name of the backup config source resource.

` string backup_config_source_display_name = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The backupConfigSourceDisplayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` | This builder for chaining.  
  
### setBackupConfigSourceDisplayNameBytes(ByteString value)
    
    
    public BackupConfigDetails.Builder setBackupConfigSourceDisplayNameBytes(ByteString value)

Output only. The display name of the backup config source resource.

` string backup_config_source_display_name = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for backupConfigSourceDisplayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` | This builder for chaining.  
  
### setBackupDrPlanConfig(BackupDrPlanConfig value)
    
    
    public BackupConfigDetails.Builder setBackupDrPlanConfig(BackupDrPlanConfig value)

Google Cloud Backup and DR's Backup Plan specific data.

`.google.cloud.backupdr.v1.BackupDrPlanConfig backup_dr_plan_config = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BackupDrPlanConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDrPlanConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### setBackupDrPlanConfig(BackupDrPlanConfig.Builder builderForValue)
    
    
    public BackupConfigDetails.Builder setBackupDrPlanConfig(BackupDrPlanConfig.Builder builderForValue)

Google Cloud Backup and DR's Backup Plan specific data.

`.google.cloud.backupdr.v1.BackupDrPlanConfig backup_dr_plan_config = 10;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[BackupDrPlanConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDrPlanConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### setBackupDrTemplateConfig(BackupDrTemplateConfig value)
    
    
    public BackupConfigDetails.Builder setBackupDrTemplateConfig(BackupDrTemplateConfig value)

Google Cloud Backup and DR's Template specific data.

`.google.cloud.backupdr.v1.BackupDrTemplateConfig backup_dr_template_config = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BackupDrTemplateConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDrTemplateConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### setBackupDrTemplateConfig(BackupDrTemplateConfig.Builder builderForValue)
    
    
    public BackupConfigDetails.Builder setBackupDrTemplateConfig(BackupDrTemplateConfig.Builder builderForValue)

Google Cloud Backup and DR's Template specific data.

`.google.cloud.backupdr.v1.BackupDrTemplateConfig backup_dr_template_config = 11;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[BackupDrTemplateConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupDrTemplateConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### setBackupLocations(int index, BackupLocation value)
    
    
    public BackupConfigDetails.Builder setBackupLocations(int index, BackupLocation value)

The locations where the backups are to be stored.

`repeated .google.cloud.backupdr.v1.BackupLocation backup_locations = 12;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[BackupLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupLocation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### setBackupLocations(int index, BackupLocation.Builder builderForValue)
    
    
    public BackupConfigDetails.Builder setBackupLocations(int index, BackupLocation.Builder builderForValue)

The locations where the backups are to be stored.

`repeated .google.cloud.backupdr.v1.BackupLocation backup_locations = 12;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[BackupLocation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupLocation.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### setBackupVault(String value)
    
    
    public BackupConfigDetails.Builder setBackupVault(String value)

Output only. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the backup vault that will store the backups generated through this backup configuration. Example: "//backupdr.googleapis.com/v1/projects/{project}/locations/{region}/backupVaults/{backupvaultId}"

`string backup_vault = 8 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The backupVault to set.  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` | This builder for chaining.  
  
### setBackupVaultBytes(ByteString value)
    
    
    public BackupConfigDetails.Builder setBackupVaultBytes(ByteString value)

Output only. The [full resource name](https://cloud.google.com/asset-inventory/docs/resource-name-format) of the backup vault that will store the backups generated through this backup configuration. Example: "//backupdr.googleapis.com/v1/projects/{project}/locations/{region}/backupVaults/{backupvaultId}"

`string backup_vault = 8 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for backupVault to set.  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` | This builder for chaining.  
  
### setLatestSuccessfulBackupTime(Timestamp value)
    
    
    public BackupConfigDetails.Builder setLatestSuccessfulBackupTime(Timestamp value)

Output only. Timestamp of the latest successful backup created via this backup configuration.

` .google.protobuf.Timestamp latest_successful_backup_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### setLatestSuccessfulBackupTime(Timestamp.Builder builderForValue)
    
    
    public BackupConfigDetails.Builder setLatestSuccessfulBackupTime(Timestamp.Builder builderForValue)

Output only. Timestamp of the latest successful backup created via this backup configuration.

` .google.protobuf.Timestamp latest_successful_backup_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### setPitrSettings(PitrSettings value)
    
    
    public BackupConfigDetails.Builder setPitrSettings(PitrSettings value)

Output only. Point in time recovery settings of the backup configuration resource.

` .google.cloud.backupdr.v1.PitrSettings pitr_settings = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PitrSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.PitrSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### setPitrSettings(PitrSettings.Builder builderForValue)
    
    
    public BackupConfigDetails.Builder setPitrSettings(PitrSettings.Builder builderForValue)

Output only. Point in time recovery settings of the backup configuration resource.

` .google.cloud.backupdr.v1.PitrSettings pitr_settings = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[PitrSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.PitrSettings.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` |   
  
### setState(BackupConfigDetails.State value)
    
    
    public BackupConfigDetails.Builder setState(BackupConfigDetails.State value)

Output only. The state of the backup config resource.

` .google.cloud.backupdr.v1.BackupConfigDetails.State state = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BackupConfigDetails.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.State)`  
The state to set.  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` | This builder for chaining.  
  
### setStateValue(int value)
    
    
    public BackupConfigDetails.Builder setStateValue(int value)

Output only. The state of the backup config resource.

` .google.cloud.backupdr.v1.BackupConfigDetails.State state = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for state to set.  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` | This builder for chaining.  
  
### setType(BackupConfigDetails.Type value)
    
    
    public BackupConfigDetails.Builder setType(BackupConfigDetails.Type value)

Output only. The type of the backup config resource.

` .google.cloud.backupdr.v1.BackupConfigDetails.Type type = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BackupConfigDetails.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Type)`  
The type to set.  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` | This builder for chaining.  
  
### setTypeValue(int value)
    
    
    public BackupConfigDetails.Builder setTypeValue(int value)

Output only. The type of the backup config resource.

` .google.cloud.backupdr.v1.BackupConfigDetails.Type type = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for type to set.  
**Returns**  
---  
**Type** | **Description**  
`[BackupConfigDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.BackupConfigDetails.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
