---
url: https://docs.cloud.google.com/cdn/docs/image-opt-monitor-troubleshoot/
title: Monitor and troubleshoot \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:29.377243+00:00
---

# Monitor and troubleshoot  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/image-opt-monitor-troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Monitor and troubleshoot Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the troubleshooting scenarios and best practices for using Cloud CDN image optimization.

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Troubleshooting

Scenario | Troubleshooting steps  
---|---  
Images are not optimized and are served without changes | 

  * Verify that you have enabled image optimization in the URL map for the given route.
  * Verify that the `content-type` header in the response is a supported image format.

  
Images are not optimized and return errors | 

  * Verify that the image is within the maximum size limits.
  * If the operation times out, verify the image size and the number of operations that you are trying to apply, and then retry the operation. If the problem persists, contact Google Cloud Support.

  
  
## Best practices

To maximize the benefits of image optimization, follow these best practices:

  * **Optimize version count** : limit the number of unique variations, such as resolutions, that you create for a single image. Creating too many versions can reduce cache efficiency and lower the overall cache hit ratio.

  * **Preprocess complex images** : for exceptionally large images or complex transformations, consider preprocessing before you serve them. Real-time processing of these images might affect performance.

  * **Manage request velocity** : image processing is CPU-intensive; although Cloud CDN image optimization is designed to scale, sudden high volumes can impact performance.

  * **Secure endpoints** : implement signed URLs to restrict transformation requests to authorized clients, which protects your origin and caching infrastructure from unwanted processing loads.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
