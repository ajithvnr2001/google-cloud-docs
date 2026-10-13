---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder
title: Class ApiOperation.Builder (0.52.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:35:10.305961+00:00
---

# Class ApiOperation.Builder (0.52.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ApiOperation.Builder (0.52.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.52.0 (latest)  0.48.0  0.47.0  0.46.0  0.44.0  0.41.0  0.40.0  0.38.0  0.36.0  0.35.0  0.34.0  0.33.0  0.31.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.23.0  0.21.0  0.20.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.2.0  0.1.0 
    
    
    public static final class ApiOperation.Builder extends GeneratedMessage.Builder<ApiOperation.Builder> implements ApiOperationOrBuilder

Represents an operation contained in an API version in the API Hub. An operation is added/updated/deleted in an API version when a new spec is added or an existing spec is updated/deleted in a version. Currently, an operation will be created only corresponding to OpenAPI spec as parsing is supported for OpenAPI spec. Alternatively operations can be managed via create,update and delete APIs, creation of apiOperation can be possible only for version with no parsed operations and update/delete can be possible only for operations created via create API.

Protobuf type `google.cloud.apihub.v1.ApiOperation`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > ApiOperation.Builder

## Implements

[ApiOperationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperationOrBuilder)

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

### addAllSourceMetadata(Iterable<? extends SourceMetadata> values)
    
    
    public ApiOperation.Builder addAllSourceMetadata(Iterable<? extends SourceMetadata> values)

Output only. The list of sources and metadata from the sources of the API operation.

` repeated .google.cloud.apihub.v1.SourceMetadata source_metadata = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.apihub.v1.SourceMetadata>`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### addSourceMetadata(SourceMetadata value)
    
    
    public ApiOperation.Builder addSourceMetadata(SourceMetadata value)

Output only. The list of sources and metadata from the sources of the API operation.

` repeated .google.cloud.apihub.v1.SourceMetadata source_metadata = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SourceMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.SourceMetadata)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### addSourceMetadata(SourceMetadata.Builder builderForValue)
    
    
    public ApiOperation.Builder addSourceMetadata(SourceMetadata.Builder builderForValue)

Output only. The list of sources and metadata from the sources of the API operation.

` repeated .google.cloud.apihub.v1.SourceMetadata source_metadata = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SourceMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.SourceMetadata.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### addSourceMetadata(int index, SourceMetadata value)
    
    
    public ApiOperation.Builder addSourceMetadata(int index, SourceMetadata value)

Output only. The list of sources and metadata from the sources of the API operation.

` repeated .google.cloud.apihub.v1.SourceMetadata source_metadata = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[SourceMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.SourceMetadata)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### addSourceMetadata(int index, SourceMetadata.Builder builderForValue)
    
    
    public ApiOperation.Builder addSourceMetadata(int index, SourceMetadata.Builder builderForValue)

Output only. The list of sources and metadata from the sources of the API operation.

` repeated .google.cloud.apihub.v1.SourceMetadata source_metadata = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[SourceMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.SourceMetadata.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### addSourceMetadataBuilder()
    
    
    public SourceMetadata.Builder addSourceMetadataBuilder()

Output only. The list of sources and metadata from the sources of the API operation.

` repeated .google.cloud.apihub.v1.SourceMetadata source_metadata = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SourceMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.SourceMetadata.Builder)` |   
  
### addSourceMetadataBuilder(int index)
    
    
    public SourceMetadata.Builder addSourceMetadataBuilder(int index)

Output only. The list of sources and metadata from the sources of the API operation.

` repeated .google.cloud.apihub.v1.SourceMetadata source_metadata = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SourceMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.SourceMetadata.Builder)` |   
  
### build()
    
    
    public ApiOperation build()

**Returns**  
---  
**Type** | **Description**  
`[ApiOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation)` |   
  
### buildPartial()
    
    
    public ApiOperation buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[ApiOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation)` |   
  
### clear()
    
    
    public ApiOperation.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearAttributes()
    
    
    public ApiOperation.Builder clearAttributes()

**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### clearCreateTime()
    
    
    public ApiOperation.Builder clearCreateTime()

Output only. The time at which the operation was created.

` .google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### clearDetails()
    
    
    public ApiOperation.Builder clearDetails()

Optional. Operation details. Note: Even though this field is optional, it is required for CreateApiOperation API and we will fail the request if not provided.

` .google.cloud.apihub.v1.OperationDetails details = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### clearName()
    
    
    public ApiOperation.Builder clearName()

Identifier. The name of the operation.

Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/operations/{operation}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` | This builder for chaining.  
  
### clearSourceMetadata()
    
    
    public ApiOperation.Builder clearSourceMetadata()

Output only. The list of sources and metadata from the sources of the API operation.

` repeated .google.cloud.apihub.v1.SourceMetadata source_metadata = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### clearSpec()
    
    
    public ApiOperation.Builder clearSpec()

Output only. The name of the spec will be of the format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}` Note:The name of the spec will be empty if the operation is created via CreateApiOperation API.

` string spec = 2 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` | This builder for chaining.  
  
### clearUpdateTime()
    
    
    public ApiOperation.Builder clearUpdateTime()

Output only. The time at which the operation was last updated.

` .google.protobuf.Timestamp update_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### containsAttributes(String key)
    
    
    public boolean containsAttributes(String key)

Optional. The list of user defined attributes associated with the API operation resource. The key is the attribute name. It will be of the format: `projects/{project}/locations/{location}/attributes/{attribute}`. The value is the attribute values associated with the resource.

` map<string, .google.cloud.apihub.v1.AttributeValues> attributes = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAttributes() (deprecated)
    
    
    public Map<String,AttributeValues> getAttributes()

Use [#getAttributesMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder#com_google_cloud_apihub_v1_ApiOperation_Builder_getAttributesMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[AttributeValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.AttributeValues)>` |   
  
### getAttributesCount()
    
    
    public int getAttributesCount()

Optional. The list of user defined attributes associated with the API operation resource. The key is the attribute name. It will be of the format: `projects/{project}/locations/{location}/attributes/{attribute}`. The value is the attribute values associated with the resource.

` map<string, .google.cloud.apihub.v1.AttributeValues> attributes = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAttributesMap()
    
    
    public Map<String,AttributeValues> getAttributesMap()

Optional. The list of user defined attributes associated with the API operation resource. The key is the attribute name. It will be of the format: `projects/{project}/locations/{location}/attributes/{attribute}`. The value is the attribute values associated with the resource.

` map<string, .google.cloud.apihub.v1.AttributeValues> attributes = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[AttributeValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.AttributeValues)>` |   
  
### getAttributesOrDefault(String key, AttributeValues defaultValue)
    
    
    public AttributeValues getAttributesOrDefault(String key, AttributeValues defaultValue)

Optional. The list of user defined attributes associated with the API operation resource. The key is the attribute name. It will be of the format: `projects/{project}/locations/{location}/attributes/{attribute}`. The value is the attribute values associated with the resource.

` map<string, .google.cloud.apihub.v1.AttributeValues> attributes = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[AttributeValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.AttributeValues)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AttributeValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.AttributeValues)` |   
  
### getAttributesOrThrow(String key)
    
    
    public AttributeValues getAttributesOrThrow(String key)

Optional. The list of user defined attributes associated with the API operation resource. The key is the attribute name. It will be of the format: `projects/{project}/locations/{location}/attributes/{attribute}`. The value is the attribute values associated with the resource.

` map<string, .google.cloud.apihub.v1.AttributeValues> attributes = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AttributeValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.AttributeValues)` |   
  
### getCreateTime()
    
    
    public Timestamp getCreateTime()

Output only. The time at which the operation was created.

` .google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeBuilder()
    
    
    public Timestamp.Builder getCreateTimeBuilder()

Output only. The time at which the operation was created.

` .google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getCreateTimeOrBuilder()
    
    
    public TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The time at which the operation was created.

` .google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDefaultInstanceForType()
    
    
    public ApiOperation getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[ApiOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getDetails()
    
    
    public OperationDetails getDetails()

Optional. Operation details. Note: Even though this field is optional, it is required for CreateApiOperation API and we will fail the request if not provided.

` .google.cloud.apihub.v1.OperationDetails details = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[OperationDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationDetails)` | The details.  
  
### getDetailsBuilder()
    
    
    public OperationDetails.Builder getDetailsBuilder()

Optional. Operation details. Note: Even though this field is optional, it is required for CreateApiOperation API and we will fail the request if not provided.

` .google.cloud.apihub.v1.OperationDetails details = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[OperationDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationDetails.Builder)` |   
  
### getDetailsOrBuilder()
    
    
    public OperationDetailsOrBuilder getDetailsOrBuilder()

Optional. Operation details. Note: Even though this field is optional, it is required for CreateApiOperation API and we will fail the request if not provided.

` .google.cloud.apihub.v1.OperationDetails details = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[OperationDetailsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationDetailsOrBuilder)` |   
  
### getMutableAttributes() (deprecated)
    
    
    public Map<String,AttributeValues> getMutableAttributes()

Use alternate mutation accessors instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[AttributeValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.AttributeValues)>` |   
  
### getName()
    
    
    public String getName()

Identifier. The name of the operation.

Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/operations/{operation}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

Identifier. The name of the operation.

Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/operations/{operation}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getSourceMetadata(int index)
    
    
    public SourceMetadata getSourceMetadata(int index)

Output only. The list of sources and metadata from the sources of the API operation.

` repeated .google.cloud.apihub.v1.SourceMetadata source_metadata = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SourceMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.SourceMetadata)` |   
  
### getSourceMetadataBuilder(int index)
    
    
    public SourceMetadata.Builder getSourceMetadataBuilder(int index)

Output only. The list of sources and metadata from the sources of the API operation.

` repeated .google.cloud.apihub.v1.SourceMetadata source_metadata = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SourceMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.SourceMetadata.Builder)` |   
  
### getSourceMetadataBuilderList()
    
    
    public List<SourceMetadata.Builder> getSourceMetadataBuilderList()

Output only. The list of sources and metadata from the sources of the API operation.

` repeated .google.cloud.apihub.v1.SourceMetadata source_metadata = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.SourceMetadata.Builder)>` |   
  
### getSourceMetadataCount()
    
    
    public int getSourceMetadataCount()

Output only. The list of sources and metadata from the sources of the API operation.

` repeated .google.cloud.apihub.v1.SourceMetadata source_metadata = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSourceMetadataList()
    
    
    public List<SourceMetadata> getSourceMetadataList()

Output only. The list of sources and metadata from the sources of the API operation.

` repeated .google.cloud.apihub.v1.SourceMetadata source_metadata = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SourceMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.SourceMetadata)>` |   
  
### getSourceMetadataOrBuilder(int index)
    
    
    public SourceMetadataOrBuilder getSourceMetadataOrBuilder(int index)

Output only. The list of sources and metadata from the sources of the API operation.

` repeated .google.cloud.apihub.v1.SourceMetadata source_metadata = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SourceMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.SourceMetadataOrBuilder)` |   
  
### getSourceMetadataOrBuilderList()
    
    
    public List<? extends SourceMetadataOrBuilder> getSourceMetadataOrBuilderList()

Output only. The list of sources and metadata from the sources of the API operation.

` repeated .google.cloud.apihub.v1.SourceMetadata source_metadata = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.apihub.v1.SourceMetadataOrBuilder>` |   
  
### getSpec()
    
    
    public String getSpec()

Output only. The name of the spec will be of the format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}` Note:The name of the spec will be empty if the operation is created via CreateApiOperation API.

` string spec = 2 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The spec.  
  
### getSpecBytes()
    
    
    public ByteString getSpecBytes()

Output only. The name of the spec will be of the format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}` Note:The name of the spec will be empty if the operation is created via CreateApiOperation API.

` string spec = 2 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for spec.  
  
### getUpdateTime()
    
    
    public Timestamp getUpdateTime()

Output only. The time at which the operation was last updated.

` .google.protobuf.Timestamp update_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeBuilder()
    
    
    public Timestamp.Builder getUpdateTimeBuilder()

Output only. The time at which the operation was last updated.

` .google.protobuf.Timestamp update_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getUpdateTimeOrBuilder()
    
    
    public TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The time at which the operation was last updated.

` .google.protobuf.Timestamp update_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCreateTime()
    
    
    public boolean hasCreateTime()

Output only. The time at which the operation was created.

` .google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasDetails()
    
    
    public boolean hasDetails()

Optional. Operation details. Note: Even though this field is optional, it is required for CreateApiOperation API and we will fail the request if not provided.

` .google.cloud.apihub.v1.OperationDetails details = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the details field is set.  
  
### hasUpdateTime()
    
    
    public boolean hasUpdateTime()

Output only. The time at which the operation was last updated.

` .google.protobuf.Timestamp update_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
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

### mergeCreateTime(Timestamp value)
    
    
    public ApiOperation.Builder mergeCreateTime(Timestamp value)

Output only. The time at which the operation was created.

` .google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### mergeDetails(OperationDetails value)
    
    
    public ApiOperation.Builder mergeDetails(OperationDetails value)

Optional. Operation details. Note: Even though this field is optional, it is required for CreateApiOperation API and we will fail the request if not provided.

` .google.cloud.apihub.v1.OperationDetails details = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[OperationDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationDetails)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### mergeFrom(ApiOperation other)
    
    
    public ApiOperation.Builder mergeFrom(ApiOperation other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ApiOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public ApiOperation.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public ApiOperation.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeUpdateTime(Timestamp value)
    
    
    public ApiOperation.Builder mergeUpdateTime(Timestamp value)

Output only. The time at which the operation was last updated.

` .google.protobuf.Timestamp update_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### putAllAttributes(Map<String,AttributeValues> values)
    
    
    public ApiOperation.Builder putAllAttributes(Map<String,AttributeValues> values)

Optional. The list of user defined attributes associated with the API operation resource. The key is the attribute name. It will be of the format: `projects/{project}/locations/{location}/attributes/{attribute}`. The value is the attribute values associated with the resource.

` map<string, .google.cloud.apihub.v1.AttributeValues> attributes = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[AttributeValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.AttributeValues)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### putAttributes(String key, AttributeValues value)
    
    
    public ApiOperation.Builder putAttributes(String key, AttributeValues value)

Optional. The list of user defined attributes associated with the API operation resource. The key is the attribute name. It will be of the format: `projects/{project}/locations/{location}/attributes/{attribute}`. The value is the attribute values associated with the resource.

` map<string, .google.cloud.apihub.v1.AttributeValues> attributes = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[AttributeValues](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.AttributeValues)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### putAttributesBuilderIfAbsent(String key)
    
    
    public AttributeValues.Builder putAttributesBuilderIfAbsent(String key)

Optional. The list of user defined attributes associated with the API operation resource. The key is the attribute name. It will be of the format: `projects/{project}/locations/{location}/attributes/{attribute}`. The value is the attribute values associated with the resource.

` map<string, .google.cloud.apihub.v1.AttributeValues> attributes = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AttributeValues.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.AttributeValues.Builder)` |   
  
### removeAttributes(String key)
    
    
    public ApiOperation.Builder removeAttributes(String key)

Optional. The list of user defined attributes associated with the API operation resource. The key is the attribute name. It will be of the format: `projects/{project}/locations/{location}/attributes/{attribute}`. The value is the attribute values associated with the resource.

` map<string, .google.cloud.apihub.v1.AttributeValues> attributes = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### removeSourceMetadata(int index)
    
    
    public ApiOperation.Builder removeSourceMetadata(int index)

Output only. The list of sources and metadata from the sources of the API operation.

` repeated .google.cloud.apihub.v1.SourceMetadata source_metadata = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### setCreateTime(Timestamp value)
    
    
    public ApiOperation.Builder setCreateTime(Timestamp value)

Output only. The time at which the operation was created.

` .google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### setCreateTime(Timestamp.Builder builderForValue)
    
    
    public ApiOperation.Builder setCreateTime(Timestamp.Builder builderForValue)

Output only. The time at which the operation was created.

` .google.protobuf.Timestamp create_time = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### setDetails(OperationDetails value)
    
    
    public ApiOperation.Builder setDetails(OperationDetails value)

Optional. Operation details. Note: Even though this field is optional, it is required for CreateApiOperation API and we will fail the request if not provided.

` .google.cloud.apihub.v1.OperationDetails details = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[OperationDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationDetails)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### setDetails(OperationDetails.Builder builderForValue)
    
    
    public ApiOperation.Builder setDetails(OperationDetails.Builder builderForValue)

Optional. Operation details. Note: Even though this field is optional, it is required for CreateApiOperation API and we will fail the request if not provided.

` .google.cloud.apihub.v1.OperationDetails details = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[OperationDetails.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.OperationDetails.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### setName(String value)
    
    
    public ApiOperation.Builder setName(String value)

Identifier. The name of the operation.

Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/operations/{operation}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public ApiOperation.Builder setNameBytes(ByteString value)

Identifier. The name of the operation.

Format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/operations/{operation}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` | This builder for chaining.  
  
### setSourceMetadata(int index, SourceMetadata value)
    
    
    public ApiOperation.Builder setSourceMetadata(int index, SourceMetadata value)

Output only. The list of sources and metadata from the sources of the API operation.

` repeated .google.cloud.apihub.v1.SourceMetadata source_metadata = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[SourceMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.SourceMetadata)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### setSourceMetadata(int index, SourceMetadata.Builder builderForValue)
    
    
    public ApiOperation.Builder setSourceMetadata(int index, SourceMetadata.Builder builderForValue)

Output only. The list of sources and metadata from the sources of the API operation.

` repeated .google.cloud.apihub.v1.SourceMetadata source_metadata = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[SourceMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.SourceMetadata.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### setSpec(String value)
    
    
    public ApiOperation.Builder setSpec(String value)

Output only. The name of the spec will be of the format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}` Note:The name of the spec will be empty if the operation is created via CreateApiOperation API.

` string spec = 2 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The spec to set.  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` | This builder for chaining.  
  
### setSpecBytes(ByteString value)
    
    
    public ApiOperation.Builder setSpecBytes(ByteString value)

Output only. The name of the spec will be of the format: `projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}` Note:The name of the spec will be empty if the operation is created via CreateApiOperation API.

` string spec = 2 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for spec to set.  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` | This builder for chaining.  
  
### setUpdateTime(Timestamp value)
    
    
    public ApiOperation.Builder setUpdateTime(Timestamp value)

Output only. The time at which the operation was last updated.

` .google.protobuf.Timestamp update_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
### setUpdateTime(Timestamp.Builder builderForValue)
    
    
    public ApiOperation.Builder setUpdateTime(Timestamp.Builder builderForValue)

Output only. The time at which the operation was last updated.

` .google.protobuf.Timestamp update_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiOperation.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-apihub/latest/com.google.cloud.apihub.v1.ApiOperation.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
