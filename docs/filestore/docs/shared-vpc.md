---
url: https://docs.cloud.google.com/filestore/docs/shared-vpc/
title: Create an instance on a Shared VPC network in service projects \u00a0|\u00a0 Filestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:20.595419+00:00
---

# Create an instance on a Shared VPC network in service projects  |  Filestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/shared-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Guides ](https://docs.cloud.google.com/filestore/docs/overview)



Send feedback 

#  Create an instance on a Shared VPC network in service projects Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial walks you through the process of creating a Filestore instance on a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) network from a service project. 

You can create Filestore instances on a Shared VPC network in either the host project or one of its associated service projects. When creating an instance in the host project, you can select the Shared VPC network as normal and service project clients can connect to the instance. However, if you want to create the instance in a service project, you must first enable private services access on the Shared VPC network from the host project.

## Objectives

  * Enable [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) on the Shared VPC network.
  * Create an instance on the Shared VPC network.
  * Mount the instance.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [ Filestore](https://docs.cloud.google.com/filestore/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  2. Create a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc) with a host project and a connected service project.
  3. Enable the Filestore and Service Networking APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=file.googleapis.com,servicenetworking.googleapis.com)




## Enable private service access on the Shared VPC network

To create a Filestore instance in a service project that uses a Shared VPC network, the Shared VPC network must have [private services access (PSA)](https://docs.cloud.google.com/vpc/docs/private-services-access) enabled. See [Configuring a reserved IP address range](https://docs.cloud.google.com/filestore/docs/creating-instances#configure_a_reserved_ip_address_range) for specific Filestore requirements.

#### Check if private service access is enabled for the Shared VPC network

Check if private service access is already enabled for the Shared VPC network using one of the following methods:

###  Google Cloud console 

  1. In the Google Cloud console, go to the Filestore Instances page.

[Go to the Filestore instances page](https://console.cloud.google.com/filestore/instances)

  2. Click **Create Instance**.

  3. Select the Shared VPC network that you want to use.

  4. Click **Advanced network options**.

  5. The **Private services access connection** section indicates whether private services access is enabled.




###  gcloud CLI 

Run the following [`services vpc-peerings list`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/vpc-peerings/list) command:
    
    
    gcloud beta services vpc-peerings list \
        --network=SHARED_VPC_NAME \
        --project=HOST_PROJECT_ID
    

Replace the following:

  * SHARED_VPC_NAME with the name of the Shared VPC network that you want to use for your Filestore instance.
  * HOST_PROJECT_ID with the project ID of the host project that contains the Shared VPC network.



If private service access is already enabled, the response shows that a peering is established for `servicenetworking-googleapis-com`:
    
    
    network: projects/PROJECT_NUMBER/global/networks/SHARED_VPC_NAME
    peering: servicenetworking-googleapis-com
    reservedPeeringRanges: RANGES
    

If private services access is enabled for the Shared VPC network, you can [start creating Filestore instances](https://docs.cloud.google.com/filestore/docs/shared-vpc#create_a_instance_on_the_network) on it. Otherwise, you must first enable private service access.

#### Enable private services access

You must have the Owner (`roles/owner`), Editor (`roles/editor`), or Network Management Admin (`roles/networkmanagement.admin`) role to create allocated IP address ranges and manage private connections. If you do not have these privileges, contact your network administrator. For more information, see [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

Enable private services access on a Shared VPC network using one of the following methods:

###  Google Cloud console 

#### Reserve an IP address range in the Shared VPC network for Google managed services

  1. Go to the VPC networks page in the Google Cloud console.

[Go to the VPC networks page](https://console.cloud.google.com/networking/networks/list)

  2. Select the host project that contains the Shared VPC network you want to use.

  3. Click the name of the Shared VPC network that you want to create your Filestore instance on.

  4. Select the **Private service connection** tab.

  5. In the **Private service connection** tab, select the **Allocated IP ranges for services** tab.

  6. Click **Allocate IP range** and configure it as follows:

     * **Name** : `google-service-range`
     * **Description** : `Peering range for Google managed services`
     * **IP range** :

       * Select **Automatic**.
       * In the text field, enter `20` for the prefix. This range is used by all Google Cloud managed services, so in practice, you may need something larger. Basic-tier instances require a prefix of /29 and enterprise-tier, zonal and regional-tier instances with a higher capacity range (previously high scale SSD), and zonal and regional-tier instances with a lower capacity range require a /26 prefix.
  7. Click **Allocate** to create the allocated range.




#### Create a private connection for the Shared VPC network and the Google-managed services network

  1. Go to the VPC networks page in the Google Cloud console.

[Go to the VPC networks page](https://console.cloud.google.com/networking/networks/list)

  2. Select the host project that contains the Shared VPC network you want to use.

  3. Click the name of the Shared VPC network that you want to create your Filestore instance on.

  4. Select the **Private services access** tab.

  5. In the **Private services access** tab, select the **Private connections to services** tab.

  6. Click **Create connection**.

  7. For the **Assigned allocation** , select `google-service-range`.

  8. Click **Connect** to create the connection.




###  gcloud CLI 

  1. Reserve an IP address range in the Shared VPC network for Google managed services by running the following [`compute addresses create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) command:
         
         gcloud compute addresses create google-service-range \
             --global \
             --purpose=VPC_PEERING \
             --prefix-length=PREFIX \
             --description="Peering range for Google managed services" \
             --network=SHARED_VPC_NAME \
             --project=PROJECT_ID
         

Replace the following:

     * PREFIX with a prefix length. Basic-tier instances require a /29 prefix and zonal-tier instances require a /26 prefix. However, this range is used by all Google Cloud-managed services. If you plan on using multiple Filestore instances or other Google Cloud-managed services, then you need a larger prefix, for example, /20.
     * SHARED_VPC_NAME with the name of the Shared VPC network that you want to create your Filestore instance on.
     * PROJECT_ID with the project ID of the host project that contains the Shared VPC network.
  2. Create a private connection for the Shared VPC network and the Google managed services network by running the [`services vpc-peerings connect`](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/connect) command:
         
         gcloud services vpc-peerings connect \
             --service=servicenetworking.googleapis.com \
             --ranges=google-service-range \
             --network=SHARED_VPC_NAME \
             --project=HOST_PROJECT_ID
         

Replace the following:

     * SHARED_VPC_NAME with the name of the Shared VPC network that you want to create your Filestore instance on.
     * HOST_PROJECT_ID with the project ID of the host project that contains the Shared VPC network.

The command initiates a long-running operation and returns an operation name.

  3. Check whether the operation succeeded using the [`services vpc-peerings operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/operations/describe) command:
         
         gcloud services vpc-peerings operations describe \
             --name=OPERATION_NAME
         

Replace OPERATION_NAME with the operation name that was returned from the previous step.




For more information on allocating IP address ranges and creating private connections, see [Configuring private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access).

### Optional: Enable VPC Service Controls

Once private services access is enabled, you can optionally enable the [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview). To do so, run the [`services vpc-peerings enable-vpc-service-controls`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/services/vpc-peerings/enable-vpc-service-controls) command:
    
    
    gcloud beta services vpc-peerings enable-vpc-service-controls \
        --network=SHARED_VPC_NAME \
        --project=HOST_PROJECT_ID \
        --service=servicenetworking.googleapis.com
    

Replace the following:

  * SHARED_VPC_NAME with the name of the Shared VPC network that you want to create your Filestore instance on.
  * HOST_PROJECT_ID with the project ID of the host project that contains the Shared VPC network.



For more information on using Filestore with VPC Service Controls, see [Securing instances with a service perimeter](https://docs.cloud.google.com/filestore/docs/vpc-sc).

## Create a Filestore instance on the Shared VPC network

Once your Shared VPC network has private services access enabled, you can start creating Filestore instances on it from a service project.

###  Google Cloud console 

  1. In the Google Cloud console, go to the Filestore Instances page.

[Go to the Filestore instances page](https://console.cloud.google.com/filestore/instances)

  2. Click **Create Instance** and configure the instance as follows:

     * Set **Instance ID** to `nfs-server`.
     * Set **Instance type** to **Basic**.
     * Set **Storage type** to **HDD**.
     * Set **Allocate capacity** to 1`TB`.
     * Set **Region** to **us-central1** and **Zone** to **us-central1-c**.
     * Set **VPC network** to the Shared VPC network, which shows up in the format "projects/HOST_PROJECT_ID/global/networks/SHARED_VPC_NAME".
     * Set **File share name** to `vol1`.
     * Set **Allocated IP range** to **Use an automatically allocated IP range**.
     * Set **Access controls** to **Grant access to all clients**.
  3. Click **Create**.




###  gcloud CLI 

Run the following [`instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/create) command:
    
    
    gcloud filestore instances create nfs-server \
        --project=SERVICE_PROJECT_ID \
        --zone=us-central1-c \
        --tier=BASIC_HDD \
        --file-share=name="vol1",capacity=1TiB \
        --network=name="projects/HOST_PROJECT_ID/global/networks/SHARED_VPC_NAME",connect-mode=PRIVATE_SERVICE_ACCESS
    

Replace the following:

  * SERVICE_PROJECT_ID with the project ID of the service project that you want to create a Filestore instance in.
  * HOST_PROJECT_ID with the project ID of the host project that contains the Shared VPC network.
  * SHARED_VPC_NAME with the name of the Shared VPC network that you want to create your Filestore instance on.



### Optional: Import subnet routes

If your [Filestore instances use public IPs (non-RFC 1918 IP addresses)](https://docs.cloud.google.com/filestore/docs/networking#ip_resource_requirements), and if electing to [enable PSA](https://docs.cloud.google.com/filestore/docs/shared-vpc#enable_private_service_access_on_the_network), you must import the instance's public IP subnet routes into the Shared VPC network by updating the service networking VPC peering to allow importing of subnet routes with public IPs. For more information, see [Update a peering connection](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#update-peer-connection).

## Mount your instance on a service project client

Once you create a Filestore instance on a shared VPC network, you can mount that instance to any client that's on the same network. For instructions on mounting, see [Mounting file shares on Compute Engine clients](https://docs.cloud.google.com/filestore/docs/mounting-fileshares).

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the Filestore instance

###  Google Cloud console 

  1. In the Google Cloud console, go to the Filestore Instances page.

[Go to the Filestore instances page](https://console.cloud.google.com/filestore/instances)

  2. Click the **`nfs-server`** instance ID to open the instance details page.

  3. Click **Delete** _delete_.

  4. When prompted, type the instance ID.

  5. Click **Delete**.




###  gcloud CLI 

Delete the `nfs-server` instance using the [`instances delete`](https://docs.cloud.google.com/sdk/gcloud/reference/filestore/instances/delete) command:
    
    
    gcloud filestore instances delete nfs-server --zone=us-central1-c
    

## What's next

  * Learn how to [copy data to the mounted file share](https://docs.cloud.google.com/filestore/docs/copying-data).
  * Learn how to [mount file shares on clients in a remote network](https://docs.cloud.google.com/filestore/docs/remote-mounting).
  * [Troubleshoot common Filestore issues](https://docs.cloud.google.com/filestore/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
