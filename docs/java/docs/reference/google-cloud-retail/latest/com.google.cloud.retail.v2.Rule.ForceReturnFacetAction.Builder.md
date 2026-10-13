---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.Builder
title: Class Rule.ForceReturnFacetAction.Builder (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:08.318370+00:00
---

# Class Rule.ForceReturnFacetAction.Builder (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Rule.ForceReturnFacetAction.Builder (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.1  2.4.0  2.3.0  2.2.3  2.1.0  2.0.19 
    
    
    public static final class Rule.ForceReturnFacetAction.Builder extends GeneratedMessage.Builder<Rule.ForceReturnFacetAction.Builder> implements Rule.ForceReturnFacetActionOrBuilder

Force returns an attribute/facet in the request around a certain position or above.

  * Rule Condition: Must specify non-empty Condition.query_terms (for search only) or Condition.page_categories (for browse only), but can't specify both.

  * Action Inputs: attribute name, position

  * Action Result: Will force return a facet key around a certain position or above if the condition is satisfied.

Example: Suppose the query is "shoes", the Condition.query_terms is "shoes", the ForceReturnFacetAction.FacetPositionAdjustment.attribute_name is "size" and the ForceReturnFacetAction.FacetPositionAdjustment.position is 8.

Two cases: a) The facet key "size" is not already in the top 8 slots, then the facet "size" will appear at a position close to 8. b) The facet key "size" in among the top 8 positions in the request, then it will stay at its current rank.




Protobuf type `google.cloud.retail.v2.Rule.ForceReturnFacetAction`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > Rule.ForceReturnFacetAction.Builder

## Implements

[Rule.ForceReturnFacetActionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetActionOrBuilder)

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

### addAllFacetPositionAdjustments(Iterable<? extends Rule.ForceReturnFacetAction.FacetPositionAdjustment> values)
    
    
    public Rule.ForceReturnFacetAction.Builder addAllFacetPositionAdjustments(Iterable<? extends Rule.ForceReturnFacetAction.FacetPositionAdjustment> values)

Each instance corresponds to a force return attribute for the given condition. There can't be more 15 instances here.

` repeated .google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment facet_position_adjustments = 1; `

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Rule.ForceReturnFacetAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.Builder)` |   
  
### addFacetPositionAdjustments(Rule.ForceReturnFacetAction.FacetPositionAdjustment value)
    
    
    public Rule.ForceReturnFacetAction.Builder addFacetPositionAdjustments(Rule.ForceReturnFacetAction.FacetPositionAdjustment value)

Each instance corresponds to a force return attribute for the given condition. There can't be more 15 instances here.

` repeated .google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment facet_position_adjustments = 1; `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Rule.ForceReturnFacetAction.FacetPositionAdjustment](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Rule.ForceReturnFacetAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.Builder)` |   
  
### addFacetPositionAdjustments(Rule.ForceReturnFacetAction.FacetPositionAdjustment.Builder builderForValue)
    
    
    public Rule.ForceReturnFacetAction.Builder addFacetPositionAdjustments(Rule.ForceReturnFacetAction.FacetPositionAdjustment.Builder builderForValue)

Each instance corresponds to a force return attribute for the given condition. There can't be more 15 instances here.

` repeated .google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment facet_position_adjustments = 1; `

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Rule.ForceReturnFacetAction.FacetPositionAdjustment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Rule.ForceReturnFacetAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.Builder)` |   
  
### addFacetPositionAdjustments(int index, Rule.ForceReturnFacetAction.FacetPositionAdjustment value)
    
    
    public Rule.ForceReturnFacetAction.Builder addFacetPositionAdjustments(int index, Rule.ForceReturnFacetAction.FacetPositionAdjustment value)

Each instance corresponds to a force return attribute for the given condition. There can't be more 15 instances here.

` repeated .google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment facet_position_adjustments = 1; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Rule.ForceReturnFacetAction.FacetPositionAdjustment](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Rule.ForceReturnFacetAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.Builder)` |   
  
### addFacetPositionAdjustments(int index, Rule.ForceReturnFacetAction.FacetPositionAdjustment.Builder builderForValue)
    
    
    public Rule.ForceReturnFacetAction.Builder addFacetPositionAdjustments(int index, Rule.ForceReturnFacetAction.FacetPositionAdjustment.Builder builderForValue)

Each instance corresponds to a force return attribute for the given condition. There can't be more 15 instances here.

` repeated .google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment facet_position_adjustments = 1; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Rule.ForceReturnFacetAction.FacetPositionAdjustment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Rule.ForceReturnFacetAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.Builder)` |   
  
### addFacetPositionAdjustmentsBuilder()
    
    
    public Rule.ForceReturnFacetAction.FacetPositionAdjustment.Builder addFacetPositionAdjustmentsBuilder()

Each instance corresponds to a force return attribute for the given condition. There can't be more 15 instances here.

` repeated .google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment facet_position_adjustments = 1; `

**Returns**  
---  
**Type** | **Description**  
`[Rule.ForceReturnFacetAction.FacetPositionAdjustment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment.Builder)` |   
  
### addFacetPositionAdjustmentsBuilder(int index)
    
    
    public Rule.ForceReturnFacetAction.FacetPositionAdjustment.Builder addFacetPositionAdjustmentsBuilder(int index)

Each instance corresponds to a force return attribute for the given condition. There can't be more 15 instances here.

` repeated .google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment facet_position_adjustments = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Rule.ForceReturnFacetAction.FacetPositionAdjustment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment.Builder)` |   
  
### build()
    
    
    public Rule.ForceReturnFacetAction build()

**Returns**  
---  
**Type** | **Description**  
`[Rule.ForceReturnFacetAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction)` |   
  
### buildPartial()
    
    
    public Rule.ForceReturnFacetAction buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[Rule.ForceReturnFacetAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction)` |   
  
### clear()
    
    
    public Rule.ForceReturnFacetAction.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[Rule.ForceReturnFacetAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearFacetPositionAdjustments()
    
    
    public Rule.ForceReturnFacetAction.Builder clearFacetPositionAdjustments()

Each instance corresponds to a force return attribute for the given condition. There can't be more 15 instances here.

` repeated .google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment facet_position_adjustments = 1; `

**Returns**  
---  
**Type** | **Description**  
`[Rule.ForceReturnFacetAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.Builder)` |   
  
### getDefaultInstanceForType()
    
    
    public Rule.ForceReturnFacetAction getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Rule.ForceReturnFacetAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getFacetPositionAdjustments(int index)
    
    
    public Rule.ForceReturnFacetAction.FacetPositionAdjustment getFacetPositionAdjustments(int index)

Each instance corresponds to a force return attribute for the given condition. There can't be more 15 instances here.

` repeated .google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment facet_position_adjustments = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Rule.ForceReturnFacetAction.FacetPositionAdjustment](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment)` |   
  
### getFacetPositionAdjustmentsBuilder(int index)
    
    
    public Rule.ForceReturnFacetAction.FacetPositionAdjustment.Builder getFacetPositionAdjustmentsBuilder(int index)

Each instance corresponds to a force return attribute for the given condition. There can't be more 15 instances here.

` repeated .google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment facet_position_adjustments = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Rule.ForceReturnFacetAction.FacetPositionAdjustment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment.Builder)` |   
  
### getFacetPositionAdjustmentsBuilderList()
    
    
    public List<Rule.ForceReturnFacetAction.FacetPositionAdjustment.Builder> getFacetPositionAdjustmentsBuilderList()

Each instance corresponds to a force return attribute for the given condition. There can't be more 15 instances here.

` repeated .google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment facet_position_adjustments = 1; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment.Builder)>` |   
  
### getFacetPositionAdjustmentsCount()
    
    
    public int getFacetPositionAdjustmentsCount()

Each instance corresponds to a force return attribute for the given condition. There can't be more 15 instances here.

` repeated .google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment facet_position_adjustments = 1; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getFacetPositionAdjustmentsList()
    
    
    public List<Rule.ForceReturnFacetAction.FacetPositionAdjustment> getFacetPositionAdjustmentsList()

Each instance corresponds to a force return attribute for the given condition. There can't be more 15 instances here.

` repeated .google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment facet_position_adjustments = 1; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[FacetPositionAdjustment](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment)>` |   
  
### getFacetPositionAdjustmentsOrBuilder(int index)
    
    
    public Rule.ForceReturnFacetAction.FacetPositionAdjustmentOrBuilder getFacetPositionAdjustmentsOrBuilder(int index)

Each instance corresponds to a force return attribute for the given condition. There can't be more 15 instances here.

` repeated .google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment facet_position_adjustments = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Rule.ForceReturnFacetAction.FacetPositionAdjustmentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustmentOrBuilder)` |   
  
### getFacetPositionAdjustmentsOrBuilderList()
    
    
    public List<? extends Rule.ForceReturnFacetAction.FacetPositionAdjustmentOrBuilder> getFacetPositionAdjustmentsOrBuilderList()

Each instance corresponds to a force return attribute for the given condition. There can't be more 15 instances here.

` repeated .google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment facet_position_adjustments = 1; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustmentOrBuilder>` |   
  
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

### mergeFrom(Rule.ForceReturnFacetAction other)
    
    
    public Rule.ForceReturnFacetAction.Builder mergeFrom(Rule.ForceReturnFacetAction other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Rule.ForceReturnFacetAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Rule.ForceReturnFacetAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public Rule.ForceReturnFacetAction.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Rule.ForceReturnFacetAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public Rule.ForceReturnFacetAction.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Rule.ForceReturnFacetAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### removeFacetPositionAdjustments(int index)
    
    
    public Rule.ForceReturnFacetAction.Builder removeFacetPositionAdjustments(int index)

Each instance corresponds to a force return attribute for the given condition. There can't be more 15 instances here.

` repeated .google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment facet_position_adjustments = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Rule.ForceReturnFacetAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.Builder)` |   
  
### setFacetPositionAdjustments(int index, Rule.ForceReturnFacetAction.FacetPositionAdjustment value)
    
    
    public Rule.ForceReturnFacetAction.Builder setFacetPositionAdjustments(int index, Rule.ForceReturnFacetAction.FacetPositionAdjustment value)

Each instance corresponds to a force return attribute for the given condition. There can't be more 15 instances here.

` repeated .google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment facet_position_adjustments = 1; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Rule.ForceReturnFacetAction.FacetPositionAdjustment](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Rule.ForceReturnFacetAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.Builder)` |   
  
### setFacetPositionAdjustments(int index, Rule.ForceReturnFacetAction.FacetPositionAdjustment.Builder builderForValue)
    
    
    public Rule.ForceReturnFacetAction.Builder setFacetPositionAdjustments(int index, Rule.ForceReturnFacetAction.FacetPositionAdjustment.Builder builderForValue)

Each instance corresponds to a force return attribute for the given condition. There can't be more 15 instances here.

` repeated .google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment facet_position_adjustments = 1; `

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Rule.ForceReturnFacetAction.FacetPositionAdjustment.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.FacetPositionAdjustment.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Rule.ForceReturnFacetAction.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-retail/latest/com.google.cloud.retail.v2.Rule.ForceReturnFacetAction.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
