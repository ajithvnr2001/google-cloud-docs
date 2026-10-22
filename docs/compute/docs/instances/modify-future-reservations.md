---
url: https://docs.cloud.google.com/compute/docs/instances/modify-future-reservations/
title: Modify future reservation requests \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:38.733717+00:00
---

# Modify future reservation requests  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/modify-future-reservations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Modify future reservation requests Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to modify future reservation requests.

You can modify a future reservation request any time before its start time, provided it hasn't been canceled or is not pending approval. Modifying a future reservation request is useful when your capacity needs change—for example, when you want to increase the number of reserved virtual machine (VM) instances or change the reservation period. If you want to modify a shared future reservation request, then you must modify the request using the owner project.

To modify an auto-created reservation after its reservation period has ended, see [Modify reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-modify).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permission that you need to modify future reservation requests, ask your administrator to grant you the [Compute Future Reservation Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.futureReservationAdmin) (`roles/compute.futureReservationAdmin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.futureReservations.update` permission, which is required to modify future reservation requests. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Modifiable properties

A future reservation request has several properties that define the reservation, determine its behavior, and specify the resources to reserve. You can modify these properties as described in the following sections.

### After creation

After creating a future reservation request, you can't modify the following properties:

  * The name of the future reservation request.

  * The project in which the future reservation request was created.

  * The zone where the future reservation request is located.

  * The instance template to use and the VM properties specified in the instance template.




To modify any of these properties before a future reservation request enters its lock time, create a new request.

### Before submission

Before submitting a future reservation request to Google Cloud for review, or after submitting a future reservation request for review and the request is declined, you can modify the following properties:

  * Auto-delete option

  * Description

  * GPUs and the GPU type

  * Local SSD disks and the disks interface type

  * Machine series and machine type

  * Minimum CPU platform

  * Name prefix

  * Share settings

  * Start and end time of the reservation period

  * Total count (Number of VMs)




Modifying a draft future reservation request state is immediate, and there are no limits to the number of times you can modify it. If you're modifying a declined (`DECLINED`) future reservation request, then you can only modify the request if you submit it again for review.

### After approval

After Google Cloud approves a future reservation, you can modify it before the future reservation reaches a procurement status of provisioning (`PROVISIONING`). Specifically, you can modify the following properties:

  * **By modifying the future reservation at any time** :

    * Auto-delete option

    * Description

    * Name prefix

  * **By submitting a[modification request](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#future-reservations-modification) no earlier than 72 hours before the start time**:

    * GPUs and the GPU type*

    * Local SSD disks and the disks interface type*

    * Machine series and machine type*

    * Minimum CPU platform*

    * Share settings

    * Start and end time of the reservation period

    * Total count (Number of VMs)*




* If you request to change any VM properties, or significantly increase or decrease the total count, within 14 days from the future reservation's start time, then Google Cloud is likely to decline your modification request.

## Modify future reservation requests

Before modifying a future reservation request, review the properties that you can modify, if you haven't already.

If you want to modify a single-project future reservation request created through an instance template into a shared future reservation request, then you can't use the same template to create VMs that can consume the auto-created reservations outside of the project that created the shared future reservation request. For the projects the future reservation is shared with, you must create similar instance templates in those projects or create VMs by specifying properties directly.

To modify a future reservation request, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click the **Future reservations** tab.

  3. In the **Name** column, click the name of the future reservation request that you want to modify.

The details page of the selected future reservation request opens.

  4. If you want to modify the auto-delete option, description, or name prefix of an approved future reservation, then do one or more of the following:

     * To modify the auto-delete option, in the **Auto-created reservations auto-delete time** row, click edit **Edit** , and then do the following:

       1. Specify if you want to enable, disable, or modify the auto-delete option by doing one of the following:

          * To enable the auto-delete option or change the time when Compute Engine automatically deletes the auto-created reservations, do the following:

            1. Click the **Enable auto-delete** toggle to the on position.

            2. Optional: For **Auto-delete time** , enter a new date and time when to delete the auto-created reservations. The date and time must be after the end time of the reservation period. If you leave this field empty, then the auto-created reservations are deleted within two hours after the reservation period's end time.

          * Otherwise, click the **Enable auto-delete** toggle to the off position.

       2. Click **Submit**.

     * To modify the name prefix, in the **Prefix** row, click edit **Edit** , and then do the following:

       1. For **Prefix** , enter a new name prefix.

       2. Click **Submit**.

     * To modify the description, in the **Description** row, click edit **Edit** , and then do the following:

       1. For **Description** , enter a new description.

       2. Click **Submit**.

  5. Click edit **Edit** or edit **Edit draft**.

The page to edit the selected future reservation request opens.

  6. To modify a future reservation request and submit it to Google Cloud for review, or save the draft request, do one or more of the following:

     * For **Prefix** , enter a new name prefix for the auto-created reservations provisioned for this future reservation request.

     * For **Description** , enter a new description.

     * Modify the **Start time** or **End time** for your future reservation request. Make sure of the following:

       * The start time can't be later than one year from the date and time at which you submit a future reservation request for review.

       * Specify a [recommended value for the start time](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#recommended-start-time) to help ensure that you have sufficient time before your future reservation enters its lock time.

       * Specify a [recommended minimum reservation period](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#recommended-minimum-reservation-period) to increase the likelihood that Google Cloud approves your request after submitting it for review.

     * In the **Share type** section, you can select either **Local** or **Shared**. If you select **Shared** , you can add or remove projects to share the future reservation request with. You can include up to 100 projects.

     * For **Number of VM instances** , enter the total count of VMs that you want reserved.

**Caution:** If you want to increase the number of VMs to reserve, then verify that you have sufficient quota for the additional resources that you're requesting to reserve. Otherwise, Google Cloud declines your modification request.
     * If you're modifying a future reservation that wasn't created through an instance template, then, in the **Machine configuration** section, you can change the following:

       * The machine series and machine type used in the reserved VMs.

       * The GPUs to attach to the reserved VMs.

       * The Local SSD disks and the disk interface type of the reserved VMs.

     * In the **Auto-generated reservations auto-delete** section, you can enable or disable the automatic deletion of auto-created reservations for your future reservation request.

  7. Depending on the procurement status of the future reservation request that you're modifying, do one of the following:

     * If you're modifying a draft future reservation request, then do one of the following:

       * To save your changes, click **Save draft**.

       * To submit the draft future reservation request to Google Cloud for review, click **Submit**.

     * Otherwise, click **Submit**.




If you submit a modification request, then the **Reservations** page opens. Otherwise, the details page of the future reservation opens.

###  gcloud 

To modify a future reservation request, use the [`gcloud compute future-reservations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/update).
    
    
    gcloud compute future-reservations update FUTURE_RESERVATION_NAME \
        --accelerator=count=NUMBER_OF_ACCELERATORS,type=ACCELERATOR_TYPE \
        --description="DESCRIPTION" \
        --local-ssd=size=375,interface=INTERFACE \
        --machine-type=MACHINE_TYPE \
        --min-cpu-platform=MIN_CPU_PLATFORM \
        --name-prefix=NAME_PREFIX \
        --planning-status=PLANNING_STATUS \
        --share-setting=SHARE_SETTING \
        --share-with=CONSUMER_PROJECT_IDS \
        --start-time=START_TIME \
        --end-time=END_TIME \
        --total-count=TOTAL_COUNT \
        --zone=ZONE
    

Replace the following:

  * `FUTURE_RESERVATION_NAME`: the name of the future reservation request.

  * `PLANNING_STATUS`: the planning status of the future reservation request. Specify one of the following values:

    * To modify a draft future reservation request without submitting it for review: `DRAFT`.

    * To submit the future reservation request for review: `SUBMITTED`.

  * `ZONE`: the zone where the future reservation request is located.




Replace one or more of the following placeholders, or remove them along with their corresponding flags:

  * To enable Compute Engine to automatically delete the auto-created reservations after the end time of the reservation period, do one of the following:

    * To delete the reservations within two hours after the end time (default), include the `--auto-delete-auto-created-reservations` flag.
          
          gcloud compute future-reservations update FUTURE_RESERVATION_NAME \
              **--auto-delete-auto-created-reservations** \
              --planning-status=PLANNING_STATUS \
              --zone=ZONE
          

    * To delete the auto-created reservations at a specific time after the end time of the reservation period, include the `--auto-delete-auto-created-reservations` and `--auto-created-reservations-delete-time` flags.
          
          gcloud compute future-reservations update FUTURE_RESERVATION_NAME \
              **--auto-created-reservations-delete-time= AUTO_CREATED_RESERVATIONS_DELETE_TIME** \
              **--auto-delete-auto-created-reservations** \
              --planning-status=PLANNING_STATUS \
              --zone=ZONE
          

Replace `AUTO_CREATED_RESERVATIONS_DELETE_TIME` with a date and time formatted as an [RFC 3339 timestamp](https://tools.ietf.org/html/rfc3339).

    * To delete the auto-created reservations after a specific duration after the end time of the reservation period, include the `--auto-delete-auto-created-reservations` and `--auto-created-reservations-duration` flags.
          
          gcloud compute future-reservations update FUTURE_RESERVATION_NAME \
              **--auto-created-reservations-duration= DURATION_BEFORE_DELETE** \
              **--auto-delete-auto-created-reservations** \
              --planning-status=PLANNING_STATUS \
              --zone=ZONE
          

Replace `DURATION_BEFORE_DELETE` with a duration in days, hours, minutes, or seconds. For example, specify `30m` for 30 minutes, or `1d2h3m4s` for 1 day, 2 hours, 3 minutes, and 4 seconds.

  * To disable Compute Engine from automatically deleting the auto-created reservations provisioned for this future reservation request, include the `--no-auto-delete-auto-created-reservations` flag.
        
        gcloud compute future-reservations update FUTURE_RESERVATION_NAME \
            **--no-auto-delete-auto-created-reservations** \
            --planning-status=PLANNING_STATUS \
            --zone=ZONE
        

  * To add or remove GPUs attached to reserved N1 VMs, or update the GPU type, do one of the following:

    * To change the number and type of GPUs, replace the following:

      * `NUMBER_OF_ACCELERATORS`: the number of GPUs to add per reserved VM.

      * `ACCELERATOR_TYPE`: the type of GPU to add to the reserved VMs. Verify that [the GPU is available in the zone](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones) where the future reservation request is located. Otherwise, modifying the request fails.

    * To remove all GPUs attached to reserved N1 VMs, replace the `--accelerator` flag with the `--clear-accelerator` flag.

  * `DESCRIPTION`: A new description for your future reservation request.

  * To add or remove Local SSD disks from your reserved VMs, or edit the Local SSD disk interface type, do one of the following:

    * To add Local SSD disks or edit the disk interface type, replace the `INTERFACE` with one of the following values:

      * If your boot disk image [has optimized NVMe drivers](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface): `nvme`.

      * Otherwise: `scsi`.

Include the `--local-ssd` flag for as many Local SSD disks that you want to add. You can specify a maximum of 24 Local SSD disks.

    * To remove all Local SSD disks attached to the reserved VMs, remove all `--local-ssd` flags and include the `--clear-local-ssd` flag.

  * `MACHINE_TYPE`: The new machine type to use for each reserved VM. If you change the machine type, then also specify a [recommended minimum reservation period](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#recommended-minimum-reservation-period) for the new machine series. Otherwise, Google Cloud is likely to decline your modification request.

  * `MINIMUM_CPU_PLATFORM`: A new minimum CPU platform to use for each reserved VM.

  * `NAME_PREFIX`: A new name prefix for the auto-created reservations provisioned for your future reservation request.

  * `SHARE_SETTING`: A new share type for your future reservation request. Specify one of the following values:

    * For a single-project future reservation request: `local`. To avoid errors, you must also replace the `--share-with` flag with the `--clear-share-settings` flag.

    * For a shared future reservation request: `projects`. To avoid errors, you must also specify at least one consumer project in the `--share-with` flag.

  * `CONSUMER_PROJECT_IDS`: A comma-separated list of IDs of projects that you want to share your future reservation request with—for example, `project-1,project-2`. You can specify up to 100 consumer projects.

  * `START_TIME`: The new start time of the reservation period formatted as an [RFC 3339 timestamp](https://tools.ietf.org/html/rfc3339). The start time can't be later than one year from the date and time at which you submit the modification request for review. To have sufficient time to optionally cancel, delete, or modify a future reservation after it's approved and before it enters its lock time, specify a [recommended start time](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#recommended-start-time).

  * `END_TIME`: The new end time of the reservation period formatted as an RFC 3339 timestamp. To increase the likelihood that Google Cloud approves your request after submission, specify a [recommended minimum reservation period](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#recommended-minimum-reservation-period). To specify a duration instead of an end time, replace the `--end-time` flag with the `--duration=END_DURATION` flag. Replace `END_DURATION` with the duration of the reservation period in seconds. For example, specify `1209600` for 1,209,600 seconds (14 days).

**Important:** Verify that your reservation period doesn't overlap with the reservation period of another existing future reservation request with matching VM properties and zone, and that was created in or is shared with your current project. Otherwise, modifying the future reservation request fails.
  * `TOTAL_COUNT`: The new total number of VMs that you want reserved for the period, VM configuration, and project(s) specified in your future reservation request. If you want to increase the total count, than verify that you have sufficient quota for the resources that you're reserving. Otherwise, Google Cloud declines your modification request.




For example, consider a draft shared future reservation request named `fr-03` and located in zone `us-central1-a`. Suppose that you want to modify this shared future reservation request by making the following changes:

  * Convert the request into a single-project future reservation request.

  * Disable the auto-delete option.

  * Reserve 100 VMs.

  * Submit the future reservation request to Google Cloud for review.




To modify `fr-03`, run the following command:
    
    
    gcloud compute future-reservations update fr-03 \
        --clear-share-settings \
        --no-auto-delete-auto-created-reservations \
        --planning-status=SUBMITTED \
        --share-setting=local \
        --total-count=100 \
        --zone=us-central1-a
    

###  REST 

To modify a future reservation request, make a `PATCH` request to the [`futureReservations.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/update).
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations/FUTURE_RESERVATION_NAME?updateMask=UPDATE_FIELDS
    
    {
      "autoDeleteAutoCreatedReservations": "AUTO_DELETE_AUTO_CREATED_RESERVATIONS",
      "description": "DESCRIPTION",
      "name": "FUTURE_RESERVATION_NAME",
      "namePrefix": "NAME_PREFIX",
      "planningStatus": "PLANNING_STATUS",
      "shareSettings": {
        "projects": [
          "CONSUMER_PROJECT_ID_1",
          "CONSUMER_PROJECT_ID_2"
        ],
        "shareType": "SHARE_TYPE"
      },
      "specificSkuProperties": {
        "instanceProperties": {
          "guestAccelerators": [
            {
              "acceleratorCount": NUMBER_OF_ACCELERATORS,
              "acceleratorType": "ACCELERATOR_TYPE"
            }
          ],
          "localSsds": [
            {
              "diskSizeGb": "375",
              "interface": "INTERFACE_1"
            },
            {
              "diskSizeGb": "375",
              "interface": "INTERFACE_2"
            }
          ],
          "machineType": "MACHINE_TYPE",
          "minCpuPlatform": "MINIMUM_CPU_PLATFORM"
        },
        "totalCount": "TOTAL_COUNT"
      },
      "timeWindow": {
        "endTime": "END_TIME",
        "startTime": "START_TIME"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the future reservation request is located.

  * `ZONE`: the zone where the future reservation request is located.

  * `FUTURE_RESERVATION_NAME`: the name of the future reservation request.

  * `UPDATE_FIELDS`: a comma-separated list of fields to update in the request body. You must encode each comma as `%2C`. If you specify a field in the `updateMask` query parameter and in the request body, then this updates the value of the field. Otherwise, if you specify the field only in the `updateMask` query parameter, then this deletes the field.

For example, to update the `autoDeleteAutoCreatedReservations`, `totalCount`, and `endTime` fields in your future reservation request, specify the following:
        
        autoDeleteAutoCreatedReservations**%2C** specificSkuProperties.totalCount**%2C** timeWindow.endTime
        

  * `PLANNING_STATUS`: the planning status of the future reservation request. Specify one of the following values:

    * To modify a draft future reservation request without submitting it for review: `DRAFT`.

    * To submit the modification request for review: `SUBMITTED`.




Replace one or more of the following placeholders, or remove them along with their corresponding fields:

  * `AUTO_DELETE_AUTO_CREATED_RESERVATIONS`: If you set this field to `true`, then Compute Engine automatically deletes the auto-created reservations provisioned for your future reservation request. By default, the deletion is within two hours after the reservation period's end time. To change this, do one of the following:

    * To delete the auto-created reservations at a specific time after the end time of your reservation period, set the `autoDeleteAutoCreatedReservations` to `true` and specify the `autoCreatedReservationsDeleteTime` field.
          
          PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations/FUTURE_RESERVATION_NAME?updateMask=autoDeleteAutoCreatedReservations**%2C** autoCreatedReservationsDeleteTime**%2C** planningStatus
          
          {
            **"autoDeleteAutoCreatedReservations": "true",
            "autoCreatedReservationsDeleteTime": " DELETE_TIME"**,
            "name": "FUTURE_RESERVATION_NAME",
            "planningStatus": "PLANNING_STATUS"
          }
          

Replace `DELETE_TIME` with a date and time when Compute Engine deletes reservations. The date and time must be formatted as an [RFC 3339 timestamp](https://tools.ietf.org/html/rfc3339).

    * To delete the auto-created reservations after a specific duration from the start time of the reservation period, set the `autoDeleteAutoCreatedReservations` to `true` and specify the `autoCreatedReservationsDuration` field.
          
          PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations/FUTURE_RESERVATION_NAME?updateMask=autoDeleteAutoCreatedReservations**%2C** autoCreatedReservationsDuration**%2C** planningStatus
          
          {
            **"autoDeleteAutoCreatedReservations": "true",
            "autoCreatedReservationsDuration": {
              "seconds": " DURATION_BEFORE_DELETE"
            }**,
            "name": "FUTURE_RESERVATION_NAME",
            "planningStatus": "PLANNING_STATUS"
          }
          

Replace `DURATION_BEFORE_DELETE` with a duration in seconds. For example, specify `604800` for 604,800 seconds (7 days).

  * `DESCRIPTION`: A new description for the future reservation request.

  * `NAME_PREFIX`: A new name prefix for the auto-created reservations provisioned for your future reservation request.

  * `CONSUMER_PROJECT_ID_1` and `CONSUMER_PROJECT_ID_2`: The IDs of projects that you want to share your future reservation request with. The projects must be in the same organization as the owner project. You can specify up to 100 consumer projects.

  * `SHARE_TYPE`: A new share type for your future reservation request. Do one of the following:

    * To specify a single-project future reservation request, do the following:

      * Specify `LOCAL`.

      * Remove the `shareSettings.projects` field.

    * To specify a shared future reservation request, do the following:

      * Specify `SPECIFIC_PROJECTS`.

      * Specify at least one consumer project in the `shareSettings.projects` field. The consumer projects must be in the same organization as the owner project. You can specify up to 100 consumer projects.

  * To change the number and type of GPUs to attach to your reserved N1 VMs, replace the following:

    * `NUMBER_OF_ACCELERATORS`: the number of GPUs to add per reserved VM.

    * `ACCELERATOR_TYPE`: the type of GPU to add to the reserved VMs. Verify that [the GPU is available in the zone](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones) where the future reservation request is located. Otherwise, modifying the request fails.

  * `INTERFACE_1` and `INTERFACE_2`: The type of disk interface type for the Local SSD disks attached to each reserved VM. Specify one of the following values:

    * If your boot disk image [has optimized NVMe drivers](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface): `NVME`.

    * Otherwise: `SCSI`.

You can specify a maximum of 24 Local SSD disks.

  * `MACHINE_TYPE`: The new machine type to use for each reserved VM. If you change the machine type, then also specify a [recommended minimum reservation period](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#recommended-minimum-reservation-period). for the new machine series. Otherwise, Google Cloud is less likely to approve your modification request.

  * `MINIMUM_CPU_PLATFORM`: A new minimum CPU platform to use for each reserved VM.

  * `TOTAL_COUNT`: The new total number of VMs that you want reserved for the period, VM configuration, and project(s) specified in this future reservation request. If you want to increase the total count, than verify that you have sufficient quota for the resources that you're reserving. Otherwise, Google Cloud declines your modification request.

  * `START_TIME`: The new start time of the reservation period formatted as an [RFC 3339 timestamp](https://tools.ietf.org/html/rfc3339). The start time can't be later than one year from the date and time at which you submit the modification request for review. To have sufficient time to optionally cancel, delete, or modify a future reservation after it's approved and before it enters its lock time, specify a [recommended start time](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#recommended-start-time).

  * `END_TIME`: The new end time of the reservation period formatted as an RFC 3339 timestamp. To increase the likelihood that Google Cloud approves your request after submission, specify a [minimum reservation period](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#recommended-minimum-reservation-period). To specify a duration instead of an end time, replace the `endTime` field with the `duration` field:
        
        PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations/FUTURE_RESERVATION_NAME?updateMask=timeWindow.duration**%2C** planningStatus
        
        {
          "name": "FUTURE_RESERVATION_NAME",
          "planningStatus": "PLANNING_STATUS",
          "timeWindow": {
            **"duration": {
              "seconds": " END_DURATION"
            }**
          }
        }
        

Replace `END_DURATION` with a duration in seconds. For example, specify `1209600` for 1,209,600 seconds (14 days).

**Important:** Verify that your reservation period doesn't overlap with the reservation period of another existing future reservation request with matching VM properties and zone, and that was created in or is shared with your current project. Otherwise, modifying the future reservation request fails.



For example, consider a draft shared future reservation request named `fr-03` and located in zone `us-central1-a`. Suppose that you want to modify this shared future reservation request by making the following changes:

  * Convert the request into a single-project future reservation request.

  * Disable the auto-delete option.

  * Reserve 100 VMs.

  * Submit the future reservation request to Google Cloud for review.




To modify `fr-03`, make a `PATCH` request as follows:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/futureReservations/fr-03?updateMask=autoDeleteAutoCreatedReservations%2CplanningStatus%2CshareSettings.shareType%2CspecificSkuProperties.totalCount
    
    {
      "autoDeleteAutoCreatedReservations": false,
      "name": "fr-03",
      "planningStatus": "SUBMITTED",
      "shareSettings": {
        "shareType": "LOCAL"
      },
      "specificSkuProperties": {
        "totalCount": "100"
      }
    }
    

After modifying a future reservation request, you can monitor its procurement or update statuses by [viewing the details of the future reservation request](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-future-reservations).

## Change other properties in a future reservation request

To change properties that you can't modify [after creating a future reservation request](https://docs.cloud.google.com/compute/docs/instances/modify-future-reservations#after-creation), and before the request is approved and enters its lock time, do the following:

  1. To stop the future reservation request from restricting the type of future reservation requests that you can create in your project, or in the projects that the future reservation request is shared with, [delete the future reservation request](https://docs.cloud.google.com/compute/docs/instances/delete-future-reservations).

  2. Create a new [single-project](https://docs.cloud.google.com/compute/docs/instances/create-single-project-future-reservations) or [shared future reservation request](https://docs.cloud.google.com/compute/docs/instances/create-shared-future-reservations) with the updates that you want.




## Troubleshoot

If you run into errors when modifying a future reservation request, then see how to [troubleshoot future reservation requests](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshoot-future-reservations).

If you still encounter issues after troubleshooting, then contact your account representative or [Google Cloud Support](https://cloud.google.com/contact).

## What's next

  * Learn how to [view future reservation requests](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view-future-reservations).

  * Learn how to [cancel or delete future reservation requests](https://docs.cloud.google.com/compute/docs/instances/delete-future-reservations).

  * After a reservation period's start time, learn how to [consume the auto-created reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_any_matching_reservation).

  * After a reservation period's end time, learn how to [modify the auto-created reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-modify).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
