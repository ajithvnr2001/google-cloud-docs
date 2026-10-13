---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-VodSession/
title: Video Stitcher V1 API - Class Google::Cloud::Video::Stitcher::V1::VodSession (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:40:41.255954+00:00
---

# Video Stitcher V1 API - Class Google::Cloud::Video::Stitcher::V1::VodSession (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-VodSession/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Video Stitcher V1 API - Class Google::Cloud::Video::Stitcher::V1::VodSession (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.0  0.8.2  0.7.0  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Video Stitcher V1 API class Google::Cloud::Video::Stitcher::V1::VodSession.

Metadata for a VOD session. The session expires 4 hours after its creation.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #ad_tag_macro_map
    
    
    def ad_tag_macro_map() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Key value pairs for ad tag macro replacement, only available for VOD sessions that do not implement Google Ad manager ad insertion. If the specified ad tag URI has macros, this field provides the mapping to the value that will replace the macro in the ad tag URI.

Macros are designated by square brackets, for example:

Ad tag URI: `"https://doubleclick.google.com/ad/1?geo_id=[geoId]"`

Ad tag macro map: `{"geoId": "123"}`

Fully qualified ad tag: `"https://doubleclick.google.com/ad/1?geo_id=123"`




### #ad_tag_macro_map=
    
    
    def ad_tag_macro_map=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Key value pairs for ad tag macro replacement, only available for VOD sessions that do not implement Google Ad manager ad insertion. If the specified ad tag URI has macros, this field provides the mapping to the value that will replace the macro in the ad tag URI.

Macros are designated by square brackets, for example:

Ad tag URI: `"https://doubleclick.google.com/ad/1?geo_id=[geoId]"`

Ad tag macro map: `{"geoId": "123"}`

Fully qualified ad tag: `"https://doubleclick.google.com/ad/1?geo_id=123"`




**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Key value pairs for ad tag macro replacement, only available for VOD sessions that do not implement Google Ad manager ad insertion. If the specified ad tag URI has macros, this field provides the mapping to the value that will replace the macro in the ad tag URI.

Macros are designated by square brackets, for example:

Ad tag URI: `"https://doubleclick.google.com/ad/1?geo_id=[geoId]"`

Ad tag macro map: `{"geoId": "123"}`

Fully qualified ad tag: `"https://doubleclick.google.com/ad/1?geo_id=123"`




### #ad_tag_uri
    
    
    def ad_tag_uri() -> ::String

**Returns**

  * (::String) — Ad tag URI. For most use cases, you should create a [VodConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-VodConfig "Google::Cloud::Video::Stitcher::V1::VodConfig \(class\)") with this information rather than setting this field directly. 



### #ad_tag_uri=
    
    
    def ad_tag_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — Ad tag URI. For most use cases, you should create a [VodConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-VodConfig "Google::Cloud::Video::Stitcher::V1::VodConfig \(class\)") with this information rather than setting this field directly. 



**Returns**

  * (::String) — Ad tag URI. For most use cases, you should create a [VodConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-VodConfig "Google::Cloud::Video::Stitcher::V1::VodConfig \(class\)") with this information rather than setting this field directly. 



### #ad_tracking
    
    
    def ad_tracking() -> ::Google::Cloud::Video::Stitcher::V1::AdTracking

**Returns**

  * ([::Google::Cloud::Video::Stitcher::V1::AdTracking](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-AdTracking)) — Required. Determines how the ad should be tracked. 



### #ad_tracking=
    
    
    def ad_tracking=(value) -> ::Google::Cloud::Video::Stitcher::V1::AdTracking

**Parameter**

  * **value** ([::Google::Cloud::Video::Stitcher::V1::AdTracking](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-AdTracking)) — Required. Determines how the ad should be tracked. 



**Returns**

  * ([::Google::Cloud::Video::Stitcher::V1::AdTracking](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-AdTracking)) — Required. Determines how the ad should be tracked. 



### #asset_id
    
    
    def asset_id() -> ::String

**Returns**

  * (::String) — Output only. The generated ID of the VodSession's source media. 



### #gam_settings
    
    
    def gam_settings() -> ::Google::Cloud::Video::Stitcher::V1::VodSession::GamSettings

**Returns**

  * ([::Google::Cloud::Video::Stitcher::V1::VodSession::GamSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-VodSession-GamSettings)) — This field should be set with appropriate values if GAM is being used for ads. 



### #gam_settings=
    
    
    def gam_settings=(value) -> ::Google::Cloud::Video::Stitcher::V1::VodSession::GamSettings

**Parameter**

  * **value** ([::Google::Cloud::Video::Stitcher::V1::VodSession::GamSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-VodSession-GamSettings)) — This field should be set with appropriate values if GAM is being used for ads. 



**Returns**

  * ([::Google::Cloud::Video::Stitcher::V1::VodSession::GamSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-VodSession-GamSettings)) — This field should be set with appropriate values if GAM is being used for ads. 



### #interstitials
    
    
    def interstitials() -> ::Google::Cloud::Video::Stitcher::V1::Interstitials

**Returns**

  * ([::Google::Cloud::Video::Stitcher::V1::Interstitials](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-Interstitials)) — Output only. Metadata of what was stitched into the content. 



### #manifest_options
    
    
    def manifest_options() -> ::Google::Cloud::Video::Stitcher::V1::ManifestOptions

**Returns**

  * ([::Google::Cloud::Video::Stitcher::V1::ManifestOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-ManifestOptions)) — Additional options that affect the output of the manifest. 



### #manifest_options=
    
    
    def manifest_options=(value) -> ::Google::Cloud::Video::Stitcher::V1::ManifestOptions

**Parameter**

  * **value** ([::Google::Cloud::Video::Stitcher::V1::ManifestOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-ManifestOptions)) — Additional options that affect the output of the manifest. 



**Returns**

  * ([::Google::Cloud::Video::Stitcher::V1::ManifestOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-ManifestOptions)) — Additional options that affect the output of the manifest. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. The name of the VOD session, in the form of `projects/{project_number}/locations/{location}/vodSessions/{id}`. 



### #play_uri
    
    
    def play_uri() -> ::String

**Returns**

  * (::String) — Output only. The playback URI of the stitched content. 



### #source_uri
    
    
    def source_uri() -> ::String

**Returns**

  * (::String) — URI of the media to stitch. For most use cases, you should create a [VodConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-VodConfig "Google::Cloud::Video::Stitcher::V1::VodConfig \(class\)") with this information rather than setting this field directly. 



### #source_uri=
    
    
    def source_uri=(value) -> ::String

**Parameter**

  * **value** (::String) — URI of the media to stitch. For most use cases, you should create a [VodConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-VodConfig "Google::Cloud::Video::Stitcher::V1::VodConfig \(class\)") with this information rather than setting this field directly. 



**Returns**

  * (::String) — URI of the media to stitch. For most use cases, you should create a [VodConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-VodConfig "Google::Cloud::Video::Stitcher::V1::VodConfig \(class\)") with this information rather than setting this field directly. 



### #vod_config
    
    
    def vod_config() -> ::String

**Returns**

  * (::String) — The resource name of the VOD config for this session, in the form of `projects/{project}/locations/{location}/vodConfigs/{id}`. 



### #vod_config=
    
    
    def vod_config=(value) -> ::String

**Parameter**

  * **value** (::String) — The resource name of the VOD config for this session, in the form of `projects/{project}/locations/{location}/vodConfigs/{id}`. 



**Returns**

  * (::String) — The resource name of the VOD config for this session, in the form of `projects/{project}/locations/{location}/vodConfigs/{id}`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
