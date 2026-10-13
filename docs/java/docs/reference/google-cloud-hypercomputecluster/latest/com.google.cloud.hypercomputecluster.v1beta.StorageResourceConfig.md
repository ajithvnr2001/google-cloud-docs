---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig
title: Class StorageResourceConfig (0.19.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:17:20.898751+00:00
---

# Class StorageResourceConfig (0.19.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class StorageResourceConfig (0.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.19.0 (latest)  0.15.0  0.14.0  0.13.0  0.11.0  0.8.0  0.7.0  0.5.0  0.3.0  0.2.0  0.1.0 
    
    
    public final class StorageResourceConfig extends GeneratedMessage implements StorageResourceConfigOrBuilder

Describes how a storage resource should be initialized. Each storage resource can either be imported from an existing Google Cloud resource or initialized when the cluster is created.

Protobuf type `google.cloud.hypercomputecluster.v1beta.StorageResourceConfig`

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html) > [AbstractMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html) > [GeneratedMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html) > StorageResourceConfig

## Implements

[StorageResourceConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfigOrBuilder)

## Inherited Members

[AbstractMessage.equals(Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_equals_java_lang_Object_)

[AbstractMessage.findInitializationErrors()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_findInitializationErrors__)

[AbstractMessage.getInitializationErrorString()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_getInitializationErrorString__)

[AbstractMessage.hashCode()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_hashCode__)

[AbstractMessage.hashFields(int,Map<Descriptors.FieldDescriptor,Object>)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_hashFields_int_java_util_Map_com_google_protobuf_Descriptors_FieldDescriptor_java_lang_Object__)

[AbstractMessage.newBuilderForType(AbstractMessage.BuilderParent)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_newBuilderForType_com_google_protobuf_AbstractMessage_BuilderParent_)

[AbstractMessage.toString()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_toString__)

[AbstractMessageLite.<T>addAll(Iterable<T>,List<? super T>)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite__T_addAll_java_lang_Iterable_T__java_util_List___super_T__)

[AbstractMessageLite.checkByteStringIsUtf8(ByteString)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite_checkByteStringIsUtf8_com_google_protobuf_ByteString_)

[AbstractMessageLite.toByteArray()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite_toByteArray__)

[AbstractMessageLite.toByteString()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite_toByteString__)

[AbstractMessageLite.writeDelimitedTo(OutputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite_writeDelimitedTo_java_io_OutputStream_)

[AbstractMessageLite.writeTo(OutputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite_writeTo_java_io_OutputStream_)

com.google.protobuf.GeneratedMessage.<ContainingT,T>newFileScopedGeneratedExtension(java.lang.Class<?>,com.google.protobuf.Message)

com.google.protobuf.GeneratedMessage.<ContainingT,T>newMessageScopedGeneratedExtension(com.google.protobuf.Message,int,java.lang.Class<?>,com.google.protobuf.Message)

com.google.protobuf.GeneratedMessage.<ListT>makeMutableCopy(ListT)

com.google.protobuf.GeneratedMessage.<ListT>makeMutableCopy(ListT,int)

[GeneratedMessage.<M>parseDelimitedWithIOException(Parser<M>,InputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseDelimitedWithIOException_com_google_protobuf_Parser_M__java_io_InputStream_)

[GeneratedMessage.<M>parseDelimitedWithIOException(Parser<M>,InputStream,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseDelimitedWithIOException_com_google_protobuf_Parser_M__java_io_InputStream_com_google_protobuf_ExtensionRegistryLite_)

[GeneratedMessage.<M>parseWithIOException(Parser<M>,CodedInputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseWithIOException_com_google_protobuf_Parser_M__com_google_protobuf_CodedInputStream_)

[GeneratedMessage.<M>parseWithIOException(Parser<M>,CodedInputStream,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseWithIOException_com_google_protobuf_Parser_M__com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

[GeneratedMessage.<M>parseWithIOException(Parser<M>,InputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseWithIOException_com_google_protobuf_Parser_M__java_io_InputStream_)

[GeneratedMessage.<M>parseWithIOException(Parser<M>,InputStream,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseWithIOException_com_google_protobuf_Parser_M__java_io_InputStream_com_google_protobuf_ExtensionRegistryLite_)

com.google.protobuf.GeneratedMessage.<T>emptyList(java.lang.Class<T>)

com.google.protobuf.GeneratedMessage.<V>serializeBooleanMapTo(com.google.protobuf.CodedOutputStream,com.google.protobuf.MapField<java.lang.Boolean,V>,com.google.protobuf.MapEntry<java.lang.Boolean,V>,int)

com.google.protobuf.GeneratedMessage.<V>serializeIntegerMapTo(com.google.protobuf.CodedOutputStream,com.google.protobuf.MapField<java.lang.Integer,V>,com.google.protobuf.MapEntry<java.lang.Integer,V>,int)

com.google.protobuf.GeneratedMessage.<V>serializeLongMapTo(com.google.protobuf.CodedOutputStream,com.google.protobuf.MapField<java.lang.Long,V>,com.google.protobuf.MapEntry<java.lang.Long,V>,int)

com.google.protobuf.GeneratedMessage.<V>serializeStringMapTo(com.google.protobuf.CodedOutputStream,com.google.protobuf.MapField<java.lang.String,V>,com.google.protobuf.MapEntry<java.lang.String,V>,int)

com.google.protobuf.GeneratedMessage.canUseUnsafe()

[GeneratedMessage.computeStringSize(int,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_computeStringSize_int_java_lang_Object_)

[GeneratedMessage.computeStringSizeNoTag(Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_computeStringSizeNoTag_java_lang_Object_)

com.google.protobuf.GeneratedMessage.emptyBooleanList()

com.google.protobuf.GeneratedMessage.emptyDoubleList()

com.google.protobuf.GeneratedMessage.emptyFloatList()

com.google.protobuf.GeneratedMessage.emptyIntList()

com.google.protobuf.GeneratedMessage.emptyLongList()

[GeneratedMessage.getAllFields()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getAllFields__)

[GeneratedMessage.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getDescriptorForType__)

[GeneratedMessage.getField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.getOneofFieldDescriptor(Descriptors.OneofDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getOneofFieldDescriptor_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessage.getParserForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getParserForType__)

[GeneratedMessage.getRepeatedField(Descriptors.FieldDescriptor,int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_int_)

[GeneratedMessage.getRepeatedFieldCount(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getRepeatedFieldCount_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.getSerializedSize()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getSerializedSize__)

[GeneratedMessage.getUnknownFields()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getUnknownFields__)

[GeneratedMessage.hasField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_hasField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.hasOneof(Descriptors.OneofDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_hasOneof_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessage.internalGetFieldAccessorTable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_internalGetFieldAccessorTable__)

[GeneratedMessage.internalGetMapField(int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_internalGetMapField_int_)

com.google.protobuf.GeneratedMessage.internalGetMapFieldReflection(int)

[GeneratedMessage.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_isInitialized__)

com.google.protobuf.GeneratedMessage.isStringEmpty(java.lang.Object)

[GeneratedMessage.makeExtensionsImmutable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_makeExtensionsImmutable__)

com.google.protobuf.GeneratedMessage.mergeFromAndMakeImmutableInternal(com.google.protobuf.CodedInputStream,com.google.protobuf.ExtensionRegistryLite)

com.google.protobuf.GeneratedMessage.newInstance(com.google.protobuf.GeneratedMessage.UnusedPrivateParameter)

[GeneratedMessage.parseUnknownField(CodedInputStream,UnknownFieldSet.Builder,ExtensionRegistryLite,int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_parseUnknownField_com_google_protobuf_CodedInputStream_com_google_protobuf_UnknownFieldSet_Builder_com_google_protobuf_ExtensionRegistryLite_int_)

com.google.protobuf.GeneratedMessage.parseUnknownFieldProto3(com.google.protobuf.CodedInputStream,com.google.protobuf.UnknownFieldSet.Builder,com.google.protobuf.ExtensionRegistryLite,int)

[GeneratedMessage.writeReplace()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_writeReplace__)

[GeneratedMessage.writeString(CodedOutputStream,int,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_writeString_com_google_protobuf_CodedOutputStream_int_java_lang_Object_)

[GeneratedMessage.writeStringNoTag(CodedOutputStream,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_writeStringNoTag_com_google_protobuf_CodedOutputStream_java_lang_Object_)

[GeneratedMessage.writeTo(CodedOutputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_writeTo_com_google_protobuf_CodedOutputStream_)

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields 

### EXISTING_BUCKET_FIELD_NUMBER
    
    
    public static final int EXISTING_BUCKET_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### EXISTING_FILESTORE_FIELD_NUMBER
    
    
    public static final int EXISTING_FILESTORE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### EXISTING_LUSTRE_FIELD_NUMBER
    
    
    public static final int EXISTING_LUSTRE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### NEW_BUCKET_FIELD_NUMBER
    
    
    public static final int NEW_BUCKET_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### NEW_FILESTORE_FIELD_NUMBER
    
    
    public static final int NEW_FILESTORE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### NEW_LUSTRE_FIELD_NUMBER
    
    
    public static final int NEW_LUSTRE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Static Methods 

### getDefaultInstance()
    
    
    public static StorageResourceConfig getDefaultInstance()

**Returns**  
---  
**Type** | **Description**  
`[StorageResourceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig)` |   
  
### getDescriptor()
    
    
    public static final Descriptors.Descriptor getDescriptor()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
  
### newBuilder()
    
    
    public static StorageResourceConfig.Builder newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[StorageResourceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig.Builder)` |   
  
### newBuilder(StorageResourceConfig prototype)
    
    
    public static StorageResourceConfig.Builder newBuilder(StorageResourceConfig prototype)

**Parameter**  
---  
**Name** | **Description**  
`prototype` | `[StorageResourceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageResourceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig.Builder)` |   
  
### parseDelimitedFrom(InputStream input)
    
    
    public static StorageResourceConfig parseDelimitedFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageResourceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static StorageResourceConfig parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageResourceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(byte[] data)
    
    
    public static StorageResourceConfig parseFrom(byte[] data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageResourceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)
    
    
    public static StorageResourceConfig parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageResourceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data)
    
    
    public static StorageResourceConfig parseFrom(ByteString data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageResourceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)
    
    
    public static StorageResourceConfig parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageResourceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(CodedInputStream input)
    
    
    public static StorageResourceConfig parseFrom(CodedInputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageResourceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static StorageResourceConfig parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageResourceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input)
    
    
    public static StorageResourceConfig parseFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageResourceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static StorageResourceConfig parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageResourceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(ByteBuffer data)
    
    
    public static StorageResourceConfig parseFrom(ByteBuffer data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageResourceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)
    
    
    public static StorageResourceConfig parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageResourceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parser()
    
    
    public static Parser<StorageResourceConfig> parser()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[StorageResourceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig)>` |   
  
## Methods 

### equals(Object obj)
    
    
    public boolean equals(Object obj)

**Parameter**  
---  
**Name** | **Description**  
`obj` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[AbstractMessage.equals(Object other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_equals_java_lang_Object_)

### getConfigCase()
    
    
    public StorageResourceConfig.ConfigCase getConfigCase()

**Returns**  
---  
**Type** | **Description**  
`[StorageResourceConfig.ConfigCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig.ConfigCase)` |   
  
### getDefaultInstanceForType()
    
    
    public StorageResourceConfig getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[StorageResourceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig)` |   
  
### getExistingBucket()
    
    
    public ExistingBucketConfig getExistingBucket()

Optional. Immutable. If set, indicates that an existing Cloud Storage bucket should be imported.

` .google.cloud.hypercomputecluster.v1beta.ExistingBucketConfig existing_bucket = 4 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ExistingBucketConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.ExistingBucketConfig)` | The existingBucket.  
  
### getExistingBucketOrBuilder()
    
    
    public ExistingBucketConfigOrBuilder getExistingBucketOrBuilder()

Optional. Immutable. If set, indicates that an existing Cloud Storage bucket should be imported.

` .google.cloud.hypercomputecluster.v1beta.ExistingBucketConfig existing_bucket = 4 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ExistingBucketConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.ExistingBucketConfigOrBuilder)` |   
  
### getExistingFilestore()
    
    
    public ExistingFilestoreConfig getExistingFilestore()

Optional. Immutable. If set, indicates that an existing Filestore instance should be imported.

` .google.cloud.hypercomputecluster.v1beta.ExistingFilestoreConfig existing_filestore = 2 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ExistingFilestoreConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.ExistingFilestoreConfig)` | The existingFilestore.  
  
### getExistingFilestoreOrBuilder()
    
    
    public ExistingFilestoreConfigOrBuilder getExistingFilestoreOrBuilder()

Optional. Immutable. If set, indicates that an existing Filestore instance should be imported.

` .google.cloud.hypercomputecluster.v1beta.ExistingFilestoreConfig existing_filestore = 2 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ExistingFilestoreConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.ExistingFilestoreConfigOrBuilder)` |   
  
### getExistingLustre()
    
    
    public ExistingLustreConfig getExistingLustre()

Optional. Immutable. If set, indicates that an existing Managed Lustre instance should be imported.

` .google.cloud.hypercomputecluster.v1beta.ExistingLustreConfig existing_lustre = 6 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ExistingLustreConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.ExistingLustreConfig)` | The existingLustre.  
  
### getExistingLustreOrBuilder()
    
    
    public ExistingLustreConfigOrBuilder getExistingLustreOrBuilder()

Optional. Immutable. If set, indicates that an existing Managed Lustre instance should be imported.

` .google.cloud.hypercomputecluster.v1beta.ExistingLustreConfig existing_lustre = 6 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[ExistingLustreConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.ExistingLustreConfigOrBuilder)` |   
  
### getNewBucket()
    
    
    public NewBucketConfig getNewBucket()

Optional. Immutable. If set, indicates that a new Cloud Storage bucket should be created.

` .google.cloud.hypercomputecluster.v1beta.NewBucketConfig new_bucket = 3 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[NewBucketConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.NewBucketConfig)` | The newBucket.  
  
### getNewBucketOrBuilder()
    
    
    public NewBucketConfigOrBuilder getNewBucketOrBuilder()

Optional. Immutable. If set, indicates that a new Cloud Storage bucket should be created.

` .google.cloud.hypercomputecluster.v1beta.NewBucketConfig new_bucket = 3 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[NewBucketConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.NewBucketConfigOrBuilder)` |   
  
### getNewFilestore()
    
    
    public NewFilestoreConfig getNewFilestore()

Optional. Immutable. If set, indicates that a new Filestore instance should be created.

` .google.cloud.hypercomputecluster.v1beta.NewFilestoreConfig new_filestore = 1 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[NewFilestoreConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.NewFilestoreConfig)` | The newFilestore.  
  
### getNewFilestoreOrBuilder()
    
    
    public NewFilestoreConfigOrBuilder getNewFilestoreOrBuilder()

Optional. Immutable. If set, indicates that a new Filestore instance should be created.

` .google.cloud.hypercomputecluster.v1beta.NewFilestoreConfig new_filestore = 1 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[NewFilestoreConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.NewFilestoreConfigOrBuilder)` |   
  
### getNewLustre()
    
    
    public NewLustreConfig getNewLustre()

Optional. Immutable. If set, indicates that a new Managed Lustre instance should be created.

` .google.cloud.hypercomputecluster.v1beta.NewLustreConfig new_lustre = 5 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[NewLustreConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.NewLustreConfig)` | The newLustre.  
  
### getNewLustreOrBuilder()
    
    
    public NewLustreConfigOrBuilder getNewLustreOrBuilder()

Optional. Immutable. If set, indicates that a new Managed Lustre instance should be created.

` .google.cloud.hypercomputecluster.v1beta.NewLustreConfig new_lustre = 5 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[NewLustreConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.NewLustreConfigOrBuilder)` |   
  
### getParserForType()
    
    
    public Parser<StorageResourceConfig> getParserForType()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[StorageResourceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig)>` |   
**Overrides**

[GeneratedMessage.getParserForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getParserForType__)

### getSerializedSize()
    
    
    public int getSerializedSize()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.getSerializedSize()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getSerializedSize__)

### hasExistingBucket()
    
    
    public boolean hasExistingBucket()

Optional. Immutable. If set, indicates that an existing Cloud Storage bucket should be imported.

` .google.cloud.hypercomputecluster.v1beta.ExistingBucketConfig existing_bucket = 4 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the existingBucket field is set.  
  
### hasExistingFilestore()
    
    
    public boolean hasExistingFilestore()

Optional. Immutable. If set, indicates that an existing Filestore instance should be imported.

` .google.cloud.hypercomputecluster.v1beta.ExistingFilestoreConfig existing_filestore = 2 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the existingFilestore field is set.  
  
### hasExistingLustre()
    
    
    public boolean hasExistingLustre()

Optional. Immutable. If set, indicates that an existing Managed Lustre instance should be imported.

` .google.cloud.hypercomputecluster.v1beta.ExistingLustreConfig existing_lustre = 6 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the existingLustre field is set.  
  
### hasNewBucket()
    
    
    public boolean hasNewBucket()

Optional. Immutable. If set, indicates that a new Cloud Storage bucket should be created.

` .google.cloud.hypercomputecluster.v1beta.NewBucketConfig new_bucket = 3 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the newBucket field is set.  
  
### hasNewFilestore()
    
    
    public boolean hasNewFilestore()

Optional. Immutable. If set, indicates that a new Filestore instance should be created.

` .google.cloud.hypercomputecluster.v1beta.NewFilestoreConfig new_filestore = 1 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the newFilestore field is set.  
  
### hasNewLustre()
    
    
    public boolean hasNewLustre()

Optional. Immutable. If set, indicates that a new Managed Lustre instance should be created.

` .google.cloud.hypercomputecluster.v1beta.NewLustreConfig new_lustre = 5 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = IMMUTABLE]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the newLustre field is set.  
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[AbstractMessage.hashCode()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_hashCode__)

### internalGetFieldAccessorTable()
    
    
    protected GeneratedMessage.FieldAccessorTable internalGetFieldAccessorTable()

**Returns**  
---  
**Type** | **Description**  
`[FieldAccessorTable](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.FieldAccessorTable.html)` |   
**Overrides**

[GeneratedMessage.internalGetFieldAccessorTable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_internalGetFieldAccessorTable__)

### isInitialized()
    
    
    public final boolean isInitialized()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_isInitialized__)

### newBuilderForType()
    
    
    public StorageResourceConfig.Builder newBuilderForType()

**Returns**  
---  
**Type** | **Description**  
`[StorageResourceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig.Builder)` |   
  
### newBuilderForType(AbstractMessage.BuilderParent parent)
    
    
    protected StorageResourceConfig.Builder newBuilderForType(AbstractMessage.BuilderParent parent)

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[BuilderParent](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.BuilderParent.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageResourceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig.Builder)` |   
**Overrides**

[AbstractMessage.newBuilderForType(AbstractMessage.BuilderParent parent)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_newBuilderForType_com_google_protobuf_AbstractMessage_BuilderParent_)

### toBuilder()
    
    
    public StorageResourceConfig.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[StorageResourceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.StorageResourceConfig.Builder)` |   
  
### writeTo(CodedOutputStream output)
    
    
    public void writeTo(CodedOutputStream output)

**Parameter**  
---  
**Name** | **Description**  
`output` | `[CodedOutputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream.html)`  
  
**Overrides**

[GeneratedMessage.writeTo(CodedOutputStream output)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_writeTo_com_google_protobuf_CodedOutputStream_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
