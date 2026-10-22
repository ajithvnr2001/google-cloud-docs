---
url: https://docs.cloud.google.com/cdn/docs/image-opt-use-cases/
title: Image optimization use cases \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:53.950702+00:00
---

# Image optimization use cases  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/image-opt-use-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Image optimization use cases Stay organized with collections  Save and categorize content based on your preferences. 

This page provides examples for advanced image processing behavior, pipeline ordering effects, and automatic image normalization rules.

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Order of transformations

Operations in the `imop` query parameter string run sequentially from left to right with an exception of `metadata` or `scale` running first and `canvas` running last. Because every operation acts directly on the visual output of the preceding operation, the sequence of your parameters affects the final visual quality and detail preservation of the derivative image.

Consider a source image that is _1,000_ pixels wide by _1,000_ pixels high:

**Example:`Resize` then `Crop`**

`https://www.example.com/image.jpg?imop=Resize,width=200;Crop,left=0.5`

  1. **Resize** : The original 1000×1000 px image is resized to **200×200 px** (preserving the 1:1 aspect ratio).

  2. **Crop** : the `left=0.5` operation crops out the left half of the already-resized image.




**Result** : A **100 x 200 px** image representing the right 50% of the content.

**Example :`Crop` then `Resize`**

`https://www.example.com/image.jpg?imop=Crop,left=0.5;Resize,width=200`

  1. **Crop** : The `left=0.5`operation extracts the right 50% of the high-resolution source image first, creating a `500 x 1000 px` intermediate image (changing the aspect ratio to 1:2).

  2. **Resize** : The `width=200` parameter resizes this intermediate image. To preserve the new 1:2 aspect ratio, the height scales to **400 px**.




**Result** : A **200 * 400 px** final image.

## Stretch and upscaling behavior

By default, the image optimization service enforces a strict, downscale-only strategy to conserve edge delivery bandwidth and protect visual quality. If you request dimensions larger than the original image, Cloud CDN ignores the enlargement and outputs the image at its original size.

To override this behavior and force an asset to upscale, you must explicitly declare the `stretch` value.

**Validation requirements for upscaling**

  * **Dual sizing rule** : the `stretch` value is permitted only if you explicitly provide both the `width` and `height` parameters in the `Resize` operation

  * **Single dimension constraint** : If you include `scaling=stretch` while defining only a single dimension, such as `width` or `height`, image optimization service rejects the entire request.




For example,

**Valid request** : `?imop=resize,width=500,height=500,scaling=stretch`

**Invalid request** : `?imop=resize,width=500, scaling=stretch`

## Caching and cache invalidation

When you update an original image on your origin server, you must invalidate the cached version to ensure Cloud CDN retrieves and serves the updated asset.

### Caching behavior

Every unique combination of transformation parameters appended to an image URL creates a separate, distinct cache entry at the edge. To optimize your cache-hit ratio, avoid creating excessive numbers of unique parameter variations. For example, single-pixel changes.

Cloud CDN normalizes cache keys to group identical transformation parameters regardless of their order in the query string.

### Invalidation behavior

When you update an original image on your origin server, you only need to submit a single invalidation request for the base image URL. The enhanced Cloud CDN automatically purges both the cached original image and all of its automatically generated variants (such as WebP or optimized versions) globally.

**How Variant Invalidation Works**

When you issue a cache invalidation request using a path pattern that matches a base image URL, for example,`/images/my-picture.jpg`, Cloud CDN automatically identifies and purges:

  * The original cached source image.

  * All of its previously generated variants




You can apply Cloud CDN cache invalidation using:

  * Google Google Cloud console: navigate to Network Services > [Cloud CDN](https://docs.cloud.google.com/cdn/docs/invalidating-cached-content#invalidate_only_one_file), select the origin, and go to the **Cache Invalidation** tab. Alternatively, go to Network Services > Load Balancing, select your load balancer, and use the **Cache Invalidation** tab.

  * Google Cloud CLI: use the `Google Cloud CLI compute url-maps invalidate-cdn-cache` command.

  * Cache Tags : Cache tags is the recommended approach for managing optimized images. This lets you issue invalidation requests targeting a specific tag, which purges the content associated with it for more granular control.




For example:

To invalidate `/images/my-picture.jpg` and all of its optimized variants globally:

  * Path: specify the exact path `/images/my-picture.jpg`.

  * Host (Optional): specify the host if you only want to clear the image for a specific domain.




When submitted, this single action removes all optimized versions of the image from edge caches globally, ensuring users immediately receive the updated version on their next request.

## Color profile and image orientation in EXIF (normalization)

Modern smartphones and digital cameras frequently save images with raw, unrotated pixel grids and rely on an embedded EXIF orientation tag to to instruct the viewing device to rotate the image. For example, 90 degrees clockwise for portrait orientation. Similarly, embedded ICC color profiles define how colors display across different monitors.

To help ensure predictable operations, the image optimization edge pipeline automatically normalizes images before running any transformations.

## Normalization process

  * Prior to executing transformations, the edge engine reads EXIF orientation tags and ICC color profile metadata and physically applies them to the pixel grid. This helps ensure coordinate predictability for subsequent `crop` and `resize` parameters.

  * Operations, such as `crop`, `resize` or `scale` execute correctly against the true visual dimensions to prevent visual errors.

  * After applying adjustments to the core pixels, the edge engine removes all non-essential metadata from the file to maximize size savings. By default, it retains `copyright` unless a specific value is requested in metadata operation.




## What's next

  * [Securing image transformation requests](https://docs.cloud.google.com/cdn/docs/image-opt-security)
  * [Troubleshoot and Best Practices](https://docs.cloud.google.com/cdn/docs/image-opt-monitor-troubleshoot)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
