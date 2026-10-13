---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile
title: Class ConnectionProfile (1.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:00.303443+00:00
---

# Class ConnectionProfile (1.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ConnectionProfile (1.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.98.0 (latest)  1.94.0  1.93.0  1.92.0  1.90.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.80.0  1.79.0  1.77.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.0  1.69.0  1.67.0  1.66.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.2  1.1.1  1.0.0  0.4.2 
    
    
    public final class ConnectionProfile extends GeneratedMessage implements ConnectionProfileOrBuilder

A set of reusable connection configurations to be used as a source or destination for a stream.

Protobuf type `google.cloud.datastream.v1.ConnectionProfile`

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html) > [AbstractMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html) > [GeneratedMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html) > ConnectionProfile

## Implements

[ConnectionProfileOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfileOrBuilder)

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

### BIGQUERY_PROFILE_FIELD_NUMBER
    
    
    public static final int BIGQUERY_PROFILE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### CREATE_TIME_FIELD_NUMBER
    
    
    public static final int CREATE_TIME_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### DISPLAY_NAME_FIELD_NUMBER
    
    
    public static final int DISPLAY_NAME_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### FORWARD_SSH_CONNECTIVITY_FIELD_NUMBER
    
    
    public static final int FORWARD_SSH_CONNECTIVITY_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### GCS_PROFILE_FIELD_NUMBER
    
    
    public static final int GCS_PROFILE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### LABELS_FIELD_NUMBER
    
    
    public static final int LABELS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MONGODB_PROFILE_FIELD_NUMBER
    
    
    public static final int MONGODB_PROFILE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MYSQL_PROFILE_FIELD_NUMBER
    
    
    public static final int MYSQL_PROFILE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### NAME_FIELD_NUMBER
    
    
    public static final int NAME_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### ORACLE_PROFILE_FIELD_NUMBER
    
    
    public static final int ORACLE_PROFILE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### POSTGRESQL_PROFILE_FIELD_NUMBER
    
    
    public static final int POSTGRESQL_PROFILE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### PRIVATE_CONNECTIVITY_FIELD_NUMBER
    
    
    public static final int PRIVATE_CONNECTIVITY_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SALESFORCE_PROFILE_FIELD_NUMBER
    
    
    public static final int SALESFORCE_PROFILE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SATISFIES_PZI_FIELD_NUMBER
    
    
    public static final int SATISFIES_PZI_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SATISFIES_PZS_FIELD_NUMBER
    
    
    public static final int SATISFIES_PZS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SQL_SERVER_PROFILE_FIELD_NUMBER
    
    
    public static final int SQL_SERVER_PROFILE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### STATIC_SERVICE_IP_CONNECTIVITY_FIELD_NUMBER
    
    
    public static final int STATIC_SERVICE_IP_CONNECTIVITY_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### UPDATE_TIME_FIELD_NUMBER
    
    
    public static final int UPDATE_TIME_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Static Methods 

### getDefaultInstance()
    
    
    public static ConnectionProfile getDefaultInstance()

**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)` |   
  
### getDescriptor()
    
    
    public static final Descriptors.Descriptor getDescriptor()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
  
### newBuilder()
    
    
    public static ConnectionProfile.Builder newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile.Builder)` |   
  
### newBuilder(ConnectionProfile prototype)
    
    
    public static ConnectionProfile.Builder newBuilder(ConnectionProfile prototype)

**Parameter**  
---  
**Name** | **Description**  
`prototype` | `[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile.Builder)` |   
  
### parseDelimitedFrom(InputStream input)
    
    
    public static ConnectionProfile parseDelimitedFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static ConnectionProfile parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(byte[] data)
    
    
    public static ConnectionProfile parseFrom(byte[] data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)
    
    
    public static ConnectionProfile parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data)
    
    
    public static ConnectionProfile parseFrom(ByteString data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)
    
    
    public static ConnectionProfile parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(CodedInputStream input)
    
    
    public static ConnectionProfile parseFrom(CodedInputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static ConnectionProfile parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input)
    
    
    public static ConnectionProfile parseFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static ConnectionProfile parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(ByteBuffer data)
    
    
    public static ConnectionProfile parseFrom(ByteBuffer data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)
    
    
    public static ConnectionProfile parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parser()
    
    
    public static Parser<ConnectionProfile> parser()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)>` |   
  
## Methods 

### containsLabels(String key)
    
    
    public boolean containsLabels(String key)

Labels.

`map<string, string> labels = 4;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
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

### getBigqueryProfile()
    
    
    public BigQueryProfile getBigqueryProfile()

BigQuery Connection Profile configuration.

`.google.cloud.datastream.v1.BigQueryProfile bigquery_profile = 103;`

**Returns**  
---  
**Type** | **Description**  
`[BigQueryProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.BigQueryProfile)` | The bigqueryProfile.  
  
### getBigqueryProfileOrBuilder()
    
    
    public BigQueryProfileOrBuilder getBigqueryProfileOrBuilder()

BigQuery Connection Profile configuration.

`.google.cloud.datastream.v1.BigQueryProfile bigquery_profile = 103;`

**Returns**  
---  
**Type** | **Description**  
`[BigQueryProfileOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.BigQueryProfileOrBuilder)` |   
  
### getConnectivityCase()
    
    
    public ConnectionProfile.ConnectivityCase getConnectivityCase()

**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile.ConnectivityCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile.ConnectivityCase)` |   
  
### getCreateTime()
    
    
    public Timestamp getCreateTime()

Output only. The create time of the resource.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The create time of the resource.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDefaultInstanceForType()
    
    
    public ConnectionProfile getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)` |   
  
### getDisplayName()
    
    
    public String getDisplayName()

Required. Display name.

`string display_name = 5 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public ByteString getDisplayNameBytes()

Required. Display name.

`string display_name = 5 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getForwardSshConnectivity()
    
    
    public ForwardSshTunnelConnectivity getForwardSshConnectivity()

Forward SSH tunnel connectivity.

`.google.cloud.datastream.v1.ForwardSshTunnelConnectivity forward_ssh_connectivity = 201; `

**Returns**  
---  
**Type** | **Description**  
`[ForwardSshTunnelConnectivity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ForwardSshTunnelConnectivity)` | The forwardSshConnectivity.  
  
### getForwardSshConnectivityOrBuilder()
    
    
    public ForwardSshTunnelConnectivityOrBuilder getForwardSshConnectivityOrBuilder()

Forward SSH tunnel connectivity.

`.google.cloud.datastream.v1.ForwardSshTunnelConnectivity forward_ssh_connectivity = 201; `

**Returns**  
---  
**Type** | **Description**  
`[ForwardSshTunnelConnectivityOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ForwardSshTunnelConnectivityOrBuilder)` |   
  
### getGcsProfile()
    
    
    public GcsProfile getGcsProfile()

Cloud Storage ConnectionProfile configuration.

`.google.cloud.datastream.v1.GcsProfile gcs_profile = 101;`

**Returns**  
---  
**Type** | **Description**  
`[GcsProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.GcsProfile)` | The gcsProfile.  
  
### getGcsProfileOrBuilder()
    
    
    public GcsProfileOrBuilder getGcsProfileOrBuilder()

Cloud Storage ConnectionProfile configuration.

`.google.cloud.datastream.v1.GcsProfile gcs_profile = 101;`

**Returns**  
---  
**Type** | **Description**  
`[GcsProfileOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.GcsProfileOrBuilder)` |   
  
### getLabels() (deprecated)
    
    
    public Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile#com_google_cloud_datastream_v1_ConnectionProfile_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public int getLabelsCount()

Labels.

`map<string, string> labels = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public Map<String,String> getLabelsMap()

Labels.

`map<string, string> labels = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public String getLabelsOrDefault(String key, String defaultValue)

Labels.

`map<string, string> labels = 4;`

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

Labels.

`map<string, string> labels = 4;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMongodbProfile()
    
    
    public MongodbProfile getMongodbProfile()

MongoDB Connection Profile configuration.

`.google.cloud.datastream.v1.MongodbProfile mongodb_profile = 108;`

**Returns**  
---  
**Type** | **Description**  
`[MongodbProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.MongodbProfile)` | The mongodbProfile.  
  
### getMongodbProfileOrBuilder()
    
    
    public MongodbProfileOrBuilder getMongodbProfileOrBuilder()

MongoDB Connection Profile configuration.

`.google.cloud.datastream.v1.MongodbProfile mongodb_profile = 108;`

**Returns**  
---  
**Type** | **Description**  
`[MongodbProfileOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.MongodbProfileOrBuilder)` |   
  
### getMysqlProfile()
    
    
    public MysqlProfile getMysqlProfile()

MySQL ConnectionProfile configuration.

`.google.cloud.datastream.v1.MysqlProfile mysql_profile = 102;`

**Returns**  
---  
**Type** | **Description**  
`[MysqlProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.MysqlProfile)` | The mysqlProfile.  
  
### getMysqlProfileOrBuilder()
    
    
    public MysqlProfileOrBuilder getMysqlProfileOrBuilder()

MySQL ConnectionProfile configuration.

`.google.cloud.datastream.v1.MysqlProfile mysql_profile = 102;`

**Returns**  
---  
**Type** | **Description**  
`[MysqlProfileOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.MysqlProfileOrBuilder)` |   
  
### getName()
    
    
    public String getName()

Output only. Identifier. The resource's name.

` string name = 1 [(.google.api.field_behavior) = IDENTIFIER, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

Output only. Identifier. The resource's name.

` string name = 1 [(.google.api.field_behavior) = IDENTIFIER, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getOracleProfile()
    
    
    public OracleProfile getOracleProfile()

Oracle ConnectionProfile configuration.

`.google.cloud.datastream.v1.OracleProfile oracle_profile = 100;`

**Returns**  
---  
**Type** | **Description**  
`[OracleProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OracleProfile)` | The oracleProfile.  
  
### getOracleProfileOrBuilder()
    
    
    public OracleProfileOrBuilder getOracleProfileOrBuilder()

Oracle ConnectionProfile configuration.

`.google.cloud.datastream.v1.OracleProfile oracle_profile = 100;`

**Returns**  
---  
**Type** | **Description**  
`[OracleProfileOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.OracleProfileOrBuilder)` |   
  
### getParserForType()
    
    
    public Parser<ConnectionProfile> getParserForType()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[ConnectionProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile)>` |   
**Overrides**

[GeneratedMessage.getParserForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getParserForType__)

### getPostgresqlProfile()
    
    
    public PostgresqlProfile getPostgresqlProfile()

PostgreSQL Connection Profile configuration.

`.google.cloud.datastream.v1.PostgresqlProfile postgresql_profile = 104;`

**Returns**  
---  
**Type** | **Description**  
`[PostgresqlProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.PostgresqlProfile)` | The postgresqlProfile.  
  
### getPostgresqlProfileOrBuilder()
    
    
    public PostgresqlProfileOrBuilder getPostgresqlProfileOrBuilder()

PostgreSQL Connection Profile configuration.

`.google.cloud.datastream.v1.PostgresqlProfile postgresql_profile = 104;`

**Returns**  
---  
**Type** | **Description**  
`[PostgresqlProfileOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.PostgresqlProfileOrBuilder)` |   
  
### getPrivateConnectivity()
    
    
    public PrivateConnectivity getPrivateConnectivity()

Private connectivity.

`.google.cloud.datastream.v1.PrivateConnectivity private_connectivity = 202;`

**Returns**  
---  
**Type** | **Description**  
`[PrivateConnectivity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.PrivateConnectivity)` | The privateConnectivity.  
  
### getPrivateConnectivityOrBuilder()
    
    
    public PrivateConnectivityOrBuilder getPrivateConnectivityOrBuilder()

Private connectivity.

`.google.cloud.datastream.v1.PrivateConnectivity private_connectivity = 202;`

**Returns**  
---  
**Type** | **Description**  
`[PrivateConnectivityOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.PrivateConnectivityOrBuilder)` |   
  
### getProfileCase()
    
    
    public ConnectionProfile.ProfileCase getProfileCase()

**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile.ProfileCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile.ProfileCase)` |   
  
### getSalesforceProfile()
    
    
    public SalesforceProfile getSalesforceProfile()

Salesforce Connection Profile configuration.

`.google.cloud.datastream.v1.SalesforceProfile salesforce_profile = 107;`

**Returns**  
---  
**Type** | **Description**  
`[SalesforceProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.SalesforceProfile)` | The salesforceProfile.  
  
### getSalesforceProfileOrBuilder()
    
    
    public SalesforceProfileOrBuilder getSalesforceProfileOrBuilder()

Salesforce Connection Profile configuration.

`.google.cloud.datastream.v1.SalesforceProfile salesforce_profile = 107;`

**Returns**  
---  
**Type** | **Description**  
`[SalesforceProfileOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.SalesforceProfileOrBuilder)` |   
  
### getSatisfiesPzi()
    
    
    public boolean getSatisfiesPzi()

Output only. Reserved for future use.

`optional bool satisfies_pzi = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The satisfiesPzi.  
  
### getSatisfiesPzs()
    
    
    public boolean getSatisfiesPzs()

Output only. Reserved for future use.

`optional bool satisfies_pzs = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The satisfiesPzs.  
  
### getSerializedSize()
    
    
    public int getSerializedSize()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.getSerializedSize()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getSerializedSize__)

### getSqlServerProfile()
    
    
    public SqlServerProfile getSqlServerProfile()

SQLServer Connection Profile configuration.

`.google.cloud.datastream.v1.SqlServerProfile sql_server_profile = 105;`

**Returns**  
---  
**Type** | **Description**  
`[SqlServerProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.SqlServerProfile)` | The sqlServerProfile.  
  
### getSqlServerProfileOrBuilder()
    
    
    public SqlServerProfileOrBuilder getSqlServerProfileOrBuilder()

SQLServer Connection Profile configuration.

`.google.cloud.datastream.v1.SqlServerProfile sql_server_profile = 105;`

**Returns**  
---  
**Type** | **Description**  
`[SqlServerProfileOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.SqlServerProfileOrBuilder)` |   
  
### getStaticServiceIpConnectivity()
    
    
    public StaticServiceIpConnectivity getStaticServiceIpConnectivity()

Static Service IP connectivity.

` .google.cloud.datastream.v1.StaticServiceIpConnectivity static_service_ip_connectivity = 200; `

**Returns**  
---  
**Type** | **Description**  
`[StaticServiceIpConnectivity](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StaticServiceIpConnectivity)` | The staticServiceIpConnectivity.  
  
### getStaticServiceIpConnectivityOrBuilder()
    
    
    public StaticServiceIpConnectivityOrBuilder getStaticServiceIpConnectivityOrBuilder()

Static Service IP connectivity.

` .google.cloud.datastream.v1.StaticServiceIpConnectivity static_service_ip_connectivity = 200; `

**Returns**  
---  
**Type** | **Description**  
`[StaticServiceIpConnectivityOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.StaticServiceIpConnectivityOrBuilder)` |   
  
### getUpdateTime()
    
    
    public Timestamp getUpdateTime()

Output only. The update time of the resource.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The update time of the resource.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasBigqueryProfile()
    
    
    public boolean hasBigqueryProfile()

BigQuery Connection Profile configuration.

`.google.cloud.datastream.v1.BigQueryProfile bigquery_profile = 103;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bigqueryProfile field is set.  
  
### hasCreateTime()
    
    
    public boolean hasCreateTime()

Output only. The create time of the resource.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasForwardSshConnectivity()
    
    
    public boolean hasForwardSshConnectivity()

Forward SSH tunnel connectivity.

`.google.cloud.datastream.v1.ForwardSshTunnelConnectivity forward_ssh_connectivity = 201; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the forwardSshConnectivity field is set.  
  
### hasGcsProfile()
    
    
    public boolean hasGcsProfile()

Cloud Storage ConnectionProfile configuration.

`.google.cloud.datastream.v1.GcsProfile gcs_profile = 101;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gcsProfile field is set.  
  
### hasMongodbProfile()
    
    
    public boolean hasMongodbProfile()

MongoDB Connection Profile configuration.

`.google.cloud.datastream.v1.MongodbProfile mongodb_profile = 108;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the mongodbProfile field is set.  
  
### hasMysqlProfile()
    
    
    public boolean hasMysqlProfile()

MySQL ConnectionProfile configuration.

`.google.cloud.datastream.v1.MysqlProfile mysql_profile = 102;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the mysqlProfile field is set.  
  
### hasOracleProfile()
    
    
    public boolean hasOracleProfile()

Oracle ConnectionProfile configuration.

`.google.cloud.datastream.v1.OracleProfile oracle_profile = 100;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the oracleProfile field is set.  
  
### hasPostgresqlProfile()
    
    
    public boolean hasPostgresqlProfile()

PostgreSQL Connection Profile configuration.

`.google.cloud.datastream.v1.PostgresqlProfile postgresql_profile = 104;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the postgresqlProfile field is set.  
  
### hasPrivateConnectivity()
    
    
    public boolean hasPrivateConnectivity()

Private connectivity.

`.google.cloud.datastream.v1.PrivateConnectivity private_connectivity = 202;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the privateConnectivity field is set.  
  
### hasSalesforceProfile()
    
    
    public boolean hasSalesforceProfile()

Salesforce Connection Profile configuration.

`.google.cloud.datastream.v1.SalesforceProfile salesforce_profile = 107;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the salesforceProfile field is set.  
  
### hasSatisfiesPzi()
    
    
    public boolean hasSatisfiesPzi()

Output only. Reserved for future use.

`optional bool satisfies_pzi = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the satisfiesPzi field is set.  
  
### hasSatisfiesPzs()
    
    
    public boolean hasSatisfiesPzs()

Output only. Reserved for future use.

`optional bool satisfies_pzs = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the satisfiesPzs field is set.  
  
### hasSqlServerProfile()
    
    
    public boolean hasSqlServerProfile()

SQLServer Connection Profile configuration.

`.google.cloud.datastream.v1.SqlServerProfile sql_server_profile = 105;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sqlServerProfile field is set.  
  
### hasStaticServiceIpConnectivity()
    
    
    public boolean hasStaticServiceIpConnectivity()

Static Service IP connectivity.

` .google.cloud.datastream.v1.StaticServiceIpConnectivity static_service_ip_connectivity = 200; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the staticServiceIpConnectivity field is set.  
  
### hasUpdateTime()
    
    
    public boolean hasUpdateTime()

Output only. The update time of the resource.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
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

com.google.protobuf.GeneratedMessage.internalGetMapFieldReflection(int)

### isInitialized()
    
    
    public final boolean isInitialized()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_isInitialized__)

### newBuilderForType()
    
    
    public ConnectionProfile.Builder newBuilderForType()

**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile.Builder)` |   
  
### newBuilderForType(AbstractMessage.BuilderParent parent)
    
    
    protected ConnectionProfile.Builder newBuilderForType(AbstractMessage.BuilderParent parent)

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[BuilderParent](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.BuilderParent.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile.Builder)` |   
**Overrides**

[AbstractMessage.newBuilderForType(AbstractMessage.BuilderParent parent)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_newBuilderForType_com_google_protobuf_AbstractMessage_BuilderParent_)

### toBuilder()
    
    
    public ConnectionProfile.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[ConnectionProfile.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastream/latest/com.google.cloud.datastream.v1.ConnectionProfile.Builder)` |   
  
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
