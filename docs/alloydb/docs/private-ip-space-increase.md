---
url: https://docs.cloud.google.com/alloydb/docs/private-ip-space-increase/
title: Increase private services access address space \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:42.132726+00:00
---

# Increase private services access address space  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/private-ip-space-increase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Increase private services access address space Stay organized with collections  Save and categorize content based on your preferences. 

To resolve an IP address shortage when creating an AlloyDB for PostgreSQL cluster or instance in a region that uses private services access, you can increase the allocated IP address space in your Virtual Private Cloud (VPC) network.

When you create an AlloyDB cluster or instance in a region that doesn't yet have any clusters or instances, AlloyDB creates a `/24` subnet in that region. If the existing IP address space available to AlloyDB is not large enough to create the subnet, your attempt to create the cluster or instance fails until you allocate additional IP address space.

## Before you begin

  * The Google Cloud project you are using must have been [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#before-you-begin). 
  * You must have one of these IAM roles in the Google Cloud project you are using: 
    * `roles/alloydb.admin` (the AlloyDB Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)

If you don't have any of these roles, contact your Organization Administrator to request access.

  * To increase the IP address range, you also must have these Identity and Access Management (IAM) permissions: 
    * `compute.networks.list`
    * `compute.addresses.create`
    * `compute.addresses.list`
    * `servicenetworking.services.addPeering`



## Procedure

To increase the AlloyDB IP address space, perform two operations:

  * Create an additional allocated IP address range in your VPC network.
  * Add the additional address range to the existing private services access connection in your VPC network.



###  Console 

  1. Go to the **VPC networks** page in the Google Cloud console.

[Go to the VPC networks page](https://console.cloud.google.com/networking/networks/list)

  2. Select the project where your VPC network resides.

  3. Select the VPC network that contains your existing private services access connection.

  4. Select the **Private services access** tab.

  5. In the **Private services access** tab, select the **Allocated IP ranges for services** tab.

  6. Click **Allocate IP range**.

  7. Enter a **Name** and **Description** for the allocated range.

  8. Specify an **IP range** for the allocation:

**Note:** To provide sufficient address space for AlloyDB, specify a prefix length of `16` or less.
     * To specify an IP address range, select **Custom** and then enter a CIDR block, such as `192.168.0.0/16`.
     * To specify a prefix length and let Google select an available range, select **Automatic** and then enter a prefix length, such as `16`.
  9. Click **Allocate** to create the allocated range.

  10. In the **Private services access** tab, select the **Private connections to services** tab.

  11. Click **servicenetworking-googleapis-com**.

  12. In the **Update a private connection** dialog, click the **Assigned allocation** box and then select the additional allocated IP range you created earlier.

  13. Click **Update** to update the connection.




###  gcloud 

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

  1. Use the `gcloud config set project` command to set the default project to the one where your VPC network resides:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with the ID of the project where your VPC network resides.

  2. Use the `gcloud compute addresses create` command to create an additional allocated IP address range.

**Note:** To provide sufficient address space for AlloyDB, specify a prefix length of `16` or less.
     * To specify an address range and a prefix length (subnet mask), use the `--addresses` and `--prefix-length` flags. For example, to allocate the CIDR block `192.168.0.0/16`, specify `192.168.0.0` for the address and `16` for the prefix length:
           
           gcloud compute addresses create RESERVED_RANGE_NAME \
               --global \
               --purpose=VPC_PEERING \
               --addresses=192.168.0.0 \
               --prefix-length=16 \
               --description="DESCRIPTION" \
               --network=VPC_NETWORK
           

     * To specify only a prefix length (subnet mask), use the `--prefix-length` flag. When you omit the address range, Google Cloud automatically selects an unused address range in your VPC network. The following example selects an unused IP address range with a `16`-bit prefix length:
           
           gcloud compute addresses create RESERVED_RANGE_NAME \
               --global \
               --purpose=VPC_PEERING \
               --prefix-length=16 \
               --description="DESCRIPTION" \
               --network=VPC_NETWORK
           

Replace the following placeholders with relevant values:

     * `RESERVED_RANGE_NAME`: a name for the allocated range, such as `additional-alloydb-range`.

     * `DESCRIPTION`: a description for the range, such as `allocated to extend AlloyDB range`.

     * `VPC_NETWORK`: the name of your VPC network, such as `my-vpc-network`.

The following example creates an additional allocated IP range in the `default` VPC network:
    
    gcloud compute addresses create additional-alloydb-range \
        --global \
        --purpose=VPC_PEERING \
        --prefix-length=16 \
        --description="allocated to extend AlloyDB range" \
        --network=default
    

  3. Use the `gcloud services vpc-peerings list` command to get a list of IP ranges already allocated to your private services access connection:
         
         gcloud services vpc-peerings list \
             --service=servicenetworking.googleapis.com \
             --network=VPC_NETWORK
         

Replace `VPC_NETWORK` with the name of your VPC network, such as `my-vpc-network`.

The list of IP ranges already allocated to your private services access connection appears after `reservedPeeringRanges`.

  4. Use the `gcloud services vpc-peerings update` command to add the additional address range to the private services access connection:
         
         gcloud services vpc-peerings update \
             --service=servicenetworking.googleapis.com \
             --ranges=RESERVED_RANGE_NAME,EXISTING_RANGES_LIST \
             --network=VPC_NETWORK
         

Replace the following placeholders with relevant values:

     * `RESERVED_RANGE_NAME`: the name of the additional allocated IP address range you created.

     * `EXISTING_RANGES_LIST`: a comma-separated list of the IP address ranges already allocated to the private services access connection.

     * `VPC_NETWORK`: the name of your VPC network.

The command initiates a long-running operation, returning an operation name.

  5. Check whether the operation was successful:
         
         gcloud services vpc-peerings operations describe OPERATION_NAME
         

Replace `OPERATION_NAME` with the operation name that was returned from the previous step.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
