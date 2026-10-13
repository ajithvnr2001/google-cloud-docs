---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.SecurityProfileGroupServiceGrpc.SecurityProfileGroupServiceBlockingV2Stub
title: Class SecurityProfileGroupServiceGrpc.SecurityProfileGroupServiceBlockingV2Stub (0.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:11:05.592108+00:00
---

# Class SecurityProfileGroupServiceGrpc.SecurityProfileGroupServiceBlockingV2Stub (0.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.SecurityProfileGroupServiceGrpc.SecurityProfileGroupServiceBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SecurityProfileGroupServiceGrpc.SecurityProfileGroupServiceBlockingV2Stub (0.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.102.0 (latest)  0.98.0  0.97.0  0.96.0  0.94.0  0.91.0  0.90.0  0.88.0  0.86.0  0.85.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.67.0  0.66.0  0.65.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.4  0.5.1  0.4.4 
    
    
    public static final class SecurityProfileGroupServiceGrpc.SecurityProfileGroupServiceBlockingV2Stub extends AbstractBlockingStub<SecurityProfileGroupServiceGrpc.SecurityProfileGroupServiceBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service SecurityProfileGroupService.

SecurityProfileGroup is a resource that defines an action for specific threat signatures or severity levels.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > SecurityProfileGroupServiceGrpc.SecurityProfileGroupServiceBlockingV2Stub

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
    
    
    protected SecurityProfileGroupServiceGrpc.SecurityProfileGroupServiceBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityProfileGroupServiceGrpc.SecurityProfileGroupServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.SecurityProfileGroupServiceGrpc.SecurityProfileGroupServiceBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createSecurityProfile(CreateSecurityProfileRequest request)
    
    
    public Operation createSecurityProfile(CreateSecurityProfileRequest request)

Creates a new SecurityProfile in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSecurityProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateSecurityProfileRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createSecurityProfileGroup(CreateSecurityProfileGroupRequest request)
    
    
    public Operation createSecurityProfileGroup(CreateSecurityProfileGroupRequest request)

Creates a new SecurityProfileGroup in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSecurityProfileGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.CreateSecurityProfileGroupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteSecurityProfile(DeleteSecurityProfileRequest request)
    
    
    public Operation deleteSecurityProfile(DeleteSecurityProfileRequest request)

Deletes a single SecurityProfile.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSecurityProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteSecurityProfileRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteSecurityProfileGroup(DeleteSecurityProfileGroupRequest request)
    
    
    public Operation deleteSecurityProfileGroup(DeleteSecurityProfileGroupRequest request)

Deletes a single SecurityProfileGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSecurityProfileGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.DeleteSecurityProfileGroupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getSecurityProfile(GetSecurityProfileRequest request)
    
    
    public SecurityProfile getSecurityProfile(GetSecurityProfileRequest request)

Gets details of a single SecurityProfile.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSecurityProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetSecurityProfileRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityProfile](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.SecurityProfile)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getSecurityProfileGroup(GetSecurityProfileGroupRequest request)
    
    
    public SecurityProfileGroup getSecurityProfileGroup(GetSecurityProfileGroupRequest request)

Gets details of a single SecurityProfileGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSecurityProfileGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.GetSecurityProfileGroupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityProfileGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.SecurityProfileGroup)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listSecurityProfileGroups(ListSecurityProfileGroupsRequest request)
    
    
    public ListSecurityProfileGroupsResponse listSecurityProfileGroups(ListSecurityProfileGroupsRequest request)

Lists SecurityProfileGroups in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSecurityProfileGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListSecurityProfileGroupsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListSecurityProfileGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListSecurityProfileGroupsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listSecurityProfiles(ListSecurityProfilesRequest request)
    
    
    public ListSecurityProfilesResponse listSecurityProfiles(ListSecurityProfilesRequest request)

Lists SecurityProfiles in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSecurityProfilesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListSecurityProfilesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListSecurityProfilesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.ListSecurityProfilesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateSecurityProfile(UpdateSecurityProfileRequest request)
    
    
    public Operation updateSecurityProfile(UpdateSecurityProfileRequest request)

Updates the parameters of a single SecurityProfile.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSecurityProfileRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateSecurityProfileRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateSecurityProfileGroup(UpdateSecurityProfileGroupRequest request)
    
    
    public Operation updateSecurityProfileGroup(UpdateSecurityProfileGroupRequest request)

Updates the parameters of a single SecurityProfileGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSecurityProfileGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-network-security/latest/com.google.cloud.networksecurity.v1.UpdateSecurityProfileGroupRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
