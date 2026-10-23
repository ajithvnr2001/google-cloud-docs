---
url: https://docs.cloud.google.com/tpu/docs/consume-reservation/
title: Consume a reservation \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:23.905651+00:00
---

# Consume a reservation  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/consume-reservation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Consume a reservation

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

If you have a TPU reservation, you can use your reserved resources to create TPUs that match the reservation's properties. This action is known as _consuming a reservation_. For information about consuming a TPU reservation when using Google Kubernetes Engine (GKE), see [TPU reservation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#tpu_reservation) in the GKE documentation.

**Important:** When you consume a future reservation that was created in calendar mode, you must specify the name of the reservation you want to consume, described in the next section.

## Consume a specific reservation

When you create resources with the [`gcloud alpha compute tpus queued-resources create` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/tpus/queued-resources/create), use the [`--reservation` flag](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/tpus/queued-resources/create#--reservation) to specify the name of the reservation to consume. For future reservations created in calendar mode, you must also set the [`--provisioning-model` flag](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/tpus/queued-resources/create#--provisioning-model) to `reservation-bound`:
    
    
    gcloud alpha compute tpus queued-resources create QUEUED_RESOURCE_ID \
        --node-id=TPU_NAME \
        --zone=ZONE \
        --accelerator-type=ACCELERATOR_TYPE \
        --runtime-version=SOFTWARE_VERSION \
        --reservation=RESERVATION_URL \
        --provisioning-model=reservation-bound # Only required for calendar mode

Replace the following placeholder variables:

  * QUEUED_RESOURCE_ID: A user-assigned ID for the queued resource request.
  * TPU_NAME: A user-assigned ID (name) for the TPU that is created when the queued resource request is allocated.
  * ZONE: The zone in which to create the TPU VM. For more information about supported zones, see [Regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones).
  * ACCELERATOR_TYPE: Specifies the version and size of the Cloud TPU to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * SOFTWARE_VERSION: The Cloud TPU [software version](https://docs.cloud.google.com/tpu/docs/runtimes).
  * RESERVATION_URL: The URL of the reservation. Specify one of the following values: 
    * If the reservation is in your project: `RESERVATION_NAME`
    * If the reservation is in another project and your project can consume it: `projects/OWNER_PROJECT_ID/reservations/RESERVATION_NAME`



## Consume any matching reservation

**Important:** This method is not supported for future reservations created in calendar mode. When you consume a future reservation created in calendar mode, you must specify the name of the reservation you want to consume, described in the previous section.

You can use the `--reserved` flag to automatically determine the reservation to use based on the accelerator type, project ID, and zone.

### CreateNode

To consume any matching reservation using the CreateNode API, use the [`gcloud alpha compute tpus tpu-vm create` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/tpus/tpu-vm/create) with the [`--reserved` flag](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/tpus/tpu-vm/create#--reserved):
    
    
    gcloud alpha compute tpus tpu-vm create TPU_NAME \
        --zone=ZONE \
        --accelerator-type=ACCELERATOR_TYPE \
        --version=SOFTWARE_VERSION \
        --reserved

Replace the following placeholder variables:

  * TPU_NAME: A name for the TPU.
  * ZONE: The zone where to create the TPU VM, which must match the reservation zone.
  * ACCELERATOR_TYPE: Specifies the version and size of the Cloud TPU to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * SOFTWARE_VERSION: The Cloud TPU [software version](https://docs.cloud.google.com/tpu/docs/runtimes).



### Queued resources

To consume any matching reservation using [queued resources](https://docs.cloud.google.com/tpu/docs/queued-resources), use the [`gcloud alpha compute tpus queued-resources create` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/tpus/queued-resources/create) with the [`--reserved` flag](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/tpus/queued-resources/create#--reserved):
    
    
    gcloud alpha compute tpus queued-resources create QUEUED_RESOURCE_ID \
        --node-id=TPU_NAME \
        --zone=ZONE \
        --accelerator-type=ACCELERATOR_TYPE \
        --runtime-version=SOFTWARE_VERSION \
        --reserved

Replace the following placeholder variables:

  * QUEUED_RESOURCE_ID: A user-assigned ID for the queued resource request.
  * TPU_NAME: A user-assigned ID (name) for the TPU that is created when the queued resource request is allocated.
  * ZONE: The zone in which to create the TPU VM and where the reservation exists.
  * ACCELERATOR_TYPE: Specifies the version and size of the Cloud TPU to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * SOFTWARE_VERSION: The Cloud TPU [software version](https://docs.cloud.google.com/tpu/docs/runtimes).



## Check reservation usage

You can only check a shared reservation usage from its owner project. If you are in a consumer project, then you must switch to the owner project to check the reservation usage.

To see how much of the reservation is in use, use the [`gcloud compute reservations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/describe):
    
    
    gcloud compute reservations describe RESERVATION_NAME \
        --project=PROJECT_ID --zone=ZONE

Replace the following placeholder variables:

  * RESERVATION_NAME: The name of the reservation.
  * PROJECT_ID: The ID of the project that contains the reservation.
  * ZONE: The zone where the reservation exists.



To list all reservations in a project, use the [`gcloud compute reservations list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/reservations/list):
    
    
    gcloud compute reservations list --project=PROJECT_ID

Replace the following placeholder variable:

  * PROJECT_ID: The ID of the project.



## What's next

  * [Learn about Cloud TPU reservations](https://docs.cloud.google.com/tpu/docs/about-tpu-reservations)
  * [Share a reservation between projects](https://docs.cloud.google.com/tpu/docs/share-reservation)
  * [Manage your TPUs](https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
