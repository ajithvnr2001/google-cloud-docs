---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder
title: Class SupportedDatabaseFlag.Builder (0.88.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:09.405624+00:00
---

# Class SupportedDatabaseFlag.Builder (0.88.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SupportedDatabaseFlag.Builder (0.88.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.88.0 (latest)  0.84.0  0.83.0  0.82.0  0.80.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.63.0  0.62.0  0.61.0  0.59.0  0.57.0  0.56.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class SupportedDatabaseFlag.Builder extends GeneratedMessage.Builder<SupportedDatabaseFlag.Builder> implements SupportedDatabaseFlagOrBuilder

SupportedDatabaseFlag gives general information about a database flag, like type and allowed values. This is a static value that is defined on the server side, and it cannot be modified by callers. To set the Database flags on a particular Instance, a caller should modify the Instance.database_flags field.

Protobuf type `google.cloud.alloydb.v1.SupportedDatabaseFlag`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > SupportedDatabaseFlag.Builder

## Implements

[SupportedDatabaseFlagOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlagOrBuilder)

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

### addAllSupportedDbVersions(Iterable<? extends DatabaseVersion> values)
    
    
    public SupportedDatabaseFlag.Builder addAllSupportedDbVersions(Iterable<? extends DatabaseVersion> values)

Major database engine versions for which this flag is supported.

`repeated .google.cloud.alloydb.v1.DatabaseVersion supported_db_versions = 5;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.alloydb.v1.DatabaseVersion>`  
The supportedDbVersions to add.  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### addAllSupportedDbVersionsValue(Iterable<Integer> values)
    
    
    public SupportedDatabaseFlag.Builder addAllSupportedDbVersionsValue(Iterable<Integer> values)

Major database engine versions for which this flag is supported.

`repeated .google.cloud.alloydb.v1.DatabaseVersion supported_db_versions = 5;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>`  
The enum numeric values on the wire for supportedDbVersions to add.  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### addSupportedDbVersions(DatabaseVersion value)
    
    
    public SupportedDatabaseFlag.Builder addSupportedDbVersions(DatabaseVersion value)

Major database engine versions for which this flag is supported.

`repeated .google.cloud.alloydb.v1.DatabaseVersion supported_db_versions = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DatabaseVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.DatabaseVersion)`  
The supportedDbVersions to add.  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### addSupportedDbVersionsValue(int value)
    
    
    public SupportedDatabaseFlag.Builder addSupportedDbVersionsValue(int value)

Major database engine versions for which this flag is supported.

`repeated .google.cloud.alloydb.v1.DatabaseVersion supported_db_versions = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for supportedDbVersions to add.  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### build()
    
    
    public SupportedDatabaseFlag build()

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag)` |   
  
### buildPartial()
    
    
    public SupportedDatabaseFlag buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag)` |   
  
### clear()
    
    
    public SupportedDatabaseFlag.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearAcceptsMultipleValues()
    
    
    public SupportedDatabaseFlag.Builder clearAcceptsMultipleValues()

Whether the database flag accepts multiple values. If true, a comma-separated list of stringified values may be specified.

`bool accepts_multiple_values = 4;`

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### clearFlagName()
    
    
    public SupportedDatabaseFlag.Builder clearFlagName()

The name of the database flag, e.g. "max_allowed_packets". The is a possibly key for the Instance.database_flags map field.

`string flag_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### clearIntegerRestrictions()
    
    
    public SupportedDatabaseFlag.Builder clearIntegerRestrictions()

Restriction on INTEGER type value.

` .google.cloud.alloydb.v1.SupportedDatabaseFlag.IntegerRestrictions integer_restrictions = 8; `

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` |   
  
### clearName()
    
    
    public SupportedDatabaseFlag.Builder clearName()

The name of the flag resource, following Google Cloud conventions, e.g.:

  * projects/{project}/locations/{location}/flags/{flag} This field currently has no semantic meaning.



`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### clearRecommendedIntegerValue()
    
    
    public SupportedDatabaseFlag.Builder clearRecommendedIntegerValue()

The recommended value for an INTEGER flag.

`.google.protobuf.Int64Value recommended_integer_value = 11;`

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` |   
  
### clearRecommendedStringValue()
    
    
    public SupportedDatabaseFlag.Builder clearRecommendedStringValue()

The recommended value for a STRING flag.

`string recommended_string_value = 10;`

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### clearRecommendedValue()
    
    
    public SupportedDatabaseFlag.Builder clearRecommendedValue()

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` |   
  
### clearRequiresDbRestart()
    
    
    public SupportedDatabaseFlag.Builder clearRequiresDbRestart()

Whether setting or updating this flag on an Instance requires a database restart. If a flag that requires database restart is set, the backend will automatically restart the database (making sure to satisfy any availability SLO's).

`bool requires_db_restart = 6;`

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### clearRestrictions()
    
    
    public SupportedDatabaseFlag.Builder clearRestrictions()

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` |   
  
### clearScope()
    
    
    public SupportedDatabaseFlag.Builder clearScope()

The scope of the flag.

`.google.cloud.alloydb.v1.SupportedDatabaseFlag.Scope scope = 9;`

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### clearStringRestrictions()
    
    
    public SupportedDatabaseFlag.Builder clearStringRestrictions()

Restriction on STRING type value.

` .google.cloud.alloydb.v1.SupportedDatabaseFlag.StringRestrictions string_restrictions = 7; `

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` |   
  
### clearSupportedDbVersions()
    
    
    public SupportedDatabaseFlag.Builder clearSupportedDbVersions()

Major database engine versions for which this flag is supported.

`repeated .google.cloud.alloydb.v1.DatabaseVersion supported_db_versions = 5;`

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### clearValueType()
    
    
    public SupportedDatabaseFlag.Builder clearValueType()

`.google.cloud.alloydb.v1.SupportedDatabaseFlag.ValueType value_type = 3;`

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### getAcceptsMultipleValues()
    
    
    public boolean getAcceptsMultipleValues()

Whether the database flag accepts multiple values. If true, a comma-separated list of stringified values may be specified.

`bool accepts_multiple_values = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The acceptsMultipleValues.  
  
### getDefaultInstanceForType()
    
    
    public SupportedDatabaseFlag getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getFlagName()
    
    
    public String getFlagName()

The name of the database flag, e.g. "max_allowed_packets". The is a possibly key for the Instance.database_flags map field.

`string flag_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The flagName.  
  
### getFlagNameBytes()
    
    
    public ByteString getFlagNameBytes()

The name of the database flag, e.g. "max_allowed_packets". The is a possibly key for the Instance.database_flags map field.

`string flag_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for flagName.  
  
### getIntegerRestrictions()
    
    
    public SupportedDatabaseFlag.IntegerRestrictions getIntegerRestrictions()

Restriction on INTEGER type value.

` .google.cloud.alloydb.v1.SupportedDatabaseFlag.IntegerRestrictions integer_restrictions = 8; `

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.IntegerRestrictions](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.IntegerRestrictions)` | The integerRestrictions.  
  
### getIntegerRestrictionsBuilder()
    
    
    public SupportedDatabaseFlag.IntegerRestrictions.Builder getIntegerRestrictionsBuilder()

Restriction on INTEGER type value.

` .google.cloud.alloydb.v1.SupportedDatabaseFlag.IntegerRestrictions integer_restrictions = 8; `

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.IntegerRestrictions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.IntegerRestrictions.Builder)` |   
  
### getIntegerRestrictionsOrBuilder()
    
    
    public SupportedDatabaseFlag.IntegerRestrictionsOrBuilder getIntegerRestrictionsOrBuilder()

Restriction on INTEGER type value.

` .google.cloud.alloydb.v1.SupportedDatabaseFlag.IntegerRestrictions integer_restrictions = 8; `

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.IntegerRestrictionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.IntegerRestrictionsOrBuilder)` |   
  
### getName()
    
    
    public String getName()

The name of the flag resource, following Google Cloud conventions, e.g.:

  * projects/{project}/locations/{location}/flags/{flag} This field currently has no semantic meaning.



`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

The name of the flag resource, following Google Cloud conventions, e.g.:

  * projects/{project}/locations/{location}/flags/{flag} This field currently has no semantic meaning.



`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getRecommendedIntegerValue()
    
    
    public Int64Value getRecommendedIntegerValue()

The recommended value for an INTEGER flag.

`.google.protobuf.Int64Value recommended_integer_value = 11;`

**Returns**  
---  
**Type** | **Description**  
`[Int64Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64Value.html)` | The recommendedIntegerValue.  
  
### getRecommendedIntegerValueBuilder()
    
    
    public Int64Value.Builder getRecommendedIntegerValueBuilder()

The recommended value for an INTEGER flag.

`.google.protobuf.Int64Value recommended_integer_value = 11;`

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64Value.Builder.html)` |   
  
### getRecommendedIntegerValueOrBuilder()
    
    
    public Int64ValueOrBuilder getRecommendedIntegerValueOrBuilder()

The recommended value for an INTEGER flag.

`.google.protobuf.Int64Value recommended_integer_value = 11;`

**Returns**  
---  
**Type** | **Description**  
`[Int64ValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64ValueOrBuilder.html)` |   
  
### getRecommendedStringValue()
    
    
    public String getRecommendedStringValue()

The recommended value for a STRING flag.

`string recommended_string_value = 10;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The recommendedStringValue.  
  
### getRecommendedStringValueBytes()
    
    
    public ByteString getRecommendedStringValueBytes()

The recommended value for a STRING flag.

`string recommended_string_value = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for recommendedStringValue.  
  
### getRecommendedValueCase()
    
    
    public SupportedDatabaseFlag.RecommendedValueCase getRecommendedValueCase()

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.RecommendedValueCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.RecommendedValueCase)` |   
  
### getRequiresDbRestart()
    
    
    public boolean getRequiresDbRestart()

Whether setting or updating this flag on an Instance requires a database restart. If a flag that requires database restart is set, the backend will automatically restart the database (making sure to satisfy any availability SLO's).

`bool requires_db_restart = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The requiresDbRestart.  
  
### getRestrictionsCase()
    
    
    public SupportedDatabaseFlag.RestrictionsCase getRestrictionsCase()

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.RestrictionsCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.RestrictionsCase)` |   
  
### getScope()
    
    
    public SupportedDatabaseFlag.Scope getScope()

The scope of the flag.

`.google.cloud.alloydb.v1.SupportedDatabaseFlag.Scope scope = 9;`

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Scope](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Scope)` | The scope.  
  
### getScopeValue()
    
    
    public int getScopeValue()

The scope of the flag.

`.google.cloud.alloydb.v1.SupportedDatabaseFlag.Scope scope = 9;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for scope.  
  
### getStringRestrictions()
    
    
    public SupportedDatabaseFlag.StringRestrictions getStringRestrictions()

Restriction on STRING type value.

` .google.cloud.alloydb.v1.SupportedDatabaseFlag.StringRestrictions string_restrictions = 7; `

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.StringRestrictions](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.StringRestrictions)` | The stringRestrictions.  
  
### getStringRestrictionsBuilder()
    
    
    public SupportedDatabaseFlag.StringRestrictions.Builder getStringRestrictionsBuilder()

Restriction on STRING type value.

` .google.cloud.alloydb.v1.SupportedDatabaseFlag.StringRestrictions string_restrictions = 7; `

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.StringRestrictions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.StringRestrictions.Builder)` |   
  
### getStringRestrictionsOrBuilder()
    
    
    public SupportedDatabaseFlag.StringRestrictionsOrBuilder getStringRestrictionsOrBuilder()

Restriction on STRING type value.

` .google.cloud.alloydb.v1.SupportedDatabaseFlag.StringRestrictions string_restrictions = 7; `

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.StringRestrictionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.StringRestrictionsOrBuilder)` |   
  
### getSupportedDbVersions(int index)
    
    
    public DatabaseVersion getSupportedDbVersions(int index)

Major database engine versions for which this flag is supported.

`repeated .google.cloud.alloydb.v1.DatabaseVersion supported_db_versions = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[DatabaseVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.DatabaseVersion)` | The supportedDbVersions at the given index.  
  
### getSupportedDbVersionsCount()
    
    
    public int getSupportedDbVersionsCount()

Major database engine versions for which this flag is supported.

`repeated .google.cloud.alloydb.v1.DatabaseVersion supported_db_versions = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of supportedDbVersions.  
  
### getSupportedDbVersionsList()
    
    
    public List<DatabaseVersion> getSupportedDbVersionsList()

Major database engine versions for which this flag is supported.

`repeated .google.cloud.alloydb.v1.DatabaseVersion supported_db_versions = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[DatabaseVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.DatabaseVersion)>` | A list containing the supportedDbVersions.  
  
### getSupportedDbVersionsValue(int index)
    
    
    public int getSupportedDbVersionsValue(int index)

Major database engine versions for which this flag is supported.

`repeated .google.cloud.alloydb.v1.DatabaseVersion supported_db_versions = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of supportedDbVersions at the given index.  
  
### getSupportedDbVersionsValueList()
    
    
    public List<Integer> getSupportedDbVersionsValueList()

Major database engine versions for which this flag is supported.

`repeated .google.cloud.alloydb.v1.DatabaseVersion supported_db_versions = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for supportedDbVersions.  
  
### getValueType()
    
    
    public SupportedDatabaseFlag.ValueType getValueType()

`.google.cloud.alloydb.v1.SupportedDatabaseFlag.ValueType value_type = 3;`

**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.ValueType](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.ValueType)` | The valueType.  
  
### getValueTypeValue()
    
    
    public int getValueTypeValue()

`.google.cloud.alloydb.v1.SupportedDatabaseFlag.ValueType value_type = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for valueType.  
  
### hasIntegerRestrictions()
    
    
    public boolean hasIntegerRestrictions()

Restriction on INTEGER type value.

` .google.cloud.alloydb.v1.SupportedDatabaseFlag.IntegerRestrictions integer_restrictions = 8; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the integerRestrictions field is set.  
  
### hasRecommendedIntegerValue()
    
    
    public boolean hasRecommendedIntegerValue()

The recommended value for an INTEGER flag.

`.google.protobuf.Int64Value recommended_integer_value = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the recommendedIntegerValue field is set.  
  
### hasRecommendedStringValue()
    
    
    public boolean hasRecommendedStringValue()

The recommended value for a STRING flag.

`string recommended_string_value = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the recommendedStringValue field is set.  
  
### hasStringRestrictions()
    
    
    public boolean hasStringRestrictions()

Restriction on STRING type value.

` .google.cloud.alloydb.v1.SupportedDatabaseFlag.StringRestrictions string_restrictions = 7; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the stringRestrictions field is set.  
  
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

### mergeFrom(SupportedDatabaseFlag other)
    
    
    public SupportedDatabaseFlag.Builder mergeFrom(SupportedDatabaseFlag other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SupportedDatabaseFlag](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public SupportedDatabaseFlag.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public SupportedDatabaseFlag.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeIntegerRestrictions(SupportedDatabaseFlag.IntegerRestrictions value)
    
    
    public SupportedDatabaseFlag.Builder mergeIntegerRestrictions(SupportedDatabaseFlag.IntegerRestrictions value)

Restriction on INTEGER type value.

` .google.cloud.alloydb.v1.SupportedDatabaseFlag.IntegerRestrictions integer_restrictions = 8; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SupportedDatabaseFlag.IntegerRestrictions](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.IntegerRestrictions)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` |   
  
### mergeRecommendedIntegerValue(Int64Value value)
    
    
    public SupportedDatabaseFlag.Builder mergeRecommendedIntegerValue(Int64Value value)

The recommended value for an INTEGER flag.

`.google.protobuf.Int64Value recommended_integer_value = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Int64Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64Value.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` |   
  
### mergeStringRestrictions(SupportedDatabaseFlag.StringRestrictions value)
    
    
    public SupportedDatabaseFlag.Builder mergeStringRestrictions(SupportedDatabaseFlag.StringRestrictions value)

Restriction on STRING type value.

` .google.cloud.alloydb.v1.SupportedDatabaseFlag.StringRestrictions string_restrictions = 7; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SupportedDatabaseFlag.StringRestrictions](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.StringRestrictions)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` |   
  
### setAcceptsMultipleValues(boolean value)
    
    
    public SupportedDatabaseFlag.Builder setAcceptsMultipleValues(boolean value)

Whether the database flag accepts multiple values. If true, a comma-separated list of stringified values may be specified.

`bool accepts_multiple_values = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The acceptsMultipleValues to set.  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### setFlagName(String value)
    
    
    public SupportedDatabaseFlag.Builder setFlagName(String value)

The name of the database flag, e.g. "max_allowed_packets". The is a possibly key for the Instance.database_flags map field.

`string flag_name = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The flagName to set.  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### setFlagNameBytes(ByteString value)
    
    
    public SupportedDatabaseFlag.Builder setFlagNameBytes(ByteString value)

The name of the database flag, e.g. "max_allowed_packets". The is a possibly key for the Instance.database_flags map field.

`string flag_name = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for flagName to set.  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### setIntegerRestrictions(SupportedDatabaseFlag.IntegerRestrictions value)
    
    
    public SupportedDatabaseFlag.Builder setIntegerRestrictions(SupportedDatabaseFlag.IntegerRestrictions value)

Restriction on INTEGER type value.

` .google.cloud.alloydb.v1.SupportedDatabaseFlag.IntegerRestrictions integer_restrictions = 8; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SupportedDatabaseFlag.IntegerRestrictions](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.IntegerRestrictions)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` |   
  
### setIntegerRestrictions(SupportedDatabaseFlag.IntegerRestrictions.Builder builderForValue)
    
    
    public SupportedDatabaseFlag.Builder setIntegerRestrictions(SupportedDatabaseFlag.IntegerRestrictions.Builder builderForValue)

Restriction on INTEGER type value.

` .google.cloud.alloydb.v1.SupportedDatabaseFlag.IntegerRestrictions integer_restrictions = 8; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SupportedDatabaseFlag.IntegerRestrictions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.IntegerRestrictions.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` |   
  
### setName(String value)
    
    
    public SupportedDatabaseFlag.Builder setName(String value)

The name of the flag resource, following Google Cloud conventions, e.g.:

  * projects/{project}/locations/{location}/flags/{flag} This field currently has no semantic meaning.



`string name = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public SupportedDatabaseFlag.Builder setNameBytes(ByteString value)

The name of the flag resource, following Google Cloud conventions, e.g.:

  * projects/{project}/locations/{location}/flags/{flag} This field currently has no semantic meaning.



`string name = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### setRecommendedIntegerValue(Int64Value value)
    
    
    public SupportedDatabaseFlag.Builder setRecommendedIntegerValue(Int64Value value)

The recommended value for an INTEGER flag.

`.google.protobuf.Int64Value recommended_integer_value = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Int64Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64Value.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` |   
  
### setRecommendedIntegerValue(Int64Value.Builder builderForValue)
    
    
    public SupportedDatabaseFlag.Builder setRecommendedIntegerValue(Int64Value.Builder builderForValue)

The recommended value for an INTEGER flag.

`.google.protobuf.Int64Value recommended_integer_value = 11;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64Value.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` |   
  
### setRecommendedStringValue(String value)
    
    
    public SupportedDatabaseFlag.Builder setRecommendedStringValue(String value)

The recommended value for a STRING flag.

`string recommended_string_value = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The recommendedStringValue to set.  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### setRecommendedStringValueBytes(ByteString value)
    
    
    public SupportedDatabaseFlag.Builder setRecommendedStringValueBytes(ByteString value)

The recommended value for a STRING flag.

`string recommended_string_value = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for recommendedStringValue to set.  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### setRequiresDbRestart(boolean value)
    
    
    public SupportedDatabaseFlag.Builder setRequiresDbRestart(boolean value)

Whether setting or updating this flag on an Instance requires a database restart. If a flag that requires database restart is set, the backend will automatically restart the database (making sure to satisfy any availability SLO's).

`bool requires_db_restart = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The requiresDbRestart to set.  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### setScope(SupportedDatabaseFlag.Scope value)
    
    
    public SupportedDatabaseFlag.Builder setScope(SupportedDatabaseFlag.Scope value)

The scope of the flag.

`.google.cloud.alloydb.v1.SupportedDatabaseFlag.Scope scope = 9;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SupportedDatabaseFlag.Scope](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Scope)`  
The scope to set.  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### setScopeValue(int value)
    
    
    public SupportedDatabaseFlag.Builder setScopeValue(int value)

The scope of the flag.

`.google.cloud.alloydb.v1.SupportedDatabaseFlag.Scope scope = 9;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for scope to set.  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### setStringRestrictions(SupportedDatabaseFlag.StringRestrictions value)
    
    
    public SupportedDatabaseFlag.Builder setStringRestrictions(SupportedDatabaseFlag.StringRestrictions value)

Restriction on STRING type value.

` .google.cloud.alloydb.v1.SupportedDatabaseFlag.StringRestrictions string_restrictions = 7; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SupportedDatabaseFlag.StringRestrictions](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.StringRestrictions)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` |   
  
### setStringRestrictions(SupportedDatabaseFlag.StringRestrictions.Builder builderForValue)
    
    
    public SupportedDatabaseFlag.Builder setStringRestrictions(SupportedDatabaseFlag.StringRestrictions.Builder builderForValue)

Restriction on STRING type value.

` .google.cloud.alloydb.v1.SupportedDatabaseFlag.StringRestrictions string_restrictions = 7; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SupportedDatabaseFlag.StringRestrictions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.StringRestrictions.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` |   
  
### setSupportedDbVersions(int index, DatabaseVersion value)
    
    
    public SupportedDatabaseFlag.Builder setSupportedDbVersions(int index, DatabaseVersion value)

Major database engine versions for which this flag is supported.

`repeated .google.cloud.alloydb.v1.DatabaseVersion supported_db_versions = 5;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[DatabaseVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.DatabaseVersion)`  
The supportedDbVersions to set.  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### setSupportedDbVersionsValue(int index, int value)
    
    
    public SupportedDatabaseFlag.Builder setSupportedDbVersionsValue(int index, int value)

Major database engine versions for which this flag is supported.

`repeated .google.cloud.alloydb.v1.DatabaseVersion supported_db_versions = 5;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for supportedDbVersions to set.  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### setValueType(SupportedDatabaseFlag.ValueType value)
    
    
    public SupportedDatabaseFlag.Builder setValueType(SupportedDatabaseFlag.ValueType value)

`.google.cloud.alloydb.v1.SupportedDatabaseFlag.ValueType value_type = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SupportedDatabaseFlag.ValueType](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.ValueType)`  
The valueType to set.  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
### setValueTypeValue(int value)
    
    
    public SupportedDatabaseFlag.Builder setValueTypeValue(int value)

`.google.cloud.alloydb.v1.SupportedDatabaseFlag.ValueType value_type = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for valueType to set.  
**Returns**  
---  
**Type** | **Description**  
`[SupportedDatabaseFlag.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.SupportedDatabaseFlag.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
