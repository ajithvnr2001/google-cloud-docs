---
url: https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks/
title: Quickstart: Create and manage VPC networks \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:48.753897+00:00
---

# Quickstart: Create and manage VPC networks  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and manage VPC networks

This document describes how to create, modify, and delete Virtual Private Cloud (VPC) networks and subnetworks. Before reading this document, ensure that you are familiar with the characteristics of VPC networks as described in [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc). Networks and subnets are [different resources](https://docs.cloud.google.com/vpc/docs/subnets#vpc_networks_and_subnets) in Google Cloud.

**Note:** If you're getting started with Google Cloud, you can create an initial VPC network as part of the [Google Cloud setup process](https://docs.cloud.google.com/docs/enterprise/setup-checklist).

If you plan to enable IPv6 ranges on subnets, see [IPv6 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges).

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how VPC performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try VPC free ](https://console.cloud.google.com/freetrial)

## Create networks

You can choose to create an auto mode or custom mode VPC network. Each new network that you create must have a unique name within the same project.

You can optionally create your network using a network profile provided by Google Cloud for a specific use case. You only need to configure a network profile if you want to run [AI Hypercomputer](https://docs.cloud.google.com/ai-hypercomputer/docs/overview) workloads that require RDMA NICs. For more information, see [RDMA network profiles](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles).

### Create an auto mode VPC network

When you create an [auto mode](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges) VPC network, one [subnet](https://docs.cloud.google.com/vpc/docs/subnets) is created in each Google Cloud region. As new regions become available, new subnets in those regions are automatically added to the auto mode VPC network. IPv4 ranges for the automatically created subnets come from a [predetermined set of ranges](https://docs.cloud.google.com/vpc/docs/subnets#ip-ranges). All auto mode VPC networks use the same set of IPv4 ranges.

Subnets with IPv6 address ranges are not supported on auto mode VPC networks. Create a custom mode VPC network if you want to create subnets with IPv6 address ranges.

**Important:** Read the [considerations for auto mode VPC networks](https://docs.cloud.google.com/vpc/docs/vpc#auto-mode-considerations) before you create one for production use. Production networks should be planned in advance, and custom mode VPC networks are better suited for most production use cases.

To create an auto mode VPC network, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. Enter a **Name** for the network.

  4. To configure the maximum transmission unit (MTU) of the network, do the following:

     * To use the default value of `1460`, keep the **Set MTU automatically** checkbox selected.
     * To set a custom value, do the following: 
       1. Review the information in [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).
       2. Clear the **Set MTU automatically** checkbox.
       3. In the **Maximum transmission unit (MTU)** field, choose an MTU value.
  5. Choose **Automatic** for the **Subnet creation mode**.

  6. In the **Firewall rules** section, select zero or more predefined [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls). The rules address common use cases for connectivity to instances.

Whether or not you select pre-defined rules, you can [create your own firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls) after you create the network.

Each predefined rule name starts with the name of the VPC network that you are creating, `NETWORK`. In the **IPv4 firewall rules** tab, the predefined ingress firewall rule named **`NETWORK -allow-custom`** is editable. By default it specifies the source range `10.128.0.0/9`, which contains current and future IPv4 ranges for subnets in an auto mode network. The right side of the row that contains the rule, click **Edit** to select subnets, add additional IPv4 ranges, and specify protocols and ports.

  7. Choose the **Dynamic routing mode** for the VPC network.

For more information, see [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks). You can change the dynamic routing mode later.

  8. Click **Create**.




###  gcloud 

Use the [`networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create).
    
    
    gcloud compute networks create NETWORK \
        --subnet-mode=auto \
        --bgp-routing-mode=DYNAMIC_ROUTING_MODE \
        --mtu=MTU
    

Replace the following:

  * `NETWORK`: a name for the VPC network.
  * `DYNAMIC_ROUTING_MODE`: controls the behavior of Cloud Routers in the network. Can be either `global` or `regional`. The default is `regional`. For more information, see [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks).
  * `MTU`: the maximum transmission unit (MTU), which is the largest packet size of the network. MTU can be set to any value from `1300` to `8896`. The default is `1460`. Before setting the MTU to a value higher than `1460`, review [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).



### Terraform

Use the [`google_compute_network` Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network).

`MTU` is the maximum transmission unit, or largest packet size, of the network. MTU can be set to any value from `1300` to `8896`. The default is `1460`. Before setting the MTU to a value higher than `1460`, review [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).
    
    
    resource "google_compute_network" "vpc_network" {
      project                 = var.project_id # Replace this with your project ID in quotes
      name                    = "my-auto-mode-network"
      auto_create_subnetworks = true
      mtu                     = 1460
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  API 

Make a `POST` request to the [`networks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks
    {
      "autoCreateSubnetworks": true,
      "name": "auto-network1",
      "mtu": MTU
    }

Replace the following:

  * `PROJECT_ID`: the ID of the project where the VPC network is created.
  * `MTU`: the maximum transmission unit (MTU), which is the largest packet size of the network. MTU can be set to any value from `1300` to `8896`. The default is `1460`. Before setting the MTU to a value higher than `1460`, review [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).



To specify the [dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#dynamic-routing-mode-effects-on-learned-routes) of the VPC network, include the `routingConfig` field:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks
    {
      "routingConfig": {
        "routingMode": "DYNAMIC_ROUTING_MODE"
      },
      "autoCreateSubnetworks": true,
      "name": "NETWORK",
      "mtu": MTU
    }

Replace the following:

  * `PROJECT_ID`: the ID of the project where the VPC network is created.
  * `NETWORK`: a name for the VPC network.
  * `DYNAMIC_ROUTING_MODE`: controls the behavior of Cloud Routers in the network. Can be either `GLOBAL` or `REGIONAL`. The default is `REGIONAL`. For more information, see [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks).
  * `MTU`: the maximum transmission unit (MTU), which is the largest packet size of the network. MTU can be set to any value from `1300` to `8896`. The default is `1460`. Before setting the MTU to a value higher than `1460`, review [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).



### Create a custom mode VPC network with IPv4-only subnets

For custom mode VPC networks, create a network, then create the subnets that you want within a region. You do not have to specify subnets for all regions right away, or even at all, but you cannot create instances in a region that has no subnet defined. Finally, define the firewall rules for your network.

Each subnet in a VPC network can have a different configuration; you don't need to configure them all as IPv4-only, for example. You can also change an IPv4-only only subnet to dual-stack later.

To create a custom mode VPC network with IPv4-only subnets, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. Enter a **Name** for the network.

  4. To configure the MTU of the network, do the following:

     * To use the default value of `1460`, keep the **Set MTU automatically** checkbox selected.
     * To set a custom value, do the following: 
       1. Review the information in [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).
       2. Clear the **Set MTU automatically** checkbox.
       3. In the **Maximum transmission unit (MTU)** field, choose an MTU value.
  5. Choose **Custom** for the **Subnet creation mode**.

  6. In the **New subnet** section, specify the following configuration parameters for a subnet:

     1. Provide a **Name** for the subnet.
     2. Select a **Region**.
     3. Enter an **IP address range**. This is the [primary IPv4 range](https://docs.cloud.google.com/vpc/docs/vpc#vpc_networks_and_subnets) for the subnet.

If you select a range that is not an RFC 1918 address, confirm that the range doesn't conflict with an existing configuration. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).

     4. To define a secondary range for the subnet, click **Create secondary IP range**.

If you select a range that is not an RFC 1918 address, confirm that the range doesn't conflict with an existing configuration. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).

     5. **Private Google Access** : Choose whether to enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-access-options) for the subnet when you create it or later by editing it.

     6. **Flow logs** : Choose whether to enable [VPC flow logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) for the subnet when you create it or later by editing it.

     7. Click **Done**.

  7. To add more subnets, click **Add subnet** and repeat the previous steps. You can also add more subnets to the network after you have created the network.

  8. In the **Firewall rules** section, select zero or more predefined [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) in the **IPv4 firewall rules**. The rules address common use cases for connectivity to instances.

If you don't select any predefined rules, you can [create your own firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls) after you create the network.

Each predefined rule name starts with the name of the VPC network that you are creating, `NETWORK`. In the **IPv4 firewall rules** tab, the predefined ingress firewall rule named **`NETWORK -allow-custom`** is editable. On the right side of the row that contains the rule, click **Edit** to select subnets, add additional IPv4 ranges, and specify protocols and ports.

The **`NETWORK -allow-custom`** firewall rule is not automatically updated if you later add additional subnets. If you need firewall rules for the new subnets, you must update the firewall configuration to add the rules.

  9. Choose the **Dynamic routing mode** for the VPC network.

For more information, see [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks). You can change the dynamic routing mode later.

  10. Click **Create**.




###  gcloud 

Use the [`networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create).
    
    
    gcloud compute networks create NETWORK \
        --subnet-mode=custom \
        --bgp-routing-mode=DYNAMIC_ROUTING_MODE \
        --mtu=MTU
    

Replace the following:

  * `NETWORK`: a name for the VPC network.
  * `DYNAMIC_ROUTING_MODE`: controls the behavior of Cloud Routers in the network. Can be either `global` or `regional`. The default is `regional`. For more information, see [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks).
  * `MTU`: the maximum transmission unit (MTU), which is the largest packet size of the network. MTU can be set to any value from `1300` to `8896`. The default is `1460`. Before setting the MTU to a value higher than `1460`, review [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).



Next, add subnets to your network.

### Terraform

Use the [`google_compute_network` Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network).

`MTU` is the maximum transmission unit, or largest packet size, of the network. MTU can be set to any value from `1300` to `8896`. The default is `1460`. Before setting the MTU to a value higher than `1460`, review [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).
    
    
    resource "google_compute_network" "vpc_network" {
      project                 = var.project_id # Replace this with your project ID in quotes
      name                    = "my-custom-mode-network"
      auto_create_subnetworks = false
      mtu                     = 1460
    }

Next, add subnets to your network.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  API 

Make a `POST` request to the [`networks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks
    {
      "autoCreateSubnetworks": false,
      "name": "NETWORK",
      "mtu": MTU,
      "routingConfig": {
        "routingMode": "DYNAMIC_ROUTING_MODE"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the VPC network is created.
  * `NETWORK`: a name for the VPC network.
  * `DYNAMIC_ROUTING_MODE`: controls the behavior of Cloud Routers in the network. Can be either `GLOBAL` or `REGIONAL`. The default is `REGIONAL`. For more information, see [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks).
  * `MTU`: the maximum transmission unit (MTU), which is the largest packet size of the network. MTU can be set to any value from `1300` to `8896`. The default is `1460`. Before setting the MTU to a value higher than `1460`, review [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).



Next, add subnets to your network.

### Create a custom mode VPC network with a dual-stack subnet

You can create subnets when you create the network, or you can add them later.

A dual-stack subnet can have one of the following configurations for its primary IP address ranges:

  * Internal IPv4 range and _internal_ IPv6 range
  * Internal IPv4 range and _external_ IPv6 range



Each subnet in a VPC network can have a different configuration; you don't need to configure them all as dual-stack, for example.

By default, the addresses for a subnet's IPv6 range are provided by Google. If you want to use BYOIP to bring your own IPv6 addresses, see [Assign subnet ranges](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes#create-subnets) instead.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. Enter a **Name** for the network.

  4. To configure the MTU of the network, do the following:

     * To use the default value of `1460`, keep the **Set MTU automatically** checkbox selected.
     * To set a custom value: 
       1. Review the information in [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).
       2. Clear the **Set MTU automatically** checkbox.
       3. In the **Maximum transmission unit (MTU)** field, choose an MTU value.
  5. For **Subnet creation mode** , choose **Custom**.

  6. If you want to configure internal IPv6 address ranges on subnets in this network, complete these steps:

     1. In the **Private IPv6 address settings** section, select **Configure a ULA internal IPv6 range for this VPC Network**.
     2. For **Allocate internal IPv6 range** , select **Automatically** or **Manually**.

If you select **Manually** , enter a `/48` range from within the `fd20::/20` range. If the range is in use, you are prompted to provide a different range.

  7. In the **New subnet** section, specify the following configuration parameters for a subnet:

     1. Provide a **Name** for the subnet.
     2. Select a **Region**.
     3. To create a dual-stack subnet, for **IP stack type** , select **IPv4 and IPv6 (dual-stack)**.
     4. Enter an **IPv4 range**. This is the [primary IPv4 range](https://docs.cloud.google.com/vpc/docs/vpc#vpc_networks_and_subnets) for the subnet.

If you select a range that is not an RFC 1918 address, confirm that the range doesn't conflict with an existing configuration. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).

     5. Select an **IPv6 access type** : **External** or **Internal**.

     6. Click **Done**.

  8. To add more subnets, click **Add subnet** and repeat the previous steps.

Each subnet in a VPC network can have different stack type and IPv6 access type configurations. You do not need to configure all subnets in a given network as dual-stack subnets.

You can also add more subnets of any stack type to the network after you create the network.

  9. In the **Firewall rules** section, select zero or more predefined [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) in the **IPv4 firewall rules** and **IPv6 firewall rules** tabs. The rules address common use cases for connectivity to instances.

If you don't select any predefined rules, you can [create your own firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls) after you create the network.

Each predefined rule name starts with the name of the VPC network that you are creating, `NETWORK`. In both the **IPv4 firewall rules** tab and the **IPv6 firewall rules** tab, there is an editable predefined ingress firewall rule; the IPv4 rule is named **`NETWORK -allow-custom`** and the IPv6 rule is named **`NETWORK -allow-ipv6-custom`**. On the right side of the row that contains the rule, click **Edit** to select subnets, add additional IP ranges, and specify protocols and ports.

The **`NETWORK -allow-custom`** and **`NETWORK -allow-ipv6-custom`** firewall rule are not automatically updated if you later add additional subnets. If you need firewall rules for the new subnets, you must update the firewall configuration to add the rules.

  10. Choose the **Dynamic routing mode** for the VPC network.

For more information, see [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks). You can change the dynamic routing mode later.

  11. Click **Create**.




###  gcloud 

Use the [`networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create). After you have created the network, you can add subnets to it.

If you want to configure _internal_ IPv6 ranges on any subnets in this network, use the `--enable-ula-internal-ipv6` flag. This option assigns a `/48` ULA prefix from within the `fd20::/20` range used by Google for internal IPv6 subnet ranges. If you want to select the `/48` IPv6 range that is assigned, use the `--internal-ipv6-range` flag to specify a range.

You can omit both flags if you want to configure only _external_ IPv6 on subnets in this VPC network.
    
    
    gcloud compute networks create NETWORK \
        --subnet-mode=custom \
        [ --enable-ula-internal-ipv6 [ --internal-ipv6-range=ULA_IPV6_RANGE ]] \
        --bgp-routing-mode=DYNAMIC_ROUTING_MODE \
        --mtu=MTU
    

Replace the following:

  * `NETWORK`: a name for the VPC network.

  * `ULA_IPV6_RANGE`: a `/48` prefix from within the `fd20::/20` range used by Google for internal IPv6 subnet ranges. If you don't use the `--internal-ipv6-range` flag, Google selects a `/48` prefix for the network.

  * `DYNAMIC_ROUTING_MODE`: controls the behavior of Cloud Routers in the network. Can be either `global` or `regional`. The default is `regional`. For more information, see [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks).

  * `MTU`: the maximum transmission unit (MTU), which is the largest packet size of the network. MTU can be set to any value from `1300` to `8896`. The default is `1460`. Before setting the MTU to a value higher than `1460`, review [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).




### Terraform

Use the [`google_compute_network` Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network).

If you want to configure internal IPv6 ranges on any subnets in this network, use the `enable_ula_internal_ipv6` argument.

See the following example:
    
    
    resource "google_compute_network" "default" {
      name                     = "vpc-network-ipv6"
      auto_create_subnetworks  = false
      enable_ula_internal_ipv6 = true
    }

Next, add subnets to your network.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  API 

Make a `POST` request to the [`networks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/insert). After you have created the network, you can add subnets to it.

If you want to configure _internal_ IPv6 ranges on any subnets in this network, set `enableUlaInternalIpv6` to true. This option assigns a `/48` range from within the `fd20::/20` range used by Google for internal IPv6 subnet ranges. If you want to select which `/48` IPv6 range is assigned, also use the `internalIpv6Range` field when you specify a range.

To configure only _external_ IPv6 on subnets in this VPC network, omit both fields.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks
    {
      "autoCreateSubnetworks": false,
      "name": "NETWORK",
      "mtu": MTU,
      "enableUlaInternalIpv6": true,
      "internalIpv6Range": "ULA_IPV6_RANGE",
      "routingConfig": {
        "routingMode": "DYNAMIC_ROUTING_MODE"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the VPC network is created.
  * `NETWORK`: a name for the VPC network.
  * `MTU`: the maximum transmission unit (MTU), which is the largest packet size of the network. MTU can be set to any value from `1300` to `8896`. The default is `1460`. Before setting the MTU to a value higher than `1460`, review [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).
  * `ULA_IPV6_RANGE`: a `/48` prefix from within the `fd20::/20` range used by Google for internal IPv6 subnet ranges. If you don't provide a value for `internalIpv6Range`, Google selects a `/48` prefix for the network.
  * `DYNAMIC_ROUTING_MODE`: controls the behavior of Cloud Routers in the network. Can be either `GLOBAL` or `REGIONAL`. The default is `REGIONAL`. For more information, see [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks).



### Create a custom mode VPC network with IPv6-only subnets

You can create subnets when you create the network, or you can add them later.

An IPv6-only subnet can have an _internal_ IPv6 range or an _external_ IPv6 range.

Each subnet in a VPC network can have a different configuration; you don't need to configure them all as IPv6-only, for example.

You can't change a dual-stack or IPv4-only subnet to IPv6-only. Conversely, you can't change an IPv6-only subnet to IPv4-only or dual-stack.

By default, the IPv6 addresses for a subnet are provided by Google. If you want to use BYOIP to bring your own IPv6 addresses, see [Assign subnet ranges](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes#create-subnets) instead.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. Enter a **Name** for the network.

  4. To configure the MTU of the network, do the following:

     * To use the default value of `1460`, keep the **Set MTU automatically** checkbox selected.
     * To set a custom value, do the following: 
       1. Review the information in [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).
       2. Clear the **Set MTU automatically** checkbox.
       3. In the **Maximum transmission unit (MTU)** field, choose an MTU value.
  5. For **Subnet creation mode** , choose **Custom**.

  6. To configure internal IPv6 address ranges on subnets in this network, complete these steps:

     1. In the **Private IPv6 address settings** section, select **Configure a ULA internal IPv6 range for this VPC Network**.
     2. For **Allocate internal IPv6 range** , select **Automatically** or **Manually**.

If you select **Manually** , enter a `/48` range from within the `fd20::/20` range. If the range is in use, you are prompted to provide a different range.

  7. In the **New subnet** section, specify the following configuration parameters for a subnet:

     1. Provide a **Name** for the subnet.
     2. Select a **Region**.
     3. To create an IPv6-only subnet, for **IP stack type** , select **IPv6 (single-stack)**.
     4. Select an IPv6 access type: **External** or **Internal**.
     5. Click **Done**.
  8. To add more subnets, click **Add subnet** and repeat the previous steps.

Each subnet in a VPC network can have different stack type and IPv6 access type configurations. You don't need to configure all subnets in a given network as IPv6-only subnets.

You can also add more subnets of any stack type to the network after you create the network.

  9. In the **Firewall rules** section, select zero or more predefined [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) in the **IPv6 firewall rules** tab. The rules address common use cases for connectivity to instances.

If you don't select any predefined rules, you can [create your own firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls) after you create the network.

Each predefined rule name starts with the name of the VPC network that you are creating, `NETWORK`. In the **IPv6 firewall rules** tab, there is an editable predefined ingress firewall rule named **`NETWORK -allow-ipv6-custom`**. On the row that contains the rule, click **Edit** to select subnets, add additional IP ranges, and specify protocols and ports.

The **`NETWORK -allow-ipv6-custom`** firewall rule isn't automatically updated if you later add additional subnets. If you need firewall rules for the new subnets, you must update the firewall configuration to add the rules.

  10. Choose the **Dynamic routing mode** for the VPC network.

For more information, see [Dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks). You can change the dynamic routing mode later.

  11. Click **Create**.




###  gcloud 

Use the [`networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create). After you have created the network, you can add subnets to it.

If you want to configure _internal_ IPv6 ranges on any subnets in this network, use the `--enable-ula-internal-ipv6` flag. This option assigns a `/48` ULA prefix from within the `fd20::/20` range used by Google for internal IPv6 subnet ranges. If you want to select the `/48` IPv6 range that is assigned, use the `--internal-ipv6-range` flag to specify a range.

You can omit both flags if you want to configure only _external_ IPv6 on subnets in this VPC network.
    
    
    gcloud compute networks create NETWORK \
        --subnet-mode=custom \
        [ --enable-ula-internal-ipv6 [ --internal-ipv6-range=ULA_IPV6_RANGE ]] \
        --bgp-routing-mode=DYNAMIC_ROUTING_MODE \
        --mtu=MTU
    

Replace the following:

  * `NETWORK`: a name for the VPC network.

  * `ULA_IPV6_RANGE`: a `/48` prefix from within the `fd20::/20` range used by Google for internal IPv6 subnet ranges. If you don't use the `--internal-ipv6-range` flag, Google selects a `/48` prefix for the network.

  * `DYNAMIC_ROUTING_MODE`: controls the behavior of Cloud Routers in the network. Can be either `global` or `regional`. The default is `regional`. For more information, see [Dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks).

  * `MTU`: the maximum transmission unit (MTU), which is the largest packet size of the network. MTU can be set to any value from `1300` to `8896`. The default is `1460`. Before setting the MTU to a value higher than `1460`, review [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).




### Terraform

Use the [`google_compute_network` Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_network).

If you want to configure internal IPv6 ranges on any subnets in this network, use the `enable_ula_internal_ipv6` argument.

See the following example:
    
    
    resource "google_compute_network" "default" {
      name                     = "vpc-network-ipv6"
      auto_create_subnetworks  = false
      enable_ula_internal_ipv6 = true
    }

Next, add subnets to your network.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  API 

Make a `POST` request to the [`networks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/insert). After you have created the network, you can add subnets to it.

If you want to configure _internal_ IPv6 ranges on any subnets in this network, set `enableUlaInternalIpv6` to true. This option assigns a `/48` range from within the `fd20::/20` range used by Google for internal IPv6 subnet ranges. If you want to select which `/48` IPv6 range that is assigned, also use the `internalIpv6Range` field to specify a range.

You can omit both fields if you want to configure only _external_ IPv6 on subnets in this VPC network.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks
    {
      "autoCreateSubnetworks": false,
      "name": "NETWORK",
      "mtu": MTU,
      "enableUlaInternalIpv6": true,
      "internalIpv6Range": "ULA_IPV6_RANGE",
      "routingConfig": {
        "routingMode": "DYNAMIC_ROUTING_MODE"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the VPC network is created.
  * `NETWORK`: a name for the VPC network.
  * `MTU`: the maximum transmission unit (MTU), which is the largest packet size of the network. MTU can be set to any value from `1300` to `8896`. The default is `1460`. Before setting the MTU to a value higher than `1460`, review [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).
  * `ULA_IPV6_RANGE`: a `/48` prefix from within the `fd20::/20` range used by Google for internal IPv6 subnet ranges. If you don't provide a value for `internalIpv6Range`, Google selects a `/48` prefix for the network.
  * `DYNAMIC_ROUTING_MODE`: controls the behavior of Cloud Routers in the network. Can be either `GLOBAL` or `REGIONAL`. The default is `REGIONAL`. For more information, see [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks).



### About firewall rules

After you create a network, [create firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls) to allow or deny traffic between resources in the network, such as communication between VM instances. You also use firewall rules to control what traffic leaves or enters the VPC network to or from the internet.

## View networks

View the VPC and legacy networks in your project. For VPC networks, you can view information about their subnets and their subnet creation mode.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

The console lists all of your VPC and legacy networks.

  2. Select a VPC network to view its details, such as its peering connections and subnets.




###  gcloud 

  1. To list the networks in your project, use the [`networks list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/list).
         
         gcloud compute networks list
         

The command lists all of your VPC and legacy networks. Legacy networks show a subnet creation mode of `LEGACY`, while VPC networks show either `AUTO` or `CUSTOM`.
         
         NAME             SUBNET_MODE  BGP_ROUTING_MODE  IPV4_RANGE     GATEWAY_IPV4
         custom-network   CUSTOM       REGIONAL
         default          AUTO         REGIONAL
         legacy-network1  LEGACY       REGIONAL          10.240.0.0/16  10.240.0.1
         

  2. To describe a network and view its details, such as peering connections and subnets, use the [`networks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/describe).
         
         gcloud compute networks describe NETWORK
         

Replace `NETWORK` with the name of the network.




###  API 

  1. To list all networks in your project, make a `GET` request to the [`networks.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/list).
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks
         

Replace `PROJECT_ID` with the ID of the project that contains the VPC networks to list.

  2. To describe a network and view its details, make a `GET` request to the [`networks.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/get).
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK
         

Replace the following:

     * `PROJECT_ID`: the ID of the project that contains the VPC network.
     * `NETWORK`: the name of the VPC network to describe.



## Work with subnets

The following sections describe how to create and manage subnets.

### List subnets

You can see all the subnets that exist for a project or VPC network, including details about IP address utilization.

IP address utilization shows the number of free and allocated IP addresses that exist in a subnet. The allocated total includes IP addresses that are managed by Compute Engine, such as VMs and internal forwarding rules. However, this total doesn't include some IP addresses the are managed outside of Compute Engine, such as the stable IP addresses used by `ClusterIP` Kubernetes Services.

The allocated IP address total also includes the unusable [IPv4](https://docs.cloud.google.com/vpc/docs/subnets#unusable-ip-addresses-in-every-subnet) and [IPv6](https://docs.cloud.google.com/vpc/docs/subnets#unusable-ip-addresses-in-every-ipv6-subnet) addresses that are reserved for internal use.

To view utilization details for IPv6 addresses, use the gcloud CLI or send an API request. For IPv6 utilization, the total values are calculated by the following equation: (`high` * 2^64) + `low` = total value.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. To view subnets, do one of the following:

     * Click the name of a network, and then click the **Subnets** tab on the **VPC network details** page.

This view lets you add new subnets and modify other configurations for a single selected network.

     * Click the **Subnets in current project** tab and select one or more networks from the **VPC networks** list.

This view lets you list the subnets in more than one network.

The percentage of available IP addresses that are assigned to resources is displayed in the **Primary IPv4 range availability** column. To see the specific number of free and allocated IP addresses, hold the pointer over this column in the row where you want to view details.




###  gcloud 

You can list all subnets in all networks in your project, or you can show only the subnets for a particular network or region. The following examples demonstrate how to use the [`subnets list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list).

  * To list all subnets in all VPC networks, use the following command:
        
        gcloud compute networks subnets list
        

  * To list all subnets in a particular VPC network, use the following command:
        
        gcloud compute networks subnets list \
            --network=NETWORK
        

Replace `NETWORK` with the name of the network.

  * To list all subnets in a particular region, use the following command:
        
        gcloud compute networks subnets list \
            --filter="region:( REGION … )"
        

Replace `REGION` with the name of the region.

  * To list all subnets in your project and include their IP address utilization, use the following command:
        
        gcloud compute networks subnets list \
            --view=WITH_UTILIZATION
        




###  API 

  * To list all subnets in your project, make a `GET` request to the [`subnetworks.aggregatedList` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/aggregatedList).
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/subnetworks
        

Replace `PROJECT_ID` with the ID of the project that contains the subnets to list.

  * To list all subnets in a region and include their IP address utilization, make the following `GET` request:
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks?views=WITH_UTILIZATION
        




### Describe a subnet

You can view the details of an existing subnet—such as its primary IPv4 ranges, secondary IP ranges, IPv6 ranges, IP address utilization, and region—by following the steps in this section.

IP address utilization shows the number of free and allocated IP addresses that exist in a subnet. The allocated total includes IP addresses that are managed by Compute Engine, such as VMs and internal forwarding rules. However, this total doesn't include some IP addresses the are managed outside of Compute Engine, such as the stable IP addresses used by `ClusterIP` Kubernetes Services.

The allocated IP address total also includes the unusable [IPv4](https://docs.cloud.google.com/vpc/docs/subnets#unusable-ip-addresses-in-every-subnet) and [IPv6](https://docs.cloud.google.com/vpc/docs/subnets#unusable-ip-addresses-in-every-ipv6-subnet) addresses that are reserved for internal use.

To view utilization details for IPv6 addresses, use the gcloud CLI or send an API request. For IPv6 utilization, the total values are calculated by the following equation: (`high` * 2^64) + `low` = total value.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

All networks and subnets in your project are presented in a hierarchical view, where subnets are shown as entries within networks.

  2. To focus on subnets for a particular network, click the name of a network. On its _VPC network details_ page, click the name of a subnet in the **Subnets** tab to view its _Subnet details_ page.




###  gcloud 

  1. List subnets to determine the names and regions of existing subnets in your project.

  2. Use the [`subnets describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/describe).

     * To describe the subnet, use the following command:
           
           gcloud compute networks subnets describe SUBNET \
               --region=REGION
           

Replace the following:

       * `SUBNET`: the subnet to describe
       * `REGION`: the region of the subnet to describe
     * To describe the subnet and view its IP address utilization, use the following command:
           
           gcloud compute networks subnets describe SUBNET \
               --region=REGION \
               --view=WITH_UTILIZATION
           




###  API 

  1. To list subnets in a particular region and find a subnet's name, make a `GET` request to the [`subnetworks.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/list).
         
         GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks
         

Replace the following:

     * `PROJECT_ID`: the ID of the project that contains the subnets to list.
     * `REGION`: the name of the Google Cloud region that contains the subnets to list.
  2. Make a `GET` request to the [`subnetworks.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/get).

     * To describe the subnet, send the following request:
           
           GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET
           

Replace the following:

       * `PROJECT_ID`: the ID of the project that contains the subnet to describe.
       * `REGION`: the name of the Google Cloud region that contains the subnet to describe.
       * `SUBNET`: the name of the subnet to describe.
     * To describe the subnet and view its IP address utilization, send the following request:
           
           GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET?views=WITH_UTILIZATION
           




### Add an IPv4-only subnet

When you create a subnet, you set a name, a region, and at least a primary IPv4 address range according to the [name](https://docs.cloud.google.com/vpc/docs/subnets#subnet-name-limitations) and [IPv4 subnet range](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-range-limitations) limitations.

To create an IPv4-only subnet, do the following.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of a VPC network to show its _VPC network details_ page.

  3. Click **Add subnet**. In the panel that appears:

     1. Provide a **Name**.
     2. Select a **Region**.
     3. Enter an **IP address range**. This is the [primary IPv4 range](https://docs.cloud.google.com/vpc/docs/vpc#vpc_networks_and_subnets) for the subnet.

If you select a range that is not an RFC 1918 address, confirm that the range doesn't conflict with an existing configuration. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).

     4. To define a secondary range for the subnet, click **Create secondary IP range**.

If you select a range that is not an RFC 1918 address, confirm that the range doesn't conflict with an existing configuration. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).

     5. **Private Google access** : You can enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-access-options) for the subnet when you create it or later by editing it.

     6. **Flow logs** : You can enable [VPC flow logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) for the subnet when you create it or later by editing it.

     7. Click **Add**.




###  gcloud 

Use the [`subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
    
    
    gcloud compute networks subnets create SUBNET \
        --network=NETWORK \
        --range=PRIMARY_RANGE \
        --region=REGION
    

Replace the following:

  * `SUBNET`: a name for the new subnet.
  * `NETWORK`: the name of the VPC network that contains the new subnet.
  * `PRIMARY_RANGE`: the primary IPv4 range for the new subnet, in CIDR notation. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).
  * `REGION`: the Google Cloud region in which the new subnet is created.



You can modify the preceding command with the following optional flags:

  * `--secondary-range=SECONDARY_RANGE_NAME=SECONDARY_RANGE`: Replace `SECONDARY_RANGE_NAME` with a name for the secondary range. Replace `SECONDARY_RANGE` with a secondary range in CIDR notation. The [per network limits](https://docs.cloud.google.com/vpc/docs/quota#per_network) describe the maximum number of secondary ranges that you can define for each subnet.
  * `--enable-flow-logs`: Enables [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) in the subnet at creation time.
  * `--enable-private-ip-google-access`: Enables [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-access-options) in the subnet at creation time.
  * `--purpose`: Enables you to specify the [purpose of the subnet](https://docs.cloud.google.com/vpc/docs/subnets#purpose).
  * `--role`: Enables you to specify a role (active or backup) for a [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets).



Next, create [firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls#creating_firewall_rules).

### Terraform

Use a [Terraform module](https://github.com/terraform-google-modules/terraform-google-network).

`MTU` is the maximum transmission unit, or largest packet size, of the network. MTU can be set to any value from `1300` to `8896`. The default is `1460`. Before setting the MTU to a value higher than `1460`, review [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).
    
    
    module "test-vpc-module" {
      source       = "terraform-google-modules/network/google"
      version      = "~> 18.0"
      project_id   = var.project_id # Replace this with your project ID in quotes
      network_name = "my-custom-mode-network"
      mtu          = 1460
    
      subnets = [
        {
          subnet_name   = "subnet-01"
          subnet_ip     = "10.10.10.0/24"
          subnet_region = "us-west1"
        },
        {
          subnet_name           = "subnet-02"
          subnet_ip             = "10.10.20.0/24"
          subnet_region         = "us-west1"
          subnet_private_access = "true"
          subnet_flow_logs      = "true"
        },
        {
          subnet_name               = "subnet-03"
          subnet_ip                 = "10.10.30.0/24"
          subnet_region             = "us-west1"
          subnet_flow_logs          = "true"
          subnet_flow_logs_interval = "INTERVAL_10_MIN"
          subnet_flow_logs_sampling = 0.7
          subnet_flow_logs_metadata = "INCLUDE_ALL_METADATA"
          subnet_flow_logs_filter   = "false"
        }
      ]
    }

Next, create [firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules).

###  API 

Make a `POST` request to the [`subnetworks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks
    {
      "ipCidrRange": "IP_RANGE",
      "network": "NETWORK_URL",
      "name": "SUBNET"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the VPC network to modify.
  * `REGION`: the name of the Google Cloud region where the subnet is added.
  * `IP_RANGE`: the primary IPv4 address range for the subnet. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).
  * `NETWORK_URL`: the URL of the VPC network where you're adding the subnet.
  * `SUBNET`: a name for the subnet.



Next, create [firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules).

### Add a dual-stack subnet

**Note:** The Google Cloud console doesn't support selecting the IPv6 network tier. To explicitly set external IPv6 addresses to Standard Tier ([Preview](https://cloud.google.com/products#product-launch-stages)), use the gcloud CLI or the API.

Dual-stack subnets have both IPv4 and IPv6 address ranges. You can create a subnet with [external or internal IPv6 addresses](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges).

By default, the addresses for a subnet's IPv6 range are provided by Google. If you want to use BYOIP to bring your own IPv6 addresses, see [Assign subnet ranges](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes#create-subnets) instead.

To create a dual-stack subnet, do the following.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of a VPC network to show its _VPC network details_ page.

  3. Click **Add subnet**. In the panel that appears:

     1. Provide a **Name**.
     2. Select a **Region**.
     3. For **IP stack type** , select **IPv4 and IPv6 (dual-stack)**.
     4. Enter an **IPv4 range**. This is the [primary IPv4 range](https://docs.cloud.google.com/vpc/docs/vpc#vpc_networks_and_subnets) for the subnet.

If you select a range that is not an RFC 1918 address, confirm that the range doesn't conflict with an existing configuration. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).

     5. Select an **IPv6 access type** : **Internal** or **External**.

If you want to set the access type to **Internal** , but the **Internal** option is not available, check that an internal IPv6 range is assigned on the network.

     6. Click **Add**.




###  gcloud 

Use the [`subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create). If you're creating an internal IPv6 subnet range, make sure that the network has an assigned internal IPv6 ULA range.
    
    
    gcloud compute networks subnets create SUBNET \
        --network=NETWORK \
        --range=PRIMARY_IPv4_RANGE \
        --stack-type=IPV4_IPV6 \
        --ipv6-access-type=IPv6_ACCESS_TYPE \
        --ipv6-network-tier=IPV6_NETWORK_TIER \
        --region=REGION
    

Replace the following:

  * `SUBNET`: a name for the new subnet.
  * `NETWORK`: the name of the VPC network that will contain the new subnet.
  * `PRIMARY_IPv4_RANGE`: the primary IPv4 range for the new subnet, in CIDR notation. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).
  * `IPv6_ACCESS_TYPE`: the IPv6 access type. It can be `EXTERNAL` or `INTERNAL`.
  * `IPV6_NETWORK_TIER`: the subnet's network service tier. Can be `STANDARD` ([Preview](https://cloud.google.com/products#product-launch-stages)) or `PREMIUM`.
  * `REGION`: the Google Cloud region in which the new subnet will be created.



### Terraform

Use the [`google_compute_subnetwork` Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_subnetwork).

See the following example:
    
    
    resource "google_compute_subnetwork" "subnet_dual_stack" {
      name             = "subnet-dual-stack"
      ip_cidr_range    = "10.0.0.0/22"
      region           = "us-west2"
      stack_type       = "IPV4_IPV6"
      ipv6_access_type = "INTERNAL"
      network          = google_compute_network.default.id
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  API 

Make a `POST` request to the [`subnetworks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/insert). If you're creating an internal IPv6 subnet range, make sure that the network has an assigned internal IPv6 ULA range.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks
    {
      "ipCidrRange": "IP_RANGE",
      "network": "NETWORK_URL",
      "name": "SUBNET"
      "stackType": IPV4_IPV6,
      "ipv6AccessType": IPv6_ACCESS_TYPE
      "ipv6NetworkTier": IPV6_NETWORK_TIER,
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the VPC network to modify.
  * `REGION`: the name of the Google Cloud region where the subnet is added.
  * `IP_RANGE`: the primary IPv4 address range for the subnet. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).
  * `NETWORK_URL`: the URL of the VPC network where you're adding the subnet.
  * `SUBNET`: a name for the subnet.
  * `IPv6_ACCESS_TYPE`: the IPv6 access type. It can be `EXTERNAL` or `INTERNAL`.
  * `IPV6_NETWORK_TIER`: the subnet's network service tier. Can be `STANDARD` ([Preview](https://cloud.google.com/products#product-launch-stages)) or `PREMIUM`.



### Add an IPv6-only subnet

You can create an IPv6-only subnet with [external or internal IPv6 addresses](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges) enabled.

By default, the addresses for a subnet's IPv6 range are provided by Google. If you want to use BYOIP to bring your own IPv6 addresses, see [Assign subnet ranges](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes#create-subnets) instead.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. To view the **VPC network details** page, click the name of a VPC network.

  3. On the **Subnets** tab, click add_box**Add subnet**. In the panel that appears:

     1. Provide a **Name**.
     2. Select a **Region**.
     3. For **IP stack type** , select **IPv6 (single-stack)**.
     4. Select an IPv6 access type: **Internal** or **External**.

If you want to set the access type to **Internal** , but the **Internal** option is not available, check that an internal IPv6 range is assigned on the network.

     5. Click **Add**.




###  gcloud 

Use the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
    
    
    gcloud compute networks subnets create SUBNET \
        --network=NETWORK \
        --stack-type=IPV6_ONLY \
        --ipv6-access-type=IPv6_ACCESS_TYPE \
        --ipv6-network-tier=IPV6_NETWORK_TIER \
        --region=REGION
    

Replace the following:

  * `SUBNET`: a name for the new subnet.
  * `NETWORK`: the name of the VPC network to contain the new subnet.
  * `IPv6_ACCESS_TYPE`: the IPv6 access type. The access type can be either `EXTERNAL` or `INTERNAL`.
  * `REGION`: the Google Cloud region in which the new subnet is to be created.
  * `IPV6_NETWORK_TIER`: the subnet's network service tier. Can be `STANDARD` ([Preview](https://cloud.google.com/products#product-launch-stages)) or `PREMIUM`.



### Terraform

Use the [`google_compute_subnetwork` Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_subnetwork).

See the following example:
    
    
    resource "google_compute_subnetwork" "subnet_ipv6_only" {
      name             = "subnet-ipv6-only"
      region           = "us-central1"
      network          = google_compute_network.default.id
      stack_type       = "IPV6_ONLY"
      ipv6_access_type = "INTERNAL"
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  API 

Make a `POST` request to the [`subnetworks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks
    {
      "network": "NETWORK_URL",
      "name": "SUBNET"
      "stackType": IPV6_ONLY,
      "ipv6AccessType": IPv6_ACCESS_TYPE
      "ipv6NetworkTier": IPV6_NETWORK_TIER,
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the VPC network to modify.
  * `REGION`: the name of the Google Cloud region where the subnet is added.
  * `NETWORK_URL`: the URL of the VPC network where you are adding the subnet.
  * `SUBNET`: a name for the subnet.
  * `IPv6_ACCESS_TYPE`: the IPv6 access type. The access type can be either `EXTERNAL` or `INTERNAL`.
  * `IPV6_NETWORK_TIER`: the subnet's network service tier. Can be `STANDARD` ([Preview](https://cloud.google.com/products#product-launch-stages)) or `PREMIUM`.



### Change an IPv4-only subnet to dual-stack

Dual-stack subnets have both IPv4 and IPv6 subnet ranges. You can add either [an internal or an external IPv6 subnet range](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges) to an existing IPv4-only subnet in a custom mode VPC network. For more information, see [IPv6 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges).

By default, the addresses for a subnet's IPv6 range are provided by Google. If you want to use BYOIP to bring your own IPv6 addresses, see [Assign subnet ranges](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes#create-subnets) instead.

When you enable external IPv6 access on an IPv4-only subnet for the first time, you can also choose its IPv6 network tier. This option is available only when you use gcloud or the API. Additionally, you can't change the network tier after you've set it for a dual-stack subnet.

To change a subnet's stack type to dual-stack, do the following.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of a network to view the **VPC network details** page.

  3. In the **Subnets** tab, click the name of the subnet that you want to modify.

  4. In the **Subnet details** page, click **Edit**.

  5. For **IP stack type** , select **IPv4 and IPv6 (dual-stack)**.

  6. Select an **IPv6 access type** : **Internal** or **External**.

If you want to set the access type to **Internal** , but the **Internal** option is not available, check that an internal IPv6 range is assigned for the network.

  7. Click **Save**.




###  gcloud 

Use the [`subnets update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update).
    
    
    gcloud compute networks subnets update SUBNET \
        --stack-type=IPV4_IPV6 \
        --ipv6-access-type=IPv6_ACCESS_TYPE \
        [--ipv6-network-tier=IPV6_NETWORK_TIER] \
        --region=REGION
    

Replace the following:

  * `SUBNET`: the name of the subnet.
  * `REGION`: the region of the subnet.
  * `IPv6_ACCESS_TYPE`: the IPv6 access type of the subnet. It can be `EXTERNAL` or `INTERNAL`.
  * `IPV6_NETWORK_TIER`: the subnet's network service tier. Can be `STANDARD` ([Preview](https://cloud.google.com/products#product-launch-stages)) or `PREMIUM`. You can only specify this tier when updating an IPv4-only subnet to dual-stack with `EXTERNAL` IPv6 access for the first time.
  * `REGION`: the region of the subnet.



###  API 

Make a `PATCH` request to the [`subnetworks.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/patch).
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET
    {
      "stackType": IPV4_IPV6,
      "ipv6AccessType": IPv6_ACCESS_TYPE,
      "ipv6NetworkTier": IPV6_NETWORK_TIER
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the VPC network to modify.
  * `REGION`: the subnet's region.
  * `SUBNET`: the name of the subnet.
  * `IPv6_ACCESS_TYPE`: the IPv6 access type. It can be `EXTERNAL` or `INTERNAL`.
  * `IPV6_NETWORK_TIER`: the subnet's network service tier. Can be `STANDARD` ([Preview](https://cloud.google.com/products#product-launch-stages)) or `PREMIUM`. You can only specify this tier when updating an IPv4-only subnet to dual-stack with `EXTERNAL` IPv6 access for the first time.



### Change a dual-stack subnet to IPv4 only

You can change a subnet's stack type from IPv4 and IPv6 (dual-stack) to IPv4 only (single-stack) if the IPv6 access type is _external_.

If you make this change, you cannot create new dual-stack VMs that are connected to that subnet. However, existing dual-stack VMs are not affected. If you need to change a VM's stack type to be IPv4 only, see [Change the stack type of a VM](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address#update-vm-stacktype).

This change is supported in Google Cloud CLI and the API only.

Changing the stack type from IPv4 and IPv6 (dual-stack) to IPv4 only (single-stack) is not supported if the IPv6 access type is _internal_.

To change a subnet's stack type to IPv4 only, do the following.

###  gcloud 

Use the [`subnets update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update).
    
    
    gcloud compute networks subnets update SUBNET \
        --stack-type=IPV4_ONLY \
        --region=REGION
    

Replace the following:

  * `SUBNET`: the name of the subnet.
  * `REGION`: the subnet's Google Cloud region



###  API 

Make a `PATCH` request to the [`subnetworks.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/patch).
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET
    {
      "stackType": IPV4_ONLY,
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the VPC network to modify.
  * `REGION`: the subnet's Google Cloud region.
  * `SUBNET`: the name of the subnet.



### Add a subnet that uses an IPv6 BYOIP address range

Bring your own IP addresses (BYOIP) lets you import global unicast address (GUA) ranges that you can assign to a subnet's internal or external IPv6 address range. When you assign a subnet an internal GUA range, the addresses are configured as privately used GUAs that aren't publicly routable.

For more information, see [Assign subnet ranges](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes#create-subnets).

### Add a subnet that uses a reserved IPv4 internal range

If you have a reserved internal range with usage type set to `FOR_VPC`, and peering type set to `FOR_SELF`, you can create a subnet that uses all or part of that range. For more information, see [Create subnetworks with IPv4 internal ranges](https://docs.cloud.google.com/vpc/docs/create-use-internal-ranges#create-subnets-with-ranges).

### Delete a subnet

Use the following directions to delete a manually created subnet. Before you can delete a subnet, you must delete all resources that use it. For example, you need to [delete VMs](https://docs.cloud.google.com/compute/docs/instances/deleting-instance), reserved internal IP addresses, internal forwarding rules, and Cloud NAT gateways that use the subnet.

**Note:** For auto mode VPC networks, you **cannot** delete any of the automatically created subnets. However, you can convert an auto mode VPC network to a custom mode VPC network and then delete any unused automatically created subnets.

To delete a subnet, do the following.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

All networks and subnets in your project are presented in a hierarchical view, where subnets are shown as entries within networks.

  2. To view a particular network, click the name of a network. On its **VPC network details** page, click the name of a subnet in the **Subnets** tab to view its **Subnet details** page.

  3. Click **Delete subnet**.

  4. In the message that appears, click **Delete** to confirm.




###  gcloud 

Use the [`subnets delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/delete).
    
    
    gcloud compute networks subnets delete SUBNET \
        --region=REGION
    

Replace the following:

  * `SUBNET`: the name of the subnet to delete.
  * `REGION`: the region of the subnet to delete.



###  API 

Make a `DELETE` request to the [`subnetworks.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/delete).
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the subnet to delete.
  * `REGION`: the name of the Google Cloud region that contains the subnet to delete.
  * `SUBNET`: the name of the subnet to delete.



### Expand a primary IPv4 range

You can expand the primary IPv4 range of an existing subnet by modifying its subnet mask, setting the prefix length to a _smaller_ number. The proposed new primary IPv4 range of the subnet must follow the rules listed in the [IPv4 subnet range limitations](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-range-limitations).

When expanding the IPv4 range of an automatically created subnet in an auto mode VPC network (or in a custom mode VPC network that was previously an auto mode VPC network), the broadest prefix (subnet mask) you can use is `/16`. Any prefix broader than `/16` would conflict with [the primary IPv4 ranges of the other automatically created subnets](https://docs.cloud.google.com/vpc/docs/subnets#ip-ranges).

You can't expand subnets that are used exclusively for load balancer proxies. For more information, see [Proxy-only subnets for load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets).

Expanding the primary IPv4 range of a subnet can take several minutes to complete. During expansion, traffic within the subnet is _not_ interrupted.

If you expand the primary IPv4 range of a subnet, you might need to modify other configurations that are assuming this IP address range.

  * If you have [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) or [firewall policy rules](https://docs.cloud.google.com/vpc/docs/firewall-policies-rule-details) that use the original IPv4 address range as a source or destination, add additional firewall rules to apply the same rules to the extended range.
  * If a Google Kubernetes Engine (GKE) cluster uses the subnet whose primary IPv4 address range you expand, you must [add the expanded IP range to the control plane authorized networks list](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks#add).

**Caution:** Expanding the primary IPv4 range of a subnet cannot be undone. You cannot shrink the primary IPv4 range of a subnet. Expand primary IPv4 ranges conservatively; you can always expand them again. Consider IPv4 address space in any networks to which your VPC network is or will be connected before you expand a subnet's primary IPv4 range.

To expand a subnet's primary IPv4 range, do the following.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

All networks and subnets in your project are presented in a hierarchical view, where subnets are shown as entries within networks.

  2. To focus on subnets for a particular network, click the name of a network. On its **VPC network details** page, click the name of a subnet in the **Subnets** tab to view its **Subnet details** page.

  3. Click **Edit**.

  4. Enter a new, broader CIDR block in the **IP address range** field.

For valid ranges, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).

  5. Click **Save**.




###  gcloud 

Use the [`subnets expand-ip-range` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/expand-ip-range).
    
    
    gcloud compute networks subnets expand-ip-range SUBNET \
        --region=REGION \
        --prefix-length=PREFIX_LENGTH
    

Replace the following:

  * `SUBNET`: the name of the subnet.
  * `REGION`: the region in which the subnet is located.
  * `PREFIX_LENGTH`: a subnet mask size in bits. If the primary IPv4 range is `10.1.2.0/24`, you can supply `20` to reduce the subnet mask to 20 bits, which changes the primary IPv4 range to `10.1.2.0/20`. For valid ranges, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).



###  API 

Make a `POST` request to the [`subnetworks.expandIpCidrRange` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/expandIpCidrRange).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET/expandIpCidrRange
    {
      "ipCidrRange": "IP_RANGE"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the subnet to modify.
  * `REGION`: the name of the Google Cloud region that contains the subnet to modify.
  * `SUBNET`: the name of the subnet to modify.
  * `IP_RANGE`: the expanded IPv4 address range for the subnet. For valid ranges, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).



### Edit secondary IPv4 ranges

You can add secondary IPv4 ranges to subnets, or you can remove any secondary IPv4 range as long as no resources are using IP addresses in it.

###  gcloud 

To add a new secondary IPv4 range to a subnet, use the [`subnets update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update).
    
    
    gcloud compute networks subnets update SUBNET \
        --region=REGION \
        --add-secondary-ranges=SECONDARY_RANGE_NAME=SECONDARY_RANGE
    

Replace the following:

  * `SUBNET`: the name of the subnet.
  * `REGION`: the region in which the subnet is located.
  * `SECONDARY_RANGE_NAME`: a name for the secondary range.
  * `SECONDARY_RANGE`: the secondary IPv4 range in CIDR notation. For valid ranges, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).



To remove a secondary IPv4 range from a subnet, use the [`subnets update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update).
    
    
    gcloud compute networks subnets update SUBNET \
        --region=REGION \
        --remove-secondary-ranges=SECONDARY_RANGE_NAME
    

Replace the following:

  * `SUBNET`: the name of the subnet.
  * `REGION`: the region in which the subnet is located.
  * `SECONDARY_RANGE_NAME`: the name of the secondary range to remove.



###  API 

To modify secondary IPv4 address ranges for an existing subnet, make a `PATCH` request to the [`subnetworks.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/patch).
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET
    {
      "secondaryIpRanges": [
      {
        "rangeName": "SECONDARY_RANGE_NAME",
        "ipCidrRange": "IP_RANGE"
      },
      {
        "rangeName": "SECONDARY_RANGE_NAME",
        "ipCidrRange": "IP_RANGE"
      }],
      "fingerprint": "SUBNETWORK_FINGERPRINT"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the subnet to modify.
  * `REGION`: the name of the Google Cloud region that contains the subnet to modify.
  * `SUBNET`: the name of the subnet to modify.
  * `SECONDARY_RANGE_NAME`: a name for the secondary IPv4 address range.
  * `IP_RANGE`: the expanded IPv4 address range for the subnet. For valid ranges, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).
  * `SUBNET_FINGERPRINT`: the fingerprint ID for the existing subnet, which is provided when you describe a subnet.



## Modify networks

### Convert an auto mode VPC network to custom mode

You can convert an auto mode VPC network to a custom mode VPC network using this procedure. Review the [considerations for auto mode VPC networks](https://docs.cloud.google.com/vpc/docs/vpc#auto-mode-considerations) for background information about reasons why you might want to do this.

Converting an auto mode VPC network to a custom mode VPC network **preserves** all of its automatically created subnets and any subnets you have added. Subnet names and IP ranges are not changed.

**Important:** You cannot convert a custom mode VPC network to an auto mode VPC network. Conversion from auto to custom mode is a one-way process. Auto mode VPC networks that have been converted to custom mode operate as if they had been created in custom mode.

After you convert an auto mode VPC network to custom mode, you must review all API calls and gcloud CLI commands that implicitly reference any subnet that was automatically created while the network was in auto mode. API calls and commands will need to be modified so that they reference the subnet explicitly. For gcloud CLI commands that have a subnet specification flag (`--subnet`), that flag is required to reference subnets in a custom mode VPC network.

To convert an auto mode VPC network to a custom mode VPC network, do the following.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of a VPC network to show its **VPC network details** page.

  3. Click **Edit**.

  4. In the **Subnet creation mode** section, choose **Custom**.

  5. Click **Save**.




###  gcloud 

Use the [`networks update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/update).
    
    
    gcloud compute networks update NETWORK \
        --switch-to-custom-subnet-mode
    

Replace `NETWORK` with the name of the network to update.

###  API 

Make a `POST` request to the [`networks.switchToCustomMode` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/switchToCustomMode).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK/switchToCustomMode
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the VPC network to convert.
  * `NETWORK`: the name of the VPC network to convert.



### Assign an internal IPv6 ULA range to a network

If you want to configure internal IPv6 unique local addresses (ULAs) on a subnet, you must first enable ULA addresses on the VPC network. When you enable ULAs, a `/48` ULA range is assigned to the network. Addresses are allocated from this range when you assign a ULA range to a subnet.

This step isn't required if you're assigning an internal IPv6 subnet range from a BYOIP sub-prefix.

After you have enabled a ULA range for your VPC network, you can do the following:

  * Add dual-stack subnets
  * Change an IPv4-only subnet to dual-stack
  * Add IPv6-only subnets



To assign an internal ULA range to a network, do the following.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of a VPC network to show its _VPC network details_ page.

  3. Click **Edit**.

  4. In the **Private IPv6 address settings** section, select **Configure a ULA internal IPv6 range for this VPC Network**.

  5. Optional: You can provide the prefix to use for the internal IPv6 range.

     1. For **Allocate ULA internal IPv6 range** , click **Manually**.
     2. Enter a `/48` range from within the `fd20::/20` range.

If the range is in use, you are prompted to enter a different range.

  6. Click **Save**.




###  gcloud 

Use the [`networks update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/update).

The `--enable-ula-internal-ipv6` flag assigns a `/48` prefix from within the `fd20::/20` range used by Google for internal IPv6 subnet ranges. If you want to select the `/48` IPv6 range that is assigned, use the `--internal-ipv6-range` flag to specify a range.
    
    
    gcloud compute networks update NAME \
        --enable-ula-internal-ipv6 \
        [ --internal-ipv6-range=ULA_IPV6_RANGE ]
    
    

Replace the following:

  * `NAME`: the name of the VPC network.
  * `ULA_IPV6_RANGE`: the range of IPv6 addresses to which you need to allocate a ULA prefix.



###  API 

Make a `PATCH` request to the [`networks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/insert).

Setting `enableUlaInternalIpv6` to true assigns a `/48` range from within the `fd20::/20` range used by Google for internal IPv6 subnet ranges. If you want to select which `/48` IPv6 range is assigned, also use the `internalIpv6Range` field to specify a range.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networksa/NETWORK
    {
      "enableUlaInternalIpv6": true,
      "internalIpv6Range": "ULA_IPV6_RANGE",
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the VPC network is created.
  * `NETWORK`: a name for the VPC network.
  * `ULA_IPV6_RANGE`: a `/48` prefix from within the `fd20::/20` range used by Google for internal IPv6 subnet ranges. If you don't provide a value for `internalIpv6Range`, Google selects a `/48` prefix for the network.



### Change the dynamic routing mode

Each VPC network has an associated dynamic routing mode that controls the behavior of Cloud Routers in the network. Refer to the [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks) section in _VPC networks_ to understand how each mode affects how Cloud Routers share routes and apply learned routes.

**Caution:** Changing the dynamic routing mode has the potential to interrupt traffic within the network, or enable or disable routes in unexpected ways. Carefully review the role of each Cloud Router before changing the dynamic routing mode.

To change a VPC network's dynamic routing mode, do the following.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of a VPC network to show its **VPC network details** page.

  3. Click **Edit**.

  4. In the **Dynamic routing mode** section, choose either **Global** or **Regional**.

  5. Click **Save**.




###  gcloud 

Use the [`networks update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/update).
    
    
    gcloud compute networks update NETWORK \
        --bgp-routing-mode=DYNAMIC_ROUTING_MODE
    

Replace the following:

  * `NETWORK`: the name of the VPC network to update.
  * `DYNAMIC_ROUTING_MODE`: controls the behavior of Cloud Routers in the network. Can be either `global` or `regional`. The default is `regional`. For more information, see [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks).



###  API 

Make a `PATCH` request to the [`subnetworks.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/patch).
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK
    {
      "routingConfig": {
        "routingMode": "ROUTING_MODE"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the VPC network to modify.
  * `NETWORK`: the name of the VPC network to modify.
  * `ROUTING_MODE`: controls the behavior of Cloud Routers in the network. Can be either `GLOBAL` or `REGIONAL`. The default is `REGIONAL`. For more information, see [dynamic routing mode](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks).



### Change the MTU of a network

For information about changing the MTU of a VPC network, see [Change the MTU setting of a VPC network](https://docs.cloud.google.com/vpc/docs/change-mtu-vpc-network).

### Delete a network

If a network is not being used, you can delete it. Before you can delete a network, you must delete all resources in all of its subnets, and all resources that reference the network. Resources that reference the network include [VPC Network Peering connections](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#deleting-peer), [Cloud VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/deleting-a-gateway), [Cloud Routers](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-routers#deletes), [Serverless VPC Access connectors](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#delete-connector) and their connected services, [firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls#deleting_firewall_rules), and [custom static routes](https://docs.cloud.google.com/vpc/docs/using-routes#deletingaroute).

To delete a VPC network, do the following.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of a VPC network to show its **VPC network details** page.

  3. Click **Delete VPC network**.

  4. In the message that appears, click **Delete** to confirm.




###  gcloud 

Use the [`networks delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/delete).
    
    
    gcloud compute networks delete NETWORK
    

Replace `NETWORK` with the name of the network to delete.

###  API 

Make a `DELETE` request to the [`networks.delete` method](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/delete).
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the VPC network to delete.
  * `NETWORK`: the name of the VPC network to delete.



## Monitor your VPC network

You can enable logging of network flows to and from VMs. See [Using VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs) for instructions.

You can enable logging for firewall rules to see which rules allowed or blocked which traffic. See [Using Firewall Rules Logging](https://docs.cloud.google.com/vpc/docs/using-firewall-rules-logging) for instructions.

## Migrate VMs

You can migrate your virtual machine (VM) instances from one network to another within a given project. For instructions, see [Migrating a VM between networks](https://docs.cloud.google.com/compute/docs/instances/migrating-interfaces-between-networks).

## Troubleshooting

### Can't delete a VPC network that was used with Serverless VPC Access

You might receive an error when attempting to delete a VPC network for which Serverless VPC Access was configured even if you have deleted the associated Serverless VPC Access connector. The error message is similar to the following: `The network resource 'RESOURCE' cannot be deleted because it is being used by a Serverless resource.` This error occurs because there is still an association between one or more serverless resources and the VPC network.

To resolve this issue, remove any associations to the Serverless VPC Access connector from the serverless resources:

  1. If any Cloud Run services or functions used the connector, then for each service or function, follow the steps to [Disconnect a Cloud Run service from a VPC network](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors#disconnect-service).

  2. If any Cloud Run jobs used the connector, then for each job, follow the steps to [Disconnect a Cloud Run job from a VPC network](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors#disconnect-job)

  3. If any App Engine services used the connector, then for each service, follow the steps to [Disconnect an App Engine service from a VPC network](https://docs.cloud.google.com/appengine/docs/standard/connecting-vpc#disconnect).

  4. After you disconnect all serverless resources from the VPC network, delete the VPC network.




To prevent this issue from happening again, ensure that you disconnect any serverless resources before deleting a connector as described in [Delete a connector](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors#delete).

In rare cases, you might still receive an error after completing the steps in this section. If you still can't delete the VPC network, contact [Cloud Customer Care](https://cloud.google.com/support).

### Error: `Constraint constraints/compute.requireVpcFlowLogs violated`

This error occurs if both of these conditions apply:

  * An organization policy constraint has been set that requires that VPC Flow Logs is configured.

  * You create a subnet, or update the VPC Flow Logs configuration of an existing subnet, and the configuration does not meet the requirements of the policy.




For more information about this constraint and its effects on subnet creation and updates, see [Organization policy constraints for VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/org-policy-flow-logs).

### Resource not found error

When deleting a VPC network, you might see a message that is similar to the following: `The resource "aet-uscentral1-subnet--1-egrfw" was not found.`

For information about this error and its solution, see [Resource not found error](https://docs.cloud.google.com/vpc/docs/using-firewalls#resource-not-found) in the VPC firewall rules documentation.

### Resource already exists

When you create a subnet, you see a message that is similar to the following: `The resource 'SUBNET_URI' already exists`. You see this error if there's already a subnet with the same name and region as the subnet that you're trying to create. For more information about subnet names, see [Limitations for naming subnets](https://docs.cloud.google.com/vpc/docs/subnets#subnet-name-limitations).

## What's next

  * For information about routes, see [Routes](https://docs.cloud.google.com/vpc/docs/routes).
  * For information about firewall rules, see [Firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls).
  * For more details about VPC networking, see [Advanced VPC concepts](https://docs.cloud.google.com/vpc/docs/advanced-vpc).
  * Learn about [using a hybrid subnet to migrate workloads to a VPC network without changing IP addresses](https://docs.cloud.google.com/vpc/docs/hybrid-subnets).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how VPC performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try VPC free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
