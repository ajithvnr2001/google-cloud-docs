---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-ManifestOptions/
title: Video Stitcher V1 API - Class Google::Cloud::Video::Stitcher::V1::ManifestOptions (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:25:30.367676+00:00
---

# Video Stitcher V1 API - Class Google::Cloud::Video::Stitcher::V1::ManifestOptions (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-ManifestOptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Video Stitcher V1 API - Class Google::Cloud::Video::Stitcher::V1::ManifestOptions (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.0  0.8.2  0.7.0  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Video Stitcher V1 API class Google::Cloud::Video::Stitcher::V1::ManifestOptions.

Options for manifest generation.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #bitrate_order
    
    
    def bitrate_order() -> ::Google::Cloud::Video::Stitcher::V1::ManifestOptions::OrderPolicy

**Returns**

  * ([::Google::Cloud::Video::Stitcher::V1::ManifestOptions::OrderPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-ManifestOptions-OrderPolicy)) — If specified, the output manifest will orders the video and muxed renditions by bitrate according to the ordering policy. 



### #bitrate_order=
    
    
    def bitrate_order=(value) -> ::Google::Cloud::Video::Stitcher::V1::ManifestOptions::OrderPolicy

**Parameter**

  * **value** ([::Google::Cloud::Video::Stitcher::V1::ManifestOptions::OrderPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-ManifestOptions-OrderPolicy)) — If specified, the output manifest will orders the video and muxed renditions by bitrate according to the ordering policy. 



**Returns**

  * ([::Google::Cloud::Video::Stitcher::V1::ManifestOptions::OrderPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-ManifestOptions-OrderPolicy)) — If specified, the output manifest will orders the video and muxed renditions by bitrate according to the ordering policy. 



### #include_renditions
    
    
    def include_renditions() -> ::Array<::Google::Cloud::Video::Stitcher::V1::RenditionFilter>

**Returns**

  * (::Array<[::Google::Cloud::Video::Stitcher::V1::RenditionFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-RenditionFilter)>) — If specified, the output manifest will only return renditions matching the specified filters. 



### #include_renditions=
    
    
    def include_renditions=(value) -> ::Array<::Google::Cloud::Video::Stitcher::V1::RenditionFilter>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Video::Stitcher::V1::RenditionFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-RenditionFilter)>) — If specified, the output manifest will only return renditions matching the specified filters. 



**Returns**

  * (::Array<[::Google::Cloud::Video::Stitcher::V1::RenditionFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher-v1/latest/Google-Cloud-Video-Stitcher-V1-RenditionFilter)>) — If specified, the output manifest will only return renditions matching the specified filters. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
