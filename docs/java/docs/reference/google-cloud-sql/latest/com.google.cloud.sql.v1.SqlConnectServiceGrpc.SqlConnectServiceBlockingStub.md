---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlConnectServiceGrpc.SqlConnectServiceBlockingStub
title: Class SqlConnectServiceGrpc.SqlConnectServiceBlockingStub (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:53.480351+00:00
---

# Class SqlConnectServiceGrpc.SqlConnectServiceBlockingStub (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlConnectServiceGrpc.SqlConnectServiceBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SqlConnectServiceGrpc.SqlConnectServiceBlockingStub (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public static final class SqlConnectServiceGrpc.SqlConnectServiceBlockingStub extends AbstractBlockingStub<SqlConnectServiceGrpc.SqlConnectServiceBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service SqlConnectService.

Cloud SQL connect service.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > SqlConnectServiceGrpc.SqlConnectServiceBlockingStub

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
    
    
    protected SqlConnectServiceGrpc.SqlConnectServiceBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[SqlConnectServiceGrpc.SqlConnectServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.SqlConnectServiceGrpc.SqlConnectServiceBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### generateEphemeralCert(GenerateEphemeralCertRequest request)
    
    
    public GenerateEphemeralCertResponse generateEphemeralCert(GenerateEphemeralCertRequest request)

Generates a short-lived X509 certificate containing the provided public key and signed by a private key specific to the target instance. Users may use the certificate to authenticate as themselves when connecting to the database.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateEphemeralCertRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.GenerateEphemeralCertRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GenerateEphemeralCertResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.GenerateEphemeralCertResponse)` |   
  
### getConnectSettings(GetConnectSettingsRequest request)
    
    
    public ConnectSettings getConnectSettings(GetConnectSettingsRequest request)

Retrieves connect settings about a Cloud SQL instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetConnectSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.GetConnectSettingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ConnectSettings)` |   
  
### resolveConnectSettings(ResolveConnectSettingsRequest request)
    
    
    public ConnectSettings resolveConnectSettings(ResolveConnectSettingsRequest request)

Retrieves connect settings about a Cloud SQL instance using the instance DNS name.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResolveConnectSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ResolveConnectSettingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ConnectSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.ConnectSettings)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
