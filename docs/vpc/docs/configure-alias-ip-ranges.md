---
url: https://docs.cloud.google.com/vpc/docs/configure-alias-ip-ranges/
title: Configure alias IP ranges \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:16.667271+00:00
---

# Configure alias IP ranges  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/configure-alias-ip-ranges/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure alias IP ranges

This document contains instructions for configuring alias IP addresses and alias IP ranges by using the Google Cloud console and the Google Cloud CLI. Before executing these commands, review [Alias IP ranges](https://docs.cloud.google.com/vpc/docs/alias-ip).

## Limitations

### Subnet

  * The per network [limits](https://docs.cloud.google.com/vpc/docs/quota#per_network) describe the maximum number of secondary ranges that you can define for each subnet.
  * You cannot add _and_ remove secondary ranges at the same time. Adding and removing must be done as separate steps.
  * CIDR expansion isn't supported for secondary ranges.



### VM instance

  * Alias IP ranges are supported on all virtual machine (VM) network interfaces. Routing is configured automatically for alias IP ranges on the primary network interface but not on secondary interfaces. If you have [multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts), you must configure policy routing for the additional interfaces. For an example of how to do this, see the following tutorial: [Configure routing for an additional network interface](https://docs.cloud.google.com/vpc/docs/configure-routing-additional-interface).
  * Alias IP ranges can be added or deleted, but they can't be updated.
  * If you remove an alias IP range from one VM and assign it to another VM, it might take up to a minute for the transfer to complete.
  * Firewall source tags aren't supported for alias IP addresses. This means that when you configure source tags in firewall rules, the source tags match the VM primary IP address but not the alias IP addresses. Use source ranges to allow or deny ingress traffic from alias IP addresses.
  * Internal DNS resolves a VM name to its primary IP. Additional names for alias IPs aren't configured automatically but might be added manually.



### VPC network

  * Adding or removing a large number of alias IP ranges at the same time can take a long time. For example, it might take up to 10 minutes to add or delete 7,000 alias IP ranges.
  * Auto mode Virtual Private Cloud (VPC) networks can't be deleted if secondary subnet ranges are present.
  * In a static route, the next-hop IP address must be the primary IP address of the VM. Alias IP addresses aren't supported as next-hop IP addresses.
  * IPv6 addresses aren't supported.
  * Alias IP ranges are only supported in VPC networks, not legacy networks. To determine your network type, list your networks. VPC networks have a mode of `custom` or `auto`. Legacy networks have a mode of `legacy`.



## Subnet commands

VM alias IP ranges must be assigned from a range owned by the subnet that the VM is in. All subnets have a primary range, which is the standard range of internal IP addresses that defines the subnet. A subnet can also have one or more secondary IP ranges of internal IP addresses. You can assign alias IP ranges from either the primary or secondary ranges of the subnet.

You must give each secondary range a name that is unique for the subnet. When assigning an alias IP range to a VM, the secondary range name tells Google Cloud from which subnet range to assign the alias IPs.

All ranges, both primary and secondary, must be unique across all subnets in the VPC network and in any networks attached by using VPC Network Peering, Cloud VPN, or Cloud Interconnect.

This section shows you how to create a subnet with a secondary range, add a secondary range to an existing subnet, or remove a secondary range from a subnet. After your subnet has the range you want to use, see the Work with VM instances section for information about assigning a range to a VM.

### Create a subnet with one or more secondary CIDR ranges

This command assumes you have a VPC network already. If you do _not_ , [create one](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

This command is the same whether you are creating a subnet for the VM's primary interface or one of the [secondary interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts).

Using a secondary range for alias IP allocation lets you separate the IP space for services hosted in the VM, which helps you create firewall rules that allow access only to the services running on the VM and block access to the VM's primary IP address.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of an existing network.

  3. Click **Add subnet**.

  4. Enter a name for the new subnet.

  5. Specify the region.

  6. Enter an IP address range in CIDR notation—for example, `10.65.61.0/24`.

  7. Click **Create secondary IP range**.

  8. Enter a subnet range name.

  9. Enter a secondary IP range in CIDR notation—for example, `10.9.0.0/24`.

  10. To add secondary IP ranges, for each range, click **Add IP range** , then provide a name and range.

  11. Click **Add**.




###  gcloud 
    
    
    gcloud compute networks subnets create s1 \
        --network NETWORK_NAME \
        --region REGION \
        --range 10.65.61.0/24 \
        --secondary-range RANGE_NAME_1=RANGE_CIDR_1,RANGE_NAME_2=RANGE_CIDR_2,...
    

Replace the following:

  * `NETWORK_NAME`: the name of the network where you want to create the subnet.
  * `REGION`: the region where you are creating the subnet.
  * `RANGE_NAME_1`=`RANGE_CIDR_1` and `RANGE_NAME_2`=`RANGE_CIDR_2`: the names of the secondary ranges from which to draw the alias IP ranges and the alias IP range itself—for example, `range1=10.9.0.0/24`.



For the complete syntax, see the [`gcloud` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).

###  API 

Create a subnet with one or more secondary ranges.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks
    {
      "ipCidrRange": "PRIMARY_IP_RANGE",
      "network": "NETWORK_URL",
      "name": "SUBNET_NAME",
      "secondaryIpRanges": [
      {
        "rangeName": "SECONDARY_RANGE_NAME_1",
        "ipCidrRange": "SECONDARY_IP_RANGE_1"
      },
      {
        "rangeName": "SECONDARY_RANGE_NAME_2",
        "ipCidrRange": "SECONDARY_IP_RANGE_2"
      },
      ...]
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the VPC network where the subnet is to be created.
  * `REGION`: the region where the subnet is to be located.
  * `PRIMARY_IP_RANGE`: the primary IP address range for the subnet.
  * `NETWORK_URL`: the URL or the VPC network where the subnet is to be created.
  * `SUBNET_NAME`: a name for the subnet.
  * `SECONDARY_RANGE_NAME_1` and `SECONDARY_RANGE_NAME_2`: the names to use for the secondary ranges.
  * `SECONDARY_IP_RANGE_1` and `SECONDARY_IP_RANGE_2`: the IP address ranges to use for the secondary ranges.



For more information, see the [`subnetworks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/insert).

### Terraform

You can use the [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_subnetwork) to create a subnet with one or more secondary ranges.

The Terraform arguments have example values that you can change.
    
    
    resource "google_compute_subnetwork" "network-with-private-secondary-ip-ranges" {
      project       = var.project_id # Replace this with your project ID in quotes
      name          = "test-subnetwork"
      ip_cidr_range = "10.2.0.0/16"
      region        = "us-central1"
      network       = "test-vpc-network"
      secondary_ip_range {
        range_name    = "tf-test-secondary-range-update1"
        ip_cidr_range = "192.168.10.0/24"
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

### Add secondary CIDR ranges to an existing subnet

This procedure assumes you have a subnet that you want to use, but you need to add one or more secondary ranges.

We recommend using a secondary range for alias IP allocation to create firewall rules that allow access to the services running on a VM, but not to the VM's primary IP address.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of a subnet to modify to view its details page.

  3. Click **Edit**.

  4. In the **Secondary IP ranges** section, click **Add IP range**.

  5. Enter a name for **Subnet range name**.

  6. Enter a range for **Secondary IP range** in CIDR notation—for example, `10.9.0.0/24`.

  7. To add secondary IP ranges, for each range, click **Add IP range** , then provide a name and range.

  8. Click **Save**.




###  gcloud 
    
    
    gcloud compute networks subnets update SUBNET_NAME \
        --region REGION \
        --add-secondary-ranges RANGE_NAME_1=RANGE_CIDR_1,RANGE_NAME_2=RANGE_CIDR_2,...
    

Replace the following:

  * `SUBNET_NAME`: the name of the subnet that you want to add the secondary ranges to.
  * `REGION`: the region where you are creating the subnet.
  * `RANGE_NAME_1`=`RANGE_CIDR_1` and `RANGE_NAME_2`=`RANGE_CIDR_2`: the names of the secondary ranges from which to draw the alias IP ranges and the alias IP range itself—for example, `range1=10.9.0.0/24`.



For the complete syntax, see the [`gcloud` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update).

###  API 

Add a secondary range to an existing subnet.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME
    {
      "secondaryIpRanges": [
      {
        "rangeName": "SECONDARY_RANGE_NAME_1",
        "ipCidrRange": "SECONDARY_IP_RANGE_1"
      },
      {
        "rangeName": "SECONDARY_RANGE_NAME_2",
        "ipCidrRange": "SECONDARY_IP_RANGE_2"
      },
      ...],
      "fingerprint": "SUBNET_FINGERPRINT"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the subnet to modify.
  * `REGION`: the region where the subnet is located.
  * `SUBNET_NAME`: the name of the subnet to modify.
  * `SECONDARY_RANGE_NAME_1` and `SECONDARY_RANGE_NAME_2`: the names to use for the secondary ranges.
  * `SECONDARY_IP_RANGE_1` and `SECONDARY_IP_RANGE_2`: the IP address ranges to use for the secondary ranges.
  * `SUBNET_FINGERPRINT`: the fingerprint ID for the existing subnet, which is provided when you [describe a subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#describing_an_existing_subnet).



For more information, see the [`subnetworks.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/patch).

### Remove a secondary CIDR range from a subnet

You can remove existing secondary ranges from a subnet. To view the ranges that are associated with a subnet, see [Describe a subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#describing_an_existing_subnet).

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of a subnet to modify to view its details page.

  3. Click **Edit**.

  4. In the **Secondary IP ranges** section, click **X** next to the secondary range to remove.

  5. Click **Save**.




###  gcloud 
    
    
    gcloud compute networks subnets update SUBNET_NAME \
        --region REGION \
        --remove-secondary-ranges RANGE_NAME_1,RANGE_NAME_2,...
    

Replace the following:

  * `SUBNET_NAME`: the name of the subnet that you want to remove the secondary ranges from.
  * `REGION`: the region where you are creating the subnet.
  * `RANGE_NAME_1` and `RANGE_NAME_2`: the names of the secondary ranges to be removed from the target subnet `SUBNET_NAME`—for example, `range1=10.9.0.0/24`.



For the complete syntax, see the [`gcloud` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update).

###  API 

Exclude secondary ranges to remove them. The following example removes all secondary ranges from an existing subnet:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME
    {
      "fingerprint": "SUBNET_FINGERPRINT",
      "secondaryIpRanges": [
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the subnet to modify.
  * `REGION`: the region where the subnet is located.
  * `SUBNET_NAME`: the name of the subnet to modify.
  * `SUBNET_FINGERPRINT`: the fingerprint ID for the existing subnet, which is provided when you [describe a subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#describing_an_existing_subnet).



For more information, see the [`subnetworks.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/patch).

## Work with VM instances

These commands show how to create an instance with an alias IP range, add one or more alias IP ranges to an existing VM instance, or remove one or more ranges from an existing VM instance.

### Create a VM with an alias IP range in the primary CIDR range

Use this procedure if you want to assign an alias IP range from the primary range of the subnet. The range you choose must not already be in use, even in part, by any other resource on the VPC network.

Use this procedure if you want the instance's primary interface and alias IP addresses to be in the same range.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click add_box**Create instance**.

  3. Enter a name for the new instance.

  4. Specify a zone.

  5. Click **Networking**.

  6. In the **Network interfaces** section, expand the default network interface.

  7. In **Alias IP ranges** , click add**Add IP range**.

  8. Leave **Subnet range 1** set to **Primary**.

  9. In **Alias IP range** , enter an IP range in CIDR notation. This range must be an unused subrange of the primary range.

  10. Click **Create**.




###  gcloud 
    
    
    gcloud compute instances create vm1 \
        --zone ZONE \
        --network-interface "subnet=SUBNET_NAME,aliases=RANGE_CIDR_1;RANGE_CIDR_2,..."
    

Replace the following:

  * `ZONE`: the zone to contain the instance.
  * `SUBNET_NAME`: the name of the subnet to contain the instance.
  * `RANGE_CIDR_1` and `RANGE_CIDR_2`: the IP ranges from the primary subnet to assign to the interface. The ranges can be a specific range (`192.168.100.0/24`), a single IP address (`192.168.100.1`), or a netmask in CIDR format (`/24`). If the IP range is specified by netmask only, the IP allocator chooses an available range with the specified netmask and allocates it to the network interface. To specify more than one range, separate the ranges with semicolons (`;`).



For the complete syntax, see the [`gcloud` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).

###  API 

Create an instance with an alias IP address from the primary IP address range of the instance's subnet.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    {
      "networkInterfaces": [
        {
          "aliasIpRanges": [
            {
              "ipCidrRange": "CIDR_RANGE"
            }
          ]
        },
        ...
      ],
      ...
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you create the instance.
  * `ZONE`: the Google Cloud zone where the instance is to be created.
  * `CIDR_RANGE`: the IP range from the primary subnet to assign to the interface. The range can be a specific range (`192.168.100.0/24`), a single IP address (`192.168.100.1`), or a netmask in CIDR format (`/24`). If you specify the IP range by netmask only, the IP address allocator chooses an available range with the specified netmask and assigns it to the network interface.



For more information, see the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).

### Create a VM with an alias IP range in a secondary CIDR range

Use this procedure if you want to assign an alias IP range taken from a secondary range of the subnet. We recommend keeping the alias IP ranges separate from the primary range of the subnet to create firewall rules that allow access to the services running on a VM, but not to the VM's primary IP address.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click add_box**Create instance**.

  3. Enter a name for the new instance.

  4. Specify a zone.

  5. Click **Networking**.

  6. In the **Network interfaces** section, expand the default network interface.

  7. In **Alias IP ranges** , click add**Add IP range**.

  8. In **Subnet range** , select the secondary IP range to use.

  9. For **Alias IP range** , enter an IP range in CIDR notation. This range must be an unused range of the secondary IP range.

  10. Click **Create**.




###  gcloud 
    
    
    gcloud compute instances create vm3 \
        --zone ZONE \
        --network-interface subnet=SUBNET_NAME,aliases=RANGE_NAME:RANGE_CIDR
     

Replace the following:

  * `ZONE`: the zone to contain the instance.
  * `SUBNET_NAME`: the name of the subnet to contain the instance.
  * `RANGE_NAME`: the name of the subnet secondary range from which to draw the alias IP range.
  * `RANGE_CIDR`: the IP range to assign to the interface. The range can be a specific range (`192.168.100.0/24`), a single IP address (`192.168.100.1`), or a netmask in CIDR format (`/24`). If the IP range is specified by netmask only, the IP allocator chooses an available range with the specified netmask and allocates it to the network interface.



For the complete syntax , see the [`gcloud` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).

###  API 

Create an instance with an alias IP address from the secondary IP address range of the instance's subnet.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    {
      "networkInterfaces": [
        {
          "aliasIpRanges": [
            {
              "ipCidrRange": "SECONDARY_CIDR_RANGE",
              "subnetworkRangeName": "SECONDARY_RANGE_NAME"
            }
          ]
        },
        ...
      ],
      ...
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you create the instance.
  * `ZONE`: the Google Cloud zone where you create the instance.
  * `SECONDARY_CIDR_RANGE: the IP range to assign to the interface. The range can be a specific range (`192.168.100.0/24`), a single IP address (`192.168.100.1`), or a netmask in CIDR format (`/24`). If you specify the IP range by netmask only, the IP address allocator chooses an available range with the specified netmask and assigns it to the network interface.
  * `SECONDARY_RANGE_NAME`: the name of the subnet secondary range from which to draw the alias IP range.



For more information, see the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).

### Create a VM with multiple interfaces and alias IP addresses

This example creates two networks, each with one subnet, and a VM with interfaces in both networks. If you already have two VPC networks, you can skip to the "Create a VM with interfaces in both networks" step.

###  Console 

Create the first network and subnet:

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `my-network1`.

  4. Set **Subnet creation mode** to `Custom`, then specify a subnet name of `my-subnet1`.

  5. Specify a region.

  6. Set **IP address range** to `172.16.1.0/24`.

  7. Click **Create secondary IP range**.

  8. Set **Subnet range name** to `range1`.

  9. Set **Secondary IP range** to `10.1.0.0/16`.

  10. Click **Done**.

  11. Click **Create**.




Create the second network and subnet:

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. For **Name** , enter `my-network2`.

  4. Set **Subnet creation mode** to `Custom`, then specify a subnet name of `my-subnet2`.

  5. For **Region** , specify the same region as you did for the first network and subnet.

  6. Set **IP address range** to `172.16.2.0/24`.

  7. Click **Create secondary IP range**.

  8. Set **Subnet range name** to`range2`.

  9. Set **Secondary IP range** to `10.2.0.0/16`.

  10. Click **Done**.

  11. Click **Create**.




Create a VM with interfaces in both networks:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click add_box**Create instance**.

  3. Set the zone to the region where you created the subnets.

  4. Click **Networking**.

  5. Click the first network interface.

     1. Set **Network** to `my-network1`.
     2. Set **Subnetwork** to `my-subnet1`.
     3. Click **Alias IP ranges**.
     4. Click **Add IP range**.
     5. Set **Subnet range** to `Primary`.
     6. Set **Alias IP range** to `/32`.
     7. Click **Add IP range**.
     8. Set **Subnet range** to `range1`.
     9. Set **Alias IP range** to `/24`.
     10. Click **Done**.
  6. Click **Add network interface**.

     1. Select `my-network2`.
     2. Set **Subnetwork** to `my-subnet2`.
     3. Click **Alias IP ranges**.
     4. Click **Add IP range**.
     5. Set **Subnet range** to `Primary`.
     6. Set **Alias IP range** to `/32`.
     7. Click **Add IP range**.
     8. Set **Subnet range** to `range2`.
     9. Set **Alias IP range** to `/24`.
     10. Click **Done**.
  7. Click **Create**.




###  gcloud 

  1. Create the first network:
         
         gcloud compute networks create my-network1 --subnet-mode CUSTOM
         

  2. Add a subnet:
         
         gcloud compute networks subnets create my-subnet1 \
             --network my-network1 \
             --range 172.16.1.0/24 \
             --secondary-range range1=10.1.0.0/16
         

  3. Create a second network:
         
         gcloud compute networks create my-network2 --subnet-mode CUSTOM
         

  4. Add a subnet:
         
         gcloud compute networks subnets create my-subnet2 \
             --network my-network2 \
             --range 172.16.2.0/24 \
             --secondary-range range2=10.2.0.0/16
         

  5. Create a VM with interfaces in both networks. The first network interface listed, the one in `my-subnet1`, is the primary interface:
         
         gcloud compute instances create multi-nic-alias-vm \
             --machine-type f1-micro \
             --network-interface "subnet=my-subnet1,aliases=/32;range1:/24" \
             --network-interface "subnet=my-subnet2,aliases=/32;range2:/24"
         

  6. Use the display command to see the interfaces and their addresses:
         
         gcloud compute instances describe multi-nic-alias-vm
         
         
         ...
         networkInterfaces:
         - ...
           aliasIpRanges:
           - ipCidrRange: 172.16.1.2/32
           - ipCidrRange: 10.1.0.0/24
             subnetworkRangeName: range1
           name: nic0
           network: .../networks/my-network1
           networkIP: 172.16.1.3
           subnetwork: .../subnetworks/my-subnet1
           ...
         - ...
           aliasIpRanges:
           - ipCidrRange: 172.16.2.2/32
           - ipCidrRange: 10.2.0.0/24
             subnetworkRangeName: range2
           name: nic1
           network: .../networks/my-network2
           networkIP: 172.16.2.3
           subnetwork: .../subnetworks/my-subnet2
           




###  API 

  1. Create two custom mode VPC networks named `my-network1` and `my-network2`. For more information, see [Create a custom mode VPC network with only IPv4 subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network).

  2. Add subnets to the VPC networks. For more information, see [Add an IPv4-only subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnets).

     1. Add a subnet named `my-subnet1` to `my-network1`. Specify `172.16.1.0/24` for the primary range and `10.1.0.0/16` for the secondary range with the name `range1`.

     2. Add a subnet named `my-subnet2` to `my-network2`. Specify `172.16.2.0/24` for the primary range and `10.2.0.0/16` for the secondary range with the name `range2`.

  3. Create a VM instance with interfaces in both networks.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
         {
           "networkInterfaces": [
             {
               "subnetwork": "projects/PROJECT_ID/regions/REGION/subnetworks/my-subnet1",
               "aliasIpRanges": [
                 {
                   "ipCidrRange": "/32",
                 },
                 {
                   "subnetworkRangeName": "range1",
                   "ipCidrRange": "/24"
                 }
               ]
             },
             {
               "subnetwork": "projects/PROJECT_ID/regions/REGION/subnetworks/my-subnet2",
               "aliasIpRanges": [
                 {
                   "ipCidrRange": "/32",
                 },
                 {
                   "subnetworkRangeName": "range2",
                   "ipCidrRange": "/24"
                 }
               ]
             }
           ],
           ...
         }
         

Replace the following:

     * `PROJECT_ID`: the ID of the project where you create the instance.
     * `ZONE`: the Google Cloud zone where the instance is to be created.
     * `REGION`: the Google Cloud region where the subnet is located. The subnets must be in the same region as the instance.

For more information, see the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).




### Add alias IP ranges to an existing instance

You can add an alias IP range to a running instance.

The new addresses might not be available immediately, even after the API call has finished. New addresses are available only after the guest OS has added the addresses and routes.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of an existing instance.

  3. Click **Edit**.

  4. In **Network interfaces** , click the network interface to which to add an alias IP range (**`nic0`** for this example).

  5. Click **Alias IP ranges**.

  6. Click **Add IP range**.

  7. Select a **Subnet range**.

  8. Enter an alias IP range.

  9. Click **Done**.

  10. Click **Save**.




###  gcloud 
    
    
    gcloud compute instances network-interfaces update INSTANCE_NAME \
        --zone ZONE \
        [--network-interface NETWORK_INTERFACE; default="nic0"] \
        --aliases "RANGE_NAME_1:RANGE_CIDR_1; \
        RANGE_NAME_2:RANGE_CIDR_2;..."
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance to modify.
  * `ZONE`: the zone that contains the instance.
  * `NETWORK_INTERFACE`: the name of the network interface to which to add an alias IP address range.
  * `RANGE_NAME_1` and `RANGE_NAME_2`: the names of the subnet secondary ranges from which to draw the alias IP range. If you are assigning ranges from the subnet's primary range, omit this value.
  * `RANGE_CIDR_1` and `RANGE_CIDR_2`: the IP ranges to assign to the interface. The ranges can be a specific range (`192.168.100.0/24`), a single IP address (`192.168.100.1`), or a netmask in CIDR format (`/24`). If the IP range is specified by netmask only, the IP allocator chooses an available range with the specified netmask and allocates it to the network interface.



For the complete syntax, see the [`gcloud` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/network-interfaces/update).

###  API 

Add alias IP ranges to an existing instance.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/updateNetworkInterface?networkInterface=NETWORK_INTERFACE_NAME
    {
      "aliasIpRanges": [
        {
          "ipCidrRange": "SECONDARY_IP_RANGE",
          "subnetworkRangeName": "SECONDARY_RANGE_NAME"
        },
        existing ranges...
      ],
      "fingerprint": "INTERFACE_FINGERPRINT"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the instance to modify.
  * `ZONE`: the Google Cloud zone in which to create the instance.
  * `INSTANCE_NAME`: the name of the instance to modify.
  * `NETWORK_INTERFACE_NAME`: the name of the instance's network interface to modify.
  * `SECONDARY_IP_RANGE`: the IP range to assign to the interface. The range can be a specific range (`192.168.100.0/24`), a single IP address (`192.168.100.1`), or a netmask in CIDR format (`/24`). If you specify the IP range by netmask only, the IP address allocator chooses an available range with the specified netmask and assigns it to the network interface.
  * `SECONDARY_RANGE_NAME`: the name of the subnet secondary range from which to draw the alias IP range. If you are assigning ranges from the subnet's primary range, omit this field.
  * `INTERFACE_FINGERPRINT`: the fingerprint ID for the existing network interface, which is provided when you describe an instance.



For more information, see the [`instances.updateNetworkInterface` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/updateNetworkInterface).

### Modify alias IP ranges for an existing instance

You can add more alias IP ranges to an existing instance or remove one or more ranges.

The address changes might not be visible immediately. The API call must finish and the guest OS must modify the addresses and routes.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of an existing instance.

  3. Click **Edit**.

  4. In **Network interfaces** , click the network interface to which to add an alias IP range (**`nic0`** for this example).

  5. Click **Alias IP ranges**.

  6. To add an alias IP range, click **Add Alias IP range**.

  7. To remove an alias IP range, click the **X** next to the alias IP range.

  8. Click **Done**.

  9. Click **Save**.




###  gcloud 
    
    
    gcloud compute instances network-interfaces update INSTANCE_NAME \
        --zone ZONE \
        [--network-interface NETWORK_INTERFACE; default="nic0"] \
        --aliases "RANGES_TO_RETAIN;NEW_RANGE_NAME:NEW_RANGE_CIDR;..."
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance to modify.
  * `ZONE`: the zone that contains the instance.
  * `NETWORK_INTERFACE`: the name of the network interface to modify.
  * `RANGES_TO_RETAIN`: the existing ranges, in `CURRENT_RANGE_NAME`: `CURRENT_RANGE_CIDR` format, that you want to keep. If you are adding ranges to an instance that doesn't have any, these values are blank. If you are removing all ranges from the instance, the entire `--aliases` field is blank.
  * `NEW_RANGE_NAME`: the name of the subnet secondary range from which to draw any new alias IP ranges. If you are assigning ranges from the subnet's primary range, omit this value.
  * `NEW_RANGE_CIDR`: the IP address range to assign to the interface. This range can be a specific range (`192.168.100.0/24`), a single IP address (`192.168.100.1`), or a netmask in CIDR format (`/24`). If the IP address range is specified by netmask only, the IP allocator chooses an available range with the specified netmask and allocates it to the network interface.



To add ranges, run the command and specify all the existing and all the new alias IP ranges. Pairs are separated by semicolons—for example: `--aliases "CURRENT_RANGE_NAME:CURRENT_RANGE_CIDR;NEW_RANGE_NAME:NEW_RANGE_CIDR"`.

To remove ranges, run the command and specify only the alias IP ranges that you want to keep. If you are keeping ranges from a secondary range, you must specify the name of the secondary range. A CIDR range can be a specific range (`192.168.100.0/24`) or a single IP address (`192.168.100.1`)—for example: `--aliases "RANGE_NAME:RANGE_CIDR;RANGE_CIDR"`.

To remove all ranges, run the command and specify the `--aliases` flag, but use quotes to provide a blank input—for example: `--aliases ""`.

You cannot add and remove ranges in the same `gcloud` command. To remove some ranges and add others with the gcloud CLI, first run the command to remove unneeded ranges, and then run it again to add needed ranges.

For the complete syntax, see the [`gcloud` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/network-interfaces/update).

###  API 

For a network interface of an existing instance, add or remove alias IP address ranges.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/updateNetworkInterface?networkInterface=NETWORK_INTERFACE_NAME
    {
      "aliasIpRanges": [
        include new and existing ranges to add them...
        exclude existing ranges to remove them...
      ],
      "fingerprint": "INTERFACE_FINGERPRINT"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the instance to modify.
  * `ZONE`: the zone that contains the instance.
  * `INSTANCE_NAME`: the name of the instance to modify.
  * `NETWORK_INTERFACE_NAME`: the name of the instance's network interface to modify.
  * `INTERFACE_FINGERPRINT`: the fingerprint ID for the existing network interface, which is provided when you describe an instance.



For more information, see the [`instances.updateNetworkInterface` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/updateNetworkInterface).

## Troubleshooting

This section lists various issues that you might encounter when configuring alias IP ranges.

### Cannot create VM instance with alias IP

  1. Verify that the network is a VPC network. Alias IPs aren't supported on legacy networks.
         
         gcloud compute networks list --filter="name=NETWORK_NAME"
         

The network `MODE` must be `auto` or `custom`.

  2. If a subnet range name is specified, verify the following:
         
         gcloud compute networks subnets describe SUBNET_NAME --region=REGION
         

     * The subnet has a secondary range with the corresponding name.
     * The requested alias IP range is inside this secondary range or, if using netmask, is smaller than the primary range.
  3. If subnet range name isn't specified, verify that the requested alias IP range is inside the primary subnet range or, if using netmask, is smaller than the primary range.




### Cannot connect to alias IP

  1. Verify firewall rules.

     1. List all firewall-rules:
            
            gcloud compute firewall-rules list --format=json
            

     2. Verify that traffic to and from an alias IP range is allowed.

**Note:** Source service account and source tags only expand to primary network IP addresses of matching instances.
     3. If necessary, add firewall rules to allow pinging an alias IP range:
            
            gcloud compute firewall-rules create FIREWALL_NAME1 \
                --network NETWORK_NAME \
                --priority 0 \
                --source-ranges ALIAS_IP \
                --allow icmp
            
            
            gcloud compute firewall-rules create FIREWALL_NAME2 \
                --network NETWORK_NAME \
                --priority 0 \
                --direction out \
                --destination-ranges ALIAS_IP \
                --allow icmp
            

  2. Ensure that the VM recognizes the IP alias ranges as being local. On Linux distributions such as Debian, this can typically be done as follows.

     1. [Connect to the instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) and run this command:
            
            ip route show table local
            

The output is similar to the following:
            
            local ALIAS_IP_RANGE dev eth0  proto 66  scope host
            

     2. In `/etc/default/instance_configs.cfg`, ensure that the `ip_aliases` setting is set to `true`. If you need to change this, you must also restart the guest agent:
            
            systemctl restart google-guest-agent
            

     3. If the local route is not present, configure it using this command:
            
            ip route add to local ALIAS_IP_RANGE dev eth0 proto 66
            




### Auto-starting service doesn't bind to alias IP address

On supported Linux distributions, alias IP addresses are automatically set as local addresses by the preinstalled guest agent. This means that no OS-level configuration is needed.

However, this also means that the OS doesn't recognize the alias IP addresses as local addresses before the guest agent is running. If you have auto-starting services on your VM and they start before the guest agent, they can't bind to the alias IP addresses.

For example, an Apache HTTP server might exit with the following error:
    
    
    could not bind to address ALIAS_IP:80
    

To solve this issue, configure your service to start after the guest agent. On distributions that use `systemctl`, use the following steps.

  1. As a privileged user, run the following command to add a drop-in snippet for the service that is not working correctly—for example, an Apache HTTP Server on Debian would be `apache2`:
         
         systemctl edit YOUR_SERVICE
         

  2. In the text editor, add the following lines. Make sure that you add the lines above the line reading `Lines below this comment will be discarded`.
         
         [Unit]
         After=google-guest-agent.service
         




### My secondary IP range isn't listed

Secondary IP ranges aren't listed as regular subnets. To verify that the subnet secondary IP range is created, use the `gcloud compute networks subnets describe` command.

  1. Create a subnet.
         
         gcloud compute networks subnets create my-subnet \
             --region us-central1 \
             --network my-network \
             --range 10.9.0.0/16 \
             --secondary-range secondaryrange1=172.16.0.0/12
         

The output is similar to the following:
         
         Created [https://www.googleapis.com/compute/v1/projects/google.com:my-project/regions/us-central1/subnetworks/my-subnet].
         NAME       REGION       NETWORK     RANGE
         my-subnet  us-central1  my-network  10.9.0.0/16
         

  2. List your subnets.
         
         gcloud compute networks subnets list
         

The output is similar to the following:
         
         NAME       REGION       NETWORK     RANGE
         my-subnet  us-central1  my-network  10.9.0.0/16
         

  3. Get details on a subnet to see the secondary ranges.
         
         gcloud compute networks subnets describe my-subnet --region us-central1
         

The output is similar to the following:
         
         ...
         ipCidrRange: 10.9.0.0/16
         ...
         secondaryIpRanges:
         - ipCidrRange: 172.16.0.0/12
           rangeName: secondaryrange1
         ...
         




### The specified subnet secondary range doesn't exist

When creating a VM, if you get an error saying that the secondary range doesn't exist, ensure the following:

  * The subnet has a secondary range with the specified name.
  * You are creating your VM within the subnet that has the secondary range.



You can see this error by running the following commands:

  1. Create a subnet with a secondary range.
         
         gcloud compute networks subnets create my-subnet \
             --region us-central1 \
             --network my-network \
             --range 10.9.0.0/16 \
             --secondary-range secondaryrange1=172.16.0.0/12
         

The output is similar to the following:
         
         Created [https://www.googleapis.com/compute/v1/projects/google.com:my-project/regions/us-central1/subnetworks/my-subnet].
         NAME       REGION       NETWORK     RANGE
         my-subnet  us-central1  my-network  10.9.0.0/16
         

  2. Create an instance in another network, such as the default network, rather than in the newly created subnet.
         
         gcloud compute instances create instance-1 \
             --zone us-central1-a \
             --network default
         

The output is similar to the following:
         
         Created [https://www.googleapis.com/compute/v1/projects/google.com:my-project/zones/us-central1-a/instances/instance-1].
         NAME        ZONE           MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP    STATUS
         instance-1  us-central1-a  n1-standard-1               10.128.0.2     47.82.96.9  RUNNING
         

  3. Try to assign an alias IP range from the subnet created in step 1. The command fails because the secondary range is in a different subnet from the instance.
         
         gcloud compute instances network-interfaces update instance-1 \
             --zone us-central1-a \
             --aliases secondaryrange1:172.16.0.10/32
         

The output is similar to the following:
         
         ERROR: (gcloud.compute.instances.network-interfaces.update) HTTPError 400: Invalid value for field 'resource.aliasIpRanges[0].subnetworkRangeName': 'secondaryrange'. The specified subnetwork secondary range does not exist.
         

  4. Create another instance, this one with its interface in the subnet created in step 1.
         
         gcloud compute instances create instance-2 \
             --zone us-central1-a \
             --network-interface subnet=my-subnet
         

The output is similar to the following:
         
         Created [https://www.googleapis.com/compute/v1/projects/google.com:my-project/zones/us-central1-a/instances/instance-2].
         NAME        ZONE           MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP    STATUS
         instance-2  us-central1-a  n1-standard-1               10.9.0.2     38.74.204.89  RUNNING
         

  5. Add an alias IP range to the interface. This time, the command succeeds because the interface and the secondary range are in the same subnet.
         
         gcloud compute instances network-interfaces update instance-2 \
             --zone us-central1-a \
             --aliases secondaryrange1:172.16.0.10/32
         

The output is similar to the following:
         
         Updating network interface [nic0] of instance [instance-2]...done.
         




### Can't add and remove secondary IP ranges in the same request

Adding and removing subnetwork secondary IP ranges in the same command isn't supported. The gcloud CLI commands to add and remove secondary ranges preserve the existing ranges that aren't modified.

To add and remove ranges, run the two commands separately.
    
    
    gcloud compute networks subnets update SUBNET_NAME \
        --add-secondary-ranges RANGE_NAME_1=RANGE_CIDR_1,RANGE_NAME_2=RANGE_CIDR_2,...
    
    
    
    gcloud compute networks subnets update  SUBNET_NAME \
        --remove-secondary-ranges RANGE_NAME_1,RANGE_NAME_2,...
    

For more information about this command, use `gcloud compute networks subnets update --help`.

### Can't simultaneously add and remove alias IP ranges

Adding and removing VM alias IP ranges in the same request isn't supported. The existing range must be explicitly removed before you can add the new range.

The gcloud CLI command to update alias IP ranges does _not_ preserve the existing ranges, so omitting a range is treated as a request to delete that range.

For example, if the current VM has an alias range `10.9.27.0/24` and the new requested range is `/24`, the command to request the `/24` is rejected because it is interpreted as removing `10.9.27.0/24` and adding `/24`.

Example:

  1. Create alias IP range.
         
         gcloud compute instances create vm --network-interface "subnet=s1,aliases=10.9.27.0/24"
         

  2. Try to add `/24` without specifying the existing range. An error results.
         
         gcloud compute instances network-interfaces update vm --aliases "/24"
         ERROR: (gcloud.compute.instances.network-interfaces.update) HTTPError 400: Invalid value for field 'resource.
         aliasIpRanges': ''. Cannot simultaneously add and remove alias IP ranges.
         

  3. Update the VM to have no alias IP range.
         
         gcloud compute instances network-interfaces update vm --aliases ""
         Updating network interface [nic0] of instance [vm]...done.
         

  4. Add the new alias IP range.
         
         gcloud compute instances network-interfaces update vm --aliases "/24"
         Updating network interface [nic0] of instance [vm]...done.
         




For more information about this command, use `gcloud compute instances network-interfaces update --help`.

### Firewall rule source tags and source service accounts

Firewall source service account and source tags only expand to primary network IPs of matching instances and don't apply to alias IPs of matching instances. So, a firewall rule based on source tags doesn't affect traffic from an instance alias IP address. Alias IP addresses can be added to firewall rules as source or destination ranges.

### Issues with VMs with multiple interfaces and alias IP ranges

See [Troubleshoot VMs with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/troubleshoot-multiple-interfaces).

### Enabling IP alias on Google Cloud images disables `cbr0` bridge on self-managed Kubernetes clusters

On images provided by Google, the [Google guest agent](https://github.com/GoogleCloudPlatform/guest-agent) creates local routes for alias IP address ranges. For self-managed Kubernetes clusters, you must configure the Google guest agent so that it doesn't create local routes for alias IP ranges. This step isn't required for GKE clusters because GKE disables the creation of local routes for alias IP ranges on its node images.

**Symptoms** :

  * Kubernetes Pods lose network access if the local route created by the Guest agent removes the alias IP range from the `cbr0` interface.

  * A packet capture on the Linux bridge device (`tcpdump -ni cbr arp`) shows a lack of ARP responses from the `cbr0` interface even though that interface is up.

  * Inspecting the local route table (`ip route show table local`) reveals that the alias IP address range is assigned to the primary network interface (for example, `eth0` or `ens4`) instead of the container bridge interface (`cbr0`).




**Fix** :

  1. Run the appropriate command listed in [Installed packages for the guest environment](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#wgei_packages) to determine whether the node VM is running the [Google guest agent](https://github.com/GoogleCloudPlatform/guest-agent/blob/main/README.md) or [an earlier Compute Engine package](https://github.com/GoogleCloudPlatform/compute-image-packages/blob/master/packages/python-google-compute-engine/README.md).

  2. If your node VM isn't running the Google guest agent, [install the guest agent](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#installing_guest_environment) or use a more recent image supplied by Google.

  3. Configure the Google guest agent to skip creating local routes for alias IP ranges and forwarding rules.

     1. Edit `/etc/default/instance_configs.cfg`, setting `ip_forwarding=false` in the `[NetworkInterfaces]` section. You can create the `[NetworkInterfaces]` section if it's not already present in the `instance_configs.cfg` file.

     2. Do one of the following tasks:

        * [Restart](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#restart-vm) the node VM.

        * Restart the `google-guest-agent.service` service, and edit the local route table.

To restart the `google-guest-agent.service` service, run `sudo systemctl restart google-guest-agent.service`. Then edit the local route table to remove any entries for the alias IP address ranges—for example:
              
              sudo ip route del local ALIAS_IP_RANGE dev DEVICE_IDENTIFIER
              

Replace the following:

          * `ALIAS_IP_RANGE`: the alias IP address range.
          * `DEVICE_IDENTIFIER`: the identifier of the network interface—for example, `ens4` or `eth0`.

For more information, see [Configuration](https://github.com/GoogleCloudPlatform/guest-agent#configuration) in the Google guest agent documentation.




## What's next

  * Read more about [instances](https://docs.cloud.google.com/compute/docs/instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
