---
url: https://docs.cloud.google.com/vision/docs/cmek/
title: CMEK compliance in Vision API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:21.888394+00:00
---

# CMEK compliance in Vision API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/docs/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Vision API ](https://docs.cloud.google.com/vision/docs)
  * [ Resources ](https://docs.cloud.google.com/vision/docs/resources)



Send feedback 

#  CMEK compliance in Vision API Stay organized with collections  Save and categorize content based on your preferences. 

By default, Google Cloud automatically [encrypts data when it is at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) using encryption keys managed by Google.

Vision API has two batch asynchronous annotation requests: [AsyncBatchAnnotateImages](https://docs.cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#google.cloud.vision.v1.ImageAnnotator.AsyncBatchAnnotateImages) and [AsyncBatchAnnotateFiles](https://docs.cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#google.cloud.vision.v1.ImageAnnotator.AsyncBatchAnnotateFiles). These methods store your data on disk internally during processing (see the [Data Usage FAQ](https://docs.cloud.google.com/vision/docs/data-usage) for more information). The rest of this topic describes CMEK compliance in Vision API, and how this temporary data is protected at rest. For more information about CMEK in general, see the [Cloud Key Management Service documentation about CMEK](https://docs.cloud.google.com/kms/docs/cmek).

## How CMEK compliance works in Vision API

In Vision API, batch annotation request methods are either synchronous or asynchronous.

  * Synchronous Vision API methods don't persist data to disk and thus are automatically CMEK-compliant, with no configuration required:

    * [BatchAnnotateImages](https://docs.cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#google.cloud.vision.v1.ImageAnnotator.BatchAnnotateImages)
    * [BatchAnnotateFiles](https://docs.cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#google.cloud.vision.v1.ImageAnnotator.BatchAnnotateFiles)
  * Asynchronous Vision API methods do persist data to disk temporarily (see [Data Usage FAQ](https://docs.cloud.google.com/vision/docs/data-usage)). These methods are automatically CMEK-compliant, with no configuration required:

    * [AsyncBatchAnnotateImages](https://docs.cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#google.cloud.vision.v1.ImageAnnotator.AsyncBatchAnnotateImages)
    * [AsyncBatchAnnotateFiles](https://docs.cloud.google.com/vision/docs/reference/rpc/google.cloud.vision.v1#google.cloud.vision.v1.ImageAnnotator.AsyncBatchAnnotateFiles)



Before Vision API writes data to disk, the data is automatically encrypted using an ephemeral key called a data-encryption key (DEK). A new DEK is automatically generated for each asynchronous annotation request.

The DEK itself is encrypted by another key called the key encryption key (KEK). The KEK is not accessible to Google engineers or support staff.

When the ephemeral key (DEK) that was used to encrypt its temporary data is destroyed, the temporary data can no longer be accessed, even if the data hasn't been deleted yet.

Vision API writes the results of a batch annotation request to your Cloud Storage bucket, which also has support for CMEK. It is recommended to set up a [default encryption key](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#using_default_encryption_keys) on your input and output buckets.

**Note:** CMEK keys are not supported for [Product Search](https://docs.cloud.google.com/vision/product-search/docs).

For more information about data usage in Vision API, see the [Data Usage FAQ](https://docs.cloud.google.com/vision/docs/data-usage).

## What's next?

  * Learn more about [Batch annotation requests](https://docs.cloud.google.com/vision/docs/batch)
  * Learn more about [CMEK](https://docs.cloud.google.com/kms/docs/cmek)
  * Learn more about [Cloud KMS](https://docs.cloud.google.com/kms/docs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
