---
url: https://docs.cloud.google.com/build/docs/private-pools/set-up-private-pool-to-use-in-vpc-network/
title: Set up environment to use private pools in a VPC network \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:51:10.414334+00:00
---

# Set up environment to use private pools in a VPC network  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/private-pools/set-up-private-pool-to-use-in-vpc-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Set up environment to use private pools in a VPC network Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to set up your network environment to use private pools in a VPC network. If you're not familiar with private pools, read [Private pools overview](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview).

## Understanding the network configuration options

Private pools are hosted in a Google-owned Virtual Private Cloud network called the service producer network. When setting up a private pool, you can either choose to use the [_service producer network_](https://docs.cloud.google.com/vpc/docs/private-services-access) or set up a private connection between the service producer network and the VPC network that contains your resources.

Choose one of the following network configuration schemes depending on the needs of your organization:

  * **Use the service producer network by itself** : Use this option if:

    * you are not looking for builds to access resources within your private network
    * you want [configurable machine types and sizes](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview)

This is the default network option for creating the private pool and does not require any network setup. If you're interested in this option, proceed to [creating the private pool](https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools).

  * **Set up a private connection between the service producer network and your VPC network** : The private connection enables VM instances in your VPC network and private pools to communicate exclusively using internal IP addresses. Use this option if:

    * you want builds to access resources in your VPC network
    * you want configurable machine types and sizes



## Setting up a private connection between your VPC network and the service producer network

  1. You must have an [existing VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network) that you will use to connect to the service producer network.

  2. To use the command-line examples in this guide, install and configure the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk).

**Note:** If you've installed gcloud CLI previously, make sure you have the latest available version by running `gcloud components update`.
  3. Enable API:

###  Console 

  


Enable the Cloud Build and the Service Networking APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,servicenetworking.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/private-pools/set-up-private-pool-environment)

###  gcloud 

Enable the Cloud Build and the Service Networking APIs:
         
         gcloud services enable cloudbuild.googleapis.com servicenetworking.googleapis.com
         

  4. To ensure that has the necessary permissions to set up a private connection, ask your administrator to grant the [Compute Engine Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role to on the service account for the Google Cloud project in which the VPC network resides. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  5. In the VPC network, allocate a named internal IP range:

The IP range you specify here will be subject to [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) that are defined in the VPC network.

Cloud Build reserves the IP ranges `192.168.10.0/24` and `172.17.0.0/16` for the Docker bridge network. When allocating the IP ranges for resources in your project(s), we recommend selecting a range outside of `192.168.10.0/24` and `172.17.0.0/16` in cases when Cloud Build builders are to access these resources.

For example, the Google Kubernetes Engine control plane address range `192.168.10.96/28` wouldn't be accessible from the Cloud Build `gke-deploy` builder due to the overlap.

###  Console 

     1. Go to the VPC networks page in the Google Cloud console.

[Go to the VPC networks page](https://console.cloud.google.com/networking/networks/list)

     2. Select the VPC network that will connect to the private pool's VPC network.

     3. Select the **Private service access** tab.

     4. In the **Private service access** tab, select the **Allocated IP ranges for services** tab.

     5. Click **Allocate IP range**.

     6. Enter a **Name** and **Description** for the allocated range.

     7. Specify an **IP range** for the allocation:

        * To specify an IP address range, select **Custom** and then enter a CIDR block.
        * To specify a prefix length and let Google select an available range, select **Automatic** and then enter a prefix length. The prefix length must be `/24` or lower, such as `/22`, `/21`, etc.
**Note:** The private pool uses a default prefix length of `/24`. When configuring a private pool in the `peeredNetworkIpRange` field, you can use a higher prefix length and specify a smaller IP range.
     8. Click **Allocate** to create the allocated range.

###  gcloud 

To specify an address range and a prefix length (subnet mask), use the `addresses` and `prefix-length` flags. The prefix length must be /24 or lower, such as /22, /21, etc. For example, to allocate the CIDR block `192.168.0.0/16`, specify `192.168.0.0` for the address and `16` for the prefix length.
    
    gcloud compute addresses create RESERVED_RANGE_NAME \
          --global \
          --purpose=VPC_PEERING \
          --addresses=192.168.0.0 \
          --prefix-length=16 \
          --description=DESCRIPTION \
          --network=VPC_NETWORK
    

To specify just a prefix length (subnet mask), just use the `prefix-length` flag. When you omit the address range, Google Cloud automatically selects an unused address range in your VPC network. The following example selects an unused IP address range with a `16` bit prefix length.
    
    gcloud compute addresses create RESERVED_RANGE_NAME \
          --global \
          --purpose=VPC_PEERING \
          --prefix-length=16 \
          --description=DESCRIPTION \
          --network=VPC_NETWORK
    

Replace the placeholder values in the command with the following:

     * `RESERVED_RANGE_NAME`: a name for the allocated range, such as `my-allocated-range`.
     * `DESCRIPTION`: a description for the range, such as `allocated for my-service`.
     * `VPC_NETWORK`: the name of your VPC network, such as `my-vpc-network`.

**Note:** The private pool uses a default prefix length of `/24`. When configuring a private pool in the `peeredNetworkIpRange` field, you can use a higher prefix length and specify a smaller IP range.

  6. Create a private connection between the service producer network and your VPC network:

###  Console 

     1. Go to the VPC networks page in the Google Cloud console.

[Go to the VPC networks page](https://console.cloud.google.com/networking/networks/list)

     2. Select the VPC network that will connect to the private pool's VPC network.

     3. Select the **Private service access** tab.

     4. In the **Private service access** tab, select the **Private connections to services** tab.

     5. Click **Create connection** to create a private connection between your network and the service producer network.

     6. For the **Assigned allocation** , select the allocated range that you created in the previous step.

     7. Click **Connect** to create the connection.

###  gcloud 

     1. Create a private connection:
            
            gcloud services vpc-peerings connect \
                --service=servicenetworking.googleapis.com \
                --ranges=ALLOCATED_RANGE_NAME \
                --network=VPC_NETWORK \
                --project=PROJECT_ID
            

Replace the placeholder values in the command with the following:

        * `ALLOCATED_RANGE_NAME`: the name allocated range you created in the previous step.
        * `VPC_NETWORK`: the name of your VPC network.
        * `PROJECT_ID`: the ID of the project that contains your VPC network.

The command initiates a long-running operation, returning an operation name.

     2. Check whether the operation was successful, replacing `OPERATION_NAME` with the operation name that was returned from the previous step.
            
            gcloud services vpc-peerings operations describe \
                --name=OPERATION_NAME
            

**Warning:** If you delete this private connection, you will break all private pools that are peered to your VPC network. We recommend that you delete private pools that rely on a private connection before deleting the private connection.
  7. [OPTIONAL: Shared VPC scenario]. If you are using [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), create the allocated IP range and private connection in the host project. Typically, a network administrator in the host project must do these tasks. After the host project is set up with the private connection, VM instances in service projects can use the private connection with the service producer network. The project that hosts the VPC connection and the project that contains the private pool must be part of the same organization.

  8. [OPTIONAL: Using firewall rules]. If you're creating an [ingress firewall rule](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) in the VPC network, specify the same IP range that you allocate here in the **source filter** for the ingress rule.




## What's next

  * Learn how to [create and manage private pools](https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
