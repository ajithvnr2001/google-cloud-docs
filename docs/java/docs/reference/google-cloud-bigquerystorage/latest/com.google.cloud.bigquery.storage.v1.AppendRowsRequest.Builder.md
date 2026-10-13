---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder
title: Class AppendRowsRequest.Builder (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:59:29.229197+00:00
---

# Class AppendRowsRequest.Builder (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AppendRowsRequest.Builder (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 
    
    
    public static final class AppendRowsRequest.Builder extends GeneratedMessage.Builder<AppendRowsRequest.Builder> implements AppendRowsRequestOrBuilder

Request message for `AppendRows`.

Because AppendRows is a bidirectional streaming RPC, certain parts of the AppendRowsRequest need only be specified for the first request before switching table destinations. You can also switch table destinations within the same connection for the default stream.

The size of a single AppendRowsRequest must be less than 20 MB in size. Requests larger than this return an error, typically `INVALID_ARGUMENT`.

Protobuf type `google.cloud.bigquery.storage.v1.AppendRowsRequest`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > AppendRowsRequest.Builder

## Implements

[AppendRowsRequestOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequestOrBuilder)

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
    
    
    public AppendRowsRequest build()

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest)` |   
  
### buildPartial()
    
    
    public AppendRowsRequest buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest)` |   
  
### clear()
    
    
    public AppendRowsRequest.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearArrowRows()
    
    
    public AppendRowsRequest.Builder clearArrowRows()

Rows in arrow format.

`.google.cloud.bigquery.storage.v1.AppendRowsRequest.ArrowData arrow_rows = 5;`

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### clearClientStats()
    
    
    public AppendRowsRequest.Builder clearClientStats()

Optional. Stats and telemetry data gathered on the client side.

` .google.cloud.bigquery.storage.v1.ClientStats client_stats = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### clearDefaultMissingValueInterpretation()
    
    
    public AppendRowsRequest.Builder clearDefaultMissingValueInterpretation()

Optional. Default missing value interpretation for all columns in the table. When a value is specified on an `AppendRowsRequest`, it is applied to all requests from that point forward, until a subsequent `AppendRowsRequest` sets it to a different value. `missing_value_interpretation` can override `default_missing_value_interpretation`. For example, if you want to write `NULL` instead of using default values for some columns, you can set `default_missing_value_interpretation` to `DEFAULT_VALUE` and at the same time, set `missing_value_interpretations` to `NULL_VALUE` on those columns.

` .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation default_missing_value_interpretation = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` | This builder for chaining.  
  
### clearMissingValueInterpretations()
    
    
    public AppendRowsRequest.Builder clearMissingValueInterpretations()

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### clearOffset()
    
    
    public AppendRowsRequest.Builder clearOffset()

If present, the write is only performed if the next append offset is same as the provided value. If not present, the write is performed at the current end of stream. Specifying a value for this field is not allowed when calling AppendRows for the '_default' stream.

`.google.protobuf.Int64Value offset = 2;`

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### clearProtoRows()
    
    
    public AppendRowsRequest.Builder clearProtoRows()

Rows in proto format.

`.google.cloud.bigquery.storage.v1.AppendRowsRequest.ProtoData proto_rows = 4;`

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### clearRows()
    
    
    public AppendRowsRequest.Builder clearRows()

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### clearTraceId()
    
    
    public AppendRowsRequest.Builder clearTraceId()

Id set by client to annotate its identity. Only initial request setting is respected.

`string trace_id = 6;`

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` | This builder for chaining.  
  
### clearWriteStream()
    
    
    public AppendRowsRequest.Builder clearWriteStream()

Required. The write_stream identifies the append operation. It must be provided in the following scenarios:

  * In the first request to an AppendRows connection.

  * In all subsequent requests to an AppendRows connection, if you use the same connection to write to multiple tables or change the input schema for default streams.

For explicitly created write streams, the format is:

  * `projects/{project}/datasets/{dataset}/tables/{table}/streams/{id}`

For the special default stream, the format is:

  * `projects/{project}/datasets/{dataset}/tables/{table}/streams/_default`.

An example of a possible sequence of requests with write_stream fields within a single connection:

  * r1: {write_stream: stream_name_1}

  * r2: {write_stream: /*omit*/}

  * r3: {write_stream: /*omit*/}

  * r4: {write_stream: stream_name_2}

  * r5: {write_stream: stream_name_2}

The destination changed in request_4, so the write_stream field must be populated in all subsequent requests in this stream.




` string write_stream = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` | This builder for chaining.  
  
### containsMissingValueInterpretations(String key)
    
    
    public boolean containsMissingValueInterpretations(String key)

A map to indicate how to interpret missing value for some fields. Missing values are fields present in user schema but missing in rows. The key is the field name. The value is the interpretation of missing values for the field.

For example, a map {'foo': NULL_VALUE, 'bar': DEFAULT_VALUE} means all missing values in field foo are interpreted as NULL, all missing values in field bar are interpreted as the default value of field bar in table schema.

If a field is not in this map and has missing values, the missing values in this field are interpreted as NULL.

This field only applies to the current request, it won't affect other requests on the connection.

Currently, field name can only be top-level column name, can't be a struct field path like 'foo.bar'.

` map<string, .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation> missing_value_interpretations = 7; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getArrowRows()
    
    
    public AppendRowsRequest.ArrowData getArrowRows()

Rows in arrow format.

`.google.cloud.bigquery.storage.v1.AppendRowsRequest.ArrowData arrow_rows = 5;`

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.ArrowData](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.ArrowData)` | The arrowRows.  
  
### getArrowRowsBuilder()
    
    
    public AppendRowsRequest.ArrowData.Builder getArrowRowsBuilder()

Rows in arrow format.

`.google.cloud.bigquery.storage.v1.AppendRowsRequest.ArrowData arrow_rows = 5;`

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.ArrowData.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.ArrowData.Builder)` |   
  
### getArrowRowsOrBuilder()
    
    
    public AppendRowsRequest.ArrowDataOrBuilder getArrowRowsOrBuilder()

Rows in arrow format.

`.google.cloud.bigquery.storage.v1.AppendRowsRequest.ArrowData arrow_rows = 5;`

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.ArrowDataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.ArrowDataOrBuilder)` |   
  
### getClientStats()
    
    
    public ClientStats getClientStats()

Optional. Stats and telemetry data gathered on the client side.

` .google.cloud.bigquery.storage.v1.ClientStats client_stats = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ClientStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ClientStats)` | The clientStats.  
  
### getClientStatsBuilder()
    
    
    public ClientStats.Builder getClientStatsBuilder()

Optional. Stats and telemetry data gathered on the client side.

` .google.cloud.bigquery.storage.v1.ClientStats client_stats = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ClientStats.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ClientStats.Builder)` |   
  
### getClientStatsOrBuilder()
    
    
    public ClientStatsOrBuilder getClientStatsOrBuilder()

Optional. Stats and telemetry data gathered on the client side.

` .google.cloud.bigquery.storage.v1.ClientStats client_stats = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ClientStatsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ClientStatsOrBuilder)` |   
  
### getDefaultInstanceForType()
    
    
    public AppendRowsRequest getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest)` |   
  
### getDefaultMissingValueInterpretation()
    
    
    public AppendRowsRequest.MissingValueInterpretation getDefaultMissingValueInterpretation()

Optional. Default missing value interpretation for all columns in the table. When a value is specified on an `AppendRowsRequest`, it is applied to all requests from that point forward, until a subsequent `AppendRowsRequest` sets it to a different value. `missing_value_interpretation` can override `default_missing_value_interpretation`. For example, if you want to write `NULL` instead of using default values for some columns, you can set `default_missing_value_interpretation` to `DEFAULT_VALUE` and at the same time, set `missing_value_interpretations` to `NULL_VALUE` on those columns.

` .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation default_missing_value_interpretation = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.MissingValueInterpretation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation)` | The defaultMissingValueInterpretation.  
  
### getDefaultMissingValueInterpretationValue()
    
    
    public int getDefaultMissingValueInterpretationValue()

Optional. Default missing value interpretation for all columns in the table. When a value is specified on an `AppendRowsRequest`, it is applied to all requests from that point forward, until a subsequent `AppendRowsRequest` sets it to a different value. `missing_value_interpretation` can override `default_missing_value_interpretation`. For example, if you want to write `NULL` instead of using default values for some columns, you can set `default_missing_value_interpretation` to `DEFAULT_VALUE` and at the same time, set `missing_value_interpretations` to `NULL_VALUE` on those columns.

` .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation default_missing_value_interpretation = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for defaultMissingValueInterpretation.  
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getMissingValueInterpretations() (deprecated)
    
    
    public Map<String,AppendRowsRequest.MissingValueInterpretation> getMissingValueInterpretations()

Use [#getMissingValueInterpretationsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder#com_google_cloud_bigquery_storage_v1_AppendRowsRequest_Builder_getMissingValueInterpretationsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[MissingValueInterpretation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation)>` |   
  
### getMissingValueInterpretationsCount()
    
    
    public int getMissingValueInterpretationsCount()

A map to indicate how to interpret missing value for some fields. Missing values are fields present in user schema but missing in rows. The key is the field name. The value is the interpretation of missing values for the field.

For example, a map {'foo': NULL_VALUE, 'bar': DEFAULT_VALUE} means all missing values in field foo are interpreted as NULL, all missing values in field bar are interpreted as the default value of field bar in table schema.

If a field is not in this map and has missing values, the missing values in this field are interpreted as NULL.

This field only applies to the current request, it won't affect other requests on the connection.

Currently, field name can only be top-level column name, can't be a struct field path like 'foo.bar'.

` map<string, .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation> missing_value_interpretations = 7; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMissingValueInterpretationsMap()
    
    
    public Map<String,AppendRowsRequest.MissingValueInterpretation> getMissingValueInterpretationsMap()

A map to indicate how to interpret missing value for some fields. Missing values are fields present in user schema but missing in rows. The key is the field name. The value is the interpretation of missing values for the field.

For example, a map {'foo': NULL_VALUE, 'bar': DEFAULT_VALUE} means all missing values in field foo are interpreted as NULL, all missing values in field bar are interpreted as the default value of field bar in table schema.

If a field is not in this map and has missing values, the missing values in this field are interpreted as NULL.

This field only applies to the current request, it won't affect other requests on the connection.

Currently, field name can only be top-level column name, can't be a struct field path like 'foo.bar'.

` map<string, .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation> missing_value_interpretations = 7; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[MissingValueInterpretation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation)>` |   
  
### getMissingValueInterpretationsOrDefault(String key, AppendRowsRequest.MissingValueInterpretation defaultValue)
    
    
    public AppendRowsRequest.MissingValueInterpretation getMissingValueInterpretationsOrDefault(String key, AppendRowsRequest.MissingValueInterpretation defaultValue)

A map to indicate how to interpret missing value for some fields. Missing values are fields present in user schema but missing in rows. The key is the field name. The value is the interpretation of missing values for the field.

For example, a map {'foo': NULL_VALUE, 'bar': DEFAULT_VALUE} means all missing values in field foo are interpreted as NULL, all missing values in field bar are interpreted as the default value of field bar in table schema.

If a field is not in this map and has missing values, the missing values in this field are interpreted as NULL.

This field only applies to the current request, it won't affect other requests on the connection.

Currently, field name can only be top-level column name, can't be a struct field path like 'foo.bar'.

` map<string, .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation> missing_value_interpretations = 7; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[AppendRowsRequest.MissingValueInterpretation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.MissingValueInterpretation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation)` |   
  
### getMissingValueInterpretationsOrThrow(String key)
    
    
    public AppendRowsRequest.MissingValueInterpretation getMissingValueInterpretationsOrThrow(String key)

A map to indicate how to interpret missing value for some fields. Missing values are fields present in user schema but missing in rows. The key is the field name. The value is the interpretation of missing values for the field.

For example, a map {'foo': NULL_VALUE, 'bar': DEFAULT_VALUE} means all missing values in field foo are interpreted as NULL, all missing values in field bar are interpreted as the default value of field bar in table schema.

If a field is not in this map and has missing values, the missing values in this field are interpreted as NULL.

This field only applies to the current request, it won't affect other requests on the connection.

Currently, field name can only be top-level column name, can't be a struct field path like 'foo.bar'.

` map<string, .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation> missing_value_interpretations = 7; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.MissingValueInterpretation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation)` |   
  
### getMissingValueInterpretationsValue() (deprecated)
    
    
    public Map<String,Integer> getMissingValueInterpretationsValue()

Use [#getMissingValueInterpretationsValueMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder#com_google_cloud_bigquery_storage_v1_AppendRowsRequest_Builder_getMissingValueInterpretationsValueMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),java.lang.Integer>` |   
  
### getMissingValueInterpretationsValueMap()
    
    
    public Map<String,Integer> getMissingValueInterpretationsValueMap()

A map to indicate how to interpret missing value for some fields. Missing values are fields present in user schema but missing in rows. The key is the field name. The value is the interpretation of missing values for the field.

For example, a map {'foo': NULL_VALUE, 'bar': DEFAULT_VALUE} means all missing values in field foo are interpreted as NULL, all missing values in field bar are interpreted as the default value of field bar in table schema.

If a field is not in this map and has missing values, the missing values in this field are interpreted as NULL.

This field only applies to the current request, it won't affect other requests on the connection.

Currently, field name can only be top-level column name, can't be a struct field path like 'foo.bar'.

` map<string, .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation> missing_value_interpretations = 7; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),java.lang.Integer>` |   
  
### getMissingValueInterpretationsValueOrDefault(String key, int defaultValue)
    
    
    public int getMissingValueInterpretationsValueOrDefault(String key, int defaultValue)

A map to indicate how to interpret missing value for some fields. Missing values are fields present in user schema but missing in rows. The key is the field name. The value is the interpretation of missing values for the field.

For example, a map {'foo': NULL_VALUE, 'bar': DEFAULT_VALUE} means all missing values in field foo are interpreted as NULL, all missing values in field bar are interpreted as the default value of field bar in table schema.

If a field is not in this map and has missing values, the missing values in this field are interpreted as NULL.

This field only applies to the current request, it won't affect other requests on the connection.

Currently, field name can only be top-level column name, can't be a struct field path like 'foo.bar'.

` map<string, .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation> missing_value_interpretations = 7; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMissingValueInterpretationsValueOrThrow(String key)
    
    
    public int getMissingValueInterpretationsValueOrThrow(String key)

A map to indicate how to interpret missing value for some fields. Missing values are fields present in user schema but missing in rows. The key is the field name. The value is the interpretation of missing values for the field.

For example, a map {'foo': NULL_VALUE, 'bar': DEFAULT_VALUE} means all missing values in field foo are interpreted as NULL, all missing values in field bar are interpreted as the default value of field bar in table schema.

If a field is not in this map and has missing values, the missing values in this field are interpreted as NULL.

This field only applies to the current request, it won't affect other requests on the connection.

Currently, field name can only be top-level column name, can't be a struct field path like 'foo.bar'.

` map<string, .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation> missing_value_interpretations = 7; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMutableMissingValueInterpretations() (deprecated)
    
    
    public Map<String,AppendRowsRequest.MissingValueInterpretation> getMutableMissingValueInterpretations()

Use alternate mutation accessors instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[MissingValueInterpretation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation)>` |   
  
### getMutableMissingValueInterpretationsValue() (deprecated)
    
    
    public Map<String,Integer> getMutableMissingValueInterpretationsValue()

Use alternate mutation accessors instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),java.lang.Integer>` |   
  
### getOffset()
    
    
    public Int64Value getOffset()

If present, the write is only performed if the next append offset is same as the provided value. If not present, the write is performed at the current end of stream. Specifying a value for this field is not allowed when calling AppendRows for the '_default' stream.

`.google.protobuf.Int64Value offset = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Int64Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64Value.html)` | The offset.  
  
### getOffsetBuilder()
    
    
    public Int64Value.Builder getOffsetBuilder()

If present, the write is only performed if the next append offset is same as the provided value. If not present, the write is performed at the current end of stream. Specifying a value for this field is not allowed when calling AppendRows for the '_default' stream.

`.google.protobuf.Int64Value offset = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64Value.Builder.html)` |   
  
### getOffsetOrBuilder()
    
    
    public Int64ValueOrBuilder getOffsetOrBuilder()

If present, the write is only performed if the next append offset is same as the provided value. If not present, the write is performed at the current end of stream. Specifying a value for this field is not allowed when calling AppendRows for the '_default' stream.

`.google.protobuf.Int64Value offset = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Int64ValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64ValueOrBuilder.html)` |   
  
### getProtoRows()
    
    
    public AppendRowsRequest.ProtoData getProtoRows()

Rows in proto format.

`.google.cloud.bigquery.storage.v1.AppendRowsRequest.ProtoData proto_rows = 4;`

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.ProtoData](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.ProtoData)` | The protoRows.  
  
### getProtoRowsBuilder()
    
    
    public AppendRowsRequest.ProtoData.Builder getProtoRowsBuilder()

Rows in proto format.

`.google.cloud.bigquery.storage.v1.AppendRowsRequest.ProtoData proto_rows = 4;`

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.ProtoData.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.ProtoData.Builder)` |   
  
### getProtoRowsOrBuilder()
    
    
    public AppendRowsRequest.ProtoDataOrBuilder getProtoRowsOrBuilder()

Rows in proto format.

`.google.cloud.bigquery.storage.v1.AppendRowsRequest.ProtoData proto_rows = 4;`

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.ProtoDataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.ProtoDataOrBuilder)` |   
  
### getRowsCase()
    
    
    public AppendRowsRequest.RowsCase getRowsCase()

**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.RowsCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.RowsCase)` |   
  
### getTraceId()
    
    
    public String getTraceId()

Id set by client to annotate its identity. Only initial request setting is respected.

`string trace_id = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The traceId.  
  
### getTraceIdBytes()
    
    
    public ByteString getTraceIdBytes()

Id set by client to annotate its identity. Only initial request setting is respected.

`string trace_id = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for traceId.  
  
### getWriteStream()
    
    
    public String getWriteStream()

Required. The write_stream identifies the append operation. It must be provided in the following scenarios:

  * In the first request to an AppendRows connection.

  * In all subsequent requests to an AppendRows connection, if you use the same connection to write to multiple tables or change the input schema for default streams.

For explicitly created write streams, the format is:

  * `projects/{project}/datasets/{dataset}/tables/{table}/streams/{id}`

For the special default stream, the format is:

  * `projects/{project}/datasets/{dataset}/tables/{table}/streams/_default`.

An example of a possible sequence of requests with write_stream fields within a single connection:

  * r1: {write_stream: stream_name_1}

  * r2: {write_stream: /*omit*/}

  * r3: {write_stream: /*omit*/}

  * r4: {write_stream: stream_name_2}

  * r5: {write_stream: stream_name_2}

The destination changed in request_4, so the write_stream field must be populated in all subsequent requests in this stream.




` string write_stream = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The writeStream.  
  
### getWriteStreamBytes()
    
    
    public ByteString getWriteStreamBytes()

Required. The write_stream identifies the append operation. It must be provided in the following scenarios:

  * In the first request to an AppendRows connection.

  * In all subsequent requests to an AppendRows connection, if you use the same connection to write to multiple tables or change the input schema for default streams.

For explicitly created write streams, the format is:

  * `projects/{project}/datasets/{dataset}/tables/{table}/streams/{id}`

For the special default stream, the format is:

  * `projects/{project}/datasets/{dataset}/tables/{table}/streams/_default`.

An example of a possible sequence of requests with write_stream fields within a single connection:

  * r1: {write_stream: stream_name_1}

  * r2: {write_stream: /*omit*/}

  * r3: {write_stream: /*omit*/}

  * r4: {write_stream: stream_name_2}

  * r5: {write_stream: stream_name_2}

The destination changed in request_4, so the write_stream field must be populated in all subsequent requests in this stream.




` string write_stream = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for writeStream.  
  
### hasArrowRows()
    
    
    public boolean hasArrowRows()

Rows in arrow format.

`.google.cloud.bigquery.storage.v1.AppendRowsRequest.ArrowData arrow_rows = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the arrowRows field is set.  
  
### hasClientStats()
    
    
    public boolean hasClientStats()

Optional. Stats and telemetry data gathered on the client side.

` .google.cloud.bigquery.storage.v1.ClientStats client_stats = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the clientStats field is set.  
  
### hasOffset()
    
    
    public boolean hasOffset()

If present, the write is only performed if the next append offset is same as the provided value. If not present, the write is performed at the current end of stream. Specifying a value for this field is not allowed when calling AppendRows for the '_default' stream.

`.google.protobuf.Int64Value offset = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the offset field is set.  
  
### hasProtoRows()
    
    
    public boolean hasProtoRows()

Rows in proto format.

`.google.cloud.bigquery.storage.v1.AppendRowsRequest.ProtoData proto_rows = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the protoRows field is set.  
  
### internalGetFieldAccessorTable()
    
    
    protected GeneratedMessage.FieldAccessorTable internalGetFieldAccessorTable()

**Returns**  
---  
**Type** | **Description**  
`[FieldAccessorTable](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.FieldAccessorTable.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.internalGetFieldAccessorTable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_internalGetFieldAccessorTable__)

### internalGetMapFieldReflection(int number)
    
    
    protected MapFieldReflectionAccessor internalGetMapFieldReflection(int number)

**Parameter**  
---  
**Name** | **Description**  
`number` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.MapFieldReflectionAccessor` |   
**Overrides**

com.google.protobuf.GeneratedMessage.Builder.internalGetMapFieldReflection(int)

### internalGetMutableMapFieldReflection(int number)
    
    
    protected MapFieldReflectionAccessor internalGetMutableMapFieldReflection(int number)

**Parameter**  
---  
**Name** | **Description**  
`number` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.protobuf.MapFieldReflectionAccessor` |   
**Overrides**

com.google.protobuf.GeneratedMessage.Builder.internalGetMutableMapFieldReflection(int)

### isInitialized()
    
    
    public final boolean isInitialized()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_isInitialized__)

### mergeArrowRows(AppendRowsRequest.ArrowData value)
    
    
    public AppendRowsRequest.Builder mergeArrowRows(AppendRowsRequest.ArrowData value)

Rows in arrow format.

`.google.cloud.bigquery.storage.v1.AppendRowsRequest.ArrowData arrow_rows = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AppendRowsRequest.ArrowData](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.ArrowData)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### mergeClientStats(ClientStats value)
    
    
    public AppendRowsRequest.Builder mergeClientStats(ClientStats value)

Optional. Stats and telemetry data gathered on the client side.

` .google.cloud.bigquery.storage.v1.ClientStats client_stats = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ClientStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ClientStats)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### mergeFrom(AppendRowsRequest other)
    
    
    public AppendRowsRequest.Builder mergeFrom(AppendRowsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AppendRowsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public AppendRowsRequest.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public AppendRowsRequest.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeOffset(Int64Value value)
    
    
    public AppendRowsRequest.Builder mergeOffset(Int64Value value)

If present, the write is only performed if the next append offset is same as the provided value. If not present, the write is performed at the current end of stream. Specifying a value for this field is not allowed when calling AppendRows for the '_default' stream.

`.google.protobuf.Int64Value offset = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Int64Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64Value.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### mergeProtoRows(AppendRowsRequest.ProtoData value)
    
    
    public AppendRowsRequest.Builder mergeProtoRows(AppendRowsRequest.ProtoData value)

Rows in proto format.

`.google.cloud.bigquery.storage.v1.AppendRowsRequest.ProtoData proto_rows = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AppendRowsRequest.ProtoData](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.ProtoData)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### putAllMissingValueInterpretations(Map<String,AppendRowsRequest.MissingValueInterpretation> values)
    
    
    public AppendRowsRequest.Builder putAllMissingValueInterpretations(Map<String,AppendRowsRequest.MissingValueInterpretation> values)

A map to indicate how to interpret missing value for some fields. Missing values are fields present in user schema but missing in rows. The key is the field name. The value is the interpretation of missing values for the field.

For example, a map {'foo': NULL_VALUE, 'bar': DEFAULT_VALUE} means all missing values in field foo are interpreted as NULL, all missing values in field bar are interpreted as the default value of field bar in table schema.

If a field is not in this map and has missing values, the missing values in this field are interpreted as NULL.

This field only applies to the current request, it won't affect other requests on the connection.

Currently, field name can only be top-level column name, can't be a struct field path like 'foo.bar'.

` map<string, .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation> missing_value_interpretations = 7; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[MissingValueInterpretation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### putAllMissingValueInterpretationsValue(Map<String,Integer> values)
    
    
    public AppendRowsRequest.Builder putAllMissingValueInterpretationsValue(Map<String,Integer> values)

A map to indicate how to interpret missing value for some fields. Missing values are fields present in user schema but missing in rows. The key is the field name. The value is the interpretation of missing values for the field.

For example, a map {'foo': NULL_VALUE, 'bar': DEFAULT_VALUE} means all missing values in field foo are interpreted as NULL, all missing values in field bar are interpreted as the default value of field bar in table schema.

If a field is not in this map and has missing values, the missing values in this field are interpreted as NULL.

This field only applies to the current request, it won't affect other requests on the connection.

Currently, field name can only be top-level column name, can't be a struct field path like 'foo.bar'.

` map<string, .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation> missing_value_interpretations = 7; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),java.lang.Integer>`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### putMissingValueInterpretations(String key, AppendRowsRequest.MissingValueInterpretation value)
    
    
    public AppendRowsRequest.Builder putMissingValueInterpretations(String key, AppendRowsRequest.MissingValueInterpretation value)

A map to indicate how to interpret missing value for some fields. Missing values are fields present in user schema but missing in rows. The key is the field name. The value is the interpretation of missing values for the field.

For example, a map {'foo': NULL_VALUE, 'bar': DEFAULT_VALUE} means all missing values in field foo are interpreted as NULL, all missing values in field bar are interpreted as the default value of field bar in table schema.

If a field is not in this map and has missing values, the missing values in this field are interpreted as NULL.

This field only applies to the current request, it won't affect other requests on the connection.

Currently, field name can only be top-level column name, can't be a struct field path like 'foo.bar'.

` map<string, .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation> missing_value_interpretations = 7; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[AppendRowsRequest.MissingValueInterpretation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### putMissingValueInterpretationsValue(String key, int value)
    
    
    public AppendRowsRequest.Builder putMissingValueInterpretationsValue(String key, int value)

A map to indicate how to interpret missing value for some fields. Missing values are fields present in user schema but missing in rows. The key is the field name. The value is the interpretation of missing values for the field.

For example, a map {'foo': NULL_VALUE, 'bar': DEFAULT_VALUE} means all missing values in field foo are interpreted as NULL, all missing values in field bar are interpreted as the default value of field bar in table schema.

If a field is not in this map and has missing values, the missing values in this field are interpreted as NULL.

This field only applies to the current request, it won't affect other requests on the connection.

Currently, field name can only be top-level column name, can't be a struct field path like 'foo.bar'.

` map<string, .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation> missing_value_interpretations = 7; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### removeMissingValueInterpretations(String key)
    
    
    public AppendRowsRequest.Builder removeMissingValueInterpretations(String key)

A map to indicate how to interpret missing value for some fields. Missing values are fields present in user schema but missing in rows. The key is the field name. The value is the interpretation of missing values for the field.

For example, a map {'foo': NULL_VALUE, 'bar': DEFAULT_VALUE} means all missing values in field foo are interpreted as NULL, all missing values in field bar are interpreted as the default value of field bar in table schema.

If a field is not in this map and has missing values, the missing values in this field are interpreted as NULL.

This field only applies to the current request, it won't affect other requests on the connection.

Currently, field name can only be top-level column name, can't be a struct field path like 'foo.bar'.

` map<string, .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation> missing_value_interpretations = 7; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### setArrowRows(AppendRowsRequest.ArrowData value)
    
    
    public AppendRowsRequest.Builder setArrowRows(AppendRowsRequest.ArrowData value)

Rows in arrow format.

`.google.cloud.bigquery.storage.v1.AppendRowsRequest.ArrowData arrow_rows = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AppendRowsRequest.ArrowData](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.ArrowData)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### setArrowRows(AppendRowsRequest.ArrowData.Builder builderForValue)
    
    
    public AppendRowsRequest.Builder setArrowRows(AppendRowsRequest.ArrowData.Builder builderForValue)

Rows in arrow format.

`.google.cloud.bigquery.storage.v1.AppendRowsRequest.ArrowData arrow_rows = 5;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[AppendRowsRequest.ArrowData.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.ArrowData.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### setClientStats(ClientStats value)
    
    
    public AppendRowsRequest.Builder setClientStats(ClientStats value)

Optional. Stats and telemetry data gathered on the client side.

` .google.cloud.bigquery.storage.v1.ClientStats client_stats = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ClientStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ClientStats)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### setClientStats(ClientStats.Builder builderForValue)
    
    
    public AppendRowsRequest.Builder setClientStats(ClientStats.Builder builderForValue)

Optional. Stats and telemetry data gathered on the client side.

` .google.cloud.bigquery.storage.v1.ClientStats client_stats = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ClientStats.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.ClientStats.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### setDefaultMissingValueInterpretation(AppendRowsRequest.MissingValueInterpretation value)
    
    
    public AppendRowsRequest.Builder setDefaultMissingValueInterpretation(AppendRowsRequest.MissingValueInterpretation value)

Optional. Default missing value interpretation for all columns in the table. When a value is specified on an `AppendRowsRequest`, it is applied to all requests from that point forward, until a subsequent `AppendRowsRequest` sets it to a different value. `missing_value_interpretation` can override `default_missing_value_interpretation`. For example, if you want to write `NULL` instead of using default values for some columns, you can set `default_missing_value_interpretation` to `DEFAULT_VALUE` and at the same time, set `missing_value_interpretations` to `NULL_VALUE` on those columns.

` .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation default_missing_value_interpretation = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AppendRowsRequest.MissingValueInterpretation](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation)`  
The defaultMissingValueInterpretation to set.  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` | This builder for chaining.  
  
### setDefaultMissingValueInterpretationValue(int value)
    
    
    public AppendRowsRequest.Builder setDefaultMissingValueInterpretationValue(int value)

Optional. Default missing value interpretation for all columns in the table. When a value is specified on an `AppendRowsRequest`, it is applied to all requests from that point forward, until a subsequent `AppendRowsRequest` sets it to a different value. `missing_value_interpretation` can override `default_missing_value_interpretation`. For example, if you want to write `NULL` instead of using default values for some columns, you can set `default_missing_value_interpretation` to `DEFAULT_VALUE` and at the same time, set `missing_value_interpretations` to `NULL_VALUE` on those columns.

` .google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation default_missing_value_interpretation = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for defaultMissingValueInterpretation to set.  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` | This builder for chaining.  
  
### setOffset(Int64Value value)
    
    
    public AppendRowsRequest.Builder setOffset(Int64Value value)

If present, the write is only performed if the next append offset is same as the provided value. If not present, the write is performed at the current end of stream. Specifying a value for this field is not allowed when calling AppendRows for the '_default' stream.

`.google.protobuf.Int64Value offset = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Int64Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64Value.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### setOffset(Int64Value.Builder builderForValue)
    
    
    public AppendRowsRequest.Builder setOffset(Int64Value.Builder builderForValue)

If present, the write is only performed if the next append offset is same as the provided value. If not present, the write is performed at the current end of stream. Specifying a value for this field is not allowed when calling AppendRows for the '_default' stream.

`.google.protobuf.Int64Value offset = 2;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64Value.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### setProtoRows(AppendRowsRequest.ProtoData value)
    
    
    public AppendRowsRequest.Builder setProtoRows(AppendRowsRequest.ProtoData value)

Rows in proto format.

`.google.cloud.bigquery.storage.v1.AppendRowsRequest.ProtoData proto_rows = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AppendRowsRequest.ProtoData](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.ProtoData)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### setProtoRows(AppendRowsRequest.ProtoData.Builder builderForValue)
    
    
    public AppendRowsRequest.Builder setProtoRows(AppendRowsRequest.ProtoData.Builder builderForValue)

Rows in proto format.

`.google.cloud.bigquery.storage.v1.AppendRowsRequest.ProtoData proto_rows = 4;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[AppendRowsRequest.ProtoData.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.ProtoData.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` |   
  
### setTraceId(String value)
    
    
    public AppendRowsRequest.Builder setTraceId(String value)

Id set by client to annotate its identity. Only initial request setting is respected.

`string trace_id = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The traceId to set.  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` | This builder for chaining.  
  
### setTraceIdBytes(ByteString value)
    
    
    public AppendRowsRequest.Builder setTraceIdBytes(ByteString value)

Id set by client to annotate its identity. Only initial request setting is respected.

`string trace_id = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for traceId to set.  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` | This builder for chaining.  
  
### setWriteStream(String value)
    
    
    public AppendRowsRequest.Builder setWriteStream(String value)

Required. The write_stream identifies the append operation. It must be provided in the following scenarios:

  * In the first request to an AppendRows connection.

  * In all subsequent requests to an AppendRows connection, if you use the same connection to write to multiple tables or change the input schema for default streams.

For explicitly created write streams, the format is:

  * `projects/{project}/datasets/{dataset}/tables/{table}/streams/{id}`

For the special default stream, the format is:

  * `projects/{project}/datasets/{dataset}/tables/{table}/streams/_default`.

An example of a possible sequence of requests with write_stream fields within a single connection:

  * r1: {write_stream: stream_name_1}

  * r2: {write_stream: /*omit*/}

  * r3: {write_stream: /*omit*/}

  * r4: {write_stream: stream_name_2}

  * r5: {write_stream: stream_name_2}

The destination changed in request_4, so the write_stream field must be populated in all subsequent requests in this stream.




` string write_stream = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The writeStream to set.  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` | This builder for chaining.  
  
### setWriteStreamBytes(ByteString value)
    
    
    public AppendRowsRequest.Builder setWriteStreamBytes(ByteString value)

Required. The write_stream identifies the append operation. It must be provided in the following scenarios:

  * In the first request to an AppendRows connection.

  * In all subsequent requests to an AppendRows connection, if you use the same connection to write to multiple tables or change the input schema for default streams.

For explicitly created write streams, the format is:

  * `projects/{project}/datasets/{dataset}/tables/{table}/streams/{id}`

For the special default stream, the format is:

  * `projects/{project}/datasets/{dataset}/tables/{table}/streams/_default`.

An example of a possible sequence of requests with write_stream fields within a single connection:

  * r1: {write_stream: stream_name_1}

  * r2: {write_stream: /*omit*/}

  * r3: {write_stream: /*omit*/}

  * r4: {write_stream: stream_name_2}

  * r5: {write_stream: stream_name_2}

The destination changed in request_4, so the write_stream field must be populated in all subsequent requests in this stream.




` string write_stream = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for writeStream to set.  
**Returns**  
---  
**Type** | **Description**  
`[AppendRowsRequest.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.AppendRowsRequest.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
