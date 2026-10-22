---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-configure-hub/
title: Configure a hub \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:24.548977+00:00
---

# Configure a hub  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-configure-hub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Configure a hub Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information about how to create a hub to which VPC spokes in a different project can be attached. It also provides details about how to select the preset options for [mesh or star connectivity topologies](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies) for VPC spokes during hub creation.

As a hub administrator, you can update a spoke group by using the [`gcloud network-connectivity hubs groups update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/update). You can add a list of project IDs or project numbers to enable auto-accept for spokes. When auto-accept is enabled, the spoke from the auto-accept project is automatically connected to the hub without the need for individual spoke proposal review and goes into the `ACTIVE` state. For projects not included in the auto-accept list, the spoke remains in the `INACTIVE` state until you review and accept the spoke.

You can list the _center_ and _edge_ groups as nested resources for a specific hub by using the [`gcloud network-connectivity hubs groups list --hub` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/list). For hubs created with the mesh topology, the output returns the default group. For hubs created with the star topology, the output returns _center_ and _edge_ groups.

## Before you begin

Before you get started, review the following sections.

### Create or select a project

To make it easier to configure NCC, start by identifying a valid project.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. If you are using the Google Cloud CLI, set your project ID by using the [`gcloud config set` command](https://docs.cloud.google.com/sdk/gcloud/reference/config/set).
         
         gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your unique project ID.

The gcloud CLI instructions on this page assume that you have set your project ID. 

  13. To confirm that you set the project ID correctly, use the [`gcloud config list` command](https://docs.cloud.google.com/sdk/gcloud/reference/config/list).
         
         gcloud config list --format='text(core.project)'




### Enable the Network Connectivity API

Before you can perform _any_ tasks using Network Connectivity Center (NCC), you must enable the Network Connectivity API.

###  Console

To enable the Network Connectivity API:

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. Click **Enable**.




Alternatively, you can enable the API by using the [Google Cloud console API Library](https://console.cloud.google.com/apis/library?project=_), as described in [Enabling APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis).

### Get access

To work with NCC, you need the permissions described in [Roles and permissions](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/access-control).

### Identify resources

When you reference resources by using the gcloud CLI or the API, use the conventions described in the following table.

Convention | Supported for | Notes | Example  
---|---|---|---  
Full URI | All resources | Use one of these methods to reference Router appliance instances. | 
    
    
    "https://www.googleapis.com/compute/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME"
    
            
  
[Relative resource name](https://google.aip.dev/122) | All resources | 
    
    
    "projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME"
    
          
  
Name | Regional and global resources | Use this method for hubs, spokes, VPN tunnels, and VLAN attachments. | 
    
    
     "HUB_NAME"
    
          
  
#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.hubs.create` to create a hub
  * `networkconnectivity.hubs.delete` to delete a hub
  * `networkconnectivity.hubs.listSpokes` to list spokes
  * Additionally, if you are working in the Google Cloud console: 
    * `networkconnectivity.hubs.get`
    * `networkconnectivity.hubs.list`
    * `networkconnectivity.spokes.list`
    * `compute.projects.get`




**Roles**

  * [Hub & Spoke Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.hubAdmin)`
  * If you are working in the Google Cloud console, [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute) (`roles/compute.networkViewer`)



## Create a hub

To create a hub, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project.

  3. Click **Create hub**.

  4. Complete the **Basic configuration** section of the form:

     1. Enter a **Hub name**.
     2. Optional: Enter a **Description**.
     3. Choose the [preset topology type](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#preset-topologies).
     4. Optional: To add a label, click **Add Item** , and then enter a **Key** and **Value**.
     5. Verify that the form displays the correct **Project ID**. If the project ID is incorrect, select a different project by using the menu at the top of the page.
  5. In the **Private Service Connect connection propagation** section, enable or disable Private Service Connect connection propagation by clicking **On** or **Off**.

  6. Do one of the following:

     * If you want to create a spoke that is attached to this hub, click **Next step** and complete the spoke-creation section of the form. For instructions, see [Create a VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-vpc-spoke).
     * If you don't want to create a spoke right now, click **Create** to finish creating your new hub.



###  gcloud 

To create a hub, use the [`gcloud network-connectivity hubs create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/create).
    
    
      gcloud network-connectivity hubs create HUB_NAME \
          --policy-mode="POLICY_MODE" \
          --preset-topology="TOPOLOGY_TYPE" \
          --description="DESCRIPTION" \
          --labels="KEY"="VALUE"
    

If you want to enable Private Service Connect propagated connection globally for the NCC hub, use the `--export-psc` flag.
    
    
      gcloud network-connectivity hubs create HUB_NAME \
          --description="DESCRIPTION" \
          --labels="KEY"="VALUE" \
          --export-psc
    

Replace the following values:

  * `HUB_NAME`: the name of the new hub
  * `POLICY_MODE`: Optional: the policy mode to enable a preset topology, for example, `PRESET`
  * `TOPOLOGY_TYPE`: the preset topology type. The supported values are `STAR` or `MESH`. The default is `MESH`.
  * `DESCRIPTION`: optional text that describes the hub
  * `KEY`: the key in the key-value pair for the optional label text
  * `VALUE`: the value in the key-value pair for the optional label text



To enable Private Service Connect connection propagation on an existing hub, see [Update a hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#update_a_hub). If you want to disable the Private Service Connect connection propagation feature on existing hubs, use the `--no-export-psc` flag. Existing propagation connections are removed asynchronously.

###  API 

To create a hub, use the [`networkconnectivity.hubs.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs/create).
    
    
      POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs
      {
        "name":"HUB_NAME",
        "description":"DESCRIPTION",
        "labels": {
          "KEY": "VALUE"
        }
      }
    

To choose a preset topology, use the same method and specify the topology:
    
    
      POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs
      {
        "name":"HUB_NAME",
        "description":"DESCRIPTION",
        "preset_topology": "TOPOLOGY_TYPE"
      }
    

If you want to enable Private Service Connect propagated connection globally for the NCC hub, set the `export-psc` value to "true".
    
    
      POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs
      {
        "export_psc": true
      }
    

Replace the following values:

  * `PROJECT_ID`: the project ID of the project that contains the new hub
  * `HUB_NAME`: the name of the new hub
  * `DESCRIPTION`: optional text that describes the hub
  * `KEY`: the key in the key-value pair for the optional label text
  * `VALUE`: the value in the key-value pair for the optional label text
  * `TOPOLOGY_TYPE`: the preset topology type. The supported values are `STAR` or `MESH`. The default is `MESH`.



To enable Private Service Connect connection propagation on an existing hub, see [Update a hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#update_a_hub). If you want to disable the Private Service Connect connection propagation feature on an existing hub, set the `export_psc` value to "false". Existing propagation connections are removed asynchronously.

For detailed information about additional hub commands, such as list, describe, and update, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).

## Manage _auto-accept_ projects for spoke groups

To update auto-accept projects for a spoke group, follow these steps.

###  Console 

  1. In the Google Cloud console, go to **Network Connectivity Center**.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select the project in which the hub resides.

  3. Click the hub name for which you want to update the auto-accept projects.

  4. On the **Hub details** page, under **Groups** , click **Edit** next to the group name. For mesh topology connectivity, there is a single **default** group. For star topology connectivity, the groups are **center** and **edge**.

  5. On the **Edit group** pane, perform one of these steps:

     * To add projects you want to auto-accept spokes from, click **Add project ID** and type the **Project ID**. To add more projects, click **Add project ID**.

     * To remove a project ID from the auto-accept list, click deleteDelete next to **Project ID**.

  6. Click **Save**.




###  gcloud 

To update a spoke group, use the [`gcloud network-connectivity hubs groups update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/groups/update).
    
    
    gcloud network-connectivity hubs groups update GROUP_NAME \
      --hub=HUB_NAME \
      --description=DESCRIPTION \
      --add-auto-accept-projects=PROJECT_NAME_1,PROJECT_NAME_2
    

Replace the following:

  * `GROUP_NAME`: the name of the group
  * `HUB_NAME`: the name of the hub
  * `DESCRIPTION`: optional text that describes the group
  * `PROJECT_NAME_1`, `PROJECT_NAME_2`: a comma-separated list of one or more project IDs or project numbers that you want to enable auto-accept for



To clear all projects from the auto-accept projects list, use the `--clear-auto-accept-projects` flag.
    
    
    gcloud network-connectivity hubs groups update GROUP_NAME \
      --hub=HUB_NAME \
      --description=DESCRIPTION \
      --clear-auto-accept-projects
    

Replace the following:

  * `GROUP_NAME`: the name of the group
  * `HUB_NAME`: the name of the hub
  * `DESCRIPTION`: optional text that describes the hub



To remove specific projects from the auto-accept projects list, use the `--remove-auto-accept-projects` flag.
    
    
    gcloud network-connectivity hubs groups update GROUP_NAME \
      --hub=HUB_NAME \
      --description=DESCRIPTION \
      --remove-auto-accept-projects=PROJECT_NAME_1,PROJECT_NAME_2
    

Replace the following:

  * `GROUP_NAME`: the name of the group
  * `HUB_NAME`: the name of the hub
  * `DESCRIPTION`: optional text that describes the hub
  * `PROJECT_NAME_1`, `PROJECT_NAME_2`: a comma-separated list of one or more project IDs or project numbers that you want to disable auto-accept for



###  API 

To update auto-accept projects for a spoke group, use the

[`networkconnectivity.hubs.groups.update` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs.groups/patch).
    
    
      PATCH https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs/HUB_NAME/groups/GROUP_NAME/updateMask=auto_accept.auto_accept_projects
      {
       "auto_accept": {
           "auto_accept_projects": ["PROJECT_NAME_1","PROJECT_NAME_2"],
        }
      }
    

Replace the following:

  * `PROJECT_ID`: the project ID in which you created the hub
  * `HUB_NAME`: the name of the hub
  * `GROUP_NAME`: the name of the group
  * `PROJECT_NAME_1`, `PROJECT_NAME_2`: a comma-separated list of one or more project IDs or project numbers that you want to add or remove auto-accept for



## Delete a hub

To delete a hub, follow these steps.

Before you can delete a hub, you must delete or reject all spokes attached to the hub. If the spoke is in a different project, you might not have permission to delete it. In that case, you must reject the spoke.

For steps to delete a spoke, see [Delete a spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#deleting-a-spoke).

###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project.

  3. Click the **Hubs** tab.

  4. In the hub list, select the hub that you want to delete.

  5. Click the **Spoke** tab. All the spokes that are attached to this hub are listed with their status.

  6. From the list of active spokes, [delete the active spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#deleting-a-spoke). If you don't have permissions to delete the spoke, [reject the spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-review-proposed-spokes#reject-a-spoke-proposal).

  7. Click delete**Delete hub**.

  8. In the confirmation dialog, do one of the following:

     * Click **Cancel** if you don't want to delete the hub.
     * Click **Delete** to delete the hub.



###  gcloud 

  1. To list all active spokes attached to the hub that you want to delete, use the [`gcloud network-connectivity hubs list-spokes` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/list-spokes).
         
         gcloud network-connectivity hubs list-spokes HUB_NAME \
             --filter="state:ACTIVE"
         

Replace `HUB_NAME` with the name of the hub that you want to delete.

  2. [Delete the active spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#deleting-a-spoke). If you don't have permissions to delete the spoke, [reject the spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-review-proposed-spokes#reject-a-spoke-proposal).

  3. To delete a hub, use the [`gcloud network-connectivity hubs delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/delete).
         
         gcloud network-connectivity hubs delete HUB_NAME
         

Replace `HUB_NAME` with the name of the hub.




###  API 

  1. To list all active spokes attached to the hub that you want to delete, use the [`networkconnectivity.hubs.listSpokes` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs/listSpokes).
         
         GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs/HUB_NAME:listSpokes
         

Replace the following values:

     * `PROJECT_ID`: the project ID of the project that contains the hub for which you want to list spokes
     * `HUB_NAME`: the name of the hub for which you want to list spokes
  2. [Delete the active spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#deleting-a-spoke). If you don't have permissions to delete the spoke, [reject the spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-review-proposed-spokes#reject-a-spoke-proposal).

  3. To delete the hub, use the [`networkconnectivity.hubs.delete` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs/delete).
         
         DELETE https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs/HUB_NAME
         

Replace the following values:

     * `PROJECT_ID`: the project ID of the project that contains the hub to delete
     * `HUB_NAME`: the name of the hub to delete



## What's next

  * To create hubs and spokes, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).
  * To view a list of partners whose solutions are integrated with NCC, see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).
  * To find solutions for common issues, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting).
  * To get details about API and Google Cloud CLI commands, see [APIs and reference](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
