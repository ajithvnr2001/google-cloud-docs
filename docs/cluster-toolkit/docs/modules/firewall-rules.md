---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/firewall-rules/
title: Create firewall rules \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:18.875058+00:00
---

# Create firewall rules  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/firewall-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create firewall rules Stay organized with collections  Save and categorize content based on your preferences. 

Use the `firewall-rules` module to create custom firewall rules for your existing VPC networks.

This module lets you define specific ingress traffic policies and egress traffic policies. By using these policies, you can help secure your infrastructure by checking that only authorized connections reach your Compute Engine instances. You can use this module with other Cluster Toolkit modules to construct app-specific security perimeters, or you can combine it with the [`pre-existing-vpc` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/pre-existing-vpc) to authorize traffic for pre-existing networks.

For the complete list of inputs and outputs for this module, see the [`firewall-rules` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/network/firewall-rules#inputs) page in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You've installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for the `firewall-rules` module, see the [`examples/gke-a4/gke-a4.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-a4/gke-a4.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page.
  * The `firewall-rules` module doesn't create a continuous long-running workload or a full cluster. It creates [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) for your VPC network to control traffic between cluster components.



### Required roles

To get the permissions that you need to create firewall rules, ask your administrator to grant you the [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Define firewall rules

To help secure your network, you must specify the exact ports, protocols, and IP address ranges that your deployment requires.

The following example from the [`ml-slurm.yaml` file on GitHub](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/ml-slurm.yaml) shows how to define ingress rules. This configuration assumes that the default VPC network requires internal traffic access and Identity-Aware Proxy tunneling for Secure Shell (SSH) connections.
    
    
    - group: primary
      modules:
      - id: network
        source: modules/network/pre-existing-vpc
    
      # This example assumes that the default network requires internal traffic
      # access and IAP tunneling for SSH connections
      - id: firewall_rule
        source: modules/network/firewall-rules
        use:
        - network
        settings:
          ingress_rules:
          - name: $(vars.deployment_name)-allow-internal-traffic
            description: Allow internal traffic
            destination_ranges:
            - $(network.subnetwork_address)
            source_ranges:
            - $(network.subnetwork_address)
            allow:
            - protocol: tcp
              ports:
              - 0-65535
            - protocol: udp
              ports:
              - 0-65535
            - protocol: icmp
          - name: $(vars.deployment_name)-allow-iap-ssh
            description: Allow IAP-tunneled SSH connections
            destination_ranges:
            - $(network.subnetwork_address)
            source_ranges:
            - 35.235.240.0/20
            allow:
            - protocol: tcp
              ports:
              - 22
    

## What's next

  * For the complete list of inputs and outputs for this module, see the [`firewall-rules` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/network/firewall-rules#inputs) page in the Cluster Toolkit GitHub repository.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
