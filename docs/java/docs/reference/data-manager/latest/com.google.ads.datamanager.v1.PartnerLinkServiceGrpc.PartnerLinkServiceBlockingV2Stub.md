---
url: https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.PartnerLinkServiceGrpc.PartnerLinkServiceBlockingV2Stub
title: Class PartnerLinkServiceGrpc.PartnerLinkServiceBlockingV2Stub (0.20.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:28:10.989835+00:00
---

# Class PartnerLinkServiceGrpc.PartnerLinkServiceBlockingV2Stub (0.20.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.PartnerLinkServiceGrpc.PartnerLinkServiceBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PartnerLinkServiceGrpc.PartnerLinkServiceBlockingV2Stub (0.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.0 (latest)  0.16.0  0.15.0  0.14.0  0.12.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class PartnerLinkServiceGrpc.PartnerLinkServiceBlockingV2Stub extends AbstractBlockingStub<PartnerLinkServiceGrpc.PartnerLinkServiceBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service PartnerLinkService.

Service for managing partner links.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > PartnerLinkServiceGrpc.PartnerLinkServiceBlockingV2Stub

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
    
    
    protected PartnerLinkServiceGrpc.PartnerLinkServiceBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[PartnerLinkServiceGrpc.PartnerLinkServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.PartnerLinkServiceGrpc.PartnerLinkServiceBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createPartnerLink(CreatePartnerLinkRequest request)
    
    
    public PartnerLink createPartnerLink(CreatePartnerLinkRequest request)

Creates a partner link for the given account. Authorization Headers: This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`



**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePartnerLinkRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.CreatePartnerLinkRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PartnerLink](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.PartnerLink)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deletePartnerLink(DeletePartnerLinkRequest request)
    
    
    public Empty deletePartnerLink(DeletePartnerLinkRequest request)

Deletes a partner link for the given account. Authorization Headers: This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`



**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePartnerLinkRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.DeletePartnerLinkRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### searchPartnerLinks(SearchPartnerLinksRequest request)
    
    
    public SearchPartnerLinksResponse searchPartnerLinks(SearchPartnerLinksRequest request)

Searches for all partner links to and from a given account. Authorization Headers: This method supports the following optional headers to define how the API authorizes access for the request:

  * `login-account`: (Optional) The resource name of the account where the Google Account of the credentials is a user. If not set, defaults to the account of the request. Format: `accountTypes/{loginAccountType}/accounts/{loginAccountId}`



**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchPartnerLinksRequest](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.SearchPartnerLinksRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SearchPartnerLinksResponse](https://docs.cloud.google.com/java/docs/reference/data-manager/latest/com.google.ads.datamanager.v1.SearchPartnerLinksResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
