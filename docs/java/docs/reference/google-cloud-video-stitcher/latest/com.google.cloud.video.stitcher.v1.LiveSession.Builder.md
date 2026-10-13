---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder
title: Class LiveSession.Builder (0.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:21:59.433489+00:00
---

# Class LiveSession.Builder (0.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LiveSession.Builder (0.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.99.0 (latest)  0.95.0  0.94.0  0.93.0  0.91.0  0.88.0  0.87.0  0.85.0  0.83.0  0.82.0  0.80.0  0.78.0  0.76.0  0.75.0  0.74.0  0.73.0  0.72.0  0.70.0  0.68.0  0.67.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.6  0.1.2 
    
    
    public static final class LiveSession.Builder extends GeneratedMessage.Builder<LiveSession.Builder> implements LiveSessionOrBuilder

Metadata for a live session. The session expires 5 minutes after the client stops fetching the session's playlists.

Protobuf type `google.cloud.video.stitcher.v1.LiveSession`

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractMessageLite.Builder<MessageType,BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessageLite.Builder.html) > [AbstractMessage.Builder<BuilderType>](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html) > [GeneratedMessage.Builder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html) > LiveSession.Builder

## Implements

[LiveSessionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSessionOrBuilder)

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
    
    
    public LiveSession build()

**Returns**  
---  
**Type** | **Description**  
`[LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession)` |   
  
### buildPartial()
    
    
    public LiveSession buildPartial()

**Returns**  
---  
**Type** | **Description**  
`[LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession)` |   
  
### clear()
    
    
    public LiveSession.Builder clear()

**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.clear()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_clear__)

### clearAdTagMacros()
    
    
    public LiveSession.Builder clearAdTagMacros()

**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` |   
  
### clearAdTracking()
    
    
    public LiveSession.Builder clearAdTracking()

Determines how the ad should be tracked. This overrides the value set in the live config for this session.

`.google.cloud.video.stitcher.v1.AdTracking ad_tracking = 17;`

**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` | This builder for chaining.  
  
### clearGamSettings()
    
    
    public LiveSession.Builder clearGamSettings()

This field should be set with appropriate values if GAM is being used for ads.

`.google.cloud.video.stitcher.v1.LiveSession.GamSettings gam_settings = 15;`

**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` |   
  
### clearLiveConfig()
    
    
    public LiveSession.Builder clearLiveConfig()

Required. The resource name of the live config for this session, in the form of `projects/{project}/locations/{location}/liveConfigs/{id}`.

` string live_config = 16 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` | This builder for chaining.  
  
### clearManifestOptions()
    
    
    public LiveSession.Builder clearManifestOptions()

Additional options that affect the output of the manifest.

`.google.cloud.video.stitcher.v1.ManifestOptions manifest_options = 10;`

**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` |   
  
### clearName()
    
    
    public LiveSession.Builder clearName()

Output only. The name of the live session, in the form of `projects/{project}/locations/{location}/liveSessions/{id}`.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` | This builder for chaining.  
  
### clearPlayUri()
    
    
    public LiveSession.Builder clearPlayUri()

Output only. The URI to play the live session's ad-stitched stream.

`string play_uri = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` | This builder for chaining.  
  
### containsAdTagMacros(String key)
    
    
    public boolean containsAdTagMacros(String key)

Key value pairs for ad tag macro replacement, only available for live sessions that do not implement Google Ad manager ad insertion. If the specified ad tag URI has macros, this field provides the mapping to the value that will replace the macro in the ad tag URI.

Macros are designated by square brackets, for example:

Ad tag URI: "https://doubleclick.google.com/ad/1?geo_id=[geoId]"

Ad tag macros: `{"geoId": "123"}`

Fully qualified ad tag: `"<https://doubleclick.google.com/ad/1?geo_id=123>"`

`map<string, string> ad_tag_macros = 6;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAdTagMacros() (deprecated)
    
    
    public Map<String,String> getAdTagMacros()

Use [#getAdTagMacrosMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder#com_google_cloud_video_stitcher_v1_LiveSession_Builder_getAdTagMacrosMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getAdTagMacrosCount()
    
    
    public int getAdTagMacrosCount()

Key value pairs for ad tag macro replacement, only available for live sessions that do not implement Google Ad manager ad insertion. If the specified ad tag URI has macros, this field provides the mapping to the value that will replace the macro in the ad tag URI.

Macros are designated by square brackets, for example:

Ad tag URI: "https://doubleclick.google.com/ad/1?geo_id=[geoId]"

Ad tag macros: `{"geoId": "123"}`

Fully qualified ad tag: `"<https://doubleclick.google.com/ad/1?geo_id=123>"`

`map<string, string> ad_tag_macros = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAdTagMacrosMap()
    
    
    public Map<String,String> getAdTagMacrosMap()

Key value pairs for ad tag macro replacement, only available for live sessions that do not implement Google Ad manager ad insertion. If the specified ad tag URI has macros, this field provides the mapping to the value that will replace the macro in the ad tag URI.

Macros are designated by square brackets, for example:

Ad tag URI: "https://doubleclick.google.com/ad/1?geo_id=[geoId]"

Ad tag macros: `{"geoId": "123"}`

Fully qualified ad tag: `"<https://doubleclick.google.com/ad/1?geo_id=123>"`

`map<string, string> ad_tag_macros = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getAdTagMacrosOrDefault(String key, String defaultValue)
    
    
    public String getAdTagMacrosOrDefault(String key, String defaultValue)

Key value pairs for ad tag macro replacement, only available for live sessions that do not implement Google Ad manager ad insertion. If the specified ad tag URI has macros, this field provides the mapping to the value that will replace the macro in the ad tag URI.

Macros are designated by square brackets, for example:

Ad tag URI: "https://doubleclick.google.com/ad/1?geo_id=[geoId]"

Ad tag macros: `{"geoId": "123"}`

Fully qualified ad tag: `"<https://doubleclick.google.com/ad/1?geo_id=123>"`

`map<string, string> ad_tag_macros = 6;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getAdTagMacrosOrThrow(String key)
    
    
    public String getAdTagMacrosOrThrow(String key)

Key value pairs for ad tag macro replacement, only available for live sessions that do not implement Google Ad manager ad insertion. If the specified ad tag URI has macros, this field provides the mapping to the value that will replace the macro in the ad tag URI.

Macros are designated by square brackets, for example:

Ad tag URI: "https://doubleclick.google.com/ad/1?geo_id=[geoId]"

Ad tag macros: `{"geoId": "123"}`

Fully qualified ad tag: `"<https://doubleclick.google.com/ad/1?geo_id=123>"`

`map<string, string> ad_tag_macros = 6;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getAdTracking()
    
    
    public AdTracking getAdTracking()

Determines how the ad should be tracked. This overrides the value set in the live config for this session.

`.google.cloud.video.stitcher.v1.AdTracking ad_tracking = 17;`

**Returns**  
---  
**Type** | **Description**  
`[AdTracking](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.AdTracking)` | The adTracking.  
  
### getAdTrackingValue()
    
    
    public int getAdTrackingValue()

Determines how the ad should be tracked. This overrides the value set in the live config for this session.

`.google.cloud.video.stitcher.v1.AdTracking ad_tracking = 17;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for adTracking.  
  
### getDefaultInstanceForType()
    
    
    public LiveSession getDefaultInstanceForType()

**Returns**  
---  
**Type** | **Description**  
`[LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession)` |   
  
### getDescriptorForType()
    
    
    public Descriptors.Descriptor getDescriptorForType()

**Returns**  
---  
**Type** | **Description**  
`[Descriptor](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.Descriptor.html)` |   
**Overrides**

[GeneratedMessage.Builder<BuilderType>.getDescriptorForType()](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.GeneratedMessage.Builder.html#com_google_protobuf_GeneratedMessage_Builder_getDescriptorForType__)

### getGamSettings()
    
    
    public LiveSession.GamSettings getGamSettings()

This field should be set with appropriate values if GAM is being used for ads.

`.google.cloud.video.stitcher.v1.LiveSession.GamSettings gam_settings = 15;`

**Returns**  
---  
**Type** | **Description**  
`[LiveSession.GamSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.GamSettings)` | The gamSettings.  
  
### getGamSettingsBuilder()
    
    
    public LiveSession.GamSettings.Builder getGamSettingsBuilder()

This field should be set with appropriate values if GAM is being used for ads.

`.google.cloud.video.stitcher.v1.LiveSession.GamSettings gam_settings = 15;`

**Returns**  
---  
**Type** | **Description**  
`[LiveSession.GamSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.GamSettings.Builder)` |   
  
### getGamSettingsOrBuilder()
    
    
    public LiveSession.GamSettingsOrBuilder getGamSettingsOrBuilder()

This field should be set with appropriate values if GAM is being used for ads.

`.google.cloud.video.stitcher.v1.LiveSession.GamSettings gam_settings = 15;`

**Returns**  
---  
**Type** | **Description**  
`[LiveSession.GamSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.GamSettingsOrBuilder)` |   
  
### getLiveConfig()
    
    
    public String getLiveConfig()

Required. The resource name of the live config for this session, in the form of `projects/{project}/locations/{location}/liveConfigs/{id}`.

` string live_config = 16 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The liveConfig.  
  
### getLiveConfigBytes()
    
    
    public ByteString getLiveConfigBytes()

Required. The resource name of the live config for this session, in the form of `projects/{project}/locations/{location}/liveConfigs/{id}`.

` string live_config = 16 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for liveConfig.  
  
### getManifestOptions()
    
    
    public ManifestOptions getManifestOptions()

Additional options that affect the output of the manifest.

`.google.cloud.video.stitcher.v1.ManifestOptions manifest_options = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ManifestOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ManifestOptions)` | The manifestOptions.  
  
### getManifestOptionsBuilder()
    
    
    public ManifestOptions.Builder getManifestOptionsBuilder()

Additional options that affect the output of the manifest.

`.google.cloud.video.stitcher.v1.ManifestOptions manifest_options = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ManifestOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ManifestOptions.Builder)` |   
  
### getManifestOptionsOrBuilder()
    
    
    public ManifestOptionsOrBuilder getManifestOptionsOrBuilder()

Additional options that affect the output of the manifest.

`.google.cloud.video.stitcher.v1.ManifestOptions manifest_options = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ManifestOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ManifestOptionsOrBuilder)` |   
  
### getMutableAdTagMacros() (deprecated)
    
    
    public Map<String,String> getMutableAdTagMacros()

Use alternate mutation accessors instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getName()
    
    
    public String getName()

Output only. The name of the live session, in the form of `projects/{project}/locations/{location}/liveSessions/{id}`.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public ByteString getNameBytes()

Output only. The name of the live session, in the form of `projects/{project}/locations/{location}/liveSessions/{id}`.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPlayUri()
    
    
    public String getPlayUri()

Output only. The URI to play the live session's ad-stitched stream.

`string play_uri = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The playUri.  
  
### getPlayUriBytes()
    
    
    public ByteString getPlayUriBytes()

Output only. The URI to play the live session's ad-stitched stream.

`string play_uri = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for playUri.  
  
### hasGamSettings()
    
    
    public boolean hasGamSettings()

This field should be set with appropriate values if GAM is being used for ads.

`.google.cloud.video.stitcher.v1.LiveSession.GamSettings gam_settings = 15;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the gamSettings field is set.  
  
### hasManifestOptions()
    
    
    public boolean hasManifestOptions()

Additional options that affect the output of the manifest.

`.google.cloud.video.stitcher.v1.ManifestOptions manifest_options = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the manifestOptions field is set.  
  
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

### mergeFrom(LiveSession other)
    
    
    public LiveSession.Builder mergeFrom(LiveSession other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[LiveSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` |   
  
### mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)
    
    
    public LiveSession.Builder mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)

**Parameters**  
---  
**Name** | **Description**  
`input` | `[CodedInputStream](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.CodedInputStream.html)`  
  
`extensionRegistry` | `[ExtensionRegistryLite](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ExtensionRegistryLite.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(CodedInputStream input, ExtensionRegistryLite extensionRegistry)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_CodedInputStream_com_google_protobuf_ExtensionRegistryLite_)

**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### mergeFrom(Message other)
    
    
    public LiveSession.Builder mergeFrom(Message other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Message](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Message.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` |   
**Overrides**

[AbstractMessage.Builder<BuilderType>.mergeFrom(Message other)](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AbstractMessage.Builder.html#com_google_protobuf_AbstractMessage_Builder_mergeFrom_com_google_protobuf_Message_)

### mergeGamSettings(LiveSession.GamSettings value)
    
    
    public LiveSession.Builder mergeGamSettings(LiveSession.GamSettings value)

This field should be set with appropriate values if GAM is being used for ads.

`.google.cloud.video.stitcher.v1.LiveSession.GamSettings gam_settings = 15;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[LiveSession.GamSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.GamSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` |   
  
### mergeManifestOptions(ManifestOptions value)
    
    
    public LiveSession.Builder mergeManifestOptions(ManifestOptions value)

Additional options that affect the output of the manifest.

`.google.cloud.video.stitcher.v1.ManifestOptions manifest_options = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ManifestOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ManifestOptions)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` |   
  
### putAdTagMacros(String key, String value)
    
    
    public LiveSession.Builder putAdTagMacros(String key, String value)

Key value pairs for ad tag macro replacement, only available for live sessions that do not implement Google Ad manager ad insertion. If the specified ad tag URI has macros, this field provides the mapping to the value that will replace the macro in the ad tag URI.

Macros are designated by square brackets, for example:

Ad tag URI: "https://doubleclick.google.com/ad/1?geo_id=[geoId]"

Ad tag macros: `{"geoId": "123"}`

Fully qualified ad tag: `"<https://doubleclick.google.com/ad/1?geo_id=123>"`

`map<string, string> ad_tag_macros = 6;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` |   
  
### putAllAdTagMacros(Map<String,String> values)
    
    
    public LiveSession.Builder putAllAdTagMacros(Map<String,String> values)

Key value pairs for ad tag macro replacement, only available for live sessions that do not implement Google Ad manager ad insertion. If the specified ad tag URI has macros, this field provides the mapping to the value that will replace the macro in the ad tag URI.

Macros are designated by square brackets, for example:

Ad tag URI: "https://doubleclick.google.com/ad/1?geo_id=[geoId]"

Ad tag macros: `{"geoId": "123"}`

Fully qualified ad tag: `"<https://doubleclick.google.com/ad/1?geo_id=123>"`

`map<string, string> ad_tag_macros = 6;`

**Parameter**  
---  
**Name** | **Description**  
`values` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` |   
  
### removeAdTagMacros(String key)
    
    
    public LiveSession.Builder removeAdTagMacros(String key)

Key value pairs for ad tag macro replacement, only available for live sessions that do not implement Google Ad manager ad insertion. If the specified ad tag URI has macros, this field provides the mapping to the value that will replace the macro in the ad tag URI.

Macros are designated by square brackets, for example:

Ad tag URI: "https://doubleclick.google.com/ad/1?geo_id=[geoId]"

Ad tag macros: `{"geoId": "123"}`

Fully qualified ad tag: `"<https://doubleclick.google.com/ad/1?geo_id=123>"`

`map<string, string> ad_tag_macros = 6;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` |   
  
### setAdTracking(AdTracking value)
    
    
    public LiveSession.Builder setAdTracking(AdTracking value)

Determines how the ad should be tracked. This overrides the value set in the live config for this session.

`.google.cloud.video.stitcher.v1.AdTracking ad_tracking = 17;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[AdTracking](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.AdTracking)`  
The adTracking to set.  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` | This builder for chaining.  
  
### setAdTrackingValue(int value)
    
    
    public LiveSession.Builder setAdTrackingValue(int value)

Determines how the ad should be tracked. This overrides the value set in the live config for this session.

`.google.cloud.video.stitcher.v1.AdTracking ad_tracking = 17;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The enum numeric value on the wire for adTracking to set.  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` | This builder for chaining.  
  
### setGamSettings(LiveSession.GamSettings value)
    
    
    public LiveSession.Builder setGamSettings(LiveSession.GamSettings value)

This field should be set with appropriate values if GAM is being used for ads.

`.google.cloud.video.stitcher.v1.LiveSession.GamSettings gam_settings = 15;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[LiveSession.GamSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.GamSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` |   
  
### setGamSettings(LiveSession.GamSettings.Builder builderForValue)
    
    
    public LiveSession.Builder setGamSettings(LiveSession.GamSettings.Builder builderForValue)

This field should be set with appropriate values if GAM is being used for ads.

`.google.cloud.video.stitcher.v1.LiveSession.GamSettings gam_settings = 15;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[LiveSession.GamSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.GamSettings.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` |   
  
### setLiveConfig(String value)
    
    
    public LiveSession.Builder setLiveConfig(String value)

Required. The resource name of the live config for this session, in the form of `projects/{project}/locations/{location}/liveConfigs/{id}`.

` string live_config = 16 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The liveConfig to set.  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` | This builder for chaining.  
  
### setLiveConfigBytes(ByteString value)
    
    
    public LiveSession.Builder setLiveConfigBytes(ByteString value)

Required. The resource name of the live config for this session, in the form of `projects/{project}/locations/{location}/liveConfigs/{id}`.

` string live_config = 16 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for liveConfig to set.  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` | This builder for chaining.  
  
### setManifestOptions(ManifestOptions value)
    
    
    public LiveSession.Builder setManifestOptions(ManifestOptions value)

Additional options that affect the output of the manifest.

`.google.cloud.video.stitcher.v1.ManifestOptions manifest_options = 10;`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ManifestOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ManifestOptions)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` |   
  
### setManifestOptions(ManifestOptions.Builder builderForValue)
    
    
    public LiveSession.Builder setManifestOptions(ManifestOptions.Builder builderForValue)

Additional options that affect the output of the manifest.

`.google.cloud.video.stitcher.v1.ManifestOptions manifest_options = 10;`

**Parameter**  
---  
**Name** | **Description**  
`builderForValue` | `[ManifestOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.ManifestOptions.Builder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` |   
  
### setName(String value)
    
    
    public LiveSession.Builder setName(String value)

Output only. The name of the live session, in the form of `projects/{project}/locations/{location}/liveSessions/{id}`.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The name to set.  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` | This builder for chaining.  
  
### setNameBytes(ByteString value)
    
    
    public LiveSession.Builder setNameBytes(ByteString value)

Output only. The name of the live session, in the form of `projects/{project}/locations/{location}/liveSessions/{id}`.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for name to set.  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` | This builder for chaining.  
  
### setPlayUri(String value)
    
    
    public LiveSession.Builder setPlayUri(String value)

Output only. The URI to play the live session's ad-stitched stream.

`string play_uri = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The playUri to set.  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` | This builder for chaining.  
  
### setPlayUriBytes(ByteString value)
    
    
    public LiveSession.Builder setPlayUriBytes(ByteString value)

Output only. The URI to play the live session's ad-stitched stream.

`string play_uri = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)`  
The bytes for playUri to set.  
**Returns**  
---  
**Type** | **Description**  
`[LiveSession.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LiveSession.Builder)` | This builder for chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
