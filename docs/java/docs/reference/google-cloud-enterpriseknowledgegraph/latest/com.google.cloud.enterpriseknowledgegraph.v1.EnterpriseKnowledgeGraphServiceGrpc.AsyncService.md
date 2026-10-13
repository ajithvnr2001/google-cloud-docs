---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-enterpriseknowledgegraph/latest/com.google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphServiceGrpc.AsyncService
title: Interface EnterpriseKnowledgeGraphServiceGrpc.AsyncService (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:46:29.000394+00:00
---

# Interface EnterpriseKnowledgeGraphServiceGrpc.AsyncService (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-enterpriseknowledgegraph/latest/com.google.cloud.enterpriseknowledgegraph.v1.EnterpriseKnowledgeGraphServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface EnterpriseKnowledgeGraphServiceGrpc.AsyncService (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface EnterpriseKnowledgeGraphServiceGrpc.AsyncService

APIs for enterprise knowledge graph product.

## Methods 

### cancelEntityReconciliationJob(CancelEntityReconciliationJobRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void cancelEntityReconciliationJob(CancelEntityReconciliationJobRequest request, StreamObserver<Empty> responseObserver)

Cancels a EntityReconciliationJob. Success of cancellation is not guaranteed.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CancelEntityReconciliationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-enterpriseknowledgegraph/latest/com.google.cloud.enterpriseknowledgegraph.v1.CancelEntityReconciliationJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### createEntityReconciliationJob(CreateEntityReconciliationJobRequest request, StreamObserver<EntityReconciliationJob> responseObserver)
    
    
    public default void createEntityReconciliationJob(CreateEntityReconciliationJobRequest request, StreamObserver<EntityReconciliationJob> responseObserver)

Creates a EntityReconciliationJob. A EntityReconciliationJob once created will right away be attempted to start.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateEntityReconciliationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-enterpriseknowledgegraph/latest/com.google.cloud.enterpriseknowledgegraph.v1.CreateEntityReconciliationJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[EntityReconciliationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-enterpriseknowledgegraph/latest/com.google.cloud.enterpriseknowledgegraph.v1.EntityReconciliationJob)>`  
  
  
### deleteEntityReconciliationJob(DeleteEntityReconciliationJobRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteEntityReconciliationJob(DeleteEntityReconciliationJobRequest request, StreamObserver<Empty> responseObserver)

Deletes a EntityReconciliationJob. It only deletes the job when the job state is in FAILED, SUCCEEDED, and CANCELLED.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteEntityReconciliationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-enterpriseknowledgegraph/latest/com.google.cloud.enterpriseknowledgegraph.v1.DeleteEntityReconciliationJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### getEntityReconciliationJob(GetEntityReconciliationJobRequest request, StreamObserver<EntityReconciliationJob> responseObserver)
    
    
    public default void getEntityReconciliationJob(GetEntityReconciliationJobRequest request, StreamObserver<EntityReconciliationJob> responseObserver)

Gets a EntityReconciliationJob.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEntityReconciliationJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-enterpriseknowledgegraph/latest/com.google.cloud.enterpriseknowledgegraph.v1.GetEntityReconciliationJobRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[EntityReconciliationJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-enterpriseknowledgegraph/latest/com.google.cloud.enterpriseknowledgegraph.v1.EntityReconciliationJob)>`  
  
  
### listEntityReconciliationJobs(ListEntityReconciliationJobsRequest request, StreamObserver<ListEntityReconciliationJobsResponse> responseObserver)
    
    
    public default void listEntityReconciliationJobs(ListEntityReconciliationJobsRequest request, StreamObserver<ListEntityReconciliationJobsResponse> responseObserver)

Lists Entity Reconciliation Jobs.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEntityReconciliationJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-enterpriseknowledgegraph/latest/com.google.cloud.enterpriseknowledgegraph.v1.ListEntityReconciliationJobsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListEntityReconciliationJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-enterpriseknowledgegraph/latest/com.google.cloud.enterpriseknowledgegraph.v1.ListEntityReconciliationJobsResponse)>`  
  
  
### lookup(LookupRequest request, StreamObserver<LookupResponse> responseObserver)
    
    
    public default void lookup(LookupRequest request, StreamObserver<LookupResponse> responseObserver)

Finds the Cloud KG entities with CKG ID(s).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-enterpriseknowledgegraph/latest/com.google.cloud.enterpriseknowledgegraph.v1.LookupRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[LookupResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-enterpriseknowledgegraph/latest/com.google.cloud.enterpriseknowledgegraph.v1.LookupResponse)>`  
  
  
### lookupPublicKg(LookupPublicKgRequest request, StreamObserver<LookupPublicKgResponse> responseObserver)
    
    
    public default void lookupPublicKg(LookupPublicKgRequest request, StreamObserver<LookupPublicKgResponse> responseObserver)

Finds the public KG entities with public KG ID(s).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LookupPublicKgRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-enterpriseknowledgegraph/latest/com.google.cloud.enterpriseknowledgegraph.v1.LookupPublicKgRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[LookupPublicKgResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-enterpriseknowledgegraph/latest/com.google.cloud.enterpriseknowledgegraph.v1.LookupPublicKgResponse)>`  
  
  
### search(SearchRequest request, StreamObserver<SearchResponse> responseObserver)
    
    
    public default void search(SearchRequest request, StreamObserver<SearchResponse> responseObserver)

Searches the Cloud KG entities with entity name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-enterpriseknowledgegraph/latest/com.google.cloud.enterpriseknowledgegraph.v1.SearchRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SearchResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-enterpriseknowledgegraph/latest/com.google.cloud.enterpriseknowledgegraph.v1.SearchResponse)>`  
  
  
### searchPublicKg(SearchPublicKgRequest request, StreamObserver<SearchPublicKgResponse> responseObserver)
    
    
    public default void searchPublicKg(SearchPublicKgRequest request, StreamObserver<SearchPublicKgResponse> responseObserver)

Searches the public KG entities with entity name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchPublicKgRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-enterpriseknowledgegraph/latest/com.google.cloud.enterpriseknowledgegraph.v1.SearchPublicKgRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SearchPublicKgResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-enterpriseknowledgegraph/latest/com.google.cloud.enterpriseknowledgegraph.v1.SearchPublicKgResponse)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
