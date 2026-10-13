---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceGrpc.AsyncService
title: Interface DatasetServiceGrpc.AsyncService (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:13.127332+00:00
---

# Interface DatasetServiceGrpc.AsyncService (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DatasetServiceGrpc.AsyncService (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public static interface DatasetServiceGrpc.AsyncService

The service that manages Vertex AI Dataset and its child resources.

## Methods 

### createDataset(CreateDatasetRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createDataset(CreateDatasetRequest request, StreamObserver<Operation> responseObserver)

Creates a Dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDatasetRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createDatasetVersion(CreateDatasetVersionRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createDatasetVersion(CreateDatasetVersionRequest request, StreamObserver<Operation> responseObserver)

Create a version from a Dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDatasetVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateDatasetVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteDataset(DeleteDatasetRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteDataset(DeleteDatasetRequest request, StreamObserver<Operation> responseObserver)

Deletes a Dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteDatasetRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteDatasetVersion(DeleteDatasetVersionRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteDatasetVersion(DeleteDatasetVersionRequest request, StreamObserver<Operation> responseObserver)

Deletes a Dataset version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDatasetVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteDatasetVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteSavedQuery(DeleteSavedQueryRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteSavedQuery(DeleteSavedQueryRequest request, StreamObserver<Operation> responseObserver)

Deletes a SavedQuery.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSavedQueryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteSavedQueryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### exportData(ExportDataRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void exportData(ExportDataRequest request, StreamObserver<Operation> responseObserver)

Exports data from a Dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportDataRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getAnnotationSpec(GetAnnotationSpecRequest request, StreamObserver<AnnotationSpec> responseObserver)
    
    
    public default void getAnnotationSpec(GetAnnotationSpecRequest request, StreamObserver<AnnotationSpec> responseObserver)

Gets an AnnotationSpec.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAnnotationSpecRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetAnnotationSpecRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AnnotationSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AnnotationSpec)>`  
  
  
### getDataset(GetDatasetRequest request, StreamObserver<Dataset> responseObserver)
    
    
    public default void getDataset(GetDatasetRequest request, StreamObserver<Dataset> responseObserver)

Gets a Dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetDatasetRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset)>`  
  
  
### getDatasetVersion(GetDatasetVersionRequest request, StreamObserver<DatasetVersion> responseObserver)
    
    
    public default void getDatasetVersion(GetDatasetVersionRequest request, StreamObserver<DatasetVersion> responseObserver)

Gets a Dataset version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDatasetVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetDatasetVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[DatasetVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetVersion)>`  
  
  
### importData(ImportDataRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void importData(ImportDataRequest request, StreamObserver<Operation> responseObserver)

Imports data into a Dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportDataRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### listAnnotations(ListAnnotationsRequest request, StreamObserver<ListAnnotationsResponse> responseObserver)
    
    
    public default void listAnnotations(ListAnnotationsRequest request, StreamObserver<ListAnnotationsResponse> responseObserver)

Lists Annotations belongs to a dataitem.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAnnotationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListAnnotationsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListAnnotationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListAnnotationsResponse)>`  
  
  
### listDataItems(ListDataItemsRequest request, StreamObserver<ListDataItemsResponse> responseObserver)
    
    
    public default void listDataItems(ListDataItemsRequest request, StreamObserver<ListDataItemsResponse> responseObserver)

Lists DataItems in a Dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDataItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDataItemsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListDataItemsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDataItemsResponse)>`  
  
  
### listDatasetVersions(ListDatasetVersionsRequest request, StreamObserver<ListDatasetVersionsResponse> responseObserver)
    
    
    public default void listDatasetVersions(ListDatasetVersionsRequest request, StreamObserver<ListDatasetVersionsResponse> responseObserver)

Lists DatasetVersions in a Dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDatasetVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDatasetVersionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListDatasetVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDatasetVersionsResponse)>`  
  
  
### listDatasets(ListDatasetsRequest request, StreamObserver<ListDatasetsResponse> responseObserver)
    
    
    public default void listDatasets(ListDatasetsRequest request, StreamObserver<ListDatasetsResponse> responseObserver)

Lists Datasets in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDatasetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDatasetsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListDatasetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListDatasetsResponse)>`  
  
  
### listSavedQueries(ListSavedQueriesRequest request, StreamObserver<ListSavedQueriesResponse> responseObserver)
    
    
    public default void listSavedQueries(ListSavedQueriesRequest request, StreamObserver<ListSavedQueriesResponse> responseObserver)

Lists SavedQueries in a Dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSavedQueriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListSavedQueriesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSavedQueriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListSavedQueriesResponse)>`  
  
  
### restoreDatasetVersion(RestoreDatasetVersionRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void restoreDatasetVersion(RestoreDatasetVersionRequest request, StreamObserver<Operation> responseObserver)

Restores a dataset version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RestoreDatasetVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.RestoreDatasetVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### searchDataItems(SearchDataItemsRequest request, StreamObserver<SearchDataItemsResponse> responseObserver)
    
    
    public default void searchDataItems(SearchDataItemsRequest request, StreamObserver<SearchDataItemsResponse> responseObserver)

Searches DataItems in a Dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchDataItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SearchDataItemsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SearchDataItemsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.SearchDataItemsResponse)>`  
  
  
### updateDataset(UpdateDatasetRequest request, StreamObserver<Dataset> responseObserver)
    
    
    public default void updateDataset(UpdateDatasetRequest request, StreamObserver<Dataset> responseObserver)

Updates a Dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateDatasetRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Dataset)>`  
  
  
### updateDatasetVersion(UpdateDatasetVersionRequest request, StreamObserver<DatasetVersion> responseObserver)
    
    
    public default void updateDatasetVersion(UpdateDatasetVersionRequest request, StreamObserver<DatasetVersion> responseObserver)

Updates a DatasetVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDatasetVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateDatasetVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[DatasetVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DatasetVersion)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
