---
url: https://docs.cloud.google.com/compute/docs/instance-groups/update-on-repair/
title: Apply configuration updates during repairs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:21.019902+00:00
---

# Apply configuration updates during repairs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/update-on-repair/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Apply configuration updates during repairs Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure your MIG to apply the latest instance template and [per-instance configurations](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#per_instance_configs) when recreating a VM during [repair](https://docs.cloud.google.com/compute/docs/instance-groups/about-repair) operations. Applying the latest available configuration during a repair operation is also known as _update on repair_. This document also describes how to check whether update on repair is enabled in your MIG, and if enabled, how to disable update on repair.

By default, during a repair, a MIG recreates a VM using the same instance configuration that was originally used to create the VM. If updates for the group's instance template or per-instance configurations are available, then you have the option to apply these changes to a VM being repaired.

If you want to automatically apply configuration updates to all or a set of VMs (`PROACTIVE`), or selectively update specific instances (`OPPORTUNISTIC`), see [Applying new configurations to VMs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs).

**Note:** If the update type of your MIG is set to [`PROACTIVE`](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups) and you configure update on repair, then the MIG does not take into account [`maxUnavailable`](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#max_unavailable) during update on repair. For example, assume that the `maxUnavailable` is 5 and the MIG is already in the process of updating 5 VMs based on the update policy. Among the other VMs in the MIG, if 3 VMs fail, then the MIG updates all 3 failed VMs during their repair regardless of `maxUnavailable`.

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




## Configure update on repair

To configure update on repair, use the Google Cloud console, gcloud CLI, or REST.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the MIG where you want to configure update on repair.

  3. Click **Edit** to modify the MIG.

  4. Click **Instance lifecycle and autohealing** to expand the section.

  5. In the **Updates during VM instance repair** section, select **Update the instance configuration**.

  6. Click **Save**.




###  gcloud 

For an existing MIG, use the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update):
    
    
    gcloud compute instance-groups managed update MIG_NAME \
        **--force-update-on-repair**
    

For a new MIG, use the [`create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create):
    
    
    gcloud compute instance-groups managed create MIG_NAME \
        --template INSTANCE_TEMPLATE_URL_ \
        --size SIZE \
        **--force-update-on-repair**
    

Replace the following:

  * `MIG_NAME`: The name of the instance group.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `SIZE`: The target size of the instance group.



###  REST 

For an existing zonal MIG, use the [`instanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch), or, for an existing regional MIG, use the [`regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch).

Make the following call to configure update on repair in an existing zonal MIG:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME
    {
      "instanceLifecyclePolicy": {
        **"forceUpdateOnRepair": YES**
      }
    }
    

For a new zonal MIG, use the [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert), or, for a new regional MIG, use the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert).

Make the following call to configure update on repair when creating a zonal MIG:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers
    {
      "name": "MIG_NAME",
      "instanceTemplate": "INSTANCE_TEMPLATE_URL",
      "targetSize": SIZE,
      "instanceLifecyclePolicy": {
        **"forceUpdateOnRepair": YES**
      }
    }
    

Replace the following:

  * `PROJECT_ID`: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `ZONE`: The zone where the MIG is located.
  * `MIG_NAME`: The name of the instance group.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `SIZE`: The target size of the instance group.



## Check whether update on repair is enabled

By default, a MIG does not update a VM during a repair. To check whether update on repair is enabled for your MIG, use the Google Cloud console, gcloud CLI, or REST to view update on repair configuration.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the MIG of which you want to check the configuration.

  3. Click **Details** tab.

  4. In the **VM instance lifecycle** section, check the option selected for **Updates during VM instance repair**. If the field shows **Update the instance configuration** , then update on repair is enabled.




###  gcloud 

Use the [`describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe) as follows:
    
    
    gcloud compute instance-groups managed describe MIG_NAME \
    --format="(instanceLifecyclePolicy)"
    

In the response body, check for the `forceUpdateOnRepair` field, which has one of the following values:

  * `NO`: Default. MIG doesn't update VMs when they are repaired.
  * `YES`: MIG updates the VMs during their repair.



The following is a sample output:
    
    
    instanceLifecyclePolicy:
     **forceUpdateOnRepair: YES**
    

###  REST 

For a zonal MIG, use the [`instanceGroupManagers.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/get), or, for a regional MIG, use the [`regionInstanceGroupManagers.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/get).

For example, in a zonal MIG, use the following command:
    
    
    GET https://compute.googleapis.com/compute/v1/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME
    

In the response body, check for the `instanceLifecyclePolicy.forceUpdateOnRepair` field, which has one of the following values:

  * `NO`: Default. MIG doesn't update VMs when they are repaired.
  * `YES`: MIG updates the VMs during their repair.



The following is a sample response:
    
    
    {
      ...
      "name": "example-mig",
      "targetSize": 12,
      ...
      "instanceLifecyclePolicy": {
        **"forceUpdateOnRepair": "YES"**
      },
      ...
    }
    

Replace the following:

  * `PROJECT_ID`: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `ZONE`: The zone where the MIG is located.
  * `MIG_NAME`: The name of the instance group.



## Disable update on repair

When your MIG repairs a VM, if you want the MIG to use the original instance template or the per-instance configurations that were used to create the VM, then you must disable update on repair. By default, update on repair is disabled for a MIG.

Use the Google Cloud console, gcloud CLI, or REST to disable update on repair.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the MIG where you want to disable update on repair.

  3. Click **Edit** to modify the MIG.

  4. Click **Instance lifecycle and autohealing** to expand the section.

  5. In the **Updates during VM instance repair** section, select **Keep the same instance configuration**.

  6. Click **Save**.




###  gcloud 

Use the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update) to set the `--no-force-update-on-repair` flag as follows:
    
    
    gcloud compute instance-groups managed update MIG_NAME \
        **--no-force-update-on-repair**
    

###  REST 

For a zonal MIG, use the [`instanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch), or, for a regional MIG, use the [`regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch).

For example, to disable update on repair for a zonal MIG, use the following command:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME
    {
      "instanceLifecyclePolicy":
      { "forceUpdateOnRepair": NO
      }
    }
    

Replace the following:

  * `PROJECT_ID`: Your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `ZONE`: The zone where the MIG is located.
  * `MIG_NAME`: The name of the instance group.



## What's next

  * [Set up application health check and autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs).
  * If you have configured an application-based health check for your MIG, [monitor VM health state changes](https://docs.cloud.google.com/compute/docs/instance-groups/monitoring-managed-instance-health-state-changes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
