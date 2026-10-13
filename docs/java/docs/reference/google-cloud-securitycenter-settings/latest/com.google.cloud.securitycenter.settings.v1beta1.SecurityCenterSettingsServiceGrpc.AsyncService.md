---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.SecurityCenterSettingsServiceGrpc.AsyncService
title: Interface SecurityCenterSettingsServiceGrpc.AsyncService (0.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:28.163295+00:00
---

# Interface SecurityCenterSettingsServiceGrpc.AsyncService (0.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.SecurityCenterSettingsServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SecurityCenterSettingsServiceGrpc.AsyncService (0.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.102.0 (latest)  0.98.0  0.97.0  0.96.0  0.94.0  0.91.0  0.90.0  0.88.0  0.86.0  0.85.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.75.0  0.73.0  0.71.0  0.70.0  0.67.0  0.66.0  0.65.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.6  0.5.13 
    
    
    public static interface SecurityCenterSettingsServiceGrpc.AsyncService

## API Overview

The SecurityCenterSettingsService is a sub-api of `securitycenter.googleapis.com`. The service provides methods to manage Security Center Settings, and Component Settings for GCP organizations, folders, projects, and clusters.

## Methods 

### batchCalculateEffectiveSettings(BatchCalculateEffectiveSettingsRequest request, StreamObserver<BatchCalculateEffectiveSettingsResponse> responseObserver)
    
    
    public default void batchCalculateEffectiveSettings(BatchCalculateEffectiveSettingsRequest request, StreamObserver<BatchCalculateEffectiveSettingsResponse> responseObserver)

Gets a list of effective settings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCalculateEffectiveSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.BatchCalculateEffectiveSettingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BatchCalculateEffectiveSettingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.BatchCalculateEffectiveSettingsResponse)>`  
  
  
### batchGetSettings(BatchGetSettingsRequest request, StreamObserver<BatchGetSettingsResponse> responseObserver)
    
    
    public default void batchGetSettings(BatchGetSettingsRequest request, StreamObserver<BatchGetSettingsResponse> responseObserver)

Gets a list of settings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchGetSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.BatchGetSettingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BatchGetSettingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.BatchGetSettingsResponse)>`  
  
  
### calculateEffectiveComponentSettings(CalculateEffectiveComponentSettingsRequest request, StreamObserver<ComponentSettings> responseObserver)
    
    
    public default void calculateEffectiveComponentSettings(CalculateEffectiveComponentSettingsRequest request, StreamObserver<ComponentSettings> responseObserver)

Gets the Effective Component Settings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CalculateEffectiveComponentSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.CalculateEffectiveComponentSettingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ComponentSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.ComponentSettings)>`  
  
  
### calculateEffectiveSettings(CalculateEffectiveSettingsRequest request, StreamObserver<Settings> responseObserver)
    
    
    public default void calculateEffectiveSettings(CalculateEffectiveSettingsRequest request, StreamObserver<Settings> responseObserver)

CalculateEffectiveSettings looks up all of the Security Center Settings resources in the GCP resource hierarchy, and calculates the effective settings on that resource by applying the following rules:

  * Settings provided closer to the target resource take precedence over those further away (e.g. folder will override organization level settings).
  * Product defaults can be overridden at org, folder, project, and cluster levels.
  * Detectors will be filtered out if they belong to a billing tier the customer has not configured.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CalculateEffectiveSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.CalculateEffectiveSettingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.Settings)>`  
  
  
### getComponentSettings(GetComponentSettingsRequest request, StreamObserver<ComponentSettings> responseObserver)
    
    
    public default void getComponentSettings(GetComponentSettingsRequest request, StreamObserver<ComponentSettings> responseObserver)

Gets the Component Settings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetComponentSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.GetComponentSettingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ComponentSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.ComponentSettings)>`  
  
  
### getServiceAccount(GetServiceAccountRequest request, StreamObserver<ServiceAccount> responseObserver)
    
    
    public default void getServiceAccount(GetServiceAccountRequest request, StreamObserver<ServiceAccount> responseObserver)

Retrieves the organizations service account, if it exists, otherwise it creates the organization service account. This API is idempotent and will only create a service account once. On subsequent calls it will return the previously created service account. SHA, SCC and CTD Infra Automation will use this SA. This SA will not have any permissions when created. The UI will provision this via IAM or the user will using their own internal process. This API only creates SAs on the organization. Folders are not supported and projects will use per-project SAs associated with APIs enabled on a project. This API will be called by the UX onboarding workflow.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetServiceAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.GetServiceAccountRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.ServiceAccount)>`  
  
  
### getSettings(GetSettingsRequest request, StreamObserver<Settings> responseObserver)
    
    
    public default void getSettings(GetSettingsRequest request, StreamObserver<Settings> responseObserver)

Gets the Settings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.GetSettingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.Settings)>`  
  
  
### listComponents(ListComponentsRequest request, StreamObserver<ListComponentsResponse> responseObserver)
    
    
    public default void listComponents(ListComponentsRequest request, StreamObserver<ListComponentsResponse> responseObserver)

Retrieves an unordered list of available SCC components.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListComponentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.ListComponentsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListComponentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.ListComponentsResponse)>`  
  
  
### listDetectors(ListDetectorsRequest request, StreamObserver<ListDetectorsResponse> responseObserver)
    
    
    public default void listDetectors(ListDetectorsRequest request, StreamObserver<ListDetectorsResponse> responseObserver)

Retrieves an unordered list of available detectors.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDetectorsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.ListDetectorsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListDetectorsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.ListDetectorsResponse)>`  
  
  
### resetComponentSettings(ResetComponentSettingsRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void resetComponentSettings(ResetComponentSettingsRequest request, StreamObserver<Empty> responseObserver)

Reset the organization, folder or project's component settings and return the settings to the default. Settings are present at the organization, folder and project levels. Using Reset for a folder or project will remove the override that was set and result in the organization-level settings being used.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResetComponentSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.ResetComponentSettingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### resetSettings(ResetSettingsRequest request, StreamObserver<Empty> responseObserver)
    
    
    public default void resetSettings(ResetSettingsRequest request, StreamObserver<Empty> responseObserver)

Reset the organization, folder or project's settings and return the settings of just that resource to the default. Settings are present at the organization, folder, project, and cluster levels. Using Reset on a sub-organization level will remove that resource's override and result in the parent's settings being used (eg: if Reset on a cluster, project settings will be used). Using Reset on organization will remove the override that was set and result in default settings being used.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResetSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.ResetSettingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### updateComponentSettings(UpdateComponentSettingsRequest request, StreamObserver<ComponentSettings> responseObserver)
    
    
    public default void updateComponentSettings(UpdateComponentSettingsRequest request, StreamObserver<ComponentSettings> responseObserver)

Updates the Component Settings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateComponentSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.UpdateComponentSettingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ComponentSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.ComponentSettings)>`  
  
  
### updateSettings(UpdateSettingsRequest request, StreamObserver<Settings> responseObserver)
    
    
    public default void updateSettings(UpdateSettingsRequest request, StreamObserver<Settings> responseObserver)

Updates the Settings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.UpdateSettingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Settings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter-settings/latest/com.google.cloud.securitycenter.settings.v1beta1.Settings)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
