---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReviewsServiceGrpc.AsyncService
title: Interface ProductReviewsServiceGrpc.AsyncService (0.45.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:15:17.060818+00:00
---

# Interface ProductReviewsServiceGrpc.AsyncService (0.45.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReviewsServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ProductReviewsServiceGrpc.AsyncService (0.45.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.45.0 (latest)  0.41.0  0.40.0  0.39.0  0.37.0  0.34.0  0.33.0  0.31.0  0.29.0  0.28.0  0.26.0  0.24.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.14.0  0.13.0  0.10.0  0.9.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface ProductReviewsServiceGrpc.AsyncService

Service to manage product reviews.

## Methods 

### deleteProductReview(DeleteProductReviewRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteProductReview(DeleteProductReviewRequest request, StreamObserver<Empty> responseObserver)

Deletes a product review.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteProductReviewRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.DeleteProductReviewRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### getProductReview(GetProductReviewRequest request, StreamObserver<ProductReview> responseObserver)
    
    
    public default void getProductReview(GetProductReviewRequest request, StreamObserver<ProductReview> responseObserver)

Gets a product review.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProductReviewRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.GetProductReviewRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ProductReview](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReview)>`  
  
  
### insertProductReview(InsertProductReviewRequest request, StreamObserver<ProductReview> responseObserver)
    
    
    public default void insertProductReview(InsertProductReviewRequest request, StreamObserver<ProductReview> responseObserver)

Inserts a product review.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[InsertProductReviewRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.InsertProductReviewRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ProductReview](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ProductReview)>`  
  
  
### listProductReviews(ListProductReviewsRequest request, StreamObserver<ListProductReviewsResponse> responseObserver)
    
    
    public default void listProductReviews(ListProductReviewsRequest request, StreamObserver<ListProductReviewsResponse> responseObserver)

Lists product reviews.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProductReviewsRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ListProductReviewsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListProductReviewsResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-reviews/latest/com.google.shopping.merchant.reviews.v1beta.ListProductReviewsResponse)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
