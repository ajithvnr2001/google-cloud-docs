---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.SecurityCenterGrpc.SecurityCenterFutureStub
title: Class SecurityCenterGrpc.SecurityCenterFutureStub (2.107.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:52:47.224330+00:00
---

# Class SecurityCenterGrpc.SecurityCenterFutureStub (2.107.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.SecurityCenterGrpc.SecurityCenterFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SecurityCenterGrpc.SecurityCenterFutureStub (2.107.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.107.0 (latest)  2.103.0  2.102.0  2.101.0  2.99.0  2.96.0  2.95.0  2.93.0  2.91.0  2.90.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.72.0  2.71.0  2.70.0  2.68.0  2.67.0  2.66.0  2.65.0  2.64.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.10.0  2.9.0  2.8.0  2.7.1  2.6.0  2.5.6  2.3.2 
    
    
    public static final class SecurityCenterGrpc.SecurityCenterFutureStub extends AbstractFutureStub<SecurityCenterGrpc.SecurityCenterFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service SecurityCenter.

V1p1Beta1 APIs for Security Center service.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > SecurityCenterGrpc.SecurityCenterFutureStub

## Inherited Members

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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
    
    
    protected SecurityCenterGrpc.SecurityCenterFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterGrpc.SecurityCenterFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.SecurityCenterGrpc.SecurityCenterFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createFinding(CreateFindingRequest request)
    
    
    public ListenableFuture<Finding> createFinding(CreateFindingRequest request)

Creates a finding. The corresponding source must exist for finding creation to succeed.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateFindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.CreateFindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.Finding)>` |   
  
### createNotificationConfig(CreateNotificationConfigRequest request)
    
    
    public ListenableFuture<NotificationConfig> createNotificationConfig(CreateNotificationConfigRequest request)

Creates a notification config.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateNotificationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.CreateNotificationConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.NotificationConfig)>` |   
  
### createSource(CreateSourceRequest request)
    
    
    public ListenableFuture<Source> createSource(CreateSourceRequest request)

Creates a source.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.CreateSourceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.Source)>` |   
  
### deleteNotificationConfig(DeleteNotificationConfigRequest request)
    
    
    public ListenableFuture<Empty> deleteNotificationConfig(DeleteNotificationConfigRequest request)

Deletes a notification config.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNotificationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.DeleteNotificationConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public ListenableFuture<Policy> getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy on the specified Source.

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<com.google.iam.v1.Policy>` |   
  
### getNotificationConfig(GetNotificationConfigRequest request)
    
    
    public ListenableFuture<NotificationConfig> getNotificationConfig(GetNotificationConfigRequest request)

Gets a notification config.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNotificationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.GetNotificationConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.NotificationConfig)>` |   
  
### getOrganizationSettings(GetOrganizationSettingsRequest request)
    
    
    public ListenableFuture<OrganizationSettings> getOrganizationSettings(GetOrganizationSettingsRequest request)

Gets the settings for an organization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetOrganizationSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.GetOrganizationSettingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[OrganizationSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.OrganizationSettings)>` |   
  
### getSource(GetSourceRequest request)
    
    
    public ListenableFuture<Source> getSource(GetSourceRequest request)

Gets a source.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.GetSourceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.Source)>` |   
  
### groupAssets(GroupAssetsRequest request)
    
    
    public ListenableFuture<GroupAssetsResponse> groupAssets(GroupAssetsRequest request)

Filters an organization's assets and groups them by their specified properties.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GroupAssetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.GroupAssetsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[GroupAssetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.GroupAssetsResponse)>` |   
  
### groupFindings(GroupFindingsRequest request)
    
    
    public ListenableFuture<GroupFindingsResponse> groupFindings(GroupFindingsRequest request)

Filters an organization or source's findings and groups them by their specified properties. To group across all sources provide a `-` as the source id. Example: /v1/organizations/{organization_id}/sources/-/findings, /v1/folders/{folder_id}/sources/-/findings, /v1/projects/{project_id}/sources/-/findings

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GroupFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.GroupFindingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[GroupFindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.GroupFindingsResponse)>` |   
  
### listAssets(ListAssetsRequest request)
    
    
    public ListenableFuture<ListAssetsResponse> listAssets(ListAssetsRequest request)

Lists an organization's assets.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAssetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.ListAssetsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListAssetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.ListAssetsResponse)>` |   
  
### listFindings(ListFindingsRequest request)
    
    
    public ListenableFuture<ListFindingsResponse> listFindings(ListFindingsRequest request)

Lists an organization or source's findings. To list across all sources provide a `-` as the source id. Example: /v1p1beta1/organizations/{organization_id}/sources/-/findings

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListFindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.ListFindingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListFindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.ListFindingsResponse)>` |   
  
### listNotificationConfigs(ListNotificationConfigsRequest request)
    
    
    public ListenableFuture<ListNotificationConfigsResponse> listNotificationConfigs(ListNotificationConfigsRequest request)

Lists notification configs.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNotificationConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.ListNotificationConfigsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListNotificationConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.ListNotificationConfigsResponse)>` |   
  
### listSources(ListSourcesRequest request)
    
    
    public ListenableFuture<ListSourcesResponse> listSources(ListSourcesRequest request)

Lists all sources belonging to an organization.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.ListSourcesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListSourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.ListSourcesResponse)>` |   
  
### runAssetDiscovery(RunAssetDiscoveryRequest request)
    
    
    public ListenableFuture<Operation> runAssetDiscovery(RunAssetDiscoveryRequest request)

Runs asset discovery. The discovery is tracked with a long-running operation. This API can only be called with limited frequency for an organization. If it is called too frequently the caller will receive a TOO_MANY_REQUESTS error.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RunAssetDiscoveryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.RunAssetDiscoveryRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### setFindingState(SetFindingStateRequest request)
    
    
    public ListenableFuture<Finding> setFindingState(SetFindingStateRequest request)

Updates the state of a finding.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetFindingStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.SetFindingStateRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.Finding)>` |   
  
### setIamPolicy(SetIamPolicyRequest request)
    
    
    public ListenableFuture<Policy> setIamPolicy(SetIamPolicyRequest request)

Sets the access control policy on the specified Source.

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<com.google.iam.v1.Policy>` |   
  
### testIamPermissions(TestIamPermissionsRequest request)
    
    
    public ListenableFuture<TestIamPermissionsResponse> testIamPermissions(TestIamPermissionsRequest request)

Returns the permissions that a caller has on the specified source.

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.TestIamPermissionsRequest`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### updateFinding(UpdateFindingRequest request)
    
    
    public ListenableFuture<Finding> updateFinding(UpdateFindingRequest request)

Creates or updates a finding. The corresponding source must exist for a finding creation to succeed.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateFindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.UpdateFindingRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.Finding)>` |   
  
### updateNotificationConfig(UpdateNotificationConfigRequest request)
    
    
    public ListenableFuture<NotificationConfig> updateNotificationConfig(UpdateNotificationConfigRequest request)

Updates a notification config. The following update fields are allowed: description, pubsub_topic, streaming_config.filter

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateNotificationConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.UpdateNotificationConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[NotificationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.NotificationConfig)>` |   
  
### updateOrganizationSettings(UpdateOrganizationSettingsRequest request)
    
    
    public ListenableFuture<OrganizationSettings> updateOrganizationSettings(UpdateOrganizationSettingsRequest request)

Updates an organization's settings.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateOrganizationSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.UpdateOrganizationSettingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[OrganizationSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.OrganizationSettings)>` |   
  
### updateSecurityMarks(UpdateSecurityMarksRequest request)
    
    
    public ListenableFuture<SecurityMarks> updateSecurityMarks(UpdateSecurityMarksRequest request)

Updates security marks.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSecurityMarksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.UpdateSecurityMarksRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[SecurityMarks](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.SecurityMarks)>` |   
  
### updateSource(UpdateSourceRequest request)
    
    
    public ListenableFuture<Source> updateSource(UpdateSourceRequest request)

Updates a source.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSourceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.UpdateSourceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Source](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1p1beta1.Source)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
