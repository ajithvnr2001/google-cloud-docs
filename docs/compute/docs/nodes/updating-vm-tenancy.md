---
url: https://docs.cloud.google.com/compute/docs/nodes/updating-vm-tenancy/
title: Updating VM tenancy \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:20:36.236804+00:00
---

# Updating VM tenancy  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/nodes/updating-vm-tenancy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Updating VM tenancy Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This page describes how to update a VM's tenancy by modifying the VM's node affinity labels.

By default, Compute Engine deploys VMs on multi-tenant hosts. On multi-tenant hosts, VMs typically share host resources with VMs from other projects and customers. When you move a VM to a [sole-tenant node](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes), your project has exclusive access to and complete control of the sole-tenant node hardware. You are the only tenant on that node, so your workloads are isolated from the workloads of other projects and their VMs.

By modifying node affinity labels, you can move a VM in the following ways:

  * From a multi-tenant host to a sole-tenant node group or node
  * From a sole-tenant node group or node to a multi-tenant host
  * From one sole-tenant node to another sole-tenant node or node group
  * From a sole-tenant node group to another sole-tenant node group or node



## Temporarily moving workloads into sole-tenancy

Due to fluctuating requirements of your workloads, such as periodic needs for additional isolation to examine performance, or changes to your compliance regulations, you might need to temporarily move specific workloads to sole-tenant nodes. Then, when you no longer need sole-tenancy, redeploy your VMs to a multi-tenant host. When you modify the tenancy of a VM, Compute Engine preserves the configurations of the VM.

## Rebalancing sole-tenant workloads

In addition to moving VMs to and from sole-tenant nodes and node groups, you can move VMs between nodes and node groups, which can help you consolidate nodes and rebalance workloads. Moving a VM requires a restart, so plan moving VMs based on the availability requirements of your workloads.

## Limitations

  * When you move a VM that is already running on a sole-tenant node, the VM might restart on another node. If a VM's sole tenancy is specified by node group name or by using the `node-group-name` [default affinity label](https://docs.cloud.google.com/compute/docs/nodes#default_affinity_labels), the VM can restart on any node in the node group. If the VM's sole tenancy is specified using affinity or anti-affinity [custom affinity labels](https://docs.cloud.google.com/compute/docs/nodes#custom_affinity_labels), the VM might restart on any node of any node group in the zone.



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




## Moving a VM into sole-tenancy

Update tenancy by moving the VM to a specific sole-tenant node or node group from another node or node group or from a multi-tenant host.

###  gcloud 

  1. Stop the VM.
         
         gcloud compute instances stop VM_NAME
         

Replace `VM_NAME` with the name of the VM to stop.

  2. Update the tenancy by specifying the node group to move the VM to.
         
         gcloud compute instances set-scheduling VM_NAME \
             --node-group=NODE_GROUP_NAME
         

Replace the following:

     * `VM_NAME` name of the VM to move to a specific node group

     * `NODE_GROUP_NAME` name of the node group to move the VM to

Alternatively, you can move a VM to a sole-tenant node by using the name of the node or by using a affinity label. For more information, see the [`gcloud compute instances set-scheduling` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling).

  3. Start the VM.
         
         gcloud compute instances start VM_NAME
         

Replace `VM_NAME` with the name of the VM to start on the node group previously specified by the contents of an affinity label file.




###  REST 

  1. Stop the VM. For more information about this command, see [instances.stop](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/stop).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/stop
         

Replace the following:

     * `PROJECT_ID`: ID of the project containing the VM to stop

     * `ZONE` zone containing the project

     * `VM_NAME` name of the VM to stop

  2. Update the tenancy by specifying the node group to move the VM to.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setScheduling
         
         {
           "nodeAffinities": [
             {
               "key": "compute.googleapis.com/node-group-name",
               "operator": "IN",
               "values": [
                 "NODE_GROUP_NAME"
               ]
             }
           ]
         }
         

Replace the following:

     * `PROJECT_ID` ID of the project containing the VM to move

     * `ZONE` zone containing the project

     * `VM_NAME` name of the VM to move to a specific node group

     * `NODE_GROUP_NAME` name of the node group to move the VM to

Alternatively, you can move a VM to a sole-tenant node by using the name of the node or by using a affinity label. For more information, see the [`instances.setScheduling` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/setScheduling).

  3. Start the VM. For more information about this command, see [`instances.start`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/start).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/start
         

Replace the following:

     * `PROJECT_ID` ID of the project containing the VM to start

     * `ZONE` zone containing the project

     * `VM_NAME` name of the VM to start




## Moving a VM out of sole-tenancy

If your VM no longer requires dedicated hardware, for example, after an event that required your VM to be isolated from other VMs, move the VM from a sole-tenant node to a multi-tenant host.

###  gcloud 

  1. Stop the VM.
         
         gcloud compute instances stop VM_NAME
         

Replace `VM_NAME` with the name of the VM to stop.

  2. Clear the node affinities from the VM so you can move it to a multi-tenant host.
         
         gcloud compute instances set-scheduling VM_NAME --clear-node-affinities
         

Replace `VM_NAME` with the name of the VM for which to [remove node affinities](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/set-scheduling#--clear-node-affinities).

  3. Start the VM on a multi-tenant host.
         
         gcloud compute instances start VM_NAME
         

Replace `VM_NAME` with the name of the VM from which you previously cleared the node affinities.




###  REST 

  1. Stop the VM. For more information about this command, see [`instances.stop`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/stop).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/stop
         

Replace the following:

     * `PROJECT_ID` ID of the project containing the VM to stop

     * `ZONE` zone containing the project

     * `VM_NAME` name of the VM to stop

  2. Clear the node affinities from the VM to move it to a multi-tenant host.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setScheduling
         
         {
           "nodeAffinities": []
         }
         

Replace the following:

     * `PROJECT_ID` ID of the project containing the VM to move

     * `ZONE` zone containing the project

     * `VM_NAME` name of the VM from which to clear node affinities

  3. Start the VM on a multi-tenant host. For more information about this command, see [instances.start](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/start).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/start
         

Replace the following:

     * `PROJECT_ID` ID of the project containing the VM to start

     * `ZONE` zone containing the project

     * `VM_NAME` name of the VM to start




## What's next

  * Before moving VMs onto sole-tenant nodes, read about [sole-tenant node pricing](https://cloud.google.com/compute/sole-tenant-pricing).


  * Read [Bringing your own licenses](https://docs.cloud.google.com/compute/docs/nodes/bringing-your-own-licenses).
  * Read the [FAQ about Microsoft licenses](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing-faq).
  * Learn [how to bring images with existing licenses to Google Cloud](https://docs.cloud.google.com/compute/docs/instances/windows/bring-your-own-license/bringing-your-own-license-sole-tenant-nodes).
  * Learn how to [autoscale sole-tenant node groups](https://docs.cloud.google.com/compute/docs/nodes/autoscaling-node-groups).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
