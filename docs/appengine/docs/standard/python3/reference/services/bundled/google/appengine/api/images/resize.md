---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/resize/
title: google.appengine.api.images.resize \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:12:26.255439+00:00
---

# google.appengine.api.images.resize  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/resize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.images.resize Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/images/__init__.py#L1059-L1126) Resizes a given image file while maintaining the aspect ratio.
    
    
    google.appengine.api.images.resize(
        image_data,
        width=0,
        height=0,
        output_encoding=PNG,
        quality=None,
        correct_orientation=UNCHANGED_ORIENTATION,
        crop_to_fit=False,
        crop_offset_x=0.5,
        crop_offset_y=0.5,
        allow_stretch=False,
        rpc=None,
        transparent_substitution_rgb=None
    )
    

If both `width` and `height` are specified, the more restricting of the two values will be used when resizing the image. The maximum dimension allowed for both width and height is 4000 pixels. If both `width` and `height` are specified and `crop_to_fit` is `True`, the less restricting of the two values will be used when resizing and the image will be cropped to fit the specified size. In this case, the center of cropping can be adjusted by `crop_offset_x` and `crop_offset_y`. | 

## Args  
  
---  
  
`image_data` |  String of the source image data.   
`width` |  Integer of the width (in pixels) to change the image width to.   
`height` |  Integer of the height (in pixels) to change the image height to.   
`output_encoding` |  A value from `OUTPUT_ENCODING_TYPES`.   
`quality` |  A value between 1 and 100 to specify the quality of the encoding. This value is only used to control JPEG quality.   
`correct_orientation` |  A value from `ORIENTATION_CORRECTION_TYPE` to indicate if orientation correction should be performed during the transformation.   
`crop_to_fit` |  If `True`, and both `width` and `height` are specified, the image is cropped after being resized to fit the specified dimensions.   
`crop_offset_x` |  Float value between 0.0 and 1.0. 0 is left and 1 is right. The default value is 0.5, or the center of image.   
`crop_offset_y` |  Float value between 0.0 and 1.0. 0 is top and 1 is bottom. The default value is 0.5, or the center of image.   
`allow_stretch` |  If `True`, and both `width` and `height` are specified, the image is stretched to fit the resized dimensions without maintaining the aspect ratio.   
`rpc` |  Optional UserRPC object.   
`transparent_substitution_rgb` |  When transparent pixels are not supported in the destination image format, then transparent pixels will be substituted for the specified color, which must be in 32-bit RGB format.   
  
## Returns  
  
---  
Raw image data of the resized image.   
  
## Raises  
  
---  
  
`TypeError` |  When `width` or `height` are not of integer or long type.   
`BadRequestError` |  When the specified `width` or `height` is invalid.   
`Error` |  All other errors. See `Image.ExecuteTransforms` for more details.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
