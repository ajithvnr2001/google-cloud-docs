---
url: https://docs.cloud.google.com/cdn/docs/imageoptimization/
title: Image optimization Overview \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:53.998361+00:00
---

# Image optimization Overview  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/imageoptimization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Image optimization Overview Stay organized with collections  Save and categorize content based on your preferences. 

## What is image optimization?

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Image optimization is the process of modifying and delivering high-quality images in the optimal format, dimensions, and resolution for the device accessing them. Resizing, compressing, and selecting the right file formats, it dramatically reduces image file sizes without compromising visual quality. Unoptimized images are unnecessarily large, forcing users to download extra data. Optimizing images helps your pages load faster, which improves the user experience and keeps visitors on your website longer.

Cloud CDN image optimization lets you dynamically transform your images. Image optimization offloads compute-intensive image transformations from your origin servers, which reduces compute and data egress costs while improving page load times and SEO rankings.

This page describes how to configure Cloud CDN image optimization to process and deliver images directly from the network edge.

Image optimization lets you use explicit URL query parameters for granular, real-time control over image attributes, such as resizing, cropping, and format conversion.

Image optimization is an output caching solution. The service processes an image on its first request for a specific transformation and caches the resulting variant at the edge. Subsequent requests for the same parameters are served directly from the CDN cache.

## Key benefits

  * **Enhanced web performance** : delivers resized, high-quality images directly from Google's global edge network, reducing Page Load Time and Time to Interactive (TTI).

  * **Lower Total Cost of Ownership (TCO)** : on-the-fly transformations significantly reduce egress bandwidth costs by serving lighter, highly compressed images.

  * **Secure image transformations** : prevents unauthorized image tampering, DDoS exploits, or compute-draining requests through seamless integration with [Service Extensions](https://docs.cloud.google.com/service-extensions/docs/overview) and Cloud CDN [Signed URLs](https://docs.cloud.google.com/cdn/docs/using-signed-urls).




Use the following guides to get started with Cloud CDN image optimization:

  * [Getting started](https://docs.cloud.google.com/cdn/docs/configure-image-optimization): to configure image optimization, understand supported input and output image formats and request syntax.
  * [Supported operations](https://docs.cloud.google.com/cdn/docs/image-opt-supportedops): to understand all the supported formats, their attributes and examples.
  * [Limitations](https://docs.cloud.google.com/cdn/docs/image-opt-limitations): to know about the image optimization limitations and threshold values.
  * [Image optimization use cases](https://docs.cloud.google.com/cdn/docs/image-opt-use-cases): to understand the behavior of image transformations, order of transformation, caching and more.
  * [Securing image transformation requests](https://docs.cloud.google.com/cdn/docs/image-opt-security): to know about security considerations for Cloud CDN image optimization.
  * [Troubleshoot and Best Practices](https://docs.cloud.google.com/cdn/docs/image-opt-monitor-troubleshoot): to know about how to monitor the logs and troubleshoot common issues.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
