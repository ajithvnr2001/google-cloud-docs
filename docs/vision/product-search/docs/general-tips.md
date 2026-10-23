---
url: https://docs.cloud.google.com/vision/product-search/docs/general-tips/
title: General tips \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:05.236878+00:00
---

# General tips  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/general-tips/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)
  * [ Support ](https://docs.cloud.google.com/vision/product-search/docs/general-tips)



Send feedback 

#  General tips Stay organized with collections  Save and categorize content based on your preferences. 

This page describes troubleshooting steps that you might find helpful if you run into problems using Vision API Product Search.

### Search results

#### What is the maximum number of results returned?

The maximum number of results returned will vary from query to query due to implementation details. The maximum guaranteed amount of results returned is 500. If more are requested, the requested number may not be met. 

#### Can I set a score threshold for results?

The search result scores are not calibrated. This means that the result scores for a given query will be comparable (this is how results are ranked). However, the result scores for query A and query B are _not necessarily_ comparable. This means there is no one fixed threshold suitable for a given use case.

It is possible to set a threshold based on your own experiments. If you want to set a threshold, you should set this threshold on a per item label basis. This means that you should set a results score threshold for "Shoes" independently of "Bags", etc. for each label. 

#### Is there a way to know why a particular result was ranked higher than another?

Currently the Vision API Product Search does not support any features that explain why a particular result was returned. 

#### What is the difference between using `productGroupedResults` and using the Object Localizer feature of the Vision API?

The `productGroupedResults` response will return a list of detected items, their predicted label and score, their bounding boxes, and a ranked list of product search results for each item. This response is equivalent to first sending the query image to the Object Localizer feature of the Vision API and then sending the image along with each product item bounding box (filtered to the relevant labels) to Vision API Product Search.

One benefit of using `productGroupedResults` is that it is faster and more direct because it only makes a single API call. However, if there is some custom application logic that needs to be implemented between the object detection and the search query then a two step method is a good approach. An example of such a case would be adding Vision API Product Search filters based on object labels. 

#### If I know the location of a product in an image should I crop the image before querying the API with it?

This situation might arise if, for example, a user is allowed to draw a bounding box around the item that they want to search. In general you should not crop the image before sending it to the API. The reason is that our API will use both the query bounding box to return targeted results as well as the overall image context, which is frequently helpful for improving the results. 

### Reference images

#### What are good product reference images?

Good reference images show the product clearly and do not have any other objects in the image. A typical example of good reference images are ["packshot"](https://en.wikipedia.org/wiki/Packshot) images. These images are frequently used to show the user a product on the product page or in advertising, and typically taken in front of a white background. Images of the product in other environments also make good reference images provided there are not any other products in the image. You should use all such images that are available for reference images. 

#### What is the ideal image size for reference images and images you use to search for products? 

An ideal image focuses on the product, and the product fills the majority of the image ; images containing only a small or unclear representation of a product will produce less desirable results. Consequently, the apparent size of the product in the image matters more than specific image size. However, as a _general_ recommendation, use images with 600 pixels or more on the largest side for reference and search images. 

#### What is the optimal number of reference images for a particular product?

The Vision API Product Search can work well even with only one reference image of a product. Typically 3 to 8 images provide necessary information to get proper results from the Vision API Product Search, especially if these images have some variations. Such variations include different orientations of the product, different lighting, or a different background. Additional reference images can be added to the index, and should not generally decrease accuracy.

#### How can I get more reference images for my products?

The best way to improve the accuracy of Vision API Product Search is to add more good reference images for products. If you have already uploaded a representative set of product images and you'd still like to increase the accuracy for some products you can use other existing images or collect more images for those products. 

To use other existing images make sure they clearly show the product and don't have other distracting objects. For example, you might have photos of a model wearing a particular shirt along with pants. This image _alone_ wouldn't be a good reference image for the shirt product. However, if you provide a bounding box around the shirt or crop the image to only include the shirt it would be a good reference image. You can use the Vision API's [Object Localizer](https://docs.cloud.google.com/vision/docs/object-localizer) feature to propose boxes. This method can be used alongside or instead of human-provided bounding box annotations. 

#### Would it help the accuracy of the API to add data augmentations to my product set?

The idea of adding augmented versions of existing reference images (for example, left-right flips, jittered contrast, etc.) is sensible, but typically does little to increase the accuracy. 

### Data management

#### What is the recommended way to update a product set in production?

Update your product set with new products as your inventory changes. If the changes are small you can add or delete products as needed. Alternatively, if there is a significant change in your inventory or in your reference images you can create a new product set with the changes and test the search quality before fully switching over to the new set. In either case, you should keep track of which products and image are in your product set by saving your batch import CSV file for easy reference or rollback. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
