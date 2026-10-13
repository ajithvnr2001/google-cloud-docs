---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ConfigDeliveryGrpc.ConfigDeliveryBlockingStub
title: Class ConfigDeliveryGrpc.ConfigDeliveryBlockingStub (0.33.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:41.062165+00:00
---

# Class ConfigDeliveryGrpc.ConfigDeliveryBlockingStub (0.33.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ConfigDeliveryGrpc.ConfigDeliveryBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ConfigDeliveryGrpc.ConfigDeliveryBlockingStub (0.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.33.0 (latest)  0.29.0  0.28.0  0.27.0  0.25.0  0.22.0  0.21.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.4.0  0.2.0  0.1.0 
    
    
    public static final class ConfigDeliveryGrpc.ConfigDeliveryBlockingStub extends AbstractBlockingStub<ConfigDeliveryGrpc.ConfigDeliveryBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service ConfigDelivery.

ConfigDelivery service manages the deployment of kubernetes configuration to a fleet of kubernetes clusters.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > ConfigDeliveryGrpc.ConfigDeliveryBlockingStub

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

### abortRollout(AbortRolloutRequest request)
    
    
    public Operation abortRollout(AbortRolloutRequest request)

Abort a Rollout.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AbortRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.AbortRolloutRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected ConfigDeliveryGrpc.ConfigDeliveryBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConfigDeliveryGrpc.ConfigDeliveryBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ConfigDeliveryGrpc.ConfigDeliveryBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createFleetPackage(CreateFleetPackageRequest request)
    
    
    public Operation createFleetPackage(CreateFleetPackageRequest request)

Creates a new FleetPackage in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateFleetPackageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.CreateFleetPackageRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createRelease(CreateReleaseRequest request)
    
    
    public Operation createRelease(CreateReleaseRequest request)

Creates a new Release in a given project, location and resource bundle.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateReleaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.CreateReleaseRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createResourceBundle(CreateResourceBundleRequest request)
    
    
    public Operation createResourceBundle(CreateResourceBundleRequest request)

Creates a new ResourceBundle in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateResourceBundleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.CreateResourceBundleRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createVariant(CreateVariantRequest request)
    
    
    public Operation createVariant(CreateVariantRequest request)

Creates a new Variant in a given project, location, resource bundle, and release.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateVariantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.CreateVariantRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteFleetPackage(DeleteFleetPackageRequest request)
    
    
    public Operation deleteFleetPackage(DeleteFleetPackageRequest request)

Deletes a single FleetPackage.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteFleetPackageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.DeleteFleetPackageRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteRelease(DeleteReleaseRequest request)
    
    
    public Operation deleteRelease(DeleteReleaseRequest request)

Deletes a single Release.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteReleaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.DeleteReleaseRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteResourceBundle(DeleteResourceBundleRequest request)
    
    
    public Operation deleteResourceBundle(DeleteResourceBundleRequest request)

Deletes a single ResourceBundle.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteResourceBundleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.DeleteResourceBundleRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteVariant(DeleteVariantRequest request)
    
    
    public Operation deleteVariant(DeleteVariantRequest request)

Deletes a single Variant.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteVariantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.DeleteVariantRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### getFleetPackage(GetFleetPackageRequest request)
    
    
    public FleetPackage getFleetPackage(GetFleetPackageRequest request)

Gets details of a single FleetPackage.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetFleetPackageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.GetFleetPackageRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[FleetPackage](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.FleetPackage)` |   
  
### getRelease(GetReleaseRequest request)
    
    
    public Release getRelease(GetReleaseRequest request)

Gets details of a single Release.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetReleaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.GetReleaseRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Release](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.Release)` |   
  
### getResourceBundle(GetResourceBundleRequest request)
    
    
    public ResourceBundle getResourceBundle(GetResourceBundleRequest request)

Gets details of a single ResourceBundle.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetResourceBundleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.GetResourceBundleRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ResourceBundle](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ResourceBundle)` |   
  
### getRollout(GetRolloutRequest request)
    
    
    public Rollout getRollout(GetRolloutRequest request)

Gets details of a single Rollout.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.GetRolloutRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Rollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.Rollout)` |   
  
### getVariant(GetVariantRequest request)
    
    
    public Variant getVariant(GetVariantRequest request)

Gets details of a single Variant.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetVariantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.GetVariantRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Variant](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.Variant)` |   
  
### listFleetPackages(ListFleetPackagesRequest request)
    
    
    public ListFleetPackagesResponse listFleetPackages(ListFleetPackagesRequest request)

Lists FleetPackages in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFleetPackagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ListFleetPackagesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListFleetPackagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ListFleetPackagesResponse)` |   
  
### listReleases(ListReleasesRequest request)
    
    
    public ListReleasesResponse listReleases(ListReleasesRequest request)

Lists Releases in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListReleasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ListReleasesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListReleasesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ListReleasesResponse)` |   
  
### listResourceBundles(ListResourceBundlesRequest request)
    
    
    public ListResourceBundlesResponse listResourceBundles(ListResourceBundlesRequest request)

Lists ResourceBundles in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListResourceBundlesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ListResourceBundlesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListResourceBundlesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ListResourceBundlesResponse)` |   
  
### listRollouts(ListRolloutsRequest request)
    
    
    public ListRolloutsResponse listRollouts(ListRolloutsRequest request)

Lists Rollouts in a given project, location, and Fleet Package.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListRolloutsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ListRolloutsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListRolloutsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ListRolloutsResponse)` |   
  
### listVariants(ListVariantsRequest request)
    
    
    public ListVariantsResponse listVariants(ListVariantsRequest request)

Lists Variants in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListVariantsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ListVariantsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListVariantsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ListVariantsResponse)` |   
  
### resumeRollout(ResumeRolloutRequest request)
    
    
    public Operation resumeRollout(ResumeRolloutRequest request)

Resume a Rollout.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResumeRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ResumeRolloutRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### suspendRollout(SuspendRolloutRequest request)
    
    
    public Operation suspendRollout(SuspendRolloutRequest request)

Suspend a Rollout.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SuspendRolloutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.SuspendRolloutRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateFleetPackage(UpdateFleetPackageRequest request)
    
    
    public Operation updateFleetPackage(UpdateFleetPackageRequest request)

Updates the parameters of a single FleetPackage.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateFleetPackageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.UpdateFleetPackageRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateRelease(UpdateReleaseRequest request)
    
    
    public Operation updateRelease(UpdateReleaseRequest request)

Updates the parameters of a single Release.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateReleaseRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.UpdateReleaseRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateResourceBundle(UpdateResourceBundleRequest request)
    
    
    public Operation updateResourceBundle(UpdateResourceBundleRequest request)

Updates the parameters of a single ResourceBundle.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateResourceBundleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.UpdateResourceBundleRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateVariant(UpdateVariantRequest request)
    
    
    public Operation updateVariant(UpdateVariantRequest request)

Updates the parameters of a single Variant.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateVariantRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.UpdateVariantRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
