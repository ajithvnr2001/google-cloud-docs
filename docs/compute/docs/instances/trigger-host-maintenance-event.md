---
url: https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event/
title: Manually start a host maintenance event \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:40:01.275162+00:00
---

# Manually start a host maintenance event  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manually start a host maintenance event Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This page explains how to manually start a [host maintenance event](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview) on supported Compute Engine instances. This feature lets you start a maintenance event to control the timing of your instance's maintenance. This is useful for workloads that might be impacted by degraded performance or downtime, for which you need the maintenance window to start at a specific time.

When you manually start a maintenance event, the host maintenance starts immediately. You can't specify a date or time for the maintenance event to start. If you don't use this feature, then the maintenance event occurs at the time indicated in the [upcoming maintenance notification](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event#overview_of_maintenance_notifications).

If you want to first test how your applications will handle a maintenance event, you can [simulate a maintenance event](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance).

### Supported machine series

You can manually start a host maintenance event for instances that use the following machine types:

  * **Accelerator-optimized machine families** :

    * GPUs:

      * [A4X machine types with 4 GPUs](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms)

      * [A4 machine types with 8 GPUs](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms)

      * [A3 Ultra machine types with 8 GPUs](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-vms)

      * [A3 Mega machine types with 8 GPUs](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-mega-vms)

      * [A3 High machine types with 8 GPUs](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-high-vms)

      * [A3 Edge machine types with 8 GPUs](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-edge-vms)

      * [A2 Ultra machine types with 8 GPUs](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-ultra-vms)

      * [A2 Standard machine types with 8 or 16 GPUs](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-standard-vms)

      * [G4 machine types with 8 GPUs](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series)

      * [G2 machine types with 8 GPUs](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-standard-vms)

      * [N1 machine types with 4 NVIDIA T4 GPUs](https://docs.cloud.google.com/compute/docs/gpus#t4-gpus)

      * [N1 machine types with 4 NVIDIA P4 GPUs](https://docs.cloud.google.com/compute/docs/gpus#p4-gpus)

      * [N1 machine types with 8 NVIDIA V100 GPUs](https://docs.cloud.google.com/compute/docs/gpus#v100-gpus)

    * TPUs:

      * [TPU7x](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu7x)

      * [TPU v6e](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#v6e) VMs in a slice with a topology of `2x4` or larger.

      * [TPU v5p](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#v5p)

  * **Compute-optimized machine families** :

    * [H3 machine types with 88 vCPUs](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h3_machine_types)

    * [H4D machine types with 192 vCPUs](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_machine_types)

  * **General-purpose machine families** :

    * [C4 machine types with 192 or 288 vCPUs or with Local SSD disks attached](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_machine_types)

    * [C4 bare metal instances with 288 vCPUs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4_machine_types)

    * [C4A machine types with Local SSD disks attached](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_machine_types)

    * [C4D machine types with 384 vCPUs or with Local SSD disks attached](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_machine_types)

    * [C4D bare metal instances with 384 vCPUs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4d_machine_types)

    * [C3 machine types with 176 vCPUs or with Local SSD disks attached](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_machine_types)

    * [C3 bare metal instances with 192 vCPUs](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3_machine_types)

    * [C3D machine types with 360 vCPUs or with Local SSD disks attached](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c3d_machine_types)

  * **Memory-optimized machine families** :

**Note:** You can't use the procedures documented on this page to manually start a host maintenance event for an X4 instance. For information about the workaround, see [Manually triggering host maintenance doesn't work for X4 instances](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#x4-ctm).
    * [M4 machine types](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m4_machine_types) and M4N

    * [M3 machine types](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m3_machine_types)

    * [M2 machine types](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m2_machine_types)

    * [M1 machine types](https://docs.cloud.google.com/compute/docs/memory-optimized-machines#m1_machine_types)

  * **Network-optimized machine families** :

    * [C4N](https://docs.cloud.google.com/compute/docs/network-optimized-machines#c4n_series)

    * [M4N](https://docs.cloud.google.com/compute/docs/network-optimized-machines#m4n_series)

  * **Storage-optimized machine families** :

    * [Z4D machine types](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4d_machine_types)

    * [Z4M machine types](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_machine_types)

    * [Z3 machine types](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z3_machine_types)




## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

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

To get the permissions that you need to manage VM maintenance, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to manage VM maintenance. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage VM maintenance:

  * To get information about a compute instance: `compute.instances.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Manually start a host maintenance event

Compute Engine sends notifications for upcoming maintenance events by multiple methods. Using the information in the notifications, you can determine the timeframe for when you can manually start a maintenance event.

### Check the notification information

You can find your maintenance event notifications in one of the following ways:

  * [Querying your compute instances or metadata server](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event#check-vms-for-maintenance-event)
  * [Using Cloud Logging](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event#check-logs-for-maintenance)



If the notification about a host maintenance event contains `canReschedule=True` and `maintenanceStatus=Pending`, then you have the option to start the maintenance at a time of your choosing, or wait for the maintenance event to take place at the time specified by `windowStartTime`.

If there is no notification, and you try to manually start a maintenance event, the following message is displayed:

`There is no reschedulable upcoming maintenance.`

This message indicates that no maintenance event has been scheduled and that no action needs to be taken.

### Start the maintenance event

You can start host maintenance at a time of your choosing, rather than wait for the scheduled time. Use the Google Cloud CLI or REST to trigger the maintenance event, which then starts immediately.

###  gcloud 

To start a maintenance event, use the [`compute instances perform-maintenance` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/perform-maintenance). The host maintenance starts immediately after entering the command.
    
    
    gcloud compute instances perform-maintenance INSTANCE_NAME \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: The of the name of the compute instance.
  * `ZONE`: The zone where the instance resides.



The response is similar to the following:
    
    
    resourceStatus:
      upcomingMaintenance:
        canReschedule: false
        latestWindowStartTime: '2025-01-15T19:57:17Z'
        maintenanceStatus: ONGOING
        type: SCHEDULED
        windowEndTime: '2025-01-15T23:57:11Z'
        windowStartTime: '2025-01-15T19:57:16Z'
    

In the response, `canReschedule` is set to `false` and `maintenanceStatus` is set to `ONGOING`, which indicates that the host maintenance operation is underway.

###  REST 

To start a maintenance event, construct a `POST` request using the [`instances.performMaintenance` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/performMaintenance).
    
    
    POST: https://compute.googleapis.com/compute/v1/projects/PROJECT_NAME/zones/ZONE/instances/INSTANCE_NAME/performMaintenance
    

Replace the following:

  * `PROJECT_NAME`: The name of the project
  * `ZONE`: The zone where the compute instance resides
  * `INSTANCE_NAME`: The name of the instance



The response looks like this:
    
    
    upcomingMaintenance:{
      "canReschedule":false
      "latestWindowStartTime": "2023-12-01T19:00:01Z"
      "maintenanceStatus":"ONGOING"
      "type":"SCHEDULED"
      "windowEndTime": "2023-12-01T22:00:00Z"
      "windowStartTime": "2023-12-01T19:00:00Z"
    }
    

In the response, `canReschedule` is set to `false` and `maintenanceStatus` is set to `ONGOING`, which indicates that the host maintenance operation is underway.

## What's next

  * Learn how to [Simulate a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance).
  * Learn how to [Get live migration notices](https://docs.cloud.google.com/compute/docs/metadata/getting-live-migration-notice).
  * Learn how to [Configure alerts for host maintenance notifications](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event#alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
