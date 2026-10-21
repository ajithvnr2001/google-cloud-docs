---
url: https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces/
title: Create VMs with multiple network interfaces \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:12.853364+00:00
---

# Create VMs with multiple network interfaces  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create VMs with multiple network interfaces

This page describes how to create VM instances with multiple network interfaces.

## Before you begin

Before you begin, ensure that you're familiar with the characteristics of instances with multiple network interfaces as described in the [Multiple network interfaces overview](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts).

## IAM roles

To create an instance with multiple network interfaces, you must have one of the following roles:

  * Project Owner or Editor role
  * [Compute Instance Admin (v1) role](https://docs.cloud.google.com/compute/docs/access/iam#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)



**Creating and deleting instances and instance templates with multiple interfaces in a project not using a Shared VPC environment:** A user with the Owner, Editor, or Compute Instance Admin (v1) role can create an instance with multiple interfaces associated with VPC networks and subnets that are part of that same project.

**Creating and deleting instances and instance templates with multiple interfaces in Shared VPC environments:** A user with the Owner, Editor, or Compute Instance Admin (v1) role can create an instance with multiple interfaces. If any of the interfaces are attached to a subnet in a Shared VPC host project, you must also have the [Compute Network User role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) (`roles/compute.networkUser`) for the whole host project or for the subnets you need to use.

To learn more about permissions, read the [Compute Engine IAM documentation](https://docs.cloud.google.com/compute/docs/access/iam).

## Create VM instances with multiple network interfaces

This section describes how to create an instance with multiple network interfaces, including vNICs and Dynamic NICs. For general instructions about creating instances, see [Create and start a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

The first interface is always created as `nic0`, and it is always the default interface.

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Machine configuration** pane, do the following:

     1. In the **Name** field, enter a name for the instance.
     2. In the **Region** field, select a region.
     3. In the **Zone** field, select a zone.
  3. In the navigation menu, click **Networking** to view the **Networking** pane.

  4. In the **Network interfaces** section, expand the network interface to edit it.

     1. For **Network** and **Subnetwork** , select the network and subnetwork that you want to use.

If you want to configure IPv6 addresses on the interface, select a subnet that has an `/64` IPv6 address range configured. The IPv6 access type of the subnet determines whether the instance receives an internal `/96` IPv6 address range or an external `/96` IPv6 address range.

     2. Select one of the following options for the **IP stack type** for the interface:

        * **IPv4 (single-stack)**
        * **IPv4 and IPv6 (dual-stack)**
        * **IPv6 (single-stack)**
     3. For interfaces with IPv4 addresses, do the following:

        1. For **Primary internal IPv4 address** , select one of the following:

           * **Ephemeral (Automatic)** to automatically assign a new ephemeral IPv4 address
           * **Ephemeral (Custom)** to manually specify a new ephemeral IPv4 address
           * A reserved static internal IPv4 address from the list
           * **Reserve static internal IPv4 address** to reserve and assign a new static internal IPv4 address
        2. For **External IPv4 address** , select one of the following:

           * **Ephemeral** to assign a new ephemeral IPv4 address
           * **None** to not assign an external IPv4 address
           * A reserved static IPv4 address from the list
           * **Reserve static external IP address** to reserve and assign a new static external IPv4 address
        3. You can optionally assign one or more [alias IP ranges](https://docs.cloud.google.com/vpc/docs/configure-alias-ip-ranges) to the network interface. To assign an alias IP range, do the following:

           1. In **Alias IP ranges** , click add**Add IP range**.
           2. In **Subnet range** , select a subnet primary IPv4 address range or a subnet secondary IPv4 address range to use.
           3. For **Alias IP range** , enter an IP range in CIDR notation. This range must be an unused range of the subnet IP range that you selected.

For more information about assigning alias IP ranges to VM network interfaces, see [Configure alias IP ranges](https://docs.cloud.google.com/vpc/docs/configure-alias-ip-ranges).

     4. For interfaces with IPv6 addresses, do the following, depending on the access type of the connected subnet:

        1. For **Primary internal IPv6 address** , select one of the following: 
           * **Ephemeral (Automatic)** to automatically assign a new ephemeral internal IPv6 address range
           * **Ephemeral (Custom)** to manually specify a new ephemeral internal IPv6 address range
           * A reserved static internal IPv6 address range from the list
           * **Reserve static internal IPv6 address** to reserve and assign a new static internal IPv6 address range
        2. For **External IPv6 address** , select one of the following: 
           * **Ephemeral (Automatic)** to automatically assign a new ephemeral external IPv6 address range
           * **Ephemeral (Custom)** to manually specify a new ephemeral external IPv6 address range
           * A reserved static external IPv6 address range from the list
           * **Reserve static external IPv6 address** to reserve and assign a new static external IPv6 address range
     5. To finish modifying the network interface, click **Done**.

  5. To add another network interface:

     1. To add a vNIC, click **Add a network interface** and complete the form by entering the details of the vNIC.

     2. To add a Dynamic NIC, click **Add a Dynamic Network Interface** and do the following:

        1. In the **Parent network interface** field, select the parent vNIC for which to create the Dynamic NIC.
        2. In the **VLAN ID** field, enter the VLAN ID of the Dynamic NIC.
        3. Complete the form by entering the remaining details of the Dynamic NIC.
  6. Continue with the instance creation process.

  7. Click **Create**.




###  gcloud 

To create network interfaces on a new instance, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).

Include the `--network-interface` flag for each interface, followed by any appropriate networking keys, such as `network`, `subnet`, `private-network-ip`, `address`, `external-ipv6-address` and `vlan`.

Including the `vlan` key creates a Dynamic NIC. If you create a Dynamic NIC, you must also follow the steps for [configuring the guest OS for Dynamic NICs](https://docs.cloud.google.com/vpc/docs/add-dynamic-nics#configure-guest-os) after you create the instance.

To view examples of how to create instances with multiple interfaces, see example configurations.

This snippet only illustrates the `--network-interface` flag, one of many possible parameters that you can specify when creating an instance.
    
    
    gcloud compute instances create INSTANCE_NAME \
        --zone ZONE \
        --network-interface \
            network=NETWORK_A,subnet=SUBNET_A, \
            stack-type=STACK_TYPE, \
            private-network-ip=INTERNAL_IPV4_ADDRESS, \
            address=EXTERNAL_IPV4_ADDRESS | no-address, \
            internal-ipv6-address=INTERNAL_IPV6_ADDRESS \
        ...
        --network-interface \
            network=NETWORK_B,subnet=SUBNET_B, \
            stack-type=STACK_TYPE, \
            external-ipv6-address=EXTERNAL_IPV6_ADDRESS, \
            external-ipv6-prefix-length=96, \
            ipv6-network-tier=PREMIUM, \
            vlan=VLAN_ID \
        ...
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance to create.
  * `ZONE`: the zone where the instance is created.
  * `NETWORK_A`, `NETWORK_B`: the network where the interface attaches.
  * `SUBNET_A`, `SUBNET_B`: the subnet where the interface attaches.
  * `STACK_TYPE`: the stack type for the interface.

The default value is `IPV4_ONLY`. Specify `IPV4_IPV6` to configure a dual-stack interface, or `IPV6_ONLY` to configure an IPv6-only interface.

  * Values for interfaces with IPv4 addresses:

    * `INTERNAL_IPV4_ADDRESS`: the internal IPv4 address that you want the interface to have in the target subnet. Omit if you just want any valid address assigned.
    * `EXTERNAL_IPV4_ADDRESS`: the external IPv4 address of the interface.

You must have previously reserved an external IPv4 address. If you don't want the interface to have an external IP address, specify "no-address" instead of `address=EXTERNAL_IPV4_ADDRESS`. If you want the interface to receive an ephemeral external IP address, specify `address=''`.

  * Values for interfaces with IPv6 addresses:

    * `INTERNAL_IPV6_ADDRESS`: the internal IPv6 address range that you want the interface to have in the target subnet. If not specified, Google Cloud automatically assigns an internal IPv6 address range from the subnet.
    * `EXTERNAL_IPV6_ADDRESS`: the external IPv6 address range that you want the interface to have in the target subnet. If not specified, Google Cloud automatically assigns an external IPv6 address range from the subnet.
**Note:** An interface can have only one IPv6 address range, either internal or external, but not both.
  * `VLAN_ID`: a VLAN ID. Specifying a VLAN ID configures the network interface as a Dynamic NIC. You must place a Dynamic NIC after its parent vNIC in the command.




###  API 

Use the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) to create an instance with multiple network interfaces.

Including the `vlan` field creates a Dynamic NIC. If you create a Dynamic NIC, you must also follow the steps for [configuring the guest OS for Dynamic NICs](https://docs.cloud.google.com/vpc/docs/add-dynamic-nics#configure-guest-os) after you create the instance.

See the following examples:

  * To create an instance with only internal IPv4 addresses, do the following:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
        {
        ....
        
        "networkInterfaces": [
          {
            "networkIP": "IPV4_ADDRESS_A",
            "subnetwork": "regions/REGION/subnetworks/SUBNET_A"
          },
          {
            "networkIP": "IPV4_ADDRESS_B",
            "subnetwork": "regions/REGION/subnetworks/SUBNET_B",
            "vlan": "VLAN_ID"
          },
            for each interface, specify a network...
        ],
        other instance settings...
        }
        

Replace the following:

    * `PROJECT_ID`: the ID of the project that contains the instance.
    * `ZONE`: the zone that contains the instance.
    * `IPV4_ADDRESS_A`, `IPV4_ADDRESS_B`: the internal IPv4 addresses that you want to assign to each network interface.
    * `REGION`: the region that contains the instance.
    * `SUBNET_A, SUBNET_B`: the subnets where each network interface is located.
    * `VLAN_ID`: a VLAN ID. Specifying a VLAN ID configures the network interface as a Dynamic NIC. You must place a Dynamic NIC after its parent vNIC the request.
  * To create an instance with both internal IPv4 and internal IPv6 addresses, do the following:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
        {
        ....
        
        "networkInterfaces": [
          {
            "subnetwork": "regions/REGION/subnetworks/SUBNET_A",
            "ipv6Address": "IPV6_ADDRESS_A",
            "internalIpv6PrefixLength": 96,
            "stackType": IPV4_IPV6,
            "ipv6AccessType": INTERNAL
          },
          {
            "subnetwork": "regions/REGION/subnetworks/SUBNET_B",
            "ipv6Address": "IPV6_ADDRESS_B",
            "internalIpv6PrefixLength": 96,
            "stackType": IPV4_IPV6,
            "ipv6AccessType": INTERNAL,
            "vlan": "VLAN_ID"
          },
            for each interface, specify a network...
        ],
        other instance settings...
        }
        

Replace the following:

    * `PROJECT_ID`: the ID of the project that contains the instance.
    * `ZONE`: the zone that contains the instance.
    * `REGION`: the region that contains the instance.
    * `SUBNET_A, SUBNET_B`: the subnets where each network interface is located.
    * `IPV6_ADDRESS_A, IPV6_ADDRESS_B`: the internal IPv6 address range that you want the interface to have in the target subnet. If not specified, Google Cloud automatically assigns an internal IPv6 address range from the subnet.
    * `VLAN_ID`: a VLAN ID. Specifying a VLAN ID configures the network interface as a Dynamic NIC. You must place a Dynamic NIC after its parent vNIC.
  * To create an instance with only internal IPv6 addresses, do the following:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
        {
        ....
        
        "networkInterfaces": [
          {
            "subnetwork": "regions/REGION/subnetworks/SUBNET_A",
            "ipv6Address": "IPV6_ADDRESS_A",
            "internalIpv6PrefixLength": 96,
            "stackType": IPV6_ONLY,
            "ipv6AccessType": INTERNAL
          },
          {
            "subnetwork": "regions/REGION/subnetworks/SUBNET_B",
            "ipv6Address": "IPV6_ADDRESS_B",
            "internalIpv6PrefixLength": 96,
            "stackType": IPV6_ONLY,
            "ipv6AccessType": INTERNAL,
            "vlan": "VLAN_ID"
          },
            for each interface, specify a network...
        ],
        other instance settings...
        }
        

Replace the following:

    * `PROJECT_ID`: the ID of the project that contains the instance.
    * `ZONE`: the zone that contains the instance.
    * `REGION`: the region that contains the instance.
    * `SUBNET_A, SUBNET_B`: the subnets where each network interface is located.
    * `IPV6_ADDRESS_A, IPV6_ADDRESS_B`: the internal IPv6 address range that you want the interface to have in the target subnet. If not specified, Google Cloud automatically assigns an internal IPv6 address range from the subnet.
    * `VLAN_ID`: a VLAN ID. Specifying a VLAN ID configures the network interface as a Dynamic NIC. You must place a Dynamic NIC after its parent vNIC. 



### Terraform

You can use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance) to create an instance with multiple network interfaces.

The Terraform arguments have example values that you can change.
    
    
    resource "google_compute_instance" "default" {
      project      = var.project_id # Replace with your project ID in quotes
      zone         = "us-central1-b"
      name         = "backend-instance"
      machine_type = "e2-medium"
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-9"
        }
      }
      network_interface {
        subnetwork = var.subnet_1 # Replace with self link to a subnetwork in quotes
        network_ip = "10.0.0.14"
      }
      network_interface {
        subnetwork = var.subnet_2 # Replace with self link to a subnetwork in quotes
        network_ip = "10.10.20.14"
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## Example configurations

The following sections show how to create instances with multiple interfaces.

### Configure multiple vNICs and Dynamic NICs

The following sample command creates an instance with the following network interfaces:

  * A vNIC named `nic0` that is the parent of the following: 
    * A Dynamic NIC named `nic0.2`
  * A vNIC named `nic1` that is the parent of the following: 
    * A Dynamic NIC named `nic1.4`
    * A Dynamic NIC named `nic1.5`


    
    
    gcloud compute instances create vm1 \
        --zone zone-a \
        --network-interface=network=network-a,subnet=subnet-a \
        --network-interface=network=network-b,subnet=subnet-b,vlan=2 \
        --network-interface=network=network-c,subnet=subnet-c \
        --network-interface=network=network-d,subnet=subnet-d,vlan=4 \
        --network-interface=network=network-e,subnet=subnet-e,vlan=5
    

After you create an instance with Dynamic NICs, you must also [configure the guest OS for Dynamic NICs](https://docs.cloud.google.com/vpc/docs/add-dynamic-nics#configure-guest-os).

### Configure multiple network interfaces with only IPv4 addresses

The following sample command creates an instance with three network interfaces.
    
    
    gcloud compute instances create vm1 --machine-type=n1-standard-4 \
        --network-interface '' \
        --network-interface network=net1,subnet=subnet-a,private-network-ip=10.10.10.2,address=EXTERNAL_IPV4_ADDRESS \
        --network-interface network=net2,subnet=subnet-b,private-network-ip=10.10.20.2,no-address
    

The interfaces are created as follows:

  * `nic0` is created with default settings. The interface is attached to a subnet in the default VPC network, with an automatically allocated internal IP address and an ephemeral external IP address.

  * `nic1` is attached to subnet `subnet-a` in network `net1`, with an internal IPv4 address of `10.10.10.2` and a static external IPv4 address, `EXTERNAL_IPV4_ADDRESS`.

  * `nic2` is attached to subnet `subnet-b` in network `net2`, with an internal IPv4 address of `10.10.20.2` and no external IP address.




For a complete description of the `gcloud compute instances create` command and the `--network-interface` flag, read the [documentation for the command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).

You can use the IP address from the network interface that you have added to set up DNS forwarding. To learn more about configuring Cloud DNS forwarding zones, see [Forwarding zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#forwarding_zones).

### Configure multiple network interfaces with both IPv4 and IPv6 addresses

The following sample command creates a dual-stack instance with two network interfaces.
    
    
    gcloud compute instances create vm1 \
        --network-interface network=dual-int,subnet=int-subnet,stack-type=IPV4_IPV6 \
        --network-interface network=dual-ext,subnet=ext-subnet,stack-type=IPV4_IPV6,ipv6-network-tier=PREMIUM \
        --machine-type=n1-standard-4 --zone=ZONE_A
    

The interfaces are created as follows:

  * `nic0` is attached to subnet `int-subnet` in network `dual-int`, with an ephemeral internal IPv4 address and an ephemeral internal IPv6 address range.

  * `nic1` is attached to subnet `ext-subnet` in network `dual-ext`, with an ephemeral internal IPv4 address and an ephemeral external IPv6 address range.




### Configure multiple network interfaces with only IPv6 addresses

The following sample command creates an IPv6-only instance with three network interfaces.
    
    
    gcloud compute instances create vm1 \
        --network-interface network=ipv6-only-int-a,subnet=int-subnet-a,stack-type=IPV6_ONLY \
        --network-interface network=ipv6-only-int-b,subnet=int-subnet-b,stack-type=IPV6_ONLY,internal-ipv6-address=fd20:db8:0:0:1:0:: \
        --network-interface network=ipv6-only-ext,subnet=ext-subnet,stack-type=IPV6_ONLY,ipv6-network-tier=PREMIUM,external-ipv6-address=EXTERNAL_IPV6_ADDRESS \
        --machine-type=n1-standard-4 --zone=us-west2-a
    

The interfaces are created as follows:

  * `nic0` is attached to subnet `int-subnet-a` in network `ipv6-only-int-a`, with an automatically allocated ephemeral internal IPv6 address.

  * `nic1` is attached to subnet `int-subnet-b` in network `ipv6-only-int-b`, with a custom ephemeral internal IPv6 address range `fd20:db8:0:0:1:0::/96`.

  * `nic2` is attached to subnet `ext-subnet` in network `ipv6-only-ext`, with a static external IPv6 address range, `EXTERNAL_IPV6_ADDRESS`.




### Configure multiple network interfaces for instance groups

You can use instances with multiple network interfaces in unmanaged instance groups and managed instance groups.

For [unmanaged instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances), create each instance individually, ensuring that the `nic0` network interface for each instance is attached to the same subnet. Then, add the instances to the unmanaged instance group.

To configure multiple network interfaces for [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances), you must specify the network configuration for each interface in the instance template, by setting the `--network-interface` flag once for each interface. The following sample creates an instance template with three network interfaces:
    
    
    gcloud compute instance-templates create template-1 \
        --network-interface subnet=net0-subnet-a \
        --network-interface subnet=net1-subnet-b,no-address \
        --network-interface subnet=net2-subnet-c,no-address \
        --region REGION_A
    

Because subnet names in each region of a project must be unique, specifying subnets by name implicitly associates each interface with a VPC network. In this example, each interface uses a subnet that is in a unique VPC network:

  * `nic0` uses the `net0-subnet-a` subnet
  * `nic1` uses the `net1-subnet-b` subnet
  * `nic2` uses the `net2-subnet-c` subnet



The `no-address` option in the `--network-interface` flag indicates that the interface is configured without an external IPv4 address. The internal IP address comes from the subnet used by the interface. For complete information about the flags and syntax, see the [`--network-interface` flag for the `instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--network-interface).

**Note:** Connecting to a Shared VPC network by using interfaces other than `nic0` is supported only in the gcloud CLI and the API for Compute Engine instance templates.

## What's next

  * [Configure routing for an additional interface](https://docs.cloud.google.com/vpc/docs/configure-routing-additional-interface)
  * [Add Dynamic NICs to an instance](https://docs.cloud.google.com/vpc/docs/add-dynamic-nics)
  * [View network interfaces for an instance](https://docs.cloud.google.com/compute/docs/instances/view-network-properties#view_network_interfaces_for_an_instance)
  * [Update the network interfaces for an instance](https://docs.cloud.google.com/compute/docs/networking/update-network-interfaces)
  * [Delete Dynamic NICs from an instance](https://docs.cloud.google.com/vpc/docs/delete-dynamic-nics)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
