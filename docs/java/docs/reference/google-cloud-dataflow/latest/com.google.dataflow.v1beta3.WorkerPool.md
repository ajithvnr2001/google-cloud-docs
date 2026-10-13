---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool
title: Class WorkerPool (0.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:33:03.181555+00:00
---

# Class WorkerPool (0.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class WorkerPool (0.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.103.0 (latest)  0.99.0  0.98.0  0.97.0  0.95.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.82.0  0.80.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.68.0  0.67.0  0.66.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.5.0 
    
    
    public final class WorkerPool extends GeneratedMessage implements WorkerPoolOrBuilder

Describes one particular pool of Cloud Dataflow workers to be instantiated by the Cloud Dataflow service in order to perform the computations required by a job. Note that a workflow job may use multiple pools, in order to match the various computational requirements of the various stages of the job.

Protobuf type `google.dataflow.v1beta3.WorkerPool`

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html) > [AbstractMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html) > [GeneratedMessage](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html) > WorkerPool

## Implements

[WorkerPoolOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPoolOrBuilder)

## Inherited Members

[AbstractMessage.equals(Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_equals_java_lang_Object_)

[AbstractMessage.findInitializationErrors()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_findInitializationErrors__)

[AbstractMessage.getInitializationErrorString()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_getInitializationErrorString__)

[AbstractMessage.hashCode()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_hashCode__)

[AbstractMessage.hashFields(int,Map<Descriptors.FieldDescriptor,Object>)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_hashFields_int_java_util_Map_com_google_protobuf_Descriptors_FieldDescriptor_java_lang_Object__)

[AbstractMessage.newBuilderForType(AbstractMessage.BuilderParent)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_newBuilderForType_com_google_protobuf_AbstractMessage_BuilderParent_)

[AbstractMessage.toString()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_toString__)

[AbstractMessageLite.<T>addAll(Iterable<T>,List<? super T>)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite__T_addAll_java_lang_Iterable_T__java_util_List___super_T__)

[AbstractMessageLite.checkByteStringIsUtf8(ByteString)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite_checkByteStringIsUtf8_com_google_protobuf_ByteString_)

[AbstractMessageLite.toByteArray()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite_toByteArray__)

[AbstractMessageLite.toByteString()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite_toByteString__)

[AbstractMessageLite.writeDelimitedTo(OutputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite_writeDelimitedTo_java_io_OutputStream_)

[AbstractMessageLite.writeTo(OutputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.html#com_google_protobuf_AbstractMessageLite_writeTo_java_io_OutputStream_)

com.google.protobuf.GeneratedMessage.<ContainingT,T>newFileScopedGeneratedExtension(java.lang.Class<?>,com.google.protobuf.Message)

com.google.protobuf.GeneratedMessage.<ContainingT,T>newMessageScopedGeneratedExtension(com.google.protobuf.Message,int,java.lang.Class<?>,com.google.protobuf.Message)

com.google.protobuf.GeneratedMessage.<ListT>makeMutableCopy(ListT)

com.google.protobuf.GeneratedMessage.<ListT>makeMutableCopy(ListT,int)

[GeneratedMessage.<M>parseDelimitedWithIOException(Parser<M>,InputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseDelimitedWithIOException_com_google_protobuf_Parser_M__java_io_InputStream_)

[GeneratedMessage.<M>parseDelimitedWithIOException(Parser<M>,InputStream,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseDelimitedWithIOException_com_google_protobuf_Parser_M__java_io_InputStream_com_google_protobuf_ExtensionRegistryLite_)

[GeneratedMessage.<M>parseWithIOException(Parser<M>,CodedInputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseWithIOException_com_google_protobuf_Parser_M__com_google_protobuf_CodedInputStream_)

[GeneratedMessage.<M>parseWithIOException(Parser<M>,CodedInputStream,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseWithIOException_com_google_protobuf_Parser_M__com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

[GeneratedMessage.<M>parseWithIOException(Parser<M>,InputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseWithIOException_com_google_protobuf_Parser_M__java_io_InputStream_)

[GeneratedMessage.<M>parseWithIOException(Parser<M>,InputStream,ExtensionRegistryLite)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage__M_parseWithIOException_com_google_protobuf_Parser_M__java_io_InputStream_com_google_protobuf_ExtensionRegistryLite_)

com.google.protobuf.GeneratedMessage.<T>emptyList(java.lang.Class<T>)

com.google.protobuf.GeneratedMessage.<V>serializeBooleanMapTo(com.google.protobuf.CodedOutputStream,com.google.protobuf.MapField<java.lang.Boolean,V>,com.google.protobuf.MapEntry<java.lang.Boolean,V>,int)

com.google.protobuf.GeneratedMessage.<V>serializeIntegerMapTo(com.google.protobuf.CodedOutputStream,com.google.protobuf.MapField<java.lang.Integer,V>,com.google.protobuf.MapEntry<java.lang.Integer,V>,int)

com.google.protobuf.GeneratedMessage.<V>serializeLongMapTo(com.google.protobuf.CodedOutputStream,com.google.protobuf.MapField<java.lang.Long,V>,com.google.protobuf.MapEntry<java.lang.Long,V>,int)

com.google.protobuf.GeneratedMessage.<V>serializeStringMapTo(com.google.protobuf.CodedOutputStream,com.google.protobuf.MapField<java.lang.String,V>,com.google.protobuf.MapEntry<java.lang.String,V>,int)

com.google.protobuf.GeneratedMessage.canUseUnsafe()

[GeneratedMessage.computeStringSize(int,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_computeStringSize_int_java_lang_Object_)

[GeneratedMessage.computeStringSizeNoTag(Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_computeStringSizeNoTag_java_lang_Object_)

com.google.protobuf.GeneratedMessage.emptyBooleanList()

com.google.protobuf.GeneratedMessage.emptyDoubleList()

com.google.protobuf.GeneratedMessage.emptyFloatList()

com.google.protobuf.GeneratedMessage.emptyIntList()

com.google.protobuf.GeneratedMessage.emptyLongList()

[GeneratedMessage.getAllFields()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getAllFields__)

[GeneratedMessage.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getDescriptorForType__)

[GeneratedMessage.getField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.getOneofFieldDescriptor(Descriptors.OneofDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getOneofFieldDescriptor_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessage.getParserForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getParserForType__)

[GeneratedMessage.getRepeatedField(Descriptors.FieldDescriptor,int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getRepeatedField_com_google_protobuf_Descriptors_FieldDescriptor_int_)

[GeneratedMessage.getRepeatedFieldCount(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getRepeatedFieldCount_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.getSerializedSize()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getSerializedSize__)

[GeneratedMessage.getUnknownFields()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getUnknownFields__)

[GeneratedMessage.hasField(Descriptors.FieldDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_hasField_com_google_protobuf_Descriptors_FieldDescriptor_)

[GeneratedMessage.hasOneof(Descriptors.OneofDescriptor)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_hasOneof_com_google_protobuf_Descriptors_OneofDescriptor_)

[GeneratedMessage.internalGetFieldAccessorTable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_internalGetFieldAccessorTable__)

[GeneratedMessage.internalGetMapField(int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_internalGetMapField_int_)

com.google.protobuf.GeneratedMessage.internalGetMapFieldReflection(int)

[GeneratedMessage.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_isInitialized__)

com.google.protobuf.GeneratedMessage.isStringEmpty(java.lang.Object)

[GeneratedMessage.makeExtensionsImmutable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_makeExtensionsImmutable__)

com.google.protobuf.GeneratedMessage.mergeFromAndMakeImmutableInternal(com.google.protobuf.CodedInputStream,com.google.protobuf.ExtensionRegistryLite)

com.google.protobuf.GeneratedMessage.newInstance(com.google.protobuf.GeneratedMessage.UnusedPrivateParameter)

[GeneratedMessage.parseUnknownField(CodedInputStream,UnknownFieldSet.Builder,ExtensionRegistryLite,int)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_parseUnknownField_com_google_protobuf_CodedInputStream_com_google_protobuf_UnknownFieldSet_Builder_com_google_protobuf_ExtensionRegistryLite_int_)

com.google.protobuf.GeneratedMessage.parseUnknownFieldProto3(com.google.protobuf.CodedInputStream,com.google.protobuf.UnknownFieldSet.Builder,com.google.protobuf.ExtensionRegistryLite,int)

[GeneratedMessage.writeReplace()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_writeReplace__)

[GeneratedMessage.writeString(CodedOutputStream,int,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_writeString_com_google_protobuf_CodedOutputStream_int_java_lang_Object_)

[GeneratedMessage.writeStringNoTag(CodedOutputStream,Object)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_writeStringNoTag_com_google_protobuf_CodedOutputStream_java_lang_Object_)

[GeneratedMessage.writeTo(CodedOutputStream)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_writeTo_com_google_protobuf_CodedOutputStream_)

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields 

### AUTOSCALING_SETTINGS_FIELD_NUMBER
    
    
    public static final int AUTOSCALING_SETTINGS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### DATA_DISKS_FIELD_NUMBER
    
    
    public static final int DATA_DISKS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### DEFAULT_PACKAGE_SET_FIELD_NUMBER
    
    
    public static final int DEFAULT_PACKAGE_SET_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### DISK_PROVISIONED_IOPS_FIELD_NUMBER
    
    
    public static final int DISK_PROVISIONED_IOPS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### DISK_PROVISIONED_THROUGHPUT_MIBPS_FIELD_NUMBER
    
    
    public static final int DISK_PROVISIONED_THROUGHPUT_MIBPS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### DISK_SIZE_GB_FIELD_NUMBER
    
    
    public static final int DISK_SIZE_GB_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### DISK_SOURCE_IMAGE_FIELD_NUMBER
    
    
    public static final int DISK_SOURCE_IMAGE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### DISK_TYPE_FIELD_NUMBER
    
    
    public static final int DISK_TYPE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### IP_CONFIGURATION_FIELD_NUMBER
    
    
    public static final int IP_CONFIGURATION_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### KIND_FIELD_NUMBER
    
    
    public static final int KIND_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MACHINE_TYPE_FIELD_NUMBER
    
    
    public static final int MACHINE_TYPE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### METADATA_FIELD_NUMBER
    
    
    public static final int METADATA_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### NETWORK_FIELD_NUMBER
    
    
    public static final int NETWORK_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### NUM_THREADS_PER_WORKER_FIELD_NUMBER
    
    
    public static final int NUM_THREADS_PER_WORKER_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### NUM_WORKERS_FIELD_NUMBER
    
    
    public static final int NUM_WORKERS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### ON_HOST_MAINTENANCE_FIELD_NUMBER
    
    
    public static final int ON_HOST_MAINTENANCE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### PACKAGES_FIELD_NUMBER
    
    
    public static final int PACKAGES_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### POOL_ARGS_FIELD_NUMBER
    
    
    public static final int POOL_ARGS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SDK_HARNESS_CONTAINER_IMAGES_FIELD_NUMBER
    
    
    public static final int SDK_HARNESS_CONTAINER_IMAGES_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SUBNETWORK_FIELD_NUMBER
    
    
    public static final int SUBNETWORK_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### TASKRUNNER_SETTINGS_FIELD_NUMBER
    
    
    public static final int TASKRUNNER_SETTINGS_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### TEARDOWN_POLICY_FIELD_NUMBER
    
    
    public static final int TEARDOWN_POLICY_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### WORKER_HARNESS_CONTAINER_IMAGE_FIELD_NUMBER
    
    
    public static final int WORKER_HARNESS_CONTAINER_IMAGE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### ZONE_FIELD_NUMBER
    
    
    public static final int ZONE_FIELD_NUMBER

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Static Methods 

### getDefaultInstance()
    
    
    public static WorkerPool getDefaultInstance()

**Returns**  
---  
**Type** | **Description**  
`[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool)` |   
  
### getDescriptor()
    
    
    public static final Descriptors.Descriptor getDescriptor()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
  
### newBuilder()
    
    
    public static WorkerPool.Builder newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[WorkerPool.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool.Builder)` |   
  
### newBuilder(WorkerPool prototype)
    
    
    public static WorkerPool.Builder newBuilder(WorkerPool prototype)

**Parameter**  
---  
**Name** | **Description**  
`prototype` | `[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkerPool.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool.Builder)` |   
  
### parseDelimitedFrom(InputStream input)
    
    
    public static WorkerPool parseDelimitedFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static WorkerPool parseDelimitedFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(byte[] data)
    
    
    public static WorkerPool parseFrom(byte[] data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)
    
    
    public static WorkerPool parseFrom(byte[] data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `byte[]`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data)
    
    
    public static WorkerPool parseFrom(ByteString data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)
    
    
    public static WorkerPool parseFrom(ByteString data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(CodedInputStream input)
    
    
    public static WorkerPool parseFrom(CodedInputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static WorkerPool parseFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input)
    
    
    public static WorkerPool parseFrom(InputStream input)

**Parameter**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public static WorkerPool parseFrom(InputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[InputStream](https://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### parseFrom(ByteBuffer data)
    
    
    public static WorkerPool parseFrom(ByteBuffer data)

**Parameter**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)
    
    
    public static WorkerPool parseFrom(ByteBuffer data, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`data` | `[ByteBuffer](https://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InvalidProtocolBufferException](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.InvalidProtocolBufferException.html)` |   
  
### parser()
    
    
    public static Parser<WorkerPool> parser()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool)>` |   
  
## Methods 

### containsMetadata(String key)
    
    
    public boolean containsMetadata(String key)

Metadata to set on the Google Compute Engine VMs.

`map<string, string> metadata = 13;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### equals(Object obj)
    
    
    public boolean equals(Object obj)

**Parameter**  
---  
**Name** | **Description**  
`obj` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[AbstractMessage.equals(Object other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_equals_java_lang_Object_)

### getAutoscalingSettings()
    
    
    public AutoscalingSettings getAutoscalingSettings()

Settings for autoscaling of this WorkerPool.

`.google.dataflow.v1beta3.AutoscalingSettings autoscaling_settings = 14;`

**Returns**  
---  
**Type** | **Description**  
`[AutoscalingSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.AutoscalingSettings)` | The autoscalingSettings.  
  
### getAutoscalingSettingsOrBuilder()
    
    
    public AutoscalingSettingsOrBuilder getAutoscalingSettingsOrBuilder()

Settings for autoscaling of this WorkerPool.

`.google.dataflow.v1beta3.AutoscalingSettings autoscaling_settings = 14;`

**Returns**  
---  
**Type** | **Description**  
`[AutoscalingSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.AutoscalingSettingsOrBuilder)` |   
  
### getDataDisks(int index)
    
    
    public Disk getDataDisks(int index)

Data disks that are used by a VM in this workflow.

`repeated .google.dataflow.v1beta3.Disk data_disks = 12;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.Disk)` |   
  
### getDataDisksCount()
    
    
    public int getDataDisksCount()

Data disks that are used by a VM in this workflow.

`repeated .google.dataflow.v1beta3.Disk data_disks = 12;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDataDisksList()
    
    
    public List<Disk> getDataDisksList()

Data disks that are used by a VM in this workflow.

`repeated .google.dataflow.v1beta3.Disk data_disks = 12;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Disk](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.Disk)>` |   
  
### getDataDisksOrBuilder(int index)
    
    
    public DiskOrBuilder getDataDisksOrBuilder(int index)

Data disks that are used by a VM in this workflow.

`repeated .google.dataflow.v1beta3.Disk data_disks = 12;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DiskOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.DiskOrBuilder)` |   
  
### getDataDisksOrBuilderList()
    
    
    public List<? extends DiskOrBuilder> getDataDisksOrBuilderList()

Data disks that are used by a VM in this workflow.

`repeated .google.dataflow.v1beta3.Disk data_disks = 12;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.dataflow.v1beta3.DiskOrBuilder>` |   
  
### getDefaultInstanceForType()
    
    
    public WorkerPool getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool)` |   
  
### getDefaultPackageSet()
    
    
    public DefaultPackageSet getDefaultPackageSet()

The default package set to install. This allows the service to select a default set of packages which are useful to worker harnesses written in a particular language.

`.google.dataflow.v1beta3.DefaultPackageSet default_package_set = 4;`

**Returns**  
---  
**Type** | **Description**  
`[DefaultPackageSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.DefaultPackageSet)` | The defaultPackageSet.  
  
### getDefaultPackageSetValue()
    
    
    public int getDefaultPackageSetValue()

The default package set to install. This allows the service to select a default set of packages which are useful to worker harnesses written in a particular language.

`.google.dataflow.v1beta3.DefaultPackageSet default_package_set = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for defaultPackageSet.  
  
### getDiskProvisionedIops()
    
    
    public long getDiskProvisionedIops()

Optional. IOPS provisioned for the root disk for VMs.

`int64 disk_provisioned_iops = 23 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The diskProvisionedIops.  
  
### getDiskProvisionedThroughputMibps()
    
    
    public long getDiskProvisionedThroughputMibps()

Optional. Throughput provisioned for the root disk for VMs.

`int64 disk_provisioned_throughput_mibps = 24 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The diskProvisionedThroughputMibps.  
  
### getDiskSizeGb()
    
    
    public int getDiskSizeGb()

Size of root disk for VMs, in GB. If zero or unspecified, the service will attempt to choose a reasonable default.

`int32 disk_size_gb = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The diskSizeGb.  
  
### getDiskSourceImage()
    
    
    public String getDiskSourceImage()

Fully qualified source image for disks.

`string disk_source_image = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The diskSourceImage.  
  
### getDiskSourceImageBytes()
    
    
    public ByteString getDiskSourceImageBytes()

Fully qualified source image for disks.

`string disk_source_image = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for diskSourceImage.  
  
### getDiskType()
    
    
    public String getDiskType()

Type of root disk for VMs. If empty or unspecified, the service will attempt to choose a reasonable default.

`string disk_type = 16;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The diskType.  
  
### getDiskTypeBytes()
    
    
    public ByteString getDiskTypeBytes()

Type of root disk for VMs. If empty or unspecified, the service will attempt to choose a reasonable default.

`string disk_type = 16;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for diskType.  
  
### getIpConfiguration()
    
    
    public WorkerIPAddressConfiguration getIpConfiguration()

Configuration for VM IPs.

`.google.dataflow.v1beta3.WorkerIPAddressConfiguration ip_configuration = 21;`

**Returns**  
---  
**Type** | **Description**  
`[WorkerIPAddressConfiguration](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerIPAddressConfiguration)` | The ipConfiguration.  
  
### getIpConfigurationValue()
    
    
    public int getIpConfigurationValue()

Configuration for VM IPs.

`.google.dataflow.v1beta3.WorkerIPAddressConfiguration ip_configuration = 21;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for ipConfiguration.  
  
### getKind()
    
    
    public String getKind()

The kind of the worker pool; currently only `harness` and `shuffle` are supported.

`string kind = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kind.  
  
### getKindBytes()
    
    
    public ByteString getKindBytes()

The kind of the worker pool; currently only `harness` and `shuffle` are supported.

`string kind = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kind.  
  
### getMachineType()
    
    
    public String getMachineType()

Machine type (e.g. "n1-standard-1"). If empty or unspecified, the service will attempt to choose a reasonable default.

`string machine_type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The machineType.  
  
### getMachineTypeBytes()
    
    
    public ByteString getMachineTypeBytes()

Machine type (e.g. "n1-standard-1"). If empty or unspecified, the service will attempt to choose a reasonable default.

`string machine_type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for machineType.  
  
### getMetadata() (deprecated)
    
    
    public Map<String,String> getMetadata()

Use [#getMetadataMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool#com_google_dataflow_v1beta3_WorkerPool_getMetadataMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getMetadataCount()
    
    
    public int getMetadataCount()

Metadata to set on the Google Compute Engine VMs.

`map<string, string> metadata = 13;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMetadataMap()
    
    
    public Map<String,String> getMetadataMap()

Metadata to set on the Google Compute Engine VMs.

`map<string, string> metadata = 13;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getMetadataOrDefault(String key, String defaultValue)
    
    
    public String getMetadataOrDefault(String key, String defaultValue)

Metadata to set on the Google Compute Engine VMs.

`map<string, string> metadata = 13;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMetadataOrThrow(String key)
    
    
    public String getMetadataOrThrow(String key)

Metadata to set on the Google Compute Engine VMs.

`map<string, string> metadata = 13;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getNetwork()
    
    
    public String getNetwork()

Network to which VMs will be assigned. If empty or unspecified, the service will use the network "default".

`string network = 17;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The network.  
  
### getNetworkBytes()
    
    
    public ByteString getNetworkBytes()

Network to which VMs will be assigned. If empty or unspecified, the service will use the network "default".

`string network = 17;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for network.  
  
### getNumThreadsPerWorker()
    
    
    public int getNumThreadsPerWorker()

The number of threads per worker harness. If empty or unspecified, the service will choose a number of threads (according to the number of cores on the selected machine type for batch, or 1 by convention for streaming).

`int32 num_threads_per_worker = 20;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The numThreadsPerWorker.  
  
### getNumWorkers()
    
    
    public int getNumWorkers()

Number of Google Compute Engine workers in this pool needed to execute the job. If zero or unspecified, the service will attempt to choose a reasonable default.

`int32 num_workers = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The numWorkers.  
  
### getOnHostMaintenance()
    
    
    public String getOnHostMaintenance()

The action to take on host maintenance, as defined by the Google Compute Engine API.

`string on_host_maintenance = 11;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The onHostMaintenance.  
  
### getOnHostMaintenanceBytes()
    
    
    public ByteString getOnHostMaintenanceBytes()

The action to take on host maintenance, as defined by the Google Compute Engine API.

`string on_host_maintenance = 11;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for onHostMaintenance.  
  
### getPackages(int index)
    
    
    public Package getPackages(int index)

Packages to be installed on workers.

`repeated .google.dataflow.v1beta3.Package packages = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Package](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.Package)` |   
  
### getPackagesCount()
    
    
    public int getPackagesCount()

Packages to be installed on workers.

`repeated .google.dataflow.v1beta3.Package packages = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPackagesList()
    
    
    public List<Package> getPackagesList()

Packages to be installed on workers.

`repeated .google.dataflow.v1beta3.Package packages = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Package](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.Package)>` |   
  
### getPackagesOrBuilder(int index)
    
    
    public PackageOrBuilder getPackagesOrBuilder(int index)

Packages to be installed on workers.

`repeated .google.dataflow.v1beta3.Package packages = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PackageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.PackageOrBuilder)` |   
  
### getPackagesOrBuilderList()
    
    
    public List<? extends PackageOrBuilder> getPackagesOrBuilderList()

Packages to be installed on workers.

`repeated .google.dataflow.v1beta3.Package packages = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.dataflow.v1beta3.PackageOrBuilder>` |   
  
### getParserForType()
    
    
    public Parser<WorkerPool> getParserForType()

**Returns**  
---  
**Type** | **Description**  
`[Parser](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Parser.html)<[WorkerPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool)>` |   
**Overrides**

[GeneratedMessage.getParserForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getParserForType__)

### getPoolArgs()
    
    
    public Any getPoolArgs()

Extra arguments for this worker pool.

`.google.protobuf.Any pool_args = 15;`

**Returns**  
---  
**Type** | **Description**  
`[Any](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Any.html)` | The poolArgs.  
  
### getPoolArgsOrBuilder()
    
    
    public AnyOrBuilder getPoolArgsOrBuilder()

Extra arguments for this worker pool.

`.google.protobuf.Any pool_args = 15;`

**Returns**  
---  
**Type** | **Description**  
`[AnyOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AnyOrBuilder.html)` |   
  
### getSdkHarnessContainerImages(int index)
    
    
    public SdkHarnessContainerImage getSdkHarnessContainerImages(int index)

Set of SDK harness containers needed to execute this pipeline. This will only be set in the Fn API path. For non-cross-language pipelines this should have only one entry. Cross-language pipelines will have two or more entries.

` repeated .google.dataflow.v1beta3.SdkHarnessContainerImage sdk_harness_container_images = 22; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SdkHarnessContainerImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.SdkHarnessContainerImage)` |   
  
### getSdkHarnessContainerImagesCount()
    
    
    public int getSdkHarnessContainerImagesCount()

Set of SDK harness containers needed to execute this pipeline. This will only be set in the Fn API path. For non-cross-language pipelines this should have only one entry. Cross-language pipelines will have two or more entries.

` repeated .google.dataflow.v1beta3.SdkHarnessContainerImage sdk_harness_container_images = 22; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSdkHarnessContainerImagesList()
    
    
    public List<SdkHarnessContainerImage> getSdkHarnessContainerImagesList()

Set of SDK harness containers needed to execute this pipeline. This will only be set in the Fn API path. For non-cross-language pipelines this should have only one entry. Cross-language pipelines will have two or more entries.

` repeated .google.dataflow.v1beta3.SdkHarnessContainerImage sdk_harness_container_images = 22; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[SdkHarnessContainerImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.SdkHarnessContainerImage)>` |   
  
### getSdkHarnessContainerImagesOrBuilder(int index)
    
    
    public SdkHarnessContainerImageOrBuilder getSdkHarnessContainerImagesOrBuilder(int index)

Set of SDK harness containers needed to execute this pipeline. This will only be set in the Fn API path. For non-cross-language pipelines this should have only one entry. Cross-language pipelines will have two or more entries.

` repeated .google.dataflow.v1beta3.SdkHarnessContainerImage sdk_harness_container_images = 22; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SdkHarnessContainerImageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.SdkHarnessContainerImageOrBuilder)` |   
  
### getSdkHarnessContainerImagesOrBuilderList()
    
    
    public List<? extends SdkHarnessContainerImageOrBuilder> getSdkHarnessContainerImagesOrBuilderList()

Set of SDK harness containers needed to execute this pipeline. This will only be set in the Fn API path. For non-cross-language pipelines this should have only one entry. Cross-language pipelines will have two or more entries.

` repeated .google.dataflow.v1beta3.SdkHarnessContainerImage sdk_harness_container_images = 22; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.dataflow.v1beta3.SdkHarnessContainerImageOrBuilder>` |   
  
### getSerializedSize()
    
    
    public int getSerializedSize()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.getSerializedSize()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_getSerializedSize__)

### getSubnetwork()
    
    
    public String getSubnetwork()

Subnetwork to which VMs will be assigned, if desired. Expected to be of the form "regions/REGION/subnetworks/SUBNETWORK".

`string subnetwork = 19;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The subnetwork.  
  
### getSubnetworkBytes()
    
    
    public ByteString getSubnetworkBytes()

Subnetwork to which VMs will be assigned, if desired. Expected to be of the form "regions/REGION/subnetworks/SUBNETWORK".

`string subnetwork = 19;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for subnetwork.  
  
### getTaskrunnerSettings()
    
    
    public TaskRunnerSettings getTaskrunnerSettings()

Settings passed through to Google Compute Engine workers when using the standard Dataflow task runner. Users should ignore this field.

`.google.dataflow.v1beta3.TaskRunnerSettings taskrunner_settings = 10;`

**Returns**  
---  
**Type** | **Description**  
`[TaskRunnerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.TaskRunnerSettings)` | The taskrunnerSettings.  
  
### getTaskrunnerSettingsOrBuilder()
    
    
    public TaskRunnerSettingsOrBuilder getTaskrunnerSettingsOrBuilder()

Settings passed through to Google Compute Engine workers when using the standard Dataflow task runner. Users should ignore this field.

`.google.dataflow.v1beta3.TaskRunnerSettings taskrunner_settings = 10;`

**Returns**  
---  
**Type** | **Description**  
`[TaskRunnerSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.TaskRunnerSettingsOrBuilder)` |   
  
### getTeardownPolicy()
    
    
    public TeardownPolicy getTeardownPolicy()

Sets the policy for determining when to turndown worker pool. Allowed values are: `TEARDOWN_ALWAYS`, `TEARDOWN_ON_SUCCESS`, and `TEARDOWN_NEVER`. `TEARDOWN_ALWAYS` means workers are always torn down regardless of whether the job succeeds. `TEARDOWN_ON_SUCCESS` means workers are torn down if the job succeeds. `TEARDOWN_NEVER` means the workers are never torn down.

If the workers are not torn down by the service, they will continue to run and use Google Compute Engine VM resources in the user's project until they are explicitly terminated by the user. Because of this, Google recommends using the `TEARDOWN_ALWAYS` policy except for small, manually supervised test jobs.

If unknown or unspecified, the service will attempt to choose a reasonable default.

`.google.dataflow.v1beta3.TeardownPolicy teardown_policy = 6;`

**Returns**  
---  
**Type** | **Description**  
`[TeardownPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.TeardownPolicy)` | The teardownPolicy.  
  
### getTeardownPolicyValue()
    
    
    public int getTeardownPolicyValue()

Sets the policy for determining when to turndown worker pool. Allowed values are: `TEARDOWN_ALWAYS`, `TEARDOWN_ON_SUCCESS`, and `TEARDOWN_NEVER`. `TEARDOWN_ALWAYS` means workers are always torn down regardless of whether the job succeeds. `TEARDOWN_ON_SUCCESS` means workers are torn down if the job succeeds. `TEARDOWN_NEVER` means the workers are never torn down.

If the workers are not torn down by the service, they will continue to run and use Google Compute Engine VM resources in the user's project until they are explicitly terminated by the user. Because of this, Google recommends using the `TEARDOWN_ALWAYS` policy except for small, manually supervised test jobs.

If unknown or unspecified, the service will attempt to choose a reasonable default.

`.google.dataflow.v1beta3.TeardownPolicy teardown_policy = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for teardownPolicy.  
  
### getWorkerHarnessContainerImage()
    
    
    public String getWorkerHarnessContainerImage()

Required. Docker container image that executes the Cloud Dataflow worker harness, residing in Google Container Registry.

Deprecated for the Fn API path. Use sdk_harness_container_images instead.

`string worker_harness_container_image = 18;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The workerHarnessContainerImage.  
  
### getWorkerHarnessContainerImageBytes()
    
    
    public ByteString getWorkerHarnessContainerImageBytes()

Required. Docker container image that executes the Cloud Dataflow worker harness, residing in Google Container Registry.

Deprecated for the Fn API path. Use sdk_harness_container_images instead.

`string worker_harness_container_image = 18;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for workerHarnessContainerImage.  
  
### getZone()
    
    
    public String getZone()

Zone to run the worker pools in. If empty or unspecified, the service will attempt to choose a reasonable default.

`string zone = 9;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The zone.  
  
### getZoneBytes()
    
    
    public ByteString getZoneBytes()

Zone to run the worker pools in. If empty or unspecified, the service will attempt to choose a reasonable default.

`string zone = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for zone.  
  
### hasAutoscalingSettings()
    
    
    public boolean hasAutoscalingSettings()

Settings for autoscaling of this WorkerPool.

`.google.dataflow.v1beta3.AutoscalingSettings autoscaling_settings = 14;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the autoscalingSettings field is set.  
  
### hasPoolArgs()
    
    
    public boolean hasPoolArgs()

Extra arguments for this worker pool.

`.google.protobuf.Any pool_args = 15;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the poolArgs field is set.  
  
### hasTaskrunnerSettings()
    
    
    public boolean hasTaskrunnerSettings()

Settings passed through to Google Compute Engine workers when using the standard Dataflow task runner. Users should ignore this field.

`.google.dataflow.v1beta3.TaskRunnerSettings taskrunner_settings = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the taskrunnerSettings field is set.  
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[AbstractMessage.hashCode()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_hashCode__)

### internalGetFieldAccessorTable()
    
    
    protected GeneratedMessage.FieldAccessorTable internalGetFieldAccessorTable()

**Returns**  
---  
**Type** | **Description**  
`[FieldAccessorTable](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.FieldAccessorTable.html)` |   
**Overrides**

[GeneratedMessage.internalGetFieldAccessorTable()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_internalGetFieldAccessorTable__)

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

com.google.protobuf.GeneratedMessage.internalGetMapFieldReflection(int)

### isInitialized()
    
    
    public final boolean isInitialized()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[GeneratedMessage.isInitialized()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_isInitialized__)

### newBuilderForType()
    
    
    public WorkerPool.Builder newBuilderForType()

**Returns**  
---  
**Type** | **Description**  
`[WorkerPool.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool.Builder)` |   
  
### newBuilderForType(AbstractMessage.BuilderParent parent)
    
    
    protected WorkerPool.Builder newBuilderForType(AbstractMessage.BuilderParent parent)

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[BuilderParent](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.BuilderParent.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkerPool.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool.Builder)` |   
**Overrides**

[AbstractMessage.newBuilderForType(AbstractMessage.BuilderParent parent)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.html#com_google_protobuf_AbstractMessage_newBuilderForType_com_google_protobuf_AbstractMessage_BuilderParent_)

### toBuilder()
    
    
    public WorkerPool.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[WorkerPool.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataflow/latest/com.google.dataflow.v1beta3.WorkerPool.Builder)` |   
  
### writeTo(CodedOutputStream output)
    
    
    public void writeTo(CodedOutputStream output)

**Parameter**  
---  
**Name** | **Description**  
`output` | `[CodedOutputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedOutputStream.html)`  
  
**Overrides**

[GeneratedMessage.writeTo(CodedOutputStream output)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.html#com_google_protobuf_GeneratedMessage_writeTo_com_google_protobuf_CodedOutputStream_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
