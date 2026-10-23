---
url: https://docs.cloud.google.com/alloydb/docs/configure-connectivity/
title: Enable private services access \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:15.252894+00:00
---

# Enable private services access  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/configure-connectivity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Enable private services access Stay organized with collections  Save and categorize content based on your preferences. 

To let your AlloyDB for PostgreSQL instances communicate privately with resources in your Virtual Private Cloud (VPC) network and with Google-managed services, you can allocate VPC IP address ranges and create a private services access connection. For an overview of how AlloyDB uses private services access to let its internal resources communicate with each other, see [About private services access](https://docs.cloud.google.com/alloydb/docs/about-private-services-access).

To create a private services access configuration in a VPC network that resides in the same Google Cloud project as your AlloyDB cluster, you perform two operations:

  * Create an allocated IP address range in the VPC network.

  * Create a private connection between the VPC network and the underlying Google Cloud VPC network. You can also configure private services access to connect your AlloyDB cluster to resources residing in a separate Google Cloud project. To do this, you must merge the two projects' VPC networks [using Shared VPC](https://docs.cloud.google.com/alloydb/docs/about-private-services-access#shared).




### Before you begin

  * The Google Cloud project you are using must have been [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#before-you-begin). 
  * You must have one of these IAM roles in the Google Cloud project you are using: 
    * `roles/alloydb.admin` (the AlloyDB Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)

If you don't have any of these roles, contact your Organization Administrator to request access.

  * To create a private services access configuration, you also must have these IAM permissions: 
    * `compute.networks.list`
    * `compute.addresses.create`
    * `compute.addresses.list`
    * `servicenetworking.services.addPeering`



## Create VPC IP address ranges

###  Console 

  1. Go to the VPC networks page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Select the project where AlloyDB and the VPC network reside.

  3. Click the name of VPC network that you want to use for private services access.

**Note:** The default VPC network is created for most consumer projects, and is best suited if you're beginning your experimentation with AlloyDB.
  4. On the **VPC network details** page, scroll through the list of tabs to the **Private services access** tab and then click it.

  5. In the **Private services access** tab, click the **Allocated IP ranges for services** tab.

  6. Click **Allocate IP range**.

  7. In the **Name** and **Description** fields, enter a name and a description for the allocated range.

  8. Specify an **IP range** value for the allocation:

     * To specify an IP address range, click **Custom** , and then enter a CIDR block, such as `192.168.0.0/16`.

To provide sufficient address space for AlloyDB, we recommend a prefix length of `16` or less.

     * To specify a prefix length and let Google select an available range, follow these steps:

       1. Click **Automatic**.

       2. Enter a prefix length as a plain number, such as `16`.

  9. Click **Allocate** to create the allocated range.

  10. In the **Private services access** tab, click the **Private connections to services** tab.

  11. Click **Create connection** to create a private connection between your network and a service producer.

  12. Make sure that **Google Cloud** is the **Connected service producer**.

  13. For the **Assigned allocation** , select the allocated IP range you created earlier.

  14. Click **Connect** to create the connection.




###  gcloud 

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

  1. Use the [`gcloud config set`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set) command to set the default project to the one where AlloyDB and the VPC network reside.
         
         gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with the ID of the project where AlloyDB and the VPC network reside.

  2. Use the [`gcloud compute addresses create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) command to create an allocated IP address range.

To provide sufficient address space for AlloyDB, we recommend a prefix length of `16` or less.

     * To specify an address range and a prefix length (subnet mask), use the `--addresses` and `--prefix-length` flags. For example, to allocate the CIDR block `192.168.0.0/16`, specify `192.168.0.0` for the address and `16` for the prefix length.
           
           gcloud compute addresses create RESERVED_RANGE_NAME \
                   --global \
                   --purpose=VPC_PEERING \
                   --addresses=192.168.0.0 \
                   --prefix-length=16 \
                   --description="DESCRIPTION" \
                   --network=VPC_NETWORK

Replace the following:

       * `RESERVED_RANGE_NAME`: a name for the allocated range, such as `my-allocated-range`

       * `DESCRIPTION`: a description for the range, such as `allocated for my-service`

       * `VPC_NETWORK`: the name of your VPC network, such as `my-vpc-network`. In case of Shared VPC network, set to the fully qualified path of the VPC network—for example, `projects/cymbal-project/global/networks/shared-vpc-network`.

     * To specify only a prefix length (subnet mask), use the `--prefix-length` flag. When you omit the address range, Google Cloud automatically selects an unused address range in your VPC network.

The following example selects an unused IP address range with a `16` bit prefix length:
           
           gcloud compute addresses create RESERVED_RANGE_NAME \
                   --global \
                   --purpose=VPC_PEERING \
                   --prefix-length=16 \
                   --description="DESCRIPTION" \
                   --network=VPC_NETWORK

The following example creates a private connection to Google so that the VM instances in the `default` VPC network can use private services access to reach Google services that support it.
    
    gcloud compute addresses create google-managed-services-default \
            --global \
            --purpose=VPC_PEERING \
            --prefix-length=16 \
            --description="peering range for Google" \
            --network=default

  3. Use the [`gcloud services vpc-peerings connect`](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/connect) command to create a private connection.
         
         gcloud services vpc-peerings connect \
                 --service=servicenetworking.googleapis.com \
                 --ranges=RESERVED_RANGE_NAME \
                 --network=VPC_NETWORK

Replace the following:

     * `RESERVED_RANGE_NAME`: the name of the allocated IP address range you created

     * `VPC_NETWORK`: the name of your VPC network

The command initiates a long-running operation, returning an operation name.

  4. Check whether the operation was successful.
         
         gcloud services vpc-peerings operations describe \
                 --name=OPERATION_NAME

Replace `OPERATION_NAME` with the operation name that was returned from the previous step.




## What's next

  * [Create a cluster and its primary instance.](https://docs.cloud.google.com/alloydb/docs/cluster-create)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
