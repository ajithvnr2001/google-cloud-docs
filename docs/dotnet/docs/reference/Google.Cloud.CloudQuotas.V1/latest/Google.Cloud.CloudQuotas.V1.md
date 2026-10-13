---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1
title: Cloud Quotas v1 API - Namespace Google.Cloud.CloudQuotas.V1 (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:20.041804+00:00
---

# Cloud Quotas v1 API - Namespace Google.Cloud.CloudQuotas.V1 (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Quotas v1 API - Namespace Google.Cloud.CloudQuotas.V1 (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0-beta05 

## Classes 

### [CloudQuotas](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotas)

The Cloud Quotas API is an infrastructure service for Google Cloud that lets service consumers list and manage their resource usage limits.

  * List/Get the metadata and current status of the quotas for a service.
  * Create/Update quota preferencess that declare the preferred quota values.
  * Check the status of a quota preference request.
  * List/Get pending and historical quota preference.



### [CloudQuotas.CloudQuotasBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotas.CloudQuotasBase)

Base class for server-side implementations of CloudQuotas

### [CloudQuotas.CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotas.CloudQuotasClient)

Client for CloudQuotas

### [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient)

CloudQuotas client wrapper, for convenient use.

### [CloudQuotasClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClientBuilder)

Builder class for [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient) to provide simple configuration of credentials, endpoint etc.

### [CloudQuotasClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClientImpl)

CloudQuotas client wrapper implementation, for convenient use.

### [CloudQuotasSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasSettings)

Settings for [CloudQuotasClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CloudQuotasClient) instances.

### [CreateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.CreateQuotaPreferenceRequest)

Message for creating a QuotaPreference

### [DimensionsInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.DimensionsInfo)

The detailed quota information such as effective quota value for a combination of dimensions.

### [GetQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaAdjusterSettingsRequest)

Request for getting QuotaAdjusterSettings

### [GetQuotaInfoRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaInfoRequest)

Message for getting a QuotaInfo

### [GetQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.GetQuotaPreferenceRequest)

Message for getting a QuotaPreference

### [ListQuotaInfosRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosRequest)

Message for requesting list of QuotaInfos

### [ListQuotaInfosResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaInfosResponse)

Message for response to listing QuotaInfos

### [ListQuotaPreferencesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesRequest)

Message for requesting list of QuotaPreferences

### [ListQuotaPreferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ListQuotaPreferencesResponse)

Message for response to listing QuotaPreferences

### [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName)

Resource name for the `Location` resource.

### [QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)

The QuotaAdjusterSettings resource defines the settings for the Quota Adjuster.

### [QuotaAdjusterSettings.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings.Types)

Container for nested types declared in the QuotaAdjusterSettings message type.

### [QuotaAdjusterSettingsManager](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManager)

The Quotas Adjuster Settings API is an infrastructure service for Google Cloud that lets service consumers view and update their quota adjuster settings.

  * Update quota adjuster settings.
  * Get the name of the configurations.



### [QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerBase)

Base class for server-side implementations of QuotaAdjusterSettingsManager

### [QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManager.QuotaAdjusterSettingsManagerClient)

Client for QuotaAdjusterSettingsManager

### [QuotaAdjusterSettingsManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManagerClient)

QuotaAdjusterSettingsManager client wrapper, for convenient use.

### [QuotaAdjusterSettingsManagerClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManagerClientBuilder)

Builder class for [QuotaAdjusterSettingsManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManagerClient) to provide simple configuration of credentials, endpoint etc.

### [QuotaAdjusterSettingsManagerClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManagerClientImpl)

QuotaAdjusterSettingsManager client wrapper implementation, for convenient use.

### [QuotaAdjusterSettingsManagerSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManagerSettings)

Settings for [QuotaAdjusterSettingsManagerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsManagerClient) instances.

### [QuotaAdjusterSettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsName)

Resource name for the `QuotaAdjusterSettings` resource.

### [QuotaConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaConfig)

The preferred quota configuration.

### [QuotaConfig.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaConfig.Types)

Container for nested types declared in the QuotaConfig message type.

### [QuotaDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaDetails)

The quota details for a map of dimensions.

### [QuotaIncreaseEligibility](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaIncreaseEligibility)

Eligibility information regarding requesting increase adjustment of a quota.

### [QuotaIncreaseEligibility.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaIncreaseEligibility.Types)

Container for nested types declared in the QuotaIncreaseEligibility message type.

### [QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo)

QuotaInfo represents information about a particular quota for a given project, folder or organization.

### [QuotaInfo.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.Types)

Container for nested types declared in the QuotaInfo message type.

### [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName)

Resource name for the `QuotaInfo` resource.

### [QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)

QuotaPreference represents the preferred quota configuration specified for a project, folder or organization. There is only one QuotaPreference resource for a quota value targeting a unique set of dimensions.

### [QuotaPreferenceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName)

Resource name for the `QuotaPreference` resource.

### [RolloutInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.RolloutInfo)

[Output only] Rollout information of a quota.

### [ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName)

Resource name for the `Service` resource.

### [UpdateQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaAdjusterSettingsRequest)

Request for updating QuotaAdjusterSettings

### [UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaPreferenceRequest)

Message for updating a QuotaPreference

## Enums 

### [LocationName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName.ResourceNameType)

The possible contents of [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.LocationName).

### [QuotaAdjusterSettings.Types.Enablement](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings.Types.Enablement)

The enablement status of the quota adjuster.

### [QuotaAdjusterSettingsName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsName.ResourceNameType)

The possible contents of [QuotaAdjusterSettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsName).

### [QuotaConfig.Types.Origin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaConfig.Types.Origin)

The enumeration of the origins of quota preference requests.

### [QuotaIncreaseEligibility.Types.IneligibilityReason](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaIncreaseEligibility.Types.IneligibilityReason)

The enumeration of reasons when it is ineligible to request increase adjustment.

### [QuotaInfo.Types.ContainerType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.Types.ContainerType)

The enumeration of the types of a cloud resource container.

### [QuotaInfoName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName.ResourceNameType)

The possible contents of [QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName).

### [QuotaPreferenceName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName.ResourceNameType)

The possible contents of [QuotaPreferenceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName).

### [QuotaSafetyCheck](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaSafetyCheck)

Enumerations of quota safety checks.

### [ServiceName.ResourceNameType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName.ResourceNameType)

The possible contents of [ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.ServiceName).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
