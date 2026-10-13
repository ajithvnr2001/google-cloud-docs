---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfileOrBuilder
title: Interface DaiEncodingProfileOrBuilder (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:51:10.495751+00:00
---

# Interface DaiEncodingProfileOrBuilder (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfileOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DaiEncodingProfileOrBuilder (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface DaiEncodingProfileOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAudioSettings()
    
    
    public abstract AudioSettings getAudioSettings()

Optional. Information about the audio media, if present. This field will only be set if the media contains audio. Only MEDIA and IFRAME variant types can set audio.

` .google.ads.admanager.v1.AudioSettings audio_settings = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AudioSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AudioSettings)` | The audioSettings.  
  
### getAudioSettingsOrBuilder()
    
    
    public abstract AudioSettingsOrBuilder getAudioSettingsOrBuilder()

Optional. Information about the audio media, if present. This field will only be set if the media contains audio. Only MEDIA and IFRAME variant types can set audio.

` .google.ads.admanager.v1.AudioSettings audio_settings = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AudioSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.AudioSettingsOrBuilder)` |   
  
### getContainerType()
    
    
    public abstract ContainerTypeEnum.ContainerType getContainerType()

Required. The digital container type of the underlying media. This is required for MEDIA and IFRAME variant types.

` optional .google.ads.admanager.v1.ContainerTypeEnum.ContainerType container_type = 6 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ContainerTypeEnum.ContainerType](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.ContainerTypeEnum.ContainerType)` | The containerType.  
  
### getContainerTypeValue()
    
    
    public abstract int getContainerTypeValue()

Required. The digital container type of the underlying media. This is required for MEDIA and IFRAME variant types.

` optional .google.ads.admanager.v1.ContainerTypeEnum.ContainerType container_type = 6 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for containerType.  
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Required. The name of the DaiEncodingProfile. It may be at most 64 characters. The name field can contain alphanumeric characters and symbols other than the following: ", ', =, !, +, #, , ~, ;, ^, (, ), <, >, [, ], the white space character.

`optional string display_name = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Required. The name of the DaiEncodingProfile. It may be at most 64 characters. The name field can contain alphanumeric characters and symbols other than the following: ", ', =, !, +, #, , ~, ;, ^, (, ), <, >, [, ], the white space character.

`optional string display_name = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getName()
    
    
    public abstract String getName()

Identifier. The resource name of the `DaiEncodingProfile`. Format: `networks/{network_code}/daiEncodingProfiles/{dai_encoding_profile_id}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The resource name of the `DaiEncodingProfile`. Format: `networks/{network_code}/daiEncodingProfiles/{dai_encoding_profile_id}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getStatus()
    
    
    public abstract DaiEncodingProfileStatusEnum.DaiEncodingProfileStatus getStatus()

Output only. The status of this DaiEncodingProfile.

DAI encoding profiles are created in the [DaiEncodingProfileStatus.ACTIVE][] state by default.

Only active profiles will be allowed to be associated with live streams.

` optional .google.ads.admanager.v1.DaiEncodingProfileStatusEnum.DaiEncodingProfileStatus status = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[DaiEncodingProfileStatusEnum.DaiEncodingProfileStatus](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfileStatusEnum.DaiEncodingProfileStatus)` | The status.  
  
### getStatusValue()
    
    
    public abstract int getStatusValue()

Output only. The status of this DaiEncodingProfile.

DAI encoding profiles are created in the [DaiEncodingProfileStatus.ACTIVE][] state by default.

Only active profiles will be allowed to be associated with live streams.

` optional .google.ads.admanager.v1.DaiEncodingProfileStatusEnum.DaiEncodingProfileStatus status = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for status.  
  
### getVariantType()
    
    
    public abstract DaiEncodingProfileVariantTypeEnum.DaiEncodingProfileVariantType getVariantType()

Required. The variant playlist type that this DaiEncodingProfile represents.

` optional .google.ads.admanager.v1.DaiEncodingProfileVariantTypeEnum.DaiEncodingProfileVariantType variant_type = 5 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[DaiEncodingProfileVariantTypeEnum.DaiEncodingProfileVariantType](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.DaiEncodingProfileVariantTypeEnum.DaiEncodingProfileVariantType)` | The variantType.  
  
### getVariantTypeValue()
    
    
    public abstract int getVariantTypeValue()

Required. The variant playlist type that this DaiEncodingProfile represents.

` optional .google.ads.admanager.v1.DaiEncodingProfileVariantTypeEnum.DaiEncodingProfileVariantType variant_type = 5 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for variantType.  
  
### getVideoSettings()
    
    
    public abstract VideoSettings getVideoSettings()

Optional. Information about the video media, if present. This field will only be set if the media contains video, or is an IFRAME variant type.

` .google.ads.admanager.v1.VideoSettings video_settings = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[VideoSettings](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.VideoSettings)` | The videoSettings.  
  
### getVideoSettingsOrBuilder()
    
    
    public abstract VideoSettingsOrBuilder getVideoSettingsOrBuilder()

Optional. Information about the video media, if present. This field will only be set if the media contains video, or is an IFRAME variant type.

` .google.ads.admanager.v1.VideoSettings video_settings = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[VideoSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.VideoSettingsOrBuilder)` |   
  
### hasAudioSettings()
    
    
    public abstract boolean hasAudioSettings()

Optional. Information about the audio media, if present. This field will only be set if the media contains audio. Only MEDIA and IFRAME variant types can set audio.

` .google.ads.admanager.v1.AudioSettings audio_settings = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the audioSettings field is set.  
  
### hasContainerType()
    
    
    public abstract boolean hasContainerType()

Required. The digital container type of the underlying media. This is required for MEDIA and IFRAME variant types.

` optional .google.ads.admanager.v1.ContainerTypeEnum.ContainerType container_type = 6 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the containerType field is set.  
  
### hasDisplayName()
    
    
    public abstract boolean hasDisplayName()

Required. The name of the DaiEncodingProfile. It may be at most 64 characters. The name field can contain alphanumeric characters and symbols other than the following: ", ', =, !, +, #, , ~, ;, ^, (, ), <, >, [, ], the white space character.

`optional string display_name = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the displayName field is set.  
  
### hasStatus()
    
    
    public abstract boolean hasStatus()

Output only. The status of this DaiEncodingProfile.

DAI encoding profiles are created in the [DaiEncodingProfileStatus.ACTIVE][] state by default.

Only active profiles will be allowed to be associated with live streams.

` optional .google.ads.admanager.v1.DaiEncodingProfileStatusEnum.DaiEncodingProfileStatus status = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the status field is set.  
  
### hasVariantType()
    
    
    public abstract boolean hasVariantType()

Required. The variant playlist type that this DaiEncodingProfile represents.

` optional .google.ads.admanager.v1.DaiEncodingProfileVariantTypeEnum.DaiEncodingProfileVariantType variant_type = 5 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the variantType field is set.  
  
### hasVideoSettings()
    
    
    public abstract boolean hasVideoSettings()

Optional. Information about the video media, if present. This field will only be set if the media contains video, or is an IFRAME variant type.

` .google.ads.admanager.v1.VideoSettings video_settings = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the videoSettings field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
