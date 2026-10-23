---
url: https://docs.cloud.google.com/tpu/docs/consume-reservation-compute/
title: Consume a reservation \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:24.068844+00:00
---

# Consume a reservation  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/consume-reservation-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Consume a reservation

If you have a TPU reservation, you can use your reserved resources to create TPUs that match the reservation's properties. This action is known as _consuming a reservation_. For information about consuming a TPU reservation when using Google Kubernetes Engine (GKE), see [TPU reservation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus#tpu_reservation) in the GKE documentation.

How you consume a reservation depends on how you create your TPU VMs. You can create TPU VM instances or a MIG with TPUs.

## Consume a reservation when creating a TPU VM

When you create a TPU VM instance, specify the reservation to consume by using the `--reservation-affinity=specific` and `--reservation` parameters:
    
    
      gcloud compute instances create TPU_NAME \
        --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --zone=ZONE \
        --reservation-affinity=specific \
        --reservation=projects/PROJECT_ID/reservations/RESERVATION_NAME \
        --provisioning-model=reservation-bound \
        --maintenance-policy=TERMINATE
    

Replace the following placeholders:

  * TPU_NAME: The name of your TPU VM.
  * MACHINE_TYPE: The machine type for the TPU VM (for example, `ct6e-standard-8t`).
  * IMAGE_FAMILY: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
  * IMAGE_PROJECT: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.
  * ZONE: The zone for the TPU VM (for example, us-central1-b).
  * PROJECT_ID: The ID of the project for which the reservation was made.
  * RESERVATION_NAME: The name of the reservation formatted as `projects/OWNER_PROJECT_ID/reservations/RESERVATION_NAME`.



## Consume a reservation when creating a MIG

There are two kinds of MIGs you can create with TPU VMs:

  * MIGs with single-host slices.
  * MIGs with a multi-host slice.



### Consume a reservation when you create a MIG with single-host slices

To consume a reservation when you create a MIG with single-host slices, you specify the reservation as part of the instance template.

To create a MIG with single-host slices:

  1. Create instance template
  2. Optional: Create workload policy
  3. Create MIG



#### Create an instance template that consumes a reservation
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
         --machine-type=MACHINE_TYPE \
         --maintenance-policy=TERMINATE \
         --instance-termination-action=DELETE \
         --reservation-affinity=specific \
         --provisioning-model=reservation-bound \
         --reservation=RESERVATION_NAME \
         --image-family=IMAGE_FAMILY \
         --image-project=IMAGE_PROJECT
    

Replace the following placeholders:

  * INSTANCE_TEMPLATE_NAME: The name of your instance template.
  * MACHINE_TYPE: The machine type for the TPU VM (for example, `ct6e-standard-8t`).
  * RESERVATION_NAME: The name of the reservation formatted as `projects/OWNER_PROJECT_ID/reservations/RESERVATION_NAME`.
  * IMAGE_FAMILY: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
  * IMAGE_PROJECT: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.



#### Create the MIG

You can create a [zonal MIG](https://docs.cloud.google.com/compute/docs/instance-groups/create-zonal-mig) or a [regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs).

##### Create a zonal MIG
    
    
    gcloud compute instance-groups managed create MIG_NAME \
        --size=SIZE \
        --template=INSTANCE_TEMPLATE_NAME \
        --zone=ZONE
    

Replace the following placeholders:

  * MIG_NAME: The name of your MIG.
  * SIZE: The number of TPU VMs in the MIG.
  * INSTANCE_TEMPLATE_NAME: The name of your instance template.
  * ZONE: The zone where you want your MIG to be provisioned.



##### Create a regional MIG
    
    
    gcloud compute instance-groups managed create MIG_NAME \
        --size=SIZE \
        --template=INSTANCE_TEMPLATE_NAME\
        --region=REGION \
        --target-distribution-shape=any
    

Replace the following placeholders:

  * MIG_NAME: The name of your MIG.
  * SIZE: The number of TPU VMs in the MIG.
  * INSTANCE_TEMPLATE_NAME: The name of your instance template.
  * REGION: The zone where you want your MIG to be provisioned.



For more information about `--target-distribution-shape` flag, see [Set a target distribution shape for VMs in a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape).

### Consume a reservation when you create a MIG with a multi-host slice

To consume a reservation when you create a MIG with a multi-host slice, you specify the reservation as part of the instance template.

#### Create an instance template that consumes a reservation
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
         --machine-type=MACHINE_TYPE \
         --maintenance-policy=TERMINATE \
         --instance-termination-action=DELETE \
         --reservation-affinity=specific \
         --provisioning-model=reservation-bound \
         --reservation=RESERVATION_NAME \
         --image-family=IMAGE_FAMILY \
         --image-project=IMAGE_PROJECT
    

Replace the following placeholders:

  * INSTANCE_TEMPLATE_NAME: The name of your instance template.
  * MACHINE_TYPE: The machine type for the TPU VM (for example, `ct6e-standard-8t`).
  * RESERVATION_NAME: The name of the reservation formatted as `projects/OWNER_PROJECT_ID/reservations/RESERVATION_NAME`.
  * IMAGE_FAMILY: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
  * IMAGE_PROJECT: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.



#### Create a workload policy

You can specify a workload policy for your MIGs. For more information, see [Workload policy for MIGs](https://docs.cloud.google.com/ai-hypercomputer/docs/placement-policy-and-workload-policy#workload-policy).
    
    
    gcloud compute resource-policies create workload WORKLOAD_POLICY_NAME \
      --type=high-throughput \
      --accelerator-topology=TOPOLOGY
    

Replace the following placeholders:

  * WORKLOAD_POLICY_NAME: A name for your workload policy.
  * TOPOLOGY: The topology of the TPU VMs, for example, `4x4x8`. For more information about topology for each version of TPU, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).



#### Create the MIG

You can create a zonal or regional MIG.

##### Create a zonal MIG
    
    
    gcloud compute instance-groups managed create MIG_NAME \
        --size=SIZE \
        --target-size-policy-mode=bulk \
        --default-action-on-vm-failure=do-nothing \
        --template=INSTANCE_TEMPLATE_URL \
        --zone=ZONE \
        --workload-policy=WORKLOAD_POLICY_URL
    

Replace the following placeholders:

  * MIG_NAME: The name of your MIG.
  * SIZE: The number of TPU VMs in the MIG.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * ZONE: The zone where you want your MIG to be provisioned.
  * WORKLOAD_POLICY_URL: The URL of the workload policy that you want to use to create instances in the MIG. For example: `projects/PROJECT_ID/regions/WORKLOAD_POLICY_REGION/resourcePolicies/WORKLOAD_POLICY_NAME`



##### Create a regional MIG
    
    
    gcloud compute instance-groups managed create MIG_NAME \
        --size=SIZE \
        --target-size-policy-mode=bulk \
        --default-action-on-vm-failure=do-nothing \
        --template=INSTANCE_TEMPLATE_URL \
        --zone=ZONE \
        --target-distribution-shape=any-single-zone \
        --instance-redistribution-type=none \
        --workload-policy=WORKLOAD_POLICY_URL
    

Replace the following placeholders:

  * MIG_NAME: The name of your MIG.
  * SIZE: The number of TPU VMs in the MIG.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * ZONE: The zone where you want your MIG to be provisioned.
  * WORKLOAD_POLICY_URL: The URL of the workload policy that you want to use to create instances in the MIG. For example: `projects/PROJECT_ID/regions/WORKLOAD_POLICY_REGION/resourcePolicies/WORKLOAD_POLICY_NAME`



## Check reservation usage

You can only check shared reservation usage from its owner project. If you are in a consumer project, you must switch to the owner project to check the reservation usage.

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
