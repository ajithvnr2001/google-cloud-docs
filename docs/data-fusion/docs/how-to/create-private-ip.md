---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip/
title: Create a private instance with VPC peering \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:24.663987+00:00
---

# Create a private instance with VPC peering  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/create-private-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Create a private instance with VPC peering Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a Cloud Data Fusion instance with an internal IP address. You create the instance in a [VPC](https://docs.cloud.google.com/vpc/docs/overview) network or a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) network.

**Note:** In Cloud Data Fusion 6.10.0 and later, we recommend creating private instances with [Private Service Connect](https://docs.cloud.google.com/data-fusion/docs/how-to/configure-private-service-connect), not with VPC network peering.

A private Cloud Data Fusion instance has the following benefits:

  * Connections to the instance are established over a private VPC network in your Google Cloud project. Traffic over the network doesn't go through the public internet.

  * The instance can connect to your on-premises resources, such as relational databases because your on-premises network connects to the Google Cloud private VPC network through [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview). You can securely access your on-premises resources, such as databases, over the private network without opening up access to Google Cloud.




## Objectives

  * Set up the VPC network or the Shared VPC network.
  * Allocate an IP range that will be used to deploy the Cloud Data Fusion instance in the tenant project.
  * Create the Cloud Data Fusion private instance.
  * Set up the VPC network peering between the VPC that contains the Cloud Data Fusion instance and the VPC that contains the associated tenant project.
  * For Shared VPC networks, set up Identity and Access Management (IAM) permissions.
  * If your private instance uses Cloud Data Fusion version 6.2.0 or earlier, create a firewall rule.
  * Let different Google Cloud services communicate internally with each other by enabling Private Google Access on the Managed Service for Apache Spark subnet.



## Before you begin

  * To learn about Cloud Data Fusion's deployment architecture, see [Networking](https://docs.cloud.google.com/data-fusion/docs/concepts/networking).



## Set up the VPC network

If you haven't already done so, [create a VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks) or a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#setting_up_shared_vpc).

To set up your VPC network, you must allocate an IP address range.

### Allocate an IP range

### VPC network

If you're not using a Shared VPC network, Cloud Data Fusion allocates an IP range by default when you create an instance.

**Note:** If you're not using a Shared VPC network, skip this section and go to Create a private instance.

### Shared VPC network

**Note:** Follow these steps only if you're using a Shared VPC network.

To use a Shared VPC you must allocate an IP range for your Cloud Data Fusion instance.

To allocate an IP range for your Cloud Data Fusion instance, follow these steps:

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. In the **Name** column, click the VPC network in which you want to create a private Cloud Data Fusion instance.

The **VPC network details** page opens.

  3. Click **Private service connection**. If prompted, enable the Service Networking API by clicking **Enable API**.

![Configure VPC network details.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/private-ip/vpc-network-details.png)

  4. Click **Allocate IP range**.

     1. Give your IP range a name.

     2. For **IP range** , click **Automatic**.

**Note:** For custom ranges, Cloud Data Fusion supports [valid private IPv4 address ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges), including non-RFC 1918 IP ranges. It doesn't support privately used external IP address ranges. This range allocation doesn't have to consume IPs from any of your subnets, but it must not overlap with any range allocations that you make in the future.
     3. Specify a prefix size of `22`.

**Note:** The IP range `/22` is required per Cloud Data Fusion instance and cannot be shared by multiple instances. The IP range belongs to Google Cloud and is where the underlying instance components and infrastructure are hosted.
     4. Click **Allocate**.

![Allocate an IP range.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/private-ip/allocate-ip-range.png)




## Create a private instance

Create the private Cloud Data Fusion instance in a VPC network or a Shared VPC network.

**Caution:** After you create a Cloud Data Fusion instance, you cannot change its edition.

### VPC network

To create the instance in a VPC network, use either the Google Cloud console or cURL.

If you use the Google Cloud console to create your private instance, Cloud Data Fusion allocates the `/22` IP address range by default. To choose a different IP range, you must use the cURL command.

### Console

  1. Go to the **Create Data Fusion instance** page.

[ Go to Create Data Fusion instance](https://console.cloud.google.com/data-fusion/instance-create)

  2. Enter an instance name and description for your instance.

  3. Select the **Region** in which to create the instance.

  4. Select a Cloud Data Fusion **Version** and [**Edition**](https://cloud.google.com/data-fusion/pricing).

  5. Specify the [**Managed Service for Apache Spark service account**](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/service-accounts) to use for running your Cloud Data Fusion pipeline in Managed Service for Apache Spark. The default Compute Engine account is pre-selected.

**Note:** You must grant appropriate Identity and Access Management roles for your needs to the service account. For more information, see [Granting service account user permission](https://docs.cloud.google.com/data-fusion/docs/how-to/granting-service-account-permission).
  6. Expand the **Advanced Options** menu and click **Enable Private IP**.

  7. In the **Network** field, choose a network in which to create the instance.

  8. Click **Create**. It takes up to 30 minutes for the instance creation process to complete.

**Note:** While Cloud Data Fusion creates your instance, a progress wheel displays next to the instance name on the **Instances** page. After completion, it turns into a green check mark and indicates that you can start using the instance.



### cURL

For your convenience, you can export the following variables, or you can directly substitute these values into the following commands:
    
    
    export PROJECT=PROJECT_ID
    export LOCATION=REGION
    export DATA_FUSION_API_NAME=datafusion.googleapis.com
    

To create the instance, call its [`create()`](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances/create) method:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" https://$DATA_FUSION_API_NAME/v1/projects/$PROJECT/locations/$LOCATION/instances?instance_id=INSTANCE_ID -X POST -d '{"description": "Private CDF instance created through REST.", "type": "ENTERPRISE", "privateInstance": true, "networkConfig": {"network": "NETWORK_NAME", "ipAllocation": "IP_RANGE"}}'
    

Replace the following:

  * `INSTANCE_ID`: The ID string your new instance should get.
  * `NETWORK_NAME`: The name of the VPC network where you want to create your private instance.
  * `IP_RANGE`: The IP range that you allocated. To find the IP range in the Google Cloud console, go to **VPC network details** > **Private service connection** > **Internal IP range** .



### Shared VPC network

To create your instance in a Shared VPC network, use cURL, not the Google Cloud console.

### cURL

For your convenience, you can export the following variables. Alternatively, you can directly substitute these values in the following commands:
    
    
    export PROJECT=PROJECT_ID
    export LOCATION=REGION
    export DATA_FUSION_API_NAME=datafusion.googleapis.com
    

To create the instance, call its [`create()`](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances/create) method:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" https://$DATA_FUSION_API_NAME/v1/projects/$PROJECT/locations/$LOCATION/instances?instanceId=INSTANCE_ID -X POST -d '{"description": "Private CDF instance created through REST.", "type": "ENTERPRISE", "privateInstance": true, "networkConfig": {"network": "projects/SHARED_VPC_HOST_PROJECT_ID/global/networks/NETWORK_NAME", "ipAllocation": "IP_RANGE"}}'
    

Replace the following:

  * `INSTANCE_ID`: The ID string your new instance should get.
  * `SHARED_VPC_HOST_PROJECT_ID`: The ID of the project that's [hosting the Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc).
  * `NETWORK_NAME`: The name of the VPC network in which you want to create the private instance.
  * `IP_RANGE`: The IP range that you allocated. To find the IP range in the Google Cloud console, go to the **VPC network details** page > **Private service connection** > **Internal IP range**.

**Note:** You cannot use an IP range allocated to another Google Cloud service. It must be the same IP range that was allocated in the previous step.**Note:** When using a Shared VPC network, the name of the VPC network peering that is created between your project and the tenant project is a combination of VPC network name and instance name. The length of the [VPC network peering name](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks) must not exceed 63 characters.

## Set up VPC network peering

**Key Point:** Your Cloud Data Fusion instance is created in its own VPC and you might need to set up VPC network peering to connect with the source and sink that you use in your pipeline.

Cloud Data Fusion services that you use in your [design environment](https://docs.cloud.google.com/data-fusion/docs/concepts/networking#design_environment) (for example: Wrangler, Connection Manager, and Schema Validation) initiate network connections from the tenant project VPC to the source systems. Cloud Data Fusion uses [VPC network peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) to establish network connectivity to the VPC or Shared VPC that contains your instance. The VPC network peering lets Cloud Data Fusion access resources in your network through internal IP addresses using your own VPC and its controls. To connect with a resource in another network, see the steps for connection use cases.

The following section describes how to [create a peering configuration](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#creating_a_peering_configuration) between your network and the Cloud Data Fusion [tenant project](https://docs.cloud.google.com/service-infrastructure/docs/manage-tenant-projects) network.

### Get the tenant project ID

To create a peering configuration, you need the [tenant project](https://docs.cloud.google.com/data-fusion/docs/concepts/overview#tenant-project) ID.

  1. Go to the Cloud Data Fusion **Instances** page. 

[ Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. In the **Instance Name** column, select the instance.

  3. On the **Instance details** page, copy the **Tenant project ID** , which is required when you create a peering connection in the following steps.




### Create a peering connection

  1. Go to the **VPC network peering** page.

[Go to VPC network peering](https://console.cloud.google.com/networking/vpc-connectivity/peering)

  2. Click **Create connection** > **Continue**.

  3. On the **Create peering connection** page that opens, do the following:

     1. Enter a **Name** for your peering connection.
     2. For **Your VPC network** , select the network that contains your Cloud Data Fusion instance.
     3. For **Peered VPC network** , select **In another project**.
     4. For **Project ID** , enter the tenant project ID you found previously in this tutorial.
     5. For **VPC network name** , select a network or enter INSTANCE_REGION-INSTANCE_ID.

Replace the following:

        * INSTANCE_REGION: the region in which you created your Cloud Data Fusion instance.
        * INSTANCE_ID: the ID of your Cloud Data Fusion instance.
**Note:** When the instance is created, a VPC network named INSTANCE_REGION`-`INSTANCE_ID is created in the tenant project. The private Cloud Data Fusion instance is deployed in that VPC. This network already exists with the configuration to peer with your customer project VPC.
     6. Select the Internet Protocol version for the peering connection to exchange IPv4 and IPv6 routes between your VPC network and the peered VPC network. For more information, see [VPC network peering](https://docs.cloud.google.com/vpc/docs/vpc-peering).

     7. Select **Export custom routes** so that custom [routes](https://docs.cloud.google.com/vpc/docs/routes) can be exported from your VPC network to the tenant VPC network.

     8. Choose whether to allow subnet routes with public IPv4 to be imported or exported into your VPC network.

     9. Click **Create**.

The VPC network peering becomes active shortly after it is created.




## Set up IAM permissions

### VPC network

Skip this step and go to Create a firewall rule.

### Shared VPC network

If you create your Cloud Data Fusion instance in a Shared VPC network, you must grant the [Compute Network User role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) to the following service accounts. To give permissions to all subnets, grant the role to the Shared VPC host project.

To further control access, instead grant the role to a specific subnet, and the [Network Viewer role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkViewer) on the host project.

  * Cloud Data Fusion service account: `service-PROJECT_NUMBER@gcp-sa-datafusion.iam.gserviceaccount.com`
  * Managed Service for Apache Spark service account: `service-PROJECT_NUMBER@dataproc-accounts.iam.gserviceaccount.com`



`PROJECT_NUMBER` is the number of the Google Cloud project that contains your Cloud Data Fusion instance.

For more information, see [Granting access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#granting-console) to the required service accounts.

## Create a firewall rule

Create a firewall rule on your VPC network that allows for incoming SSH connections from the IP range you specified when you created your private Cloud Data Fusion instance.

This step is required for Cloud Data Fusion versions earlier than 6.2.0. It allows communication between Cloud Data Fusion and Managed Service for Apache Spark clusters running pipelines.

You can create the firewall rule by [using the Google Cloud console](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) or by [using the gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create).

### Console

See [Creating firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules).

### gcloud

Run the following command: 
    
    
    gcloud compute firewall-rules create FIREWALL_NAME-allow-ssh --allow=tcp:22 --source-ranges=IP_RANGE --network=NETWORK_NAME --project=PROJECT_ID
    

Replace the following:

  * `FIREWALL_NAME`: The name of the firewall rule to create.
  * `IP_RANGE`: The IP range you allocated.
  * `NETWORK_NAME`: The name of the network to which the firewall rule is attached. It's the name of the VPC network in which you created the private instance.
  * `PROJECT_ID`: The ID of the project that's [hosting the VPC network](https://docs.cloud.google.com/vpc/docs/vpc).



## Steps for connection use cases

The following sections describe connection-related use cases for private instances.

### Enable Private Google Access

To [access resources through internal IP addresses](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/network#create_a_cluster_with_internal_ip_addresses_only), Cloud Data Fusion must create the Managed Service for Apache Spark clusters and run the data pipelines in a subnet that has Private Google Access. You must enable Private Google Access for the subnet that contains the Managed Service for Apache Spark clusters.

  * If only one subnet is present in the region where the Managed Service for Apache Spark clusters are launched, then the cluster is launched in that subnet.
  * If there are multiple subnets in a region, you must configure Cloud Data Fusion to select the subnet with Private Google Access for launching Managed Service for Apache Spark clusters.

**Caution:** If Private Google Access isn't enabled on that subnet, the pipeline run fails. To specify the subnet after you create an instance, edit the compute profile.



To enable Private Google Access for the subnet, see [Private Google Access configuration](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-pga).

### Optional: Connect to other sources

After you create a private instance in Cloud Data Fusion, you can connect to other sources, such as the following use cases:

  * [On-premises databases and systems running in other VPC networks](https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-vpc-network)
  * Other Google Cloud services running in their own network in private mode, such as [Cloud SQL](https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-cloud-sql-source)
  * [Sources on the public internet](https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-public-source)



### Optional: Enable DNS Peering

Enable [DNS Peering](https://docs.cloud.google.com/data-fusion/docs/how-to/resolve-domain-names) in the following cases:

  * When Cloud Data Fusion connects to systems through hostnames, and not IP addresses
  * When the target system is deployed behind a load balancer, such as it does in some SAP deployments



## What's next

  * Learn about [security concepts in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/security).
  * Learn about [connecting to resources in external networks](https://docs.cloud.google.com/data-fusion/docs/how-to/connect-to-vpc-network).
  * Learn about other key Cloud Data Fusion [concepts and features](https://docs.cloud.google.com/data-fusion/docs/concepts/overview).
  * See Cloud Data Fusion [pricing](https://cloud.google.com/data-fusion/pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
