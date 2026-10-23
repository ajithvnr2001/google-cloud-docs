---
url: https://docs.cloud.google.com/managed-lustre/docs/self-service-maintenance/
title: Perform self-service maintenance \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:42:58.111076+00:00
---

# Perform self-service maintenance  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/self-service-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Perform self-service maintenance Stay organized with collections  Save and categorize content based on your preferences. 

Self-service maintenance lets you apply maintenance upgrades to your Managed Lustre instances on demand.

When Managed Lustre releases a new software version, it becomes available immediately for self-service maintenance. This is typically several weeks before automated maintenance reaches your instance.

You can perform self-service maintenance at any time once a version is available. If your instance has a maintenance policy, you can perform self-service maintenance up until 1 hour before a scheduled maintenance window.

For an overview of maintenance impact and policies, see [Maintenance overview](https://docs.cloud.google.com/managed-lustre/docs/maintenance).

## Check available maintenance versions

Managed Lustre instances track maintenance releases using the following version fields:

  * `effectiveVersion`: Output only. The software release version running on your instance. For example, `Lustre_20260516.00_p00`.
  * `availableVersion`: Output only. A qualified, newer software release version that your instance is eligible to upgrade to. If this field is empty, your instance is already running the latest available release.
  * `targetVersion`: Input only. The parameter specified in an update request to initiate an upgrade to a candidate version or to `latest`.



To verify your instance's current version and check whether an upgrade is available:

###  gcloud CLI 

Run the [`gcloud lustre instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/lustre/instances/describe) command with a format filter:
    
    
    gcloud lustre instances describe INSTANCE_ID \
      --location=LOCATION \
      --format="yaml(effectiveVersion, availableVersion, state)"

Replace the following:

  * INSTANCE_ID: The ID of your Managed Lustre instance.
  * LOCATION: The zone where your instance is located.



If a newer version is available, the output resembles the following:
    
    
    availableVersion: Lustre_20260716.01_p00
    effectiveVersion: Lustre_20260516.00_p00
    state: ACTIVE
    

If `availableVersion` is empty, your instance is already running the latest available release.

###  REST 

To check the version details for an instance, send a `GET` request to the instance endpoint:
    
    
    GET https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID
    Authorization: Bearer ACCESS_TOKEN
    

Where:

  * PROJECT_ID is your Google Cloud project ID.
  * LOCATION is the zone in which the instance resides.
  * INSTANCE_ID is the ID of the Managed Lustre instance.



If a newer version is available, the response contains `effectiveVersion` and `availableVersion`:
    
    
    {
      "name": "projects/my-project/locations/us-central1-a/instances/my-instance",
      "state": "ACTIVE",
      "effectiveVersion": "Lustre_20260516.00_p00",
      "availableVersion": "Lustre_20260716.01_p00"
    }
    

If `availableVersion` is omitted or empty, your instance is already running the latest available release.

See the [`instances.get`](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/get) API reference for more details.

## Perform a self-service upgrade

To upgrade your instance to an available software version:

###  gcloud CLI 

Run the [`gcloud lustre instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/lustre/instances/update) command with the `--target-version` flag:
    
    
    gcloud lustre instances update INSTANCE_ID \
      --location=LOCATION \
      --target-version=latest

Replace the following:

  * INSTANCE_ID: The ID of your Managed Lustre instance.
  * LOCATION: The zone where your instance is located.



To upgrade to a specific qualified release version instead of `latest`, pass the version string:
    
    
    gcloud lustre instances update INSTANCE_ID \
      --location=LOCATION \
      --target-version=TARGET_VERSION

Replace TARGET_VERSION with the version string from `availableVersion`. For example, `Lustre_20260716.01_p00`.

###  REST 

To upgrade an instance using the REST API, send a `PATCH` request to the instance endpoint, specifying `targetVersion` in the `updateMask` query parameter:
    
    
    PATCH https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID?updateMask=targetVersion
    Authorization: Bearer ACCESS_TOKEN
    
    {
      "targetVersion": "latest"
    }
    

Where:

  * PROJECT_ID is your Google Cloud project ID.
  * LOCATION is the zone in which the instance resides.
  * INSTANCE_ID is the ID of the Managed Lustre instance.



To upgrade to a specific qualified release version instead of `latest`, specify the version string in the request body, such as `"targetVersion": "Lustre_20260716.01_p00"`.

See the [`instances.patch`](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/patch) API reference for more details.

## Track maintenance progress

The upgrade executes as an asynchronous long-running operation. Self-service maintenance doesn't trigger automated notification emails.

To track progress in real time:

###  gcloud CLI 

Poll the operation status using the [`gcloud lustre operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/lustre/operations/describe) command:
    
    
    gcloud lustre operations describe OPERATION_ID \
      --location=LOCATION

Replace the following:

  * OPERATION_ID: The operation ID returned by the update command.
  * LOCATION: The zone where your instance is located.



The instance state displays `UPGRADING` while the upgrade is in progress and returns to `ACTIVE` once complete.

###  REST 

Send a `GET` request to the [`operations.get`](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.operations/get) endpoint:
    
    
    GET https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID
    Authorization: Bearer ACCESS_TOKEN
    

Where:

  * PROJECT_ID is your Google Cloud project ID.
  * LOCATION is the zone in which the instance resides.
  * OPERATION_ID is the operation ID returned by the update request.



See the [`operations.get`](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.operations/get) API reference for more details.

When the upgrade succeeds:

  1. The instance returns to `ACTIVE` state.
  2. `effectiveVersion` reflects the newly applied version string.
  3. `availableVersion` is cleared and omitted from API responses.



## Interaction with scheduled maintenance

If your instance has upcoming scheduled maintenance, successfully completing a self-service upgrade automatically cancels that upcoming scheduled maintenance. If you're [subscribed to maintenance notifications](https://docs.cloud.google.com/managed-lustre/docs/maintenance-notifications#notifications), you receive an automated **Maintenance canceled** email notification.

If a self-service upgrade fails, the pending scheduled maintenance window is not canceled. The instance returns to `ACTIVE` state on its current version, and the scheduled maintenance window is retained.

You cannot trigger a self-service upgrade within 1 hour of an upcoming scheduled maintenance window. Attempting to initiate an upgrade during this period returns a `409 CONFLICT` error to avoid overlapping with the upcoming scheduled maintenance.

## Error messages

Possible self-service maintenance errors include:

  * **`Instance is already running version "<CURRENT>"`**: Occurs if you attempt to upgrade to the software version already running on the instance.
  * **`Downgrading to a lower version is not supported.`** : Occurs if you attempt to downgrade to an earlier software version.
  * **`Version "<TARGET>" is not a valid update version.`**: Occurs if the specified version does not match the instance's `availableVersion` string or `latest`.
  * **`Instance must be in ACTIVE state to update version`** : Occurs if an upgrade is initiated while the instance is not in the `ACTIVE` state.
  * **`Cannot trigger self-service update within 1 hour of a scheduled maintenance window`** : Occurs if a self-service upgrade is initiated less than 1 hour before an upcoming scheduled maintenance window.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
