---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServiceFactory
title: Class ImagesServiceFactory (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:05:06.057581+00:00
---

# Class ImagesServiceFactory (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesServiceFactory

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class ImagesServiceFactory (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class ImagesServiceFactory

Factory for creating an [ImagesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService), [Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)s and [Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform)s.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ImagesServiceFactory

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Methods 

### getImagesService()
    
    
    public static ImagesService getImagesService()

Creates an implementation of the ImagesService.

**Returns**  
---  
**Type** | **Description**  
`[ImagesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService)` | an images service  
  
### makeComposite(Image image, int xOffset, int yOffset, float opacity, Composite.Anchor anchor)
    
    
    public static Composite makeComposite(Image image, int xOffset, int yOffset, float opacity, Composite.Anchor anchor)

Creates an image composition operation.

**Parameters**  
---  
**Name** | **Description**  
`image` | `[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)`  
The image to be composited.  
`xOffset` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Offset in the x axis from the anchor point.  
`yOffset` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Offset in the y axis from the anchor point.  
`opacity` | `[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Opacity to be used for the image in range [0.0, 1.0].  
`anchor` | `[Composite.Anchor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Composite.Anchor)`  
Anchor position from the enum [Composite.Anchor](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Composite.Anchor). The anchor position of the image is aligned with the anchor position of the canvas and then the offsets are applied.  
**Returns**  
---  
**Type** | **Description**  
`[Composite](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Composite)` | A composition operation.  
  
### makeCompositeTransform()
    
    
    public static CompositeTransform makeCompositeTransform()

Creates a composite transform that can represent multiple transforms applied in series.

**Returns**  
---  
**Type** | **Description**  
`[CompositeTransform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.CompositeTransform)` | an empty composite transform  
  
### makeCompositeTransform(Collection<Transform> transforms)
    
    
    public static CompositeTransform makeCompositeTransform(Collection<Transform> transforms)

Creates a composite transform that can represent multiple transforms applied in series.

**Parameter**  
---  
**Name** | **Description**  
`transforms` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform)>`  
Transforms for this composite transform to apply.  
**Returns**  
---  
**Type** | **Description**  
`[CompositeTransform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.CompositeTransform)` | a composite transform containing the provided transforms  
  
### makeCrop(double leftX, double topY, double rightX, double bottomY)
    
    
    public static Transform makeCrop(double leftX, double topY, double rightX, double bottomY)

Creates a transform that will crop an image to fit within the bounding box specified.

The arguments define the top left and bottom right corners of the bounding box used to crop the image as a percentage of the total image size. Each argument should be in the range 0.0 to 1.0 inclusive.

**Parameters**  
---  
**Name** | **Description**  
`leftX` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
X coordinate of the top left corner of the bounding box  
`topY` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Y coordinate of the top left corner of the bounding box  
`rightX` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
X coordinate of the bottom right corner of the bounding box  
`bottomY` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Y coordinate of the bottom right corner of the bounding box  
**Returns**  
---  
**Type** | **Description**  
`[Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform)` | a crop transform  
  
### makeCrop(float leftX, float topY, float rightX, float bottomY)
    
    
    public static Transform makeCrop(float leftX, float topY, float rightX, float bottomY)

Creates a transform that will crop an image to fit within the bounding box specified.

The arguments define the top left and bottom right corners of the bounding box used to crop the image as a percentage of the total image size. Each argument should be in the range 0.0 to 1.0 inclusive.

**Parameters**  
---  
**Name** | **Description**  
`leftX` | `[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
X coordinate of the top left corner of the bounding box  
`topY` | `[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Y coordinate of the top left corner of the bounding box  
`rightX` | `[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
X coordinate of the bottom right corner of the bounding box  
`bottomY` | `[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Y coordinate of the bottom right corner of the bounding box  
**Returns**  
---  
**Type** | **Description**  
`[Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform)` | a crop transform  
  
### makeHorizontalFlip()
    
    
    public static Transform makeHorizontalFlip()

Creates a transform that will horizontally flip an image.

**Returns**  
---  
**Type** | **Description**  
`[Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform)` | a horizontal flip transform  
  
### makeImFeelingLucky()
    
    
    public static Transform makeImFeelingLucky()

Creates a transform that automatically adjust contrast and color levels.

This is similar to the "I'm Feeling Lucky" button in Picasa.

**Returns**  
---  
**Type** | **Description**  
`[Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform)` | an ImFeelingLucky autolevel transform  
  
### makeImage(byte[] imageData)
    
    
    public static Image makeImage(byte[] imageData)

Creates an image from the provided `imageData`.

**Parameter**  
---  
**Name** | **Description**  
`imageData` | `byte[]`  
image data to store in the image  
**Returns**  
---  
**Type** | **Description**  
`[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)` | an Image containing the supplied image data  
  
### makeImageFromBlob(BlobKey blobKey)
    
    
    public static Image makeImageFromBlob(BlobKey blobKey)

Create an image backed by the specified `blobKey`. Note that the returned [Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image) object can be used with all [ImagesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService) methods, but most of the methods on the Image itself will currently throw UnsupportedOperationException.

**Parameter**  
---  
**Name** | **Description**  
`blobKey` | `[BlobKey](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.BlobKey)`  
referencing the image  
**Returns**  
---  
**Type** | **Description**  
`[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)` | an Image that references the specified blob data  
  
### makeImageFromFilename(String filename)
    
    
    public static Image makeImageFromFilename(String filename)

Create an image backed by the specified `filename`. Note that the returned [Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image) object can be used with all [ImagesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService) methods, but most of the methods on the Image itself will currently throw UnsupportedOperationException.

**Parameter**  
---  
**Name** | **Description**  
`filename` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
referencing the image. Currently only Google Storage files in the format "/gs/bucket_name/object_name" are supported.  
**Returns**  
---  
**Type** | **Description**  
`[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)` | an Image that references the specified blob data  
  
### makeResize(int width, int height)
    
    
    public static Transform makeResize(int width, int height)

Creates a transform that will resize an image to fit within a box with width `width` and height `height`.

**Parameters**  
---  
**Name** | **Description**  
`width` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
width of the bounding box  
`height` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
height of the bounding box  
**Returns**  
---  
**Type** | **Description**  
`[Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform)` | a resize transform  
  
### makeResize(int width, int height, boolean allowStretch)
    
    
    public static Transform makeResize(int width, int height, boolean allowStretch)

Creates a resize transform that will resize an image to fit within a box of width `width` and height `height`. If `allowStretch` is `true`, the aspect ratio of the original image will be ignored.

**Parameters**  
---  
**Name** | **Description**  
`width` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
width of the bounding box  
`height` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
height of the bounding box  
`allowStretch` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
allow the image to be resized ignoring the aspect ratio  
**Returns**  
---  
**Type** | **Description**  
`[Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform)` | a resize transform  
  
### makeResize(int width, int height, double cropOffsetX, double cropOffsetY)
    
    
    public static Transform makeResize(int width, int height, double cropOffsetX, double cropOffsetY)

Creates a transform that will resize an image to exactly fit a box with width `width` and height `height` by resizing to the less constraining dimension and cropping the other. The center of the crop region is controlled by `cropOffsetX` and `cropOffsetY`.

**Parameters**  
---  
**Name** | **Description**  
`width` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
width of the bounding box  
`height` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
height of the bounding box  
`cropOffsetX` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the relative horizontal position of the center  
`cropOffsetY` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the relative vertical position of the center  
**Returns**  
---  
**Type** | **Description**  
`[Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform)` | a resize transform  
  
### makeResize(int width, int height, float cropOffsetX, float cropOffsetY)
    
    
    public static Transform makeResize(int width, int height, float cropOffsetX, float cropOffsetY)

Creates a transform that will resize an image to exactly fit a box with width `width` and height `height` by resizing to the less constraining dimension and cropping the other. The center of the crop region is controlled by `cropOffsetX` and `cropOffsetY`.

**Parameters**  
---  
**Name** | **Description**  
`width` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
width of the bounding box  
`height` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
height of the bounding box  
`cropOffsetX` | `[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the relative horizontal position of the center  
`cropOffsetY` | `[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the relative vertical position of the center  
**Returns**  
---  
**Type** | **Description**  
`[Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform)` | a resize transform  
  
### makeRotate(int degrees)
    
    
    public static Transform makeRotate(int degrees)

Creates a transform that rotates an image by `degrees` degrees clockwise.

**Parameter**  
---  
**Name** | **Description**  
`degrees` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The number of degrees by which to rotate. Must be a multiple of 90.  
**Returns**  
---  
**Type** | **Description**  
`[Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform)` | a rotation transform  
  
### makeVerticalFlip()
    
    
    public static Transform makeVerticalFlip()

Creates a transform that will vertically flip an image.

**Returns**  
---  
**Type** | **Description**  
`[Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform)` | a vertical flip transform  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
