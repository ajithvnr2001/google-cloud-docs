---
url: https://docs.cloud.google.com/vpc/docs/configure-private-services-access/
title: Configure private services access \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:49.309230+00:00
---

# Configure private services access  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/configure-private-services-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure private services access

[Private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) is a private connection between your VPC network and a network owned by Google or a third party. Google or the third party, entities who are offering services, are also known as _service producers_. The private connection enables VM instances in your VPC network and the services that you access to communicate exclusively by using internal IP addresses. VM instances don't need internet access or external IP addresses to reach services that are available through private services access.

To use private services access, you do the following:

  * Create an allocated range.

An allocated range [reserves an IP address range for use by the producer](https://docs.cloud.google.com/vpc/docs/private-services-access#peering), avoiding IP address overlaps between the service consumer and service producer networks.

  * Create a private connection.

The private connection uses VPC Network Peering to [establish connectivity between the service consumer and service producer networks](https://docs.cloud.google.com/vpc/docs/private-services-access#private-connection).




For information about other private access options, see [Private access options for services](https://docs.cloud.google.com/vpc/docs/private-access-options).

## Before you begin

To establish a private connection, complete the following prerequisites:

  * Read the [private services access overview](https://docs.cloud.google.com/vpc/docs/private-services-access), including which [services are supported](https://docs.cloud.google.com/vpc/docs/private-services-access#private-services-supported-services), the [reachability of service instances](https://docs.cloud.google.com/vpc/docs/private-services-access#reachability), and [limitations](https://docs.cloud.google.com/vpc/docs/private-services-access#limitations).
  * Create a Google Cloud project or choose an existing one. To learn how to create a Google Cloud project, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
  * [Enable](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/getting-started) the [Service Networking API](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest) in your project. The API is required to create a private connection.
  * Create or choose a VPC network to use to connect to the service producer's network. VM instances must use this VPC network to connect to services over a private connection.
  * Install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) if you want to run the gcloud CLI command-line examples in this guide.



### Permissions

Project owners and IAM members with the [Compute Network Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`) can create allocated IP address ranges and manage private connections.

For more information about Compute Engine roles, see [Compute Engine IAM roles and permissions](https://docs.cloud.google.com/compute/docs/access/iam).

## Choose an IP address range for the allocated range

Creating an allocated range reserves an IP address range for use by the service producer. Consider the following when you choose a range for your allocation:

  * Check the service producer documentation to see if they have any requirements or recommendations for the allocated range size.

For Google services, the minimum size is a single `/24` block, but the recommended size is a `/16` block.

  * Select an allocated range that is completely separate from current and future subnet ranges, including subnet ranges from networks connected by using VPC Network Peering, and subnet ranges from VPC spokes connected to the same NCC hub.

  * Select a range that doesn't exactly match or contain the destinations of any custom static or dynamic routes.

When a service producer selects an unused portion of an allocated range to use as a candidate for new resources, it excludes all custom route destinations that exactly match or fit within the allocated range. When a VPC network contains an allocated range and custom routes with destinations that match or fit within the allocated range, the usable portion of the allocated range is reduced. This configuration can lead to unexpected allocation exhausted errors.

For example, if you create an allocated range for `10.0.0.0/16`, the following applies:

    * If a custom route with a destination for `10.0.0.0/16` exists or is created later, all of the `10.0.0.0/16` range is considered unavailable. If a service producer attempts to use the allocated range, Google Cloud returns an allocation exhausted error.

    * If a custom route with a destination for `10.0.0.0/20` exists or is created later, the `10.0.0.0/20` portion of the `10.0.0.0/16` allocated range is considered unavailable. If a service producer attempts to use the allocated range, and the available portion of your allocated range is insufficient for a service producer, Google Cloud returns an allocation exhausted error.

    * If a custom route with a destination for `10.0.0.0/8` exists or is created later, this doesn't affect the availability of the `10.0.0.0/16` allocated range.

  * Select a range that doesn't conflict with your other IP address needs:

    * Some Google and third-party products use `172.17.0.0/16` for routing within the guest operating system. For example, the [default Docker bridge network](https://docs.docker.com/network/network-tutorial-standalone/#use-the-default-bridge-network) uses this range. If you depend on a product that uses `172.17.0.0/16`, don't use `172.17.0.0/16` in an allocated range for private services access.
    * If you're using an [auto mode](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) VPC network, you can't create an allocated range that matches or overlaps with `10.128.0.0/9`. Google uses the `10.128.0.0/9` range for [automatically created subnets](https://docs.cloud.google.com/vpc/docs/subnets#ip-ranges), including those in future regions.
  * Select a CIDR block that is large enough to meet your current and future needs.

If you later find that the range isn't sufficient in size, expand the range if possible. Although you can assign multiple allocations to a single service producer, Google enforces a [quota](https://docs.cloud.google.com/vpc/docs/quota#per_project) on the number of IP address ranges that you can allocate but not the size (netmask) of each range.




## Create an allocated range

The following steps describe how to create an allocated IP address range.

When a Google service allocates a range on your behalf, the service uses the following format to name the allocation: `google-managed-services-CONSUMER_NETWORK_NAME`. If this allocation exists, Google services use the existing one instead of creating another one. You can use the same naming convention that Google uses to signal to other users or Google services that an allocation for Google already exists.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Select the VPC network that will connect to a service producer.

  3. Select the **Private services access** tab.

  4. On the **Private services access** tab, select the **Allocated IP ranges for services** tab.

  5. Click **Allocate IP range**.

  6. Enter a **Name** and **Description** for the allocated range.

  7. Configure the IP address range for the allocation:

     * To specify a specific IP address range, select **Custom** and then enter a CIDR block, such as `192.168.0.0/16`.
     * To let Google select an available range, select **Automatic** and then enter a prefix length, such as `16`.
  8. Click **Allocate** to create the allocated range.




###  gcloud 

To create an allocated range in your VPC network, use the [`gcloud compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create).

  * To specify an address range and a prefix length (subnet mask), use the `--addresses` and `--prefix-length` flags. For example, to allocate the CIDR block `192.168.0.0/16`, specify `192.168.0.0` for the address and `16` for the prefix length.
        
        gcloud compute addresses create RESERVED_RANGE_NAME \
                --global \
                --purpose=VPC_PEERING \
                --addresses=192.168.0.0 \
                --prefix-length=16 \
                --description="DESCRIPTION" \
                --network=VPC_NETWORK
            

    * To specify just a prefix length (subnet mask), just use the `prefix-length` flag. When you omit the address range, Google Cloud automatically selects an unused address range in your VPC network. The following example selects an unused IP address range with a `16` bit prefix length.
    
    gcloud compute addresses create RESERVED_RANGE_NAME \
            --global \
            --purpose=VPC_PEERING \
            --prefix-length=16 \
            --description="DESCRIPTION" \
            --network=VPC_NETWORK
        

Replace the following:

    * `RESERVED_RANGE_NAME`: a name for the allocated range, such as `my-allocated-range`.

    * `DESCRIPTION`: a description for the range, such as `allocated for my-service`.

    * `VPC_NETWORK`: the name of your VPC network, such as `my-vpc-network`.

The following example creates a private connection to Google so that the VM instances in the `my-network` VPC network can use private services access to reach Google services that support it.
    
    gcloud compute addresses create google-managed-services-my-network \
        --global \
        --purpose=VPC_PEERING \
        --prefix-length=16 \
        --description="peering range for Google" \
        --network=my-network
    




###  Terraform 

To create an allocated range in your VPC network, use the [`google_compute_global_address` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_global_address).
    
    
    resource "google_compute_global_address" "private_ip_address" {
      name          = "private-ip-address"
      purpose       = "VPC_PEERING"
      address_type  = "INTERNAL"
      prefix_length = 16
      network       = google_compute_network.peering_network.id
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

If you see an error about the `compute.globalAddresses.list` permission for the project, see [Service account permissions](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#service_account_permissions).

**Important:** If you are peering with multiple service producer organizations, you should use a different IP address allocation for each one in the service consumer organization. Google Cloud doesn't check if your allocation overlaps with dynamic routes. If one service producer uses dynamic routes with the service consumer, these routes aren't visible to the other producers. This could result in multiple producers allocating from the same range and leading to routing issues.

## List allocated IP address ranges

To list allocated IP address ranges, use the [`gcloud compute addresses list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/list).
    
    
    gcloud compute addresses list --global --filter="purpose=VPC_PEERING"
    

## Create a private connection

After you create an allocated range, you can create a private connection to a service producer. The private connection establishes a [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) connection between your VPC network and the service producer's network.

Consider the following when you create a private connection:

  * If a single service producer offers multiple services, you only need one private connection for all of the producer's services.
  * If a single service producer offers multiple services and you want to control which allocated ranges are used for different service resources, you can use multiple VPC networks each with their own private connections. This configuration lets you select a particular network when creating a new managed service resource to ensure that the associated allocated ranges are used for the new resource.
  * Don't reuse the same allocated range for multiple service producers. If you connect to multiple service producers, use a unique allocated range for each service producer. Using different allocated ranges avoids IP address overlap, and helps you manage your network settings, such as routes and firewall rules, for each service producer.




### Console

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Select the VPC network that will connect to a service producer.

  3. Select the **Private services access** tab.

  4. On the **Private services access** tab, select the **Private connections to services** tab.

  5. Click **Create connection** to create a private connection between your network and a service producer.

  6. For the **Assigned allocation** , select one or more existing allocated ranges that aren't being used by other service producers.

  7. Click **Connect** to create the connection.




###  gcloud 

  1. Use the [`gcloud services vpc-peerings connect` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/connect).
         
         gcloud services vpc-peerings connect \
             --service=servicenetworking.googleapis.com \
             --ranges=RESERVED_RANGE_NAME \
             --network=VPC_NETWORK
         

Replace the following:

     * `RESERVED_RANGE_NAME`: the name of one or more allocated ranges.

     * `VPC_NETWORK`: the name of your VPC network.

The command initiates a long-running operation, returning an operation name.

  2. To check whether the operation was successful, use the [`gcloud services vpc-peerings operations describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/operations/describe).
         
         gcloud services vpc-peerings operations describe \
             --name=OPERATION_NAME
         

Replace `OPERATION_NAME` with the operation name that was returned from the previous step.




You can specify more than one allocated range when you create a private connection. For example, if a range has been exhausted, you can assign additional allocated ranges. The service uses IP addresses from all of the provided ranges in the order that you specified.

###  Terraform 

To create a private connection, use the [`google_service_networking_connection` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/service_networking_connection).
    
    
    resource "google_service_networking_connection" "default" {
      network                 = google_compute_network.peering_network.id
      service                 = "servicenetworking.googleapis.com"
      reserved_peering_ranges = [google_compute_global_address.private_ip_address.name]
    }

## List private connections

After you create a private connection, you can list it to check that it exists. The list also shows the list of allocated ranges that are associated with each connection. For example, if you don't remember which allocated range you assigned to a connection, view the list to find out.

### Console

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Select the VPC network that contains the connections.

  3. Select the **Private services access** tab.

  4. On the **Private services access** tab, select the **Private connections to services** tab to view all the network's private connections.




###  gcloud 

Use the [`gcloud services vpc-peerings list` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/list).
    
    
    gcloud services vpc-peerings list \
        --network=VPC_NETWORK
    

Replace `VPC_NETWORK` with the name of your VPC network.

## Modify a private connection

You can't modify an allocated range, but you can update a private connection to add or remove allocated ranges without disrupting traffic.

  * **Add ranges** : as you scale, you might add or replace an allocated range if you're close to exhausting the existing one. If you add another allocated range to a private connection, more IP addresses are available to the service producer when creating new service resources for any service they provide. You can't reserve a specific allocated range within a private connection for use by a particular service.

For more information about adding or replacing ranges, see IP address range exhaustion.

  * **Remove ranges** : when you remove a range from a private connection, the following applies:

    * The allocated range is no longer associated with the private connection, but it isn't deleted.

      * If a removed range is no longer in use you can delete the allocation.
    * Existing service producer resources might continue to use the removed range.

    * Private services access doesn't use the removed ranges to allocate new subnets.




### Console

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Select the VPC network that contains the connections.

  3. Select the **Private services access** tab.

  4. On the **Private services access** tab, select the **Private connections to services** tab to view all the network's private connections.

  5. Click a connection name in the list.

  6. In the **Assigned allocation** list, select the allocated ranges that you want to associate with the private connection. Clear the checkboxes for any allocated ranges that you want to remove from the private connection.

  7. Click **OK**.




###  gcloud 

To add or remove assigned allocated IP address ranges on an existing private connection, use the [`gcloud services vpc-peerings update` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/update).
    
    
    gcloud services vpc-peerings update \
        --service=servicenetworking.googleapis.com \
        --ranges=RESERVED_RANGE_NAME \
        --network=VPC_NETWORK \
        [--force]
    

Replace the following:

  * `RESERVED_RANGE_NAME`: a list of one or more names of allocated ranges to assign to the private connection.

`RESERVED_RANGE_NAME` replaces the previous list of allocated ranges. If you omit a range that was previously associated with this private connection, the range is removed from the connection. You must use the `--force` flag to remove a range.

  * `VPC_NETWORK`: the name of your VPC network.




## Delete an allocated IP address range

Before you delete an allocated IP address range, check if the range is in use by a private connection.

If the allocated IP address range is in use, first modify the private connection to remove the range. Then delete the allocated IP address range.

If you delete an allocated IP address that is in use, and you don't modify the private connection, the following applies:

  * Existing connections remain active, but there's nothing preventing your VPC network from using IP addresses that overlap with the service producer's network.

  * If you delete the only allocated IP address range that is associated with a private connection, the service can't create new subnets because there's no allocated IP address range to select from.

  * If you later create an allocated IP address range that matches or overlaps the deleted range, adding the range to a private connection fails.




To avoid these problems, always modify your private connections when you delete an in-use allocated IP address range.

### Console

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Select the VPC network that contains the allocations to delete.

  3. Select the **Private services access** tab.

  4. On the **Private services access** tab, select the **Allocated IP ranges for services** tab.

  5. Select the allocation to delete.

  6. Click **Release** to return the allocated IP address range to network's pool of available internal IP addresses.

If the allocated IP address range is still assigned to an existing connection, you must enter additional confirmation before you can release the allocation.

  7. Click **Release** again to confirm the deletion.




###  gcloud 

Delete the allocation by specifying the name of your allocation.
    
    
    gcloud compute addresses delete NAME \
        --global
    

Replace`NAME` with the name of the allocated range that you want to delete.

## Delete a private connection

To delete a private connection, complete the procedure in this section. Don't attempt to delete a private connection by deleting its associated VPC Network Peering connection directly.

Before you delete a private connection, you must delete all the service instances that you access through the connection.

  * Service instance deletion behavior can vary based on the service. The service's resources might be deleted immediately, or they might be deleted after a waiting period. If there is a waiting period, you can't delete the private connection until the waiting period has passed and the service producer's resources are deleted.

For example, if you [delete a Cloud SQL instance](https://docs.cloud.google.com/sql/docs/mysql/delete-instance), you receive a success response, but the service waits for four days before deleting the service producer resources. The waiting period means that if you change your mind about deleting the service, you can request to [restore the resources](https://docs.cloud.google.com/sql/docs/mysql/delete-instance#restore-deleted-cloud-sql-instance). If you try to delete the connection during the waiting period, the deletion fails with a message that the resources are still in use by the service producer.

  * You can't delete a private connection that's in use by a [producer VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-overview). To delete the connection, first delete the producer VPC spoke.




### Console

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Select the VPC network that contains the connections to delete.

  3. Select the **Private services access** tab.

  4. On the **Private services access** tab, select the **Private connection to services** tab.

  5. Select the private connection to delete.

  6. Click **Delete** to delete.

  7. Click **Delete** again to confirm the deletion.




###  gcloud 

To delete a private connection's VPC Network Peering connection, use the [`gcloud services vpc-peerings delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/delete).
    
    
    gcloud services vpc-peerings delete \
        --service=servicenetworking.googleapis.com \
        --network=VPC_NETWORK
    

Replace `VPC_NETWORK` with the name of your VPC network.

## Share private DNS zones with service producers

Cloud DNS private zones are private to your VPC network. If you want to let a service producer network resolve names from your private zone, you can configure DNS peering between the two networks.

When you configure DNS peering, you provide a VPC network and a DNS suffix. If the service producer needs to resolve an address with that DNS suffix, the service producer forwards those queries to your VPC network to be resolved.

These [supported services](https://docs.cloud.google.com/vpc/docs/private-services-access#private-services-supported-services) support DNS peering, with the exception of Cloud SQL.

If you want to enable DNS peering, you must [enable](https://console.cloud.google.com/apis/library/dns.googleapis.com) the [Cloud DNS API](https://docs.cloud.google.com/dns/docs/reference/v1) in your project.

### Peer DNS with a service producer

###  gcloud 

To set up DNS peering between your VPC network and the service provider network, use the [`gcloud services peered-dns-domains create` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/peered-dns-domains/create).
    
    
    gcloud services peered-dns-domains create PEERING_NAME \
        --network=VPC_NETWORK \
        --dns-suffix=DNS_SUFFIX
    

Replace the following:

  * `PEERING_NAME`: a name for this DNS peering configuration.

  * `VPC_NETWORK`: the name of your VPC network that is connected to the service producer using private services access.

  * `DNS_SUFFIX`: the DNS suffix you want to peer with the service producer. You must provide a complete DNS domain name, _including_ the dot. For example, `example.com.` is a valid DNS suffix.




###  Terraform 

To set up DNS peering between your VPC network and the service provider network, use the [`google_service_networking_peered_dns_domain` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_service_networking_peered_dns_domain).
    
    
    ## Uncomment this block after adding a valid DNS suffix
    
    # resource "google_service_networking_peered_dns_domain" "default" {
    #   name       = "example-com"
    #   network    = google_compute_network.peering_network.name
    #   dns_suffix = "example.com."
    #   service    = "servicenetworking.googleapis.com"
    # }
    

### List DNS peering configurations

###  gcloud 

Use the [`gcloud services peered-dns-domains list` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/peered-dns-domains/list).
    
    
    gcloud services peered-dns-domains list \
        --network=VPC_NETWORK
    

Replace `VPC_NETWORK` with the name of your VPC network.

### Delete a DNS peering configuration

###  gcloud 

Use the [`gcloud services peered-dns-domains delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/peered-dns-domains/delete).
    
    
    gcloud services peered-dns-domains delete PEERING_NAME \
        --network=VPC_NETWORK
    

Replace the following:

  * `PEERING_NAME`: the name of the DNS peering configuration.

  * `VPC_NETWORK`: the name of your VPC network.




## Configure hybrid connectivity

By default, the service producer's network only learns the subnet routes from your VPC network. Therefore, any request that's not from a subnet IP range is dropped by the service producer.

To configure connectivity between your on-premises hosts and the service producer's network, do the following:

  * In your VPC network, [update the peering connection](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#update-peer-connection) to export custom routes to the service producer's network. Exporting routes sends all [eligible static and dynamic routes](https://docs.cloud.google.com/vpc/docs/vpc-peering#route-exchange-options) that are in your VPC network, such as routes to your on-premises network, to the service producer's network. The service producer's network automatically imports them and then can send traffic back to your on-premises network through the VPC network.

When you export custom routes to the service producer's network, the service producer network learns those routes. If any of these learned routes overlap with the ranges used for [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access), traffic from the service producer network intended for Google services might be incorrectly routed over the peering connection to your network.

To prevent routing conflicts, do one of the following:

    * Avoid exporting custom routes that overlap with the ranges used for [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access).
    * Enable [VPC Service Controls](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/enable-vpc-service-controls) for your private services access connection. Enabling VPC Service Controls configures perimeter routing for Google services inside the perimeter, preventing routing conflicts caused by overlapping custom routes.
  * Ensure that the prefixes that include the allocated IP ranges for private services access are being correctly advertised to your on-premises network. To understand how you can advertise custom IPv4 prefixes using Cloud Router, see [Advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes).

  * Check that the VLAN attachment or Cloud VPN tunnel terminates in the same VPC network (or Shared VPC network) as the private connection because VPC Network Peering doesn't provide transitive routing.




## Troubleshooting

The following sections contain troubleshooting information for private services access.

### How much of my allocation is being used?

When you create a private connection with a service producer, you allocate an IP address range for them to use. If you use multiple services from a service producer, each service reserves a chunk of IP addresses from that allocated range. You can check which services are using which IP addresses so that, for example, you can see which services are using large blocks of IP addresses and avoid IP address exhaustion.

To view the allocation ratio for your allocated ranges, use Network Analyzer. For more information, see [Private services access IP address utilization summary](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/vpc-network/ip-utilization#psa-ip-allocation-ratio-summary).

Alternatively, to view which service is using a particular IP address range:

  1. List your private connections.
  2. Find the peering connection name that connects you to the relevant service producer.
  3. [List the routes](https://docs.cloud.google.com/vpc/docs/using-routes#listingroutes) for your VPC network.
  4. Find the routes with a next hop that match the peering connection name. The destination range of the routes indicates which IP addresses each service is using.



### IP address range exhaustion

For a given private connection, if you exhaust your allocated IP address space, Google Cloud returns this error: `Failed to create subnetwork. Couldn't find free blocks in allocated IP ranges.`

You might see this error because the allocated range isn't sufficient for your usage, or because a custom static or dynamic route is preventing the allocated range from being fully used. For more information about routing considerations, see Choose an IP address range for the allocated range.

You can expand the existing allocation or add new ones. The expanded allocation must be a contiguous IP address range that includes the existing range. We recommend expanding an allocation because there's no limit on the size of an allocation, but there is a limit on the number of allocations that you can create per project and per connection. For more information, see [Static global internal IPv4 addresses](https://docs.cloud.google.com/vpc/docs/quota#static-global-internal-ipv4-addresses) and [Allocated IP address ranges per private connection](https://docs.cloud.google.com/vpc/docs/quota#ip-ranges-per-private-connection).

To expand an existing allocation:

  1. List your private connections and record the name of the allocated range you need to expand.
  2. Delete the existing allocated range that you want to expand.
  3. Create a new allocated range by using the same name as the deleted range. Specify an IP address range that includes the deleted IP address range. That way, existing peered resources that are using the old allocated range can continue to use the same IP addresses without colliding with resources in your VPC network. For example, if the previous allocated range was `192.168.0.0/20`, create a new allocated range



To add allocated ranges to an existing private connection:

  1. Create a new allocated range. This range doesn't have to be contiguous with existing allocated ranges.
  2. Add the allocated range to the existing private connection.

**Important:** Don't delete an allocated range that is used by a private connection unless you need to replace it with a new, larger allocated range. Don't replace an allocated range that's in use with a smaller range. If you delete or shrink an allocated range that's in use, you prevent the service producer from being able to create new subnets on your behalf in their network.

### Service account permissions

If you see an error about the `compute.globalAddresses.list` permission for a project when creating an allocated range, or if you experience errors such as `Error 400: Precondition check failed` while creating, listing, or modifying private connections, it might be a problem with Identity and Access Management (IAM) roles for your Service Networking API [service account](https://docs.cloud.google.com/iam/docs/service-account-types#google-managed). This service account is created automatically after you enable the Service Networking API. It can take time for the account to be provisioned and display on the **IAM** page.

### Console

To ensure that the service account has the correct IAM role, do the following:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Select the **Include Google-provided role grants** checkbox.

  3. In the **Name** column, find the **Service Networking Service Agent** principal, and then click edit**Edit principal** in the corresponding row.

  4. In the **Role** field, ensure that the **Service Networking Service Agent** role (`roles/servicenetworking.serviceAgent`) is present.

  5. If the **Service Networking Service Agent** role is not present, click either add**Add role** or add**Add another role**.

  6. Click **Select a role**.

  7. In the **Filter** text box, enter `Service Networking Service Agent`.

  8. Select **Service Networking Service Agent** from the list, and then click **Save**.




###  gcloud 

To create a Service Networking API service account, use the [`gcloud projects add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding).
    
    
    gcloud projects add-iam-policy-binding HOST_PROJECT_NAME \
        --member=serviceAccount:service-HOST_PROJECT_NUMBER@service-networking.iam.gserviceaccount.com \
        --role=roles/servicenetworking.serviceAgent

Replace the following:

  * `HOST_PROJECT_NAME`: the name of the host project.
  * `HOST_PROJECT_NUMBER`: the number of the host project.



### Peering subnet route persists after updating allocated range

After you update the allocated IP address range of a private services connection, the old peering subnet route might still appear in the routing table of your VPC network. The route persists because the IP address range is still in use.

To resolve this issue, do the following:

  * Make sure that if you delete an allocated range, that you also update the private connection.
  * Delete or update any resources that use the old IP address range.



The peering subnet route is removed automatically after the IP address range is no longer in use. There might be a delay between deleting the resource, and the service producer fully deleting the resource. For example, if the old IP address range is being used by a Cloud SQL instance, it can take up to four days for the service producer to fully delete your instance. The peering subnet route is removed after the deletion is complete.

### Unable to create a new private connection

If you attempt to create a new private connection after deleting the VPC Network Peering connection associated with a previous private connection, Google Cloud might return an error. For troubleshooting information, see the following error messages.

To prevent this issue from happening, follow the procedure to delete a private connection instead of deleting the associated VPC Network Peering connection directly.

  * Cannot modify allocated ranges error: 
        
        ERROR: Cannot modify allocated ranges in CreateConnection. Please use UpdateConnection. Existing allocated IP ranges: ALLOCATED_RANGE_NAMES.

If you get this error, do the following:

    1. Recreate the private connection that you deleted and use the allocated range names returned by the error. You must use the same allocated range names when recreating the connection, but the corresponding IP address ranges (CIDR blocks) can be the same or different.

To create the private connection, see Create a private connection.

    2. If necessary, modify the private connection to add or remove allocated ranges. You might want to use different allocated ranges than the allocated ranges that you specified when you recreated the private connection in the previous step.

To modify the private connection, see Modify a private connection.

  * Transient internal error:
        
        ERROR: (gcloud.services.vpc-peerings.connect) The operation "operations/OPERATION_ID"
        resulted in a failure "encountered some transient internal error, please try again later"

If you get this error, contact [Cloud Support](https://console.cloud.google.com/support?referrer=PlatformBarHelp).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
