---
url: https://docs.cloud.google.com/compute/docs/nodes/manually-live-migrate/
title: Manually live migrate VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:18.403301+00:00
---

# Manually live migrate VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/nodes/manually-live-migrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manually live migrate VMs Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

To move sole-tenant VMs to a different node or node group, you can manually initiate a live migration. You can also manually initiate a live migration to move a multi-tenant VM into sole-tenancy. For information about how to move a VM out of sole-tenancy, see [Move a VM out of sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/updating-vm-tenancy#moving_a_vm_out_of_sole-tenancy).

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




## API rate limits

Manual live migration requests are categorized in the **Queries** [API rate limit](https://docs.cloud.google.com/compute/docs/api-rate-limits).

## Manually live migrate VMs into or within sole-tenancy

To manually live migrate VMs into or within sole-tenancy, use the gcloud CLI or REST.

If the destination of the VM is a node group, Compute Engine selects the node within the group that has both enough space for the VM and the least amount of spare capacity.

You cannot perform live migration between projects while using shared sole-tenant node groups.

**Warning:** If a node group uses the [**Migrate within node group** (`MIGRATE_WITHIN_NODE_GROUP`) host maintenance policy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#migrate_within_node_group_host_maintenance_policy), then you can't manually live migrate and pin active VMs to a specific node within that group. Doing so results in a scheduling compatibility constraint error. Instead, target the node group by specifying `--node-group` in the gcloud CLI or the `compute.googleapis.com/node-group-name` affinity label key in REST.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions):

  * `compute.instances.update` permissions on the VM. 



###  gcloud 

To manually live migrate VMs into or within sole-tenancy, use the following [`gcloud compute instances update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/update):
    
    
    gcloud compute instances update VM_NAME \
        ( --node=NODE \
          --node-group=NODE_GROUP \
          --node-affinity-file=NODE_AFFINITY_FILE )
    

Replace the following:

  * `VM_NAME`: the name of the VM to update the node affinity labels for.



Replace exactly one of the following:

  * `NODE`: the name of the node to live migrate the VM to.

  * `NODE_GROUP`: the name of the node group to live migrate the VM to.

  * `NODE_AFFINITY_FILE`: the name of a JSON file containing a configuration of nodes on which this VM could be scheduled. For more information, see [Configure node affinity labels](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms#configure_node_affinity_labels).




###  REST 

To manually live migrate VMs into or within sole-tenancy, use the following [`instances.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/update):
    
    
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME
    
    {
      ...
      "scheduling": {
        "nodeAffinities": [
          {
            "key": "NODE_AFFINITY_LABEL_KEY",
            "operator": "IN",
            "values": [
              "NODE_AFFINITY_LABEL_VALUE"
            ]
          }
        ]
      }
      ...
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that has the VM to update the node affinity labels for.

  * `ZONE`: the zone of the VM to update the node affinity labels for.

  * `VM_NAME`: the name of the VM to update the node affinity labels for.

  * `NODE_AFFINITY_LABEL_KEY`: one of the following strings that specifies whether to live migrate the VM to a node group or node:

VM destination | Key to specify  
---|---  
Node group | `compute.googleapis.com/node-group-name`  
Node | `compute.googleapis.com/node-name`  
  * `NODE_AFFINITY_LABEL_VALUE`: the name of the node group or node to live migrate the VM to.




## What's next

  * [Learn how to move a VM out of sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/updating-vm-tenancy#moving_a_vm_out_of_sole-tenancy)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
