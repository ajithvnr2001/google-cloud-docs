---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder
title: Class PatchJobs.PatchJob.Builder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:02.958634+00:00
---

# Class PatchJobs.PatchJob.Builder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PatchJobs.PatchJob.Builder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.6  2.4.3  2.3.2 
    
    
    public static final class PatchJobs.PatchJob.Builder extends GeneratedMessage.Builder<PatchJobs.PatchJob.Builder> implements PatchJobs.PatchJobOrBuilder

A high level representation of a patch job that is either in progress or has completed.

Instance details are not included in the job. To paginate through instance details, use ListPatchJobInstanceDetails.

For more information about patch jobs, see [Creating patch jobs](https://cloud.google.com/compute/docs/os-patch-management/create-patch-job).

Protobuf type `google.cloud.osconfig.v1.PatchJob`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > PatchJobs.PatchJob.Builder

## Implements

[PatchJobs.PatchJobOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJobOrBuilder)

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
    
    
    public PatchJobs.PatchJob build()

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob)` |   
  
### buildPartial()
    
    
    public PatchJobs.PatchJob buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob)` |   
  
### clear()
    
    
    public PatchJobs.PatchJob.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearCreateTime()
    
    
    public PatchJobs.PatchJob.Builder clearCreateTime()

Time this patch job was created.

`.google.protobuf.Timestamp create_time = 3;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### clearDescription()
    
    
    public PatchJobs.PatchJob.Builder clearDescription()

Description of the patch job. Length of the description is limited to 1024 characters.

`string description = 2;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` | This builder for chaining.  
  
### clearDisplayName()
    
    
    public PatchJobs.PatchJob.Builder clearDisplayName()

Display name for this patch job. This is not a unique identifier.

`string display_name = 14;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` | This builder for chaining.  
  
### clearDryRun()
    
    
    public PatchJobs.PatchJob.Builder clearDryRun()

If this patch job is a dry run, the agent reports that it has finished without running any updates on the VM instance.

`bool dry_run = 10;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` | This builder for chaining.  
  
### clearDuration()
    
    
    public PatchJobs.PatchJob.Builder clearDuration()

Duration of the patch job. After the duration ends, the patch job times out.

`.google.protobuf.Duration duration = 8;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### clearErrorMessage()
    
    
    public PatchJobs.PatchJob.Builder clearErrorMessage()

If this patch job failed, this message provides information about the failure.

`string error_message = 11;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` | This builder for chaining.  
  
### clearInstanceDetailsSummary()
    
    
    public PatchJobs.PatchJob.Builder clearInstanceDetailsSummary()

Summary of instance details.

` .google.cloud.osconfig.v1.PatchJob.InstanceDetailsSummary instance_details_summary = 9; `

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### clearInstanceFilter()
    
    
    public PatchJobs.PatchJob.Builder clearInstanceFilter()

Instances to patch.

`.google.cloud.osconfig.v1.PatchInstanceFilter instance_filter = 13;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### clearName()
    
    
    public PatchJobs.PatchJob.Builder clearName()

Unique identifier for this patch job in the form `projects/*/patchJobs/*`

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` | This builder for chaining.  
  
### clearPatchConfig()
    
    
    public PatchJobs.PatchJob.Builder clearPatchConfig()

Patch configuration being applied.

`.google.cloud.osconfig.v1.PatchConfig patch_config = 7;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### clearPatchDeployment()
    
    
    public PatchJobs.PatchJob.Builder clearPatchDeployment()

Output only. Name of the patch deployment that created this patch job.

` string patch_deployment = 15 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` | This builder for chaining.  
  
### clearPercentComplete()
    
    
    public PatchJobs.PatchJob.Builder clearPercentComplete()

Reflects the overall progress of the patch job in the range of 0.0 being no progress to 100.0 being complete.

`double percent_complete = 12;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` | This builder for chaining.  
  
### clearRollout()
    
    
    public PatchJobs.PatchJob.Builder clearRollout()

Rollout strategy being applied.

`.google.cloud.osconfig.v1.PatchRollout rollout = 16;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### clearState()
    
    
    public PatchJobs.PatchJob.Builder clearState()

The current state of the PatchJob.

`.google.cloud.osconfig.v1.PatchJob.State state = 5;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` | This builder for chaining.  
  
### clearUpdateTime()
    
    
    public PatchJobs.PatchJob.Builder clearUpdateTime()

Last time this patch job was updated.

`.google.protobuf.Timestamp update_time = 4;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### getCreateTime()
    
    
    public Timestamp getCreateTime()

Time this patch job was created.

`.google.protobuf.Timestamp create_time = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeBuilder()
    
    
    public Timestamp.Builder getCreateTimeBuilder()

Time this patch job was created.

`.google.protobuf.Timestamp create_time = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getCreateTimeOrBuilder()
    
    
    public TimestampOrBuilder getCreateTimeOrBuilder()

Time this patch job was created.

`.google.protobuf.Timestamp create_time = 3;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDefaultInstanceForType()
    
    
    public PatchJobs.PatchJob getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob)` |   
  
### getDescription()
    
    
    public String getDescription()

Description of the patch job. Length of the description is limited to 1024 characters.

`string description = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public ByteString getDescriptionBytes()

Description of the patch job. Length of the description is limited to 1024 characters.

`string description = 2;`

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

Display name for this patch job. This is not a unique identifier.

`string display_name = 14;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public ByteString getDisplayNameBytes()

Display name for this patch job. This is not a unique identifier.

`string display_name = 14;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getDryRun()
    
    
    public boolean getDryRun()

If this patch job is a dry run, the agent reports that it has finished without running any updates on the VM instance.

`bool dry_run = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The dryRun.  
  
### getDuration()
    
    
    public Duration getDuration()

Duration of the patch job. After the duration ends, the patch job times out.

`.google.protobuf.Duration duration = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The duration.  
  
### getDurationBuilder()
    
    
    public Duration.Builder getDurationBuilder()

Duration of the patch job. After the duration ends, the patch job times out.

`.google.protobuf.Duration duration = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)` |   
  
### getDurationOrBuilder()
    
    
    public DurationOrBuilder getDurationOrBuilder()

Duration of the patch job. After the duration ends, the patch job times out.

`.google.protobuf.Duration duration = 8;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getErrorMessage()
    
    
    public String getErrorMessage()

If this patch job failed, this message provides information about the failure.

`string error_message = 11;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The errorMessage.  
  
### getErrorMessageBytes()
    
    
    public ByteString getErrorMessageBytes()

If this patch job failed, this message provides information about the failure.

`string error_message = 11;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for errorMessage.  
  
### getInstanceDetailsSummary()
    
    
    public PatchJobs.PatchJob.InstanceDetailsSummary getInstanceDetailsSummary()

Summary of instance details.

` .google.cloud.osconfig.v1.PatchJob.InstanceDetailsSummary instance_details_summary = 9; `

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.InstanceDetailsSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.InstanceDetailsSummary)` | The instanceDetailsSummary.  
  
### getInstanceDetailsSummaryBuilder()
    
    
    public PatchJobs.PatchJob.InstanceDetailsSummary.Builder getInstanceDetailsSummaryBuilder()

Summary of instance details.

` .google.cloud.osconfig.v1.PatchJob.InstanceDetailsSummary instance_details_summary = 9; `

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.InstanceDetailsSummary.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.InstanceDetailsSummary.Builder)` |   
  
### getInstanceDetailsSummaryOrBuilder()
    
    
    public PatchJobs.PatchJob.InstanceDetailsSummaryOrBuilder getInstanceDetailsSummaryOrBuilder()

Summary of instance details.

` .google.cloud.osconfig.v1.PatchJob.InstanceDetailsSummary instance_details_summary = 9; `

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.InstanceDetailsSummaryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.InstanceDetailsSummaryOrBuilder)` |   
  
### getInstanceFilter()
    
    
    public PatchJobs.PatchInstanceFilter getInstanceFilter()

Instances to patch.

`.google.cloud.osconfig.v1.PatchInstanceFilter instance_filter = 13;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchInstanceFilter)` | The instanceFilter.  
  
### getInstanceFilterBuilder()
    
    
    public PatchJobs.PatchInstanceFilter.Builder getInstanceFilterBuilder()

Instances to patch.

`.google.cloud.osconfig.v1.PatchInstanceFilter instance_filter = 13;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchInstanceFilter.Builder)` |   
  
### getInstanceFilterOrBuilder()
    
    
    public PatchJobs.PatchInstanceFilterOrBuilder getInstanceFilterOrBuilder()

Instances to patch.

`.google.cloud.osconfig.v1.PatchInstanceFilter instance_filter = 13;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchInstanceFilterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchInstanceFilterOrBuilder)` |   
  
### getName()
    
    
    public String getName()

Unique identifier for this patch job in the form `projects/*/patchJobs/*`

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

Unique identifier for this patch job in the form `projects/*/patchJobs/*`

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPatchConfig()
    
    
    public PatchJobs.PatchConfig getPatchConfig()

Patch configuration being applied.

`.google.cloud.osconfig.v1.PatchConfig patch_config = 7;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchConfig)` | The patchConfig.  
  
### getPatchConfigBuilder()
    
    
    public PatchJobs.PatchConfig.Builder getPatchConfigBuilder()

Patch configuration being applied.

`.google.cloud.osconfig.v1.PatchConfig patch_config = 7;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchConfig.Builder)` |   
  
### getPatchConfigOrBuilder()
    
    
    public PatchJobs.PatchConfigOrBuilder getPatchConfigOrBuilder()

Patch configuration being applied.

`.google.cloud.osconfig.v1.PatchConfig patch_config = 7;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchConfigOrBuilder)` |   
  
### getPatchDeployment()
    
    
    public String getPatchDeployment()

Output only. Name of the patch deployment that created this patch job.

` string patch_deployment = 15 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The patchDeployment.  
  
### getPatchDeploymentBytes()
    
    
    public ByteString getPatchDeploymentBytes()

Output only. Name of the patch deployment that created this patch job.

` string patch_deployment = 15 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for patchDeployment.  
  
### getPercentComplete()
    
    
    public double getPercentComplete()

Reflects the overall progress of the patch job in the range of 0.0 being no progress to 100.0 being complete.

`double percent_complete = 12;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The percentComplete.  
  
### getRollout()
    
    
    public PatchJobs.PatchRollout getRollout()

Rollout strategy being applied.

`.google.cloud.osconfig.v1.PatchRollout rollout = 16;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchRollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchRollout)` | The rollout.  
  
### getRolloutBuilder()
    
    
    public PatchJobs.PatchRollout.Builder getRolloutBuilder()

Rollout strategy being applied.

`.google.cloud.osconfig.v1.PatchRollout rollout = 16;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchRollout.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchRollout.Builder)` |   
  
### getRolloutOrBuilder()
    
    
    public PatchJobs.PatchRolloutOrBuilder getRolloutOrBuilder()

Rollout strategy being applied.

`.google.cloud.osconfig.v1.PatchRollout rollout = 16;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchRolloutOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchRolloutOrBuilder)` |   
  
### getState()
    
    
    public PatchJobs.PatchJob.State getState()

The current state of the PatchJob.

`.google.cloud.osconfig.v1.PatchJob.State state = 5;`

**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.State)` | The state.  
  
### getStateValue()
    
    
    public int getStateValue()

The current state of the PatchJob.

`.google.cloud.osconfig.v1.PatchJob.State state = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getUpdateTime()
    
    
    public Timestamp getUpdateTime()

Last time this patch job was updated.

`.google.protobuf.Timestamp update_time = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeBuilder()
    
    
    public Timestamp.Builder getUpdateTimeBuilder()

Last time this patch job was updated.

`.google.protobuf.Timestamp update_time = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)` |   
  
### getUpdateTimeOrBuilder()
    
    
    public TimestampOrBuilder getUpdateTimeOrBuilder()

Last time this patch job was updated.

`.google.protobuf.Timestamp update_time = 4;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCreateTime()
    
    
    public boolean hasCreateTime()

Time this patch job was created.

`.google.protobuf.Timestamp create_time = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasDuration()
    
    
    public boolean hasDuration()

Duration of the patch job. After the duration ends, the patch job times out.

`.google.protobuf.Duration duration = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the duration field is set.  
  
### hasInstanceDetailsSummary()
    
    
    public boolean hasInstanceDetailsSummary()

Summary of instance details.

` .google.cloud.osconfig.v1.PatchJob.InstanceDetailsSummary instance_details_summary = 9; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the instanceDetailsSummary field is set.  
  
### hasInstanceFilter()
    
    
    public boolean hasInstanceFilter()

Instances to patch.

`.google.cloud.osconfig.v1.PatchInstanceFilter instance_filter = 13;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the instanceFilter field is set.  
  
### hasPatchConfig()
    
    
    public boolean hasPatchConfig()

Patch configuration being applied.

`.google.cloud.osconfig.v1.PatchConfig patch_config = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the patchConfig field is set.  
  
### hasRollout()
    
    
    public boolean hasRollout()

Rollout strategy being applied.

`.google.cloud.osconfig.v1.PatchRollout rollout = 16;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rollout field is set.  
  
### hasUpdateTime()
    
    
    public boolean hasUpdateTime()

Last time this patch job was updated.

`.google.protobuf.Timestamp update_time = 4;`

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

### isInitialized()
    
    
    public final boolean isInitialized()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_isInitialized__)

### mergeCreateTime(Timestamp value)
    
    
    public PatchJobs.PatchJob.Builder mergeCreateTime(Timestamp value)

Time this patch job was created.

`.google.protobuf.Timestamp create_time = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### mergeDuration(Duration value)
    
    
    public PatchJobs.PatchJob.Builder mergeDuration(Duration value)

Duration of the patch job. After the duration ends, the patch job times out.

`.google.protobuf.Duration duration = 8;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### mergeFrom(PatchJobs.PatchJob other)
    
    
    public PatchJobs.PatchJob.Builder mergeFrom(PatchJobs.PatchJob other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[PatchJobs.PatchJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public PatchJobs.PatchJob.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public PatchJobs.PatchJob.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeInstanceDetailsSummary(PatchJobs.PatchJob.InstanceDetailsSummary value)
    
    
    public PatchJobs.PatchJob.Builder mergeInstanceDetailsSummary(PatchJobs.PatchJob.InstanceDetailsSummary value)

Summary of instance details.

` .google.cloud.osconfig.v1.PatchJob.InstanceDetailsSummary instance_details_summary = 9; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PatchJobs.PatchJob.InstanceDetailsSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.InstanceDetailsSummary)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### mergeInstanceFilter(PatchJobs.PatchInstanceFilter value)
    
    
    public PatchJobs.PatchJob.Builder mergeInstanceFilter(PatchJobs.PatchInstanceFilter value)

Instances to patch.

`.google.cloud.osconfig.v1.PatchInstanceFilter instance_filter = 13;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PatchJobs.PatchInstanceFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchInstanceFilter)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### mergePatchConfig(PatchJobs.PatchConfig value)
    
    
    public PatchJobs.PatchJob.Builder mergePatchConfig(PatchJobs.PatchConfig value)

Patch configuration being applied.

`.google.cloud.osconfig.v1.PatchConfig patch_config = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PatchJobs.PatchConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### mergeRollout(PatchJobs.PatchRollout value)
    
    
    public PatchJobs.PatchJob.Builder mergeRollout(PatchJobs.PatchRollout value)

Rollout strategy being applied.

`.google.cloud.osconfig.v1.PatchRollout rollout = 16;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PatchJobs.PatchRollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchRollout)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### mergeUpdateTime(Timestamp value)
    
    
    public PatchJobs.PatchJob.Builder mergeUpdateTime(Timestamp value)

Last time this patch job was updated.

`.google.protobuf.Timestamp update_time = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### setCreateTime(Timestamp value)
    
    
    public PatchJobs.PatchJob.Builder setCreateTime(Timestamp value)

Time this patch job was created.

`.google.protobuf.Timestamp create_time = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### setCreateTime(Timestamp.Builder builderForValue)
    
    
    public PatchJobs.PatchJob.Builder setCreateTime(Timestamp.Builder builderForValue)

Time this patch job was created.

`.google.protobuf.Timestamp create_time = 3;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### setDescription(String value)
    
    
    public PatchJobs.PatchJob.Builder setDescription(String value)

Description of the patch job. Length of the description is limited to 1024 characters.

`string description = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The description to set.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` | This builder for chaining.  
  
### setDescriptionBytes(ByteString value)
    
    
    public PatchJobs.PatchJob.Builder setDescriptionBytes(ByteString value)

Description of the patch job. Length of the description is limited to 1024 characters.

`string description = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for description to set.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` | This builder for chaining.  
  
### setDisplayName(String value)
    
    
    public PatchJobs.PatchJob.Builder setDisplayName(String value)

Display name for this patch job. This is not a unique identifier.

`string display_name = 14;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` | This builder for chaining.  
  
### setDisplayNameBytes(ByteString value)
    
    
    public PatchJobs.PatchJob.Builder setDisplayNameBytes(ByteString value)

Display name for this patch job. This is not a unique identifier.

`string display_name = 14;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for displayName to set.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` | This builder for chaining.  
  
### setDryRun(boolean value)
    
    
    public PatchJobs.PatchJob.Builder setDryRun(boolean value)

If this patch job is a dry run, the agent reports that it has finished without running any updates on the VM instance.

`bool dry_run = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The dryRun to set.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` | This builder for chaining.  
  
### setDuration(Duration value)
    
    
    public PatchJobs.PatchJob.Builder setDuration(Duration value)

Duration of the patch job. After the duration ends, the patch job times out.

`.google.protobuf.Duration duration = 8;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### setDuration(Duration.Builder builderForValue)
    
    
    public PatchJobs.PatchJob.Builder setDuration(Duration.Builder builderForValue)

Duration of the patch job. After the duration ends, the patch job times out.

`.google.protobuf.Duration duration = 8;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### setErrorMessage(String value)
    
    
    public PatchJobs.PatchJob.Builder setErrorMessage(String value)

If this patch job failed, this message provides information about the failure.

`string error_message = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The errorMessage to set.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` | This builder for chaining.  
  
### setErrorMessageBytes(ByteString value)
    
    
    public PatchJobs.PatchJob.Builder setErrorMessageBytes(ByteString value)

If this patch job failed, this message provides information about the failure.

`string error_message = 11;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for errorMessage to set.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` | This builder for chaining.  
  
### setInstanceDetailsSummary(PatchJobs.PatchJob.InstanceDetailsSummary value)
    
    
    public PatchJobs.PatchJob.Builder setInstanceDetailsSummary(PatchJobs.PatchJob.InstanceDetailsSummary value)

Summary of instance details.

` .google.cloud.osconfig.v1.PatchJob.InstanceDetailsSummary instance_details_summary = 9; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PatchJobs.PatchJob.InstanceDetailsSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.InstanceDetailsSummary)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### setInstanceDetailsSummary(PatchJobs.PatchJob.InstanceDetailsSummary.Builder builderForValue)
    
    
    public PatchJobs.PatchJob.Builder setInstanceDetailsSummary(PatchJobs.PatchJob.InstanceDetailsSummary.Builder builderForValue)

Summary of instance details.

` .google.cloud.osconfig.v1.PatchJob.InstanceDetailsSummary instance_details_summary = 9; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[PatchJobs.PatchJob.InstanceDetailsSummary.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.InstanceDetailsSummary.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### setInstanceFilter(PatchJobs.PatchInstanceFilter value)
    
    
    public PatchJobs.PatchJob.Builder setInstanceFilter(PatchJobs.PatchInstanceFilter value)

Instances to patch.

`.google.cloud.osconfig.v1.PatchInstanceFilter instance_filter = 13;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PatchJobs.PatchInstanceFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchInstanceFilter)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### setInstanceFilter(PatchJobs.PatchInstanceFilter.Builder builderForValue)
    
    
    public PatchJobs.PatchJob.Builder setInstanceFilter(PatchJobs.PatchInstanceFilter.Builder builderForValue)

Instances to patch.

`.google.cloud.osconfig.v1.PatchInstanceFilter instance_filter = 13;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[PatchJobs.PatchInstanceFilter.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchInstanceFilter.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### setName(String value)
    
    
    public PatchJobs.PatchJob.Builder setName(String value)

Unique identifier for this patch job in the form `projects/*/patchJobs/*`

`string name = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public PatchJobs.PatchJob.Builder setNameBytes(ByteString value)

Unique identifier for this patch job in the form `projects/*/patchJobs/*`

`string name = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` | This builder for chaining.  
  
### setPatchConfig(PatchJobs.PatchConfig value)
    
    
    public PatchJobs.PatchJob.Builder setPatchConfig(PatchJobs.PatchConfig value)

Patch configuration being applied.

`.google.cloud.osconfig.v1.PatchConfig patch_config = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PatchJobs.PatchConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### setPatchConfig(PatchJobs.PatchConfig.Builder builderForValue)
    
    
    public PatchJobs.PatchJob.Builder setPatchConfig(PatchJobs.PatchConfig.Builder builderForValue)

Patch configuration being applied.

`.google.cloud.osconfig.v1.PatchConfig patch_config = 7;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[PatchJobs.PatchConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### setPatchDeployment(String value)
    
    
    public PatchJobs.PatchJob.Builder setPatchDeployment(String value)

Output only. Name of the patch deployment that created this patch job.

` string patch_deployment = 15 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The patchDeployment to set.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` | This builder for chaining.  
  
### setPatchDeploymentBytes(ByteString value)
    
    
    public PatchJobs.PatchJob.Builder setPatchDeploymentBytes(ByteString value)

Output only. Name of the patch deployment that created this patch job.

` string patch_deployment = 15 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for patchDeployment to set.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` | This builder for chaining.  
  
### setPercentComplete(double value)
    
    
    public PatchJobs.PatchJob.Builder setPercentComplete(double value)

Reflects the overall progress of the patch job in the range of 0.0 being no progress to 100.0 being complete.

`double percent_complete = 12;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The percentComplete to set.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` | This builder for chaining.  
  
### setRollout(PatchJobs.PatchRollout value)
    
    
    public PatchJobs.PatchJob.Builder setRollout(PatchJobs.PatchRollout value)

Rollout strategy being applied.

`.google.cloud.osconfig.v1.PatchRollout rollout = 16;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PatchJobs.PatchRollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchRollout)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### setRollout(PatchJobs.PatchRollout.Builder builderForValue)
    
    
    public PatchJobs.PatchJob.Builder setRollout(PatchJobs.PatchRollout.Builder builderForValue)

Rollout strategy being applied.

`.google.cloud.osconfig.v1.PatchRollout rollout = 16;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[PatchJobs.PatchRollout.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchRollout.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### setState(PatchJobs.PatchJob.State value)
    
    
    public PatchJobs.PatchJob.Builder setState(PatchJobs.PatchJob.State value)

The current state of the PatchJob.

`.google.cloud.osconfig.v1.PatchJob.State state = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PatchJobs.PatchJob.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.State)`  
The state to set.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` | This builder for chaining.  
  
### setStateValue(int value)
    
    
    public PatchJobs.PatchJob.Builder setStateValue(int value)

The current state of the PatchJob.

`.google.cloud.osconfig.v1.PatchJob.State state = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for state to set.  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` | This builder for chaining.  
  
### setUpdateTime(Timestamp value)
    
    
    public PatchJobs.PatchJob.Builder setUpdateTime(Timestamp value)

Last time this patch job was updated.

`.google.protobuf.Timestamp update_time = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
### setUpdateTime(Timestamp.Builder builderForValue)
    
    
    public PatchJobs.PatchJob.Builder setUpdateTime(Timestamp.Builder builderForValue)

Last time this patch job was updated.

`.google.protobuf.Timestamp update_time = 4;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PatchJobs.PatchJob.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1.PatchJobs.PatchJob.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
