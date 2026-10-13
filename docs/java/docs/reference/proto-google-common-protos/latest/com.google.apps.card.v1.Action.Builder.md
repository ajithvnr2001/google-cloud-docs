---
url: https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder
title: Class Action.Builder (2.78.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:47.011047+00:00
---

# Class Action.Builder (2.78.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Action.Builder (2.78.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.78.0 (latest)  2.74.0  2.73.0  2.72.0  2.70.0  2.67.0  2.66.0  2.65.1  2.64.1  2.63.2  2.62.0  2.61.3  2.60.0  2.59.2  2.58.0  2.57.0  2.56.0  2.54.1  2.53.0  2.52.0  2.51.0  2.50.1  2.49.0  2.48.0  2.46.0  2.45.1  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.1  2.38.0  2.37.1  2.36.0  2.34.0  2.33.0  2.32.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.1  2.22.1  2.21.1  2.15.0  2.14.3  2.13.0  2.12.0  2.11.0  2.10.0  2.9.6  2.8.4  2.7.4 
    
    
    public static final class Action.Builder extends GeneratedMessage.Builder<Action.Builder> implements ActionOrBuilder

An action that describes the behavior when the form is submitted. For example, you can invoke an Apps Script script to handle the form. If the action is triggered, the form values are sent to the server.

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

Protobuf type `google.apps.card.v1.Action`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > Action.Builder

## Implements

[ActionOrBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.ActionOrBuilder)

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

### addAllParameters(Iterable<? extends Action.ActionParameter> values)
    
    
    public Action.Builder addAllParameters(Iterable<? extends Action.ActionParameter> values)

List of action parameters.

`repeated .google.apps.card.v1.Action.ActionParameter parameters = 2;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<? extends com.google.apps.card.v1.Action.ActionParameter>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` |   
  
### addAllRequiredWidgets(Iterable<String> values)
    
    
    public Action.Builder addAllRequiredWidgets(Iterable<String> values)

Optional. Fill this list with the names of widgets that this Action needs for a valid submission.

If the widgets listed here don't have a value when this Action is invoked, the form submission is aborted.

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

`repeated string required_widgets = 6;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The requiredWidgets to add.  
**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` | This builder for chaining.  
  
### addParameters(Action.ActionParameter value)
    
    
    public Action.Builder addParameters(Action.ActionParameter value)

List of action parameters.

`repeated .google.apps.card.v1.Action.ActionParameter parameters = 2;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Action.ActionParameter](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.ActionParameter)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` |   
  
### addParameters(Action.ActionParameter.Builder builderForValue)
    
    
    public Action.Builder addParameters(Action.ActionParameter.Builder builderForValue)

List of action parameters.

`repeated .google.apps.card.v1.Action.ActionParameter parameters = 2;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[Action.ActionParameter.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.ActionParameter.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` |   
  
### addParameters(int index, Action.ActionParameter value)
    
    
    public Action.Builder addParameters(int index, Action.ActionParameter value)

List of action parameters.

`repeated .google.apps.card.v1.Action.ActionParameter parameters = 2;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Action.ActionParameter](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.ActionParameter)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` |   
  
### addParameters(int index, Action.ActionParameter.Builder builderForValue)
    
    
    public Action.Builder addParameters(int index, Action.ActionParameter.Builder builderForValue)

List of action parameters.

`repeated .google.apps.card.v1.Action.ActionParameter parameters = 2;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Action.ActionParameter.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.ActionParameter.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` |   
  
### addParametersBuilder()
    
    
    public Action.ActionParameter.Builder addParametersBuilder()

List of action parameters.

`repeated .google.apps.card.v1.Action.ActionParameter parameters = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Action.ActionParameter.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.ActionParameter.Builder)` |   
  
### addParametersBuilder(int index)
    
    
    public Action.ActionParameter.Builder addParametersBuilder(int index)

List of action parameters.

`repeated .google.apps.card.v1.Action.ActionParameter parameters = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.ActionParameter.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.ActionParameter.Builder)` |   
  
### addRequiredWidgets(String value)
    
    
    public Action.Builder addRequiredWidgets(String value)

Optional. Fill this list with the names of widgets that this Action needs for a valid submission.

If the widgets listed here don't have a value when this Action is invoked, the form submission is aborted.

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

`repeated string required_widgets = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The requiredWidgets to add.  
**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` | This builder for chaining.  
  
### addRequiredWidgetsBytes(ByteString value)
    
    
    public Action.Builder addRequiredWidgetsBytes(ByteString value)

Optional. Fill this list with the names of widgets that this Action needs for a valid submission.

If the widgets listed here don't have a value when this Action is invoked, the form submission is aborted.

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

`repeated string required_widgets = 6;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes of the requiredWidgets to add.  
**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` | This builder for chaining.  
  
### build()
    
    
    public Action build()

**Returns**  
---  
**Type** | **Description**  
`[Action](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action)` |   
  
### buildPartial()
    
    
    public Action buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[Action](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action)` |   
  
### clear()
    
    
    public Action.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearAllWidgetsAreRequired()
    
    
    public Action.Builder clearAllWidgetsAreRequired()

Optional. If this is true, then all widgets are considered required by this action.

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

`bool all_widgets_are_required = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` | This builder for chaining.  
  
### clearFunction()
    
    
    public Action.Builder clearFunction()

A custom function to invoke when the containing element is clicked or otherwise activated.

For example usage, see [Read form data](https://developers.google.com/workspace/chat/read-form-data).

`string function = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` | This builder for chaining.  
  
### clearInteraction()
    
    
    public Action.Builder clearInteraction()

Optional. Required when opening a [dialog](https://developers.google.com/workspace/chat/dialogs).

What to do in response to an interaction with a user, such as a user clicking a button in a card message.

If unspecified, the app responds by executing an `action`—like opening a link or running a function—as normal.

By specifying an `interaction`, the app can respond in special interactive ways. For example, by setting `interaction` to `OPEN_DIALOG`, the app can open a [dialog](https://developers.google.com/workspace/chat/dialogs). When specified, a loading indicator isn't shown. If specified for an add-on, the entire card is stripped and nothing is shown in the client.

[Google Chat apps](https://developers.google.com/workspace/chat):

`.google.apps.card.v1.Action.Interaction interaction = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` | This builder for chaining.  
  
### clearLoadIndicator()
    
    
    public Action.Builder clearLoadIndicator()

Specifies the loading indicator that the action displays while making the call to the action.

`.google.apps.card.v1.Action.LoadIndicator load_indicator = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` | This builder for chaining.  
  
### clearParameters()
    
    
    public Action.Builder clearParameters()

List of action parameters.

`repeated .google.apps.card.v1.Action.ActionParameter parameters = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` |   
  
### clearPersistValues()
    
    
    public Action.Builder clearPersistValues()

Indicates whether form values persist after the action. The default value is `false`.

If `true`, form values remain after the action is triggered. To let the user make changes while the action is being processed, set [`LoadIndicator`](https://developers.google.com/workspace/add-ons/reference/rpc/google.apps.card.v1#loadindicator) to `NONE`. For [card messages](https://developers.google.com/workspace/chat/api/guides/v1/messages/create#create) in Chat apps, you must also set the action's [`ResponseType`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages#responsetype) to `UPDATE_MESSAGE` and use the same [`card_id`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages#CardWithId) from the card that contained the action.

If `false`, the form values are cleared when the action is triggered. To prevent the user from making changes while the action is being processed, set [`LoadIndicator`](https://developers.google.com/workspace/add-ons/reference/rpc/google.apps.card.v1#loadindicator) to `SPINNER`.

`bool persist_values = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` | This builder for chaining.  
  
### clearRequiredWidgets()
    
    
    public Action.Builder clearRequiredWidgets()

Optional. Fill this list with the names of widgets that this Action needs for a valid submission.

If the widgets listed here don't have a value when this Action is invoked, the form submission is aborted.

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

`repeated string required_widgets = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` | This builder for chaining.  
  
### getAllWidgetsAreRequired()
    
    
    public boolean getAllWidgetsAreRequired()

Optional. If this is true, then all widgets are considered required by this action.

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

`bool all_widgets_are_required = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The allWidgetsAreRequired.  
  
### getDefaultInstanceForType()
    
    
    public Action getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[Action](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getFunction()
    
    
    public String getFunction()

A custom function to invoke when the containing element is clicked or otherwise activated.

For example usage, see [Read form data](https://developers.google.com/workspace/chat/read-form-data).

`string function = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The function.  
  
### getFunctionBytes()
    
    
    public ByteString getFunctionBytes()

A custom function to invoke when the containing element is clicked or otherwise activated.

For example usage, see [Read form data](https://developers.google.com/workspace/chat/read-form-data).

`string function = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for function.  
  
### getInteraction()
    
    
    public Action.Interaction getInteraction()

Optional. Required when opening a [dialog](https://developers.google.com/workspace/chat/dialogs).

What to do in response to an interaction with a user, such as a user clicking a button in a card message.

If unspecified, the app responds by executing an `action`—like opening a link or running a function—as normal.

By specifying an `interaction`, the app can respond in special interactive ways. For example, by setting `interaction` to `OPEN_DIALOG`, the app can open a [dialog](https://developers.google.com/workspace/chat/dialogs). When specified, a loading indicator isn't shown. If specified for an add-on, the entire card is stripped and nothing is shown in the client.

[Google Chat apps](https://developers.google.com/workspace/chat):

`.google.apps.card.v1.Action.Interaction interaction = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Action.Interaction](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Interaction)` | The interaction.  
  
### getInteractionValue()
    
    
    public int getInteractionValue()

Optional. Required when opening a [dialog](https://developers.google.com/workspace/chat/dialogs).

What to do in response to an interaction with a user, such as a user clicking a button in a card message.

If unspecified, the app responds by executing an `action`—like opening a link or running a function—as normal.

By specifying an `interaction`, the app can respond in special interactive ways. For example, by setting `interaction` to `OPEN_DIALOG`, the app can open a [dialog](https://developers.google.com/workspace/chat/dialogs). When specified, a loading indicator isn't shown. If specified for an add-on, the entire card is stripped and nothing is shown in the client.

[Google Chat apps](https://developers.google.com/workspace/chat):

`.google.apps.card.v1.Action.Interaction interaction = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for interaction.  
  
### getLoadIndicator()
    
    
    public Action.LoadIndicator getLoadIndicator()

Specifies the loading indicator that the action displays while making the call to the action.

`.google.apps.card.v1.Action.LoadIndicator load_indicator = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Action.LoadIndicator](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.LoadIndicator)` | The loadIndicator.  
  
### getLoadIndicatorValue()
    
    
    public int getLoadIndicatorValue()

Specifies the loading indicator that the action displays while making the call to the action.

`.google.apps.card.v1.Action.LoadIndicator load_indicator = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for loadIndicator.  
  
### getParameters(int index)
    
    
    public Action.ActionParameter getParameters(int index)

List of action parameters.

`repeated .google.apps.card.v1.Action.ActionParameter parameters = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.ActionParameter](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.ActionParameter)` |   
  
### getParametersBuilder(int index)
    
    
    public Action.ActionParameter.Builder getParametersBuilder(int index)

List of action parameters.

`repeated .google.apps.card.v1.Action.ActionParameter parameters = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.ActionParameter.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.ActionParameter.Builder)` |   
  
### getParametersBuilderList()
    
    
    public List<Action.ActionParameter.Builder> getParametersBuilderList()

List of action parameters.

`repeated .google.apps.card.v1.Action.ActionParameter parameters = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.ActionParameter.Builder)>` |   
  
### getParametersCount()
    
    
    public int getParametersCount()

List of action parameters.

`repeated .google.apps.card.v1.Action.ActionParameter parameters = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getParametersList()
    
    
    public List<Action.ActionParameter> getParametersList()

List of action parameters.

`repeated .google.apps.card.v1.Action.ActionParameter parameters = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ActionParameter](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.ActionParameter)>` |   
  
### getParametersOrBuilder(int index)
    
    
    public Action.ActionParameterOrBuilder getParametersOrBuilder(int index)

List of action parameters.

`repeated .google.apps.card.v1.Action.ActionParameter parameters = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.ActionParameterOrBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.ActionParameterOrBuilder)` |   
  
### getParametersOrBuilderList()
    
    
    public List<? extends Action.ActionParameterOrBuilder> getParametersOrBuilderList()

List of action parameters.

`repeated .google.apps.card.v1.Action.ActionParameter parameters = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.apps.card.v1.Action.ActionParameterOrBuilder>` |   
  
### getPersistValues()
    
    
    public boolean getPersistValues()

Indicates whether form values persist after the action. The default value is `false`.

If `true`, form values remain after the action is triggered. To let the user make changes while the action is being processed, set [`LoadIndicator`](https://developers.google.com/workspace/add-ons/reference/rpc/google.apps.card.v1#loadindicator) to `NONE`. For [card messages](https://developers.google.com/workspace/chat/api/guides/v1/messages/create#create) in Chat apps, you must also set the action's [`ResponseType`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages#responsetype) to `UPDATE_MESSAGE` and use the same [`card_id`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages#CardWithId) from the card that contained the action.

If `false`, the form values are cleared when the action is triggered. To prevent the user from making changes while the action is being processed, set [`LoadIndicator`](https://developers.google.com/workspace/add-ons/reference/rpc/google.apps.card.v1#loadindicator) to `SPINNER`.

`bool persist_values = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The persistValues.  
  
### getRequiredWidgets(int index)
    
    
    public String getRequiredWidgets(int index)

Optional. Fill this list with the names of widgets that this Action needs for a valid submission.

If the widgets listed here don't have a value when this Action is invoked, the form submission is aborted.

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

`repeated string required_widgets = 6;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The requiredWidgets at the given index.  
  
### getRequiredWidgetsBytes(int index)
    
    
    public ByteString getRequiredWidgetsBytes(int index)

Optional. Fill this list with the names of widgets that this Action needs for a valid submission.

If the widgets listed here don't have a value when this Action is invoked, the form submission is aborted.

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

`repeated string required_widgets = 6;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the requiredWidgets at the given index.  
  
### getRequiredWidgetsCount()
    
    
    public int getRequiredWidgetsCount()

Optional. Fill this list with the names of widgets that this Action needs for a valid submission.

If the widgets listed here don't have a value when this Action is invoked, the form submission is aborted.

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

`repeated string required_widgets = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of requiredWidgets.  
  
### getRequiredWidgetsList()
    
    
    public ProtocolStringList getRequiredWidgetsList()

Optional. Fill this list with the names of widgets that this Action needs for a valid submission.

If the widgets listed here don't have a value when this Action is invoked, the form submission is aborted.

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

`repeated string required_widgets = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ProtocolStringList](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ProtocolStringList.html)` | A list containing the requiredWidgets.  
  
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

### mergeFrom(Action other)
    
    
    public Action.Builder mergeFrom(Action other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Action](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public Action.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public Action.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### removeParameters(int index)
    
    
    public Action.Builder removeParameters(int index)

List of action parameters.

`repeated .google.apps.card.v1.Action.ActionParameter parameters = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` |   
  
### setAllWidgetsAreRequired(boolean value)
    
    
    public Action.Builder setAllWidgetsAreRequired(boolean value)

Optional. If this is true, then all widgets are considered required by this action.

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

`bool all_widgets_are_required = 7;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The allWidgetsAreRequired to set.  
**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` | This builder for chaining.  
  
### setFunction(String value)
    
    
    public Action.Builder setFunction(String value)

A custom function to invoke when the containing element is clicked or otherwise activated.

For example usage, see [Read form data](https://developers.google.com/workspace/chat/read-form-data).

`string function = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The function to set.  
**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` | This builder for chaining.  
  
### setFunctionBytes(ByteString value)
    
    
    public Action.Builder setFunctionBytes(ByteString value)

A custom function to invoke when the containing element is clicked or otherwise activated.

For example usage, see [Read form data](https://developers.google.com/workspace/chat/read-form-data).

`string function = 1;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for function to set.  
**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` | This builder for chaining.  
  
### setInteraction(Action.Interaction value)
    
    
    public Action.Builder setInteraction(Action.Interaction value)

Optional. Required when opening a [dialog](https://developers.google.com/workspace/chat/dialogs).

What to do in response to an interaction with a user, such as a user clicking a button in a card message.

If unspecified, the app responds by executing an `action`—like opening a link or running a function—as normal.

By specifying an `interaction`, the app can respond in special interactive ways. For example, by setting `interaction` to `OPEN_DIALOG`, the app can open a [dialog](https://developers.google.com/workspace/chat/dialogs). When specified, a loading indicator isn't shown. If specified for an add-on, the entire card is stripped and nothing is shown in the client.

[Google Chat apps](https://developers.google.com/workspace/chat):

`.google.apps.card.v1.Action.Interaction interaction = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Action.Interaction](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Interaction)`  
The interaction to set.  
**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` | This builder for chaining.  
  
### setInteractionValue(int value)
    
    
    public Action.Builder setInteractionValue(int value)

Optional. Required when opening a [dialog](https://developers.google.com/workspace/chat/dialogs).

What to do in response to an interaction with a user, such as a user clicking a button in a card message.

If unspecified, the app responds by executing an `action`—like opening a link or running a function—as normal.

By specifying an `interaction`, the app can respond in special interactive ways. For example, by setting `interaction` to `OPEN_DIALOG`, the app can open a [dialog](https://developers.google.com/workspace/chat/dialogs). When specified, a loading indicator isn't shown. If specified for an add-on, the entire card is stripped and nothing is shown in the client.

[Google Chat apps](https://developers.google.com/workspace/chat):

`.google.apps.card.v1.Action.Interaction interaction = 5;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for interaction to set.  
**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` | This builder for chaining.  
  
### setLoadIndicator(Action.LoadIndicator value)
    
    
    public Action.Builder setLoadIndicator(Action.LoadIndicator value)

Specifies the loading indicator that the action displays while making the call to the action.

`.google.apps.card.v1.Action.LoadIndicator load_indicator = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[Action.LoadIndicator](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.LoadIndicator)`  
The loadIndicator to set.  
**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` | This builder for chaining.  
  
### setLoadIndicatorValue(int value)
    
    
    public Action.Builder setLoadIndicatorValue(int value)

Specifies the loading indicator that the action displays while making the call to the action.

`.google.apps.card.v1.Action.LoadIndicator load_indicator = 3;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for loadIndicator to set.  
**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` | This builder for chaining.  
  
### setParameters(int index, Action.ActionParameter value)
    
    
    public Action.Builder setParameters(int index, Action.ActionParameter value)

List of action parameters.

`repeated .google.apps.card.v1.Action.ActionParameter parameters = 2;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`value` | `[Action.ActionParameter](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.ActionParameter)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` |   
  
### setParameters(int index, Action.ActionParameter.Builder builderForValue)
    
    
    public Action.Builder setParameters(int index, Action.ActionParameter.Builder builderForValue)

List of action parameters.

`repeated .google.apps.card.v1.Action.ActionParameter parameters = 2;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`builderForValue` | `[Action.ActionParameter.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.ActionParameter.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` |   
  
### setPersistValues(boolean value)
    
    
    public Action.Builder setPersistValues(boolean value)

Indicates whether form values persist after the action. The default value is `false`.

If `true`, form values remain after the action is triggered. To let the user make changes while the action is being processed, set [`LoadIndicator`](https://developers.google.com/workspace/add-ons/reference/rpc/google.apps.card.v1#loadindicator) to `NONE`. For [card messages](https://developers.google.com/workspace/chat/api/guides/v1/messages/create#create) in Chat apps, you must also set the action's [`ResponseType`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages#responsetype) to `UPDATE_MESSAGE` and use the same [`card_id`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.messages#CardWithId) from the card that contained the action.

If `false`, the form values are cleared when the action is triggered. To prevent the user from making changes while the action is being processed, set [`LoadIndicator`](https://developers.google.com/workspace/add-ons/reference/rpc/google.apps.card.v1#loadindicator) to `SPINNER`.

`bool persist_values = 4;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The persistValues to set.  
**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` | This builder for chaining.  
  
### setRequiredWidgets(int index, String value)
    
    
    public Action.Builder setRequiredWidgets(int index, String value)

Optional. Fill this list with the names of widgets that this Action needs for a valid submission.

If the widgets listed here don't have a value when this Action is invoked, the form submission is aborted.

[Google Workspace add-ons and Chat apps](https://developers.google.com/workspace/extend):

`repeated string required_widgets = 6;`

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index to set the value at.  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The requiredWidgets to set.  
**Returns**  
---  
**Type** | **Description**  
`[Action.Builder](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.apps.card.v1.Action.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
