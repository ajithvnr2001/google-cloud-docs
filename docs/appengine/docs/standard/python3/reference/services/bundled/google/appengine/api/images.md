---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/
title: Module: google.appengine.api.images \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:57:12.488995+00:00
---

# Module: google.appengine.api.images  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.api.images Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/images/__init__.py) Image manipulation API. App Engine provides the ability to manipulate image data using a dedicated Images service. The Images service can resize, rotate, flip, and crop images; it can composite multiple images into a single image; and it can convert image data between several formats. It can also enhance photographs using a predefined algorithm. The API can also provide information about an image, such as its format, width, height, and a histogram of color values.

## Modules

[`images_blob_stub`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/images_blob_stub) module: Stub version of the blob-related parts of the images API. [`images_stub`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/images_stub) module: Stub version of the images API.

## Classes

[`class AccessDeniedError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/AccessDeniedError): The application does not have permission to access the image. [`class BadImageError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/BadImageError): The image data is corrupt. [`class BlobKeyRequiredError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/BlobKeyRequiredError): A blob key is required for this operation. [`class Error`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/Error): Base error class for this module. [`class Image`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/Image): Image object to manipulate. [`class InvalidBlobKeyError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/InvalidBlobKeyError): The provided blob key was invalid. [`class LargeImageError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/LargeImageError): The image data is too large to process. [`class NotImageError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/NotImageError): The image data given is not recognizable as an image. [`class ObjectNotFoundError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/ObjectNotFoundError): The blob key referred to an object that does not exist. [`class TransformationError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/TransformationError): An error occurred while attempting to transform the image. [`class UnsupportedSizeError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/UnsupportedSizeError): The size that was specified is not supported by requested operation.

## Functions

[`composite(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/composite): Composites one or more images onto a canvas. [`composite_async(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/composite_async): Asynchronously composites one or more images onto a canvas. [`create_rpc(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/create_rpc): Creates an RPC object for use with the Images API. [`crop(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/crop): Crops the image. [`crop_async(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/crop_async): Asynchronously crops the given image. [`delete_serving_url(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/delete_serving_url): Deletes a serving URL created for `blob_key` using `get_serving_url`. [`delete_serving_url_async(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/delete_serving_url_async): Deletes a serving URL created using get_serving_url - async version. [`get_serving_url(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/get_serving_url): Obtains a URL that will serve the underlying image. [`get_serving_url_async(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/get_serving_url_async): Asynchronously obtains a URL that will serve the underlying image. [`histogram(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/histogram): Calculates the histogram of the given image. [`histogram_async(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/histogram_async): Calculates the histogram of the given image - async version. [`horizontal_flip(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/horizontal_flip): Flips the image horizontally. [`horizontal_flip_async(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/horizontal_flip_async): Asynchronously flips the image horizontally. [`im_feeling_lucky(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/im_feeling_lucky): Automatically adjusts image levels. [`im_feeling_lucky_async(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/im_feeling_lucky_async): Asynchronously automatically adjusts image levels. [`resize(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/resize): Resizes a given image file while maintaining the aspect ratio. [`resize_async(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/resize_async): Asynchronously resizes an image file, maintaining the aspect ratio. [`rotate(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/rotate): Rotates an image a given number of degrees clockwise. [`rotate_async(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/rotate_async): Asynchronously rotates an image a specified number of degrees clockwise. [`vertical_flip(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/vertical_flip): Flips the image vertically. [`vertical_flip_async(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/vertical_flip_async): Asynchronously flips the image vertically. | 

## Other Members  
  
---  
  
ANCHOR_TYPES | 
    
    
    {
     0,
     1,
     2,
     3,
     4,
     5,
     6,
     7,
     8
    }
      
  
BMP |  `-1`  
BOTTOM_CENTER |  `7`  
BOTTOM_LEFT |  `6`  
BOTTOM_RIGHT |  `8`  
CENTER_CENTER |  `4`  
CENTER_LEFT |  `3`  
CENTER_RIGHT |  `5`  
CORRECT_ORIENTATION |  `1`  
GIF |  `-2`  
ICO |  `-3`  
IMG_SERVING_CROP_SIZES |  `[32, 48, 64, 72, 80, 104, 136, 144, 150, 160]`  
IMG_SERVING_SIZES |  `[32, 48, 64, 72, 80, 90, 94, 104, 110, 120, 128, 144, 150, 160, 200, 220, 288, 320, 400, 512, 576, 640, 720, 800, 912, 1024, 1152, 1280, 1440, 1600]`  
IMG_SERVING_SIZES_LIMIT |  `3200`  
JPEG |  `1`  
MAX_COMPOSITES_PER_REQUEST |  `16`  
MAX_TRANSFORMS_PER_REQUEST |  `10`  
ORIENTATION_CORRECTION_TYPE | 
    
    
    {
     0,
     1
    }
      
  
OUTPUT_ENCODING_TYPES | 
    
    
    {
     0,
     1,
     2
    }
      
  
PNG |  `0`  
TIFF |  `-4`  
TOP_CENTER |  `1`  
TOP_LEFT |  `0`  
TOP_RIGHT |  `2`  
UNCHANGED_ORIENTATION |  `0`  
WEBP |  `2`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
