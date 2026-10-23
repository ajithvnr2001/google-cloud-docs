---
url: https://docs.cloud.google.com/vmware-engine/docs/networking/howto-setup-private-service-access/
title: (Legacy) Set up private connections \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:01.964608+00:00
---

# (Legacy) Set up private connections  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/networking/howto-setup-private-service-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# (Legacy) Set up private connections

**Caution:** Enabling private services access is only required for legacy networks. You don't need to enable private services for standard networks.

Private services access is a private connection between your Virtual Private Cloud (VPC) network and networks in VMware Engine. This page explains how to set up private services access to Google Cloud VMware Engine and connect your VPC network to your private cloud.

Private services access enables the following behavior:

  * Exclusive communication by internal IP address for virtual machine (VM) instances in your VPC network and VMware VMs. VM instances don't need internet access or external IP addresses to reach services that are available through private services access.
  * Communication between VMware VMs and [Google Cloud-supported services](https://docs.cloud.google.com/vpc/docs/private-services-access#private-services-supported-services), which support private services access using internal IP addresses.
  * Use of existing on-premises connections to connect to your VMware Engine private cloud, if you have on-premises connectivity using Cloud VPN or Cloud Interconnect to your VPC network.



You can set up private services access independently of VMware Engine private cloud creation. The private connection can be created before or after creation of the private cloud to which you want to connect your VPC network.

## Permissions

  1. Make sure that you have the following role or roles on the project: Compute > Network Admin 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 



## Before you begin

  1. You must have an existing VPC network.
  2. [Activate the Service Networking API](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/getting-started) in your project.
  3. [Configure private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access) in the VPC network you want to connect to.

**Note:** You must allocate address ranges for the private service connection, for private cloud management, and for workload network segments. This ensures that there are no IP address conflicts between your VPC network subnets and the IP addresses you use in VMware Engine.
  4. Locate the **Peered project ID** of your VPC network by doing the following:

     1. In the [Google Cloud console](https://console.cloud.google.com/), go to **VPC network peering**. A VPC network peering connection with name **servicenetworking-googleapis-com** is listed in the peering table.
     2. Copy the **Peered project ID** so that you can use it while setting up a private connection in the Google Cloud console.



## Multi-VPC connectivity

VMware Engine lets you access the same private cloud from different VPC networks without the need to change any existing VPC architectures deployed in Google Cloud. For example, multi-VPC connectivity is useful when you have separate VPC networks for testing and development.

This situation requires VPC networks to communicate with VMware VMs or other destination addresses in separate vSphere resource groups on the same private cloud or across multiple private clouds.

By default, you can peer 3 VPC networks per region. This peering limit includes the VPC peering used by the [internet access network service](https://docs.cloud.google.com/vmware-engine/docs/networking/workload-internet-access). To increase this limit, [contact Cloud Customer Care](https://docs.cloud.google.com/vmware-engine/docs/support).

### IP address uniqueness

When you connect your VPC network to a VMware Engine regional network, follow these guidelines to ensure IP address uniqueness:

  * VMware Engine IP ranges and subnets in your VPC network can't use the same IP address ranges.

  * VMware Engine IP ranges can't fit within a subnet IP address range in your VPC network. Subnet routes in your VPC network must have the most specific IP address ranges.

  * Carefully review the VPC network routes overview for details about how VPC network routes work.

  * If you need to connect two or more VMware Engine networks to the same VPC network, you must either use unique IP ranges for each VMware Engine network, or you must only enable NSX connectivity for one of the VMware Engine networks using the same IP ranges as another VMware Engine network.


**Caution:** Not following these guidelines might result in unexpected behaviors, including unreachability of your VMware Engine private clouds.

## Create a private connection

Create a private connection in the console, Google Cloud CLI, or the REST API. In your request, set the connection type to `PRIVATE_SERVICE_ACCESS` and the routing mode to `GLOBAL` routing mode.

###  Console 

  1. In the Google Cloud console, go to the **Private connections** page.

[Go to Private connections](https://console.cloud.google.com/vmwareengine/private-connections)

  2. Click **Create**.

  3. Provide a **Name** and **Description** for the connection.

  4. Select the VMware Engine network to connect to.

  5. In the **Peered project ID** field, paste the **Peered project ID** that you copied in the prerequisites.

  6. In **Private connection type** , select **Private services access**.

  7. Select the routing mode for this VPC network peering connection. In most cases, we recommend the [global routing mode](https://docs.cloud.google.com/vpc/docs/vpc-peering#global). If you don't want Google services peered with your VPC network to communicate across regions, select the `Regional` routing mode instead. This Selection overrides the existing routing mode.

  8. Click **Submit**.




When the connection is created, you can select the specific connection from the list of private connections. The details page for each private connection displays the routing mode of the private connection and any routes learned over VPC peering.

The **Exported routes** table shows private clouds learned from the region and exported over VPC peering. When multiple VPC networks are peered to the same VMware Engine regional network, routes received from one VPC network are not advertised to the other VPC network.

###  gcloud 

  1. Create a private connection by running the [`gcloud vmware private-connections create` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-connections/create):
         
         gcloud vmware private-connections create PRIVATE_CONNECTION_ID \
           --location=REGION\
           --description="" \
           --vmware-engine-network=NETWORK_ID \
           --service-project=SERVICE_NETWORKING_TENANT_PROJECT\
           --type=PRIVATE_SERVICE_ACCESS \
           --routing-mode=MODE
         

**Note:** For this command, there is a flag, `--service-network`, that is auto-populated in `gcloud` based on the type of private connection being created. If you interact with the API directly, you must pass the full name of the `service_network` in the format: `projects/PROJECT_ID/global/networks/NETWORK_ID`.

Replace the following:

     * `PRIVATE_CONNECTION_ID`: the private connection name to create
     * `REGION`: the region to create this private connection in; this must match the VMware Engine network region
     * `NETWORK_ID`: the VMware Engine network name
     * `SERVICE_NETWORKING_TENANT_PROJECT`: the project name for this service networking tenant VPC. You can find the SNTP in the PEER_PROJECT column of the peering name `servicenetworking-googleapis-com`.
     * `MODE`: the routing mode, either `GLOBAL` or `REGIONAL`
  2. Optional: If you want to list your private connections, run the [`gcloud vmware private-connections list` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-connections/list):
         
         gcloud vmware private-connections list \
             --location=REGION

Replace the following:

     * `REGION`: the region of the network to list.



### API

To create a Compute Engine VPC and a private service access connection using the VMware Engine API:

  1. Create a private connection by making a `POST` request:
         
         POST "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/privateConnections?private_connection_id=PRIVATE_CONNECTION_ID"
         
         '{
           "description": "My first private connection",
           "vmware_engine_network":
         "projects/PROJECT_ID/locations/REGION/vmwareEngineNetworks/NETWORK_ID
           "type": "PRIVATE_SERVICE_ACCESS",
           "routing_mode": "MODE",
           "service_network":
         "projects/SERVICE_NETWORKING_TENANT_PROJECT/global/networks/SERVICE_NETWORK"
         }'
         

Replace the following:

     * `PRIVATE_CONNECTION_ID`: the private connection name for this request
     * `REGION`: the region to create this private connection in
     * `NETWORK_ID`: the VMware Engine network for this request
     * `SERVICE_NETWORKING_TENANT_PROJECT`: the project name for this service networking tenant VPC. You can find the SNTP in the PEER_PROJECT column of the peering name `servicenetworking-googleapis-com`
     * `SERVICE_NETWORK`: the network in the tenant project
  2. Optional: If you want to list your private connections, make a `GET` request:
         
         GET "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/privateConnections"
         

Replace the following:

     * `PROJECT_ID`: the project name for this request.
     * `REGION`: the region to list the private connections in.



## Edit a private connection

You can edit a private connection after creating it. Once created, you can change the routing mode between `GLOBAL` and `REGIONAL`. In Google Cloud CLI or the API, you can also update the description of the private connection.`

###  Console 

  1. In the Google Cloud console, go to the **Private connections** page.

[Go to Private connections](https://console.cloud.google.com/vmwareengine/private-connections)

  2. Click the name of the private connection you want to edit.

  3. On the details page, click **Edit**.

  4. Update the description or the routing mode of the connection.

  5. **Save** your changes.




###  gcloud 

Edit a private connection by running the [`gcloud vmware private-connections update` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-connections/update):
    
    
    gcloud vmware private-connections update PRIVATE_CONNECTION_ID \
       --location=REGION \
       --description=DESCRIPTION \
       --routing-mode=MODE
    

Replace the following:

  * `PROJECT_ID`: the project name for this request
  * `REGION`: the region to update this private connection in
  * `DESCRIPTION`: the new description to use
  * `PRIVATE_CONNECTION_ID`: the private connection ID for this request
  * `MODE`: the routing mode, either `GLOBAL` or `REGIONAL`



###  API 

To edit a private connection using the VMware Engine API, make a `PATCH` request:
    
    
    PATCH "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/privateConnections/PRIVATE_CONNECTION_ID?update_mask=description, routing_mode"
    
    '{
      "description": "Updated description for the private connection",
      "routing_mode": "MODE"
    }'

Replace the following:

  * `PROJECT_ID`: the project name for this request
  * `REGION`: the region to update this private connection in
  * `PRIVATE_CONNECTION_ID`: the private connection name for this request
  * `MODE`: the routing mode, either `GLOBAL` or `REGIONAL`



## Describe a private connection

You can get the description of any private connection using the Google Cloud CLI or VMware Engine API.

###  gcloud 

Get a description of a private connection by running the [`gcloud vmware private-connections describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-connections/describe):
    
    
    gcloud vmware private-connections describe PRIVATE_CONNECTION_ID \
        --location=REGION
    

Replace the following:

  * `PRIVATE_CONNECTION_ID`: the private connection name for this request
  * `REGION`: the region of the private connection.



###  API 

To get a description of a private connection using the VMware Engine API, make a `GET` request:
    
    
    GET "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/privateConnections/PRIVATE_CONNECTION_ID"
    

Replace the following:

  * `PROJECT_ID`: the project name for this request.
  * `PRIVATE_CONNECTION_ID`: the private connection name for this request.
  * `REGION`: the region of the private connection.



After the private connections you deleted are no longer visible in the list of private connections, you can delete the private connection in the Google Cloud console. Performing this step out of order can result in stale DNS entries in both Google Cloud projects.

## List peering routes for a private connection

To list peering routes exchanged for a private connection, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Private connections** page.

[Go to Private connections](https://console.cloud.google.com/vmwareengine/private-connections)

  2. Click the name of the private connection you want to view.




The details page describes imported and exported routes.

###  gcloud 

List peering routes exchanged for a private connection by running the [`gcloud vmware private-connections routes list` command](https://docs.cloud.google.com/sdk/gcloud/reference/vmware/private-connections/routes/list):
    
    
    gcloud vmware private-connections routes list \
        --private-connection=PRIVATE_CONNECTION_ID \
        --location=REGION

Replace the following:

  * `PRIVATE_CONNECTION_ID`: the private connection name for this request.
  * `REGION`: the region of the private connection.



###  API 

To list peering routes exchanged for a private connection using the VMware Engine API, make a `GET` request:
    
    
    GET "https://vmwareengine.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/privateConnections/PRIVATE_CONNECTION_ID/peeringRoutes"
    

Replace the following:

  * `PROJECT_ID`: the project name for this request.
  * `REGION`: the region of the private connection.
  * `PRIVATE_CONNECTION_ID`: the private connection name for this request.



## Routing limits

The maximum number of routes that a private cloud can _receive_ is **200**. For example, those routes can come from on-premises networks, peered VPC networks, and other private clouds in the same VPC network. This route limit corresponds to the Cloud Router maximum number of custom route advertisements per BGP session limit.

In a given region, you can _advertise_ at most **100** unique routes from VMware Engine to your VPC network using private services access. For example, those unique routes include private cloud management IP address ranges, NSX workload network segments, and HCX internal IP address ranges. This route limit includes all private clouds in the region and corresponds to the Cloud Router learned route limit.

For information about routing limits, see [Cloud Router Quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits).

## Troubleshooting

The following video will show you how to verify and troubleshoot peering connection issues between Google Cloud VPC and Google Cloud VMware Engine.

## What's next

  * [Manage your private cloud resources and activity](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
