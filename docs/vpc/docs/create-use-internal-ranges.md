---
url: https://docs.cloud.google.com/vpc/docs/create-use-internal-ranges/
title: Create and use internal ranges \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:12.976221+00:00
---

# Create and use internal ranges  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/create-use-internal-ranges/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and use internal ranges

This document describes how to create, use, and delete internal ranges.

Internal ranges help you manage a unified IP address space across Virtual Private Cloud (VPC) networks by letting you allocate blocks of internal IP addresses and specify how those blocks can be used.

## Before you begin

  * To use the command-line examples in this guide, install or update to the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).
  * You must [enable](https://console.cloud.google.com/apis/library/networkconnectivity.googleapis.com) the [Network Connectivity API](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest) in your project.
  * Identify or create a [VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks).



### Required roles

To get the permissions that you need to work with internal ranges, ask your administrator to grant you the [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Reserve internal ranges

You specify at least two things when creating an internal range: the IP addresses to allocate and the network to allocate the addresses in. You can create an IPv4 or IPv6 internal range with a specific CIDR block, or you can have Google Cloud allocate an IPv4 block automatically. You can't create an IPv6 internal range with an automatically allocated address block.

When you request an automatically allocated IPv4 CIDR block, you provide a prefix length and one or more optional target IPv4 CIDR blocks. If you don't specify a target CIDR block, Google Cloud uses the following default target ranges:

  * For custom mode VPC networks, the default ranges are `10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16`.
  * For auto mode VPC networks, the default ranges are `10.0.0.0/9`, `172.16.0.0/12`, and `192.168.0.0/16`.



Google Cloud accounts for existing IP address allocations and allocates the internal range a free CIDR block of the chosen size from within the target CIDR blocks. You can further refine this allocation by providing an optional list of CIDR blocks to exclude. Google Cloud allocates an IP address block to the internal range that doesn't overlap with any excluded block. The list of excluded blocks can't be updated after you create an internal range.

To control the method that Google Cloud uses to automatically select a free block, you can specify an [allocation strategy](https://docs.cloud.google.com/vpc/docs/internal-ranges#allocation-strategies). If you don't specify an allocation strategy, Google Cloud randomly allocates a free IP address range from within the target CIDR blocks (or the default range, if no target CIDR blocks are specified).

IPv6 internal ranges let you prevent the [automatic assignment of IP addresses](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-specifications) to new IPv6-only or dual-stack subnets. IPv6 internal ranges must have the usage type `EXTERNAL_TO_VPC` and the peering type `FOR_SELF`. You must include a specific IPv6 CIDR block, and the `overlaps` field must be empty or unspecified.

To prevent users from updating an internal range's CIDR block or overlap configuration, you can create an immutable internal range. Immutable internal ranges prevent changes to these properties, but you can still update the description. Immutability can't be changed after the internal range is created.

By default, Google Cloud blocks the creation of internal ranges or resources if they share overlapping IP addresses in the same VPC network. You can configure an IPv4 internal range to allow overlap with the address ranges of existing subnets, new and existing routes, or both. You can't create Google Cloud resources that use IP addresses from an existing internal range, unless you explicitly associate the resource with the internal range (for subnets) or configure overlapping (for routes).

###  Console 

  1. In the Google Cloud console, go to the **Internal ranges** page.

[Go to Internal ranges](https://console.cloud.google.com/networking/internal-ranges/list)

  2. Click **Reserve internal range**.

  3. Enter a name.

  4. Optional: Enter a description.

  5. Select an IP version.

     * If you select **IPv4** , do the following:

       1. Specify whether the internal range is immutable.
       2. Select a reservation method.

          * If you select **Automatic** , do the following:

            1. Select an [allocation algorithm](https://docs.cloud.google.com/vpc/docs/internal-ranges#allocation-strategies).
            2. Select a prefix length.
            3. Enter a target IP address range. You can add multiple target ranges.
            4. Optional: Click **Add a range to exclude** , and then enter an IP address range to exclude. You can add multiple excluded ranges.

Google Cloud allocates an IP address block to the internal range that doesn't overlap with any excluded range. This list can't be updated after the internal range is created.

          * If you select **Let me specify** , enter an IP range in CIDR notation.

       3. Select a network.

       4. Select a peering type.

       5. Select a usage type.

       6. Optional: In the **Allowed overlaps** section, specify whether the internal range can overlap with existing subnets, new and existing routes, or both.

     * If you select **IPv6** , do the following:

       1. Specify whether the internal range is immutable.
       2. Select **Let me specify** , and then enter an IPv6 or IPv4-mapped IPv6 CIDR block.
       3. Select a network.
       4. Click **Peering** , and then select **For self**.
       5. Click **Usage** , and then select **External to VPC**.
  6. Click **Reserve**.




###  gcloud 

  * To reserve an internal range for a specific IPv4 or IPv6 CIDR block, use the [`gcloud network-connectivity internal-ranges create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create).
        
        gcloud network-connectivity internal-ranges create RANGE_NAME \
            --ip-cidr-range=CIDR_RANGE \
            --network=NETWORK_NAME \
            --description="DESCRIPTION" \
            --peering=PEERING_TYPE \
            --usage=USAGE_TYPE
        

Replace the following:

    * `RANGE_NAME`: the name of the new internal range
    * `CIDR_RANGE`: the IPv4, IPv6, or IPv4-mapped IPv6 CIDR block to allocate to the new internal range 
      * If you specify an IPv6 block, you must do the following: 
        * Set the `peering` type to `FOR_SELF`.
        * Set the `usage` type to `EXTERNAL_TO_VPC`.
    * `NETWORK_NAME`: the name of the network to create the internal range in
    * `DESCRIPTION`: an optional description of the internal range
    * `PEERING_TYPE`: the peering type of the internal range

Options are `FOR_SELF`, `FOR_PEER`, and `NOT_SHARED`. `FOR_SELF` is the default.

    * `USAGE_TYPE`: the usage type of the internal range

Options are `FOR_VPC`, `EXTERNAL_TO_VPC`, and `FOR_MIGRATION`. The default value is `FOR_VPC`.

      * If you use the `FOR_MIGRATION` option, you must also specify source and target subnets. For an example, see Reserve IPv4 internal ranges for subnet migration.
  * To reserve an IPv4 internal range with an automatically allocated CIDR block, use the following command:
        
        gcloud network-connectivity internal-ranges create RANGE_NAME \
            --network=NETWORK_NAME \
            --prefix-length=PREFIX_LENGTH \
            --target-cidr-range=TARGET_CIDR_RANGE \
            --peering=PEERING_TYPE \
            --usage=USAGE_TYPE \
            --description="DESCRIPTION" \
            --allocation-strategy=ALLOCATION_STRATEGY
            [--first-available-ranges-lookup-size=FIRST_N_LOOKUP_SIZE]
        

Replace the following:

    * `PREFIX_LENGTH`: the prefix length of the allocated IP addresses
    * `TARGET_CIDR_RANGE`: the target CIDR block from which to allocate an IPv4 address block

      * For custom mode VPC networks, the default CIDR blocks are `10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16`.
      * For auto mode VPC networks, the default CIDR blocks are `10.0.0.0/9`, `172.16.0.0/12`, and `192.168.0.0/16`.

You can enter multiple CIDR blocks in a comma-separated list.

    * `ALLOCATION_STRATEGY`: the allocation strategy that you want to use for this internal range's CIDR block

Options are `RANDOM`, `FIRST_AVAILABLE`, `RANDOM_FIRST_N_AVAILABLE`, and `FIRST_SMALLEST_FITTING`. The default is `RANDOM`.

    * `FIRST_N_LOOKUP_SIZE`: for the `RANDOM_FIRST_N_AVAILABLE` allocation strategy, the number of free CIDR blocks to find before randomly determining one

Only include this flag if you choose the `RANDOM_FIRST_N_AVAILABLE` allocation strategy.

  * If you want to exclude IP address ranges when reserving an IPv4 internal range with an automatically allocated CIDR block, use the following command:
        
        gcloud alpha network-connectivity internal-ranges create RANGE_NAME \
            --network=NETWORK_NAME \
            --prefix-length=PREFIX_LENGTH \
            --target-cidr-range=TARGET_CIDR_RANGE \
            --peering=PEERING_TYPE \
            --usage=USAGE_TYPE \
            --description="DESCRIPTION" \
            --exclude-cidr-ranges=EXCLUDED_RANGES
        

Replace `EXCLUDED_RANGES` with a comma-separated list of one or more IPv4 CIDR blocks to exclude. Google Cloud allocates an IP address block to the internal range that doesn't overlap with any excluded block. The list can't be updated after the internal range is created.

  * To reserve an IPv4 internal range with overlap, use the following command:
        
        gcloud network-connectivity internal-ranges create RANGE_NAME \
            --ip-cidr-range=CIDR_RANGE \
            --network=NETWORK_NAME \
            --description="DESCRIPTION" \
            --peering=PEERING_TYPE \
            --usage=USAGE_TYPE \
            --overlaps=OVERLAPS
        

Replace `OVERLAPS` with the type of overlap to allow. Options are `OVERLAP_EXISTING_SUBNET_RANGE` and `OVERLAP_ROUTE_RANGE`. You can include both values in a comma-separated list.

  * To reserve an immutable internal range, use the following command:
        
        gcloud network-connectivity internal-ranges create RANGE_NAME \
            --ip-cidr-range=CIDR_RANGE \
            --network=NETWORK_NAME \
            --description="DESCRIPTION" \
            --peering=PEERING_TYPE \
            --usage=USAGE_TYPE \
            --immutable
        




###  API 

  * To reserve an internal range for a specific IPv4 or IPv6 CIDR block, make a `POST` request to the [`projects.locations.internalRanges.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.internalRanges/create).
        
        POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/internalRanges?internalRangeId=RANGE_NAME
        {
          "ipCidrRange": "CIDR_RANGE",
          "network": "NETWORK_NAME",
          "description": "DESCRIPTION",
          "peering": "PEERING_TYPE",
          "usage": "USAGE_TYPE"
        }
        

Replace the following:

    * `PROJECT_ID`: the ID of the parent project for the internal range
    * `RANGE_NAME`: the name of the internal range
    * `CIDR_RANGE`: the IPv4, IPv6, or IPv4-mapped IPv6 CIDR block to allocate to the internal range 
      * If you specify an IPv6 block, you must do the following: 
        * Set the `peering` type to `FOR_SELF`.
        * Set the `usage` type to `EXTERNAL_TO_VPC`.
    * `NETWORK_NAME`: the name of the network to create the internal range in
    * `DESCRIPTION`: an optional description of the new internal range
    * `PEERING_TYPE`: the peering type of the internal range

Options are `FOR_SELF`, `FOR_PEER`, and `NOT_SHARED`. `FOR_SELF` is the default.

    * `USAGE_TYPE`: the usage type of the internal range

Options are `FOR_VPC`, `EXTERNAL_TO_VPC`, and `FOR_MIGRATION`. The default value is `FOR_VPC`.

      * If you use the `FOR_MIGRATION` option, you must also specify source and target subnets. For an example, see Reserve IPv4 internal ranges for subnet migration.
  * To reserve an IPv4 internal range with an automatically allocated CIDR block, make the following request:
        
        POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/internalRanges?internalRangeId=RANGE_NAME
        {
          "prefixLength": PREFIX_LENGTH,
          "targetCidrRange": "TARGET_CIDR_RANGE",
          "network": "NETWORK_NAME",
          "description": "DESCRIPTION",
          "peering": "PEERING_TYPE",
          "usage": "USAGE_TYPE",
          "allocationOptions": {
            "allocationStrategy": "ALLOCATION_STRATEGY",
            ["firstAvailableRangesLookupSize": FIRST_N_LOOKUP_SIZE]
          }
        }
        

Replace the following:

    * `PREFIX_LENGTH`: the CIDR prefix length for the range's IP address block
    * `TARGET_CIDR_RANGE`: the target CIDR block from which to allocate an IPv4 address block

      * For custom mode VPC networks, the default CIDR blocks are `10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16`.
      * For auto mode VPC networks, the default CIDR blocks are `10.0.0.0/9`, `172.16.0.0/12`, and `192.168.0.0/16`.

You can specify multiple CIDR blocks in a JSON array.

    * `ALLOCATION_STRATEGY`: the allocation strategy that you want to use for this internal range's CIDR block

Options are `RANDOM`, `FIRST_AVAILABLE`, `RANDOM_FIRST_N_AVAILABLE`, and `FIRST_SMALLEST_FITTING`. The default is `RANDOM`.

    * `FIRST_N_LOOKUP_SIZE`: For the `RANDOM_FIRST_N_AVAILABLE` allocation strategy, the number of free CIDR blocks to find before randomly determining one

Only include this field if you choose the `RANDOM_FIRST_N_AVAILABLE` allocation strategy.

  * If you want to exclude IP address ranges when reserving an IPv4 internal range with an automatically allocated CIDR block, make the following request:
        
        POST https://networkconnectivity.googleapis.com/v1alpha1/projects/PROJECT_ID/locations/global/internalRanges?internalRangeId=RANGE_NAME
        {
          "prefixLength": PREFIX_LENGTH,
          "targetCidrRange": "TARGET_CIDR_RANGE",
          "network": "NETWORK_NAME",
          "description": "DESCRIPTION",
          "peering": "PEERING_TYPE",
          "usage": "USAGE_TYPE",
          "excludeCidrRanges": ["EXCLUDED_RANGE_1","EXCLUDED_RANGE_2"]
        }
        

Replace `EXCLUDED_RANGE_1` and `EXCLUDED_RANGE_2` with one or more IPv4 CIDR blocks to exclude. Google Cloud allocates an IP address block to the internal range that doesn't overlap with any excluded block. The list can't be updated after the internal range is created.

  * To reserve an IPv4 internal range with overlap, make the following request:
        
        POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/internalRanges?internalRangeId=RANGE_NAME
        {
          "ipCidrRange": "CIDR_RANGE",
          "network": "NETWORK_NAME",
          "description": "DESCRIPTION",
          "peering": "PEERING_TYPE",
          "usage": "USAGE_TYPE",
          "overlaps": ["OVERLAPS"]
        }
        

Replace `OVERLAPS` with the type of overlap to allow. Options are `OVERLAP_EXISTING_SUBNET_RANGE` and `OVERLAP_ROUTE_RANGE`. You can include both values in a JSON array.

  * To reserve an immutable internal range, make the following request:
        
        POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/internalRanges?internalRangeId=RANGE_NAME
        {
          "ipCidrRange": "CIDR_RANGE",
          "network": "NETWORK_NAME",
          "description": "DESCRIPTION",
          "peering": "PEERING_TYPE",
          "usage": "USAGE_TYPE",
          "immutable": true
        }
        




## Reserve IPv4 internal ranges for subnet migration

You can use an internal range to migrate a CIDR range from one subnet to another. For more information, see [Migrating IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/internal-ranges#for-migration).

###  gcloud 

Use the [`gcloud network-connectivity internal-ranges create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create).
    
    
    gcloud network-connectivity internal-ranges create RANGE_NAME \
        --ip-cidr-range=CIDR_RANGE \
        --network=NETWORK_NAME \
        --peering=FOR_SELF \
        --usage=FOR_MIGRATION \
        --migration-source=SOURCE_SUBNET \
        --migration-target=TARGET_SUBNET
    

Replace the following:

  * `RANGE_NAME`: the name of the internal range to create
  * `CIDR_RANGE`: the IPv4 CIDR block of the subnet that you want to migrate
  * `NETWORK_NAME`: the name of the network to create the internal range in
  * `SOURCE_SUBNET`: the URI of the source subnet
  * `TARGET_SUBNET`: the URI of the target subnet



###  API 

Make a `POST` request to the [`projects.locations.internalRanges.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.internalRanges/create).
    
    
    POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/internalRanges?internalRangeId=RANGE_NAME
    {
      "ipCidrRange": "CIDR_RANGE",
      "network": "NETWORK_NAME",
      "peering": "FOR_SELF",
      "usage": "FOR_MIGRATION",
      "migration": {
        "source": "SOURCE_SUBNET",
        "target": "TARGET_SUBNET"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the parent project for the internal range
  * `RANGE_NAME`: the name of the new internal range
  * `CIDR_RANGE`: the IPv4 CIDR block of the subnet that you want to migrate
  * `NETWORK_NAME`: the name of the network to create the internal range in
  * `SOURCE_SUBNET`: the URI of the source subnet
  * `TARGET_SUBNET`: the URI of the target subnet



## Create subnetworks with IPv4 internal ranges

You can create an IPv4-only or dual-stack subnet and use an internal range to specify the subnet's primary internal IPv4 address range. The subnet can be associated with an entire internal range or only part of the range. Secondary ranges for subnets can also be associated with internal ranges.

###  Console 

  1. Reserve an IPv4 internal range in the network where you want to create a new subnet. Set the usage type on this internal range to `For VPC`, and set the peering type to `For self`.

  2. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  3. Click the name of a VPC network to show its **VPC network details** page.

  4. Click **Add subnet**. In the dialog that appears:

     1. Provide a name.
     2. Select a region.
     3. Select the **Associate with an internal range** checkbox.
     4. For **Reserved internal range** , make a selection.
     5. Optional: To associate the subnet with part of the internal range, enter an IPv4 range.
     6. Click **Add**.



###  gcloud 

  1. Reserve an IPv4 internal range in the network where you want to create a new subnet. Set the usage type on this internal range to `FOR_VPC`, and set the peering type to `FOR_SELF`.
  2. Do one of the following:

     * To create a subnet that is associated with an entire internal range, use the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
           
           gcloud compute networks subnets create SUBNET_NAME \
               --reserved-internal-range=networkconnectivity.googleapis.com/projects/PROJECT_ID/locations/global/internalRanges/RANGE_NAME \
               --network=NETWORK_NAME \
               --region=REGION
           

Replace the following:

       * `SUBNET_NAME`: the name of the subnet
       * `PROJECT_ID`: the ID of the project to create the subnet in
       * `RANGE_NAME`: the name of the internal range to associate with the subnet
       * `NETWORK_NAME`: the name of the network to create the subnet in
       * `REGION`: the region to create the subnet in
     * To create a subnet that is associated with part of an internal range, use the following command:
           
           gcloud compute networks subnets create SUBNET_NAME \
               --reserved-internal-range=networkconnectivity.googleapis.com/projects/PROJECT_ID/locations/global/internalRanges/RANGE_NAME \
               --range=IP_RANGE \
               --network=NETWORK_NAME \
               --region=REGION
           

Replace `IP_RANGE` with an IPv4 CIDR range that is a subset of the internal range.




For example, the following commands create a subnet that is associated with only the `10.9.1.0/24` part of an internal range that reserves the `10.9.0.0/16` CIDR block.
    
    
    gcloud network-connectivity internal-ranges create reserved-range-one \
        --ip-cidr-range=10.9.0.0/16 \
        --network=vpc-one
    
    
    
    gcloud compute networks subnets create subnet-one \
        --reserved-internal-range=networkconnectivity.googleapis.com/projects/project-one/locations/global/internalRanges/reserved-range-one \
        --range=10.9.1.0/24 \
        --network=vpc-one \
        --region=us-central1
    

###  API 

  1. Reserve an IPv4 internal range in the network where you want to create a new subnet. Set the usage type on this internal range to `FOR_VPC`, and set the peering type to `FOR_SELF`.
  2. Do one of the following:

     * To create a subnet that is associated with an entire internal range, make a `POST` request to the [`subnetworks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/insert).
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks
           {
             "name" : "SUBNET_NAME",
             "reservedInternalRange" : "networkconnectivity.googleapis.com/projects/PROJECT_ID/locations/global/internalRanges/RANGE_NAME",
             "network" : "NETWORK"
           }
           

Replace the following:

       * `PROJECT_ID`: the ID of the parent project for the new subnet
       * `REGION`: the region to create the subnet in
       * `SUBNET_NAME`: the name of the new subnet
       * `PROJECT_ID`: the ID of the project to create a subnet in
       * `RANGE_NAME`: the name of the internal range to use for the new subnet
       * `NETWORK`: the name of the network to create the subnet in
     * To create a subnet that is associated with part of an internal range, make the following request:
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks
           {
             "name" : "SUBNET_NAME",
             "reservedInternalRange" : "networkconnectivity.googleapis.com/projects/PROJECT_ID/locations/global/internalRanges/RANGE_NAME",
             "range" : "IP_RANGE",
             "network" : "NETWORK"
           }
           

Replace `IP_RANGE` with an IPv4 CIDR range that is a subset of the internal range.




For example, the following requests create a subnet that is associated with only the `10.9.1.0/24` part of an internal range that contains the `10.9.0.0/16` CIDR block.
    
    
    POST https://networkconnectivity.googleapis.com/v1/projects/sample-project/locations/global/internalRanges?internalRangeId=reserved-for-subnet
    {
      "targetCidrRange": "10.9.0.0/16",
      "network": "network-b"
    }
    
    
    
    POST https://compute.googleapis.com/compute/v1/projects/11223344/regions/us-central1/subnetworks
    {
      "name" : "subnet-with-partial-range",
      "reservedInternalRange" : "networkconnectivity.googleapis.com/projects/project-one/locations/global/internalRanges/reserved-for-subnet",
      "range" : "10.9.1.0/24",
      "network" : "network-b"
    }
    

## Create GKE clusters with IPv4 internal ranges

You can use IPv4 internal ranges to allocate IP addresses for Google Kubernetes Engine (GKE) [VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips).

###  gcloud 

  1. Create the following IPv4 internal ranges by using the [`gcloud network-connectivity internal-ranges create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/create).

     * For GKE [nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes):
    
    gcloud network-connectivity internal-ranges create gke-nodes-1 \
        --prefix-length=NODE_PREFIX_LENGTH \
        --network=NETWORK
    

     * For GKE [pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/pod#what_is_a_pod):
    
    gcloud network-connectivity internal-ranges create gke-pods-1 \
        --prefix-length=POD_PREFIX_LENGTH \
        --network=NETWORK
    

     * For GKE [services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#what-is-a-service):
    
    gcloud network-connectivity internal-ranges create gke-services-1 \
        --prefix-length=SERVICE_PREFIX_LENGTH \
        --network=NETWORK
    

Replace the following:

     * `NODE_PREFIX_LENGTH`: the prefix length for the internal range that is associated with GKE nodes
     * `POD_PREFIX_LENGTH`: the prefix length for the internal range that is associated with GKE pods
     * `SERVICE_PREFIX_LENGTH`: the prefix length for the internal range that is associated with GKE services
     * `NETWORK`: the name of the network
  2. Create a subnet with the internal ranges that you created in the previous step by using the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
         
         gcloud compute networks subnets create gke-subnet-1 \
             --network=NETWORK \
             --region=REGION \
             --reserved-internal-range="//networkconnectivity.googleapis.com/projects/PROJECT_ID/locations/global/internalRanges/gke-nodes-1" \
             --secondary-range-with-reserved-internal-range="pods=//networkconnectivity.googleapis.com/projects/PROJECT_ID/locations/global/internalRanges/gke-pods-1,services=//networkconnectivity.googleapis.com/projects/PROJECT_ID/locations/global/internalRanges/gke-services-1"
         

Replace the following:

     * `REGION`: the region of the subnet
     * `PROJECT_ID`: the ID of the project
  3. Create the VPC-native cluster by using the [`gcloud container clusters create` command](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create).
         
         gcloud container clusters create CLUSTER_NAME \
             --network=NETWORK \
             --subnetwork=gke-subnet-1 \
             --zone=ZONE \
             --cluster-secondary-range-name=pods \
             --services-secondary-range-name=services \
             --enable-ip-alias
         

Replace `ZONE` with the zone of the cluster.




###  API 

  1. Create the following internal ranges by making `POST` requests to the [`projects.locations.internalRanges.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.internalRanges/create).

     * For GKE [nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes):
    
    POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/internalRanges?internalRangeId=gke-nodes-1
    {
      "network": "NETWORK",
      "prefixLength": NODE_PREFIX_LENGTH,
      "peering": "FOR_SELF",
      "usage": "FOR_VPC"
    }
    

     * For GKE [pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/pod#what_is_a_pod):
    
    POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/internalRanges?internalRangeId=gke-pods-1
    {
      "network": "NETWORK",
      "prefixLength": POD_PREFIX_LENGTH,
      "peering": "FOR_SELF",
      "usage": "FOR_VPC"
    }
    

     * For GKE [services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#what-is-a-service):
    
    POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/internalRanges?internalRangeId=gke-services-1
    {
      "network": "NETWORK",
      "prefixLength": SERVICE_PREFIX_LENGTH,
      "peering": "FOR_SELF",
      "usage": "FOR_VPC"
    }
    

Replace the following:

     * `PROJECT_ID`: the ID of the project
     * `NETWORK`: the name of the network
     * `NODE_PREFIX_LENGTH`: the prefix length for the internal range that is associated with GKE nodes
     * `POD_PREFIX_LENGTH`: the prefix length for the internal range that is associated with GKE pods
     * `SERVICE_PREFIX_LENGTH`: the prefix length for the internal range that is associated with GKE services
  2. Create a subnet with the internal ranges that you created in the previous step by making a `POST` request to the [`subnetworks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/insert).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks
         {
           "name": "gke-subnet-1",
           "network": "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK",
           "privateIpGoogleAccess": false,
           "reservedInternalRange": "//networkconnectivity.googleapis.com/projects/PROJECT_ID/locations/global/internalRanges/gke-nodes-1",
           "secondaryIpRanges": [
             {
               "rangeName": "pods",
               "reservedInternalRange": "//networkconnectivity.googleapis.com/projects/PROJECT_ID/locations/global/internalRanges/gke-pods-1"
             },
             {
               "rangeName": "services",
               "reservedInternalRange": "//networkconnectivity.googleapis.com/projects/PROJECT_ID/locations/global/internalRanges/gke-services-1"
             }
           ]
         }
         

Replace the following:

     * `PROJECT_ID`: the ID of the project
     * `REGION`: the region of the subnet
     * `NETWORK`: the network of the subnet
  3. Create the VPC-native cluster by making a `POST` request to the [`clusters.create` method](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.zones.clusters/create).
         
         POST https://container.googleapis.com/v1/projects/PROJECT_ID/locations/ZONE/clusters
         {
           "cluster": {
             "ipAllocationPolicy": {
               "clusterSecondaryRangeName": "pods",
               "createSubnetwork": false,
               "servicesSecondaryRangeName": "services",
               "useIpAliases": true
             },
             "name": "CLUSTER_NAME",
             "network": "NETWORK",
             "nodePools": [
               {
                 "config": {
                   "oauthScopes": [
                     "https://www.googleapis.com/auth/devstorage.read_only",
                     "https://www.googleapis.com/auth/logging.write",
                     "https://www.googleapis.com/auth/monitoring",
                     "https://www.googleapis.com/auth/service.management.readonly",
                     "https://www.googleapis.com/auth/servicecontrol",
                     "https://www.googleapis.com/auth/trace.append"
                   ]
                 },
                 "initialNodeCount": 3,
                 "management": {
                   "autoRepair": true,
                   "autoUpgrade": true
                 },
                 "name": "default-pool",
                 "upgradeSettings": {
                   "maxSurge": 1
                 }
               }
             ],
             "subnetwork": "gke-subnet-1"
           },
           "parent": "projects/PROJECT_ID/locations/ZONE"
         }
         

Replace the following:

     * `PROJECT_ID`: the ID of the project
     * `ZONE`: the zone of the cluster
     * `CLUSTER_NAME`: the name of the new cluster
     * `NETWORK`: the network of the cluster



## List internal ranges

You can list internal ranges to view all internal ranges in your current project or a specific VPC network. To list projects in a VPC network, use the Google Cloud CLI or send an API request.

###  Console 

  * In the Google Cloud console, go to the **Internal ranges** page.

[Go to Internal ranges](https://console.cloud.google.com/networking/internal-ranges/list)




###  gcloud 

  * To view all internal ranges in your current project, use the [`gcloud network-connectivity internal-ranges list` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/list).
        
        gcloud network-connectivity internal-ranges list
        

  * To view all internal ranges in a VPC network, use the `internal-ranges list` command and include a filter.
        
        gcloud network-connectivity internal-ranges list \
            --filter=network:NETWORK_NAME \
            --project=PROJECT_ID
        

Replace the following:

    * `NETWORK_NAME`: the name of the VPC network to list internal ranges in
    * `PROJECT_ID`: the ID of the project that contains the VPC network



###  API 

  * To view all internal ranges in a project, make a `GET` request to the [`projects.locations.internalRanges.list` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.internalRanges/list).
        
        GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/internalRanges
        

Replace `PROJECT_ID` with the ID of the project to view internal ranges in.

  * To view all internal ranges in a VPC network, make a `GET` request to the `projects.locations.internalRanges.list` method and include a filter.
        
        GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/internalRanges?filter=network=\"https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK_NAME\"
        

Replace `NETWORK_NAME` with the name of the VPC network to list internal ranges in.




## Describe internal ranges

You can describe an internal range to view details about the chosen range, including any subnets that are associated with the internal range.

###  Console 

  1. In the Google Cloud console, go to the **Internal ranges** page.

[Go to Internal ranges](https://console.cloud.google.com/networking/internal-ranges/list)

  2. Click the **Name** of the internal range that you want to describe.




###  gcloud 

Use the [`gcloud network-connectivity internal-ranges describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/describe).
    
    
    gcloud network-connectivity internal-ranges describe RANGE_NAME
    

Replace `RANGE_NAME` with the name of the internal range to describe.

###  API 

Make a `GET` request to the [`projects.locations.internalRanges.get` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.internalRanges/get).
    
    
    GET https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/internalRanges/RANGE_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the parent project for the internal range
  * `RANGE_NAME`: the name of the internal range to describe



## Update internal ranges

If an internal range is immutable, you can only update the description. If an internal range is mutable, you can expand the range's CIDR block and update its overlap property and description.

To expand an internal range, you can either update the range's CIDR block or decrease its prefix length, and the updated CIDR block must contain the previous block.

If you want to narrow the allocated range or modify another element, delete the internal range and create a new one.

To update an IPv4 internal range's overlap property, send an API request or use the Google Cloud CLI.

###  Console 

  1. In the Google Cloud console, go to the **Internal ranges** page.

[Go to Internal ranges](https://console.cloud.google.com/networking/internal-ranges/list)

  2. Click the name of the internal range that you want to update.

  3. To expand the range's CIDR block, click **Expand range** , and then do one of the following:

     * For IPv4 internal ranges, click **Prefix length** , and then do the following: 
       1. In the **Prefix length** field, select a prefix length that is smaller than the previous prefix.
       2. Click **Expand**.
     * For IPv4 or IPv6 internal ranges, click **IP range** , and then do the following: 
       1. Enter an IPv4, IPv6, or IPv4-mapped IPv6 CIDR block. The new block must contain the earlier one.
       2. Click **Expand**.
  4. To update the range's description, do the following:

     1. Click  mode_edit**Edit description**
     2. Enter a new description.
     3. Click **Save**.



###  gcloud 

  * To update an internal range, use the [`gcloud network-connectivity internal-ranges update` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/update). Omit flags for properties that you don't want to modify.
        
        gcloud network-connectivity internal-ranges update RANGE_NAME \
            --ip-cidr-range=CIDR_RANGE \
            --overlaps=OVERLAPS \
            --description=DESCRIPTION
        

Replace the following:

    * `RANGE_NAME`: the name of the internal range
    * `CIDR_RANGE`: the expanded IPv4, IPv6, IPv4-mapped IPv6 CIDR block, which must contain the previous block
    * `OVERLAPS`: the type of overlap to allow (IPv4 ranges only)

Options are `OVERLAP_EXISTING_SUBNET_RANGE` and `OVERLAP_ROUTE_RANGE`. You can include both values in a comma-separated list. To disable overlap, include the flag but don't specify a value (`--overlaps=`).

    * `DESCRIPTION`: the updated description

  * To expand an internal range by decreasing its prefix length, use the following command:
        
        gcloud network-connectivity internal-ranges update RANGE_NAME \
            --prefix-length=PREFIX_LENGTH
        

Replace `PREFIX_LENGTH` with the updated prefix length, which must be less than the previous prefix length.




###  API 

  * To expand an internal range by updating its CIDR range, make a `PATCH` request to the [`projects.locations.internalRanges.patch` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.internalRanges/patch).
        
        PATCH https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/internalRanges/RANGE_NAME?updateMask=ipCidrRange
        {
          "ipCidrRange": "CIDR_RANGE"
        }
        

Replace the following:

    * `PROJECT_ID`: the ID of the parent project for the internal range
    * `RANGE_NAME`: the name of the internal range
    * `CIDR_RANGE`: the expanded IPv4, IPv6, or IPv4-mapped IPv6 CIDR block, which must contain the previous block
  * To expand an internal range by decreasing its prefix length, make the following request:
        
        PATCH https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/internalRanges/RANGE_NAME?updateMask=prefixLength
        {
          "prefixLength": PREFIX_LENGTH
        }
        

Replace `PREFIX_LENGTH` with the updated prefix length, which must be less than the previous prefix length.

  * To update an IPv4 internal range's overlap property, make the following request:
        
        PATCH https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/internalRanges/RANGE_NAME?updateMask=overlaps
        {
          "overlaps": ["OVERLAPS"]
        }
        

Replace `OVERLAPS` with the type of overlap to allow. Options are `OVERLAP_EXISTING_SUBNET_RANGE` and `OVERLAP_ROUTE_RANGE`. You can include both values in a JSON array. To disable overlap, include the field but don't specify a value (`"overlaps": []`).

  * To update an internal range's description, make the following request:
        
        PATCH https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/internalRanges/RANGE_NAME?updateMask=description
        {
          "description": "DESCRIPTION"
        }
        

Replace `DESCRIPTION` with the updated description.




## Delete internal ranges

You can delete an internal range if it is not associated with a Google Cloud resource such as a subnet. To delete an internal range that is associated with a Google Cloud resource, first delete the associated resource.

###  Console 

  1. In the Google Cloud console, go to the **Internal ranges** page.

[Go to Internal ranges](https://console.cloud.google.com/networking/internal-ranges/list)

  2. Click the name of the internal range that you want to delete.

  3. Click **Delete**.

  4. To confirm, click **Delete**.




###  gcloud 

Use the [`gcloud network-connectivity internal-ranges delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/internal-ranges/delete).
    
    
    gcloud network-connectivity internal-ranges delete RANGE_TO_DELETE
    

Replace `RANGE_TO_DELETE` with the name of the internal range to delete.

###  API 

Make a `DELETE` request to the [`projects.locations.internalRanges.delete` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.internalRanges/delete).
    
    
    DELETE https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/internalRanges/RANGE_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the parent project for the internal range
  * `RANGE_NAME`: the name of the internal range



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
