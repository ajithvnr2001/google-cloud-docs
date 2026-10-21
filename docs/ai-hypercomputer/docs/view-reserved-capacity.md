---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity/
title: View reserved capacity \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:34:53.298394+00:00
---

# View reserved capacity  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  View reserved capacity Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document explains how to view your requests for reserved capacity and your reserved capacity for AI Hypercomputer. By viewing the availability, properties, and topology of your reserved capacity and requests, you can plan reserved capacity for your workloads.

The scope of this document is limited to workloads that use a capacity option that mentions _future reservations_. For more information about the capacity options for AI Hypercomputer, see [Capacity overview](https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity). 

After Google Cloud approves a future reservation request, Compute Engine automatically creates (_auto-creates_) an empty reservation for your requested resources. You can then view the reservation to plan your workload. Later, at the requested start time, the following occurs: 

  * Compute Engine adds your reserved Compute Engine instances to the reservation. You can then start using the reservation by creating compute instances that match the reservation.
  * You can modify the reservation to allow Vertex AI training or prediction jobs to use it. For instructions, see [ Modify the sharing policy of a reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-modify#modify-sharing-policy).



## Limitations

You can view a shared reservation or shared future reservation request only in the project where Google created it.

## Before you begin

  1. **Reserve capacity:** If your project hasn't already, reserve capacity for AI Hypercomputer by using one of the following options: 
     * [ Reserve capacity through your account team](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity)
     * [ Create a future reservation request in calendar mode](https://docs.cloud.google.com/compute/docs/instances/create-future-reservations-calendar-mode)
  2. Select the tab for how you plan to use the samples on this page:

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

To get the permissions that you need to view reservations, ask your administrator to grant you the [Compute Future Reservation User ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.futureReservationUser) (`roles/compute.futureReservationUser`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view reservations. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view reservations:

  * To view the details of a future reservation request: `compute.futureReservations.get` on the project 
  * To view the details of a reservation: `compute.reservations.get` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View your requests for reserved capacity

To view your future reservation requests, use one or more of the following methods:

  * To get an overview of all future reservation requests in your project, view a list of your future reservation requests.
  * To view the full details of a single future reservation request, view the details of a future reservation request.



### View a list of your future reservation requests

You can view a list of your future reservation requests to see the reservation period, status, and zone of your requests.

To view a list of your future reservation requests, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Reservations** page. 

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click the **Future reservations** tab. The table lists each future reservation request, and each table column describes a property.
  3. Optional: To refine your list of requests, in the filter_list **Filter** field, select the properties that you want to filter the requests by.



### gcloud

To view a list of your future reservation requests, use the [`gcloud compute future-reservations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/list): 
    
    
    gcloud compute future-reservations list
    

The output is similar to the following example:
    
    
    NAME: fr-01
    TOTAL_COUNT: 100
    START_TIME: 2026-07-20T07:00:00Z
    END_TIME: 2026-08-05T07:00:00Z
    PROCUREMENT_STATUS: FULFILLED
    ZONE: us-west4-b
    
    NAME: fr-02
    TOTAL_COUNT: 10
    START_TIME: 2026-07-20T07:00:00Z
    END_TIME: 2026-12-01T00:00:00Z
    PROCUREMENT_STATUS: PENDING_APPROVAL
    ZONE: us-west4-b
    

If you want to refine your list of future reservation requests, then use the same command with the [`--filter` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/list#--filter). 

### REST

To view a list of your future reservation requests, make a `GET` request to one of the following methods:

  * To view a list of requests across all zones: [`futureReservations.aggregatedList` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/aggregatedList)
  * To view a list of requests in a specific zone: [`futureReservations.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/list)



For example, to view a list of requests across all zones, make a `GET` request as follows:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/futureReservations
    

Replace `PROJECT_ID` with the ID of the project where the requests exist.

The output for a list of future reservations requests in a single zone is similar to the following:
    
    
    {
      "id": "projects/example-project/aggregated/futureReservations",
      "items": [
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
        },
        ...
      ],
      "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/aggregated/futureReservations",
      "etag": "AnzKY34l-cvvV-JnniESJ0dtQvQ=/hvc4jaHpxFAZmOt1FVtKNgzZu-M=",
      "kind": "compute#futureReservationsListResponse"
    }
    

If you want to refine your list of future reservation requests, then make the same request and, in the request URL, include the `filter` [query parameter](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/aggregatedList#body.QUERY_PARAMETERS.filter).

### View the details of a future reservation request

You can view the details of a future reservation request to review the properties and reservation period of your reserved resources.

To view the details of a future reservation request, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. Click the **Future reservations** tab. The table lists each future reservation request, and each table column describes a property.
  3. To view the details of a request, in the **Name** column, click the name of the request. A page that gives the details of the future reservation request opens.



### gcloud

To view the details of a future reservation request, use the [ `gcloud compute future-reservations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/future-reservations/describe):
    
    
    gcloud compute future-reservations describe FUTURE_RESERVATION_NAME \
        --zone=ZONE
    

Replace the following:

  * `FUTURE_RESERVATION_NAME`: the name of the future reservation request.
  * `ZONE`: the zone where the future reservation request exists.



The output is similar to the following example:
    
    
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
        -   acceleratorCount: 8
          acceleratorType: nvidia-h200-141gb
        localSsds:
        -   diskSizeGb: '375'
          interface: NVME
        ...
      machineType: a3-ultragpu-8g
    totalCount: '2'
    storagePoolProperties:
      requestedStoragePoolProvisionedCapacity:
        poolProvisionedCapacityGb: '102400'
        poolProvisionedIops: '100000'
        poolProvisionedThroughput: '1024'
      storagePoolType: 'hyperdisk-balanced'
    status:
      autoCreatedReservations:
      -   https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west1-b/reservations/example-reservation
      fulfilledCount: '2'
      lockTime: '2026-01-27T19:15:00Z'
      procurementStatus: DRAFTING
    timeWindow:
      endTime: '2026-02-10T19:20:00Z'
      startTime: '2026-01-27T19:20:00Z'
    zone: https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west1-b
    

### REST

To view the details of a future reservation request, make a `GET` request to the [`futureReservations.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/futureReservations/get):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/futureReservations/FUTURE_RESERVATION_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the future reservation request exists.
  * `ZONE`: the zone where the future reservation request exists.
  * `FUTURE_RESERVATION_NAME`: the name of the future reservation request.



The output is similar to the following:
    
    
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
          "poolProvisionedCapacityGb": "102400",
          "poolProvisionedIops": "100000",
          "poolProvisionedThroughput": "1024"
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
    

## View your reserved capacity

View your reserved capacity when you want to do one or more of the following:

  * Identify a reservation, block, and sub-block that you want to use to deploy a workload.
  * Understand the properties, usage, and topology of your reserved capacity.



To view your reserved capacity, use one or more of the following methods:

  * To see an overview of all the reserved capacity in your project and check for any unused reserved capacity, view a list of your reservations.
  * To review the properties and availability of all the reserved VMs for a reservation, view the details of a reservation.
  * To understand how the blocks and sub-blocks of capacity for a reservation are organized, such as for integration with your scheduler or planning tool, view the topology of a reservation.



### View a list of your reservations

You can view a list of your reservations in your project to see all of the reserved capacity in your project and search for a reservation to use to deploy your workload.

To view a list of your reservations, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Reservations** page. 

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

On the **On-demand reservations** tab (default), the table lists each reservation, and each table column describes a property.

  2. Optional: To refine your list of reservations, in the filter_list **Filter** field, select the properties that you want to filter the reservations by.



### gcloud

To view a list of your reservations, use the [`gcloud compute reservations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/list): 
    
    
    gcloud compute reservations list
    

The output is similar to the following:
    
    
    NAME: r-01
    IN_USE_COUNT: 0
    COUNT: 5
    ZONE: europe-west4-b
    SHARE_TYPE: LOCAL
    
    NAME: r-02
    IN_USE_COUNT: 3
    COUNT: 10
    ZONE: europe-west4-b
    SHARE_TYPE: LOCAL
    

If you want to refine your list of reservations, then use the same command with the [`--filter` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/list#--filter). 

### REST

To view a list of your reservations, make a `GET` request to one of the following methods:

  * To view a list of your reservations across all zones: [`reservations.aggregatedList` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/aggregatedList)
  * To view a list of your reservations in a single zone: [`reservations.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/list)



For example, to view a list of your reservations across all zones, make a `GET` request as follows:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/reservations
    

Replace `PROJECT_ID` with the ID of the project where the reservations exist.

The output for a list of reservations in a single zone is similar to the following:
    
    
    {
      "id": "projects/example-project/zones/europe-west1-b/futureReservations",
      "items": [
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
        ...
      ],
      "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/zones/europe-west1-b/futureReservations",
      "etag": "AnzKY34l-cvvV-JnniESJ0dtQvQ=/hvc4jaHpxFAZmOt1FVtKNgzZu-M=",
      "kind": "compute#futureReservationsListResponse"
    }
    

If you want to refine your list of reservations, then make the same request and, in the request URL, include the [`filter` query parameter](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/aggregatedList#body.QUERY_PARAMETERS.filter). 

### View the details of a reservation

You can view the details of a reservations in your project to understand details like the following:

  * Which types of compute instances are in the reservation.
  * How many compute instances are reserved and available in the reservation.
  * The health of your reserved resources in a reservation, including the number of healthy blocks in the reservation. You can only view the health of a reservation by using the gcloud CLI or the REST.
  * **`schedulingType`** : how Compute Engine schedules host maintenance for the compute instances in your cluster.



If you want to understand the blocks and sub-blocks of a reservation, see View the topology of a reservation instead.

To view the details of a reservation, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. In the **On-demand reservations** table, in the **Name** column, click the name of the reservation that you want to view the details of. A page that gives the details of the reservation appears.



### gcloud

To view the details of a reservation, use the [ `gcloud compute reservations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/describe):
    
    
    gcloud compute reservations describe RESERVATION_NAME \
        --zone=ZONE
    

Replace the following:

  * `RESERVATION_NAME`: the name of the reservation.
  * `ZONE`: the zone where the reservation exists.



The output is similar to the following example:
    
    
    advancedDeploymentControl:
      reservationOperationalMode: ALL_CAPACITY
    creationTimestamp: '2025-07-18T13:23:22.191-07:00'
    deleteAtTime: '2026-06-19T00:00:00Z'
    deploymentType: DENSE
    enableEmergentMaintenance: false
    id: '4298354039694234582'
    kind: compute#reservation
    name: example-res1
    reservationSharingPolicy:
      serviceShareType: DISALLOW_ALL
    resourceStatus:
      healthInfo:
        degradedBlockCount: 0
        healthStatus: HEALTHY
        healthyBlockCount: 1
      reservationBlockCount: 1
      reservationMaintenance:
        schedulingType: GROUPED
    schedulingType: GROUPED
    selfLink: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/reservations/example-res1
    selfLinkWithId: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/reservations/4298354039694234582
    shareSettings:
      shareType: LOCAL
    specificReservation:
      assuredCount: '18'
      count: '18'
      inUseCount: '2'
      instanceProperties:
        guestAccelerators:
        -   acceleratorCount: 4
          acceleratorType: nvidia-gb200
        localSsds:
        -   diskSizeGb: '3000'
          interface: NVME
        -   diskSizeGb: '3000'
          interface: NVME
        -   diskSizeGb: '3000'
          interface: NVME
        -   diskSizeGb: '3000'
          interface: NVME
        machineType: a4x-highgpu-4g
    specificReservationRequired: true
    status: READY
    zone: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a
    

The output includes the following fields for the reservation:

  * `name`: the name of the reservation.
  * `healthInfo`: the health information for the reservation as follows: 
    * `degradedBlockCount`: the number of degraded blocks in the reservation.
    * `healthStatus`: the overall health status of the reservation.
    * `healthyBlockCount`: the number of healthy blocks in the reservation.
  * `reservationBlockCount`: the total number of blocks in the reservation.
  * `assuredCount`: the total number of VMs that can be deployed using the reservation. If this value is less than `count`, see how to troubleshoot [ fewer VMs available for consumption](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption#fewer-vms-available).
  * `inUseCount`: the number of VMs that are already deployed in the reservation.
  * `instanceProperties`: the properties of the VMs that can be deployed the reservation. 



### REST

To view the details of a reservation, make a `GET` request to the [ `reservations.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/get):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations/RESERVATION_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the reservation exists.
  * `ZONE`: the zone where the reservation exists.
  * `RESERVATION_NAME`: the name of the reservation.



The output is similar to the following:
    
    
    {
      "specificReservation": {
        "instanceProperties": {
          "machineType": "a4x-highgpu-4g",
          "guestAccelerators": [
            {
              "acceleratorType": "nvidia-gb200",
              "acceleratorCount": 4
            }
          ],
          "localSsds": [
            {
              "diskSizeGb": "3000",
              "interface": "NVME"
            },
            {
              "diskSizeGb": "3000",
              "interface": "NVME"
            },
            {
              "diskSizeGb": "3000",
              "interface": "NVME"
            },
            {
              "diskSizeGb": "3000",
              "interface": "NVME"
            }
          ]
        },
        "count": "36",
        "inUseCount": "35",
        "assuredCount": "33"
      },
      "kind": "compute#reservation",
      "id": "6823689647457870910",
      "creationTimestamp": "2025-08-04T13:40:50.496-07:00",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/reservations/example-res1",
      "zone": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a",
      "name": "example-res1",
      "specificReservationRequired": true,
      "status": "READY",
      "shareSettings": {
        "shareType": "SPECIFIC_PROJECTS"
      },
      "resourceStatus": {
        "reservationMaintenance": {
          "upcomingGroupMaintenance": {
            "type": "SCHEDULED",
            "canReschedule": false,
            "maintenanceStatus": "ONGOING"
          },
          "maintenanceOngoingCount": 2,
          "maintenancePendingCount": 34,
          "schedulingType": "GROUPED",
          "subblockInfraMaintenanceOngoingCount": 0,
          "subblockInfraMaintenancePendingCount": 0,
          "instanceMaintenanceOngoingCount": 3,
          "instanceMaintenancePendingCount": 32
        },
        "reservationBlockCount": 1,
        "healthInfo": {
          "healthStatus": "DEGRADED",
          "healthyBlockCount": 0,
          "degradedBlockCount": 1
        }
      },
      "reservationSharingPolicy": {
        "serviceShareType": "DISALLOW_ALL"
      },
      "deploymentType": "DENSE",
      "advancedDeploymentControl": {
        "reservationOperationalMode": "ALL_CAPACITY"
      },
      "enableEmergentMaintenance": false,
      "schedulingType": "GROUPED",
      "deleteAtTime": "2025-10-01T00:00:00Z"
    }
    

The output includes the following fields for the reservation:

  * `instanceProperties`: the properties of the compute instances that can be deployed in the reservation.
  * `inUseCount`: the number of compute instances that are already deployed in the reservation.
  * `assuredCount`: the total number of compute instances that can be deployed by using the reservation. If this value is less than `count`, see how to troubleshoot [ fewer VMs available for consumption](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption#fewer-vms-available).
  * `name`: the name of the reservation.
  * `healthInfo`: the health information for the reservation as follows: 
    * `healthStatus`: the overall health status of the reservation.
    * `healthyBlockCount`: the number of healthy blocks in the reservation.
    * `degradedBlockCount`: the number of degraded blocks in the reservation.



### View the topology of a reservation

You can view the detailed topology information of a reservation to help you decide where to create compute instances within the reserved blocks and sub-blocks. For information about the placement of reserved compute instances that are already deployed, see [View topology of a compute instance](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/instance-topology). 

If you want to view other details about a reservation, see view the details of a reservation instead.

#### View reserved blocks

To list and describe the available blocks in a reservation, use any of the following methods. This task helps you determine the following:

  * Which blocks of capacity are in the reservation.
  * How much capacity is available in each block.
  * The health of each block, including its number of healthy sub-blocks. (Only available by using gcloud CLI or REST.)
  * The name, block, and sub-block of all the compute instances that are deployed in the block. (Only available when viewing a specific block by using gcloud CLI or REST.)



### Console

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. In the **On-demand reservations** table, in the **Name** column, click the name of the reservation that you want to view the details of. The details page of the reservation opens.
  3. In the **Resource topology** section, you can view information about your reserved blocks. This information includes the following for each block: 
     * **Block ID** : the name of the block.
     * **Count** : the total number of compute instances that can be deployed in the block.
     * **In use** : the number of compute instances that are already deployed in the block.



### gcloud

You can view the blocks in a reservation using the following commands:

  * To view _all_ the available blocks in a reservation, use the [ `gcloud compute reservations blocks list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/blocks/list): 
        
        gcloud compute reservations blocks list RESERVATION_NAME \
            --zone=ZONE
        

  * To view a _specific_ block in a reservation, use the [ `gcloud compute reservations blocks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/blocks/describe). To also view the name and topology of all the compute instances that are deployed in the block, add the `--full-view=BLOCK_VIEW_FULL` flag. 
        
        gcloud compute reservations blocks describe RESERVATION_NAME \
            --zone=ZONE \
            --block-name=BLOCK_NAME \
            --full-view=BLOCK_VIEW_FULL
        




Replace the following:

  * `RESERVATION_NAME`: the name of the reservation.
  * `ZONE`: the zone where the reservation exists.
  * `BLOCK_NAME`: the name of the block.



The output for each block is similar to the following example:
    
    
    resource:
      count: 36
      creationTimestamp: '2025-08-04T15:15:07.074-07:00'
      healthInfo:
        degradedSubBlockCount: 2
        healthStatus: DEGRADED
        healthySubBlockCount: 0
      id: '4360924059555106309'
      inUseCount: 35
      kind: compute#reservationBlock
      name: example-res1-block-0001
      physicalTopology:
        block: 1acd074d42cd3be9e4486b524db2e9ab
        cluster: us-central1-cluster-dnkc
        instances:
        -   instanceId: '5815586279631866288'
          physicalHostTopology:
            host: c229b308380a83e0ca345d4a0de05aa7
            subBlock: c02af6bdaeccacef571e0adbe79e8c28
          projectId: 'PROJECT_NUMBER'
        ...
        -   instanceId: '8389759878923049076'
          physicalHostTopology:
            host: '3ac534f00c20e6e0c87c3aaff2705be6'
            subBlock: 'c081876ba0aa2857d608eb30a5b2fa40'
          projectId: 'PROJECT_NUMBER'
      reservationMaintenance:
        instanceMaintenanceOngoingCount: 3
        instanceMaintenancePendingCount: 32
        maintenanceOngoingCount: 2
        maintenancePendingCount: 34
        schedulingType: GROUPED
        subblockInfraMaintenanceOngoingCount: 0
        subblockInfraMaintenancePendingCount: 0
        upcomingGroupMaintenance:
          canReschedule: false
          maintenanceReasons:
          -   PLANNED_UPDATE
          maintenanceStatus: ONGOING
          type: SCHEDULED
          windowEndTime: '2025-09-08T17:00:00.000-07:00'
          windowStartTime: '2025-09-08T13:00:00.000-07:00'
      reservationSubBlockCount: 2
      reservationSubBlockInUseCount: 2
      selfLink: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/reservations/example-res1/reservationBlocks/example-res1-block-0001
      selfLinkWithId: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/reservations/example-res1/reservationBlocks/4360924059555106309
      status: READY
      zone: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a
    

The output includes the following fields for each block:

  * `count`: the total number of compute instances that can be deployed in the block.
  * `healthInfo`: the health information for the block as follows: 
    * `degradedSubBlockCount`: the number of degraded sub-blocks in the block.
    * `healthStatus`: the overall health status of the block.
    * `healthySubBlockCount`: the number of healthy sub-blocks in the block.
  * `inUseCount`: the number of compute instances that are already deployed in the block.
  * `name`: the name of the block.
  * `physicalTopology`: the physical location of the block, which also appears in [ compute instance topology](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/instance-topology), as follows: 
    * `block`: the organization-specific ID of the block.
    * `cluster`: the global name of the cluster.
    * `instances`: a list of the names and physical locations of all the compute instances in the block as follows. (This field only appears when you include the `--full-view=BLOCK_VIEW_FULL` flag.) 
      * `instanceId`: the ID of an instance.
      * `subBlock`: the organization-specific ID of the sub-block where this instance is located.
      * `block`: the organization-specific ID of the block where this instance is located.
  * `reservationSubBlockCount`: the number of sub-blocks in the block.
  * `reservationSubBlockInUseCount`: the number of sub-blocks in the block with at least one compute instance already deployed.



### REST

You can view the blocks in a reservation using the following methods:

  * To view _all_ the available blocks in a reservation, make a `GET` request to the [ `reservationBlocks.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservationBlocks/list): 
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations/RESERVATION_NAME/reservationBlocks
        

  * To view a _specific_ block in a reservation, make a `GET` request to the [ `reservationBlocks.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservationBlocks/get). To also view the name and topology of all the compute instances that are deployed in the block, add the `?view=FULL` query parameter. 
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations/RESERVATION_NAME/reservationBlocks/BLOCK_NAME?view=FULL
        




Replace the following:

  * `PROJECT_ID`: the ID of the project where the reservation exists.
  * `ZONE`: the zone where the reservation exists.
  * `RESERVATION_NAME`: the name of the reservation.
  * `BLOCK_NAME`: the name of the block.



The output for each block is similar to the following:
    
    
    {
      "resource": {
        "kind": "compute#reservationBlock",
        "id": "4360924059555106309",
        "creationTimestamp": "2025-08-04T15:15:07.074-07:00",
        "name": "example-res1-block-0001",
        "zone": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a",
        "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/reservations/example-res1/reservationBlocks/example-res1-block-0001",
        "selfLinkWithId": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/reservations/example-res1/reservationBlocks/4360924059555106309",
        "count": 36,
        "inUseCount": 35,
        "reservationMaintenance": {
          "upcomingGroupMaintenance": {
            "type": "SCHEDULED",
            "canReschedule": false,
            "windowStartTime": "2025-09-08T13:00:00.000-07:00",
            "windowEndTime": "2025-09-08T17:00:00.000-07:00",
            "maintenanceStatus": "ONGOING",
            "maintenanceReasons": [
              "PLANNED_UPDATE"
            ]
          },
          "maintenanceOngoingCount": 2,
          "maintenancePendingCount": 34,
          "schedulingType": "GROUPED",
          "subblockInfraMaintenanceOngoingCount": 0,
          "subblockInfraMaintenancePendingCount": 0,
          "instanceMaintenanceOngoingCount": 3,
          "instanceMaintenancePendingCount": 32
        },
        "status": "READY",
        "physicalTopology": {
          "cluster": "us-central1-cluster-dnkc",
          "block": "1acd074d42cd3be9e4486b524db2e9ab",
          "instances": [
            {
              "instanceId": "5815586279631866288",
              "projectId": "PROJECT_NUMBER",
              "physicalHostTopology": {
                "subBlock": "c02af6bdaeccacef571e0adbe79e8c28",
                "host": "c229b308380a83e0ca345d4a0de05aa7"
              }
            },
            ...
            {
              "instanceId": "8389759878923049076",
              "projectId": "PROJECT_NUMBER",
              "physicalHostTopology": {
                "subBlock": "c081876ba0aa2857d608eb30a5b2fa40",
                "host": "3ac534f00c20e6e0c87c3aaff2705be6"
              }
            }
          ]
        },
        "reservationSubBlockCount": 2,
        "reservationSubBlockInUseCount": 2,
        "healthInfo": {
          "healthStatus": "DEGRADED",
          "healthySubBlockCount": 0,
          "degradedSubBlockCount": 2
        }
      }
    }
    

The output includes the following fields for each block:

  * `name`: the name of the block.
  * `count`: the total number of compute instances that can be deployed in the block.
  * `inUseCount`: the number of compute instances that are already deployed in the block.
  * `physicalTopology`: the physical location of the block, which also appears in [ compute instance topology](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/instance-topology), as follows: 
    * `cluster`: the global name of the cluster.
    * `block`: the organization-specific ID of the block.
    * `instances`: a list of the names and physical locations of all the compute instances in the block as follows. (This field only appears when you include the `?view=FULL` query parameter.) 
      * `instanceId`: the ID of an instance.
      * `subBlock`: the organization-specific ID of the sub-block where this compute instance is located.
      * `block`: the organization-specific ID of the block where this compute instance is located.
  * `reservationSubBlockCount`: the number of sub-blocks in the block.
  * `reservationSubBlockInUseCount`: the number of sub-blocks in the block with at least one compute instance already deployed.
  * `healthInfo`: the health information for the block as follows: 
    * `healthStatus`: the overall health status of the block.
    * `healthySubBlockCount`: the number of healthy sub-blocks in the block.
    * `degradedSubBlockCount`: the number of degraded sub-blocks in the block.



#### View reserved sub-blocks

To list and describe the available sub-blocks in a block of an reservation, use the Google Cloud CLI or REST API. This task helps you determine the following:

  * Which sub-blocks of capacity are in the reserved block.
  * How much capacity is available in each sub-block.
  * The health of each sub-block, including its number of healthy host machines and number of healthy accelerator interconnects.



### gcloud

You can view the sub-blocks in a reservation using the following commands:

  * To view _all_ the available sub-blocks in a block of a reservation, use the [ `gcloud compute reservations sub-blocks list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/sub-blocks/list): 
        
        gcloud compute reservations sub-blocks list RESERVATION_NAME \
            --zone=ZONE \
            --block-name=BLOCK_NAME
        

  * To view a _specific_ the sub-block in a block of a reservation, use the [ `gcloud compute reservations sub-blocks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/sub-blocks/describe): 
        
        gcloud compute reservations sub-blocks describe RESERVATION_NAME \
            --zone=ZONE \
            --block-name=BLOCK_NAME \
            --sub-block-name=SUB-BLOCK_NAME
        




Replace the following:

  * `RESERVATION_NAME`: the name of the reservation.
  * `ZONE`: the zone where the reservation exists.
  * `BLOCK_NAME`: the name of the block.
  * `SUB-BLOCK_NAME`: the name of the sub-block.



The output for each sub-block is similar to the following:
    
    
    count: 18
    creationTimestamp: '2025-07-18T14:50:01.652-07:00'
    healthInfo:
      degradedHostCount: 0
      degradedInfraCount: 0
      healthStatus: HEALTHY
      healthyHostCount: 18
      healthyInfraCount: 1
    id: '6848013619223297894'
    inUseCount: 2
    kind: compute#reservationSubBlock
    name: example-res1-block-0001-subblock-0001
    physicalTopology:
      block: 2b6aa63faa2b60b7ecd3b87ec337f270
      cluster: us-central1-cluster-xvhj
      subBlock: 556a310b49a0b247bc109cc7f997cea2
    reservationSubBlockMaintenance:
      schedulingType: GROUPED
    selfLink: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/reservations/example-res1/reservationBlocks/example-res1-block-0001/reservationSubBlocks/example-res1-block-0001-subblock-0001
    selfLinkWithId: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/reservations/example-res1/reservationBlocks/example-res1-block-0001/reservationSubBlocks/6848013619223297894
    status: READY
    zone: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a
    

The output includes the following fields for each sub-block:

  * `count`: the total number of compute instances that can be deployed in the sub-block.
  * `healthInfo`: the health information for the sub-block as follows: 
    * `degradedHostCount`: the number of degraded host machines in the sub-block.
    * `degradedInfraCount`: the number of degraded accelerator interconnects in the sub-block.
    * `healthStatus`: the overall health status of the sub-block.
    * `healthyHostCount`: the number of healthy host machines in the sub-block.
    * `healthyInfraCount`: the number of healthy accelerator interconnects in the sub-block.
  * `inUseCount`: the number of compute instances that are already deployed in the sub-block.
  * `name`: the name of the sub-block.
  * `physicalTopology`: the physical location of the sub-block, which also appears in [ compute instance topology](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/instance-topology), as follows: 
    * `block`: the organization-specific ID of the block.
    * `cluster`: the global name of the cluster.
    * `subblock`: the organization-specific ID of the sub-block.



### REST

You can view the sub-blocks in a reservation using the following methods:

  * To view _all_ the available sub-blocks in a block of a reservation, make a `GET` request to the [ `reservationSubBlocks.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservationSubBlocks/list): 
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations/RESERVATION_NAME/reservationBlocks/BLOCK_NAME/reservationSubBlocks
        

  * To view a _specific_ sub-block in a block of a reservation, make a `GET` request to the [ `reservationSubBlocks.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservationSubBlocks/get): 
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations/RESERVATION_NAME/reservationBlocks/BLOCK_NAME/reservationSubBlocks/SUB-BLOCK_NAME
        




Replace the following:

  * `PROJECT_ID`: the ID of the project where the reservation exists.
  * `ZONE`: the zone where the reservation exists.
  * `RESERVATION_NAME`: the name of the reservation.
  * `BLOCK_NAME`: the name of the block.
  * `SUB-BLOCK_NAME`: the name of the sub-block.



The output for each sub-block is similar to the following:
    
    
    {
      "resource": {
        "kind": "compute#reservationSubBlock",
        "id": "5679680646666817028",
        "creationTimestamp": "2025-08-04T15:15:07.625-07:00",
        "name": "example-res1-block-0001-subblock-0001",
        "zone": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a",
        "selfLink": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/reservations/example-res1/reservationBlocks/example-res1-block-0001/reservationSubBlocks/example-res1-block-0001-subblock-0001",
        "selfLinkWithId": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/reservations/example-res1/reservationBlocks/example-res1-block-0001/reservationSubBlocks/5679680646666817028",
        "count": 18,
        "inUseCount": 18,
        "reservationSubBlockMaintenance": {
          "upcomingGroupMaintenance": {
            "type": "SCHEDULED",
            "canReschedule": false,
            "windowStartTime": "2025-09-08T13:00:00.000-07:00",
            "windowEndTime": "2025-09-08T17:00:00.000-07:00",
            "maintenanceStatus": "ONGOING",
            "maintenanceReasons": [
              "PLANNED_UPDATE"
            ]
          },
          "maintenanceOngoingCount": 2,
          "maintenancePendingCount": 16,
          "schedulingType": "GROUPED",
          "subblockInfraMaintenanceOngoingCount": 0,
          "subblockInfraMaintenancePendingCount": 0,
          "instanceMaintenanceOngoingCount": 3,
          "instanceMaintenancePendingCount": 15
        },
        "status": "READY",
        "physicalTopology": {
          "cluster": "us-central1-cluster-dnkc",
          "block": "1acd074d42cd3be9e4486b524db2e9ab",
          "subBlock": "c081876ba0aa2857d608eb30a5b2fa40"
        },
        "healthInfo": {
          "healthStatus": "DEGRADED",
          "healthyHostCount": 16,
          "degradedHostCount": 2,
          "healthyInfraCount": 1,
          "degradedInfraCount": 0
        }
      }
    }
    

The output includes the following fields for each sub-block:

  * `name`: the name of the sub-block.
  * `count`: the total number of compute instances that can be deployed in the sub-block.
  * `inUseCount`: the number of compute instances that are already deployed in the sub-block.
  * `physicalTopology`: the physical location of the sub-block, which also appears in [ compute instance topology](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/instance-topology), as follows: 
    * `cluster`: the global name of the cluster.
    * `block`: the organization-specific ID of the block.
    * `subblock`: the organization-specific ID of the sub-block.
  * `healthInfo`: the health information for the sub-block as follows: 
    * `healthStatus`: the overall health status of the sub-block.
    * `healthyHostCount`: the number of healthy host machines in the sub-block.
    * `degradedHostCount`: the number of degraded host machines in the sub-block.
    * `healthyInfraCount`: the number of healthy accelerator interconnects in the sub-block.
    * `degradedInfraCount`: the number of degraded accelerator interconnects in the sub-block.



## What's next

  * To learn about creating compute instances and clusters, see [Compute instance and cluster creation overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview).
  * To view your reservation consumption, see [View reservation consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-view#view_reservation_consumption).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
