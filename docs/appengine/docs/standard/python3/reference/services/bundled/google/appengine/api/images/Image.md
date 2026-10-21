---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/Image/
title: google.appengine.api.images.Image \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:50:56.125393+00:00
---

# google.appengine.api.images.Image  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/Image/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.images.Image Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/images/__init__.py#L190-L1028) Image object to manipulate. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.images.Image(
        image_data=None, blob_key=None, filename=None
    )
    

| 

## Args  
  
---  
  
`image_data` |  Byte of the image data.   
`blob_key` |  A `BlobKey`, `BlobInfo`, string, or Unicode representation of the blob key of the blob that contains the image data.   
`filename` |  String of the file name of a Google Storage file that contains the image data. Must be in the format `/gs/bucket_name/object_name`.   
  
## Raises  
  
---  
  
`NotImageError` |  If the given data is empty.   
  
## Attributes  
  
---  
  
`format` |  Retrieves the format of the image.   
`height` |  Retrieves the height of the image.   
`width` |  Retrieves the width of the image.   
  
## Methods

### `CheckValidIntParameter`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/images/__init__.py#L1019-L1028)
    
    
    @staticmethod
    CheckValidIntParameter(
        parameter, min_value, max_value, name
    )
    

Checks that a parameter is an integer within the specified range.

### `crop`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/images/__init__.py#L674-L712)
    
    
    crop(
        left_x, top_y, right_x, bottom_y
    )
    

Crops the image.

The four arguments are the scaling numbers that describe the bounding box that will crop the image. The upper left point of the bounding box will be at (`left_x*image_width`, `top_y*image_height`), and the lower right point will be at (`right_x*image_width`, `bottom_y*image_height`).

Args  
---  
  
`left_x` |  Float value between 0.0 and 1.0, inclusive.   
`top_y` |  Float value between 0.0 and 1.0, inclusive.   
`right_x` |  Float value between 0.0 and 1.0, inclusive.   
`bottom_y` |  Float value between 0.0 and 1.0, inclusive.   
  
Raises  
---  
  
`TypeError` |  If the arguments are not of type float.   
`BadRequestError` |  When the bounding box values are invalid or if `MAX_TRANSFORMS_PER_REQUEST` transforms have already been requested for this image.   
  
### `execute_transforms`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/images/__init__.py#L771-L817)
    
    
    execute_transforms(
        output_encoding=PNG,
        quality=None,
        parse_source_metadata=False,
        transparent_substitution_rgb=None,
        rpc=None
    )
    

Performs transformations on a given image.

You can only execute one transformation per image per `execute_transforms()` call.

Args  
---  
  
`output_encoding` |  A value from `OUTPUT_ENCODING_TYPES`.   
`quality` |  A value between 1 and 100 to specify the quality of the encoding. This value is only used for JPEG and WEBP quality control.   
`parse_source_metadata` |  When `True`, the metadata (EXIF) of the source image is parsed before any transformations. The results can be retrieved via [`Image.get_original_metadata`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/Image#get_original_metadata).   
`transparent_substitution_rgb` |  When transparent pixels are not supported in the destination image format, transparent pixels will be substituted for the specified color, which must be 32-bit RGB format.   
`rpc` |  A UserRPC object.   
  
Returns  
---  
A string of the image data after the transformations have been performed on it.   
  
Raises  
---  
  
`BadRequestError` |  When the request specifications are invalid.   
`NotImageError` |  When the image data given is not an image.   
`BadImageError` |  When the image data given is corrupt.   
`LargeImageError` |  When the image data given is too large to process.   
`InvalidBlobKeyError` |  When the blob key provided is invalid.   
`TransformationError` |  When an error occurs during image manipulation.   
`AccessDeniedError` |  When the blob key refers to a Google Storage object, and the application does not have permission to access the object.   
`ObjectNotFoundError` |  When the blob key refers to an object that no longer exists.   
`Error` |  All other error conditions.   
  
### `execute_transforms_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/images/__init__.py#L819-L923)
    
    
    execute_transforms_async(
        output_encoding=PNG,
        quality=None,
        parse_source_metadata=False,
        transparent_substitution_rgb=None,
        rpc=None
    )
    

Asynchronously performs transformations on a given image.

Args  
---  
  
`output_encoding` |  A value from `OUTPUT_ENCODING_TYPES`.   
`quality` |  A value between 1 and 100 to specify the quality of the encoding. This value is only used for JPEG & WEBP quality control.   
`parse_source_metadata` |  When `True`, the metadata (EXIF) of the source image is parsed before any transformations. The results can be retrieved via [`Image.get_original_metadata`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/Image#get_original_metadata).   
`transparent_substitution_rgb` |  When transparent pixels are not supported in the destination image format, transparent pixels will be substituted for the specified color, which must be in 32-bit RGB format.   
`rpc` |  A UserRPC object.   
  
Returns  
---  
A UserRPC object.   
  
Raises  
---  
  
`BadRequestError` |  When the request specifications are invalid.   
`NotImageError` |  When the image data given is not an image.   
`BadImageError` |  When the image data given is corrupt.   
`LargeImageError` |  When the image data given is too large to process.   
`InvalidBlobKeyError` |  When the blob key provided is invalid.   
`TransformationError` |  When an error occurs during image manipulation.   
`AccessDeniedError` |  When the blob key refers to a Google Storage object, and the application does not have permission to access the object.   
`ValueError` |  When `transparent_substitution_rgb` is not an integer.   
`Error` |  All other error conditions.   
  
### `get_original_metadata`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/images/__init__.py#L729-L757)
    
    
    get_original_metadata()
    

Lists the metadata of the original image.

Returns a dictionary of metadata extracted from the original image during `execute_transform`.

#### Note:

Some of the EXIF fields are processed; for example, fields with multiple values are returned as lists, rational types are returned as floats, GPS coordinates are already parsed to signed floats, etc.

`ImageWidth` and `ImageLength` fields are corrected if they did not correspond to the actual dimensions of the original image.

Returns  
---  
Dictionary of metadata with string keys. If `execute_transform` was called with `parse_metadata` set to `True`, this dictionary contains information about the various properties of the original image, such as dimensions, color profile, and properties from EXIF. Even if `parse_metadata` was `False` or the images did not have any metadata, the dictionary will contain a limited set of metadata, with least `ImageWidth` and `ImageLength` dimensions of the original image being returned. This call will return `None` if it is called before a successful `execute_transfrom` call.   
  
### `histogram`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/images/__init__.py#L946-L969)
    
    
    histogram(
        rpc=None
    )
    

Calculates the histogram of the image.

Args  
---  
  
`rpc` |  A UserRPC object.   
  
Returns  
---  
3 256-element lists containing the number of occurences of each value of each color in the order RGB. You can learn more about color histograms at `Wikipedia`_.   
  
Raises  
---  
  
`NotImageError` |  When the image data supplied is not an image.   
`BadImageError` |  When the image data supplied is corrupt.   
`LargeImageError` |  When the image data supplied is too large to process.   
`Error` |  All other error conditions.   
  
.. _Wikipedia: http://en.wikipedia.org/wiki/Color_histogram

### `histogram_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/images/__init__.py#L971-L1017)
    
    
    histogram_async(
        rpc=None
    )
    

Asynchronously calculates the histogram of the image.

Args  
---  
  
`rpc` |  An optional UserRPC object.   
  
Returns  
---  
  
`rpc` |  A UserRPC object.   
  
Raises  
---  
  
`NotImageError` |  When the image data supplied is not an image.   
`BadImageError` |  When the image data supplied is corrupt.   
`LargeImageError` |  When the image data supplied is too large to process.   
`Error` |  All other error conditions.   
  
### `horizontal_flip`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/images/__init__.py#L629-L641)
    
    
    horizontal_flip()
    

Flips the image horizontally.

Raises  
---  
  
`BadRequestError` |  If `MAX_TRANSFORMS_PER_REQUEST` transforms have already been requested on the image.   
  
### `im_feeling_lucky`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/images/__init__.py#L714-L727)
    
    
    im_feeling_lucky()
    

Automatically adjusts the image's contrast and color levels.

This is similar to the "I'm Feeling Lucky" button in Picasa.

Raises  
---  
  
`BadRequestError` |  If `MAX_TRANSFORMS_PER_REQUEST` transforms have already been requested for this image.   
  
### `resize`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/images/__init__.py#L520-L596)
    
    
    resize(
        width=0,
        height=0,
        crop_to_fit=False,
        crop_offset_x=0.5,
        crop_offset_y=0.5,
        allow_stretch=False
    )
    

Resizes the image, maintaining the aspect ratio.

If both `width` and `height` are specified, the more restricting of the two values will be used when the image is resized. The maximum dimension allowed for both `width` and `height` is 4000 pixels.

If both `width` and `height` are specified, and `crop_to_fit` is `True`, the less restricting of the two values will be used when the image is resized, and the image will be cropped to fit the specified size. In this case, the center of cropping can be adjusted by `crop_offset_x` and `crop_offset_y`.

Args  
---  
  
`width` |  Integer of the width in pixels to change the image width to.   
`height` |  Integer of the height in pixels to change the image height to.   
`crop_to_fit` |  If `True`, and both `width` and `height` are specified, the image is cropped after it is resized to fit the specified dimensions.   
`crop_offset_x` |  Float value between 0.0 and 1.0. 0 is left, and 1 is right. The default value is 0.5, or the center of the image.   
`crop_offset_y` |  Float value between 0.0 and 1.0. 0 is top, and 1 is bottom. The default value is 0.5, or the center of the image.   
`allow_stretch` |  If `True`, and both `width` and `height` are specified, the image is stretched to fit the resize dimensions without maintaining the aspect ratio.   
  
Raises  
---  
  
`TypeError` |  When `width` or `height` is not an integer or long type.   
`BadRequestError` |  When the height or width is invalid, or if `MAX_TRANSFORMS_PER_REQUEST` transforms have already been requested on this image.   
  
### `rotate`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/images/__init__.py#L598-L627)
    
    
    rotate(
        degrees
    )
    

Rotates an image a given number of degrees clockwise.

Args  
---  
  
`degrees` |  Integer value of the number of degrees that an image must be rotated. This value must be a multiple of 90.   
  
Raises  
---  
  
`TypeError` |  When `degrees` is not an integer or long type.   
`BadRequestError` |  When the `degrees` value is invalid or if `MAX_TRANSFORMS_PER_REQUEST` transforms have already been requested.   
  
### `set_correct_orientation`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/images/__init__.py#L444-L473)
    
    
    set_correct_orientation(
        correct_orientation
    )
    

Sets a flag to correct the image orientation based on image metadata.

EXIF metadata within the image may contain a parameter that indicates its proper orientation. This value can equal 1 through 8, inclusive. Setting the orientation to 1 means that the image is in its "normal" orientation, i.e., it should be viewed as it is stored. Normally, this orientation value has no effect on the behavior of the transformations. However, if you call this function with the `correct_orientation` argument, any orientation specified in the EXIF metadata will be corrected during the first transformation.

#### Note:

If `correct_orientation` is specified, but the image is already in portrait orientation, i.e., "taller" than it is "wide," no corrections will be made, since the camera has likely already corrected it.

Whether the correction was requested or not, the orientation value in the transformed image is always cleared to indicate that no additional corrections of the returned image's orientation is necessary.

Args  
---  
  
`correct_orientation` |  A value from `ORIENTATION_CORRECTION_TYPE`.   
  
Raises  
---  
  
`BadRequestError` |  If the `correct_orientation` value is invalid.   
  
### `vertical_flip`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/images/__init__.py#L643-L654)
    
    
    vertical_flip()
    

Flips the image vertically.

Raises  
---  
  
`BadRequestError` |  If `MAX_TRANSFORMS_PER_REQUEST` transforms have already been requested on the image.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
