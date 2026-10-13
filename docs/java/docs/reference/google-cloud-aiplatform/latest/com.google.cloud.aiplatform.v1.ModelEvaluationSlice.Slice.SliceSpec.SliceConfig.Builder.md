---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder
title: Class ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:39.755368+00:00
---

# Class ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public static final class ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder extends GeneratedMessage.Builder<ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder> implements ModelEvaluationSlice.Slice.SliceSpec.SliceConfigOrBuilder

Specification message containing the config for this SliceSpec. When `kind` is selected as `value` and/or `range`, only a single slice will be computed. When `all_values` is present, a separate slice will be computed for each possible label/value for the corresponding key in `config`. Examples, with feature zip_code with values 12345, 23334, 88888 and feature country with values "US", "Canada", "Mexico" in the dataset:

Example 1:

{ "zip_code": { "value": { "float_value": 12345.0 } } }

A single slice for any data with zip_code 12345 in the dataset.

Example 2:

{ "zip_code": { "range": { "low": 12345, "high": 20000 } } }

A single slice containing data where the zip_codes between 12345 and 20000 For this example, data with the zip_code of 12345 will be in this slice.

Example 3:

{ "zip_code": { "range": { "low": 10000, "high": 20000 } }, "country": { "value": { "string_value": "US" } } }

A single slice containing data where the zip_codes between 10000 and 20000 has the country "US". For this example, data with the zip_code of 12345 and country "US" will be in this slice.

Example 4:

{ "country": {"all_values": { "value": true } } }

Three slices are computed, one for each unique country in the dataset.

Example 5:

{ "country": { "all_values": { "value": true } }, "zip_code": { "value": { "float_value": 12345.0 } } }

Three slices are computed, one for each unique country in the dataset where the zip_code is also 12345. For this example, data with zip_code 12345 and country "US" will be in one slice, zip_code 12345 and country "Canada" in another slice, and zip_code 12345 and country "Mexico" in another slice, totaling 3 slices.

Protobuf type ` google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder

## Implements

[ModelEvaluationSlice.Slice.SliceSpec.SliceConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfigOrBuilder)

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
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.SliceConfig build()

**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.SliceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig)` |   
  
### buildPartial()
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.SliceConfig buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.SliceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig)` |   
  
### clear()
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearAllValues()
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder clearAllValues()

If all_values is set to true, then all possible labels of the keyed feature will have another slice computed. Example: `{"all_values":{"value":true}}`

`.google.protobuf.BoolValue all_values = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder)` |   
  
### clearKind()
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder clearKind()

**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder)` |   
  
### clearRange()
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder clearRange()

A range of values for a numerical feature. Example: `{"range":{"low":10000.0,"high":50000.0}}` will capture 12345 and 23334 in the slice.

`.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Range range = 2; `

**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder)` |   
  
### clearValue()
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder clearValue()

A unique specific value for a given feature. Example: `{ "value": { "string_value": "12345" } }`

`.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Value value = 1; `

**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder)` |   
  
### getAllValues()
    
    
    public BoolValue getAllValues()

If all_values is set to true, then all possible labels of the keyed feature will have another slice computed. Example: `{"all_values":{"value":true}}`

`.google.protobuf.BoolValue all_values = 3;`

**Returns**  
---  
**Type** | **Description**  
`[BoolValue](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValue.html)` | The allValues.  
  
### getAllValuesBuilder()
    
    
    public BoolValue.Builder getAllValuesBuilder()

If all_values is set to true, then all possible labels of the keyed feature will have another slice computed. Example: `{"all_values":{"value":true}}`

`.google.protobuf.BoolValue all_values = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValue.Builder.html)` |   
  
### getAllValuesOrBuilder()
    
    
    public BoolValueOrBuilder getAllValuesOrBuilder()

If all_values is set to true, then all possible labels of the keyed feature will have another slice computed. Example: `{"all_values":{"value":true}}`

`.google.protobuf.BoolValue all_values = 3;`

**Returns**  
---  
**Type** | **Description**  
`[BoolValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValueOrBuilder.html)` |   
  
### getDefaultInstanceForType()
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.SliceConfig getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.SliceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getKindCase()
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.KindCase getKindCase()

**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.KindCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.KindCase)` |   
  
### getRange()
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.Range getRange()

A range of values for a numerical feature. Example: `{"range":{"low":10000.0,"high":50000.0}}` will capture 12345 and 23334 in the slice.

`.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Range range = 2; `

**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.Range](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Range)` | The range.  
  
### getRangeBuilder()
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.Range.Builder getRangeBuilder()

A range of values for a numerical feature. Example: `{"range":{"low":10000.0,"high":50000.0}}` will capture 12345 and 23334 in the slice.

`.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Range range = 2; `

**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.Range.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Range.Builder)` |   
  
### getRangeOrBuilder()
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.RangeOrBuilder getRangeOrBuilder()

A range of values for a numerical feature. Example: `{"range":{"low":10000.0,"high":50000.0}}` will capture 12345 and 23334 in the slice.

`.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Range range = 2; `

**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.RangeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.RangeOrBuilder)` |   
  
### getValue()
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.Value getValue()

A unique specific value for a given feature. Example: `{ "value": { "string_value": "12345" } }`

`.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Value value = 1; `

**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Value)` | The value.  
  
### getValueBuilder()
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.Value.Builder getValueBuilder()

A unique specific value for a given feature. Example: `{ "value": { "string_value": "12345" } }`

`.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Value value = 1; `

**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.Value.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Value.Builder)` |   
  
### getValueOrBuilder()
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.ValueOrBuilder getValueOrBuilder()

A unique specific value for a given feature. Example: `{ "value": { "string_value": "12345" } }`

`.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Value value = 1; `

**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.ValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.ValueOrBuilder)` |   
  
### hasAllValues()
    
    
    public boolean hasAllValues()

If all_values is set to true, then all possible labels of the keyed feature will have another slice computed. Example: `{"all_values":{"value":true}}`

`.google.protobuf.BoolValue all_values = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the allValues field is set.  
  
### hasRange()
    
    
    public boolean hasRange()

A range of values for a numerical feature. Example: `{"range":{"low":10000.0,"high":50000.0}}` will capture 12345 and 23334 in the slice.

`.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Range range = 2; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the range field is set.  
  
### hasValue()
    
    
    public boolean hasValue()

A unique specific value for a given feature. Example: `{ "value": { "string_value": "12345" } }`

`.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Value value = 1; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the value field is set.  
  
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

### mergeAllValues(BoolValue value)
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder mergeAllValues(BoolValue value)

If all_values is set to true, then all possible labels of the keyed feature will have another slice computed. Example: `{"all_values":{"value":true}}`

`.google.protobuf.BoolValue all_values = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BoolValue](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValue.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder)` |   
  
### mergeFrom(ModelEvaluationSlice.Slice.SliceSpec.SliceConfig other)
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder mergeFrom(ModelEvaluationSlice.Slice.SliceSpec.SliceConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ModelEvaluationSlice.Slice.SliceSpec.SliceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeRange(ModelEvaluationSlice.Slice.SliceSpec.Range value)
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder mergeRange(ModelEvaluationSlice.Slice.SliceSpec.Range value)

A range of values for a numerical feature. Example: `{"range":{"low":10000.0,"high":50000.0}}` will capture 12345 and 23334 in the slice.

`.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Range range = 2; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ModelEvaluationSlice.Slice.SliceSpec.Range](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Range)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder)` |   
  
### mergeValue(ModelEvaluationSlice.Slice.SliceSpec.Value value)
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder mergeValue(ModelEvaluationSlice.Slice.SliceSpec.Value value)

A unique specific value for a given feature. Example: `{ "value": { "string_value": "12345" } }`

`.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Value value = 1; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ModelEvaluationSlice.Slice.SliceSpec.Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Value)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder)` |   
  
### setAllValues(BoolValue value)
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder setAllValues(BoolValue value)

If all_values is set to true, then all possible labels of the keyed feature will have another slice computed. Example: `{"all_values":{"value":true}}`

`.google.protobuf.BoolValue all_values = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BoolValue](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValue.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder)` |   
  
### setAllValues(BoolValue.Builder builderForValue)
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder setAllValues(BoolValue.Builder builderForValue)

If all_values is set to true, then all possible labels of the keyed feature will have another slice computed. Example: `{"all_values":{"value":true}}`

`.google.protobuf.BoolValue all_values = 3;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValue.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder)` |   
  
### setRange(ModelEvaluationSlice.Slice.SliceSpec.Range value)
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder setRange(ModelEvaluationSlice.Slice.SliceSpec.Range value)

A range of values for a numerical feature. Example: `{"range":{"low":10000.0,"high":50000.0}}` will capture 12345 and 23334 in the slice.

`.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Range range = 2; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ModelEvaluationSlice.Slice.SliceSpec.Range](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Range)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder)` |   
  
### setRange(ModelEvaluationSlice.Slice.SliceSpec.Range.Builder builderForValue)
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder setRange(ModelEvaluationSlice.Slice.SliceSpec.Range.Builder builderForValue)

A range of values for a numerical feature. Example: `{"range":{"low":10000.0,"high":50000.0}}` will capture 12345 and 23334 in the slice.

`.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Range range = 2; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ModelEvaluationSlice.Slice.SliceSpec.Range.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Range.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder)` |   
  
### setValue(ModelEvaluationSlice.Slice.SliceSpec.Value value)
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder setValue(ModelEvaluationSlice.Slice.SliceSpec.Value value)

A unique specific value for a given feature. Example: `{ "value": { "string_value": "12345" } }`

`.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Value value = 1; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ModelEvaluationSlice.Slice.SliceSpec.Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Value)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder)` |   
  
### setValue(ModelEvaluationSlice.Slice.SliceSpec.Value.Builder builderForValue)
    
    
    public ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder setValue(ModelEvaluationSlice.Slice.SliceSpec.Value.Builder builderForValue)

A unique specific value for a given feature. Example: `{ "value": { "string_value": "12345" } }`

`.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Value value = 1; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ModelEvaluationSlice.Slice.SliceSpec.Value.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.Value.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
