---
url: https://docs.cloud.google.com/compute/docs/hpc/reserve-capacity-account-team/
title: Reserve capacity through your account team \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:08.072025+00:00
---

# Reserve capacity through your account team  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/hpc/reserve-capacity-account-team/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Reserve capacity through your account team Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to obtain capacity when you want to use future reservation requests to reserve [capacity blocks](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#block). This provisioning method lets you create HPC clusters with enhanced cluster management capabilities.

For a very high assurance that your workloads have the resources they need, request a future reservation from Google. You can reserve blocks of compute capacity and, optionally, a Hyperdisk pool in a single request for a defined duration, starting on a specific date and time that you choose. Based on your request, Google creates a draft future reservation request. After you review and submit this draft request, and Google Cloud approves it, Compute Engine creates an empty reservation and prepares your Hyperdisk pool. Then, at your chosen start time, Compute Engine provisions your requested capacity into the auto-created reservation and Hyperdisk pool all at once. You can then use the reserved resources to create VMs until the reservation period ends.

If you don't need to reserve densely allocated resources for your instances to minimize network latency, then see instead [Compute Engine instances provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).

## Limitations

This section describes the limitations for future reservation requests, and for the auto-created reservations and Hyperdisk pools for a request.

### Limitations for future reservation requests

After Google creates a draft future reservation request for you, the following limitations apply:

  * **Pre-existing pools** : 
    * **Hyperdisk Storage Pools** : you can't reserve capacity for a pre-existing pool. Google automatically creates a new pool when it delivers your reservation.
    * **Hyperdisk Exapools** : you can increase the capacity of an existing Exapool by submitting subsequent future reservation requests. To add capacity to an existing Exapool, contact your account team.
  * **Modifications** : after you submit the request for review, and Google Cloud approves it, you can't modify the request details.
  * **Cancellations** : after the request is submitted, approved, and its state changes to `PROVISIONING`, you can no longer cancel or delete the request. You commit to pay for the requested capacity from the request's start time, regardless of usage.



### Limitations for auto-created reservations and Hyperdisk pools

After Compute Engine creates a reservation and, if requested, a Hyperdisk pool to fulfill your reservation request, the following limitations apply:

  * You can use the reserved capacity only after your request reaches its start time.
  * You can modify a reservation only by using the following methods. To increase the number of compute instances in a reservation or resources in a Hyperdisk pool, contact your account team.

    * [ Enable hardware emergency maintenance notifications](https://docs.cloud.google.com/compute/docs/hpc/manage-host-events-reservations-h4d#emergency-notifications)
    * [Modify the share type for a reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-modify#modify-share-type)
    * [ Modify the projects that can consume a reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-modify#modifying-consumer-projects-shared-reservation)
  * You can't manually delete the reservation or any associated Hyperdisk pool. If you choose to retain your reservation after the reservation period ends, then contact your account team to delete the reservation and associated Hyperdisk pool.



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

To get the permissions that you need to create a future reservation request, ask your administrator to grant you the [Compute Future Reservation User ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.futureReservationUser) (`roles/compute.futureReservationUser`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a future reservation request. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a future reservation request:

  * To allow Compute Engine to auto-create reservations: `compute.reservations.create` on the project 
  * To create a future reservation request: `compute.futureReservations.create` on the project 
  * To specify an instance template: `compute.instanceTemplates.useReadOnly` on the instance template 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Quota

As part of the future reservation request process, Google manages quota for your reserved resources. You don't need to request quota. At the start time of your approved future reservation, Google automatically increases your quota if your project doesn't have enough for the reserved resources.

## Overview

To reserve blocks of capacity, complete the following steps:

  1. **Request capacity through your account team**. Contact your account team to specify the type and number of resources that you want to reserve.
  2. **Review and submit a draft reservation request**. After Google creates a draft future reservation request, review it. If it looks correct, then submit the request for review. Google Cloud immediately approves it.



## Request capacity through your account team

Contact your account team and provide the following information for Google to create a draft future reservation request:

  * **Project number** : the number of the project where your account team creates the request and Compute Engine provisions the capacity.
  * **Machine type** : the machine type to reserve. You can specify one of the following: 
    * `h4d-standard-192`
    * `h4d-highmem-192`
    * `h4d-highmem-192-lssd`
  * **Zone** : the zone where you want to reserve capacity. To review the available regions and zones for the machine type, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available). 
  * **Deployment type** : specify a _dense_ deployment type. This configuration allocates your accelerators physically close to each other to minimize network hops and optimize for the lowest latency. Google recommends this configuration for clustered GPU workloads to reduce network latency.
  * **Total count** : the total number of VMs to reserve. Block sizes and VM count per block vary based on machine type and availability. Your account team can provide more details for your request.
  * **Start time** : the start time of the reservation period. You can use the reserved capacity at that time. If you request a Hyperdisk pool, then the start time must be on or before the start time for the compute instances. Format a start time as an RFC 3339 timestamp: 
        
        YYYY-MM-DD**T** HH:MM:SSOFFSET
        

Replace the following:

    * `YYYY-MM-DD`: a date formatted as a four-digit year, two-digit month, and a two-digit day of the month, separated by hyphens (`-`).
    * `HH:MM:SS`: a time formatted as a two-digit hour by using a 24-hour time, two-digit minutes, and two-digit seconds, separated by colons (`:`).
    * `OFFSET`: the time zone formatted as an offset of [Coordinated Universal Time (UTC)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). For example, to use the Pacific Standard Time (PST), specify `-08:00`. To use no offset, specify `Z`.
  * **End time** : the end time of the reservation period. The end time of the reservation for compute capacity and Hyperdisk pool capacity must match. You must format an end time as an RFC 3339 timestamp. At that time, Compute Engine does the following: 
    * Deletes the auto-created reservation and any associated empty Hyperdisk pools.
    * Based on the [ termination action](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime#limit-runtime-new-vm) that you specify for your VMs, Compute Engine stops or deletes any VMs that you created by using the auto-created reservation.
  * **Reservation name** : the name of the reservation that Compute Engine creates to deliver your reserved capacity. Compute Engine can create only [ specifically targeted reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation).
  * **Reservation automatic deletion** : whether you want Compute Engine to automatically delete the auto-created reservation and any associated Hyperdisk pool at the end of the reservation period. If you want to manually delete the reservation, then you must contact your account team to delete the reservation.
  * **Maintenance scheduling type** : how Compute Engine schedules host maintenance for the VMs in your cluster. Specify one of the following options: 
    * To synchronize maintenance across all H4D instances in your reserved blocks, use `GROUPED`.
    * To use different maintenance schedules for your H4D instances, use `INDEPENDENT`.
  * **Reservation operational mode** : whether you or Google Cloud manages the VM recovery process after a host error or faulty host report.

For H4D VMs, specify **Managed mode (`HIGHLY_AVAILABLE_CAPACITY`)**. This mode lets Google Cloud manage the maintenance and recovery process for a VM by automatically replacing faulty machines. This approach increases the availability of your VMs and helps you quickly restart them on new hosts. However, the topology of your VMs might change after Compute Engine replaces a machine.

**Important:** In the managed mode, calls to the report faulty host API may be rate-limited per reservation. 
  * **Share type** : whether only your project can use the auto-created reservation (`LOCAL`), or other projects can use the reservation (`SPECIFIC_PROJECTS`). To share reserved capacity with other projects in your organization, do the following: 
    1. If you haven't already, then verify that the project where Google creates the request is [allowed to create shared reservations](https://docs.cloud.google.com/compute/docs/instances/manage-shared-reservations-creation).
    2. Provide the numbers of the projects to share the reserved capacity with. You can specify up to 100 projects in your organization.
**Caution:** If you want usage from the shared projects to qualify for resource-based committed use discounts (CUDs) from the current project, then complete the following steps: 
    1. Enable [ CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects) on the current project's Cloud Billing account.
    2. Share your reservation only with projects that are linked to the same Cloud Billing account.

**If you don't meet these conditions, then usage from those projects won't be eligible for the shared CUDs and Compute Engine charges you on-demand rates.**

  * **Commitment name** : if your reservation period is one year or longer, then Google Cloud creates a [resource-based commitment](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) for those resources and attaches the commitment to your reservation. If your reservation period is less than 3 years, then you receive committed use discounts (CUDs) that apply to the 1-year plan for that commitment. If your reservation period is 3 years or more, then you receive CUDs that apply to the 3-year plan.

If you share the reserved capacity with other projects, then those projects get CUDs only if they use the same Cloud Billing account as the project where you reserve capacity. For details, see [Share resource-based CUDs across projects](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects).

The commitment has the same start and end dates as your reservation, but the activation times might differ. If you specify the reservation start time as 12:00 AM US and Canadian Pacific Time, then the commitment becomes active at 12:00 AM on your chosen start date. If you specify a different start time, then the commitment becomes active at 12:00 AM on the following day of your chosen start date.

**Caution:** If you use your reservation before the commitment becomes active, then you pay on-demand rates. To receive CUDs, wait until the commitment becomes active before you use your reservation. 
  * **Hyperdisk pool** : whether you want to reserve storage capacity along with your compute instances as a [Hyperdisk pool](https://docs.cloud.google.com/compute/docs/disks/pools). If you submitted a reservation request for compute capacity without storage, then you can submit a subsequent request. To submit a request for a Hyperdisk pool, provide the following details:

    * **Hyperdisk pool name** : a name for the Hyperdisk pool. The name must be unique within your project.
    * **Hyperdisk pool type** : choose whether you want to create a Storage Pool or an Exapool, and whether you want to create only Hyperdisk Balanced or Hyperdisk Throughput volumes in your pool. For guidance, see [How to choose a Hyperdisk pool type](https://docs.cloud.google.com/compute/docs/disks/pools#choose) and [Choose a Hyperdisk type](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#when-to-use). After you make your choices, specify one of the following values:

      * **`hyperdisk-balanced`** : creates a Hyperdisk Balanced Storage Pool. This pool supports boot disks and non-boot disks. You must also specify the provisioned capacity in GiB, provisioned IOPS, and provisioned throughput in MiB/s.
      * **`hyperdisk-throughput`** : creates a Hyperdisk Throughput Storage Pool. This pool supports non-boot disks only. You must also specify the provisioned capacity in GiB and provisioned throughput in MiB/s.
      * **`hdb-exapool`** : creates a Hyperdisk Balanced Exapool for workloads that require 500 TiB or more of storage. This pool supports boot disks and non-boot disks. You must specify the provisioned capacity in GiB and your workload optimization type (`read-optimized`, `write-optimized`, or `capacity-optimized`).
      * **`hdt-exapool`** : creates a Hyperdisk Throughput Exapool for workloads that require 500 TiB or more of storage. This pool supports non-boot disks only. You must specify the provisioned capacity in GiB and your workload optimization type (`read-optimized`, `write-optimized`, or `capacity-optimized`).



After Google creates the draft future reservation request, your account team contacts you.

## Review and submit a draft reservation request

After you give the resource details to your account team, Google creates a draft future reservation request. You can review the draft request and, if correct, submit it for review. You must submit the request before the request start time.

**Caution:** When you submit a request, you confirm your commitment to reserve your requested capacity. After Google Cloud approves the request, and the request state changes to `PROVISIONING`, you can't cancel, modify, or delete the request. You commit to pay for the requested capacity from the request's start time, whether you use the capacity or not. 

To review and submit a draft future reservation request, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click the **Future reservations** tab. The **Future Reservations** table lists each future reservation request in your project, and each table column describes a property.
  3. In the **Name** column, click the name of the draft request that Google created for you. A page that gives the details of the future reservation request opens.
  4. In the **Basic information** and resource details sections, verify that the request details, such as **Dates** and **Share type** , are correct. Also, if you requested a commitment, verify that it's specified. If any of these details are incorrect, then contact your account team.
  5. If everything looks accurate, then submit your request:

     1. Click edit **Edit draft**. A page to modify the draft request appears.
     2. Click **Create**. The **Reservation** page appears. Within a few minutes, Google Cloud approves your request, and then Compute Engine creates an empty reservation. If you requested storage resources, then Compute Engine creates a new Storage Pool or Exapool, or increases capacity for an existing Exapool.



### gcloud

  1. To view a list of future reservation requests in your project, use the [`gcloud compute future-reservations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/list) with the `--filter` flag set to `PROCUREMENT_STATUS=DRAFTING`: 
         
         gcloud compute future-reservations list --filter=PROCUREMENT_STATUS=DRAFTING
         

  2. In the command output, look for the reservation request that has the name that you provided to your account team.
  3. To view the details of the draft request, use the [`gcloud compute future-reservations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/describe): 
         
         gcloud compute future-reservations describe FUTURE_RESERVATION_NAME \
             --zone=ZONE
         

Replace the following:

     * `FUTURE_RESERVATION_NAME`: the name of the draft future reservation request.
     * `ZONE`: the zone where Google created the request.

The output is similar to the following:
    
    autoCreatedReservationsDeleteTime: '2026-02-10T19:20:00Z'
    creationTimestamp: '2025-11-27T11:14:58.305-08:00'
    deploymentType: DENSE
    id: '7979651787097007552'
    kind: compute#futureReservation
    name: example-draft-request
    planningStatus: DRAFT
    reservationName: example-reservation
    schedulingType: INDEPENDENT
    selfLink: https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west4-b/futureReservations/example-draft-request
    selfLinkWithId: https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west4-b/futureReservations/7979651787097007552
    specificReservationRequired: true
    specificSkuProperties:
       instanceProperties:
         localSsds:
      -   diskSizeGb: '375'
          interface: NVME
        ...
      machineType: h4d-highmem-192-lssd
    totalCount: '2'
    status:
      autoCreatedReservations:
      -   https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west4-b/reservations/example-reservation
      fulfilledCount: '2'
      lockTime: '2026-01-27T19:15:00Z'
      procurementStatus: DRAFTING
    timeWindow:
      endTime: '2026-02-10T19:20:00Z'
      startTime: '2026-01-27T19:20:00Z'
    zone: https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west4-b
    

  4. In the output, verify that the request details, such as the reservation period, share type, and compute instance properties are correct. Also, if you requested a commitment, verify that it's specified in the output. If the details are incorrect, then contact your account team.
  5. To submit the draft request for review, use the [`gcloud compute future-reservations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/update) with the `--planning-status` flag set to `SUBMITTED`: 
         
         gcloud compute future-reservations update FUTURE_RESERVATION_NAME \
             --planning-status=SUBMITTED \
             --zone=ZONE
         

Within a few minutes, Google Cloud approves your request, and then Compute Engine creates an empty reservation. If you requested storage resources, then Compute Engine creates a new Storage Pool or Exapool, or increases capacity for an existing Exapool.




### REST

  1. To view a list of future reservation requests in your project, make a `GET` request to the [`futureReservations.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/list). In the request URL, include the `filter` query parameter and set it to `status.procurementStatus=DRAFTING`: 
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations?filter=status.procurementStatus=DRAFTING
         

Replace the following:

     * `PROJECT_ID`: the ID of the project where Google created the draft future reservation request.
     * `ZONE`: the zone where the request exists.
  2. In the request output, look for the reservation request that has the name that you provided to your account team.
  3. To view the details of the draft request, make a `GET` request to the [beta `futureReservations.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/get): 
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations/FUTURE_RESERVATION_NAME
         

Replace `FUTURE_RESERVATION_NAME` with the name of the draft future reservation request.

The output is similar to the following:
         
         {
           "specificSkuProperties": {
             "instanceProperties": {
               "machineType": "h4d-highmem-192-lssd",
               "localSsds": [
                 {
                   "diskSizeGb": "375",
                   "interface": "NVME"
                 },
                 ...
               ]
             },
             "totalCount": "2"
           },
           "kind": "compute#futureReservation",
           "id": "7979651787097007552",
           "creationTimestamp": "2025-11-27T11:14:58.305-08:00",
           "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west4-b/futureReservations/example-draft-request",
           "selfLinkWithId": "https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west4-b/futureReservations/7979651787097007552",
           "zone": "https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west4-b",
           "name": "example-draft-request",
           "timeWindow": {
             "startTime": "2026-01-27T19:20:00Z",
             "endTime": "2026-02-10T19:20:00Z"
           },
           "status": {
             "procurementStatus": "DRAFTING",
             "lockTime": "2026-01-27T19:15:00Z"
             },
           "planningStatus": "DRAFT",
           "specificReservationRequired": true,
           "reservationName": "example-reservation",
           "deploymentType": "DENSE",
           "schedulingType": "INDEPENDENT",
           "autoCreatedReservationsDeleteTime": "2026-02-10T19:20:00Z"
         }
         

  4. In the output, verify that the request details, such as the reservation period, share type, and compute instance properties are correct. Also, if you requested a commitment, verify that it's specified in the output. If the details are incorrect, then contact your account team.
  5. To submit the draft request for review, make a `PATCH` request to the [beta `futureReservations.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/update). In the request URL, include the `updateMask` query parameter and set it to `planningStatus`: 
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations/FUTURE_RESERVATION_NAME?updateMask=planningStatus
         
         {
           "name": "FUTURE_RESERVATION_NAME",
           "planningStatus": "SUBMITTED"
         }
         

Within a few minutes, Google Cloud approves your request, and then Compute Engine creates an empty reservation. If you requested storage resources, then Compute Engine creates a new Storage Pool or Exapool, or increases capacity for an existing Exapool.




## What's next

  * [View reserved capacity](https://docs.cloud.google.com/compute/docs/hpc/view-reserved-capacity)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
