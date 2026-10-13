---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder
title: Class Execution.Builder (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:23:33.500274+00:00
---

# Class Execution.Builder (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Execution.Builder (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.5  0.2.1  0.1.2 
    
    
    public static final class Execution.Builder extends GeneratedMessage.Builder<Execution.Builder> implements ExecutionOrBuilder

Execution represents the configuration of a single execution. A execution an immutable resource that references a container image which is run to completion.

Protobuf type `google.cloud.run.v2.Execution`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > Execution.Builder

## Implements

[ExecutionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ExecutionOrBuilder)

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

### addAllConditions(Iterable<? extends Condition> values)
    
    
    public Execution.Builder addAllConditions(Iterable<? extends Condition> values)

Output only. The Condition of this Execution, containing its readiness status, and detailed error information in case it did not reach the desired state.

` repeated .google.cloud.run.v2.Condition conditions = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.run.v2.Condition>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### addConditions(Condition value)
    
    
    public Execution.Builder addConditions(Condition value)

Output only. The Condition of this Execution, containing its readiness status, and detailed error information in case it did not reach the desired state.

` repeated .google.cloud.run.v2.Condition conditions = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Condition)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### addConditions(Condition.Builder builderForValue)
    
    
    public Execution.Builder addConditions(Condition.Builder builderForValue)

Output only. The Condition of this Execution, containing its readiness status, and detailed error information in case it did not reach the desired state.

` repeated .google.cloud.run.v2.Condition conditions = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Condition.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Condition.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### addConditions(int index, Condition value)
    
    
    public Execution.Builder addConditions(int index, Condition value)

Output only. The Condition of this Execution, containing its readiness status, and detailed error information in case it did not reach the desired state.

` repeated .google.cloud.run.v2.Condition conditions = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Condition)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### addConditions(int index, Condition.Builder builderForValue)
    
    
    public Execution.Builder addConditions(int index, Condition.Builder builderForValue)

Output only. The Condition of this Execution, containing its readiness status, and detailed error information in case it did not reach the desired state.

` repeated .google.cloud.run.v2.Condition conditions = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Condition.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Condition.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### addConditionsBuilder()
    
    
    public Condition.Builder addConditionsBuilder()

Output only. The Condition of this Execution, containing its readiness status, and detailed error information in case it did not reach the desired state.

` repeated .google.cloud.run.v2.Condition conditions = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Condition.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Condition.Builder)` |   
  
### addConditionsBuilder(int index)
    
    
    public Condition.Builder addConditionsBuilder(int index)

Output only. The Condition of this Execution, containing its readiness status, and detailed error information in case it did not reach the desired state.

` repeated .google.cloud.run.v2.Condition conditions = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Condition.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Condition.Builder)` |   
  
### build()
    
    
    public Execution build()

**Returns**  
---  
**Type** | **Description**  
`[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution)` |   
  
### buildPartial()
    
    
    public Execution buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution)` |   
  
### clear()
    
    
    public Execution.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearAnnotations()
    
    
    public Execution.Builder clearAnnotations()

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### clearCancelledCount()
    
    
    public Execution.Builder clearCancelledCount()

Output only. The number of tasks which reached phase Cancelled.

`int32 cancelled_count = 24 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### clearCompletionTime()
    
    
    public Execution.Builder clearCompletionTime()

Output only. Represents time when the execution was completed. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp completion_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### clearConditions()
    
    
    public Execution.Builder clearConditions()

Output only. The Condition of this Execution, containing its readiness status, and detailed error information in case it did not reach the desired state.

` repeated .google.cloud.run.v2.Condition conditions = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### clearCreateTime()
    
    
    public Execution.Builder clearCreateTime()

Output only. Represents time when the execution was acknowledged by the execution controller. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### clearCreator()
    
    
    public Execution.Builder clearCreator()

Output only. Email address of the authenticated creator.

`string creator = 32 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### clearDeleteTime()
    
    
    public Execution.Builder clearDeleteTime()

Output only. For a deleted resource, the deletion time. It is only populated as a response to a Delete request.

` .google.protobuf.Timestamp delete_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### clearEtag()
    
    
    public Execution.Builder clearEtag()

Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates.

`string etag = 99 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### clearExpireTime()
    
    
    public Execution.Builder clearExpireTime()

Output only. For a deleted resource, the time after which it will be permamently deleted. It is only populated as a response to a Delete request.

` .google.protobuf.Timestamp expire_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### clearFailedCount()
    
    
    public Execution.Builder clearFailedCount()

Output only. The number of tasks which reached phase Failed.

`int32 failed_count = 21 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### clearGeneration()
    
    
    public Execution.Builder clearGeneration()

Output only. A number that monotonically increases every time the user modifies the desired state.

`int64 generation = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### clearJob()
    
    
    public Execution.Builder clearJob()

Output only. The name of the parent Job.

` string job = 12 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### clearLabels()
    
    
    public Execution.Builder clearLabels()

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### clearLaunchStage()
    
    
    public Execution.Builder clearLaunchStage()

The least stable launch stage needed to create this resource, as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). Cloud Run supports `ALPHA`, `BETA`, and `GA`.

Note that this value might not be what was used as input. For example, if ALPHA was provided as input in the parent resource, but only BETA and GA-level features are were, this field will be BETA.

`.google.api.LaunchStage launch_stage = 11;`

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### clearLogUri()
    
    
    public Execution.Builder clearLogUri()

Output only. URI where logs for this execution can be found in Cloud Console.

`string log_uri = 26 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### clearName()
    
    
    public Execution.Builder clearName()

Output only. The unique name of this Execution.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### clearObservedGeneration()
    
    
    public Execution.Builder clearObservedGeneration()

Output only. The generation of this Execution. See comments in `reconciling` for additional information on reconciliation process in Cloud Run.

`int64 observed_generation = 18 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### clearParallelism()
    
    
    public Execution.Builder clearParallelism()

Output only. Specifies the maximum desired number of tasks the execution should run at any given time. Must be <= task_count. The actual number of tasks running in steady state will be less than this number when ((.spec.task_count - .status.successful) < .spec.parallelism), i.e. when the work left to do is less than max parallelism.

`int32 parallelism = 13 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### clearReconciling()
    
    
    public Execution.Builder clearReconciling()

Output only. Indicates whether the resource's reconciliation is still in progress. See comments in `Job.reconciling` for additional information on reconciliation process in Cloud Run.

`bool reconciling = 16 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### clearRetriedCount()
    
    
    public Execution.Builder clearRetriedCount()

Output only. The number of tasks which have retried at least once.

`int32 retried_count = 25 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### clearRunningCount()
    
    
    public Execution.Builder clearRunningCount()

Output only. The number of actively running tasks.

`int32 running_count = 19 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### clearSatisfiesPzs()
    
    
    public Execution.Builder clearSatisfiesPzs()

Output only. Reserved for future use.

`bool satisfies_pzs = 27 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### clearStartTime()
    
    
    public Execution.Builder clearStartTime()

Output only. Represents time when the execution started to run. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp start_time = 22 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### clearSucceededCount()
    
    
    public Execution.Builder clearSucceededCount()

Output only. The number of tasks which reached phase Succeeded.

`int32 succeeded_count = 20 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### clearTaskCount()
    
    
    public Execution.Builder clearTaskCount()

Output only. Specifies the desired number of tasks the execution should run. Setting to 1 means that parallelism is limited to 1 and the success of that task signals the success of the execution.

`int32 task_count = 14 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### clearTemplate()
    
    
    public Execution.Builder clearTemplate()

Output only. The template used to create tasks for this execution.

` .google.cloud.run.v2.TaskTemplate template = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### clearUid()
    
    
    public Execution.Builder clearUid()

Output only. Server assigned unique identifier for the Execution. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted.

`string uid = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### clearUpdateTime()
    
    
    public Execution.Builder clearUpdateTime()

Output only. The last-modified time.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### containsAnnotations(String key)
    
    
    public boolean containsAnnotations(String key)

Output only. Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects.

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsLabels(String key)
    
    
    public boolean containsLabels(String key)

Output only. Unstructured key value map that can be used to organize and categorize objects. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit <https://cloud.google.com/resource-manager/docs/creating-managing-labels> or <https://cloud.google.com/run/docs/configuring/labels>

`map<string, string> labels = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAnnotations() (deprecated)
    
    
    public Map<String,String> getAnnotations()

Use [#getAnnotationsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder#com_google_cloud_run_v2_Execution_Builder_getAnnotationsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getAnnotationsCount()
    
    
    public int getAnnotationsCount()

Output only. Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects.

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAnnotationsMap()
    
    
    public Map<String,String> getAnnotationsMap()

Output only. Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects.

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getAnnotationsOrDefault(String key, String defaultValue)
    
    
    public String getAnnotationsOrDefault(String key, String defaultValue)

Output only. Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects.

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getAnnotationsOrThrow(String key)
    
    
    public String getAnnotationsOrThrow(String key)

Output only. Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects.

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getCancelledCount()
    
    
    public int getCancelledCount()

Output only. The number of tasks which reached phase Cancelled.

`int32 cancelled_count = 24 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The cancelledCount.  
  
### getCompletionTime()
    
    
    public Timestamp getCompletionTime()

Output only. Represents time when the execution was completed. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp completion_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The completionTime.  
  
### getCompletionTimeBuilder()
    
    
    public Timestamp.Builder getCompletionTimeBuilder()

Output only. Represents time when the execution was completed. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp completion_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getCompletionTimeOrBuilder()
    
    
    public TimestampOrBuilder getCompletionTimeOrBuilder()

Output only. Represents time when the execution was completed. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp completion_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getConditions(int index)
    
    
    public Condition getConditions(int index)

Output only. The Condition of this Execution, containing its readiness status, and detailed error information in case it did not reach the desired state.

` repeated .google.cloud.run.v2.Condition conditions = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Condition)` |   
  
### getConditionsBuilder(int index)
    
    
    public Condition.Builder getConditionsBuilder(int index)

Output only. The Condition of this Execution, containing its readiness status, and detailed error information in case it did not reach the desired state.

` repeated .google.cloud.run.v2.Condition conditions = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Condition.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Condition.Builder)` |   
  
### getConditionsBuilderList()
    
    
    public List<Condition.Builder> getConditionsBuilderList()

Output only. The Condition of this Execution, containing its readiness status, and detailed error information in case it did not reach the desired state.

` repeated .google.cloud.run.v2.Condition conditions = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Condition.Builder)>` |   
  
### getConditionsCount()
    
    
    public int getConditionsCount()

Output only. The Condition of this Execution, containing its readiness status, and detailed error information in case it did not reach the desired state.

` repeated .google.cloud.run.v2.Condition conditions = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getConditionsList()
    
    
    public List<Condition> getConditionsList()

Output only. The Condition of this Execution, containing its readiness status, and detailed error information in case it did not reach the desired state.

` repeated .google.cloud.run.v2.Condition conditions = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Condition)>` |   
  
### getConditionsOrBuilder(int index)
    
    
    public ConditionOrBuilder getConditionsOrBuilder(int index)

Output only. The Condition of this Execution, containing its readiness status, and detailed error information in case it did not reach the desired state.

` repeated .google.cloud.run.v2.Condition conditions = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConditionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.ConditionOrBuilder)` |   
  
### getConditionsOrBuilderList()
    
    
    public List<? extends ConditionOrBuilder> getConditionsOrBuilderList()

Output only. The Condition of this Execution, containing its readiness status, and detailed error information in case it did not reach the desired state.

` repeated .google.cloud.run.v2.Condition conditions = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.run.v2.ConditionOrBuilder>` |   
  
### getCreateTime()
    
    
    public Timestamp getCreateTime()

Output only. Represents time when the execution was acknowledged by the execution controller. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeBuilder()
    
    
    public Timestamp.Builder getCreateTimeBuilder()

Output only. Represents time when the execution was acknowledged by the execution controller. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getCreateTimeOrBuilder()
    
    
    public TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Represents time when the execution was acknowledged by the execution controller. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getCreator()
    
    
    public String getCreator()

Output only. Email address of the authenticated creator.

`string creator = 32 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The creator.  
  
### getCreatorBytes()
    
    
    public ByteString getCreatorBytes()

Output only. Email address of the authenticated creator.

`string creator = 32 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for creator.  
  
### getDefaultInstanceForType()
    
    
    public Execution getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution)` |   
  
### getDeleteTime()
    
    
    public Timestamp getDeleteTime()

Output only. For a deleted resource, the deletion time. It is only populated as a response to a Delete request.

` .google.protobuf.Timestamp delete_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The deleteTime.  
  
### getDeleteTimeBuilder()
    
    
    public Timestamp.Builder getDeleteTimeBuilder()

Output only. For a deleted resource, the deletion time. It is only populated as a response to a Delete request.

` .google.protobuf.Timestamp delete_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getDeleteTimeOrBuilder()
    
    
    public TimestampOrBuilder getDeleteTimeOrBuilder()

Output only. For a deleted resource, the deletion time. It is only populated as a response to a Delete request.

` .google.protobuf.Timestamp delete_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getEtag()
    
    
    public String getEtag()

Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates.

`string etag = 99 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The etag.  
  
### getEtagBytes()
    
    
    public ByteString getEtagBytes()

Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates.

`string etag = 99 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for etag.  
  
### getExpireTime()
    
    
    public Timestamp getExpireTime()

Output only. For a deleted resource, the time after which it will be permamently deleted. It is only populated as a response to a Delete request.

` .google.protobuf.Timestamp expire_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The expireTime.  
  
### getExpireTimeBuilder()
    
    
    public Timestamp.Builder getExpireTimeBuilder()

Output only. For a deleted resource, the time after which it will be permamently deleted. It is only populated as a response to a Delete request.

` .google.protobuf.Timestamp expire_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getExpireTimeOrBuilder()
    
    
    public TimestampOrBuilder getExpireTimeOrBuilder()

Output only. For a deleted resource, the time after which it will be permamently deleted. It is only populated as a response to a Delete request.

` .google.protobuf.Timestamp expire_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getFailedCount()
    
    
    public int getFailedCount()

Output only. The number of tasks which reached phase Failed.

`int32 failed_count = 21 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The failedCount.  
  
### getGeneration()
    
    
    public long getGeneration()

Output only. A number that monotonically increases every time the user modifies the desired state.

`int64 generation = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The generation.  
  
### getJob()
    
    
    public String getJob()

Output only. The name of the parent Job.

` string job = 12 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The job.  
  
### getJobBytes()
    
    
    public ByteString getJobBytes()

Output only. The name of the parent Job.

` string job = 12 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for job.  
  
### getLabels() (deprecated)
    
    
    public Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder#com_google_cloud_run_v2_Execution_Builder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public int getLabelsCount()

Output only. Unstructured key value map that can be used to organize and categorize objects. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit <https://cloud.google.com/resource-manager/docs/creating-managing-labels> or <https://cloud.google.com/run/docs/configuring/labels>

`map<string, string> labels = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public Map<String,String> getLabelsMap()

Output only. Unstructured key value map that can be used to organize and categorize objects. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit <https://cloud.google.com/resource-manager/docs/creating-managing-labels> or <https://cloud.google.com/run/docs/configuring/labels>

`map<string, string> labels = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public String getLabelsOrDefault(String key, String defaultValue)

Output only. Unstructured key value map that can be used to organize and categorize objects. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit <https://cloud.google.com/resource-manager/docs/creating-managing-labels> or <https://cloud.google.com/run/docs/configuring/labels>

`map<string, string> labels = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

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

Output only. Unstructured key value map that can be used to organize and categorize objects. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit <https://cloud.google.com/resource-manager/docs/creating-managing-labels> or <https://cloud.google.com/run/docs/configuring/labels>

`map<string, string> labels = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLaunchStage()
    
    
    public LaunchStage getLaunchStage()

The least stable launch stage needed to create this resource, as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). Cloud Run supports `ALPHA`, `BETA`, and `GA`.

Note that this value might not be what was used as input. For example, if ALPHA was provided as input in the parent resource, but only BETA and GA-level features are were, this field will be BETA.

`.google.api.LaunchStage launch_stage = 11;`

**Returns**  
---  
**Type** | **Description**  
`com.google.api.LaunchStage` | The launchStage.  
  
### getLaunchStageValue()
    
    
    public int getLaunchStageValue()

The least stable launch stage needed to create this resource, as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). Cloud Run supports `ALPHA`, `BETA`, and `GA`.

Note that this value might not be what was used as input. For example, if ALPHA was provided as input in the parent resource, but only BETA and GA-level features are were, this field will be BETA.

`.google.api.LaunchStage launch_stage = 11;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for launchStage.  
  
### getLogUri()
    
    
    public String getLogUri()

Output only. URI where logs for this execution can be found in Cloud Console.

`string log_uri = 26 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The logUri.  
  
### getLogUriBytes()
    
    
    public ByteString getLogUriBytes()

Output only. URI where logs for this execution can be found in Cloud Console.

`string log_uri = 26 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for logUri.  
  
### getMutableAnnotations() (deprecated)
    
    
    public Map<String,String> getMutableAnnotations()

Use alternate mutation accessors instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getMutableLabels() (deprecated)
    
    
    public Map<String,String> getMutableLabels()

Use alternate mutation accessors instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getName()
    
    
    public String getName()

Output only. The unique name of this Execution.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

Output only. The unique name of this Execution.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getObservedGeneration()
    
    
    public long getObservedGeneration()

Output only. The generation of this Execution. See comments in `reconciling` for additional information on reconciliation process in Cloud Run.

`int64 observed_generation = 18 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The observedGeneration.  
  
### getParallelism()
    
    
    public int getParallelism()

Output only. Specifies the maximum desired number of tasks the execution should run at any given time. Must be <= task_count. The actual number of tasks running in steady state will be less than this number when ((.spec.task_count - .status.successful) < .spec.parallelism), i.e. when the work left to do is less than max parallelism.

`int32 parallelism = 13 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The parallelism.  
  
### getReconciling()
    
    
    public boolean getReconciling()

Output only. Indicates whether the resource's reconciliation is still in progress. See comments in `Job.reconciling` for additional information on reconciliation process in Cloud Run.

`bool reconciling = 16 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The reconciling.  
  
### getRetriedCount()
    
    
    public int getRetriedCount()

Output only. The number of tasks which have retried at least once.

`int32 retried_count = 25 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The retriedCount.  
  
### getRunningCount()
    
    
    public int getRunningCount()

Output only. The number of actively running tasks.

`int32 running_count = 19 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The runningCount.  
  
### getSatisfiesPzs()
    
    
    public boolean getSatisfiesPzs()

Output only. Reserved for future use.

`bool satisfies_pzs = 27 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The satisfiesPzs.  
  
### getStartTime()
    
    
    public Timestamp getStartTime()

Output only. Represents time when the execution started to run. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp start_time = 22 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The startTime.  
  
### getStartTimeBuilder()
    
    
    public Timestamp.Builder getStartTimeBuilder()

Output only. Represents time when the execution started to run. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp start_time = 22 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getStartTimeOrBuilder()
    
    
    public TimestampOrBuilder getStartTimeOrBuilder()

Output only. Represents time when the execution started to run. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp start_time = 22 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getSucceededCount()
    
    
    public int getSucceededCount()

Output only. The number of tasks which reached phase Succeeded.

`int32 succeeded_count = 20 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The succeededCount.  
  
### getTaskCount()
    
    
    public int getTaskCount()

Output only. Specifies the desired number of tasks the execution should run. Setting to 1 means that parallelism is limited to 1 and the success of that task signals the success of the execution.

`int32 task_count = 14 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The taskCount.  
  
### getTemplate()
    
    
    public TaskTemplate getTemplate()

Output only. The template used to create tasks for this execution.

` .google.cloud.run.v2.TaskTemplate template = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TaskTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.TaskTemplate)` | The template.  
  
### getTemplateBuilder()
    
    
    public TaskTemplate.Builder getTemplateBuilder()

Output only. The template used to create tasks for this execution.

` .google.cloud.run.v2.TaskTemplate template = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TaskTemplate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.TaskTemplate.Builder)` |   
  
### getTemplateOrBuilder()
    
    
    public TaskTemplateOrBuilder getTemplateOrBuilder()

Output only. The template used to create tasks for this execution.

` .google.cloud.run.v2.TaskTemplate template = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TaskTemplateOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.TaskTemplateOrBuilder)` |   
  
### getUid()
    
    
    public String getUid()

Output only. Server assigned unique identifier for the Execution. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted.

`string uid = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The uid.  
  
### getUidBytes()
    
    
    public ByteString getUidBytes()

Output only. Server assigned unique identifier for the Execution. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted.

`string uid = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for uid.  
  
### getUpdateTime()
    
    
    public Timestamp getUpdateTime()

Output only. The last-modified time.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeBuilder()
    
    
    public Timestamp.Builder getUpdateTimeBuilder()

Output only. The last-modified time.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getUpdateTimeOrBuilder()
    
    
    public TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The last-modified time.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCompletionTime()
    
    
    public boolean hasCompletionTime()

Output only. Represents time when the execution was completed. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp completion_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the completionTime field is set.  
  
### hasCreateTime()
    
    
    public boolean hasCreateTime()

Output only. Represents time when the execution was acknowledged by the execution controller. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasDeleteTime()
    
    
    public boolean hasDeleteTime()

Output only. For a deleted resource, the deletion time. It is only populated as a response to a Delete request.

` .google.protobuf.Timestamp delete_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the deleteTime field is set.  
  
### hasExpireTime()
    
    
    public boolean hasExpireTime()

Output only. For a deleted resource, the time after which it will be permamently deleted. It is only populated as a response to a Delete request.

` .google.protobuf.Timestamp expire_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the expireTime field is set.  
  
### hasStartTime()
    
    
    public boolean hasStartTime()

Output only. Represents time when the execution started to run. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp start_time = 22 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the startTime field is set.  
  
### hasTemplate()
    
    
    public boolean hasTemplate()

Output only. The template used to create tasks for this execution.

` .google.cloud.run.v2.TaskTemplate template = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the template field is set.  
  
### hasUpdateTime()
    
    
    public boolean hasUpdateTime()

Output only. The last-modified time.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
### internalGetFieldAccessorTable()
    
    
    protected GeneratedMessage.FieldAccessorTable internalGetFieldAccessorTable()

**Returns**  
---  
**Type** | **Description**  
`[FieldAccessorTable](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.FieldAccessorTable.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.internalGetFieldAccessorTable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_internalGetFieldAccessorTable__)

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

com.google.protobuf.GeneratedMessage.Builder.internalGetMapFieldReflection(int)

### internalGetMutableMapFieldReflection(int number)
    
    
    protected MapFieldReflectionAccessor internalGetMutableMapFieldReflection(int number)

**Parameter**  
---  
**Name** | **Description**  
`number` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.MapFieldReflectionAccessor` |   
**Overrides**

com.google.protobuf.GeneratedMessage.Builder.internalGetMutableMapFieldReflection(int)

### isInitialized()
    
    
    public final boolean isInitialized()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_isInitialized__)

### mergeCompletionTime(Timestamp value)
    
    
    public Execution.Builder mergeCompletionTime(Timestamp value)

Output only. Represents time when the execution was completed. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp completion_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### mergeCreateTime(Timestamp value)
    
    
    public Execution.Builder mergeCreateTime(Timestamp value)

Output only. Represents time when the execution was acknowledged by the execution controller. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### mergeDeleteTime(Timestamp value)
    
    
    public Execution.Builder mergeDeleteTime(Timestamp value)

Output only. For a deleted resource, the deletion time. It is only populated as a response to a Delete request.

` .google.protobuf.Timestamp delete_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### mergeExpireTime(Timestamp value)
    
    
    public Execution.Builder mergeExpireTime(Timestamp value)

Output only. For a deleted resource, the time after which it will be permamently deleted. It is only populated as a response to a Delete request.

` .google.protobuf.Timestamp expire_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### mergeFrom(Execution other)
    
    
    public Execution.Builder mergeFrom(Execution other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public Execution.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public Execution.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeStartTime(Timestamp value)
    
    
    public Execution.Builder mergeStartTime(Timestamp value)

Output only. Represents time when the execution started to run. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp start_time = 22 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### mergeTemplate(TaskTemplate value)
    
    
    public Execution.Builder mergeTemplate(TaskTemplate value)

Output only. The template used to create tasks for this execution.

` .google.cloud.run.v2.TaskTemplate template = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[TaskTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.TaskTemplate)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### mergeUpdateTime(Timestamp value)
    
    
    public Execution.Builder mergeUpdateTime(Timestamp value)

Output only. The last-modified time.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### putAllAnnotations(Map<String,String> values)
    
    
    public Execution.Builder putAllAnnotations(Map<String,String> values)

Output only. Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects.

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### putAllLabels(Map<String,String> values)
    
    
    public Execution.Builder putAllLabels(Map<String,String> values)

Output only. Unstructured key value map that can be used to organize and categorize objects. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit <https://cloud.google.com/resource-manager/docs/creating-managing-labels> or <https://cloud.google.com/run/docs/configuring/labels>

`map<string, string> labels = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### putAnnotations(String key, String value)
    
    
    public Execution.Builder putAnnotations(String key, String value)

Output only. Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects.

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### putLabels(String key, String value)
    
    
    public Execution.Builder putLabels(String key, String value)

Output only. Unstructured key value map that can be used to organize and categorize objects. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit <https://cloud.google.com/resource-manager/docs/creating-managing-labels> or <https://cloud.google.com/run/docs/configuring/labels>

`map<string, string> labels = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### removeAnnotations(String key)
    
    
    public Execution.Builder removeAnnotations(String key)

Output only. Unstructured key value map that may be set by external tools to store and arbitrary metadata. They are not queryable and should be preserved when modifying objects.

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### removeConditions(int index)
    
    
    public Execution.Builder removeConditions(int index)

Output only. The Condition of this Execution, containing its readiness status, and detailed error information in case it did not reach the desired state.

` repeated .google.cloud.run.v2.Condition conditions = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### removeLabels(String key)
    
    
    public Execution.Builder removeLabels(String key)

Output only. Unstructured key value map that can be used to organize and categorize objects. User-provided labels are shared with Google's billing system, so they can be used to filter, or break down billing charges by team, component, environment, state, etc. For more information, visit <https://cloud.google.com/resource-manager/docs/creating-managing-labels> or <https://cloud.google.com/run/docs/configuring/labels>

`map<string, string> labels = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### setCancelledCount(int value)
    
    
    public Execution.Builder setCancelledCount(int value)

Output only. The number of tasks which reached phase Cancelled.

`int32 cancelled_count = 24 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The cancelledCount to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setCompletionTime(Timestamp value)
    
    
    public Execution.Builder setCompletionTime(Timestamp value)

Output only. Represents time when the execution was completed. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp completion_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### setCompletionTime(Timestamp.Builder builderForValue)
    
    
    public Execution.Builder setCompletionTime(Timestamp.Builder builderForValue)

Output only. Represents time when the execution was completed. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp completion_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### setConditions(int index, Condition value)
    
    
    public Execution.Builder setConditions(int index, Condition value)

Output only. The Condition of this Execution, containing its readiness status, and detailed error information in case it did not reach the desired state.

` repeated .google.cloud.run.v2.Condition conditions = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Condition](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Condition)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### setConditions(int index, Condition.Builder builderForValue)
    
    
    public Execution.Builder setConditions(int index, Condition.Builder builderForValue)

Output only. The Condition of this Execution, containing its readiness status, and detailed error information in case it did not reach the desired state.

` repeated .google.cloud.run.v2.Condition conditions = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Condition.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Condition.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### setCreateTime(Timestamp value)
    
    
    public Execution.Builder setCreateTime(Timestamp value)

Output only. Represents time when the execution was acknowledged by the execution controller. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### setCreateTime(Timestamp.Builder builderForValue)
    
    
    public Execution.Builder setCreateTime(Timestamp.Builder builderForValue)

Output only. Represents time when the execution was acknowledged by the execution controller. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### setCreator(String value)
    
    
    public Execution.Builder setCreator(String value)

Output only. Email address of the authenticated creator.

`string creator = 32 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The creator to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setCreatorBytes(ByteString value)
    
    
    public Execution.Builder setCreatorBytes(ByteString value)

Output only. Email address of the authenticated creator.

`string creator = 32 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for creator to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setDeleteTime(Timestamp value)
    
    
    public Execution.Builder setDeleteTime(Timestamp value)

Output only. For a deleted resource, the deletion time. It is only populated as a response to a Delete request.

` .google.protobuf.Timestamp delete_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### setDeleteTime(Timestamp.Builder builderForValue)
    
    
    public Execution.Builder setDeleteTime(Timestamp.Builder builderForValue)

Output only. For a deleted resource, the deletion time. It is only populated as a response to a Delete request.

` .google.protobuf.Timestamp delete_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### setEtag(String value)
    
    
    public Execution.Builder setEtag(String value)

Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates.

`string etag = 99 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The etag to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setEtagBytes(ByteString value)
    
    
    public Execution.Builder setEtagBytes(ByteString value)

Output only. A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates.

`string etag = 99 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for etag to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setExpireTime(Timestamp value)
    
    
    public Execution.Builder setExpireTime(Timestamp value)

Output only. For a deleted resource, the time after which it will be permamently deleted. It is only populated as a response to a Delete request.

` .google.protobuf.Timestamp expire_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### setExpireTime(Timestamp.Builder builderForValue)
    
    
    public Execution.Builder setExpireTime(Timestamp.Builder builderForValue)

Output only. For a deleted resource, the time after which it will be permamently deleted. It is only populated as a response to a Delete request.

` .google.protobuf.Timestamp expire_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### setFailedCount(int value)
    
    
    public Execution.Builder setFailedCount(int value)

Output only. The number of tasks which reached phase Failed.

`int32 failed_count = 21 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The failedCount to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setGeneration(long value)
    
    
    public Execution.Builder setGeneration(long value)

Output only. A number that monotonically increases every time the user modifies the desired state.

`int64 generation = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The generation to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setJob(String value)
    
    
    public Execution.Builder setJob(String value)

Output only. The name of the parent Job.

` string job = 12 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The job to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setJobBytes(ByteString value)
    
    
    public Execution.Builder setJobBytes(ByteString value)

Output only. The name of the parent Job.

` string job = 12 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for job to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setLaunchStage(LaunchStage value)
    
    
    public Execution.Builder setLaunchStage(LaunchStage value)

The least stable launch stage needed to create this resource, as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). Cloud Run supports `ALPHA`, `BETA`, and `GA`.

Note that this value might not be what was used as input. For example, if ALPHA was provided as input in the parent resource, but only BETA and GA-level features are were, this field will be BETA.

`.google.api.LaunchStage launch_stage = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `com.google.api.LaunchStage`  
The launchStage to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setLaunchStageValue(int value)
    
    
    public Execution.Builder setLaunchStageValue(int value)

The least stable launch stage needed to create this resource, as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages). Cloud Run supports `ALPHA`, `BETA`, and `GA`.

Note that this value might not be what was used as input. For example, if ALPHA was provided as input in the parent resource, but only BETA and GA-level features are were, this field will be BETA.

`.google.api.LaunchStage launch_stage = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for launchStage to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setLogUri(String value)
    
    
    public Execution.Builder setLogUri(String value)

Output only. URI where logs for this execution can be found in Cloud Console.

`string log_uri = 26 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The logUri to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setLogUriBytes(ByteString value)
    
    
    public Execution.Builder setLogUriBytes(ByteString value)

Output only. URI where logs for this execution can be found in Cloud Console.

`string log_uri = 26 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for logUri to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setName(String value)
    
    
    public Execution.Builder setName(String value)

Output only. The unique name of this Execution.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public Execution.Builder setNameBytes(ByteString value)

Output only. The unique name of this Execution.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setObservedGeneration(long value)
    
    
    public Execution.Builder setObservedGeneration(long value)

Output only. The generation of this Execution. See comments in `reconciling` for additional information on reconciliation process in Cloud Run.

`int64 observed_generation = 18 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The observedGeneration to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setParallelism(int value)
    
    
    public Execution.Builder setParallelism(int value)

Output only. Specifies the maximum desired number of tasks the execution should run at any given time. Must be <= task_count. The actual number of tasks running in steady state will be less than this number when ((.spec.task_count - .status.successful) < .spec.parallelism), i.e. when the work left to do is less than max parallelism.

`int32 parallelism = 13 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The parallelism to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setReconciling(boolean value)
    
    
    public Execution.Builder setReconciling(boolean value)

Output only. Indicates whether the resource's reconciliation is still in progress. See comments in `Job.reconciling` for additional information on reconciliation process in Cloud Run.

`bool reconciling = 16 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The reconciling to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setRetriedCount(int value)
    
    
    public Execution.Builder setRetriedCount(int value)

Output only. The number of tasks which have retried at least once.

`int32 retried_count = 25 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The retriedCount to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setRunningCount(int value)
    
    
    public Execution.Builder setRunningCount(int value)

Output only. The number of actively running tasks.

`int32 running_count = 19 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The runningCount to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setSatisfiesPzs(boolean value)
    
    
    public Execution.Builder setSatisfiesPzs(boolean value)

Output only. Reserved for future use.

`bool satisfies_pzs = 27 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The satisfiesPzs to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setStartTime(Timestamp value)
    
    
    public Execution.Builder setStartTime(Timestamp value)

Output only. Represents time when the execution started to run. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp start_time = 22 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### setStartTime(Timestamp.Builder builderForValue)
    
    
    public Execution.Builder setStartTime(Timestamp.Builder builderForValue)

Output only. Represents time when the execution started to run. It is not guaranteed to be set in happens-before order across separate operations.

` .google.protobuf.Timestamp start_time = 22 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### setSucceededCount(int value)
    
    
    public Execution.Builder setSucceededCount(int value)

Output only. The number of tasks which reached phase Succeeded.

`int32 succeeded_count = 20 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The succeededCount to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setTaskCount(int value)
    
    
    public Execution.Builder setTaskCount(int value)

Output only. Specifies the desired number of tasks the execution should run. Setting to 1 means that parallelism is limited to 1 and the success of that task signals the success of the execution.

`int32 task_count = 14 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The taskCount to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setTemplate(TaskTemplate value)
    
    
    public Execution.Builder setTemplate(TaskTemplate value)

Output only. The template used to create tasks for this execution.

` .google.cloud.run.v2.TaskTemplate template = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[TaskTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.TaskTemplate)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### setTemplate(TaskTemplate.Builder builderForValue)
    
    
    public Execution.Builder setTemplate(TaskTemplate.Builder builderForValue)

Output only. The template used to create tasks for this execution.

` .google.cloud.run.v2.TaskTemplate template = 15 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[TaskTemplate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.TaskTemplate.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### setUid(String value)
    
    
    public Execution.Builder setUid(String value)

Output only. Server assigned unique identifier for the Execution. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted.

`string uid = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The uid to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setUidBytes(ByteString value)
    
    
    public Execution.Builder setUidBytes(ByteString value)

Output only. Server assigned unique identifier for the Execution. The value is a UUID4 string and guaranteed to remain unchanged until the resource is deleted.

`string uid = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for uid to set.  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` | This builder for chaining.  
  
### setUpdateTime(Timestamp value)
    
    
    public Execution.Builder setUpdateTime(Timestamp value)

Output only. The last-modified time.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
### setUpdateTime(Timestamp.Builder builderForValue)
    
    
    public Execution.Builder setUpdateTime(Timestamp.Builder builderForValue)

Output only. The last-modified time.

` .google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Execution.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-run/latest/com.google.cloud.run.v2.Execution.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
