---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProviderServiceGrpc
title: Class AuthProviderServiceGrpc (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:58.282475+00:00
---

# Class AuthProviderServiceGrpc (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProviderServiceGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AuthProviderServiceGrpc (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public final class AuthProviderServiceGrpc

Service describing handlers for resources

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > AuthProviderServiceGrpc

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

### bindService(AuthProviderServiceGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(AuthProviderServiceGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[AuthProviderServiceGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProviderServiceGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getCreateAuthProviderMethod()
    
    
    public static MethodDescriptor<CreateAuthProviderRequest,AuthProvider> getCreateAuthProviderMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.CreateAuthProviderRequest),[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider)>` |   
  
### getDeleteAuthProviderMethod()
    
    
    public static MethodDescriptor<DeleteAuthProviderRequest,Empty> getDeleteAuthProviderMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.DeleteAuthProviderRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDeleteAuthorizationMethod()
    
    
    public static MethodDescriptor<DeleteAuthorizationRequest,Empty> getDeleteAuthorizationMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteAuthorizationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.DeleteAuthorizationRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDisableAuthProviderMethod()
    
    
    public static MethodDescriptor<DisableAuthProviderRequest,AuthProvider> getDisableAuthProviderMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DisableAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.DisableAuthProviderRequest),[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider)>` |   
  
### getEnableAuthProviderMethod()
    
    
    public static MethodDescriptor<EnableAuthProviderRequest,AuthProvider> getEnableAuthProviderMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[EnableAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.EnableAuthProviderRequest),[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider)>` |   
  
### getGetAccessSummaryMethod()
    
    
    public static MethodDescriptor<GetAccessSummaryRequest,AccessSummary> getGetAccessSummaryMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetAccessSummaryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.GetAccessSummaryRequest),[AccessSummary](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AccessSummary)>` |   
  
### getGetAuthProviderMethod()
    
    
    public static MethodDescriptor<GetAuthProviderRequest,AuthProvider> getGetAuthProviderMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.GetAuthProviderRequest),[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider)>` |   
  
### getGetAuthorizationMethod()
    
    
    public static MethodDescriptor<GetAuthorizationRequest,Authorization> getGetAuthorizationMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetAuthorizationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.GetAuthorizationRequest),[Authorization](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.Authorization)>` |   
  
### getListAccessSummariesMethod()
    
    
    public static MethodDescriptor<ListAccessSummariesRequest,ListAccessSummariesResponse> getListAccessSummariesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListAccessSummariesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAccessSummariesRequest),[ListAccessSummariesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAccessSummariesResponse)>` |   
  
### getListAuthProvidersMethod()
    
    
    public static MethodDescriptor<ListAuthProvidersRequest,ListAuthProvidersResponse> getListAuthProvidersMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListAuthProvidersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAuthProvidersRequest),[ListAuthProvidersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAuthProvidersResponse)>` |   
  
### getListAuthorizationsMethod()
    
    
    public static MethodDescriptor<ListAuthorizationsRequest,ListAuthorizationsResponse> getListAuthorizationsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListAuthorizationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAuthorizationsRequest),[ListAuthorizationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.ListAuthorizationsResponse)>` |   
  
### getQueryAuthProvidersMethod()
    
    
    public static MethodDescriptor<QueryAuthProvidersRequest,QueryAuthProvidersResponse> getQueryAuthProvidersMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[QueryAuthProvidersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.QueryAuthProvidersRequest),[QueryAuthProvidersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.QueryAuthProvidersResponse)>` |   
  
### getQueryWorkloadsMethod()
    
    
    public static MethodDescriptor<QueryWorkloadsRequest,QueryWorkloadsResponse> getQueryWorkloadsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[QueryWorkloadsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.QueryWorkloadsRequest),[QueryWorkloadsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.QueryWorkloadsResponse)>` |   
  
### getRevokeAuthorizationMethod()
    
    
    public static MethodDescriptor<RevokeAuthorizationRequest,RevokeAuthorizationResponse> getRevokeAuthorizationMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[RevokeAuthorizationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.RevokeAuthorizationRequest),[RevokeAuthorizationResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.RevokeAuthorizationResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getUndeleteAuthProviderMethod()
    
    
    public static MethodDescriptor<UndeleteAuthProviderRequest,AuthProvider> getUndeleteAuthProviderMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UndeleteAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.UndeleteAuthProviderRequest),[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider)>` |   
  
### getUpdateAuthProviderMethod()
    
    
    public static MethodDescriptor<UpdateAuthProviderRequest,AuthProvider> getUpdateAuthProviderMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateAuthProviderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.UpdateAuthProviderRequest),[AuthProvider](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProvider)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static AuthProviderServiceGrpc.AuthProviderServiceBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceGrpc.AuthProviderServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProviderServiceGrpc.AuthProviderServiceBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static AuthProviderServiceGrpc.AuthProviderServiceBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceGrpc.AuthProviderServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProviderServiceGrpc.AuthProviderServiceBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static AuthProviderServiceGrpc.AuthProviderServiceFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceGrpc.AuthProviderServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProviderServiceGrpc.AuthProviderServiceFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static AuthProviderServiceGrpc.AuthProviderServiceStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[AuthProviderServiceGrpc.AuthProviderServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-agentidentity/latest/com.google.cloud.agentidentity.v1.AuthProviderServiceGrpc.AuthProviderServiceStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
