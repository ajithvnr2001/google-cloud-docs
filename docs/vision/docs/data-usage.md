---
url: https://docs.cloud.google.com/vision/docs/data-usage/
title: Data Usage FAQ \u00a0|\u00a0 Cloud Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:23.838310+00:00
---

# Data Usage FAQ  |  Cloud Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/data-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Resources ](https://docs.cloud.google.com/vision/docs/resources)



Send feedback 

#  Data Usage FAQ Stay organized with collections  Save and categorize content based on your preferences. 

Does Google use the image I send to the Vision API?
    Google does not use any of your content (such as images and labels) for any purpose except to provide you with the Vision API service.
Will Google share the image I send to the Vision API?
    We won't make the content that you send available to the public. We won't share the content with any third party. The content is only used by Google as necessary to provide the Vision API service. Vision API complies with the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum). 
Will the image I send to the Vision API, the results or other information about the request itself, be stored on Google servers? If so, how long and where is the information kept, and do I have access to it?
     For online (immediate response) operations (`BatchAnnotateImages` and `BatchAnnotateFiles`), the image data is processed in memory and not persisted to disk. 
     For asynchronous offline batch operations (`AsyncBatchAnnotateImages` and `AsyncBatchAnnotateFiles`), we must store that image for a short period of time in order to perform the analysis and return the results to you. The stored image is typically deleted right after the processing is done, with a failsafe [Time to live (TTL)](https://en.wikipedia.org/wiki/Time_to_live) of a few hours. 
     Google also temporarily logs some metadata about your Vision API requests (such as the time the request was received and the size of the request) to improve our service and combat abuse. 
**Note:** For more information, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek) in the Cloud KMS documentation. How does Google protect and ensure the security of the data I send to Vision API?
    Refer to the [Google Cloud Security](https://cloud.google.com/security) page which describes the security measures in place for Google Cloud Services.
Does Google use my data for improving Cloud Vision?
    Google does not use the content you send to train and improve our Cloud Vision features such as its machine perception model.
Does Google claim ownership of the content I send in the request to Vision API?
    Google does not claim any ownership in any of the content that you transmit to the Vision API. 
Can I resell the Vision API?
    No, you are not permitted to resell the Vision API service. However, you can use Vision API features as a component to solutions you offer to your end customers. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
