---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder
title: Class RetryConfig.Builder (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:25:06.486216+00:00
---

# Class RetryConfig.Builder (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RetryConfig.Builder (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.12  2.2.0  2.1.11 
    
    
    public static final class RetryConfig.Builder extends GeneratedMessage.Builder<RetryConfig.Builder> implements RetryConfigOrBuilder

Retry config.

These settings determine when a failed task attempt is retried.

Protobuf type `google.cloud.tasks.v2.RetryConfig`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > RetryConfig.Builder

## Implements

[RetryConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfigOrBuilder)

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
    
    
    public RetryConfig build()

**Returns**  
---  
**Type** | **Description**  
`[RetryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig)` |   
  
### buildPartial()
    
    
    public RetryConfig buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[RetryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig)` |   
  
### clear()
    
    
    public RetryConfig.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[RetryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearMaxAttempts()
    
    
    public RetryConfig.Builder clearMaxAttempts()

Number of attempts per task, including the first attempt. (If the first attempt fails, there will be `max_attempts - 1` retries.)

Must be greater than or equal to -1, which indicates unlimited attempts.

Cloud Tasks stops retrying only when `max_attempts` and `max_retry_duration` are both satisfied, or when the task is successfully executed. When the task has been attempted `max_attempts` times and when the `max_retry_duration` time has passed, no further attempts are made, and the task is deleted. If `max_attempts` is set to -1 and `max_retry_duration` is set to 0, the task is retried until the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit is reached.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [task_retry_limit in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`int32 max_attempts = 1;`

**Returns**  
---  
**Type** | **Description**  
`[RetryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder)` | This builder for chaining.  
  
### clearMaxBackoff()
    
    
    public RetryConfig.Builder clearMaxBackoff()

A task will be scheduled for retry between min_backoff and max_backoff duration after it fails, if the queue's RetryConfig specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [max_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration max_backoff = 4;`

**Returns**  
---  
**Type** | **Description**  
`[RetryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder)` |   
  
### clearMaxDoublings()
    
    
    public RetryConfig.Builder clearMaxDoublings()

The time between retries will double `max_doublings` times.

A task's retry interval starts at min_backoff, then doubles `max_doublings` times, then increases linearly, and finally retries at intervals of max_backoff up to max_attempts times.

For example, if min_backoff is 10s, max_backoff is 300s, and `max_doublings` is 3, then the a task will first be retried in 10s. The retry interval will double three times, and then increase linearly by 2^3 * 10s. Finally, the task will retry at intervals of max_backoff until the task has been attempted max_attempts times. Thus, the requests will retry at 10s, 20s, 40s, 80s, 160s, 240s, 300s, 300s, ....

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [max_doublings in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`int32 max_doublings = 5;`

**Returns**  
---  
**Type** | **Description**  
`[RetryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder)` | This builder for chaining.  
  
### clearMaxRetryDuration()
    
    
    public RetryConfig.Builder clearMaxRetryDuration()

If positive, `max_retry_duration` specifies the time limit for retrying a failed task, measured from when the task was first attempted. Once `max_retry_duration` time has passed _and_ the task has been attempted max_attempts times, no further attempts are made and the task is deleted.

A zero (0) indicates an unlimited duration, up to the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For the maximum possible value or the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_retry_duration` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [task_age_limit in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration max_retry_duration = 2;`

**Returns**  
---  
**Type** | **Description**  
`[RetryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder)` |   
  
### clearMinBackoff()
    
    
    public RetryConfig.Builder clearMinBackoff()

A task will be scheduled for retry between min_backoff and max_backoff duration after it fails, if the queue's RetryConfig specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `min_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [min_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration min_backoff = 3;`

**Returns**  
---  
**Type** | **Description**  
`[RetryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder)` |   
  
### getDefaultInstanceForType()
    
    
    public RetryConfig getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[RetryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getMaxAttempts()
    
    
    public int getMaxAttempts()

Number of attempts per task, including the first attempt. (If the first attempt fails, there will be `max_attempts - 1` retries.)

Must be greater than or equal to -1, which indicates unlimited attempts.

Cloud Tasks stops retrying only when `max_attempts` and `max_retry_duration` are both satisfied, or when the task is successfully executed. When the task has been attempted `max_attempts` times and when the `max_retry_duration` time has passed, no further attempts are made, and the task is deleted. If `max_attempts` is set to -1 and `max_retry_duration` is set to 0, the task is retried until the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit is reached.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [task_retry_limit in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`int32 max_attempts = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maxAttempts.  
  
### getMaxBackoff()
    
    
    public Duration getMaxBackoff()

A task will be scheduled for retry between min_backoff and max_backoff duration after it fails, if the queue's RetryConfig specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [max_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration max_backoff = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The maxBackoff.  
  
### getMaxBackoffBuilder()
    
    
    public Duration.Builder getMaxBackoffBuilder()

A task will be scheduled for retry between min_backoff and max_backoff duration after it fails, if the queue's RetryConfig specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [max_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration max_backoff = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)` |   
  
### getMaxBackoffOrBuilder()
    
    
    public DurationOrBuilder getMaxBackoffOrBuilder()

A task will be scheduled for retry between min_backoff and max_backoff duration after it fails, if the queue's RetryConfig specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [max_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration max_backoff = 4;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getMaxDoublings()
    
    
    public int getMaxDoublings()

The time between retries will double `max_doublings` times.

A task's retry interval starts at min_backoff, then doubles `max_doublings` times, then increases linearly, and finally retries at intervals of max_backoff up to max_attempts times.

For example, if min_backoff is 10s, max_backoff is 300s, and `max_doublings` is 3, then the a task will first be retried in 10s. The retry interval will double three times, and then increase linearly by 2^3 * 10s. Finally, the task will retry at intervals of max_backoff until the task has been attempted max_attempts times. Thus, the requests will retry at 10s, 20s, 40s, 80s, 160s, 240s, 300s, 300s, ....

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [max_doublings in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`int32 max_doublings = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maxDoublings.  
  
### getMaxRetryDuration()
    
    
    public Duration getMaxRetryDuration()

If positive, `max_retry_duration` specifies the time limit for retrying a failed task, measured from when the task was first attempted. Once `max_retry_duration` time has passed _and_ the task has been attempted max_attempts times, no further attempts are made and the task is deleted.

A zero (0) indicates an unlimited duration, up to the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For the maximum possible value or the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_retry_duration` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [task_age_limit in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration max_retry_duration = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The maxRetryDuration.  
  
### getMaxRetryDurationBuilder()
    
    
    public Duration.Builder getMaxRetryDurationBuilder()

If positive, `max_retry_duration` specifies the time limit for retrying a failed task, measured from when the task was first attempted. Once `max_retry_duration` time has passed _and_ the task has been attempted max_attempts times, no further attempts are made and the task is deleted.

A zero (0) indicates an unlimited duration, up to the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For the maximum possible value or the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_retry_duration` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [task_age_limit in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration max_retry_duration = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)` |   
  
### getMaxRetryDurationOrBuilder()
    
    
    public DurationOrBuilder getMaxRetryDurationOrBuilder()

If positive, `max_retry_duration` specifies the time limit for retrying a failed task, measured from when the task was first attempted. Once `max_retry_duration` time has passed _and_ the task has been attempted max_attempts times, no further attempts are made and the task is deleted.

A zero (0) indicates an unlimited duration, up to the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For the maximum possible value or the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_retry_duration` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [task_age_limit in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration max_retry_duration = 2;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getMinBackoff()
    
    
    public Duration getMinBackoff()

A task will be scheduled for retry between min_backoff and max_backoff duration after it fails, if the queue's RetryConfig specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `min_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [min_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration min_backoff = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The minBackoff.  
  
### getMinBackoffBuilder()
    
    
    public Duration.Builder getMinBackoffBuilder()

A task will be scheduled for retry between min_backoff and max_backoff duration after it fails, if the queue's RetryConfig specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `min_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [min_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration min_backoff = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)` |   
  
### getMinBackoffOrBuilder()
    
    
    public DurationOrBuilder getMinBackoffOrBuilder()

A task will be scheduled for retry between min_backoff and max_backoff duration after it fails, if the queue's RetryConfig specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `min_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [min_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration min_backoff = 3;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### hasMaxBackoff()
    
    
    public boolean hasMaxBackoff()

A task will be scheduled for retry between min_backoff and max_backoff duration after it fails, if the queue's RetryConfig specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [max_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration max_backoff = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maxBackoff field is set.  
  
### hasMaxRetryDuration()
    
    
    public boolean hasMaxRetryDuration()

If positive, `max_retry_duration` specifies the time limit for retrying a failed task, measured from when the task was first attempted. Once `max_retry_duration` time has passed _and_ the task has been attempted max_attempts times, no further attempts are made and the task is deleted.

A zero (0) indicates an unlimited duration, up to the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For the maximum possible value or the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_retry_duration` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [task_age_limit in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration max_retry_duration = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maxRetryDuration field is set.  
  
### hasMinBackoff()
    
    
    public boolean hasMinBackoff()

A task will be scheduled for retry between min_backoff and max_backoff duration after it fails, if the queue's RetryConfig specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `min_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [min_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration min_backoff = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the minBackoff field is set.  
  
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

### mergeFrom(RetryConfig other)
    
    
    public RetryConfig.Builder mergeFrom(RetryConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RetryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RetryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public RetryConfig.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RetryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public RetryConfig.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RetryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeMaxBackoff(Duration value)
    
    
    public RetryConfig.Builder mergeMaxBackoff(Duration value)

A task will be scheduled for retry between min_backoff and max_backoff duration after it fails, if the queue's RetryConfig specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [max_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration max_backoff = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RetryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder)` |   
  
### mergeMaxRetryDuration(Duration value)
    
    
    public RetryConfig.Builder mergeMaxRetryDuration(Duration value)

If positive, `max_retry_duration` specifies the time limit for retrying a failed task, measured from when the task was first attempted. Once `max_retry_duration` time has passed _and_ the task has been attempted max_attempts times, no further attempts are made and the task is deleted.

A zero (0) indicates an unlimited duration, up to the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For the maximum possible value or the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_retry_duration` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [task_age_limit in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration max_retry_duration = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RetryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder)` |   
  
### mergeMinBackoff(Duration value)
    
    
    public RetryConfig.Builder mergeMinBackoff(Duration value)

A task will be scheduled for retry between min_backoff and max_backoff duration after it fails, if the queue's RetryConfig specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `min_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [min_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration min_backoff = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RetryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder)` |   
  
### setMaxAttempts(int value)
    
    
    public RetryConfig.Builder setMaxAttempts(int value)

Number of attempts per task, including the first attempt. (If the first attempt fails, there will be `max_attempts - 1` retries.)

Must be greater than or equal to -1, which indicates unlimited attempts.

Cloud Tasks stops retrying only when `max_attempts` and `max_retry_duration` are both satisfied, or when the task is successfully executed. When the task has been attempted `max_attempts` times and when the `max_retry_duration` time has passed, no further attempts are made, and the task is deleted. If `max_attempts` is set to -1 and `max_retry_duration` is set to 0, the task is retried until the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit is reached.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [task_retry_limit in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`int32 max_attempts = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The maxAttempts to set.  
**Returns**  
---  
**Type** | **Description**  
`[RetryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder)` | This builder for chaining.  
  
### setMaxBackoff(Duration value)
    
    
    public RetryConfig.Builder setMaxBackoff(Duration value)

A task will be scheduled for retry between min_backoff and max_backoff duration after it fails, if the queue's RetryConfig specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [max_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration max_backoff = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RetryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder)` |   
  
### setMaxBackoff(Duration.Builder builderForValue)
    
    
    public RetryConfig.Builder setMaxBackoff(Duration.Builder builderForValue)

A task will be scheduled for retry between min_backoff and max_backoff duration after it fails, if the queue's RetryConfig specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [max_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration max_backoff = 4;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RetryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder)` |   
  
### setMaxDoublings(int value)
    
    
    public RetryConfig.Builder setMaxDoublings(int value)

The time between retries will double `max_doublings` times.

A task's retry interval starts at min_backoff, then doubles `max_doublings` times, then increases linearly, and finally retries at intervals of max_backoff up to max_attempts times.

For example, if min_backoff is 10s, max_backoff is 300s, and `max_doublings` is 3, then the a task will first be retried in 10s. The retry interval will double three times, and then increase linearly by 2^3 * 10s. Finally, the task will retry at intervals of max_backoff until the task has been attempted max_attempts times. Thus, the requests will retry at 10s, 20s, 40s, 80s, 160s, 240s, 300s, 300s, ....

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [max_doublings in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`int32 max_doublings = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The maxDoublings to set.  
**Returns**  
---  
**Type** | **Description**  
`[RetryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder)` | This builder for chaining.  
  
### setMaxRetryDuration(Duration value)
    
    
    public RetryConfig.Builder setMaxRetryDuration(Duration value)

If positive, `max_retry_duration` specifies the time limit for retrying a failed task, measured from when the task was first attempted. Once `max_retry_duration` time has passed _and_ the task has been attempted max_attempts times, no further attempts are made and the task is deleted.

A zero (0) indicates an unlimited duration, up to the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For the maximum possible value or the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_retry_duration` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [task_age_limit in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration max_retry_duration = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RetryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder)` |   
  
### setMaxRetryDuration(Duration.Builder builderForValue)
    
    
    public RetryConfig.Builder setMaxRetryDuration(Duration.Builder builderForValue)

If positive, `max_retry_duration` specifies the time limit for retrying a failed task, measured from when the task was first attempted. Once `max_retry_duration` time has passed _and_ the task has been attempted max_attempts times, no further attempts are made and the task is deleted.

A zero (0) indicates an unlimited duration, up to the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For the maximum possible value or the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_retry_duration` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [task_age_limit in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration max_retry_duration = 2;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RetryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder)` |   
  
### setMinBackoff(Duration value)
    
    
    public RetryConfig.Builder setMinBackoff(Duration value)

A task will be scheduled for retry between min_backoff and max_backoff duration after it fails, if the queue's RetryConfig specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `min_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [min_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration min_backoff = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RetryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder)` |   
  
### setMinBackoff(Duration.Builder builderForValue)
    
    
    public RetryConfig.Builder setMinBackoff(Duration.Builder builderForValue)

A task will be scheduled for retry between min_backoff and max_backoff duration after it fails, if the queue's RetryConfig specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `min_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [min_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

`.google.protobuf.Duration min_backoff = 3;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.Builder.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RetryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2.RetryConfig.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
