---
url: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder
title: Class PropertyQuota.Builder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:10:58.807132+00:00
---

# Class PropertyQuota.Builder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PropertyQuota.Builder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0 
    
    
    public static final class PropertyQuota.Builder extends GeneratedMessage.Builder<PropertyQuota.Builder> implements PropertyQuotaOrBuilder

Current state of all quotas for this Analytics Property. If any quota for a property is exhausted, all requests to that property will return Resource Exhausted errors.

Protobuf type `google.analytics.data.v1beta.PropertyQuota`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > PropertyQuota.Builder

## Implements

[PropertyQuotaOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuotaOrBuilder)

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
    
    
    public PropertyQuota build()

**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota)` |   
  
### buildPartial()
    
    
    public PropertyQuota buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota)` |   
  
### clear()
    
    
    public PropertyQuota.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearConcurrentRequests()
    
    
    public PropertyQuota.Builder clearConcurrentRequests()

Standard Analytics Properties can send up to 10 concurrent requests; Analytics 360 Properties can use up to 50 concurrent requests.

`.google.analytics.data.v1beta.QuotaStatus concurrent_requests = 3;`

**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### clearPotentiallyThresholdedRequestsPerHour()
    
    
    public PropertyQuota.Builder clearPotentiallyThresholdedRequestsPerHour()

Analytics Properties can send up to 120 requests with potentially thresholded dimensions per hour. In a batch request, each report request is individually counted for this quota if the request contains potentially thresholded dimensions.

` .google.analytics.data.v1beta.QuotaStatus potentially_thresholded_requests_per_hour = 5; `

**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### clearServerErrorsPerProjectPerHour()
    
    
    public PropertyQuota.Builder clearServerErrorsPerProjectPerHour()

Standard Analytics Properties and cloud project pairs can have up to 10 server errors per hour; Analytics 360 Properties and cloud project pairs can have up to 50 server errors per hour.

`.google.analytics.data.v1beta.QuotaStatus server_errors_per_project_per_hour = 4; `

**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### clearTokensPerDay()
    
    
    public PropertyQuota.Builder clearTokensPerDay()

Standard Analytics Properties can use up to 200,000 tokens per day; Analytics 360 Properties can use 2,000,000 tokens per day. Most requests consume fewer than 10 tokens.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_day = 1;`

**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### clearTokensPerHour()
    
    
    public PropertyQuota.Builder clearTokensPerHour()

Standard Analytics Properties can use up to 40,000 tokens per hour; Analytics 360 Properties can use 400,000 tokens per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_hour = 2;`

**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### clearTokensPerProjectPerHour()
    
    
    public PropertyQuota.Builder clearTokensPerProjectPerHour()

Analytics Properties can use up to 35% of their tokens per project per hour. This amounts to standard Analytics Properties can use up to 14,000 tokens per project per hour, and Analytics 360 Properties can use 140,000 tokens per project per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_project_per_hour = 6;`

**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### getConcurrentRequests()
    
    
    public QuotaStatus getConcurrentRequests()

Standard Analytics Properties can send up to 10 concurrent requests; Analytics 360 Properties can use up to 50 concurrent requests.

`.google.analytics.data.v1beta.QuotaStatus concurrent_requests = 3;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)` | The concurrentRequests.  
  
### getConcurrentRequestsBuilder()
    
    
    public QuotaStatus.Builder getConcurrentRequestsBuilder()

Standard Analytics Properties can send up to 10 concurrent requests; Analytics 360 Properties can use up to 50 concurrent requests.

`.google.analytics.data.v1beta.QuotaStatus concurrent_requests = 3;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatus.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus.Builder)` |   
  
### getConcurrentRequestsOrBuilder()
    
    
    public QuotaStatusOrBuilder getConcurrentRequestsOrBuilder()

Standard Analytics Properties can send up to 10 concurrent requests; Analytics 360 Properties can use up to 50 concurrent requests.

`.google.analytics.data.v1beta.QuotaStatus concurrent_requests = 3;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatusOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatusOrBuilder)` |   
  
### getDefaultInstanceForType()
    
    
    public PropertyQuota getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getPotentiallyThresholdedRequestsPerHour()
    
    
    public QuotaStatus getPotentiallyThresholdedRequestsPerHour()

Analytics Properties can send up to 120 requests with potentially thresholded dimensions per hour. In a batch request, each report request is individually counted for this quota if the request contains potentially thresholded dimensions.

` .google.analytics.data.v1beta.QuotaStatus potentially_thresholded_requests_per_hour = 5; `

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)` | The potentiallyThresholdedRequestsPerHour.  
  
### getPotentiallyThresholdedRequestsPerHourBuilder()
    
    
    public QuotaStatus.Builder getPotentiallyThresholdedRequestsPerHourBuilder()

Analytics Properties can send up to 120 requests with potentially thresholded dimensions per hour. In a batch request, each report request is individually counted for this quota if the request contains potentially thresholded dimensions.

` .google.analytics.data.v1beta.QuotaStatus potentially_thresholded_requests_per_hour = 5; `

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatus.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus.Builder)` |   
  
### getPotentiallyThresholdedRequestsPerHourOrBuilder()
    
    
    public QuotaStatusOrBuilder getPotentiallyThresholdedRequestsPerHourOrBuilder()

Analytics Properties can send up to 120 requests with potentially thresholded dimensions per hour. In a batch request, each report request is individually counted for this quota if the request contains potentially thresholded dimensions.

` .google.analytics.data.v1beta.QuotaStatus potentially_thresholded_requests_per_hour = 5; `

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatusOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatusOrBuilder)` |   
  
### getServerErrorsPerProjectPerHour()
    
    
    public QuotaStatus getServerErrorsPerProjectPerHour()

Standard Analytics Properties and cloud project pairs can have up to 10 server errors per hour; Analytics 360 Properties and cloud project pairs can have up to 50 server errors per hour.

`.google.analytics.data.v1beta.QuotaStatus server_errors_per_project_per_hour = 4; `

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)` | The serverErrorsPerProjectPerHour.  
  
### getServerErrorsPerProjectPerHourBuilder()
    
    
    public QuotaStatus.Builder getServerErrorsPerProjectPerHourBuilder()

Standard Analytics Properties and cloud project pairs can have up to 10 server errors per hour; Analytics 360 Properties and cloud project pairs can have up to 50 server errors per hour.

`.google.analytics.data.v1beta.QuotaStatus server_errors_per_project_per_hour = 4; `

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatus.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus.Builder)` |   
  
### getServerErrorsPerProjectPerHourOrBuilder()
    
    
    public QuotaStatusOrBuilder getServerErrorsPerProjectPerHourOrBuilder()

Standard Analytics Properties and cloud project pairs can have up to 10 server errors per hour; Analytics 360 Properties and cloud project pairs can have up to 50 server errors per hour.

`.google.analytics.data.v1beta.QuotaStatus server_errors_per_project_per_hour = 4; `

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatusOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatusOrBuilder)` |   
  
### getTokensPerDay()
    
    
    public QuotaStatus getTokensPerDay()

Standard Analytics Properties can use up to 200,000 tokens per day; Analytics 360 Properties can use 2,000,000 tokens per day. Most requests consume fewer than 10 tokens.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_day = 1;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)` | The tokensPerDay.  
  
### getTokensPerDayBuilder()
    
    
    public QuotaStatus.Builder getTokensPerDayBuilder()

Standard Analytics Properties can use up to 200,000 tokens per day; Analytics 360 Properties can use 2,000,000 tokens per day. Most requests consume fewer than 10 tokens.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_day = 1;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatus.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus.Builder)` |   
  
### getTokensPerDayOrBuilder()
    
    
    public QuotaStatusOrBuilder getTokensPerDayOrBuilder()

Standard Analytics Properties can use up to 200,000 tokens per day; Analytics 360 Properties can use 2,000,000 tokens per day. Most requests consume fewer than 10 tokens.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_day = 1;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatusOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatusOrBuilder)` |   
  
### getTokensPerHour()
    
    
    public QuotaStatus getTokensPerHour()

Standard Analytics Properties can use up to 40,000 tokens per hour; Analytics 360 Properties can use 400,000 tokens per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_hour = 2;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)` | The tokensPerHour.  
  
### getTokensPerHourBuilder()
    
    
    public QuotaStatus.Builder getTokensPerHourBuilder()

Standard Analytics Properties can use up to 40,000 tokens per hour; Analytics 360 Properties can use 400,000 tokens per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_hour = 2;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatus.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus.Builder)` |   
  
### getTokensPerHourOrBuilder()
    
    
    public QuotaStatusOrBuilder getTokensPerHourOrBuilder()

Standard Analytics Properties can use up to 40,000 tokens per hour; Analytics 360 Properties can use 400,000 tokens per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_hour = 2;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatusOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatusOrBuilder)` |   
  
### getTokensPerProjectPerHour()
    
    
    public QuotaStatus getTokensPerProjectPerHour()

Analytics Properties can use up to 35% of their tokens per project per hour. This amounts to standard Analytics Properties can use up to 14,000 tokens per project per hour, and Analytics 360 Properties can use 140,000 tokens per project per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_project_per_hour = 6;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)` | The tokensPerProjectPerHour.  
  
### getTokensPerProjectPerHourBuilder()
    
    
    public QuotaStatus.Builder getTokensPerProjectPerHourBuilder()

Analytics Properties can use up to 35% of their tokens per project per hour. This amounts to standard Analytics Properties can use up to 14,000 tokens per project per hour, and Analytics 360 Properties can use 140,000 tokens per project per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_project_per_hour = 6;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatus.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus.Builder)` |   
  
### getTokensPerProjectPerHourOrBuilder()
    
    
    public QuotaStatusOrBuilder getTokensPerProjectPerHourOrBuilder()

Analytics Properties can use up to 35% of their tokens per project per hour. This amounts to standard Analytics Properties can use up to 14,000 tokens per project per hour, and Analytics 360 Properties can use 140,000 tokens per project per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_project_per_hour = 6;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatusOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatusOrBuilder)` |   
  
### hasConcurrentRequests()
    
    
    public boolean hasConcurrentRequests()

Standard Analytics Properties can send up to 10 concurrent requests; Analytics 360 Properties can use up to 50 concurrent requests.

`.google.analytics.data.v1beta.QuotaStatus concurrent_requests = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the concurrentRequests field is set.  
  
### hasPotentiallyThresholdedRequestsPerHour()
    
    
    public boolean hasPotentiallyThresholdedRequestsPerHour()

Analytics Properties can send up to 120 requests with potentially thresholded dimensions per hour. In a batch request, each report request is individually counted for this quota if the request contains potentially thresholded dimensions.

` .google.analytics.data.v1beta.QuotaStatus potentially_thresholded_requests_per_hour = 5; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the potentiallyThresholdedRequestsPerHour field is set.  
  
### hasServerErrorsPerProjectPerHour()
    
    
    public boolean hasServerErrorsPerProjectPerHour()

Standard Analytics Properties and cloud project pairs can have up to 10 server errors per hour; Analytics 360 Properties and cloud project pairs can have up to 50 server errors per hour.

`.google.analytics.data.v1beta.QuotaStatus server_errors_per_project_per_hour = 4; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the serverErrorsPerProjectPerHour field is set.  
  
### hasTokensPerDay()
    
    
    public boolean hasTokensPerDay()

Standard Analytics Properties can use up to 200,000 tokens per day; Analytics 360 Properties can use 2,000,000 tokens per day. Most requests consume fewer than 10 tokens.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_day = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the tokensPerDay field is set.  
  
### hasTokensPerHour()
    
    
    public boolean hasTokensPerHour()

Standard Analytics Properties can use up to 40,000 tokens per hour; Analytics 360 Properties can use 400,000 tokens per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_hour = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the tokensPerHour field is set.  
  
### hasTokensPerProjectPerHour()
    
    
    public boolean hasTokensPerProjectPerHour()

Analytics Properties can use up to 35% of their tokens per project per hour. This amounts to standard Analytics Properties can use up to 14,000 tokens per project per hour, and Analytics 360 Properties can use 140,000 tokens per project per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_project_per_hour = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the tokensPerProjectPerHour field is set.  
  
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

### mergeConcurrentRequests(QuotaStatus value)
    
    
    public PropertyQuota.Builder mergeConcurrentRequests(QuotaStatus value)

Standard Analytics Properties can send up to 10 concurrent requests; Analytics 360 Properties can use up to 50 concurrent requests.

`.google.analytics.data.v1beta.QuotaStatus concurrent_requests = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### mergeFrom(PropertyQuota other)
    
    
    public PropertyQuota.Builder mergeFrom(PropertyQuota other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[PropertyQuota](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public PropertyQuota.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public PropertyQuota.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergePotentiallyThresholdedRequestsPerHour(QuotaStatus value)
    
    
    public PropertyQuota.Builder mergePotentiallyThresholdedRequestsPerHour(QuotaStatus value)

Analytics Properties can send up to 120 requests with potentially thresholded dimensions per hour. In a batch request, each report request is individually counted for this quota if the request contains potentially thresholded dimensions.

` .google.analytics.data.v1beta.QuotaStatus potentially_thresholded_requests_per_hour = 5; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### mergeServerErrorsPerProjectPerHour(QuotaStatus value)
    
    
    public PropertyQuota.Builder mergeServerErrorsPerProjectPerHour(QuotaStatus value)

Standard Analytics Properties and cloud project pairs can have up to 10 server errors per hour; Analytics 360 Properties and cloud project pairs can have up to 50 server errors per hour.

`.google.analytics.data.v1beta.QuotaStatus server_errors_per_project_per_hour = 4; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### mergeTokensPerDay(QuotaStatus value)
    
    
    public PropertyQuota.Builder mergeTokensPerDay(QuotaStatus value)

Standard Analytics Properties can use up to 200,000 tokens per day; Analytics 360 Properties can use 2,000,000 tokens per day. Most requests consume fewer than 10 tokens.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_day = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### mergeTokensPerHour(QuotaStatus value)
    
    
    public PropertyQuota.Builder mergeTokensPerHour(QuotaStatus value)

Standard Analytics Properties can use up to 40,000 tokens per hour; Analytics 360 Properties can use 400,000 tokens per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_hour = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### mergeTokensPerProjectPerHour(QuotaStatus value)
    
    
    public PropertyQuota.Builder mergeTokensPerProjectPerHour(QuotaStatus value)

Analytics Properties can use up to 35% of their tokens per project per hour. This amounts to standard Analytics Properties can use up to 14,000 tokens per project per hour, and Analytics 360 Properties can use 140,000 tokens per project per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_project_per_hour = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### setConcurrentRequests(QuotaStatus value)
    
    
    public PropertyQuota.Builder setConcurrentRequests(QuotaStatus value)

Standard Analytics Properties can send up to 10 concurrent requests; Analytics 360 Properties can use up to 50 concurrent requests.

`.google.analytics.data.v1beta.QuotaStatus concurrent_requests = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### setConcurrentRequests(QuotaStatus.Builder builderForValue)
    
    
    public PropertyQuota.Builder setConcurrentRequests(QuotaStatus.Builder builderForValue)

Standard Analytics Properties can send up to 10 concurrent requests; Analytics 360 Properties can use up to 50 concurrent requests.

`.google.analytics.data.v1beta.QuotaStatus concurrent_requests = 3;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[QuotaStatus.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### setPotentiallyThresholdedRequestsPerHour(QuotaStatus value)
    
    
    public PropertyQuota.Builder setPotentiallyThresholdedRequestsPerHour(QuotaStatus value)

Analytics Properties can send up to 120 requests with potentially thresholded dimensions per hour. In a batch request, each report request is individually counted for this quota if the request contains potentially thresholded dimensions.

` .google.analytics.data.v1beta.QuotaStatus potentially_thresholded_requests_per_hour = 5; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### setPotentiallyThresholdedRequestsPerHour(QuotaStatus.Builder builderForValue)
    
    
    public PropertyQuota.Builder setPotentiallyThresholdedRequestsPerHour(QuotaStatus.Builder builderForValue)

Analytics Properties can send up to 120 requests with potentially thresholded dimensions per hour. In a batch request, each report request is individually counted for this quota if the request contains potentially thresholded dimensions.

` .google.analytics.data.v1beta.QuotaStatus potentially_thresholded_requests_per_hour = 5; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[QuotaStatus.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### setServerErrorsPerProjectPerHour(QuotaStatus value)
    
    
    public PropertyQuota.Builder setServerErrorsPerProjectPerHour(QuotaStatus value)

Standard Analytics Properties and cloud project pairs can have up to 10 server errors per hour; Analytics 360 Properties and cloud project pairs can have up to 50 server errors per hour.

`.google.analytics.data.v1beta.QuotaStatus server_errors_per_project_per_hour = 4; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### setServerErrorsPerProjectPerHour(QuotaStatus.Builder builderForValue)
    
    
    public PropertyQuota.Builder setServerErrorsPerProjectPerHour(QuotaStatus.Builder builderForValue)

Standard Analytics Properties and cloud project pairs can have up to 10 server errors per hour; Analytics 360 Properties and cloud project pairs can have up to 50 server errors per hour.

`.google.analytics.data.v1beta.QuotaStatus server_errors_per_project_per_hour = 4; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[QuotaStatus.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### setTokensPerDay(QuotaStatus value)
    
    
    public PropertyQuota.Builder setTokensPerDay(QuotaStatus value)

Standard Analytics Properties can use up to 200,000 tokens per day; Analytics 360 Properties can use 2,000,000 tokens per day. Most requests consume fewer than 10 tokens.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_day = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### setTokensPerDay(QuotaStatus.Builder builderForValue)
    
    
    public PropertyQuota.Builder setTokensPerDay(QuotaStatus.Builder builderForValue)

Standard Analytics Properties can use up to 200,000 tokens per day; Analytics 360 Properties can use 2,000,000 tokens per day. Most requests consume fewer than 10 tokens.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_day = 1;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[QuotaStatus.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### setTokensPerHour(QuotaStatus value)
    
    
    public PropertyQuota.Builder setTokensPerHour(QuotaStatus value)

Standard Analytics Properties can use up to 40,000 tokens per hour; Analytics 360 Properties can use 400,000 tokens per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_hour = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### setTokensPerHour(QuotaStatus.Builder builderForValue)
    
    
    public PropertyQuota.Builder setTokensPerHour(QuotaStatus.Builder builderForValue)

Standard Analytics Properties can use up to 40,000 tokens per hour; Analytics 360 Properties can use 400,000 tokens per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_hour = 2;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[QuotaStatus.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### setTokensPerProjectPerHour(QuotaStatus value)
    
    
    public PropertyQuota.Builder setTokensPerProjectPerHour(QuotaStatus value)

Analytics Properties can use up to 35% of their tokens per project per hour. This amounts to standard Analytics Properties can use up to 14,000 tokens per project per hour, and Analytics 360 Properties can use 140,000 tokens per project per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_project_per_hour = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
### setTokensPerProjectPerHour(QuotaStatus.Builder builderForValue)
    
    
    public PropertyQuota.Builder setTokensPerProjectPerHour(QuotaStatus.Builder builderForValue)

Analytics Properties can use up to 35% of their tokens per project per hour. This amounts to standard Analytics Properties can use up to 14,000 tokens per project per hour, and Analytics 360 Properties can use 140,000 tokens per project per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_project_per_hour = 6;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[QuotaStatus.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PropertyQuota.Builder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuota.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
