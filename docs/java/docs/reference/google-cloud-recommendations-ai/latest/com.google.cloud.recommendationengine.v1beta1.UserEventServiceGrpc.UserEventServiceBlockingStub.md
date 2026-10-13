---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.UserEventServiceGrpc.UserEventServiceBlockingStub
title: Class UserEventServiceGrpc.UserEventServiceBlockingStub (0.106.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:51:02.176387+00:00
---

# Class UserEventServiceGrpc.UserEventServiceBlockingStub (0.106.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.UserEventServiceGrpc.UserEventServiceBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class UserEventServiceGrpc.UserEventServiceBlockingStub (0.106.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.106.0 (latest)  0.102.0  0.101.0  0.100.0  0.98.0  0.95.0  0.94.0  0.92.0  0.90.0  0.89.0  0.87.0  0.85.0  0.83.0  0.82.0  0.81.0  0.80.0  0.79.0  0.77.0  0.75.0  0.74.0  0.71.0  0.70.0  0.69.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.4  0.8.10 
    
    
    public static final class UserEventServiceGrpc.UserEventServiceBlockingStub extends AbstractBlockingStub<UserEventServiceGrpc.UserEventServiceBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service UserEventService.

Service for ingesting end user actions on the customer website.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > UserEventServiceGrpc.UserEventServiceBlockingStub

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
    
    
    protected UserEventServiceGrpc.UserEventServiceBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[UserEventServiceGrpc.UserEventServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.UserEventServiceGrpc.UserEventServiceBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### collectUserEvent(CollectUserEventRequest request)
    
    
    public HttpBody collectUserEvent(CollectUserEventRequest request)

Writes a single user event from the browser. This uses a GET request to due to browser restriction of POST-ing to a 3rd party domain. This method is used only by the Recommendations AI JavaScript pixel. Users should not call this method directly.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CollectUserEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.CollectUserEventRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.api.HttpBody` |   
  
### importUserEvents(ImportUserEventsRequest request)
    
    
    public Operation importUserEvents(ImportUserEventsRequest request)

Bulk import of User events. Request processing might be synchronous. Events that already exist are skipped. Use this method for backfilling historical user events. Operation.response is of type ImportResponse. Note that it is possible for a subset of the items to be successfully inserted. Operation.metadata is of type ImportMetadata.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportUserEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.ImportUserEventsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### listUserEvents(ListUserEventsRequest request)
    
    
    public ListUserEventsResponse listUserEvents(ListUserEventsRequest request)

Gets a list of user events within a time range, with potential filtering.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListUserEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.ListUserEventsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListUserEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.ListUserEventsResponse)` |   
  
### purgeUserEvents(PurgeUserEventsRequest request)
    
    
    public Operation purgeUserEvents(PurgeUserEventsRequest request)

Deletes permanently all user events specified by the filter provided. Depending on the number of events specified by the filter, this operation could take hours or days to complete. To test a filter, use the list command first.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PurgeUserEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.PurgeUserEventsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### writeUserEvent(WriteUserEventRequest request)
    
    
    public UserEvent writeUserEvent(WriteUserEventRequest request)

Writes a single user event.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[WriteUserEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.WriteUserEventRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UserEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-recommendations-ai/latest/com.google.cloud.recommendationengine.v1beta1.UserEvent)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
