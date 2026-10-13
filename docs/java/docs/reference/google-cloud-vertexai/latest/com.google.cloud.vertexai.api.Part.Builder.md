---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder
title: Class Part.Builder (1.48.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:45.416385+00:00
---

# Class Part.Builder (1.48.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Part.Builder (1.48.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.48.0 (latest)  1.47.0  1.45.0  1.43.0  1.42.0  1.40.0  1.38.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.30.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.20.1  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class Part.Builder extends GeneratedMessage.Builder<Part.Builder> implements PartOrBuilder

A datatype containing media that is part of a multi-part `Content` message.

A `Part` consists of data which has an associated datatype. A `Part` can only contain one of the accepted types in `Part.data`.

A `Part` must have a fixed IANA MIME type identifying the type and subtype of the media if `inline_data` or `file_data` field is filled with raw bytes.

Protobuf type `google.cloud.vertexai.v1.Part`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > Part.Builder

## Implements

[PartOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.PartOrBuilder)

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
    
    
    public Part build()

**Returns**  
---  
**Type** | **Description**  
`[Part](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part)` |   
  
### buildPartial()
    
    
    public Part buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[Part](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part)` |   
  
### clear()
    
    
    public Part.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearCodeExecutionResult()
    
    
    public Part.Builder clearCodeExecutionResult()

Optional. Result of executing the [ExecutableCode].

` .google.cloud.vertexai.v1.CodeExecutionResult code_execution_result = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### clearData()
    
    
    public Part.Builder clearData()

**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### clearExecutableCode()
    
    
    public Part.Builder clearExecutableCode()

Optional. Code generated by the model that is meant to be executed.

` .google.cloud.vertexai.v1.ExecutableCode executable_code = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### clearFileData()
    
    
    public Part.Builder clearFileData()

Optional. URI based data.

` .google.cloud.vertexai.v1.FileData file_data = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### clearFunctionCall()
    
    
    public Part.Builder clearFunctionCall()

Optional. A predicted [FunctionCall] returned from the model that contains a string representing the [FunctionDeclaration.name] with the parameters and their values.

` .google.cloud.vertexai.v1.FunctionCall function_call = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### clearFunctionResponse()
    
    
    public Part.Builder clearFunctionResponse()

Optional. The result output of a [FunctionCall] that contains a string representing the [FunctionDeclaration.name] and a structured JSON object containing any output from the function call. It is used as context to the model.

` .google.cloud.vertexai.v1.FunctionResponse function_response = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### clearInlineData()
    
    
    public Part.Builder clearInlineData()

Optional. Inlined bytes data.

` .google.cloud.vertexai.v1.Blob inline_data = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### clearMetadata()
    
    
    public Part.Builder clearMetadata()

**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### clearText()
    
    
    public Part.Builder clearText()

Optional. Text part (can be code).

`string text = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` | This builder for chaining.  
  
### clearThought()
    
    
    public Part.Builder clearThought()

Indicates if the part is thought from the model.

`bool thought = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` | This builder for chaining.  
  
### clearThoughtSignature()
    
    
    public Part.Builder clearThoughtSignature()

An opaque signature for the thought so it can be reused in subsequent requests.

`bytes thought_signature = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` | This builder for chaining.  
  
### clearVideoMetadata()
    
    
    public Part.Builder clearVideoMetadata()

Optional. Video metadata. The metadata should only be specified while the video data is presented in inline_data or file_data.

` .google.cloud.vertexai.v1.VideoMetadata video_metadata = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### getCodeExecutionResult()
    
    
    public CodeExecutionResult getCodeExecutionResult()

Optional. Result of executing the [ExecutableCode].

` .google.cloud.vertexai.v1.CodeExecutionResult code_execution_result = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CodeExecutionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.CodeExecutionResult)` | The codeExecutionResult.  
  
### getCodeExecutionResultBuilder()
    
    
    public CodeExecutionResult.Builder getCodeExecutionResultBuilder()

Optional. Result of executing the [ExecutableCode].

` .google.cloud.vertexai.v1.CodeExecutionResult code_execution_result = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CodeExecutionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.CodeExecutionResult.Builder)` |   
  
### getCodeExecutionResultOrBuilder()
    
    
    public CodeExecutionResultOrBuilder getCodeExecutionResultOrBuilder()

Optional. Result of executing the [ExecutableCode].

` .google.cloud.vertexai.v1.CodeExecutionResult code_execution_result = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CodeExecutionResultOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.CodeExecutionResultOrBuilder)` |   
  
### getDataCase()
    
    
    public Part.DataCase getDataCase()

**Returns**  
---  
**Type** | **Description**  
`[Part.DataCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.DataCase)` |   
  
### getDefaultInstanceForType()
    
    
    public Part getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Part](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getExecutableCode()
    
    
    public ExecutableCode getExecutableCode()

Optional. Code generated by the model that is meant to be executed.

` .google.cloud.vertexai.v1.ExecutableCode executable_code = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ExecutableCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.ExecutableCode)` | The executableCode.  
  
### getExecutableCodeBuilder()
    
    
    public ExecutableCode.Builder getExecutableCodeBuilder()

Optional. Code generated by the model that is meant to be executed.

` .google.cloud.vertexai.v1.ExecutableCode executable_code = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ExecutableCode.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.ExecutableCode.Builder)` |   
  
### getExecutableCodeOrBuilder()
    
    
    public ExecutableCodeOrBuilder getExecutableCodeOrBuilder()

Optional. Code generated by the model that is meant to be executed.

` .google.cloud.vertexai.v1.ExecutableCode executable_code = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ExecutableCodeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.ExecutableCodeOrBuilder)` |   
  
### getFileData()
    
    
    public FileData getFileData()

Optional. URI based data.

` .google.cloud.vertexai.v1.FileData file_data = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FileData](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.FileData)` | The fileData.  
  
### getFileDataBuilder()
    
    
    public FileData.Builder getFileDataBuilder()

Optional. URI based data.

` .google.cloud.vertexai.v1.FileData file_data = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FileData.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.FileData.Builder)` |   
  
### getFileDataOrBuilder()
    
    
    public FileDataOrBuilder getFileDataOrBuilder()

Optional. URI based data.

` .google.cloud.vertexai.v1.FileData file_data = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FileDataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.FileDataOrBuilder)` |   
  
### getFunctionCall()
    
    
    public FunctionCall getFunctionCall()

Optional. A predicted [FunctionCall] returned from the model that contains a string representing the [FunctionDeclaration.name] with the parameters and their values.

` .google.cloud.vertexai.v1.FunctionCall function_call = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FunctionCall](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.FunctionCall)` | The functionCall.  
  
### getFunctionCallBuilder()
    
    
    public FunctionCall.Builder getFunctionCallBuilder()

Optional. A predicted [FunctionCall] returned from the model that contains a string representing the [FunctionDeclaration.name] with the parameters and their values.

` .google.cloud.vertexai.v1.FunctionCall function_call = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FunctionCall.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.FunctionCall.Builder)` |   
  
### getFunctionCallOrBuilder()
    
    
    public FunctionCallOrBuilder getFunctionCallOrBuilder()

Optional. A predicted [FunctionCall] returned from the model that contains a string representing the [FunctionDeclaration.name] with the parameters and their values.

` .google.cloud.vertexai.v1.FunctionCall function_call = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FunctionCallOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.FunctionCallOrBuilder)` |   
  
### getFunctionResponse()
    
    
    public FunctionResponse getFunctionResponse()

Optional. The result output of a [FunctionCall] that contains a string representing the [FunctionDeclaration.name] and a structured JSON object containing any output from the function call. It is used as context to the model.

` .google.cloud.vertexai.v1.FunctionResponse function_response = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FunctionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.FunctionResponse)` | The functionResponse.  
  
### getFunctionResponseBuilder()
    
    
    public FunctionResponse.Builder getFunctionResponseBuilder()

Optional. The result output of a [FunctionCall] that contains a string representing the [FunctionDeclaration.name] and a structured JSON object containing any output from the function call. It is used as context to the model.

` .google.cloud.vertexai.v1.FunctionResponse function_response = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FunctionResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.FunctionResponse.Builder)` |   
  
### getFunctionResponseOrBuilder()
    
    
    public FunctionResponseOrBuilder getFunctionResponseOrBuilder()

Optional. The result output of a [FunctionCall] that contains a string representing the [FunctionDeclaration.name] and a structured JSON object containing any output from the function call. It is used as context to the model.

` .google.cloud.vertexai.v1.FunctionResponse function_response = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FunctionResponseOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.FunctionResponseOrBuilder)` |   
  
### getInlineData()
    
    
    public Blob getInlineData()

Optional. Inlined bytes data.

` .google.cloud.vertexai.v1.Blob inline_data = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Blob)` | The inlineData.  
  
### getInlineDataBuilder()
    
    
    public Blob.Builder getInlineDataBuilder()

Optional. Inlined bytes data.

` .google.cloud.vertexai.v1.Blob inline_data = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Blob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Blob.Builder)` |   
  
### getInlineDataOrBuilder()
    
    
    public BlobOrBuilder getInlineDataOrBuilder()

Optional. Inlined bytes data.

` .google.cloud.vertexai.v1.Blob inline_data = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[BlobOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.BlobOrBuilder)` |   
  
### getMetadataCase()
    
    
    public Part.MetadataCase getMetadataCase()

**Returns**  
---  
**Type** | **Description**  
`[Part.MetadataCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.MetadataCase)` |   
  
### getText()
    
    
    public String getText()

Optional. Text part (can be code).

`string text = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The text.  
  
### getTextBytes()
    
    
    public ByteString getTextBytes()

Optional. Text part (can be code).

`string text = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for text.  
  
### getThought()
    
    
    public boolean getThought()

Indicates if the part is thought from the model.

`bool thought = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The thought.  
  
### getThoughtSignature()
    
    
    public ByteString getThoughtSignature()

An opaque signature for the thought so it can be reused in subsequent requests.

`bytes thought_signature = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The thoughtSignature.  
  
### getVideoMetadata()
    
    
    public VideoMetadata getVideoMetadata()

Optional. Video metadata. The metadata should only be specified while the video data is presented in inline_data or file_data.

` .google.cloud.vertexai.v1.VideoMetadata video_metadata = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[VideoMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.VideoMetadata)` | The videoMetadata.  
  
### getVideoMetadataBuilder()
    
    
    public VideoMetadata.Builder getVideoMetadataBuilder()

Optional. Video metadata. The metadata should only be specified while the video data is presented in inline_data or file_data.

` .google.cloud.vertexai.v1.VideoMetadata video_metadata = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[VideoMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.VideoMetadata.Builder)` |   
  
### getVideoMetadataOrBuilder()
    
    
    public VideoMetadataOrBuilder getVideoMetadataOrBuilder()

Optional. Video metadata. The metadata should only be specified while the video data is presented in inline_data or file_data.

` .google.cloud.vertexai.v1.VideoMetadata video_metadata = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[VideoMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.VideoMetadataOrBuilder)` |   
  
### hasCodeExecutionResult()
    
    
    public boolean hasCodeExecutionResult()

Optional. Result of executing the [ExecutableCode].

` .google.cloud.vertexai.v1.CodeExecutionResult code_execution_result = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the codeExecutionResult field is set.  
  
### hasExecutableCode()
    
    
    public boolean hasExecutableCode()

Optional. Code generated by the model that is meant to be executed.

` .google.cloud.vertexai.v1.ExecutableCode executable_code = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the executableCode field is set.  
  
### hasFileData()
    
    
    public boolean hasFileData()

Optional. URI based data.

` .google.cloud.vertexai.v1.FileData file_data = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the fileData field is set.  
  
### hasFunctionCall()
    
    
    public boolean hasFunctionCall()

Optional. A predicted [FunctionCall] returned from the model that contains a string representing the [FunctionDeclaration.name] with the parameters and their values.

` .google.cloud.vertexai.v1.FunctionCall function_call = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the functionCall field is set.  
  
### hasFunctionResponse()
    
    
    public boolean hasFunctionResponse()

Optional. The result output of a [FunctionCall] that contains a string representing the [FunctionDeclaration.name] and a structured JSON object containing any output from the function call. It is used as context to the model.

` .google.cloud.vertexai.v1.FunctionResponse function_response = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the functionResponse field is set.  
  
### hasInlineData()
    
    
    public boolean hasInlineData()

Optional. Inlined bytes data.

` .google.cloud.vertexai.v1.Blob inline_data = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the inlineData field is set.  
  
### hasText()
    
    
    public boolean hasText()

Optional. Text part (can be code).

`string text = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the text field is set.  
  
### hasVideoMetadata()
    
    
    public boolean hasVideoMetadata()

Optional. Video metadata. The metadata should only be specified while the video data is presented in inline_data or file_data.

` .google.cloud.vertexai.v1.VideoMetadata video_metadata = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the videoMetadata field is set.  
  
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

### mergeCodeExecutionResult(CodeExecutionResult value)
    
    
    public Part.Builder mergeCodeExecutionResult(CodeExecutionResult value)

Optional. Result of executing the [ExecutableCode].

` .google.cloud.vertexai.v1.CodeExecutionResult code_execution_result = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CodeExecutionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.CodeExecutionResult)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### mergeExecutableCode(ExecutableCode value)
    
    
    public Part.Builder mergeExecutableCode(ExecutableCode value)

Optional. Code generated by the model that is meant to be executed.

` .google.cloud.vertexai.v1.ExecutableCode executable_code = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ExecutableCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.ExecutableCode)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### mergeFileData(FileData value)
    
    
    public Part.Builder mergeFileData(FileData value)

Optional. URI based data.

` .google.cloud.vertexai.v1.FileData file_data = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[FileData](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.FileData)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### mergeFrom(Part other)
    
    
    public Part.Builder mergeFrom(Part other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Part](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public Part.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public Part.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeFunctionCall(FunctionCall value)
    
    
    public Part.Builder mergeFunctionCall(FunctionCall value)

Optional. A predicted [FunctionCall] returned from the model that contains a string representing the [FunctionDeclaration.name] with the parameters and their values.

` .google.cloud.vertexai.v1.FunctionCall function_call = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[FunctionCall](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.FunctionCall)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### mergeFunctionResponse(FunctionResponse value)
    
    
    public Part.Builder mergeFunctionResponse(FunctionResponse value)

Optional. The result output of a [FunctionCall] that contains a string representing the [FunctionDeclaration.name] and a structured JSON object containing any output from the function call. It is used as context to the model.

` .google.cloud.vertexai.v1.FunctionResponse function_response = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[FunctionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.FunctionResponse)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### mergeInlineData(Blob value)
    
    
    public Part.Builder mergeInlineData(Blob value)

Optional. Inlined bytes data.

` .google.cloud.vertexai.v1.Blob inline_data = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Blob)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### mergeVideoMetadata(VideoMetadata value)
    
    
    public Part.Builder mergeVideoMetadata(VideoMetadata value)

Optional. Video metadata. The metadata should only be specified while the video data is presented in inline_data or file_data.

` .google.cloud.vertexai.v1.VideoMetadata video_metadata = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[VideoMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.VideoMetadata)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### setCodeExecutionResult(CodeExecutionResult value)
    
    
    public Part.Builder setCodeExecutionResult(CodeExecutionResult value)

Optional. Result of executing the [ExecutableCode].

` .google.cloud.vertexai.v1.CodeExecutionResult code_execution_result = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CodeExecutionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.CodeExecutionResult)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### setCodeExecutionResult(CodeExecutionResult.Builder builderForValue)
    
    
    public Part.Builder setCodeExecutionResult(CodeExecutionResult.Builder builderForValue)

Optional. Result of executing the [ExecutableCode].

` .google.cloud.vertexai.v1.CodeExecutionResult code_execution_result = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[CodeExecutionResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.CodeExecutionResult.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### setExecutableCode(ExecutableCode value)
    
    
    public Part.Builder setExecutableCode(ExecutableCode value)

Optional. Code generated by the model that is meant to be executed.

` .google.cloud.vertexai.v1.ExecutableCode executable_code = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ExecutableCode](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.ExecutableCode)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### setExecutableCode(ExecutableCode.Builder builderForValue)
    
    
    public Part.Builder setExecutableCode(ExecutableCode.Builder builderForValue)

Optional. Code generated by the model that is meant to be executed.

` .google.cloud.vertexai.v1.ExecutableCode executable_code = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ExecutableCode.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.ExecutableCode.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### setFileData(FileData value)
    
    
    public Part.Builder setFileData(FileData value)

Optional. URI based data.

` .google.cloud.vertexai.v1.FileData file_data = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[FileData](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.FileData)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### setFileData(FileData.Builder builderForValue)
    
    
    public Part.Builder setFileData(FileData.Builder builderForValue)

Optional. URI based data.

` .google.cloud.vertexai.v1.FileData file_data = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[FileData.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.FileData.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### setFunctionCall(FunctionCall value)
    
    
    public Part.Builder setFunctionCall(FunctionCall value)

Optional. A predicted [FunctionCall] returned from the model that contains a string representing the [FunctionDeclaration.name] with the parameters and their values.

` .google.cloud.vertexai.v1.FunctionCall function_call = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[FunctionCall](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.FunctionCall)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### setFunctionCall(FunctionCall.Builder builderForValue)
    
    
    public Part.Builder setFunctionCall(FunctionCall.Builder builderForValue)

Optional. A predicted [FunctionCall] returned from the model that contains a string representing the [FunctionDeclaration.name] with the parameters and their values.

` .google.cloud.vertexai.v1.FunctionCall function_call = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[FunctionCall.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.FunctionCall.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### setFunctionResponse(FunctionResponse value)
    
    
    public Part.Builder setFunctionResponse(FunctionResponse value)

Optional. The result output of a [FunctionCall] that contains a string representing the [FunctionDeclaration.name] and a structured JSON object containing any output from the function call. It is used as context to the model.

` .google.cloud.vertexai.v1.FunctionResponse function_response = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[FunctionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.FunctionResponse)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### setFunctionResponse(FunctionResponse.Builder builderForValue)
    
    
    public Part.Builder setFunctionResponse(FunctionResponse.Builder builderForValue)

Optional. The result output of a [FunctionCall] that contains a string representing the [FunctionDeclaration.name] and a structured JSON object containing any output from the function call. It is used as context to the model.

` .google.cloud.vertexai.v1.FunctionResponse function_response = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[FunctionResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.FunctionResponse.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### setInlineData(Blob value)
    
    
    public Part.Builder setInlineData(Blob value)

Optional. Inlined bytes data.

` .google.cloud.vertexai.v1.Blob inline_data = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Blob)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### setInlineData(Blob.Builder builderForValue)
    
    
    public Part.Builder setInlineData(Blob.Builder builderForValue)

Optional. Inlined bytes data.

` .google.cloud.vertexai.v1.Blob inline_data = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Blob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Blob.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### setText(String value)
    
    
    public Part.Builder setText(String value)

Optional. Text part (can be code).

`string text = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The text to set.  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` | This builder for chaining.  
  
### setTextBytes(ByteString value)
    
    
    public Part.Builder setTextBytes(ByteString value)

Optional. Text part (can be code).

`string text = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for text to set.  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` | This builder for chaining.  
  
### setThought(boolean value)
    
    
    public Part.Builder setThought(boolean value)

Indicates if the part is thought from the model.

`bool thought = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The thought to set.  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` | This builder for chaining.  
  
### setThoughtSignature(ByteString value)
    
    
    public Part.Builder setThoughtSignature(ByteString value)

An opaque signature for the thought so it can be reused in subsequent requests.

`bytes thought_signature = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The thoughtSignature to set.  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` | This builder for chaining.  
  
### setVideoMetadata(VideoMetadata value)
    
    
    public Part.Builder setVideoMetadata(VideoMetadata value)

Optional. Video metadata. The metadata should only be specified while the video data is presented in inline_data or file_data.

` .google.cloud.vertexai.v1.VideoMetadata video_metadata = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[VideoMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.VideoMetadata)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
### setVideoMetadata(VideoMetadata.Builder builderForValue)
    
    
    public Part.Builder setVideoMetadata(VideoMetadata.Builder builderForValue)

Optional. Video metadata. The metadata should only be specified while the video data is presented in inline_data or file_data.

` .google.cloud.vertexai.v1.VideoMetadata video_metadata = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[VideoMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.VideoMetadata.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Part.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vertexai/latest/com.google.cloud.vertexai.api.Part.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-30 UTC."],[],[]] 
