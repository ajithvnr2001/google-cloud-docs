---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1
title: Google Cloud Security Command Center v1p1beta1 API - Namespace Google.Cloud.SecurityCenter.V1P1Beta1 (3.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:12.458808+00:00
---

# Google Cloud Security Command Center v1p1beta1 API - Namespace Google.Cloud.SecurityCenter.V1P1Beta1 (3.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Security Command Center v1p1beta1 API - Namespace Google.Cloud.SecurityCenter.V1P1Beta1 (3.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1)
  * [ 3.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/3.0.0-beta05/Google.Cloud.SecurityCenter.V1P1Beta1)
  * [ 2.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/2.0.0-beta07/Google.Cloud.SecurityCenter.V1P1Beta1)



## Classes 

### [Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.Asset)

Security Command Center representation of a Google Cloud resource.

The Asset is a Security Command Center resource that captures information about a single Google Cloud resource. All modifications to an Asset are only within the context of Security Command Center and don't affect the referenced Google Cloud resource.

### [Asset.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.Asset.Types)

Container for nested types declared in the Asset message type.

### [Asset.Types.IamPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.Asset.Types.IamPolicy)

Cloud IAM Policy information associated with the Google Cloud resource described by the Security Command Center asset. This information is managed and defined by the Google Cloud resource and cannot be modified by the user.

### [Asset.Types.SecurityCenterProperties](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.Asset.Types.SecurityCenterProperties)

Security Command Center managed properties. These properties are managed by Security Command Center and cannot be modified by the user.

### [AssetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.AssetName)

Resource name for the `Asset` resource.

### [CreateFindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.CreateFindingRequest)

Request message for creating a finding.

### [CreateNotificationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.CreateNotificationConfigRequest)

Request message for creating a notification config.

### [CreateSourceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.CreateSourceRequest)

Request message for creating a source.

### [DeleteNotificationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.DeleteNotificationConfigRequest)

Request message for deleting a notification config.

### [Finding](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.Finding)

Security Command Center finding.

A finding is a record of assessment data (security, risk, health or privacy) ingested into Security Command Center for presentation, notification, analysis, policy testing, and enforcement. For example, an XSS vulnerability in an App Engine application is a finding.

### [Finding.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.Finding.Types)

Container for nested types declared in the Finding message type.

### [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.FindingName)

Resource name for the `Finding` resource.

### [Folder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.Folder)

Message that contains the resource name and display name of a folder resource.

### [GetNotificationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.GetNotificationConfigRequest)

Request message for getting a notification config.

### [GetOrganizationSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.GetOrganizationSettingsRequest)

Request message for getting organization settings.

### [GetSourceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.GetSourceRequest)

Request message for getting a source.

### [GroupAssetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.GroupAssetsRequest)

Request message for grouping by assets.

### [GroupAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.GroupAssetsResponse)

Response message for grouping by assets.

### [GroupFindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.GroupFindingsRequest)

Request message for grouping by findings.

### [GroupFindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.GroupFindingsResponse)

Response message for group by findings.

### [GroupResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.GroupResult)

Result containing the properties and count of a groupBy request.

### [ListAssetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsRequest)

Request message for listing assets.

### [ListAssetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse)

Response message for listing assets.

### [ListAssetsResponse.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse.Types)

Container for nested types declared in the ListAssetsResponse message type.

### [ListAssetsResponse.Types.ListAssetsResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse.Types.ListAssetsResult)

Result containing the Asset and its State.

### [ListAssetsResponse.Types.ListAssetsResult.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse.Types.ListAssetsResult.Types)

Container for nested types declared in the ListAssetsResult message type.

### [ListFindingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListFindingsRequest)

Request message for listing findings.

### [ListFindingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListFindingsResponse)

Response message for listing findings.

### [ListFindingsResponse.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListFindingsResponse.Types)

Container for nested types declared in the ListFindingsResponse message type.

### [ListFindingsResponse.Types.ListFindingsResult](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListFindingsResponse.Types.ListFindingsResult)

Result containing the Finding and its StateChange.

### [ListFindingsResponse.Types.ListFindingsResult.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListFindingsResponse.Types.ListFindingsResult.Types)

Container for nested types declared in the ListFindingsResult message type.

### [ListFindingsResponse.Types.ListFindingsResult.Types.Resource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListFindingsResponse.Types.ListFindingsResult.Types.Resource)

Information related to the Google Cloud resource that is associated with this finding.

### [ListNotificationConfigsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListNotificationConfigsRequest)

Request message for listing notification configs.

### [ListNotificationConfigsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListNotificationConfigsResponse)

Response message for listing notification configs.

### [ListSourcesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListSourcesRequest)

Request message for listing sources.

### [ListSourcesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListSourcesResponse)

Response message for listing sources.

### [NotificationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.NotificationConfig)

Security Command Center notification configs.

A notification config is a Security Command Center resource that contains the configuration to send notifications for create/update events of findings, assets and etc.

### [NotificationConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.NotificationConfig.Types)

Container for nested types declared in the NotificationConfig message type.

### [NotificationConfig.Types.StreamingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.NotificationConfig.Types.StreamingConfig)

The config for streaming-based notifications, which send each event as soon as it is detected.

### [NotificationConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.NotificationConfigName)

Resource name for the `NotificationConfig` resource.

### [NotificationMessage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.NotificationMessage)

Security Command Center's Notification

### [OrganizationSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.OrganizationSettings)

User specified settings that are attached to the Security Command Center organization.

### [OrganizationSettings.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.OrganizationSettings.Types)

Container for nested types declared in the OrganizationSettings message type.

### [OrganizationSettings.Types.AssetDiscoveryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.OrganizationSettings.Types.AssetDiscoveryConfig)

The configuration used for Asset Discovery runs.

### [OrganizationSettings.Types.AssetDiscoveryConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.OrganizationSettings.Types.AssetDiscoveryConfig.Types)

Container for nested types declared in the AssetDiscoveryConfig message type.

### [OrganizationSettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.OrganizationSettingsName)

Resource name for the `OrganizationSettings` resource.

### [Resource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.Resource)

Information related to the Google Cloud resource.

### [RunAssetDiscoveryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.RunAssetDiscoveryRequest)

Request message for running asset discovery for an organization.

### [RunAssetDiscoveryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.RunAssetDiscoveryResponse)

Response of asset discovery run

### [RunAssetDiscoveryResponse.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.RunAssetDiscoveryResponse.Types)

Container for nested types declared in the RunAssetDiscoveryResponse message type.

### [SecurityCenter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.SecurityCenter)

V1p1Beta1 APIs for Security Center service.

### [SecurityCenter.SecurityCenterBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.SecurityCenter.SecurityCenterBase)

Base class for server-side implementations of SecurityCenter

### [SecurityCenter.SecurityCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.SecurityCenter.SecurityCenterClient)

Client for SecurityCenter

### [SecurityCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.SecurityCenterClient)

SecurityCenter client wrapper, for convenient use.

### [SecurityCenterClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.SecurityCenterClientBuilder)

Builder class for [SecurityCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.SecurityCenterClient) to provide simple configuration of credentials, endpoint etc.

### [SecurityCenterClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.SecurityCenterClientImpl)

SecurityCenter client wrapper implementation, for convenient use.

### [SecurityCenterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.SecurityCenterSettings)

Settings for [SecurityCenterClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.SecurityCenterClient) instances.

### [SecurityMarks](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.SecurityMarks)

User specified security marks that are attached to the parent Security Command Center resource. Security marks are scoped within a Security Command Center organization -- they can be modified and viewed by all users who have proper permissions on the organization.

### [SecurityMarksName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.SecurityMarksName)

Resource name for the `SecurityMarks` resource.

### [SetFindingStateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.SetFindingStateRequest)

Request message for updating a finding's state.

### [Source](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.Source)

Security Command Center finding source. A finding source is an entity or a mechanism that can produce a finding. A source is like a container of findings that come from the same scanner, logger, monitor, etc.

### [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.SourceName)

Resource name for the `Source` resource.

### [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.TopicName)

Resource name for the `Topic` resource.

### [UpdateFindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.UpdateFindingRequest)

Request message for updating or creating a finding.

### [UpdateNotificationConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.UpdateNotificationConfigRequest)

Request message for updating a notification config.

### [UpdateOrganizationSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.UpdateOrganizationSettingsRequest)

Request message for updating an organization's settings.

### [UpdateSecurityMarksRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.UpdateSecurityMarksRequest)

Request message for updating a SecurityMarks resource.

### [UpdateSourceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.UpdateSourceRequest)

Request message for updating a source.

## Enums 

### [AssetName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.AssetName.ResourceNameType)

The possible contents of [AssetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.AssetName).

### [Finding.Types.Severity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.Finding.Types.Severity)

The severity of the finding. This field is managed by the source that writes the finding.

### [Finding.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.Finding.Types.State)

The state of the finding.

### [FindingName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.FindingName.ResourceNameType)

The possible contents of [FindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.FindingName).

### [ListAssetsResponse.Types.ListAssetsResult.Types.StateChange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListAssetsResponse.Types.ListAssetsResult.Types.StateChange)

The change in state of the asset.

When querying across two points in time this describes the change between the two points: ADDED, REMOVED, or ACTIVE. If there was no compare_duration supplied in the request the state change will be: UNUSED

### [ListFindingsResponse.Types.ListFindingsResult.Types.StateChange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.ListFindingsResponse.Types.ListFindingsResult.Types.StateChange)

The change in state of the finding.

When querying across two points in time this describes the change in the finding between the two points: CHANGED, UNCHANGED, ADDED, or REMOVED. Findings can not be deleted, so REMOVED implies that the finding at timestamp does not match the filter specified, but it did at timestamp - compare_duration. If there was no compare_duration supplied in the request the state change will be: UNUSED

### [NotificationConfig.NotifyConfigOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.NotificationConfig.NotifyConfigOneofCase)

Enum of possible cases for the "notify_config" oneof.

### [NotificationConfig.Types.EventType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.NotificationConfig.Types.EventType)

The type of events.

### [NotificationConfigName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.NotificationConfigName.ResourceNameType)

The possible contents of [NotificationConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.NotificationConfigName).

### [NotificationMessage.EventOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.NotificationMessage.EventOneofCase)

Enum of possible cases for the "event" oneof.

### [OrganizationSettings.Types.AssetDiscoveryConfig.Types.InclusionMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.OrganizationSettings.Types.AssetDiscoveryConfig.Types.InclusionMode)

The mode of inclusion when running Asset Discovery. Asset discovery can be limited by explicitly identifying projects to be included or excluded. If INCLUDE_ONLY is set, then only those projects within the organization and their children are discovered during asset discovery. If EXCLUDE is set, then projects that don't match those projects are discovered during asset discovery. If neither are set, then all projects within the organization are discovered during asset discovery.

### [OrganizationSettingsName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.OrganizationSettingsName.ResourceNameType)

The possible contents of [OrganizationSettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.OrganizationSettingsName).

### [RunAssetDiscoveryResponse.Types.State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.RunAssetDiscoveryResponse.Types.State)

The state of an asset discovery run.

### [SecurityMarksName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.SecurityMarksName.ResourceNameType)

The possible contents of [SecurityMarksName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.SecurityMarksName).

### [SourceName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.SourceName.ResourceNameType)

The possible contents of [SourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.SourceName).

### [TopicName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.TopicName.ResourceNameType)

The possible contents of [TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.V1P1Beta1/latest/Google.Cloud.SecurityCenter.V1P1Beta1.TopicName).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
