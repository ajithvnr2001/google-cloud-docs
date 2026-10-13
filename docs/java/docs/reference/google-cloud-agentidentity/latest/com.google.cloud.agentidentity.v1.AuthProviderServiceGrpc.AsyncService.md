---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProviderServiceGrpc.AsyncService
title: Interface AuthProviderServiceGrpc.AsyncService (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:55.373616+00:00
---

# Interface AuthProviderServiceGrpc.AsyncService (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProviderServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AuthProviderServiceGrpc.AsyncService (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public static interface AuthProviderServiceGrpc.AsyncService

Service describing handlers for resources

## Methods 

### createAuthProvider(CreateAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)
    
    
    public default void createAuthProvider(CreateAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)

Creates a new AuthProvider in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.CreateAuthProviderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider)>`  
  
  
### deleteAuthProvider(DeleteAuthProviderRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteAuthProvider(DeleteAuthProviderRequest request, StreamObserver<Empty> responseObserver)

Deletes a single AuthProvider.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.DeleteAuthProviderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteAuthorization(DeleteAuthorizationRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void deleteAuthorization(DeleteAuthorizationRequest request, StreamObserver<Empty> responseObserver)

Deletes a single Authorization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAuthorizationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.DeleteAuthorizationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### disableAuthProvider(DisableAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)
    
    
    public default void disableAuthProvider(DisableAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)

Disables a single AuthProvider.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DisableAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.DisableAuthProviderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider)>`  
  
  
### enableAuthProvider(EnableAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)
    
    
    public default void enableAuthProvider(EnableAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)

Enables a single AuthProvider.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[EnableAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.EnableAuthProviderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider)>`  
  
  
### getAccessSummary(GetAccessSummaryRequest request, StreamObserver<AccessSummary> responseObserver)
    
    
    public default void getAccessSummary(GetAccessSummaryRequest request, StreamObserver<AccessSummary> responseObserver)

Gets details of a single AccessSummary.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAccessSummaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.GetAccessSummaryRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AccessSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AccessSummary)>`  
  
  
### getAuthProvider(GetAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)
    
    
    public default void getAuthProvider(GetAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)

Gets details of a single AuthProvider.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.GetAuthProviderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider)>`  
  
  
### getAuthorization(GetAuthorizationRequest request, StreamObserver<Authorization> responseObserver)
    
    
    public default void getAuthorization(GetAuthorizationRequest request, StreamObserver<Authorization> responseObserver)

Gets details of a single Authorization.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAuthorizationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.GetAuthorizationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Authorization](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.Authorization)>`  
  
  
### listAccessSummaries(ListAccessSummariesRequest request, StreamObserver<ListAccessSummariesResponse> responseObserver)
    
    
    public default void listAccessSummaries(ListAccessSummariesRequest request, StreamObserver<ListAccessSummariesResponse> responseObserver)

Lists AccessSummaries in a given project and location. Supported Filters:

  * `workload_id`: Filter by the SPIFFE ID of the agent. Example: `workload_id="spiffe://example.com/ns/default/sa/my-agent"`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAccessSummariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAccessSummariesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListAccessSummariesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAccessSummariesResponse)>`  
  
  
### listAuthProviders(ListAuthProvidersRequest request, StreamObserver<ListAuthProvidersResponse> responseObserver)
    
    
    public default void listAuthProviders(ListAuthProvidersRequest request, StreamObserver<ListAuthProvidersResponse> responseObserver)

Lists AuthProviders in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAuthProvidersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAuthProvidersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListAuthProvidersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAuthProvidersResponse)>`  
  
  
### listAuthorizations(ListAuthorizationsRequest request, StreamObserver<ListAuthorizationsResponse> responseObserver)
    
    
    public default void listAuthorizations(ListAuthorizationsRequest request, StreamObserver<ListAuthorizationsResponse> responseObserver)

Lists Authorizations in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAuthorizationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAuthorizationsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListAuthorizationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAuthorizationsResponse)>`  
  
  
### queryAuthProviders(QueryAuthProvidersRequest request, StreamObserver<QueryAuthProvidersResponse> responseObserver)
    
    
    public default void queryAuthProviders(QueryAuthProvidersRequest request, StreamObserver<QueryAuthProvidersResponse> responseObserver)

Queries what all auth_providers are used by a given workload_id.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryAuthProvidersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.QueryAuthProvidersRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QueryAuthProvidersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.QueryAuthProvidersResponse)>`  
  
  
### queryWorkloads(QueryWorkloadsRequest request, StreamObserver<QueryWorkloadsResponse> responseObserver)
    
    
    public default void queryWorkloads(QueryWorkloadsRequest request, StreamObserver<QueryWorkloadsResponse> responseObserver)

Queries what all workloads are using a given auth_provider.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[QueryWorkloadsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.QueryWorkloadsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[QueryWorkloadsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.QueryWorkloadsResponse)>`  
  
  
### revokeAuthorization(RevokeAuthorizationRequest request, StreamObserver<RevokeAuthorizationResponse> responseObserver)
    
    
    public default void revokeAuthorization(RevokeAuthorizationRequest request, StreamObserver<RevokeAuthorizationResponse> responseObserver)

Revokes all authorizations for a specific user on an AuthProvider. This deletes all authorization records associated with the user and AuthProvider, effectively revoking access across all agents.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RevokeAuthorizationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.RevokeAuthorizationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[RevokeAuthorizationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.RevokeAuthorizationResponse)>`  
  
  
### undeleteAuthProvider(UndeleteAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)
    
    
    public default void undeleteAuthProvider(UndeleteAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)

Undeletes a single AuthProvider.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UndeleteAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.UndeleteAuthProviderRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider)>`  
  
  
### updateAuthProvider(UpdateAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)
    
    
    public default void updateAuthProvider(UpdateAuthProviderRequest request, StreamObserver<AuthProvider> responseObserver)

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
