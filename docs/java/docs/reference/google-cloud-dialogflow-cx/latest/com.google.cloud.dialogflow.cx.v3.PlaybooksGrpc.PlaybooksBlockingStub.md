---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybooksGrpc.PlaybooksBlockingStub
title: Class PlaybooksGrpc.PlaybooksBlockingStub (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:34:51.326434+00:00
---

# Class PlaybooksGrpc.PlaybooksBlockingStub (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybooksGrpc.PlaybooksBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PlaybooksGrpc.PlaybooksBlockingStub (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.7  0.13.1  0.12.1  0.11.5 
    
    
    public static final class PlaybooksGrpc.PlaybooksBlockingStub extends AbstractBlockingStub<PlaybooksGrpc.PlaybooksBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service Playbooks.

Service for managing Playbooks.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > PlaybooksGrpc.PlaybooksBlockingStub

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
    
    
    protected PlaybooksGrpc.PlaybooksBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[PlaybooksGrpc.PlaybooksBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybooksGrpc.PlaybooksBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createPlaybook(CreatePlaybookRequest request)
    
    
    public Playbook createPlaybook(CreatePlaybookRequest request)

Creates a playbook in a specified agent.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePlaybookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreatePlaybookRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook)` |   
  
### createPlaybookVersion(CreatePlaybookVersionRequest request)
    
    
    public PlaybookVersion createPlaybookVersion(CreatePlaybookVersionRequest request)

Creates a version for the specified Playbook.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePlaybookVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.CreatePlaybookVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PlaybookVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybookVersion)` |   
  
### deletePlaybook(DeletePlaybookRequest request)
    
    
    public Empty deletePlaybook(DeletePlaybookRequest request)

Deletes a specified playbook.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePlaybookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeletePlaybookRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
  
### deletePlaybookVersion(DeletePlaybookVersionRequest request)
    
    
    public Empty deletePlaybookVersion(DeletePlaybookVersionRequest request)

Deletes the specified version of the Playbook.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePlaybookVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DeletePlaybookVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
  
### exportPlaybook(ExportPlaybookRequest request)
    
    
    public Operation exportPlaybook(ExportPlaybookRequest request)

Exports the specified playbook to a binary file. Note that resources (e.g. examples, tools) that the playbook references will also be exported.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportPlaybookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ExportPlaybookRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### getPlaybook(GetPlaybookRequest request)
    
    
    public Playbook getPlaybook(GetPlaybookRequest request)

Retrieves the specified Playbook.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPlaybookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetPlaybookRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook)` |   
  
### getPlaybookVersion(GetPlaybookVersionRequest request)
    
    
    public PlaybookVersion getPlaybookVersion(GetPlaybookVersionRequest request)

Retrieves the specified version of the Playbook.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPlaybookVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.GetPlaybookVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PlaybookVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.PlaybookVersion)` |   
  
### importPlaybook(ImportPlaybookRequest request)
    
    
    public Operation importPlaybook(ImportPlaybookRequest request)

Imports the specified playbook to the specified agent from a binary file.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportPlaybookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ImportPlaybookRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### listPlaybookVersions(ListPlaybookVersionsRequest request)
    
    
    public ListPlaybookVersionsResponse listPlaybookVersions(ListPlaybookVersionsRequest request)

Lists versions for the specified Playbook.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPlaybookVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListPlaybookVersionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListPlaybookVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListPlaybookVersionsResponse)` |   
  
### listPlaybooks(ListPlaybooksRequest request)
    
    
    public ListPlaybooksResponse listPlaybooks(ListPlaybooksRequest request)

Returns a list of playbooks in the specified agent.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPlaybooksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListPlaybooksRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListPlaybooksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.ListPlaybooksResponse)` |   
  
### restorePlaybookVersion(RestorePlaybookVersionRequest request)
    
    
    public RestorePlaybookVersionResponse restorePlaybookVersion(RestorePlaybookVersionRequest request)

Retrieves the specified version of the Playbook and stores it as the current playbook draft, returning the playbook with resources updated.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RestorePlaybookVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RestorePlaybookVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RestorePlaybookVersionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.RestorePlaybookVersionResponse)` |   
  
### updatePlaybook(UpdatePlaybookRequest request)
    
    
    public Playbook updatePlaybook(UpdatePlaybookRequest request)

Updates the specified Playbook.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePlaybookRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.UpdatePlaybookRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Playbook](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.Playbook)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
