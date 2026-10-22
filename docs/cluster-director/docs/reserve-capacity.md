---
url: https://docs.cloud.google.com/cluster-director/docs/reserve-capacity/
title: Reserve capacity through your account team \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:41:59.248831+00:00
---

# Reserve capacity through your account team  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/reserve-capacity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Reserve capacity through your account team Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to use future reservations for capacity blocks to reserve capacity for Compute Engine instances with GPUs attached and optional Hyperdisk pools for compute nodes. To learn more about your options to obtain capacity in Cluster Director, see [Choose a consumption option](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option).

To help ensure that you have the resources to create GPU instances and the storage capacity to create disks for those instances in a cluster partition, complete the following steps:

  1. **Request a future reservation from Google**. You reserve blocks of compute capacity and storage pool capacity for a defined duration and start time that you choose.

  2. **Review the draft request created by Google**. Based on your request, Google creates a future reservation request. You can then review the request details and, if needed, contact your account team to make changes.

  3. **Submit the request**. After you submit the request, Google Cloud approves it within a few minutes. Then, Compute Engine creates an empty reservation and, if requested, a Hyperdisk pool.

  4. **Consume your reserved resources**. At your request start time, Compute Engine delivers the reserved resources. You can then use the reservation to create GPU instances until the reservation period ends. Also, you can create disks in the Hyperdisk pool for your artificial intelligence (AI) or machine learning (ML) workloads.




## Limitations

This section describes the limitations for future reservation requests for capacity blocks, and for the auto-created reservations, Hyperdisk pools, and commitments for a request.

### Limitations for future reservation requests

After Google creates a draft future reservation request for capacity blocks, the following limitations apply:

  * **Pre-existing pools** :

    * **Hyperdisk Storage Pools** : you can't reserve capacity for a pre-existing pool. Google automatically creates a new pool when it delivers your reservation.

    * **Hyperdisk Exapools** : you can increase the capacity of an existing Exapool by submitting subsequent future reservation requests. To add capacity to an existing Exapool, contact your account team.

  * **Modifications** : after you submit the request for review, and Google Cloud approves it, you can't modify the request details.

  * **Cancellations** : after the request is submitted, approved, and its state changes to `PROVISIONING`, you can no longer cancel or delete the request. You commit to pay for the requested capacity from the request's start time, regardless of usage.




### Limitations for auto-created reservations and Hyperdisk pools

After Compute Engine creates a reservation and, if requested, a Hyperdisk pool to fulfill your reservation request, the following limitations apply:

  * You can start using the reserved capacity only after your request reaches its start time.

  * You can modify a reservation only by using the following methods. To increase the number of compute instances in a reservation or resources in a Hyperdisk pool, contact your account team.

    * [Modify the share type for a reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-modify#modify-share-type)

    * [Modify the projects that can consume a reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-modify#modifying-consumer-projects-shared-reservation)




### Limitations for attached commitments

If your auto-created reservations include an attached resource-based commitment, then the following limitations apply:

  * You can't renew, extend, merge, split, or upgrade that commitment.

  * If you use your reserved resources before the commitment becomes active, then you pay on-demand rates. To receive committed use discounts (CUDs), wait until the commitment becomes active before you use your reservation.




## Before you begin

Before you request a future reservation for capacity blocks, do the following:

  * As part of the process for using future reservations for capacity blocks, Google manages quota for your reserved resources. You don't need to request quota. At the start time of your approved future reservation, Google automatically increases your quota if you lack it for the reserved resources.

  * Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

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

  * To let Compute Engine auto-create reservations: `compute.reservations.create` on the project 
  * To create a future reservation request: `compute.futureReservations.create` on the project 
  * To specify an instance template: `compute.instanceTemplates.useReadOnly` on the instance template 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Request capacity through your account team

Contact your account team and provide the following information for Google to create a draft future reservation request:

  * **Project number** : the number of the project where your account team creates the request and Compute Engine provisions the capacity.

  * **Machine type** : the machine type to reserve. You can specify one of the following:

    * A4X (`a4x-highgpu-4g`)

    * A4 (`a4-highgpu-8g`)

    * A3 Ultra (`a3-ultragpu-8g`)

    * A3 Mega (`a3-megagpu-8g`)

  * **Zone** : the zone where you want to reserve capacity. To review the available regions and zones for a GPU machine type, see [GPU locations](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones).

  * **Total count** : the total number of compute instances to reserve. You can only reserve multiples of two compute instances. Block sizes and compute instance count per block vary based on machine type and availability. Your account team can provide more details for your request.

  * **Start time** : the start time of the reservation period. You can start using the reserved capacity at that time. If you request a Hyperdisk pool, then the start time must be on or before the start time for the compute instances. Format a start time as an RFC 3339 timestamp:
        
        YYYY-MM-DD**T** HH:MM:SSOFFSET
        

Replace the following:

    * `YYYY-MM-DD`: a date formatted as a four-digit year, two-digit month, and a two-digit day of the month, separated by hyphens (`-`). For example, to specify December 31, 2026, use `2026-12-31`.

    * `HH:MM:SS`: a time formatted as two-digit hours (24-hour time), two-digit minutes, and two-digit seconds, separated by colons (`:`).

    * `OFFSET`: the time zone formatted as an offset of [Coordinated Universal Time (UTC)](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). For example, to use the Pacific Standard Time (PST), specify `-08:00`. To use no offset, specify `Z`.

  * **End time** : the end time of the reservation period. The end time of the reservation for compute capacity and Hyperdisk pool capacity must match. You must format an end time as an RFC 3339 timestamp. At that time, Compute Engine does the following:

    * Deletes the auto-created reservation and the associated empty Hyperdisk pools.

    * Stops or deletes any compute instances that consume the auto-created reservation, based on the [termination action](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime#limit-runtime-new-vm) that you configured.

  * **Reservation name** : the name of the reservation that Compute Engine creates to deliver your reserved capacity. Compute Engine can only create [specifically targeted reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation).

  * **Reservation automatic deletion** : whether you want Compute Engine to automatically delete the auto-created reservation and any associated Hyperdisk pool at the end of the reservation period. If you want to manually delete the reservation, then you must contact your account team to delete the reservation.

  * **Share type** : whether only your project can use the auto-created reservation (`LOCAL`), or other projects can use the reservation (`SPECIFIC_PROJECTS`). To share the reserved capacity with other projects in your Google Cloud organization, complete the following steps:

    1. If you haven't already, then verify that the project where Google creates the request is [allowed to create shared reservations](https://docs.cloud.google.com/compute/docs/instances/manage-shared-reservations-creation).

    2. Provide the numbers of the projects to share the reserved capacity with. You can specify up to 100 projects that are in the same organization as the project in which you want to reserve capacity.

  * **Commitment name** : if your reservation period is one year or longer, then you must purchase and attach a [resource-based commitment](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) to your reserved resources. You can purchase a commitment with a 1-year or 3-year plan. If you share the reserved capacity with other projects, then those projects get discounts only if they use the same Cloud Billing account as the project where you reserve capacity. For details, see [Enable CUD sharing for resource-based commitments](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#turning-on-committed-use-discount-sharing).

**Important:** A commitment becomes active at 12:00 AM US and Canadian Pacific Time (UTC-8, or UTC-7 during daylight saving time) on your chosen start date. If you specify a different start time, then the commitment becomes active at 12:00 AM on the following day. For example, if you specify a start time at 3:00 PM on December 1, 2026, the commitment becomes active at 12:00 AM on December 2, 2026.
  * **Hyperdisk pool** : whether you want to reserve storage capacity along with your compute instances as a [Hyperdisk pool](https://docs.cloud.google.com/compute/docs/disks/pools). If you submitted a reservation request for compute capacity without storage, then you can submit a subsequent request. To submit a request for a Hyperdisk pool, then provide the following details:

    * **Hyperdisk pool name** : a name for the Hyperdisk pool. The name must be unique within your project.

    * **Hyperdisk pool type** : choose whether you want to create a Storage Pool or an Exapool, and whether you want to create only Hyperdisk Balanced or Hyperdisk Throughput volumes in your pool. For guidance, see [How to choose a Hyperdisk pool type](https://docs.cloud.google.com/compute/docs/disks/pools#choose) and [Choose a Hyperdisk type](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#when-to-use). After you make your choices, specify one of the following values:

      * **`hyperdisk-balanced`** : creates a Hyperdisk Balanced Storage Pool. This pool supports boot disks and non-boot disks. You must also specify the provisioned capacity in GiB, provisioned IOPS, and provisioned throughput in MiB/s.

      * **`hyperdisk-throughput`** : creates a Hyperdisk Throughput Storage Pool. This pool supports non-boot disks only. You must also specify the provisioned capacity in GiB and provisioned throughput in MiB/s.

      * **`hdb-exapool`** : creates a Hyperdisk Balanced Exapool for workloads that require 500 TiB or more of storage. This pool supports boot disks and non-boot disks. You must specify the provisioned capacity in GiB and your workload optimization type (`read-optimized`, `write-optimized`, or `capacity-optimized`).

      * **`hdt-exapool`** : creates a Hyperdisk Throughput Exapool for workloads that require 500 TiB or more of storage. This pool supports non-boot disks only. You must specify the provisioned capacity in GiB and your workload optimization type (`read-optimized`, `write-optimized`, or `capacity-optimized`).




When Google creates the draft future reservation request, your account team contacts you.

## Review and submit a draft reservation request

After you provide the type and amount of resources to reserve to your account team, Google creates a draft future reservation request. You can review the draft request and, if correct, submit it for review. You must submit the request before the request start time.

**Caution:** When you submit a request, you confirm your commitment to reserve your requested capacity. After Google Cloud approves the request, and the request state changes to `PROVISIONING`, you can't cancel, modify, or delete the request. You commit to pay for the requested capacity from the request's start time, regardless of usage.

To review and submit a draft future reservation request, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click the **Future reservations** tab. The **Future Reservations** table lists each future reservation request in your project, and each table column describes a property.

  3. In the **Name** column, click the name of the draft request that Google created for you. A page that gives the details of the future reservation request opens.

  4. In the **Basic information** and resource details sections, verify that the request details, such as **Dates** and **Share type** , are correct. Also, if you requested a commitment, verify that it's specified. If any of these details are incorrect, then contact your account team.

  5. If everything looks accurate, then submit your request:

     1. Click edit **Edit draft**. A page to modify the draft request appears.

     2. Click **Create**. The **Reservation** page appears. Within a few minutes, Google Cloud approves your request, and then Compute Engine creates an empty reservation. If you requested storage resources, then Compute Engine creates a new Storage Pool or Exapool, or increases capacity for an existing Exapool.




###  gcloud 

  1. To view a list of future reservation requests in your project, use the [`gcloud compute future-reservations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/list) with the `--filter` flag set to `PROCUREMENT_STATUS=DRAFTING`:
         
         gcloud compute future-reservations list --filter=PROCUREMENT_STATUS=DRAFTING
         

  2. In the command output, look for the reservation request that has the name that you provided to your account team.

  3. To view the details of the draft request, use the [`gcloud compute future-reservations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/describe).

Select and run one of the following commands:

###  Bash 
         
         gcloud compute future-reservations describe FUTURE_RESERVATION_NAME \
             --zone=ZONE
         

###  Powershell 
         
         gcloud compute future-reservations describe FUTURE_RESERVATION_NAME `
             --zone=ZONE
         

###  cmd.exe 
         
         gcloud compute future-reservations describe FUTURE_RESERVATION_NAME ^
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
    selfLink: https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west1-b/futureReservations/example-draft-request
    selfLinkWithId: https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west1-b/futureReservations/7979651787097007552
    specificReservationRequired: true
    specificSkuProperties:
      instanceProperties:
        guestAccelerators:
        - acceleratorCount: 8
          acceleratorType: nvidia-h200-141gb
        localSsds:
        - diskSizeGb: '375'
          interface: NVME
        ...
      machineType: a3-ultragpu-8g
    storagePoolProperties:
      requestedStoragePoolProvisionedCapacity:
        poolProvisionedCapacityGb: '10240'
        poolProvisionedIops: '100000'
        poolProvisionedThroughput: '2048'
      storagePoolType: 'hyperdisk-balanced'
    totalCount: '2'
    status:
      autoCreatedReservations:
      - https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west1-b/reservations/example-reservation
      fulfilledCount: '2'
      lockTime: '2026-01-27T19:15:00Z'
      procurementStatus: DRAFTING
    timeWindow:
      endTime: '2026-02-10T19:20:00Z'
      startTime: '2026-01-27T19:20:00Z'
    zone: https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west1-b
    

  4. In the command output, verify that the request details, such as the reservation period, share type, and compute instance properties are correct. Also, if you purchased a commitment, verify that it's specified in the output. If the details are incorrect, then contact your account team.

  5. To submit the draft request for review, use the [`gcloud compute future-reservations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/update) with the `--planning-status` flag set to `SUBMITTED`.

Select and run one of the following commands:

###  Bash 
         
         gcloud compute future-reservations update FUTURE_RESERVATION_NAME \
             --planning-status=SUBMITTED \
             --zone=ZONE
         

###  Powershell 
         
         gcloud compute future-reservations update FUTURE_RESERVATION_NAME `
             --planning-status=SUBMITTED `
             --zone=ZONE
         

###  cmd.exe 
         
         gcloud compute future-reservations update FUTURE_RESERVATION_NAME ^
             --planning-status=SUBMITTED ^
             --zone=ZONE
         

Within a few minutes, Google Cloud approves your request, and then Compute Engine creates an empty reservation. If you requested storage resources, then Compute Engine creates a new Storage Pool or Exapool, or increases capacity for an existing Exapool.




###  REST 

  1. To view a list of future reservation requests in your project, make a `GET` request to the [`futureReservations.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/list).

Your request must include the following HTTP method and request URL:
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations?filter=status.procurementStatus=DRAFTING
         

Replace the following:

     * `PROJECT_ID`: the ID of the project where Google created the draft future reservation request.

     * `ZONE`: the zone where Google created the request.

To send your request, select one of the following options:

###  curl (Bash) 
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations?filter=status.procurementStatus=DRAFTING"
    

###  Powershell 
    
    $cred = gcloud auth print-access-token
    $headers = @{ "Authorization" = "Bearer $cred" }
    
    Invoke-WebRequest `
        -Method GET `
        -Headers $headers `
        -Uri "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations?filter=status.procurementStatus=DRAFTING" | Select-Object -Expand Content
    

###  curl (cmd.exe) 
    
    curl -X GET ^
         -H "Authorization: Bearer $(gcloud auth print-access-token)" ^
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations?filter=status.procurementStatus=DRAFTING"
    

  2. In the request output, look for the reservation request that has the name that you provided to your account team.

  3. To view the details of the draft request, make a `GET` request to the [`futureReservations.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/get).

Your request must include the following HTTP method and request URL:
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations/FUTURE_RESERVATION_NAME
         

Replace `FUTURE_RESERVATION_NAME` with the name of the draft future reservation request.

To send your request, select one of the following options:

###  curl (Bash) 
         
         curl -X GET \
              -H "Authorization: Bearer $(gcloud auth print-access-token)" \
              "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations/FUTURE_RESERVATION_NAME"
         

###  Powershell 
         
         $cred = gcloud auth print-access-token
         $headers = @{ "Authorization" = "Bearer $cred" }
         
         Invoke-WebRequest `
             -Method GET `
             -Headers $headers `
             -Uri "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations/FUTURE_RESERVATION_NAME" | Select-Object -Expand Content
         

###  curl (cmd.exe) 
         
         curl -X GET ^
              -H "Authorization: Bearer $(gcloud auth print-access-token)" ^
              "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations/FUTURE_RESERVATION_NAME"
         

The response is similar to the following:
         
         {
           "specificSkuProperties": {
             "instanceProperties": {
               "machineType": "a3-ultragpu-8g",
               "guestAccelerators": [
                 {
                   "acceleratorType": "nvidia-h200-141gb",
                   "acceleratorCount": 8
                 }
               ],
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
           "storagePoolProperties": {
             "requestedStoragePoolProvisionedCapacity": {
               "poolProvisionedCapacityGb": "10240",
               "poolProvisionedIops": "100000",
               "poolProvisionedThroughput": "2048"
             },
             "storagePoolType": "hyperdisk-balanced"
           },
           "kind": "compute#futureReservation",
           "id": "7979651787097007552",
           "creationTimestamp": "2025-11-27T11:14:58.305-08:00",
           "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west1-b/futureReservations/example-draft-request",
           "selfLinkWithId": "https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west1-b/futureReservations/7979651787097007552",
           "zone": "https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west1-b",
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
         

  4. In the output, verify that the request details, such as the reservation period, share type, and compute instance properties are correct. Also, if you requested a commitment, verify that it's specified. If the details are incorrect, then contact your account team.

  5. To submit the draft request for review, make a `PATCH` request to the [`futureReservations.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/update).

Your request must include the following HTTP method and request URL:
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations/FUTURE_RESERVATION_NAME?updateMask=planningStatus
         

In the request body, include the following:
         
         {
           "name": "FUTURE_RESERVATION_NAME",
           "planningStatus": "SUBMITTED"
         }
         

Save the request body in a file named `request.json`. Then, to send your request, select one of the following options:

###  curl (Bash) 
         
         curl -X PATCH \
              -H "Authorization: Bearer $(gcloud auth print-access-token)" \
              -H "Content-Type: application/json; charset=utf-8" \
              -d @request.json \
              "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations/FUTURE_RESERVATION_NAME?updateMask=planningStatus"
         

###  Powershell 
         
         $cred = gcloud auth print-access-token
         $headers = @{ "Authorization" = "Bearer $cred" }
         
         Invoke-WebRequest `
             -Method PATCH `
             -Headers $headers `
             -ContentType: "application/json; charset=utf-8" `
             -InFile request.json `
             -Uri "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations/FUTURE_RESERVATION_NAME?updateMask=planningStatus" | Select-Object -Expand Content
         

###  curl (cmd.exe) 
         
         curl -X PATCH ^
              -H "Authorization: Bearer $(gcloud auth print-access-token)" ^
              -H "Content-Type: application/json; charset=utf-8" ^
              -d @request.json ^
              "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations/FUTURE_RESERVATION_NAME?updateMask=planningStatus"
         

Within a few minutes, Google Cloud approves your request, and then Compute Engine creates an empty reservation. If you requested storage resources, then Compute Engine creates a new Storage Pool or Exapool, or increases capacity for an existing Exapool.




## What's next

  * [View reserved capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
