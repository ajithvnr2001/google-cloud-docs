---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder
title: Class Tensorboard.Builder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:17.920926+00:00
---

# Class Tensorboard.Builder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Tensorboard.Builder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public static final class Tensorboard.Builder extends GeneratedMessage.Builder<Tensorboard.Builder> implements TensorboardOrBuilder

Tensorboard is a physical database that stores users' training metrics. A default Tensorboard is provided in each region of a Google Cloud project. If needed users can also create extra Tensorboards in their projects.

Protobuf type `google.cloud.aiplatform.v1.Tensorboard`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > Tensorboard.Builder

## Implements

[TensorboardOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TensorboardOrBuilder)

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
    
    
    public Tensorboard build()

**Returns**  
---  
**Type** | **Description**  
`[Tensorboard](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard)` |   
  
### buildPartial()
    
    
    public Tensorboard buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[Tensorboard](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard)` |   
  
### clear()
    
    
    public Tensorboard.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearBlobStoragePathPrefix()
    
    
    public Tensorboard.Builder clearBlobStoragePathPrefix()

Output only. Consumer project Cloud Storage path prefix used to store blob data, which can either be a bucket or directory. Does not end with a '/'.

`string blob_storage_path_prefix = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` | This builder for chaining.  
  
### clearCreateTime()
    
    
    public Tensorboard.Builder clearCreateTime()

Output only. Timestamp when this Tensorboard was created.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` |   
  
### clearDescription()
    
    
    public Tensorboard.Builder clearDescription()

Description of this Tensorboard.

`string description = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` | This builder for chaining.  
  
### clearDisplayName()
    
    
    public Tensorboard.Builder clearDisplayName()

Required. User provided name of this Tensorboard.

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` | This builder for chaining.  
  
### clearEncryptionSpec()
    
    
    public Tensorboard.Builder clearEncryptionSpec()

Customer-managed encryption key spec for a Tensorboard. If set, this Tensorboard and all sub-resources of this Tensorboard will be secured by this key.

`.google.cloud.aiplatform.v1.EncryptionSpec encryption_spec = 11;`

**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` |   
  
### clearEtag()
    
    
    public Tensorboard.Builder clearEtag()

Used to perform a consistent read-modify-write updates. If not set, a blind "overwrite" update happens.

`string etag = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` | This builder for chaining.  
  
### clearIsDefault()
    
    
    public Tensorboard.Builder clearIsDefault()

Used to indicate if the TensorBoard instance is the default one. Each project & region can have at most one default TensorBoard instance. Creation of a default TensorBoard instance and updating an existing TensorBoard instance to be default will mark all other TensorBoard instances (if any) as non default.

`bool is_default = 12;`

**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` | This builder for chaining.  
  
### clearLabels()
    
    
    public Tensorboard.Builder clearLabels()

**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` |   
  
### clearName()
    
    
    public Tensorboard.Builder clearName()

Output only. Name of the Tensorboard. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` | This builder for chaining.  
  
### clearRunCount()
    
    
    public Tensorboard.Builder clearRunCount()

Output only. The number of Runs stored in this Tensorboard.

`int32 run_count = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` | This builder for chaining.  
  
### clearSatisfiesPzi()
    
    
    public Tensorboard.Builder clearSatisfiesPzi()

Output only. Reserved for future use.

`bool satisfies_pzi = 14 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` | This builder for chaining.  
  
### clearSatisfiesPzs()
    
    
    public Tensorboard.Builder clearSatisfiesPzs()

Output only. Reserved for future use.

`bool satisfies_pzs = 13 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` | This builder for chaining.  
  
### clearUpdateTime()
    
    
    public Tensorboard.Builder clearUpdateTime()

Output only. Timestamp when this Tensorboard was last updated.

` .google.protobuf.Timestamp update_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` |   
  
### containsLabels(String key)
    
    
    public boolean containsLabels(String key)

The labels with user-defined metadata to organize your Tensorboards.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Tensorboard (System labels are excluded).

See <https://goo.gl/xmQnxf> for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.

`map<string, string> labels = 8;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBlobStoragePathPrefix()
    
    
    public String getBlobStoragePathPrefix()

Output only. Consumer project Cloud Storage path prefix used to store blob data, which can either be a bucket or directory. Does not end with a '/'.

`string blob_storage_path_prefix = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The blobStoragePathPrefix.  
  
### getBlobStoragePathPrefixBytes()
    
    
    public ByteString getBlobStoragePathPrefixBytes()

Output only. Consumer project Cloud Storage path prefix used to store blob data, which can either be a bucket or directory. Does not end with a '/'.

`string blob_storage_path_prefix = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for blobStoragePathPrefix.  
  
### getCreateTime()
    
    
    public Timestamp getCreateTime()

Output only. Timestamp when this Tensorboard was created.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeBuilder()
    
    
    public Timestamp.Builder getCreateTimeBuilder()

Output only. Timestamp when this Tensorboard was created.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getCreateTimeOrBuilder()
    
    
    public TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Timestamp when this Tensorboard was created.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDefaultInstanceForType()
    
    
    public Tensorboard getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Tensorboard](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard)` |   
  
### getDescription()
    
    
    public String getDescription()

Description of this Tensorboard.

`string description = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public ByteString getDescriptionBytes()

Description of this Tensorboard.

`string description = 3;`

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

Required. User provided name of this Tensorboard.

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public ByteString getDisplayNameBytes()

Required. User provided name of this Tensorboard.

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getEncryptionSpec()
    
    
    public EncryptionSpec getEncryptionSpec()

Customer-managed encryption key spec for a Tensorboard. If set, this Tensorboard and all sub-resources of this Tensorboard will be secured by this key.

`.google.cloud.aiplatform.v1.EncryptionSpec encryption_spec = 11;`

**Returns**  
---  
**Type** | **Description**  
`[EncryptionSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EncryptionSpec)` | The encryptionSpec.  
  
### getEncryptionSpecBuilder()
    
    
    public EncryptionSpec.Builder getEncryptionSpecBuilder()

Customer-managed encryption key spec for a Tensorboard. If set, this Tensorboard and all sub-resources of this Tensorboard will be secured by this key.

`.google.cloud.aiplatform.v1.EncryptionSpec encryption_spec = 11;`

**Returns**  
---  
**Type** | **Description**  
`[EncryptionSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EncryptionSpec.Builder)` |   
  
### getEncryptionSpecOrBuilder()
    
    
    public EncryptionSpecOrBuilder getEncryptionSpecOrBuilder()

Customer-managed encryption key spec for a Tensorboard. If set, this Tensorboard and all sub-resources of this Tensorboard will be secured by this key.

`.google.cloud.aiplatform.v1.EncryptionSpec encryption_spec = 11;`

**Returns**  
---  
**Type** | **Description**  
`[EncryptionSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EncryptionSpecOrBuilder)` |   
  
### getEtag()
    
    
    public String getEtag()

Used to perform a consistent read-modify-write updates. If not set, a blind "overwrite" update happens.

`string etag = 9;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The etag.  
  
### getEtagBytes()
    
    
    public ByteString getEtagBytes()

Used to perform a consistent read-modify-write updates. If not set, a blind "overwrite" update happens.

`string etag = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for etag.  
  
### getIsDefault()
    
    
    public boolean getIsDefault()

Used to indicate if the TensorBoard instance is the default one. Each project & region can have at most one default TensorBoard instance. Creation of a default TensorBoard instance and updating an existing TensorBoard instance to be default will mark all other TensorBoard instances (if any) as non default.

`bool is_default = 12;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The isDefault.  
  
### getLabels() (deprecated)
    
    
    public Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder#com_google_cloud_aiplatform_v1_Tensorboard_Builder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public int getLabelsCount()

The labels with user-defined metadata to organize your Tensorboards.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Tensorboard (System labels are excluded).

See <https://goo.gl/xmQnxf> for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.

`map<string, string> labels = 8;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public Map<String,String> getLabelsMap()

The labels with user-defined metadata to organize your Tensorboards.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Tensorboard (System labels are excluded).

See <https://goo.gl/xmQnxf> for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.

`map<string, string> labels = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public String getLabelsOrDefault(String key, String defaultValue)

The labels with user-defined metadata to organize your Tensorboards.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Tensorboard (System labels are excluded).

See <https://goo.gl/xmQnxf> for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.

`map<string, string> labels = 8;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLabelsOrThrow(String key)
    
    
    public String getLabelsOrThrow(String key)

The labels with user-defined metadata to organize your Tensorboards.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Tensorboard (System labels are excluded).

See <https://goo.gl/xmQnxf> for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.

`map<string, string> labels = 8;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMutableLabels() (deprecated)
    
    
    public Map<String,String> getMutableLabels()

Use alternate mutation accessors instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getName()
    
    
    public String getName()

Output only. Name of the Tensorboard. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

Output only. Name of the Tensorboard. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getRunCount()
    
    
    public int getRunCount()

Output only. The number of Runs stored in this Tensorboard.

`int32 run_count = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The runCount.  
  
### getSatisfiesPzi()
    
    
    public boolean getSatisfiesPzi()

Output only. Reserved for future use.

`bool satisfies_pzi = 14 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The satisfiesPzi.  
  
### getSatisfiesPzs()
    
    
    public boolean getSatisfiesPzs()

Output only. Reserved for future use.

`bool satisfies_pzs = 13 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The satisfiesPzs.  
  
### getUpdateTime()
    
    
    public Timestamp getUpdateTime()

Output only. Timestamp when this Tensorboard was last updated.

` .google.protobuf.Timestamp update_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeBuilder()
    
    
    public Timestamp.Builder getUpdateTimeBuilder()

Output only. Timestamp when this Tensorboard was last updated.

` .google.protobuf.Timestamp update_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getUpdateTimeOrBuilder()
    
    
    public TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. Timestamp when this Tensorboard was last updated.

` .google.protobuf.Timestamp update_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCreateTime()
    
    
    public boolean hasCreateTime()

Output only. Timestamp when this Tensorboard was created.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasEncryptionSpec()
    
    
    public boolean hasEncryptionSpec()

Customer-managed encryption key spec for a Tensorboard. If set, this Tensorboard and all sub-resources of this Tensorboard will be secured by this key.

`.google.cloud.aiplatform.v1.EncryptionSpec encryption_spec = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the encryptionSpec field is set.  
  
### hasUpdateTime()
    
    
    public boolean hasUpdateTime()

Output only. Timestamp when this Tensorboard was last updated.

` .google.protobuf.Timestamp update_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

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
    
    
    public Tensorboard.Builder mergeCreateTime(Timestamp value)

Output only. Timestamp when this Tensorboard was created.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` |   
  
### mergeEncryptionSpec(EncryptionSpec value)
    
    
    public Tensorboard.Builder mergeEncryptionSpec(EncryptionSpec value)

Customer-managed encryption key spec for a Tensorboard. If set, this Tensorboard and all sub-resources of this Tensorboard will be secured by this key.

`.google.cloud.aiplatform.v1.EncryptionSpec encryption_spec = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[EncryptionSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EncryptionSpec)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` |   
  
### mergeFrom(Tensorboard other)
    
    
    public Tensorboard.Builder mergeFrom(Tensorboard other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Tensorboard](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public Tensorboard.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public Tensorboard.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeUpdateTime(Timestamp value)
    
    
    public Tensorboard.Builder mergeUpdateTime(Timestamp value)

Output only. Timestamp when this Tensorboard was last updated.

` .google.protobuf.Timestamp update_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` |   
  
### putAllLabels(Map<String,String> values)
    
    
    public Tensorboard.Builder putAllLabels(Map<String,String> values)

The labels with user-defined metadata to organize your Tensorboards.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Tensorboard (System labels are excluded).

See <https://goo.gl/xmQnxf> for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.

`map<string, string> labels = 8;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` |   
  
### putLabels(String key, String value)
    
    
    public Tensorboard.Builder putLabels(String key, String value)

The labels with user-defined metadata to organize your Tensorboards.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Tensorboard (System labels are excluded).

See <https://goo.gl/xmQnxf> for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.

`map<string, string> labels = 8;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` |   
  
### removeLabels(String key)
    
    
    public Tensorboard.Builder removeLabels(String key)

The labels with user-defined metadata to organize your Tensorboards.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Tensorboard (System labels are excluded).

See <https://goo.gl/xmQnxf> for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable.

`map<string, string> labels = 8;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` |   
  
### setBlobStoragePathPrefix(String value)
    
    
    public Tensorboard.Builder setBlobStoragePathPrefix(String value)

Output only. Consumer project Cloud Storage path prefix used to store blob data, which can either be a bucket or directory. Does not end with a '/'.

`string blob_storage_path_prefix = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The blobStoragePathPrefix to set.  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` | This builder for chaining.  
  
### setBlobStoragePathPrefixBytes(ByteString value)
    
    
    public Tensorboard.Builder setBlobStoragePathPrefixBytes(ByteString value)

Output only. Consumer project Cloud Storage path prefix used to store blob data, which can either be a bucket or directory. Does not end with a '/'.

`string blob_storage_path_prefix = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for blobStoragePathPrefix to set.  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` | This builder for chaining.  
  
### setCreateTime(Timestamp value)
    
    
    public Tensorboard.Builder setCreateTime(Timestamp value)

Output only. Timestamp when this Tensorboard was created.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` |   
  
### setCreateTime(Timestamp.Builder builderForValue)
    
    
    public Tensorboard.Builder setCreateTime(Timestamp.Builder builderForValue)

Output only. Timestamp when this Tensorboard was created.

` .google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` |   
  
### setDescription(String value)
    
    
    public Tensorboard.Builder setDescription(String value)

Description of this Tensorboard.

`string description = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The description to set.  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` | This builder for chaining.  
  
### setDescriptionBytes(ByteString value)
    
    
    public Tensorboard.Builder setDescriptionBytes(ByteString value)

Description of this Tensorboard.

`string description = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for description to set.  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` | This builder for chaining.  
  
### setDisplayName(String value)
    
    
    public Tensorboard.Builder setDisplayName(String value)

Required. User provided name of this Tensorboard.

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` | This builder for chaining.  
  
### setDisplayNameBytes(ByteString value)
    
    
    public Tensorboard.Builder setDisplayNameBytes(ByteString value)

Required. User provided name of this Tensorboard.

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` | This builder for chaining.  
  
### setEncryptionSpec(EncryptionSpec value)
    
    
    public Tensorboard.Builder setEncryptionSpec(EncryptionSpec value)

Customer-managed encryption key spec for a Tensorboard. If set, this Tensorboard and all sub-resources of this Tensorboard will be secured by this key.

`.google.cloud.aiplatform.v1.EncryptionSpec encryption_spec = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[EncryptionSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EncryptionSpec)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` |   
  
### setEncryptionSpec(EncryptionSpec.Builder builderForValue)
    
    
    public Tensorboard.Builder setEncryptionSpec(EncryptionSpec.Builder builderForValue)

Customer-managed encryption key spec for a Tensorboard. If set, this Tensorboard and all sub-resources of this Tensorboard will be secured by this key.

`.google.cloud.aiplatform.v1.EncryptionSpec encryption_spec = 11;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[EncryptionSpec.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EncryptionSpec.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` |   
  
### setEtag(String value)
    
    
    public Tensorboard.Builder setEtag(String value)

Used to perform a consistent read-modify-write updates. If not set, a blind "overwrite" update happens.

`string etag = 9;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The etag to set.  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` | This builder for chaining.  
  
### setEtagBytes(ByteString value)
    
    
    public Tensorboard.Builder setEtagBytes(ByteString value)

Used to perform a consistent read-modify-write updates. If not set, a blind "overwrite" update happens.

`string etag = 9;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for etag to set.  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` | This builder for chaining.  
  
### setIsDefault(boolean value)
    
    
    public Tensorboard.Builder setIsDefault(boolean value)

Used to indicate if the TensorBoard instance is the default one. Each project & region can have at most one default TensorBoard instance. Creation of a default TensorBoard instance and updating an existing TensorBoard instance to be default will mark all other TensorBoard instances (if any) as non default.

`bool is_default = 12;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The isDefault to set.  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` | This builder for chaining.  
  
### setName(String value)
    
    
    public Tensorboard.Builder setName(String value)

Output only. Name of the Tensorboard. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public Tensorboard.Builder setNameBytes(ByteString value)

Output only. Name of the Tensorboard. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` | This builder for chaining.  
  
### setRunCount(int value)
    
    
    public Tensorboard.Builder setRunCount(int value)

Output only. The number of Runs stored in this Tensorboard.

`int32 run_count = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The runCount to set.  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` | This builder for chaining.  
  
### setSatisfiesPzi(boolean value)
    
    
    public Tensorboard.Builder setSatisfiesPzi(boolean value)

Output only. Reserved for future use.

`bool satisfies_pzi = 14 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The satisfiesPzi to set.  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` | This builder for chaining.  
  
### setSatisfiesPzs(boolean value)
    
    
    public Tensorboard.Builder setSatisfiesPzs(boolean value)

Output only. Reserved for future use.

`bool satisfies_pzs = 13 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The satisfiesPzs to set.  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` | This builder for chaining.  
  
### setUpdateTime(Timestamp value)
    
    
    public Tensorboard.Builder setUpdateTime(Timestamp value)

Output only. Timestamp when this Tensorboard was last updated.

` .google.protobuf.Timestamp update_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` |   
  
### setUpdateTime(Timestamp.Builder builderForValue)
    
    
    public Tensorboard.Builder setUpdateTime(Timestamp.Builder builderForValue)

Output only. Timestamp when this Tensorboard was last updated.

` .google.protobuf.Timestamp update_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Tensorboard.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Tensorboard.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
