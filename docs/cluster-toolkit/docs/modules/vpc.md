---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/vpc/
title: Create a VPC network \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:12.692227+00:00
---

# Create a VPC network  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create a VPC network Stay organized with collections  Save and categorize content based on your preferences. 

Use the `vpc` module to create a new VPC network that contains one or more subnetworks and a Cloud Router for each region that has a subnetwork.

By using this module, you establish an isolated and secure network foundation for your cluster infrastructure. By default, this module simplifies your network configuration because it automatically provisions the following resources:

  * A Cloud NAT gateway to provide outbound internet access for Compute Engine instances that lack public IP addresses. Compute instances with public IP addresses bypass the NAT gateway to directly access the public internet.
  * A firewall rule that authorizes inbound Secure Shell (SSH) access from Identity-Aware Proxy.
  * A firewall rule that authorizes all internal traffic within the network.
  * Google Private Access for all subnetworks. This configuration helps to ensure that your compute instances can access Google APIs and services, such as Cloud Storage, even if the instances lack public IP addresses.



You can customize or disable these default behaviors by adjusting the module inputs. This module relies on networking support from the [Cloud Foundation Toolkit](https://cloud.google.com/foundation-toolkit).

For the complete list of inputs and outputs for this module, see the [`vpc` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/network/vpc#inputs) page in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for the `vpc` module, see the [`examples/hpc-slurm.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/hpc-slurm.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page.
  * The `vpc` module doesn't create a continuous long-running workload or a full cluster. It provisions a [VPC network](https://docs.cloud.google.com/vpc/docs/vpc) and a single subnetwork that provide isolated and secure networking for your cluster.



To get the permissions that you need to use Identity-Aware Proxy for SSH access, ask your administrator to grant you the [IAP-secured Tunnel User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.tunnelResourceAccessor) (`roles/iap.tunnelResourceAccessor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Required roles

To get the permissions that you need to create the VPC network and associated resources, ask your administrator to grant you the [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure subnetworks

The `vpc` module always provisions at least one primary subnetwork to host your resources.

The module determines the primary subnetwork based on the first element in the `subnetworks` list. If you don't provide the `subnetworks` list, the module calculates a default subnetwork based on the values that you provide for the `subnetwork_name` variable, the `region` variable, the `network_address_range` variable, and the `default_primary_subnetwork_size` variable.

If you define multiple subnetworks within the `subnetworks` list, you must specify either the `subnet_ip` setting or the `new_bits` setting for each subnetwork:

  * **CIDR IP range:** Define an explicit Classless Inter-Domain Routing (CIDR) IP address range by using the `subnet_ip` field.
  * **Subnetwork size:** Define the size of the CIDR subnetwork in bits by using the `new_bits` field. If you use this setting, the module calculates the IP address ranges by using the `network_address_range` value as the base IP address.

**Warning:** If you use the `new_bits` setting to calculate IP address ranges automatically, we don't recommend that you modify individual subnetworks after the initial deployment. Modification causes the module to recalculate the IP address ranges for every subnetwork. To add new subnetworks safely, append them to the end of the `subnetworks` list.



## Configure SSH access

By default, the module creates a firewall rule to authorize inbound SSH access from IAP. To use this connection method, you must possess the IAP-secured Tunnel User role (`roles/iap.tunnelResourceAccessor`).

If you prefer to authorize standard SSH access from a known IP address instead of using IAP, you can define a custom rule by using the `firewall_rules` setting.

## Example configurations

The following sections provide examples that demonstrate how to configure the `vpc` module.

### Basic network creation

The following example demonstrates how to create a new VPC network named `cluster-net` by using the default configuration:
    
    
      - id: network1
        source: modules/network/vpc
        settings:
          network_name: cluster-net
    
    

### Custom SSH access

The following example demonstrates how to configure a custom firewall rule that authorizes SSH access from a specific IP address:
    
    
      - id: network1
        source: modules/network/vpc
        settings:
          firewall_rules:
          - name: ssh-my-machine
            direction: INGRESS
            ranges: [YOUR_IP_ADDRESS/32]
            allow:
            - protocol: tcp
              ports: [22]
    
    

Replace `YOUR_IP_ADDRESS` with the source IP address from which you plan to initiate the SSH connection.

## Deprecated variables

Google has deprecated the following variables:

  * `primary_subnetwork`
  * `additional_subnetworks`
  * `subnetwork_size`



To retain existing functionality and support explicit IP address ranges, we recommend that you adopt the following replacement variables:

  * **`subnetworks`:** use this variable to replace the `primary_subnetwork` variable and the `additional_subnetworks` variable. You can generate a value for this new variable by merging your previous primary and additional subnetworks into a single list.
  * **`default_primary_subnetwork_size`:** use this variable to replace the `subnetwork_size` variable. You can directly copy your explicit setting from the `subnetwork_size` variable.

**Note:** Cluster Toolkit doesn't support configurations that mix deprecated variables with the new replacement variables.

## What's next

  * For the complete list of inputs and outputs for this module, see the [`vpc` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/network/vpc#inputs) page in the Cluster Toolkit GitHub repository.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
