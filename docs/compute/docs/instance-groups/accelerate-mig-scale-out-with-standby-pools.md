---
url: https://docs.cloud.google.com/compute/docs/instance-groups/accelerate-mig-scale-out-with-standby-pools/
title: Accelerate scale out with suspended and stopped VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:18:26.380997+00:00
---

# Accelerate scale out with suspended and stopped VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/accelerate-mig-scale-out-with-standby-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Accelerate scale out with suspended and stopped VMs Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how the standby pool of suspended and stopped virtual machine (VM) instances works and how you can use the standby pool to accelerate the scale out of a managed instance group (MIG).

## Before you begin

  * Review the introductory page about [suspended and stopped VMs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/suspended-and-stopped-vms-in-mig).
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Use MIG API for autoscaling

We recommend that you use Compute Engine autoscaler for autoscaling your MIG. However, if for some reason you prefer to use a different autoscaler, use the endpoints of the [MIG API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers) to handle suspended and stopped VMs.

## Choose between suspended and stopped pools

Choosing between suspended and stopped pools depends on your specific use case. For best performances, you should experiment with different standby pool types for your scale out scenarios to determine which one best suits your needs. Different workloads might show shorter time to serve with different options. In some cases, the operation of copying the memory state from storage to the VM might take more time than restarting the VM or creating a new VM from scratch.

To find the best approach, start from these guidelines:

  * Use suspended VMs if your VMs require a time-consuming memory initialization, because suspended VMs preserve the memory state. Make sure that your application can be suspended and resumed. Keeping the memory state requires additional storage and might incur extra costs.
  * Use stopped VMs if your VM initialization focuses mainly on the initialization of data stored in the persistent disks.



## Edit the standby policy in a MIG

This section describes how to set the standby pool mode to scale out pool and the initial delay.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the instance group that you want to edit.

  3. Click **Edit** to modify this managed instance group.

  4. Click **Advanced options** to expand the section.

  5. In the **Standby pool** section, select **Scale-out**.

  6. In the **Initial delay** field, enter the number of seconds that the MIG should wait before suspending or stopping a VM. The initial delay gives the initialization script the time to prepare your VM for quick scale out.

  7. Click **Save**.




###  gcloud 

Use the [`instance-groups managed update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update) and specify the operation mode and the initial delay.
    
    
    gcloud compute instance-groups managed update MIG_NAME \
      --standby-policy-mode=scale-out-pool \
      --standby-policy-initial-delay=DELAY \
      [--region=REGION | --zone=ZONE]
    

Replace the following:

  * `MIG_NAME`: the name of the MIG.
  * `DELAY`: the number of seconds that the MIG should wait before suspending or stopping a VM. The initial delay gives the initialization script the time to prepare your VM for quick scale out.
  * `REGION`: for a regional MIG, the region where the MIG is located.
  * `ZONE`: for a zonal MIG, the zone where the MIG is located.



###  Terraform 

The following sample creates a zonal MIG with a standby policy. Use the `standby_policy` block to set an initial delay and to set the mode to `SCALE_OUT_POOL`.

The sample uses the [`google_compute_instance_group_manager` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_group_manager). For a regional MIG, use the [`google_compute_region_instance_group_manager` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_instance_group_manager).
    
    
    resource "google_compute_instance_group_manager" "default" {
      name               = "standby-mig"
      base_instance_name = "test"
      target_size        = 3
      zone               = "us-central1-f"
    
      version {
        instance_template = google_compute_instance_template.default.id
        name              = "primary"
      }
      standby_policy {
        initial_delay_sec = 50
        mode              = "SCALE_OUT_POOL"
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

Use the [`instanceGroupManager.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) and specify the operation mode and initial delay in the request body. For regional MIGs, use the [`regionInstanceGroupManager.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch).
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME
    
    {
    // ...
    "standbyPolicy": {
      "mode": "SCALE_OUT_POOL",
      "initialDelaySec": DELAY
    }
    // ...
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `ZONE`: for a zonal MIG, the zone where the MIG is located. 
    * For a regional MIG, replace `zones/ZONE` with `regions/REGION` and specify the region of the MIG.
  * `MIG_NAME`: the name of the MIG.
  * `DELAY`: the number of seconds that the MIG should wait before suspending or stopping a VM. The initial delay gives the initialization script the time to prepare your VM for quick scale out.



## Resize the standby pool in a MIG

This section describes how to resize the standby pools of suspended and stopped VMs in a MIG.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the instance group that you want to edit.

  3. Click **Edit** to modify this managed instance group.

  4. Click **Advanced options** to expand the section.

  5. In the **Standby pool** section, enter the new sizes in the **Suspended VMs** and **Stopped VMs** fields.

  6. Click **Save**.




###  gcloud 

Use the [`instance-groups managed update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update) with the `--suspended-size` and `--stopped-size` flags.
    
    
    gcloud compute instance-groups managed update MIG_NAME \
    --suspended-size=SUSPENDED_SIZE \
    --stopped-size=STOPPED_SIZE \
    [--region=REGION | --zone=ZONE]
    

Replace the following:

  * `MIG_NAME`: the name of the MIG in which to suspend an instance.
  * `SUSPENDED_SIZE`: the number of suspended VMs that the MIG should maintain at any given time.
  * `STOPPED_SIZE`: the number of stopped VMs that the MIG should maintain at any given time.
  * `REGION`: for a regional MIG, the region where the MIG is located.
  * `ZONE`: for a zonal MIG, the zone where the MIG is located.



###  Terraform 

The following sample creates a zonal MIG with target sizes for suspended and stopped VMs. To set the target sizes, use the `target_suspended_size` and the `target_stopped_size` arguments.

The sample uses the [`google_compute_instance_group_manager` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_group_manager). For a regional MIG, use the [`google_compute_region_instance_group_manager` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_instance_group_manager).
    
    
    resource "google_compute_instance_group_manager" "default" {
      name                  = "standby-mig"
      base_instance_name    = "test"
      target_size           = 1
      target_suspended_size = 1
      target_stopped_size   = 2
      zone                  = "us-central1-f"
    
      version {
        instance_template = google_compute_instance_template.default.id
        name              = "primary"
      }
      standby_policy {
        initial_delay_sec = 50
        mode              = "SCALE_OUT_POOL"
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

Use the [`instanceGroupManager.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) and specify the sizes of pools of suspended and stopped VMs in the request body. For regional MIGs, use the [`regionInstanceGroupManager.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch).
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME
    
    {
    // ...
    "targetSuspendedSize": SUSPENDED_SIZE,
    "targetStoppedSize": STOPPED_SIZE
    // ...
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `ZONE`: for a zonal MIG, the zone where the MIG is located. 
    * For a regional MIG, replace `zones/ZONE` with `regions/REGION` and specify the region of the MIG.
  * `MIG_NAME`: the name of the MIG in which to stop an instance.
  * `SUSPENDED_SIZE`: the number of suspended VMs that the MIG should maintain at any given time.
  * `STOPPED_SIZE`: the number of stopped VMs that the MIG should maintain at any given time.



## What's next

  * Learn how to [manually suspend or stop VMs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/manually-suspend-or-stop-vms-in-mig).
  * Learn more about [updates for suspended and stopped VMs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#update_standby_pool).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
