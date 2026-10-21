---
url: https://docs.cloud.google.com/tpu/docs/prepare-for-maintenance/
title: Manage maintenance events for TPUs on Google-managed infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:21.712068+00:00
---

# Manage maintenance events for TPUs on Google-managed infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/prepare-for-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage maintenance events for TPUs on Google-managed infrastructure

TPU VMs are instances of Compute Engine VMs with attached TPU hardware. Compute Engine VMs are subject to [Compute Engine VM maintenance events](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#maintenanceevents). Each TPU is connected to a Compute Engine VM, so using more TPUs (for example, in a TPU slice) increases the likelihood of one of your VMs encountering a maintenance event.

This document discusses approaches to handle maintenance events for long-running training jobs on TPUs. For information about handling maintenance events for TPUs in Google Kubernetes Engine (GKE), see [Manage GKE node disruption for GPUs and TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu).

## View notifications for upcoming maintenance

By monitoring your instance's upcoming maintenance windows, you can proactively prepare your workloads to handle upcoming maintenance with minimal disruption. For more information, see [Monitor and plan for a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) in the Compute Engine documentation.

## Use checkpoints for fast recovery from maintenance events

Checkpoints are key to short recoveries from maintenance events and should be saved frequently. We recommend saving checkpoints approximately every hour. Not checkpointing often enough risks losing a lot of training progress due to maintenance events or other training interruptions.

**Important:** When a TPU crashes or is shut down for a maintenance event, any data stored on the VM's boot disk may be lost. Therefore, we recommend that you save checkpoints to some form of external storage, such as a Google Cloud Hyperdisk volume or a Cloud Storage bucket. For more information, see [TPU storage options](https://docs.cloud.google.com/tpu/docs/storage-options).

Checkpoints generally refer to all of the saved parameters used in training, such as model weights. The time it takes to save a checkpoint can range from seconds to minutes.

While TPUs often recover automatically from maintenance events, there are edge cases where the job doesn't restart automatically. When this happens, you need to delete and recreate the TPU resources and restart the training job from a saved checkpoint.

There are different mechanisms for saving and loading checkpoints for each ML framework. Supported Cloud TPU models generally have checkpointing built-in. For more information on checkpointing, see the following documentation:

  * [PyTorch](https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html)
  * [JAX and Flax](https://flax.readthedocs.io/en/stable/guides/checkpointing.html)



## Detect maintenance events

To detect if and when a maintenance event occurred on your TPU, check the system event audit logs in Cloud Logging. For more information, see View maintenance event logs.

You can also check for upcoming maintenance events using the [`gcloud compute instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe) command. For more information, see [Monitor and plan for a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) in the Compute Engine documentation.

### View maintenance event logs

You can view historical logs of maintenance events on your TPU in [system event audit logs](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event#check-logs-for-maintenance).

  1. In the Google Cloud console navigation menu, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. Use the following search query to view any TPU VMs that have been terminated for maintenance:

`"compute.instances.terminateOnHostMaintenance"`

The results display logs for any interruptions and repairs of your TPU workers within your search timeframe. The logs include:

     * The date and time of the event
     * The type of event
     * The reason for the termination in the `protoPayload.metadata.terminateReason` field



## Manually start maintenance

You can manually start a pending host maintenance event on your TPU VM to proactively handle upcoming maintenance with minimal disruption. For more information, see [Manually start a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) in the Compute Engine documentation.

## What's next

  * [Monitor and plan for a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event)
  * [Manually start a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
