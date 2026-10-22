---
url: https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-internal-ip-address/
title: Configure static internal IP addresses \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:57.688163+00:00
---

# Configure static internal IP addresses  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-internal-ip-address/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Configure static internal IP addresses Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to configure and manage static internal IPv4 or IPv6 addresses for your Compute Engine virtual machine (VM) and bare metal instances.

If an instance requires a fixed internal IP address that does not change, you can obtain a static internal IP address for that instance by using one of the following options:

  * You can [reserve a static internal IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#reservenewip), and then specify the reserved address when creating an instance.
  * You can also create the instance with an ephemeral internal IP address and then [promote that ephemeral IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#promote-in-use-internal-address) to a static internal IP address.



To learn how to manage secondary internal IP addresses, read [Alias IP ranges](https://docs.cloud.google.com/compute/docs/alias-ip).

In Compute Engine, each VM instance can have [multiple network interfaces](https://docs.cloud.google.com/compute/docs/create-use-multiple-interfaces). Each interface can have one external IP address, one primary internal IP address, and [one or more secondary internal IP addresses](https://docs.cloud.google.com/compute/docs/alias-ip). To learn about IP addresses, read the [IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses) documentation.

With static internal IP addresses, you can always use the same IP address for a VM, even if you have to delete and recreate the VM.

To configure a static external IP address instead of an internal IP address, see [Configure static external IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address).

## Before you begin

  * Read about [IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses).
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to configure and manage static IP addresses, ask your administrator to grant you the following IAM roles on your project: 

  * To create and update VMs: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to configure and manage static IP addresses. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to configure and manage static IP addresses:

  * `compute.instances.update` on the VM instance 
  * `compute.instances.updateNetworkInterface` on the VM instance 
  * `compute.instances.addAccessConfig` on the VM instance 
  * `compute.instances.deleteAccessConfig` on the VM instance 
  * `compute.networks.list` on the network 
  * `compute.subnetworks.use` on the subnet 
  * `compute.subnetworks.list` on the subnet 
  * To create VMs: 
    * `compute.instances.create` on the project
    * To use a custom image to create the VM: `compute.images.useReadOnly` on the image
    * To use a snapshot to create the VM: `compute.snapshots.useReadOnly` on the snapshot
    * To use an instance template to create the VM: `compute.instanceTemplates.useReadOnly` on the instance template
    * To assign a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) to the VM: `compute.networks.use` on the project
    * To specify a static IP address for the VM: `compute.addresses.use` on the project
    * To assign an external IP address to the VM when using a legacy network: `compute.networks.useExternalIp` on the project
    * To specify a subnet for the VM: `compute.subnetworks.use` on the project or on the chosen subnet
    * To assign an external IP address to the VM when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet
    * To set VM instance metadata for the VM: `compute.instances.setMetadata` on the project
    * To set tags for the VM: `compute.instances.setTags` on the VM
    * To set labels for the VM: `compute.instances.setLabels` on the VM
    * To set a service account for the VM to use: `compute.instances.setServiceAccount` on the VM
    * To create a new disk for the VM: `compute.disks.create` on the project
    * To attach an existing disk in read-only or read-write mode: `compute.disks.use` on the disk
    * To attach an existing disk in read-only mode: `compute.disks.useReadOnly` on the disk



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

  * The number of static internal IP addresses that you can reserve cannot exceed your project's quota. For more information, see the per-project [quotas](https://docs.cloud.google.com/vpc/docs/quota) in the VPC documentation.

  * Only one resource at a time can use a static internal IP address.

  * Reserving a static internal IP address is only supported for VPC networks. It is not supported for legacy mode networks.

  * Deleting a resource does not automatically release a static internal IP address. You must manually release static internal IP addresses when you no longer require them.

  * Each VM can have multiple network interfaces, and each interface can have the following IP addresses assigned according to its [stack type](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#stack-types):

    * IPv4-only interfaces: 
      * An internal IPv4 address (required)
      * An external IPv4 address (optional)
    * Dual-stack (IPv4 and IPv6) interfaces: 
      * An internal IPv4 address (required)
      * An external IPv4 address (optional)
      * A `/96` IPv6 address range, either internal or external, but not both (required)
    * IPv6-only interfaces: 
      * A `/96` IPv6 address range, either internal or external, but not both (required)
  * You can't unassign or change the following:

    * The internal IPv4 address of an existing resource. For example, you can't assign a new static internal IP address to a running or a stopped VM instance.
    * The internal IPv6 address of a VM with an IPv6-only network interface.

You can, however, promote an ephemeral internal IP address of a resource to a static internal IP address so that the address remains reserved even after the resource is deleted.

  * You cannot change the name of a static IP address.

  * Static internal IP addresses are regional, meaning they are restricted to the region in which they are reserved. For example, if there is a reserved static internal IP address in `Region A`, you can only use the IP address in `Region A`.




## How to configure a static internal IP address

You can reserve a static internal IP address, and then specify the reserved address when creating an instance. You can also create the VM with an ephemeral internal IP address and then promote that ephemeral IP address to a static internal IP address.

To use a static internal IP address, you must have a VPC network in place for your project. To view the VPC networks in your project, see [View VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#viewing-networks).

**Reserve a static internal IPv4 or IPv6 address and then associate it with a specific VM**

In this scenario, you separately reserve a static internal IP address and then assign it to an instance:

  1. [Choose a subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#listing_existing_subnets) in your VPC network. For IPv6 addresses, make sure that it is a subnet with an internal IPv6 address range.

  2. [Reserve an internal IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address) from the subnet's primary IP range. This step creates a named internal IP address resource that contains that specific internal IP address. Reserving the IP address prevents Google Cloud from automatically allocating that address as an ephemeral address.

  3. Use the reserved internal IP address by associating it with an instance when you create the VM resource.




**Specify an ephemeral internal IPv4 or IPv6 address for an instance and then promote the address**

In this scenario, you promote an ephemeral internal IPv4 or IPv6 address that is still attached to an instance:

  1. [Choose a subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#listing_existing_subnets) in your VPC network. For IPv6 addresses, make sure that it is a subnet with an IPv6 address range.

  2. Create an instance with either an automatically allocated ephemeral IPv4 or IPv6 address or a custom IPv4 or IPv6 address.

  3. [Promote](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#promote-in-use-internal-address) the ephemeral internal IP address to a static address.




## View available static internal IP addresses

To view all your existing static internal IP addresses, complete the following steps.

###  Console 

  1. In the Google Cloud console, go to the **IP addresses** page.

[Go to IP addresses](https://console.cloud.google.com/networking/addresses)

  2. Click **Internal IP addresses**.




###  gcloud 

Use the [`gcloud compute addresses list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/list):
    
    
    gcloud compute addresses list

###  API 

Use the [`addresses.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/list):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/addresses

Replace the following:

  * `PROJECT_ID`: the project ID for this request
  * `REGION`: the name of the region for this request



To list all the addresses in all regions, use the [`addresses.aggregatedList` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/aggregatedList):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/addresses

## How internal IP addresses are assigned

The network interfaces for an instance are assigned IP addresses from the subnet that they are connected to. Each IPv4-only or dual-stack network interface has one primary internal IPv4 address that is assigned from the subnet's primary IPv4 range. Each IPv6-only or dual-stack network interface connected to a subnet with an internal IPv6 address range is assigned an internal IPv6 address.

Internal IPv4 addresses can be assigned in the following ways:

  * Compute Engine assigns a single IPv4 address from the primary IPv4 subnet range automatically.
  * You can assign a specific internal IPv4 address when you create an instance, or you can [reserve a static internal IPv4 address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#reservenewip) for your project and assign that address to network interface of an instance.



Internal IPv6 addresses can be assigned in the following ways:

  * Compute Engine assigns a single `/96` range from the IPv6 subnet range automatically.
  * You can assign a custom `/96` range from the subnet's internal IPv6 range when you create an instance, or you can [reserve a static internal IPv6 address range](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#reservenewip) from the subnet's internal IPv6 range and assign it to the network interface of an instance.



## Use reserved static internal IP addresses when creating resources

After you reserve a static internal IP address, you can assign the reserved address when creating an instance or an internal load balancer.

The following procedures describe how to use static internal IP addresses when creating resources:

  * Create an instance with a reserved internal IPv4 or IPv6 address
  * Use a static internal IPv4 or IPv6 address for a secondary network interface



### Create an instance with a reserved internal IPv4 or IPv6 address

When you create an instance that is connected to a dual-stack or IPv6-only subnet with an internal IPv6 range, and you don't specify a custom ephemeral internal IPv6 address or reserved static internal IPv6 address, Compute Engine automatically assigns the instance an ephemeral internal IPv6 address from the subnet's IPv6 range.

###  Console 

  1. In the Google Cloud console, go to the **Create a VM instance** page.

[Go to Create a VM instance](https://console.cloud.google.com/compute/instancesAdd)

  2. Expand the **Advanced options** section.

  3. Expand the **Networking** section.

  4. To assign an internal IPv4 address, do the following:

     1. Select a network and a subnetwork.
     2. Select a reserved internal IPv4 address from the **Primary internal IPv4 address** list.

Alternatively, select **Reserve static internal IP address** and reserve a new static internal IPv4 address.

  5. To assign an internal IPv6 address, do the following:

     1. Select a network that contains a subnet with an IPv6 address range.
     2. Select a dual-stack or IPv6-only subnet from the **Subnetwork** list. The subnet _must_ have the `INTERNAL` IPv6 access type.
     3. For **IP stack type** , select **IPv4 and IPv6 (dual-stack)** or **IPv6 (single-stack)**.
     4. Select a reserved internal IPv6 address from the **Primary internal IPv6 address** list.

Alternatively, select **Reserve static internal IPv6 address** and reserve a new static internal IPv6 address.

  6. To finish modifying the default network interface, click **Done**.

  7. Continue with the instance creation process.

  8. Click **Create**.




###  gcloud 

  * Use the [`instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) to create an instance with a reserved internal IPv4 address, and use the `--private-network-ip` flag to specify the IP address:
        
        gcloud compute instances create INSTANCE_NAME \
            --private-network-ip IP_ADDRESS
        

Replace the following:

    * `INSTANCE_NAME`: the name of the instance that you want to create
    * `IP_ADDRESS`: the IP address that you want to assign

If you're using a custom subnet mode network, you must also specify the subnet by using the `--subnet SUBNET` parameter.

  * To create an instance with a reserved internal IPv6 address, use the `--internal-ipv6-address` flag to specify the IP address:
        
        gcloud compute instances create INSTANCE_NAME \
            --subnet SUBNETWORK \
            --stack-type STACK_TYPE \
            --internal-ipv6-address INTERNAL_IPV6_ADDRESS \
            --zone ZONE
        

Replace the following:

    * `INSTANCE_NAME`: the name of the instance that you want to create
    * `SUBNETWORK`: the subnet for the internal IPv6 address
    * `STACK_TYPE`: the stack type for the instance, either `IPV4_IPV6` or `IPv6_ONLY`.
    * `INTERNAL_IPV6_ADDRESS`: the `/96` IPv6 address, the IP address name, or the URI of the address resource. The IP address must be reserved before you can use it.
    * `ZONE`: the zone to create the instance in.



###  REST 

To create an instance with a static internal IP address, use the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).

  * For internal IPv4 addresses, explicitly provide the `networkInterfaces[].networkIP` property with the internal IPv4 address that you want to assign for the instance.

For example:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
        
        {
        "name": "INSTANCE_NAME",
        "machineType": "zones/us-central1-f/machineTypes/e2-micro",
        "networkInterfaces": [{
          "accessConfigs": [{
            "type": "ONE_TO_ONE_NAT",
            "name": "External NAT",
          }],
          "network": "global/networks/default",
          "networkIP": "IPV4_ADDRESS"
        }],
        "disks": [{
          "autoDelete": "true",
          "boot": "true",
          "type": "PERSISTENT",
          "initializeParams": {
              "sourceImage": "projects/debian-cloud/global/images/debian-13-trixie-v20260902"
          }
        }]
        }

Replace the following:

    * `PROJECT_ID`: the ID of the project to create the instance in
    * `ZONE`: the zone to create the instance in
    * `INSTANCE_NAME`: the name of the virtual machine
    * `IPV4_ADDRESS`: the internal IPv4 address to assign to the instance
  * For internal IPv6 addresses, explicitly specify the values for the following properties:

    * `networkInterfaces[].stackType`
    * `networkInterfaces[].ipv6Address`
    * `networkInterfaces[].internalIpv6PrefixLength`
    * `networkInterfaces[].ipv6AccessType`

For example:
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    {
    "name": "INSTANCE_NAME",
    "machineType": "zones/us-central1-f/machineTypes/n4-standard-2",
    "networkInterfaces": [{
      "network": "global/networks/default",
      "stackType": "STACK_TYPE"
      "ipv6Address": "IPV6_ADDRESS",
      "internalIpv6PrefixLength": 96
    }],
    "disks": [{
      "autoDelete": "true",
      "boot": "true",
      "type": "PERSISTENT",
      "initializeParams": {
          "sourceImage": "projects/debian-cloud/global/images/debian-13-trixie-v20260902"
      }
    }]
    }

Replace the following:

    * `PROJECT_ID`: the ID of the project to create the instance in.
    * `ZONE`: the zone to create the instance in.
    * `INSTANCE_NAME`: the name of the instance.
    * `STACK_TYPE`: the stack type for the instance, either `IPV4_IPV6` or `IPv6_ONLY`.
    * `IPV6_ADDRESS`: the internal IPv6 address to assign to the instance.



If you delete an instance with an ephemeral IP address, the address goes back into the unallocated address pool. If you need an internal IP address to persist beyond the life of the instance, you can [reserve a static internal IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#reservenewip).

### Assign a static internal address to an instance's secondary network interface

When you create an instance with multiple network interfaces, you can use a reserved static internal IPv4 or IPv6 address for both primary and secondary network interfaces.

To use a static internal IPv4 or IPv6 address for a secondary network interface, see [Create instances with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces#creating_virtual_machine_instances_with_multiple_network_interfaces).

## Change or assign an internal IPv4 address to an existing instance

After you create an instance, you might need to manage its internal IPv4 address. For example, you might want to ensure that the instance retains its current IP address permanently, or you might need to change the instance to use a different IP address. Depending on your goal, you can either keep the current address by promoting it to a static address, or change the address to a different internal IPv4 address.

If you want to keep the compute instance's current ephemeral internal IPv4 address and prevent it from changing when the instance is stopped or deleted, you can [promote the ephemeral internal IP address to a static address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#promote-in-use-internal-address).

If you want to change the internal IPv4 address, you can't directly change or unassign the internal IPv4 address of an existing compute instance, nor can you directly assign a new static internal IPv4 address to an existing instance's network interface within the same subnet. For more information, see Limitations.

To change the internal IPv4 address of an existing compute instance, use one of the following methods:

  * **Migrate the compute instance to a different subnet or network** : When you migrate a stopped instance's network interface to another subnet or network, you can specify a new internal IPv4 address (either automatically allocated or custom). If you want the instance to remain in the same network, you can migrate it to a temporary subnet or network and then migrate it back with the new internal IPv4 address. For instructions, see [Migrating a VM between networks](https://docs.cloud.google.com/compute/docs/instances/migrating-interfaces-between-networks).

  * **Recreate the compute instance from a snapshot or image** : You can recreate the compute instance and assign a specific static internal IPv4 address:

    1. [Reserve a static internal IPv4 address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#reservenewip) in the target subnet if you haven't already done so.
    2. [Stop the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance).
    3. [Create a snapshot](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) or [create a custom image](https://docs.cloud.google.com/compute/docs/images/create-custom) from the instance's boot disk.
    4. [Create a new compute instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) using the snapshot or custom image as the boot disk.
    5. During instance creation, in the **Networking** settings, specify the reserved static internal IPv4 address.
    6. (Optional) After verifying that the new instance works as expected, [delete the original compute instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance).



## Change or assign an internal IPv6 address to an existing instance

You can change or assign an internal IPv6 address for an existing dual-stack instance. If the instance is IPv4-only and you want to assign an IPv6 address, you must first change its stack type to dual-stack.

If the instance already has an internal IPv6 address assigned to it, you must first unassign that address. Then, assign a new address to the instance by using the instance's network interface.

**Note:** If you need to update the IP address of a forwarding rule, see [Change the IP address of a forwarding rule](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#update-forwarding-rule).

To change or assign a static internal IPv6 address to an existing instance, complete the following steps.

###  Console 

  1. [Reserve a static internal IPv6 address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#reservenewip).
  2. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  3. Click the name of the instance whose internal IPv6 address you want to change.

  4. On the **Instance details** page, complete the following steps:

     1. Click **Edit**.
     2. Expand **Network interfaces**.
     3. If the instance is IPv4-only and you want to assign an IPv6 address, you must first change the stack type to dual-stack.
     4. In the **Primary internal IPv6 address** list, do one of the following: 
        * To automatically assign a new ephemeral IPv6 address, choose **Ephemeral (Automatic)**.
        * To manually specify a new ephemeral IPv6 address, choose **Ephemeral (Custom)**.
        * To assign an existing static internal IP address, choose the name of a reserved IPv6 address from the list.
     5. Click **Done**.
  5. Click **Save**.




###  gcloud 

Use the [`compute instances network-interfaces update` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/update).
    
    
    gcloud compute instances network-interfaces update INSTANCE_NAME \
        --network-interface NIC \
        --ipv6-network-tier PREMIUM \
        --stack-type STACK_TYPE \
        --internal-ipv6-address INTERNAL_IPV6_ADDRESS \
        --zone ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance that you want to create
  * `NIC`: the name of the network interface to update
  * `STACK_TYPE`: the stack type for the instance, which must be `IPV4_IPV6`
  * `INTERNAL_IPV6_ADDRESS`: the `/96` internal IPv6 address to be assigned to the interface, the IP address name, or the URI of the address resource
  * `ZONE`: the zone for the instance



###  REST 

Use the [`instances.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/update). Update the `networkInterfaces[].ipv6Address` property with the internal IPv6 address that you want to assign.

For example: 
    
    
     POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
      {
          ...
          "networkInterfaces": [{
              "accessConfigs": [{
                  "type": "ONE_TO_ONE_NAT",
                  "name": "External NAT",
              }],
              "stackType": "STACK_TYPE"
              "ipv6Address": "IPV6_ADDRESS",
              "internalIpv6PrefixLength": 96
              "subnetwork": "regions/REGION/subnetworks/SUBNETWORK",
          }],
          "disks": [{
              "autoDelete": "true",
              "boot": "true",
              "type": "PERSISTENT",
              "initializeParams": {
                  "sourceImage": "projects/debian-cloud/global/images/debian-13-trixie-v20260902"
              }
          }]
     }
     

Replace the following:

  * `PROJECT_ID`: the ID of the project the instance is in
  * `ZONE`: the zone to create the instance in
  * `INSTANCE_NAME`: the name of the instance
  * `STACK_TYPE`: the stack type for the instance, which must be `IPV4_IPV6`
  * `IPV6_ADDRESS`: the internal IPv6 address to assign to the instance

If you specify the URI of the internal IPv6 address resource or an IPv6 address range as the value for `IPV6_ADDRESS`, then you must leave the value of `internalIpv6PrefixLength` blank.




## Manage static internal IP addresses

The following procedures let you manage static internal IP addresses for your instances:

  * Determine if an internal IPv4 or IPv6 address is ephemeral or static
  * List static internal IPv4 or IPv6 addresses
  * Unassign a static internal IPv6 address
  * Release a static internal IPv6 address



### Determine if an internal IPv4 or IPv6 address is ephemeral or static

Static and ephemeral internal IP addresses behave and appear the same in most contexts. However, with static internal IP addresses, you can use the same IP address for the same resource even if you delete and re-create the resource. 

In general, an ephemeral IP address is released if you stop or delete the resource.

To determine if an address is static or ephemeral, do the following:

  1. In the Google Cloud console, go to the **IP addresses** page.

[Go to IP addresses](https://console.cloud.google.com/networking/addresses/list)

  2. Find the address in the list and check the **Type** column for the type of IP address.




### Unassign a static internal IPv6 address

You can unassign a static internal IPv6 address from a dual-stack instance by updating the stack type for the instance's network interface or by [deleting the instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance) to which the address is assigned.

When you unassign an internal IPv6 address, the system removes it from the resource but keeps the address reserved for your project. You can later reassign the address to another resource.

To unassign a static internal IPv6 address from an instance, complete the following steps.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the instance whose internal IPv6 address you want to unassign.

  3. On the **Instance details** page, complete the following steps:

     1. Click **Edit**.
     2. Expand **Network interfaces**.
     3. For **IP stack type** , select **IPv4 (single-stack)**.
     4. Click **Done**.
  4. Click **Save**.




###  gcloud 

Use the [`compute instances network-interfaces update` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/network-interfaces/update) with the `--stack-type` flag set to `IPV4_ONLY`:
    
    
    gcloud compute instances network-interfaces update INSTANCE_NAME \
        --network-interface=NIC \
        --stack-type=IPV4_ONLY \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance whose network interface you want to update
  * `NIC`: the name of the network interface to update
  * `ZONE`: the zone for the instance



Check that your static internal IPv6 address is now available and marked as `RESERVED` instead of `IN_USE`:
    
    
    gcloud compute addresses list \
        --filter="region=REGION AND name=INSTANCE_NAME"
    

###  REST 

Update the instance stack type of the network interface where the internal IPv6 address is attached:

  1. Make a `PATCH` request to the [`instances.updateNetworkInterface` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/updateNetworkInterface).
  2. In the request body, update the value of the `stackType` field to `IPV4_ONLY`.

For example:
         
         PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/updateNetworkInterface
         {
             "networkInterfaces": [{
                 ...
                 "stackType" : "IPV4_ONLY"
                 ...
             }]
         }
         

Replace the following:

     * `PROJECT_ID`: the ID of the project that the instance is in
     * `ZONE`: the zone to create the instance in
     * `INSTANCE_NAME`: the name of the instance



### Release a static internal IP address

If you no longer need a static internal IPv4 or IPv6 IP address, you can release the IP address by deleting the IP address resource. Deleting an instance doesn't automatically release a static external IP address. You must manually release static external IP addresses when you no longer require them.

To release a static internal IP address, see [Release a static internal IPv4 or IPv6 address](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#delete_a_static_internal_ip_address) in the VPC documentation.

## What's next

  * [IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses)
  * [Configure a static external IP address](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address)
  * Assign [multiple internal IP addresses using alias IP addresses](https://docs.cloud.google.com/compute/docs/alias-ip)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
