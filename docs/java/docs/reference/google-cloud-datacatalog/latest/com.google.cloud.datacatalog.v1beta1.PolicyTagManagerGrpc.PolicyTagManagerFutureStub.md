---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.PolicyTagManagerGrpc.PolicyTagManagerFutureStub
title: Class PolicyTagManagerGrpc.PolicyTagManagerFutureStub (1.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:33.791658+00:00
---

# Class PolicyTagManagerGrpc.PolicyTagManagerFutureStub (1.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.PolicyTagManagerGrpc.PolicyTagManagerFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PolicyTagManagerGrpc.PolicyTagManagerFutureStub (1.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.101.0 (latest)  1.100.0  1.99.0  1.97.0  1.94.0  1.93.0  1.91.0  1.89.0  1.88.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.70.0  1.69.0  1.68.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.5  1.8.4  1.7.2  1.6.2  1.5.4 
    
    
    public static final class PolicyTagManagerGrpc.PolicyTagManagerFutureStub extends AbstractFutureStub<PolicyTagManagerGrpc.PolicyTagManagerFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service PolicyTagManager.

The policy tag manager API service allows clients to manage their taxonomies and policy tags.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > PolicyTagManagerGrpc.PolicyTagManagerFutureStub

## Inherited Members

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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
    
    
    protected PolicyTagManagerGrpc.PolicyTagManagerFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[PolicyTagManagerGrpc.PolicyTagManagerFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.PolicyTagManagerGrpc.PolicyTagManagerFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createPolicyTag(CreatePolicyTagRequest request)
    
    
    public ListenableFuture<PolicyTag> createPolicyTag(CreatePolicyTagRequest request)

Creates a policy tag in the specified taxonomy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePolicyTagRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.CreatePolicyTagRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[PolicyTag](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.PolicyTag)>` |   
  
### createTaxonomy(CreateTaxonomyRequest request)
    
    
    public ListenableFuture<Taxonomy> createTaxonomy(CreateTaxonomyRequest request)

Creates a taxonomy in the specified project.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateTaxonomyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.CreateTaxonomyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Taxonomy](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Taxonomy)>` |   
  
### deletePolicyTag(DeletePolicyTagRequest request)
    
    
    public ListenableFuture<Empty> deletePolicyTag(DeletePolicyTagRequest request)

Deletes a policy tag. Also deletes all of its descendant policy tags.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePolicyTagRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.DeletePolicyTagRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteTaxonomy(DeleteTaxonomyRequest request)
    
    
    public ListenableFuture<Empty> deleteTaxonomy(DeleteTaxonomyRequest request)

Deletes a taxonomy. This operation will also delete all policy tags in this taxonomy along with their associated policies.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteTaxonomyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.DeleteTaxonomyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public ListenableFuture<Policy> getIamPolicy(GetIamPolicyRequest request)

Gets the IAM policy for a taxonomy or a policy tag.

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<com.google.iam.v1.Policy>` |   
  
### getPolicyTag(GetPolicyTagRequest request)
    
    
    public ListenableFuture<PolicyTag> getPolicyTag(GetPolicyTagRequest request)

Gets a policy tag.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPolicyTagRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.GetPolicyTagRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[PolicyTag](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.PolicyTag)>` |   
  
### getTaxonomy(GetTaxonomyRequest request)
    
    
    public ListenableFuture<Taxonomy> getTaxonomy(GetTaxonomyRequest request)

Gets a taxonomy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTaxonomyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.GetTaxonomyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Taxonomy](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Taxonomy)>` |   
  
### listPolicyTags(ListPolicyTagsRequest request)
    
    
    public ListenableFuture<ListPolicyTagsResponse> listPolicyTags(ListPolicyTagsRequest request)

Lists all policy tags in a taxonomy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPolicyTagsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.ListPolicyTagsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListPolicyTagsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.ListPolicyTagsResponse)>` |   
  
### listTaxonomies(ListTaxonomiesRequest request)
    
    
    public ListenableFuture<ListTaxonomiesResponse> listTaxonomies(ListTaxonomiesRequest request)

Lists all taxonomies in a project in a particular location that the caller has permission to view.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTaxonomiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.ListTaxonomiesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListTaxonomiesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.ListTaxonomiesResponse)>` |   
  
### setIamPolicy(SetIamPolicyRequest request)
    
    
    public ListenableFuture<Policy> setIamPolicy(SetIamPolicyRequest request)

Sets the IAM policy for a taxonomy or a policy tag.

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<com.google.iam.v1.Policy>` |   
  
### testIamPermissions(TestIamPermissionsRequest request)
    
    
    public ListenableFuture<TestIamPermissionsResponse> testIamPermissions(TestIamPermissionsRequest request)

Returns the permissions that a caller has on the specified taxonomy or policy tag.

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.TestIamPermissionsRequest`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updatePolicyTag(UpdatePolicyTagRequest request)
    
    
    public ListenableFuture<PolicyTag> updatePolicyTag(UpdatePolicyTagRequest request)

Updates a policy tag.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePolicyTagRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.UpdatePolicyTagRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[PolicyTag](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.PolicyTag)>` |   
  
### updateTaxonomy(UpdateTaxonomyRequest request)
    
    
    public ListenableFuture<Taxonomy> updateTaxonomy(UpdateTaxonomyRequest request)

Updates a taxonomy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTaxonomyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.UpdateTaxonomyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Taxonomy](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1beta1.Taxonomy)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
