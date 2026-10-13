---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureOnlineStoreAdminServiceGrpc.AsyncService
title: Interface FeatureOnlineStoreAdminServiceGrpc.AsyncService (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:34.927377+00:00
---

# Interface FeatureOnlineStoreAdminServiceGrpc.AsyncService (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureOnlineStoreAdminServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface FeatureOnlineStoreAdminServiceGrpc.AsyncService (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public static interface FeatureOnlineStoreAdminServiceGrpc.AsyncService

The service that handles CRUD and List for resources for FeatureOnlineStore.

## Methods 

### createFeatureOnlineStore(CreateFeatureOnlineStoreRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createFeatureOnlineStore(CreateFeatureOnlineStoreRequest request, StreamObserver<Operation> responseObserver)

Creates a new FeatureOnlineStore in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureOnlineStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureOnlineStoreRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createFeatureView(CreateFeatureViewRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createFeatureView(CreateFeatureViewRequest request, StreamObserver<Operation> responseObserver)

Creates a new FeatureView in a given FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateFeatureViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.CreateFeatureViewRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteFeatureOnlineStore(DeleteFeatureOnlineStoreRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteFeatureOnlineStore(DeleteFeatureOnlineStoreRequest request, StreamObserver<Operation> responseObserver)

Deletes a single FeatureOnlineStore. The FeatureOnlineStore must not contain any FeatureViews.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureOnlineStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteFeatureOnlineStoreRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteFeatureView(DeleteFeatureViewRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteFeatureView(DeleteFeatureViewRequest request, StreamObserver<Operation> responseObserver)

Deletes a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteFeatureViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.DeleteFeatureViewRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getFeatureOnlineStore(GetFeatureOnlineStoreRequest request, StreamObserver<FeatureOnlineStore> responseObserver)
    
    
    public default void getFeatureOnlineStore(GetFeatureOnlineStoreRequest request, StreamObserver<FeatureOnlineStore> responseObserver)

Gets details of a single FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureOnlineStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetFeatureOnlineStoreRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FeatureOnlineStore](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureOnlineStore)>`  
  
  
### getFeatureView(GetFeatureViewRequest request, StreamObserver<FeatureView> responseObserver)
    
    
    public default void getFeatureView(GetFeatureViewRequest request, StreamObserver<FeatureView> responseObserver)

Gets details of a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetFeatureViewRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FeatureView](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureView)>`  
  
  
### getFeatureViewSync(GetFeatureViewSyncRequest request, StreamObserver<FeatureViewSync> responseObserver)
    
    
    public default void getFeatureViewSync(GetFeatureViewSyncRequest request, StreamObserver<FeatureViewSync> responseObserver)

Gets details of a single FeatureViewSync.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetFeatureViewSyncRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.GetFeatureViewSyncRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FeatureViewSync](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.FeatureViewSync)>`  
  
  
### listFeatureOnlineStores(ListFeatureOnlineStoresRequest request, StreamObserver<ListFeatureOnlineStoresResponse> responseObserver)
    
    
    public default void listFeatureOnlineStores(ListFeatureOnlineStoresRequest request, StreamObserver<ListFeatureOnlineStoresResponse> responseObserver)

Lists FeatureOnlineStores in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureOnlineStoresRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListFeatureOnlineStoresRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListFeatureOnlineStoresResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListFeatureOnlineStoresResponse)>`  
  
  
### listFeatureViewSyncs(ListFeatureViewSyncsRequest request, StreamObserver<ListFeatureViewSyncsResponse> responseObserver)
    
    
    public default void listFeatureViewSyncs(ListFeatureViewSyncsRequest request, StreamObserver<ListFeatureViewSyncsResponse> responseObserver)

Lists FeatureViewSyncs in a given FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureViewSyncsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListFeatureViewSyncsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListFeatureViewSyncsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListFeatureViewSyncsResponse)>`  
  
  
### listFeatureViews(ListFeatureViewsRequest request, StreamObserver<ListFeatureViewsResponse> responseObserver)
    
    
    public default void listFeatureViews(ListFeatureViewsRequest request, StreamObserver<ListFeatureViewsResponse> responseObserver)

Lists FeatureViews in a given FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListFeatureViewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListFeatureViewsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListFeatureViewsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ListFeatureViewsResponse)>`  
  
  
### syncFeatureView(SyncFeatureViewRequest request, StreamObserver<SyncFeatureViewResponse> responseObserver)
    
    
    public default void syncFeatureView(SyncFeatureViewRequest request, StreamObserver<SyncFeatureViewResponse> responseObserver)

Triggers on-demand sync for the FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SyncFeatureViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SyncFeatureViewRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SyncFeatureViewResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SyncFeatureViewResponse)>`  
  
  
### updateFeatureOnlineStore(UpdateFeatureOnlineStoreRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateFeatureOnlineStore(UpdateFeatureOnlineStoreRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single FeatureOnlineStore.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureOnlineStoreRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateFeatureOnlineStoreRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateFeatureView(UpdateFeatureViewRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateFeatureView(UpdateFeatureViewRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single FeatureView.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateFeatureViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UpdateFeatureViewRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
