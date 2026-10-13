---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewServiceGrpc.OrgPolicyViolationsPreviewServiceBlockingV2Stub
title: Class OrgPolicyViolationsPreviewServiceGrpc.OrgPolicyViolationsPreviewServiceBlockingV2Stub (0.78.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:37.715124+00:00
---

# Class OrgPolicyViolationsPreviewServiceGrpc.OrgPolicyViolationsPreviewServiceBlockingV2Stub (0.78.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewServiceGrpc.OrgPolicyViolationsPreviewServiceBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class OrgPolicyViolationsPreviewServiceGrpc.OrgPolicyViolationsPreviewServiceBlockingV2Stub (0.78.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.78.0 (latest)  0.74.0  0.73.0  0.72.0  0.70.0  0.67.0  0.66.0  0.64.0  0.62.0  0.61.0  0.59.0  0.57.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.49.0  0.47.0  0.46.0  0.43.0  0.42.0  0.41.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class OrgPolicyViolationsPreviewServiceGrpc.OrgPolicyViolationsPreviewServiceBlockingV2Stub extends AbstractBlockingStub<OrgPolicyViolationsPreviewServiceGrpc.OrgPolicyViolationsPreviewServiceBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service OrgPolicyViolationsPreviewService.

Violations Preview API service for OrgPolicy. An OrgPolicyViolationsPreview is a preview of the violations that will exist as soon as a proposed OrgPolicy change is submitted. To create an OrgPolicyViolationsPreview, the API user specifies the changes they wish to make and requests the generation of a preview via [GenerateViolationsPreview][]. the OrgPolicy Simulator service then scans the API user's currently existing resources to determine these resources violate the newly set OrgPolicy.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > OrgPolicyViolationsPreviewServiceGrpc.OrgPolicyViolationsPreviewServiceBlockingV2Stub

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
    
    
    protected OrgPolicyViolationsPreviewServiceGrpc.OrgPolicyViolationsPreviewServiceBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrgPolicyViolationsPreviewServiceGrpc.OrgPolicyViolationsPreviewServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewServiceGrpc.OrgPolicyViolationsPreviewServiceBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createOrgPolicyViolationsPreview(CreateOrgPolicyViolationsPreviewRequest request)
    
    
    public Operation createOrgPolicyViolationsPreview(CreateOrgPolicyViolationsPreviewRequest request)

CreateOrgPolicyViolationsPreview creates an OrgPolicyViolationsPreview for the proposed changes in the provided [OrgPolicyViolationsPreview.OrgPolicyOverlay][]. The changes to OrgPolicy are specified by this `OrgPolicyOverlay`. The resources to scan are inferred from these specified changes.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateOrgPolicyViolationsPreviewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.CreateOrgPolicyViolationsPreviewRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getOrgPolicyViolationsPreview(GetOrgPolicyViolationsPreviewRequest request)
    
    
    public OrgPolicyViolationsPreview getOrgPolicyViolationsPreview(GetOrgPolicyViolationsPreviewRequest request)

GetOrgPolicyViolationsPreview gets the specified OrgPolicyViolationsPreview. Each OrgPolicyViolationsPreview is available for at least 7 days.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetOrgPolicyViolationsPreviewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.GetOrgPolicyViolationsPreviewRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrgPolicyViolationsPreview](https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.OrgPolicyViolationsPreview)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listOrgPolicyViolations(ListOrgPolicyViolationsRequest request)
    
    
    public ListOrgPolicyViolationsResponse listOrgPolicyViolations(ListOrgPolicyViolationsRequest request)

ListOrgPolicyViolations lists the [OrgPolicyViolations][] that are present in an OrgPolicyViolationsPreview.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOrgPolicyViolationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.ListOrgPolicyViolationsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListOrgPolicyViolationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.ListOrgPolicyViolationsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listOrgPolicyViolationsPreviews(ListOrgPolicyViolationsPreviewsRequest request)
    
    
    public ListOrgPolicyViolationsPreviewsResponse listOrgPolicyViolationsPreviews(ListOrgPolicyViolationsPreviewsRequest request)

ListOrgPolicyViolationsPreviews lists each OrgPolicyViolationsPreview in an organization. Each OrgPolicyViolationsPreview is available for at least 7 days.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOrgPolicyViolationsPreviewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.ListOrgPolicyViolationsPreviewsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListOrgPolicyViolationsPreviewsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-policysimulator/latest/com.google.cloud.policysimulator.v1.ListOrgPolicyViolationsPreviewsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
