---
url: https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address/
title: Configure IPv6 addresses for instances and instance templates \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:43:24.244848+00:00
---

# Configure IPv6 addresses for instances and instance templates  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Configure IPv6 addresses for instances and instance templates Stay organized with collections  Save and categorize content based on your preferences. 

You can configure IPv6 addresses on a Compute Engine instance if the subnet that the instance is connected to has an IPv6 range configured.

For more information about IPv6, see [IPv6 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges).

## Specifications

  * Compute instances that have both IPv4 and IPv6 configurations are _dual-stack_. The IPv6 address is in addition to any IPv4 addresses that are configured on the network interface.

  * Interfaces on dual-stack or IPv6-only instances are allocated a single `/96` range of IPv6 addresses; the first IPv6 address in the range (`/128`) is configured on the interface.

  * Any interface on the instance can have IPv6 addresses configured. For more information about configuring multiple network interfaces, see [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts).

  * The stack type of a VM's network interface determines the type of subnets to which it can connect:

    * IPv4-only interfaces can connect to dual-stack and IPv4-only subnets.
    * Dual-stack interfaces can connect to dual-stack subnets.
    * IPv6-only interfaces can connect to dual-stack and IPv6-only subnets.
  * To configure IPv6 addresses on a network interface, the interface must be connected to a dual stack or IPv6-only [subnet](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types).

  * A subnet's IPv6 access type configuration determines whether the subnet has an internal or external IPv6 range. Connected instances inherit the IPv6 access type from the subnet.

  * IPv6-only instances are supported with only Ubuntu and Debian OS images.




## Accessing instances using IPv6 addresses

The [implied IPv6 deny ingress firewall rule](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) protects instances by blocking incoming connections to their IPv6 addresses. To access instances using their IPv6 addresses, you must have a higher priority rule that allows incoming access.

For more information about firewall rules, see [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) and [Hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies).

For examples of VPC firewall rules, see [Configure firewall rules for common use cases](https://docs.cloud.google.com/vpc/docs/using-firewalls#rules-for-common-use-cases).

## IPv6 address assignment

The following list describes how IPv6 addresses are assigned to compute instances.

  * Compute instances are assigned an IPv6 address using DHCPv6. The metadata server responds to the instance's DHCPv6 requests and sends the first IPv6 address (`/128`) from the allocated `/96` range in response.

  * The metadata server uses route advertisement to publish the default route to the instance. The instance can then use this default route for all IPv6 traffic.

You can find the default route for an instance's network interface by connecting to the instance and querying the metadata server for the `gateway-ipv6` entry.
        
        curl http://metadata.google.internal/computeMetadata/v1/instance/network-interfaces/0/gateway-ipv6 -H "Metadata-Flavor: Google"
        

For more information about the metadata server, see [View and query instance metadata](https://docs.cloud.google.com/compute/docs/metadata/querying-metadata).

  * Compute instances are configured with link local IP addresses, which are assigned from the `fe80::/10` range, but they are used only for [neighbor discovery](https://en.wikipedia.org/wiki/Neighbor_Discovery_Protocol).

  * The MTU configuration on the instance's network interface applies to both IPv4 and IPv6 packets, but not all MTU values are supported in all circumstances. For more information, see [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).




## Create an instance that uses IPv6 addresses

You can create an instance that uses either a combination of IPv4 and IPv6 addresses (_dual-stack_), or you can create an instance that uses only IPv6 addresses.

For information about how to create a Compute Engine instance that uses IPv6 addresses, see the following tasks:

  * [Create a dual-stack instance](https://docs.cloud.google.com/compute/docs/instances/create-ipv6-instance#create-vm-ipv6-dual)
  * [Create an IPv6-only instance](https://docs.cloud.google.com/compute/docs/instances/create-ipv6-instance#create-vm-ipv6-only)



## Change the stack type of an instance

You can change the stack type of an existing Compute Engine instance. The stack type can be set to either of the following:

  * IPv4 only (single stack)
  * IPv4 and IPv6 (dual-stack)



If you are changing the stack type to dual-stack, the instance must be connected to a dual-stack subnet. If you need to change which subnet the instance is connected to, stop the instance and change the subnet. After the subnet is updated, you can change the instance's IP stack type.

You can't change the stack type of an IPv6-only instance.

###  Console 

  1. Go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of the instance that you want to assign an IPv6 address to.

  3. From the instance details page, complete the following steps:

     1. Click **Edit**.
     2. In **Network interfaces** , expand the interface that you want to edit.
     3. Select the **IP stack type** : **IPv4 only (single-stack)** or **IPv4 and IPv6 (dual-stack)**.
     4. Click **Done**.
  4. Click **Save**.




###  gcloud 

Update the stack type of an instance by using the [`gcloud compute instances network-interfaces update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/network-interfaces/update)
    
    
    gcloud compute instances network-interfaces update INSTANCE_NAME \
        --stack-type=STACK_TYPE \
        --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.
  * `STACK_TYPE`: the stack type for the instance: `IPV4_ONLY` or `IPV4_IPV6`.
  * `ZONE`: the zone that the instance is deployed in.



###  REST 

Update the stack type of an instance by making a `PATCH` request to the [`instances.updateNetworkInterface` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/updateNetworkInterface).
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/updateNetworkInterface
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the instance.
  * `ZONE`: the zone that the instance is deployed in.
  * `INSTANCE_NAME`: the name of the instance.



Example request body:
    
    
    {
        "stackType": "STACK_TYPE",
    }
    

Replace `STACK_TYPE` with the stack type for the instance: `IPV4_ONLY` or `IPV4_IPV6`.

## Create an instance template with IPv6 addresses

You can create a regional or global instance template that can be used to create dual-stack or IPv6-only instances. For more information, see [Create instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).

You must use the Google Cloud CLI or REST to create an instance template that creates instances that use IPv6 addresses.

###  gcloud 

To create a regional or global instance template, use the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create). If you want to create a regional instance template, you must use the `--instance-template-region` flag to specify the region for the instance template.

The following example creates a global instance template:
    
    
    gcloud compute instance-templates create TEMPLATE_NAME \
        --subnet=SUBNET \
        --stack-type=STACK_TYPE
    

Replace the following:

  * `TEMPLATE_NAME`: the name for the template.
  * `SUBNET`: a subnet that has an IPv6 subnet range.
  * `STACK_TYPE`: the stack type, either IPV4_IPV6 for a dual-stack instance, or IPV6_ONLY for an instance with external IPv6 address.



###  REST 

To create a regional instance template, use the [`regionInstanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/insert), or, to create a global instance template, use the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert).

The following example creates a global instance template:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/instanceTemplates
    

Replace `PROJECT_ID` with the project ID.

Example request body:
    
    
    {
      "name": "INSTANCE_TEMPLATE_NAME"
      "properties": {
        "machineType": "MACHINE_TYPE",
        "networkInterfaces": [
          {
            "subnetwork": "regions/REGION/subnetworks/SUBNET",
            "stackType": "STACK_TYPE",
          },
        ],
        "disks":
        [
          {
            "type": "PERSISTENT",
            "boot": true,
            "mode": "READ_WRITE",
            "initializeParams":
            {
              "sourceImage": "IMAGE_URI"
            }
          }
        ]
      }
    }
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the machine type of the instances. For example, `c3-standard-4`.
  * `SUBNET`: a subnet that has an IPv6 subnet range.
  * `REGION`: the region of the subnet.
  * `IMAGE_URI`: the URI to the [image](https://docs.cloud.google.com/compute/docs/images) that you want to use.

For example, if you specify `"sourceImage": "projects/debian-cloud/global/images/family/debian-12"`, Compute Engine creates an instance from the latest version of the operating system image in the Debian 12 image family.




To learn more about request parameters, see the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
