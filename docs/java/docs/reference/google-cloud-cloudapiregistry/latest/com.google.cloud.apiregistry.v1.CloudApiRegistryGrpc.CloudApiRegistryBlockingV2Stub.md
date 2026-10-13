---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistryGrpc.CloudApiRegistryBlockingV2Stub
title: Class CloudApiRegistryGrpc.CloudApiRegistryBlockingV2Stub (0.18.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:21.029141+00:00
---

# Class CloudApiRegistryGrpc.CloudApiRegistryBlockingV2Stub (0.18.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistryGrpc.CloudApiRegistryBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CloudApiRegistryGrpc.CloudApiRegistryBlockingV2Stub (0.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.18.0 (latest)  0.14.0  0.13.0  0.12.0  0.10.0  0.7.0  0.6.0  0.4.0  0.2.0  0.1.0 
    
    
    public static final class CloudApiRegistryGrpc.CloudApiRegistryBlockingV2Stub extends AbstractBlockingStub<CloudApiRegistryGrpc.CloudApiRegistryBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service CloudApiRegistry.

The Cloud API Registry service provides a central registry for managing API Data.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > CloudApiRegistryGrpc.CloudApiRegistryBlockingV2Stub

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
    
    
    protected CloudApiRegistryGrpc.CloudApiRegistryBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudApiRegistryGrpc.CloudApiRegistryBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.CloudApiRegistryGrpc.CloudApiRegistryBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### getMcpServer(GetMcpServerRequest request)
    
    
    public McpServer getMcpServer(GetMcpServerRequest request)

Gets a single McpServer.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMcpServerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.GetMcpServerRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[McpServer](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.McpServer)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getMcpTool(GetMcpToolRequest request)
    
    
    public McpTool getMcpTool(GetMcpToolRequest request)

Gets a single McpTool.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMcpToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.GetMcpToolRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[McpTool](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.McpTool)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listMcpServers(ListMcpServersRequest request)
    
    
    public ListMcpServersResponse listMcpServers(ListMcpServersRequest request)

Lists McpServers in a given Project.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMcpServersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.ListMcpServersRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListMcpServersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.ListMcpServersResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listMcpTools(ListMcpToolsRequest request)
    
    
    public ListMcpToolsResponse listMcpTools(ListMcpToolsRequest request)

Lists McpTools in a given McpServer.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMcpToolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.ListMcpToolsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListMcpToolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudapiregistry/latest/com.google.cloud.apiregistry.v1.ListMcpToolsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
