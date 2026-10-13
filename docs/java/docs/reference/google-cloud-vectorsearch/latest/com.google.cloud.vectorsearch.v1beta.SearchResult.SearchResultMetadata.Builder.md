---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.Builder
title: Class SearchResult.SearchResultMetadata.Builder (0.21.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:54.810554+00:00
---

# Class SearchResult.SearchResultMetadata.Builder (0.21.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SearchResult.SearchResultMetadata.Builder (0.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.21.0 (latest)  0.17.0  0.16.0  0.15.0  0.12.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.1.0 
    
    
    public static final class SearchResult.SearchResultMetadata.Builder extends GeneratedMessage.Builder<SearchResult.SearchResultMetadata.Builder> implements SearchResult.SearchResultMetadataOrBuilder

Quality signals describing how this result was retrieved, combined and re-ranked. Only populated when BatchSearchDataObjectsRequest.BatchSearchMetadataOptions.search_signals_enabled is `true`.

Protobuf type `google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > SearchResult.SearchResultMetadata.Builder

## Implements

[SearchResult.SearchResultMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadataOrBuilder)

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

### addAllSearchDistances(Iterable<? extends SearchResult.SearchResultMetadata.SearchDistance> values)
    
    
    public SearchResult.SearchResultMetadata.Builder addAllSearchDistances(Iterable<? extends SearchResult.SearchResultMetadata.SearchDistance> values)

Output only. The per-search distances for this data object, one entry per batch search that returned it.

` repeated .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance search_distances = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance>`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.Builder)` |   
  
### addSearchDistances(SearchResult.SearchResultMetadata.SearchDistance value)
    
    
    public SearchResult.SearchResultMetadata.Builder addSearchDistances(SearchResult.SearchResultMetadata.SearchDistance value)

Output only. The per-search distances for this data object, one entry per batch search that returned it.

` repeated .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance search_distances = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SearchResult.SearchResultMetadata.SearchDistance](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.Builder)` |   
  
### addSearchDistances(SearchResult.SearchResultMetadata.SearchDistance.Builder builderForValue)
    
    
    public SearchResult.SearchResultMetadata.Builder addSearchDistances(SearchResult.SearchResultMetadata.SearchDistance.Builder builderForValue)

Output only. The per-search distances for this data object, one entry per batch search that returned it.

` repeated .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance search_distances = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SearchResult.SearchResultMetadata.SearchDistance.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.Builder)` |   
  
### addSearchDistances(int index, SearchResult.SearchResultMetadata.SearchDistance value)
    
    
    public SearchResult.SearchResultMetadata.Builder addSearchDistances(int index, SearchResult.SearchResultMetadata.SearchDistance value)

Output only. The per-search distances for this data object, one entry per batch search that returned it.

` repeated .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance search_distances = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[SearchResult.SearchResultMetadata.SearchDistance](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.Builder)` |   
  
### addSearchDistances(int index, SearchResult.SearchResultMetadata.SearchDistance.Builder builderForValue)
    
    
    public SearchResult.SearchResultMetadata.Builder addSearchDistances(int index, SearchResult.SearchResultMetadata.SearchDistance.Builder builderForValue)

Output only. The per-search distances for this data object, one entry per batch search that returned it.

` repeated .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance search_distances = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[SearchResult.SearchResultMetadata.SearchDistance.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.Builder)` |   
  
### addSearchDistancesBuilder()
    
    
    public SearchResult.SearchResultMetadata.SearchDistance.Builder addSearchDistancesBuilder()

Output only. The per-search distances for this data object, one entry per batch search that returned it.

` repeated .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance search_distances = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.SearchDistance.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance.Builder)` |   
  
### addSearchDistancesBuilder(int index)
    
    
    public SearchResult.SearchResultMetadata.SearchDistance.Builder addSearchDistancesBuilder(int index)

Output only. The per-search distances for this data object, one entry per batch search that returned it.

` repeated .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance search_distances = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.SearchDistance.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance.Builder)` |   
  
### build()
    
    
    public SearchResult.SearchResultMetadata build()

**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata)` |   
  
### buildPartial()
    
    
    public SearchResult.SearchResultMetadata buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata)` |   
  
### clear()
    
    
    public SearchResult.SearchResultMetadata.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearRrfRankerResult()
    
    
    public SearchResult.SearchResultMetadata.Builder clearRrfRankerResult()

Output only. The RRF combination signals for this data object. Only set when the request combines results using RRF.

` .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.RrfRankerResult rrf_ranker_result = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.Builder)` |   
  
### clearSearchDistances()
    
    
    public SearchResult.SearchResultMetadata.Builder clearSearchDistances()

Output only. The per-search distances for this data object, one entry per batch search that returned it.

` repeated .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance search_distances = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.Builder)` |   
  
### clearVertexRankerResult()
    
    
    public SearchResult.SearchResultMetadata.Builder clearVertexRankerResult()

Output only. The Vertex re-ranking signals for this data object. Only set when the request re-ranks results using the Vertex ranker.

` .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.VertexRankerResult vertex_ranker_result = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.Builder)` |   
  
### getDefaultInstanceForType()
    
    
    public SearchResult.SearchResultMetadata getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getRrfRankerResult()
    
    
    public SearchResult.SearchResultMetadata.RrfRankerResult getRrfRankerResult()

Output only. The RRF combination signals for this data object. Only set when the request combines results using RRF.

` .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.RrfRankerResult rrf_ranker_result = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.RrfRankerResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.RrfRankerResult)` | The rrfRankerResult.  
  
### getRrfRankerResultBuilder()
    
    
    public SearchResult.SearchResultMetadata.RrfRankerResult.Builder getRrfRankerResultBuilder()

Output only. The RRF combination signals for this data object. Only set when the request combines results using RRF.

` .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.RrfRankerResult rrf_ranker_result = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.RrfRankerResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.RrfRankerResult.Builder)` |   
  
### getRrfRankerResultOrBuilder()
    
    
    public SearchResult.SearchResultMetadata.RrfRankerResultOrBuilder getRrfRankerResultOrBuilder()

Output only. The RRF combination signals for this data object. Only set when the request combines results using RRF.

` .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.RrfRankerResult rrf_ranker_result = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.RrfRankerResultOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.RrfRankerResultOrBuilder)` |   
  
### getSearchDistances(int index)
    
    
    public SearchResult.SearchResultMetadata.SearchDistance getSearchDistances(int index)

Output only. The per-search distances for this data object, one entry per batch search that returned it.

` repeated .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance search_distances = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.SearchDistance](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance)` |   
  
### getSearchDistancesBuilder(int index)
    
    
    public SearchResult.SearchResultMetadata.SearchDistance.Builder getSearchDistancesBuilder(int index)

Output only. The per-search distances for this data object, one entry per batch search that returned it.

` repeated .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance search_distances = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.SearchDistance.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance.Builder)` |   
  
### getSearchDistancesBuilderList()
    
    
    public List<SearchResult.SearchResultMetadata.SearchDistance.Builder> getSearchDistancesBuilderList()

Output only. The per-search distances for this data object, one entry per batch search that returned it.

` repeated .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance search_distances = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance.Builder)>` |   
  
### getSearchDistancesCount()
    
    
    public int getSearchDistancesCount()

Output only. The per-search distances for this data object, one entry per batch search that returned it.

` repeated .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance search_distances = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSearchDistancesList()
    
    
    public List<SearchResult.SearchResultMetadata.SearchDistance> getSearchDistancesList()

Output only. The per-search distances for this data object, one entry per batch search that returned it.

` repeated .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance search_distances = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SearchDistance](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance)>` |   
  
### getSearchDistancesOrBuilder(int index)
    
    
    public SearchResult.SearchResultMetadata.SearchDistanceOrBuilder getSearchDistancesOrBuilder(int index)

Output only. The per-search distances for this data object, one entry per batch search that returned it.

` repeated .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance search_distances = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.SearchDistanceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistanceOrBuilder)` |   
  
### getSearchDistancesOrBuilderList()
    
    
    public List<? extends SearchResult.SearchResultMetadata.SearchDistanceOrBuilder> getSearchDistancesOrBuilderList()

Output only. The per-search distances for this data object, one entry per batch search that returned it.

` repeated .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance search_distances = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistanceOrBuilder>` |   
  
### getVertexRankerResult()
    
    
    public SearchResult.SearchResultMetadata.VertexRankerResult getVertexRankerResult()

Output only. The Vertex re-ranking signals for this data object. Only set when the request re-ranks results using the Vertex ranker.

` .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.VertexRankerResult vertex_ranker_result = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.VertexRankerResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.VertexRankerResult)` | The vertexRankerResult.  
  
### getVertexRankerResultBuilder()
    
    
    public SearchResult.SearchResultMetadata.VertexRankerResult.Builder getVertexRankerResultBuilder()

Output only. The Vertex re-ranking signals for this data object. Only set when the request re-ranks results using the Vertex ranker.

` .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.VertexRankerResult vertex_ranker_result = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.VertexRankerResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.VertexRankerResult.Builder)` |   
  
### getVertexRankerResultOrBuilder()
    
    
    public SearchResult.SearchResultMetadata.VertexRankerResultOrBuilder getVertexRankerResultOrBuilder()

Output only. The Vertex re-ranking signals for this data object. Only set when the request re-ranks results using the Vertex ranker.

` .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.VertexRankerResult vertex_ranker_result = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.VertexRankerResultOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.VertexRankerResultOrBuilder)` |   
  
### hasRrfRankerResult()
    
    
    public boolean hasRrfRankerResult()

Output only. The RRF combination signals for this data object. Only set when the request combines results using RRF.

` .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.RrfRankerResult rrf_ranker_result = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rrfRankerResult field is set.  
  
### hasVertexRankerResult()
    
    
    public boolean hasVertexRankerResult()

Output only. The Vertex re-ranking signals for this data object. Only set when the request re-ranks results using the Vertex ranker.

` .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.VertexRankerResult vertex_ranker_result = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the vertexRankerResult field is set.  
  
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

### mergeFrom(SearchResult.SearchResultMetadata other)
    
    
    public SearchResult.SearchResultMetadata.Builder mergeFrom(SearchResult.SearchResultMetadata other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SearchResult.SearchResultMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public SearchResult.SearchResultMetadata.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public SearchResult.SearchResultMetadata.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeRrfRankerResult(SearchResult.SearchResultMetadata.RrfRankerResult value)
    
    
    public SearchResult.SearchResultMetadata.Builder mergeRrfRankerResult(SearchResult.SearchResultMetadata.RrfRankerResult value)

Output only. The RRF combination signals for this data object. Only set when the request combines results using RRF.

` .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.RrfRankerResult rrf_ranker_result = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SearchResult.SearchResultMetadata.RrfRankerResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.RrfRankerResult)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.Builder)` |   
  
### mergeVertexRankerResult(SearchResult.SearchResultMetadata.VertexRankerResult value)
    
    
    public SearchResult.SearchResultMetadata.Builder mergeVertexRankerResult(SearchResult.SearchResultMetadata.VertexRankerResult value)

Output only. The Vertex re-ranking signals for this data object. Only set when the request re-ranks results using the Vertex ranker.

` .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.VertexRankerResult vertex_ranker_result = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SearchResult.SearchResultMetadata.VertexRankerResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.VertexRankerResult)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.Builder)` |   
  
### removeSearchDistances(int index)
    
    
    public SearchResult.SearchResultMetadata.Builder removeSearchDistances(int index)

Output only. The per-search distances for this data object, one entry per batch search that returned it.

` repeated .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance search_distances = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.Builder)` |   
  
### setRrfRankerResult(SearchResult.SearchResultMetadata.RrfRankerResult value)
    
    
    public SearchResult.SearchResultMetadata.Builder setRrfRankerResult(SearchResult.SearchResultMetadata.RrfRankerResult value)

Output only. The RRF combination signals for this data object. Only set when the request combines results using RRF.

` .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.RrfRankerResult rrf_ranker_result = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SearchResult.SearchResultMetadata.RrfRankerResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.RrfRankerResult)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.Builder)` |   
  
### setRrfRankerResult(SearchResult.SearchResultMetadata.RrfRankerResult.Builder builderForValue)
    
    
    public SearchResult.SearchResultMetadata.Builder setRrfRankerResult(SearchResult.SearchResultMetadata.RrfRankerResult.Builder builderForValue)

Output only. The RRF combination signals for this data object. Only set when the request combines results using RRF.

` .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.RrfRankerResult rrf_ranker_result = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SearchResult.SearchResultMetadata.RrfRankerResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.RrfRankerResult.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.Builder)` |   
  
### setSearchDistances(int index, SearchResult.SearchResultMetadata.SearchDistance value)
    
    
    public SearchResult.SearchResultMetadata.Builder setSearchDistances(int index, SearchResult.SearchResultMetadata.SearchDistance value)

Output only. The per-search distances for this data object, one entry per batch search that returned it.

` repeated .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance search_distances = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[SearchResult.SearchResultMetadata.SearchDistance](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.Builder)` |   
  
### setSearchDistances(int index, SearchResult.SearchResultMetadata.SearchDistance.Builder builderForValue)
    
    
    public SearchResult.SearchResultMetadata.Builder setSearchDistances(int index, SearchResult.SearchResultMetadata.SearchDistance.Builder builderForValue)

Output only. The per-search distances for this data object, one entry per batch search that returned it.

` repeated .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance search_distances = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[SearchResult.SearchResultMetadata.SearchDistance.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.SearchDistance.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.Builder)` |   
  
### setVertexRankerResult(SearchResult.SearchResultMetadata.VertexRankerResult value)
    
    
    public SearchResult.SearchResultMetadata.Builder setVertexRankerResult(SearchResult.SearchResultMetadata.VertexRankerResult value)

Output only. The Vertex re-ranking signals for this data object. Only set when the request re-ranks results using the Vertex ranker.

` .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.VertexRankerResult vertex_ranker_result = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SearchResult.SearchResultMetadata.VertexRankerResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.VertexRankerResult)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.Builder)` |   
  
### setVertexRankerResult(SearchResult.SearchResultMetadata.VertexRankerResult.Builder builderForValue)
    
    
    public SearchResult.SearchResultMetadata.Builder setVertexRankerResult(SearchResult.SearchResultMetadata.VertexRankerResult.Builder builderForValue)

Output only. The Vertex re-ranking signals for this data object. Only set when the request re-ranks results using the Vertex ranker.

` .google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.VertexRankerResult vertex_ranker_result = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SearchResult.SearchResultMetadata.VertexRankerResult.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.VertexRankerResult.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchResult.SearchResultMetadata.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vectorsearch/latest/com.google.cloud.vectorsearch.v1beta.SearchResult.SearchResultMetadata.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
