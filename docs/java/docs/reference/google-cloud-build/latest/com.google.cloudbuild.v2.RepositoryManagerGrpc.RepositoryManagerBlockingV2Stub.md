---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.RepositoryManagerGrpc.RepositoryManagerBlockingV2Stub
title: Class RepositoryManagerGrpc.RepositoryManagerBlockingV2Stub (3.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:43:55.587969+00:00
---

# Class RepositoryManagerGrpc.RepositoryManagerBlockingV2Stub (3.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.RepositoryManagerGrpc.RepositoryManagerBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RepositoryManagerGrpc.RepositoryManagerBlockingV2Stub (3.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.101.0 (latest)  3.97.0  3.96.0  3.95.0  3.93.0  3.90.0  3.89.0  3.87.0  3.85.0  3.84.0  3.83.0  3.82.0  3.80.0  3.78.0  3.77.0  3.76.0  3.75.0  3.74.0  3.72.0  3.70.0  3.69.0  3.66.0  3.65.0  3.64.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.6  3.4.1  3.3.12 
    
    
    public static final class RepositoryManagerGrpc.RepositoryManagerBlockingV2Stub extends AbstractBlockingStub<RepositoryManagerGrpc.RepositoryManagerBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service RepositoryManager.

Manages connections to source code repositories.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > RepositoryManagerGrpc.RepositoryManagerBlockingV2Stub

## Inherited Members

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### batchCreateRepositories(BatchCreateRepositoriesRequest request)
    
    
    public Operation batchCreateRepositories(BatchCreateRepositoriesRequest request)

Creates multiple repositories inside a connection.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCreateRepositoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.BatchCreateRepositoriesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected RepositoryManagerGrpc.RepositoryManagerBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[RepositoryManagerGrpc.RepositoryManagerBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.RepositoryManagerGrpc.RepositoryManagerBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createConnection(CreateConnectionRequest request)
    
    
    public Operation createConnection(CreateConnectionRequest request)

Creates a Connection.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.CreateConnectionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createRepository(CreateRepositoryRequest request)
    
    
    public Operation createRepository(CreateRepositoryRequest request)

Creates a Repository.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.CreateRepositoryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteConnection(DeleteConnectionRequest request)
    
    
    public Operation deleteConnection(DeleteConnectionRequest request)

Deletes a single connection.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.DeleteConnectionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteRepository(DeleteRepositoryRequest request)
    
    
    public Operation deleteRepository(DeleteRepositoryRequest request)

Deletes a single repository.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.DeleteRepositoryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### fetchGitRefs(FetchGitRefsRequest request)
    
    
    public FetchGitRefsResponse fetchGitRefs(FetchGitRefsRequest request)

Fetch the list of branches or tags for a given repository.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchGitRefsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchGitRefsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FetchGitRefsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchGitRefsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### fetchLinkableRepositories(FetchLinkableRepositoriesRequest request)
    
    
    public FetchLinkableRepositoriesResponse fetchLinkableRepositories(FetchLinkableRepositoriesRequest request)

FetchLinkableRepositories get repositories from SCM that are accessible and could be added to the connection.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchLinkableRepositoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchLinkableRepositoriesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FetchLinkableRepositoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchLinkableRepositoriesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### fetchReadToken(FetchReadTokenRequest request)
    
    
    public FetchReadTokenResponse fetchReadToken(FetchReadTokenRequest request)

Fetches read token of a given repository.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchReadTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchReadTokenRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FetchReadTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchReadTokenResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### fetchReadWriteToken(FetchReadWriteTokenRequest request)
    
    
    public FetchReadWriteTokenResponse fetchReadWriteToken(FetchReadWriteTokenRequest request)

Fetches read/write token of a given repository.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FetchReadWriteTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchReadWriteTokenRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FetchReadWriteTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchReadWriteTokenResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getConnection(GetConnectionRequest request)
    
    
    public Connection getConnection(GetConnectionRequest request)

Gets details of a single connection.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.GetConnectionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.Connection)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getRepository(GetRepositoryRequest request)
    
    
    public Repository getRepository(GetRepositoryRequest request)

Gets details of a single repository.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.GetRepositoryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.Repository)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listConnections(ListConnectionsRequest request)
    
    
    public ListConnectionsResponse listConnections(ListConnectionsRequest request)

Lists Connections in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ListConnectionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListConnectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ListConnectionsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listRepositories(ListRepositoriesRequest request)
    
    
    public ListRepositoriesResponse listRepositories(ListRepositoriesRequest request)

Lists Repositories in a given connection.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRepositoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ListRepositoriesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListRepositoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ListRepositoriesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateConnection(UpdateConnectionRequest request)
    
    
    public Operation updateConnection(UpdateConnectionRequest request)

Updates a single connection.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.UpdateConnectionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
