---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder
title: Class OSPolicyAssignment.InstanceFilter.Builder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:00:16.678125+00:00
---

# Class OSPolicyAssignment.InstanceFilter.Builder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class OSPolicyAssignment.InstanceFilter.Builder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.6  2.4.3  2.3.2 
    
    
    public static final class OSPolicyAssignment.InstanceFilter.Builder extends GeneratedMessage.Builder<OSPolicyAssignment.InstanceFilter.Builder> implements OSPolicyAssignment.InstanceFilterOrBuilder

Filters to select target VMs for an assignment.

If more than one filter criteria is specified below, a VM will be selected if and only if it satisfies all of them.

Protobuf type `google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > OSPolicyAssignment.InstanceFilter.Builder

## Implements

[OSPolicyAssignment.InstanceFilterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilterOrBuilder)

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

### addAllExclusionLabels(Iterable<? extends OSPolicyAssignment.LabelSet> values)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder addAllExclusionLabels(Iterable<? extends OSPolicyAssignment.LabelSet> values)

List of label sets used for VM exclusion.

If the list has more than one label set, the VM is excluded if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet exclusion_labels = 3; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet>`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### addAllInclusionLabels(Iterable<? extends OSPolicyAssignment.LabelSet> values)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder addAllInclusionLabels(Iterable<? extends OSPolicyAssignment.LabelSet> values)

List of label sets used for VM inclusion.

If the list has more than one `LabelSet`, the VM is included if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet inclusion_labels = 2; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet>`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### addAllInventories(Iterable<? extends OSPolicyAssignment.InstanceFilter.Inventory> values)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder addAllInventories(Iterable<? extends OSPolicyAssignment.InstanceFilter.Inventory> values)

List of inventories to select VMs.

A VM is selected if its inventory data matches at least one of the following inventories.

` repeated .google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory inventories = 4; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory>`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### addExclusionLabels(OSPolicyAssignment.LabelSet value)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder addExclusionLabels(OSPolicyAssignment.LabelSet value)

List of label sets used for VM exclusion.

If the list has more than one label set, the VM is excluded if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet exclusion_labels = 3; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[OSPolicyAssignment.LabelSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### addExclusionLabels(OSPolicyAssignment.LabelSet.Builder builderForValue)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder addExclusionLabels(OSPolicyAssignment.LabelSet.Builder builderForValue)

List of label sets used for VM exclusion.

If the list has more than one label set, the VM is excluded if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet exclusion_labels = 3; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[OSPolicyAssignment.LabelSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### addExclusionLabels(int index, OSPolicyAssignment.LabelSet value)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder addExclusionLabels(int index, OSPolicyAssignment.LabelSet value)

List of label sets used for VM exclusion.

If the list has more than one label set, the VM is excluded if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet exclusion_labels = 3; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[OSPolicyAssignment.LabelSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### addExclusionLabels(int index, OSPolicyAssignment.LabelSet.Builder builderForValue)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder addExclusionLabels(int index, OSPolicyAssignment.LabelSet.Builder builderForValue)

List of label sets used for VM exclusion.

If the list has more than one label set, the VM is excluded if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet exclusion_labels = 3; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[OSPolicyAssignment.LabelSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### addExclusionLabelsBuilder()
    
    
    public OSPolicyAssignment.LabelSet.Builder addExclusionLabelsBuilder()

List of label sets used for VM exclusion.

If the list has more than one label set, the VM is excluded if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet exclusion_labels = 3; `

**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.LabelSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet.Builder)` |   
  
### addExclusionLabelsBuilder(int index)
    
    
    public OSPolicyAssignment.LabelSet.Builder addExclusionLabelsBuilder(int index)

List of label sets used for VM exclusion.

If the list has more than one label set, the VM is excluded if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet exclusion_labels = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.LabelSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet.Builder)` |   
  
### addInclusionLabels(OSPolicyAssignment.LabelSet value)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder addInclusionLabels(OSPolicyAssignment.LabelSet value)

List of label sets used for VM inclusion.

If the list has more than one `LabelSet`, the VM is included if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet inclusion_labels = 2; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[OSPolicyAssignment.LabelSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### addInclusionLabels(OSPolicyAssignment.LabelSet.Builder builderForValue)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder addInclusionLabels(OSPolicyAssignment.LabelSet.Builder builderForValue)

List of label sets used for VM inclusion.

If the list has more than one `LabelSet`, the VM is included if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet inclusion_labels = 2; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[OSPolicyAssignment.LabelSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### addInclusionLabels(int index, OSPolicyAssignment.LabelSet value)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder addInclusionLabels(int index, OSPolicyAssignment.LabelSet value)

List of label sets used for VM inclusion.

If the list has more than one `LabelSet`, the VM is included if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet inclusion_labels = 2; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[OSPolicyAssignment.LabelSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### addInclusionLabels(int index, OSPolicyAssignment.LabelSet.Builder builderForValue)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder addInclusionLabels(int index, OSPolicyAssignment.LabelSet.Builder builderForValue)

List of label sets used for VM inclusion.

If the list has more than one `LabelSet`, the VM is included if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet inclusion_labels = 2; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[OSPolicyAssignment.LabelSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### addInclusionLabelsBuilder()
    
    
    public OSPolicyAssignment.LabelSet.Builder addInclusionLabelsBuilder()

List of label sets used for VM inclusion.

If the list has more than one `LabelSet`, the VM is included if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet inclusion_labels = 2; `

**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.LabelSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet.Builder)` |   
  
### addInclusionLabelsBuilder(int index)
    
    
    public OSPolicyAssignment.LabelSet.Builder addInclusionLabelsBuilder(int index)

List of label sets used for VM inclusion.

If the list has more than one `LabelSet`, the VM is included if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet inclusion_labels = 2; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.LabelSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet.Builder)` |   
  
### addInventories(OSPolicyAssignment.InstanceFilter.Inventory value)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder addInventories(OSPolicyAssignment.InstanceFilter.Inventory value)

List of inventories to select VMs.

A VM is selected if its inventory data matches at least one of the following inventories.

` repeated .google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory inventories = 4; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[OSPolicyAssignment.InstanceFilter.Inventory](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### addInventories(OSPolicyAssignment.InstanceFilter.Inventory.Builder builderForValue)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder addInventories(OSPolicyAssignment.InstanceFilter.Inventory.Builder builderForValue)

List of inventories to select VMs.

A VM is selected if its inventory data matches at least one of the following inventories.

` repeated .google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory inventories = 4; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[OSPolicyAssignment.InstanceFilter.Inventory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### addInventories(int index, OSPolicyAssignment.InstanceFilter.Inventory value)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder addInventories(int index, OSPolicyAssignment.InstanceFilter.Inventory value)

List of inventories to select VMs.

A VM is selected if its inventory data matches at least one of the following inventories.

` repeated .google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory inventories = 4; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[OSPolicyAssignment.InstanceFilter.Inventory](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### addInventories(int index, OSPolicyAssignment.InstanceFilter.Inventory.Builder builderForValue)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder addInventories(int index, OSPolicyAssignment.InstanceFilter.Inventory.Builder builderForValue)

List of inventories to select VMs.

A VM is selected if its inventory data matches at least one of the following inventories.

` repeated .google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory inventories = 4; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[OSPolicyAssignment.InstanceFilter.Inventory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### addInventoriesBuilder()
    
    
    public OSPolicyAssignment.InstanceFilter.Inventory.Builder addInventoriesBuilder()

List of inventories to select VMs.

A VM is selected if its inventory data matches at least one of the following inventories.

` repeated .google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory inventories = 4; `

**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Inventory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory.Builder)` |   
  
### addInventoriesBuilder(int index)
    
    
    public OSPolicyAssignment.InstanceFilter.Inventory.Builder addInventoriesBuilder(int index)

List of inventories to select VMs.

A VM is selected if its inventory data matches at least one of the following inventories.

` repeated .google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory inventories = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Inventory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory.Builder)` |   
  
### build()
    
    
    public OSPolicyAssignment.InstanceFilter build()

**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter)` |   
  
### buildPartial()
    
    
    public OSPolicyAssignment.InstanceFilter buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter)` |   
  
### clear()
    
    
    public OSPolicyAssignment.InstanceFilter.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearAll()
    
    
    public OSPolicyAssignment.InstanceFilter.Builder clearAll()

Target all VMs in the project. If true, no other criteria is permitted.

`bool all = 1;`

**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` | This builder for chaining.  
  
### clearExclusionLabels()
    
    
    public OSPolicyAssignment.InstanceFilter.Builder clearExclusionLabels()

List of label sets used for VM exclusion.

If the list has more than one label set, the VM is excluded if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet exclusion_labels = 3; `

**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### clearInclusionLabels()
    
    
    public OSPolicyAssignment.InstanceFilter.Builder clearInclusionLabels()

List of label sets used for VM inclusion.

If the list has more than one `LabelSet`, the VM is included if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet inclusion_labels = 2; `

**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### clearInventories()
    
    
    public OSPolicyAssignment.InstanceFilter.Builder clearInventories()

List of inventories to select VMs.

A VM is selected if its inventory data matches at least one of the following inventories.

` repeated .google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory inventories = 4; `

**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### getAll()
    
    
    public boolean getAll()

Target all VMs in the project. If true, no other criteria is permitted.

`bool all = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The all.  
  
### getDefaultInstanceForType()
    
    
    public OSPolicyAssignment.InstanceFilter getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getExclusionLabels(int index)
    
    
    public OSPolicyAssignment.LabelSet getExclusionLabels(int index)

List of label sets used for VM exclusion.

If the list has more than one label set, the VM is excluded if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet exclusion_labels = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.LabelSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet)` |   
  
### getExclusionLabelsBuilder(int index)
    
    
    public OSPolicyAssignment.LabelSet.Builder getExclusionLabelsBuilder(int index)

List of label sets used for VM exclusion.

If the list has more than one label set, the VM is excluded if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet exclusion_labels = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.LabelSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet.Builder)` |   
  
### getExclusionLabelsBuilderList()
    
    
    public List<OSPolicyAssignment.LabelSet.Builder> getExclusionLabelsBuilderList()

List of label sets used for VM exclusion.

If the list has more than one label set, the VM is excluded if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet exclusion_labels = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet.Builder)>` |   
  
### getExclusionLabelsCount()
    
    
    public int getExclusionLabelsCount()

List of label sets used for VM exclusion.

If the list has more than one label set, the VM is excluded if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet exclusion_labels = 3; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getExclusionLabelsList()
    
    
    public List<OSPolicyAssignment.LabelSet> getExclusionLabelsList()

List of label sets used for VM exclusion.

If the list has more than one label set, the VM is excluded if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet exclusion_labels = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[LabelSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet)>` |   
  
### getExclusionLabelsOrBuilder(int index)
    
    
    public OSPolicyAssignment.LabelSetOrBuilder getExclusionLabelsOrBuilder(int index)

List of label sets used for VM exclusion.

If the list has more than one label set, the VM is excluded if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet exclusion_labels = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.LabelSetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSetOrBuilder)` |   
  
### getExclusionLabelsOrBuilderList()
    
    
    public List<? extends OSPolicyAssignment.LabelSetOrBuilder> getExclusionLabelsOrBuilderList()

List of label sets used for VM exclusion.

If the list has more than one label set, the VM is excluded if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet exclusion_labels = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSetOrBuilder>` |   
  
### getInclusionLabels(int index)
    
    
    public OSPolicyAssignment.LabelSet getInclusionLabels(int index)

List of label sets used for VM inclusion.

If the list has more than one `LabelSet`, the VM is included if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet inclusion_labels = 2; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.LabelSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet)` |   
  
### getInclusionLabelsBuilder(int index)
    
    
    public OSPolicyAssignment.LabelSet.Builder getInclusionLabelsBuilder(int index)

List of label sets used for VM inclusion.

If the list has more than one `LabelSet`, the VM is included if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet inclusion_labels = 2; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.LabelSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet.Builder)` |   
  
### getInclusionLabelsBuilderList()
    
    
    public List<OSPolicyAssignment.LabelSet.Builder> getInclusionLabelsBuilderList()

List of label sets used for VM inclusion.

If the list has more than one `LabelSet`, the VM is included if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet inclusion_labels = 2; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet.Builder)>` |   
  
### getInclusionLabelsCount()
    
    
    public int getInclusionLabelsCount()

List of label sets used for VM inclusion.

If the list has more than one `LabelSet`, the VM is included if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet inclusion_labels = 2; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getInclusionLabelsList()
    
    
    public List<OSPolicyAssignment.LabelSet> getInclusionLabelsList()

List of label sets used for VM inclusion.

If the list has more than one `LabelSet`, the VM is included if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet inclusion_labels = 2; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[LabelSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet)>` |   
  
### getInclusionLabelsOrBuilder(int index)
    
    
    public OSPolicyAssignment.LabelSetOrBuilder getInclusionLabelsOrBuilder(int index)

List of label sets used for VM inclusion.

If the list has more than one `LabelSet`, the VM is included if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet inclusion_labels = 2; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.LabelSetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSetOrBuilder)` |   
  
### getInclusionLabelsOrBuilderList()
    
    
    public List<? extends OSPolicyAssignment.LabelSetOrBuilder> getInclusionLabelsOrBuilderList()

List of label sets used for VM inclusion.

If the list has more than one `LabelSet`, the VM is included if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet inclusion_labels = 2; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSetOrBuilder>` |   
  
### getInventories(int index)
    
    
    public OSPolicyAssignment.InstanceFilter.Inventory getInventories(int index)

List of inventories to select VMs.

A VM is selected if its inventory data matches at least one of the following inventories.

` repeated .google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory inventories = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Inventory](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory)` |   
  
### getInventoriesBuilder(int index)
    
    
    public OSPolicyAssignment.InstanceFilter.Inventory.Builder getInventoriesBuilder(int index)

List of inventories to select VMs.

A VM is selected if its inventory data matches at least one of the following inventories.

` repeated .google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory inventories = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Inventory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory.Builder)` |   
  
### getInventoriesBuilderList()
    
    
    public List<OSPolicyAssignment.InstanceFilter.Inventory.Builder> getInventoriesBuilderList()

List of inventories to select VMs.

A VM is selected if its inventory data matches at least one of the following inventories.

` repeated .google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory inventories = 4; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory.Builder)>` |   
  
### getInventoriesCount()
    
    
    public int getInventoriesCount()

List of inventories to select VMs.

A VM is selected if its inventory data matches at least one of the following inventories.

` repeated .google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory inventories = 4; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getInventoriesList()
    
    
    public List<OSPolicyAssignment.InstanceFilter.Inventory> getInventoriesList()

List of inventories to select VMs.

A VM is selected if its inventory data matches at least one of the following inventories.

` repeated .google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory inventories = 4; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Inventory](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory)>` |   
  
### getInventoriesOrBuilder(int index)
    
    
    public OSPolicyAssignment.InstanceFilter.InventoryOrBuilder getInventoriesOrBuilder(int index)

List of inventories to select VMs.

A VM is selected if its inventory data matches at least one of the following inventories.

` repeated .google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory inventories = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.InventoryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.InventoryOrBuilder)` |   
  
### getInventoriesOrBuilderList()
    
    
    public List<? extends OSPolicyAssignment.InstanceFilter.InventoryOrBuilder> getInventoriesOrBuilderList()

List of inventories to select VMs.

A VM is selected if its inventory data matches at least one of the following inventories.

` repeated .google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory inventories = 4; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.InventoryOrBuilder>` |   
  
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

### mergeFrom(OSPolicyAssignment.InstanceFilter other)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder mergeFrom(OSPolicyAssignment.InstanceFilter other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[OSPolicyAssignment.InstanceFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### removeExclusionLabels(int index)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder removeExclusionLabels(int index)

List of label sets used for VM exclusion.

If the list has more than one label set, the VM is excluded if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet exclusion_labels = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### removeInclusionLabels(int index)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder removeInclusionLabels(int index)

List of label sets used for VM inclusion.

If the list has more than one `LabelSet`, the VM is included if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet inclusion_labels = 2; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### removeInventories(int index)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder removeInventories(int index)

List of inventories to select VMs.

A VM is selected if its inventory data matches at least one of the following inventories.

` repeated .google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory inventories = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### setAll(boolean value)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder setAll(boolean value)

Target all VMs in the project. If true, no other criteria is permitted.

`bool all = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The all to set.  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` | This builder for chaining.  
  
### setExclusionLabels(int index, OSPolicyAssignment.LabelSet value)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder setExclusionLabels(int index, OSPolicyAssignment.LabelSet value)

List of label sets used for VM exclusion.

If the list has more than one label set, the VM is excluded if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet exclusion_labels = 3; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[OSPolicyAssignment.LabelSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### setExclusionLabels(int index, OSPolicyAssignment.LabelSet.Builder builderForValue)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder setExclusionLabels(int index, OSPolicyAssignment.LabelSet.Builder builderForValue)

List of label sets used for VM exclusion.

If the list has more than one label set, the VM is excluded if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet exclusion_labels = 3; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[OSPolicyAssignment.LabelSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### setInclusionLabels(int index, OSPolicyAssignment.LabelSet value)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder setInclusionLabels(int index, OSPolicyAssignment.LabelSet value)

List of label sets used for VM inclusion.

If the list has more than one `LabelSet`, the VM is included if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet inclusion_labels = 2; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[OSPolicyAssignment.LabelSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### setInclusionLabels(int index, OSPolicyAssignment.LabelSet.Builder builderForValue)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder setInclusionLabels(int index, OSPolicyAssignment.LabelSet.Builder builderForValue)

List of label sets used for VM inclusion.

If the list has more than one `LabelSet`, the VM is included if any of the label sets are applicable for the VM.

`repeated .google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet inclusion_labels = 2; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[OSPolicyAssignment.LabelSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.LabelSet.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### setInventories(int index, OSPolicyAssignment.InstanceFilter.Inventory value)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder setInventories(int index, OSPolicyAssignment.InstanceFilter.Inventory value)

List of inventories to select VMs.

A VM is selected if its inventory data matches at least one of the following inventories.

` repeated .google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory inventories = 4; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[OSPolicyAssignment.InstanceFilter.Inventory](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
### setInventories(int index, OSPolicyAssignment.InstanceFilter.Inventory.Builder builderForValue)
    
    
    public OSPolicyAssignment.InstanceFilter.Builder setInventories(int index, OSPolicyAssignment.InstanceFilter.Inventory.Builder builderForValue)

List of inventories to select VMs.

A VM is selected if its inventory data matches at least one of the following inventories.

` repeated .google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory inventories = 4; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[OSPolicyAssignment.InstanceFilter.Inventory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Inventory.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OSPolicyAssignment.InstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.OSPolicyAssignment.InstanceFilter.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
