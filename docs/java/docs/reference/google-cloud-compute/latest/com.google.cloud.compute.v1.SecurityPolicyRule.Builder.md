---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder
title: Class SecurityPolicyRule.Builder (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:03:01.541795+00:00
---

# Class SecurityPolicyRule.Builder (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SecurityPolicyRule.Builder (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public static final class SecurityPolicyRule.Builder extends GeneratedMessage.Builder<SecurityPolicyRule.Builder> implements SecurityPolicyRuleOrBuilder

Represents a rule that describes one or more match conditions along with the action to be taken when traffic matches this condition (allow or deny).

Protobuf type `google.cloud.compute.v1.SecurityPolicyRule`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > SecurityPolicyRule.Builder

## Implements

[SecurityPolicyRuleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleOrBuilder)

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
    
    
    public SecurityPolicyRule build()

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule)` |   
  
### buildPartial()
    
    
    public SecurityPolicyRule buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule)` |   
  
### clear()
    
    
    public SecurityPolicyRule.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearAction()
    
    
    public SecurityPolicyRule.Builder clearAction()

The Action to perform when the rule is matched. The following are the valid actions:

  * allow: allow access to target.
  * deny(STATUS): deny access to target, returns the HTTP response code specified. Valid values for `STATUS` are 403, 404, and 502.
  * rate_based_ban: limit client traffic to the configured threshold and ban the client if the traffic exceeds the threshold. Configure parameters for this action in RateLimitOptions. Requires rate_limit_options to be set.
  * redirect: redirect to a different target. This can either be an internal reCAPTCHA redirect, or an external URL-based redirect via a 302 response. Parameters for this action can be configured via redirectOptions. This action is only supported in Global Security Policies of type CLOUD_ARMOR.
  * throttle: limit client traffic to the configured threshold. Configure parameters for this action in rateLimitOptions. Requires rate_limit_options to be set for this.
  * fairshare (preview only): when traffic reaches the threshold limit, requests from the clients matching this rule begin to be rate-limited using the Fair Share algorithm. This action is only allowed in security policies of type `CLOUD_ARMOR_INTERNAL_SERVICE`.



`optional string action = 187661878;`

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` | This builder for chaining.  
  
### clearDescription()
    
    
    public SecurityPolicyRule.Builder clearDescription()

An optional description of this resource. Provide this property when you create the resource.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` | This builder for chaining.  
  
### clearHeaderAction()
    
    
    public SecurityPolicyRule.Builder clearHeaderAction()

Optional, additional actions that are performed on headers. This field is only supported in Global Security Policies of type CLOUD_ARMOR.

` optional .google.cloud.compute.v1.SecurityPolicyRuleHttpHeaderAction header_action = 328077352; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### clearKind()
    
    
    public SecurityPolicyRule.Builder clearKind()

Output only. [Output only] Type of the resource. Alwayscompute#securityPolicyRule for security policy rules

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` | This builder for chaining.  
  
### clearMatch()
    
    
    public SecurityPolicyRule.Builder clearMatch()

A match condition that incoming traffic is evaluated against. If it evaluates to true, the corresponding 'action' is enforced.

`optional .google.cloud.compute.v1.SecurityPolicyRuleMatcher match = 103668165;`

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### clearNetworkMatch()
    
    
    public SecurityPolicyRule.Builder clearNetworkMatch()

A match condition that incoming packets are evaluated against for CLOUD_ARMOR_NETWORK security policies. If it matches, the corresponding 'action' is enforced.

The match criteria for a rule consists of built-in match fields (like 'srcIpRanges') and potentially multiple user-defined match fields ('userDefinedFields').

Field values may be extracted directly from the packet or derived from it (e.g. 'srcRegionCodes'). Some fields may not be present in every packet (e.g. 'srcPorts'). A user-defined field is only present if the base header is found in the packet and the entire field is in bounds.

Each match field may specify which values can match it, listing one or more ranges, prefixes, or exact values that are considered a match for the field. A field value must be present in order to match a specified match field. If no match values are specified for a match field, then any field value is considered to match it, and it's not required to be present. For strings specifying '*' is also equivalent to match all.

For a packet to match a rule, all specified match fields must match the corresponding field values derived from the packet.

Example:

networkMatch: srcIpRanges:

  * "192.0.2.0/24"
  * "198.51.100.0/24" userDefinedFields:
  * name: "ipv4_fragment_offset" values:
  * "1-0x1fff"

The above match condition matches packets with a source IP in 192.0.2.0/24 or 198.51.100.0/24 and a user-defined field named "ipv4_fragment_offset" with a value between 1 and 0x1fff inclusive.




` optional .google.cloud.compute.v1.SecurityPolicyRuleNetworkMatcher network_match = 463387764; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### clearPreconfiguredWafConfig()
    
    
    public SecurityPolicyRule.Builder clearPreconfiguredWafConfig()

Preconfigured WAF configuration to be applied for the rule. If the rule does not evaluate preconfigured WAF rules, i.e., if evaluatePreconfiguredWaf() is not used, this field will have no effect.

` optional .google.cloud.compute.v1.SecurityPolicyRulePreconfiguredWafConfig preconfigured_waf_config = 117805027; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### clearPreview()
    
    
    public SecurityPolicyRule.Builder clearPreview()

If set to true, the specified action is not enforced.

`optional bool preview = 218686408;`

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` | This builder for chaining.  
  
### clearPriority()
    
    
    public SecurityPolicyRule.Builder clearPriority()

An integer indicating the priority of a rule in the list. The priority must be a positive value between 0 and 2147483647. Rules are evaluated from highest to lowest priority where 0 is the highest priority and 2147483647 is the lowest priority.

`optional int32 priority = 445151652;`

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` | This builder for chaining.  
  
### clearRateLimitOptions()
    
    
    public SecurityPolicyRule.Builder clearRateLimitOptions()

Must be specified if the action is "rate_based_ban" or "throttle" or "fairshare". Cannot be specified for any other actions.

` optional .google.cloud.compute.v1.SecurityPolicyRuleRateLimitOptions rate_limit_options = 67544315; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### clearRedirectOptions()
    
    
    public SecurityPolicyRule.Builder clearRedirectOptions()

Parameters defining the redirect action. Cannot be specified for any other actions. This field is only supported in Global Security Policies of type CLOUD_ARMOR.

` optional .google.cloud.compute.v1.SecurityPolicyRuleRedirectOptions redirect_options = 163285307; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### getAction()
    
    
    public String getAction()

The Action to perform when the rule is matched. The following are the valid actions:

  * allow: allow access to target.
  * deny(STATUS): deny access to target, returns the HTTP response code specified. Valid values for `STATUS` are 403, 404, and 502.
  * rate_based_ban: limit client traffic to the configured threshold and ban the client if the traffic exceeds the threshold. Configure parameters for this action in RateLimitOptions. Requires rate_limit_options to be set.
  * redirect: redirect to a different target. This can either be an internal reCAPTCHA redirect, or an external URL-based redirect via a 302 response. Parameters for this action can be configured via redirectOptions. This action is only supported in Global Security Policies of type CLOUD_ARMOR.
  * throttle: limit client traffic to the configured threshold. Configure parameters for this action in rateLimitOptions. Requires rate_limit_options to be set for this.
  * fairshare (preview only): when traffic reaches the threshold limit, requests from the clients matching this rule begin to be rate-limited using the Fair Share algorithm. This action is only allowed in security policies of type `CLOUD_ARMOR_INTERNAL_SERVICE`.



`optional string action = 187661878;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The action.  
  
### getActionBytes()
    
    
    public ByteString getActionBytes()

The Action to perform when the rule is matched. The following are the valid actions:

  * allow: allow access to target.
  * deny(STATUS): deny access to target, returns the HTTP response code specified. Valid values for `STATUS` are 403, 404, and 502.
  * rate_based_ban: limit client traffic to the configured threshold and ban the client if the traffic exceeds the threshold. Configure parameters for this action in RateLimitOptions. Requires rate_limit_options to be set.
  * redirect: redirect to a different target. This can either be an internal reCAPTCHA redirect, or an external URL-based redirect via a 302 response. Parameters for this action can be configured via redirectOptions. This action is only supported in Global Security Policies of type CLOUD_ARMOR.
  * throttle: limit client traffic to the configured threshold. Configure parameters for this action in rateLimitOptions. Requires rate_limit_options to be set for this.
  * fairshare (preview only): when traffic reaches the threshold limit, requests from the clients matching this rule begin to be rate-limited using the Fair Share algorithm. This action is only allowed in security policies of type `CLOUD_ARMOR_INTERNAL_SERVICE`.



`optional string action = 187661878;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for action.  
  
### getDefaultInstanceForType()
    
    
    public SecurityPolicyRule getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule)` |   
  
### getDescription()
    
    
    public String getDescription()

An optional description of this resource. Provide this property when you create the resource.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public ByteString getDescriptionBytes()

An optional description of this resource. Provide this property when you create the resource.

`optional string description = 422937596;`

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

### getHeaderAction()
    
    
    public SecurityPolicyRuleHttpHeaderAction getHeaderAction()

Optional, additional actions that are performed on headers. This field is only supported in Global Security Policies of type CLOUD_ARMOR.

` optional .google.cloud.compute.v1.SecurityPolicyRuleHttpHeaderAction header_action = 328077352; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRuleHttpHeaderAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleHttpHeaderAction)` | The headerAction.  
  
### getHeaderActionBuilder()
    
    
    public SecurityPolicyRuleHttpHeaderAction.Builder getHeaderActionBuilder()

Optional, additional actions that are performed on headers. This field is only supported in Global Security Policies of type CLOUD_ARMOR.

` optional .google.cloud.compute.v1.SecurityPolicyRuleHttpHeaderAction header_action = 328077352; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRuleHttpHeaderAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleHttpHeaderAction.Builder)` |   
  
### getHeaderActionOrBuilder()
    
    
    public SecurityPolicyRuleHttpHeaderActionOrBuilder getHeaderActionOrBuilder()

Optional, additional actions that are performed on headers. This field is only supported in Global Security Policies of type CLOUD_ARMOR.

` optional .google.cloud.compute.v1.SecurityPolicyRuleHttpHeaderAction header_action = 328077352; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRuleHttpHeaderActionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleHttpHeaderActionOrBuilder)` |   
  
### getKind()
    
    
    public String getKind()

Output only. [Output only] Type of the resource. Alwayscompute#securityPolicyRule for security policy rules

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kind.  
  
### getKindBytes()
    
    
    public ByteString getKindBytes()

Output only. [Output only] Type of the resource. Alwayscompute#securityPolicyRule for security policy rules

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kind.  
  
### getMatch()
    
    
    public SecurityPolicyRuleMatcher getMatch()

A match condition that incoming traffic is evaluated against. If it evaluates to true, the corresponding 'action' is enforced.

`optional .google.cloud.compute.v1.SecurityPolicyRuleMatcher match = 103668165;`

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRuleMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleMatcher)` | The match.  
  
### getMatchBuilder()
    
    
    public SecurityPolicyRuleMatcher.Builder getMatchBuilder()

A match condition that incoming traffic is evaluated against. If it evaluates to true, the corresponding 'action' is enforced.

`optional .google.cloud.compute.v1.SecurityPolicyRuleMatcher match = 103668165;`

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRuleMatcher.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleMatcher.Builder)` |   
  
### getMatchOrBuilder()
    
    
    public SecurityPolicyRuleMatcherOrBuilder getMatchOrBuilder()

A match condition that incoming traffic is evaluated against. If it evaluates to true, the corresponding 'action' is enforced.

`optional .google.cloud.compute.v1.SecurityPolicyRuleMatcher match = 103668165;`

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRuleMatcherOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleMatcherOrBuilder)` |   
  
### getNetworkMatch()
    
    
    public SecurityPolicyRuleNetworkMatcher getNetworkMatch()

A match condition that incoming packets are evaluated against for CLOUD_ARMOR_NETWORK security policies. If it matches, the corresponding 'action' is enforced.

The match criteria for a rule consists of built-in match fields (like 'srcIpRanges') and potentially multiple user-defined match fields ('userDefinedFields').

Field values may be extracted directly from the packet or derived from it (e.g. 'srcRegionCodes'). Some fields may not be present in every packet (e.g. 'srcPorts'). A user-defined field is only present if the base header is found in the packet and the entire field is in bounds.

Each match field may specify which values can match it, listing one or more ranges, prefixes, or exact values that are considered a match for the field. A field value must be present in order to match a specified match field. If no match values are specified for a match field, then any field value is considered to match it, and it's not required to be present. For strings specifying '*' is also equivalent to match all.

For a packet to match a rule, all specified match fields must match the corresponding field values derived from the packet.

Example:

networkMatch: srcIpRanges:

  * "192.0.2.0/24"
  * "198.51.100.0/24" userDefinedFields:
  * name: "ipv4_fragment_offset" values:
  * "1-0x1fff"

The above match condition matches packets with a source IP in 192.0.2.0/24 or 198.51.100.0/24 and a user-defined field named "ipv4_fragment_offset" with a value between 1 and 0x1fff inclusive.




` optional .google.cloud.compute.v1.SecurityPolicyRuleNetworkMatcher network_match = 463387764; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRuleNetworkMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleNetworkMatcher)` | The networkMatch.  
  
### getNetworkMatchBuilder()
    
    
    public SecurityPolicyRuleNetworkMatcher.Builder getNetworkMatchBuilder()

A match condition that incoming packets are evaluated against for CLOUD_ARMOR_NETWORK security policies. If it matches, the corresponding 'action' is enforced.

The match criteria for a rule consists of built-in match fields (like 'srcIpRanges') and potentially multiple user-defined match fields ('userDefinedFields').

Field values may be extracted directly from the packet or derived from it (e.g. 'srcRegionCodes'). Some fields may not be present in every packet (e.g. 'srcPorts'). A user-defined field is only present if the base header is found in the packet and the entire field is in bounds.

Each match field may specify which values can match it, listing one or more ranges, prefixes, or exact values that are considered a match for the field. A field value must be present in order to match a specified match field. If no match values are specified for a match field, then any field value is considered to match it, and it's not required to be present. For strings specifying '*' is also equivalent to match all.

For a packet to match a rule, all specified match fields must match the corresponding field values derived from the packet.

Example:

networkMatch: srcIpRanges:

  * "192.0.2.0/24"
  * "198.51.100.0/24" userDefinedFields:
  * name: "ipv4_fragment_offset" values:
  * "1-0x1fff"

The above match condition matches packets with a source IP in 192.0.2.0/24 or 198.51.100.0/24 and a user-defined field named "ipv4_fragment_offset" with a value between 1 and 0x1fff inclusive.




` optional .google.cloud.compute.v1.SecurityPolicyRuleNetworkMatcher network_match = 463387764; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRuleNetworkMatcher.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleNetworkMatcher.Builder)` |   
  
### getNetworkMatchOrBuilder()
    
    
    public SecurityPolicyRuleNetworkMatcherOrBuilder getNetworkMatchOrBuilder()

A match condition that incoming packets are evaluated against for CLOUD_ARMOR_NETWORK security policies. If it matches, the corresponding 'action' is enforced.

The match criteria for a rule consists of built-in match fields (like 'srcIpRanges') and potentially multiple user-defined match fields ('userDefinedFields').

Field values may be extracted directly from the packet or derived from it (e.g. 'srcRegionCodes'). Some fields may not be present in every packet (e.g. 'srcPorts'). A user-defined field is only present if the base header is found in the packet and the entire field is in bounds.

Each match field may specify which values can match it, listing one or more ranges, prefixes, or exact values that are considered a match for the field. A field value must be present in order to match a specified match field. If no match values are specified for a match field, then any field value is considered to match it, and it's not required to be present. For strings specifying '*' is also equivalent to match all.

For a packet to match a rule, all specified match fields must match the corresponding field values derived from the packet.

Example:

networkMatch: srcIpRanges:

  * "192.0.2.0/24"
  * "198.51.100.0/24" userDefinedFields:
  * name: "ipv4_fragment_offset" values:
  * "1-0x1fff"

The above match condition matches packets with a source IP in 192.0.2.0/24 or 198.51.100.0/24 and a user-defined field named "ipv4_fragment_offset" with a value between 1 and 0x1fff inclusive.




` optional .google.cloud.compute.v1.SecurityPolicyRuleNetworkMatcher network_match = 463387764; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRuleNetworkMatcherOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleNetworkMatcherOrBuilder)` |   
  
### getPreconfiguredWafConfig()
    
    
    public SecurityPolicyRulePreconfiguredWafConfig getPreconfiguredWafConfig()

Preconfigured WAF configuration to be applied for the rule. If the rule does not evaluate preconfigured WAF rules, i.e., if evaluatePreconfiguredWaf() is not used, this field will have no effect.

` optional .google.cloud.compute.v1.SecurityPolicyRulePreconfiguredWafConfig preconfigured_waf_config = 117805027; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRulePreconfiguredWafConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRulePreconfiguredWafConfig)` | The preconfiguredWafConfig.  
  
### getPreconfiguredWafConfigBuilder()
    
    
    public SecurityPolicyRulePreconfiguredWafConfig.Builder getPreconfiguredWafConfigBuilder()

Preconfigured WAF configuration to be applied for the rule. If the rule does not evaluate preconfigured WAF rules, i.e., if evaluatePreconfiguredWaf() is not used, this field will have no effect.

` optional .google.cloud.compute.v1.SecurityPolicyRulePreconfiguredWafConfig preconfigured_waf_config = 117805027; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRulePreconfiguredWafConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRulePreconfiguredWafConfig.Builder)` |   
  
### getPreconfiguredWafConfigOrBuilder()
    
    
    public SecurityPolicyRulePreconfiguredWafConfigOrBuilder getPreconfiguredWafConfigOrBuilder()

Preconfigured WAF configuration to be applied for the rule. If the rule does not evaluate preconfigured WAF rules, i.e., if evaluatePreconfiguredWaf() is not used, this field will have no effect.

` optional .google.cloud.compute.v1.SecurityPolicyRulePreconfiguredWafConfig preconfigured_waf_config = 117805027; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRulePreconfiguredWafConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRulePreconfiguredWafConfigOrBuilder)` |   
  
### getPreview()
    
    
    public boolean getPreview()

If set to true, the specified action is not enforced.

`optional bool preview = 218686408;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The preview.  
  
### getPriority()
    
    
    public int getPriority()

An integer indicating the priority of a rule in the list. The priority must be a positive value between 0 and 2147483647. Rules are evaluated from highest to lowest priority where 0 is the highest priority and 2147483647 is the lowest priority.

`optional int32 priority = 445151652;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The priority.  
  
### getRateLimitOptions()
    
    
    public SecurityPolicyRuleRateLimitOptions getRateLimitOptions()

Must be specified if the action is "rate_based_ban" or "throttle" or "fairshare". Cannot be specified for any other actions.

` optional .google.cloud.compute.v1.SecurityPolicyRuleRateLimitOptions rate_limit_options = 67544315; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRuleRateLimitOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleRateLimitOptions)` | The rateLimitOptions.  
  
### getRateLimitOptionsBuilder()
    
    
    public SecurityPolicyRuleRateLimitOptions.Builder getRateLimitOptionsBuilder()

Must be specified if the action is "rate_based_ban" or "throttle" or "fairshare". Cannot be specified for any other actions.

` optional .google.cloud.compute.v1.SecurityPolicyRuleRateLimitOptions rate_limit_options = 67544315; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRuleRateLimitOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleRateLimitOptions.Builder)` |   
  
### getRateLimitOptionsOrBuilder()
    
    
    public SecurityPolicyRuleRateLimitOptionsOrBuilder getRateLimitOptionsOrBuilder()

Must be specified if the action is "rate_based_ban" or "throttle" or "fairshare". Cannot be specified for any other actions.

` optional .google.cloud.compute.v1.SecurityPolicyRuleRateLimitOptions rate_limit_options = 67544315; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRuleRateLimitOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleRateLimitOptionsOrBuilder)` |   
  
### getRedirectOptions()
    
    
    public SecurityPolicyRuleRedirectOptions getRedirectOptions()

Parameters defining the redirect action. Cannot be specified for any other actions. This field is only supported in Global Security Policies of type CLOUD_ARMOR.

` optional .google.cloud.compute.v1.SecurityPolicyRuleRedirectOptions redirect_options = 163285307; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRuleRedirectOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleRedirectOptions)` | The redirectOptions.  
  
### getRedirectOptionsBuilder()
    
    
    public SecurityPolicyRuleRedirectOptions.Builder getRedirectOptionsBuilder()

Parameters defining the redirect action. Cannot be specified for any other actions. This field is only supported in Global Security Policies of type CLOUD_ARMOR.

` optional .google.cloud.compute.v1.SecurityPolicyRuleRedirectOptions redirect_options = 163285307; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRuleRedirectOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleRedirectOptions.Builder)` |   
  
### getRedirectOptionsOrBuilder()
    
    
    public SecurityPolicyRuleRedirectOptionsOrBuilder getRedirectOptionsOrBuilder()

Parameters defining the redirect action. Cannot be specified for any other actions. This field is only supported in Global Security Policies of type CLOUD_ARMOR.

` optional .google.cloud.compute.v1.SecurityPolicyRuleRedirectOptions redirect_options = 163285307; `

**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRuleRedirectOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleRedirectOptionsOrBuilder)` |   
  
### hasAction()
    
    
    public boolean hasAction()

The Action to perform when the rule is matched. The following are the valid actions:

  * allow: allow access to target.
  * deny(STATUS): deny access to target, returns the HTTP response code specified. Valid values for `STATUS` are 403, 404, and 502.
  * rate_based_ban: limit client traffic to the configured threshold and ban the client if the traffic exceeds the threshold. Configure parameters for this action in RateLimitOptions. Requires rate_limit_options to be set.
  * redirect: redirect to a different target. This can either be an internal reCAPTCHA redirect, or an external URL-based redirect via a 302 response. Parameters for this action can be configured via redirectOptions. This action is only supported in Global Security Policies of type CLOUD_ARMOR.
  * throttle: limit client traffic to the configured threshold. Configure parameters for this action in rateLimitOptions. Requires rate_limit_options to be set for this.
  * fairshare (preview only): when traffic reaches the threshold limit, requests from the clients matching this rule begin to be rate-limited using the Fair Share algorithm. This action is only allowed in security policies of type `CLOUD_ARMOR_INTERNAL_SERVICE`.



`optional string action = 187661878;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the action field is set.  
  
### hasDescription()
    
    
    public boolean hasDescription()

An optional description of this resource. Provide this property when you create the resource.

`optional string description = 422937596;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the description field is set.  
  
### hasHeaderAction()
    
    
    public boolean hasHeaderAction()

Optional, additional actions that are performed on headers. This field is only supported in Global Security Policies of type CLOUD_ARMOR.

` optional .google.cloud.compute.v1.SecurityPolicyRuleHttpHeaderAction header_action = 328077352; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the headerAction field is set.  
  
### hasKind()
    
    
    public boolean hasKind()

Output only. [Output only] Type of the resource. Alwayscompute#securityPolicyRule for security policy rules

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the kind field is set.  
  
### hasMatch()
    
    
    public boolean hasMatch()

A match condition that incoming traffic is evaluated against. If it evaluates to true, the corresponding 'action' is enforced.

`optional .google.cloud.compute.v1.SecurityPolicyRuleMatcher match = 103668165;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the match field is set.  
  
### hasNetworkMatch()
    
    
    public boolean hasNetworkMatch()

A match condition that incoming packets are evaluated against for CLOUD_ARMOR_NETWORK security policies. If it matches, the corresponding 'action' is enforced.

The match criteria for a rule consists of built-in match fields (like 'srcIpRanges') and potentially multiple user-defined match fields ('userDefinedFields').

Field values may be extracted directly from the packet or derived from it (e.g. 'srcRegionCodes'). Some fields may not be present in every packet (e.g. 'srcPorts'). A user-defined field is only present if the base header is found in the packet and the entire field is in bounds.

Each match field may specify which values can match it, listing one or more ranges, prefixes, or exact values that are considered a match for the field. A field value must be present in order to match a specified match field. If no match values are specified for a match field, then any field value is considered to match it, and it's not required to be present. For strings specifying '*' is also equivalent to match all.

For a packet to match a rule, all specified match fields must match the corresponding field values derived from the packet.

Example:

networkMatch: srcIpRanges:

  * "192.0.2.0/24"
  * "198.51.100.0/24" userDefinedFields:
  * name: "ipv4_fragment_offset" values:
  * "1-0x1fff"

The above match condition matches packets with a source IP in 192.0.2.0/24 or 198.51.100.0/24 and a user-defined field named "ipv4_fragment_offset" with a value between 1 and 0x1fff inclusive.




` optional .google.cloud.compute.v1.SecurityPolicyRuleNetworkMatcher network_match = 463387764; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the networkMatch field is set.  
  
### hasPreconfiguredWafConfig()
    
    
    public boolean hasPreconfiguredWafConfig()

Preconfigured WAF configuration to be applied for the rule. If the rule does not evaluate preconfigured WAF rules, i.e., if evaluatePreconfiguredWaf() is not used, this field will have no effect.

` optional .google.cloud.compute.v1.SecurityPolicyRulePreconfiguredWafConfig preconfigured_waf_config = 117805027; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the preconfiguredWafConfig field is set.  
  
### hasPreview()
    
    
    public boolean hasPreview()

If set to true, the specified action is not enforced.

`optional bool preview = 218686408;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the preview field is set.  
  
### hasPriority()
    
    
    public boolean hasPriority()

An integer indicating the priority of a rule in the list. The priority must be a positive value between 0 and 2147483647. Rules are evaluated from highest to lowest priority where 0 is the highest priority and 2147483647 is the lowest priority.

`optional int32 priority = 445151652;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the priority field is set.  
  
### hasRateLimitOptions()
    
    
    public boolean hasRateLimitOptions()

Must be specified if the action is "rate_based_ban" or "throttle" or "fairshare". Cannot be specified for any other actions.

` optional .google.cloud.compute.v1.SecurityPolicyRuleRateLimitOptions rate_limit_options = 67544315; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rateLimitOptions field is set.  
  
### hasRedirectOptions()
    
    
    public boolean hasRedirectOptions()

Parameters defining the redirect action. Cannot be specified for any other actions. This field is only supported in Global Security Policies of type CLOUD_ARMOR.

` optional .google.cloud.compute.v1.SecurityPolicyRuleRedirectOptions redirect_options = 163285307; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the redirectOptions field is set.  
  
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

### mergeFrom(SecurityPolicyRule other)
    
    
    public SecurityPolicyRule.Builder mergeFrom(SecurityPolicyRule other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public SecurityPolicyRule.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public SecurityPolicyRule.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeHeaderAction(SecurityPolicyRuleHttpHeaderAction value)
    
    
    public SecurityPolicyRule.Builder mergeHeaderAction(SecurityPolicyRuleHttpHeaderAction value)

Optional, additional actions that are performed on headers. This field is only supported in Global Security Policies of type CLOUD_ARMOR.

` optional .google.cloud.compute.v1.SecurityPolicyRuleHttpHeaderAction header_action = 328077352; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SecurityPolicyRuleHttpHeaderAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleHttpHeaderAction)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### mergeMatch(SecurityPolicyRuleMatcher value)
    
    
    public SecurityPolicyRule.Builder mergeMatch(SecurityPolicyRuleMatcher value)

A match condition that incoming traffic is evaluated against. If it evaluates to true, the corresponding 'action' is enforced.

`optional .google.cloud.compute.v1.SecurityPolicyRuleMatcher match = 103668165;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SecurityPolicyRuleMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleMatcher)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### mergeNetworkMatch(SecurityPolicyRuleNetworkMatcher value)
    
    
    public SecurityPolicyRule.Builder mergeNetworkMatch(SecurityPolicyRuleNetworkMatcher value)

A match condition that incoming packets are evaluated against for CLOUD_ARMOR_NETWORK security policies. If it matches, the corresponding 'action' is enforced.

The match criteria for a rule consists of built-in match fields (like 'srcIpRanges') and potentially multiple user-defined match fields ('userDefinedFields').

Field values may be extracted directly from the packet or derived from it (e.g. 'srcRegionCodes'). Some fields may not be present in every packet (e.g. 'srcPorts'). A user-defined field is only present if the base header is found in the packet and the entire field is in bounds.

Each match field may specify which values can match it, listing one or more ranges, prefixes, or exact values that are considered a match for the field. A field value must be present in order to match a specified match field. If no match values are specified for a match field, then any field value is considered to match it, and it's not required to be present. For strings specifying '*' is also equivalent to match all.

For a packet to match a rule, all specified match fields must match the corresponding field values derived from the packet.

Example:

networkMatch: srcIpRanges:

  * "192.0.2.0/24"
  * "198.51.100.0/24" userDefinedFields:
  * name: "ipv4_fragment_offset" values:
  * "1-0x1fff"

The above match condition matches packets with a source IP in 192.0.2.0/24 or 198.51.100.0/24 and a user-defined field named "ipv4_fragment_offset" with a value between 1 and 0x1fff inclusive.




` optional .google.cloud.compute.v1.SecurityPolicyRuleNetworkMatcher network_match = 463387764; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SecurityPolicyRuleNetworkMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleNetworkMatcher)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### mergePreconfiguredWafConfig(SecurityPolicyRulePreconfiguredWafConfig value)
    
    
    public SecurityPolicyRule.Builder mergePreconfiguredWafConfig(SecurityPolicyRulePreconfiguredWafConfig value)

Preconfigured WAF configuration to be applied for the rule. If the rule does not evaluate preconfigured WAF rules, i.e., if evaluatePreconfiguredWaf() is not used, this field will have no effect.

` optional .google.cloud.compute.v1.SecurityPolicyRulePreconfiguredWafConfig preconfigured_waf_config = 117805027; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SecurityPolicyRulePreconfiguredWafConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRulePreconfiguredWafConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### mergeRateLimitOptions(SecurityPolicyRuleRateLimitOptions value)
    
    
    public SecurityPolicyRule.Builder mergeRateLimitOptions(SecurityPolicyRuleRateLimitOptions value)

Must be specified if the action is "rate_based_ban" or "throttle" or "fairshare". Cannot be specified for any other actions.

` optional .google.cloud.compute.v1.SecurityPolicyRuleRateLimitOptions rate_limit_options = 67544315; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SecurityPolicyRuleRateLimitOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleRateLimitOptions)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### mergeRedirectOptions(SecurityPolicyRuleRedirectOptions value)
    
    
    public SecurityPolicyRule.Builder mergeRedirectOptions(SecurityPolicyRuleRedirectOptions value)

Parameters defining the redirect action. Cannot be specified for any other actions. This field is only supported in Global Security Policies of type CLOUD_ARMOR.

` optional .google.cloud.compute.v1.SecurityPolicyRuleRedirectOptions redirect_options = 163285307; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SecurityPolicyRuleRedirectOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleRedirectOptions)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### setAction(String value)
    
    
    public SecurityPolicyRule.Builder setAction(String value)

The Action to perform when the rule is matched. The following are the valid actions:

  * allow: allow access to target.
  * deny(STATUS): deny access to target, returns the HTTP response code specified. Valid values for `STATUS` are 403, 404, and 502.
  * rate_based_ban: limit client traffic to the configured threshold and ban the client if the traffic exceeds the threshold. Configure parameters for this action in RateLimitOptions. Requires rate_limit_options to be set.
  * redirect: redirect to a different target. This can either be an internal reCAPTCHA redirect, or an external URL-based redirect via a 302 response. Parameters for this action can be configured via redirectOptions. This action is only supported in Global Security Policies of type CLOUD_ARMOR.
  * throttle: limit client traffic to the configured threshold. Configure parameters for this action in rateLimitOptions. Requires rate_limit_options to be set for this.
  * fairshare (preview only): when traffic reaches the threshold limit, requests from the clients matching this rule begin to be rate-limited using the Fair Share algorithm. This action is only allowed in security policies of type `CLOUD_ARMOR_INTERNAL_SERVICE`.



`optional string action = 187661878;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The action to set.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` | This builder for chaining.  
  
### setActionBytes(ByteString value)
    
    
    public SecurityPolicyRule.Builder setActionBytes(ByteString value)

The Action to perform when the rule is matched. The following are the valid actions:

  * allow: allow access to target.
  * deny(STATUS): deny access to target, returns the HTTP response code specified. Valid values for `STATUS` are 403, 404, and 502.
  * rate_based_ban: limit client traffic to the configured threshold and ban the client if the traffic exceeds the threshold. Configure parameters for this action in RateLimitOptions. Requires rate_limit_options to be set.
  * redirect: redirect to a different target. This can either be an internal reCAPTCHA redirect, or an external URL-based redirect via a 302 response. Parameters for this action can be configured via redirectOptions. This action is only supported in Global Security Policies of type CLOUD_ARMOR.
  * throttle: limit client traffic to the configured threshold. Configure parameters for this action in rateLimitOptions. Requires rate_limit_options to be set for this.
  * fairshare (preview only): when traffic reaches the threshold limit, requests from the clients matching this rule begin to be rate-limited using the Fair Share algorithm. This action is only allowed in security policies of type `CLOUD_ARMOR_INTERNAL_SERVICE`.



`optional string action = 187661878;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for action to set.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` | This builder for chaining.  
  
### setDescription(String value)
    
    
    public SecurityPolicyRule.Builder setDescription(String value)

An optional description of this resource. Provide this property when you create the resource.

`optional string description = 422937596;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The description to set.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` | This builder for chaining.  
  
### setDescriptionBytes(ByteString value)
    
    
    public SecurityPolicyRule.Builder setDescriptionBytes(ByteString value)

An optional description of this resource. Provide this property when you create the resource.

`optional string description = 422937596;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for description to set.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` | This builder for chaining.  
  
### setHeaderAction(SecurityPolicyRuleHttpHeaderAction value)
    
    
    public SecurityPolicyRule.Builder setHeaderAction(SecurityPolicyRuleHttpHeaderAction value)

Optional, additional actions that are performed on headers. This field is only supported in Global Security Policies of type CLOUD_ARMOR.

` optional .google.cloud.compute.v1.SecurityPolicyRuleHttpHeaderAction header_action = 328077352; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SecurityPolicyRuleHttpHeaderAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleHttpHeaderAction)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### setHeaderAction(SecurityPolicyRuleHttpHeaderAction.Builder builderForValue)
    
    
    public SecurityPolicyRule.Builder setHeaderAction(SecurityPolicyRuleHttpHeaderAction.Builder builderForValue)

Optional, additional actions that are performed on headers. This field is only supported in Global Security Policies of type CLOUD_ARMOR.

` optional .google.cloud.compute.v1.SecurityPolicyRuleHttpHeaderAction header_action = 328077352; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SecurityPolicyRuleHttpHeaderAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleHttpHeaderAction.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### setKind(String value)
    
    
    public SecurityPolicyRule.Builder setKind(String value)

Output only. [Output only] Type of the resource. Alwayscompute#securityPolicyRule for security policy rules

`optional string kind = 3292052;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The kind to set.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` | This builder for chaining.  
  
### setKindBytes(ByteString value)
    
    
    public SecurityPolicyRule.Builder setKindBytes(ByteString value)

Output only. [Output only] Type of the resource. Alwayscompute#securityPolicyRule for security policy rules

`optional string kind = 3292052;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for kind to set.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` | This builder for chaining.  
  
### setMatch(SecurityPolicyRuleMatcher value)
    
    
    public SecurityPolicyRule.Builder setMatch(SecurityPolicyRuleMatcher value)

A match condition that incoming traffic is evaluated against. If it evaluates to true, the corresponding 'action' is enforced.

`optional .google.cloud.compute.v1.SecurityPolicyRuleMatcher match = 103668165;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SecurityPolicyRuleMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleMatcher)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### setMatch(SecurityPolicyRuleMatcher.Builder builderForValue)
    
    
    public SecurityPolicyRule.Builder setMatch(SecurityPolicyRuleMatcher.Builder builderForValue)

A match condition that incoming traffic is evaluated against. If it evaluates to true, the corresponding 'action' is enforced.

`optional .google.cloud.compute.v1.SecurityPolicyRuleMatcher match = 103668165;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SecurityPolicyRuleMatcher.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleMatcher.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### setNetworkMatch(SecurityPolicyRuleNetworkMatcher value)
    
    
    public SecurityPolicyRule.Builder setNetworkMatch(SecurityPolicyRuleNetworkMatcher value)

A match condition that incoming packets are evaluated against for CLOUD_ARMOR_NETWORK security policies. If it matches, the corresponding 'action' is enforced.

The match criteria for a rule consists of built-in match fields (like 'srcIpRanges') and potentially multiple user-defined match fields ('userDefinedFields').

Field values may be extracted directly from the packet or derived from it (e.g. 'srcRegionCodes'). Some fields may not be present in every packet (e.g. 'srcPorts'). A user-defined field is only present if the base header is found in the packet and the entire field is in bounds.

Each match field may specify which values can match it, listing one or more ranges, prefixes, or exact values that are considered a match for the field. A field value must be present in order to match a specified match field. If no match values are specified for a match field, then any field value is considered to match it, and it's not required to be present. For strings specifying '*' is also equivalent to match all.

For a packet to match a rule, all specified match fields must match the corresponding field values derived from the packet.

Example:

networkMatch: srcIpRanges:

  * "192.0.2.0/24"
  * "198.51.100.0/24" userDefinedFields:
  * name: "ipv4_fragment_offset" values:
  * "1-0x1fff"

The above match condition matches packets with a source IP in 192.0.2.0/24 or 198.51.100.0/24 and a user-defined field named "ipv4_fragment_offset" with a value between 1 and 0x1fff inclusive.




` optional .google.cloud.compute.v1.SecurityPolicyRuleNetworkMatcher network_match = 463387764; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SecurityPolicyRuleNetworkMatcher](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleNetworkMatcher)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### setNetworkMatch(SecurityPolicyRuleNetworkMatcher.Builder builderForValue)
    
    
    public SecurityPolicyRule.Builder setNetworkMatch(SecurityPolicyRuleNetworkMatcher.Builder builderForValue)

A match condition that incoming packets are evaluated against for CLOUD_ARMOR_NETWORK security policies. If it matches, the corresponding 'action' is enforced.

The match criteria for a rule consists of built-in match fields (like 'srcIpRanges') and potentially multiple user-defined match fields ('userDefinedFields').

Field values may be extracted directly from the packet or derived from it (e.g. 'srcRegionCodes'). Some fields may not be present in every packet (e.g. 'srcPorts'). A user-defined field is only present if the base header is found in the packet and the entire field is in bounds.

Each match field may specify which values can match it, listing one or more ranges, prefixes, or exact values that are considered a match for the field. A field value must be present in order to match a specified match field. If no match values are specified for a match field, then any field value is considered to match it, and it's not required to be present. For strings specifying '*' is also equivalent to match all.

For a packet to match a rule, all specified match fields must match the corresponding field values derived from the packet.

Example:

networkMatch: srcIpRanges:

  * "192.0.2.0/24"
  * "198.51.100.0/24" userDefinedFields:
  * name: "ipv4_fragment_offset" values:
  * "1-0x1fff"

The above match condition matches packets with a source IP in 192.0.2.0/24 or 198.51.100.0/24 and a user-defined field named "ipv4_fragment_offset" with a value between 1 and 0x1fff inclusive.




` optional .google.cloud.compute.v1.SecurityPolicyRuleNetworkMatcher network_match = 463387764; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SecurityPolicyRuleNetworkMatcher.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleNetworkMatcher.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### setPreconfiguredWafConfig(SecurityPolicyRulePreconfiguredWafConfig value)
    
    
    public SecurityPolicyRule.Builder setPreconfiguredWafConfig(SecurityPolicyRulePreconfiguredWafConfig value)

Preconfigured WAF configuration to be applied for the rule. If the rule does not evaluate preconfigured WAF rules, i.e., if evaluatePreconfiguredWaf() is not used, this field will have no effect.

` optional .google.cloud.compute.v1.SecurityPolicyRulePreconfiguredWafConfig preconfigured_waf_config = 117805027; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SecurityPolicyRulePreconfiguredWafConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRulePreconfiguredWafConfig)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### setPreconfiguredWafConfig(SecurityPolicyRulePreconfiguredWafConfig.Builder builderForValue)
    
    
    public SecurityPolicyRule.Builder setPreconfiguredWafConfig(SecurityPolicyRulePreconfiguredWafConfig.Builder builderForValue)

Preconfigured WAF configuration to be applied for the rule. If the rule does not evaluate preconfigured WAF rules, i.e., if evaluatePreconfiguredWaf() is not used, this field will have no effect.

` optional .google.cloud.compute.v1.SecurityPolicyRulePreconfiguredWafConfig preconfigured_waf_config = 117805027; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SecurityPolicyRulePreconfiguredWafConfig.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRulePreconfiguredWafConfig.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### setPreview(boolean value)
    
    
    public SecurityPolicyRule.Builder setPreview(boolean value)

If set to true, the specified action is not enforced.

`optional bool preview = 218686408;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The preview to set.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` | This builder for chaining.  
  
### setPriority(int value)
    
    
    public SecurityPolicyRule.Builder setPriority(int value)

An integer indicating the priority of a rule in the list. The priority must be a positive value between 0 and 2147483647. Rules are evaluated from highest to lowest priority where 0 is the highest priority and 2147483647 is the lowest priority.

`optional int32 priority = 445151652;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The priority to set.  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` | This builder for chaining.  
  
### setRateLimitOptions(SecurityPolicyRuleRateLimitOptions value)
    
    
    public SecurityPolicyRule.Builder setRateLimitOptions(SecurityPolicyRuleRateLimitOptions value)

Must be specified if the action is "rate_based_ban" or "throttle" or "fairshare". Cannot be specified for any other actions.

` optional .google.cloud.compute.v1.SecurityPolicyRuleRateLimitOptions rate_limit_options = 67544315; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SecurityPolicyRuleRateLimitOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleRateLimitOptions)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### setRateLimitOptions(SecurityPolicyRuleRateLimitOptions.Builder builderForValue)
    
    
    public SecurityPolicyRule.Builder setRateLimitOptions(SecurityPolicyRuleRateLimitOptions.Builder builderForValue)

Must be specified if the action is "rate_based_ban" or "throttle" or "fairshare". Cannot be specified for any other actions.

` optional .google.cloud.compute.v1.SecurityPolicyRuleRateLimitOptions rate_limit_options = 67544315; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SecurityPolicyRuleRateLimitOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleRateLimitOptions.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### setRedirectOptions(SecurityPolicyRuleRedirectOptions value)
    
    
    public SecurityPolicyRule.Builder setRedirectOptions(SecurityPolicyRuleRedirectOptions value)

Parameters defining the redirect action. Cannot be specified for any other actions. This field is only supported in Global Security Policies of type CLOUD_ARMOR.

` optional .google.cloud.compute.v1.SecurityPolicyRuleRedirectOptions redirect_options = 163285307; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[SecurityPolicyRuleRedirectOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleRedirectOptions)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
### setRedirectOptions(SecurityPolicyRuleRedirectOptions.Builder builderForValue)
    
    
    public SecurityPolicyRule.Builder setRedirectOptions(SecurityPolicyRuleRedirectOptions.Builder builderForValue)

Parameters defining the redirect action. Cannot be specified for any other actions. This field is only supported in Global Security Policies of type CLOUD_ARMOR.

` optional .google.cloud.compute.v1.SecurityPolicyRuleRedirectOptions redirect_options = 163285307; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[SecurityPolicyRuleRedirectOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRuleRedirectOptions.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPolicyRule.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
