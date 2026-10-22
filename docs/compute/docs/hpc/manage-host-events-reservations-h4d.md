---
url: https://docs.cloud.google.com/compute/docs/hpc/manage-host-events-reservations-h4d/
title: Manage host events across reservations \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:11.855770+00:00
---

# Manage host events across reservations  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/hpc/manage-host-events-reservations-h4d/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manage host events across reservations Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to use the host maintenance features that are available with your reserved blocks of capacity. It explains how to monitor, plan for, and perform scheduled maintenance on your cluster of H4D instances. To manage maintenance on your virtual machine (VM) instances instead, see [Monitor and plan for a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event). 

You can proactively manage upcoming [maintenance host events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview) on your reserved blocks of capacity, whether VMs are running on them or not. This approach helps you minimize disruptions and maintain optimal performance. 

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

To get the permissions that you need to manage host maintenance events across reservations, ask your administrator to grant you the following IAM roles: 

  * [Compute Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.admin) (`roles/compute.admin`) on the project
  * For read-only access to System Event audit logs: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on the project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage host maintenance events across reservations. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage host maintenance events across reservations:

  * To start host maintenance for a reservation: `compute.reservations.performMaintenance` on the project 
  * To start host maintenance for a reservation block: `compute.reservationBlocks.performMaintenance` on the project
    * To view a list reservations 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Overview

To optimize the maintenance of your reserved blocks of capacity, complete the following steps:

  1. Set up notification alerts. Create log-based alerts to get notified about scheduled, started, or completed maintenance events for a reservation or a reservation block. This approach helps you proactively plan your activities and avoid unexpected downtime.

  2. Manage maintenance across blocks of capacity. View and, if needed, manually start maintenance across your reservations or reservation blocks. This process helps you increase the resilience of your workloads to host errors, prevent downtime, and ensure that your applications remain available.




For more information about the frequency and maintenance behavior of H4D machine types, see [Maintenance experience for H4D instances](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_maintenance).

## Set up notification alerts for reservations

You can get notified about scheduled, started, or completed maintenance events for a reservation or reservation block by [creating log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).

To create an alert for the maintenance events of a reservation or a reservation block, complete the following procedure. Repeat this procedure for each alert that you want to create.

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Click the **Show query** toggle to the on position.

  3. In the **Query** pane, build one of the following queries. These queries filter log entries to identify specific maintenance events. Repeat this procedure for each query you want to create.

     * **Receive maintenance alerts for a reservation** :

       * To receive alerts when maintenance is scheduled:
             
             protoPayload.methodName="compute.reservations.upcomingGroupMaintenance" severity>=DEFAULT
             protoPayload.status.message =~ "scheduled"
             

       * To receive alerts when maintenance has completed:
             
             protoPayload.methodName="compute.reservations.completedGroupMaintenance" severity>=DEFAULT
             protoPayload.status.message =~ "completed"
             

     * **Receive maintenance alerts for a reservation block** :

       * To receive alerts when maintenance is scheduled:
             
             protoPayload.methodName="compute.reservations.block.upcomingGroupMaintenance" severity>=DEFAULT
             protoPayload.status.message =~ "scheduled"
             

       * To receive alerts when maintenance has started:
             
             protoPayload.methodName="compute.reservations.block.startGroupMaintenance" severity>=DEFAULT
             protoPayload.status.message =~ "started"
             

       * To receive alerts when maintenance has completed:
             
             protoPayload.methodName="compute.reservations.block.completedGroupMaintenance" severity>=DEFAULT
             protoPayload.status.message =~ "completed"
             

  4. To validate the query, click **Run query**. If the query is valid, then the **Query results** pane displays log entries that match the query.

  5. In the **Query** results toolbar, click the **Actions** list, and then select add_alert **Create log alert**. The **Create logs-based alert policy** pane appears.

  6. In the **Alert details** section, do the following:

     1. In the **Alert Policy Name** field, enter a name for the policy.

     2. In the **Policy severity level** list, select **Warning** (or a higher severity).

     3. Click **Next**.

  7. In the **Choose logs to include in the alert** section, click **Next**.

  8. In the **Set notification frequency and autoclose duration** section, specify the following:

     1. In the **Time between notifications** list, select how often you want to be notified.

     2. In the **Incident autoclose duration** list, select after how long Cloud Logging stops sending notifications and automatically closes the incident.

     3. Click **Next**.

  9. In the **Who should be notified?** section, specify a [notification channel](https://docs.cloud.google.com/monitoring/support/notification-options) for Logging to send notifications to.

  10. Click **Save**.




## Manage maintenance across reservations

You can view and control maintenance for your reservations and reservation blocks as follows:

  * To check the state and scheduled time of upcoming maintenance for your reservations or reservation blocks, view maintenance state.

  * To manually start maintenance on a reservation or reservation block, rather than waiting for the scheduled maintenance date and time, manually start maintenance.

  * To manage how early you want to receive notifications when a VM's host requires emergency, unplanned maintenance after a host error or faulty host report, manage hardware emergency maintenance notifications.




### View maintenance state

You can view the upcoming maintenance state for a reservation or a reservation block by checking the value of the `upcomingGroupMaintenance` field in the reservation metadata. If a reservation lacks the `upcomingGroupMaintenance` field, then no maintenance is scheduled for the reservation or reservation block. For more information about the fields in `upcomingGroupMaintenance`, see [Maintenance status definitions](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event#maintenance-status-definitions).

Additionally, if maintenance is scheduled for a reservation block, the `upcomingGroupMaintenance` field contains the `maintenanceReasons` field. This field describes why maintenance was scheduled for your reservation block, as described in the following table:

Maintenance type | Maintenance reason | VMs state  
---|---|---  
Planned maintenance for regular maintenance | 

  * **`PLANNED_UPDATE`** : planned infrastructure maintenance
  * **`PLANNED_NETWORK_UPDATE`** : planned network maintenance

| Applies to running, stopped, or suspended VMs.  
Unplanned, emergency maintenance | 

  * **`FAILURE_DISK`** : unplanned maintenance scheduled due to an error with a disk attached to a VM. 
  * **`FAILURE_INFRA`** : unplanned maintenance scheduled due to an error with the infrastructure.
  * **`FAILURE_INTERFACE`** : unplanned maintenance scheduled due to an error with the NIC.
  * **`FAILURE_MEMORY`** : unplanned maintenance scheduled due to an error with a VM's memory. 
  * **`FAILURE_NETWORK`** : unplanned maintenance scheduled due to an error with the network.

| Applies only to running VMs.  
  
To view the `maintenanceReasons` field in a reservation block or sub-block, you must use the gcloud CLI or REST API. Otherwise, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. In the **Maintenance status** column, Compute Engine displays the maintenance state of your reservations. If you don't see this column in the **On-demand reservations** table, then click view_column **Column display options** , select the **Maintenance status** checkbox, and then click **OK**.

  3. To view the maintenance state of a reservation block, complete the following steps:

     1. In the **Name** column, click the name of the reservation. A page that gives the details of the reservation appears.

     2. In the **Blocks** table, in the **Maintenance** column, Compute Engine displays the maintenance state of the blocks within the reservation.




###  gcloud 

  1. To view the maintenance state of a reservation, use the [`gcloud compute reservations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/describe) with the `--flatten` flag set to `resourceStatus.reservationMaintenance`:
         
         gcloud compute reservations describe RESERVATION_NAME \
             --flatten=resourceStatus.reservationMaintenance \
             --zone=ZONE
         

Replace the following:

     * `RESERVATION_NAME`: the name of the reservation.

     * `ZONE`: the zone where the reservation exists.

The output is similar to one of the following:

     * If maintenance is scheduled for your reservation, then the output is similar to the following:
           
           ---
           maintenanceOngoingCount: 0
           maintenancePendingCount: 6
           schedulingType: GROUPED
           upcomingGroupMaintenance:
             canReschedule: true
             maintenanceStatus: PENDING
             type: UNSCHEDULED
             windowEndTime: '2025-11-13T14:00:00.000-08:00'
             windowStartTime: '2025-11-13T12:00:00.000-08:00'
           

If the `schedulingType` field is set to `INDEPENDENT`, then the `upcomingGroupMaintenance` field doesn't contain the `windowStartTime` and `windowEndTime` fields.

     * If maintenance isn't scheduled for your reservation, then the output is similar to the following:
           
           ---
           schedulingType: GROUPED
           

  2. If maintenance is scheduled for your reservation, then, to view the maintenance state of the blocks within the reservation, use the [`gcloud compute reservations blocks list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/blocks/list):
         
         gcloud compute reservations blocks list RESERVATION_NAME \
             --zone=ZONE
         

If maintenance is scheduled or ongoing for a reservation block, then the output is similar to the following:
         
         ---
         ...
         name: example-fr-h4d-dense-1-block-0001
         ...
         reservationBlockMaintenance:
           maintenanceOngoingCount: 0
           maintenancePendingCount: 6
           schedulingType: GROUPED
           upcomingGroupMaintenance:
             canReschedule: true
             maintenanceReasons:
             - PLANNED_UPDATE
             - PLANNED_NETWORK_UPDATE
             maintenanceStatus: PENDING
             type: UNSCHEDULED
             windowEndTime: '2025-11-13T14:00:00.000-08:00'
             windowStartTime: '2025-11-13T12:00:00.000-08:00'
         ...
         ---
         ...
         name: example-fr-h4d-dense-1-block-0002
         ...
         schedulingType: GROUPED
         ...
         




###  REST 

  1. To view the maintenance state of your reservations, make a `GET` request to one of the following methods:

     * To view reservations across all zones, use the [`reservations.aggregatedList` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/aggregatedList).

     * To view reservations in a specific zone, use the [`reservations.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/list).

In the request URL, include the following query parameters:

     * To only show the name, reserved machine type, and maintenance status of a reservation, include the `fields` query parameter set to `items.name,items.specificReservation.instanceProperties.machineType,items.resourceStatus.reservationMaintenance`.

     * To only filter by reservations that specify a specific machine type, include the `filter` query parameter set to `specificReservation.instanceProperties.machineType:MACHINE_TYPE` by using URL-encoded values.

For example, to view reservations across all zones, make a `GET` request as follows:
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/reservations?fields=items.name,items.specificReservation.instanceProperties.machineType,items.resourceStatus.reservationMaintenance&filter=specificReservation.instanceProperties.machineType%3AMACHINE_TYPE
    

Replace the following:

     * `PROJECT_ID`: the ID of the project where the reservations exist.

     * `MACHINE_TYPE`: the reserved machine type that you want to filter your reservations by.

If maintenance is scheduled or ongoing for a reservation, then the output is similar to the following:
    
    {
      "items": [
        {
          "specificReservation": {
            "instanceProperties": {
              "machineType": "MACHINE_TYPE"
            }
          },
          "name": "example-reservation",
          "resourceStatus": {
            "reservationMaintenance": {
              maintenanceOngoingCount: 0,
              maintenancePendingCount: 6,
              "schedulingType": "GROUPED",
              "upcomingGroupMaintenance": {
                "type": "SCHEDULED",
                "canReschedule": true,
                "windowStartTime": "2025-11-13T12:00:00.000-08:00",
                "windowEndTime": "2025-11-13T14:00:00.000-08:00",
                "maintenanceStatus": "PENDING"
              }
            }
          }
        },
        ...
      ]
    }
    

Optionally, to further narrow down a list of VMs, set the `filter` query parameter to a different [filter expression](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/list#body.QUERY_PARAMETERS.filter).

  2. If maintenance is scheduled for your reservation, then, to view the maintenance state of the blocks within the reservation, make a `GET` request to the [`reservationBlocks.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservationBlocks/list). In the request URL, include the `fields` query parameter set to `items.name,items.reservationMaintenance`:
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations/RESERVATION_NAME/reservationBlocks?fields=items.name,items.reservationMaintenance
         

Replace `RESERVATION_NAME` with the name of the reservation.

If maintenance is scheduled or ongoing for a reservation block, then the output is similar to the following:
         
         {
           "items": [
             {
               "name": "example-fr-h4d-dense-1-block-0001",
               "reservationBlockMaintenance": {
                 "maintenanceOngoingCount": 0,
                 "maintenancePendingCount": 6,
                 "schedulingType": "GROUPED",
                 "upcomingGroupMaintenance": {
                   "type": "SCHEDULED",
                   "canReschedule": true,
                   "windowStartTime": "2025-11-13T12:00:00.000-08:00",
                   "windowEndTime": "2025-11-13T14:00:00.000-08:00",
                   "maintenanceStatus": "PENDING",
                   "maintenanceReasons": [
                     "PLANNED_UPDATE",
                     "PLANNED_NETWORK_UPDATE"
                   ]
                 }
               }
             },
             ...
           ]
         }
         

If the `schedulingType` field is set to `INDEPENDENT` for a block, then the `upcomingGroupMaintenance` field doesn't contain the `windowStartTime` and `windowEndTime` fields.




### Manually start maintenance

You can manually start maintenance for your reservations or reservation blocks instead of waiting for the scheduled time. This action helps you more proactively control disruptions to your workloads.

Depending on the maintenance state of a reservation or reservation block, the following occurs:

Maintenance state | Description | What you see  
---|---|---  
Scheduled | Compute Engine has scheduled maintenance for the reservation. You can manually start maintenance before the scheduled time. | 

  * In the Google Cloud console, the maintenance state shows as **Ready to run - will run on DATE**.
  * In the gcloud CLI or REST API, Compute Engine sets the `maintenanceStatus` field to `PENDING`.

  
In progress | Maintenance is underway. You can't reschedule it. | 

  * In the Google Cloud console, the maintenance state shows as **Running**.
  * In the gcloud CLI or REST API, Compute Engine sets the `maintenanceStatus` field to `ONGOING`.

  
Complete | Maintenance is finished. Compute Engine has removed all maintenance notifications from the VM. | 

  * In the Google Cloud console, the maintenance state shows as **—**.
  * In the gcloud CLI or REST API, the `maintenanceStatus` field doesn't exist.

  
**Important:** If you [manually start maintenance on individual VMs](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events#start-maintenance) that exist on a reserved block, then the maintenance state of the reservation or reservation block might change from `PENDING` to `ONGOING`, and then back to `PENDING`. This process repeats until maintenance completes on all VMs that exist in a reservation or reservation block.

To manually start maintenance on specific hosts within a reservation block, use the gcloud CLI or REST API. Otherwise, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Reservations** page.

[Go to Reservations](https://console.cloud.google.com/compute/reservations)

  2. In the **Name** column, click the name of a reservation. A page that gives the details of the reservation appears.

  3. Click **Run maintenance** , and then select one of the following options:

     * To start maintenance on all blocks, select **All capacity**.

     * To start maintenance only on blocks with running VMs, select **In-use capacity**.

     * To start maintenance only on unused blocks and blocks with stopped or suspended VMs, select **Unused capacity**.

  4. To confirm, click **Ok**.




###  gcloud 

  * To start maintenance on a reservation, use the [`gcloud compute reservations perform-maintenance` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/perform-maintenance):
        
        gcloud compute reservations perform-maintenance RESERVATION_NAME \
            --scope=RESERVATION_MAINTENANCE_SCOPE \
            --zone=ZONE
        

  * To start maintenance on a reservation block, use the [`gcloud compute reservations blocks perform-maintenance` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/blocks/perform-maintenance):
        
        gcloud compute reservations blocks perform-maintenance RESERVATION_NAME \
            --block-name=BLOCK_NAME \
            --scope=BLOCK_MAINTENANCE_SCOPE \
            --zone=ZONE
        

Replace the following:

  * `RESERVATION_NAME`: the name of the reservation.

  * `RESERVATION_MAINTENANCE_SCOPE`: the maintenance scope for the reservation. Specify one of the following values:

    * To start maintenance on all blocks: `all`

    * To start maintenance only on blocks with running VMs: `running`

    * To start maintenance only on unused blocks and blocks with stopped or suspended VMs: `unused`

  * `BLOCK_NAME`: the name of a block that exists within the reservation.

  * `BLOCK_MAINTENANCE_SCOPE`: the maintenance scope for the reservation block. Specify one of the following values:

    * To start maintenance on all hosts: `all`

    * To start maintenance only on hosts with running VMs: `running`

    * To start maintenance only on unused hosts and hosts with stopped or suspended VMs: `unused`

  * `ZONE`: the zone where the reservation exists.




###  REST 

  * To start maintenance on a reservation, make a `POST` request to the [`reservations.performMaintenance` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/performMaintenance):
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations/RESERVATION_NAME/performMaintenance
        
        {
          "maintenanceScope": "RESERVATION_MAINTENANCE_SCOPE"
        }
        

  * To start maintenance on a reservation block, make a `POST` request to the [`reservationBlocks.performMaintenance` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservationBlocks/performMaintenance):
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations/RESERVATION_NAME/reservationBlocks/BLOCK_NAME/performMaintenance
        
        {
          "maintenanceScope": "BLOCK_MAINTENANCE_SCOPE"
        }
        




Replace the following:

  * `PROJECT_ID`: the ID of the project where Compute Engine automatically created the reservation.

  * `ZONE`: the zone where the reservation exists.

  * `RESERVATION_NAME`: the name of the reservation.

  * `RESERVATION_MAINTENANCE_SCOPE`: the maintenance scope for the reservation. Specify one of the following values:

    * To start maintenance on all blocks: `ALL`

    * To start maintenance only on blocks with running VMs: `RUNNING`

    * To start maintenance only on unused blocks and blocks with stopped or suspended VMs: `UNUSED`

  * `BLOCK_NAME`: the name of a block that exists within the reservation.

  * `SUB_BLOCK_NAME`: the name of a sub-block that exists within the reservation block.

  * `BLOCK_MAINTENANCE_SCOPE`: the maintenance scope for the reservation block. Specify one of the following values:

    * To start maintenance on all hosts: `ALL`

    * To start maintenance only on hosts with running VMs: `RUNNING`

    * To start maintenance only on unused hosts and hosts with stopped or suspended VMs: `UNUSED`




### Manage hardware emergency maintenance notifications

After a VM encounters an host error, or you report its host as faulty, the VM's host requires emergency, unplanned maintenance. By default, Compute Engine provides a few hours of advance notice when it schedules this type of maintenance. For reserved hosts, you can enable emergency maintenance notifications to increase this notice period to at least seven days. This approach helps you more proactively control disruptions to your workloads.

**Note:** After you enable this feature and receive a notification, you can either let Compute Engine start maintenance at the scheduled date and time, or you can manually start maintenance before the scheduled date.

To enable or disable hardware emergency maintenance notifications for a reservation, select one of the following options:

###  gcloud 

  * To enable hardware emergency maintenance notifications for a reservation, use the [`gcloud compute reservations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/update) with the `--enable-emergent-maintenance` flag:
        
        gcloud compute reservations update RESERVATION_NAME \
            --enable-emergent-maintenance \
            --zone=ZONE
        

  * To disable hardware emergency maintenance notifications for a reservation, use the [`gcloud compute reservations update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/update) with the `--no-enable-emergent-maintenance` flag:
        
        gcloud compute reservations update RESERVATION_NAME \
            --no-enable-emergent-maintenance \
            --zone=ZONE
        




Replace the following:

  * `RESERVATION_NAME`: the name of the reservation.

  * `ZONE`: the zone where the reservation exists.




###  REST 

To enable or disable hardware emergency maintenance notifications for a reservation, make a `PATCH` request to the [`reservations.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/reservations/update). In the request URL, include the `paths` query parameter set to `enableEmergentMaintenance`.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/reservations/RESERVATION_NAME?paths=enableEmergentMaintenance
    
    {
      "name": "RESERVATION_NAME",
      "enableEmergentMaintenance": EMERGENCY_MAINTENANCE_NOTIFICATIONS
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the reservation exists.

  * `ZONE`: the zone where the reservation exists.

  * `RESERVATION_NAME`: the name of the reservation.

  * `EMERGENCY_MAINTENANCE_NOTIFICATIONS`: specify one of the following values:

    * To enable notifications: `true`

    * To disable notifications: `false`




## What's next

  * Learn about [Local SSD data persistence](https://docs.cloud.google.com/compute/docs/disks/local-ssd#data_persistence) during host events

  * Learn how to perform [Local SSD data backup](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_backup) to preserve data

  * Learn about [Maintenance status definitions](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event#maintenance-status-definitions) when monitoring host maintenance events




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
