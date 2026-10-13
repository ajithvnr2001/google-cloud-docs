---
url: https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.stub.PolicyBindingsStub
title: Class PolicyBindingsStub (1.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:23:48.939834+00:00
---

# Class PolicyBindingsStub (1.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.stub.PolicyBindingsStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PolicyBindingsStub (1.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.96.0 (latest)  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.83.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.68.0  1.66.0  1.65.0  1.62.0  1.61.0  1.60.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.7.0 
    
    
    public abstract class PolicyBindingsStub implements BackgroundResource

Base stub class for the PolicyBindings service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > PolicyBindingsStub

## Implements

[BackgroundResource](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.BackgroundResource.html)

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

## Constructors 

### PolicyBindingsStub()
    
    
    public PolicyBindingsStub()

## Methods 

### close()
    
    
    public abstract void close()

### createPolicyBindingCallable()
    
    
    public UnaryCallable<CreatePolicyBindingRequest,Operation> createPolicyBindingCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreatePolicyBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.CreatePolicyBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createPolicyBindingOperationCallable()
    
    
    public OperationCallable<CreatePolicyBindingRequest,PolicyBinding,OperationMetadata> createPolicyBindingOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreatePolicyBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.CreatePolicyBindingRequest),[PolicyBinding](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.PolicyBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.OperationMetadata)>` |   
  
### deletePolicyBindingCallable()
    
    
    public UnaryCallable<DeletePolicyBindingRequest,Operation> deletePolicyBindingCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeletePolicyBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.DeletePolicyBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deletePolicyBindingOperationCallable()
    
    
    public OperationCallable<DeletePolicyBindingRequest,Empty,OperationMetadata> deletePolicyBindingOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeletePolicyBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.DeletePolicyBindingRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.OperationMetadata)>` |   
  
### getHttpJsonOperationsStub()
    
    
    public @Nullable OperationsStub getHttpJsonOperationsStub()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.api.gax.httpjson.longrunning.stub.OperationsStub` |   
  
### getOperationsStub()
    
    
    public @Nullable OperationsStub getOperationsStub()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.longrunning.stub.OperationsStub` |   
  
### getPolicyBindingCallable()
    
    
    public UnaryCallable<GetPolicyBindingRequest,PolicyBinding> getPolicyBindingCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetPolicyBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.GetPolicyBindingRequest),[PolicyBinding](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.PolicyBinding)>` |   
  
### listPolicyBindingsCallable()
    
    
    public UnaryCallable<ListPolicyBindingsRequest,ListPolicyBindingsResponse> listPolicyBindingsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPolicyBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.ListPolicyBindingsRequest),[ListPolicyBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.ListPolicyBindingsResponse)>` |   
  
### listPolicyBindingsPagedCallable()
    
    
    public UnaryCallable<ListPolicyBindingsRequest,PolicyBindingsClient.ListPolicyBindingsPagedResponse> listPolicyBindingsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListPolicyBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.ListPolicyBindingsRequest),[ListPolicyBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.PolicyBindingsClient.ListPolicyBindingsPagedResponse)>` |   
  
### searchTargetPolicyBindingsCallable()
    
    
    public UnaryCallable<SearchTargetPolicyBindingsRequest,SearchTargetPolicyBindingsResponse> searchTargetPolicyBindingsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchTargetPolicyBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.SearchTargetPolicyBindingsRequest),[SearchTargetPolicyBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.SearchTargetPolicyBindingsResponse)>` |   
  
### searchTargetPolicyBindingsPagedCallable()
    
    
    public UnaryCallable<SearchTargetPolicyBindingsRequest,PolicyBindingsClient.SearchTargetPolicyBindingsPagedResponse> searchTargetPolicyBindingsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchTargetPolicyBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.SearchTargetPolicyBindingsRequest),[SearchTargetPolicyBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.PolicyBindingsClient.SearchTargetPolicyBindingsPagedResponse)>` |   
  
### updatePolicyBindingCallable()
    
    
    public UnaryCallable<UpdatePolicyBindingRequest,Operation> updatePolicyBindingCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdatePolicyBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.UpdatePolicyBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updatePolicyBindingOperationCallable()
    
    
    public OperationCallable<UpdatePolicyBindingRequest,PolicyBinding,OperationMetadata> updatePolicyBindingOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdatePolicyBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.UpdatePolicyBindingRequest),[PolicyBinding](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.PolicyBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.OperationMetadata)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
