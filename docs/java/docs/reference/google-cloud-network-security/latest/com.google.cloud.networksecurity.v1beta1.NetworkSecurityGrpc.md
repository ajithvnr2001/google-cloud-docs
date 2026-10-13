---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.NetworkSecurityGrpc
title: Class NetworkSecurityGrpc (0.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:50.392992+00:00
---

# Class NetworkSecurityGrpc (0.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.NetworkSecurityGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class NetworkSecurityGrpc (0.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.102.0 (latest)  0.98.0  0.97.0  0.96.0  0.94.0  0.91.0  0.90.0  0.88.0  0.86.0  0.85.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.67.0  0.66.0  0.65.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.4  0.5.1  0.4.4 
    
    
    public final class NetworkSecurityGrpc

Network Security API provides resources to configure authentication and authorization policies. Refer to per API resource documentation for more information.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > NetworkSecurityGrpc

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

### bindService(NetworkSecurityGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(NetworkSecurityGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[NetworkSecurityGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.NetworkSecurityGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getCreateAuthorizationPolicyMethod()
    
    
    public static MethodDescriptor<CreateAuthorizationPolicyRequest,Operation> getCreateAuthorizationPolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateAuthorizationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.CreateAuthorizationPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getCreateClientTlsPolicyMethod()
    
    
    public static MethodDescriptor<CreateClientTlsPolicyRequest,Operation> getCreateClientTlsPolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateClientTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.CreateClientTlsPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getCreateServerTlsPolicyMethod()
    
    
    public static MethodDescriptor<CreateServerTlsPolicyRequest,Operation> getCreateServerTlsPolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateServerTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.CreateServerTlsPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteAuthorizationPolicyMethod()
    
    
    public static MethodDescriptor<DeleteAuthorizationPolicyRequest,Operation> getDeleteAuthorizationPolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteAuthorizationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.DeleteAuthorizationPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteClientTlsPolicyMethod()
    
    
    public static MethodDescriptor<DeleteClientTlsPolicyRequest,Operation> getDeleteClientTlsPolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteClientTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.DeleteClientTlsPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDeleteServerTlsPolicyMethod()
    
    
    public static MethodDescriptor<DeleteServerTlsPolicyRequest,Operation> getDeleteServerTlsPolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteServerTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.DeleteServerTlsPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getGetAuthorizationPolicyMethod()
    
    
    public static MethodDescriptor<GetAuthorizationPolicyRequest,AuthorizationPolicy> getGetAuthorizationPolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetAuthorizationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.GetAuthorizationPolicyRequest),[AuthorizationPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.AuthorizationPolicy)>` |   
  
### getGetClientTlsPolicyMethod()
    
    
    public static MethodDescriptor<GetClientTlsPolicyRequest,ClientTlsPolicy> getGetClientTlsPolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetClientTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.GetClientTlsPolicyRequest),[ClientTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ClientTlsPolicy)>` |   
  
### getGetServerTlsPolicyMethod()
    
    
    public static MethodDescriptor<GetServerTlsPolicyRequest,ServerTlsPolicy> getGetServerTlsPolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetServerTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.GetServerTlsPolicyRequest),[ServerTlsPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ServerTlsPolicy)>` |   
  
### getListAuthorizationPoliciesMethod()
    
    
    public static MethodDescriptor<ListAuthorizationPoliciesRequest,ListAuthorizationPoliciesResponse> getListAuthorizationPoliciesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListAuthorizationPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ListAuthorizationPoliciesRequest),[ListAuthorizationPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ListAuthorizationPoliciesResponse)>` |   
  
### getListClientTlsPoliciesMethod()
    
    
    public static MethodDescriptor<ListClientTlsPoliciesRequest,ListClientTlsPoliciesResponse> getListClientTlsPoliciesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListClientTlsPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ListClientTlsPoliciesRequest),[ListClientTlsPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ListClientTlsPoliciesResponse)>` |   
  
### getListServerTlsPoliciesMethod()
    
    
    public static MethodDescriptor<ListServerTlsPoliciesRequest,ListServerTlsPoliciesResponse> getListServerTlsPoliciesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListServerTlsPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ListServerTlsPoliciesRequest),[ListServerTlsPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.ListServerTlsPoliciesResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getUpdateAuthorizationPolicyMethod()
    
    
    public static MethodDescriptor<UpdateAuthorizationPolicyRequest,Operation> getUpdateAuthorizationPolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateAuthorizationPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.UpdateAuthorizationPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getUpdateClientTlsPolicyMethod()
    
    
    public static MethodDescriptor<UpdateClientTlsPolicyRequest,Operation> getUpdateClientTlsPolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateClientTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.UpdateClientTlsPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getUpdateServerTlsPolicyMethod()
    
    
    public static MethodDescriptor<UpdateServerTlsPolicyRequest,Operation> getUpdateServerTlsPolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateServerTlsPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.UpdateServerTlsPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static NetworkSecurityGrpc.NetworkSecurityBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityGrpc.NetworkSecurityBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.NetworkSecurityGrpc.NetworkSecurityBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static NetworkSecurityGrpc.NetworkSecurityBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityGrpc.NetworkSecurityBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.NetworkSecurityGrpc.NetworkSecurityBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static NetworkSecurityGrpc.NetworkSecurityFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityGrpc.NetworkSecurityFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.NetworkSecurityGrpc.NetworkSecurityFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static NetworkSecurityGrpc.NetworkSecurityStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkSecurityGrpc.NetworkSecurityStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1beta1.NetworkSecurityGrpc.NetworkSecurityStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
