---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceGrpc.AsyncService
title: Interface BusinessGlossaryServiceGrpc.AsyncService (1.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:55:31.841150+00:00
---

# Interface BusinessGlossaryServiceGrpc.AsyncService (1.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.BusinessGlossaryServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BusinessGlossaryServiceGrpc.AsyncService (1.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.97.0 (latest)  1.93.0  1.92.0  1.91.0  1.89.0  1.86.0  1.85.0  1.83.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.68.0  1.66.0  1.65.0  1.62.0  1.61.0  1.60.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.2  1.0.1  0.2.2 
    
    
    public static interface BusinessGlossaryServiceGrpc.AsyncService

BusinessGlossaryService provides APIs for managing business glossary resources for enterprise customers. The resources currently supported in Business Glossary are:

  1. Glossary
  2. GlossaryCategory
  3. GlossaryTerm



## Methods 

### createGlossary(CreateGlossaryRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createGlossary(CreateGlossaryRequest request, StreamObserver<Operation> responseObserver)

Creates a new Glossary resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateGlossaryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createGlossaryCategory(CreateGlossaryCategoryRequest request, StreamObserver<GlossaryCategory> responseObserver)
    
    
    public default void createGlossaryCategory(CreateGlossaryCategoryRequest request, StreamObserver<GlossaryCategory> responseObserver)

Creates a new GlossaryCategory resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGlossaryCategoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateGlossaryCategoryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[GlossaryCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryCategory)>`  
  
  
### createGlossaryTerm(CreateGlossaryTermRequest request, StreamObserver<GlossaryTerm> responseObserver)
    
    
    public default void createGlossaryTerm(CreateGlossaryTermRequest request, StreamObserver<GlossaryTerm> responseObserver)

Creates a new GlossaryTerm resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateGlossaryTermRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateGlossaryTermRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[GlossaryTerm](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryTerm)>`  
  
  
### deleteGlossary(DeleteGlossaryRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteGlossary(DeleteGlossaryRequest request, StreamObserver<Operation> responseObserver)

Deletes a Glossary resource. All the categories and terms within the Glossary must be deleted before the Glossary can be deleted.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteGlossaryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteGlossaryCategory(DeleteGlossaryCategoryRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteGlossaryCategory(DeleteGlossaryCategoryRequest request, StreamObserver<Empty> responseObserver)

Deletes a GlossaryCategory resource. All the GlossaryCategories and GlossaryTerms nested directly under the specified GlossaryCategory will be moved one level up to the parent in the hierarchy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGlossaryCategoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteGlossaryCategoryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteGlossaryTerm(DeleteGlossaryTermRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteGlossaryTerm(DeleteGlossaryTermRequest request, StreamObserver<Empty> responseObserver)

Deletes a GlossaryTerm resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteGlossaryTermRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteGlossaryTermRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### getGlossary(GetGlossaryRequest request, StreamObserver<Glossary> responseObserver)
    
    
    public default void getGlossary(GetGlossaryRequest request, StreamObserver<Glossary> responseObserver)

Gets a Glossary resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetGlossaryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Glossary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.Glossary)>`  
  
  
### getGlossaryCategory(GetGlossaryCategoryRequest request, StreamObserver<GlossaryCategory> responseObserver)
    
    
    public default void getGlossaryCategory(GetGlossaryCategoryRequest request, StreamObserver<GlossaryCategory> responseObserver)

Gets a GlossaryCategory resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGlossaryCategoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetGlossaryCategoryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[GlossaryCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryCategory)>`  
  
  
### getGlossaryTerm(GetGlossaryTermRequest request, StreamObserver<GlossaryTerm> responseObserver)
    
    
    public default void getGlossaryTerm(GetGlossaryTermRequest request, StreamObserver<GlossaryTerm> responseObserver)

Gets a GlossaryTerm resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetGlossaryTermRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GetGlossaryTermRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[GlossaryTerm](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryTerm)>`  
  
  
### listGlossaries(ListGlossariesRequest request, StreamObserver<ListGlossariesResponse> responseObserver)
    
    
    public default void listGlossaries(ListGlossariesRequest request, StreamObserver<ListGlossariesResponse> responseObserver)

Lists Glossary resources in a project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGlossariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListGlossariesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListGlossariesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListGlossariesResponse)>`  
  
  
### listGlossaryCategories(ListGlossaryCategoriesRequest request, StreamObserver<ListGlossaryCategoriesResponse> responseObserver)
    
    
    public default void listGlossaryCategories(ListGlossaryCategoriesRequest request, StreamObserver<ListGlossaryCategoriesResponse> responseObserver)

Lists GlossaryCategory resources in a Glossary.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGlossaryCategoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListGlossaryCategoriesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListGlossaryCategoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListGlossaryCategoriesResponse)>`  
  
  
### listGlossaryTerms(ListGlossaryTermsRequest request, StreamObserver<ListGlossaryTermsResponse> responseObserver)
    
    
    public default void listGlossaryTerms(ListGlossaryTermsRequest request, StreamObserver<ListGlossaryTermsResponse> responseObserver)

Lists GlossaryTerm resources in a Glossary.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListGlossaryTermsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListGlossaryTermsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListGlossaryTermsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.ListGlossaryTermsResponse)>`  
  
  
### updateGlossary(UpdateGlossaryRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateGlossary(UpdateGlossaryRequest request, StreamObserver<Operation> responseObserver)

Updates a Glossary resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGlossaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateGlossaryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateGlossaryCategory(UpdateGlossaryCategoryRequest request, StreamObserver<GlossaryCategory> responseObserver)
    
    
    public default void updateGlossaryCategory(UpdateGlossaryCategoryRequest request, StreamObserver<GlossaryCategory> responseObserver)

Updates a GlossaryCategory resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGlossaryCategoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateGlossaryCategoryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[GlossaryCategory](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryCategory)>`  
  
  
### updateGlossaryTerm(UpdateGlossaryTermRequest request, StreamObserver<GlossaryTerm> responseObserver)
    
    
    public default void updateGlossaryTerm(UpdateGlossaryTermRequest request, StreamObserver<GlossaryTerm> responseObserver)

Updates a GlossaryTerm resource.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateGlossaryTermRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateGlossaryTermRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[GlossaryTerm](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.GlossaryTerm)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
