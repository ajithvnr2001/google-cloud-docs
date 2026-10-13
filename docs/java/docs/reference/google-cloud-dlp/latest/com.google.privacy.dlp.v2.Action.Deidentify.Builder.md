---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder
title: Class Action.Deidentify.Builder (3.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:59.163061+00:00
---

# Class Action.Deidentify.Builder (3.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Action.Deidentify.Builder (3.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.103.0 (latest)  3.99.0  3.98.0  3.97.0  3.95.0  3.92.0  3.91.0  3.89.0  3.87.0  3.86.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.78.0  3.77.0  3.76.0  3.74.0  3.72.0  3.71.0  3.68.0  3.67.0  3.66.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.6  3.6.7  3.5.0  3.4.0  3.3.2  3.2.1  3.1.4 
    
    
    public static final class Action.Deidentify.Builder extends GeneratedMessage.Builder<Action.Deidentify.Builder> implements Action.DeidentifyOrBuilder

Create a de-identified copy of a storage bucket. Only compatible with Cloud Storage buckets.

A TransformationDetail will be created for each transformation.

Compatible with: Inspection of Cloud Storage

Protobuf type `google.privacy.dlp.v2.Action.Deidentify`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > Action.Deidentify.Builder

## Implements

[Action.DeidentifyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.DeidentifyOrBuilder)

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

### addAllFileTypesToTransform(Iterable<? extends FileType> values)
    
    
    public Action.Deidentify.Builder addAllFileTypesToTransform(Iterable<? extends FileType> values)

List of user-specified file type groups to transform. If specified, only the files with these file types are transformed. If empty, all supported files are transformed. Supported types may be automatically added over time. Any unsupported file types that are set in this field are excluded from de-identification. An error is recorded for each unsupported file in the TransformationDetails output table. Currently the only file types supported are: IMAGES, TEXT_FILES, CSV, TSV.

`repeated .google.privacy.dlp.v2.FileType file_types_to_transform = 8;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.privacy.dlp.v2.FileType>`  
The fileTypesToTransform to add.  
**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder)` | This builder for chaining.  
  
### addAllFileTypesToTransformValue(Iterable<Integer> values)
    
    
    public Action.Deidentify.Builder addAllFileTypesToTransformValue(Iterable<Integer> values)

List of user-specified file type groups to transform. If specified, only the files with these file types are transformed. If empty, all supported files are transformed. Supported types may be automatically added over time. Any unsupported file types that are set in this field are excluded from de-identification. An error is recorded for each unsupported file in the TransformationDetails output table. Currently the only file types supported are: IMAGES, TEXT_FILES, CSV, TSV.

`repeated .google.privacy.dlp.v2.FileType file_types_to_transform = 8;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>`  
The enum numeric values on the wire for fileTypesToTransform to add.  
**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder)` | This builder for chaining.  
  
### addFileTypesToTransform(FileType value)
    
    
    public Action.Deidentify.Builder addFileTypesToTransform(FileType value)

List of user-specified file type groups to transform. If specified, only the files with these file types are transformed. If empty, all supported files are transformed. Supported types may be automatically added over time. Any unsupported file types that are set in this field are excluded from de-identification. An error is recorded for each unsupported file in the TransformationDetails output table. Currently the only file types supported are: IMAGES, TEXT_FILES, CSV, TSV.

`repeated .google.privacy.dlp.v2.FileType file_types_to_transform = 8;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[FileType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FileType)`  
The fileTypesToTransform to add.  
**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder)` | This builder for chaining.  
  
### addFileTypesToTransformValue(int value)
    
    
    public Action.Deidentify.Builder addFileTypesToTransformValue(int value)

List of user-specified file type groups to transform. If specified, only the files with these file types are transformed. If empty, all supported files are transformed. Supported types may be automatically added over time. Any unsupported file types that are set in this field are excluded from de-identification. An error is recorded for each unsupported file in the TransformationDetails output table. Currently the only file types supported are: IMAGES, TEXT_FILES, CSV, TSV.

`repeated .google.privacy.dlp.v2.FileType file_types_to_transform = 8;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for fileTypesToTransform to add.  
**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder)` | This builder for chaining.  
  
### build()
    
    
    public Action.Deidentify build()

**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify)` |   
  
### buildPartial()
    
    
    public Action.Deidentify buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify)` |   
  
### clear()
    
    
    public Action.Deidentify.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearCloudStorageOutput()
    
    
    public Action.Deidentify.Builder clearCloudStorageOutput()

Required. User settable Cloud Storage bucket and folders to store de-identified files. This field must be set for Cloud Storage deidentification. The output Cloud Storage bucket must be different from the input bucket. De-identified files will overwrite files in the output path.

Form of: gs://bucket/folder/ or gs://bucket

`string cloud_storage_output = 9 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder)` | This builder for chaining.  
  
### clearFileTypesToTransform()
    
    
    public Action.Deidentify.Builder clearFileTypesToTransform()

List of user-specified file type groups to transform. If specified, only the files with these file types are transformed. If empty, all supported files are transformed. Supported types may be automatically added over time. Any unsupported file types that are set in this field are excluded from de-identification. An error is recorded for each unsupported file in the TransformationDetails output table. Currently the only file types supported are: IMAGES, TEXT_FILES, CSV, TSV.

`repeated .google.privacy.dlp.v2.FileType file_types_to_transform = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder)` | This builder for chaining.  
  
### clearOutput()
    
    
    public Action.Deidentify.Builder clearOutput()

**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder)` |   
  
### clearTransformationConfig()
    
    
    public Action.Deidentify.Builder clearTransformationConfig()

User specified deidentify templates and configs for structured, unstructured, and image files.

`.google.privacy.dlp.v2.TransformationConfig transformation_config = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder)` |   
  
### clearTransformationDetailsStorageConfig()
    
    
    public Action.Deidentify.Builder clearTransformationDetailsStorageConfig()

Config for storing transformation details.

This field specifies the configuration for storing detailed metadata about each transformation performed during a de-identification process. The metadata is stored separately from the de-identified content itself and provides a granular record of both successful transformations and any failures that occurred.

Enabling this configuration is essential for users who need to access comprehensive information about the status, outcome, and specifics of each transformation. The details are captured in the TransformationDetails message for each operation.

Key use cases:

  * **Auditing and compliance**
  * Provides a verifiable audit trail of de-identification activities, which is crucial for meeting regulatory requirements and internal data governance policies.
  * Logs what data was transformed, what transformations were applied, when they occurred, and their success status. This helps demonstrate accountability and due diligence in protecting sensitive data.

  * **Troubleshooting and debugging**

  * Offers detailed error messages and context if a transformation fails. This information is useful for diagnosing and resolving issues in the de-identification pipeline.
  * Helps pinpoint the exact location and nature of failures, speeding up the debugging process.

  * **Process verification and quality assurance**

  * Allows users to confirm that de-identification rules and transformations were applied correctly and consistently across the dataset as intended.
  * Helps in verifying the effectiveness of the chosen de-identification strategies.

  * **Data lineage and impact analysis**

  * Creates a record of how data elements were modified, contributing to data lineage. This is useful for understanding the provenance of de-identified data.
  * Aids in assessing the potential impact of de-identification choices on downstream analytical processes or data usability.

  * **Reporting and operational insights**

  * You can analyze the metadata stored in a queryable BigQuery table to generate reports on transformation success rates, common error types, processing volumes (e.g., transformedBytes), and the types of transformations applied.
  * These insights can inform optimization of de-identification configurations and resource planning.

To take advantage of these benefits, set this configuration. The stored details include a description of the transformation, success or error codes, error messages, the number of bytes transformed, the location of the transformed content, and identifiers for the job and source data.




` .google.privacy.dlp.v2.TransformationDetailsStorageConfig transformation_details_storage_config = 3; `

**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder)` |   
  
### getCloudStorageOutput()
    
    
    public String getCloudStorageOutput()

Required. User settable Cloud Storage bucket and folders to store de-identified files. This field must be set for Cloud Storage deidentification. The output Cloud Storage bucket must be different from the input bucket. De-identified files will overwrite files in the output path.

Form of: gs://bucket/folder/ or gs://bucket

`string cloud_storage_output = 9 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The cloudStorageOutput.  
  
### getCloudStorageOutputBytes()
    
    
    public ByteString getCloudStorageOutputBytes()

Required. User settable Cloud Storage bucket and folders to store de-identified files. This field must be set for Cloud Storage deidentification. The output Cloud Storage bucket must be different from the input bucket. De-identified files will overwrite files in the output path.

Form of: gs://bucket/folder/ or gs://bucket

`string cloud_storage_output = 9 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for cloudStorageOutput.  
  
### getDefaultInstanceForType()
    
    
    public Action.Deidentify getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getFileTypesToTransform(int index)
    
    
    public FileType getFileTypesToTransform(int index)

List of user-specified file type groups to transform. If specified, only the files with these file types are transformed. If empty, all supported files are transformed. Supported types may be automatically added over time. Any unsupported file types that are set in this field are excluded from de-identification. An error is recorded for each unsupported file in the TransformationDetails output table. Currently the only file types supported are: IMAGES, TEXT_FILES, CSV, TSV.

`repeated .google.privacy.dlp.v2.FileType file_types_to_transform = 8;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[FileType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FileType)` | The fileTypesToTransform at the given index.  
  
### getFileTypesToTransformCount()
    
    
    public int getFileTypesToTransformCount()

List of user-specified file type groups to transform. If specified, only the files with these file types are transformed. If empty, all supported files are transformed. Supported types may be automatically added over time. Any unsupported file types that are set in this field are excluded from de-identification. An error is recorded for each unsupported file in the TransformationDetails output table. Currently the only file types supported are: IMAGES, TEXT_FILES, CSV, TSV.

`repeated .google.privacy.dlp.v2.FileType file_types_to_transform = 8;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of fileTypesToTransform.  
  
### getFileTypesToTransformList()
    
    
    public List<FileType> getFileTypesToTransformList()

List of user-specified file type groups to transform. If specified, only the files with these file types are transformed. If empty, all supported files are transformed. Supported types may be automatically added over time. Any unsupported file types that are set in this field are excluded from de-identification. An error is recorded for each unsupported file in the TransformationDetails output table. Currently the only file types supported are: IMAGES, TEXT_FILES, CSV, TSV.

`repeated .google.privacy.dlp.v2.FileType file_types_to_transform = 8;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[FileType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FileType)>` | A list containing the fileTypesToTransform.  
  
### getFileTypesToTransformValue(int index)
    
    
    public int getFileTypesToTransformValue(int index)

List of user-specified file type groups to transform. If specified, only the files with these file types are transformed. If empty, all supported files are transformed. Supported types may be automatically added over time. Any unsupported file types that are set in this field are excluded from de-identification. An error is recorded for each unsupported file in the TransformationDetails output table. Currently the only file types supported are: IMAGES, TEXT_FILES, CSV, TSV.

`repeated .google.privacy.dlp.v2.FileType file_types_to_transform = 8;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of fileTypesToTransform at the given index.  
  
### getFileTypesToTransformValueList()
    
    
    public List<Integer> getFileTypesToTransformValueList()

List of user-specified file type groups to transform. If specified, only the files with these file types are transformed. If empty, all supported files are transformed. Supported types may be automatically added over time. Any unsupported file types that are set in this field are excluded from de-identification. An error is recorded for each unsupported file in the TransformationDetails output table. Currently the only file types supported are: IMAGES, TEXT_FILES, CSV, TSV.

`repeated .google.privacy.dlp.v2.FileType file_types_to_transform = 8;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for fileTypesToTransform.  
  
### getOutputCase()
    
    
    public Action.Deidentify.OutputCase getOutputCase()

**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.OutputCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.OutputCase)` |   
  
### getTransformationConfig()
    
    
    public TransformationConfig getTransformationConfig()

User specified deidentify templates and configs for structured, unstructured, and image files.

`.google.privacy.dlp.v2.TransformationConfig transformation_config = 7;`

**Returns**  
---  
**Type** | **Description**  
`[TransformationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransformationConfig)` | The transformationConfig.  
  
### getTransformationConfigBuilder()
    
    
    public TransformationConfig.Builder getTransformationConfigBuilder()

User specified deidentify templates and configs for structured, unstructured, and image files.

`.google.privacy.dlp.v2.TransformationConfig transformation_config = 7;`

**Returns**  
---  
**Type** | **Description**  
`[TransformationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransformationConfig.Builder)` |   
  
### getTransformationConfigOrBuilder()
    
    
    public TransformationConfigOrBuilder getTransformationConfigOrBuilder()

User specified deidentify templates and configs for structured, unstructured, and image files.

`.google.privacy.dlp.v2.TransformationConfig transformation_config = 7;`

**Returns**  
---  
**Type** | **Description**  
`[TransformationConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransformationConfigOrBuilder)` |   
  
### getTransformationDetailsStorageConfig()
    
    
    public TransformationDetailsStorageConfig getTransformationDetailsStorageConfig()

Config for storing transformation details.

This field specifies the configuration for storing detailed metadata about each transformation performed during a de-identification process. The metadata is stored separately from the de-identified content itself and provides a granular record of both successful transformations and any failures that occurred.

Enabling this configuration is essential for users who need to access comprehensive information about the status, outcome, and specifics of each transformation. The details are captured in the TransformationDetails message for each operation.

Key use cases:

  * **Auditing and compliance**
  * Provides a verifiable audit trail of de-identification activities, which is crucial for meeting regulatory requirements and internal data governance policies.
  * Logs what data was transformed, what transformations were applied, when they occurred, and their success status. This helps demonstrate accountability and due diligence in protecting sensitive data.

  * **Troubleshooting and debugging**

  * Offers detailed error messages and context if a transformation fails. This information is useful for diagnosing and resolving issues in the de-identification pipeline.
  * Helps pinpoint the exact location and nature of failures, speeding up the debugging process.

  * **Process verification and quality assurance**

  * Allows users to confirm that de-identification rules and transformations were applied correctly and consistently across the dataset as intended.
  * Helps in verifying the effectiveness of the chosen de-identification strategies.

  * **Data lineage and impact analysis**

  * Creates a record of how data elements were modified, contributing to data lineage. This is useful for understanding the provenance of de-identified data.
  * Aids in assessing the potential impact of de-identification choices on downstream analytical processes or data usability.

  * **Reporting and operational insights**

  * You can analyze the metadata stored in a queryable BigQuery table to generate reports on transformation success rates, common error types, processing volumes (e.g., transformedBytes), and the types of transformations applied.
  * These insights can inform optimization of de-identification configurations and resource planning.

To take advantage of these benefits, set this configuration. The stored details include a description of the transformation, success or error codes, error messages, the number of bytes transformed, the location of the transformed content, and identifiers for the job and source data.




` .google.privacy.dlp.v2.TransformationDetailsStorageConfig transformation_details_storage_config = 3; `

**Returns**  
---  
**Type** | **Description**  
`[TransformationDetailsStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransformationDetailsStorageConfig)` | The transformationDetailsStorageConfig.  
  
### getTransformationDetailsStorageConfigBuilder()
    
    
    public TransformationDetailsStorageConfig.Builder getTransformationDetailsStorageConfigBuilder()

Config for storing transformation details.

This field specifies the configuration for storing detailed metadata about each transformation performed during a de-identification process. The metadata is stored separately from the de-identified content itself and provides a granular record of both successful transformations and any failures that occurred.

Enabling this configuration is essential for users who need to access comprehensive information about the status, outcome, and specifics of each transformation. The details are captured in the TransformationDetails message for each operation.

Key use cases:

  * **Auditing and compliance**
  * Provides a verifiable audit trail of de-identification activities, which is crucial for meeting regulatory requirements and internal data governance policies.
  * Logs what data was transformed, what transformations were applied, when they occurred, and their success status. This helps demonstrate accountability and due diligence in protecting sensitive data.

  * **Troubleshooting and debugging**

  * Offers detailed error messages and context if a transformation fails. This information is useful for diagnosing and resolving issues in the de-identification pipeline.
  * Helps pinpoint the exact location and nature of failures, speeding up the debugging process.

  * **Process verification and quality assurance**

  * Allows users to confirm that de-identification rules and transformations were applied correctly and consistently across the dataset as intended.
  * Helps in verifying the effectiveness of the chosen de-identification strategies.

  * **Data lineage and impact analysis**

  * Creates a record of how data elements were modified, contributing to data lineage. This is useful for understanding the provenance of de-identified data.
  * Aids in assessing the potential impact of de-identification choices on downstream analytical processes or data usability.

  * **Reporting and operational insights**

  * You can analyze the metadata stored in a queryable BigQuery table to generate reports on transformation success rates, common error types, processing volumes (e.g., transformedBytes), and the types of transformations applied.
  * These insights can inform optimization of de-identification configurations and resource planning.

To take advantage of these benefits, set this configuration. The stored details include a description of the transformation, success or error codes, error messages, the number of bytes transformed, the location of the transformed content, and identifiers for the job and source data.




` .google.privacy.dlp.v2.TransformationDetailsStorageConfig transformation_details_storage_config = 3; `

**Returns**  
---  
**Type** | **Description**  
`[TransformationDetailsStorageConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransformationDetailsStorageConfig.Builder)` |   
  
### getTransformationDetailsStorageConfigOrBuilder()
    
    
    public TransformationDetailsStorageConfigOrBuilder getTransformationDetailsStorageConfigOrBuilder()

Config for storing transformation details.

This field specifies the configuration for storing detailed metadata about each transformation performed during a de-identification process. The metadata is stored separately from the de-identified content itself and provides a granular record of both successful transformations and any failures that occurred.

Enabling this configuration is essential for users who need to access comprehensive information about the status, outcome, and specifics of each transformation. The details are captured in the TransformationDetails message for each operation.

Key use cases:

  * **Auditing and compliance**
  * Provides a verifiable audit trail of de-identification activities, which is crucial for meeting regulatory requirements and internal data governance policies.
  * Logs what data was transformed, what transformations were applied, when they occurred, and their success status. This helps demonstrate accountability and due diligence in protecting sensitive data.

  * **Troubleshooting and debugging**

  * Offers detailed error messages and context if a transformation fails. This information is useful for diagnosing and resolving issues in the de-identification pipeline.
  * Helps pinpoint the exact location and nature of failures, speeding up the debugging process.

  * **Process verification and quality assurance**

  * Allows users to confirm that de-identification rules and transformations were applied correctly and consistently across the dataset as intended.
  * Helps in verifying the effectiveness of the chosen de-identification strategies.

  * **Data lineage and impact analysis**

  * Creates a record of how data elements were modified, contributing to data lineage. This is useful for understanding the provenance of de-identified data.
  * Aids in assessing the potential impact of de-identification choices on downstream analytical processes or data usability.

  * **Reporting and operational insights**

  * You can analyze the metadata stored in a queryable BigQuery table to generate reports on transformation success rates, common error types, processing volumes (e.g., transformedBytes), and the types of transformations applied.
  * These insights can inform optimization of de-identification configurations and resource planning.

To take advantage of these benefits, set this configuration. The stored details include a description of the transformation, success or error codes, error messages, the number of bytes transformed, the location of the transformed content, and identifiers for the job and source data.




` .google.privacy.dlp.v2.TransformationDetailsStorageConfig transformation_details_storage_config = 3; `

**Returns**  
---  
**Type** | **Description**  
`[TransformationDetailsStorageConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransformationDetailsStorageConfigOrBuilder)` |   
  
### hasCloudStorageOutput()
    
    
    public boolean hasCloudStorageOutput()

Required. User settable Cloud Storage bucket and folders to store de-identified files. This field must be set for Cloud Storage deidentification. The output Cloud Storage bucket must be different from the input bucket. De-identified files will overwrite files in the output path.

Form of: gs://bucket/folder/ or gs://bucket

`string cloud_storage_output = 9 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cloudStorageOutput field is set.  
  
### hasTransformationConfig()
    
    
    public boolean hasTransformationConfig()

User specified deidentify templates and configs for structured, unstructured, and image files.

`.google.privacy.dlp.v2.TransformationConfig transformation_config = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the transformationConfig field is set.  
  
### hasTransformationDetailsStorageConfig()
    
    
    public boolean hasTransformationDetailsStorageConfig()

Config for storing transformation details.

This field specifies the configuration for storing detailed metadata about each transformation performed during a de-identification process. The metadata is stored separately from the de-identified content itself and provides a granular record of both successful transformations and any failures that occurred.

Enabling this configuration is essential for users who need to access comprehensive information about the status, outcome, and specifics of each transformation. The details are captured in the TransformationDetails message for each operation.

Key use cases:

  * **Auditing and compliance**
  * Provides a verifiable audit trail of de-identification activities, which is crucial for meeting regulatory requirements and internal data governance policies.
  * Logs what data was transformed, what transformations were applied, when they occurred, and their success status. This helps demonstrate accountability and due diligence in protecting sensitive data.

  * **Troubleshooting and debugging**

  * Offers detailed error messages and context if a transformation fails. This information is useful for diagnosing and resolving issues in the de-identification pipeline.
  * Helps pinpoint the exact location and nature of failures, speeding up the debugging process.

  * **Process verification and quality assurance**

  * Allows users to confirm that de-identification rules and transformations were applied correctly and consistently across the dataset as intended.
  * Helps in verifying the effectiveness of the chosen de-identification strategies.

  * **Data lineage and impact analysis**

  * Creates a record of how data elements were modified, contributing to data lineage. This is useful for understanding the provenance of de-identified data.
  * Aids in assessing the potential impact of de-identification choices on downstream analytical processes or data usability.

  * **Reporting and operational insights**

  * You can analyze the metadata stored in a queryable BigQuery table to generate reports on transformation success rates, common error types, processing volumes (e.g., transformedBytes), and the types of transformations applied.
  * These insights can inform optimization of de-identification configurations and resource planning.

To take advantage of these benefits, set this configuration. The stored details include a description of the transformation, success or error codes, error messages, the number of bytes transformed, the location of the transformed content, and identifiers for the job and source data.




` .google.privacy.dlp.v2.TransformationDetailsStorageConfig transformation_details_storage_config = 3; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the transformationDetailsStorageConfig field is set.  
  
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

### mergeFrom(Action.Deidentify other)
    
    
    public Action.Deidentify.Builder mergeFrom(Action.Deidentify other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Action.Deidentify](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public Action.Deidentify.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public Action.Deidentify.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeTransformationConfig(TransformationConfig value)
    
    
    public Action.Deidentify.Builder mergeTransformationConfig(TransformationConfig value)

User specified deidentify templates and configs for structured, unstructured, and image files.

`.google.privacy.dlp.v2.TransformationConfig transformation_config = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[TransformationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransformationConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder)` |   
  
### mergeTransformationDetailsStorageConfig(TransformationDetailsStorageConfig value)
    
    
    public Action.Deidentify.Builder mergeTransformationDetailsStorageConfig(TransformationDetailsStorageConfig value)

Config for storing transformation details.

This field specifies the configuration for storing detailed metadata about each transformation performed during a de-identification process. The metadata is stored separately from the de-identified content itself and provides a granular record of both successful transformations and any failures that occurred.

Enabling this configuration is essential for users who need to access comprehensive information about the status, outcome, and specifics of each transformation. The details are captured in the TransformationDetails message for each operation.

Key use cases:

  * **Auditing and compliance**
  * Provides a verifiable audit trail of de-identification activities, which is crucial for meeting regulatory requirements and internal data governance policies.
  * Logs what data was transformed, what transformations were applied, when they occurred, and their success status. This helps demonstrate accountability and due diligence in protecting sensitive data.

  * **Troubleshooting and debugging**

  * Offers detailed error messages and context if a transformation fails. This information is useful for diagnosing and resolving issues in the de-identification pipeline.
  * Helps pinpoint the exact location and nature of failures, speeding up the debugging process.

  * **Process verification and quality assurance**

  * Allows users to confirm that de-identification rules and transformations were applied correctly and consistently across the dataset as intended.
  * Helps in verifying the effectiveness of the chosen de-identification strategies.

  * **Data lineage and impact analysis**

  * Creates a record of how data elements were modified, contributing to data lineage. This is useful for understanding the provenance of de-identified data.
  * Aids in assessing the potential impact of de-identification choices on downstream analytical processes or data usability.

  * **Reporting and operational insights**

  * You can analyze the metadata stored in a queryable BigQuery table to generate reports on transformation success rates, common error types, processing volumes (e.g., transformedBytes), and the types of transformations applied.
  * These insights can inform optimization of de-identification configurations and resource planning.

To take advantage of these benefits, set this configuration. The stored details include a description of the transformation, success or error codes, error messages, the number of bytes transformed, the location of the transformed content, and identifiers for the job and source data.




` .google.privacy.dlp.v2.TransformationDetailsStorageConfig transformation_details_storage_config = 3; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[TransformationDetailsStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransformationDetailsStorageConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder)` |   
  
### setCloudStorageOutput(String value)
    
    
    public Action.Deidentify.Builder setCloudStorageOutput(String value)

Required. User settable Cloud Storage bucket and folders to store de-identified files. This field must be set for Cloud Storage deidentification. The output Cloud Storage bucket must be different from the input bucket. De-identified files will overwrite files in the output path.

Form of: gs://bucket/folder/ or gs://bucket

`string cloud_storage_output = 9 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The cloudStorageOutput to set.  
**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder)` | This builder for chaining.  
  
### setCloudStorageOutputBytes(ByteString value)
    
    
    public Action.Deidentify.Builder setCloudStorageOutputBytes(ByteString value)

Required. User settable Cloud Storage bucket and folders to store de-identified files. This field must be set for Cloud Storage deidentification. The output Cloud Storage bucket must be different from the input bucket. De-identified files will overwrite files in the output path.

Form of: gs://bucket/folder/ or gs://bucket

`string cloud_storage_output = 9 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for cloudStorageOutput to set.  
**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder)` | This builder for chaining.  
  
### setFileTypesToTransform(int index, FileType value)
    
    
    public Action.Deidentify.Builder setFileTypesToTransform(int index, FileType value)

List of user-specified file type groups to transform. If specified, only the files with these file types are transformed. If empty, all supported files are transformed. Supported types may be automatically added over time. Any unsupported file types that are set in this field are excluded from de-identification. An error is recorded for each unsupported file in the TransformationDetails output table. Currently the only file types supported are: IMAGES, TEXT_FILES, CSV, TSV.

`repeated .google.privacy.dlp.v2.FileType file_types_to_transform = 8;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[FileType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FileType)`  
The fileTypesToTransform to set.  
**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder)` | This builder for chaining.  
  
### setFileTypesToTransformValue(int index, int value)
    
    
    public Action.Deidentify.Builder setFileTypesToTransformValue(int index, int value)

List of user-specified file type groups to transform. If specified, only the files with these file types are transformed. If empty, all supported files are transformed. Supported types may be automatically added over time. Any unsupported file types that are set in this field are excluded from de-identification. An error is recorded for each unsupported file in the TransformationDetails output table. Currently the only file types supported are: IMAGES, TEXT_FILES, CSV, TSV.

`repeated .google.privacy.dlp.v2.FileType file_types_to_transform = 8;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for fileTypesToTransform to set.  
**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder)` | This builder for chaining.  
  
### setTransformationConfig(TransformationConfig value)
    
    
    public Action.Deidentify.Builder setTransformationConfig(TransformationConfig value)

User specified deidentify templates and configs for structured, unstructured, and image files.

`.google.privacy.dlp.v2.TransformationConfig transformation_config = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[TransformationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransformationConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder)` |   
  
### setTransformationConfig(TransformationConfig.Builder builderForValue)
    
    
    public Action.Deidentify.Builder setTransformationConfig(TransformationConfig.Builder builderForValue)

User specified deidentify templates and configs for structured, unstructured, and image files.

`.google.privacy.dlp.v2.TransformationConfig transformation_config = 7;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[TransformationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransformationConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder)` |   
  
### setTransformationDetailsStorageConfig(TransformationDetailsStorageConfig value)
    
    
    public Action.Deidentify.Builder setTransformationDetailsStorageConfig(TransformationDetailsStorageConfig value)

Config for storing transformation details.

This field specifies the configuration for storing detailed metadata about each transformation performed during a de-identification process. The metadata is stored separately from the de-identified content itself and provides a granular record of both successful transformations and any failures that occurred.

Enabling this configuration is essential for users who need to access comprehensive information about the status, outcome, and specifics of each transformation. The details are captured in the TransformationDetails message for each operation.

Key use cases:

  * **Auditing and compliance**
  * Provides a verifiable audit trail of de-identification activities, which is crucial for meeting regulatory requirements and internal data governance policies.
  * Logs what data was transformed, what transformations were applied, when they occurred, and their success status. This helps demonstrate accountability and due diligence in protecting sensitive data.

  * **Troubleshooting and debugging**

  * Offers detailed error messages and context if a transformation fails. This information is useful for diagnosing and resolving issues in the de-identification pipeline.
  * Helps pinpoint the exact location and nature of failures, speeding up the debugging process.

  * **Process verification and quality assurance**

  * Allows users to confirm that de-identification rules and transformations were applied correctly and consistently across the dataset as intended.
  * Helps in verifying the effectiveness of the chosen de-identification strategies.

  * **Data lineage and impact analysis**

  * Creates a record of how data elements were modified, contributing to data lineage. This is useful for understanding the provenance of de-identified data.
  * Aids in assessing the potential impact of de-identification choices on downstream analytical processes or data usability.

  * **Reporting and operational insights**

  * You can analyze the metadata stored in a queryable BigQuery table to generate reports on transformation success rates, common error types, processing volumes (e.g., transformedBytes), and the types of transformations applied.
  * These insights can inform optimization of de-identification configurations and resource planning.

To take advantage of these benefits, set this configuration. The stored details include a description of the transformation, success or error codes, error messages, the number of bytes transformed, the location of the transformed content, and identifiers for the job and source data.




` .google.privacy.dlp.v2.TransformationDetailsStorageConfig transformation_details_storage_config = 3; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[TransformationDetailsStorageConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransformationDetailsStorageConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder)` |   
  
### setTransformationDetailsStorageConfig(TransformationDetailsStorageConfig.Builder builderForValue)
    
    
    public Action.Deidentify.Builder setTransformationDetailsStorageConfig(TransformationDetailsStorageConfig.Builder builderForValue)

Config for storing transformation details.

This field specifies the configuration for storing detailed metadata about each transformation performed during a de-identification process. The metadata is stored separately from the de-identified content itself and provides a granular record of both successful transformations and any failures that occurred.

Enabling this configuration is essential for users who need to access comprehensive information about the status, outcome, and specifics of each transformation. The details are captured in the TransformationDetails message for each operation.

Key use cases:

  * **Auditing and compliance**
  * Provides a verifiable audit trail of de-identification activities, which is crucial for meeting regulatory requirements and internal data governance policies.
  * Logs what data was transformed, what transformations were applied, when they occurred, and their success status. This helps demonstrate accountability and due diligence in protecting sensitive data.

  * **Troubleshooting and debugging**

  * Offers detailed error messages and context if a transformation fails. This information is useful for diagnosing and resolving issues in the de-identification pipeline.
  * Helps pinpoint the exact location and nature of failures, speeding up the debugging process.

  * **Process verification and quality assurance**

  * Allows users to confirm that de-identification rules and transformations were applied correctly and consistently across the dataset as intended.
  * Helps in verifying the effectiveness of the chosen de-identification strategies.

  * **Data lineage and impact analysis**

  * Creates a record of how data elements were modified, contributing to data lineage. This is useful for understanding the provenance of de-identified data.
  * Aids in assessing the potential impact of de-identification choices on downstream analytical processes or data usability.

  * **Reporting and operational insights**

  * You can analyze the metadata stored in a queryable BigQuery table to generate reports on transformation success rates, common error types, processing volumes (e.g., transformedBytes), and the types of transformations applied.
  * These insights can inform optimization of de-identification configurations and resource planning.

To take advantage of these benefits, set this configuration. The stored details include a description of the transformation, success or error codes, error messages, the number of bytes transformed, the location of the transformed content, and identifiers for the job and source data.




` .google.privacy.dlp.v2.TransformationDetailsStorageConfig transformation_details_storage_config = 3; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[TransformationDetailsStorageConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TransformationDetailsStorageConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.Deidentify.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Action.Deidentify.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
