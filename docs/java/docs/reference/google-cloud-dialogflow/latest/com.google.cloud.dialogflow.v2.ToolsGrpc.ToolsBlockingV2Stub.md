---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ToolsGrpc.ToolsBlockingV2Stub
title: Class ToolsGrpc.ToolsBlockingV2Stub (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:47.922201+00:00
---

# Class ToolsGrpc.ToolsBlockingV2Stub (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ToolsGrpc.ToolsBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ToolsGrpc.ToolsBlockingV2Stub (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 
    
    
    public static final class ToolsGrpc.ToolsBlockingV2Stub extends AbstractBlockingStub<ToolsGrpc.ToolsBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service Tools.

Tool Service for LLM powered Agent Assist. Tools can be used to interact with remote APIs (e.g. fetching orders) to retrieve additional information as input to LLM.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > ToolsGrpc.ToolsBlockingV2Stub

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
    
    
    protected ToolsGrpc.ToolsBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[ToolsGrpc.ToolsBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ToolsGrpc.ToolsBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createTool(CreateToolRequest request)
    
    
    public Tool createTool(CreateToolRequest request)

Creates a tool.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.CreateToolRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Tool)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteTool(DeleteToolRequest request)
    
    
    public Empty deleteTool(DeleteToolRequest request)

Deletes a tool.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.DeleteToolRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getTool(GetToolRequest request)
    
    
    public Tool getTool(GetToolRequest request)

Retrieves a tool.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.GetToolRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Tool)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listTools(ListToolsRequest request)
    
    
    public ListToolsResponse listTools(ListToolsRequest request)

Lists tools.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListToolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListToolsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListToolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ListToolsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateTool(UpdateToolRequest request)
    
    
    public Tool updateTool(UpdateToolRequest request)

Updates a tool.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateToolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.UpdateToolRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Tool](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Tool)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
