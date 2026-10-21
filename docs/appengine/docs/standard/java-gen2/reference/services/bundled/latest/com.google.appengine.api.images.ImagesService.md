---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService
title: Interface ImagesService (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:51:39.210790+00:00
---

# Interface ImagesService (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface ImagesService (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface ImagesService

The images service provides methods to apply transformations to images.

## Static Fields 

### MAX_COMPOSITES_PER_REQUEST
    
    
    public static final int MAX_COMPOSITES_PER_REQUEST

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MAX_RESIZE_DIMENSIONS
    
    
    public static final int MAX_RESIZE_DIMENSIONS

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MAX_TRANSFORMS_PER_REQUEST
    
    
    public static final int MAX_TRANSFORMS_PER_REQUEST

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### SERVING_CROP_SIZES
    
    
    public static final Set<Integer> SERVING_CROP_SIZES

**Field Value**  
---  
**Type** | **Description**  
`[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` |   
  
### SERVING_SIZES
    
    
    public static final Set<Integer> SERVING_SIZES

**Field Value**  
---  
**Type** | **Description**  
`[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` |   
  
### SERVING_SIZES_LIMIT
    
    
    public static final int SERVING_SIZES_LIMIT

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Methods 

### applyTransform(Transform transform, Image image)
    
    
    public abstract Image applyTransform(Transform transform, Image image)

Applies the provided `transform` to the provided `image` encoding the transformed image stored using PNG file format. The transform is applied in place to the provided image.

**Parameters**  
---  
**Name** | **Description**  
`transform` | `[Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform)`  
transform to be applied  
`image` | `[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)`  
image to be transformed  
**Returns**  
---  
**Type** | **Description**  
`[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)` | transformed image  
  
### applyTransform(Transform transform, Image image, ImagesService.OutputEncoding encoding)
    
    
    public abstract Image applyTransform(Transform transform, Image image, ImagesService.OutputEncoding encoding)

Applies the provided `transform` to the provided `image` encoding the transformed image stored using `encoding` file format. The transform is applied in place to the provided image.

**Parameters**  
---  
**Name** | **Description**  
`transform` | `[Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform)`  
transform to be applied  
`image` | `[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)`  
image to be transformed  
`encoding` | `[ImagesService.OutputEncoding](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService.OutputEncoding)`  
output encoding to be used  
**Returns**  
---  
**Type** | **Description**  
`[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)` | transformed image  
  
### applyTransform(Transform transform, Image image, InputSettings inputSettings, OutputSettings outputSettings)
    
    
    public abstract Image applyTransform(Transform transform, Image image, InputSettings inputSettings, OutputSettings outputSettings)

Applies the provided `transform` to the provided `image` encoding the transformed image stored using `outputSettings` interpreting `image` according to `inputSettings`. The transform is applied in place to the provided image.

**Parameters**  
---  
**Name** | **Description**  
`transform` | `[Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform)`  
transform to be applied  
`image` | `[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)`  
image to be transformed  
`inputSettings` | `[InputSettings](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.InputSettings)`  
input settings to be used  
`outputSettings` | `[OutputSettings](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.OutputSettings)`  
output settings to be used  
**Returns**  
---  
**Type** | **Description**  
`[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)` | transformed image  
  
### applyTransform(Transform transform, Image image, OutputSettings settings)
    
    
    public abstract Image applyTransform(Transform transform, Image image, OutputSettings settings)

Applies the provided `transform` to the provided `image` encoding the transformed image stored using `settings`. The transform is applied in place to the provided image.

**Parameters**  
---  
**Name** | **Description**  
`transform` | `[Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform)`  
transform to be applied  
`image` | `[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)`  
image to be transformed  
`settings` | `[OutputSettings](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.OutputSettings)`  
output settings to be used  
**Returns**  
---  
**Type** | **Description**  
`[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)` | transformed image  
  
### applyTransformAsync(Transform transform, Image image)
    
    
    public abstract Future<Image> applyTransformAsync(Transform transform, Image image)

Asynchronously applies the provided `transform` to the provided `image` encoding the transformed image stored using PNG file format. The transform is applied in place to the provided image.

**Parameters**  
---  
**Name** | **Description**  
`transform` | `[Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform)`  
transform to be applied  
`image` | `[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)`  
image to be transformed  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)>` | A future containing the transformed image or one of the exceptions documented for [#applyTransform(Transform, Image)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService#com_google_appengine_api_images_ImagesService_applyTransform_com_google_appengine_api_images_Transform_com_google_appengine_api_images_Image_).  
  
### applyTransformAsync(Transform transform, Image image, ImagesService.OutputEncoding encoding)
    
    
    public abstract Future<Image> applyTransformAsync(Transform transform, Image image, ImagesService.OutputEncoding encoding)

Asynchronously applies the provided `transform` to the provided `image` encoding the transformed image stored using `encoding` file format. The transform is applied in place to the provided image.

**Parameters**  
---  
**Name** | **Description**  
`transform` | `[Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform)`  
transform to be applied  
`image` | `[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)`  
image to be transformed  
`encoding` | `[ImagesService.OutputEncoding](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService.OutputEncoding)`  
output encoding to be used  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)>` | A future containing the transformed image or one of the exceptions documented for [#applyTransform(Transform, Image, OutputEncoding)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService#com_google_appengine_api_images_ImagesService_applyTransform_).  
  
### applyTransformAsync(Transform transform, Image image, InputSettings inputSettings, OutputSettings outputSettings)
    
    
    public abstract Future<Image> applyTransformAsync(Transform transform, Image image, InputSettings inputSettings, OutputSettings outputSettings)

Asynchronously applies the provided `transform` to the provided `image` encoding the transformed image stored using `settings` interpreting `image` according to `inputSettings`. The transform is applied in place to the provided image.

**Parameters**  
---  
**Name** | **Description**  
`transform` | `[Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform)`  
transform to be applied  
`image` | `[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)`  
image to be transformed  
`inputSettings` | `[InputSettings](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.InputSettings)`  
input settings to be used  
`outputSettings` | `[OutputSettings](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.OutputSettings)`  
output settings to be used  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)>` | A future containing the transformed image or one of the exceptions documented for [#applyTransform(Transform, Image, InputSettings, OutputSettings)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService#com_google_appengine_api_images_ImagesService_applyTransform_com_google_appengine_api_images_Transform_com_google_appengine_api_images_Image_com_google_appengine_api_images_InputSettings_com_google_appengine_api_images_OutputSettings_).  
  
### applyTransformAsync(Transform transform, Image image, OutputSettings settings)
    
    
    public abstract Future<Image> applyTransformAsync(Transform transform, Image image, OutputSettings settings)

Asynchronously applies the provided `transform` to the provided `image` encoding the transformed image stored using `settings`. The transform is applied in place to the provided image.

**Parameters**  
---  
**Name** | **Description**  
`transform` | `[Transform](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Transform)`  
transform to be applied  
`image` | `[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)`  
image to be transformed  
`settings` | `[OutputSettings](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.OutputSettings)`  
output settings to be used  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)>` | A future containing the transformed image or one of the exceptions documented for [#applyTransform(Transform, Image, OutputSettings)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService#com_google_appengine_api_images_ImagesService_applyTransform_com_google_appengine_api_images_Transform_com_google_appengine_api_images_Image_com_google_appengine_api_images_OutputSettings_).  
  
### composite(Collection<Composite> composites, int width, int height, long color)
    
    
    public abstract Image composite(Collection<Composite> composites, int width, int height, long color)

Applies the provided [Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html) of [Composite](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Composite)s using a canvas with dimensions determined by `width` and `height` and background color `color`. Uses PNG as its output encoding.

**Parameters**  
---  
**Name** | **Description**  
`composites` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[Composite](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Composite)>`  
Compositing operations to be applied.  
`width` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Width of the canvas in pixels.  
`height` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Height of the canvas in pixels.  
`color` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Background color of the canvas in ARGB format.  
**Returns**  
---  
**Type** | **Description**  
`[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)` | A new image containing the result of composition.  
  
### composite(Collection<Composite> composites, int width, int height, long color, ImagesService.OutputEncoding encoding)
    
    
    public abstract Image composite(Collection<Composite> composites, int width, int height, long color, ImagesService.OutputEncoding encoding)

Applies the provided [Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html) of [Composite](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Composite)s using a canvas with dimensions determined by `width` and `height` and background color `color`.

**Parameters**  
---  
**Name** | **Description**  
`composites` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[Composite](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Composite)>`  
Compositing operations to be applied.  
`width` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Width of the canvas in pixels.  
`height` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Height of the canvas in pixels.  
`color` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Background color of the canvas in ARGB format.  
`encoding` | `[ImagesService.OutputEncoding](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService.OutputEncoding)`  
Encoding to be used for the resulting image.  
**Returns**  
---  
**Type** | **Description**  
`[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)` | A new image containing the result of composition.  
  
### composite(Collection<Composite> composites, int width, int height, long color, OutputSettings settings)
    
    
    public abstract Image composite(Collection<Composite> composites, int width, int height, long color, OutputSettings settings)

Applies the provided [Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html) of [Composite](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Composite)s using a canvas with dimensions determined by `width` and `height` and background color `color`.

**Parameters**  
---  
**Name** | **Description**  
`composites` | `[Collection](https://docs.oracle.com/javase/8/docs/api/java/util/Collection.html)<[Composite](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Composite)>`  
Compositing operations to be applied.  
`width` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Width of the canvas in pixels.  
`height` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Height of the canvas in pixels.  
`color` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Background color of the canvas in ARGB format.  
`settings` | `[OutputSettings](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.OutputSettings)`  
OutputSettings to be used for the resulting image.  
**Returns**  
---  
**Type** | **Description**  
`[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)` | A new image containing the result of composition.  
  
### deleteServingUrl(BlobKey blobKey)
    
    
    public abstract void deleteServingUrl(BlobKey blobKey)

Deletes a URL that was previously generated by `getServingUrl(BlobKey)`.

**Parameter**  
---  
**Name** | **Description**  
`blobKey` | `[BlobKey](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.BlobKey)`  
blob key that was previously used in the call to create the serving URL.  
  
### getServingUrl(BlobKey blobKey) (deprecated)
    
    
    public abstract String getServingUrl(BlobKey blobKey)

**Deprecated.** _Replaced by[#getServingUrl(ServingUrlOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService#com_google_appengine_api_images_ImagesService_getServingUrl_com_google_appengine_api_images_ServingUrlOptions_)._

Obtains a URL that can serve the image stored as a blob dynamically. 

This URL is served by a high-performance dynamic image serving infrastructure that is available globally. The URL returned by this method is always public, but not guessable; private URLs are not currently supported. If you wish to stop serving the URL, delete the underlying blob key. This takes up to 24 hours to take effect.

The URL format also allows dynamic resizing and crop with certain restrictions. To get dynamic resizing and cropping simply append options to the end of the url obtained via this call. Here is an example: ` getServingUrl -> "<http://lh3.ggpht.com/SomeCharactersGoesHere>"`

To get a 32 pixel sized version (aspect-ratio preserved) simply append "=s32" to the url: `"<http://lh3.ggpht.com/SomeCharactersGoesHere=s32>"`

To get a 32 pixel cropped version simply append "=s32-c": `"<http://lh3.ggpht.com/SomeCharactersGoesHere=s32-c>"`

Valid sizes are any integer in the range [0, 1600] and is available as SERVING_SIZES_LIMIT.

**Parameter**  
---  
**Name** | **Description**  
`blobKey` | `[BlobKey](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.BlobKey)`  
blob key of the image to serve by the returned URL.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | a URL that can serve the image dynamically.  
  
### getServingUrl(BlobKey blobKey, boolean secureUrl) (deprecated)
    
    
    public abstract String getServingUrl(BlobKey blobKey, boolean secureUrl)

**Deprecated.** _Replaced by[#getServingUrl(ServingUrlOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService#com_google_appengine_api_images_ImagesService_getServingUrl_com_google_appengine_api_images_ServingUrlOptions_)._

Obtains a URL that can serve the image stored as a blob dynamically. 

This URL is served by a high-performance dynamic image serving infrastructure that is available globally. The URL returned by this method is always public, but not guessable; private URLs are not currently supported. If you wish to stop serving the URL, delete the underlying blob key. This takes up to 24 hours to take effect.

The URL format also allows dynamic resizing and crop with certain restrictions. To get dynamic resizing and cropping simply append options to the end of the url obtained via this call. Here is an example: ` getServingUrl -> "<http://lh3.ggpht.com/SomeCharactersGoesHere>"`

To get a 32 pixel sized version (aspect-ratio preserved) simply append "=s32" to the url: `"<http://lh3.ggpht.com/SomeCharactersGoesHere=s32>"`

To get a 32 pixel cropped version simply append "=s32-c": `"<http://lh3.ggpht.com/SomeCharactersGoesHere=s32-c>"`

Valid sizes are any integer in the range [0, 1600] and is available as SERVING_SIZES_LIMIT.

**Parameters**  
---  
**Name** | **Description**  
`blobKey` | `[BlobKey](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.BlobKey)`  
blob key of the image to serve by the returned URL.  
`secureUrl` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
controls if the url scheme should be https or http.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | a URL that can serve the image dynamically.  
  
### getServingUrl(BlobKey blobKey, int imageSize, boolean crop) (deprecated)
    
    
    public abstract String getServingUrl(BlobKey blobKey, int imageSize, boolean crop)

**Deprecated.** _Replaced by[#getServingUrl(ServingUrlOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService#com_google_appengine_api_images_ImagesService_getServingUrl_com_google_appengine_api_images_ServingUrlOptions_)._

Calculates the serving URL for specific size and crop parameters from generic URL returned by [#getServingUrl(BlobKey)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService#com_google_appengine_api_images_ImagesService_getServingUrl_com_google_appengine_api_blobstore_BlobKey_). See Also: [ImagesService#getServingUrl(BlobKey)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService#com_google_appengine_api_images_ImagesService_getServingUrl_com_google_appengine_api_blobstore_BlobKey_)

**Parameters**  
---  
**Name** | **Description**  
`blobKey` | `[BlobKey](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.BlobKey)`  
blob key of the image to serve by the returned URL with specified size and crop.  
`imageSize` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
size of the served image in pixels.  
`crop` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
controls whether the image should be resized or cropped.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | a URL that can serve the image dynamically.  
  
### getServingUrl(BlobKey blobKey, int imageSize, boolean crop, boolean secureUrl) (deprecated)
    
    
    public abstract String getServingUrl(BlobKey blobKey, int imageSize, boolean crop, boolean secureUrl)

**Deprecated.** _Replaced by[#getServingUrl(ServingUrlOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService#com_google_appengine_api_images_ImagesService_getServingUrl_com_google_appengine_api_images_ServingUrlOptions_)._

Calculates the serving URL for specific size and crop parameters from generic URL returned by [#getServingUrl(BlobKey)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService#com_google_appengine_api_images_ImagesService_getServingUrl_com_google_appengine_api_blobstore_BlobKey_). See Also: [ImagesService#getServingUrl(BlobKey)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService#com_google_appengine_api_images_ImagesService_getServingUrl_com_google_appengine_api_blobstore_BlobKey_)

**Parameters**  
---  
**Name** | **Description**  
`blobKey` | `[BlobKey](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.BlobKey)`  
blob key of the image to serve by the returned URL with specified size and crop.  
`imageSize` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
size of the served image in pixels.  
`crop` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
controls whether the image should be resized or cropped.  
`secureUrl` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
controls if the url scheme should be https or http.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | a URL that can serve the image dynamically.  
  
### getServingUrl(ServingUrlOptions options)
    
    
    public abstract String getServingUrl(ServingUrlOptions options)

Obtains a URL that can dynamically serve the image stored as a blob. 

This URL is served by a high-performance dynamic image serving infrastructure that is available globally. The URL returned by this method is always public, but not guessable; private URLs are not currently supported. If you wish to stop serving the URL, delete the underlying blob key. This takes up to 24 hours to take effect.

The URL format also allows dynamic resizing and crop with certain restrictions. To get dynamic resizing and cropping simply append options to the end of the url obtained via this call. Here is an example: ` getServingUrl -> "<http://lh3.ggpht.com/SomeCharactersGoesHere>"`

To get a 32 pixel sized version (aspect-ratio preserved) simply append "=s32" to the url: `"<http://lh3.ggpht.com/SomeCharactersGoesHere=s32>"`

To get a 32 pixel cropped version simply append "=s32-c": `"<http://lh3.ggpht.com/SomeCharactersGoesHere=s32-c>"`

Valid sizes are any integer in the range [0, 1600] (maximum is available as [#SERVING_SIZES_LIMIT](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService#com_google_appengine_api_images_ImagesService_SERVING_SIZES_LIMIT)).

**Parameter**  
---  
**Name** | **Description**  
`options` | `[ServingUrlOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ServingUrlOptions)`  
Specific options for generating the serving URL.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | a URL that can serve the image dynamically.  
  
### histogram(Image image)
    
    
    public abstract int[][] histogram(Image image)

Calculates the histogram of the image.

**Parameter**  
---  
**Name** | **Description**  
`image` | `[Image](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image)`  
image for which to calculate a histogram  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)[][]` | An array of 3 arrays of length 256, each containing the image histogram for one color channel. The channels are ordered RGB from entry 0 to 3. Each channel ranges from 0 where the color is not present to 255 where the color is fully bright.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
