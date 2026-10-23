---
url: https://docs.cloud.google.com/cdn/docs/image-opt-supportedops/
title: Supported operations \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:29.715704+00:00
---

# Supported operations  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/image-opt-supportedops/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Supported operations Stay organized with collections  Save and categorize content based on your preferences. 

This section lists the operations supported by Cloud CDN image optimization. The table includes parameters, such as operation, syntax, attributes, description and examples, which helps you create your `imop` query.

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cloud CDN image optimization supports a set of operations that let you transform your images, such as resize, crop and scale. Each operation has its own syntax, supported attributes and constraints.

This page lists the operations supported by Cloud CDN image optimization with examples that help you create your `imop` query.

**Note:** All parameter names, values, and operations are case-insensitive.Operation | Syntax and example | Attributes | Description  
---|---|---|---  
`Resize` | `?imop=Resize,width=<resized_width>,height=<resized_height>` https://www.example.com/image.jpg?imop=Resize,width=250,height=125 | 

  * `width` type: Integer (Range: 1–8192)
  * `height` type: Integer (Range: 1–8192)

the maximum `width` * `height` can't exceed _67 mpx_ (67,108,864 pixels).
* Scaling (optional) type: enum, values: proportional, stretch.
| This operation doesn't preserve the aspect ratio when you specify both the width and height parameters. If you omit either dimension, Cloud CDN image optimization calculates the other to maintain the aspect ratio.By default, image optimization enforces a strict downscale-only strategy. Specifying the `scaling=stretch` parameter enables upscaling, but the system doesn't permit this if you specify only one size parameter.   
`Scale` | `?imop=Scale,ratio=<scale_ratio>` https://www.example.com/image.jpg?imop=Scale,ratio=0.5 | `ratio`

  * Type: Float (limited to 2 decimal digits)
  * Constraint: 0 < `value`

| This operation scales the image by a specific factor and enforces downscaling only. Mutually exclusive with Resize and Crop operations. If you include the `Scale` operation with the `Resize` or `Crop` operations within a single request, the system returns an error.  
`Crop` | `?imop=Crop,shape=<shape>,left=<left>,right=<right>,top=<top&lgt;,bottom=<bottom>,snap_to_x=<snap_x>,snap_to_y=<snap_y>` https://www.example.com/image.jpg?imop=Crop,shape=rectangle,left=0.5,snap_to_x=512 | `shape`

  * Type: String (rectangle, circle)
  * Default: rectangle
  * Dependency: must be used with the crop parameter. Invalid value will return HTTP 400.

`left`, `right`, `top`, `bottom`

  * Type: Float
  * Range: 0.0 to 1.0, max 3 decimal places
  * Default: 0.0, 1.0, 0.0, 1.0

`snap_to_x, snap_to_y`

  * Type: Integer
  * Range: 0 or greater
  * Default: 0
  * Constraint: mandatory to include at least one of: left, right, top, bottom.

| This operation crops the image based on regional markers. If you specify an invalid value for the `shape` parameter, the system returns an `HTTP 400 Bad Request`. The crop coordinates automatically snap to the nearest multiple of the specified `snap_to_x` or `snap_to_y` value.  
`Canvas` | `?imop=Canvas,width=<canvas_width>,height=<canva_height>,background_color=<color>,gravity=<gravity>` https://www.example.com/image.jpg?imop=Canvas,width=250,height=125,background_color=FFF,gravity=center | `width`, `height`

  * Type: Integer
  * Range: 1–8192
  * Max width x height cannot exceed 67,108,864 pixels.

`gravity`

  * Type: String
  * Values: center, left, right, top, bottom, top_left, top_right, bottom_left, bottom_right
  * Default: center

`background_color`

  * Type: String
  * Format: 3-digit, 4-digit, or 6-digit hex codes
  * Default: 000000 (black).

| This operation enhances images by adding a background layout of specified dimensions and color. The `gravity` parameter dictates the placement of the inner image on this background canvas.  
`Rotate` | `?imop=Rotate,degrees=<rotate_degrees>` https://www.example.com/image.jpg?imop=Rotate,degrees=90 | `degrees`

  * Type: Integer
  * Allowed values: 90, 180, 270.

| This operation rotates the target image clockwise.  
`Mirror` | `?imop=Mirror,flip=<flip>` https://www.example.com/image.jpg?imop=Mirror,flip=h | `flip`

  * Type: String
  * Allowed values: h (horizontal), v (vertical), hv (horizontal & vertical).

| This operation mirrors the image either horizontally, vertically, or both.  
`Compress` | `?imop=Compress,strength=<value>` https://www.example.com/image.jpg?imop=Compress,strength=medium | `strength`

  * Type: String
  * Allowed values: very_weak, weak, medium, strong, very_strong.
  * Constraint: supported only for jpeg, avif, and webp. Values outside this range return HTTP 400.

| This operation compresses the image by decreasing the target image quality. The `strength` parameter lets you control the active image compression level.  
`Convert` | `?imop=Convert,format=<format>` https://www.example.com/image.jpg?imop=Convert,format=webp | `format`

  * Type: String.
  * Allowed values: jpeg, png, webp, avif, gif
  * Constraint: Any other unlisted value will result in a processing error.

| This operation changes the final delivery format of the image. If there is a processing conflict with the browser's incoming `ACCEPT` header specification, the system returns an `HTTP 406 Not Acceptable` error.  
`Metadata` | `?imop=Metadata,preserve=<preserve>` https://www.example.com/image.jpg?imop=Metadata,preserve=none | `preserve`

  * Type: String
  * Allowed values: none, copyright, max
  * Default: copyright

| This operation controls how image metadata properties are handled during execution: `none`: Removes all metadata properties. max: preserves all fields except EXIF orientation and color profiles which are applied on the transformation. `copyright`: keeps only `Author`, `Copyright`, and `Caption` fields.  
`Tone` | `?imop=tone,brightness=<brightness>,contrast=<contrast_level>, saturation=<saturation>` https://www.example.com/image.jpg?imop=tone,brightness=50,contrast=50,saturation=50 | 

  * `brightness`
    * Type: Integer
    * Range: -100 to 100
  * `contrast`
    * Type: Integer
    * Range: -100 to 100
  * `saturation`
    * Type: Integer
    * Range: -100 to 100

| This operation dynamically modifies the `brightness`, `contrast`, and `saturation` levels of an image. If you omit a specific parameter or set to 0, the system doesn't change that attribute. Setting saturation to -100 forces grayscale conversion.  
`Sharpen` | `?imop=Sharpen,strength=<sharpness>` https://www.example.com/image.jpg?imop=Sharpen,strength=50 | `strength`

  * Type: Integer
  * Range: 0 to 100

| This operation increases the sharpness of the image.  
`Blur` | `?imop=Blur,strength=<blur_size>` https://www.example.com/image.jpg?imop=Blur,strength=50 | `strength`

  * Type: Integer
  * Range: 0 to 100

| This operation applies a localized blur filter across the image.   
`Freeze` | `?imop=freeze,frame=<frame>` https://www.example.com/image.gif?imop=freeze,frame=0 | `frame`

  * Type: Integer
  * Range: 0 to 100.

| This operation extracts a single, static frame from an animated image sequence, such as an animated GIF. The frame parameter specifies the exact frame index to extract.  
  
## What's next

  * [Limitations](https://docs.cloud.google.com/cdn/docs/image-opt-limitations)
  * [Image optimization use cases](https://docs.cloud.google.com/cdn/docs/image-opt-use-cases)
  * [Securing image transformation requests](https://docs.cloud.google.com/cdn/docs/image-opt-security)
  * [Troubleshoot and Best Practices](https://docs.cloud.google.com/cdn/docs/image-opt-monitor-troubleshoot)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
