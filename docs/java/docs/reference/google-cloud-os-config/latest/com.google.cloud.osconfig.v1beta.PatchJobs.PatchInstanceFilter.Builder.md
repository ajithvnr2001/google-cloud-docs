---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder
title: Class PatchJobs.PatchInstanceFilter.Builder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:24:18.069644+00:00
---

# Class PatchJobs.PatchInstanceFilter.Builder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PatchJobs.PatchInstanceFilter.Builder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.6  2.4.3  2.3.2 
    
    
    public static final class PatchJobs.PatchInstanceFilter.Builder extends GeneratedMessage.Builder<PatchJobs.PatchInstanceFilter.Builder> implements PatchJobs.PatchInstanceFilterOrBuilder

A filter to target VM instances for patching. The targeted VMs must meet all criteria specified. So if both labels and zones are specified, the patch job targets only VMs with those labels and in those zones.

Protobuf type `google.cloud.osconfig.v1beta.PatchInstanceFilter`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > PatchJobs.PatchInstanceFilter.Builder

## Implements

[PatchJobs.PatchInstanceFilterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilterOrBuilder)

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

### addAllGroupLabels(Iterable<? extends PatchJobs.PatchInstanceFilter.GroupLabel> values)
    
    
    public PatchJobs.PatchInstanceFilter.Builder addAllGroupLabels(Iterable<? extends PatchJobs.PatchInstanceFilter.GroupLabel> values)

Targets VM instances matching at least one of these label sets. This allows targeting of disparate groups, for example "env=prod or env=staging".

` repeated .google.cloud.osconfig.v1beta.PatchInstanceFilter.GroupLabel group_labels = 2; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.GroupLabel>`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` |   
  
### addAllInstanceNamePrefixes(Iterable<String> values)
    
    
    public PatchJobs.PatchInstanceFilter.Builder addAllInstanceNamePrefixes(Iterable<String> values)

Targets VMs whose name starts with one of these prefixes. Similar to labels, this is another way to group VMs when targeting configs, for example prefix="prod-".

`repeated string instance_name_prefixes = 5;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The instanceNamePrefixes to add.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` | This builder for chaining.  
  
### addAllInstances(Iterable<String> values)
    
    
    public PatchJobs.PatchInstanceFilter.Builder addAllInstances(Iterable<String> values)

Targets any of the VM instances specified. Instances are specified by their URI in the form `zones/[ZONE]/instances/[INSTANCE_NAME]`, `projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]`, or `https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]`

`repeated string instances = 4;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The instances to add.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` | This builder for chaining.  
  
### addAllZones(Iterable<String> values)
    
    
    public PatchJobs.PatchInstanceFilter.Builder addAllZones(Iterable<String> values)

Targets VM instances in ANY of these zones. Leave empty to target VM instances in any zone.

`repeated string zones = 3;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The zones to add.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` | This builder for chaining.  
  
### addGroupLabels(PatchJobs.PatchInstanceFilter.GroupLabel value)
    
    
    public PatchJobs.PatchInstanceFilter.Builder addGroupLabels(PatchJobs.PatchInstanceFilter.GroupLabel value)

Targets VM instances matching at least one of these label sets. This allows targeting of disparate groups, for example "env=prod or env=staging".

` repeated .google.cloud.osconfig.v1beta.PatchInstanceFilter.GroupLabel group_labels = 2; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PatchJobs.PatchInstanceFilter.GroupLabel](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.GroupLabel)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` |   
  
### addGroupLabels(PatchJobs.PatchInstanceFilter.GroupLabel.Builder builderForValue)
    
    
    public PatchJobs.PatchInstanceFilter.Builder addGroupLabels(PatchJobs.PatchInstanceFilter.GroupLabel.Builder builderForValue)

Targets VM instances matching at least one of these label sets. This allows targeting of disparate groups, for example "env=prod or env=staging".

` repeated .google.cloud.osconfig.v1beta.PatchInstanceFilter.GroupLabel group_labels = 2; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[PatchJobs.PatchInstanceFilter.GroupLabel.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.GroupLabel.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` |   
  
### addGroupLabels(int index, PatchJobs.PatchInstanceFilter.GroupLabel value)
    
    
    public PatchJobs.PatchInstanceFilter.Builder addGroupLabels(int index, PatchJobs.PatchInstanceFilter.GroupLabel value)

Targets VM instances matching at least one of these label sets. This allows targeting of disparate groups, for example "env=prod or env=staging".

` repeated .google.cloud.osconfig.v1beta.PatchInstanceFilter.GroupLabel group_labels = 2; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[PatchJobs.PatchInstanceFilter.GroupLabel](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.GroupLabel)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` |   
  
### addGroupLabels(int index, PatchJobs.PatchInstanceFilter.GroupLabel.Builder builderForValue)
    
    
    public PatchJobs.PatchInstanceFilter.Builder addGroupLabels(int index, PatchJobs.PatchInstanceFilter.GroupLabel.Builder builderForValue)

Targets VM instances matching at least one of these label sets. This allows targeting of disparate groups, for example "env=prod or env=staging".

` repeated .google.cloud.osconfig.v1beta.PatchInstanceFilter.GroupLabel group_labels = 2; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[PatchJobs.PatchInstanceFilter.GroupLabel.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.GroupLabel.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` |   
  
### addGroupLabelsBuilder()
    
    
    public PatchJobs.PatchInstanceFilter.GroupLabel.Builder addGroupLabelsBuilder()

Targets VM instances matching at least one of these label sets. This allows targeting of disparate groups, for example "env=prod or env=staging".

` repeated .google.cloud.osconfig.v1beta.PatchInstanceFilter.GroupLabel group_labels = 2; `

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.GroupLabel.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.GroupLabel.Builder)` |   
  
### addGroupLabelsBuilder(int index)
    
    
    public PatchJobs.PatchInstanceFilter.GroupLabel.Builder addGroupLabelsBuilder(int index)

Targets VM instances matching at least one of these label sets. This allows targeting of disparate groups, for example "env=prod or env=staging".

` repeated .google.cloud.osconfig.v1beta.PatchInstanceFilter.GroupLabel group_labels = 2; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.GroupLabel.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.GroupLabel.Builder)` |   
  
### addInstanceNamePrefixes(String value)
    
    
    public PatchJobs.PatchInstanceFilter.Builder addInstanceNamePrefixes(String value)

Targets VMs whose name starts with one of these prefixes. Similar to labels, this is another way to group VMs when targeting configs, for example prefix="prod-".

`repeated string instance_name_prefixes = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The instanceNamePrefixes to add.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` | This builder for chaining.  
  
### addInstanceNamePrefixesBytes(ByteString value)
    
    
    public PatchJobs.PatchInstanceFilter.Builder addInstanceNamePrefixesBytes(ByteString value)

Targets VMs whose name starts with one of these prefixes. Similar to labels, this is another way to group VMs when targeting configs, for example prefix="prod-".

`repeated string instance_name_prefixes = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes of the instanceNamePrefixes to add.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` | This builder for chaining.  
  
### addInstances(String value)
    
    
    public PatchJobs.PatchInstanceFilter.Builder addInstances(String value)

Targets any of the VM instances specified. Instances are specified by their URI in the form `zones/[ZONE]/instances/[INSTANCE_NAME]`, `projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]`, or `https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]`

`repeated string instances = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The instances to add.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` | This builder for chaining.  
  
### addInstancesBytes(ByteString value)
    
    
    public PatchJobs.PatchInstanceFilter.Builder addInstancesBytes(ByteString value)

Targets any of the VM instances specified. Instances are specified by their URI in the form `zones/[ZONE]/instances/[INSTANCE_NAME]`, `projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]`, or `https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]`

`repeated string instances = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes of the instances to add.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` | This builder for chaining.  
  
### addZones(String value)
    
    
    public PatchJobs.PatchInstanceFilter.Builder addZones(String value)

Targets VM instances in ANY of these zones. Leave empty to target VM instances in any zone.

`repeated string zones = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The zones to add.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` | This builder for chaining.  
  
### addZonesBytes(ByteString value)
    
    
    public PatchJobs.PatchInstanceFilter.Builder addZonesBytes(ByteString value)

Targets VM instances in ANY of these zones. Leave empty to target VM instances in any zone.

`repeated string zones = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes of the zones to add.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` | This builder for chaining.  
  
### build()
    
    
    public PatchJobs.PatchInstanceFilter build()

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter)` |   
  
### buildPartial()
    
    
    public PatchJobs.PatchInstanceFilter buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter)` |   
  
### clear()
    
    
    public PatchJobs.PatchInstanceFilter.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearAll()
    
    
    public PatchJobs.PatchInstanceFilter.Builder clearAll()

Target all VM instances in the project. If true, no other criteria is permitted.

`bool all = 1;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` | This builder for chaining.  
  
### clearGroupLabels()
    
    
    public PatchJobs.PatchInstanceFilter.Builder clearGroupLabels()

Targets VM instances matching at least one of these label sets. This allows targeting of disparate groups, for example "env=prod or env=staging".

` repeated .google.cloud.osconfig.v1beta.PatchInstanceFilter.GroupLabel group_labels = 2; `

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` |   
  
### clearInstanceNamePrefixes()
    
    
    public PatchJobs.PatchInstanceFilter.Builder clearInstanceNamePrefixes()

Targets VMs whose name starts with one of these prefixes. Similar to labels, this is another way to group VMs when targeting configs, for example prefix="prod-".

`repeated string instance_name_prefixes = 5;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` | This builder for chaining.  
  
### clearInstances()
    
    
    public PatchJobs.PatchInstanceFilter.Builder clearInstances()

Targets any of the VM instances specified. Instances are specified by their URI in the form `zones/[ZONE]/instances/[INSTANCE_NAME]`, `projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]`, or `https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]`

`repeated string instances = 4;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` | This builder for chaining.  
  
### clearZones()
    
    
    public PatchJobs.PatchInstanceFilter.Builder clearZones()

Targets VM instances in ANY of these zones. Leave empty to target VM instances in any zone.

`repeated string zones = 3;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` | This builder for chaining.  
  
### getAll()
    
    
    public boolean getAll()

Target all VM instances in the project. If true, no other criteria is permitted.

`bool all = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The all.  
  
### getDefaultInstanceForType()
    
    
    public PatchJobs.PatchInstanceFilter getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getGroupLabels(int index)
    
    
    public PatchJobs.PatchInstanceFilter.GroupLabel getGroupLabels(int index)

Targets VM instances matching at least one of these label sets. This allows targeting of disparate groups, for example "env=prod or env=staging".

` repeated .google.cloud.osconfig.v1beta.PatchInstanceFilter.GroupLabel group_labels = 2; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.GroupLabel](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.GroupLabel)` |   
  
### getGroupLabelsBuilder(int index)
    
    
    public PatchJobs.PatchInstanceFilter.GroupLabel.Builder getGroupLabelsBuilder(int index)

Targets VM instances matching at least one of these label sets. This allows targeting of disparate groups, for example "env=prod or env=staging".

` repeated .google.cloud.osconfig.v1beta.PatchInstanceFilter.GroupLabel group_labels = 2; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.GroupLabel.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.GroupLabel.Builder)` |   
  
### getGroupLabelsBuilderList()
    
    
    public List<PatchJobs.PatchInstanceFilter.GroupLabel.Builder> getGroupLabelsBuilderList()

Targets VM instances matching at least one of these label sets. This allows targeting of disparate groups, for example "env=prod or env=staging".

` repeated .google.cloud.osconfig.v1beta.PatchInstanceFilter.GroupLabel group_labels = 2; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.GroupLabel.Builder)>` |   
  
### getGroupLabelsCount()
    
    
    public int getGroupLabelsCount()

Targets VM instances matching at least one of these label sets. This allows targeting of disparate groups, for example "env=prod or env=staging".

` repeated .google.cloud.osconfig.v1beta.PatchInstanceFilter.GroupLabel group_labels = 2; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getGroupLabelsList()
    
    
    public List<PatchJobs.PatchInstanceFilter.GroupLabel> getGroupLabelsList()

Targets VM instances matching at least one of these label sets. This allows targeting of disparate groups, for example "env=prod or env=staging".

` repeated .google.cloud.osconfig.v1beta.PatchInstanceFilter.GroupLabel group_labels = 2; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[GroupLabel](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.GroupLabel)>` |   
  
### getGroupLabelsOrBuilder(int index)
    
    
    public PatchJobs.PatchInstanceFilter.GroupLabelOrBuilder getGroupLabelsOrBuilder(int index)

Targets VM instances matching at least one of these label sets. This allows targeting of disparate groups, for example "env=prod or env=staging".

` repeated .google.cloud.osconfig.v1beta.PatchInstanceFilter.GroupLabel group_labels = 2; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.GroupLabelOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.GroupLabelOrBuilder)` |   
  
### getGroupLabelsOrBuilderList()
    
    
    public List<? extends PatchJobs.PatchInstanceFilter.GroupLabelOrBuilder> getGroupLabelsOrBuilderList()

Targets VM instances matching at least one of these label sets. This allows targeting of disparate groups, for example "env=prod or env=staging".

` repeated .google.cloud.osconfig.v1beta.PatchInstanceFilter.GroupLabel group_labels = 2; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.GroupLabelOrBuilder>` |   
  
### getInstanceNamePrefixes(int index)
    
    
    public String getInstanceNamePrefixes(int index)

Targets VMs whose name starts with one of these prefixes. Similar to labels, this is another way to group VMs when targeting configs, for example prefix="prod-".

`repeated string instance_name_prefixes = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The instanceNamePrefixes at the given index.  
  
### getInstanceNamePrefixesBytes(int index)
    
    
    public ByteString getInstanceNamePrefixesBytes(int index)

Targets VMs whose name starts with one of these prefixes. Similar to labels, this is another way to group VMs when targeting configs, for example prefix="prod-".

`repeated string instance_name_prefixes = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the instanceNamePrefixes at the given index.  
  
### getInstanceNamePrefixesCount()
    
    
    public int getInstanceNamePrefixesCount()

Targets VMs whose name starts with one of these prefixes. Similar to labels, this is another way to group VMs when targeting configs, for example prefix="prod-".

`repeated string instance_name_prefixes = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of instanceNamePrefixes.  
  
### getInstanceNamePrefixesList()
    
    
    public ProtocolStringList getInstanceNamePrefixesList()

Targets VMs whose name starts with one of these prefixes. Similar to labels, this is another way to group VMs when targeting configs, for example prefix="prod-".

`repeated string instance_name_prefixes = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ProtocolStringList](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolStringList.html)` | A list containing the instanceNamePrefixes.  
  
### getInstances(int index)
    
    
    public String getInstances(int index)

Targets any of the VM instances specified. Instances are specified by their URI in the form `zones/[ZONE]/instances/[INSTANCE_NAME]`, `projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]`, or `https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]`

`repeated string instances = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The instances at the given index.  
  
### getInstancesBytes(int index)
    
    
    public ByteString getInstancesBytes(int index)

Targets any of the VM instances specified. Instances are specified by their URI in the form `zones/[ZONE]/instances/[INSTANCE_NAME]`, `projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]`, or `https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]`

`repeated string instances = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the instances at the given index.  
  
### getInstancesCount()
    
    
    public int getInstancesCount()

Targets any of the VM instances specified. Instances are specified by their URI in the form `zones/[ZONE]/instances/[INSTANCE_NAME]`, `projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]`, or `https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]`

`repeated string instances = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of instances.  
  
### getInstancesList()
    
    
    public ProtocolStringList getInstancesList()

Targets any of the VM instances specified. Instances are specified by their URI in the form `zones/[ZONE]/instances/[INSTANCE_NAME]`, `projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]`, or `https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]`

`repeated string instances = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ProtocolStringList](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolStringList.html)` | A list containing the instances.  
  
### getZones(int index)
    
    
    public String getZones(int index)

Targets VM instances in ANY of these zones. Leave empty to target VM instances in any zone.

`repeated string zones = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The zones at the given index.  
  
### getZonesBytes(int index)
    
    
    public ByteString getZonesBytes(int index)

Targets VM instances in ANY of these zones. Leave empty to target VM instances in any zone.

`repeated string zones = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the zones at the given index.  
  
### getZonesCount()
    
    
    public int getZonesCount()

Targets VM instances in ANY of these zones. Leave empty to target VM instances in any zone.

`repeated string zones = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of zones.  
  
### getZonesList()
    
    
    public ProtocolStringList getZonesList()

Targets VM instances in ANY of these zones. Leave empty to target VM instances in any zone.

`repeated string zones = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ProtocolStringList](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolStringList.html)` | A list containing the zones.  
  
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

### mergeFrom(PatchJobs.PatchInstanceFilter other)
    
    
    public PatchJobs.PatchInstanceFilter.Builder mergeFrom(PatchJobs.PatchInstanceFilter other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[PatchJobs.PatchInstanceFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public PatchJobs.PatchInstanceFilter.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public PatchJobs.PatchInstanceFilter.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### removeGroupLabels(int index)
    
    
    public PatchJobs.PatchInstanceFilter.Builder removeGroupLabels(int index)

Targets VM instances matching at least one of these label sets. This allows targeting of disparate groups, for example "env=prod or env=staging".

` repeated .google.cloud.osconfig.v1beta.PatchInstanceFilter.GroupLabel group_labels = 2; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` |   
  
### setAll(boolean value)
    
    
    public PatchJobs.PatchInstanceFilter.Builder setAll(boolean value)

Target all VM instances in the project. If true, no other criteria is permitted.

`bool all = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The all to set.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` | This builder for chaining.  
  
### setGroupLabels(int index, PatchJobs.PatchInstanceFilter.GroupLabel value)
    
    
    public PatchJobs.PatchInstanceFilter.Builder setGroupLabels(int index, PatchJobs.PatchInstanceFilter.GroupLabel value)

Targets VM instances matching at least one of these label sets. This allows targeting of disparate groups, for example "env=prod or env=staging".

` repeated .google.cloud.osconfig.v1beta.PatchInstanceFilter.GroupLabel group_labels = 2; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[PatchJobs.PatchInstanceFilter.GroupLabel](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.GroupLabel)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` |   
  
### setGroupLabels(int index, PatchJobs.PatchInstanceFilter.GroupLabel.Builder builderForValue)
    
    
    public PatchJobs.PatchInstanceFilter.Builder setGroupLabels(int index, PatchJobs.PatchInstanceFilter.GroupLabel.Builder builderForValue)

Targets VM instances matching at least one of these label sets. This allows targeting of disparate groups, for example "env=prod or env=staging".

` repeated .google.cloud.osconfig.v1beta.PatchInstanceFilter.GroupLabel group_labels = 2; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[PatchJobs.PatchInstanceFilter.GroupLabel.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.GroupLabel.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` |   
  
### setInstanceNamePrefixes(int index, String value)
    
    
    public PatchJobs.PatchInstanceFilter.Builder setInstanceNamePrefixes(int index, String value)

Targets VMs whose name starts with one of these prefixes. Similar to labels, this is another way to group VMs when targeting configs, for example prefix="prod-".

`repeated string instance_name_prefixes = 5;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The instanceNamePrefixes to set.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` | This builder for chaining.  
  
### setInstances(int index, String value)
    
    
    public PatchJobs.PatchInstanceFilter.Builder setInstances(int index, String value)

Targets any of the VM instances specified. Instances are specified by their URI in the form `zones/[ZONE]/instances/[INSTANCE_NAME]`, `projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]`, or `https://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]`

`repeated string instances = 4;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The instances to set.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` | This builder for chaining.  
  
### setZones(int index, String value)
    
    
    public PatchJobs.PatchInstanceFilter.Builder setZones(int index, String value)

Targets VM instances in ANY of these zones. Leave empty to target VM instances in any zone.

`repeated string zones = 3;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The zones to set.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchInstanceFilter.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
