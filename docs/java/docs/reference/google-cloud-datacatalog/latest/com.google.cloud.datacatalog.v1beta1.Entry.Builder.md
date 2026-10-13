---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder
title: Class Entry.Builder (1.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:16:46.929279+00:00
---

# Class Entry.Builder (1.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Entry.Builder (1.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.101.0 (latest)  1.100.0  1.99.0  1.97.0  1.94.0  1.93.0  1.91.0  1.89.0  1.88.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.70.0  1.69.0  1.68.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.5  1.8.4  1.7.2  1.6.2  1.5.4 
    
    
    public static final class Entry.Builder extends GeneratedMessage.Builder<Entry.Builder> implements EntryOrBuilder

Entry Metadata. A Data Catalog Entry resource represents another resource in Google Cloud Platform (such as a BigQuery dataset or a Pub/Sub topic), or outside of Google Cloud Platform. Clients can use the `linked_resource` field in the Entry resource to refer to the original resource ID of the source system.

An Entry resource contains resource details, such as its schema. An Entry can also be used to attach flexible metadata, such as a Tag.

Protobuf type `google.cloud.datacatalog.v1beta1.Entry`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > Entry.Builder

## Implements

[EntryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.EntryOrBuilder)

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
    
    
    public Entry build()

**Returns**  
---  
**Type** | **Description**  
`[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry)` |   
  
### buildPartial()
    
    
    public Entry buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry)` |   
  
### clear()
    
    
    public Entry.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearBigqueryDateShardedSpec()
    
    
    public Entry.Builder clearBigqueryDateShardedSpec()

Specification for a group of BigQuery tables with name pattern `[prefix]YYYYMMDD`. Context: <https://cloud.google.com/bigquery/docs/partitioned-tables#partitioning_versus_sharding>.

` .google.cloud.datacatalog.v1beta1.BigQueryDateShardedSpec bigquery_date_sharded_spec = 15; `

**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### clearBigqueryTableSpec()
    
    
    public Entry.Builder clearBigqueryTableSpec()

Specification that applies to a BigQuery table. This is only valid on entries of type `TABLE`.

`.google.cloud.datacatalog.v1beta1.BigQueryTableSpec bigquery_table_spec = 12;`

**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### clearDescription()
    
    
    public Entry.Builder clearDescription()

Entry description, which can consist of several sentences or paragraphs that describe entry contents. Default value is an empty string.

`string description = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
### clearDisplayName()
    
    
    public Entry.Builder clearDisplayName()

Display information such as title and description. A short name to identify the entry, for example, "Analytics Data - Jan 2011". Default value is an empty string.

`string display_name = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
### clearEntryType()
    
    
    public Entry.Builder clearEntryType()

**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### clearGcsFilesetSpec()
    
    
    public Entry.Builder clearGcsFilesetSpec()

Specification that applies to a Cloud Storage fileset. This is only valid on entries of type FILESET.

`.google.cloud.datacatalog.v1beta1.GcsFilesetSpec gcs_fileset_spec = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### clearIntegratedSystem()
    
    
    public Entry.Builder clearIntegratedSystem()

Output only. This field indicates the entry's source system that Data Catalog integrates with, such as BigQuery or Pub/Sub.

` .google.cloud.datacatalog.v1beta1.IntegratedSystem integrated_system = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
### clearLinkedResource()
    
    
    public Entry.Builder clearLinkedResource()

The resource this metadata entry refers to.

For Google Cloud Platform resources, `linked_resource` is the [full name of the resource](https://cloud.google.com/apis/design/resource_names#full_resource_name). For example, the `linked_resource` for a table resource from BigQuery is:

  * //bigquery.googleapis.com/projects/projectId/datasets/datasetId/tables/tableId

Output only when Entry is of type in the EntryType enum. For entries with user_specified_type, this field is optional and defaults to an empty string.




`string linked_resource = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
### clearName()
    
    
    public Entry.Builder clearName()

Output only. Identifier. The Data Catalog resource name of the entry in URL format. Example:

  * projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}

Note that this Entry and its child resources may not actually be stored in the location in this name.




` string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IDENTIFIER, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
### clearSchema()
    
    
    public Entry.Builder clearSchema()

Schema of the entry. An entry might not have any schema attached to it.

`.google.cloud.datacatalog.v1beta1.Schema schema = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### clearSourceSystemTimestamps()
    
    
    public Entry.Builder clearSourceSystemTimestamps()

Output only. Timestamps about the underlying resource, not about this Data Catalog entry. Output only when Entry is of type in the EntryType enum. For entries with user_specified_type, this field is optional and defaults to an empty timestamp.

` .google.cloud.datacatalog.v1beta1.SystemTimestamps source_system_timestamps = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### clearSystem()
    
    
    public Entry.Builder clearSystem()

**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### clearType()
    
    
    public Entry.Builder clearType()

The type of the entry. Only used for Entries with types in the EntryType enum.

`.google.cloud.datacatalog.v1beta1.EntryType type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
### clearTypeSpec()
    
    
    public Entry.Builder clearTypeSpec()

**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### clearUsageSignal()
    
    
    public Entry.Builder clearUsageSignal()

Output only. Statistics on the usage level of the resource.

` .google.cloud.datacatalog.v1beta1.UsageSignal usage_signal = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### clearUserSpecifiedSystem()
    
    
    public Entry.Builder clearUserSpecifiedSystem()

This field indicates the entry's source system that Data Catalog does not integrate with. `user_specified_system` strings must begin with a letter or underscore and can only contain letters, numbers, and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.

`string user_specified_system = 18;`

**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
### clearUserSpecifiedType()
    
    
    public Entry.Builder clearUserSpecifiedType()

Entry type if it does not fit any of the input-allowed values listed in `EntryType` enum above. When creating an entry, users should check the enum values first, if nothing matches the entry to be created, then provide a custom value, for example "my_special_type". `user_specified_type` strings must begin with a letter or underscore and can only contain letters, numbers, and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.

Currently, only FILESET enum value is allowed. All other entries created through Data Catalog must use `user_specified_type`.

`string user_specified_type = 16;`

**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
### getBigqueryDateShardedSpec()
    
    
    public BigQueryDateShardedSpec getBigqueryDateShardedSpec()

Specification for a group of BigQuery tables with name pattern `[prefix]YYYYMMDD`. Context: <https://cloud.google.com/bigquery/docs/partitioned-tables#partitioning_versus_sharding>.

` .google.cloud.datacatalog.v1beta1.BigQueryDateShardedSpec bigquery_date_sharded_spec = 15; `

**Returns**  
---  
**Type** | **Description**  
`[BigQueryDateShardedSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.BigQueryDateShardedSpec)` | The bigqueryDateShardedSpec.  
  
### getBigqueryDateShardedSpecBuilder()
    
    
    public BigQueryDateShardedSpec.Builder getBigqueryDateShardedSpecBuilder()

Specification for a group of BigQuery tables with name pattern `[prefix]YYYYMMDD`. Context: <https://cloud.google.com/bigquery/docs/partitioned-tables#partitioning_versus_sharding>.

` .google.cloud.datacatalog.v1beta1.BigQueryDateShardedSpec bigquery_date_sharded_spec = 15; `

**Returns**  
---  
**Type** | **Description**  
`[BigQueryDateShardedSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.BigQueryDateShardedSpec.Builder)` |   
  
### getBigqueryDateShardedSpecOrBuilder()
    
    
    public BigQueryDateShardedSpecOrBuilder getBigqueryDateShardedSpecOrBuilder()

Specification for a group of BigQuery tables with name pattern `[prefix]YYYYMMDD`. Context: <https://cloud.google.com/bigquery/docs/partitioned-tables#partitioning_versus_sharding>.

` .google.cloud.datacatalog.v1beta1.BigQueryDateShardedSpec bigquery_date_sharded_spec = 15; `

**Returns**  
---  
**Type** | **Description**  
`[BigQueryDateShardedSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.BigQueryDateShardedSpecOrBuilder)` |   
  
### getBigqueryTableSpec()
    
    
    public BigQueryTableSpec getBigqueryTableSpec()

Specification that applies to a BigQuery table. This is only valid on entries of type `TABLE`.

`.google.cloud.datacatalog.v1beta1.BigQueryTableSpec bigquery_table_spec = 12;`

**Returns**  
---  
**Type** | **Description**  
`[BigQueryTableSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.BigQueryTableSpec)` | The bigqueryTableSpec.  
  
### getBigqueryTableSpecBuilder()
    
    
    public BigQueryTableSpec.Builder getBigqueryTableSpecBuilder()

Specification that applies to a BigQuery table. This is only valid on entries of type `TABLE`.

`.google.cloud.datacatalog.v1beta1.BigQueryTableSpec bigquery_table_spec = 12;`

**Returns**  
---  
**Type** | **Description**  
`[BigQueryTableSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.BigQueryTableSpec.Builder)` |   
  
### getBigqueryTableSpecOrBuilder()
    
    
    public BigQueryTableSpecOrBuilder getBigqueryTableSpecOrBuilder()

Specification that applies to a BigQuery table. This is only valid on entries of type `TABLE`.

`.google.cloud.datacatalog.v1beta1.BigQueryTableSpec bigquery_table_spec = 12;`

**Returns**  
---  
**Type** | **Description**  
`[BigQueryTableSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.BigQueryTableSpecOrBuilder)` |   
  
### getDefaultInstanceForType()
    
    
    public Entry getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry)` |   
  
### getDescription()
    
    
    public String getDescription()

Entry description, which can consist of several sentences or paragraphs that describe entry contents. Default value is an empty string.

`string description = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public ByteString getDescriptionBytes()

Entry description, which can consist of several sentences or paragraphs that describe entry contents. Default value is an empty string.

`string description = 4;`

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

### getDisplayName()
    
    
    public String getDisplayName()

Display information such as title and description. A short name to identify the entry, for example, "Analytics Data - Jan 2011". Default value is an empty string.

`string display_name = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public ByteString getDisplayNameBytes()

Display information such as title and description. A short name to identify the entry, for example, "Analytics Data - Jan 2011". Default value is an empty string.

`string display_name = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getEntryTypeCase()
    
    
    public Entry.EntryTypeCase getEntryTypeCase()

**Returns**  
---  
**Type** | **Description**  
`[Entry.EntryTypeCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.EntryTypeCase)` |   
  
### getGcsFilesetSpec()
    
    
    public GcsFilesetSpec getGcsFilesetSpec()

Specification that applies to a Cloud Storage fileset. This is only valid on entries of type FILESET.

`.google.cloud.datacatalog.v1beta1.GcsFilesetSpec gcs_fileset_spec = 6;`

**Returns**  
---  
**Type** | **Description**  
`[GcsFilesetSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.GcsFilesetSpec)` | The gcsFilesetSpec.  
  
### getGcsFilesetSpecBuilder()
    
    
    public GcsFilesetSpec.Builder getGcsFilesetSpecBuilder()

Specification that applies to a Cloud Storage fileset. This is only valid on entries of type FILESET.

`.google.cloud.datacatalog.v1beta1.GcsFilesetSpec gcs_fileset_spec = 6;`

**Returns**  
---  
**Type** | **Description**  
`[GcsFilesetSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.GcsFilesetSpec.Builder)` |   
  
### getGcsFilesetSpecOrBuilder()
    
    
    public GcsFilesetSpecOrBuilder getGcsFilesetSpecOrBuilder()

Specification that applies to a Cloud Storage fileset. This is only valid on entries of type FILESET.

`.google.cloud.datacatalog.v1beta1.GcsFilesetSpec gcs_fileset_spec = 6;`

**Returns**  
---  
**Type** | **Description**  
`[GcsFilesetSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.GcsFilesetSpecOrBuilder)` |   
  
### getIntegratedSystem()
    
    
    public IntegratedSystem getIntegratedSystem()

Output only. This field indicates the entry's source system that Data Catalog integrates with, such as BigQuery or Pub/Sub.

` .google.cloud.datacatalog.v1beta1.IntegratedSystem integrated_system = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[IntegratedSystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.IntegratedSystem)` | The integratedSystem.  
  
### getIntegratedSystemValue()
    
    
    public int getIntegratedSystemValue()

Output only. This field indicates the entry's source system that Data Catalog integrates with, such as BigQuery or Pub/Sub.

` .google.cloud.datacatalog.v1beta1.IntegratedSystem integrated_system = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for integratedSystem.  
  
### getLinkedResource()
    
    
    public String getLinkedResource()

The resource this metadata entry refers to.

For Google Cloud Platform resources, `linked_resource` is the [full name of the resource](https://cloud.google.com/apis/design/resource_names#full_resource_name). For example, the `linked_resource` for a table resource from BigQuery is:

  * //bigquery.googleapis.com/projects/projectId/datasets/datasetId/tables/tableId

Output only when Entry is of type in the EntryType enum. For entries with user_specified_type, this field is optional and defaults to an empty string.




`string linked_resource = 9;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The linkedResource.  
  
### getLinkedResourceBytes()
    
    
    public ByteString getLinkedResourceBytes()

The resource this metadata entry refers to.

For Google Cloud Platform resources, `linked_resource` is the [full name of the resource](https://cloud.google.com/apis/design/resource_names#full_resource_name). For example, the `linked_resource` for a table resource from BigQuery is:

  * //bigquery.googleapis.com/projects/projectId/datasets/datasetId/tables/tableId

Output only when Entry is of type in the EntryType enum. For entries with user_specified_type, this field is optional and defaults to an empty string.




`string linked_resource = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for linkedResource.  
  
### getName()
    
    
    public String getName()

Output only. Identifier. The Data Catalog resource name of the entry in URL format. Example:

  * projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}

Note that this Entry and its child resources may not actually be stored in the location in this name.




` string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IDENTIFIER, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

Output only. Identifier. The Data Catalog resource name of the entry in URL format. Example:

  * projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}

Note that this Entry and its child resources may not actually be stored in the location in this name.




` string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IDENTIFIER, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getSchema()
    
    
    public Schema getSchema()

Schema of the entry. An entry might not have any schema attached to it.

`.google.cloud.datacatalog.v1beta1.Schema schema = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Schema)` | The schema.  
  
### getSchemaBuilder()
    
    
    public Schema.Builder getSchemaBuilder()

Schema of the entry. An entry might not have any schema attached to it.

`.google.cloud.datacatalog.v1beta1.Schema schema = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Schema.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Schema.Builder)` |   
  
### getSchemaOrBuilder()
    
    
    public SchemaOrBuilder getSchemaOrBuilder()

Schema of the entry. An entry might not have any schema attached to it.

`.google.cloud.datacatalog.v1beta1.Schema schema = 5;`

**Returns**  
---  
**Type** | **Description**  
`[SchemaOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.SchemaOrBuilder)` |   
  
### getSourceSystemTimestamps()
    
    
    public SystemTimestamps getSourceSystemTimestamps()

Output only. Timestamps about the underlying resource, not about this Data Catalog entry. Output only when Entry is of type in the EntryType enum. For entries with user_specified_type, this field is optional and defaults to an empty timestamp.

` .google.cloud.datacatalog.v1beta1.SystemTimestamps source_system_timestamps = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SystemTimestamps](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.SystemTimestamps)` | The sourceSystemTimestamps.  
  
### getSourceSystemTimestampsBuilder()
    
    
    public SystemTimestamps.Builder getSourceSystemTimestampsBuilder()

Output only. Timestamps about the underlying resource, not about this Data Catalog entry. Output only when Entry is of type in the EntryType enum. For entries with user_specified_type, this field is optional and defaults to an empty timestamp.

` .google.cloud.datacatalog.v1beta1.SystemTimestamps source_system_timestamps = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SystemTimestamps.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.SystemTimestamps.Builder)` |   
  
### getSourceSystemTimestampsOrBuilder()
    
    
    public SystemTimestampsOrBuilder getSourceSystemTimestampsOrBuilder()

Output only. Timestamps about the underlying resource, not about this Data Catalog entry. Output only when Entry is of type in the EntryType enum. For entries with user_specified_type, this field is optional and defaults to an empty timestamp.

` .google.cloud.datacatalog.v1beta1.SystemTimestamps source_system_timestamps = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SystemTimestampsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.SystemTimestampsOrBuilder)` |   
  
### getSystemCase()
    
    
    public Entry.SystemCase getSystemCase()

**Returns**  
---  
**Type** | **Description**  
`[Entry.SystemCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.SystemCase)` |   
  
### getType()
    
    
    public EntryType getType()

The type of the entry. Only used for Entries with types in the EntryType enum.

`.google.cloud.datacatalog.v1beta1.EntryType type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.EntryType)` | The type.  
  
### getTypeSpecCase()
    
    
    public Entry.TypeSpecCase getTypeSpecCase()

**Returns**  
---  
**Type** | **Description**  
`[Entry.TypeSpecCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.TypeSpecCase)` |   
  
### getTypeValue()
    
    
    public int getTypeValue()

The type of the entry. Only used for Entries with types in the EntryType enum.

`.google.cloud.datacatalog.v1beta1.EntryType type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for type.  
  
### getUsageSignal()
    
    
    public UsageSignal getUsageSignal()

Output only. Statistics on the usage level of the resource.

` .google.cloud.datacatalog.v1beta1.UsageSignal usage_signal = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[UsageSignal](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.UsageSignal)` | The usageSignal.  
  
### getUsageSignalBuilder()
    
    
    public UsageSignal.Builder getUsageSignalBuilder()

Output only. Statistics on the usage level of the resource.

` .google.cloud.datacatalog.v1beta1.UsageSignal usage_signal = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[UsageSignal.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.UsageSignal.Builder)` |   
  
### getUsageSignalOrBuilder()
    
    
    public UsageSignalOrBuilder getUsageSignalOrBuilder()

Output only. Statistics on the usage level of the resource.

` .google.cloud.datacatalog.v1beta1.UsageSignal usage_signal = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[UsageSignalOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.UsageSignalOrBuilder)` |   
  
### getUserSpecifiedSystem()
    
    
    public String getUserSpecifiedSystem()

This field indicates the entry's source system that Data Catalog does not integrate with. `user_specified_system` strings must begin with a letter or underscore and can only contain letters, numbers, and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.

`string user_specified_system = 18;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The userSpecifiedSystem.  
  
### getUserSpecifiedSystemBytes()
    
    
    public ByteString getUserSpecifiedSystemBytes()

This field indicates the entry's source system that Data Catalog does not integrate with. `user_specified_system` strings must begin with a letter or underscore and can only contain letters, numbers, and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.

`string user_specified_system = 18;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for userSpecifiedSystem.  
  
### getUserSpecifiedType()
    
    
    public String getUserSpecifiedType()

Entry type if it does not fit any of the input-allowed values listed in `EntryType` enum above. When creating an entry, users should check the enum values first, if nothing matches the entry to be created, then provide a custom value, for example "my_special_type". `user_specified_type` strings must begin with a letter or underscore and can only contain letters, numbers, and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.

Currently, only FILESET enum value is allowed. All other entries created through Data Catalog must use `user_specified_type`.

`string user_specified_type = 16;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The userSpecifiedType.  
  
### getUserSpecifiedTypeBytes()
    
    
    public ByteString getUserSpecifiedTypeBytes()

Entry type if it does not fit any of the input-allowed values listed in `EntryType` enum above. When creating an entry, users should check the enum values first, if nothing matches the entry to be created, then provide a custom value, for example "my_special_type". `user_specified_type` strings must begin with a letter or underscore and can only contain letters, numbers, and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.

Currently, only FILESET enum value is allowed. All other entries created through Data Catalog must use `user_specified_type`.

`string user_specified_type = 16;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for userSpecifiedType.  
  
### hasBigqueryDateShardedSpec()
    
    
    public boolean hasBigqueryDateShardedSpec()

Specification for a group of BigQuery tables with name pattern `[prefix]YYYYMMDD`. Context: <https://cloud.google.com/bigquery/docs/partitioned-tables#partitioning_versus_sharding>.

` .google.cloud.datacatalog.v1beta1.BigQueryDateShardedSpec bigquery_date_sharded_spec = 15; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bigqueryDateShardedSpec field is set.  
  
### hasBigqueryTableSpec()
    
    
    public boolean hasBigqueryTableSpec()

Specification that applies to a BigQuery table. This is only valid on entries of type `TABLE`.

`.google.cloud.datacatalog.v1beta1.BigQueryTableSpec bigquery_table_spec = 12;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the bigqueryTableSpec field is set.  
  
### hasGcsFilesetSpec()
    
    
    public boolean hasGcsFilesetSpec()

Specification that applies to a Cloud Storage fileset. This is only valid on entries of type FILESET.

`.google.cloud.datacatalog.v1beta1.GcsFilesetSpec gcs_fileset_spec = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gcsFilesetSpec field is set.  
  
### hasIntegratedSystem()
    
    
    public boolean hasIntegratedSystem()

Output only. This field indicates the entry's source system that Data Catalog integrates with, such as BigQuery or Pub/Sub.

` .google.cloud.datacatalog.v1beta1.IntegratedSystem integrated_system = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the integratedSystem field is set.  
  
### hasSchema()
    
    
    public boolean hasSchema()

Schema of the entry. An entry might not have any schema attached to it.

`.google.cloud.datacatalog.v1beta1.Schema schema = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the schema field is set.  
  
### hasSourceSystemTimestamps()
    
    
    public boolean hasSourceSystemTimestamps()

Output only. Timestamps about the underlying resource, not about this Data Catalog entry. Output only when Entry is of type in the EntryType enum. For entries with user_specified_type, this field is optional and defaults to an empty timestamp.

` .google.cloud.datacatalog.v1beta1.SystemTimestamps source_system_timestamps = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sourceSystemTimestamps field is set.  
  
### hasType()
    
    
    public boolean hasType()

The type of the entry. Only used for Entries with types in the EntryType enum.

`.google.cloud.datacatalog.v1beta1.EntryType type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the type field is set.  
  
### hasUsageSignal()
    
    
    public boolean hasUsageSignal()

Output only. Statistics on the usage level of the resource.

` .google.cloud.datacatalog.v1beta1.UsageSignal usage_signal = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the usageSignal field is set.  
  
### hasUserSpecifiedSystem()
    
    
    public boolean hasUserSpecifiedSystem()

This field indicates the entry's source system that Data Catalog does not integrate with. `user_specified_system` strings must begin with a letter or underscore and can only contain letters, numbers, and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.

`string user_specified_system = 18;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the userSpecifiedSystem field is set.  
  
### hasUserSpecifiedType()
    
    
    public boolean hasUserSpecifiedType()

Entry type if it does not fit any of the input-allowed values listed in `EntryType` enum above. When creating an entry, users should check the enum values first, if nothing matches the entry to be created, then provide a custom value, for example "my_special_type". `user_specified_type` strings must begin with a letter or underscore and can only contain letters, numbers, and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.

Currently, only FILESET enum value is allowed. All other entries created through Data Catalog must use `user_specified_type`.

`string user_specified_type = 16;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the userSpecifiedType field is set.  
  
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

### mergeBigqueryDateShardedSpec(BigQueryDateShardedSpec value)
    
    
    public Entry.Builder mergeBigqueryDateShardedSpec(BigQueryDateShardedSpec value)

Specification for a group of BigQuery tables with name pattern `[prefix]YYYYMMDD`. Context: <https://cloud.google.com/bigquery/docs/partitioned-tables#partitioning_versus_sharding>.

` .google.cloud.datacatalog.v1beta1.BigQueryDateShardedSpec bigquery_date_sharded_spec = 15; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BigQueryDateShardedSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.BigQueryDateShardedSpec)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### mergeBigqueryTableSpec(BigQueryTableSpec value)
    
    
    public Entry.Builder mergeBigqueryTableSpec(BigQueryTableSpec value)

Specification that applies to a BigQuery table. This is only valid on entries of type `TABLE`.

`.google.cloud.datacatalog.v1beta1.BigQueryTableSpec bigquery_table_spec = 12;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BigQueryTableSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.BigQueryTableSpec)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### mergeFrom(Entry other)
    
    
    public Entry.Builder mergeFrom(Entry other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Entry](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public Entry.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public Entry.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeGcsFilesetSpec(GcsFilesetSpec value)
    
    
    public Entry.Builder mergeGcsFilesetSpec(GcsFilesetSpec value)

Specification that applies to a Cloud Storage fileset. This is only valid on entries of type FILESET.

`.google.cloud.datacatalog.v1beta1.GcsFilesetSpec gcs_fileset_spec = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[GcsFilesetSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.GcsFilesetSpec)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### mergeSchema(Schema value)
    
    
    public Entry.Builder mergeSchema(Schema value)

Schema of the entry. An entry might not have any schema attached to it.

`.google.cloud.datacatalog.v1beta1.Schema schema = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Schema)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### mergeSourceSystemTimestamps(SystemTimestamps value)
    
    
    public Entry.Builder mergeSourceSystemTimestamps(SystemTimestamps value)

Output only. Timestamps about the underlying resource, not about this Data Catalog entry. Output only when Entry is of type in the EntryType enum. For entries with user_specified_type, this field is optional and defaults to an empty timestamp.

` .google.cloud.datacatalog.v1beta1.SystemTimestamps source_system_timestamps = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SystemTimestamps](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.SystemTimestamps)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### mergeUsageSignal(UsageSignal value)
    
    
    public Entry.Builder mergeUsageSignal(UsageSignal value)

Output only. Statistics on the usage level of the resource.

` .google.cloud.datacatalog.v1beta1.UsageSignal usage_signal = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[UsageSignal](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.UsageSignal)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### setBigqueryDateShardedSpec(BigQueryDateShardedSpec value)
    
    
    public Entry.Builder setBigqueryDateShardedSpec(BigQueryDateShardedSpec value)

Specification for a group of BigQuery tables with name pattern `[prefix]YYYYMMDD`. Context: <https://cloud.google.com/bigquery/docs/partitioned-tables#partitioning_versus_sharding>.

` .google.cloud.datacatalog.v1beta1.BigQueryDateShardedSpec bigquery_date_sharded_spec = 15; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BigQueryDateShardedSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.BigQueryDateShardedSpec)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### setBigqueryDateShardedSpec(BigQueryDateShardedSpec.Builder builderForValue)
    
    
    public Entry.Builder setBigqueryDateShardedSpec(BigQueryDateShardedSpec.Builder builderForValue)

Specification for a group of BigQuery tables with name pattern `[prefix]YYYYMMDD`. Context: <https://cloud.google.com/bigquery/docs/partitioned-tables#partitioning_versus_sharding>.

` .google.cloud.datacatalog.v1beta1.BigQueryDateShardedSpec bigquery_date_sharded_spec = 15; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[BigQueryDateShardedSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.BigQueryDateShardedSpec.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### setBigqueryTableSpec(BigQueryTableSpec value)
    
    
    public Entry.Builder setBigqueryTableSpec(BigQueryTableSpec value)

Specification that applies to a BigQuery table. This is only valid on entries of type `TABLE`.

`.google.cloud.datacatalog.v1beta1.BigQueryTableSpec bigquery_table_spec = 12;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BigQueryTableSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.BigQueryTableSpec)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### setBigqueryTableSpec(BigQueryTableSpec.Builder builderForValue)
    
    
    public Entry.Builder setBigqueryTableSpec(BigQueryTableSpec.Builder builderForValue)

Specification that applies to a BigQuery table. This is only valid on entries of type `TABLE`.

`.google.cloud.datacatalog.v1beta1.BigQueryTableSpec bigquery_table_spec = 12;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[BigQueryTableSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.BigQueryTableSpec.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### setDescription(String value)
    
    
    public Entry.Builder setDescription(String value)

Entry description, which can consist of several sentences or paragraphs that describe entry contents. Default value is an empty string.

`string description = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The description to set.  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
### setDescriptionBytes(ByteString value)
    
    
    public Entry.Builder setDescriptionBytes(ByteString value)

Entry description, which can consist of several sentences or paragraphs that describe entry contents. Default value is an empty string.

`string description = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for description to set.  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
### setDisplayName(String value)
    
    
    public Entry.Builder setDisplayName(String value)

Display information such as title and description. A short name to identify the entry, for example, "Analytics Data - Jan 2011". Default value is an empty string.

`string display_name = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
### setDisplayNameBytes(ByteString value)
    
    
    public Entry.Builder setDisplayNameBytes(ByteString value)

Display information such as title and description. A short name to identify the entry, for example, "Analytics Data - Jan 2011". Default value is an empty string.

`string display_name = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
### setGcsFilesetSpec(GcsFilesetSpec value)
    
    
    public Entry.Builder setGcsFilesetSpec(GcsFilesetSpec value)

Specification that applies to a Cloud Storage fileset. This is only valid on entries of type FILESET.

`.google.cloud.datacatalog.v1beta1.GcsFilesetSpec gcs_fileset_spec = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[GcsFilesetSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.GcsFilesetSpec)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### setGcsFilesetSpec(GcsFilesetSpec.Builder builderForValue)
    
    
    public Entry.Builder setGcsFilesetSpec(GcsFilesetSpec.Builder builderForValue)

Specification that applies to a Cloud Storage fileset. This is only valid on entries of type FILESET.

`.google.cloud.datacatalog.v1beta1.GcsFilesetSpec gcs_fileset_spec = 6;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[GcsFilesetSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.GcsFilesetSpec.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### setIntegratedSystem(IntegratedSystem value)
    
    
    public Entry.Builder setIntegratedSystem(IntegratedSystem value)

Output only. This field indicates the entry's source system that Data Catalog integrates with, such as BigQuery or Pub/Sub.

` .google.cloud.datacatalog.v1beta1.IntegratedSystem integrated_system = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[IntegratedSystem](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.IntegratedSystem)`  
The integratedSystem to set.  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
### setIntegratedSystemValue(int value)
    
    
    public Entry.Builder setIntegratedSystemValue(int value)

Output only. This field indicates the entry's source system that Data Catalog integrates with, such as BigQuery or Pub/Sub.

` .google.cloud.datacatalog.v1beta1.IntegratedSystem integrated_system = 17 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for integratedSystem to set.  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
### setLinkedResource(String value)
    
    
    public Entry.Builder setLinkedResource(String value)

The resource this metadata entry refers to.

For Google Cloud Platform resources, `linked_resource` is the [full name of the resource](https://cloud.google.com/apis/design/resource_names#full_resource_name). For example, the `linked_resource` for a table resource from BigQuery is:

  * //bigquery.googleapis.com/projects/projectId/datasets/datasetId/tables/tableId

Output only when Entry is of type in the EntryType enum. For entries with user_specified_type, this field is optional and defaults to an empty string.




`string linked_resource = 9;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The linkedResource to set.  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
### setLinkedResourceBytes(ByteString value)
    
    
    public Entry.Builder setLinkedResourceBytes(ByteString value)

The resource this metadata entry refers to.

For Google Cloud Platform resources, `linked_resource` is the [full name of the resource](https://cloud.google.com/apis/design/resource_names#full_resource_name). For example, the `linked_resource` for a table resource from BigQuery is:

  * //bigquery.googleapis.com/projects/projectId/datasets/datasetId/tables/tableId

Output only when Entry is of type in the EntryType enum. For entries with user_specified_type, this field is optional and defaults to an empty string.




`string linked_resource = 9;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for linkedResource to set.  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
### setName(String value)
    
    
    public Entry.Builder setName(String value)

Output only. Identifier. The Data Catalog resource name of the entry in URL format. Example:

  * projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}

Note that this Entry and its child resources may not actually be stored in the location in this name.




` string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IDENTIFIER, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public Entry.Builder setNameBytes(ByteString value)

Output only. Identifier. The Data Catalog resource name of the entry in URL format. Example:

  * projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}

Note that this Entry and its child resources may not actually be stored in the location in this name.




` string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_behavior) = IDENTIFIER, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
### setSchema(Schema value)
    
    
    public Entry.Builder setSchema(Schema value)

Schema of the entry. An entry might not have any schema attached to it.

`.google.cloud.datacatalog.v1beta1.Schema schema = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Schema](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Schema)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### setSchema(Schema.Builder builderForValue)
    
    
    public Entry.Builder setSchema(Schema.Builder builderForValue)

Schema of the entry. An entry might not have any schema attached to it.

`.google.cloud.datacatalog.v1beta1.Schema schema = 5;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Schema.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Schema.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### setSourceSystemTimestamps(SystemTimestamps value)
    
    
    public Entry.Builder setSourceSystemTimestamps(SystemTimestamps value)

Output only. Timestamps about the underlying resource, not about this Data Catalog entry. Output only when Entry is of type in the EntryType enum. For entries with user_specified_type, this field is optional and defaults to an empty timestamp.

` .google.cloud.datacatalog.v1beta1.SystemTimestamps source_system_timestamps = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SystemTimestamps](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.SystemTimestamps)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### setSourceSystemTimestamps(SystemTimestamps.Builder builderForValue)
    
    
    public Entry.Builder setSourceSystemTimestamps(SystemTimestamps.Builder builderForValue)

Output only. Timestamps about the underlying resource, not about this Data Catalog entry. Output only when Entry is of type in the EntryType enum. For entries with user_specified_type, this field is optional and defaults to an empty timestamp.

` .google.cloud.datacatalog.v1beta1.SystemTimestamps source_system_timestamps = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SystemTimestamps.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.SystemTimestamps.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### setType(EntryType value)
    
    
    public Entry.Builder setType(EntryType value)

The type of the entry. Only used for Entries with types in the EntryType enum.

`.google.cloud.datacatalog.v1beta1.EntryType type = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[EntryType](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.EntryType)`  
The type to set.  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
### setTypeValue(int value)
    
    
    public Entry.Builder setTypeValue(int value)

The type of the entry. Only used for Entries with types in the EntryType enum.

`.google.cloud.datacatalog.v1beta1.EntryType type = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for type to set.  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
### setUsageSignal(UsageSignal value)
    
    
    public Entry.Builder setUsageSignal(UsageSignal value)

Output only. Statistics on the usage level of the resource.

` .google.cloud.datacatalog.v1beta1.UsageSignal usage_signal = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[UsageSignal](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.UsageSignal)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### setUsageSignal(UsageSignal.Builder builderForValue)
    
    
    public Entry.Builder setUsageSignal(UsageSignal.Builder builderForValue)

Output only. Statistics on the usage level of the resource.

` .google.cloud.datacatalog.v1beta1.UsageSignal usage_signal = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[UsageSignal.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.UsageSignal.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` |   
  
### setUserSpecifiedSystem(String value)
    
    
    public Entry.Builder setUserSpecifiedSystem(String value)

This field indicates the entry's source system that Data Catalog does not integrate with. `user_specified_system` strings must begin with a letter or underscore and can only contain letters, numbers, and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.

`string user_specified_system = 18;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The userSpecifiedSystem to set.  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
### setUserSpecifiedSystemBytes(ByteString value)
    
    
    public Entry.Builder setUserSpecifiedSystemBytes(ByteString value)

This field indicates the entry's source system that Data Catalog does not integrate with. `user_specified_system` strings must begin with a letter or underscore and can only contain letters, numbers, and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.

`string user_specified_system = 18;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for userSpecifiedSystem to set.  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
### setUserSpecifiedType(String value)
    
    
    public Entry.Builder setUserSpecifiedType(String value)

Entry type if it does not fit any of the input-allowed values listed in `EntryType` enum above. When creating an entry, users should check the enum values first, if nothing matches the entry to be created, then provide a custom value, for example "my_special_type". `user_specified_type` strings must begin with a letter or underscore and can only contain letters, numbers, and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.

Currently, only FILESET enum value is allowed. All other entries created through Data Catalog must use `user_specified_type`.

`string user_specified_type = 16;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The userSpecifiedType to set.  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
### setUserSpecifiedTypeBytes(ByteString value)
    
    
    public Entry.Builder setUserSpecifiedTypeBytes(ByteString value)

Entry type if it does not fit any of the input-allowed values listed in `EntryType` enum above. When creating an entry, users should check the enum values first, if nothing matches the entry to be created, then provide a custom value, for example "my_special_type". `user_specified_type` strings must begin with a letter or underscore and can only contain letters, numbers, and underscores; are case insensitive; must be at least 1 character and at most 64 characters long.

Currently, only FILESET enum value is allowed. All other entries created through Data Catalog must use `user_specified_type`.

`string user_specified_type = 16;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for userSpecifiedType to set.  
**Returns**  
---  
**Type** | **Description**  
`[Entry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Entry.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
