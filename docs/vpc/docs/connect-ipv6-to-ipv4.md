---
url: https://docs.cloud.google.com/vpc/docs/connect-ipv6-to-ipv4/
title: Configure IPv6-only subnets and instances with DNS64 and NAT64 \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:16.894602+00:00
---

# Configure IPv6-only subnets and instances with DNS64 and NAT64  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/connect-ipv6-to-ipv4/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure IPv6-only subnets and instances with DNS64 and NAT64

This page describes how to create IPv6-only subnets and instances and then configure DNS64 and NAT64 so that you can access IPv4 destinations from your IPv6-only instances.

Both Public NAT and Private NAT support NAT64. The instructions on this page show how to configure Public NAT. To get an overview of IPv6 to IPv4 connectivity in Google Cloud, see [DNS64 and NAT64 for 6to4 connectivity](https://docs.cloud.google.com/vpc/docs/ipv6-to-ipv4-overview).

## Before you begin

The instructions on this page require that you have a custom mode Virtual Private Cloud (VPC) network so that you can create subnets with IPv6 address ranges. For more information, see [Create a custom mode VPC network with IPv6-only subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-network-ipv6-only).

If you want to create a VPC network that supports subnets that have internal IPv6 addresses, you must configure a ULA internal IPv6 range when creating the network. If you have an existing network, you can [assign an internal IPv6 range to the network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#enable-internal-ipv6-network).

## Create IPv6-only subnets and instances

This section describes how to create IPv6-only subnets and instances. If you already have IPv6-only subnets and instances, you can proceed to Configure DNS64 and NAT64.

### Create an IPv6-only subnet

You can create an IPv6-only subnet with [external or internal IPv6 addresses](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges) enabled.

To create an IPv6-only subnet, do the following.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. To view the **VPC network details** page, click the name of a VPC network.

  3. On the **Subnets** tab, click add_box**Add subnet**. In the panel that appears:

     1. Provide a name.
     2. Select a region.
     3. For **IP stack type** , select **IPv6 (single-stack)**.
     4. Select an IPv6 access type: **Internal** or **External**.

If you want to set the access type to **Internal** but the **Internal** option isn't available, check that [an internal IPv6 range is assigned](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#enable-internal-ipv6-network) on the network.

     5. Click **Add**.




###  gcloud 

Use the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
    
    
    gcloud compute networks subnets create SUBNET \
        --network=NETWORK \
        --stack-type=IPV6_ONLY \
        --ipv6-access-type=IPv6_ACCESS_TYPE \
        --region=REGION
    

Replace the following:

  * `SUBNET`: a name for the new subnet.
  * `NETWORK`: the name of the VPC network to contain the new subnet.
  * `IPv6_ACCESS_TYPE`: the IPv6 access type. The access type can be either `EXTERNAL` or `INTERNAL`.
  * `REGION`: the Google Cloud region in which the new subnet is to be created.



###  API 

Make a `POST` request to the [`subnetworks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks
    {
      "network": "NETWORK_URL",
      "name": "SUBNET"
      "stackType": IPV6_ONLY,
      "ipv6AccessType": IPv6_ACCESS_TYPE
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the VPC network to modify.
  * `REGION`: the name of the Google Cloud region where the subnet is added.
  * `NETWORK_URL`: the URL of the VPC network where you are adding the subnet.
  * `SUBNET`: a name for the subnet.
  * `IPv6_ACCESS_TYPE`: the IPv6 access type. The access type can be either `EXTERNAL` or `INTERNAL`.



### Create an IPv6-only instance

###  Console 

  1. Go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. Enter a name for the instance.

  3. Select a region that contains the subnets with the IPv6 ranges configured.

  4. Optional: Change the zone for this instance. If you select **Any** , Google automatically chooses a zone for you based on machine type and availability.

  5. Expand the **Advanced options** section.

  6. Expand **Networking** , and do the following:

     1. In the **Network interfaces** section, click the network interface name to edit the settings for the network interface.

     2. For **Network** and **Subnetwork** , select the network and subnetwork that you want to use.

Select an IPv6-only subnet. The IPv6 access type of the subnet determines whether the instance receives an internal IPv6 address or an external IPv6 address.

     3. For **IP stack type** , select **IPv6 (single stack)**.

     4. For the interface's IPv6 address, do the following, depending on the access type of the connected subnet:

        1. For **Primary internal IPv6 address** , select one of the following: 
           * **Ephemeral (Automatic)** to automatically assign a new ephemeral internal IPv6 address
           * **Ephemeral (Custom)** to manually specify a new ephemeral internal IPv6 address
           * A reserved static internal IPv6 address from the list
           * **Reserve static internal IPv6 address** to reserve and assign a new static internal IPv6 address
        2. For **External IPv6 address** , select one of the following: 
           * **Ephemeral (Automatic)** to automatically assign a new ephemeral external IPv6 address
           * **Ephemeral (Custom)** to manually specify a new ephemeral external IPv6 address
           * A reserved static external IPv6 address from the list
           * **Reserve static external IPv6 address** to reserve and assign a new static external IPv6 address
     5. To finish modifying the network interface, click **Done**.

  7. Continue with the instance creation process.

  8. Click **Create**.




###  gcloud 

Create an instance by using the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).
    
    
    gcloud compute instances create INSTANCE_NAME \
        --zone ZONE \
        --network-interface=network=NETWORK,subnet=SUBNET,stack-type=IPV6_ONLY
    

Replace the following:

  * `INSTANCE_NAME`: a name for the instance.
  * `ZONE`: the zone where the instance is created, such as `europe-west1-b`. The instance's region is inferred from the zone.
  * `NETWORK`: name of the network in which to create the instance.
  * `SUBNET`: name of the subnet in which to create the instance.



###  API 

Use the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) to create an instance.
    
    
      POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
      {
         "machineType": "zones/MACHINE_TYPE_ZONE/machineTypes/MACHINE_TYPE",
         "name": "NAME",
         "disks": [
           {
             "initializeParams": {
               "sourceImage":"projects/IMAGE_PROJECT/global/images/IMAGE"
             },
             "boot": true
           }
         ],
         "networkInterfaces": [
           {
             "subnetwork": "regions/REGION/subnetworks/SUBNET",
             "stackType": "IPV6_ONLY"
           }
         ]
       }
       

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the instance.
  * `ZONE`: the zone that contains the instance.
  * `MACHINE_TYPE_ZONE`: zone containing the machine type to use for the new instance.
  * `MACHINE_TYPE`: machine type, [predefined](https://docs.cloud.google.com/compute/docs/machine-types#predefined_machine_types) or [custom](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type), for the new instance. For example, `c3-standard-4`.
  * `NAME`: the name of the instance.
  * `IMAGE_PROJECT`: Optional: the [image project](https://docs.cloud.google.com/compute/docs/images/os-details#general-info) that contains the image.
  * `IMAGE`: Optional: specify one of the following: 
    * A specific version of the OS image—for example, `debian-12-bookworm-v20241009`.
    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This creates the instance from the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, Compute Engine creates an instance using the latest version of the OS image in the Debian 12 image family. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).
  * `REGION`: the region that contains the instance.
  * `SUBNET`: the subnet where the network interface is located.



## Configure DNS64 and NAT64

This section describes how to configure both DNS64 and NAT64, which lets you access IPv4 destinations from IPv6-only instances.

### Create a DNS64 server policy

Create and configure a [DNS64 server policy](https://docs.cloud.google.com/dns/docs/server-policies-overview#dns64) so that Cloud DNS provides a synthesized IPv6 address for each IPv4 destination.

For more information about creating and managing DNS64 server policies, see [Configure DNS64](https://docs.cloud.google.com/dns/docs/configure-dns64).

To create a DNS64 server policy, do the following.

###  Console 

  1. In the Google Cloud console, go to the **Cloud DNS** page.

[Go to Cloud DNS](https://console.cloud.google.com/net-services/dns/policies/list)

  2. On the **DNS server policies** tab, click **Create policy**.

  3. In the **Name** field, enter a name for the policy.

  4. Optional: In the **Description** field, enter a description for the policy.

  5. For **DNS64** , select **On** to enable DNS64.

  6. In the **Networks** field, select the VPC network in which you want to create the policy. Select the network that contains the IPv6-only subnets and instances.




###  gcloud 

To create a DNS64 server policy, run the [`gcloud dns policies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/dns/policies/create):
    
    
    gcloud dns policies create NAME \
        --description=DESCRIPTION \
        --networks=VPC_NETWORK_LIST \
        --enable-dns64-all-queries
    

Replace the following:

  * `NAME`: a name for the policy.
  * `DESCRIPTION`: a description for the policy.
  * `VPC_NETWORK_LIST`: a comma-delimited list of VPC networks that the DNS server policy binds to. Specify the network that contains the IPv6-only subnets and instances.



###  API 

To create a DNS64 server policy, use the [`policies.create` method](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies/create):
    
    
    POST https://dns.googleapis.com/dns/v1/projects/PROJECT_ID/policies
    {
      "kind": "dns#policy",
      "networks": [
        {
          "kind": "dns#policyNetwork",
          "networkUrl": "NETWORK_URL"
        }
      ],
      "dns64Config":
        {
            "scope":
            {
              allQueries: true,
            }
        }
      }
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `NETWORK_URL`: the fully qualified URL of the VPC network that your DNS server policy must bind to, formatted as follows: `https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/VPC_NETWORK_NAME`. Specify the network that contains the IPv6-only subnets and instances.



### Create a Cloud NAT gateway to enable NAT64

Configure Public NAT by creating a Cloud NAT gateway in your VPC network and region that contains IPv6-only subnets and instances.

For more information about creating and managing Cloud NAT gateways, see [Set up and manage network address translation with Public NAT](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation).

To create a Cloud NAT gateway for NAT64, do the following.

###  Console 

  1. In the Google Cloud console, go to the **Cloud NAT** page.

[Go to Cloud NAT](https://console.cloud.google.com/net-services/nat/list)

  2. Click **Get started** or add_box**Create Cloud NAT gateway**. **Note:** If this is the first Cloud NAT gateway that you're creating, click **Get started**. If you already have existing gateways, then instead of **Get started** , Google Cloud displays the **Create Cloud NAT gateway** button. To create another gateway, click add_box**Create Cloud NAT gateway**.

  3. In the **Gateway name** field, enter a name for the gateway.

  4. For **NAT type** , select **Public**.

  5. In the **Select Cloud Router** section, configure the following:

     1. In the **Network** field, select the VPC network in which you want to create the gateway.
     2. In the **Region** field, set the region for the gateway.
     3. In the **Cloud Router** field, select or create a Cloud Router in the region.
  6. In the **Cloud NAT mapping** section, for **Source endpoint type** , make sure the **VM instances, GKE nodes, Serverless** option is selected.

  7. In the **Source IP version** field, select **IPv6 subnet ranges** , and then configure the source IPv6 subnet ranges for which you want to use Cloud NAT.

     * To use Cloud NAT for internal and external IP ranges for all subnets in the region, select **All subnets**.
     * To restrict which subnets can use Cloud NAT, select **Custom** and do the following: 
       1. In the **Subnets** section, select a subnet.
       2. Optional: If you want to specify additional subnets, click **Add subnet** and add another subnet.
  8. Configure any additional options for your Cloud NAT gateway. For more information, see [Create a Cloud NAT gateway](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation#create-nat-gateway) in the Cloud NAT documentation.

  9. Click **Create**.




###  gcloud 

This section describes how to create a Cloud NAT gateway with all of its configuration options set to their default values. For more information about customizing your gateway configuration, see [Customize configuration settings for a Cloud NAT gateway](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation#customize-settings).

To create a Cloud NAT gateway, use the [`gcloud compute routers nats create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create).

  1. [Create a Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-router-vpc-network#gcloud) in the region in which you want to use the Cloud NAT gateway. You need this Cloud Router to create your Cloud NAT gateway.

  2. Configure Cloud NAT for IPv6 source subnet ranges.

The following configuration enables NAT for all IPv6 subnet ranges in the region, in both IPv6-only and dual-stack subnets. You can alternatively configure NAT for specific subnets by using the `--nat64-custom-v6-subnet-ip-ranges` flag.
         
         gcloud compute routers nats create NAT_CONFIG \
             --router=NAT_ROUTER \
             --region=REGION \
             --auto-allocate-nat-external-ips \
             --nat64-all-v6-subnet-ip-ranges
         

Replace the following:

     * `NAT_CONFIG`: a name for your NAT configuration.
     * `NAT_ROUTER`: the name of the Cloud Router that you created in the previous step.
     * `REGION`: the region in which you want to use the Cloud NAT gateway.



###  API 

To create a Cloud Router and Cloud NAT gateway by using the API, use the [`routers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/insert) and set the `nats[]` field.

This section describes how to create a Cloud NAT gateway with all of its configuration options set to their default values. For more information about customizing your gateway configuration, see [Create a Cloud NAT gateway](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation#customize-settings).

For more information about creating a Cloud Router, see [Create a Cloud Router to connect a VPC network to a peer network](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-router-vpc-network#api).

The following configuration enables NAT for all IPv6 subnet ranges in the region. You can alternatively configure NAT for specific subnets by setting `sourceSubnetworkIpRangesToNat64` to `LIST_OF_IPV6_SUBNETWORKS` and specifying the subnets in the `nats[].nat64Subnetworks[]` field.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers
    {
      "name": "ROUTER_NAME",
      "network": "NETWORK",
      "bgp": {
        "asn": "ASN_NUMBER"
      },
      "nats": [
        {
          "name": NAT_CONFIG,
          "sourceSubnetworkIpRangesToNat64": ALL_IPV6_SUBNETWORKS,
          "natIpAllocateOption": AUTO_ONLY
        }
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the VPC network.
  * `REGION`: the region where you want to locate the Cloud Router and Cloud NAT gateway.
  * `ROUTER_NAME`: the name of the Cloud Router; this name is displayed in the Google Cloud console and is used by the Google Cloud CLI to reference the Cloud Router.
  * `NETWORK`: the VPC network in which to create the Cloud Router and Cloud NAT gateway.
  * `ASN_NUMBER`: the [private ASN](https://tools.ietf.org/html/rfc6996) (`64512`-`65534`, `4200000000`-`4294967294`) for the Cloud Router that you are configuring; this ASN can be any private ASN that you aren't already using as a peer ASN in the same region and network—for example, `65001` Cloud Router requires you to use a private ASN, but your on-premises ASN can be public or private.
  * `NAT_CONFIG`: a name for your NAT configuration.



## What's next

  * For information about managing VPC networks and subnets, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).
  * For information about IPv6-only instances, see [Configure IPv6 addresses for instances and instance templates](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address).
  * For more information about creating and managing DNS64 server policies, see [Configure DNS64](https://docs.cloud.google.com/dns/docs/configure-dns64).
  * For more information about creating and managing Cloud NAT gateways, see [Set up and manage network address translation with Public NAT](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
