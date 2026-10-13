---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.OrgPolicyGrpc
title: Class OrgPolicyGrpc (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:53:32.750058+00:00
---

# Class OrgPolicyGrpc (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.OrgPolicyGrpc

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class OrgPolicyGrpc (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.7-SNAPSHOT  2.2.1  2.1.2  2.0.10 
    
    
    public final class OrgPolicyGrpc

An interface for managing organization policies. The Organization Policy Service provides a simple mechanism for organizations to restrict the allowed configurations across their entire resource hierarchy. You can use a policy to configure restrictions on resources. For example, you can enforce a policy that restricts which Google Cloud APIs can be activated in a certain part of your resource hierarchy, or prevents serial port access to VM instances in a particular folder. Policies are inherited down through the resource hierarchy. A policy applied to a parent resource automatically applies to all its child resources unless overridden with a policy lower in the hierarchy. A constraint defines an aspect of a resource's configuration that can be controlled by an organization's policy administrator. Policies are a collection of constraints that defines their allowable configuration on a particular resource and its child resources.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > OrgPolicyGrpc

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

### bindService(OrgPolicyGrpc.AsyncService service)
    
    
    public static final ServerServiceDefinition bindService(OrgPolicyGrpc.AsyncService service)

**Parameter**  
---  
**Name** | **Description**  
`service` | `[OrgPolicyGrpc.AsyncService](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.OrgPolicyGrpc.AsyncService)`  
  
**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServerServiceDefinition` |   
  
### getCreateCustomConstraintMethod()
    
    
    public static MethodDescriptor<CreateCustomConstraintRequest,CustomConstraint> getCreateCustomConstraintMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreateCustomConstraintRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.CreateCustomConstraintRequest),[CustomConstraint](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.CustomConstraint)>` |   
  
### getCreatePolicyMethod()
    
    
    public static MethodDescriptor<CreatePolicyRequest,Policy> getCreatePolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[CreatePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.CreatePolicyRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.Policy)>` |   
  
### getDeleteCustomConstraintMethod()
    
    
    public static MethodDescriptor<DeleteCustomConstraintRequest,Empty> getDeleteCustomConstraintMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeleteCustomConstraintRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.DeleteCustomConstraintRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDeletePolicyMethod()
    
    
    public static MethodDescriptor<DeletePolicyRequest,Empty> getDeletePolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[DeletePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.DeletePolicyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getGetCustomConstraintMethod()
    
    
    public static MethodDescriptor<GetCustomConstraintRequest,CustomConstraint> getGetCustomConstraintMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetCustomConstraintRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.GetCustomConstraintRequest),[CustomConstraint](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.CustomConstraint)>` |   
  
### getGetEffectivePolicyMethod()
    
    
    public static MethodDescriptor<GetEffectivePolicyRequest,Policy> getGetEffectivePolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetEffectivePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.GetEffectivePolicyRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.Policy)>` |   
  
### getGetPolicyMethod()
    
    
    public static MethodDescriptor<GetPolicyRequest,Policy> getGetPolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[GetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.GetPolicyRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.Policy)>` |   
  
### getListConstraintsMethod()
    
    
    public static MethodDescriptor<ListConstraintsRequest,ListConstraintsResponse> getListConstraintsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListConstraintsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.ListConstraintsRequest),[ListConstraintsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.ListConstraintsResponse)>` |   
  
### getListCustomConstraintsMethod()
    
    
    public static MethodDescriptor<ListCustomConstraintsRequest,ListCustomConstraintsResponse> getListCustomConstraintsMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListCustomConstraintsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.ListCustomConstraintsRequest),[ListCustomConstraintsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.ListCustomConstraintsResponse)>` |   
  
### getListPoliciesMethod()
    
    
    public static MethodDescriptor<ListPoliciesRequest,ListPoliciesResponse> getListPoliciesMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[ListPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.ListPoliciesRequest),[ListPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.ListPoliciesResponse)>` |   
  
### getServiceDescriptor()
    
    
    public static ServiceDescriptor getServiceDescriptor()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ServiceDescriptor` |   
  
### getUpdateCustomConstraintMethod()
    
    
    public static MethodDescriptor<UpdateCustomConstraintRequest,CustomConstraint> getUpdateCustomConstraintMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdateCustomConstraintRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.UpdateCustomConstraintRequest),[CustomConstraint](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.CustomConstraint)>` |   
  
### getUpdatePolicyMethod()
    
    
    public static MethodDescriptor<UpdatePolicyRequest,Policy> getUpdatePolicyMethod()

**Returns**  
---  
**Type** | **Description**  
`io.grpc.MethodDescriptor<[UpdatePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.UpdatePolicyRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.Policy)>` |   
  
### newBlockingStub(Channel channel)
    
    
    public static OrgPolicyGrpc.OrgPolicyBlockingStub newBlockingStub(Channel channel)

Creates a new blocking-style stub that supports unary and streaming output calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrgPolicyGrpc.OrgPolicyBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.OrgPolicyGrpc.OrgPolicyBlockingStub)` |   
  
### newBlockingV2Stub(Channel channel)
    
    
    public static OrgPolicyGrpc.OrgPolicyBlockingV2Stub newBlockingV2Stub(Channel channel)

Creates a new blocking-style stub that supports all types of calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrgPolicyGrpc.OrgPolicyBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.OrgPolicyGrpc.OrgPolicyBlockingV2Stub)` |   
  
### newFutureStub(Channel channel)
    
    
    public static OrgPolicyGrpc.OrgPolicyFutureStub newFutureStub(Channel channel)

Creates a new ListenableFuture-style stub that supports unary calls on the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrgPolicyGrpc.OrgPolicyFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.OrgPolicyGrpc.OrgPolicyFutureStub)` |   
  
### newStub(Channel channel)
    
    
    public static OrgPolicyGrpc.OrgPolicyStub newStub(Channel channel)

Creates a new async stub that supports all call types for the service

**Parameter**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrgPolicyGrpc.OrgPolicyStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.OrgPolicyGrpc.OrgPolicyStub)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
