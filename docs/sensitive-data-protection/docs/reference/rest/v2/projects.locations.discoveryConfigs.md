---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.discoveryConfigs
title: REST Resource: projects.locations.discoveryConfigs \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:34.035183+00:00
---

# REST Resource: projects.locations.discoveryConfigs  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.discoveryConfigs

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  REST Resource: projects.locations.discoveryConfigs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DiscoveryConfig
    * JSON representation
  * Methods



## Resource: DiscoveryConfig

Configuration for discovery to scan resources for profile generation. Only one discovery configuration may exist per organization, folder, or project.

The generated data profiles are retained according to the [data retention policy](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#retention).

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "orgConfig": {
        object ([OrgConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.OrgConfig))
      },
      "otherCloudStartingLocation": {
        object ([OtherCloudDiscoveryStartingLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/OtherCloudDiscoveryStartingLocation))
      },
      "inspectTemplates": [
        string
      ],
      "actions": [
        {
          object ([DataProfileAction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction))
        }
      ],
      "targets": [
        {
          object ([DiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryTarget))
        }
      ],
      "errors": [
        {
          object ([Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Error))
        }
      ],
      "createTime": string,
      "updateTime": string,
      "lastRunTime": string,
      "status": enum ([Status](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.Status)),
      "processingLocation": {
        object ([ProcessingLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.ProcessingLocation))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. Unique resource name for the DiscoveryConfig, assigned by the service when the DiscoveryConfig is created, for example `projects/dlp-test-project/locations/global/discoveryConfigs/53234423`.  
`displayName` |  `string` Display name (max 100 chars)  
`orgConfig` |  `object (`[OrgConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.OrgConfig)`)` Only set when the parent is an org.  
`otherCloudStartingLocation` |  `object (`[OtherCloudDiscoveryStartingLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/OtherCloudDiscoveryStartingLocation)`)` Must be set only when scanning other clouds.  
`inspectTemplates[]` |  `string` Detection logic for profile generation.Not all template features are used by Discovery. FindingLimits, includeQuote and excludeInfoTypes have no impact on Discovery.Multiple templates may be provided if there is data in multiple regions. At most one template must be specified per-region (including "global"). Each region is scanned using the applicable template. If no region-specific template is specified, but a "global" template is specified, it will be copied to that region and used instead. If no global or region-specific template is provided for a region with data, that region's data will not be scanned.For more information, see <https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#data-residency>.  
`actions[]` |  `object (`[DataProfileAction](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileAction)`)` Actions to execute at the completion of scanning.  
`targets[]` |  `object (`[DiscoveryTarget](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.DiscoveryTarget)`)` Target to match against for determining what to scan and how frequently.  
`errors[]` |  `object (`[Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Error)`)` Output only. A stream of errors encountered when the config was activated. Repeated errors may result in the config automatically being paused. Output only field. Will return the last 100 errors. Whenever the config is modified this list will be cleared.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation timestamp of a DiscoveryConfig.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last update timestamp of a DiscoveryConfig.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastRunTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of the last time this config was executed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`status` |  `enum (`[Status](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.Status)`)` Required. A status for this configuration.  
`processingLocation` |  `object (`[ProcessingLocation](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs#DiscoveryConfig.ProcessingLocation)`)` Optional. Processing location configuration. Vertex AI dataset scanning will set processingLocation.image_fallback_type to MultiRegionProcessing by default.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.discoveryConfigs/create)`

|  Creates a config for discovery to scan and profile storage.  
  
### `[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.discoveryConfigs/delete)`

|  Deletes a discovery configuration.  
  
### `[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.discoveryConfigs/get)`

|  Gets a discovery configuration.  
  
### `[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.discoveryConfigs/list)`

|  Lists discovery configurations.  
  
### `[patch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.discoveryConfigs/patch)`

|  Updates a discovery configuration.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-21 UTC."],[],[]] 
