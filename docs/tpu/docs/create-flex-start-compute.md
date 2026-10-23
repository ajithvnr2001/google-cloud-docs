---
url: https://docs.cloud.google.com/tpu/docs/create-flex-start-compute/
title: Create TPU Flex-start VMs with Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:23.835212+00:00
---

# Create TPU Flex-start VMs with Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/create-flex-start-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create TPU Flex-start VMs with Compute Engine

TPU Flex-start VMs, powered by [Dynamic Workload Scheduler](https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler), offer a flexible, cost-effective way to access TPU resources for AI workloads for up to 7 days without long-term reservations. When you request TPU Flex-start VMs, your request remains in a queue until capacity is available. Once provisioned, the TPU VMs run for your specified duration.

TPU Flex-start VMs are a good fit for quick experimentation, small-scale testing, dynamic provisioning of TPUs for inference workloads, model fine-tuning, and workload runs that take less than 7 days. For more information about other TPU consumption options, see [Cloud TPU consumption options](https://docs.cloud.google.com/tpu/docs/consumption-options).

You can delete your TPU resources at any time to stop billing. For more information about TPU pricing, see [Cloud TPU pricing](https://cloud.google.com/tpu/pricing).

## Limitations

TPU Flex-start VMs have the following limitations:

  * You can request TPU Flex-start VMs for a duration of up to 7 days. 
  * You can request TPU7x, TPU v6e, and TPU v5p machine types. For more information about the regions and zones where these machine types are available, see [TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones). 



MIGs with TPUs have the following limitations:

  * **Lifecycle operations** : You can't stop, start, resume, or suspend TPU instances. To change configurations that require a restart or to stop incurring charges, you must delete the instances. 

  * **Regional MIG zone distribution** : You must set the [target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape) to `ANY_SINGLE_ZONE`.

  * **Configuration updates in a MIG** :

    * You can't [update](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs) a MIG that forms a multi-host TPU slice due to the defined accelerator topology.
    * You can update a MIG that forms single-host TPU slices by using the [automatic or selective methods](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#choosing_between_automated_and_selective_updates). However, the updates for single-host TPU slice don't support the restart (`RESTART`) action. If a restart is necessary and the most disruptive action allowed is replace (`REPLACE`), then the updater will replace the instance; otherwise, the update attempt fails with an error.
  * For a MIG that forms a multi-host TPU slice, the following limitations also apply: 

  * **Target size policy** : You must set the target size policy mode to [`BULK`](https://docs.cloud.google.com/compute/docs/instance-groups/about-bulk-mode). After you set this mode, you can't change it.

  * **Target size** : In bulk mode, you can set the target size to either `0` or the number of instances that are required to form the accelerator topology.

  * **Workload policy** : You must specify a workload policy in which the accelerator topology is defined. After you set the workload policy, you can't change or remove the policy from the MIG.

  * **MIG initiated repairs** : You must [turn off MIG initiated repairs](https://docs.cloud.google.com/compute/docs/instance-groups/turn-off-vm-repairs-in-mig) by setting the `defaultActionOnFailure` field to `DO_NOTHING`. In this configuration, the MIG doesn't take any action on a failed instance. Compute Engine automatically recovers the failed instance by restarting all instances in the same slice on healthy capacity. 



* **Unsupported features** : MIGs with TPUs don't support the following features:

  * [Instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility)
  * [Resize requests](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig) to obtain resources all at once
  * [Stateful configuration](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#stateful_configuration)
  * For a MIG that forms a multi-host TPU slice, the following are also not supported: 
    * [Autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler)
    * [Abandon instances](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#abandoning_instances)
    * [Delete instances](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group)



## Before you begin

Before requesting TPU Flex-start VMs, you must:

  * Install the Google Cloud CLI
  * Create a Google Cloud project
  * Enable the Compute Engine API (`compute.googleapis.com`)
  * Ensure you have the required permissions: 
    * `roles/compute.instanceAdmin.v1`
    * `roles/iam.serviceAccountUser`



For more information, see [Set up a Google Cloud project for TPUs](https://docs.cloud.google.com/tpu/docs/setup-gcp-account).

Ensure you have sufficient preemptible quota to use TPU Flex-start VMs. If your workload requires more cores than your current allocation, you can request a quota increase. For details, see [Cloud TPU quotas](https://docs.cloud.google.com/tpu/docs/quota).

## Create TPU Flex-start VMs with MIGs

To use TPU Flex-start VMs, you create a managed instance group (MIG) with a specific instance template configuration.

For general instructions on creating Flex-start VMs, see [Create Flex-start VMs](https://docs.cloud.google.com/compute/docs/instances/create-flex-start-vm).

### Create TPU Flex-start VMs with a multi-host slice

#### Create an instance template

Create an instance template specifying the `FLEX_START` provisioning model and your chosen run duration.

###  gcloud 
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --provisioning-model=FLEX_START \
        --instance-termination-action=DELETE \
        --max-run-duration=DURATION \
        --region=REGION \
        --maintenance-policy=TERMINATE
    

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
            "provisioningModel": "FLEX_START",
            "instanceTerminationAction": "DELETE",
            "maxRunDuration": {
              "seconds": "DURATION"
            }
          },
          "networkInterfaces": [
            {
              "network": "global/networks/default"
            }
          ]
        }
      }' \
      "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceTemplates"
    

Replace the following placeholders:

  * PROJECT_ID: The ID of your Google Cloud project.
  * INSTANCE_TEMPLATE_NAME: The name of your instance template.
  * MACHINE_TYPE: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM (for example, `ct6e-standard-8t`).
  * IMAGE_FAMILY: The OS image family for the TPU VM (for example, `ubuntu-accelerator-2204-amd64-with-tpu-v6e`)
  * IMAGE_PROJECT: The OS image project for the TPU VM (for example, `ubuntu-os-accelerator-images`)
  * DURATION: The maximum run duration. For REST, specify this as a number of seconds (for example, `3600` for 1 hour, or `604800` for 7 days).
  * REGION: The [region](https://docs.cloud.google.com/tpu/docs/regions-zones) in which to create the instance template.



#### Create a workload policy

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

  * PROJECT_ID: The ID of your Google Cloud project.
  * WORKLOAD_POLICY_NAME: The name of your workload policy.
  * TOPOLOGY: The topology of the TPU VMs, for example, `4x4x8`.
  * REGION: The [region](https://docs.cloud.google.com/tpu/docs/regions-zones) in which to create the workload policy.



#### Create the MIG

Create the MIG using the template.

###  gcloud 
    
    
    gcloud compute instance-groups managed create MIG_NAME \
        --zone=ZONE \
        --template=INSTANCE_TEMPLATE_URL \
        --size=SIZE \
        --workload-policy=WORKLOAD_POLICY_URL \
        --default-action-on-vm-failure=do-nothing \
        --target-size-policy-mode=bulk
    

###  REST 
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "MIG_NAME",
        "targetSize": SIZE,
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

  * PROJECT_ID: The ID of your Google Cloud project.
  * MIG_NAME: The name of your MIG.
  * ZONE: The zone of your MIG.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * SIZE: The number of instances to create.
  * WORKLOAD_POLICY_URL: The URL of the workload policy that you want to use to create instances in the MIG. For example: `projects/PROJECT_ID/regions/WORKLOAD_POLICY_REGION/resourcePolicies/WORKLOAD_POLICY_NAME`.



### Create TPU Flex-start VMs with single-host slices

#### Create an instance template

Create an instance template specifying the `FLEX_START` provisioning model and your chosen run duration.

###  gcloud 
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --provisioning-model=FLEX_START \
        --instance-termination-action=DELETE \
        --max-run-duration=DURATION \
        --region=REGION \
        --maintenance-policy=TERMINATE
    

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
            "provisioningModel": "FLEX_START",
            "instanceTerminationAction": "DELETE",
            "maxRunDuration": {
              "seconds": "DURATION"
            }
          },
          "networkInterfaces": [
            {
              "network": "global/networks/default"
            }
          ]
        }
      }' \
      "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceTemplates"
    

Replace the following placeholders:

  * PROJECT_ID: The ID of your Google Cloud project.
  * INSTANCE_TEMPLATE_NAME: The name of your instance template.
  * MACHINE_TYPE: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM (for example, `ct6e-standard-8t`).
  * IMAGE_FAMILY: The OS image family for the TPU VM (for example, `ubuntu-accelerator-2204-amd64-with-tpu-v6e`)
  * IMAGE_PROJECT: The OS image project for the TPU VM (for example, `ubuntu-os-accelerator-images`)
  * DURATION: The maximum run duration. For REST, specify this as a number of seconds (for example, `3600` for 1 hour, or `604800` for 7 days).
  * REGION: The [region](https://docs.cloud.google.com/tpu/docs/regions-zones) in which to create the instance template.



#### Create a workload policy

The following command creates a workload policy. This is optional for single-host slices.

###  gcloud 
    
    
    gcloud compute resource-policies create workload-policy WORKLOAD_POLICY_NAME \
      --type=high-throughput \
      --region=REGION
    

###  REST 
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "WORKLOAD_POLICY_NAME",
        "workloadPolicy": {
          "type": "HIGH_THROUGHPUT"
        }
      }' \
      "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies"
    

Replace the following placeholders:

  * PROJECT_ID: The ID of your Google Cloud project.
  * WORKLOAD_POLICY_NAME: A name for your workload policy.
  * REGION: The [region](https://docs.cloud.google.com/tpu/docs/regions-zones) in which to create the workload policy.



#### Create the MIG

Create the MIG using the template.

###  gcloud 
    
    
    gcloud compute instance-groups managed create MIG_NAME \
        --zone=ZONE \
        --template=INSTANCE_TEMPLATE_URL \
        --size=SIZE \
        --workload-policy=WORKLOAD_POLICY_URL
    

###  REST 
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "MIG_NAME",
        "targetSize": SIZE,
        "instanceTemplate": "INSTANCE_TEMPLATE_URL",
        "resourcePolicies": {
          "workloadPolicy": "WORKLOAD_POLICY_URL"
        }
      }' \
      "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers"
    

Replace the following placeholders:

  * PROJECT_ID: The ID of your Google Cloud project.
  * MIG_NAME: The name of your MIG.
  * ZONE: The zone of your MIG.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * SIZE: The number of instances to create.
  * WORKLOAD_POLICY_URL: The URL of the workload policy that you want to use to create instances in the MIG. For example: `projects/PROJECT_ID/regions/WORKLOAD_POLICY_REGION/resourcePolicies/WORKLOAD_POLICY_NAME`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
