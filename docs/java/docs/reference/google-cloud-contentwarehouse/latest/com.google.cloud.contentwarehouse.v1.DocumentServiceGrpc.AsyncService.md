---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentServiceGrpc.AsyncService
title: Interface DocumentServiceGrpc.AsyncService (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:50.874409+00:00
---

# Interface DocumentServiceGrpc.AsyncService (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DocumentServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DocumentServiceGrpc.AsyncService (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface DocumentServiceGrpc.AsyncService

This service lets you manage document.

## Methods 

### createDocument(CreateDocumentRequest request, StreamObserver<CreateDocumentResponse> responseObserver)
    
    
    public default void createDocument(CreateDocumentRequest request, StreamObserver<CreateDocumentResponse> responseObserver)

Creates a document.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.CreateDocumentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CreateDocumentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.CreateDocumentResponse)>`  
  
  
### deleteDocument(DeleteDocumentRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteDocument(DeleteDocumentRequest request, StreamObserver<Empty> responseObserver)

Deletes a document. Returns NOT_FOUND if the document does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.DeleteDocumentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### fetchAcl(FetchAclRequest request, StreamObserver<FetchAclResponse> responseObserver)
    
    
    public default void fetchAcl(FetchAclRequest request, StreamObserver<FetchAclResponse> responseObserver)

Gets the access control policy for a resource. Returns NOT_FOUND error if the resource does not exist. Returns an empty policy if the resource exists but does not have a policy set.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchAclRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.FetchAclRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FetchAclResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.FetchAclResponse)>`  
  
  
### getDocument(GetDocumentRequest request, StreamObserver<Document> responseObserver)
    
    
    public default void getDocument(GetDocumentRequest request, StreamObserver<Document> responseObserver)

Gets a document. Returns NOT_FOUND if the document does not exist.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.GetDocumentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Document)>`  
  
  
### lockDocument(LockDocumentRequest request, StreamObserver<Document> responseObserver)
    
    
    public default void lockDocument(LockDocumentRequest request, StreamObserver<Document> responseObserver)

Lock the document so the document cannot be updated by other users.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[LockDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.LockDocumentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Document](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.Document)>`  
  
  
### searchDocuments(SearchDocumentsRequest request, StreamObserver<SearchDocumentsResponse> responseObserver)
    
    
    public default void searchDocuments(SearchDocumentsRequest request, StreamObserver<SearchDocumentsResponse> responseObserver)

Searches for documents using provided SearchDocumentsRequest. This call only returns documents that the caller has permission to search against.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchDocumentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SearchDocumentsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SearchDocumentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SearchDocumentsResponse)>`  
  
  
### setAcl(SetAclRequest request, StreamObserver<SetAclResponse> responseObserver)
    
    
    public default void setAcl(SetAclRequest request, StreamObserver<SetAclResponse> responseObserver)

Sets the access control policy for a resource. Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetAclRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SetAclRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SetAclResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.SetAclResponse)>`  
  
  
### updateDocument(UpdateDocumentRequest request, StreamObserver<UpdateDocumentResponse> responseObserver)
    
    
    public default void updateDocument(UpdateDocumentRequest request, StreamObserver<UpdateDocumentResponse> responseObserver)

Updates a document. Returns INVALID_ARGUMENT if the name of the document is non-empty and does not equal the existing name.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDocumentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.UpdateDocumentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[UpdateDocumentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-contentwarehouse/latest/com.google.cloud.contentwarehouse.v1.UpdateDocumentResponse)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
