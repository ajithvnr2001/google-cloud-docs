---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ConfigGrpc.ConfigBlockingV2Stub
title: Class ConfigGrpc.ConfigBlockingV2Stub (0.26.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:47:32.079670+00:00
---

# Class ConfigGrpc.ConfigBlockingV2Stub (0.26.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ConfigGrpc.ConfigBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ConfigGrpc.ConfigBlockingV2Stub (0.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.26.0 (latest)  0.22.0  0.21.0  0.20.0  0.18.0  0.15.0  0.14.0  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class ConfigGrpc.ConfigBlockingV2Stub extends AbstractBlockingStub<ConfigGrpc.ConfigBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service Config.

Config Service manages compliance frameworks, cloud controls, and their configurations.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > ConfigGrpc.ConfigBlockingV2Stub

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
    
    
    protected ConfigGrpc.ConfigBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConfigGrpc.ConfigBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ConfigGrpc.ConfigBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createCloudControl(CreateCloudControlRequest request)
    
    
    public CloudControl createCloudControl(CreateCloudControlRequest request)

Creates a custom cloud control in a given parent resource. You can't create built-in cloud controls because those are managed by Google.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCloudControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CreateCloudControlRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudControl](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControl)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createFramework(CreateFrameworkRequest request)
    
    
    public Framework createFramework(CreateFrameworkRequest request)

Creates a custom framework in a given parent resource. You can't create built-in frameworks because those are managed by Google.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateFrameworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CreateFrameworkRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Framework](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.Framework)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteCloudControl(DeleteCloudControlRequest request)
    
    
    public Empty deleteCloudControl(DeleteCloudControlRequest request)

Deletes a custom cloud control, including all its major and minor revisions. Consider the following:

  * You can't delete built-in cloud controls. You can only delete cloud controls with type `CUSTOM`.
  * You can't delete cloud controls if any of the versions are referenced by a framework.
  * You can't restore a deleted cloud control. This action is permanent.



**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCloudControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeleteCloudControlRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteFramework(DeleteFrameworkRequest request)
    
    
    public Empty deleteFramework(DeleteFrameworkRequest request)

Deletes a custom framework, including all its major and minor revisions. Consider the following:

  * You can't delete built-in frameworks. You can only delete frameworks with type `CUSTOM`.
  * You can't delete frameworks that are deployed to a resource.
  * You can't restore a deleted framework. This action is permanent.



**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteFrameworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.DeleteFrameworkRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getCloudControl(GetCloudControlRequest request)
    
    
    public CloudControl getCloudControl(GetCloudControlRequest request)

Gets details about a cloud control. This method retrieves the latest major version of a cloud control that you identify by name. By default, the latest major version of the cloud control is returned. To retrieve a specific major version, include `major_revision_id` in the request.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCloudControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.GetCloudControlRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudControl](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControl)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getFramework(GetFrameworkRequest request)
    
    
    public Framework getFramework(GetFrameworkRequest request)

Gets details about a framework. This method retrieves the latest major version of the framework. To retrieve a specific major version, include `major_revision_id` in the request.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetFrameworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.GetFrameworkRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Framework](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.Framework)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listCloudControls(ListCloudControlsRequest request)
    
    
    public ListCloudControlsResponse listCloudControls(ListCloudControlsRequest request)

Lists the cloud controls (both built-in and custom) that are available in a given parent resource. The latest major version of each cloud control is returned. This method supports pagination.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCloudControlsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListCloudControlsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListCloudControlsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListCloudControlsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listFrameworks(ListFrameworksRequest request)
    
    
    public ListFrameworksResponse listFrameworks(ListFrameworksRequest request)

Lists the frameworks (both built-in and custom) that are available within the parent resource. The latest major version of each framework is returned. This method supports pagination.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFrameworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFrameworksRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListFrameworksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ListFrameworksResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateCloudControl(UpdateCloudControlRequest request)
    
    
    public CloudControl updateCloudControl(UpdateCloudControlRequest request)

Updates a custom cloud control. This method allows for partial updates of a cloud control. Use the `update_mask` to specify which fields to update. Consider the following:

  * If you provide an `update_mask`, only the fields that are specified in the mask are updated.
  * If you don't provide an `update_mask`, all the fields that are present in the request's `cloud_control` body are used to overwrite the existing resource. You can only update cloud controls with the `CUSTOM` type. A successful update creates a new version of the cloud control.



**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateCloudControlRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.UpdateCloudControlRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudControl](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CloudControl)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateFramework(UpdateFrameworkRequest request)
    
    
    public Framework updateFramework(UpdateFrameworkRequest request)

Updates a custom framework. This method allows for partial updates of a framework. Use the `update_mask` to specify which fields to update. Consider the following:

  * If you provide an `update_mask`, only the fields that are specified in the mask are updated.
  * If you don't provide an `update_mask`, all the fields that are present in the request's `framework` body are used to overwrite the existing resource. You can only update frameworks with the `CUSTOM` type. A successful update creates a new version of the framework.



**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateFrameworkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.UpdateFrameworkRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Framework](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.Framework)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
