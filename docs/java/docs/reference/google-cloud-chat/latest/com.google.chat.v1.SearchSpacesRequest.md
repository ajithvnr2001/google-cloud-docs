---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest
title: Class SearchSpacesRequest (0.63.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:17.143807+00:00
---

# Class SearchSpacesRequest (0.63.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SearchSpacesRequest (0.63.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.63.0 (latest)  0.59.0  0.58.0  0.57.0  0.55.0  0.52.0  0.51.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.28.0  0.27.0  0.26.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.1.0 
    
    
    public final class SearchSpacesRequest extends GeneratedMessage implements SearchSpacesRequestOrBuilder

Request to search for a list of spaces based on a query.

Protobuf type `google.chat.v1.SearchSpacesRequest`

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html) > [AbstractMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html) > [GeneratedMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html) > SearchSpacesRequest

## Implements

[SearchSpacesRequestOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequestOrBuilder)

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

### ORDER_BY_FIELD_NUMBER
    
    
    public static final int ORDER_BY_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### PAGE_SIZE_FIELD_NUMBER
    
    
    public static final int PAGE_SIZE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### PAGE_TOKEN_FIELD_NUMBER
    
    
    public static final int PAGE_TOKEN_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### QUERY_FIELD_NUMBER
    
    
    public static final int QUERY_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### USE_ADMIN_ACCESS_FIELD_NUMBER
    
    
    public static final int USE_ADMIN_ACCESS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Static Methods 

### getDefaultInstance()
    
    
    public static SearchSpacesRequest getDefaultInstance()

**Returns**  
---  
**Type** | **Description**  
`[SearchSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest)` |   
  
### getDescriptor()
    
    
    public static final Descriptors.Descriptor getDescriptor()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
  
### newBuilder()
    
    
    public static SearchSpacesRequest.Builder newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[SearchSpacesRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest.Builder)` |   
  
### newBuilder(SearchSpacesRequest prototype)
    
    
    public static SearchSpacesRequest.Builder newBuilder(SearchSpacesRequest prototype)

**Parameter**  
---  
**Name** | **Description**  
`prototype` | `[SearchSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchSpacesRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest.Builder)` |   
  
### parseDelimitedFrom(InputStream input)
    
    
    public static SearchSpacesRequest parseDelimitedFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static SearchSpacesRequest parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(byte[] data)
    
    
    public static SearchSpacesRequest parseFrom(byte[] data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)
    
    
    public static SearchSpacesRequest parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data)
    
    
    public static SearchSpacesRequest parseFrom(ByteString data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)
    
    
    public static SearchSpacesRequest parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(CodedInputStream input)
    
    
    public static SearchSpacesRequest parseFrom(CodedInputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static SearchSpacesRequest parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input)
    
    
    public static SearchSpacesRequest parseFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static SearchSpacesRequest parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(ByteBuffer data)
    
    
    public static SearchSpacesRequest parseFrom(ByteBuffer data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)
    
    
    public static SearchSpacesRequest parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parser()
    
    
    public static Parser<SearchSpacesRequest> parser()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[SearchSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest)>` |   
  
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

### getDefaultInstanceForType()
    
    
    public SearchSpacesRequest getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[SearchSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest)` |   
  
### getOrderBy()
    
    
    public String getOrderBy()

Optional. How the list of spaces is ordered.

Supported attributes to order by are:

  * `membership_count.joined_direct_human_user_count` — Denotes the count of human users that have directly joined a space.
  * `last_active_time` — Denotes the time when last eligible item is added to any topic of this space.
  * `create_time` — Denotes the time of the space creation.

When `useAdminAccess` is `false`, only `create_time` and `relevance` are supported for ordering. Only `DESC` is supported for these fields in non-admin searches.

Valid ordering operation values are:

  * `ASC` for ascending. Default value.

  * `DESC` for descending.

The supported syntax are when `useAdminAccess` is set to `true`:

  * `membership_count.joined_direct_human_user_count DESC`

  * `membership_count.joined_direct_human_user_count ASC`
  * `last_active_time DESC`
  * `last_active_time ASC`
  * `create_time DESC`
  * `create_time ASC`

When `useAdminAccess` is set to `false`:

  * `create_time DESC`

  * `relevance DESC` [Developer Preview](https://developers.google.com/workspace/preview).



`string order_by = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The orderBy.  
  
### getOrderByBytes()
    
    
    public ByteString getOrderByBytes()

Optional. How the list of spaces is ordered.

Supported attributes to order by are:

  * `membership_count.joined_direct_human_user_count` — Denotes the count of human users that have directly joined a space.
  * `last_active_time` — Denotes the time when last eligible item is added to any topic of this space.
  * `create_time` — Denotes the time of the space creation.

When `useAdminAccess` is `false`, only `create_time` and `relevance` are supported for ordering. Only `DESC` is supported for these fields in non-admin searches.

Valid ordering operation values are:

  * `ASC` for ascending. Default value.

  * `DESC` for descending.

The supported syntax are when `useAdminAccess` is set to `true`:

  * `membership_count.joined_direct_human_user_count DESC`

  * `membership_count.joined_direct_human_user_count ASC`
  * `last_active_time DESC`
  * `last_active_time ASC`
  * `create_time DESC`
  * `create_time ASC`

When `useAdminAccess` is set to `false`:

  * `create_time DESC`

  * `relevance DESC` [Developer Preview](https://developers.google.com/workspace/preview).



`string order_by = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for orderBy.  
  
### getPageSize()
    
    
    public int getPageSize()

The maximum number of spaces to return. The service may return fewer than this value.

If unspecified, at most 100 spaces are returned.

The maximum value is 1000 when `useAdminAccess` is set to `true`. Otherwise, the maximum value is 100. If you use a value more than the maximum value, it's automatically changed to the maximum value.

`int32 page_size = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The pageSize.  
  
### getPageToken()
    
    
    public String getPageToken()

A token, received from the previous search spaces call. Provide this parameter to retrieve the subsequent page.

When paginating, all other parameters provided should match the call that provided the page token. Passing different values to the other parameters might lead to unexpected results.

`string page_token = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pageToken.  
  
### getPageTokenBytes()
    
    
    public ByteString getPageTokenBytes()

A token, received from the previous search spaces call. Provide this parameter to retrieve the subsequent page.

When paginating, all other parameters provided should match the call that provided the page token. Passing different values to the other parameters might lead to unexpected results.

`string page_token = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pageToken.  
  
### getParserForType()
    
    
    public Parser<SearchSpacesRequest> getParserForType()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[SearchSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest)>` |   
**Overrides**

[GeneratedMessage.getParserForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getParserForType__)

### getQuery()
    
    
    public String getQuery()

Required. A search query.

You can search by using the following parameters when `useAdminAccess` is set to `true`:

  * `create_time`
  * `customer`
  * `display_name`
  * `external_user_allowed`
  * `last_active_time`
  * `space_history_state`
  * `space_type`

When `useAdminAccess` is set to `false`:

  * `display_name`

  * `external_user_allowed`
  * `space_type`

`create_time` and `last_active_time` accept a timestamp in [RFC-3339](https://www.rfc-editor.org/rfc/rfc3339) format and the supported comparison operators are: `=`, `<`, `>`, `<=`, `>=`.

`customer` is required when `useAdminAccess` is set to `true`, and is used to indicate which customer to fetch spaces from. `customers/my_customer` is the only supported value.

`display_name` only accepts the `HAS` (`:`) operator. The text to match is first tokenized into tokens and each token is prefix-matched case-insensitively and independently as a substring anywhere in the space's `display_name`. For example, `Fun Eve` matches `Fun event` or `The evening was fun`, but not `notFun event` or `even`. When `useAdminAccess` is set to `false`, `display_name` is required to retrieve meaningful results. Otherwise, the default behavior is to return an empty response.

`external_user_allowed` accepts either `true` or `false`.

`space_history_state` only accepts values from the [`historyState`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces#Space.HistoryState) field of a `space` resource.

`space_type` is required and the only valid value is `SPACE`.

Across different fields, only `AND` operators are supported. A valid example is `space_type = "SPACE" AND display_name:"Hello"` and an invalid example is `space_type = "SPACE" OR display_name:"Hello"`.

Among the same field, `space_type` doesn't support `AND` or `OR` operators. `display_name`, 'space_history_state', and 'external_user_allowed' only support `OR` operators. `last_active_time` and `create_time` support both `AND` and `OR` operators. `AND` can only be used to represent an interval, such as `last_active_time < "2022-01-01T00:00:00+00:00" AND last_active_time > "2023-01-01T00:00:00+00:00"`.

The following example queries are valid when `useAdminAccess` is set to `true`:

``` customer = "customers/my_customer" AND space_type = "SPACE"``

`` ``

``customer = "customers/my_customer" AND space_type = "SPACE" AND display_name:"Hello World"``

``

customer = "customers/my_customer" AND space_type = "SPACE" AND (last_active_time < "2020-01-01T00:00:00+00:00" OR last_active_time > "2022-01-01T00:00:00+00:00")

customer = "customers/my_customer" AND space_type = "SPACE" AND (display_name:"Hello World" OR display_name:"Fun event") AND (last_active_time > "2020-01-01T00:00:00+00:00" AND last_active_time < "2022-01-01T00:00:00+00:00")

``

``customer = "customers/my_customer" AND space_type = "SPACE" AND (create_time > "2019-01-01T00:00:00+00:00" AND create_time < "2020-01-01T00:00:00+00:00") AND (external_user_allowed = "true") AND (space_history_state = "HISTORY_ON" OR space_history_state = "HISTORY_OFF") ````

` `

`The following example queries are valid when `useAdminAccess` is set to `false`:`

` `

`` display_name:"Hello World" AND space_type = "SPACE"``

`` ``

``(display_name:"Hello" OR display_name:"Fun") AND space_type = "SPACE"``

``

(external_user_allowed = "true" AND space_type = "SPACE") // Returns an empty response.

``

``(external_user_allowed = "true" AND display_name:"Hello" AND space_type = "SPACE") ````

` `

`The maximum query length is 1,000 characters.`

` `

`Invalid queries are rejected by the server with an `INVALID_ARGUMENT` error.




`string query = 4 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The query.  
  
### getQueryBytes()
    
    
    public ByteString getQueryBytes()

Required. A search query.

You can search by using the following parameters when `useAdminAccess` is set to `true`:

  * `create_time`
  * `customer`
  * `display_name`
  * `external_user_allowed`
  * `last_active_time`
  * `space_history_state`
  * `space_type`

When `useAdminAccess` is set to `false`:

  * `display_name`

  * `external_user_allowed`
  * `space_type`

`create_time` and `last_active_time` accept a timestamp in [RFC-3339](https://www.rfc-editor.org/rfc/rfc3339) format and the supported comparison operators are: `=`, `<`, `>`, `<=`, `>=`.

`customer` is required when `useAdminAccess` is set to `true`, and is used to indicate which customer to fetch spaces from. `customers/my_customer` is the only supported value.

`display_name` only accepts the `HAS` (`:`) operator. The text to match is first tokenized into tokens and each token is prefix-matched case-insensitively and independently as a substring anywhere in the space's `display_name`. For example, `Fun Eve` matches `Fun event` or `The evening was fun`, but not `notFun event` or `even`. When `useAdminAccess` is set to `false`, `display_name` is required to retrieve meaningful results. Otherwise, the default behavior is to return an empty response.

`external_user_allowed` accepts either `true` or `false`.

`space_history_state` only accepts values from the [`historyState`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces#Space.HistoryState) field of a `space` resource.

`space_type` is required and the only valid value is `SPACE`.

Across different fields, only `AND` operators are supported. A valid example is `space_type = "SPACE" AND display_name:"Hello"` and an invalid example is `space_type = "SPACE" OR display_name:"Hello"`.

Among the same field, `space_type` doesn't support `AND` or `OR` operators. `display_name`, 'space_history_state', and 'external_user_allowed' only support `OR` operators. `last_active_time` and `create_time` support both `AND` and `OR` operators. `AND` can only be used to represent an interval, such as `last_active_time < "2022-01-01T00:00:00+00:00" AND last_active_time > "2023-01-01T00:00:00+00:00"`.

The following example queries are valid when `useAdminAccess` is set to `true`:

``` customer = "customers/my_customer" AND space_type = "SPACE"``

`` ``

``customer = "customers/my_customer" AND space_type = "SPACE" AND display_name:"Hello World"``

``

customer = "customers/my_customer" AND space_type = "SPACE" AND (last_active_time < "2020-01-01T00:00:00+00:00" OR last_active_time > "2022-01-01T00:00:00+00:00")

customer = "customers/my_customer" AND space_type = "SPACE" AND (display_name:"Hello World" OR display_name:"Fun event") AND (last_active_time > "2020-01-01T00:00:00+00:00" AND last_active_time < "2022-01-01T00:00:00+00:00")

``

``customer = "customers/my_customer" AND space_type = "SPACE" AND (create_time > "2019-01-01T00:00:00+00:00" AND create_time < "2020-01-01T00:00:00+00:00") AND (external_user_allowed = "true") AND (space_history_state = "HISTORY_ON" OR space_history_state = "HISTORY_OFF") ````

` `

`The following example queries are valid when `useAdminAccess` is set to `false`:`

` `

`` display_name:"Hello World" AND space_type = "SPACE"``

`` ``

``(display_name:"Hello" OR display_name:"Fun") AND space_type = "SPACE"``

``

(external_user_allowed = "true" AND space_type = "SPACE") // Returns an empty response.

``

``(external_user_allowed = "true" AND display_name:"Hello" AND space_type = "SPACE") ````

` `

`The maximum query length is 1,000 characters.`

` `

`Invalid queries are rejected by the server with an `INVALID_ARGUMENT` error.




`string query = 4 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for query.  
  
### getSerializedSize()
    
    
    public int getSerializedSize()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.getSerializedSize()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getSerializedSize__)

### getUseAdminAccess()
    
    
    public boolean getUseAdminAccess()

When `true`, the method runs using the user's Google Workspace administrator privileges.

The calling user must be a Google Workspace administrator with the [manage chat and spaces conversations privilege](https://support.google.com/a/answer/13369245).

Requires either the `chat.admin.spaces.readonly` or `chat.admin.spaces` [OAuth 2.0 scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes).

`bool use_admin_access = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The useAdminAccess.  
  
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
    
    
    public SearchSpacesRequest.Builder newBuilderForType()

**Returns**  
---  
**Type** | **Description**  
`[SearchSpacesRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest.Builder)` |   
  
### newBuilderForType(AbstractMessage.BuilderParent parent)
    
    
    protected SearchSpacesRequest.Builder newBuilderForType(AbstractMessage.BuilderParent parent)

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[BuilderParent](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.BuilderParent.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchSpacesRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest.Builder)` |   
**Overrides**

[AbstractMessage.newBuilderForType(AbstractMessage.BuilderParent parent)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_newBuilderForType_com_google_protobuf_AbstractMessage_BuilderParent_)

### toBuilder()
    
    
    public SearchSpacesRequest.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[SearchSpacesRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest.Builder)` |   
  
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

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
