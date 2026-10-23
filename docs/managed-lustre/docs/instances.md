---
url: https://docs.cloud.google.com/managed-lustre/docs/instances/
title: Manage Google Cloud Managed Lustre instances \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:51:05.668732+00:00
---

# Manage Google Cloud Managed Lustre instances  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)



Send feedback 

#  Manage Google Cloud Managed Lustre instances Stay organized with collections  Save and categorize content based on your preferences. 

Once you've [created an instance](https://docs.cloud.google.com/managed-lustre/docs/create-instance), Google Cloud Managed Lustre lets you list, get, update, and delete instances.

## Instance states

A Managed Lustre instance can be in any of the following states:

State | Description  
---|---  
`CREATING` | The instance is being created and is not yet ready for use.  
`ACTIVE` | The instance is available for use.  
`REPAIRING` | The instance is being repaired.  
`MAINTENANCE` or `UPGRADING` | The instance is undergoing maintenance. See [Maintenance overview](https://docs.cloud.google.com/managed-lustre/docs/maintenance) for details.  
`SUSPENDED` | The instance is suspended, typically due to an issue with a customer-managed encryption key (CMEK).  
`DELETING` | The instance is being deleted.  
  
## List instances

To list all the instances in a project:

###  Google Cloud console 

  1. Go to the **Managed Lustre** page in the Google Cloud console.

[Go to Managed Lustre](https://console.cloud.google.com/managed-lustre/)

Your project's instances are listed.




###  gcloud CLI 

Use the [`gcloud lustre instances list`](https://docs.cloud.google.com/sdk/gcloud/reference/lustre/instances/list) command:
    
    
    gcloud lustre instances list --location=LOCATION
    

Replace LOCATION with a specific zone to list all instances in that location. To view projects in **all** locations, enter `-` as the value. For example:
    
    
    gcloud lustre instances list --location=-
    

###  REST 

To list instances using the REST API, send a request to the following endpoint:
    
    
    GET https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/instances
    Authorization: Bearer ACCESS_TOKEN
    

Where the following values must be specified:

  * PROJECT_ID is your Google Cloud project ID.

  * ZONE is the zone for which to list all instances. To list instances from all zones, use `-` as the value.




See the [`instances.list`](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/list) API reference for more details.

## Get an instance

To get an instance's details:

###  Google Cloud console 

  1. Go to the **Managed Lustre** page in the Google Cloud console.

[Go to Managed Lustre](https://console.cloud.google.com/managed-lustre/)

  2. Click the instance name to view details about a specific instance.




###  gcloud CLI 

Use the [`gcloud lustre instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/lustre/instances/describe) command:
    
    
    gcloud lustre instances describe INSTANCE_NAME --location=LOCATION
    

###  REST 

To get details about a particular instance using the REST API, send a request to the following endpoint:
    
    
    GET https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/instances/INSTANCE_NAME
    Authorization: Bearer ACCESS_TOKEN
    

Where the following values must be specified:

  * PROJECT_ID is your Google Cloud project ID.

  * ZONE must be a valid Google Cloud zone that is supported by Managed Lustre. See [Supported locations](https://docs.cloud.google.com/managed-lustre/docs/locations) for a full list.

  * INSTANCE_NAME is the name of the Managed Lustre instance to return.




See the [`instances.get`](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/get) API reference for more details.

## Update an instance

You can update the following properties of an existing instance:

  * Description
  * Labels
  * Storage capacity: see [Increase the capacity of an instance](https://docs.cloud.google.com/managed-lustre/docs/increase-capacity).
  * Maintenance policy: see [Configure maintenance policies](https://docs.cloud.google.com/managed-lustre/docs/maintenance-policies).
  * Target version for self-service maintenance: see [Perform self-service maintenance](https://docs.cloud.google.com/managed-lustre/docs/self-service-maintenance).
  * Combined capacity and version updates: see Updating capacity and version simultaneously.



To update an instance:

###  Google Cloud console 

  1. Go to the **Managed Lustre** page in the Google Cloud console.

[Go to Managed Lustre](https://console.cloud.google.com/managed-lustre/)

  2. Click the **Instance name** of the instance to update. The instance overview page is displayed.

  3. Click **Edit**.

  4. Enter the new value(s).

  5. Click **Submit**.




To perform self-service maintenance on an instance using the Google Cloud console, see [Perform self-service maintenance](https://docs.cloud.google.com/managed-lustre/docs/self-service-maintenance#perform_a_self-service_update).

###  gcloud CLI 

Use the [`gcloud lustre instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/lustre/instances/update) command:
    
    
    gcloud lustre instances update INSTANCE_NAME \
      --location=LOCATION \
      --capacity-gib=NEW_CAPACITY \
      --description=NEW_DESCRIPTION \
      --maintenance-policy-weekly-windows=dayOfWeek=DAY,startTime={START_TIME} \
      --target-version=TARGET_VERSION
    

Where:

  * INSTANCE_NAME is the instance to update.
  * LOCATION is the zone in which the instance resides.
  * NEW_CAPACITY is the new storage capacity for this instance in gibibytes (GiB). The value cannot exceed the maximum allowed capacity and must be a multiple of the step size. See [Increase the capacity of an instance](https://docs.cloud.google.com/managed-lustre/docs/increase-capacity) for more details.
  * NEW_DESCRIPTION is a new value for the description field, which overwrites any existing description.

  * DAY: The day of the week for the maintenance window (e.g., `TUESDAY`).

  * START_TIME: The UTC start time of the maintenance window in dictionary format (e.g., `{hours=1,minutes=0}`).

  * TARGET_VERSION: The target software version to upgrade to. For example, `Lustre_20260716.01_p00`, or `latest`. See [Perform self-service maintenance](https://docs.cloud.google.com/managed-lustre/docs/self-service-maintenance).




To update labels, see the available commands in the [gcloud lustre instances update](https://docs.cloud.google.com/sdk/gcloud/reference/lustre/instances/update#--labels) documentation.

###  REST 

To update an instance using the REST API, send a PATCH request to its specific endpoint:
    
    
    PATCH https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/instances/INSTANCE_NAME?updateMask=UPDATE_MASK
    Authorization: Bearer ACCESS_TOKEN
    
    {
      "capacityGib": 72000,
      "description": "updated description",
      "labels": {
        "key1": "value1"
      },
      "maintenancePolicy": {
        "weeklyMaintenanceWindows": [
          {
            "dayOfWeek": "DAY",
            "startTime": {
              "hours": HOURS,
              "minutes": MINUTES
            }
          }
        ]
      },
      "targetVersion": "latest"
    }
    

Where the following values must be specified:

  * PROJECT_ID is your Google Cloud project ID.
  * ZONE is the instance's Google Cloud zone.
  * INSTANCE_NAME is the name of the Managed Lustre instance to update.
  * UPDATE_MASK is a comma-separated list of fields to update. A field will only be overwritten if it is in the mask.



The request body must contain one or more of the following fields:

  * `capacityGiB` is the new storage capacity for this instance in gibibytes (GiB). The value cannot exceed the maximum allowed capacity and must be a multiple of the step size. See [Increase the capacity of an instance](https://docs.cloud.google.com/managed-lustre/docs/increase-capacity) for more details.
  * `description` is the new description for this instance.
  * `labels` is the new set of labels for this instance. The value of `labels` is a JSON object containing one or more key:value pairs.
  * `maintenancePolicy` is the maintenance policy for the instance. See [Configure maintenance policies](https://docs.cloud.google.com/managed-lustre/docs/maintenance-policies) for details.
  * `targetVersion` is the target software version for self-service maintenance. See [Perform self-service maintenance](https://docs.cloud.google.com/managed-lustre/docs/self-service-maintenance).



See the [`instances.patch`](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/patch) API reference for more details.

### Updating capacity and version simultaneously

You can update storage capacity and apply a software version upgrade in the same update request by specifying both the new capacity and the target version.

When you submit a combined update request, Managed Lustre processes the operations sequentially within a single long-running operation:

  1. The software version upgrade executes first.
  2. Capacity expansion executes second.



I/O operations pause only during the software version upgrade phase, typically lasting 15 to 20 minutes. Once the software upgrade completes, I/O operations resume automatically while capacity expansion finalizes.

While the update runs, the instance state transitions to `UPGRADING`. You can query the status of the long-running operation using gcloud CLI or the REST API:

###  gcloud CLI 

Run the [`gcloud lustre operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/lustre/operations/describe) command:
    
    
    gcloud lustre operations describe OPERATION_ID \
      --location=LOCATION

Where:

  * OPERATION_ID is the operation ID returned by the update request.
  * LOCATION is the zone in which the instance resides.



###  REST 

Send a `GET` request to the [`operations.get`](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.operations/get) endpoint:
    
    
    GET https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/operations/OPERATION_ID
    Authorization: Bearer ACCESS_TOKEN
    

Where:

  * PROJECT_ID is your Google Cloud project ID.
  * LOCATION is the zone in which the instance resides.
  * OPERATION_ID is the operation ID returned by the update request.



See the [`operations.get`](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.operations/get) API reference for more details.

When the operation completes successfully, the operation status reports `done: true` and the instance returns to `ACTIVE` state.

If a combined update request encounters an error, the resulting instance state depends on which operation failed:

  * If the software version upgrade fails, capacity expansion does not begin. The instance remains on its current software version with its original capacity in `ACTIVE` state, and the operation fails with the version update error.
  * If the software version upgrade succeeds but capacity expansion fails, such as due to quota limits or insufficient zone capacity, the operation fails and returns the capacity error, such as `RESOURCE_EXHAUSTED`. The software upgrade is not rolled back. The instance returns to `ACTIVE` state with the new software version applied and its existing storage capacity unchanged.



To verify the active software version and capacity after an operation has succeeded or failed, run the [`gcloud lustre instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/lustre/instances/describe) command and inspect `effectiveVersion` and `capacityGib`.

### Unable to queue operation

If you see an error similar to the following when attempting to update an instance:
    
    
    ERROR: (gcloud.lustre.instances.update) ABORTED: unable to queue the operation
    

This error occurs when you attempt to start an operation while another operation of the same type is already in progress on the same instance. Managed Lustre allows one active update per instance at a time, and allows an additional update operation to be queued.

To resolve this issue, wait for the current operation to complete before starting a new one.

## Delete an instance

To delete an instance:

###  Google Cloud console 

  1. Go to the **Managed Lustre** page in the Google Cloud console.

[Go to Managed Lustre](https://console.cloud.google.com/managed-lustre/)

  2. Select the three-dot menu next to the instance to delete.

  3. Select **Delete instance**. Confirm the deletion by clicking **Delete** again.




###  gcloud CLI 

Use the [`gcloud lustre instances delete`](https://docs.cloud.google.com/sdk/gcloud/reference/lustre/instances/delete) command:
    
    
    gcloud lustre instances delete INSTANCE_NAME --location=LOCATION
    

You are prompted to confirm deletion. Type `Y` or press enter to continue.

**Tip:** Specifying the `--quiet` or `-q` flag with the command skips the interactive confirmation requirement.

###  REST 

To delete an instance using the REST API, send a request to the following endpoint:
    
    
    DELETE https://lustre.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/instances/INSTANCE_NAME
    Authorization: Bearer ACCESS_TOKEN
    

Where the following values must be specified:

  * PROJECT_ID is your Google Cloud project ID.

  * ZONE is the Google Cloud zone in which the instance is located.

  * INSTANCE_NAME is the name of the Managed Lustre instance to delete.




See the [`instances.delete`](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.instances/delete) API reference for more details.

Delete requests are long-running requests, and return an operation ID that can be queried for operation status. See the [operations.get](https://docs.cloud.google.com/managed-lustre/docs/reference/rest/v1/projects.locations.operations/get) reference for details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
