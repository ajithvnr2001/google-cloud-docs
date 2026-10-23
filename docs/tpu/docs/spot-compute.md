---
url: https://docs.cloud.google.com/tpu/docs/spot-compute/
title: Request TPU Spot VMs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:15.765333+00:00
---

# Request TPU Spot VMs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/spot-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Request TPU Spot VMs

Spot VMs offer unused capacity at significantly discounted rates. While Spot VMs are preemptible at any time, they don't have a maximum runtime duration, unlike [preemptible TPUs](https://docs.cloud.google.com/tpu/docs/preemptible). To restart a Spot VMs instance or MIG, you must delete and then recreate it.

For more information about Spot VMs, see the [Compute Engine documentation about Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot).

## Create TPU Spot VMs

You can create TPU Spot VMs as individual instances or as part of a managed instance group (MIG).

### Using MIGs for multi-host slices (Recommended)

To create TPU Spot VMs with a MIG, specify the Spot provisioning model in your instance template.

  1. **Create an instance template** :

###  gcloud 
         
         gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
             --project=PROJECT_ID \
             --machine-type=MACHINE_TYPE \
             --maintenance-policy=TERMINATE \
             --instance-termination-action=STOP \
             --provisioning-model=SPOT \
             --image-family=IMAGE_FAMILY \
         --image-project=IMAGE_PROJECT
         

###  REST 
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -d '{
             "name": "INSTANCE_TEMPLATE_NAME",
             "properties": {
             "machineType": "MACHINE_TYPE",
             "disks": [
                 {
                 "boot": true,
                 "initializeParams": {
                     "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
                 }
                 }
             ],
             "scheduling": {
                 "onHostMaintenance": "TERMINATE",
                 "provisioningModel": "SPOT",
                 "instanceTerminationAction": "STOP"
             },
             "networkInterfaces": [
                 {
                 "network": "global/networks/default"
                 }
             ]
             }
         }' \
         "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/instanceTemplates"
         

Replace the following placeholders:

     * PROJECT_ID: The ID of your Google Cloud project.
     * INSTANCE_TEMPLATE_NAME: The name of your instance template.
     * MACHINE_TYPE: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM, for example, `ct6e-standard-8t`.
     * IMAGE_FAMILY: The [OS image family](https://docs.cloud.google.com/compute/docs/images/os-details#ga_ubuntu_lts_versions) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
     * IMAGE_PROJECT: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.
  2. **Create a workload policy**

The following command creates a workload policy. This is optional for single-host slices.

###  gcloud 
         
         gcloud compute resource-policies create workload-policy WORKLOAD_POLICY_NAME \
         --type=high-throughput \
         --accelerator-topology=TOPOLOGY \
         --region=REGION
         

###  REST 
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           -d '{
             "name": "WORKLOAD_POLICY_NAME",
             "workloadPolicy": {
               "type": "HIGH_THROUGHPUT",
               "acceleratorTopology": "TOPOLOGY"
             }
           }' \
           "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies"
         

Replace the following placeholders:

     * `PROJECT_ID`: The ID of your Google Cloud project.
     * `WORKLOAD_POLICY_NAME`: The name of your workload policy.
     * `TOPOLOGY`: The topology of the TPU VMs, for example, `4x4x8`. For more information about topology for each version of TPU, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
     * `REGION`: The [region](https://docs.cloud.google.com/tpu/docs/regions-zones) for your workload policy.
  3. **Create the MIG** :

###  gcloud 
         
         gcloud compute instance-groups managed create MIG_NAME \
         --size=MIG_SIZE \
         --target-size-policy-mode=bulk \
         --template=INSTANCE_TEMPLATE_URL \
         --zone=ZONE \
         --default-action-on-vm-failure=do-nothing \
         --workload-policy=WORKLOAD_POLICY_URL
         

###  REST 
         
         curl -X POST \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           -d '{
                 "name": "MIG_NAME",
                 "targetSize": MIG_SIZE,
                 "targetSizePolicy": {
                   "mode": "BULK"
                 },
                 "instanceTemplate": "INSTANCE_TEMPLATE_URL",
                 "instanceLifecyclePolicy": {
                   "defaultActionOnFailure": "DO_NOTHING"
                 },
                 "resourcePolicies": {
                   "workloadPolicy": "WORKLOAD_POLICY_URL"
                 }
               }' \
             "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers"
         

Replace the following placeholders:

     * `PROJECT_ID`: The ID of your Google Cloud project.
     * `MIG_NAME`: The name of your MIG.
     * `MIG_SIZE`: The size of the MIG.
     * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
       * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
       * For a global instance template: `INSTANCE_TEMPLATE_ID`
     * `ZONE`: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) for your MIG.
     * `WORKLOAD_POLICY_URL`: The URL of the workload policy that you want to use to create instances in the MIG. For example: `projects/PROJECT_ID/regions/WORKLOAD_POLICY_REGION/resourcePolicies/WORKLOAD_POLICY_NAME`.
**Note:** For multi-host TPU slices, you must define a [workload policy](https://docs.cloud.google.com/ai-hypercomputer/docs/placement-policy-and-workload-policy#workload-policy) and use the `--target-size-policy-mode=bulk` flag when creating the MIG to ensure that all VMs are created in the same network and can communicate.



### Using single TPU VMs

You can also create single TPU Spot VMs.

###  gcloud 
    
    
    gcloud compute instances create TPU_NAME \
      --machine-type=MACHINE_TYPE \
      --image-family=IMAGE_FAMILY \
      --image-project=IMAGE_PROJECT \
      --zone=ZONE \
      --provisioning-model=SPOT \
      --instance-termination-action=DELETE \
      --maintenance-policy=TERMINATE
    

###  REST 
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "TPU_NAME",
        "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
            }
          }
        ],
        "scheduling": {
          "onHostMaintenance": "TERMINATE",
          "provisioningModel": "SPOT",
          "instanceTerminationAction": "DELETE"
        },
        "networkInterfaces": [
          {
            "network": "global/networks/default"
          }
        ]
      }' \
      "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances"
    

Replace the following placeholders:

  * PROJECT_ID: The ID of your Google Cloud project.
  * TPU_NAME: A name for your TPU VM.
  * MACHINE_TYPE: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM (for example `ct6e-standard-8t`).
  * IMAGE_FAMILY: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
  * IMAGE_PROJECT: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.
  * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) for the TPU VM (for example `us-central1-b`).



For more information about Spot VMs in Compute Engine, see [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot).

## Pricing and quota

Pricing for TPU Spot VMs is significantly lower than for on-demand and reserved TPUs. For more information about pricing, see [Cloud TPU pricing](https://docs.cloud.google.com/tpu/docs/pricing).

You need preemptible quota to use TPU Spot VMs. For more information, see [Quotas](https://docs.cloud.google.com/tpu/docs/quota).

## What's next

  * Learn how to [manage TPUs](https://docs.cloud.google.com/tpu/docs/managing-tpus-compute)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
