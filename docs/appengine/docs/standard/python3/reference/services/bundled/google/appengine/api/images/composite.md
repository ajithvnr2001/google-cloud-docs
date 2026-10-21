---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/composite/
title: google.appengine.api.images.composite \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:18:57.753438+00:00
---

# google.appengine.api.images.composite  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/composite/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.images.composite Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/images/__init__.py#L1610-L1658) Composites one or more images onto a canvas.
    
    
    google.appengine.api.images.composite(
        inputs, width, height, color=0, output_encoding=PNG, quality=None, rpc=None
    )
    

| 

## Args  
  
---  
  
`inputs` |  a list of tuples (`image_data`, `x_offset`, `y_offset`, `opacity`, `anchor`) where: - image_data String of the source image data. - x_offset X offset, in pixels from the anchor position. - y_offset Y offset, in piyels from the anchor position. - opacity Opacity of the image, specified as a float in range [0.0, 1.0] - anchor Anchoring point from `ANCHOR_POINTS`. The anchor point of the image is aligned with the same anchor point of the canvas. For example, `TOP_RIGHT` would place the top right corner of the image at the top right corner of the canvas, then apply the x and y offsets.   
`width` |  Canvas width, in pixels.   
`height` |  Canvas height, in pixels.   
`color` |  Canvas background color, encoded as a 32-bit unsigned integer, where each color channel is represented by one byte in ARGB order.   
`output_encoding` |  A value from `OUTPUT_ENCODING_TYPES`.   
`quality` |  A value between 1 and 100 to specify the quality of the encoding. This value is only used to control JPEG quality.   
`rpc` |  Optional UserRPC object.   
  
## Returns  
  
---  
A string that contains the image data of the composited image.   
  
## Raises  
  
---  
  
`TypeError` |  If `width`, `height`, `color`, `x_offset` or `y_offset` are not of type integer or long, or if `opacity` is not a float.   
`BadRequestError` |  If more than `MAX_TRANSFORMS_PER_REQUEST` compositions have been requested, if the canvas width or height is greater than 4000 or less than or equal to 0, if the color is invalid, if the opacity is outside the range [0,1] for any composition option, or if the anchor is invalid.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
