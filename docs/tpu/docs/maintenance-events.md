---
url: https://docs.cloud.google.com/tpu/docs/maintenance-events/
title: Prepare for maintenance events \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:20.961394+00:00
---

# Prepare for maintenance events  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/maintenance-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Prepare for maintenance events

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

TPU VMs are instances of Compute Engine VMs with attached TPU hardware. Compute Engine VMs are subject to [Compute Engine VM maintenance events](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#maintenanceevents). Each TPU is connected to a Compute Engine VM, so using more TPUs (for example, in a TPU slice) increases the likelihood of one of your VMs encountering a maintenance event.

This document discusses approaches to handle maintenance events for long-running training jobs on Cloud TPUs. For information about handling maintenance events for TPUs in Google Kubernetes Engine (GKE), see [Manage GKE node disruption for GPUs and TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu).

## View notifications for upcoming maintenance

You can view notifications for upcoming host maintenance events. By monitoring your instance's upcoming maintenance windows, you can proactively prepare your workloads to handle upcoming maintenance with minimal disruption. For more information, see [View maintenance notifications](https://docs.cloud.google.com/tpu/docs/view-maintenance-notifications).

## Use checkpoints for fast recovery from maintenance events

Checkpoints are key to short recoveries from maintenance events and should be saved frequently. A good rule of thumb is saving checkpoints approximately every hour. Not checkpointing often enough risks losing a lot of training progress due to maintenance events or other training interruptions.

**Important:** When a TPU crashes or is shut down for a maintenance event, any data stored on the VM's boot disk may be lost. Therefore, we recommend that you save checkpoints to some form of external storage, such as a Google Cloud Hyperdisk volume or a Cloud Storage bucket. For more information, see [TPU storage options](https://docs.cloud.google.com/tpu/docs/storage-options)

Checkpoints generally refer to all of the saved parameters used in training, such as model weights. The time it takes to save a checkpoint can range from the order of seconds to the order of minutes.

Although TPUs can recover automatically from most maintenance events and training jobs continue without manual intervention, there might be edge cases where the job does not restart and automatically continue. When this happens, you need to delete and recreate the TPU resources and restart the training job from a saved checkpoint. For information about how to detect and recover from automatic recovery failures, see Detect and recover from TPU failures.

There are different mechanisms for saving and loading checkpoints for each ML framework. Supported Cloud TPU models generally have checkpointing built-in. For more information on checkpointing, see: [TensorFlow 2.x](https://www.tensorflow.org/guide/checkpoint), [PyTorch](https://pytorch.org/tutorials/recipes/recipes/saving_and_loading_a_general_checkpoint.html), or [JAX/flax](https://flax.readthedocs.io/en/latest/flax.training.html).

## Use Autocheckpoint

You can use the Autocheckpoint feature to preserve training progress by configuring your code to save a non-scheduled checkpoint when a maintenance event occurs. For more information about Autocheckpoint, see [Cloud TPU Autocheckpoint](https://docs.cloud.google.com/tpu/docs/autocheckpoint).

## Retry your training script

The training script might stop as a result of an interruption event. You can use a `bash` script to continuously retry the training script until training is complete. For example:
    
    
    while ! gcloud compute tpus tpu-vm ssh ${TPU_NAME} --command "python3 TRAINING_COMMAND"; do sleep 1; done

**Note:** You need to run the script from a Cloud Shell or terminal, not from the TPU VM.

Each retry should continue from the latest checkpoint, so you should always use retry scripts in conjunction with checkpoints.

Production-ready training pipelines should use a resource management system such as Google Kubernetes Engine (GKE). For more information on using Google Kubernetes Engine with TPU VMs, see [Deploy TPU workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus).

## Detect and recover from TPU failures

When a TPU doesn't recover from a maintenance event, you can use a recovery script to detect the TPU state and delete and re-create the TPU. For an example of a recovery script, see [retry.sh](https://github.com/tensorflow/tpu/blob/master/tools/retry/retry.sh). If the process running the training script crashes, you can modify the recovery script to retry running the training script.

For information about manually deleting and re-creating a TPU, see [Manage TPU resources](https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm).

## Use collection scheduling

Cloud TPU has the concept of [collection scheduling](https://docs.cloud.google.com/tpu/docs/collection-scheduling), offering two types of collections that customers can use to support either training or serving and inference workloads. When you use this feature to deploy your Cloud TPU instances, Google Cloud applies unique maintenance schedules that best match the application. You can expect the following behaviors from each collection type:

  * **Training (default)** : This collection type is beneficial to typical training workloads where you need minimal downtime across all instances and limited unexpected interruptions in order to quickly restore your service during maintenance events. The training collection type provides parallel scheduling and execution of maintenance events for a group of instances.

  * **Serving (available using`--workload-type=AVAILABILITY_OPTIMIZED`)**: This collection type is beneficial to most serving or inference workloads where you need minimal downtime across a subset of instances (replicas) to ensure service continuity, even during maintenance events. The serving collection type provides staggered scheduling and execution of maintenance events for a group of instances. Specifying a serving collection is only supported on TPU v6e.




For more information about collection scheduling, see [TPU collection scheduling for inference workloads](https://docs.cloud.google.com/tpu/docs/collection-scheduling).

## Detect maintenance events

You can detect if and when a maintenance event occurred on your TPU using the following [`gcloud compute tpus tpu-vm describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/describe) command:
    
    
    $ gcloud compute tpus tpu-vm describe tpu-name --zone=zone  | grep 'health'

The output from this command displays the current state of the TPU and a description of the most recent maintenance event. The output should look similar to the following:
    
    
    health: HEALTHY
    healthDescription: The TPU had a maintenance event at 2022-01-26T03:44:36.265703305Z
    

### View maintenance event logs

You can view historical logs of maintenance events on your TPU in [system event audit logs](https://docs.cloud.google.com/tpu/docs/audit-logs#audited_operations).

  1. In the Google Cloud console navigation menu, go to the Logs Explorer page:

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. Use the following search query to view any TPUs that have been terminated or restarted:

`"tpu.nodes.terminate" OR "tpu.nodes.restart"`

The results display logs for any interruptions and repairs of your TPU workers within your search timeframe. The logs include:

     * The date and time of the event
     * The type of event
     * For "terminate" events, the reason for the termination in the `protoPayload.metadata.terminateReason` field



## What's next

  * [View maintenance notifications](https://docs.cloud.google.com/tpu/docs/view-maintenance-notifications)
  * [Manually start a host maintenance event](https://docs.cloud.google.com/tpu/docs/manually-start-maintenance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
