---
url: https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-basic-autoscaling/
title: Create a MIG with autoscaling enabled \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:07:35.889298+00:00
---

# Create a MIG with autoscaling enabled  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-basic-autoscaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a MIG with autoscaling enabled Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create an autoscaled [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) that automatically adds and removes VMs based on average CPU utilization across the group. For example, if the group's CPU utilization is low, the group automatically removes VMs to save on costs.

You can automatically scale a MIG based on various kinds of autoscaling signals. For more information, see the [autoscaler overview](https://docs.cloud.google.com/compute/docs/autoscaler).

You can also read about other [basic scenarios for creating a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#create_managed_group).

## Before you begin

  * [Create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates), which is required in order to create a managed instance group.
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




## Limitations

To see the full list of MIG limitations, which varies based on the configuration that you use, see [MIG limitations](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#limitations).

## Create a MIG and enable autoscaling

Use the [Google Cloud console](https://console.cloud.google.com/), the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-autoscaling), Terraform, or [REST](https://docs.cloud.google.com/compute/docs/reference/latest).

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.autoscalers.create` on the project
  * `compute.instanceGroupManagers.use` on the project



###  Console 

  1. In the console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups?walkthrough_id=compute--instance-groups--create-mig-enable-autoscaling&start_index=1#step_index=1)

The remaining steps appear in the Google Cloud console.

  2. If you have an instance group, select it and click **Edit**. If you don't have an instance group, click **Create instance group**. 
  3. For a new instance group, assign a name, then choose an instance template for the instance group or [create a new one](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).
  4. If no autoscaling configuration exists, under **Autoscaling** , click **Configure autoscaling**. 
  5. Under **Autoscaling mode** , select **On: add and remove instances to the group** to enable autoscaling. 
  6. Specify the minimum and maximum numbers of instances that you want the autoscaler to create in this group. 
  7. In the **Autoscaling metrics** section, if an existing **CPU utilization** metric does not yet exist, add one: 
     1. Click **Add metric**. 
     2. Under **Metric type** , select **CPU utilization**. 
     3. Enter the **Target CPU utilization** that you want. This value is treated as a percentage. For example, for 75% CPU utilization, enter `75`. 
     4. Under **Predictive autoscaling** , select **Off**. To learn more about predictive autoscaling, and whether it is suitable for your workload, see [Scaling based on predictions](https://docs.cloud.google.com/compute/docs/autoscaler/predictive-autoscaling). 
     5. Click **Done**. 
  8. You can use the **Initialization period** to set the initialization period, which tells the autoscaler how long it takes for your application to initialize. Specifying an accurate initialization period improves autoscaler decisions. For example, when scaling out, the autoscaler ignores data from VMs that are still initializing because those VMs might not yet represent normal usage of your application. The default initialization period is 60 seconds. 
  9. To create the MIG, click **Create**.



###  gcloud 

Before you can enable autoscaling, you must create a MIG. Follow the instructions to [create a MIG with VMs confined to a single zone](https://docs.cloud.google.com/compute/docs/instance-groups/create-zonal-mig) or [create a MIG with VMs spread across multiple zones in a region](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups).

Then use the [`set-autoscaling`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-autoscaling) sub-command to enable autoscaling for the group. For example, the following command creates an autoscaler that has a target CPU utilization of 60%. Along with the `--target-cpu-utilization` parameter, the `--max-num-replicas` parameter is also required when creating an autoscaler.

Optionally, you can set the `--min-num-replicas` indicating the minimum number of VMs that you want in the group. If you don't set the minimum, by default, MIG sets this value to 2.

You can use the `--cool-down-period` flag to set the initialization period, which tells the autoscaler how long it takes for your application to initialize. Specifying an accurate initialization period improves autoscaler decisions. For example, when scaling out, the autoscaler ignores data from VMs that are still initializing because those VMs might not yet represent normal usage of your application. The default initialization period is 60 seconds. 

**Note:** If autoscaling is already enabled for a managed instance group, the [`set-autoscaling`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-autoscaling) command overwrites the existing autoscaler to the new specifications.
    
    
    gcloud compute instance-groups managed set-autoscaling example-managed-instance-group \
      --max-num-replicas 20 \
      --target-cpu-utilization 0.60 \
      --cool-down-period 90
    

If you want, you can enable predictive autoscaling to scale out ahead of predicted load. To learn whether predictive autoscaling is suitable for your workload, see [Scaling based on predictions](https://docs.cloud.google.com/compute/docs/autoscaler/predictive-autoscaling).

You can verify that autoscaling is successfully enabled by using the [`instance-groups managed describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe), which describes the corresponding MIG and provides information about any autoscaling features for that group:
    
    
    gcloud compute instance-groups managed describe example-managed-instance-group

###  Terraform 

Before you can enable autoscaling, you must create a MIG. Follow the instructions to [create a MIG with VMs confined to a single zone](https://docs.cloud.google.com/compute/docs/instance-groups/create-zonal-mig) or [create a MIG with VMs spread across multiple zones in a region](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups).

To configure autoscaling in a MIG, you can use the [`google_compute_autoscaler` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_autoscaler).

The following sample configures autoscaling based on CPU utilization in a zonal MIG.
    
    
    resource "google_compute_autoscaler" "default" {
      name   = "example-autoscaler"
      zone   = "us-central1-f"
      target = google_compute_instance_group_manager.default.id
    
      autoscaling_policy {
        max_replicas    = 20
        min_replicas    = 0
        cooldown_period = 90
    
        cpu_utilization {
          target = 0.60
        }
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

Before you can enable autoscaling, you must [create a MIG with VMs confined to a single zone](https://docs.cloud.google.com/compute/docs/instance-groups/create-zonal-mig) or [create a MIG with VMs spread across multiple zones in a region](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups).

**Note:** Although autoscaling is a feature of managed instance groups, it is a separate API resource. Keep that in mind when you construct API requests for autoscaling.

If you have a zonal MIG, make a `POST` request to the [`autoscalers.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers/insert) method. If you have a regional MIG, use the [`regionAutoscalers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers/insert).

For example:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/autoscalers/

Your request body must contain the `name`, `target`, and `autoscalingPolicy` fields. The `autoscalingPolicy` field must define your target `cpuUtilization` value and `maxNumReplicas` value.

Optionally, you can set the `minNumReplicas` indicating the minimum number of VMs that you want in the group. If you don't set the minimum, by default, MIG sets this value to 2.

You can use the `coolDownPeriodSec` field to set the initialization period, which tells the autoscaler how long it takes for your application to initialize. Specifying an accurate initialization period improves autoscaler decisions. For example, when scaling out, the autoscaler ignores data from VMs that are still initializing because those VMs might not yet represent normal usage of your application. The default initialization period is 60 seconds. 
    
    
    {
      "name": "example-autoscaler",
      "target": "https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-f/instanceGroupManagers/example-managed-instance-group",
      "autoscalingPolicy": {
        "maxNumReplicas": 10,
        "cpuUtilization": {
          "utilizationTarget": 0.6
        },
        "coolDownPeriodSec": 90
      }
    }
    

If you want, you can enable predictive autoscaling to scale out ahead of predicted load. To learn whether predictive autoscaling is suitable for your workload, see [Scaling based on predictions](https://docs.cloud.google.com/compute/docs/autoscaler/predictive-autoscaling).

For more information about enabling autoscaling based on CPU utilization, see [Scaling based on CPU utilization](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-cpu).

## What's next

  * Learn more about [autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler) and the different kinds of scaling signals that you can add to an [autoscaling policy](https://docs.cloud.google.com/compute/docs/autoscaler#autoscaling_policy).
  * Read about [Managing autoscalers](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers).
  * [Set up application-based autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs), which periodically verifies that your application responds as expected on each of the MIG's VMs and automatically recreates unresponsive VMs.
  * Learn how to [apply a new configuration](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs) to all or to a subset of the VMs in a MIG by setting and applying a new instance template, all-instances configuration, or per-instance configuration.
  * Learn how to [add an external HTTP(S) load balancer frontend to your instance group](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute). For information about other types of load balancers, see the [Load balancing overview](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
