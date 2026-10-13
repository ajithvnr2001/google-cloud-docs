---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder
title: Class ReadRowsResponse.Builder (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:59:36.143026+00:00
---

# Class ReadRowsResponse.Builder (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ReadRowsResponse.Builder (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 
    
    
    public static final class ReadRowsResponse.Builder extends GeneratedMessage.Builder<ReadRowsResponse.Builder> implements ReadRowsResponseOrBuilder

Response from calling `ReadRows` may include row data, progress and throttling information.

Protobuf type `google.cloud.bigquery.storage.v1.ReadRowsResponse`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > ReadRowsResponse.Builder

## Implements

[ReadRowsResponseOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponseOrBuilder)

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
    
    
    public ReadRowsResponse build()

**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse)` |   
  
### buildPartial()
    
    
    public ReadRowsResponse buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse)` |   
  
### clear()
    
    
    public ReadRowsResponse.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearArrowRecordBatch()
    
    
    public ReadRowsResponse.Builder clearArrowRecordBatch()

Serialized row data in Arrow RecordBatch format.

`.google.cloud.bigquery.storage.v1.ArrowRecordBatch arrow_record_batch = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### clearArrowSchema()
    
    
    public ReadRowsResponse.Builder clearArrowSchema()

Output only. Arrow schema.

` .google.cloud.bigquery.storage.v1.ArrowSchema arrow_schema = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### clearAvroRows()
    
    
    public ReadRowsResponse.Builder clearAvroRows()

Serialized row data in AVRO format.

`.google.cloud.bigquery.storage.v1.AvroRows avro_rows = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### clearAvroSchema()
    
    
    public ReadRowsResponse.Builder clearAvroSchema()

Output only. Avro schema.

` .google.cloud.bigquery.storage.v1.AvroSchema avro_schema = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### clearRowCount()
    
    
    public ReadRowsResponse.Builder clearRowCount()

Number of serialized rows in the rows block.

`int64 row_count = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` | This builder for chaining.  
  
### clearRows()
    
    
    public ReadRowsResponse.Builder clearRows()

**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### clearSchema()
    
    
    public ReadRowsResponse.Builder clearSchema()

**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### clearStats()
    
    
    public ReadRowsResponse.Builder clearStats()

Statistics for the stream.

`.google.cloud.bigquery.storage.v1.StreamStats stats = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### clearThrottleState()
    
    
    public ReadRowsResponse.Builder clearThrottleState()

Throttling state. If unset, the latest response still describes the current throttling status.

`.google.cloud.bigquery.storage.v1.ThrottleState throttle_state = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### clearTotalEstimatedRowCount()
    
    
    public ReadRowsResponse.Builder clearTotalEstimatedRowCount()

Output only. The total estimated number of rows in the query results. Only populated when reading data from a BigQuery job.

This feature is not yet available.

` optional int64 total_estimated_row_count = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` | This builder for chaining.  
  
### clearUncompressedByteSize()
    
    
    public ReadRowsResponse.Builder clearUncompressedByteSize()

Optional. If the row data in this ReadRowsResponse is compressed, then uncompressed byte size is the original size of the uncompressed row data. If it is set to a value greater than 0, then decompress into a buffer of size uncompressed_byte_size using the compression codec that was requested during session creation time and which is specified in TableReadOptions.response_compression_codec in ReadSession. This value is not set if no response_compression_codec was not requested and it is -1 if the requested compression would not have reduced the size of this ReadRowsResponse's row data. This attempts to match Apache Arrow's behavior described here <https://github.com/apache/arrow/issues/15102> where the uncompressed length may be set to -1 to indicate that the data that follows is not compressed, which can be useful for cases where compression does not yield appreciable savings. When uncompressed_byte_size is not greater than 0, the client should skip decompression.

`optional int64 uncompressed_byte_size = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` | This builder for chaining.  
  
### getArrowRecordBatch()
    
    
    public ArrowRecordBatch getArrowRecordBatch()

Serialized row data in Arrow RecordBatch format.

`.google.cloud.bigquery.storage.v1.ArrowRecordBatch arrow_record_batch = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ArrowRecordBatch](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowRecordBatch)` | The arrowRecordBatch.  
  
### getArrowRecordBatchBuilder()
    
    
    public ArrowRecordBatch.Builder getArrowRecordBatchBuilder()

Serialized row data in Arrow RecordBatch format.

`.google.cloud.bigquery.storage.v1.ArrowRecordBatch arrow_record_batch = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ArrowRecordBatch.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowRecordBatch.Builder)` |   
  
### getArrowRecordBatchOrBuilder()
    
    
    public ArrowRecordBatchOrBuilder getArrowRecordBatchOrBuilder()

Serialized row data in Arrow RecordBatch format.

`.google.cloud.bigquery.storage.v1.ArrowRecordBatch arrow_record_batch = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ArrowRecordBatchOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowRecordBatchOrBuilder)` |   
  
### getArrowSchema()
    
    
    public ArrowSchema getArrowSchema()

Output only. Arrow schema.

` .google.cloud.bigquery.storage.v1.ArrowSchema arrow_schema = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ArrowSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowSchema)` | The arrowSchema.  
  
### getArrowSchemaBuilder()
    
    
    public ArrowSchema.Builder getArrowSchemaBuilder()

Output only. Arrow schema.

` .google.cloud.bigquery.storage.v1.ArrowSchema arrow_schema = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ArrowSchema.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowSchema.Builder)` |   
  
### getArrowSchemaOrBuilder()
    
    
    public ArrowSchemaOrBuilder getArrowSchemaOrBuilder()

Output only. Arrow schema.

` .google.cloud.bigquery.storage.v1.ArrowSchema arrow_schema = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ArrowSchemaOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowSchemaOrBuilder)` |   
  
### getAvroRows()
    
    
    public AvroRows getAvroRows()

Serialized row data in AVRO format.

`.google.cloud.bigquery.storage.v1.AvroRows avro_rows = 3;`

**Returns**  
---  
**Type** | **Description**  
`[AvroRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AvroRows)` | The avroRows.  
  
### getAvroRowsBuilder()
    
    
    public AvroRows.Builder getAvroRowsBuilder()

Serialized row data in AVRO format.

`.google.cloud.bigquery.storage.v1.AvroRows avro_rows = 3;`

**Returns**  
---  
**Type** | **Description**  
`[AvroRows.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AvroRows.Builder)` |   
  
### getAvroRowsOrBuilder()
    
    
    public AvroRowsOrBuilder getAvroRowsOrBuilder()

Serialized row data in AVRO format.

`.google.cloud.bigquery.storage.v1.AvroRows avro_rows = 3;`

**Returns**  
---  
**Type** | **Description**  
`[AvroRowsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AvroRowsOrBuilder)` |   
  
### getAvroSchema()
    
    
    public AvroSchema getAvroSchema()

Output only. Avro schema.

` .google.cloud.bigquery.storage.v1.AvroSchema avro_schema = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AvroSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AvroSchema)` | The avroSchema.  
  
### getAvroSchemaBuilder()
    
    
    public AvroSchema.Builder getAvroSchemaBuilder()

Output only. Avro schema.

` .google.cloud.bigquery.storage.v1.AvroSchema avro_schema = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AvroSchema.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AvroSchema.Builder)` |   
  
### getAvroSchemaOrBuilder()
    
    
    public AvroSchemaOrBuilder getAvroSchemaOrBuilder()

Output only. Avro schema.

` .google.cloud.bigquery.storage.v1.AvroSchema avro_schema = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AvroSchemaOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AvroSchemaOrBuilder)` |   
  
### getDefaultInstanceForType()
    
    
    public ReadRowsResponse getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getRowCount()
    
    
    public long getRowCount()

Number of serialized rows in the rows block.

`int64 row_count = 6;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The rowCount.  
  
### getRowsCase()
    
    
    public ReadRowsResponse.RowsCase getRowsCase()

**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.RowsCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.RowsCase)` |   
  
### getSchemaCase()
    
    
    public ReadRowsResponse.SchemaCase getSchemaCase()

**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.SchemaCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.SchemaCase)` |   
  
### getStats()
    
    
    public StreamStats getStats()

Statistics for the stream.

`.google.cloud.bigquery.storage.v1.StreamStats stats = 2;`

**Returns**  
---  
**Type** | **Description**  
`[StreamStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamStats)` | The stats.  
  
### getStatsBuilder()
    
    
    public StreamStats.Builder getStatsBuilder()

Statistics for the stream.

`.google.cloud.bigquery.storage.v1.StreamStats stats = 2;`

**Returns**  
---  
**Type** | **Description**  
`[StreamStats.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamStats.Builder)` |   
  
### getStatsOrBuilder()
    
    
    public StreamStatsOrBuilder getStatsOrBuilder()

Statistics for the stream.

`.google.cloud.bigquery.storage.v1.StreamStats stats = 2;`

**Returns**  
---  
**Type** | **Description**  
`[StreamStatsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamStatsOrBuilder)` |   
  
### getThrottleState()
    
    
    public ThrottleState getThrottleState()

Throttling state. If unset, the latest response still describes the current throttling status.

`.google.cloud.bigquery.storage.v1.ThrottleState throttle_state = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ThrottleState](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ThrottleState)` | The throttleState.  
  
### getThrottleStateBuilder()
    
    
    public ThrottleState.Builder getThrottleStateBuilder()

Throttling state. If unset, the latest response still describes the current throttling status.

`.google.cloud.bigquery.storage.v1.ThrottleState throttle_state = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ThrottleState.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ThrottleState.Builder)` |   
  
### getThrottleStateOrBuilder()
    
    
    public ThrottleStateOrBuilder getThrottleStateOrBuilder()

Throttling state. If unset, the latest response still describes the current throttling status.

`.google.cloud.bigquery.storage.v1.ThrottleState throttle_state = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ThrottleStateOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ThrottleStateOrBuilder)` |   
  
### getTotalEstimatedRowCount()
    
    
    public long getTotalEstimatedRowCount()

Output only. The total estimated number of rows in the query results. Only populated when reading data from a BigQuery job.

This feature is not yet available.

` optional int64 total_estimated_row_count = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The totalEstimatedRowCount.  
  
### getUncompressedByteSize()
    
    
    public long getUncompressedByteSize()

Optional. If the row data in this ReadRowsResponse is compressed, then uncompressed byte size is the original size of the uncompressed row data. If it is set to a value greater than 0, then decompress into a buffer of size uncompressed_byte_size using the compression codec that was requested during session creation time and which is specified in TableReadOptions.response_compression_codec in ReadSession. This value is not set if no response_compression_codec was not requested and it is -1 if the requested compression would not have reduced the size of this ReadRowsResponse's row data. This attempts to match Apache Arrow's behavior described here <https://github.com/apache/arrow/issues/15102> where the uncompressed length may be set to -1 to indicate that the data that follows is not compressed, which can be useful for cases where compression does not yield appreciable savings. When uncompressed_byte_size is not greater than 0, the client should skip decompression.

`optional int64 uncompressed_byte_size = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The uncompressedByteSize.  
  
### hasArrowRecordBatch()
    
    
    public boolean hasArrowRecordBatch()

Serialized row data in Arrow RecordBatch format.

`.google.cloud.bigquery.storage.v1.ArrowRecordBatch arrow_record_batch = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the arrowRecordBatch field is set.  
  
### hasArrowSchema()
    
    
    public boolean hasArrowSchema()

Output only. Arrow schema.

` .google.cloud.bigquery.storage.v1.ArrowSchema arrow_schema = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the arrowSchema field is set.  
  
### hasAvroRows()
    
    
    public boolean hasAvroRows()

Serialized row data in AVRO format.

`.google.cloud.bigquery.storage.v1.AvroRows avro_rows = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the avroRows field is set.  
  
### hasAvroSchema()
    
    
    public boolean hasAvroSchema()

Output only. Avro schema.

` .google.cloud.bigquery.storage.v1.AvroSchema avro_schema = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the avroSchema field is set.  
  
### hasStats()
    
    
    public boolean hasStats()

Statistics for the stream.

`.google.cloud.bigquery.storage.v1.StreamStats stats = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the stats field is set.  
  
### hasThrottleState()
    
    
    public boolean hasThrottleState()

Throttling state. If unset, the latest response still describes the current throttling status.

`.google.cloud.bigquery.storage.v1.ThrottleState throttle_state = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the throttleState field is set.  
  
### hasTotalEstimatedRowCount()
    
    
    public boolean hasTotalEstimatedRowCount()

Output only. The total estimated number of rows in the query results. Only populated when reading data from a BigQuery job.

This feature is not yet available.

` optional int64 total_estimated_row_count = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the totalEstimatedRowCount field is set.  
  
### hasUncompressedByteSize()
    
    
    public boolean hasUncompressedByteSize()

Optional. If the row data in this ReadRowsResponse is compressed, then uncompressed byte size is the original size of the uncompressed row data. If it is set to a value greater than 0, then decompress into a buffer of size uncompressed_byte_size using the compression codec that was requested during session creation time and which is specified in TableReadOptions.response_compression_codec in ReadSession. This value is not set if no response_compression_codec was not requested and it is -1 if the requested compression would not have reduced the size of this ReadRowsResponse's row data. This attempts to match Apache Arrow's behavior described here <https://github.com/apache/arrow/issues/15102> where the uncompressed length may be set to -1 to indicate that the data that follows is not compressed, which can be useful for cases where compression does not yield appreciable savings. When uncompressed_byte_size is not greater than 0, the client should skip decompression.

`optional int64 uncompressed_byte_size = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the uncompressedByteSize field is set.  
  
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

### mergeArrowRecordBatch(ArrowRecordBatch value)
    
    
    public ReadRowsResponse.Builder mergeArrowRecordBatch(ArrowRecordBatch value)

Serialized row data in Arrow RecordBatch format.

`.google.cloud.bigquery.storage.v1.ArrowRecordBatch arrow_record_batch = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ArrowRecordBatch](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowRecordBatch)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### mergeArrowSchema(ArrowSchema value)
    
    
    public ReadRowsResponse.Builder mergeArrowSchema(ArrowSchema value)

Output only. Arrow schema.

` .google.cloud.bigquery.storage.v1.ArrowSchema arrow_schema = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ArrowSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowSchema)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### mergeAvroRows(AvroRows value)
    
    
    public ReadRowsResponse.Builder mergeAvroRows(AvroRows value)

Serialized row data in AVRO format.

`.google.cloud.bigquery.storage.v1.AvroRows avro_rows = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AvroRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AvroRows)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### mergeAvroSchema(AvroSchema value)
    
    
    public ReadRowsResponse.Builder mergeAvroSchema(AvroSchema value)

Output only. Avro schema.

` .google.cloud.bigquery.storage.v1.AvroSchema avro_schema = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AvroSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AvroSchema)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### mergeFrom(ReadRowsResponse other)
    
    
    public ReadRowsResponse.Builder mergeFrom(ReadRowsResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ReadRowsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public ReadRowsResponse.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public ReadRowsResponse.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeStats(StreamStats value)
    
    
    public ReadRowsResponse.Builder mergeStats(StreamStats value)

Statistics for the stream.

`.google.cloud.bigquery.storage.v1.StreamStats stats = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[StreamStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamStats)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### mergeThrottleState(ThrottleState value)
    
    
    public ReadRowsResponse.Builder mergeThrottleState(ThrottleState value)

Throttling state. If unset, the latest response still describes the current throttling status.

`.google.cloud.bigquery.storage.v1.ThrottleState throttle_state = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ThrottleState](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ThrottleState)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### setArrowRecordBatch(ArrowRecordBatch value)
    
    
    public ReadRowsResponse.Builder setArrowRecordBatch(ArrowRecordBatch value)

Serialized row data in Arrow RecordBatch format.

`.google.cloud.bigquery.storage.v1.ArrowRecordBatch arrow_record_batch = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ArrowRecordBatch](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowRecordBatch)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### setArrowRecordBatch(ArrowRecordBatch.Builder builderForValue)
    
    
    public ReadRowsResponse.Builder setArrowRecordBatch(ArrowRecordBatch.Builder builderForValue)

Serialized row data in Arrow RecordBatch format.

`.google.cloud.bigquery.storage.v1.ArrowRecordBatch arrow_record_batch = 4;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ArrowRecordBatch.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowRecordBatch.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### setArrowSchema(ArrowSchema value)
    
    
    public ReadRowsResponse.Builder setArrowSchema(ArrowSchema value)

Output only. Arrow schema.

` .google.cloud.bigquery.storage.v1.ArrowSchema arrow_schema = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ArrowSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowSchema)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### setArrowSchema(ArrowSchema.Builder builderForValue)
    
    
    public ReadRowsResponse.Builder setArrowSchema(ArrowSchema.Builder builderForValue)

Output only. Arrow schema.

` .google.cloud.bigquery.storage.v1.ArrowSchema arrow_schema = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ArrowSchema.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ArrowSchema.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### setAvroRows(AvroRows value)
    
    
    public ReadRowsResponse.Builder setAvroRows(AvroRows value)

Serialized row data in AVRO format.

`.google.cloud.bigquery.storage.v1.AvroRows avro_rows = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AvroRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AvroRows)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### setAvroRows(AvroRows.Builder builderForValue)
    
    
    public ReadRowsResponse.Builder setAvroRows(AvroRows.Builder builderForValue)

Serialized row data in AVRO format.

`.google.cloud.bigquery.storage.v1.AvroRows avro_rows = 3;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[AvroRows.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AvroRows.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### setAvroSchema(AvroSchema value)
    
    
    public ReadRowsResponse.Builder setAvroSchema(AvroSchema value)

Output only. Avro schema.

` .google.cloud.bigquery.storage.v1.AvroSchema avro_schema = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AvroSchema](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AvroSchema)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### setAvroSchema(AvroSchema.Builder builderForValue)
    
    
    public ReadRowsResponse.Builder setAvroSchema(AvroSchema.Builder builderForValue)

Output only. Avro schema.

` .google.cloud.bigquery.storage.v1.AvroSchema avro_schema = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[AvroSchema.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AvroSchema.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### setRowCount(long value)
    
    
    public ReadRowsResponse.Builder setRowCount(long value)

Number of serialized rows in the rows block.

`int64 row_count = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The rowCount to set.  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` | This builder for chaining.  
  
### setStats(StreamStats value)
    
    
    public ReadRowsResponse.Builder setStats(StreamStats value)

Statistics for the stream.

`.google.cloud.bigquery.storage.v1.StreamStats stats = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[StreamStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamStats)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### setStats(StreamStats.Builder builderForValue)
    
    
    public ReadRowsResponse.Builder setStats(StreamStats.Builder builderForValue)

Statistics for the stream.

`.google.cloud.bigquery.storage.v1.StreamStats stats = 2;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[StreamStats.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StreamStats.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### setThrottleState(ThrottleState value)
    
    
    public ReadRowsResponse.Builder setThrottleState(ThrottleState value)

Throttling state. If unset, the latest response still describes the current throttling status.

`.google.cloud.bigquery.storage.v1.ThrottleState throttle_state = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ThrottleState](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ThrottleState)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### setThrottleState(ThrottleState.Builder builderForValue)
    
    
    public ReadRowsResponse.Builder setThrottleState(ThrottleState.Builder builderForValue)

Throttling state. If unset, the latest response still describes the current throttling status.

`.google.cloud.bigquery.storage.v1.ThrottleState throttle_state = 5;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ThrottleState.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ThrottleState.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` |   
  
### setTotalEstimatedRowCount(long value)
    
    
    public ReadRowsResponse.Builder setTotalEstimatedRowCount(long value)

Output only. The total estimated number of rows in the query results. Only populated when reading data from a BigQuery job.

This feature is not yet available.

` optional int64 total_estimated_row_count = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The totalEstimatedRowCount to set.  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` | This builder for chaining.  
  
### setUncompressedByteSize(long value)
    
    
    public ReadRowsResponse.Builder setUncompressedByteSize(long value)

Optional. If the row data in this ReadRowsResponse is compressed, then uncompressed byte size is the original size of the uncompressed row data. If it is set to a value greater than 0, then decompress into a buffer of size uncompressed_byte_size using the compression codec that was requested during session creation time and which is specified in TableReadOptions.response_compression_codec in ReadSession. This value is not set if no response_compression_codec was not requested and it is -1 if the requested compression would not have reduced the size of this ReadRowsResponse's row data. This attempts to match Apache Arrow's behavior described here <https://github.com/apache/arrow/issues/15102> where the uncompressed length may be set to -1 to indicate that the data that follows is not compressed, which can be useful for cases where compression does not yield appreciable savings. When uncompressed_byte_size is not greater than 0, the client should skip decompression.

`optional int64 uncompressed_byte_size = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The uncompressedByteSize to set.  
**Returns**  
---  
**Type** | **Description**  
`[ReadRowsResponse.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ReadRowsResponse.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
