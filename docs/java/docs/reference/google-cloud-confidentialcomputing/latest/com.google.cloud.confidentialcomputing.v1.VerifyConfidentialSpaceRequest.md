---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest
title: Class VerifyConfidentialSpaceRequest (0.85.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:20:52.448598+00:00
---

# Class VerifyConfidentialSpaceRequest (0.85.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class VerifyConfidentialSpaceRequest (0.85.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.85.0 (latest)  0.81.0  0.80.0  0.79.0  0.77.0  0.74.0  0.73.0  0.71.0  0.69.0  0.68.0  0.67.0  0.66.0  0.64.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.56.0  0.54.0  0.53.0  0.50.0  0.49.0  0.48.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public final class VerifyConfidentialSpaceRequest extends GeneratedMessage implements VerifyConfidentialSpaceRequestOrBuilder

A request for an attestation token, providing all the necessary information needed for this service to verify the platform state of the requestor.

Protobuf type `google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest`

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html) > [AbstractMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html) > [GeneratedMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html) > VerifyConfidentialSpaceRequest

## Implements

[VerifyConfidentialSpaceRequestOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequestOrBuilder)

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

### CHALLENGE_FIELD_NUMBER
    
    
    public static final int CHALLENGE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### GCE_SHIELDED_IDENTITY_FIELD_NUMBER
    
    
    public static final int GCE_SHIELDED_IDENTITY_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### GCP_CREDENTIALS_FIELD_NUMBER
    
    
    public static final int GCP_CREDENTIALS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### NVIDIA_ATTESTATION_FIELD_NUMBER
    
    
    public static final int NVIDIA_ATTESTATION_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### OPTIONS_FIELD_NUMBER
    
    
    public static final int OPTIONS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SIGNED_ENTITIES_FIELD_NUMBER
    
    
    public static final int SIGNED_ENTITIES_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### TD_CCEL_FIELD_NUMBER
    
    
    public static final int TD_CCEL_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### TPM_ATTESTATION_FIELD_NUMBER
    
    
    public static final int TPM_ATTESTATION_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Static Methods 

### getDefaultInstance()
    
    
    public static VerifyConfidentialSpaceRequest getDefaultInstance()

**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest)` |   
  
### getDescriptor()
    
    
    public static final Descriptors.Descriptor getDescriptor()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
  
### newBuilder()
    
    
    public static VerifyConfidentialSpaceRequest.Builder newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialSpaceRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest.Builder)` |   
  
### newBuilder(VerifyConfidentialSpaceRequest prototype)
    
    
    public static VerifyConfidentialSpaceRequest.Builder newBuilder(VerifyConfidentialSpaceRequest prototype)

**Parameter**  
---  
**Name** | **Description**  
`prototype` | `[VerifyConfidentialSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialSpaceRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest.Builder)` |   
  
### parseDelimitedFrom(InputStream input)
    
    
    public static VerifyConfidentialSpaceRequest parseDelimitedFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static VerifyConfidentialSpaceRequest parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(byte[] data)
    
    
    public static VerifyConfidentialSpaceRequest parseFrom(byte[] data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)
    
    
    public static VerifyConfidentialSpaceRequest parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data)
    
    
    public static VerifyConfidentialSpaceRequest parseFrom(ByteString data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)
    
    
    public static VerifyConfidentialSpaceRequest parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(CodedInputStream input)
    
    
    public static VerifyConfidentialSpaceRequest parseFrom(CodedInputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static VerifyConfidentialSpaceRequest parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input)
    
    
    public static VerifyConfidentialSpaceRequest parseFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static VerifyConfidentialSpaceRequest parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(ByteBuffer data)
    
    
    public static VerifyConfidentialSpaceRequest parseFrom(ByteBuffer data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)
    
    
    public static VerifyConfidentialSpaceRequest parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parser()
    
    
    public static Parser<VerifyConfidentialSpaceRequest> parser()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[VerifyConfidentialSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest)>` |   
  
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

### getChallenge()
    
    
    public String getChallenge()

Required. The name of the Challenge whose nonce was used to generate the attestation, in the format `projects/*/locations/*/challenges/*`. The provided Challenge will be consumed, and cannot be used again.

` string challenge = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The challenge.  
  
### getChallengeBytes()
    
    
    public ByteString getChallengeBytes()

Required. The name of the Challenge whose nonce was used to generate the attestation, in the format `projects/*/locations/*/challenges/*`. The provided Challenge will be consumed, and cannot be used again.

` string challenge = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for challenge.  
  
### getDefaultInstanceForType()
    
    
    public VerifyConfidentialSpaceRequest getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest)` |   
  
### getGceShieldedIdentity()
    
    
    public GceShieldedIdentity getGceShieldedIdentity()

Optional. Information about the associated Compute Engine instance. Required for td_ccel requests only - tpm_attestation requests will provide this information in the attestation.

` .google.cloud.confidentialcomputing.v1.GceShieldedIdentity gce_shielded_identity = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[GceShieldedIdentity](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.GceShieldedIdentity)` | The gceShieldedIdentity.  
  
### getGceShieldedIdentityOrBuilder()
    
    
    public GceShieldedIdentityOrBuilder getGceShieldedIdentityOrBuilder()

Optional. Information about the associated Compute Engine instance. Required for td_ccel requests only - tpm_attestation requests will provide this information in the attestation.

` .google.cloud.confidentialcomputing.v1.GceShieldedIdentity gce_shielded_identity = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[GceShieldedIdentityOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.GceShieldedIdentityOrBuilder)` |   
  
### getGcpCredentials()
    
    
    public GcpCredentials getGcpCredentials()

Optional. Credentials used to populate the "emails" claim in the claims_token. If not present, token will not contain the "emails" claim.

` .google.cloud.confidentialcomputing.v1.GcpCredentials gcp_credentials = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[GcpCredentials](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.GcpCredentials)` | The gcpCredentials.  
  
### getGcpCredentialsOrBuilder()
    
    
    public GcpCredentialsOrBuilder getGcpCredentialsOrBuilder()

Optional. Credentials used to populate the "emails" claim in the claims_token. If not present, token will not contain the "emails" claim.

` .google.cloud.confidentialcomputing.v1.GcpCredentials gcp_credentials = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[GcpCredentialsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.GcpCredentialsOrBuilder)` |   
  
### getNvidiaAttestation()
    
    
    public NvidiaAttestation getNvidiaAttestation()

Optional. An optional Nvidia attestation report, used to populate hardware rooted claims for Nvidia devices.

` .google.cloud.confidentialcomputing.v1.NvidiaAttestation nvidia_attestation = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[NvidiaAttestation](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.NvidiaAttestation)` | The nvidiaAttestation.  
  
### getNvidiaAttestationOrBuilder()
    
    
    public NvidiaAttestationOrBuilder getNvidiaAttestationOrBuilder()

Optional. An optional Nvidia attestation report, used to populate hardware rooted claims for Nvidia devices.

` .google.cloud.confidentialcomputing.v1.NvidiaAttestation nvidia_attestation = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[NvidiaAttestationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.NvidiaAttestationOrBuilder)` |   
  
### getOptions()
    
    
    public VerifyConfidentialSpaceRequest.ConfidentialSpaceOptions getOptions()

Optional. A collection of fields that modify the token output.

` .google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest.ConfidentialSpaceOptions options = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialSpaceRequest.ConfidentialSpaceOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest.ConfidentialSpaceOptions)` | The options.  
  
### getOptionsOrBuilder()
    
    
    public VerifyConfidentialSpaceRequest.ConfidentialSpaceOptionsOrBuilder getOptionsOrBuilder()

Optional. A collection of fields that modify the token output.

` .google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest.ConfidentialSpaceOptions options = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialSpaceRequest.ConfidentialSpaceOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest.ConfidentialSpaceOptionsOrBuilder)` |   
  
### getParserForType()
    
    
    public Parser<VerifyConfidentialSpaceRequest> getParserForType()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[VerifyConfidentialSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest)>` |   
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

### getSignedEntities(int index)
    
    
    public SignedEntity getSignedEntities(int index)

Optional. A list of signed entities containing container image signatures that can be used for server-side signature verification.

` repeated .google.cloud.confidentialcomputing.v1.SignedEntity signed_entities = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SignedEntity](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.SignedEntity)` |   
  
### getSignedEntitiesCount()
    
    
    public int getSignedEntitiesCount()

Optional. A list of signed entities containing container image signatures that can be used for server-side signature verification.

` repeated .google.cloud.confidentialcomputing.v1.SignedEntity signed_entities = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSignedEntitiesList()
    
    
    public List<SignedEntity> getSignedEntitiesList()

Optional. A list of signed entities containing container image signatures that can be used for server-side signature verification.

` repeated .google.cloud.confidentialcomputing.v1.SignedEntity signed_entities = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SignedEntity](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.SignedEntity)>` |   
  
### getSignedEntitiesOrBuilder(int index)
    
    
    public SignedEntityOrBuilder getSignedEntitiesOrBuilder(int index)

Optional. A list of signed entities containing container image signatures that can be used for server-side signature verification.

` repeated .google.cloud.confidentialcomputing.v1.SignedEntity signed_entities = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SignedEntityOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.SignedEntityOrBuilder)` |   
  
### getSignedEntitiesOrBuilderList()
    
    
    public List<? extends SignedEntityOrBuilder> getSignedEntitiesOrBuilderList()

Optional. A list of signed entities containing container image signatures that can be used for server-side signature verification.

` repeated .google.cloud.confidentialcomputing.v1.SignedEntity signed_entities = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.confidentialcomputing.v1.SignedEntityOrBuilder>` |   
  
### getTdCcel()
    
    
    public TdxCcelAttestation getTdCcel()

Input only. A TDX with CCEL and RTMR Attestation Quote.

` .google.cloud.confidentialcomputing.v1.TdxCcelAttestation td_ccel = 3 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TdxCcelAttestation](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.TdxCcelAttestation)` | The tdCcel.  
  
### getTdCcelOrBuilder()
    
    
    public TdxCcelAttestationOrBuilder getTdCcelOrBuilder()

Input only. A TDX with CCEL and RTMR Attestation Quote.

` .google.cloud.confidentialcomputing.v1.TdxCcelAttestation td_ccel = 3 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TdxCcelAttestationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.TdxCcelAttestationOrBuilder)` |   
  
### getTeeAttestationCase()
    
    
    public VerifyConfidentialSpaceRequest.TeeAttestationCase getTeeAttestationCase()

**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialSpaceRequest.TeeAttestationCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest.TeeAttestationCase)` |   
  
### getTpmAttestation()
    
    
    public TpmAttestation getTpmAttestation()

Input only. The TPM-specific data provided by the attesting platform, used to populate any of the claims regarding platform state.

` .google.cloud.confidentialcomputing.v1.TpmAttestation tpm_attestation = 4 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TpmAttestation](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.TpmAttestation)` | The tpmAttestation.  
  
### getTpmAttestationOrBuilder()
    
    
    public TpmAttestationOrBuilder getTpmAttestationOrBuilder()

Input only. The TPM-specific data provided by the attesting platform, used to populate any of the claims regarding platform state.

` .google.cloud.confidentialcomputing.v1.TpmAttestation tpm_attestation = 4 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TpmAttestationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.TpmAttestationOrBuilder)` |   
  
### hasGceShieldedIdentity()
    
    
    public boolean hasGceShieldedIdentity()

Optional. Information about the associated Compute Engine instance. Required for td_ccel requests only - tpm_attestation requests will provide this information in the attestation.

` .google.cloud.confidentialcomputing.v1.GceShieldedIdentity gce_shielded_identity = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gceShieldedIdentity field is set.  
  
### hasGcpCredentials()
    
    
    public boolean hasGcpCredentials()

Optional. Credentials used to populate the "emails" claim in the claims_token. If not present, token will not contain the "emails" claim.

` .google.cloud.confidentialcomputing.v1.GcpCredentials gcp_credentials = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gcpCredentials field is set.  
  
### hasNvidiaAttestation()
    
    
    public boolean hasNvidiaAttestation()

Optional. An optional Nvidia attestation report, used to populate hardware rooted claims for Nvidia devices.

` .google.cloud.confidentialcomputing.v1.NvidiaAttestation nvidia_attestation = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the nvidiaAttestation field is set.  
  
### hasOptions()
    
    
    public boolean hasOptions()

Optional. A collection of fields that modify the token output.

` .google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest.ConfidentialSpaceOptions options = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the options field is set.  
  
### hasTdCcel()
    
    
    public boolean hasTdCcel()

Input only. A TDX with CCEL and RTMR Attestation Quote.

` .google.cloud.confidentialcomputing.v1.TdxCcelAttestation td_ccel = 3 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the tdCcel field is set.  
  
### hasTpmAttestation()
    
    
    public boolean hasTpmAttestation()

Input only. The TPM-specific data provided by the attesting platform, used to populate any of the claims regarding platform state.

` .google.cloud.confidentialcomputing.v1.TpmAttestation tpm_attestation = 4 [(.google.api.field_behavior) = INPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the tpmAttestation field is set.  
  
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
    
    
    public VerifyConfidentialSpaceRequest.Builder newBuilderForType()

**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialSpaceRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest.Builder)` |   
  
### newBuilderForType(AbstractMessage.BuilderParent parent)
    
    
    protected VerifyConfidentialSpaceRequest.Builder newBuilderForType(AbstractMessage.BuilderParent parent)

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[BuilderParent](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.BuilderParent.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialSpaceRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest.Builder)` |   
**Overrides**

[AbstractMessage.newBuilderForType(AbstractMessage.BuilderParent parent)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_newBuilderForType_com_google_protobuf_AbstractMessage_BuilderParent_)

### toBuilder()
    
    
    public VerifyConfidentialSpaceRequest.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialSpaceRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-confidentialcomputing/latest/com.google.cloud.confidentialcomputing.v1.VerifyConfidentialSpaceRequest.Builder)` |   
  
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
