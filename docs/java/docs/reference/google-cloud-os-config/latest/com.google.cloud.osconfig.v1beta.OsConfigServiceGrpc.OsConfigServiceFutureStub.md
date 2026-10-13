---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.OsConfigServiceGrpc.OsConfigServiceFutureStub
title: Class OsConfigServiceGrpc.OsConfigServiceFutureStub (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:26.598184+00:00
---

# Class OsConfigServiceGrpc.OsConfigServiceFutureStub (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.OsConfigServiceGrpc.OsConfigServiceFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class OsConfigServiceGrpc.OsConfigServiceFutureStub (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.6  2.4.3  2.3.2 
    
    
    public static final class OsConfigServiceGrpc.OsConfigServiceFutureStub extends AbstractFutureStub<OsConfigServiceGrpc.OsConfigServiceFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service OsConfigService.

OS Config API The OS Config service is a server-side component that you can use to manage package installations and patch jobs for virtual machine instances.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > OsConfigServiceGrpc.OsConfigServiceFutureStub

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
    
    
    protected OsConfigServiceGrpc.OsConfigServiceFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[OsConfigServiceGrpc.OsConfigServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.OsConfigServiceGrpc.OsConfigServiceFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### cancelPatchJob(PatchJobs.CancelPatchJobRequest request)
    
    
    public ListenableFuture<PatchJobs.PatchJob> cancelPatchJob(PatchJobs.CancelPatchJobRequest request)

Cancel a patch job. The patch job must be active. Canceled patch jobs cannot be restarted.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchJobs.CancelPatchJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.CancelPatchJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[PatchJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchJob)>` |   
  
### createGuestPolicy(GuestPolicies.CreateGuestPolicyRequest request)
    
    
    public ListenableFuture<GuestPolicies.GuestPolicy> createGuestPolicy(GuestPolicies.CreateGuestPolicyRequest request)

Create an OS Config guest policy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GuestPolicies.CreateGuestPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.GuestPolicies.CreateGuestPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[GuestPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.GuestPolicies.GuestPolicy)>` |   
  
### createPatchDeployment(PatchDeployments.CreatePatchDeploymentRequest request)
    
    
    public ListenableFuture<PatchDeployments.PatchDeployment> createPatchDeployment(PatchDeployments.CreatePatchDeploymentRequest request)

Create an OS Config patch deployment.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchDeployments.CreatePatchDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchDeployments.CreatePatchDeploymentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchDeployments.PatchDeployment)>` |   
  
### deleteGuestPolicy(GuestPolicies.DeleteGuestPolicyRequest request)
    
    
    public ListenableFuture<Empty> deleteGuestPolicy(GuestPolicies.DeleteGuestPolicyRequest request)

Delete an OS Config guest policy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GuestPolicies.DeleteGuestPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.GuestPolicies.DeleteGuestPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deletePatchDeployment(PatchDeployments.DeletePatchDeploymentRequest request)
    
    
    public ListenableFuture<Empty> deletePatchDeployment(PatchDeployments.DeletePatchDeploymentRequest request)

Delete an OS Config patch deployment.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchDeployments.DeletePatchDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchDeployments.DeletePatchDeploymentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### executePatchJob(PatchJobs.ExecutePatchJobRequest request)
    
    
    public ListenableFuture<PatchJobs.PatchJob> executePatchJob(PatchJobs.ExecutePatchJobRequest request)

Patch VM instances by creating and running a patch job.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchJobs.ExecutePatchJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.ExecutePatchJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[PatchJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchJob)>` |   
  
### getGuestPolicy(GuestPolicies.GetGuestPolicyRequest request)
    
    
    public ListenableFuture<GuestPolicies.GuestPolicy> getGuestPolicy(GuestPolicies.GetGuestPolicyRequest request)

Get an OS Config guest policy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GuestPolicies.GetGuestPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.GuestPolicies.GetGuestPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[GuestPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.GuestPolicies.GuestPolicy)>` |   
  
### getPatchDeployment(PatchDeployments.GetPatchDeploymentRequest request)
    
    
    public ListenableFuture<PatchDeployments.PatchDeployment> getPatchDeployment(PatchDeployments.GetPatchDeploymentRequest request)

Get an OS Config patch deployment.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchDeployments.GetPatchDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchDeployments.GetPatchDeploymentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchDeployments.PatchDeployment)>` |   
  
### getPatchJob(PatchJobs.GetPatchJobRequest request)
    
    
    public ListenableFuture<PatchJobs.PatchJob> getPatchJob(PatchJobs.GetPatchJobRequest request)

Get the patch job. This can be used to track the progress of an ongoing patch job or review the details of completed jobs.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchJobs.GetPatchJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.GetPatchJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[PatchJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.PatchJob)>` |   
  
### listGuestPolicies(GuestPolicies.ListGuestPoliciesRequest request)
    
    
    public ListenableFuture<GuestPolicies.ListGuestPoliciesResponse> listGuestPolicies(GuestPolicies.ListGuestPoliciesRequest request)

Get a page of OS Config guest policies.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GuestPolicies.ListGuestPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.GuestPolicies.ListGuestPoliciesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListGuestPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.GuestPolicies.ListGuestPoliciesResponse)>` |   
  
### listPatchDeployments(PatchDeployments.ListPatchDeploymentsRequest request)
    
    
    public ListenableFuture<PatchDeployments.ListPatchDeploymentsResponse> listPatchDeployments(PatchDeployments.ListPatchDeploymentsRequest request)

Get a page of OS Config patch deployments.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchDeployments.ListPatchDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchDeployments.ListPatchDeploymentsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListPatchDeploymentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchDeployments.ListPatchDeploymentsResponse)>` |   
  
### listPatchJobInstanceDetails(PatchJobs.ListPatchJobInstanceDetailsRequest request)
    
    
    public ListenableFuture<PatchJobs.ListPatchJobInstanceDetailsResponse> listPatchJobInstanceDetails(PatchJobs.ListPatchJobInstanceDetailsRequest request)

Get a list of instance details for a given patch job.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchJobs.ListPatchJobInstanceDetailsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.ListPatchJobInstanceDetailsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListPatchJobInstanceDetailsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.ListPatchJobInstanceDetailsResponse)>` |   
  
### listPatchJobs(PatchJobs.ListPatchJobsRequest request)
    
    
    public ListenableFuture<PatchJobs.ListPatchJobsResponse> listPatchJobs(PatchJobs.ListPatchJobsRequest request)

Get a list of patch jobs.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchJobs.ListPatchJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.ListPatchJobsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListPatchJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchJobs.ListPatchJobsResponse)>` |   
  
### lookupEffectiveGuestPolicy(GuestPolicies.LookupEffectiveGuestPolicyRequest request)
    
    
    public ListenableFuture<GuestPolicies.EffectiveGuestPolicy> lookupEffectiveGuestPolicy(GuestPolicies.LookupEffectiveGuestPolicyRequest request)

Lookup the effective guest policy that applies to a VM instance. This lookup merges all policies that are assigned to the instance ancestry.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GuestPolicies.LookupEffectiveGuestPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.GuestPolicies.LookupEffectiveGuestPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[EffectiveGuestPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.GuestPolicies.EffectiveGuestPolicy)>` |   
  
### pausePatchDeployment(PatchDeployments.PausePatchDeploymentRequest request)
    
    
    public ListenableFuture<PatchDeployments.PatchDeployment> pausePatchDeployment(PatchDeployments.PausePatchDeploymentRequest request)

Change state of patch deployment to "PAUSED". Patch deployment in paused state doesn't generate patch jobs.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchDeployments.PausePatchDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchDeployments.PausePatchDeploymentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchDeployments.PatchDeployment)>` |   
  
### resumePatchDeployment(PatchDeployments.ResumePatchDeploymentRequest request)
    
    
    public ListenableFuture<PatchDeployments.PatchDeployment> resumePatchDeployment(PatchDeployments.ResumePatchDeploymentRequest request)

Change state of patch deployment back to "ACTIVE". Patch deployment in active state continues to generate patch jobs.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchDeployments.ResumePatchDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchDeployments.ResumePatchDeploymentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchDeployments.PatchDeployment)>` |   
  
### updateGuestPolicy(GuestPolicies.UpdateGuestPolicyRequest request)
    
    
    public ListenableFuture<GuestPolicies.GuestPolicy> updateGuestPolicy(GuestPolicies.UpdateGuestPolicyRequest request)

Update an OS Config guest policy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GuestPolicies.UpdateGuestPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.GuestPolicies.UpdateGuestPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[GuestPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.GuestPolicies.GuestPolicy)>` |   
  
### updatePatchDeployment(PatchDeployments.UpdatePatchDeploymentRequest request)
    
    
    public ListenableFuture<PatchDeployments.PatchDeployment> updatePatchDeployment(PatchDeployments.UpdatePatchDeploymentRequest request)

Update an OS Config patch deployment.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PatchDeployments.UpdatePatchDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchDeployments.UpdatePatchDeploymentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[PatchDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-os-config/latest/com.google.cloud.osconfig.v1beta.PatchDeployments.PatchDeployment)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
