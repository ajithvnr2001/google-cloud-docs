---
url: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-reviews/latest/V1beta.ListProductReviewsResponse
title: Google Shopping Merchant Reviews V1beta Client - Class ListProductReviewsResponse (0.6.6) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:10.810572+00:00
---

# Google Shopping Merchant Reviews V1beta Client - Class ListProductReviewsResponse (0.6.6)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/shopping-merchant-reviews/latest/V1beta.ListProductReviewsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Shopping Merchant Reviews V1beta Client - Class ListProductReviewsResponse (0.6.6) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.6 (latest)  0.6.1  0.5.3  0.4.0  0.3.1  0.2.0  0.1.2 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Shopping Merchant Reviews V1beta Client class ListProductReviewsResponse.

response message for the ListProductReviews method.

Generated from protobuf message `google.shopping.merchant.reviews.v1beta.ListProductReviewsResponse`

## Namespace

Google \ Shopping \ Merchant \ Reviews \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ product_reviews` |  `array<[ProductReview](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-reviews/latest/V1beta.ProductReview)>`   
The product review.  
`↳ next_page_token` |  `string`   
A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### getProductReviews

The product review.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[ProductReview](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-reviews/latest/V1beta.ProductReview)>` |   
  
### setProductReviews

The product review.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[ProductReview](https://docs.cloud.google.com/php/docs/reference/shopping-merchant-reviews/latest/V1beta.ProductReview)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getNextPageToken

A token, which can be sent as `page_token` to retrieve the next page.

If this field is omitted, there are no subsequent pages.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setNextPageToken

A token, which can be sent as `page_token` to retrieve the next page.

If this field is omitted, there are no subsequent pages.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
