---
url: https://docs.cloud.google.com/compute/docs/instance-groups/turn-off-vm-repairs-in-mig/
title: Turn off repairs in a MIG \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:25.927642+00:00
---

# Turn off repairs in a MIG  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/turn-off-vm-repairs-in-mig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Turn off repairs in a MIG Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to turn off repairs of failed and unhealthy VMs in a managed instance group (MIG) and, if already turned off, how to configure the MIG to repair VMs.

By default, a MIG automatically repairs a failed VM in the group by recreating that VM. If you've configured an application-based health check, then the MIG also repairs unhealthy VMs on which your application fails the health check. Repairing a VM based on an application-based health check is also called _autohealing_.

If you don't want a MIG to repair a failed VM or an unhealthy VM, you can turn off repairs in the MIG. Turning off repairs is useful in scenarios when you want to troubleshoot a failed VM, implement your own repair logic, or monitor application health without repairing unhealthy VMs.

To check whether repairs are already turned off in a MIG, [check the repair configuration in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#check_vm_repairs_turned_off).

For more information about repairs in a MIG, see [About repairing VMs for high availability](https://docs.cloud.google.com/compute/docs/instance-groups/about-repair).

## Before you begin

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

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Turn off repairs in a MIG

When you turn off repairs in a MIG, by default, both failed VM repairs and autohealing are turned off. If you only want to turn off autohealing, see Turn off autohealing.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instanceGroupManagers.update` on the managed instance group



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the MIG in which you want to turn off repair.

  3. Click **Edit**.

  4. Click **Instance lifecycle and autohealing** to expand the section.

     1. In the **Action on failure** section, set the **Default action on failure** field to **No action**.
     2. If you've configured autohealing and don't want the MIG to turn off autohealing, then in the **Autohealing** section, set the **On failed health check** field to **Repair instance**.
  5. Click **Save**.




###  gcloud 

To turn off repairs in a MIG, then use the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update) as follows. This turns off autohealing by default.
    
    
    gcloud compute instance-groups managed update MIG_NAME \
        --default-action-on-vm-failure=do-nothing \
        --zone=ZONE
    

If autohealing is configured in the MIG and you don't want to turn off autohealing by default, use the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update) to set the `--action-on-vm-failed-health-check` flag to `repair`. This ensures that autohealing of unhealthy VMs continues to work even if repairing failed VMs is turned off.
    
    
    gcloud compute instance-groups managed update MIG_NAME \
        --default-action-on-vm-failure=do-nothing \
        --action-on-vm-failed-health-check=repair \
        --zone=ZONE
    

Replace the following:

  * `MIG_NAME`: the name of the instance group.
  * `ZONE`: the zone where your MIG is located. For a regional MIG, use the `--region=REGION` flag.



###  REST 

To turn off repairs in a MIG, then use the API methods as follows. This turns off autohealing by default.

  * For a zonal MIG, use the [`instanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch).
  * For a regional MIG, use the [`regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch).



For example, make the following call in a zonal MIG. This turns off autohealing by default.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME
    
    {
      "instanceLifecyclePolicy":
        {
          "defaultActionOnFailure": "DO_NOTHING"
        }
      }
    

If autohealing is configured in the MIG and you don't want to turn off autohealing by default, use the API methods as follows to set the `onFailedHealthCheck` flag to `REPAIR`. This ensures that autohealing of unhealthy VMs continues to work even if repairing failed VMs is turned off.

  * For a zonal MIG, use the [`instanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch).
  * For a regional MIG, use the [`regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch).



For example, make the following call in a zonal MIG:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME
    
    {
      "instanceLifecyclePolicy":
        {
          "defaultActionOnFailure": "DO_NOTHING",
          "onFailedHealthCheck": "REPAIR"
        }
      }
    

Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `MIG_NAME`: the name of the MIG.
  * `ZONE`: the zone where the MIG is located. For a regional MIG, use `regions/REGION` in the URL.



### Limitations

If a MIG has any of the following, then you cannot turn off the repairs in the MIG by setting the `defaultActionOnFailure` field to `DO_NOTHING`:

  * [autoscaling configuration](https://docs.cloud.google.com/compute/docs/autoscaler)
  * [suspended or stopped VMs](https://docs.cloud.google.com/compute/docs/instance-groups/suspended-and-stopped-vms-in-mig)



## Turn off autohealing

When you've configured an application health check in a MIG, if you don't want the MIG to repair any unhealthy VMs, you can turn off autohealing separately. This doesn't turn off repairs of failed VMs.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instanceGroupManagers.update` on the managed instance group



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the MIG in which you want to turn off autohealing.

  3. Click **Edit**.

  4. Click **Instance lifecycle and autohealing** to expand the section.

  5. In the **Autohealing** section, set the **On failed health check** field to **No action**.

  6. Click **Save**.




###  gcloud 

To turn off autohealing in an existing MIG, use the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update) and set the `--action-on-vm-failed-health-check` flag to `do-nothing`.

For example, use the following command for a zonal MIG:
    
    
    gcloud compute instance-groups managed update MIG_NAME \
        --action-on-vm-failed-health-check=do-nothing \
        --zone=ZONE
    

Replace the following:

  * `MIG_NAME`: the name of the MIG.
  * `ZONE`: the zone where the MIG is located. For a regional MIG, use the `--region=REGION` flag.



###  REST 

To turn off autohealing in a MIG, use the API methods as follows and set the `--action-on-vm-failed-health-check` flag to `do-nothing`.

  * For a zonal MIG, use the [`instanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch).
  * For a regional MIG, use the [`regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch).



For example, make the following request to turn off autohealing in a zonal MIG:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME
    
    {
      "instanceLifecyclePolicy":
       {
         "onFailedHealthCheck": "DO_NOTHING"
       }
    }
    

Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `ZONE`: The zone where the MIG is located. For a regional MIG, use `regions/REGION` in the URL.
  * `MIG_NAME`: the name of the instance group.



## Turn on repairs or autohealing

By default, a MIG repairs failed VMs and, if autohealing is configured, the MIG also repairs unhealthy VMs. If you've turned off repairs or autohealing or both, you can turn them back on again.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instanceGroupManagers.update` on the managed instance group



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the MIG in which you want to turn on repair.

  3. Click **Edit**.

  4. Click **Instance lifecycle and autohealing** to expand the section.

     * To repair failed VMs, in the **Action on failure** section, set the **Default action on failure** field to **Repair instance**.
     * To repair unhealthy VMs, in the **Autohealing** section, set the **On failed health check** field to **Repair instance**. If you set this value to **Default action** , then autohealing uses the same setting that you configure for the **Default action on failure** field.
  5. After you finish, click **Save** to apply the changes.




###  gcloud 

To turn on repairs in a MIG, use the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update). This also turns on autohealing, if the value of the `--action-on-vm-failed-health-check` flag is `default-action`.
    
    
    gcloud compute instance-groups managed update MIG_NAME \
        --default-action-on-vm-failure=repair
    

If you've turned off autohealing separately and you want to turn it back on again, use the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update):
    
    
    gcloud compute instance-groups managed update MIG_NAME \
        --action-on-vm-failed-health-check=default-action OR repair
    

Replace the following:

  * `MIG_NAME` with the name of a MIG.
  * `default-action` OR `repair`: If you want autohealing to use the same setting that you configure for repairs of failed VMs, set the value to `default-action`. For example, when you turn off repairing of failed VMs, the MIG turns off autohealing also. If you want to control repairs of unhealthy VMs separately, set the value to `repair`.



###  REST 

To turn on repairs in a MIG, use the API method as follows. This also turns on autohealing, if the value of the `onFailedHealthCheck` field is `DEFAULT_ACTION`.

  * For a zonal MIG, use the [`instanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch).
  * For a regional MIG, use the [`regionInstanceGroupManagers.patch`method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch).



For example, make the following request in a zonal MIG:
    
    
        PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME
        {
          "instanceLifecyclePolicy": {
            "defaultActionOnFailure": "REPAIR"
          }
        }
      

If you've turned off autohealing separately and you want to turn it back on again, use the API method as follows:

  * For a zonal MIG, use the [`instanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch).
  * For a regional MIG, use the [`regionInstanceGroupManagers.patch`method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch).


    
    
      PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME
      {
        "instanceLifecyclePolicy": {
          "onFailedHealthCheck": "DEFAULT_ACTION OR REPAIR"
        }
      }
    

Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `ZONE`: the zone where your MIG is located. For a regional MIG, use `regions/REGION` in the URL.
  * `MIG_NAME`: the name of the MIG.
  * `DEFAULT_ACTION` OR `REPAIR`: If you want autohealing to use the same setting as for repairs of failed VMs, set the value to `DEFAULT_ACTION`. For example, when you turn off repairing of failed VMs, the MIG turns off autohealing also. If you want to configure autohealing separately, set the value to `REPAIR`.



## What's next

  * [Check the repair configuration in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#check_vm_repairs_turned_off).
  * Investigate the errors in a failed VM by [listing instance errors](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#listing_instance_errors).
  * [Inspect the health state of a VM](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#checking_whether_instances_are_healthy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
