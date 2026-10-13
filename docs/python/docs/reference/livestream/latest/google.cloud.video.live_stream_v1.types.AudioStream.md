---
url: https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.AudioStream
title: Class AudioStream (1.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:39:02.602026+00:00
---

# Class AudioStream (1.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.AudioStream

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AudioStream (1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.1  1.8.1  1.7.4  1.6.0  1.5.2  1.4.1  1.3.0  1.2.1  1.1.0  1.0.4  0.2.0  0.1.5 
    
    
    AudioStream(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Audio stream resource.

## Attributes  
  
---  
**Name** | **Description**  
`transmux` |  `bool`   
Specifies whether pass through (transmuxing) is enabled or not. If set to `true`, the rest of the settings, other than `mapping`, will be ignored. The default is `false`.   
`codec` |  `str`   
The codec for this audio stream. The default is `aac`. Supported audio codecs: \- `aac`  
`bitrate_bps` |  `int`   
Required. Audio bitrate in bits per second. Must be between 1 and 10,000,000.   
`channel_count` |  `int`   
Number of audio channels. Must be between 1 and 6. The default is 2.   
`channel_layout` |  `MutableSequence[str]`   
A list of channel names specifying layout of the audio channels. This only affects the metadata embedded in the container headers, if supported by the specified format. The default is `[fl, fr]`. Supported channel names: \- `fl` \- Front left channel \- `fr` \- Front right channel \- `sl` \- Side left channel \- `sr` \- Side right channel \- `fc` \- Front center channel \- `lfe` \- Low frequency   
`mapping_` |  `MutableSequence[[google.cloud.video.live_stream_v1.types.AudioStream.AudioMapping](https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.AudioStream.AudioMapping)]`   
The mapping for the input streams and audio channels.   
`sample_rate_hertz` |  `int`   
The audio sample rate in Hertz. The default is 48000 Hertz.   
  
## Classes 

### AudioMapping
    
    
    AudioMapping(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The mapping for the input streams and audio channels.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
