---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter.Builder
title: Class TemplateParameter.Builder (4.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:29.018674+00:00
---

# Class TemplateParameter.Builder (4.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TemplateParameter.Builder (4.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.96.0 (latest)  4.92.0  4.91.1  4.90.0  4.88.0  4.85.0  4.84.0  4.82.0  4.80.0  4.79.0  4.78.0  4.77.0  4.75.0  4.73.0  4.72.0  4.71.0  4.70.0  4.69.0  4.67.0  4.65.0  4.64.0  4.61.0  4.60.0  4.59.0  4.57.0  4.56.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.46.0  4.45.0  4.44.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.34.0  4.33.0  4.32.0  4.31.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.16.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.8  3.1.2  3.0.3  2.3.1 
    
    
    public static final class TemplateParameter.Builder extends GeneratedMessage.Builder<TemplateParameter.Builder> implements TemplateParameterOrBuilder

A configurable parameter that replaces one or more fields in the template. Parameterizable fields:

  * Labels
  * File uris
  * Job properties
  * Job arguments
  * Script variables
  * Main class (in HadoopJob and SparkJob)
  * Zone (in ClusterSelector)



Protobuf type `google.cloud.dataproc.v1.TemplateParameter`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > TemplateParameter.Builder

## Implements

[TemplateParameterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameterOrBuilder)

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

### addAllFields(Iterable<String> values)
    
    
    public TemplateParameter.Builder addAllFields(Iterable<String> values)

Required. Paths to all fields that the parameter replaces. A field is allowed to appear in at most one parameter's list of field paths.

A field path is similar in syntax to a google.protobuf.FieldMask. For example, a field path that references the zone field of a workflow template's cluster selector would be specified as `placement.clusterSelector.zone`.

Also, field paths can reference fields using the following syntax:

  * Values in maps can be referenced by key:
  * labels['key']
  * placement.clusterSelector.clusterLabels['key']
  * placement.managedCluster.labels['key']
  * placement.clusterSelector.clusterLabels['key']
  * jobs['step-id'].labels['key']

  * Jobs in the jobs list can be referenced by step-id:

  * jobs['step-id'].hadoopJob.mainJarFileUri
  * jobs['step-id'].hiveJob.queryFileUri
  * jobs['step-id'].pySparkJob.mainPythonFileUri
  * jobs['step-id'].hadoopJob.jarFileUris[0]
  * jobs['step-id'].hadoopJob.archiveUris[0]
  * jobs['step-id'].hadoopJob.fileUris[0]
  * jobs['step-id'].pySparkJob.pythonFileUris[0]

  * Items in repeated fields can be referenced by a zero-based index:

  * jobs['step-id'].sparkJob.args[0]

  * Other examples:

  * jobs['step-id'].hadoopJob.properties['key']
  * jobs['step-id'].hadoopJob.args[0]
  * jobs['step-id'].hiveJob.scriptVariables['key']
  * jobs['step-id'].hadoopJob.mainJarFileUri
  * placement.clusterSelector.zone

It may not be possible to parameterize maps and repeated fields in their entirety since only individual map values and individual items in repeated fields can be referenced. For example, the following field paths are invalid:

  * placement.clusterSelector.clusterLabels

  * jobs['step-id'].sparkJob.args



`repeated string fields = 2 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The fields to add.  
**Returns**  
---  
**Type** | **Description**  
`[TemplateParameter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter.Builder)` | This builder for chaining.  
  
### addFields(String value)
    
    
    public TemplateParameter.Builder addFields(String value)

Required. Paths to all fields that the parameter replaces. A field is allowed to appear in at most one parameter's list of field paths.

A field path is similar in syntax to a google.protobuf.FieldMask. For example, a field path that references the zone field of a workflow template's cluster selector would be specified as `placement.clusterSelector.zone`.

Also, field paths can reference fields using the following syntax:

  * Values in maps can be referenced by key:
  * labels['key']
  * placement.clusterSelector.clusterLabels['key']
  * placement.managedCluster.labels['key']
  * placement.clusterSelector.clusterLabels['key']
  * jobs['step-id'].labels['key']

  * Jobs in the jobs list can be referenced by step-id:

  * jobs['step-id'].hadoopJob.mainJarFileUri
  * jobs['step-id'].hiveJob.queryFileUri
  * jobs['step-id'].pySparkJob.mainPythonFileUri
  * jobs['step-id'].hadoopJob.jarFileUris[0]
  * jobs['step-id'].hadoopJob.archiveUris[0]
  * jobs['step-id'].hadoopJob.fileUris[0]
  * jobs['step-id'].pySparkJob.pythonFileUris[0]

  * Items in repeated fields can be referenced by a zero-based index:

  * jobs['step-id'].sparkJob.args[0]

  * Other examples:

  * jobs['step-id'].hadoopJob.properties['key']
  * jobs['step-id'].hadoopJob.args[0]
  * jobs['step-id'].hiveJob.scriptVariables['key']
  * jobs['step-id'].hadoopJob.mainJarFileUri
  * placement.clusterSelector.zone

It may not be possible to parameterize maps and repeated fields in their entirety since only individual map values and individual items in repeated fields can be referenced. For example, the following field paths are invalid:

  * placement.clusterSelector.clusterLabels

  * jobs['step-id'].sparkJob.args



`repeated string fields = 2 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The fields to add.  
**Returns**  
---  
**Type** | **Description**  
`[TemplateParameter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter.Builder)` | This builder for chaining.  
  
### addFieldsBytes(ByteString value)
    
    
    public TemplateParameter.Builder addFieldsBytes(ByteString value)

Required. Paths to all fields that the parameter replaces. A field is allowed to appear in at most one parameter's list of field paths.

A field path is similar in syntax to a google.protobuf.FieldMask. For example, a field path that references the zone field of a workflow template's cluster selector would be specified as `placement.clusterSelector.zone`.

Also, field paths can reference fields using the following syntax:

  * Values in maps can be referenced by key:
  * labels['key']
  * placement.clusterSelector.clusterLabels['key']
  * placement.managedCluster.labels['key']
  * placement.clusterSelector.clusterLabels['key']
  * jobs['step-id'].labels['key']

  * Jobs in the jobs list can be referenced by step-id:

  * jobs['step-id'].hadoopJob.mainJarFileUri
  * jobs['step-id'].hiveJob.queryFileUri
  * jobs['step-id'].pySparkJob.mainPythonFileUri
  * jobs['step-id'].hadoopJob.jarFileUris[0]
  * jobs['step-id'].hadoopJob.archiveUris[0]
  * jobs['step-id'].hadoopJob.fileUris[0]
  * jobs['step-id'].pySparkJob.pythonFileUris[0]

  * Items in repeated fields can be referenced by a zero-based index:

  * jobs['step-id'].sparkJob.args[0]

  * Other examples:

  * jobs['step-id'].hadoopJob.properties['key']
  * jobs['step-id'].hadoopJob.args[0]
  * jobs['step-id'].hiveJob.scriptVariables['key']
  * jobs['step-id'].hadoopJob.mainJarFileUri
  * placement.clusterSelector.zone

It may not be possible to parameterize maps and repeated fields in their entirety since only individual map values and individual items in repeated fields can be referenced. For example, the following field paths are invalid:

  * placement.clusterSelector.clusterLabels

  * jobs['step-id'].sparkJob.args



`repeated string fields = 2 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes of the fields to add.  
**Returns**  
---  
**Type** | **Description**  
`[TemplateParameter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter.Builder)` | This builder for chaining.  
  
### build()
    
    
    public TemplateParameter build()

**Returns**  
---  
**Type** | **Description**  
`[TemplateParameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter)` |   
  
### buildPartial()
    
    
    public TemplateParameter buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[TemplateParameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter)` |   
  
### clear()
    
    
    public TemplateParameter.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[TemplateParameter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearDescription()
    
    
    public TemplateParameter.Builder clearDescription()

Optional. Brief description of the parameter. Must not exceed 1024 characters.

`string description = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[TemplateParameter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter.Builder)` | This builder for chaining.  
  
### clearFields()
    
    
    public TemplateParameter.Builder clearFields()

Required. Paths to all fields that the parameter replaces. A field is allowed to appear in at most one parameter's list of field paths.

A field path is similar in syntax to a google.protobuf.FieldMask. For example, a field path that references the zone field of a workflow template's cluster selector would be specified as `placement.clusterSelector.zone`.

Also, field paths can reference fields using the following syntax:

  * Values in maps can be referenced by key:
  * labels['key']
  * placement.clusterSelector.clusterLabels['key']
  * placement.managedCluster.labels['key']
  * placement.clusterSelector.clusterLabels['key']
  * jobs['step-id'].labels['key']

  * Jobs in the jobs list can be referenced by step-id:

  * jobs['step-id'].hadoopJob.mainJarFileUri
  * jobs['step-id'].hiveJob.queryFileUri
  * jobs['step-id'].pySparkJob.mainPythonFileUri
  * jobs['step-id'].hadoopJob.jarFileUris[0]
  * jobs['step-id'].hadoopJob.archiveUris[0]
  * jobs['step-id'].hadoopJob.fileUris[0]
  * jobs['step-id'].pySparkJob.pythonFileUris[0]

  * Items in repeated fields can be referenced by a zero-based index:

  * jobs['step-id'].sparkJob.args[0]

  * Other examples:

  * jobs['step-id'].hadoopJob.properties['key']
  * jobs['step-id'].hadoopJob.args[0]
  * jobs['step-id'].hiveJob.scriptVariables['key']
  * jobs['step-id'].hadoopJob.mainJarFileUri
  * placement.clusterSelector.zone

It may not be possible to parameterize maps and repeated fields in their entirety since only individual map values and individual items in repeated fields can be referenced. For example, the following field paths are invalid:

  * placement.clusterSelector.clusterLabels

  * jobs['step-id'].sparkJob.args



`repeated string fields = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[TemplateParameter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter.Builder)` | This builder for chaining.  
  
### clearName()
    
    
    public TemplateParameter.Builder clearName()

Required. Parameter name. The parameter name is used as the key, and paired with the parameter value, which are passed to the template when the template is instantiated. The name must contain only capital letters (A-Z), numbers (0-9), and underscores (_), and must not start with a number. The maximum length is 40 characters.

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[TemplateParameter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter.Builder)` | This builder for chaining.  
  
### clearValidation()
    
    
    public TemplateParameter.Builder clearValidation()

Optional. Validation rules to be applied to this parameter's value.

` .google.cloud.dataproc.v1.ParameterValidation validation = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[TemplateParameter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter.Builder)` |   
  
### getDefaultInstanceForType()
    
    
    public TemplateParameter getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[TemplateParameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter)` |   
  
### getDescription()
    
    
    public String getDescription()

Optional. Brief description of the parameter. Must not exceed 1024 characters.

`string description = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public ByteString getDescriptionBytes()

Optional. Brief description of the parameter. Must not exceed 1024 characters.

`string description = 3 [(.google.api.field_behavior) = OPTIONAL];`

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

### getFields(int index)
    
    
    public String getFields(int index)

Required. Paths to all fields that the parameter replaces. A field is allowed to appear in at most one parameter's list of field paths.

A field path is similar in syntax to a google.protobuf.FieldMask. For example, a field path that references the zone field of a workflow template's cluster selector would be specified as `placement.clusterSelector.zone`.

Also, field paths can reference fields using the following syntax:

  * Values in maps can be referenced by key:
  * labels['key']
  * placement.clusterSelector.clusterLabels['key']
  * placement.managedCluster.labels['key']
  * placement.clusterSelector.clusterLabels['key']
  * jobs['step-id'].labels['key']

  * Jobs in the jobs list can be referenced by step-id:

  * jobs['step-id'].hadoopJob.mainJarFileUri
  * jobs['step-id'].hiveJob.queryFileUri
  * jobs['step-id'].pySparkJob.mainPythonFileUri
  * jobs['step-id'].hadoopJob.jarFileUris[0]
  * jobs['step-id'].hadoopJob.archiveUris[0]
  * jobs['step-id'].hadoopJob.fileUris[0]
  * jobs['step-id'].pySparkJob.pythonFileUris[0]

  * Items in repeated fields can be referenced by a zero-based index:

  * jobs['step-id'].sparkJob.args[0]

  * Other examples:

  * jobs['step-id'].hadoopJob.properties['key']
  * jobs['step-id'].hadoopJob.args[0]
  * jobs['step-id'].hiveJob.scriptVariables['key']
  * jobs['step-id'].hadoopJob.mainJarFileUri
  * placement.clusterSelector.zone

It may not be possible to parameterize maps and repeated fields in their entirety since only individual map values and individual items in repeated fields can be referenced. For example, the following field paths are invalid:

  * placement.clusterSelector.clusterLabels

  * jobs['step-id'].sparkJob.args



`repeated string fields = 2 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The fields at the given index.  
  
### getFieldsBytes(int index)
    
    
    public ByteString getFieldsBytes(int index)

Required. Paths to all fields that the parameter replaces. A field is allowed to appear in at most one parameter's list of field paths.

A field path is similar in syntax to a google.protobuf.FieldMask. For example, a field path that references the zone field of a workflow template's cluster selector would be specified as `placement.clusterSelector.zone`.

Also, field paths can reference fields using the following syntax:

  * Values in maps can be referenced by key:
  * labels['key']
  * placement.clusterSelector.clusterLabels['key']
  * placement.managedCluster.labels['key']
  * placement.clusterSelector.clusterLabels['key']
  * jobs['step-id'].labels['key']

  * Jobs in the jobs list can be referenced by step-id:

  * jobs['step-id'].hadoopJob.mainJarFileUri
  * jobs['step-id'].hiveJob.queryFileUri
  * jobs['step-id'].pySparkJob.mainPythonFileUri
  * jobs['step-id'].hadoopJob.jarFileUris[0]
  * jobs['step-id'].hadoopJob.archiveUris[0]
  * jobs['step-id'].hadoopJob.fileUris[0]
  * jobs['step-id'].pySparkJob.pythonFileUris[0]

  * Items in repeated fields can be referenced by a zero-based index:

  * jobs['step-id'].sparkJob.args[0]

  * Other examples:

  * jobs['step-id'].hadoopJob.properties['key']
  * jobs['step-id'].hadoopJob.args[0]
  * jobs['step-id'].hiveJob.scriptVariables['key']
  * jobs['step-id'].hadoopJob.mainJarFileUri
  * placement.clusterSelector.zone

It may not be possible to parameterize maps and repeated fields in their entirety since only individual map values and individual items in repeated fields can be referenced. For example, the following field paths are invalid:

  * placement.clusterSelector.clusterLabels

  * jobs['step-id'].sparkJob.args



`repeated string fields = 2 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the fields at the given index.  
  
### getFieldsCount()
    
    
    public int getFieldsCount()

Required. Paths to all fields that the parameter replaces. A field is allowed to appear in at most one parameter's list of field paths.

A field path is similar in syntax to a google.protobuf.FieldMask. For example, a field path that references the zone field of a workflow template's cluster selector would be specified as `placement.clusterSelector.zone`.

Also, field paths can reference fields using the following syntax:

  * Values in maps can be referenced by key:
  * labels['key']
  * placement.clusterSelector.clusterLabels['key']
  * placement.managedCluster.labels['key']
  * placement.clusterSelector.clusterLabels['key']
  * jobs['step-id'].labels['key']

  * Jobs in the jobs list can be referenced by step-id:

  * jobs['step-id'].hadoopJob.mainJarFileUri
  * jobs['step-id'].hiveJob.queryFileUri
  * jobs['step-id'].pySparkJob.mainPythonFileUri
  * jobs['step-id'].hadoopJob.jarFileUris[0]
  * jobs['step-id'].hadoopJob.archiveUris[0]
  * jobs['step-id'].hadoopJob.fileUris[0]
  * jobs['step-id'].pySparkJob.pythonFileUris[0]

  * Items in repeated fields can be referenced by a zero-based index:

  * jobs['step-id'].sparkJob.args[0]

  * Other examples:

  * jobs['step-id'].hadoopJob.properties['key']
  * jobs['step-id'].hadoopJob.args[0]
  * jobs['step-id'].hiveJob.scriptVariables['key']
  * jobs['step-id'].hadoopJob.mainJarFileUri
  * placement.clusterSelector.zone

It may not be possible to parameterize maps and repeated fields in their entirety since only individual map values and individual items in repeated fields can be referenced. For example, the following field paths are invalid:

  * placement.clusterSelector.clusterLabels

  * jobs['step-id'].sparkJob.args



`repeated string fields = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of fields.  
  
### getFieldsList()
    
    
    public ProtocolStringList getFieldsList()

Required. Paths to all fields that the parameter replaces. A field is allowed to appear in at most one parameter's list of field paths.

A field path is similar in syntax to a google.protobuf.FieldMask. For example, a field path that references the zone field of a workflow template's cluster selector would be specified as `placement.clusterSelector.zone`.

Also, field paths can reference fields using the following syntax:

  * Values in maps can be referenced by key:
  * labels['key']
  * placement.clusterSelector.clusterLabels['key']
  * placement.managedCluster.labels['key']
  * placement.clusterSelector.clusterLabels['key']
  * jobs['step-id'].labels['key']

  * Jobs in the jobs list can be referenced by step-id:

  * jobs['step-id'].hadoopJob.mainJarFileUri
  * jobs['step-id'].hiveJob.queryFileUri
  * jobs['step-id'].pySparkJob.mainPythonFileUri
  * jobs['step-id'].hadoopJob.jarFileUris[0]
  * jobs['step-id'].hadoopJob.archiveUris[0]
  * jobs['step-id'].hadoopJob.fileUris[0]
  * jobs['step-id'].pySparkJob.pythonFileUris[0]

  * Items in repeated fields can be referenced by a zero-based index:

  * jobs['step-id'].sparkJob.args[0]

  * Other examples:

  * jobs['step-id'].hadoopJob.properties['key']
  * jobs['step-id'].hadoopJob.args[0]
  * jobs['step-id'].hiveJob.scriptVariables['key']
  * jobs['step-id'].hadoopJob.mainJarFileUri
  * placement.clusterSelector.zone

It may not be possible to parameterize maps and repeated fields in their entirety since only individual map values and individual items in repeated fields can be referenced. For example, the following field paths are invalid:

  * placement.clusterSelector.clusterLabels

  * jobs['step-id'].sparkJob.args



`repeated string fields = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ProtocolStringList](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolStringList.html)` | A list containing the fields.  
  
### getName()
    
    
    public String getName()

Required. Parameter name. The parameter name is used as the key, and paired with the parameter value, which are passed to the template when the template is instantiated. The name must contain only capital letters (A-Z), numbers (0-9), and underscores (_), and must not start with a number. The maximum length is 40 characters.

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

Required. Parameter name. The parameter name is used as the key, and paired with the parameter value, which are passed to the template when the template is instantiated. The name must contain only capital letters (A-Z), numbers (0-9), and underscores (_), and must not start with a number. The maximum length is 40 characters.

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getValidation()
    
    
    public ParameterValidation getValidation()

Optional. Validation rules to be applied to this parameter's value.

` .google.cloud.dataproc.v1.ParameterValidation validation = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ParameterValidation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ParameterValidation)` | The validation.  
  
### getValidationBuilder()
    
    
    public ParameterValidation.Builder getValidationBuilder()

Optional. Validation rules to be applied to this parameter's value.

` .google.cloud.dataproc.v1.ParameterValidation validation = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ParameterValidation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ParameterValidation.Builder)` |   
  
### getValidationOrBuilder()
    
    
    public ParameterValidationOrBuilder getValidationOrBuilder()

Optional. Validation rules to be applied to this parameter's value.

` .google.cloud.dataproc.v1.ParameterValidation validation = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ParameterValidationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ParameterValidationOrBuilder)` |   
  
### hasValidation()
    
    
    public boolean hasValidation()

Optional. Validation rules to be applied to this parameter's value.

` .google.cloud.dataproc.v1.ParameterValidation validation = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the validation field is set.  
  
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

### mergeFrom(TemplateParameter other)
    
    
    public TemplateParameter.Builder mergeFrom(TemplateParameter other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[TemplateParameter](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TemplateParameter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public TemplateParameter.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TemplateParameter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public TemplateParameter.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TemplateParameter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeValidation(ParameterValidation value)
    
    
    public TemplateParameter.Builder mergeValidation(ParameterValidation value)

Optional. Validation rules to be applied to this parameter's value.

` .google.cloud.dataproc.v1.ParameterValidation validation = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ParameterValidation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ParameterValidation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TemplateParameter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter.Builder)` |   
  
### setDescription(String value)
    
    
    public TemplateParameter.Builder setDescription(String value)

Optional. Brief description of the parameter. Must not exceed 1024 characters.

`string description = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The description to set.  
**Returns**  
---  
**Type** | **Description**  
`[TemplateParameter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter.Builder)` | This builder for chaining.  
  
### setDescriptionBytes(ByteString value)
    
    
    public TemplateParameter.Builder setDescriptionBytes(ByteString value)

Optional. Brief description of the parameter. Must not exceed 1024 characters.

`string description = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for description to set.  
**Returns**  
---  
**Type** | **Description**  
`[TemplateParameter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter.Builder)` | This builder for chaining.  
  
### setFields(int index, String value)
    
    
    public TemplateParameter.Builder setFields(int index, String value)

Required. Paths to all fields that the parameter replaces. A field is allowed to appear in at most one parameter's list of field paths.

A field path is similar in syntax to a google.protobuf.FieldMask. For example, a field path that references the zone field of a workflow template's cluster selector would be specified as `placement.clusterSelector.zone`.

Also, field paths can reference fields using the following syntax:

  * Values in maps can be referenced by key:
  * labels['key']
  * placement.clusterSelector.clusterLabels['key']
  * placement.managedCluster.labels['key']
  * placement.clusterSelector.clusterLabels['key']
  * jobs['step-id'].labels['key']

  * Jobs in the jobs list can be referenced by step-id:

  * jobs['step-id'].hadoopJob.mainJarFileUri
  * jobs['step-id'].hiveJob.queryFileUri
  * jobs['step-id'].pySparkJob.mainPythonFileUri
  * jobs['step-id'].hadoopJob.jarFileUris[0]
  * jobs['step-id'].hadoopJob.archiveUris[0]
  * jobs['step-id'].hadoopJob.fileUris[0]
  * jobs['step-id'].pySparkJob.pythonFileUris[0]

  * Items in repeated fields can be referenced by a zero-based index:

  * jobs['step-id'].sparkJob.args[0]

  * Other examples:

  * jobs['step-id'].hadoopJob.properties['key']
  * jobs['step-id'].hadoopJob.args[0]
  * jobs['step-id'].hiveJob.scriptVariables['key']
  * jobs['step-id'].hadoopJob.mainJarFileUri
  * placement.clusterSelector.zone

It may not be possible to parameterize maps and repeated fields in their entirety since only individual map values and individual items in repeated fields can be referenced. For example, the following field paths are invalid:

  * placement.clusterSelector.clusterLabels

  * jobs['step-id'].sparkJob.args



`repeated string fields = 2 [(.google.api.field_behavior) = REQUIRED];`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The fields to set.  
**Returns**  
---  
**Type** | **Description**  
`[TemplateParameter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter.Builder)` | This builder for chaining.  
  
### setName(String value)
    
    
    public TemplateParameter.Builder setName(String value)

Required. Parameter name. The parameter name is used as the key, and paired with the parameter value, which are passed to the template when the template is instantiated. The name must contain only capital letters (A-Z), numbers (0-9), and underscores (_), and must not start with a number. The maximum length is 40 characters.

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[TemplateParameter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public TemplateParameter.Builder setNameBytes(ByteString value)

Required. Parameter name. The parameter name is used as the key, and paired with the parameter value, which are passed to the template when the template is instantiated. The name must contain only capital letters (A-Z), numbers (0-9), and underscores (_), and must not start with a number. The maximum length is 40 characters.

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[TemplateParameter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter.Builder)` | This builder for chaining.  
  
### setValidation(ParameterValidation value)
    
    
    public TemplateParameter.Builder setValidation(ParameterValidation value)

Optional. Validation rules to be applied to this parameter's value.

` .google.cloud.dataproc.v1.ParameterValidation validation = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ParameterValidation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ParameterValidation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TemplateParameter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter.Builder)` |   
  
### setValidation(ParameterValidation.Builder builderForValue)
    
    
    public TemplateParameter.Builder setValidation(ParameterValidation.Builder builderForValue)

Optional. Validation rules to be applied to this parameter's value.

` .google.cloud.dataproc.v1.ParameterValidation validation = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ParameterValidation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.ParameterValidation.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TemplateParameter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc/latest/com.google.cloud.dataproc.v1.TemplateParameter.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
