---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.CatalogServiceGrpc.AsyncService
title: Interface CatalogServiceGrpc.AsyncService (0.106.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:45:16.524842+00:00
---

# Interface CatalogServiceGrpc.AsyncService (0.106.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.CatalogServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CatalogServiceGrpc.AsyncService (0.106.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.106.0 (latest)  0.102.0  0.101.0  0.100.0  0.98.0  0.95.0  0.94.0  0.92.0  0.90.0  0.89.0  0.87.0  0.85.0  0.83.0  0.82.0  0.81.0  0.80.0  0.79.0  0.77.0  0.75.0  0.74.0  0.71.0  0.70.0  0.69.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.4  0.8.10 
    
    
    public static interface CatalogServiceGrpc.AsyncService

Service for ingesting catalog information of the customer's website.

## Methods 

### createCatalogItem(CreateCatalogItemRequest request, StreamObserver<CatalogItem> responseObserver)
    
    
    public default void createCatalogItem(CreateCatalogItemRequest request, StreamObserver<CatalogItem> responseObserver)

Creates a catalog item.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCatalogItemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.CreateCatalogItemRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CatalogItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.CatalogItem)>`  
  
  
### deleteCatalogItem(DeleteCatalogItemRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteCatalogItem(DeleteCatalogItemRequest request, StreamObserver<Empty> responseObserver)

Deletes a catalog item.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCatalogItemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.DeleteCatalogItemRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### getCatalogItem(GetCatalogItemRequest request, StreamObserver<CatalogItem> responseObserver)
    
    
    public default void getCatalogItem(GetCatalogItemRequest request, StreamObserver<CatalogItem> responseObserver)

Gets a specific catalog item.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCatalogItemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.GetCatalogItemRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CatalogItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.CatalogItem)>`  
  
  
### importCatalogItems(ImportCatalogItemsRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void importCatalogItems(ImportCatalogItemsRequest request, StreamObserver<Operation> responseObserver)

Bulk import of multiple catalog items. Request processing may be synchronous. No partial updating supported. Non-existing items will be created. Operation.response is of type ImportResponse. Note that it is possible for a subset of the items to be successfully updated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportCatalogItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.ImportCatalogItemsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### listCatalogItems(ListCatalogItemsRequest request, StreamObserver<ListCatalogItemsResponse> responseObserver)
    
    
    public default void listCatalogItems(ListCatalogItemsRequest request, StreamObserver<ListCatalogItemsResponse> responseObserver)

Gets a list of catalog items.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCatalogItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.ListCatalogItemsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListCatalogItemsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.ListCatalogItemsResponse)>`  
  
  
### updateCatalogItem(UpdateCatalogItemRequest request, StreamObserver<CatalogItem> responseObserver)
    
    
    public default void updateCatalogItem(UpdateCatalogItemRequest request, StreamObserver<CatalogItem> responseObserver)

Updates a catalog item. Partial updating is supported. Non-existing items will be created.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateCatalogItemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.UpdateCatalogItemRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CatalogItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.CatalogItem)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
