---
url: https://docs.cloud.google.com/tpu/docs/all-capacity-maintenance-events/
title: Manage maintenance events with TPUs in All Capacity mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:39:22.507189+00:00
---

# Manage maintenance events with TPUs in All Capacity mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/all-capacity-maintenance-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage maintenance events with TPUs in All Capacity mode

**Caution:** The [Compute Engine Service Level Agreement (SLA)](https://cloud.google.com/compute/sla) doesn't apply to All Capacity mode TPUs.

All TPU hosts go through regular maintenance. In All Capacity mode, you can plan for upcoming maintenance events and initiate the maintenance operations when you want on all of your capacity. You can update your used and unused capacity simultaneously or separately. You can also perform maintenance at a VM, a sub-block, a block, or reservation level. This fine-grained maintenance control lets you create an optimal maintenance sequence, and schedule maintenance operations to minimize business impact.

All Capacity mode only supports "grouped maintenance", which means the maintenance operations for all VM instances within a reservation are scheduled at the same time. All TPU VMs in a reservation have the same maintenance window. However, the maintenance operations can be carried out separately at the host, sub-block, block, or reservation level. Maintenance notifications are sent approximately 90 days in advance. Maintenance won't be carried out more frequently than once every 90 days.

If you're using All Capacity mode on GKE and you're using multi-host TPU slice node pools, we recommend you delete the GKE node pool before manually starting the pending maintenance for any hosts in that node pool. Once the maintenance has been executed for all hosts in the original node pool, you can recreate the node pool.

The following is an example timeline for a TPU host maintenance event:

  1. Maintenance is scheduled. A notification is sent to you that the host will be updated within 90 days.
  2. You can choose to manually update the host with 90 days.
  3. After 90 days, the maintenance operation is run without exception.
  4. If another maintenance event is scheduled before the previous event is run, the second operation is scheduled to run after 180 days, 90 days after the initial maintenance event is scheduled to occur.



## Set up maintenance notification alerts for physical capacity

Compute Engine sends you Cloud Logging events for scheduled, started, or completed maintenance. These maintenance events stay in your logs so you can build log queries to get a historical view of the maintenance for your capacity. You can also get notified about future maintenance events for a reservation, block, or sub-block by creating log-based alert policies.

To create an alert for maintenance events on your physical capacity:

  1. In the Google Cloud console, go to the [Logs Explorer](https://console.cloud.google.com/logs).
  2. Make sure **Show query** is turned on.
  3. In the query pane, build a query in the format listed in the following sections. Replace the corresponding parameter placeholder accordingly and run the query.
  4. Once you verify the returned results match what you want, you can create alerts by selecting **Create log alert** from the **Actions** drop-down in the query Results toolbar and provide the requested information.



### Query for upcoming maintenance

The following is an example query for querying for upcoming maintenance:
    
    
    protoPayload.methodName="compute.CAPACITY_COMPONENT.upcomingGroupMaintenance" severity>=DEFAULT
    protoPayload.resourceName="projects/shared-reservation-project/reservations/RESOURCE_NAME"
    protoPayload.status.message =~ "scheduled"

Replace `CAPACITY_COMPONENT` and `RESOURCE_NAME` with the following values:

Receive upcoming maintenance notification for | `CAPACITY_COMPONENT` | `RESOURCE_NAME`  
---|---|---  
All reservations | `reservations` | Omit RESOURCE_NAME  
A specific reservation | `reservations` | `YOUR_RESERVATION_NAME`  
Blocks across all reservations | `reservations.blocks` | Omit RESOURCE_NAME  
A specific block | `reservations.blocks` | `YOUR_RESERVATION_NAME/reservationBlocks/YOUR_RESERVATION_BLOCK_ID`  
Sub-blocks across all reservations | `reservations.blocks.subblocks` | Omit RESOURCE_NAME  
A specific sub-block | `reservations.blocks.subblocks` | `YOUR_RESERVATION_NAME/reservationBlocks/YOUR_RESERVATION_BLOCK_ID/reservationSubBlocks/YOUR_RESERVATION_SUBBLOCK_ID`  
  
### Query for maintenance window opening
    
    
    protoPayload.methodName="compute.reservations.CAPACITY_COMPONENT.startGroupMaintenance" severity>=DEFAULT
    protoPayload.status.message =~ "started"

Replace `CAPACITY_COMPONENT` with one of the following values:

Receive notification for a maintenance window opening for | `CAPACITY_COMPONENT`  
---|---  
Blocks in a reservations | `reservations.blocks`  
Sub-blocks in a reservation | `reservations.blocks.subblocks`  
  
### Query for completed maintenance

The following is an example query for querying for completed maintenance:
    
    
    protoPayload.methodName="compute.reservations.CAPACITY_COMPONENT.completedGroupMaintenance" severity>=DEFAULT
    protoPayload.resourceName="projects/YOUR_RESERVATION_PROJECT/reservations/RESOURCE"
    protoPayload.status.message =~ "completed"

Replace `CAPACITY_COMPONENT` and `RESOURCE_NAME` with the following values:

Receive notification for completed maintenance for | `CAPACITY_COMPONENT` | RESOURCE_NAME  
---|---|---  
All reservations | `reservations` | Omit RESOURCE_NAME  
A specific reservation | `reservations` | `YOUR_RESERVATION_NAME`  
Blocks across all reservations | `reservations.blocks` | Omit RESOURCE_NAME  
A specific block | `reservations.blocks` | `YOUR_RESERVATION_NAME/reservationBlocks/YOUR_RESERVATION_BLOCK_ID`  
Sub-blocks across all reservations | `reservations.blocks.subblocks` | Omit RESOURCE_NAME  
A specific sub-block | `reservations.blocks.subblocks` | `YOUR_RESERVATION_NAME/reservationBlocks/YOUR_RESERVATION_BLOCK_ID/reservationSubBlocks/YOUR_RESERVATION_SUBBLOCK_ID`  
  
## View the maintenance status of physical capacity

You can find out the maintenance status of your capacity through Cloud Logging, APIs, and CLI. Maintenance status information is provided at four levels: reservation, block, sub-block, and host.

###  Cloud Logging 

The following example JSON was generated in response to this example query:
    
    
    {
    "protoPayload": {
      "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
      "status": {
        "message": "Maintenance is scheduled for this block in reservation
        YOUR_RESERVATION. Review the maintenance schedule
        by describing the reservation and block via gcloud CLI"
      },
      "metadata": {
        "type":SCHEDULED
        "canReschedule":True
        "windowGroupStartTime": '2025-09-12T13:00:00.000-07:00',
        "windowGroupEndTime": '2025-09-12T17:00:00.000-07:00',
        "maintenanceGroupStatus":PENDING,
        "maintenancePendingCount":128 # Used and Unused Machines,
        "instanceMaintenancePendingCount": 64 # VMs Only
      },
    "methodName": "compute.reservations.block.upcomingGroupMaintenance",
    …
    },
    }

###  gcloud 
    
    
    gcloud compute reservations blocks describe YOUR_RESERVATION \
    --block-name=YOUR_BLOCK \
    --project=YOUR_PROJECT \
    --zone=YOUR_ZONE

The output is similar to the following:
    
    
    count: 128 # Host count
    creationTimestamp: '2025-08-19T18:23:32.825-07:00'
    id: '6404259976725386932'
    inUseCount: 64 # In use host count
    **kind: compute#reservationBlock**
    **name: exr1-block-0002**
    …
    reservationMaintenance:
    **instanceMaintenanceOngoingCount: 0**
    **instanceMaintenancePendingCount: 64 # VMs Only**
    **maintenanceOngoingCount: 0**
    **maintenancePendingCount: 128 # Used and Unused Hosts**
    schedulingType: GROUPED
    subblockInfraMaintenanceOngoingCount: 0
    subblockInfraMaintenancePendingCount: 0
    **upcomingGroupMaintenance:**
      **canReschedule: true**
      **maintenanceReasons:**
      **- PLANNED_UPDATE**
      **maintenanceStatus: PENDING**
      **type: SCHEDULED**
      **windowEndTime: '2025-09-12T17:00:00.000-07:00'**
      **windowStartTime: '2025-09-12T13:00:00.000-07:00'**
    …

The following values from the output describe the maintenance information:

  * `reservationMaintenance.instanceMaintenanceOngoingCount`: the number of used hosts being updated
  * `reservationMaintenance.instanceMaintenancePendingCount`: the number of used hosts pending maintenance
  * `reservationMaintenance.maintenanceOngoingCount`: the number of unused hosts being updated
  * `reservationMaintenance.maintenancePendingCount`: the number of unused hosts pending maintenance
  * `reservationMaintenance.upcomingGroupMaintenance.maintenanceReasons`: the type of maintenance
  * `reservationMaintenance.upcomingGroupMaintenance.maintenanceStatus`: the status of the maintenance operation
  * `reservationMaintenance.upcomingGroupMaintenance.type`: the type of maintenance (`SCHEDULED` for planned maintenance or `UNSCHEDULED` for unplanned or emergency maintenance)
  * `reservationMaintenance.upcomingGroupMaintenance.windowEndTime`: the scheduled end of the time window for the maintenance operation
  * `reservationMaintenance.upcomingGroupMaintenance.windowStartTime`: the scheduled start of the time window for the maintenance operation



## Set up maintenance notification alerts for TPU VMs

You can create alerts for maintenance events on your TPU VMs:

  1. In the Google Cloud console, go to the [Logs Explorer](https://console.cloud.google.com/logs).
  2. Set the **Show query** toggle to the "on" position.
  3. In the query pane, build a query in the format listed in the following sections.
  4. Once you verify the returned results match what you want, you can create an alert by clicking the **Actions** drop-down, select **Create log alert** and complete the information from the **Create logs-based alert policy** pane.



#### Query for when maintenance is scheduled for a VM instance
    
    
    protoPayload.methodName="compute.instances.upcomingMaintenance" severity>=DEFAULT
    protoPayload.status.message =~ "scheduled"

#### Query for when maintenance window has opened for a VM instance
    
    
    protoPayload.methodName="compute.instances.upcomingMaintenance" severity>=DEFAULT
    protoPayload.status.message =~ "ongoing"

#### Query for maintenance started for VM instances
    
    
    protoPayload.methodName="compute.instances.blocks.terminateOnHostMaintenance" severity>=DEFAULT

#### Query for when maintenance has completed for a VM instance
    
    
    protoPayload.methodName="compute.instances.upcomingMaintenance" severity>=DEFAULT
    protoPayload.status.message =~ "completed"

## View the maintenance status of a Cloud TPU VM

You can retrieve the maintenance status of a Cloud TPU VM with the Compute Engine instance API or with a `curl` command from within the guest operating system.

### Describe an instance

###  gcloud 
    
    
    gcloud compute instances describe INSTANCE --zone ZONE

This command returns output like the following:
    
    
    …
    upcomingMaintenance:{
    "type":"SCHEDULED"
    "canReschedule":True
    "windowStartTime": '2025-09-12T13:00:00.000-07:00'
    "windowEndTime": '2025-09-12T17:00:00.000-07:00'
    "latestWindowStartTime": '2025-09-12T13:00:00.000-07:00'
    "maintenanceStatus":"PENDING"
    ...

### curl
    
    
    curl http://metadata.google.internal/computeMetadata/v1/instance/upcoming-maintenance?alt=json -H "Metadata-Flavor: Google"

This command returns output like the following:
    
    
    {
    "maintenanceType":"SCHEDULED"
    "canReschedule":True
    "windowStartTime": '2025-09-12T13:00:00.000-07:00'
    "windowEndTime": '2025-09-12T17:00:00.000-07:00'
    "latestWindowStartTime": '2025-09-12T13:00:00.000-07:00'
    "maintenanceStatus":"PENDING"
    }

You can also find maintenance notifications in Cloud Logging.

The following is an example log message of a pending planned maintenance. For an example query, see [View the maintenance status of physical capacity](https://docs.cloud.google.com/tpu/docs/all-capacity-maintenance-events#vm-query-scheduled-maintenance).
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "status": {
          "message": "Maintenance is scheduled for this instance. Review the maintenance schedule by describing the VM with gcloud CLI or querying the http://metadata.google.internal/computeMetadata/v1/instance/upcoming-maintenance metadata key."
        },
        "metadata": {
          "canReschedule": true
          "latestWindowStartTime": "2024-01-01:00:00:00PST"
          "maintenanceStatus": "PENDING"
          "type": "SCHEDULED"
          "windowEndTime": "2024-01-01:00:02:00PST"
          "windowStartTime": "2024-01-01:00:00:00PST"
        },
    },
      "operation": {
        "id": "systemevent-1702539760425-60c736da2db40-701ddf19-b5424b20",
        "producer": "compute.instances.upcomingMaintenance",
        "first": true,
        "last": false
      },
    }

The following example is a log message of an ongoing unplanned maintenance, for an example query, see [Query for when a maintenance window is open](https://docs.cloud.google.com/tpu/docs/all-capacity-maintenance-events#vm-query-window-open).
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "status": {
          "message": "Maintenance window has started for this instance. Review the maintenance schedule by describing the VM with gcloud CLI or querying the http://metadata.google.internal/computeMetadata/v1/instance/upcoming-maintenance metadata key."
        },
        "metadata": {
          "canReschedule": true
          "latestWindowStartTime": "2024-01-01:00:00:00PST"
          "maintenanceStatus": "ONGOING"
          "type": "UNSCHEDULED"
          "windowEndTime": "2024-01-01:00:02:00PST"
          "windowStartTime": "2024-01-01:00:00:00PST"
        },
    },
      "operation": {
        "id": "systemevent-1702539760425-60c736da2db40-701ddf19-b5424b20",
        "producer": "compute.instances.upcomingMaintenance",
        "first": true,
        "last": false
      },
    }

The following example is a log message for completed maintenance. For an example query, see Query for when maintenance has completed for a VM instance.
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "status": {
          "message": "Maintenance window has completed for this instance. All maintenance notifications on the instance have been removed."
        },
      "operation": {
        "id": "systemevent-1702539760425-60c736da2db40-701ddf19-b5424b20",
        "producer": "compute.instances.upcomingMaintenance",
        "first": false,
        "last": true
      },
    }

## Manually start pending maintenance for physical capacity

Once a maintenance event is scheduled (`maintenanceStatus` is set to `PENDING`), you can manually start maintenance for your reservations, blocks, or sub-blocks that have the `canReschedule` property set to `True`. When you manually start a pending maintenance event, what happens depends on the maintenance state of your reservation, blocks, or sub-blocks. The following table describes what happens for each of these:

Maintenance state | Description | What you see  
---|---|---  
Scheduled | Compute Engine has scheduled maintenance for the reservation. You can manually start maintenance before the scheduled time. | In the Google Cloud CLI or REST API, the `maintenanceStatus` field is set to `PENDING`.  
In progress | Maintenance is underway. You can't reschedule it. | In the Google Cloud CLI or REST API, the `maintenanceStatus` field is set to `ONGOING`.  
Complete | Maintenance is finished. Compute Engine has removed all maintenance notifications from the VM. | In the Google Cloud CLI or REST API, the `maintenanceStatus` field doesn't exist.  
  
### Manually start maintenance on the entire reservation

The following command starts maintenance on a reservation. Use the `--scope` parameter to specify one of the following values that specify the scope of the maintenance operation:

  * All hosts: `--scope=all`
  * Hosts with running VMs: `--scope=running`
  * Unused, stopped, or suspended VMs: `--scope=unused`



To start maintenance on all blocks of a reservation run the following command:
    
    
    gcloud compute reservations perform-maintenance YOUR_RESERVATION \
      --zone=YOUR_ZONE \
      --scope=all

To check the progress of a maintenance event, run the following command:
    
    
    gcloud compute reservations describe YOUR_RESERVATION  \
      --project=YOUR_PROJECT \
      --zone=YOUR_ZONE

The output is similar to the following:
    
    
    ResourceStatus
      upcomingGroupMaintenance:
        "type":"SCHEDULED"
        "canReschedule":True
        "maintenanceStatus":"PENDING" → "ONGOING"
        "maintenancePendingCount":512 → 0 # all hosts are moved into an ongoing state.
        "maintenanceOngoingCount":0 → 512 → 256 → 0 # this number first increases to all hosts
                                               # as machines complete, this number reduces.

### Manually start maintenance on a block

The following command starts maintenance on a block. Use the `--scope` parameter to specify one of the following values that specify the scope of the maintenance operation:

  * All hosts: `--scope=all`
  * Hosts with running VMs: `--scope=running`
  * Unused, stopped, or suspended VMs: `--scope=unused`



The following command shows how to start maintenance on running hosts:
    
    
    gcloud compute reservations blocks perform-maintenance YOUR_RESERVATION \
        --block-name=YOUR_BLOCK_NAME \
        --scope=RUNNING \
        --project=YOUR_PROJECT \
        --zone=YOUR_ZONE

The following command shows how to check maintenance progress for a block:
    
    
    gcloud compute reservations blocks describe YOUR_RESERVATION \
        --block-name=YOUR_BLOCK_NAME  \
        --project=YOUR_PROJECT \
        --zone=YOUR_ZONE

The output is similar to the following:
    
    
    ResourceStatus
      upcomingGroupMaintenance:
        "maintenanceType":"SCHEDULED"
    …
        "maintenanceGroupStatus":"PENDING" → "ONGOING"
        "maintenancePending":0
     "maintenanceOngoing":70 → 0

### Manually start maintenance on a sub-block

When starting maintenance on a sub-block, you don't specify the `--scope` parameter because a sub-block is the smallest maintenance scope.

The following command starts maintenance on all hosts in a block:
    
    
    gcloud compute reservations sub-blocks perform-maintenance YOUR_RESERVATION \
        --block-name=YOUR_BLOCK_NAME \
        --sub-block-name=YOUR_SUBBLOCK_NAME \
        --project=YOUR_PROJECT \
        --zone=YOUR_ZONE

The following command checks maintenance progress:
    
    
    gcloud compute reservations sub-blocks describe YOUR_RESERVATION \
        --block-name=YOUR_BLOCK_NAME \
        --sub-block-name=YOUR_SUBBLOCK_NAME \
        --project=YOUR_PROJECT \
        --zone=YOUR_ZONE

The output is similar to the following:
    
    
    ResourceStatus
      groupMaintenance:
        "maintenanceType":"SCHEDULED"
        "canReschedule":True
        "maintenanceGroupStatus":"PENDING" → "ONGOING"
        "maintenancePendingCount": 32 → 0 # 32 hosts updated
        "maintenanceOngoingCount":0 → 32 → 0
        "instanceMaintenancePendingCount": 64 → 0
        "instanceMaintenanceOngoingCount": 0 → 64 → 0 # 64 instances updated

## Manually start pending maintenance for a TPU VM

If a host is running more than one VM, starting the maintenance on one VM triggers maintenance for all VMs on the host. For information about manually starting a maintenance event for a TPU VM, see [Manually start a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) in the Compute Engine documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
