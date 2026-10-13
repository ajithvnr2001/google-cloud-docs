---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images
title: Package com.google.appengine.api.images (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:35:25.109639+00:00
---

# Package com.google.appengine.api.images (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package com.google.appengine.api.images (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

Provides facilities for the creation and manipulation of images. The starting point is the [com.google.appengine.api.images.ImagesServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServiceFactory) class, which can produce the [com.google.appengine.api.images.ImagesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService), but also the basic [com.google.appengine.api.images.Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image) object and [com.google.appengine.api.images.Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform) classes. More information is available in the [on-line documentation](http://cloud.google.com/appengine/docs/java/images/).

Image data is represented as a `byte[]` of data, in any of the supported formats: JPEG, PNG, GIF (including animated GIF), BMP, TIFF, and ICO formats. The format can be accessed via the com.google.appengine.api.images.Image#getFormat() method. The image format may be converted during transformation.

Supported transformations include cropping, resizing, rotating in 90-degree increments, horizontal and vertical flips, and automated color enhancement. See Also: [The Images Java API in the _Google App Engine Developer's Guide_](http://cloud.google.com/appengine/docs/java/images/)., [com.google.appengine.api.images.ImagesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService)

## Classes 

### [Composite](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Composite)

A `Composite` represents a composition of an image onto a canvas.

### [CompositeTransform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.CompositeTransform)

A transform that represents zero or more transforms executed in series.

### [IImagesServiceFactoryProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.IImagesServiceFactoryProvider)

Factory provider for [IImagesServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.IImagesServiceFactory).

**Note:** This class is not intended for end users.

### [ImagesServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServiceFactory)

Factory for creating an [ImagesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService), [Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)s and [Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform)s.

### [ImagesServicePb](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb)

### [ImagesServicePb.CompositeImageOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.CompositeImageOptions)

### [ImagesServicePb.CompositeImageOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.CompositeImageOptions.Builder)

### [ImagesServicePb.ImageData](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImageData)

### [ImagesServicePb.ImageData.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImageData.Builder)

### [ImagesServicePb.ImagesCanvas](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesCanvas)

### [ImagesServicePb.ImagesCanvas.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesCanvas.Builder)

### [ImagesServicePb.ImagesCompositeRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesCompositeRequest)

### [ImagesServicePb.ImagesCompositeRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesCompositeRequest.Builder)

### [ImagesServicePb.ImagesCompositeResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesCompositeResponse)

### [ImagesServicePb.ImagesCompositeResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesCompositeResponse.Builder)

### [ImagesServicePb.ImagesDeleteUrlBaseRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesDeleteUrlBaseRequest)

### [ImagesServicePb.ImagesDeleteUrlBaseRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesDeleteUrlBaseRequest.Builder)

### [ImagesServicePb.ImagesDeleteUrlBaseResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesDeleteUrlBaseResponse)

### [ImagesServicePb.ImagesDeleteUrlBaseResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesDeleteUrlBaseResponse.Builder)

### [ImagesServicePb.ImagesGetUrlBaseRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesGetUrlBaseRequest)

### [ImagesServicePb.ImagesGetUrlBaseRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesGetUrlBaseRequest.Builder)

### [ImagesServicePb.ImagesGetUrlBaseResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesGetUrlBaseResponse)

### [ImagesServicePb.ImagesGetUrlBaseResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesGetUrlBaseResponse.Builder)

### [ImagesServicePb.ImagesHistogram](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesHistogram)

### [ImagesServicePb.ImagesHistogram.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesHistogram.Builder)

### [ImagesServicePb.ImagesHistogramRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesHistogramRequest)

### [ImagesServicePb.ImagesHistogramRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesHistogramRequest.Builder)

### [ImagesServicePb.ImagesHistogramResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesHistogramResponse)

### [ImagesServicePb.ImagesHistogramResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesHistogramResponse.Builder)

### [ImagesServicePb.ImagesServiceError](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesServiceError)

### [ImagesServicePb.ImagesServiceError.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesServiceError.Builder)

### [ImagesServicePb.ImagesServiceTransform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesServiceTransform)

### [ImagesServicePb.ImagesServiceTransform.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesServiceTransform.Builder)

### [ImagesServicePb.ImagesTransformRequest](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesTransformRequest)

### [ImagesServicePb.ImagesTransformRequest.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesTransformRequest.Builder)

### [ImagesServicePb.ImagesTransformResponse](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesTransformResponse)

### [ImagesServicePb.ImagesTransformResponse.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesTransformResponse.Builder)

### [ImagesServicePb.InputSettings](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.InputSettings)

### [ImagesServicePb.InputSettings.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.InputSettings.Builder)

### [ImagesServicePb.OutputSettings](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.OutputSettings)

### [ImagesServicePb.OutputSettings.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.OutputSettings.Builder)

### [ImagesServicePb.Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.Transform)

### [ImagesServicePb.Transform.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.Transform.Builder)

### [InputSettings](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.InputSettings)

`InputSettings` represents the different settings to specify how an [Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image) is interpreted by a transform.

### [OutputSettings](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.OutputSettings)

`OutputSettings` represents the different settings to specify how a particular transform or composite will return an [Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image).

### [ServingUrlOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ServingUrlOptions)

Allow users to customize the behavior of creating a image serving URL using the [ImagesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService).

### [ServingUrlOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ServingUrlOptions.Builder)

Contains static creation methods for [ServingUrlOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ServingUrlOptions).

### [Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform)

A transform that can be applied to an [Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image).

## Interfaces 

### [IImagesServiceFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.IImagesServiceFactory)

Factory for creating an [ImagesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService), [Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)s and [Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform)s.

### [Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)

`Image` represents an image that can be manipulated by the [ImagesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService).

### [ImagesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService)

The images service provides methods to apply transformations to images.

### [ImagesServicePb.CompositeImageOptionsOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.CompositeImageOptionsOrBuilder)

### [ImagesServicePb.ImageDataOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImageDataOrBuilder)

### [ImagesServicePb.ImagesCanvasOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesCanvasOrBuilder)

### [ImagesServicePb.ImagesCompositeRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesCompositeRequestOrBuilder)

### [ImagesServicePb.ImagesCompositeResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesCompositeResponseOrBuilder)

### [ImagesServicePb.ImagesDeleteUrlBaseRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesDeleteUrlBaseRequestOrBuilder)

### [ImagesServicePb.ImagesDeleteUrlBaseResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesDeleteUrlBaseResponseOrBuilder)

### [ImagesServicePb.ImagesGetUrlBaseRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesGetUrlBaseRequestOrBuilder)

### [ImagesServicePb.ImagesGetUrlBaseResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesGetUrlBaseResponseOrBuilder)

### [ImagesServicePb.ImagesHistogramOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesHistogramOrBuilder)

### [ImagesServicePb.ImagesHistogramRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesHistogramRequestOrBuilder)

### [ImagesServicePb.ImagesHistogramResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesHistogramResponseOrBuilder)

### [ImagesServicePb.ImagesServiceErrorOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesServiceErrorOrBuilder)

### [ImagesServicePb.ImagesServiceTransformOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesServiceTransformOrBuilder)

### [ImagesServicePb.ImagesTransformRequestOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesTransformRequestOrBuilder)

### [ImagesServicePb.ImagesTransformResponseOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesTransformResponseOrBuilder)

### [ImagesServicePb.InputSettingsOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.InputSettingsOrBuilder)

### [ImagesServicePb.OutputSettingsOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.OutputSettingsOrBuilder)

### [ImagesServicePb.TransformOrBuilder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.TransformOrBuilder)

## Enums 

### [Composite.Anchor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Composite.Anchor)

Valid anchoring positions for a compositing operation. The anchor position of the image is aligned with the anchor position of the canvas.

### [Image.Format](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image.Format)

Image formats usable by the images api.

### [ImagesService.OutputEncoding](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService.OutputEncoding)

Valid output encoding formats usable for image transforms. See Also: [PNG Image Format.](http://www.libpng.org/pub/png/), [JPEG Image Format.](https://en.wikipedia.org/wiki/JPEG), [WEBP Image Format.](https://developers.google.com/speed/webp/)

### [ImagesServicePb.CompositeImageOptions.ANCHOR](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.CompositeImageOptions.ANCHOR)

### [ImagesServicePb.ImagesServiceError.ErrorCode](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesServiceError.ErrorCode)

### [ImagesServicePb.ImagesServiceTransform.Type](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.ImagesServiceTransform.Type)

### [ImagesServicePb.InputSettings.ORIENTATION_CORRECTION_TYPE](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.InputSettings.ORIENTATION_CORRECTION_TYPE)

### [ImagesServicePb.OutputSettings.MIME_TYPE](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServicePb.OutputSettings.MIME_TYPE)

### [InputSettings.OrientationCorrection](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.InputSettings.OrientationCorrection)

Actions to take with respect to correcting image orientation based on image metadata. EXIF metadata within the image may contain a parameter indicating its proper orientation. This value can equal 1 through 8, inclusive. "1" means that the image is in its "normal" orientation, i.e., it should be viewed as it is stored.

Regardless of the `OrientationCorrection` value used, the orientation value in a transformed image is always cleared to indicate that no additional corrections of the returned image's orientation is necessary.

## Exceptions 

### [ImagesServiceFailureException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServiceFailureException)

`ImagesServiceFailureException` is thrown when any unknown error occurs while communicating with the images service.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
