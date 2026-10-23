---
url: https://docs.cloud.google.com/vision/product-search/docs/release-notes/
title: Vision API Product Search release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:40:56.491068+00:00
---

# Vision API Product Search release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/release-notes/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)
  * [ Resources ](https://docs.cloud.google.com/vision/product-search/docs/resources)



Send feedback 

#  Vision API Product Search release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Vision API Product Search. We recommend that Vision API Product Search developers periodically check this list for any new announcements. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/visionproductsearch-release-notes.xml) directly. 

## March 19, 2023

Change

**Product Search legacy category migration**

The legacy categories `"apparel"`, `"homegoods"`, and `"toys"` have been upgraded. See the December 5, 2022 release note for more information.

## December 05, 2022

Change

**Product Search legacy category migration**

In 90 days, the legacy categories `"apparel"`, `"homegoods"`, and `"toys"` will be upgraded. You will still be able to use these categories. However, when running searches, they will perform similar to the `"apparel-v2"`, `"homegoods-v2"`, and `"toys-v2"` categories.

## September 18, 2019

Feature

**Packaged goods and general vertical** :

The following product categories have been updated or added for General Availability:

  * `packagedgoods-v1` (updated)
  * `general-v1` (added)



Feature

**Batch deletion**

Batch deletion is now offered for the following product types:

  * All products in a specific product set
  * All products not in any product set



See the ["Deleting resources"](https://docs.cloud.google.com/vision/product-search/docs/delete-resources#batch_resource_deletion) topic for more information.

Change

**Model update** : The Object Localizer model has been updated.

Change

Responses to `images:annotate` requests now include an [`objectAnnotation`](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1/AnnotateImageResponse#objectannotation) field with a label for the object defined by the bounding box indicated. See the ["Searching for products"](https://docs.cloud.google.com/vision/product-search/docs/searching) topic for more information.

Change

**VPC Service Controls**

Vision Product Search VPC Service Controls provide additional security for your pipeline's resources and services. To learn more about VPC Service Controls, see the [VPC Service Controls overview](https://docs.cloud.google.com/vpc-service-controls/docs/overview). 

To learn about the limitations of using Vision Product Search with VPC Service Controls, see the [supported products and limitations](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products).

## June 07, 2019

Feature

**Packaged goods vertical** : Adds support for a `packagedgoods-v1` product category in addition to other [supported product categories](https://docs.cloud.google.com/vision/product-search/docs/product-categories).

Change

The following product categories have been updated:

  * `homegoods-v2`
  * `apparel-v2`
  * `toys-v2`



The corresponding legacy categories (`homegoods`, `apparel`, and `toys`) are still supported, but the updated categories should be used for new products.

## December 10, 2018

Feature

**Cloud Vision API Product Search General Availability (GA) Release**

Feature

**Toys vertical** : Adds support for a `toys` product category in addition to other [supported product categories](https://docs.cloud.google.com/vision/product-search/docs/product-categories).

Feature

**Multi-detection** : Detects [multiple products](https://docs.cloud.google.com/vision/product-search/docs/searching-response#multiple-product_images_multi-detection_response) in an image, and then provides similar products to each product found.

## July 24, 2018

Feature

**Beta Release of Vision Product Search**

The Beta version of Vision Product Search is now available.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
