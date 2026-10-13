---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Builder
title: Class SynonymSet.Builder (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:03:25.889571+00:00
---

# Class SynonymSet.Builder (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SynonymSet.Builder (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class SynonymSet.Builder extends GeneratedMessage.Builder<SynonymSet.Builder> implements SynonymSetOrBuilder

Represents a list of synonyms for a given context. For example a context "sales" could contain: Synonym 1: sale, invoice, bill, order Synonym 2: money, credit, finance, payment Synonym 3: shipping, freight, transport Each SynonymSets should be disjoint

Protobuf type `google.cloud.contentwarehouse.v1.SynonymSet`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > SynonymSet.Builder

## Implements

[SynonymSetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSetOrBuilder)

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

### addAllSynonyms(Iterable<? extends SynonymSet.Synonym> values)
    
    
    public SynonymSet.Builder addAllSynonyms(Iterable<? extends SynonymSet.Synonym> values)

List of Synonyms for the context.

`repeated .google.cloud.contentwarehouse.v1.SynonymSet.Synonym synonyms = 3;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.contentwarehouse.v1.SynonymSet.Synonym>`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Builder)` |   
  
### addSynonyms(SynonymSet.Synonym value)
    
    
    public SynonymSet.Builder addSynonyms(SynonymSet.Synonym value)

List of Synonyms for the context.

`repeated .google.cloud.contentwarehouse.v1.SynonymSet.Synonym synonyms = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SynonymSet.Synonym](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Synonym)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Builder)` |   
  
### addSynonyms(SynonymSet.Synonym.Builder builderForValue)
    
    
    public SynonymSet.Builder addSynonyms(SynonymSet.Synonym.Builder builderForValue)

List of Synonyms for the context.

`repeated .google.cloud.contentwarehouse.v1.SynonymSet.Synonym synonyms = 3;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SynonymSet.Synonym.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Synonym.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Builder)` |   
  
### addSynonyms(int index, SynonymSet.Synonym value)
    
    
    public SynonymSet.Builder addSynonyms(int index, SynonymSet.Synonym value)

List of Synonyms for the context.

`repeated .google.cloud.contentwarehouse.v1.SynonymSet.Synonym synonyms = 3;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[SynonymSet.Synonym](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Synonym)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Builder)` |   
  
### addSynonyms(int index, SynonymSet.Synonym.Builder builderForValue)
    
    
    public SynonymSet.Builder addSynonyms(int index, SynonymSet.Synonym.Builder builderForValue)

List of Synonyms for the context.

`repeated .google.cloud.contentwarehouse.v1.SynonymSet.Synonym synonyms = 3;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[SynonymSet.Synonym.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Synonym.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Builder)` |   
  
### addSynonymsBuilder()
    
    
    public SynonymSet.Synonym.Builder addSynonymsBuilder()

List of Synonyms for the context.

`repeated .google.cloud.contentwarehouse.v1.SynonymSet.Synonym synonyms = 3;`

**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.Synonym.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Synonym.Builder)` |   
  
### addSynonymsBuilder(int index)
    
    
    public SynonymSet.Synonym.Builder addSynonymsBuilder(int index)

List of Synonyms for the context.

`repeated .google.cloud.contentwarehouse.v1.SynonymSet.Synonym synonyms = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.Synonym.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Synonym.Builder)` |   
  
### build()
    
    
    public SynonymSet build()

**Returns**  
---  
**Type** | **Description**  
`[SynonymSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet)` |   
  
### buildPartial()
    
    
    public SynonymSet buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[SynonymSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet)` |   
  
### clear()
    
    
    public SynonymSet.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearContext()
    
    
    public SynonymSet.Builder clearContext()

This is a freeform field. Example contexts can be "sales," "engineering," "real estate," "accounting," etc. The context can be supplied during search requests.

`string context = 2;`

**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Builder)` | This builder for chaining.  
  
### clearName()
    
    
    public SynonymSet.Builder clearName()

The resource name of the SynonymSet This is mandatory for google.api.resource. Format: projects/{project_number}/locations/{location}/synonymSets/{context}.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Builder)` | This builder for chaining.  
  
### clearSynonyms()
    
    
    public SynonymSet.Builder clearSynonyms()

List of Synonyms for the context.

`repeated .google.cloud.contentwarehouse.v1.SynonymSet.Synonym synonyms = 3;`

**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Builder)` |   
  
### getContext()
    
    
    public String getContext()

This is a freeform field. Example contexts can be "sales," "engineering," "real estate," "accounting," etc. The context can be supplied during search requests.

`string context = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The context.  
  
### getContextBytes()
    
    
    public ByteString getContextBytes()

This is a freeform field. Example contexts can be "sales," "engineering," "real estate," "accounting," etc. The context can be supplied during search requests.

`string context = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for context.  
  
### getDefaultInstanceForType()
    
    
    public SynonymSet getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[SynonymSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getName()
    
    
    public String getName()

The resource name of the SynonymSet This is mandatory for google.api.resource. Format: projects/{project_number}/locations/{location}/synonymSets/{context}.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

The resource name of the SynonymSet This is mandatory for google.api.resource. Format: projects/{project_number}/locations/{location}/synonymSets/{context}.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getSynonyms(int index)
    
    
    public SynonymSet.Synonym getSynonyms(int index)

List of Synonyms for the context.

`repeated .google.cloud.contentwarehouse.v1.SynonymSet.Synonym synonyms = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.Synonym](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Synonym)` |   
  
### getSynonymsBuilder(int index)
    
    
    public SynonymSet.Synonym.Builder getSynonymsBuilder(int index)

List of Synonyms for the context.

`repeated .google.cloud.contentwarehouse.v1.SynonymSet.Synonym synonyms = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.Synonym.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Synonym.Builder)` |   
  
### getSynonymsBuilderList()
    
    
    public List<SynonymSet.Synonym.Builder> getSynonymsBuilderList()

List of Synonyms for the context.

`repeated .google.cloud.contentwarehouse.v1.SynonymSet.Synonym synonyms = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Synonym.Builder)>` |   
  
### getSynonymsCount()
    
    
    public int getSynonymsCount()

List of Synonyms for the context.

`repeated .google.cloud.contentwarehouse.v1.SynonymSet.Synonym synonyms = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSynonymsList()
    
    
    public List<SynonymSet.Synonym> getSynonymsList()

List of Synonyms for the context.

`repeated .google.cloud.contentwarehouse.v1.SynonymSet.Synonym synonyms = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Synonym](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Synonym)>` |   
  
### getSynonymsOrBuilder(int index)
    
    
    public SynonymSet.SynonymOrBuilder getSynonymsOrBuilder(int index)

List of Synonyms for the context.

`repeated .google.cloud.contentwarehouse.v1.SynonymSet.Synonym synonyms = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.SynonymOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.SynonymOrBuilder)` |   
  
### getSynonymsOrBuilderList()
    
    
    public List<? extends SynonymSet.SynonymOrBuilder> getSynonymsOrBuilderList()

List of Synonyms for the context.

`repeated .google.cloud.contentwarehouse.v1.SynonymSet.Synonym synonyms = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.contentwarehouse.v1.SynonymSet.SynonymOrBuilder>` |   
  
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

### mergeFrom(SynonymSet other)
    
    
    public SynonymSet.Builder mergeFrom(SynonymSet other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SynonymSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public SynonymSet.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public SynonymSet.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### removeSynonyms(int index)
    
    
    public SynonymSet.Builder removeSynonyms(int index)

List of Synonyms for the context.

`repeated .google.cloud.contentwarehouse.v1.SynonymSet.Synonym synonyms = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Builder)` |   
  
### setContext(String value)
    
    
    public SynonymSet.Builder setContext(String value)

This is a freeform field. Example contexts can be "sales," "engineering," "real estate," "accounting," etc. The context can be supplied during search requests.

`string context = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The context to set.  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Builder)` | This builder for chaining.  
  
### setContextBytes(ByteString value)
    
    
    public SynonymSet.Builder setContextBytes(ByteString value)

This is a freeform field. Example contexts can be "sales," "engineering," "real estate," "accounting," etc. The context can be supplied during search requests.

`string context = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for context to set.  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Builder)` | This builder for chaining.  
  
### setName(String value)
    
    
    public SynonymSet.Builder setName(String value)

The resource name of the SynonymSet This is mandatory for google.api.resource. Format: projects/{project_number}/locations/{location}/synonymSets/{context}.

`string name = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public SynonymSet.Builder setNameBytes(ByteString value)

The resource name of the SynonymSet This is mandatory for google.api.resource. Format: projects/{project_number}/locations/{location}/synonymSets/{context}.

`string name = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Builder)` | This builder for chaining.  
  
### setSynonyms(int index, SynonymSet.Synonym value)
    
    
    public SynonymSet.Builder setSynonyms(int index, SynonymSet.Synonym value)

List of Synonyms for the context.

`repeated .google.cloud.contentwarehouse.v1.SynonymSet.Synonym synonyms = 3;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[SynonymSet.Synonym](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Synonym)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Builder)` |   
  
### setSynonyms(int index, SynonymSet.Synonym.Builder builderForValue)
    
    
    public SynonymSet.Builder setSynonyms(int index, SynonymSet.Synonym.Builder builderForValue)

List of Synonyms for the context.

`repeated .google.cloud.contentwarehouse.v1.SynonymSet.Synonym synonyms = 3;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[SynonymSet.Synonym.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Synonym.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SynonymSet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SynonymSet.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
