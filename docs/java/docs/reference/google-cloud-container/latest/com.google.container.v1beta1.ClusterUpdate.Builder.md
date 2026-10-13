---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder
title: Class ClusterUpdate.Builder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:32:32.844702+00:00
---

# Class ClusterUpdate.Builder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ClusterUpdate.Builder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public static final class ClusterUpdate.Builder extends GeneratedMessage.Builder<ClusterUpdate.Builder> implements ClusterUpdateOrBuilder

ClusterUpdate describes an update to the cluster. Exactly one update can be applied to a cluster with each request, so at most one field can be provided.

Protobuf type `google.container.v1beta1.ClusterUpdate`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > ClusterUpdate.Builder

## Implements

[ClusterUpdateOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdateOrBuilder)

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

### addAllDesiredLocations(Iterable<String> values)
    
    
    public ClusterUpdate.Builder addAllDesiredLocations(Iterable<String> values)

The desired list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located.

This list must always include the cluster's primary zone.

Warning: changing cluster locations will update the locations of all node pools and will result in nodes being added and/or removed.

`repeated string desired_locations = 10;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The desiredLocations to add.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### addDesiredLocations(String value)
    
    
    public ClusterUpdate.Builder addDesiredLocations(String value)

The desired list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located.

This list must always include the cluster's primary zone.

Warning: changing cluster locations will update the locations of all node pools and will result in nodes being added and/or removed.

`repeated string desired_locations = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The desiredLocations to add.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### addDesiredLocationsBytes(ByteString value)
    
    
    public ClusterUpdate.Builder addDesiredLocationsBytes(ByteString value)

The desired list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located.

This list must always include the cluster's primary zone.

Warning: changing cluster locations will update the locations of all node pools and will result in nodes being added and/or removed.

`repeated string desired_locations = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes of the desiredLocations to add.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### build()
    
    
    public ClusterUpdate build()

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate)` |   
  
### buildPartial()
    
    
    public ClusterUpdate buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate)` |   
  
### clear()
    
    
    public ClusterUpdate.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearAdditionalPodRangesConfig()
    
    
    public ClusterUpdate.Builder clearAdditionalPodRangesConfig()

The additional pod ranges to be added to the cluster. These pod ranges can be used by node pools to allocate pod IPs.

`.google.container.v1beta1.AdditionalPodRangesConfig additional_pod_ranges_config = 120; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredAdditionalIpRangesConfig()
    
    
    public ClusterUpdate.Builder clearDesiredAdditionalIpRangesConfig()

The desired config for additional subnetworks attached to the cluster.

` .google.container.v1beta1.DesiredAdditionalIPRangesConfig desired_additional_ip_ranges_config = 145; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredAddonsConfig()
    
    
    public ClusterUpdate.Builder clearDesiredAddonsConfig()

Configurations for the various addons available to run in the cluster.

`.google.container.v1beta1.AddonsConfig desired_addons_config = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredAnonymousAuthenticationConfig()
    
    
    public ClusterUpdate.Builder clearDesiredAnonymousAuthenticationConfig()

Configuration for limiting anonymous access to all endpoints except the health checks.

` .google.container.v1beta1.AnonymousAuthenticationConfig desired_anonymous_authentication_config = 156; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredAuthenticatorGroupsConfig()
    
    
    public ClusterUpdate.Builder clearDesiredAuthenticatorGroupsConfig()

AuthenticatorGroupsConfig specifies the config for the cluster security groups settings.

` .google.container.v1beta1.AuthenticatorGroupsConfig desired_authenticator_groups_config = 63; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredAutoIpamConfig()
    
    
    public ClusterUpdate.Builder clearDesiredAutoIpamConfig()

AutoIpamConfig contains all information related to Auto IPAM

`.google.container.v1beta1.AutoIpamConfig desired_auto_ipam_config = 148;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredAutopilotClusterPolicyConfig()
    
    
    public ClusterUpdate.Builder clearDesiredAutopilotClusterPolicyConfig()

The desired autopilot cluster policies that to be enforced in the cluster.

` .google.container.v1beta1.ClusterPolicyConfig desired_autopilot_cluster_policy_config = 164; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredAutopilotWorkloadPolicyConfig()
    
    
    public ClusterUpdate.Builder clearDesiredAutopilotWorkloadPolicyConfig()

WorkloadPolicyConfig is the configuration related to GCW workload policy

` .google.container.v1beta1.WorkloadPolicyConfig desired_autopilot_workload_policy_config = 128; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredBinaryAuthorization()
    
    
    public ClusterUpdate.Builder clearDesiredBinaryAuthorization()

The desired configuration options for the Binary Authorization feature.

`.google.container.v1beta1.BinaryAuthorization desired_binary_authorization = 16;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredClusterAutoscaling()
    
    
    public ClusterUpdate.Builder clearDesiredClusterAutoscaling()

Cluster-level autoscaling configuration.

`.google.container.v1beta1.ClusterAutoscaling desired_cluster_autoscaling = 15;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredClusterTelemetry()
    
    
    public ClusterUpdate.Builder clearDesiredClusterTelemetry()

The desired telemetry integration for the cluster.

`.google.container.v1beta1.ClusterTelemetry desired_cluster_telemetry = 30;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredCompliancePostureConfig() (deprecated)
    
    
    public ClusterUpdate.Builder clearDesiredCompliancePostureConfig()

Deprecated: Compliance Posture is no longer supported. For more details, see <https://cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation>.

Enable/Disable Compliance Posture features for the cluster.

` optional .google.container.v1beta1.CompliancePostureConfig desired_compliance_posture_config = 140 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredContainerdConfig()
    
    
    public ClusterUpdate.Builder clearDesiredContainerdConfig()

The desired containerd config for the cluster.

`.google.container.v1beta1.ContainerdConfig desired_containerd_config = 134;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredControlPlaneEgress()
    
    
    public ClusterUpdate.Builder clearDesiredControlPlaneEgress()

The desired control plane egress control config for the cluster.

`.google.container.v1beta1.ControlPlaneEgress desired_control_plane_egress = 160;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredControlPlaneEndpointsConfig()
    
    
    public ClusterUpdate.Builder clearDesiredControlPlaneEndpointsConfig()

Control plane endpoints configuration.

` .google.container.v1beta1.ControlPlaneEndpointsConfig desired_control_plane_endpoints_config = 73; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredCostManagementConfig()
    
    
    public ClusterUpdate.Builder clearDesiredCostManagementConfig()

The desired configuration for the fine-grained cost management feature.

`.google.container.v1beta1.CostManagementConfig desired_cost_management_config = 49; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredDatabaseEncryption()
    
    
    public ClusterUpdate.Builder clearDesiredDatabaseEncryption()

Configuration of etcd encryption.

`.google.container.v1beta1.DatabaseEncryption desired_database_encryption = 46;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredDatapathProvider()
    
    
    public ClusterUpdate.Builder clearDesiredDatapathProvider()

The desired datapath provider for the cluster.

`.google.container.v1beta1.DatapathProvider desired_datapath_provider = 50;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### clearDesiredDefaultEnablePrivateNodes()
    
    
    public ClusterUpdate.Builder clearDesiredDefaultEnablePrivateNodes()

Override the default setting of whether future created nodes have private IP addresses only, namely NetworkConfig.default_enable_private_nodes

`optional bool desired_default_enable_private_nodes = 72;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### clearDesiredDefaultSnatStatus()
    
    
    public ClusterUpdate.Builder clearDesiredDefaultSnatStatus()

The desired status of whether to disable default sNAT for this cluster.

`.google.container.v1beta1.DefaultSnatStatus desired_default_snat_status = 28;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredDisableL4LbFirewallReconciliation()
    
    
    public ClusterUpdate.Builder clearDesiredDisableL4LbFirewallReconciliation()

Enable/Disable L4 LB VPC firewall reconciliation for the cluster.

`optional bool desired_disable_l4_lb_firewall_reconciliation = 149;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### clearDesiredDnsConfig()
    
    
    public ClusterUpdate.Builder clearDesiredDnsConfig()

DNSConfig contains clusterDNS config for this cluster.

`.google.container.v1beta1.DNSConfig desired_dns_config = 53;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredEnableCiliumClusterwideNetworkPolicy()
    
    
    public ClusterUpdate.Builder clearDesiredEnableCiliumClusterwideNetworkPolicy()

Enable/Disable Cilium Clusterwide Network Policy for the cluster.

`optional bool desired_enable_cilium_clusterwide_network_policy = 138;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### clearDesiredEnableFqdnNetworkPolicy()
    
    
    public ClusterUpdate.Builder clearDesiredEnableFqdnNetworkPolicy()

Enable/Disable FQDN Network Policy for the cluster.

`optional bool desired_enable_fqdn_network_policy = 126;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### clearDesiredEnableMultiNetworking()
    
    
    public ClusterUpdate.Builder clearDesiredEnableMultiNetworking()

Enable/Disable Multi-Networking for the cluster

`optional bool desired_enable_multi_networking = 135;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### clearDesiredEnablePrivateEndpoint() (deprecated)
    
    
    public ClusterUpdate.Builder clearDesiredEnablePrivateEndpoint()

**Deprecated.** _google.container.v1beta1.ClusterUpdate.desired_enable_private_endpoint is deprecated. See google/container/v1beta1/cluster_service.proto;l=4156_

Enable/Disable private endpoint for the cluster's master.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.enable_public_endpoint instead. Note that the value of enable_public_endpoint is reversed: if enable_private_endpoint is false, then enable_public_endpoint will be true.

`optional bool desired_enable_private_endpoint = 71 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### clearDesiredEnterpriseConfig() (deprecated)
    
    
    public ClusterUpdate.Builder clearDesiredEnterpriseConfig()

The desired enterprise configuration for the cluster.

Deprecated: GKE Enterprise features are now available without an Enterprise tier.

` .google.container.v1beta1.DesiredEnterpriseConfig desired_enterprise_config = 147 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredFleet()
    
    
    public ClusterUpdate.Builder clearDesiredFleet()

The desired fleet configuration for the cluster.

`.google.container.v1beta1.Fleet desired_fleet = 117;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredGatewayApiConfig()
    
    
    public ClusterUpdate.Builder clearDesiredGatewayApiConfig()

The desired config of Gateway API on this cluster.

`.google.container.v1beta1.GatewayAPIConfig desired_gateway_api_config = 114;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredGcfsConfig()
    
    
    public ClusterUpdate.Builder clearDesiredGcfsConfig()

The desired GCFS config for the cluster.

`.google.container.v1beta1.GcfsConfig desired_gcfs_config = 109;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredHostMaintenancePolicy()
    
    
    public ClusterUpdate.Builder clearDesiredHostMaintenancePolicy()

HostMaintenancePolicy contains the desired maintenance policy for the Google Compute Engine hosts.

`.google.container.v1beta1.HostMaintenancePolicy desired_host_maintenance_policy = 132; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredIdentityServiceConfig()
    
    
    public ClusterUpdate.Builder clearDesiredIdentityServiceConfig()

The desired Identity Service component configuration.

`.google.container.v1beta1.IdentityServiceConfig desired_identity_service_config = 66; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredImage()
    
    
    public ClusterUpdate.Builder clearDesiredImage()

The desired name of the image to use for this node. This is used to create clusters using a custom image.

`string desired_image = 44;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### clearDesiredImageProject()
    
    
    public ClusterUpdate.Builder clearDesiredImageProject()

The project containing the desired image to use for this node. This is used to create clusters using a custom image.

`string desired_image_project = 45;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### clearDesiredImageType()
    
    
    public ClusterUpdate.Builder clearDesiredImageType()

The desired image type for the node pool. NOTE: Set the "desired_node_pool" field as well.

`string desired_image_type = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### clearDesiredInTransitEncryptionConfig()
    
    
    public ClusterUpdate.Builder clearDesiredInTransitEncryptionConfig()

Specify the details of in-transit encryption. Now named inter-node transparent encryption.

` optional .google.container.v1beta1.InTransitEncryptionConfig desired_in_transit_encryption_config = 137; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### clearDesiredIntraNodeVisibilityConfig()
    
    
    public ClusterUpdate.Builder clearDesiredIntraNodeVisibilityConfig()

The desired config of Intra-node visibility.

` .google.container.v1beta1.IntraNodeVisibilityConfig desired_intra_node_visibility_config = 26; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredK8SBetaApis()
    
    
    public ClusterUpdate.Builder clearDesiredK8SBetaApis()

Beta APIs enabled for cluster.

`.google.container.v1beta1.K8sBetaAPIConfig desired_k8s_beta_apis = 131;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredL4IlbSubsettingConfig()
    
    
    public ClusterUpdate.Builder clearDesiredL4IlbSubsettingConfig()

The desired L4 Internal Load Balancer Subsetting configuration.

`.google.container.v1beta1.ILBSubsettingConfig desired_l4ilb_subsetting_config = 39; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredLocations()
    
    
    public ClusterUpdate.Builder clearDesiredLocations()

The desired list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located.

This list must always include the cluster's primary zone.

Warning: changing cluster locations will update the locations of all node pools and will result in nodes being added and/or removed.

`repeated string desired_locations = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### clearDesiredLoggingConfig()
    
    
    public ClusterUpdate.Builder clearDesiredLoggingConfig()

The desired logging configuration.

`.google.container.v1beta1.LoggingConfig desired_logging_config = 64;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredLoggingService()
    
    
    public ClusterUpdate.Builder clearDesiredLoggingService()

The logging service the cluster should use to write logs. Currently available options:

  * `logging.googleapis.com/kubernetes` \- The Cloud Logging service with a Kubernetes-native resource model
  * `logging.googleapis.com` \- The legacy Cloud Logging service (no longer available as of GKE 1.15).
  * `none` \- no logs will be exported from the cluster.

If left as an empty string,`logging.googleapis.com/kubernetes` will be used for GKE 1.14+ or `logging.googleapis.com` for earlier versions.




`string desired_logging_service = 19;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### clearDesiredManagedMachineLearningDiagnosticsConfig()
    
    
    public ClusterUpdate.Builder clearDesiredManagedMachineLearningDiagnosticsConfig()

The desired managed machine learning diagnostics configuration.

` .google.container.v1beta1.ManagedMachineLearningDiagnosticsConfig desired_managed_machine_learning_diagnostics_config = 166; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredManagedOpentelemetryConfig()
    
    
    public ClusterUpdate.Builder clearDesiredManagedOpentelemetryConfig()

The desired managed open telemetry configuration.

` .google.container.v1beta1.ManagedOpenTelemetryConfig desired_managed_opentelemetry_config = 163; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredMaster()
    
    
    public ClusterUpdate.Builder clearDesiredMaster()

Configuration for master components.

`.google.container.v1beta1.Master desired_master = 52;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredMasterAuthorizedNetworksConfig() (deprecated)
    
    
    public ClusterUpdate.Builder clearDesiredMasterAuthorizedNetworksConfig()

The desired configuration options for master authorized networks feature.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.authorized_networks_config instead.

` .google.container.v1beta1.MasterAuthorizedNetworksConfig desired_master_authorized_networks_config = 12 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredMasterVersion()
    
    
    public ClusterUpdate.Builder clearDesiredMasterVersion()

The Kubernetes version to change the master to. The only valid value is the latest supported version.

Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior:

  * "latest": picks the highest valid Kubernetes version
  * "1.X": picks the highest valid patch+gke.N patch in the 1.X version
  * "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
  * "1.X.Y-gke.N": picks an explicit Kubernetes version
  * "-": picks the default Kubernetes version



`string desired_master_version = 100;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### clearDesiredMeshCertificates()
    
    
    public ClusterUpdate.Builder clearDesiredMeshCertificates()

Configuration for issuance of mTLS keys and certificates to Kubernetes pods.

`.google.container.v1beta1.MeshCertificates desired_mesh_certificates = 67;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredMonitoringConfig()
    
    
    public ClusterUpdate.Builder clearDesiredMonitoringConfig()

The desired monitoring configuration.

`.google.container.v1beta1.MonitoringConfig desired_monitoring_config = 65;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredMonitoringService()
    
    
    public ClusterUpdate.Builder clearDesiredMonitoringService()

The monitoring service the cluster should use to write metrics. Currently available options:

  * `monitoring.googleapis.com/kubernetes` \- The Cloud Monitoring service with a Kubernetes-native resource model
  * `monitoring.googleapis.com` \- The legacy Cloud Monitoring service (no longer available as of GKE 1.15).
  * `none` \- No metrics will be exported from the cluster.

If left as an empty string,`monitoring.googleapis.com/kubernetes` will be used for GKE 1.14+ or `monitoring.googleapis.com` for earlier versions.




`string desired_monitoring_service = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### clearDesiredNetworkPerformanceConfig()
    
    
    public ClusterUpdate.Builder clearDesiredNetworkPerformanceConfig()

The desired network performance config.

` .google.container.v1beta1.NetworkConfig.ClusterNetworkPerformanceConfig desired_network_performance_config = 125; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredNetworkTierConfig()
    
    
    public ClusterUpdate.Builder clearDesiredNetworkTierConfig()

The desired network tier configuration for the cluster.

`.google.container.v1beta1.NetworkTierConfig desired_network_tier_config = 155;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredNodeCreationConfig()
    
    
    public ClusterUpdate.Builder clearDesiredNodeCreationConfig()

Optional. The desired NodeCreationConfig for the cluster.

` .google.container.v1beta1.NodeCreationConfig desired_node_creation_config = 171 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredNodeKubeletConfig()
    
    
    public ClusterUpdate.Builder clearDesiredNodeKubeletConfig()

The desired node kubelet config for the cluster.

`.google.container.v1beta1.NodeKubeletConfig desired_node_kubelet_config = 141;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredNodePoolAutoConfigKubeletConfig()
    
    
    public ClusterUpdate.Builder clearDesiredNodePoolAutoConfigKubeletConfig()

The desired node kubelet config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

` .google.container.v1beta1.NodeKubeletConfig desired_node_pool_auto_config_kubelet_config = 142; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredNodePoolAutoConfigLinuxNodeConfig()
    
    
    public ClusterUpdate.Builder clearDesiredNodePoolAutoConfigLinuxNodeConfig()

The desired Linux node config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

Currently only `cgroup_mode` can be set here.

` .google.container.v1beta1.LinuxNodeConfig desired_node_pool_auto_config_linux_node_config = 150; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredNodePoolAutoConfigNetworkTags()
    
    
    public ClusterUpdate.Builder clearDesiredNodePoolAutoConfigNetworkTags()

The desired network tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

`.google.container.v1beta1.NetworkTags desired_node_pool_auto_config_network_tags = 110; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredNodePoolAutoConfigResourceManagerTags()
    
    
    public ClusterUpdate.Builder clearDesiredNodePoolAutoConfigResourceManagerTags()

The desired resource manager tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

` .google.container.v1beta1.ResourceManagerTags desired_node_pool_auto_config_resource_manager_tags = 136; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredNodePoolAutoscaling()
    
    
    public ClusterUpdate.Builder clearDesiredNodePoolAutoscaling()

Autoscaler configuration for the node pool specified in desired_node_pool_id. If there is only one pool in the cluster and desired_node_pool_id is not provided then the change applies to that single node pool.

`.google.container.v1beta1.NodePoolAutoscaling desired_node_pool_autoscaling = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredNodePoolId()
    
    
    public ClusterUpdate.Builder clearDesiredNodePoolId()

The node pool to be upgraded. This field is mandatory if "desired_node_version", "desired_image_family", "desired_node_pool_autoscaling", or "desired_workload_metadata_config" is specified and there is more than one node pool on the cluster.

`string desired_node_pool_id = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### clearDesiredNodePoolLoggingConfig()
    
    
    public ClusterUpdate.Builder clearDesiredNodePoolLoggingConfig()

The desired node pool logging configuration defaults for the cluster.

`.google.container.v1beta1.NodePoolLoggingConfig desired_node_pool_logging_config = 116; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredNodePoolUpgradeConcurrencyConfig()
    
    
    public ClusterUpdate.Builder clearDesiredNodePoolUpgradeConcurrencyConfig()

The desired node pool upgrade concurrency configuration.

` .google.container.v1beta1.NodePoolUpgradeConcurrencyConfig desired_node_pool_upgrade_concurrency_config = 167; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredNodeVersion()
    
    
    public ClusterUpdate.Builder clearDesiredNodeVersion()

The Kubernetes version to change the nodes to (typically an upgrade).

Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior:

  * "latest": picks the highest valid Kubernetes version
  * "1.X": picks the highest valid patch+gke.N patch in the 1.X version
  * "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
  * "1.X.Y-gke.N": picks an explicit Kubernetes version
  * "-": picks the Kubernetes master version



`string desired_node_version = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### clearDesiredNotificationConfig()
    
    
    public ClusterUpdate.Builder clearDesiredNotificationConfig()

The desired notification configuration.

`.google.container.v1beta1.NotificationConfig desired_notification_config = 55;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredPodAutoscaling()
    
    
    public ClusterUpdate.Builder clearDesiredPodAutoscaling()

The desired config for pod autoscaling.

`.google.container.v1beta1.PodAutoscaling desired_pod_autoscaling = 113;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredPodSecurityPolicyConfig()
    
    
    public ClusterUpdate.Builder clearDesiredPodSecurityPolicyConfig()

The desired configuration options for the PodSecurityPolicy feature.

` .google.container.v1beta1.PodSecurityPolicyConfig desired_pod_security_policy_config = 14; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredPrivateClusterConfig() (deprecated)
    
    
    public ClusterUpdate.Builder clearDesiredPrivateClusterConfig()

The desired private cluster configuration. master_global_access_config is the only field that can be changed via this field. See also ClusterUpdate.desired_enable_private_endpoint for modifying other fields within PrivateClusterConfig.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.global_access instead.

` .google.container.v1beta1.PrivateClusterConfig desired_private_cluster_config = 25 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredPrivateIpv6GoogleAccess()
    
    
    public ClusterUpdate.Builder clearDesiredPrivateIpv6GoogleAccess()

The desired state of IPv6 connectivity to Google Services.

` .google.container.v1beta1.PrivateIPv6GoogleAccess desired_private_ipv6_google_access = 51; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### clearDesiredPrivilegedAdmissionConfig()
    
    
    public ClusterUpdate.Builder clearDesiredPrivilegedAdmissionConfig()

The desired privileged admission config for the cluster.

` .google.container.v1beta1.PrivilegedAdmissionConfig desired_privileged_admission_config = 159; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredProtectConfig() (deprecated)
    
    
    public ClusterUpdate.Builder clearDesiredProtectConfig()

Deprecated: Use DesiredSecurityPostureConfig instead. Enable/Disable Protect API features for the cluster.

` optional .google.container.v1beta1.ProtectConfig desired_protect_config = 112 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredRbacBindingConfig()
    
    
    public ClusterUpdate.Builder clearDesiredRbacBindingConfig()

RBACBindingConfig allows user to restrict ClusterRoleBindings an RoleBindings that can be created.

`optional .google.container.v1beta1.RBACBindingConfig desired_rbac_binding_config = 144; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredReleaseChannel()
    
    
    public ClusterUpdate.Builder clearDesiredReleaseChannel()

The desired release channel configuration.

`.google.container.v1beta1.ReleaseChannel desired_release_channel = 31;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredResourceUsageExportConfig()
    
    
    public ClusterUpdate.Builder clearDesiredResourceUsageExportConfig()

The desired configuration for exporting resource usage.

` .google.container.v1beta1.ResourceUsageExportConfig desired_resource_usage_export_config = 21; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredRollbackSafeUpgrade()
    
    
    public ClusterUpdate.Builder clearDesiredRollbackSafeUpgrade()

The desired rollback safe upgrade configuration.

`.google.container.v1beta1.RollbackSafeUpgrade desired_rollback_safe_upgrade = 161; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredScheduleUpgradeConfig()
    
    
    public ClusterUpdate.Builder clearDesiredScheduleUpgradeConfig()

Optional. The desired scheduled upgrades configuration for the cluster.

` .google.container.v1beta1.ScheduleUpgradeConfig desired_schedule_upgrade_config = 157 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredSecretManagerConfig()
    
    
    public ClusterUpdate.Builder clearDesiredSecretManagerConfig()

Enable/Disable Secret Manager Config.

` optional .google.container.v1beta1.SecretManagerConfig desired_secret_manager_config = 139; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredSecretSyncConfig()
    
    
    public ClusterUpdate.Builder clearDesiredSecretSyncConfig()

Configuration for sync Secret Manager secrets as k8s secrets.

`.google.container.v1beta1.SecretSyncConfig desired_secret_sync_config = 158;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredSecurityPostureConfig()
    
    
    public ClusterUpdate.Builder clearDesiredSecurityPostureConfig()

Enable/Disable Security Posture API features for the cluster.

`.google.container.v1beta1.SecurityPostureConfig desired_security_posture_config = 124; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredServiceExternalIpsConfig()
    
    
    public ClusterUpdate.Builder clearDesiredServiceExternalIpsConfig()

ServiceExternalIPsConfig specifies the config for the use of Services with ExternalIPs field.

` .google.container.v1beta1.ServiceExternalIPsConfig desired_service_external_ips_config = 60; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredShieldedNodes()
    
    
    public ClusterUpdate.Builder clearDesiredShieldedNodes()

Configuration for Shielded Nodes.

`.google.container.v1beta1.ShieldedNodes desired_shielded_nodes = 48;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredStackType()
    
    
    public ClusterUpdate.Builder clearDesiredStackType()

The desired stack type of the cluster. If a stack type is provided and does not match the current stack type of the cluster, update will attempt to change the stack type to the new type.

`.google.container.v1beta1.StackType desired_stack_type = 119;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### clearDesiredTpuConfig() (deprecated)
    
    
    public ClusterUpdate.Builder clearDesiredTpuConfig()

The desired Cloud TPU configuration. This field is deprecated due to the deprecation of 2VM TPU. The end of life date for 2VM TPU is 2025-04-25.

`.google.container.v1beta1.TpuConfig desired_tpu_config = 38 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredUserManagedKeysConfig()
    
    
    public ClusterUpdate.Builder clearDesiredUserManagedKeysConfig()

The desired user managed keys config for the cluster.

`.google.container.v1beta1.UserManagedKeysConfig desired_user_managed_keys_config = 152; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredVerticalPodAutoscaling()
    
    
    public ClusterUpdate.Builder clearDesiredVerticalPodAutoscaling()

Cluster-level Vertical Pod Autoscaling configuration.

`.google.container.v1beta1.VerticalPodAutoscaling desired_vertical_pod_autoscaling = 22; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredWorkloadAltsConfig()
    
    
    public ClusterUpdate.Builder clearDesiredWorkloadAltsConfig()

Configuration for direct-path (via ALTS) with workload identity. This feature is not officially supported for external customers in Kubernetes Engine when using Workload Identity.

`.google.container.v1beta1.WorkloadALTSConfig desired_workload_alts_config = 62;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredWorkloadCertificates()
    
    
    public ClusterUpdate.Builder clearDesiredWorkloadCertificates()

Configuration for issuance of mTLS keys and certificates to Kubernetes pods.

`.google.container.v1beta1.WorkloadCertificates desired_workload_certificates = 61; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearDesiredWorkloadIdentityConfig()
    
    
    public ClusterUpdate.Builder clearDesiredWorkloadIdentityConfig()

Configuration for Workload Identity.

`.google.container.v1beta1.WorkloadIdentityConfig desired_workload_identity_config = 47; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearEnableK8SBetaApis()
    
    
    public ClusterUpdate.Builder clearEnableK8SBetaApis()

Kubernetes open source beta apis enabled on the cluster. Only beta apis

`.google.container.v1beta1.K8sBetaAPIConfig enable_k8s_beta_apis = 122;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearEtag()
    
    
    public ClusterUpdate.Builder clearEtag()

The current etag of the cluster. If an etag is provided and does not match the current etag of the cluster, update will be blocked and an ABORTED error will be returned.

`string etag = 115;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### clearGkeAutoUpgradeConfig()
    
    
    public ClusterUpdate.Builder clearGkeAutoUpgradeConfig()

Configuration for GKE auto upgrade.

`.google.container.v1beta1.GkeAutoUpgradeConfig gke_auto_upgrade_config = 154;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearPrivateClusterConfig() (deprecated)
    
    
    public ClusterUpdate.Builder clearPrivateClusterConfig()

The desired private cluster configuration. Has no effect. Use desired_private_cluster_config instead.

` .google.container.v1beta1.PrivateClusterConfig private_cluster_config = 37 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearRemovedAdditionalPodRangesConfig()
    
    
    public ClusterUpdate.Builder clearRemovedAdditionalPodRangesConfig()

The additional pod ranges that are to be removed from the cluster. The pod ranges specified here must have been specified earlier in the 'additional_pod_ranges_config' argument.

` .google.container.v1beta1.AdditionalPodRangesConfig removed_additional_pod_ranges_config = 121; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### clearUserManagedKeysConfig() (deprecated)
    
    
    public ClusterUpdate.Builder clearUserManagedKeysConfig()

The Custom keys configuration for the cluster.

This field is deprecated. Use ClusterUpdate.desired_user_managed_keys_config instead.

` .google.container.v1beta1.UserManagedKeysConfig user_managed_keys_config = 143 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### getAdditionalPodRangesConfig()
    
    
    public AdditionalPodRangesConfig getAdditionalPodRangesConfig()

The additional pod ranges to be added to the cluster. These pod ranges can be used by node pools to allocate pod IPs.

`.google.container.v1beta1.AdditionalPodRangesConfig additional_pod_ranges_config = 120; `

**Returns**  
---  
**Type** | **Description**  
`[AdditionalPodRangesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AdditionalPodRangesConfig)` | The additionalPodRangesConfig.  
  
### getAdditionalPodRangesConfigBuilder()
    
    
    public AdditionalPodRangesConfig.Builder getAdditionalPodRangesConfigBuilder()

The additional pod ranges to be added to the cluster. These pod ranges can be used by node pools to allocate pod IPs.

`.google.container.v1beta1.AdditionalPodRangesConfig additional_pod_ranges_config = 120; `

**Returns**  
---  
**Type** | **Description**  
`[AdditionalPodRangesConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AdditionalPodRangesConfig.Builder)` |   
  
### getAdditionalPodRangesConfigOrBuilder()
    
    
    public AdditionalPodRangesConfigOrBuilder getAdditionalPodRangesConfigOrBuilder()

The additional pod ranges to be added to the cluster. These pod ranges can be used by node pools to allocate pod IPs.

`.google.container.v1beta1.AdditionalPodRangesConfig additional_pod_ranges_config = 120; `

**Returns**  
---  
**Type** | **Description**  
`[AdditionalPodRangesConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AdditionalPodRangesConfigOrBuilder)` |   
  
### getDefaultInstanceForType()
    
    
    public ClusterUpdate getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getDesiredAdditionalIpRangesConfig()
    
    
    public DesiredAdditionalIPRangesConfig getDesiredAdditionalIpRangesConfig()

The desired config for additional subnetworks attached to the cluster.

` .google.container.v1beta1.DesiredAdditionalIPRangesConfig desired_additional_ip_ranges_config = 145; `

**Returns**  
---  
**Type** | **Description**  
`[DesiredAdditionalIPRangesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DesiredAdditionalIPRangesConfig)` | The desiredAdditionalIpRangesConfig.  
  
### getDesiredAdditionalIpRangesConfigBuilder()
    
    
    public DesiredAdditionalIPRangesConfig.Builder getDesiredAdditionalIpRangesConfigBuilder()

The desired config for additional subnetworks attached to the cluster.

` .google.container.v1beta1.DesiredAdditionalIPRangesConfig desired_additional_ip_ranges_config = 145; `

**Returns**  
---  
**Type** | **Description**  
`[DesiredAdditionalIPRangesConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DesiredAdditionalIPRangesConfig.Builder)` |   
  
### getDesiredAdditionalIpRangesConfigOrBuilder()
    
    
    public DesiredAdditionalIPRangesConfigOrBuilder getDesiredAdditionalIpRangesConfigOrBuilder()

The desired config for additional subnetworks attached to the cluster.

` .google.container.v1beta1.DesiredAdditionalIPRangesConfig desired_additional_ip_ranges_config = 145; `

**Returns**  
---  
**Type** | **Description**  
`[DesiredAdditionalIPRangesConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DesiredAdditionalIPRangesConfigOrBuilder)` |   
  
### getDesiredAddonsConfig()
    
    
    public AddonsConfig getDesiredAddonsConfig()

Configurations for the various addons available to run in the cluster.

`.google.container.v1beta1.AddonsConfig desired_addons_config = 6;`

**Returns**  
---  
**Type** | **Description**  
`[AddonsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AddonsConfig)` | The desiredAddonsConfig.  
  
### getDesiredAddonsConfigBuilder()
    
    
    public AddonsConfig.Builder getDesiredAddonsConfigBuilder()

Configurations for the various addons available to run in the cluster.

`.google.container.v1beta1.AddonsConfig desired_addons_config = 6;`

**Returns**  
---  
**Type** | **Description**  
`[AddonsConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AddonsConfig.Builder)` |   
  
### getDesiredAddonsConfigOrBuilder()
    
    
    public AddonsConfigOrBuilder getDesiredAddonsConfigOrBuilder()

Configurations for the various addons available to run in the cluster.

`.google.container.v1beta1.AddonsConfig desired_addons_config = 6;`

**Returns**  
---  
**Type** | **Description**  
`[AddonsConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AddonsConfigOrBuilder)` |   
  
### getDesiredAnonymousAuthenticationConfig()
    
    
    public AnonymousAuthenticationConfig getDesiredAnonymousAuthenticationConfig()

Configuration for limiting anonymous access to all endpoints except the health checks.

` .google.container.v1beta1.AnonymousAuthenticationConfig desired_anonymous_authentication_config = 156; `

**Returns**  
---  
**Type** | **Description**  
`[AnonymousAuthenticationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AnonymousAuthenticationConfig)` | The desiredAnonymousAuthenticationConfig.  
  
### getDesiredAnonymousAuthenticationConfigBuilder()
    
    
    public AnonymousAuthenticationConfig.Builder getDesiredAnonymousAuthenticationConfigBuilder()

Configuration for limiting anonymous access to all endpoints except the health checks.

` .google.container.v1beta1.AnonymousAuthenticationConfig desired_anonymous_authentication_config = 156; `

**Returns**  
---  
**Type** | **Description**  
`[AnonymousAuthenticationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AnonymousAuthenticationConfig.Builder)` |   
  
### getDesiredAnonymousAuthenticationConfigOrBuilder()
    
    
    public AnonymousAuthenticationConfigOrBuilder getDesiredAnonymousAuthenticationConfigOrBuilder()

Configuration for limiting anonymous access to all endpoints except the health checks.

` .google.container.v1beta1.AnonymousAuthenticationConfig desired_anonymous_authentication_config = 156; `

**Returns**  
---  
**Type** | **Description**  
`[AnonymousAuthenticationConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AnonymousAuthenticationConfigOrBuilder)` |   
  
### getDesiredAuthenticatorGroupsConfig()
    
    
    public AuthenticatorGroupsConfig getDesiredAuthenticatorGroupsConfig()

AuthenticatorGroupsConfig specifies the config for the cluster security groups settings.

` .google.container.v1beta1.AuthenticatorGroupsConfig desired_authenticator_groups_config = 63; `

**Returns**  
---  
**Type** | **Description**  
`[AuthenticatorGroupsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AuthenticatorGroupsConfig)` | The desiredAuthenticatorGroupsConfig.  
  
### getDesiredAuthenticatorGroupsConfigBuilder()
    
    
    public AuthenticatorGroupsConfig.Builder getDesiredAuthenticatorGroupsConfigBuilder()

AuthenticatorGroupsConfig specifies the config for the cluster security groups settings.

` .google.container.v1beta1.AuthenticatorGroupsConfig desired_authenticator_groups_config = 63; `

**Returns**  
---  
**Type** | **Description**  
`[AuthenticatorGroupsConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AuthenticatorGroupsConfig.Builder)` |   
  
### getDesiredAuthenticatorGroupsConfigOrBuilder()
    
    
    public AuthenticatorGroupsConfigOrBuilder getDesiredAuthenticatorGroupsConfigOrBuilder()

AuthenticatorGroupsConfig specifies the config for the cluster security groups settings.

` .google.container.v1beta1.AuthenticatorGroupsConfig desired_authenticator_groups_config = 63; `

**Returns**  
---  
**Type** | **Description**  
`[AuthenticatorGroupsConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AuthenticatorGroupsConfigOrBuilder)` |   
  
### getDesiredAutoIpamConfig()
    
    
    public AutoIpamConfig getDesiredAutoIpamConfig()

AutoIpamConfig contains all information related to Auto IPAM

`.google.container.v1beta1.AutoIpamConfig desired_auto_ipam_config = 148;`

**Returns**  
---  
**Type** | **Description**  
`[AutoIpamConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AutoIpamConfig)` | The desiredAutoIpamConfig.  
  
### getDesiredAutoIpamConfigBuilder()
    
    
    public AutoIpamConfig.Builder getDesiredAutoIpamConfigBuilder()

AutoIpamConfig contains all information related to Auto IPAM

`.google.container.v1beta1.AutoIpamConfig desired_auto_ipam_config = 148;`

**Returns**  
---  
**Type** | **Description**  
`[AutoIpamConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AutoIpamConfig.Builder)` |   
  
### getDesiredAutoIpamConfigOrBuilder()
    
    
    public AutoIpamConfigOrBuilder getDesiredAutoIpamConfigOrBuilder()

AutoIpamConfig contains all information related to Auto IPAM

`.google.container.v1beta1.AutoIpamConfig desired_auto_ipam_config = 148;`

**Returns**  
---  
**Type** | **Description**  
`[AutoIpamConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AutoIpamConfigOrBuilder)` |   
  
### getDesiredAutopilotClusterPolicyConfig()
    
    
    public ClusterPolicyConfig getDesiredAutopilotClusterPolicyConfig()

The desired autopilot cluster policies that to be enforced in the cluster.

` .google.container.v1beta1.ClusterPolicyConfig desired_autopilot_cluster_policy_config = 164; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterPolicyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterPolicyConfig)` | The desiredAutopilotClusterPolicyConfig.  
  
### getDesiredAutopilotClusterPolicyConfigBuilder()
    
    
    public ClusterPolicyConfig.Builder getDesiredAutopilotClusterPolicyConfigBuilder()

The desired autopilot cluster policies that to be enforced in the cluster.

` .google.container.v1beta1.ClusterPolicyConfig desired_autopilot_cluster_policy_config = 164; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterPolicyConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterPolicyConfig.Builder)` |   
  
### getDesiredAutopilotClusterPolicyConfigOrBuilder()
    
    
    public ClusterPolicyConfigOrBuilder getDesiredAutopilotClusterPolicyConfigOrBuilder()

The desired autopilot cluster policies that to be enforced in the cluster.

` .google.container.v1beta1.ClusterPolicyConfig desired_autopilot_cluster_policy_config = 164; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterPolicyConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterPolicyConfigOrBuilder)` |   
  
### getDesiredAutopilotWorkloadPolicyConfig()
    
    
    public WorkloadPolicyConfig getDesiredAutopilotWorkloadPolicyConfig()

WorkloadPolicyConfig is the configuration related to GCW workload policy

` .google.container.v1beta1.WorkloadPolicyConfig desired_autopilot_workload_policy_config = 128; `

**Returns**  
---  
**Type** | **Description**  
`[WorkloadPolicyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadPolicyConfig)` | The desiredAutopilotWorkloadPolicyConfig.  
  
### getDesiredAutopilotWorkloadPolicyConfigBuilder()
    
    
    public WorkloadPolicyConfig.Builder getDesiredAutopilotWorkloadPolicyConfigBuilder()

WorkloadPolicyConfig is the configuration related to GCW workload policy

` .google.container.v1beta1.WorkloadPolicyConfig desired_autopilot_workload_policy_config = 128; `

**Returns**  
---  
**Type** | **Description**  
`[WorkloadPolicyConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadPolicyConfig.Builder)` |   
  
### getDesiredAutopilotWorkloadPolicyConfigOrBuilder()
    
    
    public WorkloadPolicyConfigOrBuilder getDesiredAutopilotWorkloadPolicyConfigOrBuilder()

WorkloadPolicyConfig is the configuration related to GCW workload policy

` .google.container.v1beta1.WorkloadPolicyConfig desired_autopilot_workload_policy_config = 128; `

**Returns**  
---  
**Type** | **Description**  
`[WorkloadPolicyConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadPolicyConfigOrBuilder)` |   
  
### getDesiredBinaryAuthorization()
    
    
    public BinaryAuthorization getDesiredBinaryAuthorization()

The desired configuration options for the Binary Authorization feature.

`.google.container.v1beta1.BinaryAuthorization desired_binary_authorization = 16;`

**Returns**  
---  
**Type** | **Description**  
`[BinaryAuthorization](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.BinaryAuthorization)` | The desiredBinaryAuthorization.  
  
### getDesiredBinaryAuthorizationBuilder()
    
    
    public BinaryAuthorization.Builder getDesiredBinaryAuthorizationBuilder()

The desired configuration options for the Binary Authorization feature.

`.google.container.v1beta1.BinaryAuthorization desired_binary_authorization = 16;`

**Returns**  
---  
**Type** | **Description**  
`[BinaryAuthorization.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.BinaryAuthorization.Builder)` |   
  
### getDesiredBinaryAuthorizationOrBuilder()
    
    
    public BinaryAuthorizationOrBuilder getDesiredBinaryAuthorizationOrBuilder()

The desired configuration options for the Binary Authorization feature.

`.google.container.v1beta1.BinaryAuthorization desired_binary_authorization = 16;`

**Returns**  
---  
**Type** | **Description**  
`[BinaryAuthorizationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.BinaryAuthorizationOrBuilder)` |   
  
### getDesiredClusterAutoscaling()
    
    
    public ClusterAutoscaling getDesiredClusterAutoscaling()

Cluster-level autoscaling configuration.

`.google.container.v1beta1.ClusterAutoscaling desired_cluster_autoscaling = 15;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterAutoscaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterAutoscaling)` | The desiredClusterAutoscaling.  
  
### getDesiredClusterAutoscalingBuilder()
    
    
    public ClusterAutoscaling.Builder getDesiredClusterAutoscalingBuilder()

Cluster-level autoscaling configuration.

`.google.container.v1beta1.ClusterAutoscaling desired_cluster_autoscaling = 15;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterAutoscaling.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterAutoscaling.Builder)` |   
  
### getDesiredClusterAutoscalingOrBuilder()
    
    
    public ClusterAutoscalingOrBuilder getDesiredClusterAutoscalingOrBuilder()

Cluster-level autoscaling configuration.

`.google.container.v1beta1.ClusterAutoscaling desired_cluster_autoscaling = 15;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterAutoscalingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterAutoscalingOrBuilder)` |   
  
### getDesiredClusterTelemetry()
    
    
    public ClusterTelemetry getDesiredClusterTelemetry()

The desired telemetry integration for the cluster.

`.google.container.v1beta1.ClusterTelemetry desired_cluster_telemetry = 30;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterTelemetry](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterTelemetry)` | The desiredClusterTelemetry.  
  
### getDesiredClusterTelemetryBuilder()
    
    
    public ClusterTelemetry.Builder getDesiredClusterTelemetryBuilder()

The desired telemetry integration for the cluster.

`.google.container.v1beta1.ClusterTelemetry desired_cluster_telemetry = 30;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterTelemetry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterTelemetry.Builder)` |   
  
### getDesiredClusterTelemetryOrBuilder()
    
    
    public ClusterTelemetryOrBuilder getDesiredClusterTelemetryOrBuilder()

The desired telemetry integration for the cluster.

`.google.container.v1beta1.ClusterTelemetry desired_cluster_telemetry = 30;`

**Returns**  
---  
**Type** | **Description**  
`[ClusterTelemetryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterTelemetryOrBuilder)` |   
  
### getDesiredCompliancePostureConfig() (deprecated)
    
    
    public CompliancePostureConfig getDesiredCompliancePostureConfig()

**Deprecated.** _google.container.v1beta1.ClusterUpdate.desired_compliance_posture_config is deprecated. See google/container/v1beta1/cluster_service.proto;l=4255_

Deprecated: Compliance Posture is no longer supported. For more details, see <https://cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation>.

Enable/Disable Compliance Posture features for the cluster.

` optional .google.container.v1beta1.CompliancePostureConfig desired_compliance_posture_config = 140 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[CompliancePostureConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.CompliancePostureConfig)` | The desiredCompliancePostureConfig.  
  
### getDesiredCompliancePostureConfigBuilder() (deprecated)
    
    
    public CompliancePostureConfig.Builder getDesiredCompliancePostureConfigBuilder()

Deprecated: Compliance Posture is no longer supported. For more details, see <https://cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation>.

Enable/Disable Compliance Posture features for the cluster.

` optional .google.container.v1beta1.CompliancePostureConfig desired_compliance_posture_config = 140 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[CompliancePostureConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.CompliancePostureConfig.Builder)` |   
  
### getDesiredCompliancePostureConfigOrBuilder() (deprecated)
    
    
    public CompliancePostureConfigOrBuilder getDesiredCompliancePostureConfigOrBuilder()

Deprecated: Compliance Posture is no longer supported. For more details, see <https://cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation>.

Enable/Disable Compliance Posture features for the cluster.

` optional .google.container.v1beta1.CompliancePostureConfig desired_compliance_posture_config = 140 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[CompliancePostureConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.CompliancePostureConfigOrBuilder)` |   
  
### getDesiredContainerdConfig()
    
    
    public ContainerdConfig getDesiredContainerdConfig()

The desired containerd config for the cluster.

`.google.container.v1beta1.ContainerdConfig desired_containerd_config = 134;`

**Returns**  
---  
**Type** | **Description**  
`[ContainerdConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ContainerdConfig)` | The desiredContainerdConfig.  
  
### getDesiredContainerdConfigBuilder()
    
    
    public ContainerdConfig.Builder getDesiredContainerdConfigBuilder()

The desired containerd config for the cluster.

`.google.container.v1beta1.ContainerdConfig desired_containerd_config = 134;`

**Returns**  
---  
**Type** | **Description**  
`[ContainerdConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ContainerdConfig.Builder)` |   
  
### getDesiredContainerdConfigOrBuilder()
    
    
    public ContainerdConfigOrBuilder getDesiredContainerdConfigOrBuilder()

The desired containerd config for the cluster.

`.google.container.v1beta1.ContainerdConfig desired_containerd_config = 134;`

**Returns**  
---  
**Type** | **Description**  
`[ContainerdConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ContainerdConfigOrBuilder)` |   
  
### getDesiredControlPlaneEgress()
    
    
    public ControlPlaneEgress getDesiredControlPlaneEgress()

The desired control plane egress control config for the cluster.

`.google.container.v1beta1.ControlPlaneEgress desired_control_plane_egress = 160;`

**Returns**  
---  
**Type** | **Description**  
`[ControlPlaneEgress](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ControlPlaneEgress)` | The desiredControlPlaneEgress.  
  
### getDesiredControlPlaneEgressBuilder()
    
    
    public ControlPlaneEgress.Builder getDesiredControlPlaneEgressBuilder()

The desired control plane egress control config for the cluster.

`.google.container.v1beta1.ControlPlaneEgress desired_control_plane_egress = 160;`

**Returns**  
---  
**Type** | **Description**  
`[ControlPlaneEgress.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ControlPlaneEgress.Builder)` |   
  
### getDesiredControlPlaneEgressOrBuilder()
    
    
    public ControlPlaneEgressOrBuilder getDesiredControlPlaneEgressOrBuilder()

The desired control plane egress control config for the cluster.

`.google.container.v1beta1.ControlPlaneEgress desired_control_plane_egress = 160;`

**Returns**  
---  
**Type** | **Description**  
`[ControlPlaneEgressOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ControlPlaneEgressOrBuilder)` |   
  
### getDesiredControlPlaneEndpointsConfig()
    
    
    public ControlPlaneEndpointsConfig getDesiredControlPlaneEndpointsConfig()

Control plane endpoints configuration.

` .google.container.v1beta1.ControlPlaneEndpointsConfig desired_control_plane_endpoints_config = 73; `

**Returns**  
---  
**Type** | **Description**  
`[ControlPlaneEndpointsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ControlPlaneEndpointsConfig)` | The desiredControlPlaneEndpointsConfig.  
  
### getDesiredControlPlaneEndpointsConfigBuilder()
    
    
    public ControlPlaneEndpointsConfig.Builder getDesiredControlPlaneEndpointsConfigBuilder()

Control plane endpoints configuration.

` .google.container.v1beta1.ControlPlaneEndpointsConfig desired_control_plane_endpoints_config = 73; `

**Returns**  
---  
**Type** | **Description**  
`[ControlPlaneEndpointsConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ControlPlaneEndpointsConfig.Builder)` |   
  
### getDesiredControlPlaneEndpointsConfigOrBuilder()
    
    
    public ControlPlaneEndpointsConfigOrBuilder getDesiredControlPlaneEndpointsConfigOrBuilder()

Control plane endpoints configuration.

` .google.container.v1beta1.ControlPlaneEndpointsConfig desired_control_plane_endpoints_config = 73; `

**Returns**  
---  
**Type** | **Description**  
`[ControlPlaneEndpointsConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ControlPlaneEndpointsConfigOrBuilder)` |   
  
### getDesiredCostManagementConfig()
    
    
    public CostManagementConfig getDesiredCostManagementConfig()

The desired configuration for the fine-grained cost management feature.

`.google.container.v1beta1.CostManagementConfig desired_cost_management_config = 49; `

**Returns**  
---  
**Type** | **Description**  
`[CostManagementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.CostManagementConfig)` | The desiredCostManagementConfig.  
  
### getDesiredCostManagementConfigBuilder()
    
    
    public CostManagementConfig.Builder getDesiredCostManagementConfigBuilder()

The desired configuration for the fine-grained cost management feature.

`.google.container.v1beta1.CostManagementConfig desired_cost_management_config = 49; `

**Returns**  
---  
**Type** | **Description**  
`[CostManagementConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.CostManagementConfig.Builder)` |   
  
### getDesiredCostManagementConfigOrBuilder()
    
    
    public CostManagementConfigOrBuilder getDesiredCostManagementConfigOrBuilder()

The desired configuration for the fine-grained cost management feature.

`.google.container.v1beta1.CostManagementConfig desired_cost_management_config = 49; `

**Returns**  
---  
**Type** | **Description**  
`[CostManagementConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.CostManagementConfigOrBuilder)` |   
  
### getDesiredDatabaseEncryption()
    
    
    public DatabaseEncryption getDesiredDatabaseEncryption()

Configuration of etcd encryption.

`.google.container.v1beta1.DatabaseEncryption desired_database_encryption = 46;`

**Returns**  
---  
**Type** | **Description**  
`[DatabaseEncryption](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DatabaseEncryption)` | The desiredDatabaseEncryption.  
  
### getDesiredDatabaseEncryptionBuilder()
    
    
    public DatabaseEncryption.Builder getDesiredDatabaseEncryptionBuilder()

Configuration of etcd encryption.

`.google.container.v1beta1.DatabaseEncryption desired_database_encryption = 46;`

**Returns**  
---  
**Type** | **Description**  
`[DatabaseEncryption.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DatabaseEncryption.Builder)` |   
  
### getDesiredDatabaseEncryptionOrBuilder()
    
    
    public DatabaseEncryptionOrBuilder getDesiredDatabaseEncryptionOrBuilder()

Configuration of etcd encryption.

`.google.container.v1beta1.DatabaseEncryption desired_database_encryption = 46;`

**Returns**  
---  
**Type** | **Description**  
`[DatabaseEncryptionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DatabaseEncryptionOrBuilder)` |   
  
### getDesiredDatapathProvider()
    
    
    public DatapathProvider getDesiredDatapathProvider()

The desired datapath provider for the cluster.

`.google.container.v1beta1.DatapathProvider desired_datapath_provider = 50;`

**Returns**  
---  
**Type** | **Description**  
`[DatapathProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DatapathProvider)` | The desiredDatapathProvider.  
  
### getDesiredDatapathProviderValue()
    
    
    public int getDesiredDatapathProviderValue()

The desired datapath provider for the cluster.

`.google.container.v1beta1.DatapathProvider desired_datapath_provider = 50;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for desiredDatapathProvider.  
  
### getDesiredDefaultEnablePrivateNodes()
    
    
    public boolean getDesiredDefaultEnablePrivateNodes()

Override the default setting of whether future created nodes have private IP addresses only, namely NetworkConfig.default_enable_private_nodes

`optional bool desired_default_enable_private_nodes = 72;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The desiredDefaultEnablePrivateNodes.  
  
### getDesiredDefaultSnatStatus()
    
    
    public DefaultSnatStatus getDesiredDefaultSnatStatus()

The desired status of whether to disable default sNAT for this cluster.

`.google.container.v1beta1.DefaultSnatStatus desired_default_snat_status = 28;`

**Returns**  
---  
**Type** | **Description**  
`[DefaultSnatStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DefaultSnatStatus)` | The desiredDefaultSnatStatus.  
  
### getDesiredDefaultSnatStatusBuilder()
    
    
    public DefaultSnatStatus.Builder getDesiredDefaultSnatStatusBuilder()

The desired status of whether to disable default sNAT for this cluster.

`.google.container.v1beta1.DefaultSnatStatus desired_default_snat_status = 28;`

**Returns**  
---  
**Type** | **Description**  
`[DefaultSnatStatus.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DefaultSnatStatus.Builder)` |   
  
### getDesiredDefaultSnatStatusOrBuilder()
    
    
    public DefaultSnatStatusOrBuilder getDesiredDefaultSnatStatusOrBuilder()

The desired status of whether to disable default sNAT for this cluster.

`.google.container.v1beta1.DefaultSnatStatus desired_default_snat_status = 28;`

**Returns**  
---  
**Type** | **Description**  
`[DefaultSnatStatusOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DefaultSnatStatusOrBuilder)` |   
  
### getDesiredDisableL4LbFirewallReconciliation()
    
    
    public boolean getDesiredDisableL4LbFirewallReconciliation()

Enable/Disable L4 LB VPC firewall reconciliation for the cluster.

`optional bool desired_disable_l4_lb_firewall_reconciliation = 149;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The desiredDisableL4LbFirewallReconciliation.  
  
### getDesiredDnsConfig()
    
    
    public DNSConfig getDesiredDnsConfig()

DNSConfig contains clusterDNS config for this cluster.

`.google.container.v1beta1.DNSConfig desired_dns_config = 53;`

**Returns**  
---  
**Type** | **Description**  
`[DNSConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DNSConfig)` | The desiredDnsConfig.  
  
### getDesiredDnsConfigBuilder()
    
    
    public DNSConfig.Builder getDesiredDnsConfigBuilder()

DNSConfig contains clusterDNS config for this cluster.

`.google.container.v1beta1.DNSConfig desired_dns_config = 53;`

**Returns**  
---  
**Type** | **Description**  
`[DNSConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DNSConfig.Builder)` |   
  
### getDesiredDnsConfigOrBuilder()
    
    
    public DNSConfigOrBuilder getDesiredDnsConfigOrBuilder()

DNSConfig contains clusterDNS config for this cluster.

`.google.container.v1beta1.DNSConfig desired_dns_config = 53;`

**Returns**  
---  
**Type** | **Description**  
`[DNSConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DNSConfigOrBuilder)` |   
  
### getDesiredEnableCiliumClusterwideNetworkPolicy()
    
    
    public boolean getDesiredEnableCiliumClusterwideNetworkPolicy()

Enable/Disable Cilium Clusterwide Network Policy for the cluster.

`optional bool desired_enable_cilium_clusterwide_network_policy = 138;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The desiredEnableCiliumClusterwideNetworkPolicy.  
  
### getDesiredEnableFqdnNetworkPolicy()
    
    
    public boolean getDesiredEnableFqdnNetworkPolicy()

Enable/Disable FQDN Network Policy for the cluster.

`optional bool desired_enable_fqdn_network_policy = 126;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The desiredEnableFqdnNetworkPolicy.  
  
### getDesiredEnableMultiNetworking()
    
    
    public boolean getDesiredEnableMultiNetworking()

Enable/Disable Multi-Networking for the cluster

`optional bool desired_enable_multi_networking = 135;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The desiredEnableMultiNetworking.  
  
### getDesiredEnablePrivateEndpoint() (deprecated)
    
    
    public boolean getDesiredEnablePrivateEndpoint()

**Deprecated.** _google.container.v1beta1.ClusterUpdate.desired_enable_private_endpoint is deprecated. See google/container/v1beta1/cluster_service.proto;l=4156_

Enable/Disable private endpoint for the cluster's master.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.enable_public_endpoint instead. Note that the value of enable_public_endpoint is reversed: if enable_private_endpoint is false, then enable_public_endpoint will be true.

`optional bool desired_enable_private_endpoint = 71 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The desiredEnablePrivateEndpoint.  
  
### getDesiredEnterpriseConfig() (deprecated)
    
    
    public DesiredEnterpriseConfig getDesiredEnterpriseConfig()

**Deprecated.** _google.container.v1beta1.ClusterUpdate.desired_enterprise_config is deprecated. See google/container/v1beta1/cluster_service.proto;l=4284_

The desired enterprise configuration for the cluster.

Deprecated: GKE Enterprise features are now available without an Enterprise tier.

` .google.container.v1beta1.DesiredEnterpriseConfig desired_enterprise_config = 147 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[DesiredEnterpriseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DesiredEnterpriseConfig)` | The desiredEnterpriseConfig.  
  
### getDesiredEnterpriseConfigBuilder() (deprecated)
    
    
    public DesiredEnterpriseConfig.Builder getDesiredEnterpriseConfigBuilder()

The desired enterprise configuration for the cluster.

Deprecated: GKE Enterprise features are now available without an Enterprise tier.

` .google.container.v1beta1.DesiredEnterpriseConfig desired_enterprise_config = 147 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[DesiredEnterpriseConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DesiredEnterpriseConfig.Builder)` |   
  
### getDesiredEnterpriseConfigOrBuilder() (deprecated)
    
    
    public DesiredEnterpriseConfigOrBuilder getDesiredEnterpriseConfigOrBuilder()

The desired enterprise configuration for the cluster.

Deprecated: GKE Enterprise features are now available without an Enterprise tier.

` .google.container.v1beta1.DesiredEnterpriseConfig desired_enterprise_config = 147 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[DesiredEnterpriseConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DesiredEnterpriseConfigOrBuilder)` |   
  
### getDesiredFleet()
    
    
    public Fleet getDesiredFleet()

The desired fleet configuration for the cluster.

`.google.container.v1beta1.Fleet desired_fleet = 117;`

**Returns**  
---  
**Type** | **Description**  
`[Fleet](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Fleet)` | The desiredFleet.  
  
### getDesiredFleetBuilder()
    
    
    public Fleet.Builder getDesiredFleetBuilder()

The desired fleet configuration for the cluster.

`.google.container.v1beta1.Fleet desired_fleet = 117;`

**Returns**  
---  
**Type** | **Description**  
`[Fleet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Fleet.Builder)` |   
  
### getDesiredFleetOrBuilder()
    
    
    public FleetOrBuilder getDesiredFleetOrBuilder()

The desired fleet configuration for the cluster.

`.google.container.v1beta1.Fleet desired_fleet = 117;`

**Returns**  
---  
**Type** | **Description**  
`[FleetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.FleetOrBuilder)` |   
  
### getDesiredGatewayApiConfig()
    
    
    public GatewayAPIConfig getDesiredGatewayApiConfig()

The desired config of Gateway API on this cluster.

`.google.container.v1beta1.GatewayAPIConfig desired_gateway_api_config = 114;`

**Returns**  
---  
**Type** | **Description**  
`[GatewayAPIConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GatewayAPIConfig)` | The desiredGatewayApiConfig.  
  
### getDesiredGatewayApiConfigBuilder()
    
    
    public GatewayAPIConfig.Builder getDesiredGatewayApiConfigBuilder()

The desired config of Gateway API on this cluster.

`.google.container.v1beta1.GatewayAPIConfig desired_gateway_api_config = 114;`

**Returns**  
---  
**Type** | **Description**  
`[GatewayAPIConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GatewayAPIConfig.Builder)` |   
  
### getDesiredGatewayApiConfigOrBuilder()
    
    
    public GatewayAPIConfigOrBuilder getDesiredGatewayApiConfigOrBuilder()

The desired config of Gateway API on this cluster.

`.google.container.v1beta1.GatewayAPIConfig desired_gateway_api_config = 114;`

**Returns**  
---  
**Type** | **Description**  
`[GatewayAPIConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GatewayAPIConfigOrBuilder)` |   
  
### getDesiredGcfsConfig()
    
    
    public GcfsConfig getDesiredGcfsConfig()

The desired GCFS config for the cluster.

`.google.container.v1beta1.GcfsConfig desired_gcfs_config = 109;`

**Returns**  
---  
**Type** | **Description**  
`[GcfsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GcfsConfig)` | The desiredGcfsConfig.  
  
### getDesiredGcfsConfigBuilder()
    
    
    public GcfsConfig.Builder getDesiredGcfsConfigBuilder()

The desired GCFS config for the cluster.

`.google.container.v1beta1.GcfsConfig desired_gcfs_config = 109;`

**Returns**  
---  
**Type** | **Description**  
`[GcfsConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GcfsConfig.Builder)` |   
  
### getDesiredGcfsConfigOrBuilder()
    
    
    public GcfsConfigOrBuilder getDesiredGcfsConfigOrBuilder()

The desired GCFS config for the cluster.

`.google.container.v1beta1.GcfsConfig desired_gcfs_config = 109;`

**Returns**  
---  
**Type** | **Description**  
`[GcfsConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GcfsConfigOrBuilder)` |   
  
### getDesiredHostMaintenancePolicy()
    
    
    public HostMaintenancePolicy getDesiredHostMaintenancePolicy()

HostMaintenancePolicy contains the desired maintenance policy for the Google Compute Engine hosts.

`.google.container.v1beta1.HostMaintenancePolicy desired_host_maintenance_policy = 132; `

**Returns**  
---  
**Type** | **Description**  
`[HostMaintenancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.HostMaintenancePolicy)` | The desiredHostMaintenancePolicy.  
  
### getDesiredHostMaintenancePolicyBuilder()
    
    
    public HostMaintenancePolicy.Builder getDesiredHostMaintenancePolicyBuilder()

HostMaintenancePolicy contains the desired maintenance policy for the Google Compute Engine hosts.

`.google.container.v1beta1.HostMaintenancePolicy desired_host_maintenance_policy = 132; `

**Returns**  
---  
**Type** | **Description**  
`[HostMaintenancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.HostMaintenancePolicy.Builder)` |   
  
### getDesiredHostMaintenancePolicyOrBuilder()
    
    
    public HostMaintenancePolicyOrBuilder getDesiredHostMaintenancePolicyOrBuilder()

HostMaintenancePolicy contains the desired maintenance policy for the Google Compute Engine hosts.

`.google.container.v1beta1.HostMaintenancePolicy desired_host_maintenance_policy = 132; `

**Returns**  
---  
**Type** | **Description**  
`[HostMaintenancePolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.HostMaintenancePolicyOrBuilder)` |   
  
### getDesiredIdentityServiceConfig()
    
    
    public IdentityServiceConfig getDesiredIdentityServiceConfig()

The desired Identity Service component configuration.

`.google.container.v1beta1.IdentityServiceConfig desired_identity_service_config = 66; `

**Returns**  
---  
**Type** | **Description**  
`[IdentityServiceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.IdentityServiceConfig)` | The desiredIdentityServiceConfig.  
  
### getDesiredIdentityServiceConfigBuilder()
    
    
    public IdentityServiceConfig.Builder getDesiredIdentityServiceConfigBuilder()

The desired Identity Service component configuration.

`.google.container.v1beta1.IdentityServiceConfig desired_identity_service_config = 66; `

**Returns**  
---  
**Type** | **Description**  
`[IdentityServiceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.IdentityServiceConfig.Builder)` |   
  
### getDesiredIdentityServiceConfigOrBuilder()
    
    
    public IdentityServiceConfigOrBuilder getDesiredIdentityServiceConfigOrBuilder()

The desired Identity Service component configuration.

`.google.container.v1beta1.IdentityServiceConfig desired_identity_service_config = 66; `

**Returns**  
---  
**Type** | **Description**  
`[IdentityServiceConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.IdentityServiceConfigOrBuilder)` |   
  
### getDesiredImage()
    
    
    public String getDesiredImage()

The desired name of the image to use for this node. This is used to create clusters using a custom image.

`string desired_image = 44;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The desiredImage.  
  
### getDesiredImageBytes()
    
    
    public ByteString getDesiredImageBytes()

The desired name of the image to use for this node. This is used to create clusters using a custom image.

`string desired_image = 44;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for desiredImage.  
  
### getDesiredImageProject()
    
    
    public String getDesiredImageProject()

The project containing the desired image to use for this node. This is used to create clusters using a custom image.

`string desired_image_project = 45;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The desiredImageProject.  
  
### getDesiredImageProjectBytes()
    
    
    public ByteString getDesiredImageProjectBytes()

The project containing the desired image to use for this node. This is used to create clusters using a custom image.

`string desired_image_project = 45;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for desiredImageProject.  
  
### getDesiredImageType()
    
    
    public String getDesiredImageType()

The desired image type for the node pool. NOTE: Set the "desired_node_pool" field as well.

`string desired_image_type = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The desiredImageType.  
  
### getDesiredImageTypeBytes()
    
    
    public ByteString getDesiredImageTypeBytes()

The desired image type for the node pool. NOTE: Set the "desired_node_pool" field as well.

`string desired_image_type = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for desiredImageType.  
  
### getDesiredInTransitEncryptionConfig()
    
    
    public InTransitEncryptionConfig getDesiredInTransitEncryptionConfig()

Specify the details of in-transit encryption. Now named inter-node transparent encryption.

` optional .google.container.v1beta1.InTransitEncryptionConfig desired_in_transit_encryption_config = 137; `

**Returns**  
---  
**Type** | **Description**  
`[InTransitEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.InTransitEncryptionConfig)` | The desiredInTransitEncryptionConfig.  
  
### getDesiredInTransitEncryptionConfigValue()
    
    
    public int getDesiredInTransitEncryptionConfigValue()

Specify the details of in-transit encryption. Now named inter-node transparent encryption.

` optional .google.container.v1beta1.InTransitEncryptionConfig desired_in_transit_encryption_config = 137; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for desiredInTransitEncryptionConfig.  
  
### getDesiredIntraNodeVisibilityConfig()
    
    
    public IntraNodeVisibilityConfig getDesiredIntraNodeVisibilityConfig()

The desired config of Intra-node visibility.

` .google.container.v1beta1.IntraNodeVisibilityConfig desired_intra_node_visibility_config = 26; `

**Returns**  
---  
**Type** | **Description**  
`[IntraNodeVisibilityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.IntraNodeVisibilityConfig)` | The desiredIntraNodeVisibilityConfig.  
  
### getDesiredIntraNodeVisibilityConfigBuilder()
    
    
    public IntraNodeVisibilityConfig.Builder getDesiredIntraNodeVisibilityConfigBuilder()

The desired config of Intra-node visibility.

` .google.container.v1beta1.IntraNodeVisibilityConfig desired_intra_node_visibility_config = 26; `

**Returns**  
---  
**Type** | **Description**  
`[IntraNodeVisibilityConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.IntraNodeVisibilityConfig.Builder)` |   
  
### getDesiredIntraNodeVisibilityConfigOrBuilder()
    
    
    public IntraNodeVisibilityConfigOrBuilder getDesiredIntraNodeVisibilityConfigOrBuilder()

The desired config of Intra-node visibility.

` .google.container.v1beta1.IntraNodeVisibilityConfig desired_intra_node_visibility_config = 26; `

**Returns**  
---  
**Type** | **Description**  
`[IntraNodeVisibilityConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.IntraNodeVisibilityConfigOrBuilder)` |   
  
### getDesiredK8SBetaApis()
    
    
    public K8sBetaAPIConfig getDesiredK8SBetaApis()

Beta APIs enabled for cluster.

`.google.container.v1beta1.K8sBetaAPIConfig desired_k8s_beta_apis = 131;`

**Returns**  
---  
**Type** | **Description**  
`[K8sBetaAPIConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.K8sBetaAPIConfig)` | The desiredK8sBetaApis.  
  
### getDesiredK8SBetaApisBuilder()
    
    
    public K8sBetaAPIConfig.Builder getDesiredK8SBetaApisBuilder()

Beta APIs enabled for cluster.

`.google.container.v1beta1.K8sBetaAPIConfig desired_k8s_beta_apis = 131;`

**Returns**  
---  
**Type** | **Description**  
`[K8sBetaAPIConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.K8sBetaAPIConfig.Builder)` |   
  
### getDesiredK8SBetaApisOrBuilder()
    
    
    public K8sBetaAPIConfigOrBuilder getDesiredK8SBetaApisOrBuilder()

Beta APIs enabled for cluster.

`.google.container.v1beta1.K8sBetaAPIConfig desired_k8s_beta_apis = 131;`

**Returns**  
---  
**Type** | **Description**  
`[K8sBetaAPIConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.K8sBetaAPIConfigOrBuilder)` |   
  
### getDesiredL4IlbSubsettingConfig()
    
    
    public ILBSubsettingConfig getDesiredL4IlbSubsettingConfig()

The desired L4 Internal Load Balancer Subsetting configuration.

`.google.container.v1beta1.ILBSubsettingConfig desired_l4ilb_subsetting_config = 39; `

**Returns**  
---  
**Type** | **Description**  
`[ILBSubsettingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ILBSubsettingConfig)` | The desiredL4ilbSubsettingConfig.  
  
### getDesiredL4IlbSubsettingConfigBuilder()
    
    
    public ILBSubsettingConfig.Builder getDesiredL4IlbSubsettingConfigBuilder()

The desired L4 Internal Load Balancer Subsetting configuration.

`.google.container.v1beta1.ILBSubsettingConfig desired_l4ilb_subsetting_config = 39; `

**Returns**  
---  
**Type** | **Description**  
`[ILBSubsettingConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ILBSubsettingConfig.Builder)` |   
  
### getDesiredL4IlbSubsettingConfigOrBuilder()
    
    
    public ILBSubsettingConfigOrBuilder getDesiredL4IlbSubsettingConfigOrBuilder()

The desired L4 Internal Load Balancer Subsetting configuration.

`.google.container.v1beta1.ILBSubsettingConfig desired_l4ilb_subsetting_config = 39; `

**Returns**  
---  
**Type** | **Description**  
`[ILBSubsettingConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ILBSubsettingConfigOrBuilder)` |   
  
### getDesiredLocations(int index)
    
    
    public String getDesiredLocations(int index)

The desired list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located.

This list must always include the cluster's primary zone.

Warning: changing cluster locations will update the locations of all node pools and will result in nodes being added and/or removed.

`repeated string desired_locations = 10;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The desiredLocations at the given index.  
  
### getDesiredLocationsBytes(int index)
    
    
    public ByteString getDesiredLocationsBytes(int index)

The desired list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located.

This list must always include the cluster's primary zone.

Warning: changing cluster locations will update the locations of all node pools and will result in nodes being added and/or removed.

`repeated string desired_locations = 10;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the desiredLocations at the given index.  
  
### getDesiredLocationsCount()
    
    
    public int getDesiredLocationsCount()

The desired list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located.

This list must always include the cluster's primary zone.

Warning: changing cluster locations will update the locations of all node pools and will result in nodes being added and/or removed.

`repeated string desired_locations = 10;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of desiredLocations.  
  
### getDesiredLocationsList()
    
    
    public ProtocolStringList getDesiredLocationsList()

The desired list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located.

This list must always include the cluster's primary zone.

Warning: changing cluster locations will update the locations of all node pools and will result in nodes being added and/or removed.

`repeated string desired_locations = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ProtocolStringList](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolStringList.html)` | A list containing the desiredLocations.  
  
### getDesiredLoggingConfig()
    
    
    public LoggingConfig getDesiredLoggingConfig()

The desired logging configuration.

`.google.container.v1beta1.LoggingConfig desired_logging_config = 64;`

**Returns**  
---  
**Type** | **Description**  
`[LoggingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.LoggingConfig)` | The desiredLoggingConfig.  
  
### getDesiredLoggingConfigBuilder()
    
    
    public LoggingConfig.Builder getDesiredLoggingConfigBuilder()

The desired logging configuration.

`.google.container.v1beta1.LoggingConfig desired_logging_config = 64;`

**Returns**  
---  
**Type** | **Description**  
`[LoggingConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.LoggingConfig.Builder)` |   
  
### getDesiredLoggingConfigOrBuilder()
    
    
    public LoggingConfigOrBuilder getDesiredLoggingConfigOrBuilder()

The desired logging configuration.

`.google.container.v1beta1.LoggingConfig desired_logging_config = 64;`

**Returns**  
---  
**Type** | **Description**  
`[LoggingConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.LoggingConfigOrBuilder)` |   
  
### getDesiredLoggingService()
    
    
    public String getDesiredLoggingService()

The logging service the cluster should use to write logs. Currently available options:

  * `logging.googleapis.com/kubernetes` \- The Cloud Logging service with a Kubernetes-native resource model
  * `logging.googleapis.com` \- The legacy Cloud Logging service (no longer available as of GKE 1.15).
  * `none` \- no logs will be exported from the cluster.

If left as an empty string,`logging.googleapis.com/kubernetes` will be used for GKE 1.14+ or `logging.googleapis.com` for earlier versions.




`string desired_logging_service = 19;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The desiredLoggingService.  
  
### getDesiredLoggingServiceBytes()
    
    
    public ByteString getDesiredLoggingServiceBytes()

The logging service the cluster should use to write logs. Currently available options:

  * `logging.googleapis.com/kubernetes` \- The Cloud Logging service with a Kubernetes-native resource model
  * `logging.googleapis.com` \- The legacy Cloud Logging service (no longer available as of GKE 1.15).
  * `none` \- no logs will be exported from the cluster.

If left as an empty string,`logging.googleapis.com/kubernetes` will be used for GKE 1.14+ or `logging.googleapis.com` for earlier versions.




`string desired_logging_service = 19;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for desiredLoggingService.  
  
### getDesiredManagedMachineLearningDiagnosticsConfig()
    
    
    public ManagedMachineLearningDiagnosticsConfig getDesiredManagedMachineLearningDiagnosticsConfig()

The desired managed machine learning diagnostics configuration.

` .google.container.v1beta1.ManagedMachineLearningDiagnosticsConfig desired_managed_machine_learning_diagnostics_config = 166; `

**Returns**  
---  
**Type** | **Description**  
`[ManagedMachineLearningDiagnosticsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ManagedMachineLearningDiagnosticsConfig)` | The desiredManagedMachineLearningDiagnosticsConfig.  
  
### getDesiredManagedMachineLearningDiagnosticsConfigBuilder()
    
    
    public ManagedMachineLearningDiagnosticsConfig.Builder getDesiredManagedMachineLearningDiagnosticsConfigBuilder()

The desired managed machine learning diagnostics configuration.

` .google.container.v1beta1.ManagedMachineLearningDiagnosticsConfig desired_managed_machine_learning_diagnostics_config = 166; `

**Returns**  
---  
**Type** | **Description**  
`[ManagedMachineLearningDiagnosticsConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ManagedMachineLearningDiagnosticsConfig.Builder)` |   
  
### getDesiredManagedMachineLearningDiagnosticsConfigOrBuilder()
    
    
    public ManagedMachineLearningDiagnosticsConfigOrBuilder getDesiredManagedMachineLearningDiagnosticsConfigOrBuilder()

The desired managed machine learning diagnostics configuration.

` .google.container.v1beta1.ManagedMachineLearningDiagnosticsConfig desired_managed_machine_learning_diagnostics_config = 166; `

**Returns**  
---  
**Type** | **Description**  
`[ManagedMachineLearningDiagnosticsConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ManagedMachineLearningDiagnosticsConfigOrBuilder)` |   
  
### getDesiredManagedOpentelemetryConfig()
    
    
    public ManagedOpenTelemetryConfig getDesiredManagedOpentelemetryConfig()

The desired managed open telemetry configuration.

` .google.container.v1beta1.ManagedOpenTelemetryConfig desired_managed_opentelemetry_config = 163; `

**Returns**  
---  
**Type** | **Description**  
`[ManagedOpenTelemetryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ManagedOpenTelemetryConfig)` | The desiredManagedOpentelemetryConfig.  
  
### getDesiredManagedOpentelemetryConfigBuilder()
    
    
    public ManagedOpenTelemetryConfig.Builder getDesiredManagedOpentelemetryConfigBuilder()

The desired managed open telemetry configuration.

` .google.container.v1beta1.ManagedOpenTelemetryConfig desired_managed_opentelemetry_config = 163; `

**Returns**  
---  
**Type** | **Description**  
`[ManagedOpenTelemetryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ManagedOpenTelemetryConfig.Builder)` |   
  
### getDesiredManagedOpentelemetryConfigOrBuilder()
    
    
    public ManagedOpenTelemetryConfigOrBuilder getDesiredManagedOpentelemetryConfigOrBuilder()

The desired managed open telemetry configuration.

` .google.container.v1beta1.ManagedOpenTelemetryConfig desired_managed_opentelemetry_config = 163; `

**Returns**  
---  
**Type** | **Description**  
`[ManagedOpenTelemetryConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ManagedOpenTelemetryConfigOrBuilder)` |   
  
### getDesiredMaster()
    
    
    public Master getDesiredMaster()

Configuration for master components.

`.google.container.v1beta1.Master desired_master = 52;`

**Returns**  
---  
**Type** | **Description**  
`[Master](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Master)` | The desiredMaster.  
  
### getDesiredMasterAuthorizedNetworksConfig() (deprecated)
    
    
    public MasterAuthorizedNetworksConfig getDesiredMasterAuthorizedNetworksConfig()

**Deprecated.** _google.container.v1beta1.ClusterUpdate.desired_master_authorized_networks_config is deprecated. See google/container/v1beta1/cluster_service.proto;l=4001_

The desired configuration options for master authorized networks feature.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.authorized_networks_config instead.

` .google.container.v1beta1.MasterAuthorizedNetworksConfig desired_master_authorized_networks_config = 12 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[MasterAuthorizedNetworksConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.MasterAuthorizedNetworksConfig)` | The desiredMasterAuthorizedNetworksConfig.  
  
### getDesiredMasterAuthorizedNetworksConfigBuilder() (deprecated)
    
    
    public MasterAuthorizedNetworksConfig.Builder getDesiredMasterAuthorizedNetworksConfigBuilder()

The desired configuration options for master authorized networks feature.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.authorized_networks_config instead.

` .google.container.v1beta1.MasterAuthorizedNetworksConfig desired_master_authorized_networks_config = 12 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[MasterAuthorizedNetworksConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.MasterAuthorizedNetworksConfig.Builder)` |   
  
### getDesiredMasterAuthorizedNetworksConfigOrBuilder() (deprecated)
    
    
    public MasterAuthorizedNetworksConfigOrBuilder getDesiredMasterAuthorizedNetworksConfigOrBuilder()

The desired configuration options for master authorized networks feature.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.authorized_networks_config instead.

` .google.container.v1beta1.MasterAuthorizedNetworksConfig desired_master_authorized_networks_config = 12 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[MasterAuthorizedNetworksConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.MasterAuthorizedNetworksConfigOrBuilder)` |   
  
### getDesiredMasterBuilder()
    
    
    public Master.Builder getDesiredMasterBuilder()

Configuration for master components.

`.google.container.v1beta1.Master desired_master = 52;`

**Returns**  
---  
**Type** | **Description**  
`[Master.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Master.Builder)` |   
  
### getDesiredMasterOrBuilder()
    
    
    public MasterOrBuilder getDesiredMasterOrBuilder()

Configuration for master components.

`.google.container.v1beta1.Master desired_master = 52;`

**Returns**  
---  
**Type** | **Description**  
`[MasterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.MasterOrBuilder)` |   
  
### getDesiredMasterVersion()
    
    
    public String getDesiredMasterVersion()

The Kubernetes version to change the master to. The only valid value is the latest supported version.

Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior:

  * "latest": picks the highest valid Kubernetes version
  * "1.X": picks the highest valid patch+gke.N patch in the 1.X version
  * "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
  * "1.X.Y-gke.N": picks an explicit Kubernetes version
  * "-": picks the default Kubernetes version



`string desired_master_version = 100;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The desiredMasterVersion.  
  
### getDesiredMasterVersionBytes()
    
    
    public ByteString getDesiredMasterVersionBytes()

The Kubernetes version to change the master to. The only valid value is the latest supported version.

Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior:

  * "latest": picks the highest valid Kubernetes version
  * "1.X": picks the highest valid patch+gke.N patch in the 1.X version
  * "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
  * "1.X.Y-gke.N": picks an explicit Kubernetes version
  * "-": picks the default Kubernetes version



`string desired_master_version = 100;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for desiredMasterVersion.  
  
### getDesiredMeshCertificates()
    
    
    public MeshCertificates getDesiredMeshCertificates()

Configuration for issuance of mTLS keys and certificates to Kubernetes pods.

`.google.container.v1beta1.MeshCertificates desired_mesh_certificates = 67;`

**Returns**  
---  
**Type** | **Description**  
`[MeshCertificates](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.MeshCertificates)` | The desiredMeshCertificates.  
  
### getDesiredMeshCertificatesBuilder()
    
    
    public MeshCertificates.Builder getDesiredMeshCertificatesBuilder()

Configuration for issuance of mTLS keys and certificates to Kubernetes pods.

`.google.container.v1beta1.MeshCertificates desired_mesh_certificates = 67;`

**Returns**  
---  
**Type** | **Description**  
`[MeshCertificates.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.MeshCertificates.Builder)` |   
  
### getDesiredMeshCertificatesOrBuilder()
    
    
    public MeshCertificatesOrBuilder getDesiredMeshCertificatesOrBuilder()

Configuration for issuance of mTLS keys and certificates to Kubernetes pods.

`.google.container.v1beta1.MeshCertificates desired_mesh_certificates = 67;`

**Returns**  
---  
**Type** | **Description**  
`[MeshCertificatesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.MeshCertificatesOrBuilder)` |   
  
### getDesiredMonitoringConfig()
    
    
    public MonitoringConfig getDesiredMonitoringConfig()

The desired monitoring configuration.

`.google.container.v1beta1.MonitoringConfig desired_monitoring_config = 65;`

**Returns**  
---  
**Type** | **Description**  
`[MonitoringConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.MonitoringConfig)` | The desiredMonitoringConfig.  
  
### getDesiredMonitoringConfigBuilder()
    
    
    public MonitoringConfig.Builder getDesiredMonitoringConfigBuilder()

The desired monitoring configuration.

`.google.container.v1beta1.MonitoringConfig desired_monitoring_config = 65;`

**Returns**  
---  
**Type** | **Description**  
`[MonitoringConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.MonitoringConfig.Builder)` |   
  
### getDesiredMonitoringConfigOrBuilder()
    
    
    public MonitoringConfigOrBuilder getDesiredMonitoringConfigOrBuilder()

The desired monitoring configuration.

`.google.container.v1beta1.MonitoringConfig desired_monitoring_config = 65;`

**Returns**  
---  
**Type** | **Description**  
`[MonitoringConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.MonitoringConfigOrBuilder)` |   
  
### getDesiredMonitoringService()
    
    
    public String getDesiredMonitoringService()

The monitoring service the cluster should use to write metrics. Currently available options:

  * `monitoring.googleapis.com/kubernetes` \- The Cloud Monitoring service with a Kubernetes-native resource model
  * `monitoring.googleapis.com` \- The legacy Cloud Monitoring service (no longer available as of GKE 1.15).
  * `none` \- No metrics will be exported from the cluster.

If left as an empty string,`monitoring.googleapis.com/kubernetes` will be used for GKE 1.14+ or `monitoring.googleapis.com` for earlier versions.




`string desired_monitoring_service = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The desiredMonitoringService.  
  
### getDesiredMonitoringServiceBytes()
    
    
    public ByteString getDesiredMonitoringServiceBytes()

The monitoring service the cluster should use to write metrics. Currently available options:

  * `monitoring.googleapis.com/kubernetes` \- The Cloud Monitoring service with a Kubernetes-native resource model
  * `monitoring.googleapis.com` \- The legacy Cloud Monitoring service (no longer available as of GKE 1.15).
  * `none` \- No metrics will be exported from the cluster.

If left as an empty string,`monitoring.googleapis.com/kubernetes` will be used for GKE 1.14+ or `monitoring.googleapis.com` for earlier versions.




`string desired_monitoring_service = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for desiredMonitoringService.  
  
### getDesiredNetworkPerformanceConfig()
    
    
    public NetworkConfig.ClusterNetworkPerformanceConfig getDesiredNetworkPerformanceConfig()

The desired network performance config.

` .google.container.v1beta1.NetworkConfig.ClusterNetworkPerformanceConfig desired_network_performance_config = 125; `

**Returns**  
---  
**Type** | **Description**  
`[NetworkConfig.ClusterNetworkPerformanceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NetworkConfig.ClusterNetworkPerformanceConfig)` | The desiredNetworkPerformanceConfig.  
  
### getDesiredNetworkPerformanceConfigBuilder()
    
    
    public NetworkConfig.ClusterNetworkPerformanceConfig.Builder getDesiredNetworkPerformanceConfigBuilder()

The desired network performance config.

` .google.container.v1beta1.NetworkConfig.ClusterNetworkPerformanceConfig desired_network_performance_config = 125; `

**Returns**  
---  
**Type** | **Description**  
`[NetworkConfig.ClusterNetworkPerformanceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NetworkConfig.ClusterNetworkPerformanceConfig.Builder)` |   
  
### getDesiredNetworkPerformanceConfigOrBuilder()
    
    
    public NetworkConfig.ClusterNetworkPerformanceConfigOrBuilder getDesiredNetworkPerformanceConfigOrBuilder()

The desired network performance config.

` .google.container.v1beta1.NetworkConfig.ClusterNetworkPerformanceConfig desired_network_performance_config = 125; `

**Returns**  
---  
**Type** | **Description**  
`[NetworkConfig.ClusterNetworkPerformanceConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NetworkConfig.ClusterNetworkPerformanceConfigOrBuilder)` |   
  
### getDesiredNetworkTierConfig()
    
    
    public NetworkTierConfig getDesiredNetworkTierConfig()

The desired network tier configuration for the cluster.

`.google.container.v1beta1.NetworkTierConfig desired_network_tier_config = 155;`

**Returns**  
---  
**Type** | **Description**  
`[NetworkTierConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NetworkTierConfig)` | The desiredNetworkTierConfig.  
  
### getDesiredNetworkTierConfigBuilder()
    
    
    public NetworkTierConfig.Builder getDesiredNetworkTierConfigBuilder()

The desired network tier configuration for the cluster.

`.google.container.v1beta1.NetworkTierConfig desired_network_tier_config = 155;`

**Returns**  
---  
**Type** | **Description**  
`[NetworkTierConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NetworkTierConfig.Builder)` |   
  
### getDesiredNetworkTierConfigOrBuilder()
    
    
    public NetworkTierConfigOrBuilder getDesiredNetworkTierConfigOrBuilder()

The desired network tier configuration for the cluster.

`.google.container.v1beta1.NetworkTierConfig desired_network_tier_config = 155;`

**Returns**  
---  
**Type** | **Description**  
`[NetworkTierConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NetworkTierConfigOrBuilder)` |   
  
### getDesiredNodeCreationConfig()
    
    
    public NodeCreationConfig getDesiredNodeCreationConfig()

Optional. The desired NodeCreationConfig for the cluster.

` .google.container.v1beta1.NodeCreationConfig desired_node_creation_config = 171 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[NodeCreationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeCreationConfig)` | The desiredNodeCreationConfig.  
  
### getDesiredNodeCreationConfigBuilder()
    
    
    public NodeCreationConfig.Builder getDesiredNodeCreationConfigBuilder()

Optional. The desired NodeCreationConfig for the cluster.

` .google.container.v1beta1.NodeCreationConfig desired_node_creation_config = 171 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[NodeCreationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeCreationConfig.Builder)` |   
  
### getDesiredNodeCreationConfigOrBuilder()
    
    
    public NodeCreationConfigOrBuilder getDesiredNodeCreationConfigOrBuilder()

Optional. The desired NodeCreationConfig for the cluster.

` .google.container.v1beta1.NodeCreationConfig desired_node_creation_config = 171 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[NodeCreationConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeCreationConfigOrBuilder)` |   
  
### getDesiredNodeKubeletConfig()
    
    
    public NodeKubeletConfig getDesiredNodeKubeletConfig()

The desired node kubelet config for the cluster.

`.google.container.v1beta1.NodeKubeletConfig desired_node_kubelet_config = 141;`

**Returns**  
---  
**Type** | **Description**  
`[NodeKubeletConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeKubeletConfig)` | The desiredNodeKubeletConfig.  
  
### getDesiredNodeKubeletConfigBuilder()
    
    
    public NodeKubeletConfig.Builder getDesiredNodeKubeletConfigBuilder()

The desired node kubelet config for the cluster.

`.google.container.v1beta1.NodeKubeletConfig desired_node_kubelet_config = 141;`

**Returns**  
---  
**Type** | **Description**  
`[NodeKubeletConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeKubeletConfig.Builder)` |   
  
### getDesiredNodeKubeletConfigOrBuilder()
    
    
    public NodeKubeletConfigOrBuilder getDesiredNodeKubeletConfigOrBuilder()

The desired node kubelet config for the cluster.

`.google.container.v1beta1.NodeKubeletConfig desired_node_kubelet_config = 141;`

**Returns**  
---  
**Type** | **Description**  
`[NodeKubeletConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeKubeletConfigOrBuilder)` |   
  
### getDesiredNodePoolAutoConfigKubeletConfig()
    
    
    public NodeKubeletConfig getDesiredNodePoolAutoConfigKubeletConfig()

The desired node kubelet config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

` .google.container.v1beta1.NodeKubeletConfig desired_node_pool_auto_config_kubelet_config = 142; `

**Returns**  
---  
**Type** | **Description**  
`[NodeKubeletConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeKubeletConfig)` | The desiredNodePoolAutoConfigKubeletConfig.  
  
### getDesiredNodePoolAutoConfigKubeletConfigBuilder()
    
    
    public NodeKubeletConfig.Builder getDesiredNodePoolAutoConfigKubeletConfigBuilder()

The desired node kubelet config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

` .google.container.v1beta1.NodeKubeletConfig desired_node_pool_auto_config_kubelet_config = 142; `

**Returns**  
---  
**Type** | **Description**  
`[NodeKubeletConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeKubeletConfig.Builder)` |   
  
### getDesiredNodePoolAutoConfigKubeletConfigOrBuilder()
    
    
    public NodeKubeletConfigOrBuilder getDesiredNodePoolAutoConfigKubeletConfigOrBuilder()

The desired node kubelet config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

` .google.container.v1beta1.NodeKubeletConfig desired_node_pool_auto_config_kubelet_config = 142; `

**Returns**  
---  
**Type** | **Description**  
`[NodeKubeletConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeKubeletConfigOrBuilder)` |   
  
### getDesiredNodePoolAutoConfigLinuxNodeConfig()
    
    
    public LinuxNodeConfig getDesiredNodePoolAutoConfigLinuxNodeConfig()

The desired Linux node config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

Currently only `cgroup_mode` can be set here.

` .google.container.v1beta1.LinuxNodeConfig desired_node_pool_auto_config_linux_node_config = 150; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.LinuxNodeConfig)` | The desiredNodePoolAutoConfigLinuxNodeConfig.  
  
### getDesiredNodePoolAutoConfigLinuxNodeConfigBuilder()
    
    
    public LinuxNodeConfig.Builder getDesiredNodePoolAutoConfigLinuxNodeConfigBuilder()

The desired Linux node config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

Currently only `cgroup_mode` can be set here.

` .google.container.v1beta1.LinuxNodeConfig desired_node_pool_auto_config_linux_node_config = 150; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.LinuxNodeConfig.Builder)` |   
  
### getDesiredNodePoolAutoConfigLinuxNodeConfigOrBuilder()
    
    
    public LinuxNodeConfigOrBuilder getDesiredNodePoolAutoConfigLinuxNodeConfigOrBuilder()

The desired Linux node config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

Currently only `cgroup_mode` can be set here.

` .google.container.v1beta1.LinuxNodeConfig desired_node_pool_auto_config_linux_node_config = 150; `

**Returns**  
---  
**Type** | **Description**  
`[LinuxNodeConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.LinuxNodeConfigOrBuilder)` |   
  
### getDesiredNodePoolAutoConfigNetworkTags()
    
    
    public NetworkTags getDesiredNodePoolAutoConfigNetworkTags()

The desired network tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

`.google.container.v1beta1.NetworkTags desired_node_pool_auto_config_network_tags = 110; `

**Returns**  
---  
**Type** | **Description**  
`[NetworkTags](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NetworkTags)` | The desiredNodePoolAutoConfigNetworkTags.  
  
### getDesiredNodePoolAutoConfigNetworkTagsBuilder()
    
    
    public NetworkTags.Builder getDesiredNodePoolAutoConfigNetworkTagsBuilder()

The desired network tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

`.google.container.v1beta1.NetworkTags desired_node_pool_auto_config_network_tags = 110; `

**Returns**  
---  
**Type** | **Description**  
`[NetworkTags.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NetworkTags.Builder)` |   
  
### getDesiredNodePoolAutoConfigNetworkTagsOrBuilder()
    
    
    public NetworkTagsOrBuilder getDesiredNodePoolAutoConfigNetworkTagsOrBuilder()

The desired network tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

`.google.container.v1beta1.NetworkTags desired_node_pool_auto_config_network_tags = 110; `

**Returns**  
---  
**Type** | **Description**  
`[NetworkTagsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NetworkTagsOrBuilder)` |   
  
### getDesiredNodePoolAutoConfigResourceManagerTags()
    
    
    public ResourceManagerTags getDesiredNodePoolAutoConfigResourceManagerTags()

The desired resource manager tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

` .google.container.v1beta1.ResourceManagerTags desired_node_pool_auto_config_resource_manager_tags = 136; `

**Returns**  
---  
**Type** | **Description**  
`[ResourceManagerTags](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ResourceManagerTags)` | The desiredNodePoolAutoConfigResourceManagerTags.  
  
### getDesiredNodePoolAutoConfigResourceManagerTagsBuilder()
    
    
    public ResourceManagerTags.Builder getDesiredNodePoolAutoConfigResourceManagerTagsBuilder()

The desired resource manager tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

` .google.container.v1beta1.ResourceManagerTags desired_node_pool_auto_config_resource_manager_tags = 136; `

**Returns**  
---  
**Type** | **Description**  
`[ResourceManagerTags.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ResourceManagerTags.Builder)` |   
  
### getDesiredNodePoolAutoConfigResourceManagerTagsOrBuilder()
    
    
    public ResourceManagerTagsOrBuilder getDesiredNodePoolAutoConfigResourceManagerTagsOrBuilder()

The desired resource manager tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

` .google.container.v1beta1.ResourceManagerTags desired_node_pool_auto_config_resource_manager_tags = 136; `

**Returns**  
---  
**Type** | **Description**  
`[ResourceManagerTagsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ResourceManagerTagsOrBuilder)` |   
  
### getDesiredNodePoolAutoscaling()
    
    
    public NodePoolAutoscaling getDesiredNodePoolAutoscaling()

Autoscaler configuration for the node pool specified in desired_node_pool_id. If there is only one pool in the cluster and desired_node_pool_id is not provided then the change applies to that single node pool.

`.google.container.v1beta1.NodePoolAutoscaling desired_node_pool_autoscaling = 9;`

**Returns**  
---  
**Type** | **Description**  
`[NodePoolAutoscaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolAutoscaling)` | The desiredNodePoolAutoscaling.  
  
### getDesiredNodePoolAutoscalingBuilder()
    
    
    public NodePoolAutoscaling.Builder getDesiredNodePoolAutoscalingBuilder()

Autoscaler configuration for the node pool specified in desired_node_pool_id. If there is only one pool in the cluster and desired_node_pool_id is not provided then the change applies to that single node pool.

`.google.container.v1beta1.NodePoolAutoscaling desired_node_pool_autoscaling = 9;`

**Returns**  
---  
**Type** | **Description**  
`[NodePoolAutoscaling.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolAutoscaling.Builder)` |   
  
### getDesiredNodePoolAutoscalingOrBuilder()
    
    
    public NodePoolAutoscalingOrBuilder getDesiredNodePoolAutoscalingOrBuilder()

Autoscaler configuration for the node pool specified in desired_node_pool_id. If there is only one pool in the cluster and desired_node_pool_id is not provided then the change applies to that single node pool.

`.google.container.v1beta1.NodePoolAutoscaling desired_node_pool_autoscaling = 9;`

**Returns**  
---  
**Type** | **Description**  
`[NodePoolAutoscalingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolAutoscalingOrBuilder)` |   
  
### getDesiredNodePoolId()
    
    
    public String getDesiredNodePoolId()

The node pool to be upgraded. This field is mandatory if "desired_node_version", "desired_image_family", "desired_node_pool_autoscaling", or "desired_workload_metadata_config" is specified and there is more than one node pool on the cluster.

`string desired_node_pool_id = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The desiredNodePoolId.  
  
### getDesiredNodePoolIdBytes()
    
    
    public ByteString getDesiredNodePoolIdBytes()

The node pool to be upgraded. This field is mandatory if "desired_node_version", "desired_image_family", "desired_node_pool_autoscaling", or "desired_workload_metadata_config" is specified and there is more than one node pool on the cluster.

`string desired_node_pool_id = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for desiredNodePoolId.  
  
### getDesiredNodePoolLoggingConfig()
    
    
    public NodePoolLoggingConfig getDesiredNodePoolLoggingConfig()

The desired node pool logging configuration defaults for the cluster.

`.google.container.v1beta1.NodePoolLoggingConfig desired_node_pool_logging_config = 116; `

**Returns**  
---  
**Type** | **Description**  
`[NodePoolLoggingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolLoggingConfig)` | The desiredNodePoolLoggingConfig.  
  
### getDesiredNodePoolLoggingConfigBuilder()
    
    
    public NodePoolLoggingConfig.Builder getDesiredNodePoolLoggingConfigBuilder()

The desired node pool logging configuration defaults for the cluster.

`.google.container.v1beta1.NodePoolLoggingConfig desired_node_pool_logging_config = 116; `

**Returns**  
---  
**Type** | **Description**  
`[NodePoolLoggingConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolLoggingConfig.Builder)` |   
  
### getDesiredNodePoolLoggingConfigOrBuilder()
    
    
    public NodePoolLoggingConfigOrBuilder getDesiredNodePoolLoggingConfigOrBuilder()

The desired node pool logging configuration defaults for the cluster.

`.google.container.v1beta1.NodePoolLoggingConfig desired_node_pool_logging_config = 116; `

**Returns**  
---  
**Type** | **Description**  
`[NodePoolLoggingConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolLoggingConfigOrBuilder)` |   
  
### getDesiredNodePoolUpgradeConcurrencyConfig()
    
    
    public NodePoolUpgradeConcurrencyConfig getDesiredNodePoolUpgradeConcurrencyConfig()

The desired node pool upgrade concurrency configuration.

` .google.container.v1beta1.NodePoolUpgradeConcurrencyConfig desired_node_pool_upgrade_concurrency_config = 167; `

**Returns**  
---  
**Type** | **Description**  
`[NodePoolUpgradeConcurrencyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolUpgradeConcurrencyConfig)` | The desiredNodePoolUpgradeConcurrencyConfig.  
  
### getDesiredNodePoolUpgradeConcurrencyConfigBuilder()
    
    
    public NodePoolUpgradeConcurrencyConfig.Builder getDesiredNodePoolUpgradeConcurrencyConfigBuilder()

The desired node pool upgrade concurrency configuration.

` .google.container.v1beta1.NodePoolUpgradeConcurrencyConfig desired_node_pool_upgrade_concurrency_config = 167; `

**Returns**  
---  
**Type** | **Description**  
`[NodePoolUpgradeConcurrencyConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolUpgradeConcurrencyConfig.Builder)` |   
  
### getDesiredNodePoolUpgradeConcurrencyConfigOrBuilder()
    
    
    public NodePoolUpgradeConcurrencyConfigOrBuilder getDesiredNodePoolUpgradeConcurrencyConfigOrBuilder()

The desired node pool upgrade concurrency configuration.

` .google.container.v1beta1.NodePoolUpgradeConcurrencyConfig desired_node_pool_upgrade_concurrency_config = 167; `

**Returns**  
---  
**Type** | **Description**  
`[NodePoolUpgradeConcurrencyConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolUpgradeConcurrencyConfigOrBuilder)` |   
  
### getDesiredNodeVersion()
    
    
    public String getDesiredNodeVersion()

The Kubernetes version to change the nodes to (typically an upgrade).

Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior:

  * "latest": picks the highest valid Kubernetes version
  * "1.X": picks the highest valid patch+gke.N patch in the 1.X version
  * "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
  * "1.X.Y-gke.N": picks an explicit Kubernetes version
  * "-": picks the Kubernetes master version



`string desired_node_version = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The desiredNodeVersion.  
  
### getDesiredNodeVersionBytes()
    
    
    public ByteString getDesiredNodeVersionBytes()

The Kubernetes version to change the nodes to (typically an upgrade).

Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior:

  * "latest": picks the highest valid Kubernetes version
  * "1.X": picks the highest valid patch+gke.N patch in the 1.X version
  * "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
  * "1.X.Y-gke.N": picks an explicit Kubernetes version
  * "-": picks the Kubernetes master version



`string desired_node_version = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for desiredNodeVersion.  
  
### getDesiredNotificationConfig()
    
    
    public NotificationConfig getDesiredNotificationConfig()

The desired notification configuration.

`.google.container.v1beta1.NotificationConfig desired_notification_config = 55;`

**Returns**  
---  
**Type** | **Description**  
`[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NotificationConfig)` | The desiredNotificationConfig.  
  
### getDesiredNotificationConfigBuilder()
    
    
    public NotificationConfig.Builder getDesiredNotificationConfigBuilder()

The desired notification configuration.

`.google.container.v1beta1.NotificationConfig desired_notification_config = 55;`

**Returns**  
---  
**Type** | **Description**  
`[NotificationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NotificationConfig.Builder)` |   
  
### getDesiredNotificationConfigOrBuilder()
    
    
    public NotificationConfigOrBuilder getDesiredNotificationConfigOrBuilder()

The desired notification configuration.

`.google.container.v1beta1.NotificationConfig desired_notification_config = 55;`

**Returns**  
---  
**Type** | **Description**  
`[NotificationConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NotificationConfigOrBuilder)` |   
  
### getDesiredPodAutoscaling()
    
    
    public PodAutoscaling getDesiredPodAutoscaling()

The desired config for pod autoscaling.

`.google.container.v1beta1.PodAutoscaling desired_pod_autoscaling = 113;`

**Returns**  
---  
**Type** | **Description**  
`[PodAutoscaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PodAutoscaling)` | The desiredPodAutoscaling.  
  
### getDesiredPodAutoscalingBuilder()
    
    
    public PodAutoscaling.Builder getDesiredPodAutoscalingBuilder()

The desired config for pod autoscaling.

`.google.container.v1beta1.PodAutoscaling desired_pod_autoscaling = 113;`

**Returns**  
---  
**Type** | **Description**  
`[PodAutoscaling.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PodAutoscaling.Builder)` |   
  
### getDesiredPodAutoscalingOrBuilder()
    
    
    public PodAutoscalingOrBuilder getDesiredPodAutoscalingOrBuilder()

The desired config for pod autoscaling.

`.google.container.v1beta1.PodAutoscaling desired_pod_autoscaling = 113;`

**Returns**  
---  
**Type** | **Description**  
`[PodAutoscalingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PodAutoscalingOrBuilder)` |   
  
### getDesiredPodSecurityPolicyConfig()
    
    
    public PodSecurityPolicyConfig getDesiredPodSecurityPolicyConfig()

The desired configuration options for the PodSecurityPolicy feature.

` .google.container.v1beta1.PodSecurityPolicyConfig desired_pod_security_policy_config = 14; `

**Returns**  
---  
**Type** | **Description**  
`[PodSecurityPolicyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PodSecurityPolicyConfig)` | The desiredPodSecurityPolicyConfig.  
  
### getDesiredPodSecurityPolicyConfigBuilder()
    
    
    public PodSecurityPolicyConfig.Builder getDesiredPodSecurityPolicyConfigBuilder()

The desired configuration options for the PodSecurityPolicy feature.

` .google.container.v1beta1.PodSecurityPolicyConfig desired_pod_security_policy_config = 14; `

**Returns**  
---  
**Type** | **Description**  
`[PodSecurityPolicyConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PodSecurityPolicyConfig.Builder)` |   
  
### getDesiredPodSecurityPolicyConfigOrBuilder()
    
    
    public PodSecurityPolicyConfigOrBuilder getDesiredPodSecurityPolicyConfigOrBuilder()

The desired configuration options for the PodSecurityPolicy feature.

` .google.container.v1beta1.PodSecurityPolicyConfig desired_pod_security_policy_config = 14; `

**Returns**  
---  
**Type** | **Description**  
`[PodSecurityPolicyConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PodSecurityPolicyConfigOrBuilder)` |   
  
### getDesiredPrivateClusterConfig() (deprecated)
    
    
    public PrivateClusterConfig getDesiredPrivateClusterConfig()

**Deprecated.** _google.container.v1beta1.ClusterUpdate.desired_private_cluster_config is deprecated. See google/container/v1beta1/cluster_service.proto;l=4042_

The desired private cluster configuration. master_global_access_config is the only field that can be changed via this field. See also ClusterUpdate.desired_enable_private_endpoint for modifying other fields within PrivateClusterConfig.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.global_access instead.

` .google.container.v1beta1.PrivateClusterConfig desired_private_cluster_config = 25 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[PrivateClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PrivateClusterConfig)` | The desiredPrivateClusterConfig.  
  
### getDesiredPrivateClusterConfigBuilder() (deprecated)
    
    
    public PrivateClusterConfig.Builder getDesiredPrivateClusterConfigBuilder()

The desired private cluster configuration. master_global_access_config is the only field that can be changed via this field. See also ClusterUpdate.desired_enable_private_endpoint for modifying other fields within PrivateClusterConfig.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.global_access instead.

` .google.container.v1beta1.PrivateClusterConfig desired_private_cluster_config = 25 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[PrivateClusterConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PrivateClusterConfig.Builder)` |   
  
### getDesiredPrivateClusterConfigOrBuilder() (deprecated)
    
    
    public PrivateClusterConfigOrBuilder getDesiredPrivateClusterConfigOrBuilder()

The desired private cluster configuration. master_global_access_config is the only field that can be changed via this field. See also ClusterUpdate.desired_enable_private_endpoint for modifying other fields within PrivateClusterConfig.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.global_access instead.

` .google.container.v1beta1.PrivateClusterConfig desired_private_cluster_config = 25 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[PrivateClusterConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PrivateClusterConfigOrBuilder)` |   
  
### getDesiredPrivateIpv6GoogleAccess()
    
    
    public PrivateIPv6GoogleAccess getDesiredPrivateIpv6GoogleAccess()

The desired state of IPv6 connectivity to Google Services.

` .google.container.v1beta1.PrivateIPv6GoogleAccess desired_private_ipv6_google_access = 51; `

**Returns**  
---  
**Type** | **Description**  
`[PrivateIPv6GoogleAccess](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PrivateIPv6GoogleAccess)` | The desiredPrivateIpv6GoogleAccess.  
  
### getDesiredPrivateIpv6GoogleAccessValue()
    
    
    public int getDesiredPrivateIpv6GoogleAccessValue()

The desired state of IPv6 connectivity to Google Services.

` .google.container.v1beta1.PrivateIPv6GoogleAccess desired_private_ipv6_google_access = 51; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for desiredPrivateIpv6GoogleAccess.  
  
### getDesiredPrivilegedAdmissionConfig()
    
    
    public PrivilegedAdmissionConfig getDesiredPrivilegedAdmissionConfig()

The desired privileged admission config for the cluster.

` .google.container.v1beta1.PrivilegedAdmissionConfig desired_privileged_admission_config = 159; `

**Returns**  
---  
**Type** | **Description**  
`[PrivilegedAdmissionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PrivilegedAdmissionConfig)` | The desiredPrivilegedAdmissionConfig.  
  
### getDesiredPrivilegedAdmissionConfigBuilder()
    
    
    public PrivilegedAdmissionConfig.Builder getDesiredPrivilegedAdmissionConfigBuilder()

The desired privileged admission config for the cluster.

` .google.container.v1beta1.PrivilegedAdmissionConfig desired_privileged_admission_config = 159; `

**Returns**  
---  
**Type** | **Description**  
`[PrivilegedAdmissionConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PrivilegedAdmissionConfig.Builder)` |   
  
### getDesiredPrivilegedAdmissionConfigOrBuilder()
    
    
    public PrivilegedAdmissionConfigOrBuilder getDesiredPrivilegedAdmissionConfigOrBuilder()

The desired privileged admission config for the cluster.

` .google.container.v1beta1.PrivilegedAdmissionConfig desired_privileged_admission_config = 159; `

**Returns**  
---  
**Type** | **Description**  
`[PrivilegedAdmissionConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PrivilegedAdmissionConfigOrBuilder)` |   
  
### getDesiredProtectConfig() (deprecated)
    
    
    public ProtectConfig getDesiredProtectConfig()

**Deprecated.** _google.container.v1beta1.ClusterUpdate.desired_protect_config is deprecated. See google/container/v1beta1/cluster_service.proto;l=4174_

Deprecated: Use DesiredSecurityPostureConfig instead. Enable/Disable Protect API features for the cluster.

` optional .google.container.v1beta1.ProtectConfig desired_protect_config = 112 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[ProtectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ProtectConfig)` | The desiredProtectConfig.  
  
### getDesiredProtectConfigBuilder() (deprecated)
    
    
    public ProtectConfig.Builder getDesiredProtectConfigBuilder()

Deprecated: Use DesiredSecurityPostureConfig instead. Enable/Disable Protect API features for the cluster.

` optional .google.container.v1beta1.ProtectConfig desired_protect_config = 112 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[ProtectConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ProtectConfig.Builder)` |   
  
### getDesiredProtectConfigOrBuilder() (deprecated)
    
    
    public ProtectConfigOrBuilder getDesiredProtectConfigOrBuilder()

Deprecated: Use DesiredSecurityPostureConfig instead. Enable/Disable Protect API features for the cluster.

` optional .google.container.v1beta1.ProtectConfig desired_protect_config = 112 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[ProtectConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ProtectConfigOrBuilder)` |   
  
### getDesiredRbacBindingConfig()
    
    
    public RBACBindingConfig getDesiredRbacBindingConfig()

RBACBindingConfig allows user to restrict ClusterRoleBindings an RoleBindings that can be created.

`optional .google.container.v1beta1.RBACBindingConfig desired_rbac_binding_config = 144; `

**Returns**  
---  
**Type** | **Description**  
`[RBACBindingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.RBACBindingConfig)` | The desiredRbacBindingConfig.  
  
### getDesiredRbacBindingConfigBuilder()
    
    
    public RBACBindingConfig.Builder getDesiredRbacBindingConfigBuilder()

RBACBindingConfig allows user to restrict ClusterRoleBindings an RoleBindings that can be created.

`optional .google.container.v1beta1.RBACBindingConfig desired_rbac_binding_config = 144; `

**Returns**  
---  
**Type** | **Description**  
`[RBACBindingConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.RBACBindingConfig.Builder)` |   
  
### getDesiredRbacBindingConfigOrBuilder()
    
    
    public RBACBindingConfigOrBuilder getDesiredRbacBindingConfigOrBuilder()

RBACBindingConfig allows user to restrict ClusterRoleBindings an RoleBindings that can be created.

`optional .google.container.v1beta1.RBACBindingConfig desired_rbac_binding_config = 144; `

**Returns**  
---  
**Type** | **Description**  
`[RBACBindingConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.RBACBindingConfigOrBuilder)` |   
  
### getDesiredReleaseChannel()
    
    
    public ReleaseChannel getDesiredReleaseChannel()

The desired release channel configuration.

`.google.container.v1beta1.ReleaseChannel desired_release_channel = 31;`

**Returns**  
---  
**Type** | **Description**  
`[ReleaseChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ReleaseChannel)` | The desiredReleaseChannel.  
  
### getDesiredReleaseChannelBuilder()
    
    
    public ReleaseChannel.Builder getDesiredReleaseChannelBuilder()

The desired release channel configuration.

`.google.container.v1beta1.ReleaseChannel desired_release_channel = 31;`

**Returns**  
---  
**Type** | **Description**  
`[ReleaseChannel.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ReleaseChannel.Builder)` |   
  
### getDesiredReleaseChannelOrBuilder()
    
    
    public ReleaseChannelOrBuilder getDesiredReleaseChannelOrBuilder()

The desired release channel configuration.

`.google.container.v1beta1.ReleaseChannel desired_release_channel = 31;`

**Returns**  
---  
**Type** | **Description**  
`[ReleaseChannelOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ReleaseChannelOrBuilder)` |   
  
### getDesiredResourceUsageExportConfig()
    
    
    public ResourceUsageExportConfig getDesiredResourceUsageExportConfig()

The desired configuration for exporting resource usage.

` .google.container.v1beta1.ResourceUsageExportConfig desired_resource_usage_export_config = 21; `

**Returns**  
---  
**Type** | **Description**  
`[ResourceUsageExportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ResourceUsageExportConfig)` | The desiredResourceUsageExportConfig.  
  
### getDesiredResourceUsageExportConfigBuilder()
    
    
    public ResourceUsageExportConfig.Builder getDesiredResourceUsageExportConfigBuilder()

The desired configuration for exporting resource usage.

` .google.container.v1beta1.ResourceUsageExportConfig desired_resource_usage_export_config = 21; `

**Returns**  
---  
**Type** | **Description**  
`[ResourceUsageExportConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ResourceUsageExportConfig.Builder)` |   
  
### getDesiredResourceUsageExportConfigOrBuilder()
    
    
    public ResourceUsageExportConfigOrBuilder getDesiredResourceUsageExportConfigOrBuilder()

The desired configuration for exporting resource usage.

` .google.container.v1beta1.ResourceUsageExportConfig desired_resource_usage_export_config = 21; `

**Returns**  
---  
**Type** | **Description**  
`[ResourceUsageExportConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ResourceUsageExportConfigOrBuilder)` |   
  
### getDesiredRollbackSafeUpgrade()
    
    
    public RollbackSafeUpgrade getDesiredRollbackSafeUpgrade()

The desired rollback safe upgrade configuration.

`.google.container.v1beta1.RollbackSafeUpgrade desired_rollback_safe_upgrade = 161; `

**Returns**  
---  
**Type** | **Description**  
`[RollbackSafeUpgrade](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.RollbackSafeUpgrade)` | The desiredRollbackSafeUpgrade.  
  
### getDesiredRollbackSafeUpgradeBuilder()
    
    
    public RollbackSafeUpgrade.Builder getDesiredRollbackSafeUpgradeBuilder()

The desired rollback safe upgrade configuration.

`.google.container.v1beta1.RollbackSafeUpgrade desired_rollback_safe_upgrade = 161; `

**Returns**  
---  
**Type** | **Description**  
`[RollbackSafeUpgrade.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.RollbackSafeUpgrade.Builder)` |   
  
### getDesiredRollbackSafeUpgradeOrBuilder()
    
    
    public RollbackSafeUpgradeOrBuilder getDesiredRollbackSafeUpgradeOrBuilder()

The desired rollback safe upgrade configuration.

`.google.container.v1beta1.RollbackSafeUpgrade desired_rollback_safe_upgrade = 161; `

**Returns**  
---  
**Type** | **Description**  
`[RollbackSafeUpgradeOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.RollbackSafeUpgradeOrBuilder)` |   
  
### getDesiredScheduleUpgradeConfig()
    
    
    public ScheduleUpgradeConfig getDesiredScheduleUpgradeConfig()

Optional. The desired scheduled upgrades configuration for the cluster.

` .google.container.v1beta1.ScheduleUpgradeConfig desired_schedule_upgrade_config = 157 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ScheduleUpgradeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ScheduleUpgradeConfig)` | The desiredScheduleUpgradeConfig.  
  
### getDesiredScheduleUpgradeConfigBuilder()
    
    
    public ScheduleUpgradeConfig.Builder getDesiredScheduleUpgradeConfigBuilder()

Optional. The desired scheduled upgrades configuration for the cluster.

` .google.container.v1beta1.ScheduleUpgradeConfig desired_schedule_upgrade_config = 157 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ScheduleUpgradeConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ScheduleUpgradeConfig.Builder)` |   
  
### getDesiredScheduleUpgradeConfigOrBuilder()
    
    
    public ScheduleUpgradeConfigOrBuilder getDesiredScheduleUpgradeConfigOrBuilder()

Optional. The desired scheduled upgrades configuration for the cluster.

` .google.container.v1beta1.ScheduleUpgradeConfig desired_schedule_upgrade_config = 157 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ScheduleUpgradeConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ScheduleUpgradeConfigOrBuilder)` |   
  
### getDesiredSecretManagerConfig()
    
    
    public SecretManagerConfig getDesiredSecretManagerConfig()

Enable/Disable Secret Manager Config.

` optional .google.container.v1beta1.SecretManagerConfig desired_secret_manager_config = 139; `

**Returns**  
---  
**Type** | **Description**  
`[SecretManagerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SecretManagerConfig)` | The desiredSecretManagerConfig.  
  
### getDesiredSecretManagerConfigBuilder()
    
    
    public SecretManagerConfig.Builder getDesiredSecretManagerConfigBuilder()

Enable/Disable Secret Manager Config.

` optional .google.container.v1beta1.SecretManagerConfig desired_secret_manager_config = 139; `

**Returns**  
---  
**Type** | **Description**  
`[SecretManagerConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SecretManagerConfig.Builder)` |   
  
### getDesiredSecretManagerConfigOrBuilder()
    
    
    public SecretManagerConfigOrBuilder getDesiredSecretManagerConfigOrBuilder()

Enable/Disable Secret Manager Config.

` optional .google.container.v1beta1.SecretManagerConfig desired_secret_manager_config = 139; `

**Returns**  
---  
**Type** | **Description**  
`[SecretManagerConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SecretManagerConfigOrBuilder)` |   
  
### getDesiredSecretSyncConfig()
    
    
    public SecretSyncConfig getDesiredSecretSyncConfig()

Configuration for sync Secret Manager secrets as k8s secrets.

`.google.container.v1beta1.SecretSyncConfig desired_secret_sync_config = 158;`

**Returns**  
---  
**Type** | **Description**  
`[SecretSyncConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SecretSyncConfig)` | The desiredSecretSyncConfig.  
  
### getDesiredSecretSyncConfigBuilder()
    
    
    public SecretSyncConfig.Builder getDesiredSecretSyncConfigBuilder()

Configuration for sync Secret Manager secrets as k8s secrets.

`.google.container.v1beta1.SecretSyncConfig desired_secret_sync_config = 158;`

**Returns**  
---  
**Type** | **Description**  
`[SecretSyncConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SecretSyncConfig.Builder)` |   
  
### getDesiredSecretSyncConfigOrBuilder()
    
    
    public SecretSyncConfigOrBuilder getDesiredSecretSyncConfigOrBuilder()

Configuration for sync Secret Manager secrets as k8s secrets.

`.google.container.v1beta1.SecretSyncConfig desired_secret_sync_config = 158;`

**Returns**  
---  
**Type** | **Description**  
`[SecretSyncConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SecretSyncConfigOrBuilder)` |   
  
### getDesiredSecurityPostureConfig()
    
    
    public SecurityPostureConfig getDesiredSecurityPostureConfig()

Enable/Disable Security Posture API features for the cluster.

`.google.container.v1beta1.SecurityPostureConfig desired_security_posture_config = 124; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SecurityPostureConfig)` | The desiredSecurityPostureConfig.  
  
### getDesiredSecurityPostureConfigBuilder()
    
    
    public SecurityPostureConfig.Builder getDesiredSecurityPostureConfigBuilder()

Enable/Disable Security Posture API features for the cluster.

`.google.container.v1beta1.SecurityPostureConfig desired_security_posture_config = 124; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SecurityPostureConfig.Builder)` |   
  
### getDesiredSecurityPostureConfigOrBuilder()
    
    
    public SecurityPostureConfigOrBuilder getDesiredSecurityPostureConfigOrBuilder()

Enable/Disable Security Posture API features for the cluster.

`.google.container.v1beta1.SecurityPostureConfig desired_security_posture_config = 124; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SecurityPostureConfigOrBuilder)` |   
  
### getDesiredServiceExternalIpsConfig()
    
    
    public ServiceExternalIPsConfig getDesiredServiceExternalIpsConfig()

ServiceExternalIPsConfig specifies the config for the use of Services with ExternalIPs field.

` .google.container.v1beta1.ServiceExternalIPsConfig desired_service_external_ips_config = 60; `

**Returns**  
---  
**Type** | **Description**  
`[ServiceExternalIPsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ServiceExternalIPsConfig)` | The desiredServiceExternalIpsConfig.  
  
### getDesiredServiceExternalIpsConfigBuilder()
    
    
    public ServiceExternalIPsConfig.Builder getDesiredServiceExternalIpsConfigBuilder()

ServiceExternalIPsConfig specifies the config for the use of Services with ExternalIPs field.

` .google.container.v1beta1.ServiceExternalIPsConfig desired_service_external_ips_config = 60; `

**Returns**  
---  
**Type** | **Description**  
`[ServiceExternalIPsConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ServiceExternalIPsConfig.Builder)` |   
  
### getDesiredServiceExternalIpsConfigOrBuilder()
    
    
    public ServiceExternalIPsConfigOrBuilder getDesiredServiceExternalIpsConfigOrBuilder()

ServiceExternalIPsConfig specifies the config for the use of Services with ExternalIPs field.

` .google.container.v1beta1.ServiceExternalIPsConfig desired_service_external_ips_config = 60; `

**Returns**  
---  
**Type** | **Description**  
`[ServiceExternalIPsConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ServiceExternalIPsConfigOrBuilder)` |   
  
### getDesiredShieldedNodes()
    
    
    public ShieldedNodes getDesiredShieldedNodes()

Configuration for Shielded Nodes.

`.google.container.v1beta1.ShieldedNodes desired_shielded_nodes = 48;`

**Returns**  
---  
**Type** | **Description**  
`[ShieldedNodes](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ShieldedNodes)` | The desiredShieldedNodes.  
  
### getDesiredShieldedNodesBuilder()
    
    
    public ShieldedNodes.Builder getDesiredShieldedNodesBuilder()

Configuration for Shielded Nodes.

`.google.container.v1beta1.ShieldedNodes desired_shielded_nodes = 48;`

**Returns**  
---  
**Type** | **Description**  
`[ShieldedNodes.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ShieldedNodes.Builder)` |   
  
### getDesiredShieldedNodesOrBuilder()
    
    
    public ShieldedNodesOrBuilder getDesiredShieldedNodesOrBuilder()

Configuration for Shielded Nodes.

`.google.container.v1beta1.ShieldedNodes desired_shielded_nodes = 48;`

**Returns**  
---  
**Type** | **Description**  
`[ShieldedNodesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ShieldedNodesOrBuilder)` |   
  
### getDesiredStackType()
    
    
    public StackType getDesiredStackType()

The desired stack type of the cluster. If a stack type is provided and does not match the current stack type of the cluster, update will attempt to change the stack type to the new type.

`.google.container.v1beta1.StackType desired_stack_type = 119;`

**Returns**  
---  
**Type** | **Description**  
`[StackType](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.StackType)` | The desiredStackType.  
  
### getDesiredStackTypeValue()
    
    
    public int getDesiredStackTypeValue()

The desired stack type of the cluster. If a stack type is provided and does not match the current stack type of the cluster, update will attempt to change the stack type to the new type.

`.google.container.v1beta1.StackType desired_stack_type = 119;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for desiredStackType.  
  
### getDesiredTpuConfig() (deprecated)
    
    
    public TpuConfig getDesiredTpuConfig()

**Deprecated.** _google.container.v1beta1.ClusterUpdate.desired_tpu_config is deprecated. See google/container/v1beta1/cluster_service.proto;l=4064_

The desired Cloud TPU configuration. This field is deprecated due to the deprecation of 2VM TPU. The end of life date for 2VM TPU is 2025-04-25.

`.google.container.v1beta1.TpuConfig desired_tpu_config = 38 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[TpuConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.TpuConfig)` | The desiredTpuConfig.  
  
### getDesiredTpuConfigBuilder() (deprecated)
    
    
    public TpuConfig.Builder getDesiredTpuConfigBuilder()

The desired Cloud TPU configuration. This field is deprecated due to the deprecation of 2VM TPU. The end of life date for 2VM TPU is 2025-04-25.

`.google.container.v1beta1.TpuConfig desired_tpu_config = 38 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[TpuConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.TpuConfig.Builder)` |   
  
### getDesiredTpuConfigOrBuilder() (deprecated)
    
    
    public TpuConfigOrBuilder getDesiredTpuConfigOrBuilder()

The desired Cloud TPU configuration. This field is deprecated due to the deprecation of 2VM TPU. The end of life date for 2VM TPU is 2025-04-25.

`.google.container.v1beta1.TpuConfig desired_tpu_config = 38 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[TpuConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.TpuConfigOrBuilder)` |   
  
### getDesiredUserManagedKeysConfig()
    
    
    public UserManagedKeysConfig getDesiredUserManagedKeysConfig()

The desired user managed keys config for the cluster.

`.google.container.v1beta1.UserManagedKeysConfig desired_user_managed_keys_config = 152; `

**Returns**  
---  
**Type** | **Description**  
`[UserManagedKeysConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.UserManagedKeysConfig)` | The desiredUserManagedKeysConfig.  
  
### getDesiredUserManagedKeysConfigBuilder()
    
    
    public UserManagedKeysConfig.Builder getDesiredUserManagedKeysConfigBuilder()

The desired user managed keys config for the cluster.

`.google.container.v1beta1.UserManagedKeysConfig desired_user_managed_keys_config = 152; `

**Returns**  
---  
**Type** | **Description**  
`[UserManagedKeysConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.UserManagedKeysConfig.Builder)` |   
  
### getDesiredUserManagedKeysConfigOrBuilder()
    
    
    public UserManagedKeysConfigOrBuilder getDesiredUserManagedKeysConfigOrBuilder()

The desired user managed keys config for the cluster.

`.google.container.v1beta1.UserManagedKeysConfig desired_user_managed_keys_config = 152; `

**Returns**  
---  
**Type** | **Description**  
`[UserManagedKeysConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.UserManagedKeysConfigOrBuilder)` |   
  
### getDesiredVerticalPodAutoscaling()
    
    
    public VerticalPodAutoscaling getDesiredVerticalPodAutoscaling()

Cluster-level Vertical Pod Autoscaling configuration.

`.google.container.v1beta1.VerticalPodAutoscaling desired_vertical_pod_autoscaling = 22; `

**Returns**  
---  
**Type** | **Description**  
`[VerticalPodAutoscaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.VerticalPodAutoscaling)` | The desiredVerticalPodAutoscaling.  
  
### getDesiredVerticalPodAutoscalingBuilder()
    
    
    public VerticalPodAutoscaling.Builder getDesiredVerticalPodAutoscalingBuilder()

Cluster-level Vertical Pod Autoscaling configuration.

`.google.container.v1beta1.VerticalPodAutoscaling desired_vertical_pod_autoscaling = 22; `

**Returns**  
---  
**Type** | **Description**  
`[VerticalPodAutoscaling.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.VerticalPodAutoscaling.Builder)` |   
  
### getDesiredVerticalPodAutoscalingOrBuilder()
    
    
    public VerticalPodAutoscalingOrBuilder getDesiredVerticalPodAutoscalingOrBuilder()

Cluster-level Vertical Pod Autoscaling configuration.

`.google.container.v1beta1.VerticalPodAutoscaling desired_vertical_pod_autoscaling = 22; `

**Returns**  
---  
**Type** | **Description**  
`[VerticalPodAutoscalingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.VerticalPodAutoscalingOrBuilder)` |   
  
### getDesiredWorkloadAltsConfig()
    
    
    public WorkloadALTSConfig getDesiredWorkloadAltsConfig()

Configuration for direct-path (via ALTS) with workload identity. This feature is not officially supported for external customers in Kubernetes Engine when using Workload Identity.

`.google.container.v1beta1.WorkloadALTSConfig desired_workload_alts_config = 62;`

**Returns**  
---  
**Type** | **Description**  
`[WorkloadALTSConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadALTSConfig)` | The desiredWorkloadAltsConfig.  
  
### getDesiredWorkloadAltsConfigBuilder()
    
    
    public WorkloadALTSConfig.Builder getDesiredWorkloadAltsConfigBuilder()

Configuration for direct-path (via ALTS) with workload identity. This feature is not officially supported for external customers in Kubernetes Engine when using Workload Identity.

`.google.container.v1beta1.WorkloadALTSConfig desired_workload_alts_config = 62;`

**Returns**  
---  
**Type** | **Description**  
`[WorkloadALTSConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadALTSConfig.Builder)` |   
  
### getDesiredWorkloadAltsConfigOrBuilder()
    
    
    public WorkloadALTSConfigOrBuilder getDesiredWorkloadAltsConfigOrBuilder()

Configuration for direct-path (via ALTS) with workload identity. This feature is not officially supported for external customers in Kubernetes Engine when using Workload Identity.

`.google.container.v1beta1.WorkloadALTSConfig desired_workload_alts_config = 62;`

**Returns**  
---  
**Type** | **Description**  
`[WorkloadALTSConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadALTSConfigOrBuilder)` |   
  
### getDesiredWorkloadCertificates()
    
    
    public WorkloadCertificates getDesiredWorkloadCertificates()

Configuration for issuance of mTLS keys and certificates to Kubernetes pods.

`.google.container.v1beta1.WorkloadCertificates desired_workload_certificates = 61; `

**Returns**  
---  
**Type** | **Description**  
`[WorkloadCertificates](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadCertificates)` | The desiredWorkloadCertificates.  
  
### getDesiredWorkloadCertificatesBuilder()
    
    
    public WorkloadCertificates.Builder getDesiredWorkloadCertificatesBuilder()

Configuration for issuance of mTLS keys and certificates to Kubernetes pods.

`.google.container.v1beta1.WorkloadCertificates desired_workload_certificates = 61; `

**Returns**  
---  
**Type** | **Description**  
`[WorkloadCertificates.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadCertificates.Builder)` |   
  
### getDesiredWorkloadCertificatesOrBuilder()
    
    
    public WorkloadCertificatesOrBuilder getDesiredWorkloadCertificatesOrBuilder()

Configuration for issuance of mTLS keys and certificates to Kubernetes pods.

`.google.container.v1beta1.WorkloadCertificates desired_workload_certificates = 61; `

**Returns**  
---  
**Type** | **Description**  
`[WorkloadCertificatesOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadCertificatesOrBuilder)` |   
  
### getDesiredWorkloadIdentityConfig()
    
    
    public WorkloadIdentityConfig getDesiredWorkloadIdentityConfig()

Configuration for Workload Identity.

`.google.container.v1beta1.WorkloadIdentityConfig desired_workload_identity_config = 47; `

**Returns**  
---  
**Type** | **Description**  
`[WorkloadIdentityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadIdentityConfig)` | The desiredWorkloadIdentityConfig.  
  
### getDesiredWorkloadIdentityConfigBuilder()
    
    
    public WorkloadIdentityConfig.Builder getDesiredWorkloadIdentityConfigBuilder()

Configuration for Workload Identity.

`.google.container.v1beta1.WorkloadIdentityConfig desired_workload_identity_config = 47; `

**Returns**  
---  
**Type** | **Description**  
`[WorkloadIdentityConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadIdentityConfig.Builder)` |   
  
### getDesiredWorkloadIdentityConfigOrBuilder()
    
    
    public WorkloadIdentityConfigOrBuilder getDesiredWorkloadIdentityConfigOrBuilder()

Configuration for Workload Identity.

`.google.container.v1beta1.WorkloadIdentityConfig desired_workload_identity_config = 47; `

**Returns**  
---  
**Type** | **Description**  
`[WorkloadIdentityConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadIdentityConfigOrBuilder)` |   
  
### getEnableK8SBetaApis()
    
    
    public K8sBetaAPIConfig getEnableK8SBetaApis()

Kubernetes open source beta apis enabled on the cluster. Only beta apis

`.google.container.v1beta1.K8sBetaAPIConfig enable_k8s_beta_apis = 122;`

**Returns**  
---  
**Type** | **Description**  
`[K8sBetaAPIConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.K8sBetaAPIConfig)` | The enableK8sBetaApis.  
  
### getEnableK8SBetaApisBuilder()
    
    
    public K8sBetaAPIConfig.Builder getEnableK8SBetaApisBuilder()

Kubernetes open source beta apis enabled on the cluster. Only beta apis

`.google.container.v1beta1.K8sBetaAPIConfig enable_k8s_beta_apis = 122;`

**Returns**  
---  
**Type** | **Description**  
`[K8sBetaAPIConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.K8sBetaAPIConfig.Builder)` |   
  
### getEnableK8SBetaApisOrBuilder()
    
    
    public K8sBetaAPIConfigOrBuilder getEnableK8SBetaApisOrBuilder()

Kubernetes open source beta apis enabled on the cluster. Only beta apis

`.google.container.v1beta1.K8sBetaAPIConfig enable_k8s_beta_apis = 122;`

**Returns**  
---  
**Type** | **Description**  
`[K8sBetaAPIConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.K8sBetaAPIConfigOrBuilder)` |   
  
### getEtag()
    
    
    public String getEtag()

The current etag of the cluster. If an etag is provided and does not match the current etag of the cluster, update will be blocked and an ABORTED error will be returned.

`string etag = 115;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The etag.  
  
### getEtagBytes()
    
    
    public ByteString getEtagBytes()

The current etag of the cluster. If an etag is provided and does not match the current etag of the cluster, update will be blocked and an ABORTED error will be returned.

`string etag = 115;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for etag.  
  
### getGkeAutoUpgradeConfig()
    
    
    public GkeAutoUpgradeConfig getGkeAutoUpgradeConfig()

Configuration for GKE auto upgrade.

`.google.container.v1beta1.GkeAutoUpgradeConfig gke_auto_upgrade_config = 154;`

**Returns**  
---  
**Type** | **Description**  
`[GkeAutoUpgradeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GkeAutoUpgradeConfig)` | The gkeAutoUpgradeConfig.  
  
### getGkeAutoUpgradeConfigBuilder()
    
    
    public GkeAutoUpgradeConfig.Builder getGkeAutoUpgradeConfigBuilder()

Configuration for GKE auto upgrade.

`.google.container.v1beta1.GkeAutoUpgradeConfig gke_auto_upgrade_config = 154;`

**Returns**  
---  
**Type** | **Description**  
`[GkeAutoUpgradeConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GkeAutoUpgradeConfig.Builder)` |   
  
### getGkeAutoUpgradeConfigOrBuilder()
    
    
    public GkeAutoUpgradeConfigOrBuilder getGkeAutoUpgradeConfigOrBuilder()

Configuration for GKE auto upgrade.

`.google.container.v1beta1.GkeAutoUpgradeConfig gke_auto_upgrade_config = 154;`

**Returns**  
---  
**Type** | **Description**  
`[GkeAutoUpgradeConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GkeAutoUpgradeConfigOrBuilder)` |   
  
### getPrivateClusterConfig() (deprecated)
    
    
    public PrivateClusterConfig getPrivateClusterConfig()

**Deprecated.** _google.container.v1beta1.ClusterUpdate.private_cluster_config is deprecated. See google/container/v1beta1/cluster_service.proto;l=4059_

The desired private cluster configuration. Has no effect. Use desired_private_cluster_config instead.

` .google.container.v1beta1.PrivateClusterConfig private_cluster_config = 37 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[PrivateClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PrivateClusterConfig)` | The privateClusterConfig.  
  
### getPrivateClusterConfigBuilder() (deprecated)
    
    
    public PrivateClusterConfig.Builder getPrivateClusterConfigBuilder()

The desired private cluster configuration. Has no effect. Use desired_private_cluster_config instead.

` .google.container.v1beta1.PrivateClusterConfig private_cluster_config = 37 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[PrivateClusterConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PrivateClusterConfig.Builder)` |   
  
### getPrivateClusterConfigOrBuilder() (deprecated)
    
    
    public PrivateClusterConfigOrBuilder getPrivateClusterConfigOrBuilder()

The desired private cluster configuration. Has no effect. Use desired_private_cluster_config instead.

` .google.container.v1beta1.PrivateClusterConfig private_cluster_config = 37 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[PrivateClusterConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PrivateClusterConfigOrBuilder)` |   
  
### getRemovedAdditionalPodRangesConfig()
    
    
    public AdditionalPodRangesConfig getRemovedAdditionalPodRangesConfig()

The additional pod ranges that are to be removed from the cluster. The pod ranges specified here must have been specified earlier in the 'additional_pod_ranges_config' argument.

` .google.container.v1beta1.AdditionalPodRangesConfig removed_additional_pod_ranges_config = 121; `

**Returns**  
---  
**Type** | **Description**  
`[AdditionalPodRangesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AdditionalPodRangesConfig)` | The removedAdditionalPodRangesConfig.  
  
### getRemovedAdditionalPodRangesConfigBuilder()
    
    
    public AdditionalPodRangesConfig.Builder getRemovedAdditionalPodRangesConfigBuilder()

The additional pod ranges that are to be removed from the cluster. The pod ranges specified here must have been specified earlier in the 'additional_pod_ranges_config' argument.

` .google.container.v1beta1.AdditionalPodRangesConfig removed_additional_pod_ranges_config = 121; `

**Returns**  
---  
**Type** | **Description**  
`[AdditionalPodRangesConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AdditionalPodRangesConfig.Builder)` |   
  
### getRemovedAdditionalPodRangesConfigOrBuilder()
    
    
    public AdditionalPodRangesConfigOrBuilder getRemovedAdditionalPodRangesConfigOrBuilder()

The additional pod ranges that are to be removed from the cluster. The pod ranges specified here must have been specified earlier in the 'additional_pod_ranges_config' argument.

` .google.container.v1beta1.AdditionalPodRangesConfig removed_additional_pod_ranges_config = 121; `

**Returns**  
---  
**Type** | **Description**  
`[AdditionalPodRangesConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AdditionalPodRangesConfigOrBuilder)` |   
  
### getUserManagedKeysConfig() (deprecated)
    
    
    public UserManagedKeysConfig getUserManagedKeysConfig()

**Deprecated.** _google.container.v1beta1.ClusterUpdate.user_managed_keys_config is deprecated. See google/container/v1beta1/cluster_service.proto;l=4271_

The Custom keys configuration for the cluster.

This field is deprecated. Use ClusterUpdate.desired_user_managed_keys_config instead.

` .google.container.v1beta1.UserManagedKeysConfig user_managed_keys_config = 143 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[UserManagedKeysConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.UserManagedKeysConfig)` | The userManagedKeysConfig.  
  
### getUserManagedKeysConfigBuilder() (deprecated)
    
    
    public UserManagedKeysConfig.Builder getUserManagedKeysConfigBuilder()

The Custom keys configuration for the cluster.

This field is deprecated. Use ClusterUpdate.desired_user_managed_keys_config instead.

` .google.container.v1beta1.UserManagedKeysConfig user_managed_keys_config = 143 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[UserManagedKeysConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.UserManagedKeysConfig.Builder)` |   
  
### getUserManagedKeysConfigOrBuilder() (deprecated)
    
    
    public UserManagedKeysConfigOrBuilder getUserManagedKeysConfigOrBuilder()

The Custom keys configuration for the cluster.

This field is deprecated. Use ClusterUpdate.desired_user_managed_keys_config instead.

` .google.container.v1beta1.UserManagedKeysConfig user_managed_keys_config = 143 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[UserManagedKeysConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.UserManagedKeysConfigOrBuilder)` |   
  
### hasAdditionalPodRangesConfig()
    
    
    public boolean hasAdditionalPodRangesConfig()

The additional pod ranges to be added to the cluster. These pod ranges can be used by node pools to allocate pod IPs.

`.google.container.v1beta1.AdditionalPodRangesConfig additional_pod_ranges_config = 120; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the additionalPodRangesConfig field is set.  
  
### hasDesiredAdditionalIpRangesConfig()
    
    
    public boolean hasDesiredAdditionalIpRangesConfig()

The desired config for additional subnetworks attached to the cluster.

` .google.container.v1beta1.DesiredAdditionalIPRangesConfig desired_additional_ip_ranges_config = 145; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredAdditionalIpRangesConfig field is set.  
  
### hasDesiredAddonsConfig()
    
    
    public boolean hasDesiredAddonsConfig()

Configurations for the various addons available to run in the cluster.

`.google.container.v1beta1.AddonsConfig desired_addons_config = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredAddonsConfig field is set.  
  
### hasDesiredAnonymousAuthenticationConfig()
    
    
    public boolean hasDesiredAnonymousAuthenticationConfig()

Configuration for limiting anonymous access to all endpoints except the health checks.

` .google.container.v1beta1.AnonymousAuthenticationConfig desired_anonymous_authentication_config = 156; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredAnonymousAuthenticationConfig field is set.  
  
### hasDesiredAuthenticatorGroupsConfig()
    
    
    public boolean hasDesiredAuthenticatorGroupsConfig()

AuthenticatorGroupsConfig specifies the config for the cluster security groups settings.

` .google.container.v1beta1.AuthenticatorGroupsConfig desired_authenticator_groups_config = 63; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredAuthenticatorGroupsConfig field is set.  
  
### hasDesiredAutoIpamConfig()
    
    
    public boolean hasDesiredAutoIpamConfig()

AutoIpamConfig contains all information related to Auto IPAM

`.google.container.v1beta1.AutoIpamConfig desired_auto_ipam_config = 148;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredAutoIpamConfig field is set.  
  
### hasDesiredAutopilotClusterPolicyConfig()
    
    
    public boolean hasDesiredAutopilotClusterPolicyConfig()

The desired autopilot cluster policies that to be enforced in the cluster.

` .google.container.v1beta1.ClusterPolicyConfig desired_autopilot_cluster_policy_config = 164; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredAutopilotClusterPolicyConfig field is set.  
  
### hasDesiredAutopilotWorkloadPolicyConfig()
    
    
    public boolean hasDesiredAutopilotWorkloadPolicyConfig()

WorkloadPolicyConfig is the configuration related to GCW workload policy

` .google.container.v1beta1.WorkloadPolicyConfig desired_autopilot_workload_policy_config = 128; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredAutopilotWorkloadPolicyConfig field is set.  
  
### hasDesiredBinaryAuthorization()
    
    
    public boolean hasDesiredBinaryAuthorization()

The desired configuration options for the Binary Authorization feature.

`.google.container.v1beta1.BinaryAuthorization desired_binary_authorization = 16;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredBinaryAuthorization field is set.  
  
### hasDesiredClusterAutoscaling()
    
    
    public boolean hasDesiredClusterAutoscaling()

Cluster-level autoscaling configuration.

`.google.container.v1beta1.ClusterAutoscaling desired_cluster_autoscaling = 15;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredClusterAutoscaling field is set.  
  
### hasDesiredClusterTelemetry()
    
    
    public boolean hasDesiredClusterTelemetry()

The desired telemetry integration for the cluster.

`.google.container.v1beta1.ClusterTelemetry desired_cluster_telemetry = 30;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredClusterTelemetry field is set.  
  
### hasDesiredCompliancePostureConfig() (deprecated)
    
    
    public boolean hasDesiredCompliancePostureConfig()

**Deprecated.** _google.container.v1beta1.ClusterUpdate.desired_compliance_posture_config is deprecated. See google/container/v1beta1/cluster_service.proto;l=4255_

Deprecated: Compliance Posture is no longer supported. For more details, see <https://cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation>.

Enable/Disable Compliance Posture features for the cluster.

` optional .google.container.v1beta1.CompliancePostureConfig desired_compliance_posture_config = 140 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredCompliancePostureConfig field is set.  
  
### hasDesiredContainerdConfig()
    
    
    public boolean hasDesiredContainerdConfig()

The desired containerd config for the cluster.

`.google.container.v1beta1.ContainerdConfig desired_containerd_config = 134;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredContainerdConfig field is set.  
  
### hasDesiredControlPlaneEgress()
    
    
    public boolean hasDesiredControlPlaneEgress()

The desired control plane egress control config for the cluster.

`.google.container.v1beta1.ControlPlaneEgress desired_control_plane_egress = 160;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredControlPlaneEgress field is set.  
  
### hasDesiredControlPlaneEndpointsConfig()
    
    
    public boolean hasDesiredControlPlaneEndpointsConfig()

Control plane endpoints configuration.

` .google.container.v1beta1.ControlPlaneEndpointsConfig desired_control_plane_endpoints_config = 73; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredControlPlaneEndpointsConfig field is set.  
  
### hasDesiredCostManagementConfig()
    
    
    public boolean hasDesiredCostManagementConfig()

The desired configuration for the fine-grained cost management feature.

`.google.container.v1beta1.CostManagementConfig desired_cost_management_config = 49; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredCostManagementConfig field is set.  
  
### hasDesiredDatabaseEncryption()
    
    
    public boolean hasDesiredDatabaseEncryption()

Configuration of etcd encryption.

`.google.container.v1beta1.DatabaseEncryption desired_database_encryption = 46;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredDatabaseEncryption field is set.  
  
### hasDesiredDefaultEnablePrivateNodes()
    
    
    public boolean hasDesiredDefaultEnablePrivateNodes()

Override the default setting of whether future created nodes have private IP addresses only, namely NetworkConfig.default_enable_private_nodes

`optional bool desired_default_enable_private_nodes = 72;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredDefaultEnablePrivateNodes field is set.  
  
### hasDesiredDefaultSnatStatus()
    
    
    public boolean hasDesiredDefaultSnatStatus()

The desired status of whether to disable default sNAT for this cluster.

`.google.container.v1beta1.DefaultSnatStatus desired_default_snat_status = 28;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredDefaultSnatStatus field is set.  
  
### hasDesiredDisableL4LbFirewallReconciliation()
    
    
    public boolean hasDesiredDisableL4LbFirewallReconciliation()

Enable/Disable L4 LB VPC firewall reconciliation for the cluster.

`optional bool desired_disable_l4_lb_firewall_reconciliation = 149;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredDisableL4LbFirewallReconciliation field is set.  
  
### hasDesiredDnsConfig()
    
    
    public boolean hasDesiredDnsConfig()

DNSConfig contains clusterDNS config for this cluster.

`.google.container.v1beta1.DNSConfig desired_dns_config = 53;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredDnsConfig field is set.  
  
### hasDesiredEnableCiliumClusterwideNetworkPolicy()
    
    
    public boolean hasDesiredEnableCiliumClusterwideNetworkPolicy()

Enable/Disable Cilium Clusterwide Network Policy for the cluster.

`optional bool desired_enable_cilium_clusterwide_network_policy = 138;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredEnableCiliumClusterwideNetworkPolicy field is set.  
  
### hasDesiredEnableFqdnNetworkPolicy()
    
    
    public boolean hasDesiredEnableFqdnNetworkPolicy()

Enable/Disable FQDN Network Policy for the cluster.

`optional bool desired_enable_fqdn_network_policy = 126;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredEnableFqdnNetworkPolicy field is set.  
  
### hasDesiredEnableMultiNetworking()
    
    
    public boolean hasDesiredEnableMultiNetworking()

Enable/Disable Multi-Networking for the cluster

`optional bool desired_enable_multi_networking = 135;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredEnableMultiNetworking field is set.  
  
### hasDesiredEnablePrivateEndpoint() (deprecated)
    
    
    public boolean hasDesiredEnablePrivateEndpoint()

**Deprecated.** _google.container.v1beta1.ClusterUpdate.desired_enable_private_endpoint is deprecated. See google/container/v1beta1/cluster_service.proto;l=4156_

Enable/Disable private endpoint for the cluster's master.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.enable_public_endpoint instead. Note that the value of enable_public_endpoint is reversed: if enable_private_endpoint is false, then enable_public_endpoint will be true.

`optional bool desired_enable_private_endpoint = 71 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredEnablePrivateEndpoint field is set.  
  
### hasDesiredEnterpriseConfig() (deprecated)
    
    
    public boolean hasDesiredEnterpriseConfig()

**Deprecated.** _google.container.v1beta1.ClusterUpdate.desired_enterprise_config is deprecated. See google/container/v1beta1/cluster_service.proto;l=4284_

The desired enterprise configuration for the cluster.

Deprecated: GKE Enterprise features are now available without an Enterprise tier.

` .google.container.v1beta1.DesiredEnterpriseConfig desired_enterprise_config = 147 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredEnterpriseConfig field is set.  
  
### hasDesiredFleet()
    
    
    public boolean hasDesiredFleet()

The desired fleet configuration for the cluster.

`.google.container.v1beta1.Fleet desired_fleet = 117;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredFleet field is set.  
  
### hasDesiredGatewayApiConfig()
    
    
    public boolean hasDesiredGatewayApiConfig()

The desired config of Gateway API on this cluster.

`.google.container.v1beta1.GatewayAPIConfig desired_gateway_api_config = 114;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredGatewayApiConfig field is set.  
  
### hasDesiredGcfsConfig()
    
    
    public boolean hasDesiredGcfsConfig()

The desired GCFS config for the cluster.

`.google.container.v1beta1.GcfsConfig desired_gcfs_config = 109;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredGcfsConfig field is set.  
  
### hasDesiredHostMaintenancePolicy()
    
    
    public boolean hasDesiredHostMaintenancePolicy()

HostMaintenancePolicy contains the desired maintenance policy for the Google Compute Engine hosts.

`.google.container.v1beta1.HostMaintenancePolicy desired_host_maintenance_policy = 132; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredHostMaintenancePolicy field is set.  
  
### hasDesiredIdentityServiceConfig()
    
    
    public boolean hasDesiredIdentityServiceConfig()

The desired Identity Service component configuration.

`.google.container.v1beta1.IdentityServiceConfig desired_identity_service_config = 66; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredIdentityServiceConfig field is set.  
  
### hasDesiredInTransitEncryptionConfig()
    
    
    public boolean hasDesiredInTransitEncryptionConfig()

Specify the details of in-transit encryption. Now named inter-node transparent encryption.

` optional .google.container.v1beta1.InTransitEncryptionConfig desired_in_transit_encryption_config = 137; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredInTransitEncryptionConfig field is set.  
  
### hasDesiredIntraNodeVisibilityConfig()
    
    
    public boolean hasDesiredIntraNodeVisibilityConfig()

The desired config of Intra-node visibility.

` .google.container.v1beta1.IntraNodeVisibilityConfig desired_intra_node_visibility_config = 26; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredIntraNodeVisibilityConfig field is set.  
  
### hasDesiredK8SBetaApis()
    
    
    public boolean hasDesiredK8SBetaApis()

Beta APIs enabled for cluster.

`.google.container.v1beta1.K8sBetaAPIConfig desired_k8s_beta_apis = 131;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredK8sBetaApis field is set.  
  
### hasDesiredL4IlbSubsettingConfig()
    
    
    public boolean hasDesiredL4IlbSubsettingConfig()

The desired L4 Internal Load Balancer Subsetting configuration.

`.google.container.v1beta1.ILBSubsettingConfig desired_l4ilb_subsetting_config = 39; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredL4ilbSubsettingConfig field is set.  
  
### hasDesiredLoggingConfig()
    
    
    public boolean hasDesiredLoggingConfig()

The desired logging configuration.

`.google.container.v1beta1.LoggingConfig desired_logging_config = 64;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredLoggingConfig field is set.  
  
### hasDesiredManagedMachineLearningDiagnosticsConfig()
    
    
    public boolean hasDesiredManagedMachineLearningDiagnosticsConfig()

The desired managed machine learning diagnostics configuration.

` .google.container.v1beta1.ManagedMachineLearningDiagnosticsConfig desired_managed_machine_learning_diagnostics_config = 166; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredManagedMachineLearningDiagnosticsConfig field is set.  
  
### hasDesiredManagedOpentelemetryConfig()
    
    
    public boolean hasDesiredManagedOpentelemetryConfig()

The desired managed open telemetry configuration.

` .google.container.v1beta1.ManagedOpenTelemetryConfig desired_managed_opentelemetry_config = 163; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredManagedOpentelemetryConfig field is set.  
  
### hasDesiredMaster()
    
    
    public boolean hasDesiredMaster()

Configuration for master components.

`.google.container.v1beta1.Master desired_master = 52;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredMaster field is set.  
  
### hasDesiredMasterAuthorizedNetworksConfig() (deprecated)
    
    
    public boolean hasDesiredMasterAuthorizedNetworksConfig()

**Deprecated.** _google.container.v1beta1.ClusterUpdate.desired_master_authorized_networks_config is deprecated. See google/container/v1beta1/cluster_service.proto;l=4001_

The desired configuration options for master authorized networks feature.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.authorized_networks_config instead.

` .google.container.v1beta1.MasterAuthorizedNetworksConfig desired_master_authorized_networks_config = 12 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredMasterAuthorizedNetworksConfig field is set.  
  
### hasDesiredMeshCertificates()
    
    
    public boolean hasDesiredMeshCertificates()

Configuration for issuance of mTLS keys and certificates to Kubernetes pods.

`.google.container.v1beta1.MeshCertificates desired_mesh_certificates = 67;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredMeshCertificates field is set.  
  
### hasDesiredMonitoringConfig()
    
    
    public boolean hasDesiredMonitoringConfig()

The desired monitoring configuration.

`.google.container.v1beta1.MonitoringConfig desired_monitoring_config = 65;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredMonitoringConfig field is set.  
  
### hasDesiredNetworkPerformanceConfig()
    
    
    public boolean hasDesiredNetworkPerformanceConfig()

The desired network performance config.

` .google.container.v1beta1.NetworkConfig.ClusterNetworkPerformanceConfig desired_network_performance_config = 125; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredNetworkPerformanceConfig field is set.  
  
### hasDesiredNetworkTierConfig()
    
    
    public boolean hasDesiredNetworkTierConfig()

The desired network tier configuration for the cluster.

`.google.container.v1beta1.NetworkTierConfig desired_network_tier_config = 155;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredNetworkTierConfig field is set.  
  
### hasDesiredNodeCreationConfig()
    
    
    public boolean hasDesiredNodeCreationConfig()

Optional. The desired NodeCreationConfig for the cluster.

` .google.container.v1beta1.NodeCreationConfig desired_node_creation_config = 171 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredNodeCreationConfig field is set.  
  
### hasDesiredNodeKubeletConfig()
    
    
    public boolean hasDesiredNodeKubeletConfig()

The desired node kubelet config for the cluster.

`.google.container.v1beta1.NodeKubeletConfig desired_node_kubelet_config = 141;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredNodeKubeletConfig field is set.  
  
### hasDesiredNodePoolAutoConfigKubeletConfig()
    
    
    public boolean hasDesiredNodePoolAutoConfigKubeletConfig()

The desired node kubelet config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

` .google.container.v1beta1.NodeKubeletConfig desired_node_pool_auto_config_kubelet_config = 142; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredNodePoolAutoConfigKubeletConfig field is set.  
  
### hasDesiredNodePoolAutoConfigLinuxNodeConfig()
    
    
    public boolean hasDesiredNodePoolAutoConfigLinuxNodeConfig()

The desired Linux node config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

Currently only `cgroup_mode` can be set here.

` .google.container.v1beta1.LinuxNodeConfig desired_node_pool_auto_config_linux_node_config = 150; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredNodePoolAutoConfigLinuxNodeConfig field is set.  
  
### hasDesiredNodePoolAutoConfigNetworkTags()
    
    
    public boolean hasDesiredNodePoolAutoConfigNetworkTags()

The desired network tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

`.google.container.v1beta1.NetworkTags desired_node_pool_auto_config_network_tags = 110; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredNodePoolAutoConfigNetworkTags field is set.  
  
### hasDesiredNodePoolAutoConfigResourceManagerTags()
    
    
    public boolean hasDesiredNodePoolAutoConfigResourceManagerTags()

The desired resource manager tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

` .google.container.v1beta1.ResourceManagerTags desired_node_pool_auto_config_resource_manager_tags = 136; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredNodePoolAutoConfigResourceManagerTags field is set.  
  
### hasDesiredNodePoolAutoscaling()
    
    
    public boolean hasDesiredNodePoolAutoscaling()

Autoscaler configuration for the node pool specified in desired_node_pool_id. If there is only one pool in the cluster and desired_node_pool_id is not provided then the change applies to that single node pool.

`.google.container.v1beta1.NodePoolAutoscaling desired_node_pool_autoscaling = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredNodePoolAutoscaling field is set.  
  
### hasDesiredNodePoolLoggingConfig()
    
    
    public boolean hasDesiredNodePoolLoggingConfig()

The desired node pool logging configuration defaults for the cluster.

`.google.container.v1beta1.NodePoolLoggingConfig desired_node_pool_logging_config = 116; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredNodePoolLoggingConfig field is set.  
  
### hasDesiredNodePoolUpgradeConcurrencyConfig()
    
    
    public boolean hasDesiredNodePoolUpgradeConcurrencyConfig()

The desired node pool upgrade concurrency configuration.

` .google.container.v1beta1.NodePoolUpgradeConcurrencyConfig desired_node_pool_upgrade_concurrency_config = 167; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredNodePoolUpgradeConcurrencyConfig field is set.  
  
### hasDesiredNotificationConfig()
    
    
    public boolean hasDesiredNotificationConfig()

The desired notification configuration.

`.google.container.v1beta1.NotificationConfig desired_notification_config = 55;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredNotificationConfig field is set.  
  
### hasDesiredPodAutoscaling()
    
    
    public boolean hasDesiredPodAutoscaling()

The desired config for pod autoscaling.

`.google.container.v1beta1.PodAutoscaling desired_pod_autoscaling = 113;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredPodAutoscaling field is set.  
  
### hasDesiredPodSecurityPolicyConfig()
    
    
    public boolean hasDesiredPodSecurityPolicyConfig()

The desired configuration options for the PodSecurityPolicy feature.

` .google.container.v1beta1.PodSecurityPolicyConfig desired_pod_security_policy_config = 14; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredPodSecurityPolicyConfig field is set.  
  
### hasDesiredPrivateClusterConfig() (deprecated)
    
    
    public boolean hasDesiredPrivateClusterConfig()

**Deprecated.** _google.container.v1beta1.ClusterUpdate.desired_private_cluster_config is deprecated. See google/container/v1beta1/cluster_service.proto;l=4042_

The desired private cluster configuration. master_global_access_config is the only field that can be changed via this field. See also ClusterUpdate.desired_enable_private_endpoint for modifying other fields within PrivateClusterConfig.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.global_access instead.

` .google.container.v1beta1.PrivateClusterConfig desired_private_cluster_config = 25 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredPrivateClusterConfig field is set.  
  
### hasDesiredPrivilegedAdmissionConfig()
    
    
    public boolean hasDesiredPrivilegedAdmissionConfig()

The desired privileged admission config for the cluster.

` .google.container.v1beta1.PrivilegedAdmissionConfig desired_privileged_admission_config = 159; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredPrivilegedAdmissionConfig field is set.  
  
### hasDesiredProtectConfig() (deprecated)
    
    
    public boolean hasDesiredProtectConfig()

**Deprecated.** _google.container.v1beta1.ClusterUpdate.desired_protect_config is deprecated. See google/container/v1beta1/cluster_service.proto;l=4174_

Deprecated: Use DesiredSecurityPostureConfig instead. Enable/Disable Protect API features for the cluster.

` optional .google.container.v1beta1.ProtectConfig desired_protect_config = 112 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredProtectConfig field is set.  
  
### hasDesiredRbacBindingConfig()
    
    
    public boolean hasDesiredRbacBindingConfig()

RBACBindingConfig allows user to restrict ClusterRoleBindings an RoleBindings that can be created.

`optional .google.container.v1beta1.RBACBindingConfig desired_rbac_binding_config = 144; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredRbacBindingConfig field is set.  
  
### hasDesiredReleaseChannel()
    
    
    public boolean hasDesiredReleaseChannel()

The desired release channel configuration.

`.google.container.v1beta1.ReleaseChannel desired_release_channel = 31;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredReleaseChannel field is set.  
  
### hasDesiredResourceUsageExportConfig()
    
    
    public boolean hasDesiredResourceUsageExportConfig()

The desired configuration for exporting resource usage.

` .google.container.v1beta1.ResourceUsageExportConfig desired_resource_usage_export_config = 21; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredResourceUsageExportConfig field is set.  
  
### hasDesiredRollbackSafeUpgrade()
    
    
    public boolean hasDesiredRollbackSafeUpgrade()

The desired rollback safe upgrade configuration.

`.google.container.v1beta1.RollbackSafeUpgrade desired_rollback_safe_upgrade = 161; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredRollbackSafeUpgrade field is set.  
  
### hasDesiredScheduleUpgradeConfig()
    
    
    public boolean hasDesiredScheduleUpgradeConfig()

Optional. The desired scheduled upgrades configuration for the cluster.

` .google.container.v1beta1.ScheduleUpgradeConfig desired_schedule_upgrade_config = 157 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredScheduleUpgradeConfig field is set.  
  
### hasDesiredSecretManagerConfig()
    
    
    public boolean hasDesiredSecretManagerConfig()

Enable/Disable Secret Manager Config.

` optional .google.container.v1beta1.SecretManagerConfig desired_secret_manager_config = 139; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredSecretManagerConfig field is set.  
  
### hasDesiredSecretSyncConfig()
    
    
    public boolean hasDesiredSecretSyncConfig()

Configuration for sync Secret Manager secrets as k8s secrets.

`.google.container.v1beta1.SecretSyncConfig desired_secret_sync_config = 158;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredSecretSyncConfig field is set.  
  
### hasDesiredSecurityPostureConfig()
    
    
    public boolean hasDesiredSecurityPostureConfig()

Enable/Disable Security Posture API features for the cluster.

`.google.container.v1beta1.SecurityPostureConfig desired_security_posture_config = 124; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredSecurityPostureConfig field is set.  
  
### hasDesiredServiceExternalIpsConfig()
    
    
    public boolean hasDesiredServiceExternalIpsConfig()

ServiceExternalIPsConfig specifies the config for the use of Services with ExternalIPs field.

` .google.container.v1beta1.ServiceExternalIPsConfig desired_service_external_ips_config = 60; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredServiceExternalIpsConfig field is set.  
  
### hasDesiredShieldedNodes()
    
    
    public boolean hasDesiredShieldedNodes()

Configuration for Shielded Nodes.

`.google.container.v1beta1.ShieldedNodes desired_shielded_nodes = 48;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredShieldedNodes field is set.  
  
### hasDesiredTpuConfig() (deprecated)
    
    
    public boolean hasDesiredTpuConfig()

**Deprecated.** _google.container.v1beta1.ClusterUpdate.desired_tpu_config is deprecated. See google/container/v1beta1/cluster_service.proto;l=4064_

The desired Cloud TPU configuration. This field is deprecated due to the deprecation of 2VM TPU. The end of life date for 2VM TPU is 2025-04-25.

`.google.container.v1beta1.TpuConfig desired_tpu_config = 38 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredTpuConfig field is set.  
  
### hasDesiredUserManagedKeysConfig()
    
    
    public boolean hasDesiredUserManagedKeysConfig()

The desired user managed keys config for the cluster.

`.google.container.v1beta1.UserManagedKeysConfig desired_user_managed_keys_config = 152; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredUserManagedKeysConfig field is set.  
  
### hasDesiredVerticalPodAutoscaling()
    
    
    public boolean hasDesiredVerticalPodAutoscaling()

Cluster-level Vertical Pod Autoscaling configuration.

`.google.container.v1beta1.VerticalPodAutoscaling desired_vertical_pod_autoscaling = 22; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredVerticalPodAutoscaling field is set.  
  
### hasDesiredWorkloadAltsConfig()
    
    
    public boolean hasDesiredWorkloadAltsConfig()

Configuration for direct-path (via ALTS) with workload identity. This feature is not officially supported for external customers in Kubernetes Engine when using Workload Identity.

`.google.container.v1beta1.WorkloadALTSConfig desired_workload_alts_config = 62;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredWorkloadAltsConfig field is set.  
  
### hasDesiredWorkloadCertificates()
    
    
    public boolean hasDesiredWorkloadCertificates()

Configuration for issuance of mTLS keys and certificates to Kubernetes pods.

`.google.container.v1beta1.WorkloadCertificates desired_workload_certificates = 61; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredWorkloadCertificates field is set.  
  
### hasDesiredWorkloadIdentityConfig()
    
    
    public boolean hasDesiredWorkloadIdentityConfig()

Configuration for Workload Identity.

`.google.container.v1beta1.WorkloadIdentityConfig desired_workload_identity_config = 47; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desiredWorkloadIdentityConfig field is set.  
  
### hasEnableK8SBetaApis()
    
    
    public boolean hasEnableK8SBetaApis()

Kubernetes open source beta apis enabled on the cluster. Only beta apis

`.google.container.v1beta1.K8sBetaAPIConfig enable_k8s_beta_apis = 122;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the enableK8sBetaApis field is set.  
  
### hasGkeAutoUpgradeConfig()
    
    
    public boolean hasGkeAutoUpgradeConfig()

Configuration for GKE auto upgrade.

`.google.container.v1beta1.GkeAutoUpgradeConfig gke_auto_upgrade_config = 154;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gkeAutoUpgradeConfig field is set.  
  
### hasPrivateClusterConfig() (deprecated)
    
    
    public boolean hasPrivateClusterConfig()

**Deprecated.** _google.container.v1beta1.ClusterUpdate.private_cluster_config is deprecated. See google/container/v1beta1/cluster_service.proto;l=4059_

The desired private cluster configuration. Has no effect. Use desired_private_cluster_config instead.

` .google.container.v1beta1.PrivateClusterConfig private_cluster_config = 37 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the privateClusterConfig field is set.  
  
### hasRemovedAdditionalPodRangesConfig()
    
    
    public boolean hasRemovedAdditionalPodRangesConfig()

The additional pod ranges that are to be removed from the cluster. The pod ranges specified here must have been specified earlier in the 'additional_pod_ranges_config' argument.

` .google.container.v1beta1.AdditionalPodRangesConfig removed_additional_pod_ranges_config = 121; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the removedAdditionalPodRangesConfig field is set.  
  
### hasUserManagedKeysConfig() (deprecated)
    
    
    public boolean hasUserManagedKeysConfig()

**Deprecated.** _google.container.v1beta1.ClusterUpdate.user_managed_keys_config is deprecated. See google/container/v1beta1/cluster_service.proto;l=4271_

The Custom keys configuration for the cluster.

This field is deprecated. Use ClusterUpdate.desired_user_managed_keys_config instead.

` .google.container.v1beta1.UserManagedKeysConfig user_managed_keys_config = 143 [deprecated = true]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the userManagedKeysConfig field is set.  
  
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

### mergeAdditionalPodRangesConfig(AdditionalPodRangesConfig value)
    
    
    public ClusterUpdate.Builder mergeAdditionalPodRangesConfig(AdditionalPodRangesConfig value)

The additional pod ranges to be added to the cluster. These pod ranges can be used by node pools to allocate pod IPs.

`.google.container.v1beta1.AdditionalPodRangesConfig additional_pod_ranges_config = 120; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AdditionalPodRangesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AdditionalPodRangesConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredAdditionalIpRangesConfig(DesiredAdditionalIPRangesConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredAdditionalIpRangesConfig(DesiredAdditionalIPRangesConfig value)

The desired config for additional subnetworks attached to the cluster.

` .google.container.v1beta1.DesiredAdditionalIPRangesConfig desired_additional_ip_ranges_config = 145; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DesiredAdditionalIPRangesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DesiredAdditionalIPRangesConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredAddonsConfig(AddonsConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredAddonsConfig(AddonsConfig value)

Configurations for the various addons available to run in the cluster.

`.google.container.v1beta1.AddonsConfig desired_addons_config = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AddonsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AddonsConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredAnonymousAuthenticationConfig(AnonymousAuthenticationConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredAnonymousAuthenticationConfig(AnonymousAuthenticationConfig value)

Configuration for limiting anonymous access to all endpoints except the health checks.

` .google.container.v1beta1.AnonymousAuthenticationConfig desired_anonymous_authentication_config = 156; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AnonymousAuthenticationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AnonymousAuthenticationConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredAuthenticatorGroupsConfig(AuthenticatorGroupsConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredAuthenticatorGroupsConfig(AuthenticatorGroupsConfig value)

AuthenticatorGroupsConfig specifies the config for the cluster security groups settings.

` .google.container.v1beta1.AuthenticatorGroupsConfig desired_authenticator_groups_config = 63; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AuthenticatorGroupsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AuthenticatorGroupsConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredAutoIpamConfig(AutoIpamConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredAutoIpamConfig(AutoIpamConfig value)

AutoIpamConfig contains all information related to Auto IPAM

`.google.container.v1beta1.AutoIpamConfig desired_auto_ipam_config = 148;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AutoIpamConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AutoIpamConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredAutopilotClusterPolicyConfig(ClusterPolicyConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredAutopilotClusterPolicyConfig(ClusterPolicyConfig value)

The desired autopilot cluster policies that to be enforced in the cluster.

` .google.container.v1beta1.ClusterPolicyConfig desired_autopilot_cluster_policy_config = 164; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ClusterPolicyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterPolicyConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredAutopilotWorkloadPolicyConfig(WorkloadPolicyConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredAutopilotWorkloadPolicyConfig(WorkloadPolicyConfig value)

WorkloadPolicyConfig is the configuration related to GCW workload policy

` .google.container.v1beta1.WorkloadPolicyConfig desired_autopilot_workload_policy_config = 128; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WorkloadPolicyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadPolicyConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredBinaryAuthorization(BinaryAuthorization value)
    
    
    public ClusterUpdate.Builder mergeDesiredBinaryAuthorization(BinaryAuthorization value)

The desired configuration options for the Binary Authorization feature.

`.google.container.v1beta1.BinaryAuthorization desired_binary_authorization = 16;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BinaryAuthorization](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.BinaryAuthorization)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredClusterAutoscaling(ClusterAutoscaling value)
    
    
    public ClusterUpdate.Builder mergeDesiredClusterAutoscaling(ClusterAutoscaling value)

Cluster-level autoscaling configuration.

`.google.container.v1beta1.ClusterAutoscaling desired_cluster_autoscaling = 15;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ClusterAutoscaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterAutoscaling)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredClusterTelemetry(ClusterTelemetry value)
    
    
    public ClusterUpdate.Builder mergeDesiredClusterTelemetry(ClusterTelemetry value)

The desired telemetry integration for the cluster.

`.google.container.v1beta1.ClusterTelemetry desired_cluster_telemetry = 30;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ClusterTelemetry](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterTelemetry)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredCompliancePostureConfig(CompliancePostureConfig value) (deprecated)
    
    
    public ClusterUpdate.Builder mergeDesiredCompliancePostureConfig(CompliancePostureConfig value)

Deprecated: Compliance Posture is no longer supported. For more details, see <https://cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation>.

Enable/Disable Compliance Posture features for the cluster.

` optional .google.container.v1beta1.CompliancePostureConfig desired_compliance_posture_config = 140 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CompliancePostureConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.CompliancePostureConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredContainerdConfig(ContainerdConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredContainerdConfig(ContainerdConfig value)

The desired containerd config for the cluster.

`.google.container.v1beta1.ContainerdConfig desired_containerd_config = 134;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ContainerdConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ContainerdConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredControlPlaneEgress(ControlPlaneEgress value)
    
    
    public ClusterUpdate.Builder mergeDesiredControlPlaneEgress(ControlPlaneEgress value)

The desired control plane egress control config for the cluster.

`.google.container.v1beta1.ControlPlaneEgress desired_control_plane_egress = 160;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ControlPlaneEgress](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ControlPlaneEgress)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredControlPlaneEndpointsConfig(ControlPlaneEndpointsConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredControlPlaneEndpointsConfig(ControlPlaneEndpointsConfig value)

Control plane endpoints configuration.

` .google.container.v1beta1.ControlPlaneEndpointsConfig desired_control_plane_endpoints_config = 73; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ControlPlaneEndpointsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ControlPlaneEndpointsConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredCostManagementConfig(CostManagementConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredCostManagementConfig(CostManagementConfig value)

The desired configuration for the fine-grained cost management feature.

`.google.container.v1beta1.CostManagementConfig desired_cost_management_config = 49; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CostManagementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.CostManagementConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredDatabaseEncryption(DatabaseEncryption value)
    
    
    public ClusterUpdate.Builder mergeDesiredDatabaseEncryption(DatabaseEncryption value)

Configuration of etcd encryption.

`.google.container.v1beta1.DatabaseEncryption desired_database_encryption = 46;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DatabaseEncryption](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DatabaseEncryption)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredDefaultSnatStatus(DefaultSnatStatus value)
    
    
    public ClusterUpdate.Builder mergeDesiredDefaultSnatStatus(DefaultSnatStatus value)

The desired status of whether to disable default sNAT for this cluster.

`.google.container.v1beta1.DefaultSnatStatus desired_default_snat_status = 28;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DefaultSnatStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DefaultSnatStatus)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredDnsConfig(DNSConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredDnsConfig(DNSConfig value)

DNSConfig contains clusterDNS config for this cluster.

`.google.container.v1beta1.DNSConfig desired_dns_config = 53;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DNSConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DNSConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredEnterpriseConfig(DesiredEnterpriseConfig value) (deprecated)
    
    
    public ClusterUpdate.Builder mergeDesiredEnterpriseConfig(DesiredEnterpriseConfig value)

The desired enterprise configuration for the cluster.

Deprecated: GKE Enterprise features are now available without an Enterprise tier.

` .google.container.v1beta1.DesiredEnterpriseConfig desired_enterprise_config = 147 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DesiredEnterpriseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DesiredEnterpriseConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredFleet(Fleet value)
    
    
    public ClusterUpdate.Builder mergeDesiredFleet(Fleet value)

The desired fleet configuration for the cluster.

`.google.container.v1beta1.Fleet desired_fleet = 117;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Fleet](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Fleet)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredGatewayApiConfig(GatewayAPIConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredGatewayApiConfig(GatewayAPIConfig value)

The desired config of Gateway API on this cluster.

`.google.container.v1beta1.GatewayAPIConfig desired_gateway_api_config = 114;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[GatewayAPIConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GatewayAPIConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredGcfsConfig(GcfsConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredGcfsConfig(GcfsConfig value)

The desired GCFS config for the cluster.

`.google.container.v1beta1.GcfsConfig desired_gcfs_config = 109;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[GcfsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GcfsConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredHostMaintenancePolicy(HostMaintenancePolicy value)
    
    
    public ClusterUpdate.Builder mergeDesiredHostMaintenancePolicy(HostMaintenancePolicy value)

HostMaintenancePolicy contains the desired maintenance policy for the Google Compute Engine hosts.

`.google.container.v1beta1.HostMaintenancePolicy desired_host_maintenance_policy = 132; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[HostMaintenancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.HostMaintenancePolicy)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredIdentityServiceConfig(IdentityServiceConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredIdentityServiceConfig(IdentityServiceConfig value)

The desired Identity Service component configuration.

`.google.container.v1beta1.IdentityServiceConfig desired_identity_service_config = 66; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[IdentityServiceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.IdentityServiceConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredIntraNodeVisibilityConfig(IntraNodeVisibilityConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredIntraNodeVisibilityConfig(IntraNodeVisibilityConfig value)

The desired config of Intra-node visibility.

` .google.container.v1beta1.IntraNodeVisibilityConfig desired_intra_node_visibility_config = 26; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[IntraNodeVisibilityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.IntraNodeVisibilityConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredK8SBetaApis(K8sBetaAPIConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredK8SBetaApis(K8sBetaAPIConfig value)

Beta APIs enabled for cluster.

`.google.container.v1beta1.K8sBetaAPIConfig desired_k8s_beta_apis = 131;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[K8sBetaAPIConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.K8sBetaAPIConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredL4IlbSubsettingConfig(ILBSubsettingConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredL4IlbSubsettingConfig(ILBSubsettingConfig value)

The desired L4 Internal Load Balancer Subsetting configuration.

`.google.container.v1beta1.ILBSubsettingConfig desired_l4ilb_subsetting_config = 39; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ILBSubsettingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ILBSubsettingConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredLoggingConfig(LoggingConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredLoggingConfig(LoggingConfig value)

The desired logging configuration.

`.google.container.v1beta1.LoggingConfig desired_logging_config = 64;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[LoggingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.LoggingConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredManagedMachineLearningDiagnosticsConfig(ManagedMachineLearningDiagnosticsConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredManagedMachineLearningDiagnosticsConfig(ManagedMachineLearningDiagnosticsConfig value)

The desired managed machine learning diagnostics configuration.

` .google.container.v1beta1.ManagedMachineLearningDiagnosticsConfig desired_managed_machine_learning_diagnostics_config = 166; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ManagedMachineLearningDiagnosticsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ManagedMachineLearningDiagnosticsConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredManagedOpentelemetryConfig(ManagedOpenTelemetryConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredManagedOpentelemetryConfig(ManagedOpenTelemetryConfig value)

The desired managed open telemetry configuration.

` .google.container.v1beta1.ManagedOpenTelemetryConfig desired_managed_opentelemetry_config = 163; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ManagedOpenTelemetryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ManagedOpenTelemetryConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredMaster(Master value)
    
    
    public ClusterUpdate.Builder mergeDesiredMaster(Master value)

Configuration for master components.

`.google.container.v1beta1.Master desired_master = 52;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Master](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Master)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredMasterAuthorizedNetworksConfig(MasterAuthorizedNetworksConfig value) (deprecated)
    
    
    public ClusterUpdate.Builder mergeDesiredMasterAuthorizedNetworksConfig(MasterAuthorizedNetworksConfig value)

The desired configuration options for master authorized networks feature.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.authorized_networks_config instead.

` .google.container.v1beta1.MasterAuthorizedNetworksConfig desired_master_authorized_networks_config = 12 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MasterAuthorizedNetworksConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.MasterAuthorizedNetworksConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredMeshCertificates(MeshCertificates value)
    
    
    public ClusterUpdate.Builder mergeDesiredMeshCertificates(MeshCertificates value)

Configuration for issuance of mTLS keys and certificates to Kubernetes pods.

`.google.container.v1beta1.MeshCertificates desired_mesh_certificates = 67;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MeshCertificates](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.MeshCertificates)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredMonitoringConfig(MonitoringConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredMonitoringConfig(MonitoringConfig value)

The desired monitoring configuration.

`.google.container.v1beta1.MonitoringConfig desired_monitoring_config = 65;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MonitoringConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.MonitoringConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredNetworkPerformanceConfig(NetworkConfig.ClusterNetworkPerformanceConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredNetworkPerformanceConfig(NetworkConfig.ClusterNetworkPerformanceConfig value)

The desired network performance config.

` .google.container.v1beta1.NetworkConfig.ClusterNetworkPerformanceConfig desired_network_performance_config = 125; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NetworkConfig.ClusterNetworkPerformanceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NetworkConfig.ClusterNetworkPerformanceConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredNetworkTierConfig(NetworkTierConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredNetworkTierConfig(NetworkTierConfig value)

The desired network tier configuration for the cluster.

`.google.container.v1beta1.NetworkTierConfig desired_network_tier_config = 155;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NetworkTierConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NetworkTierConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredNodeCreationConfig(NodeCreationConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredNodeCreationConfig(NodeCreationConfig value)

Optional. The desired NodeCreationConfig for the cluster.

` .google.container.v1beta1.NodeCreationConfig desired_node_creation_config = 171 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NodeCreationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeCreationConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredNodeKubeletConfig(NodeKubeletConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredNodeKubeletConfig(NodeKubeletConfig value)

The desired node kubelet config for the cluster.

`.google.container.v1beta1.NodeKubeletConfig desired_node_kubelet_config = 141;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NodeKubeletConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeKubeletConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredNodePoolAutoConfigKubeletConfig(NodeKubeletConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredNodePoolAutoConfigKubeletConfig(NodeKubeletConfig value)

The desired node kubelet config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

` .google.container.v1beta1.NodeKubeletConfig desired_node_pool_auto_config_kubelet_config = 142; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NodeKubeletConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeKubeletConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredNodePoolAutoConfigLinuxNodeConfig(LinuxNodeConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredNodePoolAutoConfigLinuxNodeConfig(LinuxNodeConfig value)

The desired Linux node config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

Currently only `cgroup_mode` can be set here.

` .google.container.v1beta1.LinuxNodeConfig desired_node_pool_auto_config_linux_node_config = 150; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[LinuxNodeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.LinuxNodeConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredNodePoolAutoConfigNetworkTags(NetworkTags value)
    
    
    public ClusterUpdate.Builder mergeDesiredNodePoolAutoConfigNetworkTags(NetworkTags value)

The desired network tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

`.google.container.v1beta1.NetworkTags desired_node_pool_auto_config_network_tags = 110; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NetworkTags](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NetworkTags)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredNodePoolAutoConfigResourceManagerTags(ResourceManagerTags value)
    
    
    public ClusterUpdate.Builder mergeDesiredNodePoolAutoConfigResourceManagerTags(ResourceManagerTags value)

The desired resource manager tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

` .google.container.v1beta1.ResourceManagerTags desired_node_pool_auto_config_resource_manager_tags = 136; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ResourceManagerTags](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ResourceManagerTags)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredNodePoolAutoscaling(NodePoolAutoscaling value)
    
    
    public ClusterUpdate.Builder mergeDesiredNodePoolAutoscaling(NodePoolAutoscaling value)

Autoscaler configuration for the node pool specified in desired_node_pool_id. If there is only one pool in the cluster and desired_node_pool_id is not provided then the change applies to that single node pool.

`.google.container.v1beta1.NodePoolAutoscaling desired_node_pool_autoscaling = 9;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NodePoolAutoscaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolAutoscaling)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredNodePoolLoggingConfig(NodePoolLoggingConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredNodePoolLoggingConfig(NodePoolLoggingConfig value)

The desired node pool logging configuration defaults for the cluster.

`.google.container.v1beta1.NodePoolLoggingConfig desired_node_pool_logging_config = 116; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NodePoolLoggingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolLoggingConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredNodePoolUpgradeConcurrencyConfig(NodePoolUpgradeConcurrencyConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredNodePoolUpgradeConcurrencyConfig(NodePoolUpgradeConcurrencyConfig value)

The desired node pool upgrade concurrency configuration.

` .google.container.v1beta1.NodePoolUpgradeConcurrencyConfig desired_node_pool_upgrade_concurrency_config = 167; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NodePoolUpgradeConcurrencyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolUpgradeConcurrencyConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredNotificationConfig(NotificationConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredNotificationConfig(NotificationConfig value)

The desired notification configuration.

`.google.container.v1beta1.NotificationConfig desired_notification_config = 55;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NotificationConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredPodAutoscaling(PodAutoscaling value)
    
    
    public ClusterUpdate.Builder mergeDesiredPodAutoscaling(PodAutoscaling value)

The desired config for pod autoscaling.

`.google.container.v1beta1.PodAutoscaling desired_pod_autoscaling = 113;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PodAutoscaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PodAutoscaling)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredPodSecurityPolicyConfig(PodSecurityPolicyConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredPodSecurityPolicyConfig(PodSecurityPolicyConfig value)

The desired configuration options for the PodSecurityPolicy feature.

` .google.container.v1beta1.PodSecurityPolicyConfig desired_pod_security_policy_config = 14; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PodSecurityPolicyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PodSecurityPolicyConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredPrivateClusterConfig(PrivateClusterConfig value) (deprecated)
    
    
    public ClusterUpdate.Builder mergeDesiredPrivateClusterConfig(PrivateClusterConfig value)

The desired private cluster configuration. master_global_access_config is the only field that can be changed via this field. See also ClusterUpdate.desired_enable_private_endpoint for modifying other fields within PrivateClusterConfig.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.global_access instead.

` .google.container.v1beta1.PrivateClusterConfig desired_private_cluster_config = 25 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PrivateClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PrivateClusterConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredPrivilegedAdmissionConfig(PrivilegedAdmissionConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredPrivilegedAdmissionConfig(PrivilegedAdmissionConfig value)

The desired privileged admission config for the cluster.

` .google.container.v1beta1.PrivilegedAdmissionConfig desired_privileged_admission_config = 159; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PrivilegedAdmissionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PrivilegedAdmissionConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredProtectConfig(ProtectConfig value) (deprecated)
    
    
    public ClusterUpdate.Builder mergeDesiredProtectConfig(ProtectConfig value)

Deprecated: Use DesiredSecurityPostureConfig instead. Enable/Disable Protect API features for the cluster.

` optional .google.container.v1beta1.ProtectConfig desired_protect_config = 112 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ProtectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ProtectConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredRbacBindingConfig(RBACBindingConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredRbacBindingConfig(RBACBindingConfig value)

RBACBindingConfig allows user to restrict ClusterRoleBindings an RoleBindings that can be created.

`optional .google.container.v1beta1.RBACBindingConfig desired_rbac_binding_config = 144; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[RBACBindingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.RBACBindingConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredReleaseChannel(ReleaseChannel value)
    
    
    public ClusterUpdate.Builder mergeDesiredReleaseChannel(ReleaseChannel value)

The desired release channel configuration.

`.google.container.v1beta1.ReleaseChannel desired_release_channel = 31;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ReleaseChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ReleaseChannel)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredResourceUsageExportConfig(ResourceUsageExportConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredResourceUsageExportConfig(ResourceUsageExportConfig value)

The desired configuration for exporting resource usage.

` .google.container.v1beta1.ResourceUsageExportConfig desired_resource_usage_export_config = 21; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ResourceUsageExportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ResourceUsageExportConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredRollbackSafeUpgrade(RollbackSafeUpgrade value)
    
    
    public ClusterUpdate.Builder mergeDesiredRollbackSafeUpgrade(RollbackSafeUpgrade value)

The desired rollback safe upgrade configuration.

`.google.container.v1beta1.RollbackSafeUpgrade desired_rollback_safe_upgrade = 161; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[RollbackSafeUpgrade](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.RollbackSafeUpgrade)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredScheduleUpgradeConfig(ScheduleUpgradeConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredScheduleUpgradeConfig(ScheduleUpgradeConfig value)

Optional. The desired scheduled upgrades configuration for the cluster.

` .google.container.v1beta1.ScheduleUpgradeConfig desired_schedule_upgrade_config = 157 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ScheduleUpgradeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ScheduleUpgradeConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredSecretManagerConfig(SecretManagerConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredSecretManagerConfig(SecretManagerConfig value)

Enable/Disable Secret Manager Config.

` optional .google.container.v1beta1.SecretManagerConfig desired_secret_manager_config = 139; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SecretManagerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SecretManagerConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredSecretSyncConfig(SecretSyncConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredSecretSyncConfig(SecretSyncConfig value)

Configuration for sync Secret Manager secrets as k8s secrets.

`.google.container.v1beta1.SecretSyncConfig desired_secret_sync_config = 158;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SecretSyncConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SecretSyncConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredSecurityPostureConfig(SecurityPostureConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredSecurityPostureConfig(SecurityPostureConfig value)

Enable/Disable Security Posture API features for the cluster.

`.google.container.v1beta1.SecurityPostureConfig desired_security_posture_config = 124; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SecurityPostureConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SecurityPostureConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredServiceExternalIpsConfig(ServiceExternalIPsConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredServiceExternalIpsConfig(ServiceExternalIPsConfig value)

ServiceExternalIPsConfig specifies the config for the use of Services with ExternalIPs field.

` .google.container.v1beta1.ServiceExternalIPsConfig desired_service_external_ips_config = 60; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ServiceExternalIPsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ServiceExternalIPsConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredShieldedNodes(ShieldedNodes value)
    
    
    public ClusterUpdate.Builder mergeDesiredShieldedNodes(ShieldedNodes value)

Configuration for Shielded Nodes.

`.google.container.v1beta1.ShieldedNodes desired_shielded_nodes = 48;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ShieldedNodes](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ShieldedNodes)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredTpuConfig(TpuConfig value) (deprecated)
    
    
    public ClusterUpdate.Builder mergeDesiredTpuConfig(TpuConfig value)

The desired Cloud TPU configuration. This field is deprecated due to the deprecation of 2VM TPU. The end of life date for 2VM TPU is 2025-04-25.

`.google.container.v1beta1.TpuConfig desired_tpu_config = 38 [deprecated = true];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[TpuConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.TpuConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredUserManagedKeysConfig(UserManagedKeysConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredUserManagedKeysConfig(UserManagedKeysConfig value)

The desired user managed keys config for the cluster.

`.google.container.v1beta1.UserManagedKeysConfig desired_user_managed_keys_config = 152; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[UserManagedKeysConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.UserManagedKeysConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredVerticalPodAutoscaling(VerticalPodAutoscaling value)
    
    
    public ClusterUpdate.Builder mergeDesiredVerticalPodAutoscaling(VerticalPodAutoscaling value)

Cluster-level Vertical Pod Autoscaling configuration.

`.google.container.v1beta1.VerticalPodAutoscaling desired_vertical_pod_autoscaling = 22; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[VerticalPodAutoscaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.VerticalPodAutoscaling)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredWorkloadAltsConfig(WorkloadALTSConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredWorkloadAltsConfig(WorkloadALTSConfig value)

Configuration for direct-path (via ALTS) with workload identity. This feature is not officially supported for external customers in Kubernetes Engine when using Workload Identity.

`.google.container.v1beta1.WorkloadALTSConfig desired_workload_alts_config = 62;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WorkloadALTSConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadALTSConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredWorkloadCertificates(WorkloadCertificates value)
    
    
    public ClusterUpdate.Builder mergeDesiredWorkloadCertificates(WorkloadCertificates value)

Configuration for issuance of mTLS keys and certificates to Kubernetes pods.

`.google.container.v1beta1.WorkloadCertificates desired_workload_certificates = 61; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WorkloadCertificates](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadCertificates)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeDesiredWorkloadIdentityConfig(WorkloadIdentityConfig value)
    
    
    public ClusterUpdate.Builder mergeDesiredWorkloadIdentityConfig(WorkloadIdentityConfig value)

Configuration for Workload Identity.

`.google.container.v1beta1.WorkloadIdentityConfig desired_workload_identity_config = 47; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WorkloadIdentityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadIdentityConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeEnableK8SBetaApis(K8sBetaAPIConfig value)
    
    
    public ClusterUpdate.Builder mergeEnableK8SBetaApis(K8sBetaAPIConfig value)

Kubernetes open source beta apis enabled on the cluster. Only beta apis

`.google.container.v1beta1.K8sBetaAPIConfig enable_k8s_beta_apis = 122;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[K8sBetaAPIConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.K8sBetaAPIConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeFrom(ClusterUpdate other)
    
    
    public ClusterUpdate.Builder mergeFrom(ClusterUpdate other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ClusterUpdate](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public ClusterUpdate.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public ClusterUpdate.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeGkeAutoUpgradeConfig(GkeAutoUpgradeConfig value)
    
    
    public ClusterUpdate.Builder mergeGkeAutoUpgradeConfig(GkeAutoUpgradeConfig value)

Configuration for GKE auto upgrade.

`.google.container.v1beta1.GkeAutoUpgradeConfig gke_auto_upgrade_config = 154;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[GkeAutoUpgradeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GkeAutoUpgradeConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergePrivateClusterConfig(PrivateClusterConfig value) (deprecated)
    
    
    public ClusterUpdate.Builder mergePrivateClusterConfig(PrivateClusterConfig value)

The desired private cluster configuration. Has no effect. Use desired_private_cluster_config instead.

` .google.container.v1beta1.PrivateClusterConfig private_cluster_config = 37 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PrivateClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PrivateClusterConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeRemovedAdditionalPodRangesConfig(AdditionalPodRangesConfig value)
    
    
    public ClusterUpdate.Builder mergeRemovedAdditionalPodRangesConfig(AdditionalPodRangesConfig value)

The additional pod ranges that are to be removed from the cluster. The pod ranges specified here must have been specified earlier in the 'additional_pod_ranges_config' argument.

` .google.container.v1beta1.AdditionalPodRangesConfig removed_additional_pod_ranges_config = 121; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AdditionalPodRangesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AdditionalPodRangesConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### mergeUserManagedKeysConfig(UserManagedKeysConfig value) (deprecated)
    
    
    public ClusterUpdate.Builder mergeUserManagedKeysConfig(UserManagedKeysConfig value)

The Custom keys configuration for the cluster.

This field is deprecated. Use ClusterUpdate.desired_user_managed_keys_config instead.

` .google.container.v1beta1.UserManagedKeysConfig user_managed_keys_config = 143 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[UserManagedKeysConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.UserManagedKeysConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setAdditionalPodRangesConfig(AdditionalPodRangesConfig value)
    
    
    public ClusterUpdate.Builder setAdditionalPodRangesConfig(AdditionalPodRangesConfig value)

The additional pod ranges to be added to the cluster. These pod ranges can be used by node pools to allocate pod IPs.

`.google.container.v1beta1.AdditionalPodRangesConfig additional_pod_ranges_config = 120; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AdditionalPodRangesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AdditionalPodRangesConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setAdditionalPodRangesConfig(AdditionalPodRangesConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setAdditionalPodRangesConfig(AdditionalPodRangesConfig.Builder builderForValue)

The additional pod ranges to be added to the cluster. These pod ranges can be used by node pools to allocate pod IPs.

`.google.container.v1beta1.AdditionalPodRangesConfig additional_pod_ranges_config = 120; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[AdditionalPodRangesConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AdditionalPodRangesConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredAdditionalIpRangesConfig(DesiredAdditionalIPRangesConfig value)
    
    
    public ClusterUpdate.Builder setDesiredAdditionalIpRangesConfig(DesiredAdditionalIPRangesConfig value)

The desired config for additional subnetworks attached to the cluster.

` .google.container.v1beta1.DesiredAdditionalIPRangesConfig desired_additional_ip_ranges_config = 145; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DesiredAdditionalIPRangesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DesiredAdditionalIPRangesConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredAdditionalIpRangesConfig(DesiredAdditionalIPRangesConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredAdditionalIpRangesConfig(DesiredAdditionalIPRangesConfig.Builder builderForValue)

The desired config for additional subnetworks attached to the cluster.

` .google.container.v1beta1.DesiredAdditionalIPRangesConfig desired_additional_ip_ranges_config = 145; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[DesiredAdditionalIPRangesConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DesiredAdditionalIPRangesConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredAddonsConfig(AddonsConfig value)
    
    
    public ClusterUpdate.Builder setDesiredAddonsConfig(AddonsConfig value)

Configurations for the various addons available to run in the cluster.

`.google.container.v1beta1.AddonsConfig desired_addons_config = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AddonsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AddonsConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredAddonsConfig(AddonsConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredAddonsConfig(AddonsConfig.Builder builderForValue)

Configurations for the various addons available to run in the cluster.

`.google.container.v1beta1.AddonsConfig desired_addons_config = 6;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[AddonsConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AddonsConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredAnonymousAuthenticationConfig(AnonymousAuthenticationConfig value)
    
    
    public ClusterUpdate.Builder setDesiredAnonymousAuthenticationConfig(AnonymousAuthenticationConfig value)

Configuration for limiting anonymous access to all endpoints except the health checks.

` .google.container.v1beta1.AnonymousAuthenticationConfig desired_anonymous_authentication_config = 156; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AnonymousAuthenticationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AnonymousAuthenticationConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredAnonymousAuthenticationConfig(AnonymousAuthenticationConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredAnonymousAuthenticationConfig(AnonymousAuthenticationConfig.Builder builderForValue)

Configuration for limiting anonymous access to all endpoints except the health checks.

` .google.container.v1beta1.AnonymousAuthenticationConfig desired_anonymous_authentication_config = 156; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[AnonymousAuthenticationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AnonymousAuthenticationConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredAuthenticatorGroupsConfig(AuthenticatorGroupsConfig value)
    
    
    public ClusterUpdate.Builder setDesiredAuthenticatorGroupsConfig(AuthenticatorGroupsConfig value)

AuthenticatorGroupsConfig specifies the config for the cluster security groups settings.

` .google.container.v1beta1.AuthenticatorGroupsConfig desired_authenticator_groups_config = 63; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AuthenticatorGroupsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AuthenticatorGroupsConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredAuthenticatorGroupsConfig(AuthenticatorGroupsConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredAuthenticatorGroupsConfig(AuthenticatorGroupsConfig.Builder builderForValue)

AuthenticatorGroupsConfig specifies the config for the cluster security groups settings.

` .google.container.v1beta1.AuthenticatorGroupsConfig desired_authenticator_groups_config = 63; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[AuthenticatorGroupsConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AuthenticatorGroupsConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredAutoIpamConfig(AutoIpamConfig value)
    
    
    public ClusterUpdate.Builder setDesiredAutoIpamConfig(AutoIpamConfig value)

AutoIpamConfig contains all information related to Auto IPAM

`.google.container.v1beta1.AutoIpamConfig desired_auto_ipam_config = 148;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AutoIpamConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AutoIpamConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredAutoIpamConfig(AutoIpamConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredAutoIpamConfig(AutoIpamConfig.Builder builderForValue)

AutoIpamConfig contains all information related to Auto IPAM

`.google.container.v1beta1.AutoIpamConfig desired_auto_ipam_config = 148;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[AutoIpamConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AutoIpamConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredAutopilotClusterPolicyConfig(ClusterPolicyConfig value)
    
    
    public ClusterUpdate.Builder setDesiredAutopilotClusterPolicyConfig(ClusterPolicyConfig value)

The desired autopilot cluster policies that to be enforced in the cluster.

` .google.container.v1beta1.ClusterPolicyConfig desired_autopilot_cluster_policy_config = 164; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ClusterPolicyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterPolicyConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredAutopilotClusterPolicyConfig(ClusterPolicyConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredAutopilotClusterPolicyConfig(ClusterPolicyConfig.Builder builderForValue)

The desired autopilot cluster policies that to be enforced in the cluster.

` .google.container.v1beta1.ClusterPolicyConfig desired_autopilot_cluster_policy_config = 164; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ClusterPolicyConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterPolicyConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredAutopilotWorkloadPolicyConfig(WorkloadPolicyConfig value)
    
    
    public ClusterUpdate.Builder setDesiredAutopilotWorkloadPolicyConfig(WorkloadPolicyConfig value)

WorkloadPolicyConfig is the configuration related to GCW workload policy

` .google.container.v1beta1.WorkloadPolicyConfig desired_autopilot_workload_policy_config = 128; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WorkloadPolicyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadPolicyConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredAutopilotWorkloadPolicyConfig(WorkloadPolicyConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredAutopilotWorkloadPolicyConfig(WorkloadPolicyConfig.Builder builderForValue)

WorkloadPolicyConfig is the configuration related to GCW workload policy

` .google.container.v1beta1.WorkloadPolicyConfig desired_autopilot_workload_policy_config = 128; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[WorkloadPolicyConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadPolicyConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredBinaryAuthorization(BinaryAuthorization value)
    
    
    public ClusterUpdate.Builder setDesiredBinaryAuthorization(BinaryAuthorization value)

The desired configuration options for the Binary Authorization feature.

`.google.container.v1beta1.BinaryAuthorization desired_binary_authorization = 16;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BinaryAuthorization](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.BinaryAuthorization)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredBinaryAuthorization(BinaryAuthorization.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredBinaryAuthorization(BinaryAuthorization.Builder builderForValue)

The desired configuration options for the Binary Authorization feature.

`.google.container.v1beta1.BinaryAuthorization desired_binary_authorization = 16;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[BinaryAuthorization.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.BinaryAuthorization.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredClusterAutoscaling(ClusterAutoscaling value)
    
    
    public ClusterUpdate.Builder setDesiredClusterAutoscaling(ClusterAutoscaling value)

Cluster-level autoscaling configuration.

`.google.container.v1beta1.ClusterAutoscaling desired_cluster_autoscaling = 15;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ClusterAutoscaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterAutoscaling)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredClusterAutoscaling(ClusterAutoscaling.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredClusterAutoscaling(ClusterAutoscaling.Builder builderForValue)

Cluster-level autoscaling configuration.

`.google.container.v1beta1.ClusterAutoscaling desired_cluster_autoscaling = 15;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ClusterAutoscaling.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterAutoscaling.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredClusterTelemetry(ClusterTelemetry value)
    
    
    public ClusterUpdate.Builder setDesiredClusterTelemetry(ClusterTelemetry value)

The desired telemetry integration for the cluster.

`.google.container.v1beta1.ClusterTelemetry desired_cluster_telemetry = 30;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ClusterTelemetry](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterTelemetry)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredClusterTelemetry(ClusterTelemetry.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredClusterTelemetry(ClusterTelemetry.Builder builderForValue)

The desired telemetry integration for the cluster.

`.google.container.v1beta1.ClusterTelemetry desired_cluster_telemetry = 30;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ClusterTelemetry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterTelemetry.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredCompliancePostureConfig(CompliancePostureConfig value) (deprecated)
    
    
    public ClusterUpdate.Builder setDesiredCompliancePostureConfig(CompliancePostureConfig value)

Deprecated: Compliance Posture is no longer supported. For more details, see <https://cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation>.

Enable/Disable Compliance Posture features for the cluster.

` optional .google.container.v1beta1.CompliancePostureConfig desired_compliance_posture_config = 140 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CompliancePostureConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.CompliancePostureConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredCompliancePostureConfig(CompliancePostureConfig.Builder builderForValue) (deprecated)
    
    
    public ClusterUpdate.Builder setDesiredCompliancePostureConfig(CompliancePostureConfig.Builder builderForValue)

Deprecated: Compliance Posture is no longer supported. For more details, see <https://cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation>.

Enable/Disable Compliance Posture features for the cluster.

` optional .google.container.v1beta1.CompliancePostureConfig desired_compliance_posture_config = 140 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[CompliancePostureConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.CompliancePostureConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredContainerdConfig(ContainerdConfig value)
    
    
    public ClusterUpdate.Builder setDesiredContainerdConfig(ContainerdConfig value)

The desired containerd config for the cluster.

`.google.container.v1beta1.ContainerdConfig desired_containerd_config = 134;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ContainerdConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ContainerdConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredContainerdConfig(ContainerdConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredContainerdConfig(ContainerdConfig.Builder builderForValue)

The desired containerd config for the cluster.

`.google.container.v1beta1.ContainerdConfig desired_containerd_config = 134;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ContainerdConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ContainerdConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredControlPlaneEgress(ControlPlaneEgress value)
    
    
    public ClusterUpdate.Builder setDesiredControlPlaneEgress(ControlPlaneEgress value)

The desired control plane egress control config for the cluster.

`.google.container.v1beta1.ControlPlaneEgress desired_control_plane_egress = 160;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ControlPlaneEgress](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ControlPlaneEgress)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredControlPlaneEgress(ControlPlaneEgress.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredControlPlaneEgress(ControlPlaneEgress.Builder builderForValue)

The desired control plane egress control config for the cluster.

`.google.container.v1beta1.ControlPlaneEgress desired_control_plane_egress = 160;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ControlPlaneEgress.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ControlPlaneEgress.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredControlPlaneEndpointsConfig(ControlPlaneEndpointsConfig value)
    
    
    public ClusterUpdate.Builder setDesiredControlPlaneEndpointsConfig(ControlPlaneEndpointsConfig value)

Control plane endpoints configuration.

` .google.container.v1beta1.ControlPlaneEndpointsConfig desired_control_plane_endpoints_config = 73; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ControlPlaneEndpointsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ControlPlaneEndpointsConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredControlPlaneEndpointsConfig(ControlPlaneEndpointsConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredControlPlaneEndpointsConfig(ControlPlaneEndpointsConfig.Builder builderForValue)

Control plane endpoints configuration.

` .google.container.v1beta1.ControlPlaneEndpointsConfig desired_control_plane_endpoints_config = 73; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ControlPlaneEndpointsConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ControlPlaneEndpointsConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredCostManagementConfig(CostManagementConfig value)
    
    
    public ClusterUpdate.Builder setDesiredCostManagementConfig(CostManagementConfig value)

The desired configuration for the fine-grained cost management feature.

`.google.container.v1beta1.CostManagementConfig desired_cost_management_config = 49; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[CostManagementConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.CostManagementConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredCostManagementConfig(CostManagementConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredCostManagementConfig(CostManagementConfig.Builder builderForValue)

The desired configuration for the fine-grained cost management feature.

`.google.container.v1beta1.CostManagementConfig desired_cost_management_config = 49; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[CostManagementConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.CostManagementConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredDatabaseEncryption(DatabaseEncryption value)
    
    
    public ClusterUpdate.Builder setDesiredDatabaseEncryption(DatabaseEncryption value)

Configuration of etcd encryption.

`.google.container.v1beta1.DatabaseEncryption desired_database_encryption = 46;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DatabaseEncryption](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DatabaseEncryption)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredDatabaseEncryption(DatabaseEncryption.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredDatabaseEncryption(DatabaseEncryption.Builder builderForValue)

Configuration of etcd encryption.

`.google.container.v1beta1.DatabaseEncryption desired_database_encryption = 46;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[DatabaseEncryption.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DatabaseEncryption.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredDatapathProvider(DatapathProvider value)
    
    
    public ClusterUpdate.Builder setDesiredDatapathProvider(DatapathProvider value)

The desired datapath provider for the cluster.

`.google.container.v1beta1.DatapathProvider desired_datapath_provider = 50;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DatapathProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DatapathProvider)`  
The desiredDatapathProvider to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredDatapathProviderValue(int value)
    
    
    public ClusterUpdate.Builder setDesiredDatapathProviderValue(int value)

The desired datapath provider for the cluster.

`.google.container.v1beta1.DatapathProvider desired_datapath_provider = 50;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for desiredDatapathProvider to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredDefaultEnablePrivateNodes(boolean value)
    
    
    public ClusterUpdate.Builder setDesiredDefaultEnablePrivateNodes(boolean value)

Override the default setting of whether future created nodes have private IP addresses only, namely NetworkConfig.default_enable_private_nodes

`optional bool desired_default_enable_private_nodes = 72;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The desiredDefaultEnablePrivateNodes to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredDefaultSnatStatus(DefaultSnatStatus value)
    
    
    public ClusterUpdate.Builder setDesiredDefaultSnatStatus(DefaultSnatStatus value)

The desired status of whether to disable default sNAT for this cluster.

`.google.container.v1beta1.DefaultSnatStatus desired_default_snat_status = 28;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DefaultSnatStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DefaultSnatStatus)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredDefaultSnatStatus(DefaultSnatStatus.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredDefaultSnatStatus(DefaultSnatStatus.Builder builderForValue)

The desired status of whether to disable default sNAT for this cluster.

`.google.container.v1beta1.DefaultSnatStatus desired_default_snat_status = 28;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[DefaultSnatStatus.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DefaultSnatStatus.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredDisableL4LbFirewallReconciliation(boolean value)
    
    
    public ClusterUpdate.Builder setDesiredDisableL4LbFirewallReconciliation(boolean value)

Enable/Disable L4 LB VPC firewall reconciliation for the cluster.

`optional bool desired_disable_l4_lb_firewall_reconciliation = 149;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The desiredDisableL4LbFirewallReconciliation to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredDnsConfig(DNSConfig value)
    
    
    public ClusterUpdate.Builder setDesiredDnsConfig(DNSConfig value)

DNSConfig contains clusterDNS config for this cluster.

`.google.container.v1beta1.DNSConfig desired_dns_config = 53;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DNSConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DNSConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredDnsConfig(DNSConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredDnsConfig(DNSConfig.Builder builderForValue)

DNSConfig contains clusterDNS config for this cluster.

`.google.container.v1beta1.DNSConfig desired_dns_config = 53;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[DNSConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DNSConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredEnableCiliumClusterwideNetworkPolicy(boolean value)
    
    
    public ClusterUpdate.Builder setDesiredEnableCiliumClusterwideNetworkPolicy(boolean value)

Enable/Disable Cilium Clusterwide Network Policy for the cluster.

`optional bool desired_enable_cilium_clusterwide_network_policy = 138;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The desiredEnableCiliumClusterwideNetworkPolicy to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredEnableFqdnNetworkPolicy(boolean value)
    
    
    public ClusterUpdate.Builder setDesiredEnableFqdnNetworkPolicy(boolean value)

Enable/Disable FQDN Network Policy for the cluster.

`optional bool desired_enable_fqdn_network_policy = 126;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The desiredEnableFqdnNetworkPolicy to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredEnableMultiNetworking(boolean value)
    
    
    public ClusterUpdate.Builder setDesiredEnableMultiNetworking(boolean value)

Enable/Disable Multi-Networking for the cluster

`optional bool desired_enable_multi_networking = 135;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The desiredEnableMultiNetworking to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredEnablePrivateEndpoint(boolean value) (deprecated)
    
    
    public ClusterUpdate.Builder setDesiredEnablePrivateEndpoint(boolean value)

**Deprecated.** _google.container.v1beta1.ClusterUpdate.desired_enable_private_endpoint is deprecated. See google/container/v1beta1/cluster_service.proto;l=4156_

Enable/Disable private endpoint for the cluster's master.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.enable_public_endpoint instead. Note that the value of enable_public_endpoint is reversed: if enable_private_endpoint is false, then enable_public_endpoint will be true.

`optional bool desired_enable_private_endpoint = 71 [deprecated = true];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The desiredEnablePrivateEndpoint to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredEnterpriseConfig(DesiredEnterpriseConfig value) (deprecated)
    
    
    public ClusterUpdate.Builder setDesiredEnterpriseConfig(DesiredEnterpriseConfig value)

The desired enterprise configuration for the cluster.

Deprecated: GKE Enterprise features are now available without an Enterprise tier.

` .google.container.v1beta1.DesiredEnterpriseConfig desired_enterprise_config = 147 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[DesiredEnterpriseConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DesiredEnterpriseConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredEnterpriseConfig(DesiredEnterpriseConfig.Builder builderForValue) (deprecated)
    
    
    public ClusterUpdate.Builder setDesiredEnterpriseConfig(DesiredEnterpriseConfig.Builder builderForValue)

The desired enterprise configuration for the cluster.

Deprecated: GKE Enterprise features are now available without an Enterprise tier.

` .google.container.v1beta1.DesiredEnterpriseConfig desired_enterprise_config = 147 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[DesiredEnterpriseConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.DesiredEnterpriseConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredFleet(Fleet value)
    
    
    public ClusterUpdate.Builder setDesiredFleet(Fleet value)

The desired fleet configuration for the cluster.

`.google.container.v1beta1.Fleet desired_fleet = 117;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Fleet](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Fleet)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredFleet(Fleet.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredFleet(Fleet.Builder builderForValue)

The desired fleet configuration for the cluster.

`.google.container.v1beta1.Fleet desired_fleet = 117;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Fleet.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Fleet.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredGatewayApiConfig(GatewayAPIConfig value)
    
    
    public ClusterUpdate.Builder setDesiredGatewayApiConfig(GatewayAPIConfig value)

The desired config of Gateway API on this cluster.

`.google.container.v1beta1.GatewayAPIConfig desired_gateway_api_config = 114;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[GatewayAPIConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GatewayAPIConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredGatewayApiConfig(GatewayAPIConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredGatewayApiConfig(GatewayAPIConfig.Builder builderForValue)

The desired config of Gateway API on this cluster.

`.google.container.v1beta1.GatewayAPIConfig desired_gateway_api_config = 114;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[GatewayAPIConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GatewayAPIConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredGcfsConfig(GcfsConfig value)
    
    
    public ClusterUpdate.Builder setDesiredGcfsConfig(GcfsConfig value)

The desired GCFS config for the cluster.

`.google.container.v1beta1.GcfsConfig desired_gcfs_config = 109;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[GcfsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GcfsConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredGcfsConfig(GcfsConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredGcfsConfig(GcfsConfig.Builder builderForValue)

The desired GCFS config for the cluster.

`.google.container.v1beta1.GcfsConfig desired_gcfs_config = 109;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[GcfsConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GcfsConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredHostMaintenancePolicy(HostMaintenancePolicy value)
    
    
    public ClusterUpdate.Builder setDesiredHostMaintenancePolicy(HostMaintenancePolicy value)

HostMaintenancePolicy contains the desired maintenance policy for the Google Compute Engine hosts.

`.google.container.v1beta1.HostMaintenancePolicy desired_host_maintenance_policy = 132; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[HostMaintenancePolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.HostMaintenancePolicy)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredHostMaintenancePolicy(HostMaintenancePolicy.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredHostMaintenancePolicy(HostMaintenancePolicy.Builder builderForValue)

HostMaintenancePolicy contains the desired maintenance policy for the Google Compute Engine hosts.

`.google.container.v1beta1.HostMaintenancePolicy desired_host_maintenance_policy = 132; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[HostMaintenancePolicy.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.HostMaintenancePolicy.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredIdentityServiceConfig(IdentityServiceConfig value)
    
    
    public ClusterUpdate.Builder setDesiredIdentityServiceConfig(IdentityServiceConfig value)

The desired Identity Service component configuration.

`.google.container.v1beta1.IdentityServiceConfig desired_identity_service_config = 66; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[IdentityServiceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.IdentityServiceConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredIdentityServiceConfig(IdentityServiceConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredIdentityServiceConfig(IdentityServiceConfig.Builder builderForValue)

The desired Identity Service component configuration.

`.google.container.v1beta1.IdentityServiceConfig desired_identity_service_config = 66; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[IdentityServiceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.IdentityServiceConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredImage(String value)
    
    
    public ClusterUpdate.Builder setDesiredImage(String value)

The desired name of the image to use for this node. This is used to create clusters using a custom image.

`string desired_image = 44;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The desiredImage to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredImageBytes(ByteString value)
    
    
    public ClusterUpdate.Builder setDesiredImageBytes(ByteString value)

The desired name of the image to use for this node. This is used to create clusters using a custom image.

`string desired_image = 44;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for desiredImage to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredImageProject(String value)
    
    
    public ClusterUpdate.Builder setDesiredImageProject(String value)

The project containing the desired image to use for this node. This is used to create clusters using a custom image.

`string desired_image_project = 45;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The desiredImageProject to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredImageProjectBytes(ByteString value)
    
    
    public ClusterUpdate.Builder setDesiredImageProjectBytes(ByteString value)

The project containing the desired image to use for this node. This is used to create clusters using a custom image.

`string desired_image_project = 45;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for desiredImageProject to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredImageType(String value)
    
    
    public ClusterUpdate.Builder setDesiredImageType(String value)

The desired image type for the node pool. NOTE: Set the "desired_node_pool" field as well.

`string desired_image_type = 8;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The desiredImageType to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredImageTypeBytes(ByteString value)
    
    
    public ClusterUpdate.Builder setDesiredImageTypeBytes(ByteString value)

The desired image type for the node pool. NOTE: Set the "desired_node_pool" field as well.

`string desired_image_type = 8;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for desiredImageType to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredInTransitEncryptionConfig(InTransitEncryptionConfig value)
    
    
    public ClusterUpdate.Builder setDesiredInTransitEncryptionConfig(InTransitEncryptionConfig value)

Specify the details of in-transit encryption. Now named inter-node transparent encryption.

` optional .google.container.v1beta1.InTransitEncryptionConfig desired_in_transit_encryption_config = 137; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[InTransitEncryptionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.InTransitEncryptionConfig)`  
The desiredInTransitEncryptionConfig to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredInTransitEncryptionConfigValue(int value)
    
    
    public ClusterUpdate.Builder setDesiredInTransitEncryptionConfigValue(int value)

Specify the details of in-transit encryption. Now named inter-node transparent encryption.

` optional .google.container.v1beta1.InTransitEncryptionConfig desired_in_transit_encryption_config = 137; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for desiredInTransitEncryptionConfig to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredIntraNodeVisibilityConfig(IntraNodeVisibilityConfig value)
    
    
    public ClusterUpdate.Builder setDesiredIntraNodeVisibilityConfig(IntraNodeVisibilityConfig value)

The desired config of Intra-node visibility.

` .google.container.v1beta1.IntraNodeVisibilityConfig desired_intra_node_visibility_config = 26; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[IntraNodeVisibilityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.IntraNodeVisibilityConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredIntraNodeVisibilityConfig(IntraNodeVisibilityConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredIntraNodeVisibilityConfig(IntraNodeVisibilityConfig.Builder builderForValue)

The desired config of Intra-node visibility.

` .google.container.v1beta1.IntraNodeVisibilityConfig desired_intra_node_visibility_config = 26; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[IntraNodeVisibilityConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.IntraNodeVisibilityConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredK8SBetaApis(K8sBetaAPIConfig value)
    
    
    public ClusterUpdate.Builder setDesiredK8SBetaApis(K8sBetaAPIConfig value)

Beta APIs enabled for cluster.

`.google.container.v1beta1.K8sBetaAPIConfig desired_k8s_beta_apis = 131;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[K8sBetaAPIConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.K8sBetaAPIConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredK8SBetaApis(K8sBetaAPIConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredK8SBetaApis(K8sBetaAPIConfig.Builder builderForValue)

Beta APIs enabled for cluster.

`.google.container.v1beta1.K8sBetaAPIConfig desired_k8s_beta_apis = 131;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[K8sBetaAPIConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.K8sBetaAPIConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredL4IlbSubsettingConfig(ILBSubsettingConfig value)
    
    
    public ClusterUpdate.Builder setDesiredL4IlbSubsettingConfig(ILBSubsettingConfig value)

The desired L4 Internal Load Balancer Subsetting configuration.

`.google.container.v1beta1.ILBSubsettingConfig desired_l4ilb_subsetting_config = 39; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ILBSubsettingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ILBSubsettingConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredL4IlbSubsettingConfig(ILBSubsettingConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredL4IlbSubsettingConfig(ILBSubsettingConfig.Builder builderForValue)

The desired L4 Internal Load Balancer Subsetting configuration.

`.google.container.v1beta1.ILBSubsettingConfig desired_l4ilb_subsetting_config = 39; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ILBSubsettingConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ILBSubsettingConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredLocations(int index, String value)
    
    
    public ClusterUpdate.Builder setDesiredLocations(int index, String value)

The desired list of Google Compute Engine [zones](https://cloud.google.com/compute/docs/zones#available) in which the cluster's nodes should be located.

This list must always include the cluster's primary zone.

Warning: changing cluster locations will update the locations of all node pools and will result in nodes being added and/or removed.

`repeated string desired_locations = 10;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The desiredLocations to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredLoggingConfig(LoggingConfig value)
    
    
    public ClusterUpdate.Builder setDesiredLoggingConfig(LoggingConfig value)

The desired logging configuration.

`.google.container.v1beta1.LoggingConfig desired_logging_config = 64;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[LoggingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.LoggingConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredLoggingConfig(LoggingConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredLoggingConfig(LoggingConfig.Builder builderForValue)

The desired logging configuration.

`.google.container.v1beta1.LoggingConfig desired_logging_config = 64;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[LoggingConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.LoggingConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredLoggingService(String value)
    
    
    public ClusterUpdate.Builder setDesiredLoggingService(String value)

The logging service the cluster should use to write logs. Currently available options:

  * `logging.googleapis.com/kubernetes` \- The Cloud Logging service with a Kubernetes-native resource model
  * `logging.googleapis.com` \- The legacy Cloud Logging service (no longer available as of GKE 1.15).
  * `none` \- no logs will be exported from the cluster.

If left as an empty string,`logging.googleapis.com/kubernetes` will be used for GKE 1.14+ or `logging.googleapis.com` for earlier versions.




`string desired_logging_service = 19;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The desiredLoggingService to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredLoggingServiceBytes(ByteString value)
    
    
    public ClusterUpdate.Builder setDesiredLoggingServiceBytes(ByteString value)

The logging service the cluster should use to write logs. Currently available options:

  * `logging.googleapis.com/kubernetes` \- The Cloud Logging service with a Kubernetes-native resource model
  * `logging.googleapis.com` \- The legacy Cloud Logging service (no longer available as of GKE 1.15).
  * `none` \- no logs will be exported from the cluster.

If left as an empty string,`logging.googleapis.com/kubernetes` will be used for GKE 1.14+ or `logging.googleapis.com` for earlier versions.




`string desired_logging_service = 19;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for desiredLoggingService to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredManagedMachineLearningDiagnosticsConfig(ManagedMachineLearningDiagnosticsConfig value)
    
    
    public ClusterUpdate.Builder setDesiredManagedMachineLearningDiagnosticsConfig(ManagedMachineLearningDiagnosticsConfig value)

The desired managed machine learning diagnostics configuration.

` .google.container.v1beta1.ManagedMachineLearningDiagnosticsConfig desired_managed_machine_learning_diagnostics_config = 166; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ManagedMachineLearningDiagnosticsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ManagedMachineLearningDiagnosticsConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredManagedMachineLearningDiagnosticsConfig(ManagedMachineLearningDiagnosticsConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredManagedMachineLearningDiagnosticsConfig(ManagedMachineLearningDiagnosticsConfig.Builder builderForValue)

The desired managed machine learning diagnostics configuration.

` .google.container.v1beta1.ManagedMachineLearningDiagnosticsConfig desired_managed_machine_learning_diagnostics_config = 166; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ManagedMachineLearningDiagnosticsConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ManagedMachineLearningDiagnosticsConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredManagedOpentelemetryConfig(ManagedOpenTelemetryConfig value)
    
    
    public ClusterUpdate.Builder setDesiredManagedOpentelemetryConfig(ManagedOpenTelemetryConfig value)

The desired managed open telemetry configuration.

` .google.container.v1beta1.ManagedOpenTelemetryConfig desired_managed_opentelemetry_config = 163; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ManagedOpenTelemetryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ManagedOpenTelemetryConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredManagedOpentelemetryConfig(ManagedOpenTelemetryConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredManagedOpentelemetryConfig(ManagedOpenTelemetryConfig.Builder builderForValue)

The desired managed open telemetry configuration.

` .google.container.v1beta1.ManagedOpenTelemetryConfig desired_managed_opentelemetry_config = 163; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ManagedOpenTelemetryConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ManagedOpenTelemetryConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredMaster(Master value)
    
    
    public ClusterUpdate.Builder setDesiredMaster(Master value)

Configuration for master components.

`.google.container.v1beta1.Master desired_master = 52;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Master](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Master)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredMaster(Master.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredMaster(Master.Builder builderForValue)

Configuration for master components.

`.google.container.v1beta1.Master desired_master = 52;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Master.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.Master.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredMasterAuthorizedNetworksConfig(MasterAuthorizedNetworksConfig value) (deprecated)
    
    
    public ClusterUpdate.Builder setDesiredMasterAuthorizedNetworksConfig(MasterAuthorizedNetworksConfig value)

The desired configuration options for master authorized networks feature.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.authorized_networks_config instead.

` .google.container.v1beta1.MasterAuthorizedNetworksConfig desired_master_authorized_networks_config = 12 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MasterAuthorizedNetworksConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.MasterAuthorizedNetworksConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredMasterAuthorizedNetworksConfig(MasterAuthorizedNetworksConfig.Builder builderForValue) (deprecated)
    
    
    public ClusterUpdate.Builder setDesiredMasterAuthorizedNetworksConfig(MasterAuthorizedNetworksConfig.Builder builderForValue)

The desired configuration options for master authorized networks feature.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.authorized_networks_config instead.

` .google.container.v1beta1.MasterAuthorizedNetworksConfig desired_master_authorized_networks_config = 12 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[MasterAuthorizedNetworksConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.MasterAuthorizedNetworksConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredMasterVersion(String value)
    
    
    public ClusterUpdate.Builder setDesiredMasterVersion(String value)

The Kubernetes version to change the master to. The only valid value is the latest supported version.

Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior:

  * "latest": picks the highest valid Kubernetes version
  * "1.X": picks the highest valid patch+gke.N patch in the 1.X version
  * "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
  * "1.X.Y-gke.N": picks an explicit Kubernetes version
  * "-": picks the default Kubernetes version



`string desired_master_version = 100;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The desiredMasterVersion to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredMasterVersionBytes(ByteString value)
    
    
    public ClusterUpdate.Builder setDesiredMasterVersionBytes(ByteString value)

The Kubernetes version to change the master to. The only valid value is the latest supported version.

Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior:

  * "latest": picks the highest valid Kubernetes version
  * "1.X": picks the highest valid patch+gke.N patch in the 1.X version
  * "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
  * "1.X.Y-gke.N": picks an explicit Kubernetes version
  * "-": picks the default Kubernetes version



`string desired_master_version = 100;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for desiredMasterVersion to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredMeshCertificates(MeshCertificates value)
    
    
    public ClusterUpdate.Builder setDesiredMeshCertificates(MeshCertificates value)

Configuration for issuance of mTLS keys and certificates to Kubernetes pods.

`.google.container.v1beta1.MeshCertificates desired_mesh_certificates = 67;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MeshCertificates](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.MeshCertificates)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredMeshCertificates(MeshCertificates.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredMeshCertificates(MeshCertificates.Builder builderForValue)

Configuration for issuance of mTLS keys and certificates to Kubernetes pods.

`.google.container.v1beta1.MeshCertificates desired_mesh_certificates = 67;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[MeshCertificates.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.MeshCertificates.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredMonitoringConfig(MonitoringConfig value)
    
    
    public ClusterUpdate.Builder setDesiredMonitoringConfig(MonitoringConfig value)

The desired monitoring configuration.

`.google.container.v1beta1.MonitoringConfig desired_monitoring_config = 65;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[MonitoringConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.MonitoringConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredMonitoringConfig(MonitoringConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredMonitoringConfig(MonitoringConfig.Builder builderForValue)

The desired monitoring configuration.

`.google.container.v1beta1.MonitoringConfig desired_monitoring_config = 65;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[MonitoringConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.MonitoringConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredMonitoringService(String value)
    
    
    public ClusterUpdate.Builder setDesiredMonitoringService(String value)

The monitoring service the cluster should use to write metrics. Currently available options:

  * `monitoring.googleapis.com/kubernetes` \- The Cloud Monitoring service with a Kubernetes-native resource model
  * `monitoring.googleapis.com` \- The legacy Cloud Monitoring service (no longer available as of GKE 1.15).
  * `none` \- No metrics will be exported from the cluster.

If left as an empty string,`monitoring.googleapis.com/kubernetes` will be used for GKE 1.14+ or `monitoring.googleapis.com` for earlier versions.




`string desired_monitoring_service = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The desiredMonitoringService to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredMonitoringServiceBytes(ByteString value)
    
    
    public ClusterUpdate.Builder setDesiredMonitoringServiceBytes(ByteString value)

The monitoring service the cluster should use to write metrics. Currently available options:

  * `monitoring.googleapis.com/kubernetes` \- The Cloud Monitoring service with a Kubernetes-native resource model
  * `monitoring.googleapis.com` \- The legacy Cloud Monitoring service (no longer available as of GKE 1.15).
  * `none` \- No metrics will be exported from the cluster.

If left as an empty string,`monitoring.googleapis.com/kubernetes` will be used for GKE 1.14+ or `monitoring.googleapis.com` for earlier versions.




`string desired_monitoring_service = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for desiredMonitoringService to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredNetworkPerformanceConfig(NetworkConfig.ClusterNetworkPerformanceConfig value)
    
    
    public ClusterUpdate.Builder setDesiredNetworkPerformanceConfig(NetworkConfig.ClusterNetworkPerformanceConfig value)

The desired network performance config.

` .google.container.v1beta1.NetworkConfig.ClusterNetworkPerformanceConfig desired_network_performance_config = 125; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NetworkConfig.ClusterNetworkPerformanceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NetworkConfig.ClusterNetworkPerformanceConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredNetworkPerformanceConfig(NetworkConfig.ClusterNetworkPerformanceConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredNetworkPerformanceConfig(NetworkConfig.ClusterNetworkPerformanceConfig.Builder builderForValue)

The desired network performance config.

` .google.container.v1beta1.NetworkConfig.ClusterNetworkPerformanceConfig desired_network_performance_config = 125; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[NetworkConfig.ClusterNetworkPerformanceConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NetworkConfig.ClusterNetworkPerformanceConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredNetworkTierConfig(NetworkTierConfig value)
    
    
    public ClusterUpdate.Builder setDesiredNetworkTierConfig(NetworkTierConfig value)

The desired network tier configuration for the cluster.

`.google.container.v1beta1.NetworkTierConfig desired_network_tier_config = 155;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NetworkTierConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NetworkTierConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredNetworkTierConfig(NetworkTierConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredNetworkTierConfig(NetworkTierConfig.Builder builderForValue)

The desired network tier configuration for the cluster.

`.google.container.v1beta1.NetworkTierConfig desired_network_tier_config = 155;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[NetworkTierConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NetworkTierConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredNodeCreationConfig(NodeCreationConfig value)
    
    
    public ClusterUpdate.Builder setDesiredNodeCreationConfig(NodeCreationConfig value)

Optional. The desired NodeCreationConfig for the cluster.

` .google.container.v1beta1.NodeCreationConfig desired_node_creation_config = 171 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NodeCreationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeCreationConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredNodeCreationConfig(NodeCreationConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredNodeCreationConfig(NodeCreationConfig.Builder builderForValue)

Optional. The desired NodeCreationConfig for the cluster.

` .google.container.v1beta1.NodeCreationConfig desired_node_creation_config = 171 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[NodeCreationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeCreationConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredNodeKubeletConfig(NodeKubeletConfig value)
    
    
    public ClusterUpdate.Builder setDesiredNodeKubeletConfig(NodeKubeletConfig value)

The desired node kubelet config for the cluster.

`.google.container.v1beta1.NodeKubeletConfig desired_node_kubelet_config = 141;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NodeKubeletConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeKubeletConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredNodeKubeletConfig(NodeKubeletConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredNodeKubeletConfig(NodeKubeletConfig.Builder builderForValue)

The desired node kubelet config for the cluster.

`.google.container.v1beta1.NodeKubeletConfig desired_node_kubelet_config = 141;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[NodeKubeletConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeKubeletConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredNodePoolAutoConfigKubeletConfig(NodeKubeletConfig value)
    
    
    public ClusterUpdate.Builder setDesiredNodePoolAutoConfigKubeletConfig(NodeKubeletConfig value)

The desired node kubelet config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

` .google.container.v1beta1.NodeKubeletConfig desired_node_pool_auto_config_kubelet_config = 142; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NodeKubeletConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeKubeletConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredNodePoolAutoConfigKubeletConfig(NodeKubeletConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredNodePoolAutoConfigKubeletConfig(NodeKubeletConfig.Builder builderForValue)

The desired node kubelet config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

` .google.container.v1beta1.NodeKubeletConfig desired_node_pool_auto_config_kubelet_config = 142; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[NodeKubeletConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodeKubeletConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredNodePoolAutoConfigLinuxNodeConfig(LinuxNodeConfig value)
    
    
    public ClusterUpdate.Builder setDesiredNodePoolAutoConfigLinuxNodeConfig(LinuxNodeConfig value)

The desired Linux node config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

Currently only `cgroup_mode` can be set here.

` .google.container.v1beta1.LinuxNodeConfig desired_node_pool_auto_config_linux_node_config = 150; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[LinuxNodeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.LinuxNodeConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredNodePoolAutoConfigLinuxNodeConfig(LinuxNodeConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredNodePoolAutoConfigLinuxNodeConfig(LinuxNodeConfig.Builder builderForValue)

The desired Linux node config for all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

Currently only `cgroup_mode` can be set here.

` .google.container.v1beta1.LinuxNodeConfig desired_node_pool_auto_config_linux_node_config = 150; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[LinuxNodeConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.LinuxNodeConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredNodePoolAutoConfigNetworkTags(NetworkTags value)
    
    
    public ClusterUpdate.Builder setDesiredNodePoolAutoConfigNetworkTags(NetworkTags value)

The desired network tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

`.google.container.v1beta1.NetworkTags desired_node_pool_auto_config_network_tags = 110; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NetworkTags](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NetworkTags)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredNodePoolAutoConfigNetworkTags(NetworkTags.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredNodePoolAutoConfigNetworkTags(NetworkTags.Builder builderForValue)

The desired network tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

`.google.container.v1beta1.NetworkTags desired_node_pool_auto_config_network_tags = 110; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[NetworkTags.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NetworkTags.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredNodePoolAutoConfigResourceManagerTags(ResourceManagerTags value)
    
    
    public ClusterUpdate.Builder setDesiredNodePoolAutoConfigResourceManagerTags(ResourceManagerTags value)

The desired resource manager tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

` .google.container.v1beta1.ResourceManagerTags desired_node_pool_auto_config_resource_manager_tags = 136; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ResourceManagerTags](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ResourceManagerTags)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredNodePoolAutoConfigResourceManagerTags(ResourceManagerTags.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredNodePoolAutoConfigResourceManagerTags(ResourceManagerTags.Builder builderForValue)

The desired resource manager tags that apply to all auto-provisioned node pools in autopilot clusters and node auto-provisioning enabled clusters.

` .google.container.v1beta1.ResourceManagerTags desired_node_pool_auto_config_resource_manager_tags = 136; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ResourceManagerTags.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ResourceManagerTags.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredNodePoolAutoscaling(NodePoolAutoscaling value)
    
    
    public ClusterUpdate.Builder setDesiredNodePoolAutoscaling(NodePoolAutoscaling value)

Autoscaler configuration for the node pool specified in desired_node_pool_id. If there is only one pool in the cluster and desired_node_pool_id is not provided then the change applies to that single node pool.

`.google.container.v1beta1.NodePoolAutoscaling desired_node_pool_autoscaling = 9;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NodePoolAutoscaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolAutoscaling)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredNodePoolAutoscaling(NodePoolAutoscaling.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredNodePoolAutoscaling(NodePoolAutoscaling.Builder builderForValue)

Autoscaler configuration for the node pool specified in desired_node_pool_id. If there is only one pool in the cluster and desired_node_pool_id is not provided then the change applies to that single node pool.

`.google.container.v1beta1.NodePoolAutoscaling desired_node_pool_autoscaling = 9;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[NodePoolAutoscaling.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolAutoscaling.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredNodePoolId(String value)
    
    
    public ClusterUpdate.Builder setDesiredNodePoolId(String value)

The node pool to be upgraded. This field is mandatory if "desired_node_version", "desired_image_family", "desired_node_pool_autoscaling", or "desired_workload_metadata_config" is specified and there is more than one node pool on the cluster.

`string desired_node_pool_id = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The desiredNodePoolId to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredNodePoolIdBytes(ByteString value)
    
    
    public ClusterUpdate.Builder setDesiredNodePoolIdBytes(ByteString value)

The node pool to be upgraded. This field is mandatory if "desired_node_version", "desired_image_family", "desired_node_pool_autoscaling", or "desired_workload_metadata_config" is specified and there is more than one node pool on the cluster.

`string desired_node_pool_id = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for desiredNodePoolId to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredNodePoolLoggingConfig(NodePoolLoggingConfig value)
    
    
    public ClusterUpdate.Builder setDesiredNodePoolLoggingConfig(NodePoolLoggingConfig value)

The desired node pool logging configuration defaults for the cluster.

`.google.container.v1beta1.NodePoolLoggingConfig desired_node_pool_logging_config = 116; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NodePoolLoggingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolLoggingConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredNodePoolLoggingConfig(NodePoolLoggingConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredNodePoolLoggingConfig(NodePoolLoggingConfig.Builder builderForValue)

The desired node pool logging configuration defaults for the cluster.

`.google.container.v1beta1.NodePoolLoggingConfig desired_node_pool_logging_config = 116; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[NodePoolLoggingConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolLoggingConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredNodePoolUpgradeConcurrencyConfig(NodePoolUpgradeConcurrencyConfig value)
    
    
    public ClusterUpdate.Builder setDesiredNodePoolUpgradeConcurrencyConfig(NodePoolUpgradeConcurrencyConfig value)

The desired node pool upgrade concurrency configuration.

` .google.container.v1beta1.NodePoolUpgradeConcurrencyConfig desired_node_pool_upgrade_concurrency_config = 167; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NodePoolUpgradeConcurrencyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolUpgradeConcurrencyConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredNodePoolUpgradeConcurrencyConfig(NodePoolUpgradeConcurrencyConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredNodePoolUpgradeConcurrencyConfig(NodePoolUpgradeConcurrencyConfig.Builder builderForValue)

The desired node pool upgrade concurrency configuration.

` .google.container.v1beta1.NodePoolUpgradeConcurrencyConfig desired_node_pool_upgrade_concurrency_config = 167; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[NodePoolUpgradeConcurrencyConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NodePoolUpgradeConcurrencyConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredNodeVersion(String value)
    
    
    public ClusterUpdate.Builder setDesiredNodeVersion(String value)

The Kubernetes version to change the nodes to (typically an upgrade).

Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior:

  * "latest": picks the highest valid Kubernetes version
  * "1.X": picks the highest valid patch+gke.N patch in the 1.X version
  * "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
  * "1.X.Y-gke.N": picks an explicit Kubernetes version
  * "-": picks the Kubernetes master version



`string desired_node_version = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The desiredNodeVersion to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredNodeVersionBytes(ByteString value)
    
    
    public ClusterUpdate.Builder setDesiredNodeVersionBytes(ByteString value)

The Kubernetes version to change the nodes to (typically an upgrade).

Users may specify either explicit versions offered by Kubernetes Engine or version aliases, which have the following behavior:

  * "latest": picks the highest valid Kubernetes version
  * "1.X": picks the highest valid patch+gke.N patch in the 1.X version
  * "1.X.Y": picks the highest valid gke.N patch in the 1.X.Y version
  * "1.X.Y-gke.N": picks an explicit Kubernetes version
  * "-": picks the Kubernetes master version



`string desired_node_version = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for desiredNodeVersion to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredNotificationConfig(NotificationConfig value)
    
    
    public ClusterUpdate.Builder setDesiredNotificationConfig(NotificationConfig value)

The desired notification configuration.

`.google.container.v1beta1.NotificationConfig desired_notification_config = 55;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NotificationConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredNotificationConfig(NotificationConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredNotificationConfig(NotificationConfig.Builder builderForValue)

The desired notification configuration.

`.google.container.v1beta1.NotificationConfig desired_notification_config = 55;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[NotificationConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.NotificationConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredPodAutoscaling(PodAutoscaling value)
    
    
    public ClusterUpdate.Builder setDesiredPodAutoscaling(PodAutoscaling value)

The desired config for pod autoscaling.

`.google.container.v1beta1.PodAutoscaling desired_pod_autoscaling = 113;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PodAutoscaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PodAutoscaling)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredPodAutoscaling(PodAutoscaling.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredPodAutoscaling(PodAutoscaling.Builder builderForValue)

The desired config for pod autoscaling.

`.google.container.v1beta1.PodAutoscaling desired_pod_autoscaling = 113;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[PodAutoscaling.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PodAutoscaling.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredPodSecurityPolicyConfig(PodSecurityPolicyConfig value)
    
    
    public ClusterUpdate.Builder setDesiredPodSecurityPolicyConfig(PodSecurityPolicyConfig value)

The desired configuration options for the PodSecurityPolicy feature.

` .google.container.v1beta1.PodSecurityPolicyConfig desired_pod_security_policy_config = 14; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PodSecurityPolicyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PodSecurityPolicyConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredPodSecurityPolicyConfig(PodSecurityPolicyConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredPodSecurityPolicyConfig(PodSecurityPolicyConfig.Builder builderForValue)

The desired configuration options for the PodSecurityPolicy feature.

` .google.container.v1beta1.PodSecurityPolicyConfig desired_pod_security_policy_config = 14; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[PodSecurityPolicyConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PodSecurityPolicyConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredPrivateClusterConfig(PrivateClusterConfig value) (deprecated)
    
    
    public ClusterUpdate.Builder setDesiredPrivateClusterConfig(PrivateClusterConfig value)

The desired private cluster configuration. master_global_access_config is the only field that can be changed via this field. See also ClusterUpdate.desired_enable_private_endpoint for modifying other fields within PrivateClusterConfig.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.global_access instead.

` .google.container.v1beta1.PrivateClusterConfig desired_private_cluster_config = 25 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PrivateClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PrivateClusterConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredPrivateClusterConfig(PrivateClusterConfig.Builder builderForValue) (deprecated)
    
    
    public ClusterUpdate.Builder setDesiredPrivateClusterConfig(PrivateClusterConfig.Builder builderForValue)

The desired private cluster configuration. master_global_access_config is the only field that can be changed via this field. See also ClusterUpdate.desired_enable_private_endpoint for modifying other fields within PrivateClusterConfig.

Deprecated: Use desired_control_plane_endpoints_config.ip_endpoints_config.global_access instead.

` .google.container.v1beta1.PrivateClusterConfig desired_private_cluster_config = 25 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[PrivateClusterConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PrivateClusterConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredPrivateIpv6GoogleAccess(PrivateIPv6GoogleAccess value)
    
    
    public ClusterUpdate.Builder setDesiredPrivateIpv6GoogleAccess(PrivateIPv6GoogleAccess value)

The desired state of IPv6 connectivity to Google Services.

` .google.container.v1beta1.PrivateIPv6GoogleAccess desired_private_ipv6_google_access = 51; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PrivateIPv6GoogleAccess](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PrivateIPv6GoogleAccess)`  
The desiredPrivateIpv6GoogleAccess to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredPrivateIpv6GoogleAccessValue(int value)
    
    
    public ClusterUpdate.Builder setDesiredPrivateIpv6GoogleAccessValue(int value)

The desired state of IPv6 connectivity to Google Services.

` .google.container.v1beta1.PrivateIPv6GoogleAccess desired_private_ipv6_google_access = 51; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for desiredPrivateIpv6GoogleAccess to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredPrivilegedAdmissionConfig(PrivilegedAdmissionConfig value)
    
    
    public ClusterUpdate.Builder setDesiredPrivilegedAdmissionConfig(PrivilegedAdmissionConfig value)

The desired privileged admission config for the cluster.

` .google.container.v1beta1.PrivilegedAdmissionConfig desired_privileged_admission_config = 159; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PrivilegedAdmissionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PrivilegedAdmissionConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredPrivilegedAdmissionConfig(PrivilegedAdmissionConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredPrivilegedAdmissionConfig(PrivilegedAdmissionConfig.Builder builderForValue)

The desired privileged admission config for the cluster.

` .google.container.v1beta1.PrivilegedAdmissionConfig desired_privileged_admission_config = 159; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[PrivilegedAdmissionConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PrivilegedAdmissionConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredProtectConfig(ProtectConfig value) (deprecated)
    
    
    public ClusterUpdate.Builder setDesiredProtectConfig(ProtectConfig value)

Deprecated: Use DesiredSecurityPostureConfig instead. Enable/Disable Protect API features for the cluster.

` optional .google.container.v1beta1.ProtectConfig desired_protect_config = 112 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ProtectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ProtectConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredProtectConfig(ProtectConfig.Builder builderForValue) (deprecated)
    
    
    public ClusterUpdate.Builder setDesiredProtectConfig(ProtectConfig.Builder builderForValue)

Deprecated: Use DesiredSecurityPostureConfig instead. Enable/Disable Protect API features for the cluster.

` optional .google.container.v1beta1.ProtectConfig desired_protect_config = 112 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ProtectConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ProtectConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredRbacBindingConfig(RBACBindingConfig value)
    
    
    public ClusterUpdate.Builder setDesiredRbacBindingConfig(RBACBindingConfig value)

RBACBindingConfig allows user to restrict ClusterRoleBindings an RoleBindings that can be created.

`optional .google.container.v1beta1.RBACBindingConfig desired_rbac_binding_config = 144; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[RBACBindingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.RBACBindingConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredRbacBindingConfig(RBACBindingConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredRbacBindingConfig(RBACBindingConfig.Builder builderForValue)

RBACBindingConfig allows user to restrict ClusterRoleBindings an RoleBindings that can be created.

`optional .google.container.v1beta1.RBACBindingConfig desired_rbac_binding_config = 144; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[RBACBindingConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.RBACBindingConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredReleaseChannel(ReleaseChannel value)
    
    
    public ClusterUpdate.Builder setDesiredReleaseChannel(ReleaseChannel value)

The desired release channel configuration.

`.google.container.v1beta1.ReleaseChannel desired_release_channel = 31;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ReleaseChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ReleaseChannel)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredReleaseChannel(ReleaseChannel.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredReleaseChannel(ReleaseChannel.Builder builderForValue)

The desired release channel configuration.

`.google.container.v1beta1.ReleaseChannel desired_release_channel = 31;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ReleaseChannel.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ReleaseChannel.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredResourceUsageExportConfig(ResourceUsageExportConfig value)
    
    
    public ClusterUpdate.Builder setDesiredResourceUsageExportConfig(ResourceUsageExportConfig value)

The desired configuration for exporting resource usage.

` .google.container.v1beta1.ResourceUsageExportConfig desired_resource_usage_export_config = 21; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ResourceUsageExportConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ResourceUsageExportConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredResourceUsageExportConfig(ResourceUsageExportConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredResourceUsageExportConfig(ResourceUsageExportConfig.Builder builderForValue)

The desired configuration for exporting resource usage.

` .google.container.v1beta1.ResourceUsageExportConfig desired_resource_usage_export_config = 21; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ResourceUsageExportConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ResourceUsageExportConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredRollbackSafeUpgrade(RollbackSafeUpgrade value)
    
    
    public ClusterUpdate.Builder setDesiredRollbackSafeUpgrade(RollbackSafeUpgrade value)

The desired rollback safe upgrade configuration.

`.google.container.v1beta1.RollbackSafeUpgrade desired_rollback_safe_upgrade = 161; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[RollbackSafeUpgrade](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.RollbackSafeUpgrade)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredRollbackSafeUpgrade(RollbackSafeUpgrade.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredRollbackSafeUpgrade(RollbackSafeUpgrade.Builder builderForValue)

The desired rollback safe upgrade configuration.

`.google.container.v1beta1.RollbackSafeUpgrade desired_rollback_safe_upgrade = 161; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[RollbackSafeUpgrade.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.RollbackSafeUpgrade.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredScheduleUpgradeConfig(ScheduleUpgradeConfig value)
    
    
    public ClusterUpdate.Builder setDesiredScheduleUpgradeConfig(ScheduleUpgradeConfig value)

Optional. The desired scheduled upgrades configuration for the cluster.

` .google.container.v1beta1.ScheduleUpgradeConfig desired_schedule_upgrade_config = 157 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ScheduleUpgradeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ScheduleUpgradeConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredScheduleUpgradeConfig(ScheduleUpgradeConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredScheduleUpgradeConfig(ScheduleUpgradeConfig.Builder builderForValue)

Optional. The desired scheduled upgrades configuration for the cluster.

` .google.container.v1beta1.ScheduleUpgradeConfig desired_schedule_upgrade_config = 157 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ScheduleUpgradeConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ScheduleUpgradeConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredSecretManagerConfig(SecretManagerConfig value)
    
    
    public ClusterUpdate.Builder setDesiredSecretManagerConfig(SecretManagerConfig value)

Enable/Disable Secret Manager Config.

` optional .google.container.v1beta1.SecretManagerConfig desired_secret_manager_config = 139; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SecretManagerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SecretManagerConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredSecretManagerConfig(SecretManagerConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredSecretManagerConfig(SecretManagerConfig.Builder builderForValue)

Enable/Disable Secret Manager Config.

` optional .google.container.v1beta1.SecretManagerConfig desired_secret_manager_config = 139; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SecretManagerConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SecretManagerConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredSecretSyncConfig(SecretSyncConfig value)
    
    
    public ClusterUpdate.Builder setDesiredSecretSyncConfig(SecretSyncConfig value)

Configuration for sync Secret Manager secrets as k8s secrets.

`.google.container.v1beta1.SecretSyncConfig desired_secret_sync_config = 158;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SecretSyncConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SecretSyncConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredSecretSyncConfig(SecretSyncConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredSecretSyncConfig(SecretSyncConfig.Builder builderForValue)

Configuration for sync Secret Manager secrets as k8s secrets.

`.google.container.v1beta1.SecretSyncConfig desired_secret_sync_config = 158;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SecretSyncConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SecretSyncConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredSecurityPostureConfig(SecurityPostureConfig value)
    
    
    public ClusterUpdate.Builder setDesiredSecurityPostureConfig(SecurityPostureConfig value)

Enable/Disable Security Posture API features for the cluster.

`.google.container.v1beta1.SecurityPostureConfig desired_security_posture_config = 124; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SecurityPostureConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SecurityPostureConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredSecurityPostureConfig(SecurityPostureConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredSecurityPostureConfig(SecurityPostureConfig.Builder builderForValue)

Enable/Disable Security Posture API features for the cluster.

`.google.container.v1beta1.SecurityPostureConfig desired_security_posture_config = 124; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SecurityPostureConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.SecurityPostureConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredServiceExternalIpsConfig(ServiceExternalIPsConfig value)
    
    
    public ClusterUpdate.Builder setDesiredServiceExternalIpsConfig(ServiceExternalIPsConfig value)

ServiceExternalIPsConfig specifies the config for the use of Services with ExternalIPs field.

` .google.container.v1beta1.ServiceExternalIPsConfig desired_service_external_ips_config = 60; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ServiceExternalIPsConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ServiceExternalIPsConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredServiceExternalIpsConfig(ServiceExternalIPsConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredServiceExternalIpsConfig(ServiceExternalIPsConfig.Builder builderForValue)

ServiceExternalIPsConfig specifies the config for the use of Services with ExternalIPs field.

` .google.container.v1beta1.ServiceExternalIPsConfig desired_service_external_ips_config = 60; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ServiceExternalIPsConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ServiceExternalIPsConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredShieldedNodes(ShieldedNodes value)
    
    
    public ClusterUpdate.Builder setDesiredShieldedNodes(ShieldedNodes value)

Configuration for Shielded Nodes.

`.google.container.v1beta1.ShieldedNodes desired_shielded_nodes = 48;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ShieldedNodes](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ShieldedNodes)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredShieldedNodes(ShieldedNodes.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredShieldedNodes(ShieldedNodes.Builder builderForValue)

Configuration for Shielded Nodes.

`.google.container.v1beta1.ShieldedNodes desired_shielded_nodes = 48;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ShieldedNodes.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ShieldedNodes.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredStackType(StackType value)
    
    
    public ClusterUpdate.Builder setDesiredStackType(StackType value)

The desired stack type of the cluster. If a stack type is provided and does not match the current stack type of the cluster, update will attempt to change the stack type to the new type.

`.google.container.v1beta1.StackType desired_stack_type = 119;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[StackType](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.StackType)`  
The desiredStackType to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredStackTypeValue(int value)
    
    
    public ClusterUpdate.Builder setDesiredStackTypeValue(int value)

The desired stack type of the cluster. If a stack type is provided and does not match the current stack type of the cluster, update will attempt to change the stack type to the new type.

`.google.container.v1beta1.StackType desired_stack_type = 119;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for desiredStackType to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setDesiredTpuConfig(TpuConfig value) (deprecated)
    
    
    public ClusterUpdate.Builder setDesiredTpuConfig(TpuConfig value)

The desired Cloud TPU configuration. This field is deprecated due to the deprecation of 2VM TPU. The end of life date for 2VM TPU is 2025-04-25.

`.google.container.v1beta1.TpuConfig desired_tpu_config = 38 [deprecated = true];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[TpuConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.TpuConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredTpuConfig(TpuConfig.Builder builderForValue) (deprecated)
    
    
    public ClusterUpdate.Builder setDesiredTpuConfig(TpuConfig.Builder builderForValue)

The desired Cloud TPU configuration. This field is deprecated due to the deprecation of 2VM TPU. The end of life date for 2VM TPU is 2025-04-25.

`.google.container.v1beta1.TpuConfig desired_tpu_config = 38 [deprecated = true];`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[TpuConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.TpuConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredUserManagedKeysConfig(UserManagedKeysConfig value)
    
    
    public ClusterUpdate.Builder setDesiredUserManagedKeysConfig(UserManagedKeysConfig value)

The desired user managed keys config for the cluster.

`.google.container.v1beta1.UserManagedKeysConfig desired_user_managed_keys_config = 152; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[UserManagedKeysConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.UserManagedKeysConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredUserManagedKeysConfig(UserManagedKeysConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredUserManagedKeysConfig(UserManagedKeysConfig.Builder builderForValue)

The desired user managed keys config for the cluster.

`.google.container.v1beta1.UserManagedKeysConfig desired_user_managed_keys_config = 152; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[UserManagedKeysConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.UserManagedKeysConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredVerticalPodAutoscaling(VerticalPodAutoscaling value)
    
    
    public ClusterUpdate.Builder setDesiredVerticalPodAutoscaling(VerticalPodAutoscaling value)

Cluster-level Vertical Pod Autoscaling configuration.

`.google.container.v1beta1.VerticalPodAutoscaling desired_vertical_pod_autoscaling = 22; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[VerticalPodAutoscaling](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.VerticalPodAutoscaling)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredVerticalPodAutoscaling(VerticalPodAutoscaling.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredVerticalPodAutoscaling(VerticalPodAutoscaling.Builder builderForValue)

Cluster-level Vertical Pod Autoscaling configuration.

`.google.container.v1beta1.VerticalPodAutoscaling desired_vertical_pod_autoscaling = 22; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[VerticalPodAutoscaling.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.VerticalPodAutoscaling.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredWorkloadAltsConfig(WorkloadALTSConfig value)
    
    
    public ClusterUpdate.Builder setDesiredWorkloadAltsConfig(WorkloadALTSConfig value)

Configuration for direct-path (via ALTS) with workload identity. This feature is not officially supported for external customers in Kubernetes Engine when using Workload Identity.

`.google.container.v1beta1.WorkloadALTSConfig desired_workload_alts_config = 62;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WorkloadALTSConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadALTSConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredWorkloadAltsConfig(WorkloadALTSConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredWorkloadAltsConfig(WorkloadALTSConfig.Builder builderForValue)

Configuration for direct-path (via ALTS) with workload identity. This feature is not officially supported for external customers in Kubernetes Engine when using Workload Identity.

`.google.container.v1beta1.WorkloadALTSConfig desired_workload_alts_config = 62;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[WorkloadALTSConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadALTSConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredWorkloadCertificates(WorkloadCertificates value)
    
    
    public ClusterUpdate.Builder setDesiredWorkloadCertificates(WorkloadCertificates value)

Configuration for issuance of mTLS keys and certificates to Kubernetes pods.

`.google.container.v1beta1.WorkloadCertificates desired_workload_certificates = 61; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WorkloadCertificates](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadCertificates)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredWorkloadCertificates(WorkloadCertificates.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredWorkloadCertificates(WorkloadCertificates.Builder builderForValue)

Configuration for issuance of mTLS keys and certificates to Kubernetes pods.

`.google.container.v1beta1.WorkloadCertificates desired_workload_certificates = 61; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[WorkloadCertificates.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadCertificates.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredWorkloadIdentityConfig(WorkloadIdentityConfig value)
    
    
    public ClusterUpdate.Builder setDesiredWorkloadIdentityConfig(WorkloadIdentityConfig value)

Configuration for Workload Identity.

`.google.container.v1beta1.WorkloadIdentityConfig desired_workload_identity_config = 47; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[WorkloadIdentityConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadIdentityConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setDesiredWorkloadIdentityConfig(WorkloadIdentityConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setDesiredWorkloadIdentityConfig(WorkloadIdentityConfig.Builder builderForValue)

Configuration for Workload Identity.

`.google.container.v1beta1.WorkloadIdentityConfig desired_workload_identity_config = 47; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[WorkloadIdentityConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.WorkloadIdentityConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setEnableK8SBetaApis(K8sBetaAPIConfig value)
    
    
    public ClusterUpdate.Builder setEnableK8SBetaApis(K8sBetaAPIConfig value)

Kubernetes open source beta apis enabled on the cluster. Only beta apis

`.google.container.v1beta1.K8sBetaAPIConfig enable_k8s_beta_apis = 122;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[K8sBetaAPIConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.K8sBetaAPIConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setEnableK8SBetaApis(K8sBetaAPIConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setEnableK8SBetaApis(K8sBetaAPIConfig.Builder builderForValue)

Kubernetes open source beta apis enabled on the cluster. Only beta apis

`.google.container.v1beta1.K8sBetaAPIConfig enable_k8s_beta_apis = 122;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[K8sBetaAPIConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.K8sBetaAPIConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setEtag(String value)
    
    
    public ClusterUpdate.Builder setEtag(String value)

The current etag of the cluster. If an etag is provided and does not match the current etag of the cluster, update will be blocked and an ABORTED error will be returned.

`string etag = 115;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The etag to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setEtagBytes(ByteString value)
    
    
    public ClusterUpdate.Builder setEtagBytes(ByteString value)

The current etag of the cluster. If an etag is provided and does not match the current etag of the cluster, update will be blocked and an ABORTED error will be returned.

`string etag = 115;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for etag to set.  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` | This builder for chaining.  
  
### setGkeAutoUpgradeConfig(GkeAutoUpgradeConfig value)
    
    
    public ClusterUpdate.Builder setGkeAutoUpgradeConfig(GkeAutoUpgradeConfig value)

Configuration for GKE auto upgrade.

`.google.container.v1beta1.GkeAutoUpgradeConfig gke_auto_upgrade_config = 154;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[GkeAutoUpgradeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GkeAutoUpgradeConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setGkeAutoUpgradeConfig(GkeAutoUpgradeConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setGkeAutoUpgradeConfig(GkeAutoUpgradeConfig.Builder builderForValue)

Configuration for GKE auto upgrade.

`.google.container.v1beta1.GkeAutoUpgradeConfig gke_auto_upgrade_config = 154;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[GkeAutoUpgradeConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.GkeAutoUpgradeConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setPrivateClusterConfig(PrivateClusterConfig value) (deprecated)
    
    
    public ClusterUpdate.Builder setPrivateClusterConfig(PrivateClusterConfig value)

The desired private cluster configuration. Has no effect. Use desired_private_cluster_config instead.

` .google.container.v1beta1.PrivateClusterConfig private_cluster_config = 37 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[PrivateClusterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PrivateClusterConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setPrivateClusterConfig(PrivateClusterConfig.Builder builderForValue) (deprecated)
    
    
    public ClusterUpdate.Builder setPrivateClusterConfig(PrivateClusterConfig.Builder builderForValue)

The desired private cluster configuration. Has no effect. Use desired_private_cluster_config instead.

` .google.container.v1beta1.PrivateClusterConfig private_cluster_config = 37 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[PrivateClusterConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.PrivateClusterConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setRemovedAdditionalPodRangesConfig(AdditionalPodRangesConfig value)
    
    
    public ClusterUpdate.Builder setRemovedAdditionalPodRangesConfig(AdditionalPodRangesConfig value)

The additional pod ranges that are to be removed from the cluster. The pod ranges specified here must have been specified earlier in the 'additional_pod_ranges_config' argument.

` .google.container.v1beta1.AdditionalPodRangesConfig removed_additional_pod_ranges_config = 121; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AdditionalPodRangesConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AdditionalPodRangesConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setRemovedAdditionalPodRangesConfig(AdditionalPodRangesConfig.Builder builderForValue)
    
    
    public ClusterUpdate.Builder setRemovedAdditionalPodRangesConfig(AdditionalPodRangesConfig.Builder builderForValue)

The additional pod ranges that are to be removed from the cluster. The pod ranges specified here must have been specified earlier in the 'additional_pod_ranges_config' argument.

` .google.container.v1beta1.AdditionalPodRangesConfig removed_additional_pod_ranges_config = 121; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[AdditionalPodRangesConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.AdditionalPodRangesConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setUserManagedKeysConfig(UserManagedKeysConfig value) (deprecated)
    
    
    public ClusterUpdate.Builder setUserManagedKeysConfig(UserManagedKeysConfig value)

The Custom keys configuration for the cluster.

This field is deprecated. Use ClusterUpdate.desired_user_managed_keys_config instead.

` .google.container.v1beta1.UserManagedKeysConfig user_managed_keys_config = 143 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[UserManagedKeysConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.UserManagedKeysConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
### setUserManagedKeysConfig(UserManagedKeysConfig.Builder builderForValue) (deprecated)
    
    
    public ClusterUpdate.Builder setUserManagedKeysConfig(UserManagedKeysConfig.Builder builderForValue)

The Custom keys configuration for the cluster.

This field is deprecated. Use ClusterUpdate.desired_user_managed_keys_config instead.

` .google.container.v1beta1.UserManagedKeysConfig user_managed_keys_config = 143 [deprecated = true]; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[UserManagedKeysConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.UserManagedKeysConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterUpdate.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1beta1.ClusterUpdate.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
