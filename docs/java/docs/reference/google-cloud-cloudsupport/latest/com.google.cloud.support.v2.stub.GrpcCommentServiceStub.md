---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.stub.GrpcCommentServiceStub
title: Class GrpcCommentServiceStub (0.83.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:51:58.306904+00:00
---

# Class GrpcCommentServiceStub (0.83.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.stub.GrpcCommentServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GrpcCommentServiceStub (0.83.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.83.0 (latest)  0.79.0  0.78.0  0.77.0  0.75.0  0.72.0  0.71.0  0.69.0  0.67.0  0.66.0  0.65.0  0.64.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.54.0  0.52.0  0.51.0  0.48.0  0.47.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public class GrpcCommentServiceStub extends CommentServiceStub

gRPC stub implementation for the CommentService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [CommentServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.stub.CommentServiceStub) > GrpcCommentServiceStub

## Inherited Members

[CommentServiceStub.close()](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.stub.CommentServiceStub#com_google_cloud_support_v2_stub_CommentServiceStub_close__)

[CommentServiceStub.createCommentCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.stub.CommentServiceStub#com_google_cloud_support_v2_stub_CommentServiceStub_createCommentCallable__)

[CommentServiceStub.getCommentCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.stub.CommentServiceStub#com_google_cloud_support_v2_stub_CommentServiceStub_getCommentCallable__)

[CommentServiceStub.listCommentsCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.stub.CommentServiceStub#com_google_cloud_support_v2_stub_CommentServiceStub_listCommentsCallable__)

[CommentServiceStub.listCommentsPagedCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.stub.CommentServiceStub#com_google_cloud_support_v2_stub_CommentServiceStub_listCommentsPagedCallable__)

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

## Static Methods 

### create(ClientContext clientContext)
    
    
    public static final GrpcCommentServiceStub create(ClientContext clientContext)

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GrpcCommentServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.stub.GrpcCommentServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ClientContext clientContext, GrpcStubCallableFactory callableFactory)
    
    
    public static final GrpcCommentServiceStub create(ClientContext clientContext, GrpcStubCallableFactory callableFactory)

**Parameters**  
---  
**Name** | **Description**  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
`callableFactory` | `[GrpcStubCallableFactory](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.GrpcStubCallableFactory.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GrpcCommentServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.stub.GrpcCommentServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(CommentServiceStubSettings settings)
    
    
    public static final GrpcCommentServiceStub create(CommentServiceStubSettings settings)

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[CommentServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.stub.CommentServiceStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GrpcCommentServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.stub.GrpcCommentServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
## Constructors 

### GrpcCommentServiceStub(CommentServiceStubSettings settings, ClientContext clientContext)
    
    
    protected GrpcCommentServiceStub(CommentServiceStubSettings settings, ClientContext clientContext)

Constructs an instance of GrpcCommentServiceStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[CommentServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.stub.CommentServiceStubSettings)`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
  
### GrpcCommentServiceStub(CommentServiceStubSettings settings, ClientContext clientContext, GrpcStubCallableFactory callableFactory)
    
    
    protected GrpcCommentServiceStub(CommentServiceStubSettings settings, ClientContext clientContext, GrpcStubCallableFactory callableFactory)

Constructs an instance of GrpcCommentServiceStub, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameters**  
---  
**Name** | **Description**  
`settings` | `[CommentServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.stub.CommentServiceStubSettings)`  
  
`clientContext` | `[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.html)`  
  
`callableFactory` | `[GrpcStubCallableFactory](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.GrpcStubCallableFactory.html)`  
  
  
## Methods 

### awaitTermination(long duration, TimeUnit unit)
    
    
    public boolean awaitTermination(long duration, TimeUnit unit)

**Parameters**  
---  
**Name** | **Description**  
`duration` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
  
### close()
    
    
    public final void close()

**Overrides**

[CommentServiceStub.close()](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.stub.CommentServiceStub#com_google_cloud_support_v2_stub_CommentServiceStub_close__)

### createCommentCallable()
    
    
    public UnaryCallable<CreateCommentRequest,Comment> createCommentCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCommentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.CreateCommentRequest),[Comment](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.Comment)>` |   
**Overrides**

[CommentServiceStub.createCommentCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.stub.CommentServiceStub#com_google_cloud_support_v2_stub_CommentServiceStub_createCommentCallable__)

### getCommentCallable()
    
    
    public UnaryCallable<GetCommentRequest,Comment> getCommentCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCommentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.GetCommentRequest),[Comment](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.Comment)>` |   
**Overrides**

[CommentServiceStub.getCommentCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.stub.CommentServiceStub#com_google_cloud_support_v2_stub_CommentServiceStub_getCommentCallable__)

### getOperationsStub()
    
    
    public GrpcOperationsStub getOperationsStub()

**Returns**  
---  
**Type** | **Description**  
`[GrpcOperationsStub](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.stub.GrpcOperationsStub.html)` |   
  
### isShutdown()
    
    
    public boolean isShutdown()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTerminated()
    
    
    public boolean isTerminated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### listCommentsCallable()
    
    
    public UnaryCallable<ListCommentsRequest,ListCommentsResponse> listCommentsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCommentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.ListCommentsRequest),[ListCommentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.ListCommentsResponse)>` |   
**Overrides**

[CommentServiceStub.listCommentsCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.stub.CommentServiceStub#com_google_cloud_support_v2_stub_CommentServiceStub_listCommentsCallable__)

### listCommentsPagedCallable()
    
    
    public UnaryCallable<ListCommentsRequest,CommentServiceClient.ListCommentsPagedResponse> listCommentsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCommentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.ListCommentsRequest),[ListCommentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.CommentServiceClient.ListCommentsPagedResponse)>` |   
**Overrides**

[CommentServiceStub.listCommentsPagedCallable()](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2.stub.CommentServiceStub#com_google_cloud_support_v2_stub_CommentServiceStub_listCommentsPagedCallable__)

### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
