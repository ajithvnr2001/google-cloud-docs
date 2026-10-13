---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.RepositoryManagerGrpc.AsyncService
title: Interface RepositoryManagerGrpc.AsyncService (3.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:43:35.979600+00:00
---

# Interface RepositoryManagerGrpc.AsyncService (3.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.RepositoryManagerGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface RepositoryManagerGrpc.AsyncService (3.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.101.0 (latest)  3.97.0  3.96.0  3.95.0  3.93.0  3.90.0  3.89.0  3.87.0  3.85.0  3.84.0  3.83.0  3.82.0  3.80.0  3.78.0  3.77.0  3.76.0  3.75.0  3.74.0  3.72.0  3.70.0  3.69.0  3.66.0  3.65.0  3.64.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.6  3.4.1  3.3.12 
    
    
    public static interface RepositoryManagerGrpc.AsyncService

Manages connections to source code repositories.

## Methods 

### batchCreateRepositories(BatchCreateRepositoriesRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void batchCreateRepositories(BatchCreateRepositoriesRequest request, StreamObserver<Operation> responseObserver)

Creates multiple repositories inside a connection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateRepositoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.BatchCreateRepositoriesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createConnection(CreateConnectionRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createConnection(CreateConnectionRequest request, StreamObserver<Operation> responseObserver)

Creates a Connection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.CreateConnectionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### createRepository(CreateRepositoryRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void createRepository(CreateRepositoryRequest request, StreamObserver<Operation> responseObserver)

Creates a Repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.CreateRepositoryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteConnection(DeleteConnectionRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteConnection(DeleteConnectionRequest request, StreamObserver<Operation> responseObserver)

Deletes a single connection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.DeleteConnectionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteRepository(DeleteRepositoryRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteRepository(DeleteRepositoryRequest request, StreamObserver<Operation> responseObserver)

Deletes a single repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.DeleteRepositoryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### fetchGitRefs(FetchGitRefsRequest request, StreamObserver<FetchGitRefsResponse> responseObserver)
    
    
    public default void fetchGitRefs(FetchGitRefsRequest request, StreamObserver<FetchGitRefsResponse> responseObserver)

Fetch the list of branches or tags for a given repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchGitRefsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchGitRefsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FetchGitRefsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchGitRefsResponse)>`  
  
  
### fetchLinkableRepositories(FetchLinkableRepositoriesRequest request, StreamObserver<FetchLinkableRepositoriesResponse> responseObserver)
    
    
    public default void fetchLinkableRepositories(FetchLinkableRepositoriesRequest request, StreamObserver<FetchLinkableRepositoriesResponse> responseObserver)

FetchLinkableRepositories get repositories from SCM that are accessible and could be added to the connection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchLinkableRepositoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchLinkableRepositoriesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FetchLinkableRepositoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchLinkableRepositoriesResponse)>`  
  
  
### fetchReadToken(FetchReadTokenRequest request, StreamObserver<FetchReadTokenResponse> responseObserver)
    
    
    public default void fetchReadToken(FetchReadTokenRequest request, StreamObserver<FetchReadTokenResponse> responseObserver)

Fetches read token of a given repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchReadTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchReadTokenRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FetchReadTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchReadTokenResponse)>`  
  
  
### fetchReadWriteToken(FetchReadWriteTokenRequest request, StreamObserver<FetchReadWriteTokenResponse> responseObserver)
    
    
    public default void fetchReadWriteToken(FetchReadWriteTokenRequest request, StreamObserver<FetchReadWriteTokenResponse> responseObserver)

Fetches read/write token of a given repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[FetchReadWriteTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchReadWriteTokenRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FetchReadWriteTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchReadWriteTokenResponse)>`  
  
  
### getConnection(GetConnectionRequest request, StreamObserver<Connection> responseObserver)
    
    
    public default void getConnection(GetConnectionRequest request, StreamObserver<Connection> responseObserver)

Gets details of a single connection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.GetConnectionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.Connection)>`  
  
  
### getRepository(GetRepositoryRequest request, StreamObserver<Repository> responseObserver)
    
    
    public default void getRepository(GetRepositoryRequest request, StreamObserver<Repository> responseObserver)

Gets details of a single repository.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.GetRepositoryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.Repository)>`  
  
  
### listConnections(ListConnectionsRequest request, StreamObserver<ListConnectionsResponse> responseObserver)
    
    
    public default void listConnections(ListConnectionsRequest request, StreamObserver<ListConnectionsResponse> responseObserver)

Lists Connections in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ListConnectionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListConnectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ListConnectionsResponse)>`  
  
  
### listRepositories(ListRepositoriesRequest request, StreamObserver<ListRepositoriesResponse> responseObserver)
    
    
    public default void listRepositories(ListRepositoriesRequest request, StreamObserver<ListRepositoriesResponse> responseObserver)

Lists Repositories in a given connection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRepositoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ListRepositoriesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListRepositoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ListRepositoriesResponse)>`  
  
  
### updateConnection(UpdateConnectionRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateConnection(UpdateConnectionRequest request, StreamObserver<Operation> responseObserver)

Updates a single connection.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.UpdateConnectionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
