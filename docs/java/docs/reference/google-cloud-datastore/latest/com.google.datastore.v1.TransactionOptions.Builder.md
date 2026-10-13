---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.Builder
title: Class TransactionOptions.Builder (3.7.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:47:00.056415+00:00
---

# Class TransactionOptions.Builder (3.7.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TransactionOptions.Builder (3.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.7.0 (latest)  3.3.0  3.2.0  3.1.0  2.40.0  2.37.0  2.36.0  2.34.0  2.33.3  2.32.3  2.31.4  2.30.0  2.29.1  2.28.2  2.27.1  2.26.4  2.25.2  2.24.3  2.23.0  2.22.0  2.21.3  2.20.2  2.19.2  2.18.5  2.17.6 
    
    
    public static final class TransactionOptions.Builder extends GeneratedMessage.Builder<TransactionOptions.Builder> implements TransactionOptionsOrBuilder

Options for beginning a new transaction.

Transactions can be created explicitly with calls to Datastore.BeginTransaction or implicitly by setting ReadOptions.new_transaction in read requests.

Protobuf type `google.datastore.v1.TransactionOptions`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > TransactionOptions.Builder

## Implements

[TransactionOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptionsOrBuilder)

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
    
    
    public TransactionOptions build()

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions)` |   
  
### buildPartial()
    
    
    public TransactionOptions buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions)` |   
  
### clear()
    
    
    public TransactionOptions.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearMode()
    
    
    public TransactionOptions.Builder clearMode()

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.Builder)` |   
  
### clearReadOnly()
    
    
    public TransactionOptions.Builder clearReadOnly()

The transaction should only allow reads.

`.google.datastore.v1.TransactionOptions.ReadOnly read_only = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.Builder)` |   
  
### clearReadWrite()
    
    
    public TransactionOptions.Builder clearReadWrite()

The transaction should allow both reads and writes.

`.google.datastore.v1.TransactionOptions.ReadWrite read_write = 1;`

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.Builder)` |   
  
### getDefaultInstanceForType()
    
    
    public TransactionOptions getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getModeCase()
    
    
    public TransactionOptions.ModeCase getModeCase()

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.ModeCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.ModeCase)` |   
  
### getReadOnly()
    
    
    public TransactionOptions.ReadOnly getReadOnly()

The transaction should only allow reads.

`.google.datastore.v1.TransactionOptions.ReadOnly read_only = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.ReadOnly](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.ReadOnly)` | The readOnly.  
  
### getReadOnlyBuilder()
    
    
    public TransactionOptions.ReadOnly.Builder getReadOnlyBuilder()

The transaction should only allow reads.

`.google.datastore.v1.TransactionOptions.ReadOnly read_only = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.ReadOnly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.ReadOnly.Builder)` |   
  
### getReadOnlyOrBuilder()
    
    
    public TransactionOptions.ReadOnlyOrBuilder getReadOnlyOrBuilder()

The transaction should only allow reads.

`.google.datastore.v1.TransactionOptions.ReadOnly read_only = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.ReadOnlyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.ReadOnlyOrBuilder)` |   
  
### getReadWrite()
    
    
    public TransactionOptions.ReadWrite getReadWrite()

The transaction should allow both reads and writes.

`.google.datastore.v1.TransactionOptions.ReadWrite read_write = 1;`

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.ReadWrite](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.ReadWrite)` | The readWrite.  
  
### getReadWriteBuilder()
    
    
    public TransactionOptions.ReadWrite.Builder getReadWriteBuilder()

The transaction should allow both reads and writes.

`.google.datastore.v1.TransactionOptions.ReadWrite read_write = 1;`

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.ReadWrite.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.ReadWrite.Builder)` |   
  
### getReadWriteOrBuilder()
    
    
    public TransactionOptions.ReadWriteOrBuilder getReadWriteOrBuilder()

The transaction should allow both reads and writes.

`.google.datastore.v1.TransactionOptions.ReadWrite read_write = 1;`

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.ReadWriteOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.ReadWriteOrBuilder)` |   
  
### hasReadOnly()
    
    
    public boolean hasReadOnly()

The transaction should only allow reads.

`.google.datastore.v1.TransactionOptions.ReadOnly read_only = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the readOnly field is set.  
  
### hasReadWrite()
    
    
    public boolean hasReadWrite()

The transaction should allow both reads and writes.

`.google.datastore.v1.TransactionOptions.ReadWrite read_write = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the readWrite field is set.  
  
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

### mergeFrom(TransactionOptions other)
    
    
    public TransactionOptions.Builder mergeFrom(TransactionOptions other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[TransactionOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public TransactionOptions.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public TransactionOptions.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeReadOnly(TransactionOptions.ReadOnly value)
    
    
    public TransactionOptions.Builder mergeReadOnly(TransactionOptions.ReadOnly value)

The transaction should only allow reads.

`.google.datastore.v1.TransactionOptions.ReadOnly read_only = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[TransactionOptions.ReadOnly](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.ReadOnly)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.Builder)` |   
  
### mergeReadWrite(TransactionOptions.ReadWrite value)
    
    
    public TransactionOptions.Builder mergeReadWrite(TransactionOptions.ReadWrite value)

The transaction should allow both reads and writes.

`.google.datastore.v1.TransactionOptions.ReadWrite read_write = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[TransactionOptions.ReadWrite](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.ReadWrite)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.Builder)` |   
  
### setReadOnly(TransactionOptions.ReadOnly value)
    
    
    public TransactionOptions.Builder setReadOnly(TransactionOptions.ReadOnly value)

The transaction should only allow reads.

`.google.datastore.v1.TransactionOptions.ReadOnly read_only = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[TransactionOptions.ReadOnly](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.ReadOnly)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.Builder)` |   
  
### setReadOnly(TransactionOptions.ReadOnly.Builder builderForValue)
    
    
    public TransactionOptions.Builder setReadOnly(TransactionOptions.ReadOnly.Builder builderForValue)

The transaction should only allow reads.

`.google.datastore.v1.TransactionOptions.ReadOnly read_only = 2;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[TransactionOptions.ReadOnly.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.ReadOnly.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.Builder)` |   
  
### setReadWrite(TransactionOptions.ReadWrite value)
    
    
    public TransactionOptions.Builder setReadWrite(TransactionOptions.ReadWrite value)

The transaction should allow both reads and writes.

`.google.datastore.v1.TransactionOptions.ReadWrite read_write = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[TransactionOptions.ReadWrite](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.ReadWrite)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.Builder)` |   
  
### setReadWrite(TransactionOptions.ReadWrite.Builder builderForValue)
    
    
    public TransactionOptions.Builder setReadWrite(TransactionOptions.ReadWrite.Builder builderForValue)

The transaction should allow both reads and writes.

`.google.datastore.v1.TransactionOptions.ReadWrite read_write = 1;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[TransactionOptions.ReadWrite.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.ReadWrite.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.v1.TransactionOptions.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
