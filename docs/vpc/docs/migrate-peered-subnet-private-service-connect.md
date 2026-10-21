---
url: https://docs.cloud.google.com/vpc/docs/migrate-peered-subnet-private-service-connect/
title: Migrate a service subnet from peering to Private Service Connect \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:16:01.613581+00:00
---

# Migrate a service subnet from peering to Private Service Connect  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/migrate-peered-subnet-private-service-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate a service subnet from peering to Private Service Connect

This document describes how service producers can [migrate their peering-based services to Private Service Connect](https://docs.cloud.google.com/vpc/docs/migrate-peered-subnet-private-service-connect) and preserve the IP address that is used to access the service. This migration process requires that all resources that are connected to a given subnet must be migrated at the same time.

The migration process is initiated by the service producer, but involves tasks that are completed by both the producer and consumer. Google-managed services can use a [service agent](https://docs.cloud.google.com/iam/docs/service-agents) to perform tasks on behalf of the consumer. The migration involves a downtime and a change in pricing for both the producer and the consumer.

Each service producer determines whether and when they are going to migrate to Private Service Connect. To learn whether a service producer is migrating from VPC Network Peering to Private Service Connect, check the service documentation or contact the service producer.

## Before you begin

  * Make sure that you understand the [migration process](https://docs.cloud.google.com/vpc/docs/about-migrating-peering-services-private-service-connect), including [considerations for migration](https://docs.cloud.google.com/vpc/docs/about-migrating-peering-services-private-service-connect#considerations).
  * Make sure that you understand the [pricing for Private Service Connect consumers and producers](https://docs.cloud.google.com/vpc/docs/about-migrating-peering-services-private-service-connect#pricing).
  * Make sure that you are familiar with [publishing a service through Private Service Connect](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services).
  * Make sure that you have the [required permissions](https://docs.cloud.google.com/vpc/docs/about-migrating-peering-services-private-service-connect#peer-migration-subnet).



## Deploy the service by using Private Service Connect

Create a new VPC network, deploy service resources in the network, and [publish the service through Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer).

When you create the load balancer for the service, use a different IP address than the one that was previously used by the load balancer. The original IP address is needed later to create the endpoint.

When you publish a service, you create a service attachment. The service attachment URI is also needed later to create the endpoint.

## Shut down the peering-based service

To shut down the peering-based service, you must create an internal range to reserve the service's IP address range before you delete the producer subnet.

### Create an internal range

Before you delete the producer subnet, create an internal range to prevent the subnet's IP address range from being reused by other subnets in either the producer or consumer network.

For more information about this internal range, see [Internal ranges for migration](https://docs.cloud.google.com/vpc/docs/about-migrating-peering-services-private-service-connect#internal-range).

### gcloud

Use the [`internal-ranges create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create).
    
    
    gcloud network-connectivity internal-ranges create RANGE_NAME \
        --project=PRODUCER_PROJECT_ID \
        --ip-cidr-range=CIDR_RANGE \
        --network=PRODUCER_NETWORK_NAME \
        --usage=FOR_MIGRATION \
        --migration-source=PRODUCER_SUBNET_URI \
        --migration-target=CONSUMER_SUBNET_URI
    

Replace the following:

  * `RANGE_NAME`: the name of the new internal range.
  * `PRODUCER_PROJECT_ID`: the ID of the producer project.
  * `CIDR_RANGE`: the CIDR range to allocate to the new internal range.
  * `PRODUCER_NETWORK_NAME`: the name of the network to create the internal range in.
  * `PRODUCER_SUBNET_URI`: the URI of the producer subnet that contains the load balancer for the service.
  * `CONSUMER_SUBNET_URI`: the URI of the intended consumer subnet. This subnet does not exist at the time you run this command.



### Delete the peering producer subnet

You must delete all resources in the producer subnet before you can delete the subnet—for example, virtual machine (VM) instances, forwarding rules, instance groups, health checks, and reserved IP addresses. After you have deleted the resources, you can [delete the subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#deleting_subnets).

## Create consumer resources

Work with the service consumer to create the following resources in their VPC network. The resources can be created manually, or for Google-managed services, can be automated through a [service agent](https://docs.cloud.google.com/iam/docs/service-agents).

### Create a peer migration subnet

Create a peer migration subnet in the consumer's VPC network to provide the IP address for the Private Service Connect endpoint. The subnet has the purpose `PEER_MIGRATION` which prevents the subnet from being used for resources other than Private Service Connect endpoints.

For more information, see [Peer migration subnets](https://docs.cloud.google.com/vpc/docs/about-migrating-peering-services-private-service-connect#peer-migration-subnet).

### Console

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of a VPC network to show its **VPC network details** page.

  3. Click the **Subnets** tab.

  4. Click **Add subnet**. In the panel that appears:

     1. Provide a name.
     2. Select a region.
     3. In the **Purpose** section, select **Peer migration**.
     4. For **IP stack type** , select **IPv4 (single-stack)**.
     5. Enter the IPv4 address range to allocate to the new subnet. This range must match the CIDR range of the internal range.

If you select a range that is not an RFC 1918 address, confirm that the range doesn't conflict with an existing configuration. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).

  5. Click **Add**.




### gcloud

Use the [`networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
    
    
    gcloud compute networks subnets create CONSUMER_SUBNET \
        --purpose=PEER_MIGRATION \
        --project=CONSUMER_PROJECT \
        --network=CONSUMER_NETWORK \
        --range=CIDR_RANGE \
        --region=REGION
    

Replace the following:

  * `CONSUMER_SUBNET`: the name of the consumer subnet
  * `CONSUMER_PROJECT`: the ID of the consumer project
  * `CONSUMER_NETWORK`: the name of the consumer network
  * `CIDR_RANGE`: the CIDR range to allocate to the new subnet; this range must match the CIDR range of the internal range
  * `REGION`: the region to create the subnet in



### Create a Private Service Connect endpoint

Create a Private Service Connect endpoint in the consumer's peer migration subnet. The consumer needs the service attachment URI to create the endpoint.

### Console

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Connected endpoints** tab.

  3. Click **Connect endpoint**.

  4. For **Target** , select **Published service**.

  5. For **Target service** , enter the service attachment URI that you want to connect to.

The service attachment URI is in this format: `projects/SERVICE_PROJECT/regions/REGION/serviceAttachments/SERVICE_NAME`

  6. For **Endpoint name** , enter a name to use for the endpoint.

  7. For **Network** , select the consumer VPC network for the endpoint.

  8. For **Subnetwork** , select the consumer peer migration subnet.

  9. To reserve an IP address for the endpoint, do the following:

     1. Click the **IP address** drop-down menu and select **Create IP address**.
     2. Enter a name and optional description for the IP address.
     3. Click **Static IP address** and select **Let me choose**.
     4. Enter the custom IP address to reserve. This IP address must be the same IP address that was used in the service's load balancer.
     5. Click **Reserve**.
  10. Click **Add endpoint**.




### gcloud

  1. Reserve an internal IP address for the endpoint.

Use the [`addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create).
         
         gcloud compute addresses create ENDPOINT_ADDRESS_NAME \
             --project=CONSUMER_PROJECT \
             --region=REGION \
             --address=ENDPOINT_ADDRESS \
             --subnet=CONSUMER_SUBNET
         

Replace the following:

     * `ENDPOINT_ADDRESS_NAME`: a name for the IP address resource
     * `CONSUMER_PROJECT`: the ID of the consumer project
     * `REGION`: the region to create the IP address in
     * `ENDPOINT_ADDRESS`: the IP address to assign to the IP address resource; this address must be the same IP address that was used in the service's load balancer
     * `CONSUMER_SUBNET`: the name of the consumer peer migration subnet
  2. Create the endpoint.

Use the [`forwarding-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/create).
         
         gcloud compute forwarding-rules create ENDPOINT \
             --region=REGION \
             --network=CONSUMER_NETWORK \
             --address=ENDPOINT_ADDRESS \
             --target-service-attachment=SERVICE_ATTACHMENT_URI
         

Replace the following:

     * `ENDPOINT`: a name for the endpoint
     * `REGION`: the region to create the endpoint in
     * `CONSUMER_NETWORK`: the name of the consumer network
     * `ENDPOINT_ADDRESS`: the reserved IP address to assign to the endpoint; you can specify the IP address directly, or use the IP address resource name
     * `SERVICE_ATTACHMENT_URI`: the URI of the service attachment



## Delete the producer's internal range

After the consumer migration subnet is created, the internal range is no longer needed and can be deleted.

### gcloud

Use the [`internal-ranges delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/delete).
    
    
    gcloud network-connectivity internal-ranges delete RANGE_NAME \
        --project=PRODUCER_PROJECT_ID
    

Replace the following:

  * `RANGE_NAME`: the name of the internal range
  * `PRODUCER_PROJECT_ID`: the ID of the producer project



## Validate that the endpoint works

Ask the consumer to confirm that they can connect to the service through the endpoint.

If the endpoint isn't working, and troubleshooting doesn't resolve the issue, you can roll back the migration.

## Finalize the migration

If the endpoint is working as expected, you can finalize the migration by updating the consumer's peer migration subnet to a regular subnet.

### Update the consumer's peer migration subnet

Updating the consumer's peer migration subnet to a regular subnet lets the consumer use the subnet for any type of resource.

**Caution:** After the subnet is updated to a regular subnet, the service migration can't be rolled back. Make sure that the consumer can access the service through the endpoint before you update the subnet.

### Console

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of a VPC network to show its **VPC network details** page.

  3. Click the **Subnets** tab.

  4. Click the name of the subnet that you want to update.

  5. Click **Edit**.

  6. In the **Purpose** section, select **Private**.

  7. Click **Save**.




### gcloud

Use the [`networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
    
    
    gcloud compute networks subnets update CONSUMER_SUBNET \
        --purpose=PRIVATE \
        --region=REGION \
        --project=CONSUMER_PROJECT
    

Replace the following:

  * `CONSUMER_SUBNET`: the name of the consumer subnet
  * `REGION`: the region of the consumer subnet
  * `CONSUMER_PROJECT`: the ID of the consumer project



### Delete the peering connections

If the peering connection is no longer needed, [delete the peering configurations](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#deleting-peer) for both the consumer and the producer.

## Roll back the migration

You can only roll back the migration if the consumer subnet hasn't yet been updated to a regular subnet. If you roll back, the service is made available through VPC Network Peering.

  1. If it still exists, delete the internal range in the producer's project.
  2. Create an internal range in the consumer's project. When rolling back, the migration source is the consumer subnet, and the migration target is the producer subnet.
         
         gcloud network-connectivity internal-ranges create RANGE_NAME \
             --project=CONSUMER_PROJECT \
             --ip-cidr-range=CIDR_RANGE \
             --network=CONSUMER_NETWORK \
             --usage=FOR_MIGRATION \
             --migration-source=CONSUMER_SUBNET_URI \
             --migration-target=PRODUCER_SUBNET_URI
         

  3. Delete the consumer's Private Service Connect endpoint.

  4. Delete the consumer's IP address resource.

  5. Recreate the producer's subnet using the same name and CIDR range. Set the subnet purpose to `PRIVATE`.

  6. Recreate the resources needed to provide the service in the producer's subnet.

  7. The consumer validates that they can access the service through the peering connection.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
