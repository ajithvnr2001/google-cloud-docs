---
url: https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.SpriteSheet
title: Class SpriteSheet (1.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:41.226711+00:00
---

# Class SpriteSheet (1.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/livestream/latest/google.cloud.video.live_stream_v1.types.SpriteSheet

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SpriteSheet (1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.1  1.8.1  1.7.4  1.6.0  1.5.2  1.4.1  1.3.0  1.2.1  1.1.0  1.0.4  0.2.0  0.1.5 
    
    
    SpriteSheet(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Sprite sheet configuration.

## Attributes  
  
---  
**Name** | **Description**  
`format_` |  `str`   
Format type. The default is `jpeg`. Supported formats: \- `jpeg`  
`file_prefix` |  `str`   
Required. File name prefix for the generated sprite sheets. If multiple sprite sheets are added to the channel, each must have a unique file prefix. Each sprite sheet has an incremental 10-digit zero-padded suffix starting from 0 before the extension, such as `sprite_sheet0000000123.jpeg`.   
`sprite_width_pixels` |  `int`   
Required. The width of the sprite in pixels. Must be an even integer.   
`sprite_height_pixels` |  `int`   
Required. The height of the sprite in pixels. Must be an even integer.   
`column_count` |  `int`   
The maximum number of sprites per row in a sprite sheet. Valid range is [1, 10] and the default value is 1.   
`row_count` |  `int`   
The maximum number of rows per sprite sheet. When the sprite sheet is full, a new sprite sheet is created. Valid range is [1, 10] and the default value is 1.   
`interval` |  `google.protobuf.duration_pb2.Duration`   
Create sprites at regular intervals. Valid range is [1 second, 1 hour] and the default value is `10s`.   
`quality` |  `int`   
The quality of the generated sprite sheet. Enter a value between 1 and 100, where 1 is the lowest quality and 100 is the highest quality. The default is 100. A high quality value corresponds to a low image data compression ratio.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
