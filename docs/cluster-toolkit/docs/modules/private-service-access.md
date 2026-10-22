---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/private-service-access/
title: Configure private service access \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:15.730061+00:00
---

# Configure private service access  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/private-service-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Configure private service access Stay organized with collections  Save and categorize content based on your preferences. 

Use the `private-service-access` module to configure private service access for your VPC networks.

This module lets you create more secure, private connections between your VPC network and Google-managed services, such as Cloud SQL or Google Cloud NetApp Volumes. This private connection ensures that your data doesn't traverse the public internet, which enhances security and performance.

The module automatically completes the following configuration steps:

  * Creates an IP address allocation with a prefix length that you specify by using the `prefix_length` variable. You can let Cluster Toolkit pick the base address automatically, or you can specify the base address by using the `address` variable.
  * Creates a private connection that establishes a VPC Network Peering connection between your VPC network and the network of the service producer.
  * Imports and exports custom routes when you connect to Google Cloud NetApp Volumes.



For the complete list of inputs and outputs for this module, see the [`private-service-access` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/network/private-service-access#inputs) page in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. For a working example of a blueprint configured for the `private-service-access` module, see the [`examples/gke-managed-lustre.yaml`](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/gke-managed-lustre.yaml) file. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * To view a complete list of blueprints, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page.



### Required roles

To get the permissions that you need to configure private service access, ask your administrator to grant you the [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure the deletion policy

Some services, such as Cloud SQL or Google Cloud NetApp Volumes, don't immediately delete internal backend resources. This deletion process can take up to a few hours. If you attempt to delete the private service access peering connection while the backend resources still exist, then the deletion fails.

To help the deletion process for these private service access connections, set the `deletion_policy` field to the `ABANDON` value.

The following sections provide examples that demonstrate how to configure the `private-service-access` module.
    
    
      - source: modules/network/private-service-access
        id: ps_connect
        use: [network]
        settings:
          deletion_policy: "ABANDON"
    

### Connect standard services

The following example demonstrates how to connect services that use a standard service networking connection:
    
    
      - source: modules/network/vpc
        id: network
    
      - source: modules/network/private-service-access
        id: ps_connect
        use: [network]
    

### Connect Google Cloud NetApp Volumes

The following example demonstrates how to connect Google Cloud NetApp Volumes so that you can use the volume as a shared file system.

This configuration imports and exports the custom routes and sets the deletion policy to abandon the connection upon destruction.
    
    
      - source: modules/network/vpc
        id: network
    
      - source: modules/network/private-service-access
        id: ps_connect
        use: [network]
        settings:
          prefix_length: 24
          service_name: "netapp.servicenetworking.goog"
          deletion_policy: "ABANDON"
    

## What's next

  * For the complete list of inputs and outputs for this module, see the [`private-service-access` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/network/private-service-access#inputs) page in the Cluster Toolkit GitHub repository.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
