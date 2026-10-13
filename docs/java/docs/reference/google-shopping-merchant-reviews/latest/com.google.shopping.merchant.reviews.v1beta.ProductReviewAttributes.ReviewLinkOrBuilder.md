---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReviewAttributes.ReviewLinkOrBuilder
title: Interface ProductReviewAttributes.ReviewLinkOrBuilder (0.45.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:49.664348+00:00
---

# Interface ProductReviewAttributes.ReviewLinkOrBuilder (0.45.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReviewAttributes.ReviewLinkOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ProductReviewAttributes.ReviewLinkOrBuilder (0.45.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.45.0 (latest)  0.41.0  0.40.0  0.39.0  0.37.0  0.34.0  0.33.0  0.31.0  0.29.0  0.28.0  0.26.0  0.24.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.14.0  0.13.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface ProductReviewAttributes.ReviewLinkOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getLink()
    
    
    public abstract String getLink()

Optional. The URI of the review landing page. For example: `<http://www.example.com/review_5.html>`.

`string link = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The link.  
  
### getLinkBytes()
    
    
    public abstract ByteString getLinkBytes()

Optional. The URI of the review landing page. For example: `<http://www.example.com/review_5.html>`.

`string link = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for link.  
  
### getType()
    
    
    public abstract ProductReviewAttributes.ReviewLink.Type getType()

Optional. Type of the review URI.

` .google.shopping.merchant.reviews.v1beta.ProductReviewAttributes.ReviewLink.Type type = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ProductReviewAttributes.ReviewLink.Type](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReviewAttributes.ReviewLink.Type)` | The type.  
  
### getTypeValue()
    
    
    public abstract int getTypeValue()

Optional. Type of the review URI.

` .google.shopping.merchant.reviews.v1beta.ProductReviewAttributes.ReviewLink.Type type = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for type.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
