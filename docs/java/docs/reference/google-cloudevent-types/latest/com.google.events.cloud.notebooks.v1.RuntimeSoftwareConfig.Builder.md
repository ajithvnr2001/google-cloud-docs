---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder
title: Class RuntimeSoftwareConfig.Builder (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:10.742972+00:00
---

# Class RuntimeSoftwareConfig.Builder (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RuntimeSoftwareConfig.Builder (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)


    
    
    public static final class RuntimeSoftwareConfig.Builder extends GeneratedMessageV3.Builder<RuntimeSoftwareConfig.Builder> implements RuntimeSoftwareConfigOrBuilder

Specifies the selection and configuration of software inside the runtime. The properties to set on runtime. Properties keys are specified in `key:value` format, for example:

  * `idle_shutdown: true`
  * `idle_shutdown_timeout: 180`
  * `enable_health_monitoring: true`



Protobuf type `google.events.cloud.notebooks.v1.RuntimeSoftwareConfig`

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessageV3.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html) > RuntimeSoftwareConfig.Builder

## Implements

[RuntimeSoftwareConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfigOrBuilder)

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

[GeneratedMessageV3.Builder.addRepeatedField(Descriptors.FieldDescriptor,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_addRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_java_lang_Object_)

[GeneratedMessageV3.Builder.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_clear__)

[GeneratedMessageV3.Builder.clearField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_clearField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessageV3.Builder.clearOneof(Descriptors.OneofDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_clearOneof_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessageV3.Builder.clone()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_clone__)

[GeneratedMessageV3.Builder.getAllFields()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_getAllFields__)

[GeneratedMessageV3.Builder.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_getDescriptorForType__)

[GeneratedMessageV3.Builder.getField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_getField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessageV3.Builder.getFieldBuilder(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_getFieldBuilder_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessageV3.Builder.getOneofFieldDescriptor(Descriptors.OneofDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_getOneofFieldDescriptor_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessageV3.Builder.getParentForChildren()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_getParentForChildren__)

[GeneratedMessageV3.Builder.getRepeatedField(Descriptors.FieldDescriptor,int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_getRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_int_)

[GeneratedMessageV3.Builder.getRepeatedFieldBuilder(Descriptors.FieldDescriptor,int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_getRepeatedFieldBuilder_com_google_protobuf_Descriptors_FieldDescriptor_int_)

[GeneratedMessageV3.Builder.getRepeatedFieldCount(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_getRepeatedFieldCount_com_google_protobuf_Descriptors_FieldDescriptor_)

com.google.protobuf.GeneratedMessageV3.Builder.getUnknownFieldSetBuilder()

[GeneratedMessageV3.Builder.getUnknownFields()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_getUnknownFields__)

[GeneratedMessageV3.Builder.hasField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_hasField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessageV3.Builder.hasOneof(Descriptors.OneofDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_hasOneof_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessageV3.Builder.internalGetFieldAccessorTable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_internalGetFieldAccessorTable__)

[GeneratedMessageV3.Builder.internalGetMapField(int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_internalGetMapField_int_)

com.google.protobuf.GeneratedMessageV3.Builder.internalGetMapFieldReflection(int)

[GeneratedMessageV3.Builder.internalGetMutableMapField(int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_internalGetMutableMapField_int_)

com.google.protobuf.GeneratedMessageV3.Builder.internalGetMutableMapFieldReflection(int)

[GeneratedMessageV3.Builder.isClean()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_isClean__)

[GeneratedMessageV3.Builder.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_isInitialized__)

[GeneratedMessageV3.Builder.markClean()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_markClean__)

[GeneratedMessageV3.Builder.mergeUnknownFields(UnknownFieldSet)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_mergeUnknownFields_com_google_protobuf_UnknownFieldSet_)

com.google.protobuf.GeneratedMessageV3.Builder.mergeUnknownLengthDelimitedField(int,com.google.protobuf.ByteString)

com.google.protobuf.GeneratedMessageV3.Builder.mergeUnknownVarintField(int,int)

[GeneratedMessageV3.Builder.newBuilderForField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_newBuilderForField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessageV3.Builder.onBuilt()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_onBuilt__)

[GeneratedMessageV3.Builder.onChanged()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_onChanged__)

com.google.protobuf.GeneratedMessageV3.Builder.parseUnknownField(com.google.protobuf.CodedInputStream,com.google.protobuf.ExtensionRegistryLite,int)

[GeneratedMessageV3.Builder.setField(Descriptors.FieldDescriptor,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_setField_com_google_protobuf_Descriptors_FieldDescriptor_java_lang_Object_)

[GeneratedMessageV3.Builder.setRepeatedField(Descriptors.FieldDescriptor,int,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_setRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_int_java_lang_Object_)

com.google.protobuf.GeneratedMessageV3.Builder.setUnknownFieldSetBuilder(com.google.protobuf.UnknownFieldSet.Builder)

[GeneratedMessageV3.Builder.setUnknownFields(UnknownFieldSet)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_setUnknownFields_com_google_protobuf_UnknownFieldSet_)

[GeneratedMessageV3.Builder.setUnknownFieldsProto3(UnknownFieldSet)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_setUnknownFieldsProto3_com_google_protobuf_UnknownFieldSet_)

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

### addAllKernels(Iterable<? extends ContainerImage> values)
    
    
    public RuntimeSoftwareConfig.Builder addAllKernels(Iterable<? extends ContainerImage> values)

Optional. Use a list of container images to use as Kernels in the notebook instance.

`repeated .google.events.cloud.notebooks.v1.ContainerImage kernels = 8;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.events.cloud.notebooks.v1.ContainerImage>`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` |   
  
### addKernels(ContainerImage value)
    
    
    public RuntimeSoftwareConfig.Builder addKernels(ContainerImage value)

Optional. Use a list of container images to use as Kernels in the notebook instance.

`repeated .google.events.cloud.notebooks.v1.ContainerImage kernels = 8;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ContainerImage](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.ContainerImage)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` |   
  
### addKernels(ContainerImage.Builder builderForValue)
    
    
    public RuntimeSoftwareConfig.Builder addKernels(ContainerImage.Builder builderForValue)

Optional. Use a list of container images to use as Kernels in the notebook instance.

`repeated .google.events.cloud.notebooks.v1.ContainerImage kernels = 8;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ContainerImage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.ContainerImage.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` |   
  
### addKernels(int index, ContainerImage value)
    
    
    public RuntimeSoftwareConfig.Builder addKernels(int index, ContainerImage value)

Optional. Use a list of container images to use as Kernels in the notebook instance.

`repeated .google.events.cloud.notebooks.v1.ContainerImage kernels = 8;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ContainerImage](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.ContainerImage)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` |   
  
### addKernels(int index, ContainerImage.Builder builderForValue)
    
    
    public RuntimeSoftwareConfig.Builder addKernels(int index, ContainerImage.Builder builderForValue)

Optional. Use a list of container images to use as Kernels in the notebook instance.

`repeated .google.events.cloud.notebooks.v1.ContainerImage kernels = 8;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ContainerImage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.ContainerImage.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` |   
  
### addKernelsBuilder()
    
    
    public ContainerImage.Builder addKernelsBuilder()

Optional. Use a list of container images to use as Kernels in the notebook instance.

`repeated .google.events.cloud.notebooks.v1.ContainerImage kernels = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ContainerImage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.ContainerImage.Builder)` |   
  
### addKernelsBuilder(int index)
    
    
    public ContainerImage.Builder addKernelsBuilder(int index)

Optional. Use a list of container images to use as Kernels in the notebook instance.

`repeated .google.events.cloud.notebooks.v1.ContainerImage kernels = 8;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContainerImage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.ContainerImage.Builder)` |   
  
### addRepeatedField(Descriptors.FieldDescriptor field, Object value)
    
    
    public RuntimeSoftwareConfig.Builder addRepeatedField(Descriptors.FieldDescriptor field, Object value)

**Parameters**  
---  
**Name** | **Description**  
`field` | `[FieldDescriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.FieldDescriptor.html)`  
  
`value` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.addRepeatedField(Descriptors.FieldDescriptor field, Object value)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_addRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_java_lang_Object_)

### build()
    
    
    public RuntimeSoftwareConfig build()

**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig)` |   
  
### buildPartial()
    
    
    public RuntimeSoftwareConfig buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig)` |   
  
### clear()
    
    
    public RuntimeSoftwareConfig.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_clear__)

### clearCustomGpuDriverPath()
    
    
    public RuntimeSoftwareConfig.Builder clearCustomGpuDriverPath()

Specify a custom Cloud Storage path where the GPU driver is stored. If not specified, we'll automatically choose from official GPU drivers.

`string custom_gpu_driver_path = 6;`

**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### clearDisableTerminal()
    
    
    public RuntimeSoftwareConfig.Builder clearDisableTerminal()

Bool indicating whether JupyterLab terminal will be available or not. Default: False

`optional bool disable_terminal = 11;`

**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### clearEnableHealthMonitoring()
    
    
    public RuntimeSoftwareConfig.Builder clearEnableHealthMonitoring()

Verifies core internal services are running. Default: True

`optional bool enable_health_monitoring = 2;`

**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### clearField(Descriptors.FieldDescriptor field)
    
    
    public RuntimeSoftwareConfig.Builder clearField(Descriptors.FieldDescriptor field)

**Parameter**  
---  
**Name** | **Description**  
`field` | `[FieldDescriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.FieldDescriptor.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.clearField(Descriptors.FieldDescriptor field)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_clearField_com_google_protobuf_Descriptors_FieldDescriptor_)

### clearIdleShutdown()
    
    
    public RuntimeSoftwareConfig.Builder clearIdleShutdown()

Runtime will automatically shutdown after idle_shutdown_time. Default: True

`optional bool idle_shutdown = 3;`

**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### clearIdleShutdownTimeout()
    
    
    public RuntimeSoftwareConfig.Builder clearIdleShutdownTimeout()

Time in minutes to wait before shutting down runtime. Default: 180 minutes

`int32 idle_shutdown_timeout = 4;`

**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### clearInstallGpuDriver()
    
    
    public RuntimeSoftwareConfig.Builder clearInstallGpuDriver()

Install Nvidia Driver automatically. Default: True

`bool install_gpu_driver = 5;`

**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### clearKernels()
    
    
    public RuntimeSoftwareConfig.Builder clearKernels()

Optional. Use a list of container images to use as Kernels in the notebook instance.

`repeated .google.events.cloud.notebooks.v1.ContainerImage kernels = 8;`

**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` |   
  
### clearMixerDisabled()
    
    
    public RuntimeSoftwareConfig.Builder clearMixerDisabled()

Bool indicating whether mixer client should be disabled. Default: False

`optional bool mixer_disabled = 13;`

**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### clearNotebookUpgradeSchedule()
    
    
    public RuntimeSoftwareConfig.Builder clearNotebookUpgradeSchedule()

Cron expression in UTC timezone, used to schedule instance auto upgrade. Please follow the [cron format](https://en.wikipedia.org/wiki/Cron).

`string notebook_upgrade_schedule = 1;`

**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### clearOneof(Descriptors.OneofDescriptor oneof)
    
    
    public RuntimeSoftwareConfig.Builder clearOneof(Descriptors.OneofDescriptor oneof)

**Parameter**  
---  
**Name** | **Description**  
`oneof` | `[OneofDescriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.OneofDescriptor.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.clearOneof(Descriptors.OneofDescriptor oneof)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_clearOneof_com_google_protobuf_Descriptors_OneofDescriptor_)

### clearPostStartupScript()
    
    
    public RuntimeSoftwareConfig.Builder clearPostStartupScript()

Path to a Bash script that automatically runs after a notebook instance fully boots up. The path must be a URL or Cloud Storage path (`gs://path-to-file/file-name`).

`string post_startup_script = 7;`

**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### clearPostStartupScriptBehavior()
    
    
    public RuntimeSoftwareConfig.Builder clearPostStartupScriptBehavior()

Behavior for the post startup script.

` .google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.PostStartupScriptBehavior post_startup_script_behavior = 10; `

**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### clearUpgradeable()
    
    
    public RuntimeSoftwareConfig.Builder clearUpgradeable()

Output only. Bool indicating whether an newer image is available in an image family.

`optional bool upgradeable = 9;`

**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### clearVersion()
    
    
    public RuntimeSoftwareConfig.Builder clearVersion()

Output only. version of boot image such as M100, from release label of the image.

`optional string version = 12;`

**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### clone()
    
    
    public RuntimeSoftwareConfig.Builder clone()

**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.clone()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_clone__)

### getCustomGpuDriverPath()
    
    
    public String getCustomGpuDriverPath()

Specify a custom Cloud Storage path where the GPU driver is stored. If not specified, we'll automatically choose from official GPU drivers.

`string custom_gpu_driver_path = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The customGpuDriverPath.  
  
### getCustomGpuDriverPathBytes()
    
    
    public ByteString getCustomGpuDriverPathBytes()

Specify a custom Cloud Storage path where the GPU driver is stored. If not specified, we'll automatically choose from official GPU drivers.

`string custom_gpu_driver_path = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for customGpuDriverPath.  
  
### getDefaultInstanceForType()
    
    
    public RuntimeSoftwareConfig getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_getDescriptorForType__)

### getDisableTerminal()
    
    
    public boolean getDisableTerminal()

Bool indicating whether JupyterLab terminal will be available or not. Default: False

`optional bool disable_terminal = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The disableTerminal.  
  
### getEnableHealthMonitoring()
    
    
    public boolean getEnableHealthMonitoring()

Verifies core internal services are running. Default: True

`optional bool enable_health_monitoring = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableHealthMonitoring.  
  
### getIdleShutdown()
    
    
    public boolean getIdleShutdown()

Runtime will automatically shutdown after idle_shutdown_time. Default: True

`optional bool idle_shutdown = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The idleShutdown.  
  
### getIdleShutdownTimeout()
    
    
    public int getIdleShutdownTimeout()

Time in minutes to wait before shutting down runtime. Default: 180 minutes

`int32 idle_shutdown_timeout = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The idleShutdownTimeout.  
  
### getInstallGpuDriver()
    
    
    public boolean getInstallGpuDriver()

Install Nvidia Driver automatically. Default: True

`bool install_gpu_driver = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The installGpuDriver.  
  
### getKernels(int index)
    
    
    public ContainerImage getKernels(int index)

Optional. Use a list of container images to use as Kernels in the notebook instance.

`repeated .google.events.cloud.notebooks.v1.ContainerImage kernels = 8;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContainerImage](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.ContainerImage)` |   
  
### getKernelsBuilder(int index)
    
    
    public ContainerImage.Builder getKernelsBuilder(int index)

Optional. Use a list of container images to use as Kernels in the notebook instance.

`repeated .google.events.cloud.notebooks.v1.ContainerImage kernels = 8;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContainerImage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.ContainerImage.Builder)` |   
  
### getKernelsBuilderList()
    
    
    public List<ContainerImage.Builder> getKernelsBuilderList()

Optional. Use a list of container images to use as Kernels in the notebook instance.

`repeated .google.events.cloud.notebooks.v1.ContainerImage kernels = 8;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.ContainerImage.Builder)>` |   
  
### getKernelsCount()
    
    
    public int getKernelsCount()

Optional. Use a list of container images to use as Kernels in the notebook instance.

`repeated .google.events.cloud.notebooks.v1.ContainerImage kernels = 8;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getKernelsList()
    
    
    public List<ContainerImage> getKernelsList()

Optional. Use a list of container images to use as Kernels in the notebook instance.

`repeated .google.events.cloud.notebooks.v1.ContainerImage kernels = 8;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ContainerImage](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.ContainerImage)>` |   
  
### getKernelsOrBuilder(int index)
    
    
    public ContainerImageOrBuilder getKernelsOrBuilder(int index)

Optional. Use a list of container images to use as Kernels in the notebook instance.

`repeated .google.events.cloud.notebooks.v1.ContainerImage kernels = 8;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContainerImageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.ContainerImageOrBuilder)` |   
  
### getKernelsOrBuilderList()
    
    
    public List<? extends ContainerImageOrBuilder> getKernelsOrBuilderList()

Optional. Use a list of container images to use as Kernels in the notebook instance.

`repeated .google.events.cloud.notebooks.v1.ContainerImage kernels = 8;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.events.cloud.notebooks.v1.ContainerImageOrBuilder>` |   
  
### getMixerDisabled()
    
    
    public boolean getMixerDisabled()

Bool indicating whether mixer client should be disabled. Default: False

`optional bool mixer_disabled = 13;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The mixerDisabled.  
  
### getNotebookUpgradeSchedule()
    
    
    public String getNotebookUpgradeSchedule()

Cron expression in UTC timezone, used to schedule instance auto upgrade. Please follow the [cron format](https://en.wikipedia.org/wiki/Cron).

`string notebook_upgrade_schedule = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The notebookUpgradeSchedule.  
  
### getNotebookUpgradeScheduleBytes()
    
    
    public ByteString getNotebookUpgradeScheduleBytes()

Cron expression in UTC timezone, used to schedule instance auto upgrade. Please follow the [cron format](https://en.wikipedia.org/wiki/Cron).

`string notebook_upgrade_schedule = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for notebookUpgradeSchedule.  
  
### getPostStartupScript()
    
    
    public String getPostStartupScript()

Path to a Bash script that automatically runs after a notebook instance fully boots up. The path must be a URL or Cloud Storage path (`gs://path-to-file/file-name`).

`string post_startup_script = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The postStartupScript.  
  
### getPostStartupScriptBehavior()
    
    
    public RuntimeSoftwareConfig.PostStartupScriptBehavior getPostStartupScriptBehavior()

Behavior for the post startup script.

` .google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.PostStartupScriptBehavior post_startup_script_behavior = 10; `

**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.PostStartupScriptBehavior](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.PostStartupScriptBehavior)` | The postStartupScriptBehavior.  
  
### getPostStartupScriptBehaviorValue()
    
    
    public int getPostStartupScriptBehaviorValue()

Behavior for the post startup script.

` .google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.PostStartupScriptBehavior post_startup_script_behavior = 10; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for postStartupScriptBehavior.  
  
### getPostStartupScriptBytes()
    
    
    public ByteString getPostStartupScriptBytes()

Path to a Bash script that automatically runs after a notebook instance fully boots up. The path must be a URL or Cloud Storage path (`gs://path-to-file/file-name`).

`string post_startup_script = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for postStartupScript.  
  
### getUpgradeable()
    
    
    public boolean getUpgradeable()

Output only. Bool indicating whether an newer image is available in an image family.

`optional bool upgradeable = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The upgradeable.  
  
### getVersion()
    
    
    public String getVersion()

Output only. version of boot image such as M100, from release label of the image.

`optional string version = 12;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The version.  
  
### getVersionBytes()
    
    
    public ByteString getVersionBytes()

Output only. version of boot image such as M100, from release label of the image.

`optional string version = 12;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for version.  
  
### hasDisableTerminal()
    
    
    public boolean hasDisableTerminal()

Bool indicating whether JupyterLab terminal will be available or not. Default: False

`optional bool disable_terminal = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the disableTerminal field is set.  
  
### hasEnableHealthMonitoring()
    
    
    public boolean hasEnableHealthMonitoring()

Verifies core internal services are running. Default: True

`optional bool enable_health_monitoring = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the enableHealthMonitoring field is set.  
  
### hasIdleShutdown()
    
    
    public boolean hasIdleShutdown()

Runtime will automatically shutdown after idle_shutdown_time. Default: True

`optional bool idle_shutdown = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the idleShutdown field is set.  
  
### hasMixerDisabled()
    
    
    public boolean hasMixerDisabled()

Bool indicating whether mixer client should be disabled. Default: False

`optional bool mixer_disabled = 13;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the mixerDisabled field is set.  
  
### hasUpgradeable()
    
    
    public boolean hasUpgradeable()

Output only. Bool indicating whether an newer image is available in an image family.

`optional bool upgradeable = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the upgradeable field is set.  
  
### hasVersion()
    
    
    public boolean hasVersion()

Output only. version of boot image such as M100, from release label of the image.

`optional string version = 12;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the version field is set.  
  
### internalGetFieldAccessorTable()
    
    
    protected GeneratedMessageV3.FieldAccessorTable internalGetFieldAccessorTable()

**Returns**  
---  
**Type** | **Description**  
`[FieldAccessorTable](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.FieldAccessorTable.html)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.internalGetFieldAccessorTable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_internalGetFieldAccessorTable__)

### isInitialized()
    
    
    public final boolean isInitialized()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_isInitialized__)

### mergeFrom(RuntimeSoftwareConfig other)
    
    
    public RuntimeSoftwareConfig.Builder mergeFrom(RuntimeSoftwareConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RuntimeSoftwareConfig](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public RuntimeSoftwareConfig.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public RuntimeSoftwareConfig.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeUnknownFields(UnknownFieldSet unknownFields)
    
    
    public final RuntimeSoftwareConfig.Builder mergeUnknownFields(UnknownFieldSet unknownFields)

**Parameter**  
---  
**Name** | **Description**  
`unknownFields` | `[UnknownFieldSet](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.UnknownFieldSet.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.mergeUnknownFields(UnknownFieldSet unknownFields)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_mergeUnknownFields_com_google_protobuf_UnknownFieldSet_)

### removeKernels(int index)
    
    
    public RuntimeSoftwareConfig.Builder removeKernels(int index)

Optional. Use a list of container images to use as Kernels in the notebook instance.

`repeated .google.events.cloud.notebooks.v1.ContainerImage kernels = 8;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` |   
  
### setCustomGpuDriverPath(String value)
    
    
    public RuntimeSoftwareConfig.Builder setCustomGpuDriverPath(String value)

Specify a custom Cloud Storage path where the GPU driver is stored. If not specified, we'll automatically choose from official GPU drivers.

`string custom_gpu_driver_path = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The customGpuDriverPath to set.  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### setCustomGpuDriverPathBytes(ByteString value)
    
    
    public RuntimeSoftwareConfig.Builder setCustomGpuDriverPathBytes(ByteString value)

Specify a custom Cloud Storage path where the GPU driver is stored. If not specified, we'll automatically choose from official GPU drivers.

`string custom_gpu_driver_path = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for customGpuDriverPath to set.  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### setDisableTerminal(boolean value)
    
    
    public RuntimeSoftwareConfig.Builder setDisableTerminal(boolean value)

Bool indicating whether JupyterLab terminal will be available or not. Default: False

`optional bool disable_terminal = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The disableTerminal to set.  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### setEnableHealthMonitoring(boolean value)
    
    
    public RuntimeSoftwareConfig.Builder setEnableHealthMonitoring(boolean value)

Verifies core internal services are running. Default: True

`optional bool enable_health_monitoring = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enableHealthMonitoring to set.  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### setField(Descriptors.FieldDescriptor field, Object value)
    
    
    public RuntimeSoftwareConfig.Builder setField(Descriptors.FieldDescriptor field, Object value)

**Parameters**  
---  
**Name** | **Description**  
`field` | `[FieldDescriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.FieldDescriptor.html)`  
  
`value` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.setField(Descriptors.FieldDescriptor field, Object value)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_setField_com_google_protobuf_Descriptors_FieldDescriptor_java_lang_Object_)

### setIdleShutdown(boolean value)
    
    
    public RuntimeSoftwareConfig.Builder setIdleShutdown(boolean value)

Runtime will automatically shutdown after idle_shutdown_time. Default: True

`optional bool idle_shutdown = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The idleShutdown to set.  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### setIdleShutdownTimeout(int value)
    
    
    public RuntimeSoftwareConfig.Builder setIdleShutdownTimeout(int value)

Time in minutes to wait before shutting down runtime. Default: 180 minutes

`int32 idle_shutdown_timeout = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The idleShutdownTimeout to set.  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### setInstallGpuDriver(boolean value)
    
    
    public RuntimeSoftwareConfig.Builder setInstallGpuDriver(boolean value)

Install Nvidia Driver automatically. Default: True

`bool install_gpu_driver = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The installGpuDriver to set.  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### setKernels(int index, ContainerImage value)
    
    
    public RuntimeSoftwareConfig.Builder setKernels(int index, ContainerImage value)

Optional. Use a list of container images to use as Kernels in the notebook instance.

`repeated .google.events.cloud.notebooks.v1.ContainerImage kernels = 8;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ContainerImage](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.ContainerImage)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` |   
  
### setKernels(int index, ContainerImage.Builder builderForValue)
    
    
    public RuntimeSoftwareConfig.Builder setKernels(int index, ContainerImage.Builder builderForValue)

Optional. Use a list of container images to use as Kernels in the notebook instance.

`repeated .google.events.cloud.notebooks.v1.ContainerImage kernels = 8;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ContainerImage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.ContainerImage.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` |   
  
### setMixerDisabled(boolean value)
    
    
    public RuntimeSoftwareConfig.Builder setMixerDisabled(boolean value)

Bool indicating whether mixer client should be disabled. Default: False

`optional bool mixer_disabled = 13;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The mixerDisabled to set.  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### setNotebookUpgradeSchedule(String value)
    
    
    public RuntimeSoftwareConfig.Builder setNotebookUpgradeSchedule(String value)

Cron expression in UTC timezone, used to schedule instance auto upgrade. Please follow the [cron format](https://en.wikipedia.org/wiki/Cron).

`string notebook_upgrade_schedule = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The notebookUpgradeSchedule to set.  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### setNotebookUpgradeScheduleBytes(ByteString value)
    
    
    public RuntimeSoftwareConfig.Builder setNotebookUpgradeScheduleBytes(ByteString value)

Cron expression in UTC timezone, used to schedule instance auto upgrade. Please follow the [cron format](https://en.wikipedia.org/wiki/Cron).

`string notebook_upgrade_schedule = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for notebookUpgradeSchedule to set.  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### setPostStartupScript(String value)
    
    
    public RuntimeSoftwareConfig.Builder setPostStartupScript(String value)

Path to a Bash script that automatically runs after a notebook instance fully boots up. The path must be a URL or Cloud Storage path (`gs://path-to-file/file-name`).

`string post_startup_script = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The postStartupScript to set.  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### setPostStartupScriptBehavior(RuntimeSoftwareConfig.PostStartupScriptBehavior value)
    
    
    public RuntimeSoftwareConfig.Builder setPostStartupScriptBehavior(RuntimeSoftwareConfig.PostStartupScriptBehavior value)

Behavior for the post startup script.

` .google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.PostStartupScriptBehavior post_startup_script_behavior = 10; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[RuntimeSoftwareConfig.PostStartupScriptBehavior](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.PostStartupScriptBehavior)`  
The postStartupScriptBehavior to set.  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### setPostStartupScriptBehaviorValue(int value)
    
    
    public RuntimeSoftwareConfig.Builder setPostStartupScriptBehaviorValue(int value)

Behavior for the post startup script.

` .google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.PostStartupScriptBehavior post_startup_script_behavior = 10; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for postStartupScriptBehavior to set.  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### setPostStartupScriptBytes(ByteString value)
    
    
    public RuntimeSoftwareConfig.Builder setPostStartupScriptBytes(ByteString value)

Path to a Bash script that automatically runs after a notebook instance fully boots up. The path must be a URL or Cloud Storage path (`gs://path-to-file/file-name`).

`string post_startup_script = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for postStartupScript to set.  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### setRepeatedField(Descriptors.FieldDescriptor field, int index, Object value)
    
    
    public RuntimeSoftwareConfig.Builder setRepeatedField(Descriptors.FieldDescriptor field, int index, Object value)

**Parameters**  
---  
**Name** | **Description**  
`field` | `[FieldDescriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.FieldDescriptor.html)`  
  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.setRepeatedField(Descriptors.FieldDescriptor field, int index, Object value)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_setRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_int_java_lang_Object_)

### setUnknownFields(UnknownFieldSet unknownFields)
    
    
    public final RuntimeSoftwareConfig.Builder setUnknownFields(UnknownFieldSet unknownFields)

**Parameter**  
---  
**Name** | **Description**  
`unknownFields` | `[UnknownFieldSet](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.UnknownFieldSet.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` |   
**Overrides**

[GeneratedMessageV3.Builder<BuilderType>.setUnknownFields(UnknownFieldSet unknownFields)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessageV3.Builder.html#com_google_protobuf_GeneratedMessageV3_Builder_setUnknownFields_com_google_protobuf_UnknownFieldSet_)

### setUpgradeable(boolean value)
    
    
    public RuntimeSoftwareConfig.Builder setUpgradeable(boolean value)

Output only. Bool indicating whether an newer image is available in an image family.

`optional bool upgradeable = 9;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The upgradeable to set.  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### setVersion(String value)
    
    
    public RuntimeSoftwareConfig.Builder setVersion(String value)

Output only. version of boot image such as M100, from release label of the image.

`optional string version = 12;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The version to set.  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
### setVersionBytes(ByteString value)
    
    
    public RuntimeSoftwareConfig.Builder setVersionBytes(ByteString value)

Output only. version of boot image such as M100, from release label of the image.

`optional string version = 12;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for version to set.  
**Returns**  
---  
**Type** | **Description**  
`[RuntimeSoftwareConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.notebooks.v1.RuntimeSoftwareConfig.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
