---
url: https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address/
title: Reserve a static internal IP address \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:26:36.440558+00:00
---

# Reserve a static internal IP address  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Reserve a static internal IP address

This page shows you how to reserve and manage static internal IPv4 or IPv6 addresses in Virtual Private Cloud (VPC) networks.

Static internal IP addresses provide the ability to reserve internal IP addresses from the IP address range configured in the subnet, and then assign those reserved internal IP addresses to resources as needed. Reserving an internal IP address takes that address out of the dynamic allocation pool and prevents it from being used for automatic allocations. Reserving static internal IP addresses requires specific Identity and Access Management (IAM) permissions so that only authorized users can reserve a static internal IP address.

With the ability to reserve static internal IP addresses, you can always use the same IP address for the same resource even if you have to delete and re-create the resource.

To reserve a static external IP address instead of an internal IP address, see [Reserve a static external IP addresses](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address).

## Before you begin

  * Read about [IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses).
  * If you haven't already, set up authentication. [Authentication](https://docs.cloud.google.com/docs/authentication) is the process by which your identity is verified for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate as follows. 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
        
        gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to reserve and manage static IP addresses, ask your administrator to grant you the [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to reserve and manage static IP addresses. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to reserve and manage static IP addresses:

  * `compute.addresses.create` on the IP address
  * `compute.addresses.createInternal` on the IP address
  * `compute.networks.list` on the network
  * `compute.subnetworks.use` on the subnet
  * `compute.subnetworks.list` on the subnet



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




## Reserve a new static internal IPv4 or IPv6 address

Before you can reserve a new static internal IP address, you must [create a VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-auto-network) with a subnet.

If you want to reserve a new static internal IPv6 unique local address (ULA), the VPC network must have a [ULA internal IPv6 range enabled](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#enable-internal-ipv6-network). In addition, the network must have a subnet with an IPv6 address range and the `INTERNAL` IPv6 access type. For more information, see [Internal IPv6 specifications](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-specifications).

To reserve a standalone internal IP address, complete the following steps.

###  Console 

  1. In the Google Cloud console, go to the **IP addresses** page. 

[Go to IP addresses](https://console.cloud.google.com/networking/addresses/list)

  2. Click **Reserve internal static IP address**. You might need to click the more_vert **More actions** menu to see this button.
  3. In the **Name** field, enter an IP address name.
  4. In the **IP version** list, select the required IP version: 
     * To reserve a static internal IPv4 address, select **IPv4**.
     * To reserve a static internal IPv6 address, select **IPv6**.
  5. In the **Network** and **Subnetwork** lists, select a VPC network and a subnet, respectively.
  6. Specify how you want to reserve the IP address: 
     * For IPv4 addresses, to specify a static internal IPv4 address to reserve, for **Static IP address** , select **Let me choose** , and then enter a custom IPv4 address. Otherwise, the system automatically assigns a static internal IPv4 address in the subnet for you.
     * For IPv6 addresses, to specify a static internal IPv6 address range to reserve, for **Static IPv6 range** , select **Let me choose** , and then enter a custom `/96` IPv6 address range from the subnet's `/64` internal IPv6 address range. Otherwise, the system automatically assigns a static internal IPv6 address range in the subnet for you.
  7. Optional: If you want to share the static internal IPv4 address in different frontends, in the **Purpose** list, choose **Shared**. The default selection is **Non-shared**.

**Note:** You cannot share a static internal IPv6 address across multiple load balancer frontends.
  8. Click **Reserve**.




###  gcloud 

  * To reserve an internal IPv4 address, use the [`compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create):
        
        gcloud compute addresses create ADDRESS_NAMES \
            --region REGION --subnet SUBNETWORK \
            --addresses IPV4_ADDRESS
        

Replace the following:

    * `ADDRESS_NAMES`: the names of one or more `[--purpose=SHARED_LOADBALANCER_VIP]` addresses that you want to create. In case of multiple addresses, specify all the addresses as a list, separated by spaces—for example, `example-address-1 example-address-2 example-address-3`
    * `REGION`: the region for this request.
    * `SUBNETWORK`: the subnet for this internal IP address.
    * `IPV4_ADDRESS`: the IP address to reserve, which must be within the subnet's primary IP range. If unspecified, an IP address is automatically allocated from the subnet.
  * To reserve an internal IPv6 address, use the [`compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/create). Specify `IPV6` as the value for `--ip-version`:
        
        gcloud compute addresses create ADDRESS_NAMES \
            --region REGION --subnet SUBNETWORK \
            --ip-version IPV6  \
            --addresses IPV6_ADDRESS
        

Replace the following:

    * `ADDRESS_NAMES`: the names of one or more addresses that you want to reserve. In case of multiple addresses, specify all the addresses as a list, separated by spaces—for example, `example-address-1 example-address-2 example-address-3`
    * `REGION`: the region for this request.
    * `SUBNETWORK`: the subnet for this internal IPv6 address.
    * `IPV6_ADDRESS`: the IP address to reserve, which must be a `/96` IPv6 address from the subnet's `/64` internal IPv6 address range. If unspecified, an IP address is automatically allocated from the subnet.



**Examples**

  * Reserve an automatically allocated internal IPv4 address from a subnet:
        
        gcloud compute addresses create example-address-1 \
            --region us-central1 \
            --subnet subnet-1
        

  * Reserve a specific internal IPv4 address from a subnet:
        
        gcloud compute addresses create example-address-1 \
            --region us-central1 \
            --subnet subnet-1 \
            --addresses 10.128.0.12
        

  * Reserve a static internal IPv6 address from a subnet:
        
        gcloud compute addresses create example-address-1 \
            --region us-central1 \
            --subnet subnet-1 \
            --ip-version IPV6
        

  * Create multiple IPv4 addresses by passing in more than one IPv4 address name; all the addresses are reserved in the same subnet:
        
        gcloud compute addresses create example-address-1 example-address-2 \
            --region us-central1 \
            --subnet subnet-1 \
            --addresses 10.128.0.12,10.128.0.13
        




### Terraform

You can use a [Terraform module](https://github.com/terraform-google-modules/terraform-google-address) to create an internal IP address.

In the following example, the Terraform arguments have example values that you can change. The example creates two specific internal IP addresses:
    
    
    module "address" {
      source     = "terraform-google-modules/address/google"
      version    = "~> 4.0"
      project_id = var.project_id # Replace this with your project ID in quotes
      region     = "asia-east1"
      subnetwork = "my-subnet"
      names      = ["internal-address1", "internal-address2"]
      addresses  = ["10.0.0.3", "10.0.0.4"]
    }

The following example creates two dynamically allocated internal IP addresses:
    
    
    module "address" {
      source     = "terraform-google-modules/address/google"
      version    = "~> 4.0"
      project_id = var.project_id # Replace this with your project ID in quotes
      region     = "asia-east1"
      subnetwork = "my-subnet"
      names      = ["internal-address1", "internal-address2"]
    }

###  API 

Use the [`addresses.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/insert):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/addresses
    

For both IPv4 and IPv6 addresses, the body of the request must include the `addressType` field, which should be `INTERNAL`, the `name` of the address, and the `subnetwork` that the IP address belongs to. The body of the request can optionally include the `purpose` of the internal IP address.

You can let the system automatically allocate an IP address for you, or use `address` to specify an internal IP address. An IPv4 address that you reserve must belong to the subnet's primary IPv4 address range. An IPv6 address that you reserve must belong to a subnet's internal IPv6 address range.
    
    
    {
      "addressType": "INTERNAL",
      "name": "IPV4_ADDRESS_NAME",
      "subnetwork": "regions/REGION/subnetworks/SUBNETWORK",
      "address": "IPV4_ADDRESS",
      "purpose": "GCE_ENDPOINT"
    }
    

For example:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/example-project/regions/us-central1/addresses
    {
      "addressType": "INTERNAL",
      "name": "example-ipv4-address-1",
      "subnetwork": "regions/us-central1/subnetworks/my-custom-subnet",
      "address": "10.128.0.12",
      "purpose": "GCE_ENDPOINT"
    }
    

For internal IPv6 addresses, you need to also specify `ipVersion` as `IPV6`.
    
    
    {
      "addressType": "INTERNAL",
      "name": "IPV6_ADDRESS_NAME",
      "ipVersion": "IPV6",
      "subnetwork": "regions/REGION/subnetworks/SUBNETWORK",
      "address": "IPV6_ADDRESS",
      "purpose": "GCE_ENDPOINT"
    }
    

For example:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/example-project/regions/us-central1/addresses
    {
      "addressType": "INTERNAL",
      "name": "example-ipv6-address-1",
      "ipVersion": "IPV6",
      "subnetwork": "regions/us-central1/subnetworks/my-custom-subnet",
      "address": "2001:db8:a0b:c0d:e0f:f0e::",
      "purpose": "GCE_ENDPOINT"
    }
    

## Reserve a static internal IP address range for HA VPN over Cloud Interconnect

You can reserve a static internal IP address range to use with HA VPN over Cloud Interconnect.

When you create the static internal IP address, you must specify the flag `--purpose=IPSEC_INTERCONNECT` and a prefix length (`--prefix-length`) between 26 and 29.

The regional internal IPv4 addresses that you reserve are applied to the HA VPN gateways used by Cloud Interconnect.

For more information, see [Assign internal IP address ranges to HA VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/ha-vpn-interconnect-internal-ips).

## Determine if an internal IPv4 or IPv6 address is ephemeral or static

Static and ephemeral internal IP addresses behave and appear the same in most contexts. However, with static internal IP addresses, you can use the same IP address for the same resource even if you delete and re-create the resource. In general, an ephemeral IP address is released if you stop or delete the resource.

To determine if an address is static or ephemeral, do the following:

  1. In the Google Cloud console, go to the **IP addresses** page.

[Go to IP addresses](https://console.cloud.google.com/networking/addresses/list)

  2. Find the address in the list and check the **Type** column for the type of IP address.




## Promote an in-use ephemeral internal IPv4 or IPv6 address to a static address

If you have ephemeral internal IP addresses that are in use, you can promote these addresses to static internal IP addresses so that the addresses remain with your project until you actively remove them.

To promote an ephemeral internal IP address to a static internal IP address, complete the following steps.

###  Console 

  1. In the Google Cloud console, go to the **IP addresses** page. 

[Go to IP addresses](https://console.cloud.google.com/networking/addresses/list)

  2. Click **Internal IP addresses**.
  3. Optional: In the **Filter** field, to search for ephemeral IP addresses, enter `ephemeral` then select **Ephermal : Type** from the drop-down list.
  4. Select the internal IP address that you want to promote.
  5. In the **More actions** menu (more_vert) at the end of the display row for the selected IP address, select **Promote to static IP address**.
  6. Enter a name for the new static IP address, and then click **Reserve**.



###  gcloud 

  1. Before promoting an existing ephemeral internal IPv6 address, you need to know the value of that IP address. Use the Google Cloud CLI to make a `describe` request to the resource to get the IP address value.

**Note:** For VM instances, the gcloud CLI returns the `networkIP` value (for IPv4) or the `ipv6Address` value (for IPv6), which is the internal IP address being used by the VM. For forwarding rules, the gcloud CLI returns the `IPAddress` value.
     * For an instance with an IPv4 address, use the following command:
           
           gcloud compute instances describe INSTANCE_NAME --zone ZONE | grep "networkIP"
           

     * For an instance with an IPv6 address, use the following command:
           
           gcloud compute instances describe INSTANCE_NAME --zone ZONE | grep "ipv6Address"
           

     * For a regional forwarding rule, use the following command:
           
           gcloud compute forwarding-rules describe FORWARDING_RULE_NAME --region REGION | grep "IPAddress"
           

For a global forwarding rule, use the `--global` flag instead of the `--region` flag.

  2. Promote the address:

     * To promote one or more existing internal IPv4 addresses, use the [`compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create) and provide the `--addresses` flag with the explicit internal IP addresses to promote:
           
           gcloud compute addresses create IPV4_ADDRESS_NAMES \
             --addresses IPV4_ADDRESSES \
             --region REGION \
             --prefix-length PREFIX_LENGTH \
             --subnet SUBNETWORK
           

Replace the following:

       * `IPV4_ADDRESS_NAMES`: the names of the IPv4 addresses. In case of multiple addresses, specify all the address names as a list, separated by spaces—for example, `example-address-name-1 example-address-name-2 example-address-name-3`. Declare the names in the same order that you declare the IP addresses. For example, suppose you specify the address names as `example-address-name-1 example-address-name-2 example-address-name-3` and the IPv4 addresses as `192.0.2.0 192.0.2.1 192.0.2.2`. In this scenario, Compute Engine maps the names and addresses in the following way:

         * `example-address-name-1`: `192.0.2.0`
         * `example-address-name-2`: `192.0.2.1`
         * `example-address-name-3`: `192.0.2.2`
       * `IPV4_ADDRESSES`: the IPv4 addresses to promote. In case of multiple addresses, specify all the addresses as a list, separated by spaces—for example, `192.0.2.0 192.0.2.1 192.0.2.2`.

       * `REGION`: the region to reserve this address.

       * `PREFIX_LENGTH`: Optional. The prefix length of the IPv4 address range. The value must be an integer between 7 and 31. Include this field only if you specify an address range. Exclude the field if the specified IPv4 address is a single IP address.

       * `SUBNETWORK`: the subnetwork for this request.

     * To promote one or more existing internal IPv6 addresses, use the [`compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/addresses/create) and provide the `--addresses` flag with the explicit internal IPv6 addresses:
           
           gcloud compute addresses create IPV6_ADDRESS_NAMES \
            --addresses IPV6_ADDRESSES \
            --region REGION \
            --prefix-length PREFIX_LENGTH \
            --subnet SUBNETWORK
           

Replace the following:

       * `IPV6_ADDRESS_NAMES`: the names of the address. Declare the names in the same order that you declare the IPv6 addresses. In this case, `IPV6_ADDRESS_NAME_1` corresponds with `IPV6_ADDRESS_1`, and `IPV6_ADDRESS_NAME_2` corresponds with `IPV6_ADDRESS_2`.
       * `IPV6_ADDRESS_1,[IPV6_ADDRESS_2,...]`: the IPv6 addresses to promote in CIDR format.
       * `PREFIX_LENGTH_1,[PREFIX_LENGTH_2,...]`: the prefix length of IPv6 addresses.
       * `REGION`: the region to reserve this address.
       * `SUBNETWORK`: the subnetwork for this request.

The internal IPv6 address remains attached to the existing instance even after it has been promoted to a static internal IPv6 address. If you need to assign the newly promoted static internal IPv6 address to another resource, first [unassign the static internal IPv6 address](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-internal-ip-address#unassignintipv6) from the existing instance.




###  API 

Use the [`addresses.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/insert):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/addresses

For both IPv4 and IPv6 addresses, the body of the request must include the `addressType`, which should be `INTERNAL`, the `name` of the address, the `address` to promote, and the `subnetwork` that the IP address belongs to. For IPv6 addresses, additionally, the body of the request must include `prefixLength` with `96` as the value.

  * Request body for promoting internal IPv4 addresses:
        
        {
        "name": "ADDRESS_NAME",
        "addressType": "INTERNAL",
        "address": "IP_ADDRESS",
        "subnetwork": "regions/REGION/subnetworks/SUBNETWORK"
        }
        

For example:
        
        POST https://compute.googleapis.com/compute/v1/projects/example-project/regions/us-central1/addresses
        {
        "name": "example-IPv4-address-1",
        "addressType": "INTERNAL",
        "address": "10.128.0.2",
        "subnetwork": "regions/us-central1/subnetworks/my-custom-subnet"
        }
        

  * Request body for promoting internal IPv6 addresses:
        
        {
        "name": "ADDRESS_NAME",
        "addressType": "INTERNAL",
        "address": "IP_ADDRESS",
        "subnetwork": "regions/REGION/subnetworks/SUBNETWORK"
        "prefixLength": 96
        }
        

For example:
        
        POST https://compute.googleapis.com/compute/v1/projects/example-project/regions/us-central1/addresses
        {
        "name": "example-IPv6-address-1",
        "addressType": "INTERNAL",
        "address": "fd20:0:0::",
        "subnetwork": "regions/us-central1/subnetworks/my-custom-subnet"
        "prefixLength": 96
        }
        




## Use a static internal IPv4 or IPv6 address with Shared VPC

You can create a reserved static internal IP address in a shared subnet of a [Shared VPC network](https://docs.cloud.google.com/compute/docs/shared-vpc). The IP address object itself is created in the same service project as the resource that will use it, even though its value comes from the range of available IP addresses in the selected shared subnet of the Shared VPC network. For more information about this use case, see the following resources:

  * The [IP addresses](https://docs.cloud.google.com/vpc/docs/shared-vpc#ip_addresses) section in the _Shared VPC overview_
  * The [Reserve a static internal IPv4 or IPv6 address](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#reserve_internal_ip) section in _Provision Shared VPC_



## List static internal IPv4 or IPv6 addresses

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

## Release a static internal IPv4 or IPv6 address

If you no longer need a static internal IP address, you can release the IP address by deleting the IP address resource.

If you are using the Google Cloud console, you can release a static IP address only if it is not being used by another resource.

If you're using the gcloud CLI or API, you can release an IP address whether or not it's being used by another resource.

  * If the IP address is not being used by a resource, the IP address is returned to the pool of available internal IP addresses.

  * If the IP address is being used by a resource, it remains attached to the resource until the resource is deleted.




To release a static internal IPv4 or IPv6 address, complete the following steps.

###  Console 

  1. In the Google Cloud console, go to the **IP addresses** page. 

[Go to IP addresses](https://console.cloud.google.com/networking/addresses/list)

  2. Select the **Internal IP addresses** tab.
  3. Optional: In the **Filter** field, enter `static` and then select **Static : Type** from the drop-down list.
  4. Select the static internal IP address that you want to release.
  5. Click **Release static address** , and then confirm this operation by clicking **Release** in the dialog.

If you don't see this option, click the **More actions** menu (more_vert) in the top menu bar, and then select **Release static address** from the list.




###  gcloud 

Use the [`compute addresses delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/delete):
    
    
    gcloud compute addresses delete ADDRESS_NAME \
        --region REGION
    

Replace the following:

  * `ADDRESS_NAME`: the name of the address to delete.
  * `REGION`: the region the address belongs to.



For example:
    
    
    gcloud compute addresses delete example-address-to-delete \
        --region us-west1
    

###  API 

Use the [`addresses.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses/delete):
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/addresses/ADDRESS_NAME

This example deletes an address in the `us-west1` region:
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/myproject/regions/us-west1/addresses/example-address-to-delete

## What's next

  * Learn how to [configure static internal IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-internal-ip-address) for VMs.
  * Create an internal load balancer that uses a static internal IPv4 address:

    * [Set up an internal passthrough Network Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal)
    * [Set up an internal Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal)
**Note:** You can create only internal passthrough Network Load Balancers by using internal IPv6 addresses. For more information about the supported IP address type for different load balancers, see [Summary of Google Cloud load balancers](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview#summary-of-google-cloud-load-balancers).
  * Learn about [IP address specifications](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#ip_address_specifications) for forwarding rules, and how to [use forwarding rules](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#use-forwarding-rules), in the _Forwarding rules overview_.

  * Learn more about [IP addresses](https://docs.cloud.google.com/vpc/docs/ip-addresses).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-03 UTC."],[],[]] 
