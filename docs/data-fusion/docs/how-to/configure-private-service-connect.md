---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/configure-private-service-connect/
title: Create a private instance with Private Service Connect \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:16.616514+00:00
---

# Create a private instance with Private Service Connect  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/configure-private-service-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Create a private instance with Private Service Connect Stay organized with collections  Save and categorize content based on your preferences. 

In Cloud Data Fusion, Private Service Connect interfaces let you establish private connectivity between your instance and resources in your Virtual Private Cloud (VPC) or on-premises networks. This setup keeps design-time operations—such as connection validations and previews—on private IP addresses without exposing workloads to the public internet.

## About Private Service Connect in Cloud Data Fusion

Cloud Data Fusion instances might need to connect to resources located on-premises, on Google Cloud, or on other cloud providers. When using Cloud Data Fusion with internal IP addresses, connections to external resources are established over a Virtual Private Cloud (VPC) network in your Google Cloud project. Traffic over the network doesn't go through the public internet. When Cloud Data Fusion is provided access to your VPC network using VPC peering, there are limitations, which become apparent when you use large-scale networks.

With Private Service Connect interfaces, Cloud Data Fusion connects to your VPC without the use of VPC peering. [Private Service Connect interface](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces) is a type of [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) that provides a way for Cloud Data Fusion to initiate private and secure connections to consumer VPC networks. This not only provides the flexibility and ease of access (like VPC peering), but also provides explicit authorization and consumer-side control that Private Service Connect offers.

The following diagram shows how Private Service Connect interface is deployed in Cloud Data Fusion:

![Deployment of Private Service Connect interface.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/private-service-connect/private-service-connect.png)

**Figure 1.** Deployment of Private Service Connect interface

**Description of Figure 1:**

  * The virtual machines (VM) running Cloud Data Fusion are hosted in a Google-owned tenant project. To access resources in the customer VPC, Cloud Data Fusion VMs use the IP address assigned by the Private Service Connect network interface, from the customer's subnet. This subnet is added to the network attachment used by Cloud Data Fusion.

  * IP packets originating from the Private Service Connect interface are treated similarly to those from a VM in the same subnet. This configuration enables Cloud Data Fusion to directly access resources in the customer VPC or a peer VPC without the need for a proxy.

  * Internet resources become accessible when Cloud NAT is enabled in the customer VPC, while on-premises resources are reachable through an interconnect.

  * To manage ingress or egress from the Private Service Connect, you can implement firewall rules.




### Key benefits

The following are the key benefits of using Cloud Data Fusion with Private Service Connect:

  * **Better control of IP space**. You control the IP addresses that Cloud Data Fusion uses to connect to your network. You choose the subnets from which the IP addresses are allocated to Cloud Data Fusion. All the traffic from Cloud Data Fusion has a source IP address from your configured subnet.

Private Service Connect eliminates the need for reserved IP addresses from a customer VPC. VPC peering requires a /22 CIDR block (1024 IP addresses) per Cloud Data Fusion instance.

  * **Improved security and isolation**. By configuring a network attachment, you control which services can access your network.

  * **Simplified Cloud Data Fusion instance setup**. Create a network attachment per customer VPC only once. No need to use proxy VMs to connect to resources on the internet, peer VPCs, or on-premises.




### Key concepts

This section explains concepts involved in Private Service Connect in Cloud Data Fusion.

#### Network attachment

Network attachment is a regional resource used to authorize Cloud Data Fusion to use and establish network connections privately, for accessing resources in your VPC. For more information, see [About network attachments](https://docs.cloud.google.com/vpc/docs/about-network-attachments).

#### Shared VPC

The following is a use case for Private Service Connect interfaces with Shared VPC:

  * The network or the infra team owns the subnets in a host project. They let the application teams use these subnets from their service project.

  * The application teams own the network attachments in a service project. The network attachment defines which Cloud Data Fusion tenant projects can connect to the subnets linked to the network attachment.




You can create a network attachment in a service project. The subnets used in a network attachment can only be in the host project.

The following diagram illustrates this use case:

![Use case for Private Service Connect interfaces with Shared VPC](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/private-service-connect/psc-usecase.png)

**Figure 2.** Use case for Private Service Connect interfaces with Shared VPC

**Description of Figure 2:**

  * The network attachment is present in the service project. The network attachment uses a subnet that belongs to a Shared VPC in the host project.

  * The Cloud Data Fusion instance is present in the service project, and it uses the network attachment from the service project for establishing private connectivity.

  * The Cloud Data Fusion instance is assigned IP addresses from the subnet in the Shared VPC.




## Before you begin

  * Private Service Connect is available only in Cloud Data Fusion version 6.10.0 and later.

  * You can enable Private Service Connect only when you create a new Cloud Data Fusion instance. You cannot migrate the existing instances to use Private Service Connect.




### Pricing

Data ingress and egress through Private Service Connect is charged. For more information, see the [Private Service Connect pricing](https://docs.cloud.google.com/vpc/network-pricing#psc-network-attachment).

**Note:** Cloud Data Fusion uses Private Service Connect interfaces for design time operations, such as connection validations and preview. Therefore, this cost is expected to be low.

### Required roles and permissions

To get the permissions that you need to create a Cloud Data Fusion instance and network attachment, ask your administrator to grant you the following Identity and Access Management (IAM) roles on your project:

  * Create a Cloud Data Fusion instance: [Cloud Data Fusion Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`)
  * Create, view, and delete network attachments: [Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`)



To ensure that Cloud Data Fusion has the necessary permissions to validate the network configuration, ask your administrator to grant the [Cloud Data Fusion service agent](https://docs.cloud.google.com/data-fusion/docs/concepts/service-accounts) (of the format `service-CUSTOMER_PROJECT_NUMBER@gcp-sa-datafusion.iam.gserviceaccount.com`) the following IAM roles on your project:

  * For the VPC associated with the network attachment: [Compute Network Viewer](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkViewer) (`roles/compute.networkViewer`)

  * For Cloud Data Fusion to add its tenant project to the producer accept list of the network attachment:

    * `compute.networkAttachments.get`
    * `compute.networkAttachments.update`
    * `compute.networkAttachments.list`

The most restrictive role with these permissions is the [Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`) role. These permissions are part of the [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) (`roles/datafusion.serviceAgent`) role, which is automatically granted to the Cloud Data Fusion service agent. Therefore, no action is required unless the service agent role grant has been explicitly removed.




For more information about granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

For more information about access control options in Cloud Data Fusion, see [Access control with IAM](https://docs.cloud.google.com/data-fusion/docs/access-control).

### Create a VPC or a Shared VPC network

Ensure that you have created a [VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks) or a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#setting_up_shared_vpc).

## Configure Private Service Connect

To configure Private Service Connect in Cloud Data Fusion, you must first create a network attachment and then create a Cloud Data Fusion instance with Private Service Connect.

### Create a network attachment

The network attachment provides a set of subnetworks. To create a network attachment, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Network attachments** page:

[Go to Network attachments](https://console.cloud.google.com/net-services/psc/list/networkAttachments)

  2. Click **Create network attachment**.

  3. In the **Name** field, enter a name for your network attachment.

  4. From the **Network** list, select a VPC or a Shared VPC network.

  5. From the **Region** list, select a Google Cloud region. This region must be the same as the Cloud Data Fusion instance.

  6. From the **Subnetwork** list, select a subnetwork range.

**Note:** The provisioning of a secondary range for a subnet isn't required for Cloud Data Fusion. Each Cloud Data Fusion instance requests up to 32 IP addresses from the network attachment. Ensure that the subnet has enough IP addresses to support the number of Cloud Data Fusion instances that you plan to create.
  7. In **Connection preference** , select **Accept connections for selected projects**.

Cloud Data Fusion automatically adds the Cloud Data Fusion tenant project to the **Accepted projects** list when you create the Cloud Data Fusion instance.

**Caution:** The option **Automatically accept connections for all projects** is less secure because it allows any service to obtain IP addresses from your subnet. We don't recommend using this option.
  8. Don't add **Accepted projects** or **Rejected projects**.

  9. Click **Create network attachment**.

![Create a network attachment](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/private-service-connect/create-network-attachment.png)




### gcloud

  1. Create one or more subnetworks. For example:
         
         gcloud compute networks subnets create subnet-1 --network=network-0 --range=10.10.1.0/24 --region=REGION
         

The network attachment uses these subnetworks in the subsequent steps.

**Note:** The provisioning of a secondary range for a subnet is not required for Cloud Data Fusion. Each Cloud Data Fusion instance requests up to 32 IP addresses from the network attachment. Ensure that the subnet has enough IP addresses to support the number of Cloud Data Fusion instances that you plan to create.
  2. Create a network attachment resource in the same region as the Cloud Data Fusion instance, with the `connection-preference` property set to `ACCEPT_MANUAL`:
         
         gcloud compute network-attachments create NAME
         --region=REGION
         --connection-preference=ACCEPT_MANUAL
         --subnets=SUBNET
         

Replace the following:

     * `NAME`: the name for your network attachment.
     * `REGION`: the name of the Google Cloud region. This region must be the same as the Cloud Data Fusion instance.
     * `SUBNET`: the name of the subnet.

The output of this command is a network attachment URL of the following format:

`projects/PROJECT/locations/REGION/network-attachments/NETWORK_ATTACHMENT_ID`.

Make a note of this URL as Cloud Data Fusion needs it for connectivity.

**Caution:** Specifying `connection-preference` as `ACCEPT_AUTOMATIC` is less secure because it allows any service to obtain IP addresses from your subnet. We don't recommend using this option.



### REST API

  1. [Create a subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnets).

  2. Create a network attachment:
         
         alias authtoken="gcloud auth print-access-token"
         NETWORK_ATTACHMENT_NAME=NETWORK_ATTACHMENT_NAME
         REGION=REGION
         SUBNET=SUBNET
         PROJECT_ID=PROJECT_ID
         
         read -r -d '' BODY << EOM
         {
           "name": "$NETWORK_ATTACHMENT_NAME",
           "description": "Network attachment for private Cloud Data Fusion",
           "connectionPreference": "ACCEPT_MANUAL",
           "subnetworks": [
             "projects/$PROJECT_ID/regions/$REGION/subnetworks/$SUBNET"
           ]
         }
         EOM
         
         curl -H "Authorization: Bearer $(authtoken)" \
         -H "Content-Type: application/json" \
         -X POST   -d "$BODY" "https://compute.googleapis.com/compute/v1/projects/$PROJECT_ID/regions/$REGION/networkAttachments"
         

Replace the following:

     * `NETWORK_ATTACHMENT_NAME`: the name for your network attachment.
     * `REGION`: the name of the Google Cloud region. This region must be the same as the Cloud Data Fusion instance.
     * `SUBNET`: the name of the subnet.
     * `PROJECT_ID`: the ID of your project.



### Create a Cloud Data Fusion instance

Cloud Data Fusion uses a /25 CIDR block (128 IPs) for resources in the tenant project. This is called the unreachable or reserved range. You can use the same IP addresses in VPCs, but Cloud Data Fusion VMs won't be able to connect with your resources using this range.

**Note:** The unreachable or reserved range used by Cloud Data Fusion mustn't overlap with the primary address range of any subnet associated with the network attachment. This is to ensure that the IP addresses assigned on Private Service Connect and non-Private Service Connect interfaces of the Cloud Data Fusion VMs don't collide.

In most of the cases, this isn't an issue, as the unreachable CIDR block lies in a non-RFC 1918 range (240.0.0.0/8), by default. If you want to control the unreachable range, refer to Advanced configurations.

To create a Cloud Data Fusion instance with Private Service Connect enabled, follow these steps:

### Console

  1. In the Google Cloud console, go to the Cloud Data Fusion **Instances** page and click **Create instance**. 

[ Create an instance](https://console.cloud.google.com/data-fusion/instance-create)

  2. In the **Instance name** field, enter a name for your new instance.

  3. In the **Description** field, enter a description for your instance.

  4. From the **Region** list, select the Google Cloud region in which you want to create the instance.

  5. From the **Version** list, select `6.10` or later.

  6. Select an **Edition**. For more information about pricing for different editions, see the [Cloud Data Fusion pricing overview](https://cloud.google.com/data-fusion/pricing).

  7. Expand **Advance options** and do the following:

     1. Select **Enable private IP**.

     2. Select **Private Service Connect** as the **Connectivity type**.

     3. In the **Network attachment** section, select the network attachment that you created in Create a network attachment.

  8. Click **Create**. It takes up to 30 minutes for the instance creation process to complete.

![Create a Cloud Data Fusion instance with Private Service Connect](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/private-service-connect/cdf-with-psc.png)




### REST API

Run the following command:
    
    
    alias authtoken="gcloud auth print-access-token"
    
    EDITION=EDITION
    PROJECT_ID=PROJECT_ID
    REGION=REGION
    CDF_ID=INSTANCE_ID
    NETWORK_ATTACHMENT_ID=NETWORK_ATTACHMENT_ID
    
    read -r -d '' BODY << EOM
    {
      "description": "PSC enabled instance",
      "version": "6.10",
      "type": "$EDITION",
      "privateInstance": "true",
      "networkConfig": {
        "connectionType": "PRIVATE_SERVICE_CONNECT_INTERFACES",
        "privateServiceConnectConfig": {
          "networkAttachment": "$NETWORK_ATTACHMENT_ID"
        }
      }
    }
    EOM
    
    curl -H "Authorization: Bearer $(authtoken)" \
    -H "Content-Type: application/json" \
    -X POST   -d "$BODY" "https://datafusion.googleapis.com/v1/projects/$PROJECT_ID/locations/$REGION/instances/?instanceId=$CDF_ID"
    

Replace the following:

  * `EDITION`: the Cloud Data Fusion edition— `BASIC`, `DEVELOPER`, or `ENTERPRISE`.
  * `PROJECT_ID`: the ID of your project.
  * `REGION`: the name of the Google Cloud region. This region must be the same as the Cloud Data Fusion instance.
  * `INSTANCE_ID`: the ID of your instance.
  * `NETWORK_ATTACHMENT_ID`: the ID of your network attachment.



### Advanced configurations

To enable sharing of subnets, you can provide the same network attachment to multiple Cloud Data Fusion instances. In contrast, if you want to dedicate a subnet for a particular Cloud Data Fusion instance, then you must provide a specific network attachment, to be used by the Cloud Data Fusion instance.

**Recommended** : To apply a uniform firewall policy to all of the Cloud Data Fusion instances, use the same network attachment.

If you want to control the /25 CIDR block that is not reachable by Cloud Data Fusion, specify the `unreachableCidrBlock` property when you create the instance. For example:
    
    
    alias authtoken="gcloud auth print-access-token"
    
    EDITION=EDITION
    PROJECT_ID=PROJECT_ID
    REGION=REGION
    CDF_ID=INSTANCE_ID
    NETWORK_ATTACHMENT_ID=NETWORK_ATTACHMENT_ID
    UNREACHABLE_RANGE=UNREACHABLE_RANGE
    
    read -r -d '' BODY << EOM
    {
      "description": "PSC enabled instance",
      "version": "6.10",
      "type": "$EDITION",
      "privateInstance": "true",
      "networkConfig": {
        "connectionType": "PRIVATE_SERVICE_CONNECT_INTERFACES",
        "privateServiceConnectConfig": {
          "unreachableCidrBlock": "$UNREACHABLE_RANGE",
          "networkAttachment": "projects/$PROJECT_ID/regions/$REGION/networkAttachments/$NETWORK_ATTACHMENT_ID"
        }
      }
    }
    EOM
    
    curl -H "Authorization: Bearer $(authtoken)" \
    -H "Content-Type: application/json" \
    -X POST -d "$BODY" "https://datafusion.googleapis.com/v1/projects/$PROJECT_ID/locations/$REGION/instances/?instanceId=$CDF_ID"
    

Replace the following:

  * `EDITION`: the Cloud Data Fusion edition— `BASIC`, `DEVELOPER`, or `ENTERPRISE`.
  * `PROJECT_ID`: the ID of your project.
  * `REGION`: the name of the Google Cloud region. This region must be the same as the Cloud Data Fusion instance.
  * `INSTANCE_ID`: the ID of your instance.
  * `NETWORK_ATTACHMENT_ID`: the ID of your network attachment.
  * `UNREACHABLE_RANGE`: the unreachable range—for example, `10.0.0.0/25`.



## Security

This section describes security between Cloud Data Fusion and consumers.

### Cloud Data Fusion to consumer security

Private Service Connect interfaces support egress firewall rules to control what Cloud Data Fusion can access within your VPC. For more information, see [Limit producer-to-consumer ingress](https://docs.cloud.google.com/vpc/docs/configure-security-network-attachments#producer-to-consumer-ingress).

### Consumer to Cloud Data Fusion security

Cloud Data Fusion VMs with Private Service Connect interface block any traffic that originates from your VPC and isn't a response packet.

## Steps for connection use cases

The following sections describe connection-related use cases for private instances.

### Enable Private Google Access

To [access resources through internal IP addresses](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/network#create_a_cluster_with_internal_ip_addresses_only), Cloud Data Fusion must create the Managed Service for Apache Spark clusters and run the data pipelines in a subnet that has Private Google Access. You must enable Private Google Access for the subnet that contains the Managed Service for Apache Spark clusters.

  * If only one subnet is present in the region where the Managed Service for Apache Spark clusters are launched, then the cluster is launched in that subnet.
  * If there are multiple subnets in a region, you must configure Cloud Data Fusion to select the subnet with Private Google Access for launching Managed Service for Apache Spark clusters.

**Caution:** If Private Google Access isn't enabled on that subnet, the pipeline run fails. To specify the subnet after you create an instance, edit the compute profile.



To enable Private Google Access for the subnet, see [Private Google Access configuration](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-pga).

### Optional: Enable DNS Peering

Enable [DNS Peering](https://docs.cloud.google.com/data-fusion/docs/how-to/resolve-domain-names) in the following cases:

  * When Cloud Data Fusion connects to systems through hostnames, and not IP addresses
  * When the target system is deployed behind a load balancer, such as it does in some SAP deployments



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
