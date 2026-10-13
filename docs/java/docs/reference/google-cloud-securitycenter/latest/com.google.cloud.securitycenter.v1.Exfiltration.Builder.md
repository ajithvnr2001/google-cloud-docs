---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder
title: Class Exfiltration.Builder (2.107.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:23.291830+00:00
---

# Class Exfiltration.Builder (2.107.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Exfiltration.Builder (2.107.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.107.0 (latest)  2.103.0  2.102.0  2.101.0  2.99.0  2.96.0  2.95.0  2.93.0  2.91.0  2.90.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.72.0  2.71.0  2.70.0  2.68.0  2.67.0  2.66.0  2.65.0  2.64.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.10.0  2.9.0  2.8.0  2.7.1  2.6.0  2.5.6  2.3.2 
    
    
    public static final class Exfiltration.Builder extends GeneratedMessage.Builder<Exfiltration.Builder> implements ExfiltrationOrBuilder

Exfiltration represents a data exfiltration attempt from one or more sources to one or more targets. The `sources` attribute lists the sources of the exfiltrated data. The `targets` attribute lists the destinations the data was copied to.

Protobuf type `google.cloud.securitycenter.v1.Exfiltration`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > Exfiltration.Builder

## Implements

[ExfiltrationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfiltrationOrBuilder)

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

### addAllSources(Iterable<? extends ExfilResource> values)
    
    
    public Exfiltration.Builder addAllSources(Iterable<? extends ExfilResource> values)

If there are multiple sources, then the data is considered "joined" between them. For instance, BigQuery can join multiple tables, and each table would be considered a source.

`repeated .google.cloud.securitycenter.v1.ExfilResource sources = 1;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.securitycenter.v1.ExfilResource>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` |   
  
### addAllTargets(Iterable<? extends ExfilResource> values)
    
    
    public Exfiltration.Builder addAllTargets(Iterable<? extends ExfilResource> values)

If there are multiple targets, each target would get a complete copy of the "joined" source data.

`repeated .google.cloud.securitycenter.v1.ExfilResource targets = 2;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.securitycenter.v1.ExfilResource>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` |   
  
### addSources(ExfilResource value)
    
    
    public Exfiltration.Builder addSources(ExfilResource value)

If there are multiple sources, then the data is considered "joined" between them. For instance, BigQuery can join multiple tables, and each table would be considered a source.

`repeated .google.cloud.securitycenter.v1.ExfilResource sources = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ExfilResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` |   
  
### addSources(ExfilResource.Builder builderForValue)
    
    
    public Exfiltration.Builder addSources(ExfilResource.Builder builderForValue)

If there are multiple sources, then the data is considered "joined" between them. For instance, BigQuery can join multiple tables, and each table would be considered a source.

`repeated .google.cloud.securitycenter.v1.ExfilResource sources = 1;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ExfilResource.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` |   
  
### addSources(int index, ExfilResource value)
    
    
    public Exfiltration.Builder addSources(int index, ExfilResource value)

If there are multiple sources, then the data is considered "joined" between them. For instance, BigQuery can join multiple tables, and each table would be considered a source.

`repeated .google.cloud.securitycenter.v1.ExfilResource sources = 1;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ExfilResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` |   
  
### addSources(int index, ExfilResource.Builder builderForValue)
    
    
    public Exfiltration.Builder addSources(int index, ExfilResource.Builder builderForValue)

If there are multiple sources, then the data is considered "joined" between them. For instance, BigQuery can join multiple tables, and each table would be considered a source.

`repeated .google.cloud.securitycenter.v1.ExfilResource sources = 1;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ExfilResource.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` |   
  
### addSourcesBuilder()
    
    
    public ExfilResource.Builder addSourcesBuilder()

If there are multiple sources, then the data is considered "joined" between them. For instance, BigQuery can join multiple tables, and each table would be considered a source.

`repeated .google.cloud.securitycenter.v1.ExfilResource sources = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ExfilResource.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource.Builder)` |   
  
### addSourcesBuilder(int index)
    
    
    public ExfilResource.Builder addSourcesBuilder(int index)

If there are multiple sources, then the data is considered "joined" between them. For instance, BigQuery can join multiple tables, and each table would be considered a source.

`repeated .google.cloud.securitycenter.v1.ExfilResource sources = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExfilResource.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource.Builder)` |   
  
### addTargets(ExfilResource value)
    
    
    public Exfiltration.Builder addTargets(ExfilResource value)

If there are multiple targets, each target would get a complete copy of the "joined" source data.

`repeated .google.cloud.securitycenter.v1.ExfilResource targets = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ExfilResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` |   
  
### addTargets(ExfilResource.Builder builderForValue)
    
    
    public Exfiltration.Builder addTargets(ExfilResource.Builder builderForValue)

If there are multiple targets, each target would get a complete copy of the "joined" source data.

`repeated .google.cloud.securitycenter.v1.ExfilResource targets = 2;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ExfilResource.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` |   
  
### addTargets(int index, ExfilResource value)
    
    
    public Exfiltration.Builder addTargets(int index, ExfilResource value)

If there are multiple targets, each target would get a complete copy of the "joined" source data.

`repeated .google.cloud.securitycenter.v1.ExfilResource targets = 2;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ExfilResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` |   
  
### addTargets(int index, ExfilResource.Builder builderForValue)
    
    
    public Exfiltration.Builder addTargets(int index, ExfilResource.Builder builderForValue)

If there are multiple targets, each target would get a complete copy of the "joined" source data.

`repeated .google.cloud.securitycenter.v1.ExfilResource targets = 2;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ExfilResource.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` |   
  
### addTargetsBuilder()
    
    
    public ExfilResource.Builder addTargetsBuilder()

If there are multiple targets, each target would get a complete copy of the "joined" source data.

`repeated .google.cloud.securitycenter.v1.ExfilResource targets = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ExfilResource.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource.Builder)` |   
  
### addTargetsBuilder(int index)
    
    
    public ExfilResource.Builder addTargetsBuilder(int index)

If there are multiple targets, each target would get a complete copy of the "joined" source data.

`repeated .google.cloud.securitycenter.v1.ExfilResource targets = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExfilResource.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource.Builder)` |   
  
### build()
    
    
    public Exfiltration build()

**Returns**  
---  
**Type** | **Description**  
`[Exfiltration](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration)` |   
  
### buildPartial()
    
    
    public Exfiltration buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[Exfiltration](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration)` |   
  
### clear()
    
    
    public Exfiltration.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearSources()
    
    
    public Exfiltration.Builder clearSources()

If there are multiple sources, then the data is considered "joined" between them. For instance, BigQuery can join multiple tables, and each table would be considered a source.

`repeated .google.cloud.securitycenter.v1.ExfilResource sources = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` |   
  
### clearTargets()
    
    
    public Exfiltration.Builder clearTargets()

If there are multiple targets, each target would get a complete copy of the "joined" source data.

`repeated .google.cloud.securitycenter.v1.ExfilResource targets = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` |   
  
### clearTotalExfiltratedBytes()
    
    
    public Exfiltration.Builder clearTotalExfiltratedBytes()

Total exfiltrated bytes processed for the entire job.

`int64 total_exfiltrated_bytes = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` | This builder for chaining.  
  
### getDefaultInstanceForType()
    
    
    public Exfiltration getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Exfiltration](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getSources(int index)
    
    
    public ExfilResource getSources(int index)

If there are multiple sources, then the data is considered "joined" between them. For instance, BigQuery can join multiple tables, and each table would be considered a source.

`repeated .google.cloud.securitycenter.v1.ExfilResource sources = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExfilResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource)` |   
  
### getSourcesBuilder(int index)
    
    
    public ExfilResource.Builder getSourcesBuilder(int index)

If there are multiple sources, then the data is considered "joined" between them. For instance, BigQuery can join multiple tables, and each table would be considered a source.

`repeated .google.cloud.securitycenter.v1.ExfilResource sources = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExfilResource.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource.Builder)` |   
  
### getSourcesBuilderList()
    
    
    public List<ExfilResource.Builder> getSourcesBuilderList()

If there are multiple sources, then the data is considered "joined" between them. For instance, BigQuery can join multiple tables, and each table would be considered a source.

`repeated .google.cloud.securitycenter.v1.ExfilResource sources = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource.Builder)>` |   
  
### getSourcesCount()
    
    
    public int getSourcesCount()

If there are multiple sources, then the data is considered "joined" between them. For instance, BigQuery can join multiple tables, and each table would be considered a source.

`repeated .google.cloud.securitycenter.v1.ExfilResource sources = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSourcesList()
    
    
    public List<ExfilResource> getSourcesList()

If there are multiple sources, then the data is considered "joined" between them. For instance, BigQuery can join multiple tables, and each table would be considered a source.

`repeated .google.cloud.securitycenter.v1.ExfilResource sources = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ExfilResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource)>` |   
  
### getSourcesOrBuilder(int index)
    
    
    public ExfilResourceOrBuilder getSourcesOrBuilder(int index)

If there are multiple sources, then the data is considered "joined" between them. For instance, BigQuery can join multiple tables, and each table would be considered a source.

`repeated .google.cloud.securitycenter.v1.ExfilResource sources = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExfilResourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResourceOrBuilder)` |   
  
### getSourcesOrBuilderList()
    
    
    public List<? extends ExfilResourceOrBuilder> getSourcesOrBuilderList()

If there are multiple sources, then the data is considered "joined" between them. For instance, BigQuery can join multiple tables, and each table would be considered a source.

`repeated .google.cloud.securitycenter.v1.ExfilResource sources = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.securitycenter.v1.ExfilResourceOrBuilder>` |   
  
### getTargets(int index)
    
    
    public ExfilResource getTargets(int index)

If there are multiple targets, each target would get a complete copy of the "joined" source data.

`repeated .google.cloud.securitycenter.v1.ExfilResource targets = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExfilResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource)` |   
  
### getTargetsBuilder(int index)
    
    
    public ExfilResource.Builder getTargetsBuilder(int index)

If there are multiple targets, each target would get a complete copy of the "joined" source data.

`repeated .google.cloud.securitycenter.v1.ExfilResource targets = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExfilResource.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource.Builder)` |   
  
### getTargetsBuilderList()
    
    
    public List<ExfilResource.Builder> getTargetsBuilderList()

If there are multiple targets, each target would get a complete copy of the "joined" source data.

`repeated .google.cloud.securitycenter.v1.ExfilResource targets = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource.Builder)>` |   
  
### getTargetsCount()
    
    
    public int getTargetsCount()

If there are multiple targets, each target would get a complete copy of the "joined" source data.

`repeated .google.cloud.securitycenter.v1.ExfilResource targets = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getTargetsList()
    
    
    public List<ExfilResource> getTargetsList()

If there are multiple targets, each target would get a complete copy of the "joined" source data.

`repeated .google.cloud.securitycenter.v1.ExfilResource targets = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ExfilResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource)>` |   
  
### getTargetsOrBuilder(int index)
    
    
    public ExfilResourceOrBuilder getTargetsOrBuilder(int index)

If there are multiple targets, each target would get a complete copy of the "joined" source data.

`repeated .google.cloud.securitycenter.v1.ExfilResource targets = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExfilResourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResourceOrBuilder)` |   
  
### getTargetsOrBuilderList()
    
    
    public List<? extends ExfilResourceOrBuilder> getTargetsOrBuilderList()

If there are multiple targets, each target would get a complete copy of the "joined" source data.

`repeated .google.cloud.securitycenter.v1.ExfilResource targets = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.securitycenter.v1.ExfilResourceOrBuilder>` |   
  
### getTotalExfiltratedBytes()
    
    
    public long getTotalExfiltratedBytes()

Total exfiltrated bytes processed for the entire job.

`int64 total_exfiltrated_bytes = 3;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The totalExfiltratedBytes.  
  
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

### mergeFrom(Exfiltration other)
    
    
    public Exfiltration.Builder mergeFrom(Exfiltration other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Exfiltration](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public Exfiltration.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public Exfiltration.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### removeSources(int index)
    
    
    public Exfiltration.Builder removeSources(int index)

If there are multiple sources, then the data is considered "joined" between them. For instance, BigQuery can join multiple tables, and each table would be considered a source.

`repeated .google.cloud.securitycenter.v1.ExfilResource sources = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` |   
  
### removeTargets(int index)
    
    
    public Exfiltration.Builder removeTargets(int index)

If there are multiple targets, each target would get a complete copy of the "joined" source data.

`repeated .google.cloud.securitycenter.v1.ExfilResource targets = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` |   
  
### setSources(int index, ExfilResource value)
    
    
    public Exfiltration.Builder setSources(int index, ExfilResource value)

If there are multiple sources, then the data is considered "joined" between them. For instance, BigQuery can join multiple tables, and each table would be considered a source.

`repeated .google.cloud.securitycenter.v1.ExfilResource sources = 1;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ExfilResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` |   
  
### setSources(int index, ExfilResource.Builder builderForValue)
    
    
    public Exfiltration.Builder setSources(int index, ExfilResource.Builder builderForValue)

If there are multiple sources, then the data is considered "joined" between them. For instance, BigQuery can join multiple tables, and each table would be considered a source.

`repeated .google.cloud.securitycenter.v1.ExfilResource sources = 1;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ExfilResource.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` |   
  
### setTargets(int index, ExfilResource value)
    
    
    public Exfiltration.Builder setTargets(int index, ExfilResource value)

If there are multiple targets, each target would get a complete copy of the "joined" source data.

`repeated .google.cloud.securitycenter.v1.ExfilResource targets = 2;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[ExfilResource](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` |   
  
### setTargets(int index, ExfilResource.Builder builderForValue)
    
    
    public Exfiltration.Builder setTargets(int index, ExfilResource.Builder builderForValue)

If there are multiple targets, each target would get a complete copy of the "joined" source data.

`repeated .google.cloud.securitycenter.v1.ExfilResource targets = 2;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[ExfilResource.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.ExfilResource.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` |   
  
### setTotalExfiltratedBytes(long value)
    
    
    public Exfiltration.Builder setTotalExfiltratedBytes(long value)

Total exfiltrated bytes processed for the entire job.

`int64 total_exfiltrated_bytes = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The totalExfiltratedBytes to set.  
**Returns**  
---  
**Type** | **Description**  
`[Exfiltration.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.Exfiltration.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
