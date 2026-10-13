---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.SecurityCenterSettingsServiceGrpc.SecurityCenterSettingsServiceFutureStub
title: Class SecurityCenterSettingsServiceGrpc.SecurityCenterSettingsServiceFutureStub (0.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:31.296788+00:00
---

# Class SecurityCenterSettingsServiceGrpc.SecurityCenterSettingsServiceFutureStub (0.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.SecurityCenterSettingsServiceGrpc.SecurityCenterSettingsServiceFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SecurityCenterSettingsServiceGrpc.SecurityCenterSettingsServiceFutureStub (0.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.102.0 (latest)  0.98.0  0.97.0  0.96.0  0.94.0  0.91.0  0.90.0  0.88.0  0.86.0  0.85.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.67.0  0.66.0  0.65.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.6  0.5.13 
    
    
    public static final class SecurityCenterSettingsServiceGrpc.SecurityCenterSettingsServiceFutureStub extends AbstractFutureStub<SecurityCenterSettingsServiceGrpc.SecurityCenterSettingsServiceFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service SecurityCenterSettingsService.

## API Overview

The SecurityCenterSettingsService is a sub-api of `securitycenter.googleapis.com`. The service provides methods to manage Security Center Settings, and Component Settings for GCP organizations, folders, projects, and clusters.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > SecurityCenterSettingsServiceGrpc.SecurityCenterSettingsServiceFutureStub

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

### batchCalculateEffectiveSettings(BatchCalculateEffectiveSettingsRequest request)
    
    
    public ListenableFuture<BatchCalculateEffectiveSettingsResponse> batchCalculateEffectiveSettings(BatchCalculateEffectiveSettingsRequest request)

Gets a list of effective settings.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchCalculateEffectiveSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.BatchCalculateEffectiveSettingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[BatchCalculateEffectiveSettingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.BatchCalculateEffectiveSettingsResponse)>` |   
  
### batchGetSettings(BatchGetSettingsRequest request)
    
    
    public ListenableFuture<BatchGetSettingsResponse> batchGetSettings(BatchGetSettingsRequest request)

Gets a list of settings.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[BatchGetSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.BatchGetSettingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[BatchGetSettingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.BatchGetSettingsResponse)>` |   
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected SecurityCenterSettingsServiceGrpc.SecurityCenterSettingsServiceFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterSettingsServiceGrpc.SecurityCenterSettingsServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.SecurityCenterSettingsServiceGrpc.SecurityCenterSettingsServiceFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### calculateEffectiveComponentSettings(CalculateEffectiveComponentSettingsRequest request)
    
    
    public ListenableFuture<ComponentSettings> calculateEffectiveComponentSettings(CalculateEffectiveComponentSettingsRequest request)

Gets the Effective Component Settings.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CalculateEffectiveComponentSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.CalculateEffectiveComponentSettingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ComponentSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.ComponentSettings)>` |   
  
### calculateEffectiveSettings(CalculateEffectiveSettingsRequest request)
    
    
    public ListenableFuture<Settings> calculateEffectiveSettings(CalculateEffectiveSettingsRequest request)

CalculateEffectiveSettings looks up all of the Security Center Settings resources in the GCP resource hierarchy, and calculates the effective settings on that resource by applying the following rules:

  * Settings provided closer to the target resource take precedence over those further away (e.g. folder will override organization level settings).
  * Product defaults can be overridden at org, folder, project, and cluster levels.
  * Detectors will be filtered out if they belong to a billing tier the customer has not configured.



**Parameter**  
---  
**Name** | **Description**  
`request` | `[CalculateEffectiveSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.CalculateEffectiveSettingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.Settings)>` |   
  
### getComponentSettings(GetComponentSettingsRequest request)
    
    
    public ListenableFuture<ComponentSettings> getComponentSettings(GetComponentSettingsRequest request)

Gets the Component Settings.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetComponentSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.GetComponentSettingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ComponentSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.ComponentSettings)>` |   
  
### getServiceAccount(GetServiceAccountRequest request)
    
    
    public ListenableFuture<ServiceAccount> getServiceAccount(GetServiceAccountRequest request)

Retrieves the organizations service account, if it exists, otherwise it creates the organization service account. This API is idempotent and will only create a service account once. On subsequent calls it will return the previously created service account. SHA, SCC and CTD Infra Automation will use this SA. This SA will not have any permissions when created. The UI will provision this via IAM or the user will using their own internal process. This API only creates SAs on the organization. Folders are not supported and projects will use per-project SAs associated with APIs enabled on a project. This API will be called by the UX onboarding workflow.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetServiceAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.GetServiceAccountRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.ServiceAccount)>` |   
  
### getSettings(GetSettingsRequest request)
    
    
    public ListenableFuture<Settings> getSettings(GetSettingsRequest request)

Gets the Settings.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.GetSettingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.Settings)>` |   
  
### listComponents(ListComponentsRequest request)
    
    
    public ListenableFuture<ListComponentsResponse> listComponents(ListComponentsRequest request)

Retrieves an unordered list of available SCC components.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListComponentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.ListComponentsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListComponentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.ListComponentsResponse)>` |   
  
### listDetectors(ListDetectorsRequest request)
    
    
    public ListenableFuture<ListDetectorsResponse> listDetectors(ListDetectorsRequest request)

Retrieves an unordered list of available detectors.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDetectorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.ListDetectorsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListDetectorsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.ListDetectorsResponse)>` |   
  
### resetComponentSettings(ResetComponentSettingsRequest request)
    
    
    public ListenableFuture<Empty> resetComponentSettings(ResetComponentSettingsRequest request)

Reset the organization, folder or project's component settings and return the settings to the default. Settings are present at the organization, folder and project levels. Using Reset for a folder or project will remove the override that was set and result in the organization-level settings being used.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResetComponentSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.ResetComponentSettingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### resetSettings(ResetSettingsRequest request)
    
    
    public ListenableFuture<Empty> resetSettings(ResetSettingsRequest request)

Reset the organization, folder or project's settings and return the settings of just that resource to the default. Settings are present at the organization, folder, project, and cluster levels. Using Reset on a sub-organization level will remove that resource's override and result in the parent's settings being used (eg: if Reset on a cluster, project settings will be used). Using Reset on organization will remove the override that was set and result in default settings being used.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ResetSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.ResetSettingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### updateComponentSettings(UpdateComponentSettingsRequest request)
    
    
    public ListenableFuture<ComponentSettings> updateComponentSettings(UpdateComponentSettingsRequest request)

Updates the Component Settings.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateComponentSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.UpdateComponentSettingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ComponentSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.ComponentSettings)>` |   
  
### updateSettings(UpdateSettingsRequest request)
    
    
    public ListenableFuture<Settings> updateSettings(UpdateSettingsRequest request)

Updates the Settings.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.UpdateSettingsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.Settings)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
