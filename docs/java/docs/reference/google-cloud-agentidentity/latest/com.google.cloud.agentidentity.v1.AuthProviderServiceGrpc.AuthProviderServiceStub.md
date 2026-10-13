---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProviderServiceGrpc.AuthProviderServiceStub
title: Class AuthProviderServiceGrpc.AuthProviderServiceStub (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:34.078410+00:00
---

# Class AuthProviderServiceGrpc.AuthProviderServiceStub (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProviderServiceGrpc.AuthProviderServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AuthProviderServiceGrpc.AuthProviderServiceStub (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public static final class AuthProviderServiceGrpc.AuthProviderServiceStub extends AbstractAsyncStub<AuthProviderServiceGrpc.AuthProviderServiceStub>

A stub to allow clients to do asynchronous rpc calls to service AuthProviderService.

Service describing handlers for resources

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > AuthProviderServiceGrpc.AuthProviderServiceStub

## Inherited Members

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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

### build(Channel channel, CallOptions callOptions)
    
    
    protected AuthProviderServiceGrpc.AuthProviderServiceStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceGrpc.AuthProviderServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProviderServiceGrpc.AuthProviderServiceStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createAuthProvider(CreateAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)
    
    
    public void createAuthProvider(CreateAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)

Creates a new AuthProvider in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.CreateAuthProviderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider)>`  
  
  
### deleteAuthProvider(DeleteAuthProviderRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteAuthProvider(DeleteAuthProviderRequest request, StreamObserver<Empty> responseObserver)

Deletes a single AuthProvider.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.DeleteAuthProviderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteAuthorization(DeleteAuthorizationRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteAuthorization(DeleteAuthorizationRequest request, StreamObserver<Empty> responseObserver)

Deletes a single Authorization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAuthorizationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.DeleteAuthorizationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### disableAuthProvider(DisableAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)
    
    
    public void disableAuthProvider(DisableAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)

Disables a single AuthProvider.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DisableAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.DisableAuthProviderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider)>`  
  
  
### enableAuthProvider(EnableAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)
    
    
    public void enableAuthProvider(EnableAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)

Enables a single AuthProvider.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[EnableAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.EnableAuthProviderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider)>`  
  
  
### getAccessSummary(GetAccessSummaryRequest request, StreamObserver<AccessSummary> responseObserver)
    
    
    public void getAccessSummary(GetAccessSummaryRequest request, StreamObserver<AccessSummary> responseObserver)

Gets details of a single AccessSummary.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAccessSummaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.GetAccessSummaryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AccessSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AccessSummary)>`  
  
  
### getAuthProvider(GetAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)
    
    
    public void getAuthProvider(GetAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)

Gets details of a single AuthProvider.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.GetAuthProviderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider)>`  
  
  
### getAuthorization(GetAuthorizationRequest request, StreamObserver<Authorization> responseObserver)
    
    
    public void getAuthorization(GetAuthorizationRequest request, StreamObserver<Authorization> responseObserver)

Gets details of a single Authorization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAuthorizationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.GetAuthorizationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Authorization](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.Authorization)>`  
  
  
### listAccessSummaries(ListAccessSummariesRequest request, StreamObserver<ListAccessSummariesResponse> responseObserver)
    
    
    public void listAccessSummaries(ListAccessSummariesRequest request, StreamObserver<ListAccessSummariesResponse> responseObserver)

Lists AccessSummaries in a given project and location. Supported Filters:

  * `workload_id`: Filter by the SPIFFE ID of the agent. Example: `workload_id="spiffe://example.com/ns/default/sa/my-agent"`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAccessSummariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAccessSummariesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListAccessSummariesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAccessSummariesResponse)>`  
  
  
### listAuthProviders(ListAuthProvidersRequest request, StreamObserver<ListAuthProvidersResponse> responseObserver)
    
    
    public void listAuthProviders(ListAuthProvidersRequest request, StreamObserver<ListAuthProvidersResponse> responseObserver)

Lists AuthProviders in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAuthProvidersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAuthProvidersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListAuthProvidersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAuthProvidersResponse)>`  
  
  
### listAuthorizations(ListAuthorizationsRequest request, StreamObserver<ListAuthorizationsResponse> responseObserver)
    
    
    public void listAuthorizations(ListAuthorizationsRequest request, StreamObserver<ListAuthorizationsResponse> responseObserver)

Lists Authorizations in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAuthorizationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAuthorizationsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListAuthorizationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAuthorizationsResponse)>`  
  
  
### queryAuthProviders(QueryAuthProvidersRequest request, StreamObserver<QueryAuthProvidersResponse> responseObserver)
    
    
    public void queryAuthProviders(QueryAuthProvidersRequest request, StreamObserver<QueryAuthProvidersResponse> responseObserver)

Queries what all auth_providers are used by a given workload_id.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryAuthProvidersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.QueryAuthProvidersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QueryAuthProvidersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.QueryAuthProvidersResponse)>`  
  
  
### queryWorkloads(QueryWorkloadsRequest request, StreamObserver<QueryWorkloadsResponse> responseObserver)
    
    
    public void queryWorkloads(QueryWorkloadsRequest request, StreamObserver<QueryWorkloadsResponse> responseObserver)

Queries what all workloads are using a given auth_provider.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryWorkloadsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.QueryWorkloadsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QueryWorkloadsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.QueryWorkloadsResponse)>`  
  
  
### revokeAuthorization(RevokeAuthorizationRequest request, StreamObserver<RevokeAuthorizationResponse> responseObserver)
    
    
    public void revokeAuthorization(RevokeAuthorizationRequest request, StreamObserver<RevokeAuthorizationResponse> responseObserver)

Revokes all authorizations for a specific user on an AuthProvider. This deletes all authorization records associated with the user and AuthProvider, effectively revoking access across all agents.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RevokeAuthorizationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.RevokeAuthorizationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[RevokeAuthorizationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.RevokeAuthorizationResponse)>`  
  
  
### undeleteAuthProvider(UndeleteAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)
    
    
    public void undeleteAuthProvider(UndeleteAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)

Undeletes a single AuthProvider.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UndeleteAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.UndeleteAuthProviderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider)>`  
  
  
### updateAuthProvider(UpdateAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)
    
    
    public void updateAuthProvider(UpdateAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)

Updates the parameters of a single AuthProvider.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.UpdateAuthProviderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
