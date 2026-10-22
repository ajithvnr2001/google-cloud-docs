---
url: https://docs.cloud.google.com/filestore/docs/configure-psc/
title: Create a Filestore instance with Private Service Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:50:59.700090+00:00
---

# Create a Filestore instance with Private Service Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/configure-psc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Create a Filestore instance with Private Service Connect Stay organized with collections  Save and categorize content based on your preferences. 

The following guide shows you how to configure your Filestore instances to use Private Service Connect with NFSv3 or NFSv4.1 file system protocols.

## About Private Service Connect

[Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) allows consumers to access managed services privately from inside their VPC network. Private Service Connect requires the consumer to provision a single internal IP address in its own Virtual Private Cloud to create a Private Service Connect endpoint, instead of allocating an entire IP address range to facilitate the connection. This single IP address is all that's required from the consumer's IP space to access the Filestore instance.

For shared Shared VPC configurations, where the Private Service Connect [endpoint](https://docs.cloud.google.com/vpc/docs/private-service-connect#endpoints) is provisioned in the VPC host project, the [service connection policy scope](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies#custom-scope) must allow the host project.

### Connection policies

To create a [Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/private-service-connect#endpoints) on the consumer target network, you must create a [service connection policy](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies) in your project. Creating such a connection policy allows separating the permissions for creating a Filestore instance and allocating networking resources, such as Private Service Connect resources and IP addresses for them. Creating a service connection policy enables the automatic creation of an endpoint in the subnet with a private IP address.

## Create a Filestore instance that uses Private Service Connect

Create a Filestore instance that uses [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) for network connections.

### Before you begin

  1. Verify if you have enough quota. Instance quota ranges by the region location and service tier you want to use. To increase available quota, you must submit a [quota increase request](https://docs.cloud.google.com/filestore/docs/requesting-quota-increases).
  2. Ensure [you have enabled the following APIs](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api#enabling_an_api):

     * [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1)
     * [Network Connectivity API](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest)
     * [Service Consumer Management API](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest)



### Create a Filestore instance

Create a Filestore instance using Google Cloud console or Google Cloud CLI.

###  Google Cloud console 

  1. In the Google Cloud console, go to the Filestore **Instances** page.

[Go to Instances](https://console.cloud.google.com/filestore/instances)

  2. Click **Create instance**.

  3. Specify the basic parameters of the instance:

     * In the **Instance ID** field, type the name you want to use for your Filestore instance.
     * For **Instance type** , select **Regional** or **Zonal** [service tier](https://docs.cloud.google.com/filestore/docs/service-tiers).

To create an enterprise instance, you must use Filestore API or Google Cloud CLI.

     * For **Capacity** , first select the capacity range, and then enter the capacity you want to use. You must use a value between 1 TB and 10 TB, in increments of 256 GiB (0.25 TiB).

     * For **Region** , use the list to select the region you want to deploy your instance in.

     * For **Protocol** , select **NFSv3** or **NFSv4.1** , depending on the [network protocol](https://docs.cloud.google.com/filestore/docs/about-supported-protocols) you want to use.

     * For **Network IP stack type** select **IPv4** or **IPv6**. Filestore with Private Service Connect IPv6 support lets you choose either an IPv4 or IPv6 endpoint per service attachment. If you select IPv6 and you also want to configure [access control](https://docs.cloud.google.com/filestore/docs), the IP address or range field will be validated for IPv6 CIDR notation. 

     * In the **VPC Network** field, select the network you want to use for the Filestore instance and NFS clients. The selected network must have a valid [service connection policy](https://docs.cloud.google.com/vpc/docs/about-service-connection-policies) to connect with the instance using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect). If such a policy doesn't exist, you must create one. Use the following instructions to create a policy.

#### How to create a service connection policy

When creating a Filestore instance you must either use a VPC network that already has a connection policy in place or create the connection policy as part of the instance creation workflow. This section explains how to create a service connection policy for the VPC network.

       1. In **VPC Network** , select the network. If the connection policy doesn't exist for the selected network, click **Create service connection policy**.
       2. In the **Policy name** field, add the name for the service connection policy.
       3. Optional: In the **Description** field provide a short description of your policy.
       4. The **Source service scope** and **Target endpoints scope** fields are populated with information you provided when creating the instance.
       5. In the **Subnetworks** field, select [subnets](https://docs.cloud.google.com/vpc/docs/subnets) used for the Filestore [service endpoints](https://docs.cloud.google.com/vpc/docs/private-service-connect#endpoints). Subnets are IP address ranges the services can use to access the Filestore instance. For more information on using subnets with Private Service Connect, see [Purposes of subnets](https://docs.cloud.google.com/vpc/docs/subnets#purpose)
       6. Optional: In the **Connection limit** field, The limit determines how many endpoints can be created by using this connection policy. If omitted, there is no limit.
       7. Click **Create policy** to finish. Continue to create the instance or review your policy in Private Service Connect.

     * In the **File share name** field, enter the name of the NFS file share that is served from the instance.

  4. Click **Create** to create the instance.




###  gcloud 

  1. If you already have the gcloud CLI installed, you can update it:
         
         gcloud components update
         

  2. [Create](https://docs.cloud.google.com/filestore/docs/\(/sdk/gcloud/reference/filestore/instances/create\)) a Filestore zonal, regional, or enterprise instance:
         
         gcloud filestore instances create INSTANCE-ID \
          --description="DESCRIPTION" \
          --region=LOCATION \
          --tier=TIER \
          --protocol=PROTOCOL \
          --file-share=name="FILE_SHARE_NAME",capacity=CAPACITY \
          --network=name="VPC_NETWORK_NAME",connect-mode=CONNECT_MODE,address-mode=ADDRESS_MODE,psc-endpoint-project=PSC_ENDPOINT_PROJECT,psc-requested-ip-address=PSC_REQUESTED_IP_ADDRESS \
          --project=CONSUMER_PROJECT_ID
         

Where:

     * INSTANCE_ID is the instance ID of the Filestore instance that you want to create. See [Name your instance](https://docs.cloud.google.com/filestore/docs/creating-instances#name_your_instance).
     * DESCRIPTION is a description for the instance you want to use.
     * LOCATION is the location where you want the Filestore instance to reside.
     * TIER is the [service tier](https://docs.cloud.google.com/filestore/docs/service-tiers) you want to use. It can be zonal, regional or enterprise.
     * PROTOCOL is `NFS_v3` or `NFS_v4_1`.
     * FILE_SHARE_NAME is the name you specify for the NFS file share that is served from the instance.
     * CAPACITY is the size you want for the file share, between 1 TiB to 10 TiB.
     * VPC_NETWORK_NAME is the name of the [VPC network](https://docs.cloud.google.com/filestore/docs/creating-instances#selecting_vpc_network) you want the instance to use. If you want to specify a Shared VPC from a service project, you must specify the fully-qualified network name, in the following format:
           
           projects/HOST_PROJECT_ID/global/networks/SHARED_VPC_NAME
           

You can't specify a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) as the VPC_NETWORK_NAME value. If necessary, create a new VPC network to use by following the instructions in [Create an auto mode VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-auto-network).

     * CONNECT_MODE is `PRIVATE_SERVICE_CONNECT`.

     * ADDRESS_MODE is the internet protocol version for which the instance has IP address assigned (`MODE_IPV4` or `MODE_IPV6`).

     * PSC_ENDPOINT_PROJECT is an optional name of the service project, where Private Service Connect endpoint is created. You can specify PSC_ENDPOINT_PROJECT if you are using Private Service Connect with Shared VPC. For more information, see [Create an instance on a Shared VPC network in service projects](https://docs.cloud.google.com/filestore/docs/shared-vpc).

     * PSC_REQUESTED_IP_ADDRESS is an optional IPv4 or IPv6 address that the instance uses when the Private Service Connect endpoint is created. The IP address must be within the subnet range configured in the service connection policy. If you don't specify an IP address, one is automatically allocated.

     * CONSUMER_PROJECT_ID is the project ID of the project that contains the Filestore instance.




### Example

The following command creates an instance with the following characteristics:

  * Instance ID is `my-instance`.
  * Project is `my-project`.
  * Region is `us-central1`.
  * Tier is `REGIONAL`.
  * File share name is `my_vol`.
  * Capacity is `1024`.
  * VPC network is `default`.
  * Protocol is `NFS_v4_1`.
  * Connect mode is `PRIVATE_SERVICE_CONNECT`.
  * Address mode is `MODE_IPV4`.


    
    
    gcloud filestore instances create my-instance \
        --project="my-project" \
        --region=us-central1 \
        --tier=REGIONAL \
        --protocol=NFS_v4_1 \
        --file-share=name="my_vol",capacity=1024 \
        --network=name=projects/host/global/networks/default,connect-mode=PRIVATE_SERVICE_CONNECT,address-mode=MODE_IPV4
    

## What's next

  * [Edit a Filestore instance](https://docs.cloud.google.com/filestore/docs/editing-instances)
  * [Create an instance on a Shared VPC network in service projects](https://docs.cloud.google.com/filestore/docs/shared-vpc)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
