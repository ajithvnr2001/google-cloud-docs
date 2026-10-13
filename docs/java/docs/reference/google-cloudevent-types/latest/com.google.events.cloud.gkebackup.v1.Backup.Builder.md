---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder
title: Class Backup.Builder (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:09.835130+00:00
---

# Class Backup.Builder (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Backup.Builder (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.gkebackup.v1.Backup.Builder)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.gkebackup.v1.Backup.Builder)


    
    
    public static final class Backup.Builder extends GeneratedMessageV3.Builder<Backup.Builder> implements BackupOrBuilder

Represents a request to perform a single point-in-time capture of some portion of the state of a GKE cluster, the record of the backup operation itself, and an anchor for the underlying artifacts that comprise the Backup (the config backup and VolumeBackups). Next id: 28

Protobuf type `google.events.cloud.gkebackup.v1.Backup`

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessageV3.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html) > Backup.Builder

## Implements

[BackupOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.BackupOrBuilder)

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

[GeneratedMessageV3.Builder.addRepeatedField(Descriptors.FieldDescriptor,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_addRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_java_lang_Object_)

[GeneratedMessageV3.Builder.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_clear__)

[GeneratedMessageV3.Builder.clearField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_clearField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessageV3.Builder.clearOneof(Descriptors.OneofDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_clearOneof_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessageV3.Builder.clone()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_clone__)

[GeneratedMessageV3.Builder.getAllFields()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_getAllFields__)

[GeneratedMessageV3.Builder.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_getDescriptorForType__)

[GeneratedMessageV3.Builder.getField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_getField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessageV3.Builder.getFieldBuilder(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_getFieldBuilder_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessageV3.Builder.getOneofFieldDescriptor(Descriptors.OneofDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_getOneofFieldDescriptor_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessageV3.Builder.getParentForChildren()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_getParentForChildren__)

[GeneratedMessageV3.Builder.getRepeatedField(Descriptors.FieldDescriptor,int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_getRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_int_)

[GeneratedMessageV3.Builder.getRepeatedFieldBuilder(Descriptors.FieldDescriptor,int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_getRepeatedFieldBuilder_com_google_protobuf_Descriptors_FieldDescriptor_int_)

[GeneratedMessageV3.Builder.getRepeatedFieldCount(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_getRepeatedFieldCount_com_google_protobuf_Descriptors_FieldDescriptor_)

com.google.protobuf.GeneratedMessageV3.Builder.getUnknownFieldSetBuilder()

[GeneratedMessageV3.Builder.getUnknownFields()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_getUnknownFields__)

[GeneratedMessageV3.Builder.hasField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_hasField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessageV3.Builder.hasOneof(Descriptors.OneofDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_hasOneof_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessageV3.Builder.internalGetFieldAccessorTable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_internalGetFieldAccessorTable__)

[GeneratedMessageV3.Builder.internalGetMapField(int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_internalGetMapField_int_)

com.google.protobuf.GeneratedMessageV3.Builder.internalGetMapFieldReflection(int)

[GeneratedMessageV3.Builder.internalGetMutableMapField(int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_internalGetMutableMapField_int_)

com.google.protobuf.GeneratedMessageV3.Builder.internalGetMutableMapFieldReflection(int)

[GeneratedMessageV3.Builder.isClean()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_isClean__)

[GeneratedMessageV3.Builder.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_isInitialized__)

[GeneratedMessageV3.Builder.markClean()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_markClean__)

[GeneratedMessageV3.Builder.mergeUnknownFields(UnknownFieldSet)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_mergeUnknownFields_com_google_protobuf_UnknownFieldSet_)

com.google.protobuf.GeneratedMessageV3.Builder.mergeUnknownLengthDelimitedField(int,com.google.protobuf.ByteString)

com.google.protobuf.GeneratedMessageV3.Builder.mergeUnknownVarintField(int,int)

[GeneratedMessageV3.Builder.newBuilderForField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_newBuilderForField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessageV3.Builder.onBuilt()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_onBuilt__)

[GeneratedMessageV3.Builder.onChanged()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_onChanged__)

com.google.protobuf.GeneratedMessageV3.Builder.parseUnknownField(com.google.protobuf.CodedInputStream,com.google.protobuf.ExtensionRegistryLite,int)

[GeneratedMessageV3.Builder.setField(Descriptors.FieldDescriptor,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_setField_com_google_protobuf_Descriptors_FieldDescriptor_java_lang_Object_)

[GeneratedMessageV3.Builder.setRepeatedField(Descriptors.FieldDescriptor,int,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_setRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_int_java_lang_Object_)

com.google.protobuf.GeneratedMessageV3.Builder.setUnknownFieldSetBuilder(com.google.protobuf.UnknownFieldSet.Builder)

[GeneratedMessageV3.Builder.setUnknownFields(UnknownFieldSet)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_setUnknownFields_com_google_protobuf_UnknownFieldSet_)

[GeneratedMessageV3.Builder.setUnknownFieldsProto3(UnknownFieldSet)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_setUnknownFieldsProto3_com_google_protobuf_UnknownFieldSet_)

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

### addRepeatedField(Descriptors.FieldDescriptor field, Object value)
    
    
    public Backup.Builder addRepeatedField(Descriptors.FieldDescriptor field, Object value)

**Parameters**  
---  
**Name** | **Description**  
`field` | `[FieldDescriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.FieldDescriptor.html)`  
  
`value` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.addRepeatedField(Descriptors.FieldDescriptor field, Object value)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_addRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_java_lang_Object_)

### build()
    
    
    public Backup build()

**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup)` |   
  
### buildPartial()
    
    
    public Backup buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup)` |   
  
### clear()
    
    
    public Backup.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_clear__)

### clearAllNamespaces()
    
    
    public Backup.Builder clearAllNamespaces()

Output only. If True, all namespaces were included in the Backup.

`bool all_namespaces = 12;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### clearBackupScope()
    
    
    public Backup.Builder clearBackupScope()

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### clearClusterMetadata()
    
    
    public Backup.Builder clearClusterMetadata()

Output only. Information about the GKE cluster from which this Backup was created.

`.google.events.cloud.gkebackup.v1.Backup.ClusterMetadata cluster_metadata = 17;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### clearCompleteTime()
    
    
    public Backup.Builder clearCompleteTime()

Output only. Completion time of the Backup

`.google.protobuf.Timestamp complete_time = 20;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### clearConfigBackupSizeBytes()
    
    
    public Backup.Builder clearConfigBackupSizeBytes()

Output only. The size of the config backup in bytes.

`int64 config_backup_size_bytes = 27;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### clearContainsSecrets()
    
    
    public Backup.Builder clearContainsSecrets()

Output only. Whether or not the Backup contains Kubernetes Secrets. Controlled by the parent BackupPlan's include_secrets value.

`bool contains_secrets = 16;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### clearContainsVolumeData()
    
    
    public Backup.Builder clearContainsVolumeData()

Output only. Whether or not the Backup contains volume data. Controlled by the parent BackupPlan's include_volume_data value.

`bool contains_volume_data = 15;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### clearCreateTime()
    
    
    public Backup.Builder clearCreateTime()

Output only. The timestamp when this Backup resource was created.

`.google.protobuf.Timestamp create_time = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### clearDeleteLockDays()
    
    
    public Backup.Builder clearDeleteLockDays()

Minimum age for this Backup (in days). If this field is set to a non-zero value, the Backup will be "locked" against deletion (either manual or automatic deletion) for the number of days provided (measured from the creation time of the Backup). MUST be an integer value between 0-90 (inclusive). Defaults to parent BackupPlan's backup_delete_lock_days setting and may only be increased (either at creation time or in a subsequent update).

`int32 delete_lock_days = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### clearDeleteLockExpireTime()
    
    
    public Backup.Builder clearDeleteLockExpireTime()

Output only. The time at which an existing delete lock will expire for this backup (calculated from create_time + delete_lock_days).

`.google.protobuf.Timestamp delete_lock_expire_time = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### clearDescription()
    
    
    public Backup.Builder clearDescription()

User specified descriptive string for this Backup.

`string description = 25;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### clearEncryptionKey()
    
    
    public Backup.Builder clearEncryptionKey()

Output only. The customer managed encryption key that was used to encrypt the Backup's artifacts. Inherited from the parent BackupPlan's encryption_key value.

`.google.events.cloud.gkebackup.v1.EncryptionKey encryption_key = 11;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### clearEtag()
    
    
    public Backup.Builder clearEtag()

Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a backup from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform backup updates in order to avoid race conditions: An `etag` is returned in the response to `GetBackup`, and systems are expected to put that etag in the request to `UpdateBackup` or `DeleteBackup` to ensure that their change will be applied to the same version of the resource.

`string etag = 24;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### clearField(Descriptors.FieldDescriptor field)
    
    
    public Backup.Builder clearField(Descriptors.FieldDescriptor field)

**Parameter**  
---  
**Name** | **Description**  
`field` | `[FieldDescriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.FieldDescriptor.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.clearField(Descriptors.FieldDescriptor field)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_clearField_com_google_protobuf_Descriptors_FieldDescriptor_)

### clearLabels()
    
    
    public Backup.Builder clearLabels()

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### clearManual()
    
    
    public Backup.Builder clearManual()

Output only. This flag indicates whether this Backup resource was created manually by a user or via a schedule in the BackupPlan. A value of True means that the Backup was created manually.

`bool manual = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### clearName()
    
    
    public Backup.Builder clearName()

Output only. The fully qualified name of the Backup. `projects/*/locations/*/backupPlans/*/backups/*`

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### clearOneof(Descriptors.OneofDescriptor oneof)
    
    
    public Backup.Builder clearOneof(Descriptors.OneofDescriptor oneof)

**Parameter**  
---  
**Name** | **Description**  
`oneof` | `[OneofDescriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.OneofDescriptor.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.clearOneof(Descriptors.OneofDescriptor oneof)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_clearOneof_com_google_protobuf_Descriptors_OneofDescriptor_)

### clearPodCount()
    
    
    public Backup.Builder clearPodCount()

Output only. The total number of Kubernetes Pods contained in the Backup.

`int32 pod_count = 26;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### clearResourceCount()
    
    
    public Backup.Builder clearResourceCount()

Output only. The total number of Kubernetes resources included in the Backup.

`int32 resource_count = 21;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### clearRetainDays()
    
    
    public Backup.Builder clearRetainDays()

The age (in days) after which this Backup will be automatically deleted. Must be an integer value >= 0:

  * If 0, no automatic deletion will occur for this Backup.
  * If not 0, this must be >= delete_lock_days and <= 365. Once a Backup is created, this value may only be increased. Defaults to the parent BackupPlan's backup_retain_days value.



`int32 retain_days = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### clearRetainExpireTime()
    
    
    public Backup.Builder clearRetainExpireTime()

Output only. The time at which this Backup will be automatically deleted (calculated from create_time + retain_days).

`.google.protobuf.Timestamp retain_expire_time = 10;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### clearSelectedApplications()
    
    
    public Backup.Builder clearSelectedApplications()

Output only. If set, the list of ProtectedApplications whose resources were included in the Backup.

`.google.events.cloud.gkebackup.v1.NamespacedNames selected_applications = 14;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### clearSelectedNamespaces()
    
    
    public Backup.Builder clearSelectedNamespaces()

Output only. If set, the list of namespaces that were included in the Backup.

`.google.events.cloud.gkebackup.v1.Namespaces selected_namespaces = 13;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### clearSizeBytes()
    
    
    public Backup.Builder clearSizeBytes()

Output only. The total size of the Backup in bytes = config backup size + sum(volume backup sizes)

`int64 size_bytes = 23;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### clearState()
    
    
    public Backup.Builder clearState()

Output only. Current state of the Backup

`.google.events.cloud.gkebackup.v1.Backup.State state = 18;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### clearStateReason()
    
    
    public Backup.Builder clearStateReason()

Output only. Human-readable description of why the backup is in the current `state`.

`string state_reason = 19;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### clearUid()
    
    
    public Backup.Builder clearUid()

Output only. Server generated global unique identifier of [UUID4](https://en.wikipedia.org/wiki/Universally_unique_identifier)

`string uid = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### clearUpdateTime()
    
    
    public Backup.Builder clearUpdateTime()

Output only. The timestamp when this Backup resource was last updated.

`.google.protobuf.Timestamp update_time = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### clearVolumeCount()
    
    
    public Backup.Builder clearVolumeCount()

Output only. The total number of volume backups contained in the Backup.

`int32 volume_count = 22;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### clone()
    
    
    public Backup.Builder clone()

**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.clone()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_clone__)

### containsLabels(String key)
    
    
    public boolean containsLabels(String key)

A set of custom labels supplied by user.

`map<string, string> labels = 6;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAllNamespaces()
    
    
    public boolean getAllNamespaces()

Output only. If True, all namespaces were included in the Backup.

`bool all_namespaces = 12;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The allNamespaces.  
  
### getBackupScopeCase()
    
    
    public Backup.BackupScopeCase getBackupScopeCase()

**Returns**  
---  
**Type** | **Description**  
`[Backup.BackupScopeCase](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.BackupScopeCase)` |   
  
### getClusterMetadata()
    
    
    public Backup.ClusterMetadata getClusterMetadata()

Output only. Information about the GKE cluster from which this Backup was created.

`.google.events.cloud.gkebackup.v1.Backup.ClusterMetadata cluster_metadata = 17;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.ClusterMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.ClusterMetadata)` | The clusterMetadata.  
  
### getClusterMetadataBuilder()
    
    
    public Backup.ClusterMetadata.Builder getClusterMetadataBuilder()

Output only. Information about the GKE cluster from which this Backup was created.

`.google.events.cloud.gkebackup.v1.Backup.ClusterMetadata cluster_metadata = 17;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.ClusterMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.ClusterMetadata.Builder)` |   
  
### getClusterMetadataOrBuilder()
    
    
    public Backup.ClusterMetadataOrBuilder getClusterMetadataOrBuilder()

Output only. Information about the GKE cluster from which this Backup was created.

`.google.events.cloud.gkebackup.v1.Backup.ClusterMetadata cluster_metadata = 17;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.ClusterMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.ClusterMetadataOrBuilder)` |   
  
### getCompleteTime()
    
    
    public Timestamp getCompleteTime()

Output only. Completion time of the Backup

`.google.protobuf.Timestamp complete_time = 20;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The completeTime.  
  
### getCompleteTimeBuilder()
    
    
    public Timestamp.Builder getCompleteTimeBuilder()

Output only. Completion time of the Backup

`.google.protobuf.Timestamp complete_time = 20;`

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getCompleteTimeOrBuilder()
    
    
    public TimestampOrBuilder getCompleteTimeOrBuilder()

Output only. Completion time of the Backup

`.google.protobuf.Timestamp complete_time = 20;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getConfigBackupSizeBytes()
    
    
    public long getConfigBackupSizeBytes()

Output only. The size of the config backup in bytes.

`int64 config_backup_size_bytes = 27;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The configBackupSizeBytes.  
  
### getContainsSecrets()
    
    
    public boolean getContainsSecrets()

Output only. Whether or not the Backup contains Kubernetes Secrets. Controlled by the parent BackupPlan's include_secrets value.

`bool contains_secrets = 16;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The containsSecrets.  
  
### getContainsVolumeData()
    
    
    public boolean getContainsVolumeData()

Output only. Whether or not the Backup contains volume data. Controlled by the parent BackupPlan's include_volume_data value.

`bool contains_volume_data = 15;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The containsVolumeData.  
  
### getCreateTime()
    
    
    public Timestamp getCreateTime()

Output only. The timestamp when this Backup resource was created.

`.google.protobuf.Timestamp create_time = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeBuilder()
    
    
    public Timestamp.Builder getCreateTimeBuilder()

Output only. The timestamp when this Backup resource was created.

`.google.protobuf.Timestamp create_time = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getCreateTimeOrBuilder()
    
    
    public TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The timestamp when this Backup resource was created.

`.google.protobuf.Timestamp create_time = 3;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDefaultInstanceForType()
    
    
    public Backup getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup)` |   
  
### getDeleteLockDays()
    
    
    public int getDeleteLockDays()

Minimum age for this Backup (in days). If this field is set to a non-zero value, the Backup will be "locked" against deletion (either manual or automatic deletion) for the number of days provided (measured from the creation time of the Backup). MUST be an integer value between 0-90 (inclusive). Defaults to parent BackupPlan's backup_delete_lock_days setting and may only be increased (either at creation time or in a subsequent update).

`int32 delete_lock_days = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The deleteLockDays.  
  
### getDeleteLockExpireTime()
    
    
    public Timestamp getDeleteLockExpireTime()

Output only. The time at which an existing delete lock will expire for this backup (calculated from create_time + delete_lock_days).

`.google.protobuf.Timestamp delete_lock_expire_time = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The deleteLockExpireTime.  
  
### getDeleteLockExpireTimeBuilder()
    
    
    public Timestamp.Builder getDeleteLockExpireTimeBuilder()

Output only. The time at which an existing delete lock will expire for this backup (calculated from create_time + delete_lock_days).

`.google.protobuf.Timestamp delete_lock_expire_time = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getDeleteLockExpireTimeOrBuilder()
    
    
    public TimestampOrBuilder getDeleteLockExpireTimeOrBuilder()

Output only. The time at which an existing delete lock will expire for this backup (calculated from create_time + delete_lock_days).

`.google.protobuf.Timestamp delete_lock_expire_time = 8;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDescription()
    
    
    public String getDescription()

User specified descriptive string for this Backup.

`string description = 25;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public ByteString getDescriptionBytes()

User specified descriptive string for this Backup.

`string description = 25;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_getDescriptorForType__)

### getEncryptionKey()
    
    
    public EncryptionKey getEncryptionKey()

Output only. The customer managed encryption key that was used to encrypt the Backup's artifacts. Inherited from the parent BackupPlan's encryption_key value.

`.google.events.cloud.gkebackup.v1.EncryptionKey encryption_key = 11;`

**Returns**  
---  
**Type** | **Description**  
`[EncryptionKey](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.EncryptionKey)` | The encryptionKey.  
  
### getEncryptionKeyBuilder()
    
    
    public EncryptionKey.Builder getEncryptionKeyBuilder()

Output only. The customer managed encryption key that was used to encrypt the Backup's artifacts. Inherited from the parent BackupPlan's encryption_key value.

`.google.events.cloud.gkebackup.v1.EncryptionKey encryption_key = 11;`

**Returns**  
---  
**Type** | **Description**  
`[EncryptionKey.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.EncryptionKey.Builder)` |   
  
### getEncryptionKeyOrBuilder()
    
    
    public EncryptionKeyOrBuilder getEncryptionKeyOrBuilder()

Output only. The customer managed encryption key that was used to encrypt the Backup's artifacts. Inherited from the parent BackupPlan's encryption_key value.

`.google.events.cloud.gkebackup.v1.EncryptionKey encryption_key = 11;`

**Returns**  
---  
**Type** | **Description**  
`[EncryptionKeyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.EncryptionKeyOrBuilder)` |   
  
### getEtag()
    
    
    public String getEtag()

Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a backup from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform backup updates in order to avoid race conditions: An `etag` is returned in the response to `GetBackup`, and systems are expected to put that etag in the request to `UpdateBackup` or `DeleteBackup` to ensure that their change will be applied to the same version of the resource.

`string etag = 24;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The etag.  
  
### getEtagBytes()
    
    
    public ByteString getEtagBytes()

Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a backup from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform backup updates in order to avoid race conditions: An `etag` is returned in the response to `GetBackup`, and systems are expected to put that etag in the request to `UpdateBackup` or `DeleteBackup` to ensure that their change will be applied to the same version of the resource.

`string etag = 24;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for etag.  
  
### getLabels()
    
    
    public Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder#com_google_events_cloud_gkebackup_v1_Backup_Builder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public int getLabelsCount()

A set of custom labels supplied by user.

`map<string, string> labels = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public Map<String,String> getLabelsMap()

A set of custom labels supplied by user.

`map<string, string> labels = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public String getLabelsOrDefault(String key, String defaultValue)

A set of custom labels supplied by user.

`map<string, string> labels = 6;`

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
    
    
    public String getLabelsOrThrow(String key)

A set of custom labels supplied by user.

`map<string, string> labels = 6;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getManual()
    
    
    public boolean getManual()

Output only. This flag indicates whether this Backup resource was created manually by a user or via a schedule in the BackupPlan. A value of True means that the Backup was created manually.

`bool manual = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The manual.  
  
### getMutableLabels()
    
    
    public Map<String,String> getMutableLabels()

Use alternate mutation accessors instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getName()
    
    
    public String getName()

Output only. The fully qualified name of the Backup. `projects/*/locations/*/backupPlans/*/backups/*`

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

Output only. The fully qualified name of the Backup. `projects/*/locations/*/backupPlans/*/backups/*`

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPodCount()
    
    
    public int getPodCount()

Output only. The total number of Kubernetes Pods contained in the Backup.

`int32 pod_count = 26;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The podCount.  
  
### getResourceCount()
    
    
    public int getResourceCount()

Output only. The total number of Kubernetes resources included in the Backup.

`int32 resource_count = 21;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The resourceCount.  
  
### getRetainDays()
    
    
    public int getRetainDays()

The age (in days) after which this Backup will be automatically deleted. Must be an integer value >= 0:

  * If 0, no automatic deletion will occur for this Backup.
  * If not 0, this must be >= delete_lock_days and <= 365. Once a Backup is created, this value may only be increased. Defaults to the parent BackupPlan's backup_retain_days value.



`int32 retain_days = 9;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The retainDays.  
  
### getRetainExpireTime()
    
    
    public Timestamp getRetainExpireTime()

Output only. The time at which this Backup will be automatically deleted (calculated from create_time + retain_days).

`.google.protobuf.Timestamp retain_expire_time = 10;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The retainExpireTime.  
  
### getRetainExpireTimeBuilder()
    
    
    public Timestamp.Builder getRetainExpireTimeBuilder()

Output only. The time at which this Backup will be automatically deleted (calculated from create_time + retain_days).

`.google.protobuf.Timestamp retain_expire_time = 10;`

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getRetainExpireTimeOrBuilder()
    
    
    public TimestampOrBuilder getRetainExpireTimeOrBuilder()

Output only. The time at which this Backup will be automatically deleted (calculated from create_time + retain_days).

`.google.protobuf.Timestamp retain_expire_time = 10;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getSelectedApplications()
    
    
    public NamespacedNames getSelectedApplications()

Output only. If set, the list of ProtectedApplications whose resources were included in the Backup.

`.google.events.cloud.gkebackup.v1.NamespacedNames selected_applications = 14;`

**Returns**  
---  
**Type** | **Description**  
`[NamespacedNames](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.NamespacedNames)` | The selectedApplications.  
  
### getSelectedApplicationsBuilder()
    
    
    public NamespacedNames.Builder getSelectedApplicationsBuilder()

Output only. If set, the list of ProtectedApplications whose resources were included in the Backup.

`.google.events.cloud.gkebackup.v1.NamespacedNames selected_applications = 14;`

**Returns**  
---  
**Type** | **Description**  
`[NamespacedNames.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.NamespacedNames.Builder)` |   
  
### getSelectedApplicationsOrBuilder()
    
    
    public NamespacedNamesOrBuilder getSelectedApplicationsOrBuilder()

Output only. If set, the list of ProtectedApplications whose resources were included in the Backup.

`.google.events.cloud.gkebackup.v1.NamespacedNames selected_applications = 14;`

**Returns**  
---  
**Type** | **Description**  
`[NamespacedNamesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.NamespacedNamesOrBuilder)` |   
  
### getSelectedNamespaces()
    
    
    public Namespaces getSelectedNamespaces()

Output only. If set, the list of namespaces that were included in the Backup.

`.google.events.cloud.gkebackup.v1.Namespaces selected_namespaces = 13;`

**Returns**  
---  
**Type** | **Description**  
`[Namespaces](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Namespaces)` | The selectedNamespaces.  
  
### getSelectedNamespacesBuilder()
    
    
    public Namespaces.Builder getSelectedNamespacesBuilder()

Output only. If set, the list of namespaces that were included in the Backup.

`.google.events.cloud.gkebackup.v1.Namespaces selected_namespaces = 13;`

**Returns**  
---  
**Type** | **Description**  
`[Namespaces.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Namespaces.Builder)` |   
  
### getSelectedNamespacesOrBuilder()
    
    
    public NamespacesOrBuilder getSelectedNamespacesOrBuilder()

Output only. If set, the list of namespaces that were included in the Backup.

`.google.events.cloud.gkebackup.v1.Namespaces selected_namespaces = 13;`

**Returns**  
---  
**Type** | **Description**  
`[NamespacesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.NamespacesOrBuilder)` |   
  
### getSizeBytes()
    
    
    public long getSizeBytes()

Output only. The total size of the Backup in bytes = config backup size + sum(volume backup sizes)

`int64 size_bytes = 23;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The sizeBytes.  
  
### getState()
    
    
    public Backup.State getState()

Output only. Current state of the Backup

`.google.events.cloud.gkebackup.v1.Backup.State state = 18;`

**Returns**  
---  
**Type** | **Description**  
`[Backup.State](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.State)` | The state.  
  
### getStateReason()
    
    
    public String getStateReason()

Output only. Human-readable description of why the backup is in the current `state`.

`string state_reason = 19;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The stateReason.  
  
### getStateReasonBytes()
    
    
    public ByteString getStateReasonBytes()

Output only. Human-readable description of why the backup is in the current `state`.

`string state_reason = 19;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for stateReason.  
  
### getStateValue()
    
    
    public int getStateValue()

Output only. Current state of the Backup

`.google.events.cloud.gkebackup.v1.Backup.State state = 18;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getUid()
    
    
    public String getUid()

Output only. Server generated global unique identifier of [UUID4](https://en.wikipedia.org/wiki/Universally_unique_identifier)

`string uid = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The uid.  
  
### getUidBytes()
    
    
    public ByteString getUidBytes()

Output only. Server generated global unique identifier of [UUID4](https://en.wikipedia.org/wiki/Universally_unique_identifier)

`string uid = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for uid.  
  
### getUpdateTime()
    
    
    public Timestamp getUpdateTime()

Output only. The timestamp when this Backup resource was last updated.

`.google.protobuf.Timestamp update_time = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeBuilder()
    
    
    public Timestamp.Builder getUpdateTimeBuilder()

Output only. The timestamp when this Backup resource was last updated.

`.google.protobuf.Timestamp update_time = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getUpdateTimeOrBuilder()
    
    
    public TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The timestamp when this Backup resource was last updated.

`.google.protobuf.Timestamp update_time = 4;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getVolumeCount()
    
    
    public int getVolumeCount()

Output only. The total number of volume backups contained in the Backup.

`int32 volume_count = 22;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The volumeCount.  
  
### hasAllNamespaces()
    
    
    public boolean hasAllNamespaces()

Output only. If True, all namespaces were included in the Backup.

`bool all_namespaces = 12;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allNamespaces field is set.  
  
### hasClusterMetadata()
    
    
    public boolean hasClusterMetadata()

Output only. Information about the GKE cluster from which this Backup was created.

`.google.events.cloud.gkebackup.v1.Backup.ClusterMetadata cluster_metadata = 17;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the clusterMetadata field is set.  
  
### hasCompleteTime()
    
    
    public boolean hasCompleteTime()

Output only. Completion time of the Backup

`.google.protobuf.Timestamp complete_time = 20;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the completeTime field is set.  
  
### hasCreateTime()
    
    
    public boolean hasCreateTime()

Output only. The timestamp when this Backup resource was created.

`.google.protobuf.Timestamp create_time = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasDeleteLockExpireTime()
    
    
    public boolean hasDeleteLockExpireTime()

Output only. The time at which an existing delete lock will expire for this backup (calculated from create_time + delete_lock_days).

`.google.protobuf.Timestamp delete_lock_expire_time = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the deleteLockExpireTime field is set.  
  
### hasEncryptionKey()
    
    
    public boolean hasEncryptionKey()

Output only. The customer managed encryption key that was used to encrypt the Backup's artifacts. Inherited from the parent BackupPlan's encryption_key value.

`.google.events.cloud.gkebackup.v1.EncryptionKey encryption_key = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the encryptionKey field is set.  
  
### hasRetainExpireTime()
    
    
    public boolean hasRetainExpireTime()

Output only. The time at which this Backup will be automatically deleted (calculated from create_time + retain_days).

`.google.protobuf.Timestamp retain_expire_time = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the retainExpireTime field is set.  
  
### hasSelectedApplications()
    
    
    public boolean hasSelectedApplications()

Output only. If set, the list of ProtectedApplications whose resources were included in the Backup.

`.google.events.cloud.gkebackup.v1.NamespacedNames selected_applications = 14;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the selectedApplications field is set.  
  
### hasSelectedNamespaces()
    
    
    public boolean hasSelectedNamespaces()

Output only. If set, the list of namespaces that were included in the Backup.

`.google.events.cloud.gkebackup.v1.Namespaces selected_namespaces = 13;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the selectedNamespaces field is set.  
  
### hasUpdateTime()
    
    
    public boolean hasUpdateTime()

Output only. The timestamp when this Backup resource was last updated.

`.google.protobuf.Timestamp update_time = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
### internalGetFieldAccessorTable()
    
    
    protected GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()

**Returns**  
---  
**Type** | **Description**  
`[FieldAccessorTable](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.FieldAccessorTable.html)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.internalGetFieldAccessorTable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_internalGetFieldAccessorTable__)

### internalGetMapField(int number)
    
    
    protected MapField internalGetMapField(int number)

**Parameter**  
---  
**Name** | **Description**  
`number` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MapField.html)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.internalGetMapField(int fieldNumber)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_internalGetMapField_int_)

### internalGetMutableMapField(int number)
    
    
    protected MapField internalGetMutableMapField(int number)

**Parameter**  
---  
**Name** | **Description**  
`number` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MapField.html)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.internalGetMutableMapField(int fieldNumber)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_internalGetMutableMapField_int_)

### isInitialized()
    
    
    public final boolean isInitialized()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_isInitialized__)

### mergeClusterMetadata(Backup.ClusterMetadata value)
    
    
    public Backup.Builder mergeClusterMetadata(Backup.ClusterMetadata value)

Output only. Information about the GKE cluster from which this Backup was created.

`.google.events.cloud.gkebackup.v1.Backup.ClusterMetadata cluster_metadata = 17;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Backup.ClusterMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.ClusterMetadata)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### mergeCompleteTime(Timestamp value)
    
    
    public Backup.Builder mergeCompleteTime(Timestamp value)

Output only. Completion time of the Backup

`.google.protobuf.Timestamp complete_time = 20;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### mergeCreateTime(Timestamp value)
    
    
    public Backup.Builder mergeCreateTime(Timestamp value)

Output only. The timestamp when this Backup resource was created.

`.google.protobuf.Timestamp create_time = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### mergeDeleteLockExpireTime(Timestamp value)
    
    
    public Backup.Builder mergeDeleteLockExpireTime(Timestamp value)

Output only. The time at which an existing delete lock will expire for this backup (calculated from create_time + delete_lock_days).

`.google.protobuf.Timestamp delete_lock_expire_time = 8;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### mergeEncryptionKey(EncryptionKey value)
    
    
    public Backup.Builder mergeEncryptionKey(EncryptionKey value)

Output only. The customer managed encryption key that was used to encrypt the Backup's artifacts. Inherited from the parent BackupPlan's encryption_key value.

`.google.events.cloud.gkebackup.v1.EncryptionKey encryption_key = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[EncryptionKey](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.EncryptionKey)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### mergeFrom(Backup other)
    
    
    public Backup.Builder mergeFrom(Backup other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Backup](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public Backup.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public Backup.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeRetainExpireTime(Timestamp value)
    
    
    public Backup.Builder mergeRetainExpireTime(Timestamp value)

Output only. The time at which this Backup will be automatically deleted (calculated from create_time + retain_days).

`.google.protobuf.Timestamp retain_expire_time = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### mergeSelectedApplications(NamespacedNames value)
    
    
    public Backup.Builder mergeSelectedApplications(NamespacedNames value)

Output only. If set, the list of ProtectedApplications whose resources were included in the Backup.

`.google.events.cloud.gkebackup.v1.NamespacedNames selected_applications = 14;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NamespacedNames](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.NamespacedNames)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### mergeSelectedNamespaces(Namespaces value)
    
    
    public Backup.Builder mergeSelectedNamespaces(Namespaces value)

Output only. If set, the list of namespaces that were included in the Backup.

`.google.events.cloud.gkebackup.v1.Namespaces selected_namespaces = 13;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Namespaces](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Namespaces)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### mergeUnknownFields(UnknownFieldSet unknownFields)
    
    
    public final Backup.Builder mergeUnknownFields(UnknownFieldSet unknownFields)

**Parameter**  
---  
**Name** | **Description**  
`unknownFields` | `[UnknownFieldSet](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.UnknownFieldSet.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.mergeUnknownFields(UnknownFieldSet unknownFields)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_mergeUnknownFields_com_google_protobuf_UnknownFieldSet_)

### mergeUpdateTime(Timestamp value)
    
    
    public Backup.Builder mergeUpdateTime(Timestamp value)

Output only. The timestamp when this Backup resource was last updated.

`.google.protobuf.Timestamp update_time = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### putAllLabels(Map<String,String> values)
    
    
    public Backup.Builder putAllLabels(Map<String,String> values)

A set of custom labels supplied by user.

`map<string, string> labels = 6;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### putLabels(String key, String value)
    
    
    public Backup.Builder putLabels(String key, String value)

A set of custom labels supplied by user.

`map<string, string> labels = 6;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### removeLabels(String key)
    
    
    public Backup.Builder removeLabels(String key)

A set of custom labels supplied by user.

`map<string, string> labels = 6;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### setAllNamespaces(boolean value)
    
    
    public Backup.Builder setAllNamespaces(boolean value)

Output only. If True, all namespaces were included in the Backup.

`bool all_namespaces = 12;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The allNamespaces to set.  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### setClusterMetadata(Backup.ClusterMetadata value)
    
    
    public Backup.Builder setClusterMetadata(Backup.ClusterMetadata value)

Output only. Information about the GKE cluster from which this Backup was created.

`.google.events.cloud.gkebackup.v1.Backup.ClusterMetadata cluster_metadata = 17;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Backup.ClusterMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.ClusterMetadata)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### setClusterMetadata(Backup.ClusterMetadata.Builder builderForValue)
    
    
    public Backup.Builder setClusterMetadata(Backup.ClusterMetadata.Builder builderForValue)

Output only. Information about the GKE cluster from which this Backup was created.

`.google.events.cloud.gkebackup.v1.Backup.ClusterMetadata cluster_metadata = 17;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Backup.ClusterMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.ClusterMetadata.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### setCompleteTime(Timestamp value)
    
    
    public Backup.Builder setCompleteTime(Timestamp value)

Output only. Completion time of the Backup

`.google.protobuf.Timestamp complete_time = 20;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### setCompleteTime(Timestamp.Builder builderForValue)
    
    
    public Backup.Builder setCompleteTime(Timestamp.Builder builderForValue)

Output only. Completion time of the Backup

`.google.protobuf.Timestamp complete_time = 20;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### setConfigBackupSizeBytes(long value)
    
    
    public Backup.Builder setConfigBackupSizeBytes(long value)

Output only. The size of the config backup in bytes.

`int64 config_backup_size_bytes = 27;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The configBackupSizeBytes to set.  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### setContainsSecrets(boolean value)
    
    
    public Backup.Builder setContainsSecrets(boolean value)

Output only. Whether or not the Backup contains Kubernetes Secrets. Controlled by the parent BackupPlan's include_secrets value.

`bool contains_secrets = 16;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The containsSecrets to set.  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### setContainsVolumeData(boolean value)
    
    
    public Backup.Builder setContainsVolumeData(boolean value)

Output only. Whether or not the Backup contains volume data. Controlled by the parent BackupPlan's include_volume_data value.

`bool contains_volume_data = 15;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The containsVolumeData to set.  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### setCreateTime(Timestamp value)
    
    
    public Backup.Builder setCreateTime(Timestamp value)

Output only. The timestamp when this Backup resource was created.

`.google.protobuf.Timestamp create_time = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### setCreateTime(Timestamp.Builder builderForValue)
    
    
    public Backup.Builder setCreateTime(Timestamp.Builder builderForValue)

Output only. The timestamp when this Backup resource was created.

`.google.protobuf.Timestamp create_time = 3;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### setDeleteLockDays(int value)
    
    
    public Backup.Builder setDeleteLockDays(int value)

Minimum age for this Backup (in days). If this field is set to a non-zero value, the Backup will be "locked" against deletion (either manual or automatic deletion) for the number of days provided (measured from the creation time of the Backup). MUST be an integer value between 0-90 (inclusive). Defaults to parent BackupPlan's backup_delete_lock_days setting and may only be increased (either at creation time or in a subsequent update).

`int32 delete_lock_days = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The deleteLockDays to set.  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### setDeleteLockExpireTime(Timestamp value)
    
    
    public Backup.Builder setDeleteLockExpireTime(Timestamp value)

Output only. The time at which an existing delete lock will expire for this backup (calculated from create_time + delete_lock_days).

`.google.protobuf.Timestamp delete_lock_expire_time = 8;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### setDeleteLockExpireTime(Timestamp.Builder builderForValue)
    
    
    public Backup.Builder setDeleteLockExpireTime(Timestamp.Builder builderForValue)

Output only. The time at which an existing delete lock will expire for this backup (calculated from create_time + delete_lock_days).

`.google.protobuf.Timestamp delete_lock_expire_time = 8;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### setDescription(String value)
    
    
    public Backup.Builder setDescription(String value)

User specified descriptive string for this Backup.

`string description = 25;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The description to set.  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### setDescriptionBytes(ByteString value)
    
    
    public Backup.Builder setDescriptionBytes(ByteString value)

User specified descriptive string for this Backup.

`string description = 25;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for description to set.  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### setEncryptionKey(EncryptionKey value)
    
    
    public Backup.Builder setEncryptionKey(EncryptionKey value)

Output only. The customer managed encryption key that was used to encrypt the Backup's artifacts. Inherited from the parent BackupPlan's encryption_key value.

`.google.events.cloud.gkebackup.v1.EncryptionKey encryption_key = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[EncryptionKey](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.EncryptionKey)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### setEncryptionKey(EncryptionKey.Builder builderForValue)
    
    
    public Backup.Builder setEncryptionKey(EncryptionKey.Builder builderForValue)

Output only. The customer managed encryption key that was used to encrypt the Backup's artifacts. Inherited from the parent BackupPlan's encryption_key value.

`.google.events.cloud.gkebackup.v1.EncryptionKey encryption_key = 11;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[EncryptionKey.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.EncryptionKey.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### setEtag(String value)
    
    
    public Backup.Builder setEtag(String value)

Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a backup from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform backup updates in order to avoid race conditions: An `etag` is returned in the response to `GetBackup`, and systems are expected to put that etag in the request to `UpdateBackup` or `DeleteBackup` to ensure that their change will be applied to the same version of the resource.

`string etag = 24;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The etag to set.  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### setEtagBytes(ByteString value)
    
    
    public Backup.Builder setEtagBytes(ByteString value)

Output only. `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a backup from overwriting each other. It is strongly suggested that systems make use of the `etag` in the read-modify-write cycle to perform backup updates in order to avoid race conditions: An `etag` is returned in the response to `GetBackup`, and systems are expected to put that etag in the request to `UpdateBackup` or `DeleteBackup` to ensure that their change will be applied to the same version of the resource.

`string etag = 24;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for etag to set.  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### setField(Descriptors.FieldDescriptor field, Object value)
    
    
    public Backup.Builder setField(Descriptors.FieldDescriptor field, Object value)

**Parameters**  
---  
**Name** | **Description**  
`field` | `[FieldDescriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.FieldDescriptor.html)`  
  
`value` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.setField(Descriptors.FieldDescriptor field, Object value)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_setField_com_google_protobuf_Descriptors_FieldDescriptor_java_lang_Object_)

### setManual(boolean value)
    
    
    public Backup.Builder setManual(boolean value)

Output only. This flag indicates whether this Backup resource was created manually by a user or via a schedule in the BackupPlan. A value of True means that the Backup was created manually.

`bool manual = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The manual to set.  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### setName(String value)
    
    
    public Backup.Builder setName(String value)

Output only. The fully qualified name of the Backup. `projects/*/locations/*/backupPlans/*/backups/*`

`string name = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public Backup.Builder setNameBytes(ByteString value)

Output only. The fully qualified name of the Backup. `projects/*/locations/*/backupPlans/*/backups/*`

`string name = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### setPodCount(int value)
    
    
    public Backup.Builder setPodCount(int value)

Output only. The total number of Kubernetes Pods contained in the Backup.

`int32 pod_count = 26;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The podCount to set.  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### setRepeatedField(Descriptors.FieldDescriptor field, int index, Object value)
    
    
    public Backup.Builder setRepeatedField(Descriptors.FieldDescriptor field, int index, Object value)

**Parameters**  
---  
**Name** | **Description**  
`field` | `[FieldDescriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.FieldDescriptor.html)`  
  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.setRepeatedField(Descriptors.FieldDescriptor field, int index, Object value)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_setRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_int_java_lang_Object_)

### setResourceCount(int value)
    
    
    public Backup.Builder setResourceCount(int value)

Output only. The total number of Kubernetes resources included in the Backup.

`int32 resource_count = 21;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The resourceCount to set.  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### setRetainDays(int value)
    
    
    public Backup.Builder setRetainDays(int value)

The age (in days) after which this Backup will be automatically deleted. Must be an integer value >= 0:

  * If 0, no automatic deletion will occur for this Backup.
  * If not 0, this must be >= delete_lock_days and <= 365. Once a Backup is created, this value may only be increased. Defaults to the parent BackupPlan's backup_retain_days value.



`int32 retain_days = 9;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The retainDays to set.  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### setRetainExpireTime(Timestamp value)
    
    
    public Backup.Builder setRetainExpireTime(Timestamp value)

Output only. The time at which this Backup will be automatically deleted (calculated from create_time + retain_days).

`.google.protobuf.Timestamp retain_expire_time = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### setRetainExpireTime(Timestamp.Builder builderForValue)
    
    
    public Backup.Builder setRetainExpireTime(Timestamp.Builder builderForValue)

Output only. The time at which this Backup will be automatically deleted (calculated from create_time + retain_days).

`.google.protobuf.Timestamp retain_expire_time = 10;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### setSelectedApplications(NamespacedNames value)
    
    
    public Backup.Builder setSelectedApplications(NamespacedNames value)

Output only. If set, the list of ProtectedApplications whose resources were included in the Backup.

`.google.events.cloud.gkebackup.v1.NamespacedNames selected_applications = 14;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NamespacedNames](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.NamespacedNames)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### setSelectedApplications(NamespacedNames.Builder builderForValue)
    
    
    public Backup.Builder setSelectedApplications(NamespacedNames.Builder builderForValue)

Output only. If set, the list of ProtectedApplications whose resources were included in the Backup.

`.google.events.cloud.gkebackup.v1.NamespacedNames selected_applications = 14;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[NamespacedNames.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.NamespacedNames.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### setSelectedNamespaces(Namespaces value)
    
    
    public Backup.Builder setSelectedNamespaces(Namespaces value)

Output only. If set, the list of namespaces that were included in the Backup.

`.google.events.cloud.gkebackup.v1.Namespaces selected_namespaces = 13;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Namespaces](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Namespaces)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### setSelectedNamespaces(Namespaces.Builder builderForValue)
    
    
    public Backup.Builder setSelectedNamespaces(Namespaces.Builder builderForValue)

Output only. If set, the list of namespaces that were included in the Backup.

`.google.events.cloud.gkebackup.v1.Namespaces selected_namespaces = 13;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Namespaces.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Namespaces.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### setSizeBytes(long value)
    
    
    public Backup.Builder setSizeBytes(long value)

Output only. The total size of the Backup in bytes = config backup size + sum(volume backup sizes)

`int64 size_bytes = 23;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The sizeBytes to set.  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### setState(Backup.State value)
    
    
    public Backup.Builder setState(Backup.State value)

Output only. Current state of the Backup

`.google.events.cloud.gkebackup.v1.Backup.State state = 18;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Backup.State](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.State)`  
The state to set.  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### setStateReason(String value)
    
    
    public Backup.Builder setStateReason(String value)

Output only. Human-readable description of why the backup is in the current `state`.

`string state_reason = 19;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The stateReason to set.  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### setStateReasonBytes(ByteString value)
    
    
    public Backup.Builder setStateReasonBytes(ByteString value)

Output only. Human-readable description of why the backup is in the current `state`.

`string state_reason = 19;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for stateReason to set.  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### setStateValue(int value)
    
    
    public Backup.Builder setStateValue(int value)

Output only. Current state of the Backup

`.google.events.cloud.gkebackup.v1.Backup.State state = 18;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for state to set.  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### setUid(String value)
    
    
    public Backup.Builder setUid(String value)

Output only. Server generated global unique identifier of [UUID4](https://en.wikipedia.org/wiki/Universally_unique_identifier)

`string uid = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The uid to set.  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### setUidBytes(ByteString value)
    
    
    public Backup.Builder setUidBytes(ByteString value)

Output only. Server generated global unique identifier of [UUID4](https://en.wikipedia.org/wiki/Universally_unique_identifier)

`string uid = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for uid to set.  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
### setUnknownFields(UnknownFieldSet unknownFields)
    
    
    public final Backup.Builder setUnknownFields(UnknownFieldSet unknownFields)

**Parameter**  
---  
**Name** | **Description**  
`unknownFields` | `[UnknownFieldSet](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.UnknownFieldSet.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.setUnknownFields(UnknownFieldSet unknownFields)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_setUnknownFields_com_google_protobuf_UnknownFieldSet_)

### setUpdateTime(Timestamp value)
    
    
    public Backup.Builder setUpdateTime(Timestamp value)

Output only. The timestamp when this Backup resource was last updated.

`.google.protobuf.Timestamp update_time = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### setUpdateTime(Timestamp.Builder builderForValue)
    
    
    public Backup.Builder setUpdateTime(Timestamp.Builder builderForValue)

Output only. The timestamp when this Backup resource was last updated.

`.google.protobuf.Timestamp update_time = 4;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` |   
  
### setVolumeCount(int value)
    
    
    public Backup.Builder setVolumeCount(int value)

Output only. The total number of volume backups contained in the Backup.

`int32 volume_count = 22;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The volumeCount to set.  
**Returns**  
---  
**Type** | **Description**  
`[Backup.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkebackup.v1.Backup.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
