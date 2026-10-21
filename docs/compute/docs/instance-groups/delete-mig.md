---
url: https://docs.cloud.google.com/compute/docs/instance-groups/delete-mig/
title: Delete a MIG \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:43.401250+00:00
---

# Delete a MIG  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/delete-mig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Delete a MIG Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to delete a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) that you no longer need so you can stop paying for the resources it uses.

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




## Delete a MIG

When you delete a MIG, all VMs in the group are deleted. You can't recover the MIG or its VMs. Before you delete a MIG, consider the following:

  * If you want to keep any of the VMs, [abandon the VMs](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#abandoning_instances) first to remove those VMs from the group. Then, delete the MIG.

  * If you enabled [graceful shutdown](https://docs.cloud.google.com/compute/docs/instances/graceful-shutdown-overview) in the instance template that your MIG uses, then the VMs in your MIG gracefully shut down when you delete the MIG. Because VMs continue to incur charges for memory and vCPUs while a graceful shutdown is in progress, you can end the graceful shutdown early when your tasks finish running, or skip it entirely if you don't need to finish active tasks.




The disks in a MIG are deleted only if you had set the disk's auto-delete property to true when defining the disks in the MIG's instance template. If a disk's auto-delete property is set to false, then you can manually clean up the disks when you no longer need them.

**Important:** You cannot delete an instance group if it is being used by a load balancer's [backend service](https://docs.cloud.google.com/compute/docs/load-balancing/http/backend-service). [Remove the backend service](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/remove-backend) before deleting the instance group.

When you delete a managed instance group and its instances by using the [Google Cloud console](https://console.cloud.google.com/) or the [gcloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute), any attached autoscaler is automatically deleted. However, if you use the [REST](https://docs.cloud.google.com/compute/docs/reference/latest/instanceGroupManagers), you must first issue a separate request to delete any attached autoscaler with the [`autoscalers.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers/delete) or [`regionAutoscalers.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers/delete). If you happen to delete the managed instance group first, you can still delete the attached autoscaler by using REST.

For each disk, you can also override the auto-delete property to specify whether the disk should be deleted when its associated instance is deleted.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instanceGroupManagers.delete` on the managed instance group



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Select one or more groups on the list that you want to delete.

  3. Click delete **Delete**. If there is no **Delete** option, then click **More actions** , and then select **Delete**.

  4. In the dialog that appears, do the following:

     1. Optional: To delete the compute instances without gracefully shutting them down, or to end an ongoing graceful shutdown, select the **Skip graceful shutdown (if applicable)** checkbox.

     2. To confirm, click **Delete**.




###  gcloud 

Use the [`delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/delete).
    
    
    gcloud compute instance-groups managed delete INSTANCE_GROUP_NAME \
        --zone ZONE

If you want to delete a MIG without gracefully shutting down its VMs, or end an ongoing graceful shutdown, then use the same command with the `--no-graceful-shutdown` flag:
    
    
    gcloud compute instance-groups managed delete INSTANCE_GROUP_NAME \
        **--no-graceful-shutdown** \
        --zone ZONE

###  REST 

Call the `delete` method for a [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/delete) or [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/delete) MIG resource. If the MIG has an attached autoscaler, you must first delete the autoscaler using the [`autoscalers.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers/delete) or [`regionAutoscalers.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers/delete).
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/INSTANCE_GROUP_NAME

If the instance group is a regional managed instance group, replace `zones/ZONE` with `regions/REGION`.

If you want to delete a MIG without gracefully shutting down its VMs, or to end an ongoing graceful shutdown, then include the `noGracefulShutdown` query parameter set to `true` in the request URL:
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/INSTANCE_GROUP_NAME**?noGracefulShutdown=true**

## What's next

  * Learn about [Getting, listing, and deleting instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
