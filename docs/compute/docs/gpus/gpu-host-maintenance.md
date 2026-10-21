---
url: https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance/
title: Handle GPU host maintenance events \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:40:16.341440+00:00
---

# Handle GPU host maintenance events  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Handle GPU host maintenance events Stay organized with collections  Save and categorize content based on your preferences. 

This document discusses how you can minimize disruptions to your GPU workloads during a maintenance event.

When Compute Engine performs [maintenance](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenanceevents) on a Compute Engine instance with [attached graphics processing units (GPUs)](https://docs.cloud.google.com/compute/docs/gpus/about-gpus), the compute instance must be stopped. This is because compute instances with attached GPUs can't be [live migrated](https://docs.cloud.google.com/compute/docs/instances/live-migration-process#limitations).

You must set these compute instances to [stop for host maintenance events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#terminate_and_optionally_restart). You can set your stopped compute instances to [automatically restart](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#autorestart) after the maintenance event completes.

**Warning:** For compute instances with GPUs, data on any Local SSD disks attached to the compute instance is unrecoverable whenever Compute Engine stops the instance for host maintenance events. For more information, see Migrate your temporary data off of Local SSD disks in this document.

Host maintenance events typically occur once every two weeks, but might occasionally run more frequently. Compute instances with attached GPUs can take up to one hour to terminate after failures or [host errors](https://docs.cloud.google.com/compute/docs/faq#hosterror).

## Receive advance notice before maintenance events

**Note:** To learn how to monitor, plan for, and perform scheduled maintenance on A4X, A4, or A3 Ultra instances, see [Manage host events across compute instances](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events) in the AI Hypercomputer documentation.

You can monitor the maintenance schedule for your Compute Engine instance, and prepare your workloads to transition through the system restart.

To receive advance notice of host events, monitor the `/computeMetadata/v1/instance/maintenance-event` metadata value. If the request to the metadata server returns `NONE`, then the compute instance isn't scheduled to stop. For example, run the following command from within a compute instance:
    
    
    curl http://metadata.google.internal/computeMetadata/v1/instance/maintenance-event -H "Metadata-Flavor: Google"
    
    NONE

If the metadata server returns `TERMINATE_ON_HOST_MAINTENANCE`, then your compute instance is scheduled for stopping. For compute instances that have attached GPUs, Compute Engine provides this notice 1 hour before the compute instance stops.

For some GPU machine series, such as A3, Compute Engine provides notice of upcoming maintenance more than an hour in advance through the `upcoming-maintenance` metadata attribute. To learn more, see [Monitor and plan for a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event).

Configure your application to transition through the maintenance event. For example, you might use one of the following techniques:

Use these notices to configure your application to transition through host maintenance events. For example, see Migrate your temporary data off of Local SSD disks in this document.

## Migrate your temporary data off of Local SSD disks

Due to [Local SSD data persistence](https://docs.cloud.google.com/compute/docs/disks/local-ssd#data_persistence), data on any Local SSD disks attached to a compute instance is unrecoverable whenever Compute Engine stops the compute instance for host maintenance events. If you want to help prevent data loss, configure your workload to migrate data off of the Local SSD disks before the compute instance is stopped. For example, you might use one of the following techniques:

  * Configure your application to temporarily move work in progress to a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/uploading-objects), then retrieve that data after the compute instance restarts.

  * Write data to a [secondary Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk). When the compute instance automatically restarts, the Persistent Disk can be reattached and your application can resume work.




## What's next?

  * Learn more about [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).
  * To learn more about managing and scaling groups of compute instances, see [Set the group's target size](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#set_the_groups_target_size). 
  * To monitor GPU performance, see [Monitor GPU performance](https://docs.cloud.google.com/compute/docs/gpus/monitor-gpus). 
  * To improve network performance, see [Use higher network bandwidth](https://docs.cloud.google.com/compute/docs/gpus/optimize-gpus).
  * Learn how to [troubleshoot VM shutdowns and reboots](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reboots).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
