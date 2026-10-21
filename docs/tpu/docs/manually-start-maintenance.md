---
url: https://docs.cloud.google.com/tpu/docs/manually-start-maintenance/
title: Manually start a host maintenance event \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:24.514781+00:00
---

# Manually start a host maintenance event  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/manually-start-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manually start a host maintenance event

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

This page explains how to manually start a host maintenance event on supported TPU VMs. This is useful for workloads that might be impacted by degraded performance or downtime, for which you need the maintenance window to start at a specific time.

When you manually start a maintenance event, the host maintenance event starts immediately. You can't specify a date or time for the maintenance event to start. If you don't use this feature, then the maintenance event occurs at the time indicated in the [upcoming maintenance notification](https://docs.cloud.google.com/tpu/docs/view-maintenance-notifications). 

For information about manually starting a maintenance event for TPUs in Google Kubernetes Engine (GKE), see [Manage GKE node disruption for GPUs and TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu).

## Limitations

You can only manually start a host maintenance event using the Cloud TPU API for TPU VMs with the following configurations:

  * Any TPU v4 or v5p VMs
  * TPU v5e or v6e VMs with the `2x4` topology configuration (for example, `v6e-8` if using the accelerator type field in the Cloud TPU API) or larger
  * GKE v5e or v6e multi-host node pools with TPU VMs that are `2x4` or larger



Starting a host maintenance immediately for larger slices **might result in slice unavailability of up to a few hours**. Normally, a host maintenance event results in the slice getting rescheduled as soon as possible to another eligible set of hosts, but for larger host maintenance event requests, there might not be sufficient capacity to immediately reschedule the slice, leading to a longer wait time.

Additionally, initiating maintenance on the Cloud TPU slice will start maintenance for all underlying TPU VMs. If you perform maintenance directly on one of the instances using the [Instances API](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/perform-maintenance), all of the instances within the Cloud TPU slice will go into maintenance. Instead, use the `queued-resources` Cloud TPU API to specify which nodes should have maintenance performed.

## Manually start a host maintenance event

You can use maintenance notifications to determine when you can manually start a maintenance event on a TPU.

### Check the notification information

You can find notifications for upcoming maintenance events using the Cloud TPU API or by querying the metadata server on your VM. For more information, see [View maintenance notifications](https://docs.cloud.google.com/tpu/docs/view-maintenance-notifications).

You can start a maintenance event ahead of time when there is an upcoming host maintenance notification present on the TPU. To start the maintenance event ahead of time, the upcoming host maintenance notification must have `canReschedule` set to `true` and `maintenanceStatus` set to `PENDING`. 

### Start the maintenance event

To start a host maintenance event, you can use the Cloud TPU API with the `perform-maintenance` command:
    
    
    gcloud alpha compute tpus tpu-vm perform-maintenance TPU_NAME \
        --zone=ZONE

When the operation completes, the `windowEndTime` and `windowStartTime` fields change to the time in which you initiated the maintenance event, and the `maintenanceStatus` field changes to `ONGOING`. The host maintenance event begins soon after.

Use the `gcloud alpha compute tpus tpu-vm describe` command to view the status of the maintenance event:
    
    
    gcloud alpha compute tpus tpu-vm describe TPU_NAME \
        --zone=ZONE

The output contains a section similar to the following:
    
    
    upcomingMaintenance:
        canReschedule: true
        latestWindowStartTime: "2025-12-01T19:00:00Z"
        maintenanceStatus: ONGOING
        type: SCHEDULED
        windowEndTime: "2025-12-01T22:00:00Z"
        windowStartTime: "2025-12-01T19:00:00Z"

Maintenance is complete when the TPU VM's state is `READY` and the output from the `gcloud alpha compute tpus tpu-vm describe` command no longer contains an `upcomingMaintenance` metadata field.

For Multislice environments, you can manually start a host maintenance event on specific slices using the following command:
    
    
    gcloud alpha compute tpus queued-resources perform-maintenance QR_NAME \
        --zone=ZONE --node-names=NODE_NAMES

**Note:** The `--node-names` flag is optional for queued resources with a single slice.

`NODE_NAMES` is a comma-separated list of slices (nodes) in the queued resource, for which you want to start a host maintenance event. For example, if the queued resource has nodes named `my-qr-0, my-qr-1`, and `my-qr-2`, a valid input to the `perform-maintenance` command would be `--node-names=my-qr-0,my-qr-1`. 

## What's next

  * [Prepare for maintenance events](https://docs.cloud.google.com/tpu/docs/maintenance-events)
  * [View maintenance notifications](https://docs.cloud.google.com/tpu/docs/view-maintenance-notifications)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
