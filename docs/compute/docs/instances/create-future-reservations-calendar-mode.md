---
url: https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode/
title: Create a future reservation request in calendar mode \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:26.007089+00:00
---

# Create a future reservation request in calendar mode  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a future reservation request in calendar mode Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create a future reservation request in calendar mode to reserve GPU, H4D, or TPU resources for your virtual machine (VM) instances. Use these requests to obtain high-demand resources for creating VMs that you plan to run for up to 90 days.

You can use future reservation requests in calendar mode to reserve resources to run the following workloads:

  * Model pre-training jobs

  * Model fine-tuning jobs

  * High performance computing (HPC) simulation workloads

  * Short-term increases in inference workloads




After Google Cloud approves your request, your reserved resources become available for you to create GPU, H4D, or TPU VMs on your specified delivery date and time. For the duration of your reservation period, only your project, and any projects that you specify when you create the request, have access to the reserved resources. You can share the reserved resources with up to 100 projects that are within the same organization as your project. To learn more about the requirements and limitations that you apply when you create a request in calendar mode, see [About future reservation requests in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview).

**Important:** You can reserve up to 80 GPU VMs or 256 H4D VMs in a single request in calendar mode. To reserve more than the maximum number of VMs or to reserve the resources for longer than 90 days, contact your [account team](https://cloud.google.com/tam) or the [sales team](https://cloud.google.com/contact).

## Before you begin

  * If you can't use future reservation requests in calendar mode, then you might not be eligible to access and use this feature. In this case, contact your [account team](https://cloud.google.com/tam) or the [sales team](https://cloud.google.com/contact).
  * To reserve H4D VMs, you must have sufficient [CPU quota](https://docs.cloud.google.com/compute/resource-usage#cpu_quota). Otherwise, reserving resources fails. Quota isn't required for reserving GPU or TPU VMs. 
  * To share your reserved capacity with other projects within your organization, verify that the project in which you want to create future reservation requests in calendar mode is [ allowed to create shared reservations](https://docs.cloud.google.com/compute/docs/instances/manage-shared-reservations-creation). Otherwise, you will encounter errors. 
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

To get the permissions that you need to create a future reservation request in calendar mode, ask your administrator to grant you the [Compute Future Reservation User ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.futureReservationUser) (`roles/compute.futureReservationUser`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a future reservation request in calendar mode. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a future reservation request in calendar mode:

  * To create a future reservation request: `compute.futureReservations.create` on the project 
  * To let Compute Engine automatically create reservations: `compute.reservations.create` on the project 
  * To view the availability of resources on a future date: `compute.advice.calendarMode` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a future reservation request in calendar mode

To create a future reservation request in calendar mode, complete the following steps:

  1. **View resource future availability**. View future availability for the GPU VMs, H4D VMs, or TPUs that you want to reserve. Then, when you create a request, specify the number, type, and reservation duration of the resources that you confirmed as available. Google Cloud is more likely to approve your request if you supply this information.

**Note:** If you create a request by using the Google Cloud console, then skip this step. You can view GPU VM, H4D VM, or TPU future availability while you create the request.

For instructions, see View resource future availability.

  2. **Create a reservation request**. Create and submit a future reservation request in calendar mode for GPU VMs, H4D VMs, or TPUs. If you can successfully create a request, then Google Cloud approves it within a minute.

For instructions, see Create a request for GPU VMs, H4D VMs, or TPUs.




### View resource future availability

You can view future availability for GPU VMs, H4D VMs, or TPUs in a region as follows:

  * For GPU or H4D VMs, up to 60 days in advance

  * For TPUs, up to 120 days in advance




To view GPU VM, H4D VM, or TPU future availability in a region, select one of the following options:

###  Console 

You can view GPU VM, H4D VM, or TPU future availability in a region when you create a future reservation request in calendar mode. For more information, see Create a request for GPU VMs, H4D VMs, or TPUs in this document.

###  gcloud 

To view GPU VM, H4D VM, or TPU future availability in a region, use the [`gcloud compute advice calendar-mode` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/advice/calendar-mode). Based on the resources that you want to view, include the following flags:

  * To view GPU VM or H4D VM availability, include the `--vm-count` and `--machine-type` flags:
        
        gcloud compute advice calendar-mode \
            **--vm-count= NUMBER_OF_VMS** \
            **--machine-type= MACHINE_TYPE** \
            --region=REGION \
            --start-time-range=from=FROM_START_TIME,to=TO_START_TIME \
            --duration-range=min=MIN_DURATION,max=MAX_DURATION
        

  * To view TPU availability, include the `--chip-count` and `--tpu-version` flags:
        
        gcloud compute advice calendar-mode \
            **--chip-count= NUMBER_OF_CHIPS** \
            **--tpu-version= TPU_VERSION** \
            --region=REGION \
            --start-time-range=from=FROM_START_TIME,to=TO_START_TIME \
            --duration-range=min=MIN_DURATION,max=MAX_DURATION
        




Replace the following:

  * `NUMBER_OF_VMS`: the number of VMs to reserve. The value must be at least `1` and no greater than `80` for GPU VMs or `256` for H4D VMs.

  * `MACHINE_TYPE`: the GPU or H4D machine type to reserve. Specify one of the following values:

    * For A4 machine types, specify `a4-highgpu-8g`.

    * For A3 Ultra machine types, specify `a3-ultragpu-8g`.

    * For A3 Mega machine types, specify `a3-megagpu-8g`.

    * For A3 High machine types with 8 GPUs, specify `a3-highgpu-8g`.

    * For H4D HPC machine types, see [H4D machine types](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_machine_types).

  * `NUMBER_OF_CHIPS`: the number of TPU chips to reserve. The value must be `1`, `4`, `8`, `16`, `32`, `64`, `128`, `256`, `512`, or `1024`.

  * `TPU_VERSION`: the TPU version to reserve. Specify one of the following values:

    * For TPU7x: `TPU7X`

    * For TPU v6e: `V6E`

    * For TPU v5p: `V5P`

  * `REGION`: the region where to reserve GPU VMs, H4D VMs, or TPUs. To check which regions and zones are supported, see [Limitations](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview#limitations).

  * `FROM_START_TIME` and `TO_START_TIME`: the earliest and latest dates that you want to reserve capacity on. Format these dates as RFC 3339 timestamps:
        
        YYYY-MM-DD**T** HH:MM:SSOFFSET
        

Replace the following:

    * `YYYY-MM-DD`: a date formatted as a four-digit year, two-digit month, and a two-digit day, separated by hyphens (`-`).

    * `HH:MM:SS`: a time formatted as a two-digit hour using a 24-hour time, two-digit minutes, and two-digit seconds, separated by colons (`:`).

    * `OFFSET`: the time zone formatted as an offset of [Coordinated Universal Time (UTC)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). For example, to use the Pacific Standard Time (PST), specify `-08:00`. To use no offset, specify `Z`.

  * `MIN_DURATION` and `MAX_DURATION`: the minimum and maximum amount of time that you want to reserve resources for. You must format these values as the number of days, hours, minutes, or seconds followed by `d`, `h`, `m`, and `s` respectively. For example, specify `24h` for 24 hours or `1d2h3m4s` for one day, two hours, three minutes, and four seconds.




The output is similar to the following:
    
    
    - recommendationsPerSpec:
        spec:
          **endTime: '2026-02-10T00:00:00Z'**
          **location: zones/us-central1-a**
          otherLocations:
            zones/us-central1-b:
              details: Recommendation in this zone is possible.
              status: RECOMMENDED
            zones/us-central1-c:
              details: Temporarily no free capacity in this zone in the
              requested time window.
              status: NO_CAPACITY
            zones/us-central1-f:
              details: This machine family is not supported in this zone.
              status: NOT_SUPPORTED
          recommendationId: 0d3f005d-f952-4fce-96f2-6af25e1591eb
          recommendationType: FUTURE_RESERVATION
          **startTime: '2026-02-07T00:00:00Z'**
    

If your requested resources are available, then the output contains the `startTime`, `endTime`, and `location` fields. These fields specify the earliest start time, the latest end time, and the zones when resources are available.

###  REST 

To view GPU VM, H4D VM, or TPU future availability in a region, make a `GET` request to the [`advice.calendarMode` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/advice/calendarMode). Based on the resources that you want to view, include the following fields in the request body:

  * To view GPU VM or H4D VM availability, include the `instanceCount` and `machineType` fields:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/advice/calendarMode
        
        {
          "futureResourcesSpecs": {
            "spec": {
              "targetResources": {
                "specificSkuResources": {
                  **"instanceCount": " NUMBER_OF_VMS"**,
                  **"machineType": " MACHINE_TYPE"**
                }
              },
              "timeRangeSpec": {
                "startTimeNotEarlierThan": "FROM_START_TIME",
                "startTimeNotLaterThan": "TO_START_TIME",
                "minDuration": "MIN_DURATION",
                "maxDuration": "MAX_DURATION"
              }
            }
          }
        }
        

  * To view TPU availability, include the `acceleratorCount` and `vmFamily` fields:
        
        POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION/advice/calendarMode
        
        {
          "futureResourcesSpecs": {
            "spec": {
              "targetResources": {
                "aggregateResources": {
                  **"acceleratorCount": " NUMBER_OF_CHIPS"**,
                  **"vmFamily": " TPU_VERSION"**
                }
              },
              "timeRangeSpec": {
                "startTimeNotEarlierThan": "FROM_START_TIME",
                "startTimeNotLaterThan": "TO_START_TIME",
                "minDuration": "MIN_DURATION",
                "maxDuration": "MAX_DURATION"
              }
            }
          }
        }
        




Replace the following:

  * `PROJECT_ID`: the ID of the project where you want to reserve resources.

  * `REGION`: the region where you want to reserve GPU VMs, H4D VMs, or TPUs. To check the regions and zones that are supported, see [Limitations](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview#limitations).

  * `NUMBER_OF_VMS`: the number of GPU or H4D VMs to reserve. For GPU VMs, the value must be between `1` and `80`. For H4D VMs, the value must be between `1` and `256`.

  * `MACHINE_TYPE`: the GPU or H4D machine type to reserve. Specify one of the following values:

    * For A4 machine types, specify `a4-highgpu-8g`.

    * For A3 Ultra machine types, specify `a3-ultragpu-8g`.

    * For A3 Mega machine types, specify `a3-megagpu-8g`.

    * For A3 High machine types with 8 GPUs, specify `a3-highgpu-8g`.

    * For H4D HPC machine types, see [H4D machine types](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_machine_types).

  * `NUMBER_OF_CHIPS`: the number of TPU chips to reserve. The value must be `1`, `4`, `8`, `16`, `32`, `64`, `128`, `256`, `512`, or `1024`.

  * `TPU_VERSION`: the TPU version to reserve. Specify one of the following values:

    * For TPU7x: `VM_FAMILY_CLOUD_TPU_POD_SLICE_TPU7X`

    * For TPU v6e: `VM_FAMILY_CLOUD_TPU_LITE_POD_SLICE_CT6E`

    * For TPU v5p: `VM_FAMILY_CLOUD_TPU_POD_SLICE_CT5P`

  * `FROM_START_TIME` and `TO_START_TIME`: the earliest and latest dates that you want to reserve capacity on. Format these dates as RFC 3339 timestamps:
        
        YYYY-MM-DD**T** HH:MM:SSOFFSET
        

Replace the following:

    * `YYYY-MM-DD`: a date formatted as a 4-digit year, 2-digit month, and a 2-digit day, separated by hyphens (`-`).

    * `HH:MM:SS`: a time formatted as a 2-digit hour using a 24-hour time, 2-digit minutes, and 2-digit seconds, separated by colons (`:`).

    * `OFFSET`: the time zone formatted as an offset of [Coordinated Universal Time (UTC)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). For example, to use the Pacific Standard Time (PST), specify `-08:00`. To use no offset, specify `Z`.

  * `MIN_DURATION` and `MAX_DURATION`: the minimum and maximum amount of time, in seconds, that you want to reserve resources for. You must format these values as the number of seconds, followed by `s`. For example, specify `86400s` for 86,400 seconds (24 hours).




The output is similar to the following:
    
    
    {
      "recommendations": [
        {
          "recommendationsPerSpec": {
            "spec": {
              "recommendationId": "a21a2fa0-72c7-4105-8179-88de5409890b",
              "recommendationType": "FUTURE_RESERVATION",
              **"startTime": "2026-02-07T00:00:00Z"** ,
              **"endTime": "2026-02-10T00:00:00Z"** ,
              "otherLocations": {
                "zones/us-central1-b": {
                  "status": "RECOMMENDED",
                  "details": "Recommendation in this zone is possible."
                },
                "zones/us-central1-c": {
                  "status": "NO_CAPACITY",
                  "details": "Temporarily no free capacity in this zone in the
                              requested time window."
                },
                "zones/us-central1-f": {
                  "status": "NOT_SUPPORTED",
                  "details": "This machine family is not supported in this zone."
                }
              },
              **"location": "zones/us-central1-a"**
            }
          }
        }
      ]
    }
    

If your requested resources are available, then the output contains the `startTime`, `endTime`, and `location` fields. These fields specify the earliest start time, the latest end time, and the zones when resources are available.

### Create a request for GPU VMs, H4D VMs, or TPUs

When you create a future reservation request in calendar mode, you must specify a reservation period as follows:

  * **Start time** : based on the resources that you want to reserve, you must specify a start time that is at least one of the following values from when you create and submit a request:

    * For GPU and H4D VMs, 87 hours (3 days and 15 hours)

    * For TPUs, 6 hours

  * **Duration** : you can reserve resources for a minimum of 24 hours and a maximum of 90 days.




To create a request by using an existing GPU or H4D VM as reference, use the Google Cloud console. Otherwise, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click the **Future reservations** tab.

  3. Click add_box **Create future reservation**. The **Create a future reservation** page appears and the **Hardware configuration** pane is selected.

  4. In the **Configurations** section, specify the properties of the GPU VMs, H4D VMs, or TPUs that you want to reserve by doing one of the following:

     * To specify GPU VM, H4D VM, or TPU properties directly, complete the following steps:

       1. Select **Specify machine type**.

       2. Click the **GPUs** , **TPUs** , or **Compute-optimized** tab, and then select a [supported](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview#limitations) GPU machine type, H4D machine type, or TPU version.

     * To specify GPU or H4D VM properties by using an existing VM as reference, select **Use existing VM** , and then select the VM.

  5. In the **Search for capacity** section, complete the following steps:

     1. In the **Region** and **Zone** lists, select the region and zone where you want to reserve resources.

     2. In the **Total capacity needed** field (when reserving GPU or H4D VMs) or **Number of chips** list (when reserving TPUs), specify the number of GPU VMs, H4D VMs, or TPU chips to reserve. You can specify the following values:

        * For GPU VMs, a value between `1` and `80`

        * For H4D VMs, a value between `1` and `256`

        * For TPU chips, a value of `1`, `4`, `8`, `16`, `32`, `64`, `128`, `256`, `512`, or `1024`

     3. In the **Start time** list, select the start time for your request.

     4. Optional: In the **Choose your start date flexibility** list, select how exact your start date needs to be.

     5. In the **Reservation duration** field, specify for how long you want to reserve resources.

     6. Click **Search for capacity**. Then, in the **Available capacity** table, select one of the available options that contain the type, number, and reservation period of the GPU VMs, H4D VMs, or TPUs to reserve.

  6. Click **Next**.

  7. In the **Share type** section, select the projects to share your reserved capacity with:

     * To use the reserved capacity only within your project, select **Local**.

     * To share the reserved capacity with other projects, select **Shared** , click add **Add projects** , and then follow the prompts to select the projects that you want to share the reserved capacity with.

  8. Click **Next**.

  9. In the **Future reservation name** field, enter a name for the request.

  10. In the **Reservation name** field, enter the name of the reservation that Compute Engine automatically creates to provision your requested capacity.

  11. Click **Create**.




###  gcloud 

To create a future reservation request in calendar mode and submit it for review, use the [`gcloud compute future-reservations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/create). Based on the resources that you want to reserve, include the following flags:

  * To reserve GPU or H4D VMs, include the `--total-count`, `--machine-type`, and `--deployment-type=DENSE` flags:
        
        gcloud compute future-reservations create FUTURE_RESERVATION_NAME \
            --auto-delete-auto-created-reservations \
            **--total-count= NUMBER_OF_VMS** \
            **--machine-type= MACHINE_TYPE** \
            **--deployment-type=DENSE** \
            --planning-status=SUBMITTED \
            --require-specific-reservation \
            --reservation-mode=CALENDAR \
            --reservation-name=RESERVATION_NAME \
            --share-setting=SHARE_TYPE \
            --start-time=START_TIME \
            --end-time=END_TIME \
            --zone=ZONE
        

  * To reserve TPUs, include the `--chip-count` and `--tpu-version` flags:
        
        gcloud compute future-reservations create FUTURE_RESERVATION_NAME \
            --auto-delete-auto-created-reservations \
            **--chip-count= NUMBER_OF_CHIPS** \
            **--tpu-version= TPU_VERSION** \
            --planning-status=SUBMITTED \
            --require-specific-reservation \
            --reservation-mode=CALENDAR \
            --reservation-name=RESERVATION_NAME \
            --share-setting=SHARE_TYPE \
            --start-time=START_TIME \
            --end-time=END_TIME \
            --zone=ZONE
        




Replace the following:

  * `FUTURE_RESERVATION_NAME`: the name of the request.

  * `NUMBER_OF_VMS`: the number of GPU or H4D VMs to reserve:

    * For GPU VMs, the value must be between `1` and `80`.

    * For H4D VMs, the value must be between `1` and `256`.

Specify a number of VMs that is equal or lower than the number of VMs that you confirmed as available.

  * `MACHINE_TYPE`: the GPU or H4D machine type to reserve.

  * `NUMBER_OF_CHIPS`: the number of TPU chips to reserve. Specify a value equal to or lower than the number of chips that you confirmed as available. The value must be one of the following: `1`, `4`, `8`, `16`, `32`, `64`, `128`, `256`, `512`, or `1024`.

  * `TPU_VERSION`: the TPU version to reserve.

  * `RESERVATION_NAME`: the name of the reservation that Compute Engine automatically creates to provision your requested capacity.

  * `SHARE_TYPE`: whether other projects in your organization can consume the reserved capacity. Specify one of the following values:

    * To use capacity only within your project: `local`

    * To share capacity with other projects: `projects`

If you specify `projects`, then you must include the [`--share-with` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/create#--share-with) set to a comma-separated list of project IDs—for example, `project-1,project-2`. You can specify up to 100 projects that are in the same organization as the owner project (the project in which you create the reservation request). Don't specify the owner project in the `--share-with` flag. By default, the owner project can already consume the reservation.

  * `START_TIME`: the start time of the request, which you must format as an RFC 3339 timestamp.

  * `END_TIME`: the end time of your reservation period, which you must format as an RFC 3339 timestamp. If you want to specify a duration, in seconds, for your reservation period instead of an end time, then replace the `--end-time` flag with the [`--duration` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/create#--duration).

  * `ZONE`: the zone where you want to reserve resources.




###  REST 

To create a future reservation request in calendar mode and submit it for review, make a `POST` request to the [`futureReservations.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/insert). Based on the resources that you want to reserve, include the following fields in the request body:

  * To reserve GPU or H4D VMs, include the `totalCount` and `machineType` fields, as well as the `deploymentType` field set to `DENSE`:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations
        
        {
          "name": "FUTURE_RESERVATION_NAME",
          "autoDeleteAutoCreatedReservations": true,
          **"deploymentType": "DENSE"** ,
          "planningStatus": "SUBMITTED",
          "reservationMode": "CALENDAR",
          "reservationName": "RESERVATION_NAME",
          "shareSettings": {
            "shareType": "SHARE_TYPE"
          },
          "specificReservationRequired": true,
          "specificSkuProperties": {
            **"totalCount": NUMBER_OF_VMS**,
            **"instanceProperties": {
              "machineType": " MACHINE_TYPE"
            }**
          },
          "timeWindow": {
            "startTime": "START_TIME",
            "endTime": "END_TIME"
          }
        }
        

  * To reserve TPUs, include the `acceleratorCount` and `vmFamily` fields:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations
        
        {
          "name": "FUTURE_RESERVATION_NAME",
          "autoDeleteAutoCreatedReservations": true,
          "planningStatus": "SUBMITTED",
          "reservationMode": "CALENDAR",
          "reservationName": "RESERVATION_NAME",
          "shareSettings": {
            "shareType": "SHARE_TYPE"
          },
          "specificReservationRequired": true,
          "aggregateReservation": {
            "reservedResources": [
              {
                "accelerator": {
                  **"acceleratorCount": NUMBER_OF_CHIPS**
                }
              }
            ],
            **"vmFamily": " TPU_VERSION"**
          },
          "timeWindow": {
            "startTime": "START_TIME",
            "endTime": "END_TIME"
          }
        }
        




Replace the following:

  * `PROJECT_ID`: the ID of the project where you want to create the request.

  * `ZONE`: the zone where you want to reserve resources.

  * `FUTURE_RESERVATION_NAME`: the name of the request.

  * `RESERVATION_NAME`: the name of the reservation that Compute Engine automatically creates to provision your requested capacity.

  * `SHARE_TYPE`: whether other projects in your organization can consume the reserved capacity. Specify one of the following values:

    * To use capacity only within your project: `LOCAL`

    * To share capacity with other projects: `SPECIFIC_PROJECTS`

If you specify `SPECIFIC_PROJECTS`, then, in the `shareSettings` field, you must include the [`projectMap` field](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/insert#request-body) to specify the projects to share the capacity with. You can specify up to 100 projects that are in the same organization as the owner project (the project in which you create the reservation request). Don't specify the owner project in the `projectMap` field. By default, the owner project can already consume the reservation.

For example, to share the requested capacity with two other projects, include the following:
    
    "shareSettings": {
      "shareType": "SPECIFIC_PROJECTS",
      **"projectMap": {
        " CONSUMER_PROJECT_ID_1": {
          "projectId": "CONSUMER_PROJECT_ID_1"
        },
        "CONSUMER_PROJECT_ID_2": {
          "projectId": "CONSUMER_PROJECT_ID_2"
        }
      }**
    }
    

Replace `CONSUMER_PROJECT_ID_1` and `CONSUMER_PROJECT_ID_2` with the IDs of two projects that you want to allow to consume the requested capacity.

  * `NUMBER_OF_VMS`: the number of GPU or H4D VMs to reserve:

    * For GPU VMs, the value must be between `1` and `80`.

    * For H4D VMs, the value must be between `1` and `256`.

Specify a number of VMs that is equal or lower than the number of VMs that you confirmed as available.

  * `MACHINE_TYPE`: the GPU or H4D machine type to reserve.

  * `NUMBER_OF_CHIPS`: the number of TPU chips to reserve. Specify a value equal to or lower than the number of chips that you confirmed as available. The value must be one of the following: `1`, `4`, `8`, `16`, `32`, `64`, `128`, `256`, `512`, or `1024`.

  * `TPU_VERSION`: the TPU version to reserve.

  * `START_TIME`: the start time of the request, which you must format as an RFC 3339 timestamp.

  * `END_TIME`: the end time of your reservation period, which you must format as an RFC 3339 timestamp. If you want to specify a duration, in seconds, for your reservation period instead of an end time, then replace the `endTime` field with the `duration` field.




## What's next

  * [View reservations or future reservation requests](https://docs.cloud.google.com/compute/docs/instances/reservations-view)

  * To consume an auto-created reservation for GPU VMs, H4D VMs, or TPUs in Compute Engine, use one of the following methods:

    * [Consume an example reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consume-calendar-mode)

    * [Create an A4 or A3 Ultra VM](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-a3u-a4)

    * [Create an A3 Mega or A3 High VM](https://docs.cloud.google.com/compute/docs/gpus/gpudirect)

    * [Create an H4D VM](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters)

    * [Create a TPU VM](https://docs.cloud.google.com/compute/docs/tpus/create-tpu-vm-instance#create_a_tpu_vm_instance_using_a_reservation)

  * To modify an auto-created reservation, use one of the following methods:

    * [Modify whether Vertex AI jobs can use a reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-modify#modify-sharing-policy)

    * [Modify the share type for a reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-modify#modify-share-type)

  * To consume an auto-created reservation for GPU VMs or TPUs in Vertex AI, use one of the following methods:

    * [Use reservations with online inference jobs](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations)

    * [Use reservations with training jobs](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations)

  * [Delete a future reservation request in calendar mode](https://docs.cloud.google.com/compute/docs/instances/delete-future-reservations-calendar-mode)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
