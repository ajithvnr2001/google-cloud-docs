---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1beta.ConversionSourcesServiceGrpc.ConversionSourcesServiceBlockingV2Stub
title: Class ConversionSourcesServiceGrpc.ConversionSourcesServiceBlockingV2Stub (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:15.531213+00:00
---

# Class ConversionSourcesServiceGrpc.ConversionSourcesServiceBlockingV2Stub (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1beta.ConversionSourcesServiceGrpc.ConversionSourcesServiceBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ConversionSourcesServiceGrpc.ConversionSourcesServiceBlockingV2Stub (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class ConversionSourcesServiceGrpc.ConversionSourcesServiceBlockingV2Stub extends AbstractBlockingStub<ConversionSourcesServiceGrpc.ConversionSourcesServiceBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service ConversionSourcesService.

Service for managing conversion sources for a merchant account.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > ConversionSourcesServiceGrpc.ConversionSourcesServiceBlockingV2Stub

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
    
    
    protected ConversionSourcesServiceGrpc.ConversionSourcesServiceBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConversionSourcesServiceGrpc.ConversionSourcesServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1beta.ConversionSourcesServiceGrpc.ConversionSourcesServiceBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createConversionSource(CreateConversionSourceRequest request)
    
    
    public ConversionSource createConversionSource(CreateConversionSourceRequest request)

Creates a new conversion source.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateConversionSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1beta.CreateConversionSourceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConversionSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1beta.ConversionSource)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteConversionSource(DeleteConversionSourceRequest request)
    
    
    public Empty deleteConversionSource(DeleteConversionSourceRequest request)

Archives an existing conversion source. If the conversion source is a Merchant Center Destination, it will be recoverable for 30 days. If the conversion source is a Google Analytics Link, it will be deleted immediately and can be restored by creating a new one.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteConversionSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1beta.DeleteConversionSourceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getConversionSource(GetConversionSourceRequest request)
    
    
    public ConversionSource getConversionSource(GetConversionSourceRequest request)

Fetches a conversion source.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetConversionSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1beta.GetConversionSourceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConversionSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1beta.ConversionSource)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listConversionSources(ListConversionSourcesRequest request)
    
    
    public ListConversionSourcesResponse listConversionSources(ListConversionSourcesRequest request)

Retrieves the list of conversion sources the caller has access to.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListConversionSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1beta.ListConversionSourcesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListConversionSourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1beta.ListConversionSourcesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### undeleteConversionSource(UndeleteConversionSourceRequest request)
    
    
    public ConversionSource undeleteConversionSource(UndeleteConversionSourceRequest request)

Re-enables an archived conversion source. Only Available for Merchant Center Destination conversion sources.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UndeleteConversionSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1beta.UndeleteConversionSourceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConversionSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1beta.ConversionSource)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateConversionSource(UpdateConversionSourceRequest request)
    
    
    public ConversionSource updateConversionSource(UpdateConversionSourceRequest request)

Updates information of an existing conversion source. Available only for Merchant Center Destination conversion sources.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateConversionSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1beta.UpdateConversionSourceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConversionSource](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-conversions/latest/com.google.shopping.merchant.conversions.v1beta.ConversionSource)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
