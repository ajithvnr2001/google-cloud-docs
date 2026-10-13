---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-Companion/
title: Video Stitcher V1 API - Class Google::Cloud::Video::Stitcher::V1::Companion (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:53:30.788937+00:00
---

# Video Stitcher V1 API - Class Google::Cloud::Video::Stitcher::V1::Companion (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-Companion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Video Stitcher V1 API - Class Google::Cloud::Video::Stitcher::V1::Companion (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.0  0.8.2  0.7.0  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Video Stitcher V1 API class Google::Cloud::Video::Stitcher::V1::Companion.

Metadata for a companion.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #ad_slot_id
    
    
    def ad_slot_id() -> ::String

**Returns**

  * (::String) — The ID used to identify the desired placement on a publisher's page. Values to be used should be discussed between publishers and advertisers. 



### #ad_slot_id=
    
    
    def ad_slot_id=(value) -> ::String

**Parameter**

  * **value** (::String) — The ID used to identify the desired placement on a publisher's page. Values to be used should be discussed between publishers and advertisers. 



**Returns**

  * (::String) — The ID used to identify the desired placement on a publisher's page. Values to be used should be discussed between publishers and advertisers. 



### #api_framework
    
    
    def api_framework() -> ::String

**Returns**

  * (::String) — The API necessary to communicate with the creative if available. 



### #api_framework=
    
    
    def api_framework=(value) -> ::String

**Parameter**

  * **value** (::String) — The API necessary to communicate with the creative if available. 



**Returns**

  * (::String) — The API necessary to communicate with the creative if available. 



### #asset_height_px
    
    
    def asset_height_px() -> ::Integer

**Returns**

  * (::Integer) — The pixel height of the creative. 



### #asset_height_px=
    
    
    def asset_height_px=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The pixel height of the creative. 



**Returns**

  * (::Integer) — The pixel height of the creative. 



### #asset_width_px
    
    
    def asset_width_px() -> ::Integer

**Returns**

  * (::Integer) — The pixel width of the creative. 



### #asset_width_px=
    
    
    def asset_width_px=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The pixel width of the creative. 



**Returns**

  * (::Integer) — The pixel width of the creative. 



### #events
    
    
    def events() -> ::Array<::Google::Cloud::Video::Stitcher::V1::Event>

**Returns**

  * (::Array<[::Google::Cloud::Video::Stitcher::V1::Event](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-Event)>) — The list of tracking events for the companion. 



### #events=
    
    
    def events=(value) -> ::Array<::Google::Cloud::Video::Stitcher::V1::Event>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Video::Stitcher::V1::Event](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-Event)>) — The list of tracking events for the companion. 



**Returns**

  * (::Array<[::Google::Cloud::Video::Stitcher::V1::Event](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-Event)>) — The list of tracking events for the companion. 



### #expanded_height_px
    
    
    def expanded_height_px() -> ::Integer

**Returns**

  * (::Integer) — The maximum pixel height of the creative in its expanded state. 



### #expanded_height_px=
    
    
    def expanded_height_px=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum pixel height of the creative in its expanded state. 



**Returns**

  * (::Integer) — The maximum pixel height of the creative in its expanded state. 



### #expanded_width_px
    
    
    def expanded_width_px() -> ::Integer

**Returns**

  * (::Integer) — The maximum pixel width of the creative in its expanded state. 



### #expanded_width_px=
    
    
    def expanded_width_px=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum pixel width of the creative in its expanded state. 



**Returns**

  * (::Integer) — The maximum pixel width of the creative in its expanded state. 



### #height_px
    
    
    def height_px() -> ::Integer

**Returns**

  * (::Integer) — The pixel height of the placement slot for the intended creative. 



### #height_px=
    
    
    def height_px=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The pixel height of the placement slot for the intended creative. 



**Returns**

  * (::Integer) — The pixel height of the placement slot for the intended creative. 



### #html_ad_resource
    
    
    def html_ad_resource() -> ::Google::Cloud::Video::Stitcher::V1::HtmlAdResource

**Returns**

  * ([::Google::Cloud::Video::Stitcher::V1::HtmlAdResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-HtmlAdResource)) — The HTML ad resource associated with the companion ad.

Note: The following fields are mutually exclusive: `html_ad_resource`, `iframe_ad_resource`, `static_ad_resource`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #html_ad_resource=
    
    
    def html_ad_resource=(value) -> ::Google::Cloud::Video::Stitcher::V1::HtmlAdResource

**Parameter**

  * **value** ([::Google::Cloud::Video::Stitcher::V1::HtmlAdResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-HtmlAdResource)) — The HTML ad resource associated with the companion ad.

Note: The following fields are mutually exclusive: `html_ad_resource`, `iframe_ad_resource`, `static_ad_resource`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Video::Stitcher::V1::HtmlAdResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-HtmlAdResource)) — The HTML ad resource associated with the companion ad.

Note: The following fields are mutually exclusive: `html_ad_resource`, `iframe_ad_resource`, `static_ad_resource`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #iframe_ad_resource
    
    
    def iframe_ad_resource() -> ::Google::Cloud::Video::Stitcher::V1::IframeAdResource

**Returns**

  * ([::Google::Cloud::Video::Stitcher::V1::IframeAdResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-IframeAdResource)) — The IFrame ad resource associated with the companion ad.

Note: The following fields are mutually exclusive: `iframe_ad_resource`, `static_ad_resource`, `html_ad_resource`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #iframe_ad_resource=
    
    
    def iframe_ad_resource=(value) -> ::Google::Cloud::Video::Stitcher::V1::IframeAdResource

**Parameter**

  * **value** ([::Google::Cloud::Video::Stitcher::V1::IframeAdResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-IframeAdResource)) — The IFrame ad resource associated with the companion ad.

Note: The following fields are mutually exclusive: `iframe_ad_resource`, `static_ad_resource`, `html_ad_resource`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Video::Stitcher::V1::IframeAdResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-IframeAdResource)) — The IFrame ad resource associated with the companion ad.

Note: The following fields are mutually exclusive: `iframe_ad_resource`, `static_ad_resource`, `html_ad_resource`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #static_ad_resource
    
    
    def static_ad_resource() -> ::Google::Cloud::Video::Stitcher::V1::StaticAdResource

**Returns**

  * ([::Google::Cloud::Video::Stitcher::V1::StaticAdResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-StaticAdResource)) — The static ad resource associated with the companion ad.

Note: The following fields are mutually exclusive: `static_ad_resource`, `iframe_ad_resource`, `html_ad_resource`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #static_ad_resource=
    
    
    def static_ad_resource=(value) -> ::Google::Cloud::Video::Stitcher::V1::StaticAdResource

**Parameter**

  * **value** ([::Google::Cloud::Video::Stitcher::V1::StaticAdResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-StaticAdResource)) — The static ad resource associated with the companion ad.

Note: The following fields are mutually exclusive: `static_ad_resource`, `iframe_ad_resource`, `html_ad_resource`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Video::Stitcher::V1::StaticAdResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-StaticAdResource)) — The static ad resource associated with the companion ad.

Note: The following fields are mutually exclusive: `static_ad_resource`, `iframe_ad_resource`, `html_ad_resource`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #width_px
    
    
    def width_px() -> ::Integer

**Returns**

  * (::Integer) — The pixel width of the placement slot for the intended creative. 



### #width_px=
    
    
    def width_px=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The pixel width of the placement slot for the intended creative. 



**Returns**

  * (::Integer) — The pixel width of the placement slot for the intended creative. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
