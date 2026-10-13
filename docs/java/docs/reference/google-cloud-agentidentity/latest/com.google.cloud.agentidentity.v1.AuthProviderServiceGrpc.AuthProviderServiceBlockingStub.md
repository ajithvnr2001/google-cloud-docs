---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProviderServiceGrpc.AuthProviderServiceBlockingStub
title: Class AuthProviderServiceGrpc.AuthProviderServiceBlockingStub (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:58.585906+00:00
---

# Class AuthProviderServiceGrpc.AuthProviderServiceBlockingStub (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProviderServiceGrpc.AuthProviderServiceBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AuthProviderServiceGrpc.AuthProviderServiceBlockingStub (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public static final class AuthProviderServiceGrpc.AuthProviderServiceBlockingStub extends AbstractBlockingStub<AuthProviderServiceGrpc.AuthProviderServiceBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service AuthProviderService.

Service describing handlers for resources

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > AuthProviderServiceGrpc.AuthProviderServiceBlockingStub

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

### build(Channel channel, CallOptions callOptions)
    
    
    protected AuthProviderServiceGrpc.AuthProviderServiceBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceGrpc.AuthProviderServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProviderServiceGrpc.AuthProviderServiceBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createAuthProvider(CreateAuthProviderRequest request)
    
    
    public AuthProvider createAuthProvider(CreateAuthProviderRequest request)

Creates a new AuthProvider in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.CreateAuthProviderRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider)` |   
  
### deleteAuthProvider(DeleteAuthProviderRequest request)
    
    
    public Empty deleteAuthProvider(DeleteAuthProviderRequest request)

Deletes a single AuthProvider.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.DeleteAuthProviderRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
  
### deleteAuthorization(DeleteAuthorizationRequest request)
    
    
    public Empty deleteAuthorization(DeleteAuthorizationRequest request)

Deletes a single Authorization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteAuthorizationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.DeleteAuthorizationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
  
### disableAuthProvider(DisableAuthProviderRequest request)
    
    
    public AuthProvider disableAuthProvider(DisableAuthProviderRequest request)

Disables a single AuthProvider.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DisableAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.DisableAuthProviderRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider)` |   
  
### enableAuthProvider(EnableAuthProviderRequest request)
    
    
    public AuthProvider enableAuthProvider(EnableAuthProviderRequest request)

Enables a single AuthProvider.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[EnableAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.EnableAuthProviderRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider)` |   
  
### getAccessSummary(GetAccessSummaryRequest request)
    
    
    public AccessSummary getAccessSummary(GetAccessSummaryRequest request)

Gets details of a single AccessSummary.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAccessSummaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.GetAccessSummaryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AccessSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AccessSummary)` |   
  
### getAuthProvider(GetAuthProviderRequest request)
    
    
    public AuthProvider getAuthProvider(GetAuthProviderRequest request)

Gets details of a single AuthProvider.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.GetAuthProviderRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider)` |   
  
### getAuthorization(GetAuthorizationRequest request)
    
    
    public Authorization getAuthorization(GetAuthorizationRequest request)

Gets details of a single Authorization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAuthorizationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.GetAuthorizationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Authorization](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.Authorization)` |   
  
### listAccessSummaries(ListAccessSummariesRequest request)
    
    
    public ListAccessSummariesResponse listAccessSummaries(ListAccessSummariesRequest request)

Lists AccessSummaries in a given project and location. Supported Filters:

  * `workload_id`: Filter by the SPIFFE ID of the agent. Example: `workload_id="spiffe://example.com/ns/default/sa/my-agent"`



**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAccessSummariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAccessSummariesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListAccessSummariesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAccessSummariesResponse)` |   
  
### listAuthProviders(ListAuthProvidersRequest request)
    
    
    public ListAuthProvidersResponse listAuthProviders(ListAuthProvidersRequest request)

Lists AuthProviders in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAuthProvidersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAuthProvidersRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListAuthProvidersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAuthProvidersResponse)` |   
  
### listAuthorizations(ListAuthorizationsRequest request)
    
    
    public ListAuthorizationsResponse listAuthorizations(ListAuthorizationsRequest request)

Lists Authorizations in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAuthorizationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAuthorizationsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListAuthorizationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAuthorizationsResponse)` |   
  
### queryAuthProviders(QueryAuthProvidersRequest request)
    
    
    public QueryAuthProvidersResponse queryAuthProviders(QueryAuthProvidersRequest request)

Queries what all auth_providers are used by a given workload_id.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryAuthProvidersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.QueryAuthProvidersRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QueryAuthProvidersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.QueryAuthProvidersResponse)` |   
  
### queryWorkloads(QueryWorkloadsRequest request)
    
    
    public QueryWorkloadsResponse queryWorkloads(QueryWorkloadsRequest request)

Queries what all workloads are using a given auth_provider.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[QueryWorkloadsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.QueryWorkloadsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[QueryWorkloadsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.QueryWorkloadsResponse)` |   
  
### revokeAuthorization(RevokeAuthorizationRequest request)
    
    
    public RevokeAuthorizationResponse revokeAuthorization(RevokeAuthorizationRequest request)

Revokes all authorizations for a specific user on an AuthProvider. This deletes all authorization records associated with the user and AuthProvider, effectively revoking access across all agents.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RevokeAuthorizationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.RevokeAuthorizationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RevokeAuthorizationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.RevokeAuthorizationResponse)` |   
  
### undeleteAuthProvider(UndeleteAuthProviderRequest request)
    
    
    public AuthProvider undeleteAuthProvider(UndeleteAuthProviderRequest request)

Undeletes a single AuthProvider.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UndeleteAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.UndeleteAuthProviderRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider)` |   
  
### updateAuthProvider(UpdateAuthProviderRequest request)
    
    
    public AuthProvider updateAuthProvider(UpdateAuthProviderRequest request)

Updates the parameters of a single AuthProvider.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.UpdateAuthProviderRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
