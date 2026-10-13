---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.CloudProductRegistryReadServiceGrpc.AsyncService
title: Interface CloudProductRegistryReadServiceGrpc.AsyncService (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:36:34.947374+00:00
---

# Interface CloudProductRegistryReadServiceGrpc.AsyncService (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.CloudProductRegistryReadServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CloudProductRegistryReadServiceGrpc.AsyncService (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public static interface CloudProductRegistryReadServiceGrpc.AsyncService

Cloud Product Registry Read Service provides capabilities to access all first and third party Google Cloud products.

## Methods 

### getLogicalProduct(GetLogicalProductRequest request, StreamObserver<LogicalProduct> responseObserver)
    
    
    public default void getLogicalProduct(GetLogicalProductRequest request, StreamObserver<LogicalProduct> responseObserver)

Gets details of a LogicalProduct.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetLogicalProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.GetLogicalProductRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[LogicalProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.LogicalProduct)>`  
  
  
### getLogicalProductVariant(GetLogicalProductVariantRequest request, StreamObserver<LogicalProductVariant> responseObserver)
    
    
    public default void getLogicalProductVariant(GetLogicalProductVariantRequest request, StreamObserver<LogicalProductVariant> responseObserver)

Get details of a LogicalProductVariant.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetLogicalProductVariantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.GetLogicalProductVariantRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[LogicalProductVariant](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.LogicalProductVariant)>`  
  
  
### getProductSuite(GetProductSuiteRequest request, StreamObserver<ProductSuite> responseObserver)
    
    
    public default void getProductSuite(GetProductSuiteRequest request, StreamObserver<ProductSuite> responseObserver)

Get details of a ProductSuite.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetProductSuiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.GetProductSuiteRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ProductSuite](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.ProductSuite)>`  
  
  
### listLogicalProductVariants(ListLogicalProductVariantsRequest request, StreamObserver<ListLogicalProductVariantsResponse> responseObserver)
    
    
    public default void listLogicalProductVariants(ListLogicalProductVariantsRequest request, StreamObserver<ListLogicalProductVariantsResponse> responseObserver)

Lists LogicalProductVariants matching given criteria.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListLogicalProductVariantsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.ListLogicalProductVariantsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListLogicalProductVariantsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.ListLogicalProductVariantsResponse)>`  
  
  
### listLogicalProducts(ListLogicalProductsRequest request, StreamObserver<ListLogicalProductsResponse> responseObserver)
    
    
    public default void listLogicalProducts(ListLogicalProductsRequest request, StreamObserver<ListLogicalProductsResponse> responseObserver)

Lists LogicalProducts matching given criteria.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListLogicalProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.ListLogicalProductsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListLogicalProductsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.ListLogicalProductsResponse)>`  
  
  
### listProductSuites(ListProductSuitesRequest request, StreamObserver<ListProductSuitesResponse> responseObserver)
    
    
    public default void listProductSuites(ListProductSuitesRequest request, StreamObserver<ListProductSuitesResponse> responseObserver)

Lists ProductSuites.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListProductSuitesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.ListProductSuitesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListProductSuitesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.ListProductSuitesResponse)>`  
  
  
### lookupEntity(LookupEntityRequest request, StreamObserver<LookupEntityResponse> responseObserver)
    
    
    public default void lookupEntity(LookupEntityRequest request, StreamObserver<LookupEntityResponse> responseObserver)

Look up entities.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupEntityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.LookupEntityRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[LookupEntityResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.LookupEntityResponse)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
