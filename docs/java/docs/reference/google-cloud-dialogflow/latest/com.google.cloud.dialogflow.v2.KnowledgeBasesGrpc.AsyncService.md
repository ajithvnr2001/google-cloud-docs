---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBasesGrpc.AsyncService
title: Interface KnowledgeBasesGrpc.AsyncService (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:41.219231+00:00
---

# Interface KnowledgeBasesGrpc.AsyncService (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBasesGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface KnowledgeBasesGrpc.AsyncService (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 
    
    
    public static interface KnowledgeBasesGrpc.AsyncService

Service for managing KnowledgeBases.

## Methods 

### createKnowledgeBase(CreateKnowledgeBaseRequest request, StreamObserver<KnowledgeBase> responseObserver)
    
    
    public default void createKnowledgeBase(CreateKnowledgeBaseRequest request, StreamObserver<KnowledgeBase> responseObserver)

Creates a knowledge base.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateKnowledgeBaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateKnowledgeBaseRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[KnowledgeBase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase)>`  
  
  
### deleteKnowledgeBase(DeleteKnowledgeBaseRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteKnowledgeBase(DeleteKnowledgeBaseRequest request, StreamObserver<Empty> responseObserver)

Deletes the specified knowledge base.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteKnowledgeBaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteKnowledgeBaseRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### getKnowledgeBase(GetKnowledgeBaseRequest request, StreamObserver<KnowledgeBase> responseObserver)
    
    
    public default void getKnowledgeBase(GetKnowledgeBaseRequest request, StreamObserver<KnowledgeBase> responseObserver)

Retrieves the specified knowledge base.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetKnowledgeBaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetKnowledgeBaseRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[KnowledgeBase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase)>`  
  
  
### listKnowledgeBases(ListKnowledgeBasesRequest request, StreamObserver<ListKnowledgeBasesResponse> responseObserver)
    
    
    public default void listKnowledgeBases(ListKnowledgeBasesRequest request, StreamObserver<ListKnowledgeBasesResponse> responseObserver)

Returns the list of all knowledge bases of the specified agent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListKnowledgeBasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListKnowledgeBasesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListKnowledgeBasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListKnowledgeBasesResponse)>`  
  
  
### updateKnowledgeBase(UpdateKnowledgeBaseRequest request, StreamObserver<KnowledgeBase> responseObserver)
    
    
    public default void updateKnowledgeBase(UpdateKnowledgeBaseRequest request, StreamObserver<KnowledgeBase> responseObserver)

Updates the specified knowledge base.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateKnowledgeBaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateKnowledgeBaseRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[KnowledgeBase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.KnowledgeBase)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
