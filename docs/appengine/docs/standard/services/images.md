---
url: https://docs.cloud.google.com/appengine/docs/standard/services/images/
title: Images API for legacy bundled services \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:45.738331+00:00
---

# Images API for legacy bundled services  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Images API for legacy bundled services Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

**Note:** To modernize image processing, we recommend that you [migrate from the App Engine Images service to Cloud Run](https://docs.cloud.google.com/appengine/migration-center/standard/python/images-to-cloud-run) by routing calls to a Cloud Run image transformation service.

App Engine provides the ability to manipulate image data using a dedicated Images service. The Images service can manipulate images, composite multiple images into a single image, convert image formats, provide image metadata such as format, width, height, and a histogram of color values.

The Images service can accept image data directly from the app, or it can use a [Cloud Storage](https://docs.cloud.google.com/storage) value. (The Images service can also use a [Cloud Blobstore](https://docs.cloud.google.com/appengine/docs/standard/services/blobstore) value, but we recommend the use of Cloud Storage.)

Images stored in Cloud Storage and Cloud Blobstore can be up to the maximum allowed value for the respective service. The transformed image is returned directly to the app, and must be less than 32 megabytes.

Cloud Storage buckets **must** use fine-grained [Access Control Lists](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists) for the Images API to work. For buckets that have been configured for uniform bucket-level access, the Images API will not be able to fetch images in that bucket and throws the error message `TransformationError`. If your bucket is configured in this manner, you can [disable uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access#set).

When you serve images from Cloud Storage, the Images API uses a Google-managed service account, `dynamic_image_service@system.gserviceaccount.com`, to fetch the image. This is normally done for you, but if this service account doesn't have the `Storage Object Viewer` role on the bucket, you might experience intermittent `403 Forbidden` errors. This happens when the image isn't available in Google's serving cache and needs to be fetched from the origin bucket.

To grant the required permission, run the following `gcloud` command:
    
    
    gcloud storage buckets add-iam-policy-binding gs://[BUCKET_NAME] \
      --member=serviceAccount:dynamic_image_service@system.gserviceaccount.com \
      --role=roles/storage.objectViewer
    

## Image Service API

## Available image transformations

The Images service can resize, rotate, flip, and crop images, and enhance photographs. It can also composite multiple images into a single image.

#### Resize

You can resize the image while maintaining the same aspect ratio. Neither the width nor the height of the resized image can exceed 4000 pixels.

![](https://docs.cloud.google.com/static/appengine/docs/images/services/images/transform_before.jpg)![](https://docs.cloud.google.com/static/appengine/docs/images/services/images/transform_resize_after.jpg)

#### Rotate

You can rotate the image in 90 degree increments.

![](https://docs.cloud.google.com/static/appengine/docs/images/services/images/transform_before.jpg)![](https://docs.cloud.google.com/static/appengine/docs/images/services/images/transform_rotate_after.jpg)

#### Flip horizontally

You can flip the image horizontally.

![](https://docs.cloud.google.com/static/appengine/docs/images/services/images/transform_before.jpg)![](https://docs.cloud.google.com/static/appengine/docs/images/services/images/transform_fliph_after.jpg)

#### Flip vertically

You can flip the image vertically.

![](https://docs.cloud.google.com/static/appengine/docs/images/services/images/transform_before.jpg)![](https://docs.cloud.google.com/static/appengine/docs/images/services/images/transform_flipv_after.jpg)

#### Crop

You can crop the image with a given bounding box.

![](https://docs.cloud.google.com/static/appengine/docs/images/services/images/transform_before.jpg)![](https://docs.cloud.google.com/static/appengine/docs/images/services/images/transform_crop_after.png)

#### I'm Feeling Lucky

The "I'm Feeling Lucky" transform enhances dark and bright colors in an image and adjusts both color and optimizes contrast.

![](https://docs.cloud.google.com/static/appengine/docs/images/services/images/transform_before.jpg)![](https://docs.cloud.google.com/static/appengine/docs/images/services/images/transform_lucky_after.png)

## Image formats

The service accepts image data in the JPEG, PNG, WEBP, GIF (including animated GIF), BMP, TIFF and ICO formats. Transformed images can be returned in the JPEG, WEBP and PNG formats.

If the input format and the output format are different, the service converts the input data to the output format before performing the transformation.

**Note:** The Images service does not support multilayer TIFF images.

## Transforming images

The Images service can use a value from [Cloud Storage](https://docs.cloud.google.com/appengine/docs/standard/using-cloud-storage) or [Blobstore](https://docs.cloud.google.com/appengine/docs/standard/services/blobstore) as the image source for a transformation. You have two ways to transform images:

  1. Using the [`Image()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/Image) class allows you to perform simple image transformations, such as crop, flip, and rotate.
  2. Using [get_serving_url()](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/get_serving_url) allows you to dynamically resize and crop images, so you don't need to store different image sizes on the server. This method returns a URL that serves the image, and transformations to the image are encoded in this URL. This function assumes that the image doesn't change; if it gets modified after you get the URL, you may get unexpected results from using the URL.



### Using the `Image()` Class

You can transform images from Cloud Storage or Blobstore if the image size is smaller than the maximum allowed by Cloud Storage or Blobstore. Note that the result of the transformation is returned directly to the app, and must not exceed the API response limit of 32 megabytes.

To transform an image from Cloud Storage or Blobstore, instead of setting the `image_data` argument of the [Image](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images) constructor with the image data, set the `blob_key` argument to the Blobstore key whose value is the image. The rest of the API behaves as expected. The `execute_transforms()` method returns the result of the transforms, or throws a `LargeImageError` if the result is larger than the maximum size of 32 megabytes. 

### Using `get_serving_url()`

**Important:** When you [migrate the Images service to Cloud Run](https://docs.cloud.google.com/appengine/migration-center/standard/python/images-to-cloud-run) with `APPENGINE_USE_CUSTOM_IMAGES_GRPC_SERVICE` set to `true`, you can't generate serving URLs. App Engine throws a runtime exception when you invoke `get_serving_url()` . This restriction prevents reliance on the legacy backend for storing and serving images. To host and serve images, store them in a [Cloud Storage](https://docs.cloud.google.com/storage/docs) bucket or distribute them using [Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview). Existing URLs created with legacy calls to `get_serving_url()` continue to serve images.

The [get_serving_url()](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/get_serving_url) method lets you generate a fixed, dedicated URL for an image that is stored in Cloud Storage or Blobstore. 

The generated URL uses highly-optimized image serving infrastructure that is separate from your application. As the image is served independently from your app, it does not generate load and can be highly cost effective. The URL returned by this method is always publicly accessible but not guessable.

If you wish to stop serving the URL, delete it using the [`delete_serving_url()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/delete_serving_url) function. 

The method returns a URL encoded with the specified size and crop arguments. If you do not specify any arguments, the method returns the default URL for the image, for example:
    
    
    http://lhx.ggpht.com/randomStringImageId
    

You can resize and crop the image dynamically by specifying the arguments in the URL. The available arguments are:

  * `=sxx` where `xx` is an integer from 0–2560 representing the length, in pixels, of the image's longest side. For example, adding `=s32` resizes the image so its longest dimension is 32 pixels.
  * `=sxx-c` where **xx** is an integer from 0–2560 representing the cropped image size in pixels, and `-c` tells the system to crop the image.

**Important:** Only the resize and crop arguments listed above are supported. Using any other arguments might result in breaking failures.
    
    
    # Resize the image to 32 pixels (aspect-ratio preserved)
    http://lhx.ggpht.com/randomStringImageId=**s32**
    
    # Crop the image to 32 pixels
    http://lhx.ggpht.com/randomStringImageId=**s32-c**
    

## Images and the development server

The development server uses your local machine to perform the capabilities of the Images service.

You can use [Pillow](https://python-pillow.org/) or a [Python interface](https://imagemagick.org/script/develop.php#python) for ImageMagick to resize, convert, and manipulate images.

## A note about deletion

To stop serving an image stored in Cloud Storage or Blobstore call the [`delete_serving_url()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/images/delete_serving_url) function. 

You should avoid directly deleting images in Cloud Storage or Blobstore as doing so can leave them accessible through the serving URL.

Serving URLs will stop working if the application that created them is disabled or deleted, even if the underlying image remains available.

## Quotas, limits, and pricing

There is currently no additional charge incurred by using the Images API. See the App Engine [pricing page](https://cloud.google.com/appengine/pricing#Billable_Resource_Unit_Costs).

Each Images API request counts toward the **Image Manipulation API Calls** quota. An app can perform multiple transformations of an image in a single API call.

Data sent to the Images service counts toward the **Data Sent to (Images) API** quota. Data received from the Images service counts toward the **Data Received from (Images) API** quota.

Each transformation of an image counts toward the **Transformations Executed** quota.

For more information, see [Quotas](https://docs.cloud.google.com/appengine/docs/quotas). You can see the current quota usage of your app by visiting the [Google Cloud console Quota Details](https://console.cloud.google.com/project/_/appengine/quotadetails) tab.

In addition to quotas, the following limits apply to the use of the Images service:

Limit | Amount  
---|---  
maximum data size of image sent to service | 32 megabytes  
maximum data size of image received from service | 32 megabytes  
maximum size of image sent or received from service | 50 megapixels  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
