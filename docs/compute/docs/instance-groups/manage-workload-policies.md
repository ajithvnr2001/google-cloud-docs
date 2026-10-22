---
url: https://docs.cloud.google.com/compute/docs/instance-groups/manage-workload-policies/
title: Replace, remove, or delete workload policies \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:37.728374+00:00
---

# Replace, remove, or delete workload policies  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/manage-workload-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Replace, remove, or delete workload policies Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to replace, remove, or delete workload policies from managed instance groups (MIGs). These actions are useful in the following scenarios:

  * **Replace a workload policy** : you can change how Compute Engine instances are located within your MIG, or switch to a different workload policy that better fits your workload's requirements.

  * **Remove a workload policy** : you can stop using specific placement rules if your workload no longer needs them, reverting the MIG to default compute instance placement behavior.

  * **Delete a workload policy** : you can permanently delete workload policies that you no longer need.




To learn how to create a workload policy, see [Create workload policies for MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/create-workload-policies).

## Limitations

You can replace or remove a workload policy from a MIG only if there are no compute instances in the MIG.

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

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




### Required roles

To get the permissions that you need to replace, remove, or delete workload policies, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to replace, remove, or delete workload policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to replace, remove, or delete workload policies:

  * To replace or remove a workload policy from a MIG: `compute.instances.update` on the project 
  * To delete a workload policy: `compute.resourcePolicies.delete` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Replace a workload policy in a MIG

To replace a workload policy in a MIG with a different, existing workload policy, select one of the following options:

###  gcloud 

  1. [Manually set the size of the MIG to `0`](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#resize_managed_group).

  2. To replace the workload policy in your MIG, use the [`gcloud compute instance-groups managed update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update) with the `--workload-policy` flag. Based on the MIG type, include one of the following flags:

     * To replace the workload policy in a zonal MIG, include the `--zone` flag:
           
           gcloud compute instance-groups managed update MIG_NAME \
               --workload-policy=WORKLOAD_POLICY \
               --zone=ZONE
           

     * To replace the workload policy in a regional MIG, include the `--region` flag:
           
           gcloud compute instance-groups managed update MIG_NAME \
               --workload-policy=WORKLOAD_POLICY \
               --region=REGION
           

Replace the following:

     * `MIG_NAME`: the name of the MIG.

     * `WORKLOAD_POLICY`: the name of the workload policy that you want to apply to your MIG.

     * `ZONE`: the zone where your zonal MIG exists.

     * `REGION`: the region where your regional MIG and the workload policy exist.




###  REST 

  1. [Manually set the size of the MIG to `0`](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#resize_managed_group).

  2. To replace the workload policy in your MIG, make a `PATCH` request to one of the following methods:

     * To replace the workload policy in a zonal MIG, make a `PATCH` request to the [`compute.instanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch):
           
           PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME
           
           {
             "workloadPolicy": "projects/PROJECT_ID/regions/REGION/resourcePolicies/WORKLOAD_POLICY"
           }
           

     * To replace the workload policy in a regional MIG, make a `PATCH` request to the [`compute.regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch):
           
           PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/MIG_NAME
           
           {
             "workloadPolicy": "projects/PROJECT_ID/regions/REGION/resourcePolicies/WORKLOAD_POLICY"
           }
           

Replace the following:

     * `PROJECT_ID`: the ID of the project where your MIG and the workload policy exist.

     * `ZONE`: the zone where your zonal MIG exists.

     * `REGION`: the region where your regional MIG and the workload policy exist.

     * `MIG_NAME`: the name of your MIG.

     * `WORKLOAD_POLICY`: the name of the workload policy that you want to apply to your MIG.




## Remove a workload policy from a MIG

To remove a workload policy from a MIG, select one of the following options:

###  gcloud 

  1. [Manually set the size of the MIG to `0`](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#resize_managed_group).

  2. To remove a workload policy from a MIG, use the [`gcloud compute instance-groups managed update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update) with the `--remove-workload-policy` flag. Based on the MIG type, include one of the following flags:

     * To remove a workload policy from a zonal MIG, include the `--zone` flag:
           
           gcloud compute instance-groups managed update MIG_NAME \
               --remove-workload-policy=WORKLOAD_POLICY \
               --zone=ZONE
           

     * To remove a workload policy from a regional MIG, include the `--region` flag:
           
           gcloud compute instance-groups managed update MIG_NAME \
               --remove-workload-policy=WORKLOAD_POLICY \
               --region=REGION
           

Replace the following:

     * `MIG_NAME`: the name of your MIG.

     * `WORKLOAD_POLICY`: the name of the workload policy that is applied to your MIG.

     * `ZONE`: the zone where your zonal MIG exists.

     * `REGION`: the region where your regional MIG exists.




###  REST 

  1. [Manually set the size of the MIG to `0`](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#resize_managed_group).

  2. To remove a workload policy from a MIG, make a `PATCH` request to one of the following methods:

     * To remove a workload policy from a zonal MIG, make a request to the [`compute.instanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch):
           
           PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME
           
           {
             "workloadPolicy": ""
           }
           

     * To remove a workload policy from a regional MIG, make a request to the [`compute.regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch):
           
           PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/MIG_NAME
           
           {
             "workloadPolicy": ""
           }
           

Replace the following:

     * `PROJECT_ID`: the ID of the project where your MIG and the workload policy exist.

     * `ZONE`: the zone where your zonal MIG exists.

     * `REGION`: the region where your regional MIG and the workload policy exist.

     * `MIG_NAME`: the name of your MIG.




## Delete a workload policy

You can't delete a workload policy that's applied to a MIG. Before you delete the policy, you must remove it from the MIG.

To delete a workload policy, select one of the following options:

###  gcloud 

To delete a workload policy, use the [`gcloud compute resource-policies delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/delete):
    
    
    gcloud compute resource-policies delete WORKLOAD_POLICY \
        --region=REGION
    

Replace the following:

  * `WORKLOAD_POLICY`: the name of an existing workload policy.

  * `REGION`: the region where the workload policy exists.




###  REST 

To delete a workload policy, make a `DELETE` request to the [`resourcePolicies.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/delete):
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the workload policy exists.

  * `REGION`: the region where the workload policy exists.

  * `POLICY_NAME`: the name of an existing workload policy.




## What's next

  * Learn how to [view workload policies](https://docs.cloud.google.com/compute/docs/instance-groups/view-workload-policies).

  * Learn how to [create workload policies for MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/create-workload-policies).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
