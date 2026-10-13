---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest
title: Class WebhookRequest (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:32.158617+00:00
---

# Class WebhookRequest (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class WebhookRequest (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.7  0.13.1  0.12.1  0.11.5 
    
    
    public final class WebhookRequest extends GeneratedMessage implements WebhookRequestOrBuilder

The request message for a webhook call. The request is sent as a JSON object and the field names will be presented in camel cases.

You may see undocumented fields in an actual request. These fields are used internally by Dialogflow and should be ignored.

Protobuf type `google.cloud.dialogflow.cx.v3.WebhookRequest`

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html) > [AbstractMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html) > [GeneratedMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html) > WebhookRequest

## Implements

[WebhookRequestOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequestOrBuilder)

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

### DETECT_INTENT_RESPONSE_ID_FIELD_NUMBER
    
    
    public static final int DETECT_INTENT_RESPONSE_ID_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### DTMF_DIGITS_FIELD_NUMBER
    
    
    public static final int DTMF_DIGITS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### FULFILLMENT_INFO_FIELD_NUMBER
    
    
    public static final int FULFILLMENT_INFO_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### INTENT_INFO_FIELD_NUMBER
    
    
    public static final int INTENT_INFO_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### LANGUAGE_CODE_FIELD_NUMBER
    
    
    public static final int LANGUAGE_CODE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### LANGUAGE_INFO_FIELD_NUMBER
    
    
    public static final int LANGUAGE_INFO_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MESSAGES_FIELD_NUMBER
    
    
    public static final int MESSAGES_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### PAGE_INFO_FIELD_NUMBER
    
    
    public static final int PAGE_INFO_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### PAYLOAD_FIELD_NUMBER
    
    
    public static final int PAYLOAD_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SENTIMENT_ANALYSIS_RESULT_FIELD_NUMBER
    
    
    public static final int SENTIMENT_ANALYSIS_RESULT_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SESSION_INFO_FIELD_NUMBER
    
    
    public static final int SESSION_INFO_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### TEXT_FIELD_NUMBER
    
    
    public static final int TEXT_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### TRANSCRIPT_FIELD_NUMBER
    
    
    public static final int TRANSCRIPT_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### TRIGGER_EVENT_FIELD_NUMBER
    
    
    public static final int TRIGGER_EVENT_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### TRIGGER_INTENT_FIELD_NUMBER
    
    
    public static final int TRIGGER_INTENT_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Static Methods 

### getDefaultInstance()
    
    
    public static WebhookRequest getDefaultInstance()

**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest)` |   
  
### getDescriptor()
    
    
    public static final Descriptors.Descriptor getDescriptor()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
  
### newBuilder()
    
    
    public static WebhookRequest.Builder newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest.Builder)` |   
  
### newBuilder(WebhookRequest prototype)
    
    
    public static WebhookRequest.Builder newBuilder(WebhookRequest prototype)

**Parameter**  
---  
**Name** | **Description**  
`prototype` | `[WebhookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest.Builder)` |   
  
### parseDelimitedFrom(InputStream input)
    
    
    public static WebhookRequest parseDelimitedFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static WebhookRequest parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(byte[] data)
    
    
    public static WebhookRequest parseFrom(byte[] data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)
    
    
    public static WebhookRequest parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data)
    
    
    public static WebhookRequest parseFrom(ByteString data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)
    
    
    public static WebhookRequest parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(CodedInputStream input)
    
    
    public static WebhookRequest parseFrom(CodedInputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static WebhookRequest parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input)
    
    
    public static WebhookRequest parseFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static WebhookRequest parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(ByteBuffer data)
    
    
    public static WebhookRequest parseFrom(ByteBuffer data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)
    
    
    public static WebhookRequest parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parser()
    
    
    public static Parser<WebhookRequest> parser()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[WebhookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest)>` |   
  
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
    
    
    public WebhookRequest getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest)` |   
  
### getDetectIntentResponseId()
    
    
    public String getDetectIntentResponseId()

Always present. The unique identifier of the DetectIntentResponse that will be returned to the API caller.

`string detect_intent_response_id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The detectIntentResponseId.  
  
### getDetectIntentResponseIdBytes()
    
    
    public ByteString getDetectIntentResponseIdBytes()

Always present. The unique identifier of the DetectIntentResponse that will be returned to the API caller.

`string detect_intent_response_id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for detectIntentResponseId.  
  
### getDtmfDigits()
    
    
    public String getDtmfDigits()

If DTMF was provided as input, this field will contain the DTMF digits.

`string dtmf_digits = 17;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The dtmfDigits.  
  
### getDtmfDigitsBytes()
    
    
    public ByteString getDtmfDigitsBytes()

If DTMF was provided as input, this field will contain the DTMF digits.

`string dtmf_digits = 17;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for dtmfDigits.  
  
### getFulfillmentInfo()
    
    
    public WebhookRequest.FulfillmentInfo getFulfillmentInfo()

Always present. Information about the fulfillment that triggered this webhook call.

`.google.cloud.dialogflow.cx.v3.WebhookRequest.FulfillmentInfo fulfillment_info = 6; `

**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest.FulfillmentInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest.FulfillmentInfo)` | The fulfillmentInfo.  
  
### getFulfillmentInfoOrBuilder()
    
    
    public WebhookRequest.FulfillmentInfoOrBuilder getFulfillmentInfoOrBuilder()

Always present. Information about the fulfillment that triggered this webhook call.

`.google.cloud.dialogflow.cx.v3.WebhookRequest.FulfillmentInfo fulfillment_info = 6; `

**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest.FulfillmentInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest.FulfillmentInfoOrBuilder)` |   
  
### getIntentInfo()
    
    
    public WebhookRequest.IntentInfo getIntentInfo()

Information about the last matched intent.

`.google.cloud.dialogflow.cx.v3.WebhookRequest.IntentInfo intent_info = 3;`

**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest.IntentInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest.IntentInfo)` | The intentInfo.  
  
### getIntentInfoOrBuilder()
    
    
    public WebhookRequest.IntentInfoOrBuilder getIntentInfoOrBuilder()

Information about the last matched intent.

`.google.cloud.dialogflow.cx.v3.WebhookRequest.IntentInfo intent_info = 3;`

**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest.IntentInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest.IntentInfoOrBuilder)` |   
  
### getLanguageCode()
    
    
    public String getLanguageCode()

The language code specified in the original request.

`string language_code = 15;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The languageCode.  
  
### getLanguageCodeBytes()
    
    
    public ByteString getLanguageCodeBytes()

The language code specified in the original request.

`string language_code = 15;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for languageCode.  
  
### getLanguageInfo()
    
    
    public LanguageInfo getLanguageInfo()

Information about the language of the request.

`.google.cloud.dialogflow.cx.v3.LanguageInfo language_info = 18;`

**Returns**  
---  
**Type** | **Description**  
`[LanguageInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.LanguageInfo)` | The languageInfo.  
  
### getLanguageInfoOrBuilder()
    
    
    public LanguageInfoOrBuilder getLanguageInfoOrBuilder()

Information about the language of the request.

`.google.cloud.dialogflow.cx.v3.LanguageInfo language_info = 18;`

**Returns**  
---  
**Type** | **Description**  
`[LanguageInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.LanguageInfoOrBuilder)` |   
  
### getMessages(int index)
    
    
    public ResponseMessage getMessages(int index)

The list of rich message responses to present to the user. Webhook can choose to append or replace this list in WebhookResponse.fulfillment_response;

`repeated .google.cloud.dialogflow.cx.v3.ResponseMessage messages = 7;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ResponseMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ResponseMessage)` |   
  
### getMessagesCount()
    
    
    public int getMessagesCount()

The list of rich message responses to present to the user. Webhook can choose to append or replace this list in WebhookResponse.fulfillment_response;

`repeated .google.cloud.dialogflow.cx.v3.ResponseMessage messages = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMessagesList()
    
    
    public List<ResponseMessage> getMessagesList()

The list of rich message responses to present to the user. Webhook can choose to append or replace this list in WebhookResponse.fulfillment_response;

`repeated .google.cloud.dialogflow.cx.v3.ResponseMessage messages = 7;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ResponseMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ResponseMessage)>` |   
  
### getMessagesOrBuilder(int index)
    
    
    public ResponseMessageOrBuilder getMessagesOrBuilder(int index)

The list of rich message responses to present to the user. Webhook can choose to append or replace this list in WebhookResponse.fulfillment_response;

`repeated .google.cloud.dialogflow.cx.v3.ResponseMessage messages = 7;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ResponseMessageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ResponseMessageOrBuilder)` |   
  
### getMessagesOrBuilderList()
    
    
    public List<? extends ResponseMessageOrBuilder> getMessagesOrBuilderList()

The list of rich message responses to present to the user. Webhook can choose to append or replace this list in WebhookResponse.fulfillment_response;

`repeated .google.cloud.dialogflow.cx.v3.ResponseMessage messages = 7;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dialogflow.cx.v3.ResponseMessageOrBuilder>` |   
  
### getPageInfo()
    
    
    public PageInfo getPageInfo()

Information about page status.

`.google.cloud.dialogflow.cx.v3.PageInfo page_info = 4;`

**Returns**  
---  
**Type** | **Description**  
`[PageInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PageInfo)` | The pageInfo.  
  
### getPageInfoOrBuilder()
    
    
    public PageInfoOrBuilder getPageInfoOrBuilder()

Information about page status.

`.google.cloud.dialogflow.cx.v3.PageInfo page_info = 4;`

**Returns**  
---  
**Type** | **Description**  
`[PageInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PageInfoOrBuilder)` |   
  
### getParserForType()
    
    
    public Parser<WebhookRequest> getParserForType()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[WebhookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest)>` |   
**Overrides**

[GeneratedMessage.getParserForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getParserForType__)

### getPayload()
    
    
    public Struct getPayload()

Custom data set in QueryParameters.payload.

`.google.protobuf.Struct payload = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` | The payload.  
  
### getPayloadOrBuilder()
    
    
    public StructOrBuilder getPayloadOrBuilder()

Custom data set in QueryParameters.payload.

`.google.protobuf.Struct payload = 8;`

**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getQueryCase()
    
    
    public WebhookRequest.QueryCase getQueryCase()

**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest.QueryCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest.QueryCase)` |   
  
### getSentimentAnalysisResult()
    
    
    public WebhookRequest.SentimentAnalysisResult getSentimentAnalysisResult()

The sentiment analysis result of the current user request. The field is filled when sentiment analysis is configured to be enabled for the request.

` .google.cloud.dialogflow.cx.v3.WebhookRequest.SentimentAnalysisResult sentiment_analysis_result = 9; `

**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest.SentimentAnalysisResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest.SentimentAnalysisResult)` | The sentimentAnalysisResult.  
  
### getSentimentAnalysisResultOrBuilder()
    
    
    public WebhookRequest.SentimentAnalysisResultOrBuilder getSentimentAnalysisResultOrBuilder()

The sentiment analysis result of the current user request. The field is filled when sentiment analysis is configured to be enabled for the request.

` .google.cloud.dialogflow.cx.v3.WebhookRequest.SentimentAnalysisResult sentiment_analysis_result = 9; `

**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest.SentimentAnalysisResultOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest.SentimentAnalysisResultOrBuilder)` |   
  
### getSerializedSize()
    
    
    public int getSerializedSize()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.getSerializedSize()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getSerializedSize__)

### getSessionInfo()
    
    
    public SessionInfo getSessionInfo()

Information about session status.

`.google.cloud.dialogflow.cx.v3.SessionInfo session_info = 5;`

**Returns**  
---  
**Type** | **Description**  
`[SessionInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionInfo)` | The sessionInfo.  
  
### getSessionInfoOrBuilder()
    
    
    public SessionInfoOrBuilder getSessionInfoOrBuilder()

Information about session status.

`.google.cloud.dialogflow.cx.v3.SessionInfo session_info = 5;`

**Returns**  
---  
**Type** | **Description**  
`[SessionInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.SessionInfoOrBuilder)` |   
  
### getText()
    
    
    public String getText()

If natural language text was provided as input, this field will contain a copy of the text.

`string text = 10;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The text.  
  
### getTextBytes()
    
    
    public ByteString getTextBytes()

If natural language text was provided as input, this field will contain a copy of the text.

`string text = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for text.  
  
### getTranscript()
    
    
    public String getTranscript()

If natural language speech audio was provided as input, this field will contain the transcript for the audio.

`string transcript = 12;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The transcript.  
  
### getTranscriptBytes()
    
    
    public ByteString getTranscriptBytes()

If natural language speech audio was provided as input, this field will contain the transcript for the audio.

`string transcript = 12;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for transcript.  
  
### getTriggerEvent()
    
    
    public String getTriggerEvent()

If an event was provided as input, this field will contain the name of the event.

`string trigger_event = 14;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The triggerEvent.  
  
### getTriggerEventBytes()
    
    
    public ByteString getTriggerEventBytes()

If an event was provided as input, this field will contain the name of the event.

`string trigger_event = 14;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for triggerEvent.  
  
### getTriggerIntent()
    
    
    public String getTriggerIntent()

If an intent was provided as input, this field will contain a copy of the intent identifier. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/intents/<IntentID>`.

`string trigger_intent = 11 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The triggerIntent.  
  
### getTriggerIntentBytes()
    
    
    public ByteString getTriggerIntentBytes()

If an intent was provided as input, this field will contain a copy of the intent identifier. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/intents/<IntentID>`.

`string trigger_intent = 11 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for triggerIntent.  
  
### hasDtmfDigits()
    
    
    public boolean hasDtmfDigits()

If DTMF was provided as input, this field will contain the DTMF digits.

`string dtmf_digits = 17;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the dtmfDigits field is set.  
  
### hasFulfillmentInfo()
    
    
    public boolean hasFulfillmentInfo()

Always present. Information about the fulfillment that triggered this webhook call.

`.google.cloud.dialogflow.cx.v3.WebhookRequest.FulfillmentInfo fulfillment_info = 6; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the fulfillmentInfo field is set.  
  
### hasIntentInfo()
    
    
    public boolean hasIntentInfo()

Information about the last matched intent.

`.google.cloud.dialogflow.cx.v3.WebhookRequest.IntentInfo intent_info = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the intentInfo field is set.  
  
### hasLanguageInfo()
    
    
    public boolean hasLanguageInfo()

Information about the language of the request.

`.google.cloud.dialogflow.cx.v3.LanguageInfo language_info = 18;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the languageInfo field is set.  
  
### hasPageInfo()
    
    
    public boolean hasPageInfo()

Information about page status.

`.google.cloud.dialogflow.cx.v3.PageInfo page_info = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pageInfo field is set.  
  
### hasPayload()
    
    
    public boolean hasPayload()

Custom data set in QueryParameters.payload.

`.google.protobuf.Struct payload = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the payload field is set.  
  
### hasSentimentAnalysisResult()
    
    
    public boolean hasSentimentAnalysisResult()

The sentiment analysis result of the current user request. The field is filled when sentiment analysis is configured to be enabled for the request.

` .google.cloud.dialogflow.cx.v3.WebhookRequest.SentimentAnalysisResult sentiment_analysis_result = 9; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sentimentAnalysisResult field is set.  
  
### hasSessionInfo()
    
    
    public boolean hasSessionInfo()

Information about session status.

`.google.cloud.dialogflow.cx.v3.SessionInfo session_info = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sessionInfo field is set.  
  
### hasText()
    
    
    public boolean hasText()

If natural language text was provided as input, this field will contain a copy of the text.

`string text = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the text field is set.  
  
### hasTranscript()
    
    
    public boolean hasTranscript()

If natural language speech audio was provided as input, this field will contain the transcript for the audio.

`string transcript = 12;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the transcript field is set.  
  
### hasTriggerEvent()
    
    
    public boolean hasTriggerEvent()

If an event was provided as input, this field will contain the name of the event.

`string trigger_event = 14;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the triggerEvent field is set.  
  
### hasTriggerIntent()
    
    
    public boolean hasTriggerIntent()

If an intent was provided as input, this field will contain a copy of the intent identifier. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/intents/<IntentID>`.

`string trigger_intent = 11 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the triggerIntent field is set.  
  
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
    
    
    public WebhookRequest.Builder newBuilderForType()

**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest.Builder)` |   
  
### newBuilderForType(AbstractMessage.BuilderParent parent)
    
    
    protected WebhookRequest.Builder newBuilderForType(AbstractMessage.BuilderParent parent)

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[BuilderParent](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.BuilderParent.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest.Builder)` |   
**Overrides**

[AbstractMessage.newBuilderForType(AbstractMessage.BuilderParent parent)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_newBuilderForType_com_google_protobuf_AbstractMessage_BuilderParent_)

### toBuilder()
    
    
    public WebhookRequest.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[WebhookRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.WebhookRequest.Builder)` |   
  
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
