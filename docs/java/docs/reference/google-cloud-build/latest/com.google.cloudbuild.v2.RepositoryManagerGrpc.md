---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.RepositoryManagerGrpc
title: Class RepositoryManagerGrpc (3.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:43:55.135782+00:00
---

# Class RepositoryManagerGrpc (3.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.RepositoryManagerGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RepositoryManagerGrpc (3.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.101.0 (latest)  3.97.0  3.96.0  3.95.0  3.93.0  3.90.0  3.89.0  3.87.0  3.85.0  3.84.0  3.83.0  3.82.0  3.80.0  3.78.0  3.77.0  3.76.0  3.75.0  3.74.0  3.72.0  3.70.0  3.69.0  3.66.0  3.65.0  3.64.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.6  3.4.1  3.3.12 
    
    
    public final class RepositoryManagerGrpc

Manages connections to source code repositories.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RepositoryManagerGrpc

## Inherited Members

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

## Static Fields 

### SERVICE_NAME
    
    
    public static final String SERVICE_NAME

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Static Methods 

### bindService(RepositoryManagerGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(RepositoryManagerGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[RepositoryManagerGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.RepositoryManagerGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getBatchCreateRepositoriesMethod()
    
    
    public static MethodDescriptor<BatchCreateRepositoriesRequest,Operation> getBatchCreateRepositoriesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[BatchCreateRepositoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.BatchCreateRepositoriesRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getCreateConnectionMethod()
    
    
    public static MethodDescriptor<CreateConnectionRequest,Operation> getCreateConnectionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.CreateConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getCreateRepositoryMethod()
    
    
    public static MethodDescriptor<CreateRepositoryRequest,Operation> getCreateRepositoryMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.CreateRepositoryRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteConnectionMethod()
    
    
    public static MethodDescriptor<DeleteConnectionRequest,Operation> getDeleteConnectionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.DeleteConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteRepositoryMethod()
    
    
    public static MethodDescriptor<DeleteRepositoryRequest,Operation> getDeleteRepositoryMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.DeleteRepositoryRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getFetchGitRefsMethod()
    
    
    public static MethodDescriptor<FetchGitRefsRequest,FetchGitRefsResponse> getFetchGitRefsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[FetchGitRefsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchGitRefsRequest),[FetchGitRefsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchGitRefsResponse)>` |   
  
### getFetchLinkableRepositoriesMethod()
    
    
    public static MethodDescriptor<FetchLinkableRepositoriesRequest,FetchLinkableRepositoriesResponse> getFetchLinkableRepositoriesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[FetchLinkableRepositoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchLinkableRepositoriesRequest),[FetchLinkableRepositoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchLinkableRepositoriesResponse)>` |   
  
### getFetchReadTokenMethod()
    
    
    public static MethodDescriptor<FetchReadTokenRequest,FetchReadTokenResponse> getFetchReadTokenMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[FetchReadTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchReadTokenRequest),[FetchReadTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchReadTokenResponse)>` |   
  
### getFetchReadWriteTokenMethod()
    
    
    public static MethodDescriptor<FetchReadWriteTokenRequest,FetchReadWriteTokenResponse> getFetchReadWriteTokenMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[FetchReadWriteTokenRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchReadWriteTokenRequest),[FetchReadWriteTokenResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.FetchReadWriteTokenResponse)>` |   
  
### getGetConnectionMethod()
    
    
    public static MethodDescriptor<GetConnectionRequest,Connection> getGetConnectionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.GetConnectionRequest),[Connection](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.Connection)>` |   
  
### getGetRepositoryMethod()
    
    
    public static MethodDescriptor<GetRepositoryRequest,Repository> getGetRepositoryMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetRepositoryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.GetRepositoryRequest),[Repository](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.Repository)>` |   
  
### getListConnectionsMethod()
    
    
    public static MethodDescriptor<ListConnectionsRequest,ListConnectionsResponse> getListConnectionsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListConnectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ListConnectionsRequest),[ListConnectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ListConnectionsResponse)>` |   
  
### getListRepositoriesMethod()
    
    
    public static MethodDescriptor<ListRepositoriesRequest,ListRepositoriesResponse> getListRepositoriesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListRepositoriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ListRepositoriesRequest),[ListRepositoriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.ListRepositoriesResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getUpdateConnectionMethod()
    
    
    public static MethodDescriptor<UpdateConnectionRequest,Operation> getUpdateConnectionMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateConnectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.UpdateConnectionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static RepositoryManagerGrpc.RepositoryManagerBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[RepositoryManagerGrpc.RepositoryManagerBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.RepositoryManagerGrpc.RepositoryManagerBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static RepositoryManagerGrpc.RepositoryManagerBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[RepositoryManagerGrpc.RepositoryManagerBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.RepositoryManagerGrpc.RepositoryManagerBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static RepositoryManagerGrpc.RepositoryManagerFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[RepositoryManagerGrpc.RepositoryManagerFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.RepositoryManagerGrpc.RepositoryManagerFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static RepositoryManagerGrpc.RepositoryManagerStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[RepositoryManagerGrpc.RepositoryManagerStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v2.RepositoryManagerGrpc.RepositoryManagerStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
