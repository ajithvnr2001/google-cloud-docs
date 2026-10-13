---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder
title: Class Inventory.WindowsUpdatePackage.Builder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:17:21.670365+00:00
---

# Class Inventory.WindowsUpdatePackage.Builder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Inventory.WindowsUpdatePackage.Builder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.6  2.4.3  2.3.2 
    
    
    public static final class Inventory.WindowsUpdatePackage.Builder extends GeneratedMessage.Builder<Inventory.WindowsUpdatePackage.Builder> implements Inventory.WindowsUpdatePackageOrBuilder

Details related to a Windows Update package. Field data and names are taken from Windows Update API IUpdate Interface: <https://docs.microsoft.com/en-us/windows/win32/api/_wua/> Descriptive fields like title, and description are localized based on the locale of the VM being updated.

Protobuf type `google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > Inventory.WindowsUpdatePackage.Builder

## Implements

[Inventory.WindowsUpdatePackageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackageOrBuilder)

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

### addAllCategories(Iterable<? extends Inventory.WindowsUpdatePackage.WindowsUpdateCategory> values)
    
    
    public Inventory.WindowsUpdatePackage.Builder addAllCategories(Iterable<? extends Inventory.WindowsUpdatePackage.WindowsUpdateCategory> values)

The categories that are associated with this update package.

` repeated .google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory categories = 3; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` |   
  
### addAllKbArticleIds(Iterable<String> values)
    
    
    public Inventory.WindowsUpdatePackage.Builder addAllKbArticleIds(Iterable<String> values)

A collection of Microsoft Knowledge Base article IDs that are associated with the update package.

`repeated string kb_article_ids = 4;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The kbArticleIds to add.  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
### addAllMoreInfoUrls(Iterable<String> values)
    
    
    public Inventory.WindowsUpdatePackage.Builder addAllMoreInfoUrls(Iterable<String> values)

A collection of URLs that provide more information about the update package.

`repeated string more_info_urls = 5;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The moreInfoUrls to add.  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
### addCategories(Inventory.WindowsUpdatePackage.WindowsUpdateCategory value)
    
    
    public Inventory.WindowsUpdatePackage.Builder addCategories(Inventory.WindowsUpdatePackage.WindowsUpdateCategory value)

The categories that are associated with this update package.

` repeated .google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory categories = 3; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Inventory.WindowsUpdatePackage.WindowsUpdateCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` |   
  
### addCategories(Inventory.WindowsUpdatePackage.WindowsUpdateCategory.Builder builderForValue)
    
    
    public Inventory.WindowsUpdatePackage.Builder addCategories(Inventory.WindowsUpdatePackage.WindowsUpdateCategory.Builder builderForValue)

The categories that are associated with this update package.

` repeated .google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory categories = 3; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Inventory.WindowsUpdatePackage.WindowsUpdateCategory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` |   
  
### addCategories(int index, Inventory.WindowsUpdatePackage.WindowsUpdateCategory value)
    
    
    public Inventory.WindowsUpdatePackage.Builder addCategories(int index, Inventory.WindowsUpdatePackage.WindowsUpdateCategory value)

The categories that are associated with this update package.

` repeated .google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory categories = 3; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Inventory.WindowsUpdatePackage.WindowsUpdateCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` |   
  
### addCategories(int index, Inventory.WindowsUpdatePackage.WindowsUpdateCategory.Builder builderForValue)
    
    
    public Inventory.WindowsUpdatePackage.Builder addCategories(int index, Inventory.WindowsUpdatePackage.WindowsUpdateCategory.Builder builderForValue)

The categories that are associated with this update package.

` repeated .google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory categories = 3; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Inventory.WindowsUpdatePackage.WindowsUpdateCategory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` |   
  
### addCategoriesBuilder()
    
    
    public Inventory.WindowsUpdatePackage.WindowsUpdateCategory.Builder addCategoriesBuilder()

The categories that are associated with this update package.

` repeated .google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory categories = 3; `

**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.WindowsUpdateCategory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory.Builder)` |   
  
### addCategoriesBuilder(int index)
    
    
    public Inventory.WindowsUpdatePackage.WindowsUpdateCategory.Builder addCategoriesBuilder(int index)

The categories that are associated with this update package.

` repeated .google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory categories = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.WindowsUpdateCategory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory.Builder)` |   
  
### addKbArticleIds(String value)
    
    
    public Inventory.WindowsUpdatePackage.Builder addKbArticleIds(String value)

A collection of Microsoft Knowledge Base article IDs that are associated with the update package.

`repeated string kb_article_ids = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The kbArticleIds to add.  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
### addKbArticleIdsBytes(ByteString value)
    
    
    public Inventory.WindowsUpdatePackage.Builder addKbArticleIdsBytes(ByteString value)

A collection of Microsoft Knowledge Base article IDs that are associated with the update package.

`repeated string kb_article_ids = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes of the kbArticleIds to add.  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
### addMoreInfoUrls(String value)
    
    
    public Inventory.WindowsUpdatePackage.Builder addMoreInfoUrls(String value)

A collection of URLs that provide more information about the update package.

`repeated string more_info_urls = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The moreInfoUrls to add.  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
### addMoreInfoUrlsBytes(ByteString value)
    
    
    public Inventory.WindowsUpdatePackage.Builder addMoreInfoUrlsBytes(ByteString value)

A collection of URLs that provide more information about the update package.

`repeated string more_info_urls = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes of the moreInfoUrls to add.  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
### build()
    
    
    public Inventory.WindowsUpdatePackage build()

**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage)` |   
  
### buildPartial()
    
    
    public Inventory.WindowsUpdatePackage buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage)` |   
  
### clear()
    
    
    public Inventory.WindowsUpdatePackage.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearCategories()
    
    
    public Inventory.WindowsUpdatePackage.Builder clearCategories()

The categories that are associated with this update package.

` repeated .google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory categories = 3; `

**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` |   
  
### clearDescription()
    
    
    public Inventory.WindowsUpdatePackage.Builder clearDescription()

The localized description of the update package.

`string description = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
### clearKbArticleIds()
    
    
    public Inventory.WindowsUpdatePackage.Builder clearKbArticleIds()

A collection of Microsoft Knowledge Base article IDs that are associated with the update package.

`repeated string kb_article_ids = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
### clearLastDeploymentChangeTime()
    
    
    public Inventory.WindowsUpdatePackage.Builder clearLastDeploymentChangeTime()

The last published date of the update, in (UTC) date and time.

`.google.protobuf.Timestamp last_deployment_change_time = 10;`

**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` |   
  
### clearMoreInfoUrls()
    
    
    public Inventory.WindowsUpdatePackage.Builder clearMoreInfoUrls()

A collection of URLs that provide more information about the update package.

`repeated string more_info_urls = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
### clearRevisionNumber()
    
    
    public Inventory.WindowsUpdatePackage.Builder clearRevisionNumber()

The revision number of this update package.

`int32 revision_number = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
### clearSupportUrl()
    
    
    public Inventory.WindowsUpdatePackage.Builder clearSupportUrl()

A hyperlink to the language-specific support information for the update.

`string support_url = 11;`

**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
### clearTitle()
    
    
    public Inventory.WindowsUpdatePackage.Builder clearTitle()

The localized title of the update package.

`string title = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
### clearUpdateId()
    
    
    public Inventory.WindowsUpdatePackage.Builder clearUpdateId()

Gets the identifier of an update package. Stays the same across revisions.

`string update_id = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
### getCategories(int index)
    
    
    public Inventory.WindowsUpdatePackage.WindowsUpdateCategory getCategories(int index)

The categories that are associated with this update package.

` repeated .google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory categories = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.WindowsUpdateCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory)` |   
  
### getCategoriesBuilder(int index)
    
    
    public Inventory.WindowsUpdatePackage.WindowsUpdateCategory.Builder getCategoriesBuilder(int index)

The categories that are associated with this update package.

` repeated .google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory categories = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.WindowsUpdateCategory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory.Builder)` |   
  
### getCategoriesBuilderList()
    
    
    public List<Inventory.WindowsUpdatePackage.WindowsUpdateCategory.Builder> getCategoriesBuilderList()

The categories that are associated with this update package.

` repeated .google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory categories = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory.Builder)>` |   
  
### getCategoriesCount()
    
    
    public int getCategoriesCount()

The categories that are associated with this update package.

` repeated .google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory categories = 3; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCategoriesList()
    
    
    public List<Inventory.WindowsUpdatePackage.WindowsUpdateCategory> getCategoriesList()

The categories that are associated with this update package.

` repeated .google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory categories = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[WindowsUpdateCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory)>` |   
  
### getCategoriesOrBuilder(int index)
    
    
    public Inventory.WindowsUpdatePackage.WindowsUpdateCategoryOrBuilder getCategoriesOrBuilder(int index)

The categories that are associated with this update package.

` repeated .google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory categories = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.WindowsUpdateCategoryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategoryOrBuilder)` |   
  
### getCategoriesOrBuilderList()
    
    
    public List<? extends Inventory.WindowsUpdatePackage.WindowsUpdateCategoryOrBuilder> getCategoriesOrBuilderList()

The categories that are associated with this update package.

` repeated .google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory categories = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategoryOrBuilder>` |   
  
### getDefaultInstanceForType()
    
    
    public Inventory.WindowsUpdatePackage getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage)` |   
  
### getDescription()
    
    
    public String getDescription()

The localized description of the update package.

`string description = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public ByteString getDescriptionBytes()

The localized description of the update package.

`string description = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getKbArticleIds(int index)
    
    
    public String getKbArticleIds(int index)

A collection of Microsoft Knowledge Base article IDs that are associated with the update package.

`repeated string kb_article_ids = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kbArticleIds at the given index.  
  
### getKbArticleIdsBytes(int index)
    
    
    public ByteString getKbArticleIdsBytes(int index)

A collection of Microsoft Knowledge Base article IDs that are associated with the update package.

`repeated string kb_article_ids = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the kbArticleIds at the given index.  
  
### getKbArticleIdsCount()
    
    
    public int getKbArticleIdsCount()

A collection of Microsoft Knowledge Base article IDs that are associated with the update package.

`repeated string kb_article_ids = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of kbArticleIds.  
  
### getKbArticleIdsList()
    
    
    public ProtocolStringList getKbArticleIdsList()

A collection of Microsoft Knowledge Base article IDs that are associated with the update package.

`repeated string kb_article_ids = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ProtocolStringList](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolStringList.html)` | A list containing the kbArticleIds.  
  
### getLastDeploymentChangeTime()
    
    
    public Timestamp getLastDeploymentChangeTime()

The last published date of the update, in (UTC) date and time.

`.google.protobuf.Timestamp last_deployment_change_time = 10;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The lastDeploymentChangeTime.  
  
### getLastDeploymentChangeTimeBuilder()
    
    
    public Timestamp.Builder getLastDeploymentChangeTimeBuilder()

The last published date of the update, in (UTC) date and time.

`.google.protobuf.Timestamp last_deployment_change_time = 10;`

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getLastDeploymentChangeTimeOrBuilder()
    
    
    public TimestampOrBuilder getLastDeploymentChangeTimeOrBuilder()

The last published date of the update, in (UTC) date and time.

`.google.protobuf.Timestamp last_deployment_change_time = 10;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getMoreInfoUrls(int index)
    
    
    public String getMoreInfoUrls(int index)

A collection of URLs that provide more information about the update package.

`repeated string more_info_urls = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The moreInfoUrls at the given index.  
  
### getMoreInfoUrlsBytes(int index)
    
    
    public ByteString getMoreInfoUrlsBytes(int index)

A collection of URLs that provide more information about the update package.

`repeated string more_info_urls = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the moreInfoUrls at the given index.  
  
### getMoreInfoUrlsCount()
    
    
    public int getMoreInfoUrlsCount()

A collection of URLs that provide more information about the update package.

`repeated string more_info_urls = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of moreInfoUrls.  
  
### getMoreInfoUrlsList()
    
    
    public ProtocolStringList getMoreInfoUrlsList()

A collection of URLs that provide more information about the update package.

`repeated string more_info_urls = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ProtocolStringList](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolStringList.html)` | A list containing the moreInfoUrls.  
  
### getRevisionNumber()
    
    
    public int getRevisionNumber()

The revision number of this update package.

`int32 revision_number = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The revisionNumber.  
  
### getSupportUrl()
    
    
    public String getSupportUrl()

A hyperlink to the language-specific support information for the update.

`string support_url = 11;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The supportUrl.  
  
### getSupportUrlBytes()
    
    
    public ByteString getSupportUrlBytes()

A hyperlink to the language-specific support information for the update.

`string support_url = 11;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for supportUrl.  
  
### getTitle()
    
    
    public String getTitle()

The localized title of the update package.

`string title = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The title.  
  
### getTitleBytes()
    
    
    public ByteString getTitleBytes()

The localized title of the update package.

`string title = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for title.  
  
### getUpdateId()
    
    
    public String getUpdateId()

Gets the identifier of an update package. Stays the same across revisions.

`string update_id = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The updateId.  
  
### getUpdateIdBytes()
    
    
    public ByteString getUpdateIdBytes()

Gets the identifier of an update package. Stays the same across revisions.

`string update_id = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for updateId.  
  
### hasLastDeploymentChangeTime()
    
    
    public boolean hasLastDeploymentChangeTime()

The last published date of the update, in (UTC) date and time.

`.google.protobuf.Timestamp last_deployment_change_time = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the lastDeploymentChangeTime field is set.  
  
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

### mergeFrom(Inventory.WindowsUpdatePackage other)
    
    
    public Inventory.WindowsUpdatePackage.Builder mergeFrom(Inventory.WindowsUpdatePackage other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Inventory.WindowsUpdatePackage](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public Inventory.WindowsUpdatePackage.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public Inventory.WindowsUpdatePackage.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeLastDeploymentChangeTime(Timestamp value)
    
    
    public Inventory.WindowsUpdatePackage.Builder mergeLastDeploymentChangeTime(Timestamp value)

The last published date of the update, in (UTC) date and time.

`.google.protobuf.Timestamp last_deployment_change_time = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` |   
  
### removeCategories(int index)
    
    
    public Inventory.WindowsUpdatePackage.Builder removeCategories(int index)

The categories that are associated with this update package.

` repeated .google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory categories = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` |   
  
### setCategories(int index, Inventory.WindowsUpdatePackage.WindowsUpdateCategory value)
    
    
    public Inventory.WindowsUpdatePackage.Builder setCategories(int index, Inventory.WindowsUpdatePackage.WindowsUpdateCategory value)

The categories that are associated with this update package.

` repeated .google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory categories = 3; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Inventory.WindowsUpdatePackage.WindowsUpdateCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` |   
  
### setCategories(int index, Inventory.WindowsUpdatePackage.WindowsUpdateCategory.Builder builderForValue)
    
    
    public Inventory.WindowsUpdatePackage.Builder setCategories(int index, Inventory.WindowsUpdatePackage.WindowsUpdateCategory.Builder builderForValue)

The categories that are associated with this update package.

` repeated .google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory categories = 3; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Inventory.WindowsUpdatePackage.WindowsUpdateCategory.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.WindowsUpdateCategory.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` |   
  
### setDescription(String value)
    
    
    public Inventory.WindowsUpdatePackage.Builder setDescription(String value)

The localized description of the update package.

`string description = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The description to set.  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
### setDescriptionBytes(ByteString value)
    
    
    public Inventory.WindowsUpdatePackage.Builder setDescriptionBytes(ByteString value)

The localized description of the update package.

`string description = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for description to set.  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
### setKbArticleIds(int index, String value)
    
    
    public Inventory.WindowsUpdatePackage.Builder setKbArticleIds(int index, String value)

A collection of Microsoft Knowledge Base article IDs that are associated with the update package.

`repeated string kb_article_ids = 4;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The kbArticleIds to set.  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
### setLastDeploymentChangeTime(Timestamp value)
    
    
    public Inventory.WindowsUpdatePackage.Builder setLastDeploymentChangeTime(Timestamp value)

The last published date of the update, in (UTC) date and time.

`.google.protobuf.Timestamp last_deployment_change_time = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` |   
  
### setLastDeploymentChangeTime(Timestamp.Builder builderForValue)
    
    
    public Inventory.WindowsUpdatePackage.Builder setLastDeploymentChangeTime(Timestamp.Builder builderForValue)

The last published date of the update, in (UTC) date and time.

`.google.protobuf.Timestamp last_deployment_change_time = 10;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` |   
  
### setMoreInfoUrls(int index, String value)
    
    
    public Inventory.WindowsUpdatePackage.Builder setMoreInfoUrls(int index, String value)

A collection of URLs that provide more information about the update package.

`repeated string more_info_urls = 5;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The moreInfoUrls to set.  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
### setRevisionNumber(int value)
    
    
    public Inventory.WindowsUpdatePackage.Builder setRevisionNumber(int value)

The revision number of this update package.

`int32 revision_number = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The revisionNumber to set.  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
### setSupportUrl(String value)
    
    
    public Inventory.WindowsUpdatePackage.Builder setSupportUrl(String value)

A hyperlink to the language-specific support information for the update.

`string support_url = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The supportUrl to set.  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
### setSupportUrlBytes(ByteString value)
    
    
    public Inventory.WindowsUpdatePackage.Builder setSupportUrlBytes(ByteString value)

A hyperlink to the language-specific support information for the update.

`string support_url = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for supportUrl to set.  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
### setTitle(String value)
    
    
    public Inventory.WindowsUpdatePackage.Builder setTitle(String value)

The localized title of the update package.

`string title = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The title to set.  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
### setTitleBytes(ByteString value)
    
    
    public Inventory.WindowsUpdatePackage.Builder setTitleBytes(ByteString value)

The localized title of the update package.

`string title = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for title to set.  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
### setUpdateId(String value)
    
    
    public Inventory.WindowsUpdatePackage.Builder setUpdateId(String value)

Gets the identifier of an update package. Stays the same across revisions.

`string update_id = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The updateId to set.  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
### setUpdateIdBytes(ByteString value)
    
    
    public Inventory.WindowsUpdatePackage.Builder setUpdateIdBytes(ByteString value)

Gets the identifier of an update package. Stays the same across revisions.

`string update_id = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for updateId to set.  
**Returns**  
---  
**Type** | **Description**  
`[Inventory.WindowsUpdatePackage.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.Inventory.WindowsUpdatePackage.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
