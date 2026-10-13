---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder
title: Class Playbook.Builder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:01:45.755846+00:00
---

# Class Playbook.Builder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Playbook.Builder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.7  0.13.1  0.12.1  0.11.5 
    
    
    public static final class Playbook.Builder extends GeneratedMessage.Builder<Playbook.Builder> implements PlaybookOrBuilder

Playbook is the basic building block to instruct the LLM how to execute a certain task.

A playbook consists of a goal to accomplish, an optional list of step by step instructions (the step instruction may refers to name of the custom or default plugin tools to use) to perform the task, a list of contextual input data to be passed in at the beginning of the invoked, and a list of output parameters to store the playbook result.

Protobuf type `google.cloud.dialogflow.cx.v3.Playbook`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > Playbook.Builder

## Implements

[PlaybookOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybookOrBuilder)

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

### addAllHandlers(Iterable<? extends Handler> values)
    
    
    public Playbook.Builder addAllHandlers(Iterable<? extends Handler> values)

Optional. A list of registered handlers to execuate based on the specified triggers.

` repeated .google.cloud.dialogflow.cx.v3.Handler handlers = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.dialogflow.cx.v3.Handler>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### addAllInlineActions(Iterable<String> values)
    
    
    public Playbook.Builder addAllInlineActions(Iterable<String> values)

Optional. Output only. Names of inline actions scoped to this playbook. These actions are in addition to those belonging to referenced tools, child playbooks, and flows, e.g. actions that are defined in the playbook's code block.

` repeated string inline_actions = 22 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The inlineActions to add.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### addAllInputParameterDefinitions(Iterable<? extends ParameterDefinition> values)
    
    
    public Playbook.Builder addAllInputParameterDefinitions(Iterable<? extends ParameterDefinition> values)

Optional. Defined structured input parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition input_parameter_definitions = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.dialogflow.cx.v3.ParameterDefinition>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### addAllOutputParameterDefinitions(Iterable<? extends ParameterDefinition> values)
    
    
    public Playbook.Builder addAllOutputParameterDefinitions(Iterable<? extends ParameterDefinition> values)

Optional. Defined structured output parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition output_parameter_definitions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.dialogflow.cx.v3.ParameterDefinition>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### addAllReferencedFlows(Iterable<String> values)
    
    
    public Playbook.Builder addAllReferencedFlows(Iterable<String> values)

Output only. The resource name of flows referenced by the current playbook in the instructions.

` repeated string referenced_flows = 12 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The referencedFlows to add.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### addAllReferencedPlaybooks(Iterable<String> values)
    
    
    public Playbook.Builder addAllReferencedPlaybooks(Iterable<String> values)

Output only. The resource name of other playbooks referenced by the current playbook in the instructions.

` repeated string referenced_playbooks = 11 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The referencedPlaybooks to add.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### addAllReferencedTools(Iterable<String> values)
    
    
    public Playbook.Builder addAllReferencedTools(Iterable<String> values)

Optional. The resource name of tools referenced by the current playbook in the instructions. If not provided explicitly, they are will be implied using the tool being referenced in goal and steps.

` repeated string referenced_tools = 13 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The referencedTools to add.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### addHandlers(Handler value)
    
    
    public Playbook.Builder addHandlers(Handler value)

Optional. A list of registered handlers to execuate based on the specified triggers.

` repeated .google.cloud.dialogflow.cx.v3.Handler handlers = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Handler](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Handler)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### addHandlers(Handler.Builder builderForValue)
    
    
    public Playbook.Builder addHandlers(Handler.Builder builderForValue)

Optional. A list of registered handlers to execuate based on the specified triggers.

` repeated .google.cloud.dialogflow.cx.v3.Handler handlers = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Handler.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Handler.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### addHandlers(int index, Handler value)
    
    
    public Playbook.Builder addHandlers(int index, Handler value)

Optional. A list of registered handlers to execuate based on the specified triggers.

` repeated .google.cloud.dialogflow.cx.v3.Handler handlers = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Handler](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Handler)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### addHandlers(int index, Handler.Builder builderForValue)
    
    
    public Playbook.Builder addHandlers(int index, Handler.Builder builderForValue)

Optional. A list of registered handlers to execuate based on the specified triggers.

` repeated .google.cloud.dialogflow.cx.v3.Handler handlers = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Handler.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Handler.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### addHandlersBuilder()
    
    
    public Handler.Builder addHandlersBuilder()

Optional. A list of registered handlers to execuate based on the specified triggers.

` repeated .google.cloud.dialogflow.cx.v3.Handler handlers = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Handler.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Handler.Builder)` |   
  
### addHandlersBuilder(int index)
    
    
    public Handler.Builder addHandlersBuilder(int index)

Optional. A list of registered handlers to execuate based on the specified triggers.

` repeated .google.cloud.dialogflow.cx.v3.Handler handlers = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Handler.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Handler.Builder)` |   
  
### addInlineActions(String value)
    
    
    public Playbook.Builder addInlineActions(String value)

Optional. Output only. Names of inline actions scoped to this playbook. These actions are in addition to those belonging to referenced tools, child playbooks, and flows, e.g. actions that are defined in the playbook's code block.

` repeated string inline_actions = 22 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The inlineActions to add.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### addInlineActionsBytes(ByteString value)
    
    
    public Playbook.Builder addInlineActionsBytes(ByteString value)

Optional. Output only. Names of inline actions scoped to this playbook. These actions are in addition to those belonging to referenced tools, child playbooks, and flows, e.g. actions that are defined in the playbook's code block.

` repeated string inline_actions = 22 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes of the inlineActions to add.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### addInputParameterDefinitions(ParameterDefinition value)
    
    
    public Playbook.Builder addInputParameterDefinitions(ParameterDefinition value)

Optional. Defined structured input parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition input_parameter_definitions = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ParameterDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### addInputParameterDefinitions(ParameterDefinition.Builder builderForValue)
    
    
    public Playbook.Builder addInputParameterDefinitions(ParameterDefinition.Builder builderForValue)

Optional. Defined structured input parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition input_parameter_definitions = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ParameterDefinition.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### addInputParameterDefinitions(int index, ParameterDefinition value)
    
    
    public Playbook.Builder addInputParameterDefinitions(int index, ParameterDefinition value)

Optional. Defined structured input parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition input_parameter_definitions = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ParameterDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### addInputParameterDefinitions(int index, ParameterDefinition.Builder builderForValue)
    
    
    public Playbook.Builder addInputParameterDefinitions(int index, ParameterDefinition.Builder builderForValue)

Optional. Defined structured input parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition input_parameter_definitions = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ParameterDefinition.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### addInputParameterDefinitionsBuilder()
    
    
    public ParameterDefinition.Builder addInputParameterDefinitionsBuilder()

Optional. Defined structured input parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition input_parameter_definitions = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ParameterDefinition.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition.Builder)` |   
  
### addInputParameterDefinitionsBuilder(int index)
    
    
    public ParameterDefinition.Builder addInputParameterDefinitionsBuilder(int index)

Optional. Defined structured input parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition input_parameter_definitions = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ParameterDefinition.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition.Builder)` |   
  
### addOutputParameterDefinitions(ParameterDefinition value)
    
    
    public Playbook.Builder addOutputParameterDefinitions(ParameterDefinition value)

Optional. Defined structured output parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition output_parameter_definitions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ParameterDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### addOutputParameterDefinitions(ParameterDefinition.Builder builderForValue)
    
    
    public Playbook.Builder addOutputParameterDefinitions(ParameterDefinition.Builder builderForValue)

Optional. Defined structured output parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition output_parameter_definitions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ParameterDefinition.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### addOutputParameterDefinitions(int index, ParameterDefinition value)
    
    
    public Playbook.Builder addOutputParameterDefinitions(int index, ParameterDefinition value)

Optional. Defined structured output parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition output_parameter_definitions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ParameterDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### addOutputParameterDefinitions(int index, ParameterDefinition.Builder builderForValue)
    
    
    public Playbook.Builder addOutputParameterDefinitions(int index, ParameterDefinition.Builder builderForValue)

Optional. Defined structured output parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition output_parameter_definitions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ParameterDefinition.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### addOutputParameterDefinitionsBuilder()
    
    
    public ParameterDefinition.Builder addOutputParameterDefinitionsBuilder()

Optional. Defined structured output parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition output_parameter_definitions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ParameterDefinition.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition.Builder)` |   
  
### addOutputParameterDefinitionsBuilder(int index)
    
    
    public ParameterDefinition.Builder addOutputParameterDefinitionsBuilder(int index)

Optional. Defined structured output parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition output_parameter_definitions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ParameterDefinition.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition.Builder)` |   
  
### addReferencedFlows(String value)
    
    
    public Playbook.Builder addReferencedFlows(String value)

Output only. The resource name of flows referenced by the current playbook in the instructions.

` repeated string referenced_flows = 12 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The referencedFlows to add.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### addReferencedFlowsBytes(ByteString value)
    
    
    public Playbook.Builder addReferencedFlowsBytes(ByteString value)

Output only. The resource name of flows referenced by the current playbook in the instructions.

` repeated string referenced_flows = 12 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes of the referencedFlows to add.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### addReferencedPlaybooks(String value)
    
    
    public Playbook.Builder addReferencedPlaybooks(String value)

Output only. The resource name of other playbooks referenced by the current playbook in the instructions.

` repeated string referenced_playbooks = 11 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The referencedPlaybooks to add.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### addReferencedPlaybooksBytes(ByteString value)
    
    
    public Playbook.Builder addReferencedPlaybooksBytes(ByteString value)

Output only. The resource name of other playbooks referenced by the current playbook in the instructions.

` repeated string referenced_playbooks = 11 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes of the referencedPlaybooks to add.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### addReferencedTools(String value)
    
    
    public Playbook.Builder addReferencedTools(String value)

Optional. The resource name of tools referenced by the current playbook in the instructions. If not provided explicitly, they are will be implied using the tool being referenced in goal and steps.

` repeated string referenced_tools = 13 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The referencedTools to add.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### addReferencedToolsBytes(ByteString value)
    
    
    public Playbook.Builder addReferencedToolsBytes(ByteString value)

Optional. The resource name of tools referenced by the current playbook in the instructions. If not provided explicitly, they are will be implied using the tool being referenced in goal and steps.

` repeated string referenced_tools = 13 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes of the referencedTools to add.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### build()
    
    
    public Playbook build()

**Returns**  
---  
**Type** | **Description**  
`[Playbook](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook)` |   
  
### buildPartial()
    
    
    public Playbook buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[Playbook](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook)` |   
  
### clear()
    
    
    public Playbook.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearCodeBlock()
    
    
    public Playbook.Builder clearCodeBlock()

Optional. The playbook's scoped code block, which may implement handlers and actions.

` .google.cloud.dialogflow.cx.v3.CodeBlock code_block = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### clearCreateTime()
    
    
    public Playbook.Builder clearCreateTime()

Output only. The timestamp of initial playbook creation.

` .google.protobuf.Timestamp create_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### clearDisplayName()
    
    
    public Playbook.Builder clearDisplayName()

Required. The human-readable name of the playbook, unique within an agent.

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### clearGoal()
    
    
    public Playbook.Builder clearGoal()

Required. High level description of the goal the playbook intend to accomplish. A goal should be concise since it's visible to other playbooks that may reference this playbook.

`string goal = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### clearHandlers()
    
    
    public Playbook.Builder clearHandlers()

Optional. A list of registered handlers to execuate based on the specified triggers.

` repeated .google.cloud.dialogflow.cx.v3.Handler handlers = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### clearInlineActions()
    
    
    public Playbook.Builder clearInlineActions()

Optional. Output only. Names of inline actions scoped to this playbook. These actions are in addition to those belonging to referenced tools, child playbooks, and flows, e.g. actions that are defined in the playbook's code block.

` repeated string inline_actions = 22 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### clearInputParameterDefinitions()
    
    
    public Playbook.Builder clearInputParameterDefinitions()

Optional. Defined structured input parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition input_parameter_definitions = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### clearInstruction()
    
    
    public Playbook.Builder clearInstruction()

Instruction to accomplish target goal.

`.google.cloud.dialogflow.cx.v3.Playbook.Instruction instruction = 17;`

**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### clearLlmModelSettings()
    
    
    public Playbook.Builder clearLlmModelSettings()

Optional. Llm model settings for the playbook.

` .google.cloud.dialogflow.cx.v3.LlmModelSettings llm_model_settings = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### clearName()
    
    
    public Playbook.Builder clearName()

The unique identifier of the playbook. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### clearOutputParameterDefinitions()
    
    
    public Playbook.Builder clearOutputParameterDefinitions()

Optional. Defined structured output parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition output_parameter_definitions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### clearPlaybookType()
    
    
    public Playbook.Builder clearPlaybookType()

Optional. Type of the playbook.

` .google.cloud.dialogflow.cx.v3.Playbook.PlaybookType playbook_type = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### clearReferencedFlows()
    
    
    public Playbook.Builder clearReferencedFlows()

Output only. The resource name of flows referenced by the current playbook in the instructions.

` repeated string referenced_flows = 12 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### clearReferencedPlaybooks()
    
    
    public Playbook.Builder clearReferencedPlaybooks()

Output only. The resource name of other playbooks referenced by the current playbook in the instructions.

` repeated string referenced_playbooks = 11 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### clearReferencedTools()
    
    
    public Playbook.Builder clearReferencedTools()

Optional. The resource name of tools referenced by the current playbook in the instructions. If not provided explicitly, they are will be implied using the tool being referenced in goal and steps.

` repeated string referenced_tools = 13 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### clearTokenCount()
    
    
    public Playbook.Builder clearTokenCount()

Output only. Estimated number of tokes current playbook takes when sent to the LLM.

`int64 token_count = 8 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### clearUpdateTime()
    
    
    public Playbook.Builder clearUpdateTime()

Output only. Last time the playbook version was updated.

` .google.protobuf.Timestamp update_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### getCodeBlock()
    
    
    public CodeBlock getCodeBlock()

Optional. The playbook's scoped code block, which may implement handlers and actions.

` .google.cloud.dialogflow.cx.v3.CodeBlock code_block = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CodeBlock](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CodeBlock)` | The codeBlock.  
  
### getCodeBlockBuilder()
    
    
    public CodeBlock.Builder getCodeBlockBuilder()

Optional. The playbook's scoped code block, which may implement handlers and actions.

` .google.cloud.dialogflow.cx.v3.CodeBlock code_block = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CodeBlock.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CodeBlock.Builder)` |   
  
### getCodeBlockOrBuilder()
    
    
    public CodeBlockOrBuilder getCodeBlockOrBuilder()

Optional. The playbook's scoped code block, which may implement handlers and actions.

` .google.cloud.dialogflow.cx.v3.CodeBlock code_block = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CodeBlockOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CodeBlockOrBuilder)` |   
  
### getCreateTime()
    
    
    public Timestamp getCreateTime()

Output only. The timestamp of initial playbook creation.

` .google.protobuf.Timestamp create_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeBuilder()
    
    
    public Timestamp.Builder getCreateTimeBuilder()

Output only. The timestamp of initial playbook creation.

` .google.protobuf.Timestamp create_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getCreateTimeOrBuilder()
    
    
    public TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The timestamp of initial playbook creation.

` .google.protobuf.Timestamp create_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDefaultInstanceForType()
    
    
    public Playbook getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Playbook](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook)` |   
  
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

Required. The human-readable name of the playbook, unique within an agent.

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public ByteString getDisplayNameBytes()

Required. The human-readable name of the playbook, unique within an agent.

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getGoal()
    
    
    public String getGoal()

Required. High level description of the goal the playbook intend to accomplish. A goal should be concise since it's visible to other playbooks that may reference this playbook.

`string goal = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The goal.  
  
### getGoalBytes()
    
    
    public ByteString getGoalBytes()

Required. High level description of the goal the playbook intend to accomplish. A goal should be concise since it's visible to other playbooks that may reference this playbook.

`string goal = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for goal.  
  
### getHandlers(int index)
    
    
    public Handler getHandlers(int index)

Optional. A list of registered handlers to execuate based on the specified triggers.

` repeated .google.cloud.dialogflow.cx.v3.Handler handlers = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Handler](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Handler)` |   
  
### getHandlersBuilder(int index)
    
    
    public Handler.Builder getHandlersBuilder(int index)

Optional. A list of registered handlers to execuate based on the specified triggers.

` repeated .google.cloud.dialogflow.cx.v3.Handler handlers = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Handler.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Handler.Builder)` |   
  
### getHandlersBuilderList()
    
    
    public List<Handler.Builder> getHandlersBuilderList()

Optional. A list of registered handlers to execuate based on the specified triggers.

` repeated .google.cloud.dialogflow.cx.v3.Handler handlers = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Handler.Builder)>` |   
  
### getHandlersCount()
    
    
    public int getHandlersCount()

Optional. A list of registered handlers to execuate based on the specified triggers.

` repeated .google.cloud.dialogflow.cx.v3.Handler handlers = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getHandlersList()
    
    
    public List<Handler> getHandlersList()

Optional. A list of registered handlers to execuate based on the specified triggers.

` repeated .google.cloud.dialogflow.cx.v3.Handler handlers = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Handler](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Handler)>` |   
  
### getHandlersOrBuilder(int index)
    
    
    public HandlerOrBuilder getHandlersOrBuilder(int index)

Optional. A list of registered handlers to execuate based on the specified triggers.

` repeated .google.cloud.dialogflow.cx.v3.Handler handlers = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HandlerOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.HandlerOrBuilder)` |   
  
### getHandlersOrBuilderList()
    
    
    public List<? extends HandlerOrBuilder> getHandlersOrBuilderList()

Optional. A list of registered handlers to execuate based on the specified triggers.

` repeated .google.cloud.dialogflow.cx.v3.Handler handlers = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dialogflow.cx.v3.HandlerOrBuilder>` |   
  
### getInlineActions(int index)
    
    
    public String getInlineActions(int index)

Optional. Output only. Names of inline actions scoped to this playbook. These actions are in addition to those belonging to referenced tools, child playbooks, and flows, e.g. actions that are defined in the playbook's code block.

` repeated string inline_actions = 22 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The inlineActions at the given index.  
  
### getInlineActionsBytes(int index)
    
    
    public ByteString getInlineActionsBytes(int index)

Optional. Output only. Names of inline actions scoped to this playbook. These actions are in addition to those belonging to referenced tools, child playbooks, and flows, e.g. actions that are defined in the playbook's code block.

` repeated string inline_actions = 22 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the inlineActions at the given index.  
  
### getInlineActionsCount()
    
    
    public int getInlineActionsCount()

Optional. Output only. Names of inline actions scoped to this playbook. These actions are in addition to those belonging to referenced tools, child playbooks, and flows, e.g. actions that are defined in the playbook's code block.

` repeated string inline_actions = 22 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of inlineActions.  
  
### getInlineActionsList()
    
    
    public ProtocolStringList getInlineActionsList()

Optional. Output only. Names of inline actions scoped to this playbook. These actions are in addition to those belonging to referenced tools, child playbooks, and flows, e.g. actions that are defined in the playbook's code block.

` repeated string inline_actions = 22 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ProtocolStringList](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolStringList.html)` | A list containing the inlineActions.  
  
### getInputParameterDefinitions(int index)
    
    
    public ParameterDefinition getInputParameterDefinitions(int index)

Optional. Defined structured input parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition input_parameter_definitions = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ParameterDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition)` |   
  
### getInputParameterDefinitionsBuilder(int index)
    
    
    public ParameterDefinition.Builder getInputParameterDefinitionsBuilder(int index)

Optional. Defined structured input parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition input_parameter_definitions = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ParameterDefinition.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition.Builder)` |   
  
### getInputParameterDefinitionsBuilderList()
    
    
    public List<ParameterDefinition.Builder> getInputParameterDefinitionsBuilderList()

Optional. Defined structured input parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition input_parameter_definitions = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition.Builder)>` |   
  
### getInputParameterDefinitionsCount()
    
    
    public int getInputParameterDefinitionsCount()

Optional. Defined structured input parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition input_parameter_definitions = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getInputParameterDefinitionsList()
    
    
    public List<ParameterDefinition> getInputParameterDefinitionsList()

Optional. Defined structured input parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition input_parameter_definitions = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ParameterDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition)>` |   
  
### getInputParameterDefinitionsOrBuilder(int index)
    
    
    public ParameterDefinitionOrBuilder getInputParameterDefinitionsOrBuilder(int index)

Optional. Defined structured input parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition input_parameter_definitions = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ParameterDefinitionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinitionOrBuilder)` |   
  
### getInputParameterDefinitionsOrBuilderList()
    
    
    public List<? extends ParameterDefinitionOrBuilder> getInputParameterDefinitionsOrBuilderList()

Optional. Defined structured input parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition input_parameter_definitions = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dialogflow.cx.v3.ParameterDefinitionOrBuilder>` |   
  
### getInstruction()
    
    
    public Playbook.Instruction getInstruction()

Instruction to accomplish target goal.

`.google.cloud.dialogflow.cx.v3.Playbook.Instruction instruction = 17;`

**Returns**  
---  
**Type** | **Description**  
`[Playbook.Instruction](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Instruction)` | The instruction.  
  
### getInstructionBuilder()
    
    
    public Playbook.Instruction.Builder getInstructionBuilder()

Instruction to accomplish target goal.

`.google.cloud.dialogflow.cx.v3.Playbook.Instruction instruction = 17;`

**Returns**  
---  
**Type** | **Description**  
`[Playbook.Instruction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Instruction.Builder)` |   
  
### getInstructionOrBuilder()
    
    
    public Playbook.InstructionOrBuilder getInstructionOrBuilder()

Instruction to accomplish target goal.

`.google.cloud.dialogflow.cx.v3.Playbook.Instruction instruction = 17;`

**Returns**  
---  
**Type** | **Description**  
`[Playbook.InstructionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.InstructionOrBuilder)` |   
  
### getLlmModelSettings()
    
    
    public LlmModelSettings getLlmModelSettings()

Optional. Llm model settings for the playbook.

` .google.cloud.dialogflow.cx.v3.LlmModelSettings llm_model_settings = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LlmModelSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.LlmModelSettings)` | The llmModelSettings.  
  
### getLlmModelSettingsBuilder()
    
    
    public LlmModelSettings.Builder getLlmModelSettingsBuilder()

Optional. Llm model settings for the playbook.

` .google.cloud.dialogflow.cx.v3.LlmModelSettings llm_model_settings = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LlmModelSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.LlmModelSettings.Builder)` |   
  
### getLlmModelSettingsOrBuilder()
    
    
    public LlmModelSettingsOrBuilder getLlmModelSettingsOrBuilder()

Optional. Llm model settings for the playbook.

` .google.cloud.dialogflow.cx.v3.LlmModelSettings llm_model_settings = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LlmModelSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.LlmModelSettingsOrBuilder)` |   
  
### getName()
    
    
    public String getName()

The unique identifier of the playbook. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

The unique identifier of the playbook. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getOutputParameterDefinitions(int index)
    
    
    public ParameterDefinition getOutputParameterDefinitions(int index)

Optional. Defined structured output parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition output_parameter_definitions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ParameterDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition)` |   
  
### getOutputParameterDefinitionsBuilder(int index)
    
    
    public ParameterDefinition.Builder getOutputParameterDefinitionsBuilder(int index)

Optional. Defined structured output parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition output_parameter_definitions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ParameterDefinition.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition.Builder)` |   
  
### getOutputParameterDefinitionsBuilderList()
    
    
    public List<ParameterDefinition.Builder> getOutputParameterDefinitionsBuilderList()

Optional. Defined structured output parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition output_parameter_definitions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition.Builder)>` |   
  
### getOutputParameterDefinitionsCount()
    
    
    public int getOutputParameterDefinitionsCount()

Optional. Defined structured output parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition output_parameter_definitions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getOutputParameterDefinitionsList()
    
    
    public List<ParameterDefinition> getOutputParameterDefinitionsList()

Optional. Defined structured output parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition output_parameter_definitions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ParameterDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition)>` |   
  
### getOutputParameterDefinitionsOrBuilder(int index)
    
    
    public ParameterDefinitionOrBuilder getOutputParameterDefinitionsOrBuilder(int index)

Optional. Defined structured output parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition output_parameter_definitions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ParameterDefinitionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinitionOrBuilder)` |   
  
### getOutputParameterDefinitionsOrBuilderList()
    
    
    public List<? extends ParameterDefinitionOrBuilder> getOutputParameterDefinitionsOrBuilderList()

Optional. Defined structured output parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition output_parameter_definitions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dialogflow.cx.v3.ParameterDefinitionOrBuilder>` |   
  
### getPlaybookType()
    
    
    public Playbook.PlaybookType getPlaybookType()

Optional. Type of the playbook.

` .google.cloud.dialogflow.cx.v3.Playbook.PlaybookType playbook_type = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Playbook.PlaybookType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.PlaybookType)` | The playbookType.  
  
### getPlaybookTypeValue()
    
    
    public int getPlaybookTypeValue()

Optional. Type of the playbook.

` .google.cloud.dialogflow.cx.v3.Playbook.PlaybookType playbook_type = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for playbookType.  
  
### getReferencedFlows(int index)
    
    
    public String getReferencedFlows(int index)

Output only. The resource name of flows referenced by the current playbook in the instructions.

` repeated string referenced_flows = 12 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The referencedFlows at the given index.  
  
### getReferencedFlowsBytes(int index)
    
    
    public ByteString getReferencedFlowsBytes(int index)

Output only. The resource name of flows referenced by the current playbook in the instructions.

` repeated string referenced_flows = 12 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the referencedFlows at the given index.  
  
### getReferencedFlowsCount()
    
    
    public int getReferencedFlowsCount()

Output only. The resource name of flows referenced by the current playbook in the instructions.

` repeated string referenced_flows = 12 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of referencedFlows.  
  
### getReferencedFlowsList()
    
    
    public ProtocolStringList getReferencedFlowsList()

Output only. The resource name of flows referenced by the current playbook in the instructions.

` repeated string referenced_flows = 12 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ProtocolStringList](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolStringList.html)` | A list containing the referencedFlows.  
  
### getReferencedPlaybooks(int index)
    
    
    public String getReferencedPlaybooks(int index)

Output only. The resource name of other playbooks referenced by the current playbook in the instructions.

` repeated string referenced_playbooks = 11 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The referencedPlaybooks at the given index.  
  
### getReferencedPlaybooksBytes(int index)
    
    
    public ByteString getReferencedPlaybooksBytes(int index)

Output only. The resource name of other playbooks referenced by the current playbook in the instructions.

` repeated string referenced_playbooks = 11 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the referencedPlaybooks at the given index.  
  
### getReferencedPlaybooksCount()
    
    
    public int getReferencedPlaybooksCount()

Output only. The resource name of other playbooks referenced by the current playbook in the instructions.

` repeated string referenced_playbooks = 11 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of referencedPlaybooks.  
  
### getReferencedPlaybooksList()
    
    
    public ProtocolStringList getReferencedPlaybooksList()

Output only. The resource name of other playbooks referenced by the current playbook in the instructions.

` repeated string referenced_playbooks = 11 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ProtocolStringList](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolStringList.html)` | A list containing the referencedPlaybooks.  
  
### getReferencedTools(int index)
    
    
    public String getReferencedTools(int index)

Optional. The resource name of tools referenced by the current playbook in the instructions. If not provided explicitly, they are will be implied using the tool being referenced in goal and steps.

` repeated string referenced_tools = 13 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The referencedTools at the given index.  
  
### getReferencedToolsBytes(int index)
    
    
    public ByteString getReferencedToolsBytes(int index)

Optional. The resource name of tools referenced by the current playbook in the instructions. If not provided explicitly, they are will be implied using the tool being referenced in goal and steps.

` repeated string referenced_tools = 13 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the referencedTools at the given index.  
  
### getReferencedToolsCount()
    
    
    public int getReferencedToolsCount()

Optional. The resource name of tools referenced by the current playbook in the instructions. If not provided explicitly, they are will be implied using the tool being referenced in goal and steps.

` repeated string referenced_tools = 13 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of referencedTools.  
  
### getReferencedToolsList()
    
    
    public ProtocolStringList getReferencedToolsList()

Optional. The resource name of tools referenced by the current playbook in the instructions. If not provided explicitly, they are will be implied using the tool being referenced in goal and steps.

` repeated string referenced_tools = 13 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ProtocolStringList](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolStringList.html)` | A list containing the referencedTools.  
  
### getTokenCount()
    
    
    public long getTokenCount()

Output only. Estimated number of tokes current playbook takes when sent to the LLM.

`int64 token_count = 8 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The tokenCount.  
  
### getUpdateTime()
    
    
    public Timestamp getUpdateTime()

Output only. Last time the playbook version was updated.

` .google.protobuf.Timestamp update_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeBuilder()
    
    
    public Timestamp.Builder getUpdateTimeBuilder()

Output only. Last time the playbook version was updated.

` .google.protobuf.Timestamp update_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getUpdateTimeOrBuilder()
    
    
    public TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. Last time the playbook version was updated.

` .google.protobuf.Timestamp update_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCodeBlock()
    
    
    public boolean hasCodeBlock()

Optional. The playbook's scoped code block, which may implement handlers and actions.

` .google.cloud.dialogflow.cx.v3.CodeBlock code_block = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the codeBlock field is set.  
  
### hasCreateTime()
    
    
    public boolean hasCreateTime()

Output only. The timestamp of initial playbook creation.

` .google.protobuf.Timestamp create_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasInstruction()
    
    
    public boolean hasInstruction()

Instruction to accomplish target goal.

`.google.cloud.dialogflow.cx.v3.Playbook.Instruction instruction = 17;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the instruction field is set.  
  
### hasLlmModelSettings()
    
    
    public boolean hasLlmModelSettings()

Optional. Llm model settings for the playbook.

` .google.cloud.dialogflow.cx.v3.LlmModelSettings llm_model_settings = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the llmModelSettings field is set.  
  
### hasUpdateTime()
    
    
    public boolean hasUpdateTime()

Output only. Last time the playbook version was updated.

` .google.protobuf.Timestamp update_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

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

### isInitialized()
    
    
    public final boolean isInitialized()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_isInitialized__)

### mergeCodeBlock(CodeBlock value)
    
    
    public Playbook.Builder mergeCodeBlock(CodeBlock value)

Optional. The playbook's scoped code block, which may implement handlers and actions.

` .google.cloud.dialogflow.cx.v3.CodeBlock code_block = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CodeBlock](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CodeBlock)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### mergeCreateTime(Timestamp value)
    
    
    public Playbook.Builder mergeCreateTime(Timestamp value)

Output only. The timestamp of initial playbook creation.

` .google.protobuf.Timestamp create_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### mergeFrom(Playbook other)
    
    
    public Playbook.Builder mergeFrom(Playbook other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Playbook](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public Playbook.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public Playbook.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeInstruction(Playbook.Instruction value)
    
    
    public Playbook.Builder mergeInstruction(Playbook.Instruction value)

Instruction to accomplish target goal.

`.google.cloud.dialogflow.cx.v3.Playbook.Instruction instruction = 17;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Playbook.Instruction](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Instruction)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### mergeLlmModelSettings(LlmModelSettings value)
    
    
    public Playbook.Builder mergeLlmModelSettings(LlmModelSettings value)

Optional. Llm model settings for the playbook.

` .google.cloud.dialogflow.cx.v3.LlmModelSettings llm_model_settings = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[LlmModelSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.LlmModelSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### mergeUpdateTime(Timestamp value)
    
    
    public Playbook.Builder mergeUpdateTime(Timestamp value)

Output only. Last time the playbook version was updated.

` .google.protobuf.Timestamp update_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### removeHandlers(int index)
    
    
    public Playbook.Builder removeHandlers(int index)

Optional. A list of registered handlers to execuate based on the specified triggers.

` repeated .google.cloud.dialogflow.cx.v3.Handler handlers = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### removeInputParameterDefinitions(int index)
    
    
    public Playbook.Builder removeInputParameterDefinitions(int index)

Optional. Defined structured input parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition input_parameter_definitions = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### removeOutputParameterDefinitions(int index)
    
    
    public Playbook.Builder removeOutputParameterDefinitions(int index)

Optional. Defined structured output parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition output_parameter_definitions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### setCodeBlock(CodeBlock value)
    
    
    public Playbook.Builder setCodeBlock(CodeBlock value)

Optional. The playbook's scoped code block, which may implement handlers and actions.

` .google.cloud.dialogflow.cx.v3.CodeBlock code_block = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CodeBlock](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CodeBlock)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### setCodeBlock(CodeBlock.Builder builderForValue)
    
    
    public Playbook.Builder setCodeBlock(CodeBlock.Builder builderForValue)

Optional. The playbook's scoped code block, which may implement handlers and actions.

` .google.cloud.dialogflow.cx.v3.CodeBlock code_block = 21 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[CodeBlock.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CodeBlock.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### setCreateTime(Timestamp value)
    
    
    public Playbook.Builder setCreateTime(Timestamp value)

Output only. The timestamp of initial playbook creation.

` .google.protobuf.Timestamp create_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### setCreateTime(Timestamp.Builder builderForValue)
    
    
    public Playbook.Builder setCreateTime(Timestamp.Builder builderForValue)

Output only. The timestamp of initial playbook creation.

` .google.protobuf.Timestamp create_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### setDisplayName(String value)
    
    
    public Playbook.Builder setDisplayName(String value)

Required. The human-readable name of the playbook, unique within an agent.

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### setDisplayNameBytes(ByteString value)
    
    
    public Playbook.Builder setDisplayNameBytes(ByteString value)

Required. The human-readable name of the playbook, unique within an agent.

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### setGoal(String value)
    
    
    public Playbook.Builder setGoal(String value)

Required. High level description of the goal the playbook intend to accomplish. A goal should be concise since it's visible to other playbooks that may reference this playbook.

`string goal = 3 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The goal to set.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### setGoalBytes(ByteString value)
    
    
    public Playbook.Builder setGoalBytes(ByteString value)

Required. High level description of the goal the playbook intend to accomplish. A goal should be concise since it's visible to other playbooks that may reference this playbook.

`string goal = 3 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for goal to set.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### setHandlers(int index, Handler value)
    
    
    public Playbook.Builder setHandlers(int index, Handler value)

Optional. A list of registered handlers to execuate based on the specified triggers.

` repeated .google.cloud.dialogflow.cx.v3.Handler handlers = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Handler](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Handler)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### setHandlers(int index, Handler.Builder builderForValue)
    
    
    public Playbook.Builder setHandlers(int index, Handler.Builder builderForValue)

Optional. A list of registered handlers to execuate based on the specified triggers.

` repeated .google.cloud.dialogflow.cx.v3.Handler handlers = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Handler.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Handler.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### setInlineActions(int index, String value)
    
    
    public Playbook.Builder setInlineActions(int index, String value)

Optional. Output only. Names of inline actions scoped to this playbook. These actions are in addition to those belonging to referenced tools, child playbooks, and flows, e.g. actions that are defined in the playbook's code block.

` repeated string inline_actions = 22 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The inlineActions to set.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### setInputParameterDefinitions(int index, ParameterDefinition value)
    
    
    public Playbook.Builder setInputParameterDefinitions(int index, ParameterDefinition value)

Optional. Defined structured input parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition input_parameter_definitions = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ParameterDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### setInputParameterDefinitions(int index, ParameterDefinition.Builder builderForValue)
    
    
    public Playbook.Builder setInputParameterDefinitions(int index, ParameterDefinition.Builder builderForValue)

Optional. Defined structured input parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition input_parameter_definitions = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ParameterDefinition.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### setInstruction(Playbook.Instruction value)
    
    
    public Playbook.Builder setInstruction(Playbook.Instruction value)

Instruction to accomplish target goal.

`.google.cloud.dialogflow.cx.v3.Playbook.Instruction instruction = 17;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Playbook.Instruction](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Instruction)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### setInstruction(Playbook.Instruction.Builder builderForValue)
    
    
    public Playbook.Builder setInstruction(Playbook.Instruction.Builder builderForValue)

Instruction to accomplish target goal.

`.google.cloud.dialogflow.cx.v3.Playbook.Instruction instruction = 17;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Playbook.Instruction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Instruction.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### setLlmModelSettings(LlmModelSettings value)
    
    
    public Playbook.Builder setLlmModelSettings(LlmModelSettings value)

Optional. Llm model settings for the playbook.

` .google.cloud.dialogflow.cx.v3.LlmModelSettings llm_model_settings = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[LlmModelSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.LlmModelSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### setLlmModelSettings(LlmModelSettings.Builder builderForValue)
    
    
    public Playbook.Builder setLlmModelSettings(LlmModelSettings.Builder builderForValue)

Optional. Llm model settings for the playbook.

` .google.cloud.dialogflow.cx.v3.LlmModelSettings llm_model_settings = 14 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[LlmModelSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.LlmModelSettings.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### setName(String value)
    
    
    public Playbook.Builder setName(String value)

The unique identifier of the playbook. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`.

`string name = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public Playbook.Builder setNameBytes(ByteString value)

The unique identifier of the playbook. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`.

`string name = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### setOutputParameterDefinitions(int index, ParameterDefinition value)
    
    
    public Playbook.Builder setOutputParameterDefinitions(int index, ParameterDefinition value)

Optional. Defined structured output parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition output_parameter_definitions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ParameterDefinition](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### setOutputParameterDefinitions(int index, ParameterDefinition.Builder builderForValue)
    
    
    public Playbook.Builder setOutputParameterDefinitions(int index, ParameterDefinition.Builder builderForValue)

Optional. Defined structured output parameters for this playbook.

` repeated .google.cloud.dialogflow.cx.v3.ParameterDefinition output_parameter_definitions = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ParameterDefinition.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ParameterDefinition.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### setPlaybookType(Playbook.PlaybookType value)
    
    
    public Playbook.Builder setPlaybookType(Playbook.PlaybookType value)

Optional. Type of the playbook.

` .google.cloud.dialogflow.cx.v3.Playbook.PlaybookType playbook_type = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Playbook.PlaybookType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.PlaybookType)`  
The playbookType to set.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### setPlaybookTypeValue(int value)
    
    
    public Playbook.Builder setPlaybookTypeValue(int value)

Optional. Type of the playbook.

` .google.cloud.dialogflow.cx.v3.Playbook.PlaybookType playbook_type = 19 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for playbookType to set.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### setReferencedFlows(int index, String value)
    
    
    public Playbook.Builder setReferencedFlows(int index, String value)

Output only. The resource name of flows referenced by the current playbook in the instructions.

` repeated string referenced_flows = 12 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The referencedFlows to set.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### setReferencedPlaybooks(int index, String value)
    
    
    public Playbook.Builder setReferencedPlaybooks(int index, String value)

Output only. The resource name of other playbooks referenced by the current playbook in the instructions.

` repeated string referenced_playbooks = 11 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The referencedPlaybooks to set.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### setReferencedTools(int index, String value)
    
    
    public Playbook.Builder setReferencedTools(int index, String value)

Optional. The resource name of tools referenced by the current playbook in the instructions. If not provided explicitly, they are will be implied using the tool being referenced in goal and steps.

` repeated string referenced_tools = 13 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The referencedTools to set.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### setTokenCount(long value)
    
    
    public Playbook.Builder setTokenCount(long value)

Output only. Estimated number of tokes current playbook takes when sent to the LLM.

`int64 token_count = 8 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The tokenCount to set.  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` | This builder for chaining.  
  
### setUpdateTime(Timestamp value)
    
    
    public Playbook.Builder setUpdateTime(Timestamp value)

Output only. Last time the playbook version was updated.

` .google.protobuf.Timestamp update_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
### setUpdateTime(Timestamp.Builder builderForValue)
    
    
    public Playbook.Builder setUpdateTime(Timestamp.Builder builderForValue)

Output only. Last time the playbook version was updated.

` .google.protobuf.Timestamp update_time = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
