---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes/
title: Work with hubs and spokes \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:57:35.957964+00:00
---

# Work with hubs and spokes  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Work with hubs and spokes Stay organized with collections  Save and categorize content based on your preferences. 

To manage network connectivity efficiently across your Google Cloud and hybrid environments, use Network Connectivity Center (NCC) hubs and spokes. NCC lets you connect multiple Virtual Private Cloud (VPC) networks and on-premises locations.

NCC integrates hybrid network connections by supporting Cloud Interconnect VLAN attachments, HA VPN tunnels, and Router appliance VMs. You can also integrate NCC Gateway spokes with third-party Security Service Edge (SSE) providers to secure hybrid workforce access to applications, manage cross-region traffic, and optimize regional deployments.

This page describes how to list, create, describe, delete, and update NCC hubs and spokes.

For an introduction to NCC, see the [Network Connectivity Center overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview).

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

Before you can perform _any_ tasks using NCC, you must enable the Network Connectivity API.

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
    
          
  
## Work with hubs

This section describes how to list, create, describe, and delete Network Connectivity Center hubs. You can also update a hub's labels or description.

### Create a hub

To use NCC, you must create at least one hub and one spoke. When you create the hub, you specify the hub topology. The topology can't be changed later.

When you create a hub, you can choose to do any of the following activities at the same time:

  * Create spokes and add the spokes to the hub. For information about the maximum number of spokes per project and per hub, see [Quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/quotas).
  * Apply labels to the hub. For more information about labels, see the [labels overview](https://docs.cloud.google.com/resource-manager/docs/labels-overview).

If you want to create a hub that uses the hybrid inspection topology to support NCC Gateway spokes, you must use either the Google Cloud CLI or the Cloud Router API instructions in this section. For more information about NCC Gateway, see the [NCC Gateway overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ncc-gateway-overview). 

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.hubs.create`
  * Additionally, if you are working in the Google Cloud console: 
    * `networkconnectivity.hubs.get`
    * `networkconnectivity.hubs.list`
    * `networkconnectivity.spokes.list`
    * `compute.projects.get`



**Roles**

  * [Hub & Spoke Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.hubAdmin`)
  * If you are working in the Google Cloud console, [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute) (`roles/compute.networkViewer`)



###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project.

  3. Click **Create hub**.

  4. Complete the **Basic configuration** section of the form:

     1. Enter a **Hub name**.
     2. Optional: Enter a **Description**.
     3. Optional: To add a label, click **Add Item** , and then enter a **Key** and **Value**.
     4. Verify that the form displays the correct **Project ID**. If the project ID is incorrect, select a different project by using the menu at the top of the page.
  5. To enable Private Service Connect connection propagation, in the **Private Service Connect connection propagation** field, click **On**.

  6. Do one of the following:

     * If you want to create a spoke, click **Next step** and complete the spoke-creation section of the form. For instructions, see one of the following sections: 
       * Create a VPC spoke
       * Create a producer VPC spoke
       * Create a Router appliance spoke
       * Create a VLAN attachment spoke
       * Create a VPN spoke
     * If you don't want to create a spoke right now, click **Create** to finish creating your new hub.



###  gcloud 

To create a hub, use the [`gcloud network-connectivity hubs create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/create).

To control Private Service Connect connection propagation through NCC, specify any of the following optional flags:

  * To enable propagation for published services and regional Google APIs, use the `--export-psc` flag. 
  * To enable propagation for global Google APIs ([Preview](https://cloud.google.com/products#product-launch-stages)), use the `--export-psc-global-google-apis` flag. 



For more information, see [Private Service Connect connection propagation through NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/psc-propagated-connection-overview).
    
    
      gcloud network-connectivity hubs create HUB_NAME \
          --project="PROJECT_ID" \
          --description="DESCRIPTION" \
          --labels="KEY"="VALUE" \
          --preset-topology="HUB_TOPOLOGY" \
          [--export-psc]
          
          [--export-psc-global-google-apis]
          
    

Replace the following values:

  * `HUB_NAME`: the name of the new hub
  * `PROJECT_ID`: the project ID of the project that contains the new hub
  * `DESCRIPTION`: an optional description of the hub
  * `KEY`: the key in the key-value pair for the optional label text
  * `HUB_TOPOLOGY`: the topology of the hub

Valid values are the following:

    * `mesh`
    * `star`
    * `hybrid-inspection`



###  API 

To create a hub, use the [`networkconnectivity.hubs.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs/create).

To control Private Service Connect connection propagation through NCC, configure the `exportPscConfig` object:

  * `exportPsc`: set to `true` to enable propagation for published services and regional Google APIs. 
  * `globalGoogleApis`: set to `true` to enable propagation for global Google APIs ([Preview](https://cloud.google.com/products#product-launch-stages)). 



For more information, see [Private Service Connect connection propagation through NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/psc-propagated-connection-overview).
    
    
      POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs
      {
        "name":"HUB_NAME",
        "description":"DESCRIPTION",
        "labels": {
          "KEY": "VALUE"
        },
        "presetTopology": "HUB_TOPOLOGY",
        "exportPsc": True|False
        
        "globalGoogleApis": True|False
        
      }
    

Replace the following values:

  * `PROJECT_ID`: the project ID of the project that contains the new hub
  * `HUB_NAME`: the name of the new hub
  * `DESCRIPTION`: an optional description of the hub
  * `KEY`: the key in the key-value pair for the optional label text
  * `VALUE`: the value in the key-value pair for the optional label text
  * `HUB_TOPOLOGY`: the topology of the hub

Valid values are the following:

    * `mesh`
    * `star`
    * `hybrid-inspection`



### List hubs

To list the hubs associated with a project, use the following guidance.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.hubs.list`
  * Additionally, if you are working in the Google Cloud console: 
    * `networkconnectivity.hubs.get`
    * `networkconnectivity.spokes.list`
    * `compute.projects.get`



**Roles**

  * One of the following: 
    * [Hub & Spoke Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.hubViewer`)
    * [Spoke Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.spokeAdmin`)
    * [Hub & Spoke Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.hubAdmin`)
  * If you are working in the Google Cloud console, [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute) (`roles/compute.networkViewer`)



###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project.

The page lists all hubs associated with the project, along with the following information about each hub:

     * The name of the hub
     * The description of the hub
     * Any labels that have been applied to the hub
     * The number of spokes associated with the hub
     * The types of spokes associated with the hub



###  gcloud 

To list the hubs associated with a project, use the [`gcloud network-connectivity hubs list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/list).
    
    
      gcloud network-connectivity hubs list
    

The command output includes the name and description of each hub.

###  API 

To list the hubs associated with a project, use the [`networkconnectivity.hubs.list` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs/list).
    
    
      GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs
    

Replace `PROJECT_ID` with the project ID of the project that contains the hubs to list.

For each hub, this method returns the following details:

  * The name of the hub
  * A timestamp that shows when the hub was created
  * A timestamp of the last update
  * Any labels applied to the hub
  * The description of the hub, if one exists
  * The unique ID of the hub
  * The state of the hub
  * A list of `routingVpcs`, which are VPC networks associated with the spokes for the hub



### Describe a hub

Use the following guidance to retrieve details about a project's hub.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.hubs.get`
  * Additionally, if you are working in the Google Cloud console: 
    * `networkconnectivity.hubs.list`
    * `networkconnectivity.spokes.list`
    * `compute.projects.get`



**Roles**

  * One of the following: 
    * [Hub & Spoke Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.hubViewer`)
    * [Spoke Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.spokeAdmin`)
    * [Hub & Spoke Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.hubAdmin`)
  * If you are working in the Google Cloud console, [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute) (`roles/compute.networkViewer`)



###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project to view information about that project's hub.

  3. To view details about the hub's spokes, click the **Spokes** tab.




###  gcloud 

To get detailed information about an existing hub, use the [`gcloud network-connectivity hubs describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/describe).
    
    
    gcloud network-connectivity hubs describe HUB_NAME
    

Replace `HUB_NAME` with the name of the hub.

Output from this command includes the following information:

  * The time the hub was created
  * The hub's description
  * Any labels applied to the hub
  * The VPC networks (`routingVpcs`) that are associated with this hub's spoke resources
  * The hub's unique identifier
  * The time the hub was last updated



If you want information about the spokes attached to a hub, see List spokes and Describe a spoke.

###  API 

To get detailed information about an existing hub, use the [`networkconnectivity.hubs.get` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs/get).
    
    
      GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs/HUB_NAME
    

Replace the following values:

  * `PROJECT_ID`: the project ID of the project that contains the hubs to describe
  * `HUB_NAME`: the name of the hub to describe



Output from this command includes the following information:

  * The time the hub was created
  * The hub's description
  * Any labels applied to the hub
  * The VPC networks (`routingVpcs`) that are associated with this hub's spoke resources
  * The hub's unique identifier
  * The time the hub was last updated



The output is similar to the following:
    
    
     {
       "name": "projects/myproject/locations/global/hubs/myhub",
       "createTime": "2021-08-29T23:40:25.844970812Z",
       "updateTime": "2021-08-30T04:20:36.738801209Z",
       "labels": {
         "environment": "test"
       },
       "description": "in review",
       "uniqueId": "d6d3e375-4224-4352-a3b6-776042419430",
       "state": "ACTIVE",
       "routingVpcs": [ {
         "uri": "https://www.googleapis.com/compute/v1/projects/myproject/global/networks/myvpcnetwork"
       } ]
     }
     

If you want information about the spokes attached to a hub, see List spokes and Describing a spoke.

### Update a hub

After a hub has been created, you can add or change any of the following:

  * Update the labels applied to the hub; for information about labels, see [Requirements for labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels#requirements)
  * Update the description of the hub
  * Enable or disable [Private Service Connect connection propagation](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/psc-propagated-connection-overview) on an existing hub. 
  * Enable or disable the propagation of Private Service Connect global Google API endpoints to other spokes in the hub by enabling the `--export-psc-global-google-apis` flag ([Preview](https://cloud.google.com/products#product-launch-stages)). 



#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.hubs.update`



**Roles**

  * [Hub & Spoke Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.hubAdmin`)



###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project.

  3. Click the name of the hub that you want to modify.

  4. On the **Hub details** page, click edit**Edit hub**.

  5. Update the hub description and labels.

  6. To enable **Private Service Connect connection propagation** , click **On**. To disable Private Service Connect connection propagation, click **Off**.

  7. Click **Save**.




###  gcloud 

To update a hub's description or add labels to a hub, use the [`gcloud network-connectivity hubs update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/update).
    
    
      gcloud network-connectivity hubs update HUB_NAME \
          --description="DESCRIPTION" \
          --update-labels="KEY"="VALUE"
    

To remove one or more labels, use the `--remove-labels` flag. To remove all labels, use the `--clear-labels` flag. For more information, see the [`gcloud network-connectivity hubs update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/update).

If you want to enable Private Service Connect propagated connection for published services and regional endpoints on an existing NCC hub, use the `--export-psc` flag.
    
    
      gcloud network-connectivity hubs update HUB_NAME \
          [--description="DESCRIPTION"] \
          --update-labels="KEY"="VALUE" \
          --export-psc
    

Replace the following values:

  * `HUB_NAME`: the name of the hub
  * `DESCRIPTION`: an optional description of the hub
  * `KEY`: the key in the key-value pair for the optional label text
  * `VALUE`: the value in the key-value pair for the optional label text



You can disable the Private Service Connect connection propagation feature on existing hubs by using the `--no-export-psc` flag. Existing propagation connections are removed asynchronously.

To enable VPC spokes to export global Google APIs through Private Service Connect endpoints for propagation to other spokes in the hub, use the `--export-psc-global-google-apis` flag. 
    
    
    <pre class="devsite-click-to-copy">
      gcloud beta network-connectivity hubs update <var>HUB_NAME</var> \
          [--description="<var>DESCRIPTION</var>"] \
          --export-psc-global-google-apis
    </pre>
    
    Replace the following values:
    
    * `HUB_NAME`: the name of the hub
    * `DESCRIPTION`: an optional description of the hub
    
    To disable VPC spokes to export global Google APIs
    through Private Service Connect endpoints for propagation
    to other spokes in the hub, use the `--no-export-psc-global-google-apis` flag.
    
    You can also use exclude export ranges to exclude
    Private Service Connect Google API endpoints
    from propagation by adding their `/32` IP address to the exclude filter.
    

###  API 

To update a hub's description or add labels to a hub, use the [`networkconnectivity.hubs.patch` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs/patch).
    
    
      PATCH https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs/HUB_NAME
      {
        "description": "DESCRIPTION",
        "labels": {
          "KEY": "VALUE"
        }
      }
    

To enable Private Service Connect propagated connection for published services and regional endpoints on an existing NCC hub, set the `export-psc` value to `true`.

To enable VPC spokes to export global Google APIs through Private Service Connect endpoints for propagation to other spokes in the hub, set the `globalGoogleApis` value to `true` global Google APIs ([Preview](https://cloud.google.com/products#product-launch-stages)).
    
    
    PATCH https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs/HUB_NAME
    {
     "export_psc": true
     "globalGoogleApis": true
    }
    

Replace the following values:

  * `PROJECT_ID`: the ID of the project that contains the hub
  * `HUB_NAME`: the name of the hub
  * `DESCRIPTION`: an optional description of the hub
  * `KEY`: the key in the key-value pair for the optional label text
  * `VALUE`: the value in the key-value pair for the optional label text



You can disable the Private Service Connect connection propagation feature on an existing hub by setting the `export_psc` value to `false`. Existing propagation connections are removed asynchronously.

### Delete a hub

Before you can delete a hub, you must delete its spokes, as described in Delete a spoke.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.hubs.delete`
  * Additionally, if you are working in the Google Cloud console: 
    * `networkconnectivity.hubs.get`
    * `networkconnectivity.hubs.list`
    * `networkconnectivity.spokes.list`
    * `compute.projects.get`



**Roles**

  * [Hub & Spoke Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.hubAdmin`)
  * If you are working in the Google Cloud console, [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute) (`roles/compute.networkViewer`)



###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project.

  3. Click delete**Delete hub**.

  4. In the confirmation dialog, do one of the following:

     * Click **Cancel** if you don't want to delete the hub.
     * Click **Delete** to delete the hub.



###  gcloud 

To delete a hub, use the [`gcloud network-connectivity hubs delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/delete).
    
    
      gcloud network-connectivity hubs delete HUB_NAME
    

Replace `HUB_NAME` with the name of the hub.

###  API 

To delete a hub, use the [`networkconnectivity.hubs.delete` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs/delete).
    
    
      DELETE https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs/HUB_NAME
    

Replace the following values:

  * `PROJECT_ID`: the project ID of the project that contains the hub to delete
  * `HUB_NAME`: the name of the hub to delete



## Work with spokes

This section describes how to list, create, describe, delete, and update NCC spokes.

### Spoke guidelines

When you create a spoke, you specify the type of Google Cloud network resource that you plan to associate with the spoke.

  * For a list of supported resource types, see the [Spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#supported-spoke-resources) section of the NCC overview.
  * For the number of resources that you can associate with a spoke, see the [Quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/quotas) page.



For hybrid spokes, we recommend creating spokes in the region closest to the site that the spoke connects to. A site could be an on-premises data center, a branch office, or another cloud provider. VPC spokes are global.

#### Requirements

You must create each spoke in the same Google Cloud region as the Network Connectivity resource that you want to associate with the spoke. For example, suppose you have a VPN tunnel that uses an HA VPN gateway in `us-central1`. If you want to create a spoke that uses this tunnel, you must create the spoke in `us-central1`.

#### Limitations

After you create a spoke, many of its attributes can't be changed. If you want to modify an attribute that can't be changed, you must delete the spoke and re-create it.

For example, the following attributes can't be changed:

  * The value of the site-to-site data transfer field.

  * The HA VPN tunnels or VLAN attachments associated with the spoke.

  * The VPC network associated with the spoke's backing resources. This limitation is relevant only to Router appliance spokes, because they have modifiable resources.


* The consumer VPC spoke and peering connection name of a producer VPC spoke. 
  * The configuration that determines which subnet ranges to include or exclude from export for a VPC spoke.



For a list of spoke attributes that _can_ be changed after the spoke is created, see Update a spoke.

#### Recommendations for attaching multiple resources to a spoke

When creating a spoke, you can add more than one resource, but all resources must be of the same type. For example, you can add multiple HA VPN tunnels, but you can't add HA VPN tunnels and VLAN attachments.

Also, for VLAN attachments and VPN tunnels, the following restriction exists: although a spoke can be associated with multiple resources, each resource can be associated with only one spoke. In contrast, a router appliance instance can be associated with multiple spokes if it has interfaces in multiple VPC networks, and if the site-to-site data transfer field is set to false. However, each interface can be associated with only one spoke.

Additionally, see the resource-specific recommendations described in the sections Create a Router appliance spoke, Create a VLAN attachment spoke, Create a VPN spoke, and Create a VPC spoke.

#### ASN spoke assignment (hybrid spokes only)

For hybrid spokes, you must assign ASNs as described in [ASN requirements](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview#asns).

#### Validate spoke resources

Before you create a spoke, the corresponding resource must be configured correctly. For more information, see the resource-specific recommendations described in the sections Create an NCC Gateway spoke, Create a VPC spoke, Create a producer VPC spoke, Create a Router appliance spoke, Create a VLAN attachment spoke, and Create a VPN spoke.

### Create an NCC Gateway spoke

###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project in which you want to create the spoke.

  3. Click the **Spokes** tab.

  4. Click **Add spokes**.

  5. In the **Select hub** section, select the hub location as follows:

     * To attach the new spoke to a hub in the same project, select **In project` PROJECT_NAME`** and select the hub name from the list.
     * Choose a **Topology** :
     * For a greenfield deployment of NCC Gateway, choose **Hybrid inspection topology**
     * For a [brownfield deployment](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/add-vlan-to-ncc-gw-spoke), you can use the existing **Star** or **Mesh** topology.
  6. Enter a **Spoke name** and optionally, a **Description**.

  7. Select **NCC Gateway** as the **Spoke type**.

If you're using hybrid inspection topology, an NCC Gateway spoke can only be in the gateways group. For detailed information about spoke groups, see [Spoke groups](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#spoke-groups).

  8. Choose the **Region** that you want the gateway spoke to be deployed in.

  9. Choose the **Aggregated capacity** of the gateway spoke, in Gbps.

Supported capacity values are 1, 10, or 100.

  10. In the **Reserved IP range** field, enter a block of IP address ranges used to allocate supporting infrastructure for this gateway—for example, `10.1.2.0/23`.

The IP address block must be a `/23` range. This IP address block must not overlap with subnets in any spoke or peer network that the gateway can communicate with.

IP address ranges can't be within the `100.64.0.0/10` block as it is a space reserved for use by the internet service provider (ISP) infrastructure.

You can't change assigned IP address ranges. Some IP address ranges are reserved for SSE partners.

**Note:** When deploying multiple NCC Gateway in different regions on the same hub, you must ensure that the reserved IP range is unique for each regional gateway instance.
  11. Optional: to add routes advertised from NCC Gateway to the hub, in the **Routes advertised from NCC Gateway to hub** section, do the following:

     * Enter the **Route name**.
     * Enter an **IP range** for the route.
     * Enter the **Priority** for the route.

To add additional routes, click **Add route** and repeat the process starting with entering a **Route name**.

  12. Click **Done**.

  13. If you want to add more spokes, click **Add spoke** and begin the process again, starting with entering a **Spoke name**.

  14. When you have finished adding spokes, click **Create**. The NCC page updates to show details about the spokes that you created.




After the spoke is created, you can associate the spoke with a Cloud Router. To do so, click the spoke that you just created. On the **Spoke details** page, click **Add Cloud Router**. Then, follow the instructions to [Create a Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/add-vlan-attachments#create-cloud-router).

You can also attach it to Secure Access Connect by clicking **Secure Access Connect attachments** and following the instructions to [Create a Secure Access Connect attachment](https://docs.cloud.google.com/secure-access-connect/docs/create-attachments).

###  gcloud 

Use the [`gcloud network-connectivity spokes gateways create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/gateways/create):
    
    
    gcloud network-connectivity spokes gateways create SPOKE_NAME \
        --region=REGION \
        --hub=HUB \
        --capacity=CAPACITY \
        --ip-range-reservations=IP_RANGE \
        --group=SPOKE_GROUP
    

Replace the following values:

  * `SPOKE_NAME`: the name of the spoke
  * `REGION`: the region that you want theNCC Gateway to be deployed in
  * `HUB`: the name of the hub for the spoke
  * `CAPACITY`: the capacity of the gateway spoke, in Gbps

Supported capacity values are 1, 10, or 100.

  * `IP_RANGE`: a block of IP address ranges used to allocate supporting infrastructure for this gateway—for example, `10.1.2.0/23`

The IP address block must be a /23 range. This IP address block must not overlap with subnets in any spoke or peer network that the gateway can communicate with.

IP address ranges can't be within the `100.64.0.0/10` block as it is a space reserved for use by the internet service provider (ISP) infrastructure.

You can't change assigned IP address ranges. Some IP address ranges are reserved for SSE partners.

**Note:** When deploying multiple NCC Gateway in different regions on the same hub, you must ensure that the reserved IP range is unique for each regional gateway instance.
  * `SPOKE_GROUP`: the spoke group for your spoke. This can vary based on the topology that you're using for your hub.

    * For a greenfield deployment of NCC Gateway, use hybrid inspection topology
    * For a [brownfield deployment](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/add-vlan-to-ncc-gw-spoke), you can use the existing Star or Mesh topology. For details, about connectivity topologies, see [Connectivity topologies](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies).



###  API 

To create an NCC Gateway spoke, use the [`projects.locations.spokes.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/create).
    
    
      POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/spokes/SPOKE_NAME
      {
        "hub":"HUB_NAME",
        "location" : LOCATION,
        "gateway": {
           "ip_range_reservation": IP_RANGE,
           "capacity": CAPACITY
           "group": SPOKE_GROUP
        },
      }
    

Replace the following values:

  * `PROJECT_ID`: the project ID of the project that contains the new spoke
  * `SPOKE_NAME`: the name of the spoke
  * `HUB_NAME`: the name of the hub that you are attaching the spoke to
  * `LOCATION`: the region that you want the NCC Gateway to be deployed in
  * `IP_RANGE`: a block of IP address ranges used to allocate supporting infrastructure for this gateway—for example, `10.1.2.0/23`

The IP address block must be a /23 range. This IP address block must not overlap with subnets in any spoke or peer network that the gateway can communicate with.

IP address ranges can't be within the `100.64.0.0/10` block as it is a space reserved for use by the internet service provider (ISP) infrastructure.

You can't change assigned IP address ranges. Some IP address ranges are reserved for SSE partners.

**Note:** When deploying multiple NCC Gateway in different regions on the same hub, you must ensure that the reserved IP range is unique for each regional gateway instance.
  * `CAPACITY`: the capacity of the gateway spoke, in Gbps

Supported capacity values are 1, 10, or 100.

  * `SPOKE_GROUP`: the spoke group for your spoke. This group can vary based on the topology that you're using for your hub. For details, see [Connectivity topologies](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies).




### Create a VPC spoke

Before creating VPC attachment spokes, consider the following guidelines:

  * VPC spokes are global because VPC networks are global.
  * There must be no subnet overlaps across VPC spokes. You can avoid this by using the `exclude export ranges` and the `include export ranges` flags. For detailed information about using filters for VPC network connectivity, see [VPC connectivity with export filters](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#vpc-connectivity-with-export-filters).
  * There can't be a subnet overlap between NCC VPC connectivity and VPC peering.
  * VPC spokes, where the hub and the VPC spoke are in different projects, have a different workflow. For more information, see [VPC spokes in a different project from a hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#vpc-spokes-different-project).
  * VPC spokes attached to a hub that supports star topology must be explicitly assigned to a [spoke group](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#limitations-of-route-exchange).
  * If you want to create a Private Service Connect connection in the VPC spoke, the hub must have Private Service Connect connection propagation enabled. For instructions about how to create a Private Service Connect endpoint, see [Create an endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint).



#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `compute.networks.use` on the VPC network being added to a spoke
  * `networkconnectivity.groups.use` on the hub that the spoke is being associated with
  * `networkconnectivity.spokes.create` in the project where the VPC network lives
  * `networkconnectivity.groups.create` on the hub to create a group
  * `networkconnectivity.groups.use` on the hub to create spokes associated with a group in a different project from the hub



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`) on the VPC network being added to a spoke
  * Group User (`roles/networkconnectivity.groupUser`) on the hub that the spoke is being associated with
  * Spoke Admin (`roles/networkconnectivity.spokeAdmin`) in the project where the VPC network lives



To connect multiple VPC networks within a given project, connect a VPC network to a spoke, and connect it to a hub.

If you are creating a VPC to connect to a hub that is configured for star topology, you must get the project ID, the hub name or URI, and the group name from the hub administrator.

If you want to assign [exclude export ranges](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#exclude-export-ranges) or [include export ranges](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#include-export-ranges), use the appropriate options during spoke creation.

To create a VPC spoke, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project in which you want to create the spoke.

  3. Click the **Spokes** tab.

  4. Click **Add spokes**.

  5. In the **Select hub** section, select the hub location as follows:

     * To attach the new spoke to a hub in the same project, select **In project` PROJECT_NAME`** and select the hub name from the list.
     * If you want to attach the new spoke to a hub in another project, select **In another project**. Enter the **Project ID** and the **Hub name** to which you want to attach your new spoke.

When you choose a hub in a different project, your spoke becomes active only when the hub administrator reviews and accepts your proposed spoke. For more details about creating spokes attached to a hub in a different project, see [VPC spokes overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview). If you are creating a VPC spoke in the same project as the hub, it is automatically accepted and activated.

  6. Enter a **Spoke name** and optionally, a **Description**.

  7. Based on the topology of the hub that you are connecting to, choose the **Spoke group** for your spoke. You can choose from the following values:

     * **Default** for a mesh topology hub
     * **Center** or **Edge** for a star topology hub. This field is required for spoke groups that use star topology
     * **Prod** , **Non-prod** , or **Services** for a hub that uses the hybrid inspection topology (only for NCC Gateway spokes)

For detailed information about spoke groups, see [Spoke groups](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#spoke-groups).

  8. Select **VPC network** as the **Spoke type**.

  9. To add a VPC network to the spoke, select one from the **Associated VPC network** list.

  10. Optional: add a **VPC spoke filter** to customize how routes are advertised by specifying IP address ranges to [exclude or include export](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#vpc-connectivity-with-export-filters) from the spoke to the hub. You can configure the spoke to export only subnet ranges that use private IPv4 addresses, only IPv6 subnet ranges (internal and external), or both subnet ranges that use private IPv4 addresses and internal and external IPv6 subnet ranges.

     1. **IPv4 ranges** : configure the export of IPv4 subnet ranges.

        * **Include export IPv4 subnet ranges from spoke to hub** : by default, this checkbox is selected and all subnet ranges that use private IPv4 addresses are exported.

If you don't want to export IPv4 subnet ranges, clear this checkbox.

If you only want to export specific IPv4 subnet ranges, select **Specify IPv4 ranges** and enter the address ranges that you want to export. The IPv4 subnet ranges that you specify must be private IPv4 address ranges, excluding privately used public IPv4 addresses. For more information, see [Valid IPv4 ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges).

        * **Exclude export IPv4 subnet ranges from spoke to hub** : if the spoke exports subnet ranges and you want to exclude specific ranges from export, enter those ranges in this field.

     2. **IPv6 ranges** : configure the export of IPv6 subnet ranges (internal and external).

        * **Include export all IPv6 subnet ranges from spoke to hub** : to export all IPv6 subnet ranges to the hub, select the checkbox.

If you only want to export specific IPv6 subnet ranges, select **Specify IPv6 ranges** and enter the address ranges that you want to export.

        * **Exclude export IPv6 subnet ranges from spoke to hub** : if the spoke exports subnet ranges and you want to exclude specific ranges from export, enter those ranges in this field.

  11. Click **Done**.

  12. If you want to add more spokes, click **Add spoke** and begin the process again, starting with entering a **Spoke name**.

  13. When you have finished adding spokes, click **Create**. The NCC page updates to show details about the spokes that you created.




###  gcloud 

To create a VPC spoke, use the [`gcloud network-connectivity spokes linked-vpc-network create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-vpc-network/create).
    
    
    gcloud network-connectivity spokes linked-vpc-network create SPOKE_NAME \
        --hub=HUB \
        --description=DESCRIPTION \
        --vpc-network=VPC_URI \
        --include-export-ranges=[INCLUDE_EXPORT_RANGES] \
        --exclude-export-ranges=[EXCLUDE_EXPORT_RANGES] \
        --global \
        --group=GROUP_NAME
    

Replace the following:

  * `SPOKE_NAME`: the name of the spoke that you are creating, such as `vpc-spoke1`
  * `HUB`: the hub for the spoke
  * `DESCRIPTION`: an optional description of the spoke
  * `VPC_URI`: the VPC network that this spoke points to
  * `INCLUDE_EXPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which subnet IP address ranges can be exported to the hub.

    * The `ALL_PRIVATE_IPV4_RANGES` keyword adds all subnet ranges that use [private IPv4 addresses](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) to the include export range list.

    * The `ALL_IPV4_RANGES` keyword includes all IPv4 addresses, equivalent to the `0.0.0.0/0` CIDR. All [valid IPv4 ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) for subnet ranges, including privately used public IPv4 address ranges, are included. You can refine the list by using the `--exclude-export-ranges` flag.

    * The `ALL_IPV6_RANGES` keyword includes all IPv6 addresses, equivalent to the `::/0` CIDR.

    * The include export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the include export ranges can match or contain another CIDR.

    * If you omit `--include-export-ranges` for a VPC spoke, the default include export ranges is the same as if you had specified `ALL_PRIVATE_IPV4_RANGES`.

    * Subnet ranges in the VPC spoke, its include export ranges, and its exclude export ranges must follow the [Export filter rules for VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-vpc-spokes).

  * `EXCLUDE_EXPORT_RANGES`: a comma-delimited list of IP address ranges that define which subnet IP address ranges are never exported to the hub.

    * The exclude export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the exclude export ranges can match or contain another CIDR.

    * Every CIDR specified in the exclude export ranges must expand to IP addresses that are fully contained by CIDRs or keywords in the include export ranges (or the default include export ranges, if you don't specify any include export ranges explicitly).

    * Exclude export ranges don't support keywords.

    * If you omit `--exclude-export-ranges`, NCC uses an empty list as the default exclude export ranges.

    * Subnet ranges in the VPC spoke, its include export ranges, and its exclude export ranges must follow the [Export filter rules for VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-vpc-spokes).

  * `GROUP_NAME`: the group that this spoke belongs to. Supported values are:

    * `Default` for a mesh topology hub
    * `Center` or `edge` for a star topology hub. This field is required for spoke groups that use star topology
    * `Prod`, `non-prod`, or `services` for a hub that uses the hybrid inspection topology (only for NCC Gateway spokes)

For detailed information about spoke groups, see [Spoke groups](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#spoke-groups).




###  API 

To create a VPC spoke, use the [`projects.locations.spokes.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/create).
    
    
      POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/spokes/SPOKE_NAME
      {
        "hub":"HUB_NAME",
        "linkedVpcNetwork": {
           "uri": VPC_URI,
           "include_export_ranges": "[INCLUDE_EXPORT_RANGES]",
           "exclude_export_ranges": "[EXCLUDE_EXPORT_RANGES]",
           "group": "GROUP_NAME"
        },
      }
    

Replace the following values:

  * `PROJECT_ID`: the project ID of the project that contains the new spoke.
  * `SPOKE_NAME`: the name of the new spoke.
  * `HUB_NAME`: the name of the hub that you are attaching the spoke to.
  * `VPC_URI`: The VPC network that this spoke points to, such as `vpc_uri`.
  * `INCLUDE_EXPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which subnet IP address ranges can be exported to the hub.

    * The `ALL_PRIVATE_IPV4_RANGES` keyword adds all subnet ranges that use [private IPv4 addresses](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) to the include export range list.

    * The `ALL_IPV4_RANGES` keyword includes all IPv4 addresses, equivalent to the `0.0.0.0/0` CIDR. All [valid IPv4 ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) for subnet ranges, including privately used public IPv4 address ranges, are included. You can refine the list by using the `--exclude-export-ranges` flag.

    * The `ALL_IPV6_RANGES` keyword includes all IPv6 addresses, equivalent to the `::/0` CIDR.

    * The include export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the include export ranges can match or contain another CIDR.

    * If you omit `include_export_ranges` for a VPC spoke, the default include export ranges is the same as if you had specified `ALL_PRIVATE_IPV4_RANGES`.

    * Subnet ranges in the VPC spoke, its include export ranges, and its exclude export ranges must follow the [Export filter rules for VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-vpc-spokes).

  * `EXCLUDE_EXPORT_RANGES`: a comma-delimited list of IP address ranges that define which subnet IP address ranges are never exported to the hub.

    * The exclude export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the exclude export ranges can match or contain another CIDR.

    * Every CIDR specified in the exclude export ranges must expand to IP addresses that are fully contained by CIDRs or keywords in the include export ranges (or the default include export ranges, if you don't specify any include export ranges explicitly).

    * Exclude export ranges don't support keywords.

    * If you omit `exclude_export_ranges`, NCC uses an empty list as the default exclude export ranges.

    * Subnet ranges in the VPC spoke, its include export ranges, and its exclude export ranges must follow the [Export filter rules for VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-vpc-spokes).

  * `GROUP_NAME`: the group that this spoke belongs to. Supported values are:

    * `Default` for a mesh topology hub
    * `Center` or `edge` for a star topology hub. This field is required for spoke groups that use star topology
    * `Prod`, `non-prod`, or `services` for a hub that uses the hybrid inspection topology (only for NCC Gateway spokes)

For detailed information about spoke groups, see [Spoke groups](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#spoke-groups).




### Create a producer VPC spoke

Before you create a producer VPC spoke:

  * Review the [considerations](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-overview#considerations) for producer VPC spokes.
  * Review the guidelines for creating VPC spokes, which also apply to producer VPC spokes.



#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.spokes.use` on the peered consumer VPC spoke
  * `networkconnectivity.groups.use` on the hub that the spoke is being associated with
  * `networkconnectivity.spokes.create` in the project where the peered consumer VPC network lives
  * `networkconnectivity.groups.create` on the hub to create a group
  * `networkconnectivity.groups.use` on the hub to create spokes associated with a group in a different project from the hub



**Roles**

  * Compute Network Admin role (`roles/compute.networkAdmin`) on the peered consumer VPC network
  * Spoke Admin role (`roles/networkconnectivity.spokeAdmin`) in the project where the peered consumer VPC network lives



To connect a service producer VPC network with other networks in a given project, connect the producer VPC network to a producer VPC spoke, and connect the producer VPC spoke to a hub.

If you use the Google Cloud CLI or the API to connect the producer VPC spoke to a hub that is configured for star topology, you must use the same group name as the existing consumer VPC spoke on the hub. If you use the Google Cloud console, the producer VPC spoke is automatically added to the same group.

If you want to assign [exclude export ranges](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#exclude-export-ranges) or [include export ranges](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#include-export-ranges), use the appropriate options during spoke creation.

To create a producer VPC spoke, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project in which you want to create the spoke.

  3. Click the **Spokes** tab.

  4. Click **Add spokes**.

  5. In the **Select hub** section, select the hub location as follows:

     * To attach the new spoke to a hub in the same project, select **In project` PROJECT_NAME`** and select the hub name from the list.
     * If you want to attach the new spoke to a hub in another project, select **In another project**. Enter the **Project ID** and the **Hub name** to which you want to attach your new spoke.

When you choose a hub in a different project, your spoke becomes active only when the hub administrator reviews and accepts your proposed spoke. For more information about creating spokes attached to a hub in a different project, see [VPC spokes overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview). If you are creating a producer VPC spoke in the same project as the hub, the auto-accept list is still considered. By default, the auto-accept list already includes the same project, so the producer VPC spoke is automatically accepted and activated.

  6. Enter a **Spoke name** and optionally, a **Description**.

  7. Select **Producer VPC network** as the **Spoke type**.

  8. Enter the name of an existing **Consumer VPC spoke** on the hub that consumes services from the producer VPC network through a VPC Network Peering connection. Google Cloud identifies the producer network through the peering connection. You can choose from one of the following options:

     * For [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access), use `servicenetworking-googleapis-com`.
     * For [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview), use `sn-netapp-prod`.
  9. Optionally, you can add a VPC spoke filter to customize how routes are advertised by entering an IP address range to [exclude or include export](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#vpc-connectivity-with-export-filters) from the spoke to hub. You can change this filter after the spoke is created.

  10. Click **Done**.

  11. If you want to add more spokes, click **Add spoke** and begin the process again, starting with entering a spoke name.

  12. When you have finished adding spokes, click **Create**. The NCC page updates to show details about the spokes that you created.




###  gcloud 

To create a producer VPC spoke, use the [`gcloud network-connectivity spokes linked-producer-vpc-network create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/create).
    
    
    gcloud network-connectivity spokes linked-producer-vpc-network create SPOKE_NAME \
        --hub=HUB \
        --description=DESCRIPTION \
        --network=CONSUMER_VPC_URI \
        --peering=PEERING_NAME \
        --include-export-ranges=[INCLUDE_EXPORT_RANGES] \
        --exclude-export-ranges=[EXCLUDE_EXPORT_RANGES] \
        --global \
        --group=GROUP_NAME
    

Replace the following:

  * `SPOKE_NAME`: the name of the spoke that you are creating, such as `producer-vpc-spoke1`
  * `HUB`: the hub for the spoke
  * `DESCRIPTION`: optional text to describe the spoke
  * `CONSUMER_VPC_URI`: the VPC network that consumes services from the producer network through a VPC Network Peering connection

Google Cloud identifies the producer VPC network through the peering connection. The consumer network that you enter must also be a spoke in the hub. You can enter the full or relative URI. The following example shows the relative URI: `projects/PROJECT_ID/global/networks/NETWORK_NAME`.

  * `PEERING_NAME`: the name of the peering between the your VPC network and the producer VPC spoke. The producer VPC spoke must be in the same project as your VPC network and must be in the `ACTIVE` state. Set the `--peering` flag to one of the following:

    * For [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access), use `servicenetworking-googleapis-com`.
    * For [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview), use `sn-netapp-prod`.
  * `INCLUDE_EXPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which subnet IP address ranges can be exported to the hub.

    * The `ALL_PRIVATE_IPV4_RANGES` keyword adds all subnet ranges that use [private IPv4 addresses](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) to the include export range list.

    * The `ALL_IPV4_RANGES` keyword includes all IPv4 addresses, equivalent to the `0.0.0.0/0` CIDR. All [valid IPv4 ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) for subnet ranges, including privately used public IPv4 address ranges, are included. You can refine the list by using the `--exclude-export-ranges` flag.

    * The `ALL_IPV6_RANGES` keyword includes all IPv6 addresses, equivalent to the `::/0` CIDR.

    * The include export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the include export ranges can match or contain another CIDR.

    * If you omit `--include-export-ranges` for a VPC spoke, the default include export ranges is the same as if you had specified `ALL_PRIVATE_IPV4_RANGES`.

    * Subnet ranges in the VPC spoke, its include export ranges, and its exclude export ranges must follow the [Export filter rules for VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-vpc-spokes).

  * `EXCLUDE_EXPORT_RANGES`: a comma-delimited list of IP address ranges that define which subnet IP address ranges are never exported to the hub.

    * The exclude export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the exclude export ranges can match or contain another CIDR.

    * Every CIDR specified in the exclude export ranges must expand to IP addresses that are fully contained by CIDRs or keywords in the include export ranges (or the default include export ranges, if you don't specify any include export ranges explicitly).

    * Exclude export ranges don't support keywords.

    * If you omit `--exclude-export-ranges`, NCC uses an empty list as the default exclude export ranges.

    * Subnet ranges in the VPC spoke, its include export ranges, and its exclude export ranges must follow the [Export filter rules for VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-vpc-spokes).

  * `GROUP_NAME`: the group this spoke belongs to—for example, `center` or `edge`. This field is required for spoke groups that use star topology. For detailed information about spoke groups, see [Spoke groups](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#spoke-groups).




###  API 

To create a producer VPC spoke, use the [`networkconnectivity.spokes.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/create).
    
    
      POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/spokes/SPOKE_NAME
      {
        "hub":"HUB_NAME",
        "linkedProducerVpcNetwork": {
           "network": "CONSUMER_VPC_URI",
           "peering_name": "PEERING_NAME",
           "include_export_ranges": "[INCLUDE_EXPORT_RANGES]",
           "exclude_export_ranges": "[EXCLUDE_EXPORT_RANGES]",
           "group": "GROUP_NAME"
        },
      }
    

Replace the following:

  * `PROJECT_ID`: the project ID of the project that contains the new spoke
  * `HUB_NAME`: the name of the hub that you are attaching the spoke to
  * `SPOKE_NAME`: the name of the spoke that you are creating
  * `CONSUMER_VPC_URI`: the VPC network that consumes services from the producer through a VPC Network Peering connection

Google Cloud identifies the producer VPC network through the peering connection. The consumer network that you enter must also be a spoke in the hub. You can enter the full or relative URI. The following example shows the relative URI: `projects/PROJECT_ID/global/networks/NETWORK_NAME`.

  * `PEERING_NAME`: the name of the peering between the your VPC network and the producer VPC spoke. The producer VPC spoke must be in the same project as your VPC network and must be in the `ACTIVE` state. Set the `--peering` flag to one of the following:

    * For [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access), use `servicenetworking-googleapis-com`.
    * For [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview), use `sn-netapp-prod`.
  * `INCLUDE_EXPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which subnet IP address ranges can be exported to the hub.

    * The `ALL_PRIVATE_IPV4_RANGES` keyword adds all subnet ranges that use [private IPv4 addresses](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) to the include export range list.

    * The `ALL_IPV4_RANGES` keyword includes all IPv4 addresses, equivalent to the `0.0.0.0/0` CIDR. All [valid IPv4 ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) for subnet ranges, including privately used public IPv4 address ranges, are included. You can refine the list by using the `--exclude-export-ranges` flag.

    * The `ALL_IPV6_RANGES` keyword includes all IPv6 addresses, equivalent to the `::/0` CIDR.

    * The include export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the include export ranges can match or contain another CIDR.

    * If you omit `--include-export-ranges` for a VPC spoke, the default include export ranges is the same as if you had specified `ALL_PRIVATE_IPV4_RANGES`.

    * Subnet ranges in the VPC spoke, its include export ranges, and its exclude export ranges must follow the [Export filter rules for VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-vpc-spokes).

  * `EXCLUDE_EXPORT_RANGES`: a comma-delimited list of IP address ranges that define which subnet IP address ranges are never exported to the hub.

    * The exclude export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the exclude export ranges can match or contain another CIDR.

    * Every CIDR specified in the exclude export ranges must expand to IP addresses that are fully contained by CIDRs or keywords in the include export ranges (or the default include export ranges, if you don't specify any include export ranges explicitly).

    * Exclude export ranges don't support keywords.

    * If you omit `--exclude-export-ranges`, NCC uses an empty list as the default exclude export ranges.

    * Subnet ranges in the VPC spoke, its include export ranges, and its exclude export ranges must follow the [Export filter rules for VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-vpc-spokes).

  * `GROUP_NAME`: the group this spoke belongs to—for example, `center` or `edge`. This field is required for spoke groups that use star topology. For detailed information about spoke groups, see [Spoke groups](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#spoke-groups). 




### Create a Router appliance spoke

If you are using a Router appliance spoke to connect to sites outside of Google Cloud, use the following guidance:

  * Unlike VLAN attachments and VPN spokes, a Router appliance spoke doesn't have to be associated with a single location outside of Google Cloud. However, because router appliance instances are regional resources, we recommend that you configure them to receive data from nearby locations.

  * If you configure multiple router appliance instances to receive data from the same set of sites, we recommend that you associate those instances with the same spoke.




If you are using a Router appliance spoke for site-to-site data transfer, use the following guidance:

  * If you link multiple router appliance instances to a spoke, be aware that NCC doesn't provide site-to-site data transfer between those instances. To use site-to-site data transfer, you must set up multiple spokes. In response, NCC permits data transfer between those spokes.



After you create a Router appliance spoke, you must set up BGP peering between the router appliance instance and a Cloud Router located in the same region. For details, see [Create router appliance instances](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/creating-router-appliances).

For information about configuring the resources that are required to create a Router appliance spoke, see the following documentation:

  * [Create router appliance instances](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/creating-router-appliances)
  * [Router appliance overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview)
  * [Cloud Router documentation](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [Compute Engine (VM) documentation](https://docs.cloud.google.com/compute/docs)



#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.spokes.create`
  * `compute.routers.get`
  * `compute.instances.get`
  * If you are working in the Google Cloud console, you need permission to view certain network resources. For details, see [Roles and permissions](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/access-control#permission-console). 



**Roles**

  * One of the following: 
    * [Spoke Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.spokeAdmin`)
    * [Hub & Spoke Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.hubAdmin`)
  * A role—such as [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute) (`roles/compute.networkViewer)`—that grants you permission to read Cloud Router resources and your spoke's resource type (in this case, VMs)
  * If you are working in the Google Cloud console, [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute) (`roles/compute.networkViewer`)



###  Console 

**Enter basic spoke details**

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.
[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)
  2. In the project menu, select a Google Cloud project.
  3. Click the **Spokes** tab.
  4. Click **Add spokes**.
  5. In the **New spoke** form, set the **Spoke type**.
  6. Enter a **Spoke name** and optionally, a **Description**.
  7. Select the **Region** field for the new spoke.
  8. Under **Site-to-site data transfer** , select **On** or **Off**. If the region you selected does not support data transfer, the field is disabled. For more information about this use case, see [Site-to-site data transfer overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer).
  9. In the **VPC network** list, select a network. If you have more than one spoke that uses the data transfer feature, all of these spokes must be in the same VPC network. So if you have already created a spoke that uses data transfer, the **VPC network** value is prepopulated and cannot be changed.



**Enter router appliance details**

  1. Choose a router appliance instance:
     1. Click **Add instance**.
     2. From the **Instances** drop-down menu, select an existing router appliance instance. 
  2. Optional: To propagate subnets that are advertised to the hub to hybrid spokes, under **Hybrid spoke filter** , click **Include all IPv4 ranges from hub to spoke**. 
  3. To add more router appliance instances to this spoke, repeat the preceding step. When you have finished, click **Done** and continue to **Save your spoke**.



**Save your spoke**

  1. If you want to add more spokes, click **Add spoke** and begin the process again, starting with entering a **Spoke name**.
  2. When you are finished adding spokes, click **Create**. The **NCC** page updates to show details about the spokes that you created.



###  gcloud 

To create a Router appliance spoke, use the [`gcloud network-connectivity spokes linked-router-appliances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-router-appliances/create).

For example, to create a spoke that has two router appliance instances and uses site-to-site data transfer, run the following command.

To enable import of subnet IP address ranges to this spoke, use the `--include-import-ranges` flag.

Use the `site-to-site-data-transfer` flag if you want to enable data transfer for the spoke. If you don't specify `site-to-site-data-transfer`, then `site-to-cloud-data-transfer` is configured by default. For more information about this use case, see [Site-to-site data transfer overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer).
    
    
      gcloud network-connectivity spokes linked-router-appliances create NAME \
          --hub=HUB_NAME \
          --description="DESCRIPTION" \
          --router-appliance=instance="ROUTER_APPLIANCE_URI",ip=IP_ADDRESS \
          --router-appliance=instance="ROUTER_APPLIANCE_URI_2",ip=IP_ADDRESS_2 \
          --region=REGION \
          --labels="KEY"="VALUE" \
          --include-export-ranges=[INCLUDE_EXPORT_RANGES,...] \
          --exclude-export-ranges=[EXCLUDE_EXPORT_RANGES,...] \
          --include-import-ranges=[INCLUDE_IMPORT_RANGES,...] \
          --exclude-import-ranges=[EXCLUDE_IMPORT_RANGES,...]
     

Replace the following values:

  * `NAME`: the name of the spoke
  * `HUB_NAME`: the name of the hub
  * `DESCRIPTION`: an optional description of the spoke
  * `ROUTER_APPLIANCE_URI`: the URI of the first router appliance instance—for example, 
        
        https://www.googleapis.com/compute/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME 

  * `IP_ADDRESS`: the internal IP address of the first router appliance instance
  * `ROUTER_APPLIANCE_URI_2`: the URI of the second router appliance instance
  * `IP_ADDRESS_2`: the internal IP address of the second router appliance instance
  * `REGION`: the Google Cloud region where the spoke is located—for example, `us-west1`
  * `KEY`: the key in the key-value pair for the optional label text
  * `VALUE`: the value in the key-value pair for the optional label text
  * `INCLUDE_EXPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which dynamic routes can be exported to the hub.

    * The `ALL_IPV4_RANGES` keyword includes all IPv4 addresses, equivalent to the `0.0.0.0/0` CIDR.

    * The include export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the include export ranges can match or contain another CIDR.

    * If you omit `--include-export-ranges` for a Router appliance spoke, the default include export ranges is the same as if you had specified `ALL_IPV4_RANGES`.

    * Dynamic routes in the Router appliance spoke, its include export ranges, and its exclude export ranges follow the [Export filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-hybrid-spokes).

  * `EXCLUDE_EXPORT_RANGES`: a comma-delimited list of IP address ranges that define which dynamic routes are never exported to the hub.

    * The exclude export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the exclude export ranges can match or contain another CIDR.

    * Every CIDR specified in the exclude export ranges must expand to IP addresses that are fully contained by CIDRs or keywords in the include export ranges (or the default include export ranges, if you don't specify any include export ranges explicitly).

    * Exclude export ranges don't support keywords.

    * If you omit the `--exclude-export-ranges`, NCC uses an empty list as the default exclude export ranges.

    * Dynamic routes in the Router appliance spoke, its include export ranges, and its exclude export ranges follow the [Export filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-hybrid-spokes).

  * `INCLUDE_IMPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which subnet routes or transit dynamic routes can be imported from the hub.

    * The `ALL_IPV4_RANGES` keyword includes all IPv4 addresses, equivalent to the `0.0.0.0/0` CIDR.

    * The include import ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the include import ranges can match or contain another CIDR.

    * If you omit `--include-import-ranges` for a Router appliance spoke, NCC uses the following defaults:

      * If the Router appliance spoke doesn't have site-to-site data transfer enabled, the default include import ranges is empty.

      * If the Router appliance spoke has site-to-site data transfer enabled, the default include import ranges contains only the IPv4 dynamic routes learned from the hub's other hybrid spokes that have site-to-site data transfer enabled (transit dynamic routes). This default include import ranges doesn't contain any subnet ranges from the hub.

      * Google recommends that you specify an explicit set of include import ranges since the default values vary and might only apply to importing dynamic routes.

    * Subnet routes and transit dynamic routes in the hub, the Router appliance spoke's include import ranges, and the Router appliance spoke's exclude import ranges follow the [Import filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#import-filter-rules-hybrid-spokes).

  * `EXCLUDE_IMPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which subnet routes or transit dynamic routes are never imported from the hub.

    * The exclude import ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the exclude import ranges can match or contain another CIDR.

    * Every CIDR specified in the exclude import ranges must expand to IP addresses that are fully contained by CIDRs or keywords in the include import ranges (or the default include import ranges, if you don't specify any include import ranges explicitly).

    * Exclude import ranges don't support keywords.

    * If you omit the `--exclude-import-ranges`, NCC uses an empty list as the default exclude import ranges.

    * Subnet routes and transit dynamic routes in the hub, the Router appliance spoke's include import ranges, and the Router appliance spoke's exclude import ranges follow the [Import filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#import-filter-rules-hybrid-spokes).




###  API 

To create a Router appliance spoke, use the [`projects.locations.spokes.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/create). For example, to create a spoke that contains two router appliance instances, use the following request:
    
    
      POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/spokes/SPOKE_NAME
      {
        "hub": "HUB_NAME",
        "labels": {"KEY": "VALUE"},
        "linkedRouterApplianceInstances": {
          "instances": [
            {
              "virtualMachine": "ROUTER_APPLIANCE_URI",
              "ipAddress": "IP_ADDRESS",
            },
            {
              "virtualMachine": "ROUTER_APPLIANCE_URI_2,
              "ipAddress": "IP_ADDRESS_2",
            }
          ],
          "siteToSiteDataTransfer": BOOLEAN
          "includeExportRanges": [INCLUDE_EXPORT_RANGES,...]
          "excludeExportRanges": [EXCLUDE_EXPORT_RANGES,...]
          "includeImportRanges": [INCLUDE_IMPORT_RANGES,...]
          "excludeImportRanges": [EXCLUDE_IMPORT_RANGES,...]
        }
      }
     

Replace the following values:

  * `PROJECT_ID`: the project ID of your project
  * `REGION`: the Google Cloud region where you want to locate the spoke—for example, `us-west1`
  * `SPOKE_NAME`: the name for the spoke
  * `HUB_NAME`: the name of the hub that you are attaching the spoke to
  * `KEY`: the key in the key-value pair for the optional label text
  * `VALUE`: the value in the key-value pair for the optional label text
  * `ROUTER_APPLIANCE_URI`: the URI of the first router appliance instance—for example, 
        
        https://www.googleapis.com/compute/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME 

  * `IP_ADDRESS`: the internal IP address of the first router appliance instance
  * `ROUTER_APPLIANCE_URI_2`: the URI of the second router appliance instance
  * `IP_ADDRESS_2`: the internal IP address of the second router appliance instance
  * `BOOLEAN`: a value that determines whether site-to-site data transfer is enabled for this spoke; for more information about this use case, see [Site-to-site data transfer overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer)
  * `INCLUDE_EXPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which dynamic routes can be exported to the hub.

    * The `ALL_IPV4_RANGES` keyword includes all IPv4 addresses, equivalent to the `0.0.0.0/0` CIDR.

    * The include export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the include export ranges can match or contain another CIDR.

    * If you omit `includeExportRanges` for a Router appliance spoke, the default include export ranges is the same as if you had specified `ALL_IPV4_RANGES`.

    * Dynamic routes in the Router appliance spoke, its include export ranges, and its exclude export ranges follow the [Export filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-hybrid-spokes).

  * `EXCLUDE_EXPORT_RANGES`: a comma-delimited list of IP address ranges that define which dynamic routes are never exported to the hub.

    * The exclude export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the exclude export ranges can match or contain another CIDR.

    * Every CIDR specified in the exclude export ranges must expand to IP addresses that are fully contained by CIDRs or keywords in the include export ranges (or the default include export ranges, if you don't specify any include export ranges explicitly).

    * Exclude export ranges don't support keywords.

    * If you omit the `excludeExportRanges`, NCC uses an empty list as the default exclude export ranges.

    * Dynamic routes in the Router appliance spoke, its include export ranges, and its exclude export ranges follow the [Export filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-hybrid-spokes).

  * `INCLUDE_IMPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which subnet routes or transit dynamic routes can be imported from the hub.

    * The `ALL_IPV4_RANGES` keyword includes all IPv4 addresses, equivalent to the `0.0.0.0/0` CIDR.

    * The include import ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the include import ranges can match or contain another CIDR.

    * If you omit `includeImportRanges` for a Router appliance spoke, NCC uses the following defaults:

      * If the Router appliance spoke doesn't have site-to-site data transfer enabled, the default include import ranges is empty.

      * If the Router appliance spoke has site-to-site data transfer enabled, the default include import ranges contains only the IPv4 dynamic routes learned from the hub's other hybrid spokes that have site-to-site data transfer enabled (transit dynamic routes). This default include import ranges doesn't contain any subnet ranges from the hub.

      * Google recommends that you specify an explicit set of include import ranges since the default values vary and might only apply to importing dynamic routes.

    * Subnet routes and transit dynamic routes in the hub, the Router appliance spoke's include import ranges, and the Router appliance spoke's exclude import ranges follow the [Import filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#import-filter-rules-hybrid-spokes).

  * `EXCLUDE_IMPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which subnet routes or transit dynamic routes are never imported from the hub.

    * The exclude import ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the exclude import ranges can match or contain another CIDR.

    * Every CIDR specified in the exclude import ranges must expand to IP addresses that are fully contained by CIDRs or keywords in the include import ranges (or the default include import ranges, if you don't specify any include import ranges explicitly).

    * Exclude import ranges don't support keywords.

    * If you omit the `excludeImportRanges`, NCC uses an empty list as the default exclude import ranges.

    * Subnet routes and transit dynamic routes in the hub, the Router appliance spoke's include import ranges, and the Router appliance spoke's exclude import ranges follow the [Import filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#import-filter-rules-hybrid-spokes).




### Create a VLAN attachment spoke

Before creating VLAN attachment spokes, consider the following guidelines:

  * If you have either Dedicated Interconnect or Partner Interconnect connections configured in a redundant configuration to the same site, you should configure both connections together as a single spoke. The redundant VLAN attachments associated with these connections must be located in the same Google Cloud region. For more information about redundant configurations, see [Best practices for Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices).
  * If you want to use Cloud Interconnect connections from different regions, you must configure them as different spokes.



For information about configuring the resources that are required to create a VLAN attachment spoke, see the following documentation:

  * [Cloud Interconnect landing page](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [Cloud Router landing page](https://docs.cloud.google.com/network-connectivity/docs/router)



For information about verifying VLAN attachment resources, see the following documentation:

  * [Getting Cloud Interconnect diagnostics](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/getting-diagnostics)
  * [Viewing Dedicated Interconnect details](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/viewing-interconnects)
  * [Viewing VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/viewing-vlans)



#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.spokes.create`
  * `compute.routers.get`
  * `compute.interconnectAttachments.get`
  * If you are working in the Google Cloud console, you need permission to view certain network resources. For details, see [Roles and permissions](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/access-control#permission-console). 



**Roles**

  * One of the following: 
    * [Spoke Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.spokeAdmin`)
    * [Hub & Spoke Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.hubAdmin`)
  * A role—such as [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute) (`roles/compute.networkViewer)`—that grants you permission to read Cloud Router resources and your spoke's resource type (in this case, VLAN attachments)
  * If you are working in the Google Cloud console, [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute) (`roles/compute.networkViewer`)



###  Console 

**Enter basic spoke details**

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.
[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)
  2. In the project menu, select a Google Cloud project.
  3. Click the **Spokes** tab.
  4. Click **Add spokes**.
  5. In the **New spoke** form, set the **Spoke type**.
  6. Enter a **Spoke name** and optionally, a **Description**.
  7. Select the **Region** field for the new spoke.
  8. Under **Site-to-site data transfer** , select **On** or **Off**. If the region you selected does not support data transfer, the field is disabled. For more information about this use case, see [Site-to-site data transfer overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer).
  9. In the **VPC network** list, select a network. If you have more than one spoke that uses the data transfer feature, all of these spokes must be in the same VPC network. So if you have already created a spoke that uses data transfer, the **VPC network** value is prepopulated and cannot be changed.



**Enter VLAN attachment details**

  1. Choose a VLAN attachment: 
     1. Click **Add attachment**.
     2. From the **VLAN attachment** menu, select an existing attachment.
  2. Optionally, to propagate subnets that are advertised to the hub to hybrid spokes, under **Hybrid spoke filter** , click **Include all IPv4 ranges from hub to spoke**. 
  3. To add more attachments to this spoke, repeat the preceding step. When you have finished, click **Done** and continue to **Save your spoke**.



**Save your spoke**

  1. If you want to add more spokes, click **Add spoke** and begin the process again, starting with entering a **Spoke name**.
  2. When you are finished adding spokes, click **Create**. The **NCC** page updates to show details about the spokes that you created.



###  gcloud 

To create a VLAN attachment spoke, use the [`gcloud network-connectivity spokes linked-interconnect-attachments create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/create).

For example, to create a spoke that has two VLAN attachments and uses site-to-site data transfer, run the following command.

To enable import of subnet IP address ranges to this spoke, use the `--include-import-ranges` flag.

Use the `site-to-site-data-transfer` flag if you want to enable data transfer for the spoke. If you don't specify `site-to-site-data-transfer`, then `site-to-cloud-data-transfer` is configured by default. For more information about this use case, see [Site-to-site data transfer overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer).

If your hub is configured to use [star topology](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#star-topology), specify the group that the spoke belongs to by using the `--group` flag.
    
    
      gcloud network-connectivity spokes linked-interconnect-attachments create SPOKE_NAME \
          --hub=HUB_NAME \
          [--description="DESCRIPTION"] \
          --group="GROUP" \
          --interconnect-attachments=VLAN_ATTACHMENT_NAME,VLAN_ATTACHMENT_NAME_2 \
          --region=REGION \
          --labels="KEY"="VALUE" \
          --include-export-ranges=[INCLUDE_EXPORT_RANGES,...] \
          --exclude-export-ranges=[EXCLUDE_EXPORT_RANGES,...] \
          --include-import-ranges=[INCLUDE_IMPORT_RANGES,...] \
          --exclude-import-ranges=[EXCLUDE_IMPORT_RANGES,...]
    

Replace the following values:

  * `SPOKE_NAME`: the name for the spoke
  * `HUB_NAME`: the name of the hub, in URI format, that you are attaching the spoke to—for example,  
`projects/myproject/locations/global/hubs/us-west-to-uk`
  * `DESCRIPTION`: an optional description of the spoke
  * `GROUP`: the group that this spoke belongs to—for example, `center`
  * `VLAN_ATTACHMENT_NAME`: the name of the first VLAN attachment to add to the spoke
  * `VLAN_ATTACHMENT_NAME_2`: the name of the second VLAN attachment; if you include a second attachment, make sure you omit a space between the comma and the name of the attachment
  * `REGION`: the Google Cloud region where the spoke is located
  * `KEY`: the key in the key-value pair for the label text
  * `VALUE`: the value in the key-value pair for the label text
  * `INCLUDE_EXPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which dynamic routes can be exported to the hub.

    * The `ALL_IPV4_RANGES` keyword includes all IPv4 addresses, equivalent to the `0.0.0.0/0` CIDR.

    * The `ALL_IPV6_RANGES` keyword includes all IPv6 addresses, equivalent to the `::/0` CIDR ([Preview](https://cloud.google.com/products#product-launch-stages)).

    * The include export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the include export ranges can match or contain another CIDR.

    * If you omit `--include-export-ranges` for a VLAN attachment spoke, the default include export ranges is the same as if you had specified `ALL_IPV4_RANGES`.

    * Dynamic routes in the VLAN attachment spoke, its include export ranges, and its exclude export ranges follow the [Export filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-hybrid-spokes).

  * `EXCLUDE_EXPORT_RANGES`: a comma-delimited list of IP address ranges that define which dynamic routes are never exported to the hub.

    * The exclude export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the exclude export ranges can match or contain another CIDR.

    * Every CIDR specified in the exclude export ranges must expand to IP addresses that are fully contained by CIDRs or keywords in the include export ranges (or the default include export ranges, if you don't specify any include export ranges explicitly).

    * Exclude export ranges don't support keywords.

    * If you omit the `--exclude-export-ranges`, NCC uses an empty list as the default exclude export ranges.

    * Dynamic routes in the VLAN attachment spoke, its include export ranges, and its exclude export ranges follow the [Export filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-hybrid-spokes).

  * `INCLUDE_IMPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which subnet routes or transit dynamic routes can be imported from the hub.

    * The `ALL_IPV4_RANGES` keyword includes all IPv4 addresses, equivalent to the `0.0.0.0/0` CIDR.

    * The `ALL_IPV6_RANGES` keyword includes all IPv6 addresses, equivalent to the `::/0` CIDR ([Preview](https://cloud.google.com/products#product-launch-stages)).

    * The include import ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the include import ranges can match or contain another CIDR.

    * If you omit `--include-import-ranges` for a VLAN attachment spoke, NCC uses the following defaults:

      * If the VLAN attachment spoke doesn't have site-to-site data transfer enabled, the default include import ranges is empty.

      * If the VLAN attachment spoke has site-to-site data transfer enabled, the default include import ranges contains only the IPv4 dynamic routes learned from the hub's other hybrid spokes that have site-to-site data transfer enabled (transit dynamic routes). This default include import ranges doesn't contain any subnet ranges from the hub.

      * Google recommends that you specify an explicit set of include import ranges since the default values vary and might only apply to importing dynamic routes.

    * Subnet routes and transit dynamic routes in the hub, the VLAN attachment spoke's include import ranges, and the VLAN attachment spoke's exclude import ranges follow the [Import filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#import-filter-rules-hybrid-spokes).

  * `EXCLUDE_IMPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which subnet routes or transit dynamic routes are never imported from the hub.

    * The exclude import ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the exclude import ranges can match or contain another CIDR.

    * Every CIDR specified in the exclude import ranges must expand to IP addresses that are fully contained by CIDRs or keywords in the include import ranges (or the default include import ranges, if you don't specify any include import ranges explicitly).

    * Exclude import ranges don't support keywords.

    * If you omit the `--exclude-import-ranges`, NCC uses an empty list as the default exclude import ranges.

    * Subnet routes and transit dynamic routes in the hub, the VLAN attachment spoke's include import ranges, and the VLAN attachment spoke's exclude import ranges follow the [Import filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#import-filter-rules-hybrid-spokes).




###  API 

To create a VLAN attachment spoke, use the [`projects.locations.spokes.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/create). For example, to create a spoke that contains two VLAN attachments and has the import of subnet IP address ranges to this spoke enabled, use the following request:
    
    
      POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/spokes/SPOKE_NAME
      {
        "hub": "HUB_NAME",
        "labels": {"KEY": "VALUE"},
        "linkedInterconnectAttachments": {
          "uris": [
            "VLAN_ATTACHMENT_NAME",
            "VLAN_ATTACHMENT_NAME_2"
          ],
          "siteToSiteDataTransfer": BOOLEAN
          "includeExportRanges": [INCLUDE_EXPORT_RANGES,...]
          "excludeExportRanges": [EXCLUDE_EXPORT_RANGES,...]
          "includeImportRanges": [INCLUDE_IMPORT_RANGES,...]
          "excludeImportRanges": [EXCLUDE_IMPORT_RANGES,...]
        }
      }
    

Replace the following values:

  * `PROJECT_ID`: the project ID of your project
  * `REGION`: the Google Cloud region where you want to locate the spoke—for example, `us-west1`
  * `SPOKE_NAME`: the name for the spoke
  * `HUB_NAME`: the name of the hub that you are attaching the spoke to
  * `KEY`: the key in the key-value pair for the optional label text
  * `VALUE`: the value in the key-value pair for the optional label text
  * `VLAN_ATTACHMENT_NAME`: the name of the first VLAN attachment to add to the spoke
  * `VLAN_ATTACHMENT_NAME_2`: the name of the second VLAN attachment
  * `BOOLEAN`: a value that determines whether site-to-site data transfer is enabled for this spoke; for more information about this use case, see [Site-to-site data transfer overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer)
  * `INCLUDE_EXPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which dynamic routes can be exported to the hub.

    * The `ALL_IPV4_RANGES` keyword includes all IPv4 addresses, equivalent to the `0.0.0.0/0` CIDR.

    * The `ALL_IPV6_RANGES` keyword includes all IPv6 addresses, equivalent to the `::/0` CIDR ([Preview](https://cloud.google.com/products#product-launch-stages)).

    * The include export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the include export ranges can match or contain another CIDR.

    * If you omit `includeExportRanges` for a VLAN attachment spoke, the default include export ranges is the same as if you had specified `ALL_IPV4_RANGES`.

    * Dynamic routes in the VLAN attachment spoke, its include export ranges, and its exclude export ranges follow the [Export filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-hybrid-spokes).

  * `EXCLUDE_EXPORT_RANGES`: a comma-delimited list of IP address ranges that define which dynamic routes are never exported to the hub.

    * The exclude export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the exclude export ranges can match or contain another CIDR.

    * Every CIDR specified in the exclude export ranges must expand to IP addresses that are fully contained by CIDRs or keywords in the include export ranges (or the default include export ranges, if you don't specify any include export ranges explicitly).

    * Exclude export ranges don't support keywords.

    * If you omit the `excludeExportRanges`, NCC uses an empty list as the default exclude export ranges.

    * Dynamic routes in the VLAN attachment spoke, its include export ranges, and its exclude export ranges follow the [Export filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-hybrid-spokes).

  * `INCLUDE_IMPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which subnet routes or transit dynamic routes can be imported from the hub.

    * The `ALL_IPV4_RANGES` keyword includes all IPv4 addresses, equivalent to the `0.0.0.0/0` CIDR.

    * The `ALL_IPV6_RANGES` keyword includes all IPv6 addresses, equivalent to the `::/0` CIDR ([Preview](https://cloud.google.com/products#product-launch-stages)).

    * The include import ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the include import ranges can match or contain another CIDR.

    * If you omit `includeImportRanges` for a VLAN attachment spoke, NCC uses the following defaults:

      * If the VLAN attachment spoke doesn't have site-to-site data transfer enabled, the default include import ranges is empty.

      * If the VLAN attachment spoke has site-to-site data transfer enabled, the default include import ranges contains only the IPv4 dynamic routes learned from the hub's other hybrid spokes that have site-to-site data transfer enabled (transit dynamic routes). This default include import ranges doesn't contain any subnet ranges from the hub.

      * Google recommends that you specify an explicit set of include import ranges since the default values vary and might only apply to importing dynamic routes.

    * Subnet routes and transit dynamic routes in the hub, the VLAN attachment spoke's include import ranges, and the VLAN attachment spoke's exclude import ranges follow the [Import filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#import-filter-rules-hybrid-spokes).

  * `EXCLUDE_IMPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which subnet routes or transit dynamic routes are never imported from the hub.

    * The exclude import ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the exclude import ranges can match or contain another CIDR.

    * Every CIDR specified in the exclude import ranges must expand to IP addresses that are fully contained by CIDRs or keywords in the include import ranges (or the default include import ranges, if you don't specify any include import ranges explicitly).

    * Exclude import ranges don't support keywords.

    * If you omit the `excludeImportRanges`, NCC uses an empty list as the default exclude import ranges.

    * Subnet routes and transit dynamic routes in the hub, the VLAN attachment spoke's include import ranges, and the VLAN attachment spoke's exclude import ranges follow the [Import filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#import-filter-rules-hybrid-spokes).




### Create a VPN spoke

Before creating VPN spokes, consider the following guidelines:

  * When linking HA VPN tunnels to a spoke, we recommend that _all_ tunnels connecting to a single site be configured together as a single spoke. The reverse is also true; two tunnels connecting to two different sites should be attached to different spokes. For example, suppose you want to connect an office in Dallas with an office in Tokyo. The tunnel that connects to Dallas must be part of a different spoke than the one that connects your VPC network to Tokyo.

  * When linking HA VPN tunnels to a spoke, you can't connect HA VPN gateways in different regions to each other in the same Google Cloud project. This is a limitation of HA VPN, not a limitation of NCC.




For information about configuring the resources that are required to create a VPN spoke, see the following documentation:

  * [Cloud VPN landing page](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [Cloud Router landing page](https://docs.cloud.google.com/network-connectivity/docs/router)



For information about verifying VPN resources, see [Checking HA VPN status](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/checking-vpn-status).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.spokes.create`
  * `compute.routers.get`
  * `compute.vpnTunnels.get`
  * If you are working in the Google Cloud console, you need permission to view certain network resources. For details, see [Roles and permissions](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/access-control#permission-console). 



**Roles**

  * One of the following: 
    * [Spoke Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.spokeAdmin`)
    * [Hub & Spoke Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.hubAdmin`)
  * A role—such as [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute) (`roles/compute.networkViewer)`—that grants you permission to read Cloud Router resources and your spoke's resource type (in this case, VPN tunnels)
  * If you are working in the Google Cloud console, [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute) (`roles/compute.networkViewer`)



###  Console 

**Enter basic spoke details**

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.
[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)
  2. In the project menu, select a Google Cloud project.
  3. Click the **Spokes** tab.
  4. Click **Add spokes**.
  5. In the **New spoke** form, set the **Spoke type**.
  6. Enter a **Spoke name** and optionally, a **Description**.
  7. Select the **Region** field for the new spoke.
  8. Under **Site-to-site data transfer** , select **On** or **Off**. If the region you selected does not support data transfer, the field is disabled. For more information about this use case, see [Site-to-site data transfer overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer).
  9. In the **VPC network** list, select a network. If you have more than one spoke that uses the data transfer feature, all of these spokes must be in the same VPC network. So if you have already created a spoke that uses data transfer, the **VPC network** value is prepopulated and cannot be changed.



**Enter VPN tunnel details**

  1. Set the **Spoke type** drop-down list to **VPN tunnels**.
  2. Select the **Region** for the spoke.
  3. Choose a tunnel: 
     1. Click **Add tunnel**.
     2. From the **VPN tunnels** drop-down menu, select an existing tunnel.
  4. Optionally, to propagate subnets that are advertised to the hub to hybrid spokes, under **Hybrid spoke filter** , click **Include all IPv4 ranges from hub to spoke**. 
  5. To add more tunnels to this spoke, repeat the preceding step. When you have finished, click **Done** and continue to **Save your spoke**.



**Save your spoke**

  1. If you want to add more spokes, click **Add spoke** and begin the process again, starting with entering a **Spoke name**.
  2. When you are finished adding spokes, click **Create**. The **NCC** page updates to show details about the spokes that you created.



###  gcloud 

To create a spoke that contains an HA VPN tunnel, use the [`gcloud network-connectivity spokes linked-vpn-tunnels create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-vpn-tunnels/create).

For example, to create a spoke that has two HA VPN tunnels and uses site-to-site data transfer, enter the following command.

To enable import of subnet IP address ranges to this spoke, use the `--include-import-ranges` flag.

Use the `site-to-site-data-transfer` flag if you want to enable data transfer for the spoke. If you don't specify `site-to-site-data-transfer`, then `site-to-cloud-data-transfer` is configured by default. For more information about this use case, see [Site-to-site data transfer overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer).

If your hub is configured to use [star topology](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#star-topology), specify the group that the spoke belongs to by using the `--group` flag.
    
    
      gcloud network-connectivity spokes linked-vpn-tunnels create SPOKE_NAME \
          --hub=HUB_NAME \
          [--description="DESCRIPTION"] \
          --group="GROUP" \
          --vpn-tunnels=TUNNEL_NAME,TUNNEL_NAME_2 \
          --region=REGION \
          --labels="KEY"="VALUE" \
          --include-export-ranges=[INCLUDE_EXPORT_RANGES] \
          --exclude-export-ranges=[EXCLUDE_EXPORT_RANGES] \
          --include-import-ranges=[INCLUDE_IMPORT_RANGES,...] \
          --exclude-import-ranges=[EXCLUDE_IMPORT_RANGES]
    

Replace the following values:

  * `SPOKE_NAME`: the name for the spoke
  * `HUB_NAME`: the name of the hub, in URI format, that you are attaching the spoke to—for example,  
`projects/PROJECT_ID/locations/global/hubs/us-west-to-uk`
  * `DESCRIPTION`: an optional description of the spoke—for example, `us-vpn-spoke`
  * `GROUP`: the group that this spoke belongs to—for example, `center`
  * `TUNNEL_NAME`: the name of the first HA VPN tunnel to add to the spoke
  * `TUNNEL_NAME_2`: the name of the second HA VPN tunnel; if you use a second tunnel, make sure you omit a space between the comma and the name of second tunnel
  * `REGION`: the Google Cloud region where the spoke is located
  * `KEY`: the key in the key-value pair for the optional label text
  * `VALUE`: the value in the key-value pair for the optional label text
  * `[INCLUDE_IMPORT_RANGES,...]`: the IP address ranges that are specified to be imported from hub subnets. Only the `ALL_IPV4_RANGES` keyword is supported. If it is empty, the hybrid spoke doesn't import any subnets from the hub.
  * `INCLUDE_EXPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which dynamic routes can be exported to the hub.

    * The `ALL_IPV4_RANGES` keyword includes all IPv4 addresses, equivalent to the `0.0.0.0/0` CIDR.

    * The `ALL_IPV6_RANGES` keyword includes all IPv6 addresses, equivalent to the `::/0` CIDR ([Preview](https://cloud.google.com/products#product-launch-stages)).

    * The include export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the include export ranges can match or contain another CIDR.

    * If you omit `--include-export-ranges` for a VPN spoke, the default include export ranges is the same as if you had specified `ALL_IPV4_RANGES`.

    * Dynamic routes in the VPN spoke, its include export ranges, and its exclude export ranges follow the [Export filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-hybrid-spokes).

  * `EXCLUDE_EXPORT_RANGES`: a comma-delimited list of IP address ranges that define which dynamic routes are never exported to the hub.

    * The exclude export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the exclude export ranges can match or contain another CIDR.

    * Every CIDR specified in the exclude export ranges must expand to IP addresses that are fully contained by CIDRs or keywords in the include export ranges (or the default include export ranges, if you don't specify any include export ranges explicitly).

    * Exclude export ranges don't support keywords.

    * If you omit the `--exclude-export-ranges`, NCC uses an empty list as the default exclude export ranges.

    * Dynamic routes in the VPN spoke, its include export ranges, and its exclude export ranges follow the [Export filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-hybrid-spokes).

  * `INCLUDE_IMPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which subnet routes or transit dynamic routes can be imported from the hub.

    * The `ALL_IPV4_RANGES` keyword includes all IPv4 addresses, equivalent to the `0.0.0.0/0` CIDR.

    * The `ALL_IPV6_RANGES` keyword includes all IPv6 addresses, equivalent to the `::/0` CIDR ([Preview](https://cloud.google.com/products#product-launch-stages)).

    * The include import ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the include import ranges can match or contain another CIDR.

    * If you omit `--include-import-ranges` for a VPN spoke, NCC uses the following defaults:

      * If the VPN spoke doesn't have site-to-site data transfer enabled, the default include import ranges is empty.

      * If the VPN spoke has site-to-site data transfer enabled, the default include import ranges contains only the IPv4 dynamic routes learned from the hub's other hybrid spokes that have site-to-site data transfer enabled (transit dynamic routes). This default include import ranges doesn't contain any subnet ranges from the hub.

      * Google recommends that you specify an explicit set of include import ranges since the default values vary and might only apply to importing dynamic routes.

    * Subnet routes and transit dynamic routes in the hub, the VPN spoke's include import ranges, and the VPN spoke's exclude import ranges follow the [Import filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#import-filter-rules-hybrid-spokes).

  * `EXCLUDE_IMPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which subnet routes or transit dynamic routes are never imported from the hub.

    * The exclude import ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the exclude import ranges can match or contain another CIDR.

    * Every CIDR specified in the exclude import ranges must expand to IP addresses that are fully contained by CIDRs or keywords in the include import ranges (or the default include import ranges, if you don't specify any include import ranges explicitly).

    * Exclude import ranges don't support keywords.

    * If you omit the `--exclude-import-ranges`, NCC uses an empty list as the default exclude import ranges.

    * Subnet routes and transit dynamic routes in the hub, the VPN spoke's include import ranges, and the VPN spoke's exclude import ranges follow the [Import filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#import-filter-rules-hybrid-spokes).




###  API 

To create a VPN spoke, use the [`projects.locations.spokes.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/create). For example, to create a spoke that contains two HA VPN tunnels and has include import subnet IP address ranges enabled, use the following request:
    
    
      POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/spokes/SPOKE_NAME
      {
        "hub": "HUB_NAME",
        "labels": {"KEY": "VALUE"},
        "linkedVpnTunnels": {
          "uris": [
            "TUNNEL_NAME",
            "TUNNEL_NAME_2"
          ],
          "siteToSiteDataTransfer": BOOLEAN,
          "includeExportRanges": [INCLUDE_EXPORT_RANGES,...]
          "excludeExportRanges": [EXCLUDE_EXPORT_RANGES,...]
          "includeImportRanges": [INCLUDE_IMPORT_RANGES,...]
          "excludeImportRanges": [EXCLUDE_IMPORT_RANGES,...]
        }
      }
    

Replace the following values:

  * `PROJECT_ID`: the project ID of your project
  * `REGION`: the Google Cloud region where you want to locate the spoke—for example, `us-west1`
  * `SPOKE_NAME`: the name for the spoke
  * `HUB_NAME`: the name of the hub that you are attaching the spoke to
  * `KEY`: the key in the key-value pair for the optional label text
  * `VALUE`: the value in the key-value pair for the optional label text
  * `TUNNEL_NAME`: the name of the first HA VPN tunnel to add to the spoke
  * `TUNNEL_NAME_2`: the name of the second HA VPN tunnel
  * `BOOLEAN`: a value that determines whether site-to-site data transfer is enabled for this spoke; for more information about this use case, see [Site-to-site data transfer overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer)
  * `INCLUDE_EXPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which dynamic routes can be exported to the hub.

    * The `ALL_IPV4_RANGES` keyword includes all IPv4 addresses, equivalent to the `0.0.0.0/0` CIDR.

    * The `ALL_IPV6_RANGES` keyword includes all IPv6 addresses, equivalent to the `::/0` CIDR ([Preview](https://cloud.google.com/products#product-launch-stages)).

    * The include export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the include export ranges can match or contain another CIDR.

    * If you omit `includeExportRanges` for a VPN spoke, the default include export ranges is the same as if you had specified `ALL_IPV4_RANGES`.

    * Dynamic routes in the VPN spoke, its include export ranges, and its exclude export ranges follow the [Export filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-hybrid-spokes).

  * `EXCLUDE_EXPORT_RANGES`: a comma-delimited list of IP address ranges that define which dynamic routes are never exported to the hub.

    * The exclude export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the exclude export ranges can match or contain another CIDR.

    * Every CIDR specified in the exclude export ranges must expand to IP addresses that are fully contained by CIDRs or keywords in the include export ranges (or the default include export ranges, if you don't specify any include export ranges explicitly).

    * Exclude export ranges don't support keywords.

    * If you omit the `excludeExportRanges`, NCC uses an empty list as the default exclude export ranges.

    * Dynamic routes in the VPN spoke, its include export ranges, and its exclude export ranges follow the [Export filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-hybrid-spokes).

  * `INCLUDE_IMPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which subnet routes or transit dynamic routes can be imported from the hub.

    * The `ALL_IPV4_RANGES` keyword includes all IPv4 addresses, equivalent to the `0.0.0.0/0` CIDR.

    * The `ALL_IPV6_RANGES` keyword includes all IPv6 addresses, equivalent to the `::/0` CIDR ([Preview](https://cloud.google.com/products#product-launch-stages)).

    * The include import ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the include import ranges can match or contain another CIDR.

    * If you omit `includeImportRanges` for a VPN spoke, NCC uses the following defaults:

      * If the VPN spoke doesn't have site-to-site data transfer enabled, the default include import ranges is empty.

      * If the VPN spoke has site-to-site data transfer enabled, the default include import ranges contains only the IPv4 dynamic routes learned from the hub's other hybrid spokes that have site-to-site data transfer enabled (transit dynamic routes). This default include import ranges doesn't contain any subnet ranges from the hub.

      * Google recommends that you specify an explicit set of include import ranges since the default values vary and might only apply to importing dynamic routes.

    * Subnet routes and transit dynamic routes in the hub, the VPN spoke's include import ranges, and the VPN spoke's exclude import ranges follow the [Import filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#import-filter-rules-hybrid-spokes).

  * `EXCLUDE_IMPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which subnet routes or transit dynamic routes are never imported from the hub.

    * The exclude import ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the exclude import ranges can match or contain another CIDR.

    * Every CIDR specified in the exclude import ranges must expand to IP addresses that are fully contained by CIDRs or keywords in the include import ranges (or the default include import ranges, if you don't specify any include import ranges explicitly).

    * Exclude import ranges don't support keywords.

    * If you omit the `excludeImportRanges`, NCC uses an empty list as the default exclude import ranges.

    * Subnet routes and transit dynamic routes in the hub, the VPN spoke's include import ranges, and the VPN spoke's exclude import ranges follow the [Import filter rules for hybrid spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#import-filter-rules-hybrid-spokes).




### List spokes

When you create a spoke, it is always associated with a hub. You can use the `list spokes` operation to list all spokes within a single project. You can also list all spokes associated with a hub across projects. See also Describe a hub.

**Note:** To list [VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview), you must set the region flag to `--global`.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.spokes.list`



**Roles**

  * One of the following: 
    * [Hub & Spoke Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.hubViewer`)
    * [Spoke Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.spokeAdmin`
    * [Hub & Spoke Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.hubAdmin`)



###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select the project that contains the hub for which you want to list the existing spokes.

  3. On the **Hub** tab, select the hub.

  4. Click the **Spoke** tab. All the spokes attached to that hub are listed.

  5. Use the **Filter** field to sort spokes by name, type, status, ID, region, resource count, BGP sessions, or description.

  6. To view details for a specific spoke, click the spoke name.




###  gcloud 

**Spokes**

  * To list existing spokes in a project, use the [`gcloud network-connectivity spokes list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/list).
        
        gcloud network-connectivity spokes list \
            --region=LOCATION
        

Replace `LOCATION` with the appropriate region.

  * To list existing VPC spokes in a project, use the same command with the `--global` flag:
        
        gcloud network-connectivity spokes list \
            --global
        

  * To list all spokes associated with a hub across all projects use the [`gcloud network-connectivity hubs list-spokes` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/list-spokes).
        
        gcloud network-connectivity hubs list-spokes HUB_NAME
        

Replace `HUB_NAME` with the name of the hub for which you want to list spokes, such as `my-hub`.




**Filters**

  * To list all VPC spokes that belong to a specific group, use the [`gcloud network-connectivity hubs list-spokes` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/list-spokes) and specify the `group` filter.
        
        gcloud network-connectivity hubs list-spokes HUB_NAME \
            --filter="group:GROUP_NAME"
        

Replace the following values:

    * `HUB_NAME`: the name of the hub for which you want to list spokes
    * `GROUP_NAME`: the name of the spoke group. Supported values are `default` for mesh topology and `center` or `edge` for a star topology hub.
  * To list all VPC spokes associated with a hub that are pending review by the hub administrator, use the same command and specify the `reason` filter.
        
        gcloud network-connectivity hubs list-spokes HUB_NAME \
            --filter="reason:PENDING_REVIEW"
        

Replace `HUB_NAME` with the name of the hub for which you want to list spokes.

  * To list all inactive VPC spokes associated with a hub, use the same command and specify the `state` filter.
        
        gcloud network-connectivity hubs list-spokes HUB_NAME \
          --filter="state:INACTIVE"
        

Replace `HUB_NAME` with the name of the hub for which you want to list inactive spokes.




###  API 

  * To list existing spokes in a project, use the [`projects.locations.spokes.list` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/list).
        
        GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/spokes
        

Replace the following values:

    * `PROJECT_ID`: the project ID of the project that contains the spokes to list
    * `LOCATION`: the region where the spoke is located—for example, `us-west1` or `global` for VPC spokes
  * To list all spokes associated with a hub across all projects, use the [`networkconnectivity.hubs.listSpokes` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs/listSpokes).
        
        GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs/HUB_NAME:listSpokes
        

Replace the following values:

    * `PROJECT_ID`: the project ID of the hub
    * `HUB_NAME`: the name of the hub for which you want to list spokes
  * To get an aggregated list of existing spokes, where the values of multiple rows are grouped together to form a single summary value, use the [`projects.locations.spokes.list` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/list) with a hyphen (`-`) after `locations` as a wildcard.
        
        GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/-/spokes
        

Replace `PROJECT_ID` with the project ID of the project that contains the spokes to list.




### Describe a spoke

To get detailed information about an existing spoke, use the following guidance.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.spokes.describe`
  * Additionally, if you are working in the Google Cloud console: 
    * `networkconnectivity.hubs.get`
    * `networkconnectivity.hubs.list`
    * `networkconnectivity.spokes.list`
    * `compute.projects.get`



**Roles**

  * One of the following: 
    * [Hub & Spoke Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.hubViewer`)
    * [Spoke Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.spokeAdmin`
    * [Hub & Spoke Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.hubAdmin`)
  * If you are working in the Google Cloud console, [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`)



###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project.

  3. On the **Hub** tab, select the hub. All the spokes attached to that hub are listed.

  4. To view details for a specific spoke, do one of the following:

     * In the **Spoke name** column, select a spoke to view the **Spoke details** page.
     * On the **Spokes** tab, click the **Spoke name** column, and then select a spoke to view the **Spoke details** page.



###  gcloud 

**Spokes**

  * To describe a spoke, use the [`gcloud network-connectivity spokes describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/describe).
        
        gcloud network-connectivity spokes describe SPOKE_NAME \
            --region=LOCATION
        

Replace the following values:

    * `SPOKE_NAME`: the name of the spoke
    * `LOCATION`: the region where the spoke is located
  * To describe a VPC spoke, use the same command with the `--global` flag:
        
        gcloud network-connectivity spokes describe SPOKE_NAME \
            --global
        

Replace `SPOKE_NAME` with the name of the spoke.




###  API 

To describe a spoke, use the [`projects.locations.spokes.get` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/get).
    
    
     GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/spokes/SPOKE_NAME
    

Replace the following values:

  * `PROJECT_ID`: the project ID of the project that contains the spoke
  * `LOCATION`: the region where the spoke is located—for example, `us-west1` or `global` for VPC spokes
  * `SPOKE_NAME`: the name of the spoke



### View the Private Service Connect connection propagation status

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.hubs.queryStatus`



**Roles**

  * One of the following: 
    * [Hub Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.hubAdmin`)
    * [Hub Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.hubViewer`)



If you have Private Service Connect connection propagation enabled, view the connection propagation status by following these steps.

###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project.

  3. On the **Hub** tab, select the hub for which you want to see the connection propagation status. The **Hub details** page lists the endpoints with the Private Service Connect connection propagation status for each endpoint.

  4. To view only the endpoints that have errors, click **Show errors only**.




###  gcloud 

Use the [`gcloud network-connectivity hubs query-status` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/query-status).

You can sort and group the results by using the `--filter`, `--limit`, `--sort-by`, and `--group-by` flags. For detailed information about how to use these flags, see the `gcloud network-connectivity hubs query-status` command page.
    
    
    gcloud network-connectivity hubs query-status HUB_NAME
    

Replace `HUB_NAME` with the name of the hub for which you want to check the connection propagation status.

The output is similar to the following:
    
    
    gcloud network-connectivity hubs query-status HUB
    
    SOURCE_FORWARDING_RULE   SOURCE_SPOKE    SOURCE_GROUP    TARGET_SPOKE    TARGET_GROUP      CODE          COUNT
    PSC1                     spoke1          default          spoke2         default           READY           1
    PSC1                     spoke1          default          spoke3         default           ERROR_..        1
    PSC1                     spoke1          default          spoke4         default           ERROR_..        1
    PSC1                     spoke1          default          spoke5         default           READY           1
    PSC2                     spoke5          default          spoke1         default           READY           1
    PSC2                     spoke5          default          spoke2         default           PROPAGATING     1
    PSC2                     spoke5          default          spoke3         default           ERROR_..        1
    PSC2                     spoke5          default          spoke4         default           ERROR_..        1
    

###  API 

  * Use the [`networkconnectivity.hubs.queryStatus` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs/queryStatus).
        
        GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs/HUB_NAME:queryStatus
        

Replace the following values:

    * `PROJECT_ID`: the project ID of the project that contains the hub
    * `HUB_NAME`: the name of the hub that you want to check the status of
  * To check the status results grouped by spoke name and status code, use the `psc_propagation_status.source_spoke,psc_propagation_status.code` string:
        
        GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs/HUB_NAME:queryStatus?group_by=psc_propagation_status.source_spoke,psc_propagation_status.code
        

  * To drill down on errors of a specific type related to a specific source spoke, specify the spoke name and the status code:
        
        GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/hubs/HUB_NAME:queryStatus?filter=psc_propagation_status.source_spoke=SPOKE_NAMEpsc_propagation_status.code=CODE
        

Replace the following values:

    * `SPOKE_NAME`: the name of the spoke that you want to check the status of
    * `CODE`: the current status code that the spoke is showing



The following table lists the propagation status messages and what they mean.

Code | Message  
---|---  
**Ready** | The propagated Private Service Connect connection is ready.   
**Propagating** | The Private Service Connect connection propagation is pending. This is a transient state.   
**Error, producer propagated connection limit exceeded** | The propagated Private Service Connect connection propagation failed because the VPC network or the project of the target spoke has exceeded the propagation connection limit set by the producer. To address this issue, see your producer's documentation or contact their support team.   
**Error, producer NAT IP space exhausted** | The Private Service Connect connection propagation failed because the NAT IP subnet space is exhausted. It is equivalent to the `Needs attention` status of the PSC connection. For details, see [Connection statuses](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#connection-statuses) in the Private Service Connect documentation.   
**Error, producer quota exceeded** | The Private Service Connect connection propagation failed because the `PSC_ILB_CONSUMER_FORWARDING_RULES_PER_PRODUCER_NETWORK` quota in the producer VPC network is exceeded.   
**Error, consumer quota exceeded** | The Private Service Connect connection propagation failed because the `PSC_PROPAGATED_CONNECTIONS_PER_VPC_NETWORK` quota in the consumer VPC network is exceeded.   
  
### Update a spoke

After a spoke is created, the properties that you can update depend on the spoke type. To update properties depending on your spoke type, use the following table:

Procedure | Description  
---|---  
Update description, labels, and include import IP address ranges | For all spoke types, you can change the spoke's description and the labels applied to the spoke; for information about labels, see [Create and update labels for projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels#requirements). If the spoke is a hybrid spoke, you can also change which IP address ranges are imported from hub subnets.  
Update exported subnet address ranges | If the spoke is a VPC or a producer VPC spoke, you can change whether the spoke includes or excludes address ranges.  
Update a Router appliance spoke's underlying resources | If the spoke is a Router appliance spoke, you can change its underlying resources; however, the new resources must be in the same VPC network as the original resources.  
To update the capacity of an NCC Gateway spoke, see Update an NCC Gateway spoke's capacity. 

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.spokes.update`



**Roles**

  * One of the following: 
    * [Spoke Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.spokeAdmin`
    * [Hub & Spoke Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.hubAdmin`)



#### Update description, labels, and include import IP address ranges

This section describes how to update a spoke's description, labels, and include IP address ranges.

**Note:** You can update a spoke's label only by using the Google Cloud CLI or by calling the Network Connectivity API.

###  gcloud 

To update a spoke, use one of the following commands:

  * [`gcloud network-connectivity spokes linked-router-appliances update`](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-router-appliances/update)
  * [`gcloud network-connectivity spokes linked-interconnect-attachments update`](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-interconnect-attachments/update)
  * [`gcloud network-connectivity spokes linked-vpn-tunnels update`](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-vpn-tunnels/update)
  * [`gcloud network-connectivity spokes linked-vpc-network update`](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-vpc-network/update)
  * [`gcloud network-connectivity spokes linked-producer-vpc-network update`](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/update)



You can update which IP address ranges are imported from hub subnets by adding the `ALL_IPV4_RANGES` keyword to the list for all hybrid spoke types.

For example, to update a Router appliance spoke's description, label, and export filters, and import filters, run the following command:
    
    
      gcloud network-connectivity spokes linked-router-appliances update SPOKE_NAME \
          --description="DESCRIPTION" \
          --region=LOCATION \
          --update-labels="KEY"="VALUE" \
          --include-export-ranges=[INCLUDE_EXPORT_RANGES,...] \
          --exclude-export-ranges=[EXCLUDE_EXPORT_RANGES,...] \
          --include-import-ranges=[INCLUDE_IMPORT_RANGES,...] \
          --exclude-import-ranges=[EXCLUDE_IMPORT_RANGES,...]
    

Replace the following values:

  * `SPOKE_NAME`: the name of the spoke to update
  * `DESCRIPTION`: a new description for the spoke
  * `LOCATION`: the Google Cloud region where the spoke is located—for example, `us-west1` or `global`
  * `KEY`: the key in the key-value pair
  * `VALUE`: the value in the key-value pair
  * `[INCLUDE_EXPORT_RANGES,...]`, `[EXCLUDE_EXPORT_RANGES,...]`, `[INCLUDE_IMPORT_RANGES,...]`, and `[EXCLUDE_IMPORT_RANGES,...]`: See Create a Router appliance spoke for details.



###  API 

To update a spoke, use the [`projects.locations.spokes.patch` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/patch). For example, to update a Router appliance spoke's description and label, run the following command:
    
    
     PATCH https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/spokes/SPOKE_NAME
     {
       "description": "DESCRIPTION"
       "labels": {
         "KEY": "VALUE"
          "includeExportRanges": [INCLUDE_EXPORT_RANGES,...]
          "excludeExportRanges": [EXCLUDE_EXPORT_RANGES,...]
          "includeImportRanges": [INCLUDE_IMPORT_RANGES,...]
          "excludeImportRanges": [EXCLUDE_IMPORT_RANGES,...]
       }
     }
    

Replace the following values:

  * `PROJECT_ID`: the project ID of the project that contains the spoke
  * `REGION`: the region where the spoke is located—for example, `us-west1`
  * `SPOKE_NAME`: the name of the spoke to update
  * `DESCRIPTION`: a new description for the spoke
  * `KEY`: the key in the key-value pair
  * `VALUE`: the value in the key-value pair
  * `[INCLUDE_EXPORT_RANGES,...]`, `[EXCLUDE_EXPORT_RANGES,...]`, `[INCLUDE_IMPORT_RANGES,...]`, and `[EXCLUDE_IMPORT_RANGES,...]`: See Create a Router appliance spoke for details.



#### Update exported subnet address ranges

This section describes how to configure which subnet address ranges are exported from a VPC spoke or producer VPC spoke to the hub, using include and exclude export filters.

For more information about IP address range export filters, see [VPC connectivity with export filters](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#vpc-connectivity-with-export-filters).

When changing the set of subnet address ranges exported from a spoke located in a project different from the hub's project, consider the following.

  * Spoke updates must comply with all the NCC [quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/quotas); otherwise, the spoke update fails.
  * If your VPC spoke is part of an [auto-accept project](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-hub-admin#auto-accept-projects) configured by a hub administrator, then your changes to include and exclude export filters are accepted automatically.
  * If your VPC spoke isn't part of an auto-accept project, the changes to include and exclude export filters requires a hub administrator's approval.

To check the status of your proposed updates, see [Check the status of a VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-check-spoke-status).

  * If your spoke update proposal is rejected by the hub administrator, you can send a new spoke update request with different filtering ranges.




###  Console 

To update whether a VPC spoke exports subnet ranges, complete the following steps:

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project.

  3. Click the **Spokes** tab.

  4. Click the name of the spoke that you want to modify, and then click edit**Edit**.

  5. Modify the selected VPC spoke filters.

     1. **IPv4 ranges** : configure the export of IPv4 subnet ranges.

        * **Include export IPv4 subnet ranges from spoke to hub** : by default, this checkbox is selected and all subnet ranges that use private IPv4 addresses are exported.

If you don't want to export IPv4 subnet ranges, clear this checkbox.

If you only want to export specific IPv4 subnet ranges, select **Specify IPv4 ranges** and enter the address ranges that you want to export. The IPv4 subnet ranges that you specify must be private IPv4 address ranges, excluding privately used public IPv4 addresses. For more information, see [Valid IPv4 ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges).

        * **Exclude export IPv4 subnet ranges from spoke to hub** : if the spoke exports subnet ranges and you want to exclude specific ranges from export, enter those ranges in this field.

     2. **IPv6 ranges** ([Preview](https://cloud.google.com/products#product-launch-stages)): configure the export of IPv6 subnet ranges (internal and external).

        * **Include export all IPv6 subnet ranges from spoke to hub** : to export all IPv6 subnet ranges to the hub, select the checkbox.

If you only want to export specific IPv6 subnet ranges, select **Specify IPv6 ranges** and enter the address ranges that you want to export.

        * **Exclude export IPv6 subnet ranges from spoke to hub** : if the spoke exports subnet ranges and you want to exclude specific ranges from export, enter those ranges in this field.

  6. Click **Save**.




###  gcloud 

To configure which subnet address ranges are exported from a VPC spoke to the hub, run the following command:
    
    
      gcloud network-connectivity spokes linked-vpc-network update SPOKE_NAME \
          --include-export-ranges=[INCLUDE_EXPORT_RANGES] \
          --exclude-export-ranges=[EXCLUDE_EXPORT_RANGES]
    

Replace the following values:

  * `SPOKE_NAME`: the name of the spoke to update

  * `INCLUDE_EXPORT_RANGES` and `EXCLUDE_EXPORT_RANGES`: See Create a VPC spoke for details.




###  API 

To update whether a VPC spoke exports subnet ranges, use the following request:
    
    
     PATCH https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/spokes/SPOKE_NAME
     {
       "linkedVpcNetwork" : {
         "includeExportRanges": "[INCLUDE_EXPORT_RANGES]",
         "excludeExportRanges": "[EXCLUDE_EXPORT_RANGES]"
        }
     }
    

Replace the following values:

  * `PROJECT_ID`: the project ID of the project that contains the spoke

  * `SPOKE_NAME`: the name of the spoke to update

  * `INCLUDE_EXPORT_RANGES` and `EXCLUDE_EXPORT_RANGES`: See Create a VPC spoke for details.




#### Update an NCC Gateway spoke's capacity

When you change the capacity on an existing gateway spoke, it can result in a brief network disruption for existing and new flows across the gateway. Also, some capacity options might be blocked for some partners.

To update the capacity of an existing NCC Gateway spoke, follow these steps.

###  gcloud 

To update the capacity of an existing NCC Gateway spoke, use the [`gcloud beta network-connectivity spokes gateways update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/gateways/update).
    
    
    gcloud beta network-connectivity spokes gateways update SPOKE_NAME \
        [--description=DESCRIPTION] \
        --region=REGION \
        --hub=HUB_NAME \
        --capacity CAPACITY
    

Replace the following:

  * `SPOKE_NAME`: the name of the spoke
  * `DESCRIPTION`: an optional description of the spoke
  * `REGION`: the region that you want NCC Gateway to be deployed in
  * `HUB_NAME`: the name of the hub for the spoke
  * `CAPACITY`: the maximum bandwidth of NCC Gateway, in Gbps



Supported values are 1 Gbps, 10 Gbps, and 100 Gbps. The default is 10 Gbps. When you change this value on an existing gateway spoke, it can result in a brief network disruption for existing and new flows across the gateway.

###  API 

To update an NCC Gateway spoke, use the [`projects.locations.spokes.patch` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.spokes/patch)
    
    
    PATCH https://networkconnectivity.googleapis.com/v1beta/projects/PROJECT/locations/LOCATION/spokes?updateMask=gateway.capacity
    {
      "name": SPOKE_NAME,
      "hub": HUB_NAME,
      "gateway": {
         "capacity": CAPACITY
      }
    }
    

Replace the following:

  * `PROJECT`: the project ID of the project that contains the spoke
  * `LOCATION`: the region that you want NCC Gateway to be deployed in
  * `SPOKE_NAME`: the name of the spoke
  * `HUB_NAME`: the name of the hub for the spoke
  * `CAPACITY`: the maximum bandwidth of NCC Gateway, in Gbps

Supported values are 1 Gbps, 10 Gbps, and 100 Gbps. The default is 10 Gbps. When you change this value on an existing gateway spoke, it can result in a brief network disruption for existing and new flows across the gateway. 




#### Update a Router appliance spoke's underlying resources

This section describes how to update a Router appliance spoke's underlying resources.

###  Console 

To change the resources used by a Router appliance spoke, complete the following steps:

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project.

  3. Click the **Spokes** tab.

  4. Click the name of the spoke that you want to modify.

  5. Do either of the following:

     * To add resources, click **Add instances** and follow the prompts to select one or more VMs. When you have finished, click **OK**.
     * To remove resources, select the VMs that you want to remove and click delete**Remove instances**. In the confirmation dialog, click **OK**.



###  gcloud 

If needed, you can update a Router appliance spoke to use a different router appliance instance, as long as the new resource is in the same VPC network as the original one. To replace the existing resource with a new one, run the following command:
    
    
      gcloud network-connectivity spokes linked-router-appliances update SPOKE_NAME \
          --region=LOCATION \
          --router-appliance=instance="ROUTER_APPLIANCE_URI",ip=IP_ADDRESS
    

Replace the following values:

  * `SPOKE_NAME`: the name of the spoke
  * `LOCATION`: the Google Cloud region where the spoke is located—for example, `us-west1`
  * `ROUTER_APPLIANCE_URI`: the URI of the new router appliance instance to associate with the spoke—for example, 
        
        "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME"

  * `IP_ADDRESS`: the internal IP address of the new router appliance instance



###  API 

If needed, you can update a Router appliance spoke to use a different router appliance instance, as long as the new resource is in the same VPC network as the original one. To replace the existing resource with a new one, use the following request:
    
    
     PATCH https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/spokes/SPOKE
     {
       "linkedRouterApplianceInstances": {
         "instances": [
           {
             "virtualMachine": "ROUTER_APPLIANCE_URI",
             "ipAddress": "IP_ADDRESS",
           }
         ]
       }
     }
    

Replace the following values:

  * `PROJECT_ID`: the project ID of the project that contains the spoke
  * `REGION`: the region where the spoke is located—for example, `us-west1`
  * `SPOKE`: the name of the spoke
  * `ROUTER_APPLIANCE_URI`: the URI of the new router appliance instance to associate with the spoke—for example, 
        
        "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME"

  * `IP_ADDRESS`: the internal IP address of the new router appliance instance



### Delete a spoke

When you delete a spoke, you also detach the resources from that spoke. That is, deleting a spoke doesn't delete the resources; it only disassociates them from the spoke.

If you want to delete an NCC Gateway spoke, you must first delete the following resources: 

  * All Cloud Routers associated with the gateway spoke
  * The Secure Access Connect attachment 

If you want to delete a VPC spoke that is associated with a producer VPC spoke, you must first delete the producer VPC spoke. 

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.spokes.delete`
  * Additionally, if you are working in the Google Cloud console:
    * `networkconnectivity.hubs.get`
    * `networkconnectivity.hubs.list`
    * `networkconnectivity.spokes.list`
    * `compute.projects.get`



**Roles**

  * One of the following: 
    * [Spoke Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.spokeAdmin`
    * [Hub & Spoke Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkconnectivity) (`roles/networkconnectivity.hubAdmin`)
  * If you are working in the Google Cloud console, [Compute Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkViewer) (`roles/compute.networkViewer`)



###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project.

  3. Click the **Spokes** tab.

  4. View the list of **Spoke names** for the project.

  5. Select the spokes to delete.

  6. Click delete**Delete spokes**.

  7. In the confirmation dialog, do one of the following:

     * Click **Cancel** if you don't want to delete the spokes.
     * Click **Delete** to delete the spokes.



###  gcloud 

To delete a spoke, use the [`gcloud network-connectivity spokes delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/delete).
    
    
      gcloud network-connectivity spokes delete SPOKE_NAME \
          --region=REGION
    

Replace the following values:

  * `SPOKE_NAME`: the name of the spoke to delete
  * `REGION`: the region where the spoke is located; this option is required in addition to the region listed in the full spoke name. If you are deleting a VPC spoke, you must specify `--global`.



###  API 

To delete an existing spoke, use the [`projects.locations.spokes.delete` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/delete).
    
    
      DELETE https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/spokes/SPOKE_NAME
    

Replace the following values:

  * `PROJECT_ID`: the project ID of the project that contains the spoke to delete
  * `LOCATION`: the region where the spoke is located—for example, `us-west1` or `--global` for VPC spokes
  * `SPOKE_NAME`: the name of the spoke to delete



## What's next

  * To view a list of partners whose solutions are integrated with NCC, see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).
  * To find solutions for Router appliance issues, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting#troubleshooting-ra).
  * To get details about API and Google Cloud CLI commands, see [APIs and reference](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
