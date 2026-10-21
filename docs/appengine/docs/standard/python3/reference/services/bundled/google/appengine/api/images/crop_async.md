---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/crop_async/
title: google.appengine.api.images.crop_async \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:38:39.860653+00:00
---

# google.appengine.api.images.crop_async  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/crop_async/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.images.crop_async Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/images/__init__.py#L1482-L1531) Asynchronously crops the given image.
    
    
    google.appengine.api.images.crop_async(
        image_data,
        left_x,
        top_y,
        right_x,
        bottom_y,
        output_encoding=PNG,
        quality=None,
        correct_orientation=UNCHANGED_ORIENTATION,
        rpc=None,
        transparent_substitution_rgb=None
    )
    

The four arguments are the scaling numbers that describe the bounding box that will crop the image. The upper left point of the bounding box will be at (`left_x*image_width`, `top_y*image_height`), and the lower right point will be at (`right_x*image_width`, `bottom_y*image_height`). | 

## Args  
  
---  
  
`image_data` |  String of the source image data.   
`left_x` |  Float value between 0.0 and 1.0, inclusive.   
`top_y` |  Float value between 0.0 and 1.0, inclusive.   
`right_x` |  Float value between 0.0 and 1.0, inclusive.   
`bottom_y` |  Float value between 0.0 and 1.0, inclusive.   
`output_encoding` |  A value from `OUTPUT_ENCODING_TYPES`.   
`quality` |  A value between 1 and 100 to specify the quality of the encoding. This value is only used to control JPEG quality.   
`correct_orientation` |  A value from `ORIENTATION_CORRECTION_TYPE` to indicate if orientation correction should be performed during the transformation.   
`rpc` |  An optional UserRPC object.   
`transparent_substitution_rgb` |  When transparent pixels are not supported in the destination image format, then transparent pixels will be substituted for the specified color, which must be in 32-bit RGB format.   
  
## Returns  
  
---  
A UserRPC object; call `get_result()` to complete the RPC and obtain the crop result.   
  
## Raises  
  
---  
  
`TypeError` |  If the args are not of type float.   
`BadRequestError` |  When the bounding box values are invalid.   
`Error` |  All other errors. See `Image.ExecuteTransforms` for more details.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
