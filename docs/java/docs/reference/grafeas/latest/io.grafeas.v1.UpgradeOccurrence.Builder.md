---
url: https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence.Builder
title: Class UpgradeOccurrence.Builder (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:15.663826+00:00
---

# Class UpgradeOccurrence.Builder (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class UpgradeOccurrence.Builder (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.5  2.3.1  2.2.3  2.1.3 
    
    
    public static final class UpgradeOccurrence.Builder extends GeneratedMessage.Builder<UpgradeOccurrence.Builder> implements UpgradeOccurrenceOrBuilder

An Upgrade Occurrence represents that a specific resource_url could install a specific upgrade. This presence is supplied via local sources (i.e. it is present in the mirror and the running system has noticed its availability). For Windows, both distribution and windows_update contain information for the Windows update.

Protobuf type `grafeas.v1.UpgradeOccurrence`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > UpgradeOccurrence.Builder

## Implements

[UpgradeOccurrenceOrBuilder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrenceOrBuilder)

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
    
    
    public UpgradeOccurrence build()

**Returns**  
---  
**Type** | **Description**  
`[UpgradeOccurrence](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence)` |   
  
### buildPartial()
    
    
    public UpgradeOccurrence buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[UpgradeOccurrence](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence)` |   
  
### clear()
    
    
    public UpgradeOccurrence.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[UpgradeOccurrence.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearDistribution()
    
    
    public UpgradeOccurrence.Builder clearDistribution()

Metadata about the upgrade for available for the specific operating system for the resource_url. This allows efficient filtering, as well as making it easier to use the occurrence.

`.grafeas.v1.UpgradeDistribution distribution = 4;`

**Returns**  
---  
**Type** | **Description**  
`[UpgradeOccurrence.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence.Builder)` |   
  
### clearPackage()
    
    
    public UpgradeOccurrence.Builder clearPackage()

Required for non-Windows OS. The package this Upgrade is for.

`string package = 1;`

**Returns**  
---  
**Type** | **Description**  
`[UpgradeOccurrence.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence.Builder)` | This builder for chaining.  
  
### clearParsedVersion()
    
    
    public UpgradeOccurrence.Builder clearParsedVersion()

Required for non-Windows OS. The version of the package in a machine + human readable form.

`.grafeas.v1.Version parsed_version = 3;`

**Returns**  
---  
**Type** | **Description**  
`[UpgradeOccurrence.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence.Builder)` |   
  
### clearWindowsUpdate()
    
    
    public UpgradeOccurrence.Builder clearWindowsUpdate()

Required for Windows OS. Represents the metadata about the Windows update.

`.grafeas.v1.WindowsUpdate windows_update = 5;`

**Returns**  
---  
**Type** | **Description**  
`[UpgradeOccurrence.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence.Builder)` |   
  
### getDefaultInstanceForType()
    
    
    public UpgradeOccurrence getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[UpgradeOccurrence](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getDistribution()
    
    
    public UpgradeDistribution getDistribution()

Metadata about the upgrade for available for the specific operating system for the resource_url. This allows efficient filtering, as well as making it easier to use the occurrence.

`.grafeas.v1.UpgradeDistribution distribution = 4;`

**Returns**  
---  
**Type** | **Description**  
`[UpgradeDistribution](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeDistribution)` | The distribution.  
  
### getDistributionBuilder()
    
    
    public UpgradeDistribution.Builder getDistributionBuilder()

Metadata about the upgrade for available for the specific operating system for the resource_url. This allows efficient filtering, as well as making it easier to use the occurrence.

`.grafeas.v1.UpgradeDistribution distribution = 4;`

**Returns**  
---  
**Type** | **Description**  
`[UpgradeDistribution.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeDistribution.Builder)` |   
  
### getDistributionOrBuilder()
    
    
    public UpgradeDistributionOrBuilder getDistributionOrBuilder()

Metadata about the upgrade for available for the specific operating system for the resource_url. This allows efficient filtering, as well as making it easier to use the occurrence.

`.grafeas.v1.UpgradeDistribution distribution = 4;`

**Returns**  
---  
**Type** | **Description**  
`[UpgradeDistributionOrBuilder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeDistributionOrBuilder)` |   
  
### getPackage()
    
    
    public String getPackage()

Required for non-Windows OS. The package this Upgrade is for.

`string package = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The package.  
  
### getPackageBytes()
    
    
    public ByteString getPackageBytes()

Required for non-Windows OS. The package this Upgrade is for.

`string package = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for package.  
  
### getParsedVersion()
    
    
    public Version getParsedVersion()

Required for non-Windows OS. The version of the package in a machine + human readable form.

`.grafeas.v1.Version parsed_version = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Version](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Version)` | The parsedVersion.  
  
### getParsedVersionBuilder()
    
    
    public Version.Builder getParsedVersionBuilder()

Required for non-Windows OS. The version of the package in a machine + human readable form.

`.grafeas.v1.Version parsed_version = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Version.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Version.Builder)` |   
  
### getParsedVersionOrBuilder()
    
    
    public VersionOrBuilder getParsedVersionOrBuilder()

Required for non-Windows OS. The version of the package in a machine + human readable form.

`.grafeas.v1.Version parsed_version = 3;`

**Returns**  
---  
**Type** | **Description**  
`[VersionOrBuilder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.VersionOrBuilder)` |   
  
### getWindowsUpdate()
    
    
    public WindowsUpdate getWindowsUpdate()

Required for Windows OS. Represents the metadata about the Windows update.

`.grafeas.v1.WindowsUpdate windows_update = 5;`

**Returns**  
---  
**Type** | **Description**  
`[WindowsUpdate](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.WindowsUpdate)` | The windowsUpdate.  
  
### getWindowsUpdateBuilder()
    
    
    public WindowsUpdate.Builder getWindowsUpdateBuilder()

Required for Windows OS. Represents the metadata about the Windows update.

`.grafeas.v1.WindowsUpdate windows_update = 5;`

**Returns**  
---  
**Type** | **Description**  
`[WindowsUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.WindowsUpdate.Builder)` |   
  
### getWindowsUpdateOrBuilder()
    
    
    public WindowsUpdateOrBuilder getWindowsUpdateOrBuilder()

Required for Windows OS. Represents the metadata about the Windows update.

`.grafeas.v1.WindowsUpdate windows_update = 5;`

**Returns**  
---  
**Type** | **Description**  
`[WindowsUpdateOrBuilder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.WindowsUpdateOrBuilder)` |   
  
### hasDistribution()
    
    
    public boolean hasDistribution()

Metadata about the upgrade for available for the specific operating system for the resource_url. This allows efficient filtering, as well as making it easier to use the occurrence.

`.grafeas.v1.UpgradeDistribution distribution = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the distribution field is set.  
  
### hasParsedVersion()
    
    
    public boolean hasParsedVersion()

Required for non-Windows OS. The version of the package in a machine + human readable form.

`.grafeas.v1.Version parsed_version = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the parsedVersion field is set.  
  
### hasWindowsUpdate()
    
    
    public boolean hasWindowsUpdate()

Required for Windows OS. Represents the metadata about the Windows update.

`.grafeas.v1.WindowsUpdate windows_update = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the windowsUpdate field is set.  
  
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

### mergeDistribution(UpgradeDistribution value)
    
    
    public UpgradeOccurrence.Builder mergeDistribution(UpgradeDistribution value)

Metadata about the upgrade for available for the specific operating system for the resource_url. This allows efficient filtering, as well as making it easier to use the occurrence.

`.grafeas.v1.UpgradeDistribution distribution = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[UpgradeDistribution](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeDistribution)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UpgradeOccurrence.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public UpgradeOccurrence.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UpgradeOccurrence.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public UpgradeOccurrence.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UpgradeOccurrence.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeFrom(UpgradeOccurrence other)
    
    
    public UpgradeOccurrence.Builder mergeFrom(UpgradeOccurrence other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpgradeOccurrence](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UpgradeOccurrence.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence.Builder)` |   
  
### mergeParsedVersion(Version value)
    
    
    public UpgradeOccurrence.Builder mergeParsedVersion(Version value)

Required for non-Windows OS. The version of the package in a machine + human readable form.

`.grafeas.v1.Version parsed_version = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Version](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Version)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UpgradeOccurrence.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence.Builder)` |   
  
### mergeWindowsUpdate(WindowsUpdate value)
    
    
    public UpgradeOccurrence.Builder mergeWindowsUpdate(WindowsUpdate value)

Required for Windows OS. Represents the metadata about the Windows update.

`.grafeas.v1.WindowsUpdate windows_update = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WindowsUpdate](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.WindowsUpdate)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UpgradeOccurrence.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence.Builder)` |   
  
### setDistribution(UpgradeDistribution value)
    
    
    public UpgradeOccurrence.Builder setDistribution(UpgradeDistribution value)

Metadata about the upgrade for available for the specific operating system for the resource_url. This allows efficient filtering, as well as making it easier to use the occurrence.

`.grafeas.v1.UpgradeDistribution distribution = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[UpgradeDistribution](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeDistribution)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UpgradeOccurrence.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence.Builder)` |   
  
### setDistribution(UpgradeDistribution.Builder builderForValue)
    
    
    public UpgradeOccurrence.Builder setDistribution(UpgradeDistribution.Builder builderForValue)

Metadata about the upgrade for available for the specific operating system for the resource_url. This allows efficient filtering, as well as making it easier to use the occurrence.

`.grafeas.v1.UpgradeDistribution distribution = 4;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[UpgradeDistribution.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeDistribution.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UpgradeOccurrence.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence.Builder)` |   
  
### setPackage(String value)
    
    
    public UpgradeOccurrence.Builder setPackage(String value)

Required for non-Windows OS. The package this Upgrade is for.

`string package = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The package to set.  
**Returns**  
---  
**Type** | **Description**  
`[UpgradeOccurrence.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence.Builder)` | This builder for chaining.  
  
### setPackageBytes(ByteString value)
    
    
    public UpgradeOccurrence.Builder setPackageBytes(ByteString value)

Required for non-Windows OS. The package this Upgrade is for.

`string package = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for package to set.  
**Returns**  
---  
**Type** | **Description**  
`[UpgradeOccurrence.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence.Builder)` | This builder for chaining.  
  
### setParsedVersion(Version value)
    
    
    public UpgradeOccurrence.Builder setParsedVersion(Version value)

Required for non-Windows OS. The version of the package in a machine + human readable form.

`.grafeas.v1.Version parsed_version = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Version](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Version)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UpgradeOccurrence.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence.Builder)` |   
  
### setParsedVersion(Version.Builder builderForValue)
    
    
    public UpgradeOccurrence.Builder setParsedVersion(Version.Builder builderForValue)

Required for non-Windows OS. The version of the package in a machine + human readable form.

`.grafeas.v1.Version parsed_version = 3;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Version.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.Version.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UpgradeOccurrence.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence.Builder)` |   
  
### setWindowsUpdate(WindowsUpdate value)
    
    
    public UpgradeOccurrence.Builder setWindowsUpdate(WindowsUpdate value)

Required for Windows OS. Represents the metadata about the Windows update.

`.grafeas.v1.WindowsUpdate windows_update = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WindowsUpdate](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.WindowsUpdate)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UpgradeOccurrence.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence.Builder)` |   
  
### setWindowsUpdate(WindowsUpdate.Builder builderForValue)
    
    
    public UpgradeOccurrence.Builder setWindowsUpdate(WindowsUpdate.Builder builderForValue)

Required for Windows OS. Represents the metadata about the Windows update.

`.grafeas.v1.WindowsUpdate windows_update = 5;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[WindowsUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.WindowsUpdate.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UpgradeOccurrence.Builder](https://docs.cloud.google.com/java/docs/reference/grafeas/latest/io.grafeas.v1.UpgradeOccurrence.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
