---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.SqlOperationsServiceGrpc.AsyncService
title: Interface SqlOperationsServiceGrpc.AsyncService (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:38.440831+00:00
---

# Interface SqlOperationsServiceGrpc.AsyncService (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.SqlOperationsServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SqlOperationsServiceGrpc.AsyncService (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public static interface SqlOperationsServiceGrpc.AsyncService

## Methods 

### cancel(SqlOperationsCancelRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void cancel(SqlOperationsCancelRequest request, StreamObserver<Empty> responseObserver)

Cancels an instance operation that has been performed on an instance. Ordinarily, this method name should be `CancelSqlOperation`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SqlOperationsCancelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.SqlOperationsCancelRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### get(SqlOperationsGetRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void get(SqlOperationsGetRequest request, StreamObserver<Operation> responseObserver)

Retrieves an instance operation that has been performed on an instance.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SqlOperationsGetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.SqlOperationsGetRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.Operation)>`  
  
  
### list(SqlOperationsListRequest request, StreamObserver<OperationsListResponse> responseObserver)
    
    
    public default void list(SqlOperationsListRequest request, StreamObserver<OperationsListResponse> responseObserver)

Lists all instance operations that have been performed on the given Cloud SQL instance in the reverse chronological order of the start time.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SqlOperationsListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.SqlOperationsListRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[OperationsListResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.OperationsListResponse)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
