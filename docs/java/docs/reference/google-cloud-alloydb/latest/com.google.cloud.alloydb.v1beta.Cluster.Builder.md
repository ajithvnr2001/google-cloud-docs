---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder
title: Class Cluster.Builder (0.88.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:58:43.164870+00:00
---

# Class Cluster.Builder (0.88.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Cluster.Builder (0.88.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.88.0 (latest)  0.84.0  0.83.0  0.82.0  0.80.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.63.0  0.62.0  0.61.0  0.59.0  0.57.0  0.56.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class Cluster.Builder extends GeneratedMessage.Builder<Cluster.Builder> implements ClusterOrBuilder

A cluster is a collection of regional AlloyDB resources. It can include a primary instance and one or more read pool instances. All cluster resources share a storage layer, which scales as needed.

Protobuf type `google.cloud.alloydb.v1beta.Cluster`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > Cluster.Builder

## Implements

[ClusterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.ClusterOrBuilder)

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
    
    
    public Cluster build()

**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster)` |   
  
### buildPartial()
    
    
    public Cluster buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster)` |   
  
### clear()
    
    
    public Cluster.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearAnnotations()
    
    
    public Cluster.Builder clearAnnotations()

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearAutomatedBackupPolicy()
    
    
    public Cluster.Builder clearAutomatedBackupPolicy()

The automated backup policy for this cluster.

If no policy is provided then the default policy will be used. If backups are supported for the cluster, the default policy takes one backup a day, has a backup window of 1 hour, and retains backups for 14 days. For more information on the defaults, consult the documentation for the message type.

`.google.cloud.alloydb.v1beta.AutomatedBackupPolicy automated_backup_policy = 17;`

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearBackupSource()
    
    
    public Cluster.Builder clearBackupSource()

Output only. Cluster created from backup.

` .google.cloud.alloydb.v1beta.BackupSource backup_source = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearCloudsqlBackupRunSource()
    
    
    public Cluster.Builder clearCloudsqlBackupRunSource()

Output only. Cluster created from CloudSQL snapshot.

` .google.cloud.alloydb.v1beta.CloudSQLBackupRunSource cloudsql_backup_run_source = 42 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearClusterType()
    
    
    public Cluster.Builder clearClusterType()

Output only. The type of the cluster. This is an output-only field and it's populated at the Cluster creation time or the Cluster promotion time. The cluster type is determined by which RPC was used to create the cluster (i.e. `CreateCluster` vs. `CreateSecondaryCluster`

` .google.cloud.alloydb.v1beta.Cluster.ClusterType cluster_type = 24 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### clearContinuousBackupConfig()
    
    
    public Cluster.Builder clearContinuousBackupConfig()

Optional. Continuous backup configuration for this cluster.

` .google.cloud.alloydb.v1beta.ContinuousBackupConfig continuous_backup_config = 27 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearContinuousBackupInfo()
    
    
    public Cluster.Builder clearContinuousBackupInfo()

Output only. Continuous backup properties for this cluster.

` .google.cloud.alloydb.v1beta.ContinuousBackupInfo continuous_backup_info = 28 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearCreateTime()
    
    
    public Cluster.Builder clearCreateTime()

Output only. Create time stamp

` .google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearDatabaseVersion()
    
    
    public Cluster.Builder clearDatabaseVersion()

Optional. The database engine major version. This is an optional field and it is populated at the Cluster creation time. If a database version is not supplied at cluster creation time, then a default database version will be used.

` .google.cloud.alloydb.v1beta.DatabaseVersion database_version = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### clearDataplexConfig()
    
    
    public Cluster.Builder clearDataplexConfig()

Optional. Configuration for Dataplex integration.

` .google.cloud.alloydb.v1beta.Cluster.DataplexConfig dataplex_config = 47 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearDeleteTime()
    
    
    public Cluster.Builder clearDeleteTime()

Output only. Delete time stamp

` .google.protobuf.Timestamp delete_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearDisplayName()
    
    
    public Cluster.Builder clearDisplayName()

User-settable and human-readable display name for the Cluster.

`string display_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### clearEncryptionConfig()
    
    
    public Cluster.Builder clearEncryptionConfig()

Optional. The encryption config can be specified to encrypt the data disks and other persistent data resources of a cluster with a customer-managed encryption key (CMEK). When this field is not specified, the cluster will then use default encryption scheme to protect the user data.

` .google.cloud.alloydb.v1beta.EncryptionConfig encryption_config = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearEncryptionInfo()
    
    
    public Cluster.Builder clearEncryptionInfo()

Output only. The encryption information for the cluster.

` .google.cloud.alloydb.v1beta.EncryptionInfo encryption_info = 20 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearEtag()
    
    
    public Cluster.Builder clearEtag()

For Resource freshness validation (<https://google.aip.dev/154>)

`string etag = 11;`

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### clearGeminiConfig() (deprecated)
    
    
    public Cluster.Builder clearGeminiConfig()

Optional. Deprecated and unused. This field will be removed in the near future.

` .google.cloud.alloydb.v1beta.GeminiClusterConfig gemini_config = 36 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearInitialUser()
    
    
    public Cluster.Builder clearInitialUser()

Input only. Initial user to setup during cluster creation. Required. If used in `RestoreCluster` this is ignored.

` .google.cloud.alloydb.v1beta.UserPassword initial_user = 14 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearLabels()
    
    
    public Cluster.Builder clearLabels()

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearMaintenanceSchedule()
    
    
    public Cluster.Builder clearMaintenanceSchedule()

Output only. The maintenance schedule for the cluster, generated for a specific rollout if a maintenance window is set.

` .google.cloud.alloydb.v1beta.MaintenanceSchedule maintenance_schedule = 37 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearMaintenanceUpdatePolicy()
    
    
    public Cluster.Builder clearMaintenanceUpdatePolicy()

Optional. The maintenance update policy determines when to allow or deny updates.

` .google.cloud.alloydb.v1beta.MaintenanceUpdatePolicy maintenance_update_policy = 32 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearMigrationSource()
    
    
    public Cluster.Builder clearMigrationSource()

Output only. Cluster created via DMS migration.

` .google.cloud.alloydb.v1beta.MigrationSource migration_source = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearName()
    
    
    public Cluster.Builder clearName()

Output only. The name of the cluster resource with the format:

  * projects/{project}/locations/{region}/clusters/{cluster_id} where the cluster ID segment should satisfy the regex expression `[a-z0-9-]+`. For more details see <https://google.aip.dev/122>. The prefix of the cluster resource name is the name of the parent resource:
  * projects/{project}/locations/{region}



`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### clearNetwork() (deprecated)
    
    
    public Cluster.Builder clearNetwork()

**Deprecated.** _google.cloud.alloydb.v1beta.Cluster.network is deprecated. See google/cloud/alloydb/v1beta/resources.proto;l=689_

Required. The resource link for the VPC network in which cluster resources are created and from which they are accessible via Private IP. The network must belong to the same project as the cluster. It is specified in the form: `projects/{project}/global/networks/{network_id}`. This is required to create a cluster. Deprecated, use network_config.network instead.

` string network = 10 [deprecated = true, (.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### clearNetworkConfig()
    
    
    public Cluster.Builder clearNetworkConfig()

` .google.cloud.alloydb.v1beta.Cluster.NetworkConfig network_config = 29 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearPrimaryConfig()
    
    
    public Cluster.Builder clearPrimaryConfig()

Output only. Cross Region replication config specific to PRIMARY cluster.

` .google.cloud.alloydb.v1beta.Cluster.PrimaryConfig primary_config = 23 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearPscConfig()
    
    
    public Cluster.Builder clearPscConfig()

Optional. The configuration for Private Service Connect (PSC) for the cluster.

` .google.cloud.alloydb.v1beta.Cluster.PscConfig psc_config = 31 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearReconciling()
    
    
    public Cluster.Builder clearReconciling()

Output only. Reconciling (<https://google.aip.dev/128#reconciliation>). Set to true if the current state of Cluster does not match the user's intended state, and the service is actively updating the resource to reconcile them. This can happen due to user-triggered updates or system actions like failover or maintenance.

`bool reconciling = 13 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### clearSatisfiesPzs()
    
    
    public Cluster.Builder clearSatisfiesPzs()

Output only. Reserved for future use.

`bool satisfies_pzs = 30 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### clearSecondaryConfig()
    
    
    public Cluster.Builder clearSecondaryConfig()

Cross Region replication config specific to SECONDARY cluster.

`.google.cloud.alloydb.v1beta.Cluster.SecondaryConfig secondary_config = 22;`

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearServiceAccountEmail()
    
    
    public Cluster.Builder clearServiceAccountEmail()

Output only. AlloyDB per-cluster service account. This service account is created per-cluster per-project, and is different from the per-project service account. The per-cluster service account naming format is subject to change.

`string service_account_email = 46 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### clearSource()
    
    
    public Cluster.Builder clearSource()

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearSslConfig() (deprecated)
    
    
    public Cluster.Builder clearSslConfig()

SSL configuration for this AlloyDB cluster.

`.google.cloud.alloydb.v1beta.SslConfig ssl_config = 18 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearState()
    
    
    public Cluster.Builder clearState()

Output only. The current serving state of the cluster.

` .google.cloud.alloydb.v1beta.Cluster.State state = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### clearSubscriptionType()
    
    
    public Cluster.Builder clearSubscriptionType()

Optional. Subscription type of the cluster.

` .google.cloud.alloydb.v1beta.SubscriptionType subscription_type = 38 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### clearTags()
    
    
    public Cluster.Builder clearTags()

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearTrialMetadata()
    
    
    public Cluster.Builder clearTrialMetadata()

Output only. Metadata for free trial clusters

` .google.cloud.alloydb.v1beta.Cluster.TrialMetadata trial_metadata = 39 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### clearUid()
    
    
    public Cluster.Builder clearUid()

Output only. The system-generated UID of the resource. The UID is assigned when the resource is created, and it is retained until it is deleted.

`string uid = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### clearUpdateTime()
    
    
    public Cluster.Builder clearUpdateTime()

Output only. Update time stamp

` .google.protobuf.Timestamp update_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### containsAnnotations(String key)
    
    
    public boolean containsAnnotations(String key)

Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. <https://google.aip.dev/128>

`map<string, string> annotations = 12;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsLabels(String key)
    
    
    public boolean containsLabels(String key)

Labels as key value pairs

`map<string, string> labels = 7;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsTags(String key)
    
    
    public boolean containsTags(String key)

Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: `<code><code> "123/environment": "production", "123/costCenter": "marketing" </code></code>`

` map<string, string> tags = 41 [(.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAnnotations() (deprecated)
    
    
    public Map<String,String> getAnnotations()

Use [#getAnnotationsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder#com_google_cloud_alloydb_v1beta_Cluster_Builder_getAnnotationsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getAnnotationsCount()
    
    
    public int getAnnotationsCount()

Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. <https://google.aip.dev/128>

`map<string, string> annotations = 12;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAnnotationsMap()
    
    
    public Map<String,String> getAnnotationsMap()

Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. <https://google.aip.dev/128>

`map<string, string> annotations = 12;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getAnnotationsOrDefault(String key, String defaultValue)
    
    
    public String getAnnotationsOrDefault(String key, String defaultValue)

Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. <https://google.aip.dev/128>

`map<string, string> annotations = 12;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getAnnotationsOrThrow(String key)
    
    
    public String getAnnotationsOrThrow(String key)

Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. <https://google.aip.dev/128>

`map<string, string> annotations = 12;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getAutomatedBackupPolicy()
    
    
    public AutomatedBackupPolicy getAutomatedBackupPolicy()

The automated backup policy for this cluster.

If no policy is provided then the default policy will be used. If backups are supported for the cluster, the default policy takes one backup a day, has a backup window of 1 hour, and retains backups for 14 days. For more information on the defaults, consult the documentation for the message type.

`.google.cloud.alloydb.v1beta.AutomatedBackupPolicy automated_backup_policy = 17;`

**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.AutomatedBackupPolicy)` | The automatedBackupPolicy.  
  
### getAutomatedBackupPolicyBuilder()
    
    
    public AutomatedBackupPolicy.Builder getAutomatedBackupPolicyBuilder()

The automated backup policy for this cluster.

If no policy is provided then the default policy will be used. If backups are supported for the cluster, the default policy takes one backup a day, has a backup window of 1 hour, and retains backups for 14 days. For more information on the defaults, consult the documentation for the message type.

`.google.cloud.alloydb.v1beta.AutomatedBackupPolicy automated_backup_policy = 17;`

**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.AutomatedBackupPolicy.Builder)` |   
  
### getAutomatedBackupPolicyOrBuilder()
    
    
    public AutomatedBackupPolicyOrBuilder getAutomatedBackupPolicyOrBuilder()

The automated backup policy for this cluster.

If no policy is provided then the default policy will be used. If backups are supported for the cluster, the default policy takes one backup a day, has a backup window of 1 hour, and retains backups for 14 days. For more information on the defaults, consult the documentation for the message type.

`.google.cloud.alloydb.v1beta.AutomatedBackupPolicy automated_backup_policy = 17;`

**Returns**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.AutomatedBackupPolicyOrBuilder)` |   
  
### getBackupSource()
    
    
    public BackupSource getBackupSource()

Output only. Cluster created from backup.

` .google.cloud.alloydb.v1beta.BackupSource backup_source = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[BackupSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.BackupSource)` | The backupSource.  
  
### getBackupSourceBuilder()
    
    
    public BackupSource.Builder getBackupSourceBuilder()

Output only. Cluster created from backup.

` .google.cloud.alloydb.v1beta.BackupSource backup_source = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[BackupSource.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.BackupSource.Builder)` |   
  
### getBackupSourceOrBuilder()
    
    
    public BackupSourceOrBuilder getBackupSourceOrBuilder()

Output only. Cluster created from backup.

` .google.cloud.alloydb.v1beta.BackupSource backup_source = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[BackupSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.BackupSourceOrBuilder)` |   
  
### getCloudsqlBackupRunSource()
    
    
    public CloudSQLBackupRunSource getCloudsqlBackupRunSource()

Output only. Cluster created from CloudSQL snapshot.

` .google.cloud.alloydb.v1beta.CloudSQLBackupRunSource cloudsql_backup_run_source = 42 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[CloudSQLBackupRunSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.CloudSQLBackupRunSource)` | The cloudsqlBackupRunSource.  
  
### getCloudsqlBackupRunSourceBuilder()
    
    
    public CloudSQLBackupRunSource.Builder getCloudsqlBackupRunSourceBuilder()

Output only. Cluster created from CloudSQL snapshot.

` .google.cloud.alloydb.v1beta.CloudSQLBackupRunSource cloudsql_backup_run_source = 42 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[CloudSQLBackupRunSource.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.CloudSQLBackupRunSource.Builder)` |   
  
### getCloudsqlBackupRunSourceOrBuilder()
    
    
    public CloudSQLBackupRunSourceOrBuilder getCloudsqlBackupRunSourceOrBuilder()

Output only. Cluster created from CloudSQL snapshot.

` .google.cloud.alloydb.v1beta.CloudSQLBackupRunSource cloudsql_backup_run_source = 42 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[CloudSQLBackupRunSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.CloudSQLBackupRunSourceOrBuilder)` |   
  
### getClusterType()
    
    
    public Cluster.ClusterType getClusterType()

Output only. The type of the cluster. This is an output-only field and it's populated at the Cluster creation time or the Cluster promotion time. The cluster type is determined by which RPC was used to create the cluster (i.e. `CreateCluster` vs. `CreateSecondaryCluster`

` .google.cloud.alloydb.v1beta.Cluster.ClusterType cluster_type = 24 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.ClusterType](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.ClusterType)` | The clusterType.  
  
### getClusterTypeValue()
    
    
    public int getClusterTypeValue()

Output only. The type of the cluster. This is an output-only field and it's populated at the Cluster creation time or the Cluster promotion time. The cluster type is determined by which RPC was used to create the cluster (i.e. `CreateCluster` vs. `CreateSecondaryCluster`

` .google.cloud.alloydb.v1beta.Cluster.ClusterType cluster_type = 24 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for clusterType.  
  
### getContinuousBackupConfig()
    
    
    public ContinuousBackupConfig getContinuousBackupConfig()

Optional. Continuous backup configuration for this cluster.

` .google.cloud.alloydb.v1beta.ContinuousBackupConfig continuous_backup_config = 27 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ContinuousBackupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.ContinuousBackupConfig)` | The continuousBackupConfig.  
  
### getContinuousBackupConfigBuilder()
    
    
    public ContinuousBackupConfig.Builder getContinuousBackupConfigBuilder()

Optional. Continuous backup configuration for this cluster.

` .google.cloud.alloydb.v1beta.ContinuousBackupConfig continuous_backup_config = 27 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ContinuousBackupConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.ContinuousBackupConfig.Builder)` |   
  
### getContinuousBackupConfigOrBuilder()
    
    
    public ContinuousBackupConfigOrBuilder getContinuousBackupConfigOrBuilder()

Optional. Continuous backup configuration for this cluster.

` .google.cloud.alloydb.v1beta.ContinuousBackupConfig continuous_backup_config = 27 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ContinuousBackupConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.ContinuousBackupConfigOrBuilder)` |   
  
### getContinuousBackupInfo()
    
    
    public ContinuousBackupInfo getContinuousBackupInfo()

Output only. Continuous backup properties for this cluster.

` .google.cloud.alloydb.v1beta.ContinuousBackupInfo continuous_backup_info = 28 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ContinuousBackupInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.ContinuousBackupInfo)` | The continuousBackupInfo.  
  
### getContinuousBackupInfoBuilder()
    
    
    public ContinuousBackupInfo.Builder getContinuousBackupInfoBuilder()

Output only. Continuous backup properties for this cluster.

` .google.cloud.alloydb.v1beta.ContinuousBackupInfo continuous_backup_info = 28 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ContinuousBackupInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.ContinuousBackupInfo.Builder)` |   
  
### getContinuousBackupInfoOrBuilder()
    
    
    public ContinuousBackupInfoOrBuilder getContinuousBackupInfoOrBuilder()

Output only. Continuous backup properties for this cluster.

` .google.cloud.alloydb.v1beta.ContinuousBackupInfo continuous_backup_info = 28 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ContinuousBackupInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.ContinuousBackupInfoOrBuilder)` |   
  
### getCreateTime()
    
    
    public Timestamp getCreateTime()

Output only. Create time stamp

` .google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeBuilder()
    
    
    public Timestamp.Builder getCreateTimeBuilder()

Output only. Create time stamp

` .google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getCreateTimeOrBuilder()
    
    
    public TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Create time stamp

` .google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDatabaseVersion()
    
    
    public DatabaseVersion getDatabaseVersion()

Optional. The database engine major version. This is an optional field and it is populated at the Cluster creation time. If a database version is not supplied at cluster creation time, then a default database version will be used.

` .google.cloud.alloydb.v1beta.DatabaseVersion database_version = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DatabaseVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.DatabaseVersion)` | The databaseVersion.  
  
### getDatabaseVersionValue()
    
    
    public int getDatabaseVersionValue()

Optional. The database engine major version. This is an optional field and it is populated at the Cluster creation time. If a database version is not supplied at cluster creation time, then a default database version will be used.

` .google.cloud.alloydb.v1beta.DatabaseVersion database_version = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for databaseVersion.  
  
### getDataplexConfig()
    
    
    public Cluster.DataplexConfig getDataplexConfig()

Optional. Configuration for Dataplex integration.

` .google.cloud.alloydb.v1beta.Cluster.DataplexConfig dataplex_config = 47 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.DataplexConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.DataplexConfig)` | The dataplexConfig.  
  
### getDataplexConfigBuilder()
    
    
    public Cluster.DataplexConfig.Builder getDataplexConfigBuilder()

Optional. Configuration for Dataplex integration.

` .google.cloud.alloydb.v1beta.Cluster.DataplexConfig dataplex_config = 47 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.DataplexConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.DataplexConfig.Builder)` |   
  
### getDataplexConfigOrBuilder()
    
    
    public Cluster.DataplexConfigOrBuilder getDataplexConfigOrBuilder()

Optional. Configuration for Dataplex integration.

` .google.cloud.alloydb.v1beta.Cluster.DataplexConfig dataplex_config = 47 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.DataplexConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.DataplexConfigOrBuilder)` |   
  
### getDefaultInstanceForType()
    
    
    public Cluster getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster)` |   
  
### getDeleteTime()
    
    
    public Timestamp getDeleteTime()

Output only. Delete time stamp

` .google.protobuf.Timestamp delete_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The deleteTime.  
  
### getDeleteTimeBuilder()
    
    
    public Timestamp.Builder getDeleteTimeBuilder()

Output only. Delete time stamp

` .google.protobuf.Timestamp delete_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getDeleteTimeOrBuilder()
    
    
    public TimestampOrBuilder getDeleteTimeOrBuilder()

Output only. Delete time stamp

` .google.protobuf.Timestamp delete_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getDisplayName()
    
    
    public String getDisplayName()

User-settable and human-readable display name for the Cluster.

`string display_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public ByteString getDisplayNameBytes()

User-settable and human-readable display name for the Cluster.

`string display_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getEncryptionConfig()
    
    
    public EncryptionConfig getEncryptionConfig()

Optional. The encryption config can be specified to encrypt the data disks and other persistent data resources of a cluster with a customer-managed encryption key (CMEK). When this field is not specified, the cluster will then use default encryption scheme to protect the user data.

` .google.cloud.alloydb.v1beta.EncryptionConfig encryption_config = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.EncryptionConfig)` | The encryptionConfig.  
  
### getEncryptionConfigBuilder()
    
    
    public EncryptionConfig.Builder getEncryptionConfigBuilder()

Optional. The encryption config can be specified to encrypt the data disks and other persistent data resources of a cluster with a customer-managed encryption key (CMEK). When this field is not specified, the cluster will then use default encryption scheme to protect the user data.

` .google.cloud.alloydb.v1beta.EncryptionConfig encryption_config = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EncryptionConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.EncryptionConfig.Builder)` |   
  
### getEncryptionConfigOrBuilder()
    
    
    public EncryptionConfigOrBuilder getEncryptionConfigOrBuilder()

Optional. The encryption config can be specified to encrypt the data disks and other persistent data resources of a cluster with a customer-managed encryption key (CMEK). When this field is not specified, the cluster will then use default encryption scheme to protect the user data.

` .google.cloud.alloydb.v1beta.EncryptionConfig encryption_config = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[EncryptionConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.EncryptionConfigOrBuilder)` |   
  
### getEncryptionInfo()
    
    
    public EncryptionInfo getEncryptionInfo()

Output only. The encryption information for the cluster.

` .google.cloud.alloydb.v1beta.EncryptionInfo encryption_info = 20 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[EncryptionInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.EncryptionInfo)` | The encryptionInfo.  
  
### getEncryptionInfoBuilder()
    
    
    public EncryptionInfo.Builder getEncryptionInfoBuilder()

Output only. The encryption information for the cluster.

` .google.cloud.alloydb.v1beta.EncryptionInfo encryption_info = 20 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[EncryptionInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.EncryptionInfo.Builder)` |   
  
### getEncryptionInfoOrBuilder()
    
    
    public EncryptionInfoOrBuilder getEncryptionInfoOrBuilder()

Output only. The encryption information for the cluster.

` .google.cloud.alloydb.v1beta.EncryptionInfo encryption_info = 20 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[EncryptionInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.EncryptionInfoOrBuilder)` |   
  
### getEtag()
    
    
    public String getEtag()

For Resource freshness validation (<https://google.aip.dev/154>)

`string etag = 11;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The etag.  
  
### getEtagBytes()
    
    
    public ByteString getEtagBytes()

For Resource freshness validation (<https://google.aip.dev/154>)

`string etag = 11;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for etag.  
  
### getGeminiConfig() (deprecated)
    
    
    public GeminiClusterConfig getGeminiConfig()

**Deprecated.** _google.cloud.alloydb.v1beta.Cluster.gemini_config is deprecated. See google/cloud/alloydb/v1beta/resources.proto;l=771_

Optional. Deprecated and unused. This field will be removed in the near future.

` .google.cloud.alloydb.v1beta.GeminiClusterConfig gemini_config = 36 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[GeminiClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.GeminiClusterConfig)` | The geminiConfig.  
  
### getGeminiConfigBuilder() (deprecated)
    
    
    public GeminiClusterConfig.Builder getGeminiConfigBuilder()

Optional. Deprecated and unused. This field will be removed in the near future.

` .google.cloud.alloydb.v1beta.GeminiClusterConfig gemini_config = 36 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[GeminiClusterConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.GeminiClusterConfig.Builder)` |   
  
### getGeminiConfigOrBuilder() (deprecated)
    
    
    public GeminiClusterConfigOrBuilder getGeminiConfigOrBuilder()

Optional. Deprecated and unused. This field will be removed in the near future.

` .google.cloud.alloydb.v1beta.GeminiClusterConfig gemini_config = 36 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[GeminiClusterConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.GeminiClusterConfigOrBuilder)` |   
  
### getInitialUser()
    
    
    public UserPassword getInitialUser()

Input only. Initial user to setup during cluster creation. Required. If used in `RestoreCluster` this is ignored.

` .google.cloud.alloydb.v1beta.UserPassword initial_user = 14 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[UserPassword](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.UserPassword)` | The initialUser.  
  
### getInitialUserBuilder()
    
    
    public UserPassword.Builder getInitialUserBuilder()

Input only. Initial user to setup during cluster creation. Required. If used in `RestoreCluster` this is ignored.

` .google.cloud.alloydb.v1beta.UserPassword initial_user = 14 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[UserPassword.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.UserPassword.Builder)` |   
  
### getInitialUserOrBuilder()
    
    
    public UserPasswordOrBuilder getInitialUserOrBuilder()

Input only. Initial user to setup during cluster creation. Required. If used in `RestoreCluster` this is ignored.

` .google.cloud.alloydb.v1beta.UserPassword initial_user = 14 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[UserPasswordOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.UserPasswordOrBuilder)` |   
  
### getLabels() (deprecated)
    
    
    public Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder#com_google_cloud_alloydb_v1beta_Cluster_Builder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public int getLabelsCount()

Labels as key value pairs

`map<string, string> labels = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public Map<String,String> getLabelsMap()

Labels as key value pairs

`map<string, string> labels = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public String getLabelsOrDefault(String key, String defaultValue)

Labels as key value pairs

`map<string, string> labels = 7;`

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

Labels as key value pairs

`map<string, string> labels = 7;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMaintenanceSchedule()
    
    
    public MaintenanceSchedule getMaintenanceSchedule()

Output only. The maintenance schedule for the cluster, generated for a specific rollout if a maintenance window is set.

` .google.cloud.alloydb.v1beta.MaintenanceSchedule maintenance_schedule = 37 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MaintenanceSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.MaintenanceSchedule)` | The maintenanceSchedule.  
  
### getMaintenanceScheduleBuilder()
    
    
    public MaintenanceSchedule.Builder getMaintenanceScheduleBuilder()

Output only. The maintenance schedule for the cluster, generated for a specific rollout if a maintenance window is set.

` .google.cloud.alloydb.v1beta.MaintenanceSchedule maintenance_schedule = 37 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MaintenanceSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.MaintenanceSchedule.Builder)` |   
  
### getMaintenanceScheduleOrBuilder()
    
    
    public MaintenanceScheduleOrBuilder getMaintenanceScheduleOrBuilder()

Output only. The maintenance schedule for the cluster, generated for a specific rollout if a maintenance window is set.

` .google.cloud.alloydb.v1beta.MaintenanceSchedule maintenance_schedule = 37 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MaintenanceScheduleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.MaintenanceScheduleOrBuilder)` |   
  
### getMaintenanceUpdatePolicy()
    
    
    public MaintenanceUpdatePolicy getMaintenanceUpdatePolicy()

Optional. The maintenance update policy determines when to allow or deny updates.

` .google.cloud.alloydb.v1beta.MaintenanceUpdatePolicy maintenance_update_policy = 32 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MaintenanceUpdatePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.MaintenanceUpdatePolicy)` | The maintenanceUpdatePolicy.  
  
### getMaintenanceUpdatePolicyBuilder()
    
    
    public MaintenanceUpdatePolicy.Builder getMaintenanceUpdatePolicyBuilder()

Optional. The maintenance update policy determines when to allow or deny updates.

` .google.cloud.alloydb.v1beta.MaintenanceUpdatePolicy maintenance_update_policy = 32 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MaintenanceUpdatePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.MaintenanceUpdatePolicy.Builder)` |   
  
### getMaintenanceUpdatePolicyOrBuilder()
    
    
    public MaintenanceUpdatePolicyOrBuilder getMaintenanceUpdatePolicyOrBuilder()

Optional. The maintenance update policy determines when to allow or deny updates.

` .google.cloud.alloydb.v1beta.MaintenanceUpdatePolicy maintenance_update_policy = 32 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[MaintenanceUpdatePolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.MaintenanceUpdatePolicyOrBuilder)` |   
  
### getMigrationSource()
    
    
    public MigrationSource getMigrationSource()

Output only. Cluster created via DMS migration.

` .google.cloud.alloydb.v1beta.MigrationSource migration_source = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MigrationSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.MigrationSource)` | The migrationSource.  
  
### getMigrationSourceBuilder()
    
    
    public MigrationSource.Builder getMigrationSourceBuilder()

Output only. Cluster created via DMS migration.

` .google.cloud.alloydb.v1beta.MigrationSource migration_source = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MigrationSource.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.MigrationSource.Builder)` |   
  
### getMigrationSourceOrBuilder()
    
    
    public MigrationSourceOrBuilder getMigrationSourceOrBuilder()

Output only. Cluster created via DMS migration.

` .google.cloud.alloydb.v1beta.MigrationSource migration_source = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MigrationSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.MigrationSourceOrBuilder)` |   
  
### getMutableAnnotations() (deprecated)
    
    
    public Map<String,String> getMutableAnnotations()

Use alternate mutation accessors instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getMutableLabels() (deprecated)
    
    
    public Map<String,String> getMutableLabels()

Use alternate mutation accessors instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getMutableTags() (deprecated)
    
    
    public Map<String,String> getMutableTags()

Use alternate mutation accessors instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getName()
    
    
    public String getName()

Output only. The name of the cluster resource with the format:

  * projects/{project}/locations/{region}/clusters/{cluster_id} where the cluster ID segment should satisfy the regex expression `[a-z0-9-]+`. For more details see <https://google.aip.dev/122>. The prefix of the cluster resource name is the name of the parent resource:
  * projects/{project}/locations/{region}



`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

Output only. The name of the cluster resource with the format:

  * projects/{project}/locations/{region}/clusters/{cluster_id} where the cluster ID segment should satisfy the regex expression `[a-z0-9-]+`. For more details see <https://google.aip.dev/122>. The prefix of the cluster resource name is the name of the parent resource:
  * projects/{project}/locations/{region}



`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getNetwork() (deprecated)
    
    
    public String getNetwork()

**Deprecated.** _google.cloud.alloydb.v1beta.Cluster.network is deprecated. See google/cloud/alloydb/v1beta/resources.proto;l=689_

Required. The resource link for the VPC network in which cluster resources are created and from which they are accessible via Private IP. The network must belong to the same project as the cluster. It is specified in the form: `projects/{project}/global/networks/{network_id}`. This is required to create a cluster. Deprecated, use network_config.network instead.

` string network = 10 [deprecated = true, (.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The network.  
  
### getNetworkBytes() (deprecated)
    
    
    public ByteString getNetworkBytes()

**Deprecated.** _google.cloud.alloydb.v1beta.Cluster.network is deprecated. See google/cloud/alloydb/v1beta/resources.proto;l=689_

Required. The resource link for the VPC network in which cluster resources are created and from which they are accessible via Private IP. The network must belong to the same project as the cluster. It is specified in the form: `projects/{project}/global/networks/{network_id}`. This is required to create a cluster. Deprecated, use network_config.network instead.

` string network = 10 [deprecated = true, (.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for network.  
  
### getNetworkConfig()
    
    
    public Cluster.NetworkConfig getNetworkConfig()

` .google.cloud.alloydb.v1beta.Cluster.NetworkConfig network_config = 29 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.NetworkConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.NetworkConfig)` | The networkConfig.  
  
### getNetworkConfigBuilder()
    
    
    public Cluster.NetworkConfig.Builder getNetworkConfigBuilder()

` .google.cloud.alloydb.v1beta.Cluster.NetworkConfig network_config = 29 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.NetworkConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.NetworkConfig.Builder)` |   
  
### getNetworkConfigOrBuilder()
    
    
    public Cluster.NetworkConfigOrBuilder getNetworkConfigOrBuilder()

` .google.cloud.alloydb.v1beta.Cluster.NetworkConfig network_config = 29 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.NetworkConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.NetworkConfigOrBuilder)` |   
  
### getPrimaryConfig()
    
    
    public Cluster.PrimaryConfig getPrimaryConfig()

Output only. Cross Region replication config specific to PRIMARY cluster.

` .google.cloud.alloydb.v1beta.Cluster.PrimaryConfig primary_config = 23 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.PrimaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.PrimaryConfig)` | The primaryConfig.  
  
### getPrimaryConfigBuilder()
    
    
    public Cluster.PrimaryConfig.Builder getPrimaryConfigBuilder()

Output only. Cross Region replication config specific to PRIMARY cluster.

` .google.cloud.alloydb.v1beta.Cluster.PrimaryConfig primary_config = 23 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.PrimaryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.PrimaryConfig.Builder)` |   
  
### getPrimaryConfigOrBuilder()
    
    
    public Cluster.PrimaryConfigOrBuilder getPrimaryConfigOrBuilder()

Output only. Cross Region replication config specific to PRIMARY cluster.

` .google.cloud.alloydb.v1beta.Cluster.PrimaryConfig primary_config = 23 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.PrimaryConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.PrimaryConfigOrBuilder)` |   
  
### getPscConfig()
    
    
    public Cluster.PscConfig getPscConfig()

Optional. The configuration for Private Service Connect (PSC) for the cluster.

` .google.cloud.alloydb.v1beta.Cluster.PscConfig psc_config = 31 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.PscConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.PscConfig)` | The pscConfig.  
  
### getPscConfigBuilder()
    
    
    public Cluster.PscConfig.Builder getPscConfigBuilder()

Optional. The configuration for Private Service Connect (PSC) for the cluster.

` .google.cloud.alloydb.v1beta.Cluster.PscConfig psc_config = 31 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.PscConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.PscConfig.Builder)` |   
  
### getPscConfigOrBuilder()
    
    
    public Cluster.PscConfigOrBuilder getPscConfigOrBuilder()

Optional. The configuration for Private Service Connect (PSC) for the cluster.

` .google.cloud.alloydb.v1beta.Cluster.PscConfig psc_config = 31 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.PscConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.PscConfigOrBuilder)` |   
  
### getReconciling()
    
    
    public boolean getReconciling()

Output only. Reconciling (<https://google.aip.dev/128#reconciliation>). Set to true if the current state of Cluster does not match the user's intended state, and the service is actively updating the resource to reconcile them. This can happen due to user-triggered updates or system actions like failover or maintenance.

`bool reconciling = 13 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The reconciling.  
  
### getSatisfiesPzs()
    
    
    public boolean getSatisfiesPzs()

Output only. Reserved for future use.

`bool satisfies_pzs = 30 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The satisfiesPzs.  
  
### getSecondaryConfig()
    
    
    public Cluster.SecondaryConfig getSecondaryConfig()

Cross Region replication config specific to SECONDARY cluster.

`.google.cloud.alloydb.v1beta.Cluster.SecondaryConfig secondary_config = 22;`

**Returns**  
---  
**Type** | **Description**  
`[Cluster.SecondaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.SecondaryConfig)` | The secondaryConfig.  
  
### getSecondaryConfigBuilder()
    
    
    public Cluster.SecondaryConfig.Builder getSecondaryConfigBuilder()

Cross Region replication config specific to SECONDARY cluster.

`.google.cloud.alloydb.v1beta.Cluster.SecondaryConfig secondary_config = 22;`

**Returns**  
---  
**Type** | **Description**  
`[Cluster.SecondaryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.SecondaryConfig.Builder)` |   
  
### getSecondaryConfigOrBuilder()
    
    
    public Cluster.SecondaryConfigOrBuilder getSecondaryConfigOrBuilder()

Cross Region replication config specific to SECONDARY cluster.

`.google.cloud.alloydb.v1beta.Cluster.SecondaryConfig secondary_config = 22;`

**Returns**  
---  
**Type** | **Description**  
`[Cluster.SecondaryConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.SecondaryConfigOrBuilder)` |   
  
### getServiceAccountEmail()
    
    
    public String getServiceAccountEmail()

Output only. AlloyDB per-cluster service account. This service account is created per-cluster per-project, and is different from the per-project service account. The per-cluster service account naming format is subject to change.

`string service_account_email = 46 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serviceAccountEmail.  
  
### getServiceAccountEmailBytes()
    
    
    public ByteString getServiceAccountEmailBytes()

Output only. AlloyDB per-cluster service account. This service account is created per-cluster per-project, and is different from the per-project service account. The per-cluster service account naming format is subject to change.

`string service_account_email = 46 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serviceAccountEmail.  
  
### getSourceCase()
    
    
    public Cluster.SourceCase getSourceCase()

**Returns**  
---  
**Type** | **Description**  
`[Cluster.SourceCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.SourceCase)` |   
  
### getSslConfig() (deprecated)
    
    
    public SslConfig getSslConfig()

**Deprecated.** _google.cloud.alloydb.v1beta.Cluster.ssl_config is deprecated. See google/cloud/alloydb/v1beta/resources.proto;l=724_

SSL configuration for this AlloyDB cluster.

`.google.cloud.alloydb.v1beta.SslConfig ssl_config = 18 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[SslConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.SslConfig)` | The sslConfig.  
  
### getSslConfigBuilder() (deprecated)
    
    
    public SslConfig.Builder getSslConfigBuilder()

SSL configuration for this AlloyDB cluster.

`.google.cloud.alloydb.v1beta.SslConfig ssl_config = 18 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[SslConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.SslConfig.Builder)` |   
  
### getSslConfigOrBuilder() (deprecated)
    
    
    public SslConfigOrBuilder getSslConfigOrBuilder()

SSL configuration for this AlloyDB cluster.

`.google.cloud.alloydb.v1beta.SslConfig ssl_config = 18 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[SslConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.SslConfigOrBuilder)` |   
  
### getState()
    
    
    public Cluster.State getState()

Output only. The current serving state of the cluster.

` .google.cloud.alloydb.v1beta.Cluster.State state = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.State)` | The state.  
  
### getStateValue()
    
    
    public int getStateValue()

Output only. The current serving state of the cluster.

` .google.cloud.alloydb.v1beta.Cluster.State state = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getSubscriptionType()
    
    
    public SubscriptionType getSubscriptionType()

Optional. Subscription type of the cluster.

` .google.cloud.alloydb.v1beta.SubscriptionType subscription_type = 38 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[SubscriptionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.SubscriptionType)` | The subscriptionType.  
  
### getSubscriptionTypeValue()
    
    
    public int getSubscriptionTypeValue()

Optional. Subscription type of the cluster.

` .google.cloud.alloydb.v1beta.SubscriptionType subscription_type = 38 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for subscriptionType.  
  
### getTags() (deprecated)
    
    
    public Map<String,String> getTags()

Use [#getTagsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder#com_google_cloud_alloydb_v1beta_Cluster_Builder_getTagsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getTagsCount()
    
    
    public int getTagsCount()

Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: `<code><code> "123/environment": "production", "123/costCenter": "marketing" </code></code>`

` map<string, string> tags = 41 [(.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getTagsMap()
    
    
    public Map<String,String> getTagsMap()

Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: `<code><code> "123/environment": "production", "123/costCenter": "marketing" </code></code>`

` map<string, string> tags = 41 [(.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getTagsOrDefault(String key, String defaultValue)
    
    
    public String getTagsOrDefault(String key, String defaultValue)

Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: `<code><code> "123/environment": "production", "123/costCenter": "marketing" </code></code>`

` map<string, string> tags = 41 [(.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getTagsOrThrow(String key)
    
    
    public String getTagsOrThrow(String key)

Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: `<code><code> "123/environment": "production", "123/costCenter": "marketing" </code></code>`

` map<string, string> tags = 41 [(.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getTrialMetadata()
    
    
    public Cluster.TrialMetadata getTrialMetadata()

Output only. Metadata for free trial clusters

` .google.cloud.alloydb.v1beta.Cluster.TrialMetadata trial_metadata = 39 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.TrialMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.TrialMetadata)` | The trialMetadata.  
  
### getTrialMetadataBuilder()
    
    
    public Cluster.TrialMetadata.Builder getTrialMetadataBuilder()

Output only. Metadata for free trial clusters

` .google.cloud.alloydb.v1beta.Cluster.TrialMetadata trial_metadata = 39 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.TrialMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.TrialMetadata.Builder)` |   
  
### getTrialMetadataOrBuilder()
    
    
    public Cluster.TrialMetadataOrBuilder getTrialMetadataOrBuilder()

Output only. Metadata for free trial clusters

` .google.cloud.alloydb.v1beta.Cluster.TrialMetadata trial_metadata = 39 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster.TrialMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.TrialMetadataOrBuilder)` |   
  
### getUid()
    
    
    public String getUid()

Output only. The system-generated UID of the resource. The UID is assigned when the resource is created, and it is retained until it is deleted.

`string uid = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The uid.  
  
### getUidBytes()
    
    
    public ByteString getUidBytes()

Output only. The system-generated UID of the resource. The UID is assigned when the resource is created, and it is retained until it is deleted.

`string uid = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for uid.  
  
### getUpdateTime()
    
    
    public Timestamp getUpdateTime()

Output only. Update time stamp

` .google.protobuf.Timestamp update_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeBuilder()
    
    
    public Timestamp.Builder getUpdateTimeBuilder()

Output only. Update time stamp

` .google.protobuf.Timestamp update_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getUpdateTimeOrBuilder()
    
    
    public TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. Update time stamp

` .google.protobuf.Timestamp update_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasAutomatedBackupPolicy()
    
    
    public boolean hasAutomatedBackupPolicy()

The automated backup policy for this cluster.

If no policy is provided then the default policy will be used. If backups are supported for the cluster, the default policy takes one backup a day, has a backup window of 1 hour, and retains backups for 14 days. For more information on the defaults, consult the documentation for the message type.

`.google.cloud.alloydb.v1beta.AutomatedBackupPolicy automated_backup_policy = 17;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the automatedBackupPolicy field is set.  
  
### hasBackupSource()
    
    
    public boolean hasBackupSource()

Output only. Cluster created from backup.

` .google.cloud.alloydb.v1beta.BackupSource backup_source = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the backupSource field is set.  
  
### hasCloudsqlBackupRunSource()
    
    
    public boolean hasCloudsqlBackupRunSource()

Output only. Cluster created from CloudSQL snapshot.

` .google.cloud.alloydb.v1beta.CloudSQLBackupRunSource cloudsql_backup_run_source = 42 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cloudsqlBackupRunSource field is set.  
  
### hasContinuousBackupConfig()
    
    
    public boolean hasContinuousBackupConfig()

Optional. Continuous backup configuration for this cluster.

` .google.cloud.alloydb.v1beta.ContinuousBackupConfig continuous_backup_config = 27 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the continuousBackupConfig field is set.  
  
### hasContinuousBackupInfo()
    
    
    public boolean hasContinuousBackupInfo()

Output only. Continuous backup properties for this cluster.

` .google.cloud.alloydb.v1beta.ContinuousBackupInfo continuous_backup_info = 28 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the continuousBackupInfo field is set.  
  
### hasCreateTime()
    
    
    public boolean hasCreateTime()

Output only. Create time stamp

` .google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasDataplexConfig()
    
    
    public boolean hasDataplexConfig()

Optional. Configuration for Dataplex integration.

` .google.cloud.alloydb.v1beta.Cluster.DataplexConfig dataplex_config = 47 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the dataplexConfig field is set.  
  
### hasDeleteTime()
    
    
    public boolean hasDeleteTime()

Output only. Delete time stamp

` .google.protobuf.Timestamp delete_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the deleteTime field is set.  
  
### hasEncryptionConfig()
    
    
    public boolean hasEncryptionConfig()

Optional. The encryption config can be specified to encrypt the data disks and other persistent data resources of a cluster with a customer-managed encryption key (CMEK). When this field is not specified, the cluster will then use default encryption scheme to protect the user data.

` .google.cloud.alloydb.v1beta.EncryptionConfig encryption_config = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the encryptionConfig field is set.  
  
### hasEncryptionInfo()
    
    
    public boolean hasEncryptionInfo()

Output only. The encryption information for the cluster.

` .google.cloud.alloydb.v1beta.EncryptionInfo encryption_info = 20 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the encryptionInfo field is set.  
  
### hasGeminiConfig() (deprecated)
    
    
    public boolean hasGeminiConfig()

**Deprecated.** _google.cloud.alloydb.v1beta.Cluster.gemini_config is deprecated. See google/cloud/alloydb/v1beta/resources.proto;l=771_

Optional. Deprecated and unused. This field will be removed in the near future.

` .google.cloud.alloydb.v1beta.GeminiClusterConfig gemini_config = 36 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the geminiConfig field is set.  
  
### hasInitialUser()
    
    
    public boolean hasInitialUser()

Input only. Initial user to setup during cluster creation. Required. If used in `RestoreCluster` this is ignored.

` .google.cloud.alloydb.v1beta.UserPassword initial_user = 14 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the initialUser field is set.  
  
### hasMaintenanceSchedule()
    
    
    public boolean hasMaintenanceSchedule()

Output only. The maintenance schedule for the cluster, generated for a specific rollout if a maintenance window is set.

` .google.cloud.alloydb.v1beta.MaintenanceSchedule maintenance_schedule = 37 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maintenanceSchedule field is set.  
  
### hasMaintenanceUpdatePolicy()
    
    
    public boolean hasMaintenanceUpdatePolicy()

Optional. The maintenance update policy determines when to allow or deny updates.

` .google.cloud.alloydb.v1beta.MaintenanceUpdatePolicy maintenance_update_policy = 32 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maintenanceUpdatePolicy field is set.  
  
### hasMigrationSource()
    
    
    public boolean hasMigrationSource()

Output only. Cluster created via DMS migration.

` .google.cloud.alloydb.v1beta.MigrationSource migration_source = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the migrationSource field is set.  
  
### hasNetworkConfig()
    
    
    public boolean hasNetworkConfig()

` .google.cloud.alloydb.v1beta.Cluster.NetworkConfig network_config = 29 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the networkConfig field is set.  
  
### hasPrimaryConfig()
    
    
    public boolean hasPrimaryConfig()

Output only. Cross Region replication config specific to PRIMARY cluster.

` .google.cloud.alloydb.v1beta.Cluster.PrimaryConfig primary_config = 23 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the primaryConfig field is set.  
  
### hasPscConfig()
    
    
    public boolean hasPscConfig()

Optional. The configuration for Private Service Connect (PSC) for the cluster.

` .google.cloud.alloydb.v1beta.Cluster.PscConfig psc_config = 31 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pscConfig field is set.  
  
### hasSecondaryConfig()
    
    
    public boolean hasSecondaryConfig()

Cross Region replication config specific to SECONDARY cluster.

`.google.cloud.alloydb.v1beta.Cluster.SecondaryConfig secondary_config = 22;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the secondaryConfig field is set.  
  
### hasSslConfig() (deprecated)
    
    
    public boolean hasSslConfig()

**Deprecated.** _google.cloud.alloydb.v1beta.Cluster.ssl_config is deprecated. See google/cloud/alloydb/v1beta/resources.proto;l=724_

SSL configuration for this AlloyDB cluster.

`.google.cloud.alloydb.v1beta.SslConfig ssl_config = 18 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sslConfig field is set.  
  
### hasTrialMetadata()
    
    
    public boolean hasTrialMetadata()

Output only. Metadata for free trial clusters

` .google.cloud.alloydb.v1beta.Cluster.TrialMetadata trial_metadata = 39 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the trialMetadata field is set.  
  
### hasUpdateTime()
    
    
    public boolean hasUpdateTime()

Output only. Update time stamp

` .google.protobuf.Timestamp update_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
### internalGetFieldAccessorTable()
    
    
    protected GeneratedMessage.FieldAccessorTable internalGetFieldAccessorTable()

**Returns**  
---  
**Type** | **Description**  
`[FieldAccessorTable](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.FieldAccessorTable.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.internalGetFieldAccessorTable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_internalGetFieldAccessorTable__)

### internalGetMapFieldReflection(int number)
    
    
    protected MapFieldReflectionAccessor internalGetMapFieldReflection(int number)

**Parameter**  
---  
**Name** | **Description**  
`number` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.MapFieldReflectionAccessor` |   
**Overrides**

com.google.protobuf.GeneratedMessage.Builder.internalGetMapFieldReflection(int)

### internalGetMutableMapFieldReflection(int number)
    
    
    protected MapFieldReflectionAccessor internalGetMutableMapFieldReflection(int number)

**Parameter**  
---  
**Name** | **Description**  
`number` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.MapFieldReflectionAccessor` |   
**Overrides**

com.google.protobuf.GeneratedMessage.Builder.internalGetMutableMapFieldReflection(int)

### isInitialized()
    
    
    public final boolean isInitialized()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_isInitialized__)

### mergeAutomatedBackupPolicy(AutomatedBackupPolicy value)
    
    
    public Cluster.Builder mergeAutomatedBackupPolicy(AutomatedBackupPolicy value)

The automated backup policy for this cluster.

If no policy is provided then the default policy will be used. If backups are supported for the cluster, the default policy takes one backup a day, has a backup window of 1 hour, and retains backups for 14 days. For more information on the defaults, consult the documentation for the message type.

`.google.cloud.alloydb.v1beta.AutomatedBackupPolicy automated_backup_policy = 17;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AutomatedBackupPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.AutomatedBackupPolicy)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### mergeBackupSource(BackupSource value)
    
    
    public Cluster.Builder mergeBackupSource(BackupSource value)

Output only. Cluster created from backup.

` .google.cloud.alloydb.v1beta.BackupSource backup_source = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BackupSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.BackupSource)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### mergeCloudsqlBackupRunSource(CloudSQLBackupRunSource value)
    
    
    public Cluster.Builder mergeCloudsqlBackupRunSource(CloudSQLBackupRunSource value)

Output only. Cluster created from CloudSQL snapshot.

` .google.cloud.alloydb.v1beta.CloudSQLBackupRunSource cloudsql_backup_run_source = 42 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CloudSQLBackupRunSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.CloudSQLBackupRunSource)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### mergeContinuousBackupConfig(ContinuousBackupConfig value)
    
    
    public Cluster.Builder mergeContinuousBackupConfig(ContinuousBackupConfig value)

Optional. Continuous backup configuration for this cluster.

` .google.cloud.alloydb.v1beta.ContinuousBackupConfig continuous_backup_config = 27 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ContinuousBackupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.ContinuousBackupConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### mergeContinuousBackupInfo(ContinuousBackupInfo value)
    
    
    public Cluster.Builder mergeContinuousBackupInfo(ContinuousBackupInfo value)

Output only. Continuous backup properties for this cluster.

` .google.cloud.alloydb.v1beta.ContinuousBackupInfo continuous_backup_info = 28 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ContinuousBackupInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.ContinuousBackupInfo)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### mergeCreateTime(Timestamp value)
    
    
    public Cluster.Builder mergeCreateTime(Timestamp value)

Output only. Create time stamp

` .google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### mergeDataplexConfig(Cluster.DataplexConfig value)
    
    
    public Cluster.Builder mergeDataplexConfig(Cluster.DataplexConfig value)

Optional. Configuration for Dataplex integration.

` .google.cloud.alloydb.v1beta.Cluster.DataplexConfig dataplex_config = 47 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Cluster.DataplexConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.DataplexConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### mergeDeleteTime(Timestamp value)
    
    
    public Cluster.Builder mergeDeleteTime(Timestamp value)

Output only. Delete time stamp

` .google.protobuf.Timestamp delete_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### mergeEncryptionConfig(EncryptionConfig value)
    
    
    public Cluster.Builder mergeEncryptionConfig(EncryptionConfig value)

Optional. The encryption config can be specified to encrypt the data disks and other persistent data resources of a cluster with a customer-managed encryption key (CMEK). When this field is not specified, the cluster will then use default encryption scheme to protect the user data.

` .google.cloud.alloydb.v1beta.EncryptionConfig encryption_config = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[EncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.EncryptionConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### mergeEncryptionInfo(EncryptionInfo value)
    
    
    public Cluster.Builder mergeEncryptionInfo(EncryptionInfo value)

Output only. The encryption information for the cluster.

` .google.cloud.alloydb.v1beta.EncryptionInfo encryption_info = 20 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[EncryptionInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.EncryptionInfo)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### mergeFrom(Cluster other)
    
    
    public Cluster.Builder mergeFrom(Cluster other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public Cluster.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public Cluster.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeGeminiConfig(GeminiClusterConfig value) (deprecated)
    
    
    public Cluster.Builder mergeGeminiConfig(GeminiClusterConfig value)

Optional. Deprecated and unused. This field will be removed in the near future.

` .google.cloud.alloydb.v1beta.GeminiClusterConfig gemini_config = 36 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[GeminiClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.GeminiClusterConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### mergeInitialUser(UserPassword value)
    
    
    public Cluster.Builder mergeInitialUser(UserPassword value)

Input only. Initial user to setup during cluster creation. Required. If used in `RestoreCluster` this is ignored.

` .google.cloud.alloydb.v1beta.UserPassword initial_user = 14 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[UserPassword](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.UserPassword)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### mergeMaintenanceSchedule(MaintenanceSchedule value)
    
    
    public Cluster.Builder mergeMaintenanceSchedule(MaintenanceSchedule value)

Output only. The maintenance schedule for the cluster, generated for a specific rollout if a maintenance window is set.

` .google.cloud.alloydb.v1beta.MaintenanceSchedule maintenance_schedule = 37 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MaintenanceSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.MaintenanceSchedule)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### mergeMaintenanceUpdatePolicy(MaintenanceUpdatePolicy value)
    
    
    public Cluster.Builder mergeMaintenanceUpdatePolicy(MaintenanceUpdatePolicy value)

Optional. The maintenance update policy determines when to allow or deny updates.

` .google.cloud.alloydb.v1beta.MaintenanceUpdatePolicy maintenance_update_policy = 32 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MaintenanceUpdatePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.MaintenanceUpdatePolicy)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### mergeMigrationSource(MigrationSource value)
    
    
    public Cluster.Builder mergeMigrationSource(MigrationSource value)

Output only. Cluster created via DMS migration.

` .google.cloud.alloydb.v1beta.MigrationSource migration_source = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MigrationSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.MigrationSource)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### mergeNetworkConfig(Cluster.NetworkConfig value)
    
    
    public Cluster.Builder mergeNetworkConfig(Cluster.NetworkConfig value)

` .google.cloud.alloydb.v1beta.Cluster.NetworkConfig network_config = 29 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Cluster.NetworkConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.NetworkConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### mergePrimaryConfig(Cluster.PrimaryConfig value)
    
    
    public Cluster.Builder mergePrimaryConfig(Cluster.PrimaryConfig value)

Output only. Cross Region replication config specific to PRIMARY cluster.

` .google.cloud.alloydb.v1beta.Cluster.PrimaryConfig primary_config = 23 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Cluster.PrimaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.PrimaryConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### mergePscConfig(Cluster.PscConfig value)
    
    
    public Cluster.Builder mergePscConfig(Cluster.PscConfig value)

Optional. The configuration for Private Service Connect (PSC) for the cluster.

` .google.cloud.alloydb.v1beta.Cluster.PscConfig psc_config = 31 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Cluster.PscConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.PscConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### mergeSecondaryConfig(Cluster.SecondaryConfig value)
    
    
    public Cluster.Builder mergeSecondaryConfig(Cluster.SecondaryConfig value)

Cross Region replication config specific to SECONDARY cluster.

`.google.cloud.alloydb.v1beta.Cluster.SecondaryConfig secondary_config = 22;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Cluster.SecondaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.SecondaryConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### mergeSslConfig(SslConfig value) (deprecated)
    
    
    public Cluster.Builder mergeSslConfig(SslConfig value)

SSL configuration for this AlloyDB cluster.

`.google.cloud.alloydb.v1beta.SslConfig ssl_config = 18 [deprecated = true];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SslConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.SslConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### mergeTrialMetadata(Cluster.TrialMetadata value)
    
    
    public Cluster.Builder mergeTrialMetadata(Cluster.TrialMetadata value)

Output only. Metadata for free trial clusters

` .google.cloud.alloydb.v1beta.Cluster.TrialMetadata trial_metadata = 39 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Cluster.TrialMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.TrialMetadata)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### mergeUpdateTime(Timestamp value)
    
    
    public Cluster.Builder mergeUpdateTime(Timestamp value)

Output only. Update time stamp

` .google.protobuf.Timestamp update_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### putAllAnnotations(Map<String,String> values)
    
    
    public Cluster.Builder putAllAnnotations(Map<String,String> values)

Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. <https://google.aip.dev/128>

`map<string, string> annotations = 12;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### putAllLabels(Map<String,String> values)
    
    
    public Cluster.Builder putAllLabels(Map<String,String> values)

Labels as key value pairs

`map<string, string> labels = 7;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### putAllTags(Map<String,String> values)
    
    
    public Cluster.Builder putAllTags(Map<String,String> values)

Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: `<code><code> "123/environment": "production", "123/costCenter": "marketing" </code></code>`

` map<string, string> tags = 41 [(.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### putAnnotations(String key, String value)
    
    
    public Cluster.Builder putAnnotations(String key, String value)

Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. <https://google.aip.dev/128>

`map<string, string> annotations = 12;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### putLabels(String key, String value)
    
    
    public Cluster.Builder putLabels(String key, String value)

Labels as key value pairs

`map<string, string> labels = 7;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### putTags(String key, String value)
    
    
    public Cluster.Builder putTags(String key, String value)

Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: `<code><code> "123/environment": "production", "123/costCenter": "marketing" </code></code>`

` map<string, string> tags = 41 [(.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### removeAnnotations(String key)
    
    
    public Cluster.Builder removeAnnotations(String key)

Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. <https://google.aip.dev/128>

`map<string, string> annotations = 12;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### removeLabels(String key)
    
    
    public Cluster.Builder removeLabels(String key)

Labels as key value pairs

`map<string, string> labels = 7;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### removeTags(String key)
    
    
    public Cluster.Builder removeTags(String key)

Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: `<code><code> "123/environment": "production", "123/costCenter": "marketing" </code></code>`

` map<string, string> tags = 41 [(.google.api.field_behavior) = INPUT_ONLY, (.google.api.field_behavior) = IMMUTABLE, (.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setAutomatedBackupPolicy(AutomatedBackupPolicy value)
    
    
    public Cluster.Builder setAutomatedBackupPolicy(AutomatedBackupPolicy value)

The automated backup policy for this cluster.

If no policy is provided then the default policy will be used. If backups are supported for the cluster, the default policy takes one backup a day, has a backup window of 1 hour, and retains backups for 14 days. For more information on the defaults, consult the documentation for the message type.

`.google.cloud.alloydb.v1beta.AutomatedBackupPolicy automated_backup_policy = 17;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AutomatedBackupPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.AutomatedBackupPolicy)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setAutomatedBackupPolicy(AutomatedBackupPolicy.Builder builderForValue)
    
    
    public Cluster.Builder setAutomatedBackupPolicy(AutomatedBackupPolicy.Builder builderForValue)

The automated backup policy for this cluster.

If no policy is provided then the default policy will be used. If backups are supported for the cluster, the default policy takes one backup a day, has a backup window of 1 hour, and retains backups for 14 days. For more information on the defaults, consult the documentation for the message type.

`.google.cloud.alloydb.v1beta.AutomatedBackupPolicy automated_backup_policy = 17;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[AutomatedBackupPolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.AutomatedBackupPolicy.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setBackupSource(BackupSource value)
    
    
    public Cluster.Builder setBackupSource(BackupSource value)

Output only. Cluster created from backup.

` .google.cloud.alloydb.v1beta.BackupSource backup_source = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BackupSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.BackupSource)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setBackupSource(BackupSource.Builder builderForValue)
    
    
    public Cluster.Builder setBackupSource(BackupSource.Builder builderForValue)

Output only. Cluster created from backup.

` .google.cloud.alloydb.v1beta.BackupSource backup_source = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[BackupSource.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.BackupSource.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setCloudsqlBackupRunSource(CloudSQLBackupRunSource value)
    
    
    public Cluster.Builder setCloudsqlBackupRunSource(CloudSQLBackupRunSource value)

Output only. Cluster created from CloudSQL snapshot.

` .google.cloud.alloydb.v1beta.CloudSQLBackupRunSource cloudsql_backup_run_source = 42 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CloudSQLBackupRunSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.CloudSQLBackupRunSource)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setCloudsqlBackupRunSource(CloudSQLBackupRunSource.Builder builderForValue)
    
    
    public Cluster.Builder setCloudsqlBackupRunSource(CloudSQLBackupRunSource.Builder builderForValue)

Output only. Cluster created from CloudSQL snapshot.

` .google.cloud.alloydb.v1beta.CloudSQLBackupRunSource cloudsql_backup_run_source = 42 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[CloudSQLBackupRunSource.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.CloudSQLBackupRunSource.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setClusterType(Cluster.ClusterType value)
    
    
    public Cluster.Builder setClusterType(Cluster.ClusterType value)

Output only. The type of the cluster. This is an output-only field and it's populated at the Cluster creation time or the Cluster promotion time. The cluster type is determined by which RPC was used to create the cluster (i.e. `CreateCluster` vs. `CreateSecondaryCluster`

` .google.cloud.alloydb.v1beta.Cluster.ClusterType cluster_type = 24 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Cluster.ClusterType](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.ClusterType)`  
The clusterType to set.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### setClusterTypeValue(int value)
    
    
    public Cluster.Builder setClusterTypeValue(int value)

Output only. The type of the cluster. This is an output-only field and it's populated at the Cluster creation time or the Cluster promotion time. The cluster type is determined by which RPC was used to create the cluster (i.e. `CreateCluster` vs. `CreateSecondaryCluster`

` .google.cloud.alloydb.v1beta.Cluster.ClusterType cluster_type = 24 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for clusterType to set.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### setContinuousBackupConfig(ContinuousBackupConfig value)
    
    
    public Cluster.Builder setContinuousBackupConfig(ContinuousBackupConfig value)

Optional. Continuous backup configuration for this cluster.

` .google.cloud.alloydb.v1beta.ContinuousBackupConfig continuous_backup_config = 27 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ContinuousBackupConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.ContinuousBackupConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setContinuousBackupConfig(ContinuousBackupConfig.Builder builderForValue)
    
    
    public Cluster.Builder setContinuousBackupConfig(ContinuousBackupConfig.Builder builderForValue)

Optional. Continuous backup configuration for this cluster.

` .google.cloud.alloydb.v1beta.ContinuousBackupConfig continuous_backup_config = 27 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ContinuousBackupConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.ContinuousBackupConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setContinuousBackupInfo(ContinuousBackupInfo value)
    
    
    public Cluster.Builder setContinuousBackupInfo(ContinuousBackupInfo value)

Output only. Continuous backup properties for this cluster.

` .google.cloud.alloydb.v1beta.ContinuousBackupInfo continuous_backup_info = 28 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ContinuousBackupInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.ContinuousBackupInfo)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setContinuousBackupInfo(ContinuousBackupInfo.Builder builderForValue)
    
    
    public Cluster.Builder setContinuousBackupInfo(ContinuousBackupInfo.Builder builderForValue)

Output only. Continuous backup properties for this cluster.

` .google.cloud.alloydb.v1beta.ContinuousBackupInfo continuous_backup_info = 28 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ContinuousBackupInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.ContinuousBackupInfo.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setCreateTime(Timestamp value)
    
    
    public Cluster.Builder setCreateTime(Timestamp value)

Output only. Create time stamp

` .google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setCreateTime(Timestamp.Builder builderForValue)
    
    
    public Cluster.Builder setCreateTime(Timestamp.Builder builderForValue)

Output only. Create time stamp

` .google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setDatabaseVersion(DatabaseVersion value)
    
    
    public Cluster.Builder setDatabaseVersion(DatabaseVersion value)

Optional. The database engine major version. This is an optional field and it is populated at the Cluster creation time. If a database version is not supplied at cluster creation time, then a default database version will be used.

` .google.cloud.alloydb.v1beta.DatabaseVersion database_version = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DatabaseVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.DatabaseVersion)`  
The databaseVersion to set.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### setDatabaseVersionValue(int value)
    
    
    public Cluster.Builder setDatabaseVersionValue(int value)

Optional. The database engine major version. This is an optional field and it is populated at the Cluster creation time. If a database version is not supplied at cluster creation time, then a default database version will be used.

` .google.cloud.alloydb.v1beta.DatabaseVersion database_version = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for databaseVersion to set.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### setDataplexConfig(Cluster.DataplexConfig value)
    
    
    public Cluster.Builder setDataplexConfig(Cluster.DataplexConfig value)

Optional. Configuration for Dataplex integration.

` .google.cloud.alloydb.v1beta.Cluster.DataplexConfig dataplex_config = 47 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Cluster.DataplexConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.DataplexConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setDataplexConfig(Cluster.DataplexConfig.Builder builderForValue)
    
    
    public Cluster.Builder setDataplexConfig(Cluster.DataplexConfig.Builder builderForValue)

Optional. Configuration for Dataplex integration.

` .google.cloud.alloydb.v1beta.Cluster.DataplexConfig dataplex_config = 47 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Cluster.DataplexConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.DataplexConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setDeleteTime(Timestamp value)
    
    
    public Cluster.Builder setDeleteTime(Timestamp value)

Output only. Delete time stamp

` .google.protobuf.Timestamp delete_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setDeleteTime(Timestamp.Builder builderForValue)
    
    
    public Cluster.Builder setDeleteTime(Timestamp.Builder builderForValue)

Output only. Delete time stamp

` .google.protobuf.Timestamp delete_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setDisplayName(String value)
    
    
    public Cluster.Builder setDisplayName(String value)

User-settable and human-readable display name for the Cluster.

`string display_name = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### setDisplayNameBytes(ByteString value)
    
    
    public Cluster.Builder setDisplayNameBytes(ByteString value)

User-settable and human-readable display name for the Cluster.

`string display_name = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### setEncryptionConfig(EncryptionConfig value)
    
    
    public Cluster.Builder setEncryptionConfig(EncryptionConfig value)

Optional. The encryption config can be specified to encrypt the data disks and other persistent data resources of a cluster with a customer-managed encryption key (CMEK). When this field is not specified, the cluster will then use default encryption scheme to protect the user data.

` .google.cloud.alloydb.v1beta.EncryptionConfig encryption_config = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[EncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.EncryptionConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setEncryptionConfig(EncryptionConfig.Builder builderForValue)
    
    
    public Cluster.Builder setEncryptionConfig(EncryptionConfig.Builder builderForValue)

Optional. The encryption config can be specified to encrypt the data disks and other persistent data resources of a cluster with a customer-managed encryption key (CMEK). When this field is not specified, the cluster will then use default encryption scheme to protect the user data.

` .google.cloud.alloydb.v1beta.EncryptionConfig encryption_config = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[EncryptionConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.EncryptionConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setEncryptionInfo(EncryptionInfo value)
    
    
    public Cluster.Builder setEncryptionInfo(EncryptionInfo value)

Output only. The encryption information for the cluster.

` .google.cloud.alloydb.v1beta.EncryptionInfo encryption_info = 20 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[EncryptionInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.EncryptionInfo)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setEncryptionInfo(EncryptionInfo.Builder builderForValue)
    
    
    public Cluster.Builder setEncryptionInfo(EncryptionInfo.Builder builderForValue)

Output only. The encryption information for the cluster.

` .google.cloud.alloydb.v1beta.EncryptionInfo encryption_info = 20 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[EncryptionInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.EncryptionInfo.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setEtag(String value)
    
    
    public Cluster.Builder setEtag(String value)

For Resource freshness validation (<https://google.aip.dev/154>)

`string etag = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The etag to set.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### setEtagBytes(ByteString value)
    
    
    public Cluster.Builder setEtagBytes(ByteString value)

For Resource freshness validation (<https://google.aip.dev/154>)

`string etag = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for etag to set.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### setGeminiConfig(GeminiClusterConfig value) (deprecated)
    
    
    public Cluster.Builder setGeminiConfig(GeminiClusterConfig value)

Optional. Deprecated and unused. This field will be removed in the near future.

` .google.cloud.alloydb.v1beta.GeminiClusterConfig gemini_config = 36 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[GeminiClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.GeminiClusterConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setGeminiConfig(GeminiClusterConfig.Builder builderForValue) (deprecated)
    
    
    public Cluster.Builder setGeminiConfig(GeminiClusterConfig.Builder builderForValue)

Optional. Deprecated and unused. This field will be removed in the near future.

` .google.cloud.alloydb.v1beta.GeminiClusterConfig gemini_config = 36 [deprecated = true, (.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[GeminiClusterConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.GeminiClusterConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setInitialUser(UserPassword value)
    
    
    public Cluster.Builder setInitialUser(UserPassword value)

Input only. Initial user to setup during cluster creation. Required. If used in `RestoreCluster` this is ignored.

` .google.cloud.alloydb.v1beta.UserPassword initial_user = 14 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[UserPassword](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.UserPassword)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setInitialUser(UserPassword.Builder builderForValue)
    
    
    public Cluster.Builder setInitialUser(UserPassword.Builder builderForValue)

Input only. Initial user to setup during cluster creation. Required. If used in `RestoreCluster` this is ignored.

` .google.cloud.alloydb.v1beta.UserPassword initial_user = 14 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[UserPassword.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.UserPassword.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setMaintenanceSchedule(MaintenanceSchedule value)
    
    
    public Cluster.Builder setMaintenanceSchedule(MaintenanceSchedule value)

Output only. The maintenance schedule for the cluster, generated for a specific rollout if a maintenance window is set.

` .google.cloud.alloydb.v1beta.MaintenanceSchedule maintenance_schedule = 37 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MaintenanceSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.MaintenanceSchedule)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setMaintenanceSchedule(MaintenanceSchedule.Builder builderForValue)
    
    
    public Cluster.Builder setMaintenanceSchedule(MaintenanceSchedule.Builder builderForValue)

Output only. The maintenance schedule for the cluster, generated for a specific rollout if a maintenance window is set.

` .google.cloud.alloydb.v1beta.MaintenanceSchedule maintenance_schedule = 37 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[MaintenanceSchedule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.MaintenanceSchedule.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setMaintenanceUpdatePolicy(MaintenanceUpdatePolicy value)
    
    
    public Cluster.Builder setMaintenanceUpdatePolicy(MaintenanceUpdatePolicy value)

Optional. The maintenance update policy determines when to allow or deny updates.

` .google.cloud.alloydb.v1beta.MaintenanceUpdatePolicy maintenance_update_policy = 32 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MaintenanceUpdatePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.MaintenanceUpdatePolicy)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setMaintenanceUpdatePolicy(MaintenanceUpdatePolicy.Builder builderForValue)
    
    
    public Cluster.Builder setMaintenanceUpdatePolicy(MaintenanceUpdatePolicy.Builder builderForValue)

Optional. The maintenance update policy determines when to allow or deny updates.

` .google.cloud.alloydb.v1beta.MaintenanceUpdatePolicy maintenance_update_policy = 32 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[MaintenanceUpdatePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.MaintenanceUpdatePolicy.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setMigrationSource(MigrationSource value)
    
    
    public Cluster.Builder setMigrationSource(MigrationSource value)

Output only. Cluster created via DMS migration.

` .google.cloud.alloydb.v1beta.MigrationSource migration_source = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MigrationSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.MigrationSource)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setMigrationSource(MigrationSource.Builder builderForValue)
    
    
    public Cluster.Builder setMigrationSource(MigrationSource.Builder builderForValue)

Output only. Cluster created via DMS migration.

` .google.cloud.alloydb.v1beta.MigrationSource migration_source = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[MigrationSource.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.MigrationSource.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setName(String value)
    
    
    public Cluster.Builder setName(String value)

Output only. The name of the cluster resource with the format:

  * projects/{project}/locations/{region}/clusters/{cluster_id} where the cluster ID segment should satisfy the regex expression `[a-z0-9-]+`. For more details see <https://google.aip.dev/122>. The prefix of the cluster resource name is the name of the parent resource:
  * projects/{project}/locations/{region}



`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public Cluster.Builder setNameBytes(ByteString value)

Output only. The name of the cluster resource with the format:

  * projects/{project}/locations/{region}/clusters/{cluster_id} where the cluster ID segment should satisfy the regex expression `[a-z0-9-]+`. For more details see <https://google.aip.dev/122>. The prefix of the cluster resource name is the name of the parent resource:
  * projects/{project}/locations/{region}



`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### setNetwork(String value) (deprecated)
    
    
    public Cluster.Builder setNetwork(String value)

**Deprecated.** _google.cloud.alloydb.v1beta.Cluster.network is deprecated. See google/cloud/alloydb/v1beta/resources.proto;l=689_

Required. The resource link for the VPC network in which cluster resources are created and from which they are accessible via Private IP. The network must belong to the same project as the cluster. It is specified in the form: `projects/{project}/global/networks/{network_id}`. This is required to create a cluster. Deprecated, use network_config.network instead.

` string network = 10 [deprecated = true, (.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The network to set.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### setNetworkBytes(ByteString value) (deprecated)
    
    
    public Cluster.Builder setNetworkBytes(ByteString value)

**Deprecated.** _google.cloud.alloydb.v1beta.Cluster.network is deprecated. See google/cloud/alloydb/v1beta/resources.proto;l=689_

Required. The resource link for the VPC network in which cluster resources are created and from which they are accessible via Private IP. The network must belong to the same project as the cluster. It is specified in the form: `projects/{project}/global/networks/{network_id}`. This is required to create a cluster. Deprecated, use network_config.network instead.

` string network = 10 [deprecated = true, (.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for network to set.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### setNetworkConfig(Cluster.NetworkConfig value)
    
    
    public Cluster.Builder setNetworkConfig(Cluster.NetworkConfig value)

` .google.cloud.alloydb.v1beta.Cluster.NetworkConfig network_config = 29 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Cluster.NetworkConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.NetworkConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setNetworkConfig(Cluster.NetworkConfig.Builder builderForValue)
    
    
    public Cluster.Builder setNetworkConfig(Cluster.NetworkConfig.Builder builderForValue)

` .google.cloud.alloydb.v1beta.Cluster.NetworkConfig network_config = 29 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Cluster.NetworkConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.NetworkConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setPrimaryConfig(Cluster.PrimaryConfig value)
    
    
    public Cluster.Builder setPrimaryConfig(Cluster.PrimaryConfig value)

Output only. Cross Region replication config specific to PRIMARY cluster.

` .google.cloud.alloydb.v1beta.Cluster.PrimaryConfig primary_config = 23 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Cluster.PrimaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.PrimaryConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setPrimaryConfig(Cluster.PrimaryConfig.Builder builderForValue)
    
    
    public Cluster.Builder setPrimaryConfig(Cluster.PrimaryConfig.Builder builderForValue)

Output only. Cross Region replication config specific to PRIMARY cluster.

` .google.cloud.alloydb.v1beta.Cluster.PrimaryConfig primary_config = 23 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Cluster.PrimaryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.PrimaryConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setPscConfig(Cluster.PscConfig value)
    
    
    public Cluster.Builder setPscConfig(Cluster.PscConfig value)

Optional. The configuration for Private Service Connect (PSC) for the cluster.

` .google.cloud.alloydb.v1beta.Cluster.PscConfig psc_config = 31 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Cluster.PscConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.PscConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setPscConfig(Cluster.PscConfig.Builder builderForValue)
    
    
    public Cluster.Builder setPscConfig(Cluster.PscConfig.Builder builderForValue)

Optional. The configuration for Private Service Connect (PSC) for the cluster.

` .google.cloud.alloydb.v1beta.Cluster.PscConfig psc_config = 31 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Cluster.PscConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.PscConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setReconciling(boolean value)
    
    
    public Cluster.Builder setReconciling(boolean value)

Output only. Reconciling (<https://google.aip.dev/128#reconciliation>). Set to true if the current state of Cluster does not match the user's intended state, and the service is actively updating the resource to reconcile them. This can happen due to user-triggered updates or system actions like failover or maintenance.

`bool reconciling = 13 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The reconciling to set.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### setSatisfiesPzs(boolean value)
    
    
    public Cluster.Builder setSatisfiesPzs(boolean value)

Output only. Reserved for future use.

`bool satisfies_pzs = 30 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The satisfiesPzs to set.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### setSecondaryConfig(Cluster.SecondaryConfig value)
    
    
    public Cluster.Builder setSecondaryConfig(Cluster.SecondaryConfig value)

Cross Region replication config specific to SECONDARY cluster.

`.google.cloud.alloydb.v1beta.Cluster.SecondaryConfig secondary_config = 22;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Cluster.SecondaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.SecondaryConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setSecondaryConfig(Cluster.SecondaryConfig.Builder builderForValue)
    
    
    public Cluster.Builder setSecondaryConfig(Cluster.SecondaryConfig.Builder builderForValue)

Cross Region replication config specific to SECONDARY cluster.

`.google.cloud.alloydb.v1beta.Cluster.SecondaryConfig secondary_config = 22;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Cluster.SecondaryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.SecondaryConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setServiceAccountEmail(String value)
    
    
    public Cluster.Builder setServiceAccountEmail(String value)

Output only. AlloyDB per-cluster service account. This service account is created per-cluster per-project, and is different from the per-project service account. The per-cluster service account naming format is subject to change.

`string service_account_email = 46 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The serviceAccountEmail to set.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### setServiceAccountEmailBytes(ByteString value)
    
    
    public Cluster.Builder setServiceAccountEmailBytes(ByteString value)

Output only. AlloyDB per-cluster service account. This service account is created per-cluster per-project, and is different from the per-project service account. The per-cluster service account naming format is subject to change.

`string service_account_email = 46 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for serviceAccountEmail to set.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### setSslConfig(SslConfig value) (deprecated)
    
    
    public Cluster.Builder setSslConfig(SslConfig value)

SSL configuration for this AlloyDB cluster.

`.google.cloud.alloydb.v1beta.SslConfig ssl_config = 18 [deprecated = true];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SslConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.SslConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setSslConfig(SslConfig.Builder builderForValue) (deprecated)
    
    
    public Cluster.Builder setSslConfig(SslConfig.Builder builderForValue)

SSL configuration for this AlloyDB cluster.

`.google.cloud.alloydb.v1beta.SslConfig ssl_config = 18 [deprecated = true];`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SslConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.SslConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setState(Cluster.State value)
    
    
    public Cluster.Builder setState(Cluster.State value)

Output only. The current serving state of the cluster.

` .google.cloud.alloydb.v1beta.Cluster.State state = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Cluster.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.State)`  
The state to set.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### setStateValue(int value)
    
    
    public Cluster.Builder setStateValue(int value)

Output only. The current serving state of the cluster.

` .google.cloud.alloydb.v1beta.Cluster.State state = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for state to set.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### setSubscriptionType(SubscriptionType value)
    
    
    public Cluster.Builder setSubscriptionType(SubscriptionType value)

Optional. Subscription type of the cluster.

` .google.cloud.alloydb.v1beta.SubscriptionType subscription_type = 38 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SubscriptionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.SubscriptionType)`  
The subscriptionType to set.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### setSubscriptionTypeValue(int value)
    
    
    public Cluster.Builder setSubscriptionTypeValue(int value)

Optional. Subscription type of the cluster.

` .google.cloud.alloydb.v1beta.SubscriptionType subscription_type = 38 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for subscriptionType to set.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### setTrialMetadata(Cluster.TrialMetadata value)
    
    
    public Cluster.Builder setTrialMetadata(Cluster.TrialMetadata value)

Output only. Metadata for free trial clusters

` .google.cloud.alloydb.v1beta.Cluster.TrialMetadata trial_metadata = 39 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Cluster.TrialMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.TrialMetadata)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setTrialMetadata(Cluster.TrialMetadata.Builder builderForValue)
    
    
    public Cluster.Builder setTrialMetadata(Cluster.TrialMetadata.Builder builderForValue)

Output only. Metadata for free trial clusters

` .google.cloud.alloydb.v1beta.Cluster.TrialMetadata trial_metadata = 39 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Cluster.TrialMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.TrialMetadata.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setUid(String value)
    
    
    public Cluster.Builder setUid(String value)

Output only. The system-generated UID of the resource. The UID is assigned when the resource is created, and it is retained until it is deleted.

`string uid = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The uid to set.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### setUidBytes(ByteString value)
    
    
    public Cluster.Builder setUidBytes(ByteString value)

Output only. The system-generated UID of the resource. The UID is assigned when the resource is created, and it is retained until it is deleted.

`string uid = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for uid to set.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` | This builder for chaining.  
  
### setUpdateTime(Timestamp value)
    
    
    public Cluster.Builder setUpdateTime(Timestamp value)

Output only. Update time stamp

` .google.protobuf.Timestamp update_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
### setUpdateTime(Timestamp.Builder builderForValue)
    
    
    public Cluster.Builder setUpdateTime(Timestamp.Builder builderForValue)

Output only. Update time stamp

` .google.protobuf.Timestamp update_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Cluster.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1beta.Cluster.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
