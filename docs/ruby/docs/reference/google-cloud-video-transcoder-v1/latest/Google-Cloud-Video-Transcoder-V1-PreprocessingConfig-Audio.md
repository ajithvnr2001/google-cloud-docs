---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-PreprocessingConfig-Audio/
title: Transcoder V1 API - Class Google::Cloud::Video::Transcoder::V1::PreprocessingConfig::Audio (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:19.368279+00:00
---

# Transcoder V1 API - Class Google::Cloud::Video::Transcoder::V1::PreprocessingConfig::Audio (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-PreprocessingConfig-Audio/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Transcoder V1 API - Class Google::Cloud::Video::Transcoder::V1::PreprocessingConfig::Audio (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.13.0  0.12.2  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.2 

Reference documentation and code samples for the Transcoder V1 API class Google::Cloud::Video::Transcoder::V1::PreprocessingConfig::Audio.

Audio preprocessing configuration.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #high_boost
    
    
    def high_boost() -> ::Boolean

**Returns**

  * (::Boolean) — Enable boosting high frequency components. The default is `false`.

**Note:** This field is not supported. 




### #high_boost=
    
    
    def high_boost=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Enable boosting high frequency components. The default is `false`.

**Note:** This field is not supported. 




**Returns**

  * (::Boolean) — Enable boosting high frequency components. The default is `false`.

**Note:** This field is not supported. 




### #low_boost
    
    
    def low_boost() -> ::Boolean

**Returns**

  * (::Boolean) — Enable boosting low frequency components. The default is `false`.

**Note:** This field is not supported. 




### #low_boost=
    
    
    def low_boost=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Enable boosting low frequency components. The default is `false`.

**Note:** This field is not supported. 




**Returns**

  * (::Boolean) — Enable boosting low frequency components. The default is `false`.

**Note:** This field is not supported. 




### #lufs
    
    
    def lufs() -> ::Float

**Returns**

  * (::Float) — 

Specify audio loudness normalization in loudness units relative to full scale (LUFS). Enter a value between -24 and 0 (the default), where:

    * -24 is the Advanced Television Systems Committee (ATSC A/85) standard
    * -23 is the EU R128 broadcast standard
    * -19 is the prior standard for online mono audio
    * -18 is the ReplayGain standard
    * -16 is the prior standard for stereo audio
    * -14 is the new online audio standard recommended by Spotify, as well as Amazon Echo
    * 0 disables normalization



### #lufs=
    
    
    def lufs=(value) -> ::Float

**Parameter**

  * **value** (::Float) — 

Specify audio loudness normalization in loudness units relative to full scale (LUFS). Enter a value between -24 and 0 (the default), where:

    * -24 is the Advanced Television Systems Committee (ATSC A/85) standard
    * -23 is the EU R128 broadcast standard
    * -19 is the prior standard for online mono audio
    * -18 is the ReplayGain standard
    * -16 is the prior standard for stereo audio
    * -14 is the new online audio standard recommended by Spotify, as well as Amazon Echo
    * 0 disables normalization



**Returns**

  * (::Float) — 

Specify audio loudness normalization in loudness units relative to full scale (LUFS). Enter a value between -24 and 0 (the default), where:

    * -24 is the Advanced Television Systems Committee (ATSC A/85) standard
    * -23 is the EU R128 broadcast standard
    * -19 is the prior standard for online mono audio
    * -18 is the ReplayGain standard
    * -16 is the prior standard for stereo audio
    * -14 is the new online audio standard recommended by Spotify, as well as Amazon Echo
    * 0 disables normalization



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
