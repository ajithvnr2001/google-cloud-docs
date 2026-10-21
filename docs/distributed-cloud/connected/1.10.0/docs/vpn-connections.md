---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/vpn-connections/
title: Create and manage VPN connections \u00a0|\u00a0 Google Distributed Cloud connected, version 1.10.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:43:36.725881+00:00
---

# Create and manage VPN connections  |  Google Distributed Cloud connected, version 1.10.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/vpn-connections/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/overview)



Send feedback 

#  Create and manage VPN connections Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create and manage Google Distributed Cloud connected VPN connection resources in a Distributed Cloud connected zone.

This functionality is only available on Distributed Cloud connected racks. Distributed Cloud connected servers don't support VPN connection resources.

For more information about Distributed Cloud VPN connections, see [How Distributed Cloud connected works](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/how-it-works).

**Note:** The Google Cloud CLI instructions on this page assume that you are using [Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with `bash` installed.

Keep the following in mind:

  * You must configure your network to [allow the traffic required](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/requirements#firewall) by Distributed Cloud VPN connections.

  * When you create a Distributed Cloud VPN connection, Distributed Cloud connected creates the required Cloud VPN gateway and Cloud Router resources. The name of the Cloud VPN gateway is prefixed with `anthos-mcc`. The name of the Cloud Router is prefixed with `gdce`. You must not modify these resources; otherwise, the Distributed Cloud VPN connection might stop functioning. If you accidentally modify these resources, you must delete and re-create the affected Distributed Cloud VPN connection.

  * Distributed Cloud connected creates a single Cloud Router per Google Cloud project per region when you create your first Distributed Cloud VPN connection in that Google Cloud project and region. All VPN connections subsequently created in that Google Cloud project and region reuse that same Cloud Router resource.

  * A Cloud Router resource can only be deleted when there are no secondary network interfaces attached to it. Distributed Cloud connected automatically deletes a Cloud Router when you delete the last remaining VPN connection attached to it.

  * Distributed Cloud VPN connections support IPv4 addresses only.

  * You can create only one VPN connection per Distributed Cloud connected cluster.

  * If your local network uses multiple network address translation (NAT) gateways, you must configure them so that your Distributed Cloud connected installation uses a single IP address for outbound traffic to your Virtual Private Cloud (VPC) network.

  * By default, Distributed Cloud connected configures a single VPN client on a single node to connect to Google Cloud by using two VPN tunnels, also known as [HA VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#ha-vpn) on the Google Cloud end. You can further increase the availability of the VPN connection by using the `--high-availability` flag. This flag instructs Distributed Cloud connected to configure two VPN clients on two separate nodes for a total of four VPN tunnels.

  * You must delete and re-create a VPN connection if you want to change its configuration.

  * You can manage VPN connections by using the Google Cloud CLI or the Distributed Cloud Edge Container API.




## Create a VPN connection

To create a Distributed Cloud VPN connection, complete the steps in this section.

To complete this task, you must have the [Edge Container Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/permissions#edge-admin) (`roles/edgecontainer.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud container vpn-connections create` command:
    
    
    gcloud edge-cloud container vpn-connections create VPN_CONNECTION_NAME \
        --project=PROJECT_ID \
        --location=REGION \
        --cluster=CLUSTER_NAME \
        --vpc-network=VPC_NETWORK_NAME \
        --nat-gateway-ip=NAT_GATEWAY_IP \
        --router=ROUTER_NAME \
        --high-availability
    

Replace the following:

  * `VPN_CONNECTION_NAME`: a descriptive name that uniquely identifies this VPN connection.
  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone is created.
  * `CLUSTER_NAME`: the name of the target Distributed Cloud connected cluster.
  * `VPC_NETWORK_NAME`: the name of the target VPC network to which this VPN connection points. This network must be in the same Google Cloud project as your Distributed Cloud connected installation.
  * `NAT_GATEWAY_IP`: the NAT gateway IP address for the target cluster. Omit this flag if you are not using NAT.
  * `ROUTER_NAME` (optional): specifies an existing Cloud Router resource to use for this VPN connection. Otherwise, Distributed Cloud connected creates a Cloud Router automatically if one does not yet exist in the target Google Cloud project and region.
  * `--high-availability` (optional): configures this VPN connection for high availability on the cluster side by setting up two separate VPN clients that run on two separate nodes. To disable high availability, omit this flag.



###  API 

Make a `POST` request to the `projects.locations.vpnConnections.create` method:
    
    
    POST /v1/PROJECT_ID/locations/REGION/vpnConnections?vpnConnectionId=VPN_CONNECTION_ID&requestId=REQUEST_ID
    {
      "name": string,
      "labels": {
       },
      "natGatewayIp": NAT_GATEWAY,
      "cluster": CLUSTER_PATH,
      "vpc": VPC_NETWORK_ID
      "enableHighAvailability": HA_ENABLE,
      "router": ROUTER_NAME,
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone is created.
  * `VPN_CONNECTION_ID`: a unique programmatic ID that identifies this node pool resource.
  * `REQUEST_ID`: a unique programmatic ID that identifies this request.
  * `VPN_CONNECTION_NAME`: a descriptive name that uniquely identifies this VPN connection.
  * `NAT_GATEWAY`: the IP address of your NAT gateway.
  * `CLUSTER_PATH`: the full canonical path to the target cluster.
  * `VPC_NETWORK_ID`: the ID of the target VPC network.
  * `HA_ENABLE`: indicates whether to configure this VPN connection for high availability on the cluster side. If set to `TRUE`, configures two separate VPN clients that run on two separate nodes.
  * `ROUTER_NAME` (optional): specifies an existing Cloud Router resource to use for this VPN connection. Otherwise, Distributed Cloud connected creates a Cloud Router automatically if one does not yet exist in the target Google Cloud project and region. 



## List VPN connections

To list the VPN connections provisioned for a Distributed Cloud connected cluster, complete the steps in this section.

To complete this task, you must have the [Edge Container Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/permissions#edge-viewer) (`roles/edgecontainer.viewer`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud container vpn-connections list` command:
    
    
    gcloud edge-cloud container vpn-connections list \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud zone is created.



###  API 

Make a `GET` request to the `projects.locations.vpnConnections.list` method:
    
    
    GET /v1/PROJECT_ID/locations/REGION/vpnConnections?filter=FILTER&pageSize=PAGE_SIZE&orderBy=SORT_BY&pageToken=PAGE_TOKEN
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone is created.
  * `FILTER`: an expression that constrains the returned results to specific values.
  * `PAGE_SIZE`: the number of results to return per page.
  * `SORT_BY`: a comma-delimited list of field names by which the returned results are sorted. The default sort order is ascending; for descending sort order, prefix the desired field with `~`.
  * `PAGE_TOKEN`: a token received in the response to the last list request in the `nextPageToken` field in the response. Send this token to receive a page of results.



## Get information about a VPN connection

To get information about a Distributed Cloud VPN connection, complete the steps in this section.

To complete this task, you must have the [Edge Container Viewer role](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/permissions#edge-viewer) (`roles/edgecontainer.viewer`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud container vpn-connections describe` command:
    
    
    gcloud edge-cloud container vpn-connections describe VPN_CONNECTION_NAME \
        --project=PROJECT_ID \
        --location=REGION
    

Replace the following:

  * `VPN_CONNECTION_NAME`: the name of the target VPN connection.
  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone is created.



###  API 

Make a `GET` request to the `projects.locations.vpnConnections.get` method:
    
    
    GET /v1/PROJECT_ID/locations/REGION/vpnConnections/VPN_CONNECTION_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone is created.
  * `VPN_CONNECTION_NAME`: the name of the target VPN connection.



## Delete a VPN connection

To delete a Distributed Cloud VPN connection, complete the steps in this section.

If you are deleting the last remaining VPN connection associated with a Cloud Router resource that Distributed Cloud previously created in the Google Cloud project, deleting the VPN connection automatically deletes the associated Cloud Router resource. However, only Cloud Router resources that are automatically created by Distributed Cloud connected are automatically deleted in this situation. Distributed Cloud connected does not delete existing Cloud Router resources that are specified by using the `--router` flag.

To complete this task, you must have the [Edge Container Admin role](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/permissions#edge-admin) (`roles/edgecontainer.admin`) in your Google Cloud project.

###  gcloud 

Use the `gcloud edge-cloud container vpn-connections delete` command:
    
    
    gcloud edge-cloud container vpn-connections delete VPN_CONNECTION_NAME \
        --location=REGION \
        --project=PROJECT_ID
    

Replace the following:

  * `VPN_CONNECTION_NAME`: a descriptive name that uniquely identifies this VPN connection.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone is created.
  * `PROJECT_ID`: the ID of the target Google Cloud project.



###  API 

Make a `DELETE` request to the `projects.locations.vpnConnections.delete` method:
    
    
    DELETE /v1/PROJECT_ID/locations/REGION/vpnConnections/VPN_CONNECTION_NAME?requestId=REQUEST_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone is created.
  * `VPN_CONNECTION_NAME`: the name of the target VPN connection.
  * `REQUEST_ID`: a unique programmatic ID that identifies this request.



## Manage cross-project VPN connections

Distributed Cloud connected also allows you to create VPN connections to VPC networks in a Google Cloud project that's different from the Google Cloud project that contains your Distributed Cloud connected cluster.

### Prerequisites

You must satisfy the prerequisites in this section before you can create cross-project VPN connections.

#### Caller account permissions

The caller user account in the target VPC project must have the following permissions. These permissions are encapsulated in the [Project IAM Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`):

  * `resourcemanager.projects.get`
  * `resourcemanager.projects.getIamPolicy`
  * `resourcemanager.projects.setIamPolicy`



For information about how to set IAM roles and permissions, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

#### Distributed Cloud service account permissions

To allow Distributed Cloud connected to create the Cloud Router and Cloud VPN resources in the target VPC project that enables the cross-project VPN connection, you must grant the [Compute Network Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) to the Distributed Cloud service account in your Distributed Cloud cluster.

To grant the Compute Network Admin role, do the following.

###  gcloud 

Use the `gcloud projects add-iam-policy-binding` command:
    
    
    gcloud projects add-iam-policy-binding VPC_PROJECT_ID \
        --member="serviceAccount:service-PROJECT_NUM@gcp-sa-edgecontainer.iam.gserviceaccount.com" \
        --role="roles/compute.networkAdmin" \
        --project=VPC_PROJECT_ID
    

Replace the following:

  * `VPC_PROJECT_ID`: the ID of the target VPC project.
  * `PROJECT_NUM`: the number of the target Distributed Cloud Google Cloud project.



### Create a cross-project VPN connection

To create a VPN connection to a VPC network in a different Google Cloud project, complete the steps in this section.

###  gcloud 

Use the `gcloud edge-cloud container vpn-connections create` command:
    
    
    gcloud edge-cloud container vpn-connections create VPN_CONNECTION_NAME \
        --project=PROJECT_ID \
        --location=REGION \
        --cluster=CLUSTER_NAME \
        --vpc-project=VPC_PROJECT_ID \
        --vpc-network=VPC_NETWORK_NAME \
        --nat-gateway-ip=NAT_GATEWAY_IP \
        --high-availability
    

Replace the following:

  * `VPN_CONNECTION_NAME`: a descriptive name that uniquely identifies this VPN connection.
  * `PROJECT_ID`: the ID of the target Distributed Cloud connected cluster Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone is created.
  * `CLUSTER_NAME`: the name of the target Distributed Cloud connected cluster.
  * `VPC_PROJECT_ID`: the ID of the target Google Cloud project containing the target VPC network.
  * `VPC_NETWORK_NAME`: the name of the target VPC network to which this VPN connection points.
  * `NAT_GATEWAY_IP`: the NAT gateway IP address for the target cluster. Omit this flag if you are not using NAT.
  * `--high-availability` (optional): configures this VPN connection for high availability on the cluster side by setting up two separate VPN clients that run on two separate nodes. To disable high availability, omit this flag.



###  API 

Make a `POST` request to the `projects.locations.vpnConnections.create` method:
    
    
    POST /v1/PROJECT_ID/locations/REGION/vpnConnections?vpnConnectionId=VPN_CONNECTION_ID&requestId=REQUEST_ID
    {
      "name": string,
      "labels": {
       },
      "natGatewayIp": NAT_GATEWAY,
      "cluster": CLUSTER_PATH,
      "vpc": VPC_NETWORK_ID,
      "vpcProject": VPC_PROJECT_ID,
      "vpcServiceAccount": var>VPC_PROJECT_SERVICE_ACCOUNT,
      "enableHighAvailability": HA_ENABLE,
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the target Google Cloud project.
  * `REGION`: the Google Cloud region in which the target Distributed Cloud connected zone is created.
  * `VPN_CONNECTION_ID`: a unique programmatic ID that identifies this node pool resource.
  * `REQUEST_ID`: a unique programmatic ID that identifies this request.
  * `VPN_CONNECTION_NAME`: a descriptive name that uniquely identifies this VPN connection.
  * `NAT_GATEWAY`: the IP address of your NAT gateway.
  * `CLUSTER_PATH`: the full canonical path to the target cluster.
  * `VPC_NETWORK_ID`: the ID of the target VPC network.
  * `VPC_PROJECT_ID`: the ID of the target Google Cloud project that contains the target VPC network.
  * `HA_ENABLE`: indicates whether to configure this VPN connection for high availability on the cluster side. If set to `TRUE`, configures two separate VPN clients that run on two separate nodes.



### Cloud Audit Logs for cross-project VPN connections

When you create a cross-project VPN connection, Cloud Audit Logs logs are written as follows:

  * The audit logs for your Distributed Cloud connected cluster record the long-running operation, authentication, and authorization information for the cross-project VPN connection. This information includes the caller of the create operation and the permissions the caller has been granted or denied.
  * The audit logs for the target VPC project record information about the Google Cloud resources that enable the cross-project VPN connection, such as the Cloud Router and Cloud VPN resources. The caller that accesses these resources is the Distributed Cloud connected service account to which you have granted the [Edge Container Service Agent role](https://docs.cloud.google.com/iam/docs/roles-permissions/edgecontainer#edgecontainer.serviceAgent) (`roles/edgecontainer.serviceAgent`).



## Limitations of VPN connections

If you modify the node pool of the cluster in which you created a particular VPN connection, you must delete and recreate that VPN connection. Otherwise, unexpected behavior might occur, including:

  * Intermittent loss of VPN connectivity
  * Inability to create VPN connections in the other clusters in the Distributed Cloud connected zone



### Limitations of cross-project VPN connections

Additionally, cross-project VPN connections have the following limitations:

  * The cross-project VPN connection resource exists only on your Distributed Cloud connected cluster.
  * If you alter the permissions on the Distributed Cloud connected service account in the target VPC project, you are not able to delete the cross-project VPN connection from your Distributed Cloud connected cluster.



## What's next

  * [Deploy workloads on Google Distributed Cloud connected](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/deploy)
  * [Manage zones](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/zones)
  * [Create and manage clusters](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/clusters)
  * [Create and manage node pools](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/nodepools)
  * [Manage virtual machines](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/virtual-machines)
  * [Manage GPU workloads](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/gpu)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
