---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.datacenterConnectors
title: REST Resource: projects.locations.sources.datacenterConnectors \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:37:33.199399+00:00
---

# REST Resource: projects.locations.sources.datacenterConnectors  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.datacenterConnectors

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Reference ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference)



Send feedback 

#  REST Resource: projects.locations.sources.datacenterConnectors Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DatacenterConnector
    * JSON representation
  * State
  * AvailableUpdates
    * JSON representation
  * ApplianceVersion
    * JSON representation
  * UpgradeStatus
    * JSON representation
  * State
  * Methods



## Resource: DatacenterConnector

DatacenterConnector message describes a connector between the Source and Google Cloud, which is installed on a vmware datacenter (an OVA vm installed by the user) to connect the Datacenter to Google Cloud and support vm migration data transfer.

JSON representation  
---  
      
    
    {
      "createTime": string,
      "updateTime": string,
      "name": string,
      "registrationId": string,
      "serviceAccount": string,
      "version": string,
      "bucket": string,
      "state": enum ([State](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.datacenterConnectors#State)),
      "stateTime": string,
      "error": {
        object ([Status](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/Status))
      },
      "applianceInfrastructureVersion": string,
      "applianceSoftwareVersion": string,
      "availableVersions": {
        object ([AvailableUpdates](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.datacenterConnectors#AvailableUpdates))
      },
      "upgradeStatus": {
        object ([UpgradeStatus](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.datacenterConnectors#UpgradeStatus))
      }
    }  
  
Fields  
---  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the connector was created (as an API call, not when it was actually installed).A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last time the connector was updated with an API call.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`name` |  `string` Output only. The connector's name.  
`registrationId` |  `string` Immutable. A unique key for this connector. This key is internal to the OVA connector and is supplied with its creation during the registration process and can not be modified.  
`serviceAccount` |  `string` The service account to use in the connector when communicating with the cloud.  
`version` |  `string` The version running in the DatacenterConnector. This is supplied by the OVA connector during the registration process and can not be modified.  
`bucket` |  `string` Output only. The communication channel between the datacenter connector and Google Cloud.  
`state` |  `enum (`[State](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.datacenterConnectors#State)`)` Output only. State of the DatacenterConnector, as determined by the health checks.  
`stateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the state was last set.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`error` |  `object (`[Status](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/Status)`)` Output only. Provides details on the state of the Datacenter Connector in case of an error.  
`applianceInfrastructureVersion` |  `string` Output only. Appliance OVA version. This is the OVA which is manually installed by the user and contains the infrastructure for the automatically updatable components on the appliance.  
`applianceSoftwareVersion` |  `string` Output only. Appliance last installed update bundle version. This is the version of the automatically updatable components on the appliance.  
`availableVersions` |  `object (`[AvailableUpdates](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.datacenterConnectors#AvailableUpdates)`)` Output only. The available versions for updating this appliance.  
`upgradeStatus` |  `object (`[UpgradeStatus](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.datacenterConnectors#UpgradeStatus)`)` Output only. The status of the current / last upgradeAppliance operation.  
  
## State

The possible values of the state.

Enums  
---  
`STATE_UNSPECIFIED` | The state is unknown. This is used for API compatibility only and is not used by the system.  
`PENDING` | The state was not sampled by the health checks yet.  
`OFFLINE` | The source was sampled by health checks and is not available.  
`FAILED` | The source is available but might not be usable yet due to unvalidated credentials or another reason. The credentials referred to are the ones to the Source. The error message will contain further details.  
`ACTIVE` | The source exists and its credentials were verified.  
  
## AvailableUpdates

Holds informatiom about the available versions for upgrade.

JSON representation  
---  
      
    
    {
      "newDeployableAppliance": {
        object ([ApplianceVersion](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.datacenterConnectors#ApplianceVersion))
      },
      "inPlaceUpdate": {
        object ([ApplianceVersion](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.datacenterConnectors#ApplianceVersion))
      }
    }  
  
Fields  
---  
`newDeployableAppliance` |  `object (`[ApplianceVersion](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.datacenterConnectors#ApplianceVersion)`)` The newest deployable version of the appliance. The current appliance can't be updated into this version, and the owner must manually deploy this OVA to a new appliance.  
`inPlaceUpdate` |  `object (`[ApplianceVersion](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.datacenterConnectors#ApplianceVersion)`)` The latest version for in place update. The current appliance can be updated to this version using the API or m4c CLI.  
  
## ApplianceVersion

Describes an appliance version.

JSON representation  
---  
      
    
    {
      "version": string,
      "uri": string,
      "critical": boolean,
      "releaseNotesUri": string
    }  
  
Fields  
---  
`version` |  `string` The appliance version.  
`uri` |  `string` A link for downloading the version.  
`critical` |  `boolean` Determine whether it's critical to upgrade the appliance to this version.  
`releaseNotesUri` |  `string` Link to a page that contains the version release notes.  
  
## UpgradeStatus

UpgradeStatus contains information about upgradeAppliance operation.

JSON representation  
---  
      
    
    {
      "version": string,
      "state": enum ([State](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.datacenterConnectors#State_1)),
      "error": {
        object ([Status](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/Status))
      },
      "startTime": string,
      "previousVersion": string
    }  
  
Fields  
---  
`version` |  `string` The version to upgrade to.  
`state` |  `enum (`[State](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.datacenterConnectors#State_1)`)` The state of the upgradeAppliance operation.  
`error` |  `object (`[Status](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/Status)`)` Output only. Provides details on the state of the upgrade operation in case of an error.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the operation was started.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`previousVersion` |  `string` The version from which we upgraded.  
  
## State

The possible values of the state.

Enums  
---  
`STATE_UNSPECIFIED` | The state was not sampled by the health checks yet.  
`RUNNING` | The upgrade has started.  
`FAILED` | The upgrade failed.  
`SUCCEEDED` | The upgrade finished successfully.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.datacenterConnectors/create)`

|  Creates a new DatacenterConnector in a given Source.  
  
### `[delete](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.datacenterConnectors/delete)`

|  Deletes a single DatacenterConnector.  
  
### `[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.datacenterConnectors/get)`

|  Gets details of a single DatacenterConnector.  
  
### `[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.datacenterConnectors/list)`

|  Lists DatacenterConnectors in a given Source.  
  
### `[upgradeAppliance](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.datacenterConnectors/upgradeAppliance)`

|  Upgrades the appliance relate to this DatacenterConnector to the in-place updateable version.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
