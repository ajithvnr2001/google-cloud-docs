---
url: https://docs.cloud.google.com/tpu/docs/request-using-flex-start/
title: Request TPU Flex-start VMs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:27.306131+00:00
---

# Request TPU Flex-start VMs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/request-using-flex-start/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Request TPU Flex-start VMs

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

TPU Flex-start VMs, powered by [Dynamic Workload Scheduler](https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler), provide a flexible and cost-effective way to access TPU resources for AI workloads. Flex-start VMs let you dynamically provision TPUs as needed, for up to 7 days, without long-term reservations or complex quota management. With TPU Flex-start VMs, you submit a TPU provisioning request that persists until capacity becomes available. Once available, the TPU VMs run for the duration that you specified in your request.

TPU Flex-start VMs are a good fit for quick experimentation, small-scale testing, dynamic provisioning of TPUs for inference workloads, model fine-tuning, and workload runs that take less than 7 days. For more information about other TPU consumption options, see [Cloud TPU consumption options](https://docs.cloud.google.com/tpu/docs/consumption-options).

You can delete your TPU resources at any time to stop billing. For more information about TPU pricing, see [Cloud TPU pricing](https://cloud.google.com/tpu/pricing).

## Limitations

TPU Flex-start VMs have the following limitations:

  * You can request TPU Flex-start VMs for a duration of up to 7 days.
  * You can request the following Cloud TPU versions and zones: 
    * **[TPU v6e](https://docs.cloud.google.com/tpu/docs/v6e)** : asia-northeast1-b, us-east5-a, us-south1-ai1b
    * **[TPU v5p](https://docs.cloud.google.com/tpu/docs/v5p)** : us-east5-a
    * **[TPU v5e](https://docs.cloud.google.com/tpu/docs/v5e)** : us-west4-a
  * You must use the [queued resources API](https://docs.cloud.google.com/tpu/docs/queued-resources) to use TPU Flex-start VMs.



## Before you begin

Before requesting TPU Flex-start VMs, you must:

  * Install the Google Cloud CLI
  * Create a Google Cloud project
  * Enable the Cloud TPU API



For more information, see [Set up the Cloud TPU environment](https://docs.cloud.google.com/tpu/docs/setup-gcp-account).

You should also make sure you have sufficient preemptible quota to use TPU Flex-start VMs. If you need more TPU cores than the amount granted by the default quota, you need to request a higher quota allocation. For more information about defaults and requesting more quota, see [Cloud TPU quotas](https://docs.cloud.google.com/tpu/docs/quota).

## Request TPU Flex-start VMs

TPU Flex-start VMs use the queued resources API to request TPU resources in a queued manner. When the requested resource becomes available, it's assigned to your Google Cloud project for your immediate, exclusive use. After the requested run duration, the TPU VMs are deleted and the queued resource moves to the `SUSPENDED` state. For more information about queued resources, see [Manage queued resources](https://docs.cloud.google.com/tpu/docs/queued-resources).

To request TPU Flex-start VMs, use the [`gcloud alpha compute tpus queued-resources create`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/tpus/queued-resources/create) command with the `--provisioning-model` flag set to `flex-start` and the `--max-run-duration` flag set to the duration you want your TPUs to run.
    
    
    gcloud alpha compute tpus queued-resources create QUEUED_RESOURCE_ID \
        --zone=ZONE \
        --accelerator-type=ACCELERATOR_TYPE \
        --runtime-version=RUNTIME_VERSION \
        --node-id=NODE_ID \
        --provisioning-model=flex-start \
        --max-run-duration=RUN_DURATION

Replace the following placeholders:

  * QUEUED_RESOURCE_ID: A user-assigned ID for the queued resource request.
  * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) in which to create the TPU VM.
  * ACCELERATOR_TYPE: Specifies the version and size of the Cloud TPU to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * RUNTIME_VERSION: The Cloud TPU [software version](https://docs.cloud.google.com/tpu/docs/runtimes).
  * NODE_ID: A user-assigned ID for the TPU that is created when the queued resource request is allocated.
  * RUN_DURATION: How long the TPUs should run. Format the duration as the number of days, hours, minutes, and seconds followed by `d`, `h`, `m`, and `s`, respectively. For example, specify `72h` for a duration of 72 hours, or specify `1d2h3m4s` for a duration of 1 day, 2 hours, 3 minutes, and 4 seconds. The maximum is 7 days.



You can further customize your queued resource request to run at specific times with additional flags:

  * `--valid-after-duration`: The duration before which the TPU must not be provisioned.
  * `--valid-after-time`: The time before which the TPU must not be provisioned.
  * `--valid-until-duration`: The duration for which the request is valid. If the request hasn't been fulfilled by this duration, the request expires and moves to the `FAILED` state.
  * `--valid-until-time`: The time for which the request is valid. If the request hasn't been fulfilled by this time, the request expires and moves to the `FAILED` state.



For more information about optional flags, see the [`gcloud alpha compute tpus queued-resources create`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/tpus/queued-resources/create) documentation.

## Get the status of a request for TPU Flex-start VMs

To monitor the status of your request for TPU Flex-start VMs, use the queued resources API to get the status of the queued resource request using the [`gcloud alpha compute tpus queued-resources describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/tpus/queued-resources/describe) command:
    
    
    gcloud alpha compute tpus queued-resources describe QUEUED_RESOURCE_ID \
        --zone ZONE

A queued resource can be in one of the following states:

  * `WAITING_FOR_RESOURCES`: The request has passed initial validation and has been added to the queue.
  * `PROVISIONING`: The request has been selected from the queue, and the TPU VMs are being created.
  * `ACTIVE`: The request has been fulfilled, and the TPU VMs are ready.
  * `FAILED`: The request couldn't be completed. Use the `describe` command for more details.
  * `SUSPENDING`: The resources associated with the request are being deleted.
  * `SUSPENDED`: The resources associated with the request have been deleted.



For more information, see [Retrieve state and diagnostic information about a queued resource request](https://docs.cloud.google.com/tpu/docs/queued-resources#retrieve_state_and_diagnostic_information_about_a_queued_resource_request).

## Monitor the run time of TPU Flex-start VMs

You can monitor the run time of TPU Flex-start VMs by checking the TPU's termination timestamp:

  1. Get the details of your queued resource request.
  2. Choose one of the following options depending on whether your TPUs have been created:

     * **If the queued resource is waiting for resources** : In the output, see the `maxRunDuration` field. This field specifies how long the TPUs will run once they're created.

     * **If the TPUs associated with the queued resource have been created** : In the output, see the `terminationTimestamp` field listed for each node in the queued resource. This field specifies when the TPU will be terminated.




## Delete a queued resource

**Important:** Queued resources consume quota regardless of their state. Delete queued resources after use to avoid blocking future requests on quota limits.

You can delete a queued resource request and the TPUs associated with the request by deleting the queued resource request and passing the `--force` flag to the [`queued-resources delete`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/tpus/queued-resources/delete) command:
    
    
    gcloud alpha compute tpus queued-resources delete QUEUED_RESOURCE_ID \
        --force

If you delete the TPU directly using the `gcloud compute tpus tpu-vm delete` command, you also need to delete the queued resource, as shown in the following example. When you delete the TPU, the queued resource request transitions to the `SUSPENDED` state, after which you can delete the queued resource request.

To delete a TPU, use the [`gcloud compute tpus tpu-vm delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/delete) command:
    
    
    gcloud compute tpus tpu-vm delete NODE_ID \
        --zone ZONE

Then, to delete the queued resource, use the [`gcloud alpha compute tpus queued-resources delete`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/tpus/queued-resources/delete) command:
    
    
    gcloud alpha compute tpus queued-resources delete QUEUED_RESOURCE_ID \
        --zone ZONE

For more information, see [Delete a queued resource request](https://docs.cloud.google.com/tpu/docs/queued-resources#delete_a_queued_resource_request).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
