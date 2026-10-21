---
url: https://docs.cloud.google.com/tpu/docs/preemptible/
title: Preemptible TPUs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:31.352451+00:00
---

# Preemptible TPUs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/preemptible/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Preemptible TPUs

**Important:** TPU Spot VMs are the latest version of preemptible TPUs. New and existing preemptible TPUs continue to be supported, and TPU Spot VMs use the same pricing model as preemptible TPUs. However, TPU Spot VMs provide new features that preemptible TPUs don't support. For example, TPU Spot VMs don't have the 24 hour run time limit of preemptible TPUs. For more information, see [Manage TPU Spot VMs](https://docs.cloud.google.com/tpu/docs/spot).**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

Preemptible TPUs cost much less than non-preemptible TPUs. The Cloud TPU service might preempt (shut down) these TPUs at any time, if it requires additional TPU resources.

## Creating a preemptible TPU VM

### gcloud
    
    
    $ gcloud compute tpus tpu-vm create demo-tpu \
      --zone=europe-west4-a \
      --accelerator-type=v3-8 \
      --version=tpu-vm-tf-2.17.1-pjrt \
      --preemptible
      

where:

  * `demo-tpu` is a name for the TPU.
  * `accelerator-type` is the type of TPU. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `version` is the [ Cloud TPU software version](https://docs.cloud.google.com/tpu/docs/runtimes#tpu_software_versions) to install.
  * `preemptible` allows Cloud TPU to preempt the TPU.



## Pricing and quota for preemptible TPUs

Pricing for preemptible TPUs is significantly lower than for normal TPUs. For details, see the [pricing page](https://cloud.google.com/tpu/pricing). You are not charged for TPUs if they are preempted in the first minute after you create them.

Quota for preemptible TPUs is generally higher, and is separate from the quota for normal TPUs. See the [quota page](https://docs.cloud.google.com/tpu/docs/quota).

## Detecting if a TPU has been preempted

You use the following `gcloud` command to check whether the Cloud TPU service has preempted your TPU:

List your available TPUs:
    
    
    gcloud compute tpus tpu-vm list
      --zone=us-central1-b
      

The output of the command displays the details of the TPUs created in your project. If a TPU has been preempted, the status changes from `READY` to `PREEMPTED`.

For example: 
    
    
    NAME       ZONE           ACCELERATOR_TYPE  NETWORK_ENDPOINT   NETWORK  RANGE          STATUS
    demo-tpu   us-central1-b  v2-8              10.240.1.2:8470    default  10.240.1.0/29  PREEMPTED

**Note:** If your Cloud TPU is preempted, you must delete it and create a new one as described in [Managing TPUs](https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm).

## Designing your machine learning application to run on preemptible TPUs

Make sure your application is resilient to restarts of the VM and TPU, by saving model checkpoints regularly and by configuring your application to restore the most recent checkpoint on restart.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
