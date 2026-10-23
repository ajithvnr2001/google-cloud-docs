---
url: https://docs.cloud.google.com/tpu/docs/spot/
title: Manage TPU Spot VMs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:15.831828+00:00
---

# Manage TPU Spot VMs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/spot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage TPU Spot VMs

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

Spot VMs make unused capacity available at highly-discounted rates. Spot VMs are preemptible at any time, but unlike [preemptible TPUs](https://docs.cloud.google.com/tpu/docs/preemptible), there is no limit on runtime duration. You can't restart TPU Spot VMs, and you must recreate them after preemption. You also can't use 120-second preemption notice duration with TPU Spot VMs. For more information about Spot VMs in general, see the [Compute Engine documentation about Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot).

## Create TPU Spot VMs

You can create TPU Spot VMs using queued resources, which adds your create request to a queue and lets you receive capacity once it is available. Creating TPUs as queued resources is a best practice. For more information, see [Queued resources user guide](https://docs.cloud.google.com/tpu/docs/queued-resources).

The following example shows how to create TPU Spot VMs using queued resources:

### gcloud

Add the `--spot` flag to the `gcloud compute tpus queued-resources` command:
    
    
    gcloud compute tpus queued-resources create QUEUED_RESOURCE_ID \
        --node-id=NODE_ID \
        --zone=europe-west4-a \
        --accelerator-type=v3-8 \
        --runtime-version=tpu-vm-tf-2.17.1-pod-pjrt \
        --spot

### curl

Add `spot: {}` to the request body:
    
    
    curl -X POST https://tpu.googleapis.com/v2alpha1/projects/PROJECT_ID/locations/europe-west4-a/queuedResources?queued_resource_id=QUEUED_RESOURCE_ID \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{
            tpu: {
            node_spec: {
                parent: "projects/PROJECT_ID/locations/europe-west4-a",
                node_id: "NODE_ID",
                node: {
                accelerator_type: "v3-8",
                runtime_version: "tpu-vm-tf-2.17.1-pod-pjrt"
                }
            }
            },
            spot: {}
        }'

### Console

  1. In the Google Cloud console, go to the **TPUs** page:

[Go to TPUs](https://console.cloud.google.com/compute/tpus)

  2. Click **Create TPU**.

  3. In the **Name** field, enter a name for your TPU.

  4. In the **Zone** box, select the [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) where you want to create the TPU.

  5. In the **TPU type** box, select an accelerator type. The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).

  6. In the **TPU software version** box, select a software version. When creating a Cloud TPU VM, the TPU software version specifies the version of the TPU runtime to install. For more information, see [TPU software versions](https://docs.cloud.google.com/tpu/docs/runtimes).

  7. Click the **Enable queueing** toggle.

  8. In the **Queued resource name** field, enter a name for your queued resource request.

  9. Expand the **Management** section.

  10. Select the **Make this a TPU Spot VM** checkbox.

  11. Click **Create**.




You can also create TPU Spot VMs without using queued resources:

### gcloud

Add the `--spot` flag to the `gcloud compute tpus tpu-vm` command:
    
    
    gcloud compute tpus tpu-vm create TPU_NAME \
        --zone=europe-west4-a \
        --accelerator-type=v3-8 \
        --version=tpu-vm-tf-2.17.1-pod-pjrt \
        --spot

### curl

Add `scheduling_config: {spot: true}` to the request body:
    
    
    curl -X POST https://tpu.googleapis.com/v2/projects/PROJECT_ID/locations/europe-west4-a/nodes?node_id=TPU_NAME \
        -H "Authorization: Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        -d '{
            accelerator_type: "v3-8",
            runtime_version: "tpu-vm-tf-2.17.1-pod-pjrt",
            network_config: {enable_external_ips: true},
            scheduling_config: {spot: true}
        }'

### Console

  1. In the Google Cloud console, go to the **TPUs** page:

[Go to TPUs](https://console.cloud.google.com/compute/tpus)

  2. Click **Create TPU**.

  3. In the **Name** field, enter a name for your TPU.

  4. In the **Zone** box, select the [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) where you want to create the TPU.

  5. In the **TPU type** box, select an accelerator type. The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).

  6. In the **TPU software version** box, select a software version. When creating a Cloud TPU VM, the TPU software version specifies the version of the TPU runtime to install. For more information, see [TPU software versions](https://docs.cloud.google.com/tpu/docs/runtimes).

  7. Expand the **Management** section.

  8. Select the **Make this a TPU Spot VM** checkbox.

  9. Click **Create**.




## Check if a TPU VM is a Spot VM

### gcloud

To confirm if your TPU VM is a Spot VM, use the describe command:
    
    
    gcloud compute tpus tpu-vm describe TPU_NAME --zone=europe-west4-a

If the TPU VM is a Spot VM, then the output includes the `spot` field set to `true`, similar to the following:
    
    
    ...
    schedulingConfig:
    spot: true
    ...
    

### Console

  1. In the Google Cloud console, go to the **TPUs** page:

[Go to TPUs](https://console.cloud.google.com/compute/tpus)

  2. Click the name of your Cloud TPU.

If the TPU VM is a Spot VM, then the **Tier** is **Spot VM**.




## Pricing and quota

Pricing for TPU Spot VMs is significantly lower than for on-demand and reserved TPUs. For more information about pricing, see [Cloud TPU pricing](https://cloud.google.com/tpu/pricing).

You need preemptible quota to use TPU Spot VMs. For more information, see [Quotas](https://docs.cloud.google.com/tpu/docs/quota).

## What's next

  * Learn how to [manage TPUs](https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
