---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection
title: Class Collection (0.7.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:31:30.760893+00:00
---

# Class Collection (0.7.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Collection (0.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.0 (latest)  0.3.0  0.2.0  0.1.0 
    
    
    public final class Collection extends GeneratedMessage implements CollectionOrBuilder

Collection represents a container of objects (such as events, entity context metadata, detection finding metadata) and state (such as investigation details).

An example use case for Collection is to model a detection and investigation from detection finding metadata to investigative state collected in the course of the investigation. For more complex investigation and response workflows a Collection could represent an incident consisting of multiple child findings or incidents. This can be expanded on to model remediation elements of a full detection and response workflow.

Protobuf type `google.backstory.Collection`

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html) > [AbstractMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html) > [GeneratedMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html) > Collection

## Implements

[CollectionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.CollectionOrBuilder)

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

### CASE_NAME_FIELD_NUMBER
    
    
    public static final int CASE_NAME_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### COLLECTION_ELEMENTS_FIELD_NUMBER
    
    
    public static final int COLLECTION_ELEMENTS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### CREATED_TIME_FIELD_NUMBER
    
    
    public static final int CREATED_TIME_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### DATA_ACCESS_SCOPE_FIELD_NUMBER
    
    
    public static final int DATA_ACCESS_SCOPE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### DETECTION_FIELD_NUMBER
    
    
    public static final int DETECTION_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### DETECTION_TIME_FIELD_NUMBER
    
    
    public static final int DETECTION_TIME_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### DETECTION_TIMING_DETAILS_FIELD_NUMBER
    
    
    public static final int DETECTION_TIMING_DETAILS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### ID_FIELD_NUMBER
    
    
    public static final int ID_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### ID_NAMESPACE_FIELD_NUMBER
    
    
    public static final int ID_NAMESPACE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### INVESTIGATION_FIELD_NUMBER
    
    
    public static final int INVESTIGATION_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### LAST_UPDATED_TIME_FIELD_NUMBER
    
    
    public static final int LAST_UPDATED_TIME_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### LATENCY_METRICS_FIELD_NUMBER
    
    
    public static final int LATENCY_METRICS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### RESPONSE_PLATFORM_INFO_FIELD_NUMBER
    
    
    public static final int RESPONSE_PLATFORM_INFO_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### RULE_RUN_FREQUENCY_FIELD_NUMBER
    
    
    public static final int RULE_RUN_FREQUENCY_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SIMULATED_EVENT_COUNT_FIELD_NUMBER
    
    
    public static final int SIMULATED_EVENT_COUNT_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SIMULATED_EVENT_NAMES_FIELD_NUMBER
    
    
    public static final int SIMULATED_EVENT_NAMES_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SOAR_ALERT_FIELD_NUMBER
    
    
    public static final int SOAR_ALERT_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SOAR_ALERT_METADATA_FIELD_NUMBER
    
    
    public static final int SOAR_ALERT_METADATA_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### TAGS_FIELD_NUMBER
    
    
    public static final int TAGS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### TIME_WINDOW_FIELD_NUMBER
    
    
    public static final int TIME_WINDOW_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### TYPE_FIELD_NUMBER
    
    
    public static final int TYPE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Static Methods 

### getDefaultInstance()
    
    
    public static Collection getDefaultInstance()

**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection)` |   
  
### getDescriptor()
    
    
    public static final Descriptors.Descriptor getDescriptor()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
  
### newBuilder()
    
    
    public static Collection.Builder newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[Collection.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection.Builder)` |   
  
### newBuilder(Collection prototype)
    
    
    public static Collection.Builder newBuilder(Collection prototype)

**Parameter**  
---  
**Name** | **Description**  
`prototype` | `[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Collection.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection.Builder)` |   
  
### parseDelimitedFrom(InputStream input)
    
    
    public static Collection parseDelimitedFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static Collection parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(byte[] data)
    
    
    public static Collection parseFrom(byte[] data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)
    
    
    public static Collection parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data)
    
    
    public static Collection parseFrom(ByteString data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)
    
    
    public static Collection parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(CodedInputStream input)
    
    
    public static Collection parseFrom(CodedInputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static Collection parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input)
    
    
    public static Collection parseFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static Collection parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(ByteBuffer data)
    
    
    public static Collection parseFrom(ByteBuffer data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)
    
    
    public static Collection parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parser()
    
    
    public static Parser<Collection> parser()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection)>` |   
  
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

### getCaseName()
    
    
    public String getCaseName()

The resource name of the Case that this collection belongs to. Example: projects/{project id}/locations/{region}/chronicle/cases/{internal_case_id}

`string case_name = 14;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The caseName.  
  
### getCaseNameBytes()
    
    
    public ByteString getCaseNameBytes()

The resource name of the Case that this collection belongs to. Example: projects/{project id}/locations/{region}/chronicle/cases/{internal_case_id}

`string case_name = 14;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for caseName.  
  
### getCollectionElements(int index)
    
    
    public Element getCollectionElements(int index)

Constituent elements of the collection. Each element shares an association that groups it together and is a component of the overall collection. For example, a detection collection may have several constituent elements that each share a correlation association that together represent a particular pattern or behavior.

`repeated .google.backstory.Element collection_elements = 9;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Element](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Element)` |   
  
### getCollectionElementsCount()
    
    
    public int getCollectionElementsCount()

Constituent elements of the collection. Each element shares an association that groups it together and is a component of the overall collection. For example, a detection collection may have several constituent elements that each share a correlation association that together represent a particular pattern or behavior.

`repeated .google.backstory.Element collection_elements = 9;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCollectionElementsList()
    
    
    public List<Element> getCollectionElementsList()

Constituent elements of the collection. Each element shares an association that groups it together and is a component of the overall collection. For example, a detection collection may have several constituent elements that each share a correlation association that together represent a particular pattern or behavior.

`repeated .google.backstory.Element collection_elements = 9;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Element](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Element)>` |   
  
### getCollectionElementsOrBuilder(int index)
    
    
    public ElementOrBuilder getCollectionElementsOrBuilder(int index)

Constituent elements of the collection. Each element shares an association that groups it together and is a component of the overall collection. For example, a detection collection may have several constituent elements that each share a correlation association that together represent a particular pattern or behavior.

`repeated .google.backstory.Element collection_elements = 9;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ElementOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.ElementOrBuilder)` |   
  
### getCollectionElementsOrBuilderList()
    
    
    public List<? extends ElementOrBuilder> getCollectionElementsOrBuilderList()

Constituent elements of the collection. Each element shares an association that groups it together and is a component of the overall collection. For example, a detection collection may have several constituent elements that each share a correlation association that together represent a particular pattern or behavior.

`repeated .google.backstory.Element collection_elements = 9;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.backstory.ElementOrBuilder>` |   
  
### getCreatedTime()
    
    
    public Timestamp getCreatedTime()

Time the collection was created.

`.google.protobuf.Timestamp created_time = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createdTime.  
  
### getCreatedTimeOrBuilder()
    
    
    public TimestampOrBuilder getCreatedTimeOrBuilder()

Time the collection was created.

`.google.protobuf.Timestamp created_time = 5;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDataAccessScope()
    
    
    public String getDataAccessScope()

The resource name of the DataAccessScope of this collection.

`string data_access_scope = 19;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The dataAccessScope.  
  
### getDataAccessScopeBytes()
    
    
    public ByteString getDataAccessScopeBytes()

The resource name of the DataAccessScope of this collection.

`string data_access_scope = 19;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for dataAccessScope.  
  
### getDefaultInstanceForType()
    
    
    public Collection getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection)` |   
  
### getDetection(int index)
    
    
    public SecurityResult getDetection(int index)

Detection metadata for findings that represent detections, can include rule details, machine learning model metadata, and indicators implicated in the detection (using the .about field).

`repeated .google.backstory.SecurityResult detection = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.SecurityResult)` |   
  
### getDetectionCount()
    
    
    public int getDetectionCount()

Detection metadata for findings that represent detections, can include rule details, machine learning model metadata, and indicators implicated in the detection (using the .about field).

`repeated .google.backstory.SecurityResult detection = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDetectionList()
    
    
    public List<SecurityResult> getDetectionList()

Detection metadata for findings that represent detections, can include rule details, machine learning model metadata, and indicators implicated in the detection (using the .about field).

`repeated .google.backstory.SecurityResult detection = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SecurityResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.SecurityResult)>` |   
  
### getDetectionOrBuilder(int index)
    
    
    public SecurityResultOrBuilder getDetectionOrBuilder(int index)

Detection metadata for findings that represent detections, can include rule details, machine learning model metadata, and indicators implicated in the detection (using the .about field).

`repeated .google.backstory.SecurityResult detection = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityResultOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.SecurityResultOrBuilder)` |   
  
### getDetectionOrBuilderList()
    
    
    public List<? extends SecurityResultOrBuilder> getDetectionOrBuilderList()

Detection metadata for findings that represent detections, can include rule details, machine learning model metadata, and indicators implicated in the detection (using the .about field).

`repeated .google.backstory.SecurityResult detection = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.backstory.SecurityResultOrBuilder>` |   
  
### getDetectionTime()
    
    
    public Timestamp getDetectionTime()

Timestamp within the time_window related to the time of the collection_elements. For Rule Detections, this timestamp is the end of the the time_window for multi-event rules or the time of the event for single event rules. For late-arriving events that trigger new alerts, the detection_time will be the event time of the event.

`.google.protobuf.Timestamp detection_time = 10;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The detectionTime.  
  
### getDetectionTimeOrBuilder()
    
    
    public TimestampOrBuilder getDetectionTimeOrBuilder()

Timestamp within the time_window related to the time of the collection_elements. For Rule Detections, this timestamp is the end of the the time_window for multi-event rules or the time of the event for single event rules. For late-arriving events that trigger new alerts, the detection_time will be the event time of the event.

`.google.protobuf.Timestamp detection_time = 10;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDetectionTimingDetails(int index)
    
    
    public Collection.DetectionTimingDetails getDetectionTimingDetails(int index)

Detection timing details for the collection. These details are used to determine prossible causes of latency for the detection. This field is only set for detections that are generated by rules.

` repeated .google.backstory.Collection.DetectionTimingDetails detection_timing_details = 20; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[Collection.DetectionTimingDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection.DetectionTimingDetails)` | The detectionTimingDetails at the given index.  
  
### getDetectionTimingDetailsCount()
    
    
    public int getDetectionTimingDetailsCount()

Detection timing details for the collection. These details are used to determine prossible causes of latency for the detection. This field is only set for detections that are generated by rules.

` repeated .google.backstory.Collection.DetectionTimingDetails detection_timing_details = 20; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of detectionTimingDetails.  
  
### getDetectionTimingDetailsList()
    
    
    public List<Collection.DetectionTimingDetails> getDetectionTimingDetailsList()

Detection timing details for the collection. These details are used to determine prossible causes of latency for the detection. This field is only set for detections that are generated by rules.

` repeated .google.backstory.Collection.DetectionTimingDetails detection_timing_details = 20; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[DetectionTimingDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection.DetectionTimingDetails)>` | A list containing the detectionTimingDetails.  
  
### getDetectionTimingDetailsValue(int index)
    
    
    public int getDetectionTimingDetailsValue(int index)

Detection timing details for the collection. These details are used to determine prossible causes of latency for the detection. This field is only set for detections that are generated by rules.

` repeated .google.backstory.Collection.DetectionTimingDetails detection_timing_details = 20; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of detectionTimingDetails at the given index.  
  
### getDetectionTimingDetailsValueList()
    
    
    public List<Integer> getDetectionTimingDetailsValueList()

Detection timing details for the collection. These details are used to determine prossible causes of latency for the detection. This field is only set for detections that are generated by rules.

` repeated .google.backstory.Collection.DetectionTimingDetails detection_timing_details = 20; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for detectionTimingDetails.  
  
### getId()
    
    
    public String getId()

Unique ID for the collection. The ID is specific to the type of collection. For example, with rule detections this is the detection ID.

`string id = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The id.  
  
### getIdBytes()
    
    
    public ByteString getIdBytes()

Unique ID for the collection. The ID is specific to the type of collection. For example, with rule detections this is the detection ID.

`string id = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for id.  
  
### getIdNamespace()
    
    
    public Id.Namespace getIdNamespace()

The ID namespace used for the Collection.

`.google.backstory.Id.Namespace id_namespace = 12;`

**Returns**  
---  
**Type** | **Description**  
`[Id.Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Id.Namespace)` | The idNamespace.  
  
### getIdNamespaceValue()
    
    
    public int getIdNamespaceValue()

The ID namespace used for the Collection.

`.google.backstory.Id.Namespace id_namespace = 12;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for idNamespace.  
  
### getInvestigation()
    
    
    public Investigation getInvestigation()

Consolidated investigation details (categorization, status, etc) typically for collections that begin as detection findings and then evolve with analyst action and feedback into investigations around the detection output.

`.google.backstory.Investigation investigation = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Investigation](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Investigation)` | The investigation.  
  
### getInvestigationOrBuilder()
    
    
    public InvestigationOrBuilder getInvestigationOrBuilder()

Consolidated investigation details (categorization, status, etc) typically for collections that begin as detection findings and then evolve with analyst action and feedback into investigations around the detection output.

`.google.backstory.Investigation investigation = 4;`

**Returns**  
---  
**Type** | **Description**  
`[InvestigationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.InvestigationOrBuilder)` |   
  
### getLastUpdatedTime()
    
    
    public Timestamp getLastUpdatedTime()

Time the collection was last updated.

`.google.protobuf.Timestamp last_updated_time = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The lastUpdatedTime.  
  
### getLastUpdatedTimeOrBuilder()
    
    
    public TimestampOrBuilder getLastUpdatedTimeOrBuilder()

Time the collection was last updated.

`.google.protobuf.Timestamp last_updated_time = 6;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getLatencyMetrics()
    
    
    public LatencyMetrics getLatencyMetrics()

The latency metrics for the specific detection. These metrics are calculated from ALL of the events that contribute to the detection, not just the sampled ones.

`.google.backstory.LatencyMetrics latency_metrics = 21;`

**Returns**  
---  
**Type** | **Description**  
`[LatencyMetrics](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.LatencyMetrics)` | The latencyMetrics.  
  
### getLatencyMetricsOrBuilder()
    
    
    public LatencyMetricsOrBuilder getLatencyMetricsOrBuilder()

The latency metrics for the specific detection. These metrics are calculated from ALL of the events that contribute to the detection, not just the sampled ones.

`.google.backstory.LatencyMetrics latency_metrics = 21;`

**Returns**  
---  
**Type** | **Description**  
`[LatencyMetricsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.LatencyMetricsOrBuilder)` |   
  
### getParserForType()
    
    
    public Parser<Collection> getParserForType()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[Collection](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection)>` |   
**Overrides**

[GeneratedMessage.getParserForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getParserForType__)

### getResponsePlatformInfo()
    
    
    public ResponsePlatformInfo getResponsePlatformInfo()

Alert related info of this same alert in customer's SOAR platform.

`.google.backstory.ResponsePlatformInfo response_platform_info = 13;`

**Returns**  
---  
**Type** | **Description**  
`[ResponsePlatformInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.ResponsePlatformInfo)` | The responsePlatformInfo.  
  
### getResponsePlatformInfoOrBuilder()
    
    
    public ResponsePlatformInfoOrBuilder getResponsePlatformInfoOrBuilder()

Alert related info of this same alert in customer's SOAR platform.

`.google.backstory.ResponsePlatformInfo response_platform_info = 13;`

**Returns**  
---  
**Type** | **Description**  
`[ResponsePlatformInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.ResponsePlatformInfoOrBuilder)` |   
  
### getRuleRunFrequency()
    
    
    public Collection.RunFrequency getRuleRunFrequency()

The run frequency of the rule when it generated the detection.

`.google.backstory.Collection.RunFrequency rule_run_frequency = 22;`

**Returns**  
---  
**Type** | **Description**  
`[Collection.RunFrequency](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection.RunFrequency)` | The ruleRunFrequency.  
  
### getRuleRunFrequencyValue()
    
    
    public int getRuleRunFrequencyValue()

The run frequency of the rule when it generated the detection.

`.google.backstory.Collection.RunFrequency rule_run_frequency = 22;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for ruleRunFrequency.  
  
### getSerializedSize()
    
    
    public int getSerializedSize()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.getSerializedSize()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getSerializedSize__)

### getSimulatedEventCount()
    
    
    public long getSimulatedEventCount()

The total number of simulated events that contributed to this detection. Simulated events are realistic threat sequences (Raw Logs or UDM) programmatically delivered into the production ingestion pipeline to verify the entire detection lifecycle—from identification to action.

`int64 simulated_event_count = 23;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The simulatedEventCount.  
  
### getSimulatedEventNames(int index)
    
    
    public String getSimulatedEventNames(int index)

The set of all values from event ingestion_labels where SIMULATED is set as the key, for all simulated events that participated in this detection.

`repeated string simulated_event_names = 24;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The simulatedEventNames at the given index.  
  
### getSimulatedEventNamesBytes(int index)
    
    
    public ByteString getSimulatedEventNamesBytes(int index)

The set of all values from event ingestion_labels where SIMULATED is set as the key, for all simulated events that participated in this detection.

`repeated string simulated_event_names = 24;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the simulatedEventNames at the given index.  
  
### getSimulatedEventNamesCount()
    
    
    public int getSimulatedEventNamesCount()

The set of all values from event ingestion_labels where SIMULATED is set as the key, for all simulated events that participated in this detection.

`repeated string simulated_event_names = 24;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of simulatedEventNames.  
  
### getSimulatedEventNamesList()
    
    
    public ProtocolStringList getSimulatedEventNamesList()

The set of all values from event ingestion_labels where SIMULATED is set as the key, for all simulated events that participated in this detection.

`repeated string simulated_event_names = 24;`

**Returns**  
---  
**Type** | **Description**  
`[ProtocolStringList](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolStringList.html)` | A list containing the simulatedEventNames.  
  
### getSoarAlert()
    
    
    public boolean getSoarAlert()

A boolean field indicating that the alert is present in SOAR.

`bool soar_alert = 17;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The soarAlert.  
  
### getSoarAlertMetadata()
    
    
    public SoarAlertMetadata getSoarAlertMetadata()

Metadata fields of alerts coming from other SIEM systems via SOAR.

`.google.backstory.SoarAlertMetadata soar_alert_metadata = 18;`

**Returns**  
---  
**Type** | **Description**  
`[SoarAlertMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.SoarAlertMetadata)` | The soarAlertMetadata.  
  
### getSoarAlertMetadataOrBuilder()
    
    
    public SoarAlertMetadataOrBuilder getSoarAlertMetadataOrBuilder()

Metadata fields of alerts coming from other SIEM systems via SOAR.

`.google.backstory.SoarAlertMetadata soar_alert_metadata = 18;`

**Returns**  
---  
**Type** | **Description**  
`[SoarAlertMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.SoarAlertMetadataOrBuilder)` |   
  
### getTags(int index)
    
    
    public String getTags(int index)

Tags set by UC/DSML/RE for the Finding during creation.

`repeated string tags = 11;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The tags at the given index.  
  
### getTagsBytes(int index)
    
    
    public ByteString getTagsBytes(int index)

Tags set by UC/DSML/RE for the Finding during creation.

`repeated string tags = 11;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the tags at the given index.  
  
### getTagsCount()
    
    
    public int getTagsCount()

Tags set by UC/DSML/RE for the Finding during creation.

`repeated string tags = 11;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of tags.  
  
### getTagsList()
    
    
    public ProtocolStringList getTagsList()

Tags set by UC/DSML/RE for the Finding during creation.

`repeated string tags = 11;`

**Returns**  
---  
**Type** | **Description**  
`[ProtocolStringList](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolStringList.html)` | A list containing the tags.  
  
### getTimeWindow()
    
    
    public Interval getTimeWindow()

Time interval that the collection represents.

`.google.type.Interval time_window = 8;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Interval` | The timeWindow.  
  
### getTimeWindowOrBuilder()
    
    
    public IntervalOrBuilder getTimeWindowOrBuilder()

Time interval that the collection represents.

`.google.type.Interval time_window = 8;`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.IntervalOrBuilder` |   
  
### getType()
    
    
    public Collection.CollectionType getType()

What the collection represents.

`.google.backstory.Collection.CollectionType type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Collection.CollectionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection.CollectionType)` | The type.  
  
### getTypeValue()
    
    
    public int getTypeValue()

What the collection represents.

`.google.backstory.Collection.CollectionType type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for type.  
  
### hasCreatedTime()
    
    
    public boolean hasCreatedTime()

Time the collection was created.

`.google.protobuf.Timestamp created_time = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createdTime field is set.  
  
### hasDetectionTime()
    
    
    public boolean hasDetectionTime()

Timestamp within the time_window related to the time of the collection_elements. For Rule Detections, this timestamp is the end of the the time_window for multi-event rules or the time of the event for single event rules. For late-arriving events that trigger new alerts, the detection_time will be the event time of the event.

`.google.protobuf.Timestamp detection_time = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the detectionTime field is set.  
  
### hasInvestigation()
    
    
    public boolean hasInvestigation()

Consolidated investigation details (categorization, status, etc) typically for collections that begin as detection findings and then evolve with analyst action and feedback into investigations around the detection output.

`.google.backstory.Investigation investigation = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the investigation field is set.  
  
### hasLastUpdatedTime()
    
    
    public boolean hasLastUpdatedTime()

Time the collection was last updated.

`.google.protobuf.Timestamp last_updated_time = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the lastUpdatedTime field is set.  
  
### hasLatencyMetrics()
    
    
    public boolean hasLatencyMetrics()

The latency metrics for the specific detection. These metrics are calculated from ALL of the events that contribute to the detection, not just the sampled ones.

`.google.backstory.LatencyMetrics latency_metrics = 21;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the latencyMetrics field is set.  
  
### hasResponsePlatformInfo()
    
    
    public boolean hasResponsePlatformInfo()

Alert related info of this same alert in customer's SOAR platform.

`.google.backstory.ResponsePlatformInfo response_platform_info = 13;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the responsePlatformInfo field is set.  
  
### hasSoarAlertMetadata()
    
    
    public boolean hasSoarAlertMetadata()

Metadata fields of alerts coming from other SIEM systems via SOAR.

`.google.backstory.SoarAlertMetadata soar_alert_metadata = 18;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the soarAlertMetadata field is set.  
  
### hasTimeWindow()
    
    
    public boolean hasTimeWindow()

Time interval that the collection represents.

`.google.type.Interval time_window = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the timeWindow field is set.  
  
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
    
    
    public Collection.Builder newBuilderForType()

**Returns**  
---  
**Type** | **Description**  
`[Collection.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection.Builder)` |   
  
### newBuilderForType(AbstractMessage.BuilderParent parent)
    
    
    protected Collection.Builder newBuilderForType(AbstractMessage.BuilderParent parent)

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[BuilderParent](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.BuilderParent.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Collection.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection.Builder)` |   
**Overrides**

[AbstractMessage.newBuilderForType(AbstractMessage.BuilderParent parent)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_newBuilderForType_com_google_protobuf_AbstractMessage_BuilderParent_)

### toBuilder()
    
    
    public Collection.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[Collection.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.Collection.Builder)` |   
  
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
