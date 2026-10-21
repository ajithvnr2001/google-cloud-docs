---
url: https://docs.cloud.google.com/compute/docs/nodes/share-node-groups/
title: Share sole-tenant node groups \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:25.483876+00:00
---

# Share sole-tenant node groups  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/nodes/share-node-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Share sole-tenant node groups Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

Shared sole-tenant node groups are similar to [local sole-tenant node groups](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_groups_and_vm_provisioning). For example, shared node groups cost the same, consume the same quota, and reside under a parent project in the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy).

The difference between shared node groups and local node groups is that other projects in your organization can provision virtual machine (VM) instances in the shared node groups.

Sharing a node group across multiple projects or an organization can help you do the following:

  * Consolidate node groups that you manage into a single project and then share those nodes with other projects or the entire organization

  * Decrease costs by deleting nodes after consolidating VMs from various projects into underutilized node groups

  * Manage sole-tenant nodes with a single team

  * Share sole-tenant nodes with smaller projects and retain security and access control boundaries between those projects

  * Perform a live migration between node groups within the same project

  * Improve the utilization of your node groups and reduce the number of reserved maintenance nodes when using the [**Migrate within node group** maintenance policy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#migrate_within_node_group_host_maintenance_policy)




The following diagram shows a node group that is shared with other projects so that other departments that manage VMs in those projects can provision VMs in a shared node group.

![Diagram of a node group that's shared across projects. Departments
            that manage VMs in different projects can provision VMs in a shared
            node group.](https://docs.cloud.google.com/static/compute/images/sole-tenancy/shared-node-groups.svg)

## Utilization benefits of shared node groups

The following table compares projects that use local node groups with projects that use shared node groups. Notice that vCPU underutilization decreases in projects that use shared node groups.

Project configuration | Local node groups | Shared node groups  
---|---|---  
Projects | 10 | 10  
vCPU / project | 24 | 24  
Node groups | 10 | 1  
Nodes / node group | 1 | 3  
vCPU / node | 80 | 80  
Utilization / node group | 24 | 80  
Underutilization / node group | 56 | 0  
**Total underutilization** | **10 x 56 = 560 vCPUs** | **1 x 0 = 0 vCPUs**  
  
## Settings for sharing node groups

Compute Engine uses the following settings for sharing node groups and provisioning VMs in the shared node groups:

  * A share setting that you configure when you create or update the sole-tenant node group. To specify whether to share the node group with other projects or with the entire organization, use the gcloud CLI settings (`--share-setting`, `--share-with`) or REST settings (`shareSetting`, `shareWith`).

  * A default `compute.googleapis.com/project` node affinity label that you use when you provision a VM in a shared node group by using node affinity labels. For information about the other default node affinity labels, see [Default affinity labels](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#default_affinity_labels).




## Maintenance policy considerations

When a node group uses the [**Migrate within node group** maintenance policy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#migrate_within_node_group_host_maintenance_policy), Compute Engine reserves at least 1 node for live migration events, so the node group must have at least 2 nodes. You can't schedule VMs on the reserved node, so node groups with this maintenance policy often have lower overall utilization. This makes workloads that require the **Migrate within node group** maintenance policy good candidates for node group sharing, as they often see the greatest benefit from improved utilization.

## IAM roles and permissions

Keep in mind the following information about IAM roles and permissions when you share a node group:

  * If a node group is shared with a project, any user that can create VMs in the listed projects or in the organization can provision VMs from those projects onto the shared node group without any changes to IAM roles or permissions.

  * The `compute.soleTenantViewer` IAM role lets you list and view node groups ([gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/list-nodes) / [REST](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeGroups/listNodes)). You cannot modify node groups with this role. Any user with this role or with permissions to list node groups, regardless of the IAM permissions on the VM, can view the project ID, name, machine type, and information about local SSDs and GPUs for all VMs in the node group.




## Limitations

  * **Compliance regime limitations:**

    * Regardless of the IAM permissions on the VM, any user with permissions to list node groups can view the project ID, name, and machine type for all VMs in the node group. Thus, due to risk of cross-project information disclosure, projects that have VMs provisioned in shared node groups should be under the same [compliance regime](https://docs.cloud.google.com/assured-workloads/docs/supported-products).
  * **Google Cloud console limitations:**

    * If you don't have permission to view VMs on the shared node group, those VMs won't appear on the VM list on the **Sole-tenant nodes** page in the Google Cloud console.
    * After modifying the sharing settings on the **Sole-tenant node groups** page, the **Shared with** setting is not updated in the UI. To see the updated **Shared with** setting, go to the **Sole-tenant nodes** page.
    * After sharing a node group with all projects within an organization or with selected projects within an organization, you can only see the shared node group from its owning project; you can't see the shared node group from the projects it has been shared with. To provision a VM on the shared node group, from the project that the node group is shared with, go to the **VM instances** page, and then modify the sole tenancy node affinity labels.
  * **Sharing limitations:**

    * You must update the sharing settings from the project that owns the node group.
    * You can specify a maximum of 100 projects when you use the `projects` share setting.
    * You cannot share node groups between organizations. For example, if you [migrate a project](https://docs.cloud.google.com/resource-manager/docs/project-migration) that contains a shared node group from one organization to another, you must also migrate all projects that have VMs running in that shared node group.
    * You cannot perform live migration between projects while using shared sole-tenant node groups. For more information, see [Manually live migrate VMs](https://docs.cloud.google.com/compute/docs/nodes/manually-live-migrate#manually_live_migrate_vms_into_or_within_sole-tenancy).



## Pricing

VMs in shared node groups don't incur additional charges, and there are no additional charges for sharing node groups. For more information about sole-tenant node pricing, see [Sole-tenant node pricing](https://cloud.google.com/compute/sole-tenant-pricing).

## Before you begin

  * Before creating a sole-tenant node group, [create a sole-tenant node template](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms#create_a_sole-tenant_node_template). 
  * Before provisioning VMs in a sole-tenant node, [check your quota](https://docs.cloud.google.com/compute/quotas-limits#check_your_allocation_quota). Depending on the number and size of nodes that you reserve, you might need to [request additional quota](https://docs.cloud.google.com/compute/quotas-limits#edit_your_quota). 
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




## Create a new node group and share it

To create a new node group and share it with other projects or with the entire organization, use the Google Cloud console, gcloud CLI, or REST.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.nodeGroups.create` permissions on the project 



###  Console 

  1. Create a sole-tenant node group. For more information, see [Create a sole-tenant node group](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms#create_a_sole-tenant_node_group).

  2. Configure the share settings by specifying one of the following in **Configure share settings** :

     * To share the node group with all projects in your organization, choose **Share this node group with all projects within the organization**.
     * To share the node group with specific projects within your organization, choose **Share this node group with selected projects within the organization**.

If you don't want to share the node group, choose **Do not share this node group with other projects**.




###  gcloud 

To create a shared node group, use the following [`gcloud compute sole-tenancy node-groups create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/create).
    
    
    gcloud compute sole-tenancy node-groups create NODE_GROUP \
        --zone=ZONE \
        --node-template=NODE_TEMPLATE \
        --target-size=SIZE \
        --share-setting=SHARE_SETTING \
        --share-with=PROJECTS
    

Replace the following:

  * `NODE_GROUP`: the name of the node group.

  * `ZONE`: the zone to create the node group in.

  * `NODE_TEMPLATE`: the name of the previously created node template.

  * `SIZE`: the number of nodes in the node group.

  * `SHARE_SETTING`: the share setting for the node group. Set to `projects` to share with specific projects, or set to `organization` to share with the entire organization.

  * `PROJECTS`: a list of project IDs or project numbers to share the node group with. Only required if you set `SHARE_SETTING` to `projects`.




###  REST 

To create a shared node group, use the following [`nodeGroups.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeGroups/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/nodeGroups
    
    {
      ...
      "name": "NODE_GROUP",
      "nodeTemplate": "NODE_TEMPLATE",
      "size": SIZE,
      "shareSettings": {
        "shareType": "SHARE_TYPE",
        "projectMap": {
          "CONSUMER_PROJECT_ID": {
            "projectId": "CONSUMER_PROJECT_ID"
          }
        }
      }
      ...
    }
    

Replace the following:

  * `PROJECT`: the name of project to create the node group in.

  * `ZONE`: the zone to create the node group in.

  * `NODE_GROUP`: the name of the node group.

  * `NODE_TEMPLATE`: the name of the previously created node template.

  * `SIZE`: the number of nodes in the node group.

  * `SHARE_TYPE`: the share setting for the node group. Set to `SPECIFIC_PROJECTS` to share with specific projects, or set to `ORGANIZATION` to share with the entire organization.

  * `CONSUMER_PROJECT_ID`: the ID of a project to share the node group with. Only required if you set `SHARE_TYPE` to `SPECIFIC_PROJECTS`.




## Provision a sole-tenant VM in a shared node group

To provision a sole-tenant VM in a shared node group, use the Google Cloud console, gcloud CLI, or REST.

###  Console 

  1. In the Google Cloud console, switch to a project that you've shared a node group with.

  2. Go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  3. Click **Create instance**.

  4. In **Zone** , choose the zone of the shared node group.

  5. In **Machine configuration** > **Series** , choose the same machine type that the shared sole-tenant node group template specifies.

  6. Expand the **Advanced options** section.

  7. Expand the **Sole-tenancy** section.

  8. Click **Browse**.

  9. Choose **Select project** and specify the project that contains the shared node group.

  10. Choose the sole-tenant node group or a specific sole-tenant node in that group to provision the VM on.




###  gcloud 

**Provision a VM in a shared node group by using the node group name**

To provision a sole-tenant VM in a shared node group by using the node group name, use the following [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).
    
    
    gcloud compute instances create VM_NAME \
        --machine-type=MACHINE_TYPE \
        --node-group=NODE_GROUP \
        --node-project=NODE_PROJECT
    

Replace the following:

  * `VM_NAME`: the name of the new sole-tenant VM to create in a shared node group

  * `MACHINE_TYPE`: the machine type for the new sole-tenant VM

  * `NODE_GROUP`: the name of the shared node group to create the sole-tenant VM in

  * `NODE_PROJECT`: the project containing the node group to provision the VM in




**Provision a VM in a shared node group by using a node affinity file**

To provision a sole-tenant VM in a shared node group by using a node affinity file, use the following [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).
    
    
    gcloud compute instances create VM_NAME \
        --machine-type=MACHINE_TYPE \
        --node-affinity-file=NODE_AFFINITY_FILE
    

Replace the following:

  * `VM_NAME`: the name of the sole-tenant VM to create in a shared node group by using an affinity label.

  * `MACHINE_TYPE`: the machine type of the sole-tenant VM to create in a shared node group.

  * `NODE_AFFINITY_FILE`: the name of the `.json` file containing the node affinity information. In the node affinity file, set the affinity label key to `"compute.googleapis.com/project"`, the operator equal to `"IN"`, and the value equal to the project containing the node group. For more information about how to configure node affinity, see [Configure node affinity labels](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms#configure_node_affinity_labels).




###  REST 

To provision a sole-tenant VM in a shared node group by using a node affinity file, use the following [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/instances
    
    {
      ...
      "name": VM_NAME,
      "machineType": MACHINE_TYPE,
      "scheduling": {
        ...
        "nodeAffinities": [
          {
            "key": KEY,
            "operator": OPERATOR,
            "values": [
              VALUE
            ]
          }
        ],
        ...
      },
      ...
    }
    

Replace the following:

  * `PROJECT`: the name of the project that owns the node group.

  * `ZONE`: the zone of the node group.

  * `VM_NAME`: the name of the sole-tenant VM to create in a shared node group by using an affinity label.

  * `MACHINE_TYPE`: the machine type of the sole-tenant VM to create in a shared node group.

  * `KEY`: the affinity label. Set to `"compute.googleapis.com/project"`.

  * `OPERATOR`: the affinity label operator. Set to `"IN"`.

  * `VALUE`: the project containing the node group to provision the VM in. Specify one project by using either the project name or project ID.




For more information about how to configure node affinity, see [Configure node affinity labels](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms#configure_node_affinity_labels).

## View the sharing settings of a node group

To view the sharing settings of a node group, use the Google Cloud console, gcloud CLI, or REST.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.nodeGroups.list` permissions on the project 



###  Console 

  1. In the Google Cloud console, go to the **Sole-tenant nodes** page.

[Go to Sole-tenant nodes](https://console.cloud.google.com/compute/soleTenancy)

  2. To view the properties of the node group, in the **Name** column, click the name of the node group.




###  gcloud 

To view the sharing settings of a node group, use the following [`gcloud compute sole-tenancy node-groups describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/describe).
    
    
    gcloud compute sole-tenancy node-groups describe NODE_GROUP
    

Replace `NODE_GROUP` with the name of the node group to view the sharing settings of.

###  REST 

To view the sharing settings of a node group, use the following [`nodeGroups.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeGroups/get).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/nodeGroups
    

Replace the following:

  * `PROJECT`: the name of project with the node group to view the sharing settings of

  * `ZONE`: the zone containing the node group to view the sharing settings of




## Share an existing node group

To share an existing node group with other projects or the entire organization, use the Google Cloud console, gcloud CLI, or REST.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.nodeGroups.update` permissions on the project in which you created the node group 



###  Console 

  1. In the Google Cloud console, go to the **Sole-tenant nodes** page.

[Go to Sole-tenant nodes](https://console.cloud.google.com/compute/soleTenancy)

  2. In the **Name** column, click the name of the node group.

  3. To share the node group with all projects within the organization or with selected projects within the organization, in **Overview** > **Shared with** , click **Edit** edit.




###  gcloud 

To update the sharing settings of a node group, use the following [`gcloud compute sole-tenancy node-groups update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/update).
    
    
    gcloud compute sole-tenancy node-groups update NODE_GROUP \
        --zone=ZONE \
        --share-setting=SHARE_SETTING \
        --share-with=PROJECTS
    

Replace the following:

  * `NODE_GROUP`: the name of the node group to update the sharing settings of.

  * `SHARE_SETTING`: the share setting for the node group. Set to `projects` to share with specific projects, or set to `organization` to share with the entire organization.

  * `PROJECTS`: a list of project IDs or project numbers to share the node group with. Only required if you set `SHARE_SETTING` to `projects`.




###  REST 

To update the sharing settings of a node group, use the following [`nodeGroups.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeGroups/patch).
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/nodeGroups/NODE_GROUP
    
    {
      "shareSettings": {
        "shareType": SHARE_TYPE,
        "projectMap": {
          string: {
            "projectId": PROJECTS
          },
        }
      }
    }
    

Replace the following:

  * `PROJECT`: the name of the project with the node groups to update the sharing settings of.

  * `ZONE`: the zone containing the node groups to update the sharing settings of.

  * `NODE_GROUP`: the name of the node group to update the sharing settings of.

  * `SHARE_TYPE`: the share setting for the node group. Set to `projects` to share with specific projects, or set to `organization` to share with the entire organization.

  * `PROJECTS`: a list of project IDs or project numbers to share the node group with. Only required if you set `SHARE_SETTING` to `SPECIFIC_PROJECTS`.




## Stop sharing a node group

To stop sharing a node group with other projects or the entire organization, use the gcloud CLI or REST.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.nodeGroups.update` permissions on the project in which you created the node group 



###  Console 

  1. In the Google Cloud console, go to the **Sole-tenant nodes** page.

[Go to Sole-tenant nodes](https://console.cloud.google.com/compute/soleTenancy)

  2. Click the **Name** of the node group.

  3. In **Overview** > **Shared with** , click **Edit** edit.

  4. To stop sharing, choose **Do not share this node group with other projects**.




###  gcloud 

To stop sharing a node group with other projects or the entire organization, use the following [`gcloud compute sole-tenancy node-groups update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/update).
    
    
    gcloud compute sole-tenancy node-groups update NODE_GROUP \
        --zone=ZONE \
        --share-setting=local
    

Replace the `NODE_GROUP` with the name of the node group to stop sharing.

###  REST 

To stop sharing a node group with other projects or the entire organization, use the following [`nodeGroups.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeGroups/patch).
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/nodeGroups/NODE_GROUP
    
    {
      "shareSettings": {
        "shareType": LOCAL
      }
    }
    

Replace the following:

  * `PROJECT`: the name of the project with the node group to stop sharing

  * `ZONE`: the zone containing the node group to stop sharing

  * `NODE_GROUP`: the name of the node group to stop sharing




## Delete a shared node group from the owning project

To delete a shared node group from the owning project, use the Google Cloud console, gcloud CLI, or REST. Before deleting a node group, stop all VMs that are running in the node group.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.nodeGroups.delete` permissions on the project in which you created the node group 



###  Console 

  1. In the Google Cloud console, go to the **Sole-tenant nodes** page.

[Go to Sole-tenant nodes](https://console.cloud.google.com/compute/soleTenancy)

  2. In the **Name** column, click the name of the node group.

  3. Click **Delete**.




###  gcloud 

To delete a shared node group from the owning project, use the following [`gcloud compute sole-tenancy node-groups delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/delete).
    
    
    gcloud compute sole-tenancy node-groups delete NODE_GROUP
    

Replace `NODE_GROUP` with the name of the node group to delete.

###  REST 

To delete a shared node group from the owning project, use the following [`nodeGroups.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeGroups/delete).
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/nodeGroups/NODE_GROUP
    

Replace the following:

  * `PROJECT`: the name of the project with the node group to delete

  * `ZONE`: the zone containing the node group to delete

  * `NODE_GROUP`: the name of the node group to delete




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
