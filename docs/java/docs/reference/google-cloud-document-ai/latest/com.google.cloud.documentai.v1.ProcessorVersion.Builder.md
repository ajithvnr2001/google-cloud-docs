---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder
title: Class ProcessorVersion.Builder (2.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:37.234628+00:00
---

# Class ProcessorVersion.Builder (2.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ProcessorVersion.Builder (2.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.103.0 (latest)  2.99.0  2.98.0  2.97.0  2.95.0  2.92.0  2.91.0  2.89.0  2.87.0  2.86.0  2.85.0  2.84.0  2.82.0  2.80.0  2.79.0  2.78.0  2.77.0  2.76.0  2.74.0  2.72.0  2.71.0  2.68.0  2.67.0  2.66.0  2.64.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.5  2.6.2  2.5.1  2.4.3  2.3.1  2.2.1  2.1.9 
    
    
    public static final class ProcessorVersion.Builder extends GeneratedMessage.Builder<ProcessorVersion.Builder> implements ProcessorVersionOrBuilder

A processor version is an implementation of a processor. Each processor can have multiple versions, pretrained by Google internally or uptrained by the customer. A processor can only have one default version at a time. Its document-processing behavior is defined by that version.

Protobuf type `google.cloud.documentai.v1.ProcessorVersion`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > ProcessorVersion.Builder

## Implements

[ProcessorVersionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersionOrBuilder)

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
    
    
    public ProcessorVersion build()

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion)` |   
  
### buildPartial()
    
    
    public ProcessorVersion buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion)` |   
  
### clear()
    
    
    public ProcessorVersion.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearCreateTime()
    
    
    public ProcessorVersion.Builder clearCreateTime()

Output only. The time the processor version was created.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
  
### clearDeprecationInfo()
    
    
    public ProcessorVersion.Builder clearDeprecationInfo()

Output only. If set, information about the eventual deprecation of this version.

` .google.cloud.documentai.v1.ProcessorVersion.DeprecationInfo deprecation_info = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
  
### clearDisplayName()
    
    
    public ProcessorVersion.Builder clearDisplayName()

The display name of the processor version.

`string display_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
### clearDocumentSchema()
    
    
    public ProcessorVersion.Builder clearDocumentSchema()

Output only. The schema of the processor version. Describes the output.

` .google.cloud.documentai.v1.DocumentSchema document_schema = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
  
### clearGenAiModelInfo()
    
    
    public ProcessorVersion.Builder clearGenAiModelInfo()

Output only. Information about Generative AI model-based processor versions.

` .google.cloud.documentai.v1.ProcessorVersion.GenAiModelInfo gen_ai_model_info = 18 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
  
### clearGoogleManaged()
    
    
    public ProcessorVersion.Builder clearGoogleManaged()

Output only. Denotes that this `ProcessorVersion` is managed by Google.

`bool google_managed = 11 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
### clearKmsKeyName()
    
    
    public ProcessorVersion.Builder clearKmsKeyName()

Output only. The KMS key name used for encryption.

`string kms_key_name = 9 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
### clearKmsKeyVersionName()
    
    
    public ProcessorVersion.Builder clearKmsKeyVersionName()

Output only. The KMS key version with which data is encrypted.

`string kms_key_version_name = 10 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
### clearLatestEvaluation()
    
    
    public ProcessorVersion.Builder clearLatestEvaluation()

Output only. The most recently invoked evaluation for the processor version.

` .google.cloud.documentai.v1.EvaluationReference latest_evaluation = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
  
### clearModelType()
    
    
    public ProcessorVersion.Builder clearModelType()

Output only. The model type of this processor version.

` .google.cloud.documentai.v1.ProcessorVersion.ModelType model_type = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
### clearName()
    
    
    public ProcessorVersion.Builder clearName()

Identifier. The resource name of the processor version. Format: `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processor_version}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
### clearSatisfiesPzi()
    
    
    public ProcessorVersion.Builder clearSatisfiesPzi()

Output only. Reserved for future use.

`bool satisfies_pzi = 17 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
### clearSatisfiesPzs()
    
    
    public ProcessorVersion.Builder clearSatisfiesPzs()

Output only. Reserved for future use.

`bool satisfies_pzs = 16 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
### clearState()
    
    
    public ProcessorVersion.Builder clearState()

Output only. The state of the processor version.

` .google.cloud.documentai.v1.ProcessorVersion.State state = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
### getCreateTime()
    
    
    public Timestamp getCreateTime()

Output only. The time the processor version was created.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeBuilder()
    
    
    public Timestamp.Builder getCreateTimeBuilder()

Output only. The time the processor version was created.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getCreateTimeOrBuilder()
    
    
    public TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The time the processor version was created.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDefaultInstanceForType()
    
    
    public ProcessorVersion getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion)` |   
  
### getDeprecationInfo()
    
    
    public ProcessorVersion.DeprecationInfo getDeprecationInfo()

Output only. If set, information about the eventual deprecation of this version.

` .google.cloud.documentai.v1.ProcessorVersion.DeprecationInfo deprecation_info = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.DeprecationInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.DeprecationInfo)` | The deprecationInfo.  
  
### getDeprecationInfoBuilder()
    
    
    public ProcessorVersion.DeprecationInfo.Builder getDeprecationInfoBuilder()

Output only. If set, information about the eventual deprecation of this version.

` .google.cloud.documentai.v1.ProcessorVersion.DeprecationInfo deprecation_info = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.DeprecationInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.DeprecationInfo.Builder)` |   
  
### getDeprecationInfoOrBuilder()
    
    
    public ProcessorVersion.DeprecationInfoOrBuilder getDeprecationInfoOrBuilder()

Output only. If set, information about the eventual deprecation of this version.

` .google.cloud.documentai.v1.ProcessorVersion.DeprecationInfo deprecation_info = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.DeprecationInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.DeprecationInfoOrBuilder)` |   
  
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

The display name of the processor version.

`string display_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public ByteString getDisplayNameBytes()

The display name of the processor version.

`string display_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getDocumentSchema()
    
    
    public DocumentSchema getDocumentSchema()

Output only. The schema of the processor version. Describes the output.

` .google.cloud.documentai.v1.DocumentSchema document_schema = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DocumentSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentSchema)` | The documentSchema.  
  
### getDocumentSchemaBuilder()
    
    
    public DocumentSchema.Builder getDocumentSchemaBuilder()

Output only. The schema of the processor version. Describes the output.

` .google.cloud.documentai.v1.DocumentSchema document_schema = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DocumentSchema.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentSchema.Builder)` |   
  
### getDocumentSchemaOrBuilder()
    
    
    public DocumentSchemaOrBuilder getDocumentSchemaOrBuilder()

Output only. The schema of the processor version. Describes the output.

` .google.cloud.documentai.v1.DocumentSchema document_schema = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DocumentSchemaOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentSchemaOrBuilder)` |   
  
### getGenAiModelInfo()
    
    
    public ProcessorVersion.GenAiModelInfo getGenAiModelInfo()

Output only. Information about Generative AI model-based processor versions.

` .google.cloud.documentai.v1.ProcessorVersion.GenAiModelInfo gen_ai_model_info = 18 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.GenAiModelInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.GenAiModelInfo)` | The genAiModelInfo.  
  
### getGenAiModelInfoBuilder()
    
    
    public ProcessorVersion.GenAiModelInfo.Builder getGenAiModelInfoBuilder()

Output only. Information about Generative AI model-based processor versions.

` .google.cloud.documentai.v1.ProcessorVersion.GenAiModelInfo gen_ai_model_info = 18 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.GenAiModelInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.GenAiModelInfo.Builder)` |   
  
### getGenAiModelInfoOrBuilder()
    
    
    public ProcessorVersion.GenAiModelInfoOrBuilder getGenAiModelInfoOrBuilder()

Output only. Information about Generative AI model-based processor versions.

` .google.cloud.documentai.v1.ProcessorVersion.GenAiModelInfo gen_ai_model_info = 18 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.GenAiModelInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.GenAiModelInfoOrBuilder)` |   
  
### getGoogleManaged()
    
    
    public boolean getGoogleManaged()

Output only. Denotes that this `ProcessorVersion` is managed by Google.

`bool google_managed = 11 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The googleManaged.  
  
### getKmsKeyName()
    
    
    public String getKmsKeyName()

Output only. The KMS key name used for encryption.

`string kms_key_name = 9 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kmsKeyName.  
  
### getKmsKeyNameBytes()
    
    
    public ByteString getKmsKeyNameBytes()

Output only. The KMS key name used for encryption.

`string kms_key_name = 9 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kmsKeyName.  
  
### getKmsKeyVersionName()
    
    
    public String getKmsKeyVersionName()

Output only. The KMS key version with which data is encrypted.

`string kms_key_version_name = 10 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kmsKeyVersionName.  
  
### getKmsKeyVersionNameBytes()
    
    
    public ByteString getKmsKeyVersionNameBytes()

Output only. The KMS key version with which data is encrypted.

`string kms_key_version_name = 10 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kmsKeyVersionName.  
  
### getLatestEvaluation()
    
    
    public EvaluationReference getLatestEvaluation()

Output only. The most recently invoked evaluation for the processor version.

` .google.cloud.documentai.v1.EvaluationReference latest_evaluation = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[EvaluationReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EvaluationReference)` | The latestEvaluation.  
  
### getLatestEvaluationBuilder()
    
    
    public EvaluationReference.Builder getLatestEvaluationBuilder()

Output only. The most recently invoked evaluation for the processor version.

` .google.cloud.documentai.v1.EvaluationReference latest_evaluation = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[EvaluationReference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EvaluationReference.Builder)` |   
  
### getLatestEvaluationOrBuilder()
    
    
    public EvaluationReferenceOrBuilder getLatestEvaluationOrBuilder()

Output only. The most recently invoked evaluation for the processor version.

` .google.cloud.documentai.v1.EvaluationReference latest_evaluation = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[EvaluationReferenceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EvaluationReferenceOrBuilder)` |   
  
### getModelType()
    
    
    public ProcessorVersion.ModelType getModelType()

Output only. The model type of this processor version.

` .google.cloud.documentai.v1.ProcessorVersion.ModelType model_type = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.ModelType](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.ModelType)` | The modelType.  
  
### getModelTypeValue()
    
    
    public int getModelTypeValue()

Output only. The model type of this processor version.

` .google.cloud.documentai.v1.ProcessorVersion.ModelType model_type = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for modelType.  
  
### getName()
    
    
    public String getName()

Identifier. The resource name of the processor version. Format: `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processor_version}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

Identifier. The resource name of the processor version. Format: `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processor_version}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getSatisfiesPzi()
    
    
    public boolean getSatisfiesPzi()

Output only. Reserved for future use.

`bool satisfies_pzi = 17 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The satisfiesPzi.  
  
### getSatisfiesPzs()
    
    
    public boolean getSatisfiesPzs()

Output only. Reserved for future use.

`bool satisfies_pzs = 16 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The satisfiesPzs.  
  
### getState()
    
    
    public ProcessorVersion.State getState()

Output only. The state of the processor version.

` .google.cloud.documentai.v1.ProcessorVersion.State state = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.State)` | The state.  
  
### getStateValue()
    
    
    public int getStateValue()

Output only. The state of the processor version.

` .google.cloud.documentai.v1.ProcessorVersion.State state = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### hasCreateTime()
    
    
    public boolean hasCreateTime()

Output only. The time the processor version was created.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasDeprecationInfo()
    
    
    public boolean hasDeprecationInfo()

Output only. If set, information about the eventual deprecation of this version.

` .google.cloud.documentai.v1.ProcessorVersion.DeprecationInfo deprecation_info = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the deprecationInfo field is set.  
  
### hasDocumentSchema()
    
    
    public boolean hasDocumentSchema()

Output only. The schema of the processor version. Describes the output.

` .google.cloud.documentai.v1.DocumentSchema document_schema = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the documentSchema field is set.  
  
### hasGenAiModelInfo()
    
    
    public boolean hasGenAiModelInfo()

Output only. Information about Generative AI model-based processor versions.

` .google.cloud.documentai.v1.ProcessorVersion.GenAiModelInfo gen_ai_model_info = 18 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the genAiModelInfo field is set.  
  
### hasLatestEvaluation()
    
    
    public boolean hasLatestEvaluation()

Output only. The most recently invoked evaluation for the processor version.

` .google.cloud.documentai.v1.EvaluationReference latest_evaluation = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the latestEvaluation field is set.  
  
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

### mergeCreateTime(Timestamp value)
    
    
    public ProcessorVersion.Builder mergeCreateTime(Timestamp value)

Output only. The time the processor version was created.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
  
### mergeDeprecationInfo(ProcessorVersion.DeprecationInfo value)
    
    
    public ProcessorVersion.Builder mergeDeprecationInfo(ProcessorVersion.DeprecationInfo value)

Output only. If set, information about the eventual deprecation of this version.

` .google.cloud.documentai.v1.ProcessorVersion.DeprecationInfo deprecation_info = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ProcessorVersion.DeprecationInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.DeprecationInfo)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
  
### mergeDocumentSchema(DocumentSchema value)
    
    
    public ProcessorVersion.Builder mergeDocumentSchema(DocumentSchema value)

Output only. The schema of the processor version. Describes the output.

` .google.cloud.documentai.v1.DocumentSchema document_schema = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DocumentSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentSchema)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
  
### mergeFrom(ProcessorVersion other)
    
    
    public ProcessorVersion.Builder mergeFrom(ProcessorVersion other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ProcessorVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public ProcessorVersion.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public ProcessorVersion.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeGenAiModelInfo(ProcessorVersion.GenAiModelInfo value)
    
    
    public ProcessorVersion.Builder mergeGenAiModelInfo(ProcessorVersion.GenAiModelInfo value)

Output only. Information about Generative AI model-based processor versions.

` .google.cloud.documentai.v1.ProcessorVersion.GenAiModelInfo gen_ai_model_info = 18 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ProcessorVersion.GenAiModelInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.GenAiModelInfo)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
  
### mergeLatestEvaluation(EvaluationReference value)
    
    
    public ProcessorVersion.Builder mergeLatestEvaluation(EvaluationReference value)

Output only. The most recently invoked evaluation for the processor version.

` .google.cloud.documentai.v1.EvaluationReference latest_evaluation = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[EvaluationReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EvaluationReference)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
  
### setCreateTime(Timestamp value)
    
    
    public ProcessorVersion.Builder setCreateTime(Timestamp value)

Output only. The time the processor version was created.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
  
### setCreateTime(Timestamp.Builder builderForValue)
    
    
    public ProcessorVersion.Builder setCreateTime(Timestamp.Builder builderForValue)

Output only. The time the processor version was created.

` .google.protobuf.Timestamp create_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
  
### setDeprecationInfo(ProcessorVersion.DeprecationInfo value)
    
    
    public ProcessorVersion.Builder setDeprecationInfo(ProcessorVersion.DeprecationInfo value)

Output only. If set, information about the eventual deprecation of this version.

` .google.cloud.documentai.v1.ProcessorVersion.DeprecationInfo deprecation_info = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ProcessorVersion.DeprecationInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.DeprecationInfo)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
  
### setDeprecationInfo(ProcessorVersion.DeprecationInfo.Builder builderForValue)
    
    
    public ProcessorVersion.Builder setDeprecationInfo(ProcessorVersion.DeprecationInfo.Builder builderForValue)

Output only. If set, information about the eventual deprecation of this version.

` .google.cloud.documentai.v1.ProcessorVersion.DeprecationInfo deprecation_info = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ProcessorVersion.DeprecationInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.DeprecationInfo.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
  
### setDisplayName(String value)
    
    
    public ProcessorVersion.Builder setDisplayName(String value)

The display name of the processor version.

`string display_name = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
### setDisplayNameBytes(ByteString value)
    
    
    public ProcessorVersion.Builder setDisplayNameBytes(ByteString value)

The display name of the processor version.

`string display_name = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
### setDocumentSchema(DocumentSchema value)
    
    
    public ProcessorVersion.Builder setDocumentSchema(DocumentSchema value)

Output only. The schema of the processor version. Describes the output.

` .google.cloud.documentai.v1.DocumentSchema document_schema = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DocumentSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentSchema)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
  
### setDocumentSchema(DocumentSchema.Builder builderForValue)
    
    
    public ProcessorVersion.Builder setDocumentSchema(DocumentSchema.Builder builderForValue)

Output only. The schema of the processor version. Describes the output.

` .google.cloud.documentai.v1.DocumentSchema document_schema = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[DocumentSchema.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.DocumentSchema.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
  
### setGenAiModelInfo(ProcessorVersion.GenAiModelInfo value)
    
    
    public ProcessorVersion.Builder setGenAiModelInfo(ProcessorVersion.GenAiModelInfo value)

Output only. Information about Generative AI model-based processor versions.

` .google.cloud.documentai.v1.ProcessorVersion.GenAiModelInfo gen_ai_model_info = 18 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ProcessorVersion.GenAiModelInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.GenAiModelInfo)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
  
### setGenAiModelInfo(ProcessorVersion.GenAiModelInfo.Builder builderForValue)
    
    
    public ProcessorVersion.Builder setGenAiModelInfo(ProcessorVersion.GenAiModelInfo.Builder builderForValue)

Output only. Information about Generative AI model-based processor versions.

` .google.cloud.documentai.v1.ProcessorVersion.GenAiModelInfo gen_ai_model_info = 18 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ProcessorVersion.GenAiModelInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.GenAiModelInfo.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
  
### setGoogleManaged(boolean value)
    
    
    public ProcessorVersion.Builder setGoogleManaged(boolean value)

Output only. Denotes that this `ProcessorVersion` is managed by Google.

`bool google_managed = 11 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The googleManaged to set.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
### setKmsKeyName(String value)
    
    
    public ProcessorVersion.Builder setKmsKeyName(String value)

Output only. The KMS key name used for encryption.

`string kms_key_name = 9 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The kmsKeyName to set.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
### setKmsKeyNameBytes(ByteString value)
    
    
    public ProcessorVersion.Builder setKmsKeyNameBytes(ByteString value)

Output only. The KMS key name used for encryption.

`string kms_key_name = 9 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for kmsKeyName to set.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
### setKmsKeyVersionName(String value)
    
    
    public ProcessorVersion.Builder setKmsKeyVersionName(String value)

Output only. The KMS key version with which data is encrypted.

`string kms_key_version_name = 10 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The kmsKeyVersionName to set.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
### setKmsKeyVersionNameBytes(ByteString value)
    
    
    public ProcessorVersion.Builder setKmsKeyVersionNameBytes(ByteString value)

Output only. The KMS key version with which data is encrypted.

`string kms_key_version_name = 10 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for kmsKeyVersionName to set.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
### setLatestEvaluation(EvaluationReference value)
    
    
    public ProcessorVersion.Builder setLatestEvaluation(EvaluationReference value)

Output only. The most recently invoked evaluation for the processor version.

` .google.cloud.documentai.v1.EvaluationReference latest_evaluation = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[EvaluationReference](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EvaluationReference)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
  
### setLatestEvaluation(EvaluationReference.Builder builderForValue)
    
    
    public ProcessorVersion.Builder setLatestEvaluation(EvaluationReference.Builder builderForValue)

Output only. The most recently invoked evaluation for the processor version.

` .google.cloud.documentai.v1.EvaluationReference latest_evaluation = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[EvaluationReference.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.EvaluationReference.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` |   
  
### setModelType(ProcessorVersion.ModelType value)
    
    
    public ProcessorVersion.Builder setModelType(ProcessorVersion.ModelType value)

Output only. The model type of this processor version.

` .google.cloud.documentai.v1.ProcessorVersion.ModelType model_type = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ProcessorVersion.ModelType](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.ModelType)`  
The modelType to set.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
### setModelTypeValue(int value)
    
    
    public ProcessorVersion.Builder setModelTypeValue(int value)

Output only. The model type of this processor version.

` .google.cloud.documentai.v1.ProcessorVersion.ModelType model_type = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for modelType to set.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
### setName(String value)
    
    
    public ProcessorVersion.Builder setName(String value)

Identifier. The resource name of the processor version. Format: `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processor_version}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public ProcessorVersion.Builder setNameBytes(ByteString value)

Identifier. The resource name of the processor version. Format: `projects/{project}/locations/{location}/processors/{processor}/processorVersions/{processor_version}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
### setSatisfiesPzi(boolean value)
    
    
    public ProcessorVersion.Builder setSatisfiesPzi(boolean value)

Output only. Reserved for future use.

`bool satisfies_pzi = 17 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The satisfiesPzi to set.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
### setSatisfiesPzs(boolean value)
    
    
    public ProcessorVersion.Builder setSatisfiesPzs(boolean value)

Output only. Reserved for future use.

`bool satisfies_pzs = 16 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The satisfiesPzs to set.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
### setState(ProcessorVersion.State value)
    
    
    public ProcessorVersion.Builder setState(ProcessorVersion.State value)

Output only. The state of the processor version.

` .google.cloud.documentai.v1.ProcessorVersion.State state = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ProcessorVersion.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.State)`  
The state to set.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
### setStateValue(int value)
    
    
    public ProcessorVersion.Builder setStateValue(int value)

Output only. The state of the processor version.

` .google.cloud.documentai.v1.ProcessorVersion.State state = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for state to set.  
**Returns**  
---  
**Type** | **Description**  
`[ProcessorVersion.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-document-ai/latest/com.google.cloud.documentai.v1.ProcessorVersion.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
