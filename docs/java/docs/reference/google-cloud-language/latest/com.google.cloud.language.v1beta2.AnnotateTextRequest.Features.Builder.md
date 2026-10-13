---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features.Builder
title: Class AnnotateTextRequest.Features.Builder (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:46:12.240354+00:00
---

# Class AnnotateTextRequest.Features.Builder (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AnnotateTextRequest.Features.Builder (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.1  2.3.4  2.2.0  2.1.10 
    
    
    public static final class AnnotateTextRequest.Features.Builder extends GeneratedMessage.Builder<AnnotateTextRequest.Features.Builder> implements AnnotateTextRequest.FeaturesOrBuilder

All available features for sentiment, syntax, and semantic analysis. Setting each one to true will enable that specific analysis for the input. Next ID: 12

Protobuf type `google.cloud.language.v1beta2.AnnotateTextRequest.Features`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > AnnotateTextRequest.Features.Builder

## Implements

[AnnotateTextRequest.FeaturesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.FeaturesOrBuilder)

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
    
    
    public AnnotateTextRequest.Features build()

**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextRequest.Features](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features)` |   
  
### buildPartial()
    
    
    public AnnotateTextRequest.Features buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextRequest.Features](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features)` |   
  
### clear()
    
    
    public AnnotateTextRequest.Features.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextRequest.Features.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearClassificationModelOptions()
    
    
    public AnnotateTextRequest.Features.Builder clearClassificationModelOptions()

The model options to use for classification. Defaults to v1 options if not specified. Only used if `classify_text` is set to true.

` .google.cloud.language.v1beta2.ClassificationModelOptions classification_model_options = 10; `

**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextRequest.Features.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features.Builder)` |   
  
### clearClassifyText()
    
    
    public AnnotateTextRequest.Features.Builder clearClassifyText()

Classify the full document into categories. If this is true, the API will use the default model which classifies into a [predefined taxonomy](https://cloud.google.com/natural-language/docs/categories).

`bool classify_text = 6;`

**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextRequest.Features.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features.Builder)` | This builder for chaining.  
  
### clearExtractDocumentSentiment()
    
    
    public AnnotateTextRequest.Features.Builder clearExtractDocumentSentiment()

Extract document-level sentiment.

`bool extract_document_sentiment = 3;`

**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextRequest.Features.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features.Builder)` | This builder for chaining.  
  
### clearExtractEntities()
    
    
    public AnnotateTextRequest.Features.Builder clearExtractEntities()

Extract entities.

`bool extract_entities = 2;`

**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextRequest.Features.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features.Builder)` | This builder for chaining.  
  
### clearExtractEntitySentiment()
    
    
    public AnnotateTextRequest.Features.Builder clearExtractEntitySentiment()

Extract entities and their associated sentiment.

`bool extract_entity_sentiment = 4;`

**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextRequest.Features.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features.Builder)` | This builder for chaining.  
  
### clearExtractSyntax()
    
    
    public AnnotateTextRequest.Features.Builder clearExtractSyntax()

Extract syntax information.

`bool extract_syntax = 1;`

**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextRequest.Features.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features.Builder)` | This builder for chaining.  
  
### clearModerateText()
    
    
    public AnnotateTextRequest.Features.Builder clearModerateText()

Moderate the document for harmful and sensitive categories.

`bool moderate_text = 11;`

**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextRequest.Features.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features.Builder)` | This builder for chaining.  
  
### getClassificationModelOptions()
    
    
    public ClassificationModelOptions getClassificationModelOptions()

The model options to use for classification. Defaults to v1 options if not specified. Only used if `classify_text` is set to true.

` .google.cloud.language.v1beta2.ClassificationModelOptions classification_model_options = 10; `

**Returns**  
---  
**Type** | **Description**  
`[ClassificationModelOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.ClassificationModelOptions)` | The classificationModelOptions.  
  
### getClassificationModelOptionsBuilder()
    
    
    public ClassificationModelOptions.Builder getClassificationModelOptionsBuilder()

The model options to use for classification. Defaults to v1 options if not specified. Only used if `classify_text` is set to true.

` .google.cloud.language.v1beta2.ClassificationModelOptions classification_model_options = 10; `

**Returns**  
---  
**Type** | **Description**  
`[ClassificationModelOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.ClassificationModelOptions.Builder)` |   
  
### getClassificationModelOptionsOrBuilder()
    
    
    public ClassificationModelOptionsOrBuilder getClassificationModelOptionsOrBuilder()

The model options to use for classification. Defaults to v1 options if not specified. Only used if `classify_text` is set to true.

` .google.cloud.language.v1beta2.ClassificationModelOptions classification_model_options = 10; `

**Returns**  
---  
**Type** | **Description**  
`[ClassificationModelOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.ClassificationModelOptionsOrBuilder)` |   
  
### getClassifyText()
    
    
    public boolean getClassifyText()

Classify the full document into categories. If this is true, the API will use the default model which classifies into a [predefined taxonomy](https://cloud.google.com/natural-language/docs/categories).

`bool classify_text = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The classifyText.  
  
### getDefaultInstanceForType()
    
    
    public AnnotateTextRequest.Features getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextRequest.Features](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getExtractDocumentSentiment()
    
    
    public boolean getExtractDocumentSentiment()

Extract document-level sentiment.

`bool extract_document_sentiment = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The extractDocumentSentiment.  
  
### getExtractEntities()
    
    
    public boolean getExtractEntities()

Extract entities.

`bool extract_entities = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The extractEntities.  
  
### getExtractEntitySentiment()
    
    
    public boolean getExtractEntitySentiment()

Extract entities and their associated sentiment.

`bool extract_entity_sentiment = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The extractEntitySentiment.  
  
### getExtractSyntax()
    
    
    public boolean getExtractSyntax()

Extract syntax information.

`bool extract_syntax = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The extractSyntax.  
  
### getModerateText()
    
    
    public boolean getModerateText()

Moderate the document for harmful and sensitive categories.

`bool moderate_text = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The moderateText.  
  
### hasClassificationModelOptions()
    
    
    public boolean hasClassificationModelOptions()

The model options to use for classification. Defaults to v1 options if not specified. Only used if `classify_text` is set to true.

` .google.cloud.language.v1beta2.ClassificationModelOptions classification_model_options = 10; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the classificationModelOptions field is set.  
  
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

### mergeClassificationModelOptions(ClassificationModelOptions value)
    
    
    public AnnotateTextRequest.Features.Builder mergeClassificationModelOptions(ClassificationModelOptions value)

The model options to use for classification. Defaults to v1 options if not specified. Only used if `classify_text` is set to true.

` .google.cloud.language.v1beta2.ClassificationModelOptions classification_model_options = 10; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ClassificationModelOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.ClassificationModelOptions)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextRequest.Features.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features.Builder)` |   
  
### mergeFrom(AnnotateTextRequest.Features other)
    
    
    public AnnotateTextRequest.Features.Builder mergeFrom(AnnotateTextRequest.Features other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AnnotateTextRequest.Features](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextRequest.Features.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public AnnotateTextRequest.Features.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextRequest.Features.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public AnnotateTextRequest.Features.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextRequest.Features.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### setClassificationModelOptions(ClassificationModelOptions value)
    
    
    public AnnotateTextRequest.Features.Builder setClassificationModelOptions(ClassificationModelOptions value)

The model options to use for classification. Defaults to v1 options if not specified. Only used if `classify_text` is set to true.

` .google.cloud.language.v1beta2.ClassificationModelOptions classification_model_options = 10; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ClassificationModelOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.ClassificationModelOptions)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextRequest.Features.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features.Builder)` |   
  
### setClassificationModelOptions(ClassificationModelOptions.Builder builderForValue)
    
    
    public AnnotateTextRequest.Features.Builder setClassificationModelOptions(ClassificationModelOptions.Builder builderForValue)

The model options to use for classification. Defaults to v1 options if not specified. Only used if `classify_text` is set to true.

` .google.cloud.language.v1beta2.ClassificationModelOptions classification_model_options = 10; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ClassificationModelOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.ClassificationModelOptions.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextRequest.Features.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features.Builder)` |   
  
### setClassifyText(boolean value)
    
    
    public AnnotateTextRequest.Features.Builder setClassifyText(boolean value)

Classify the full document into categories. If this is true, the API will use the default model which classifies into a [predefined taxonomy](https://cloud.google.com/natural-language/docs/categories).

`bool classify_text = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The classifyText to set.  
**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextRequest.Features.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features.Builder)` | This builder for chaining.  
  
### setExtractDocumentSentiment(boolean value)
    
    
    public AnnotateTextRequest.Features.Builder setExtractDocumentSentiment(boolean value)

Extract document-level sentiment.

`bool extract_document_sentiment = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The extractDocumentSentiment to set.  
**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextRequest.Features.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features.Builder)` | This builder for chaining.  
  
### setExtractEntities(boolean value)
    
    
    public AnnotateTextRequest.Features.Builder setExtractEntities(boolean value)

Extract entities.

`bool extract_entities = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The extractEntities to set.  
**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextRequest.Features.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features.Builder)` | This builder for chaining.  
  
### setExtractEntitySentiment(boolean value)
    
    
    public AnnotateTextRequest.Features.Builder setExtractEntitySentiment(boolean value)

Extract entities and their associated sentiment.

`bool extract_entity_sentiment = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The extractEntitySentiment to set.  
**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextRequest.Features.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features.Builder)` | This builder for chaining.  
  
### setExtractSyntax(boolean value)
    
    
    public AnnotateTextRequest.Features.Builder setExtractSyntax(boolean value)

Extract syntax information.

`bool extract_syntax = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The extractSyntax to set.  
**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextRequest.Features.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features.Builder)` | This builder for chaining.  
  
### setModerateText(boolean value)
    
    
    public AnnotateTextRequest.Features.Builder setModerateText(boolean value)

Moderate the document for harmful and sensitive categories.

`bool moderate_text = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The moderateText to set.  
**Returns**  
---  
**Type** | **Description**  
`[AnnotateTextRequest.Features.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v1beta2.AnnotateTextRequest.Features.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
