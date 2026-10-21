---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/netapp-storage-pool/
title: Create a NetApp Volumes storage pool \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:32:41.478249+00:00
---

# Create a NetApp Volumes storage pool  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/netapp-storage-pool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create a NetApp Volumes storage pool Stay organized with collections  Save and categorize content based on your preferences. 

Use the `netapp-storage-pool` module to provision a storage pool for [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview).

NetApp Volumes is a managed Google Cloud service that provides Network File System (NFS) and Server Message Block (SMB) shared file systems to Compute Engine instances. The service provides advanced data management capabilities and highly scalable capacity and performance.

To support NetApp Volumes, Cluster Toolkit uses two modules:

  * **`netapp-storage-pool`** : Provisions a storage pool. Storage pools are pre-provisioned storage capacity containers that host volumes. A pool also defines fundamental properties for all its volumes, such as:

    * Region
    * Attached network
    * Service level
    * Customer-managed encryption key (CMEK) encryption
    * Active Directory or Lightweight Directory Access Protocol (LDAP) settings
  * **`netapp-volume`** : Provisions a volume inside an existing storage pool. A volume is a file-system container that you share by using NFS or SMB.




For the complete list of inputs and outputs for this module, see the [`netapp-storage-pool` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/file-system/netapp-storage-pool#inputs) page in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch. To view a working example of a blueprint configured for the `netapp-storage-pool` module, go to the [Cluster blueprint catalog](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog) page, click the **Select storage type** menu and then select **NetApp Volumes**. For more information about creating and customizing blueprints, see [Cluster blueprint](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint).
  * The `netapp-storage-pool` module does not create a continuous long-running workload or a full cluster. It provisions a storage pool for [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview).
  * Verify that your project has unused quota for NetApp Volumes in your target region. Standard service levels have separate quota limits from Premium and Extreme service levels. For more information, see [Quotas and limits](https://docs.cloud.google.com/netapp/volumes/docs/quotas).
  * Verify that your network is configured for private service access. NetApp Volumes uses private service access to connect volumes to your network.



### Required roles

To get the permissions that you need to create and manage NetApp Volumes storage pools, ask your administrator to grant you the following IAM roles on your project: 

  * [NetApp Volumes Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)
  * [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## NetApp Volumes service levels

The `netapp-storage-pool` module supports the following NetApp Volumes service levels:

  * **Standard** : 16 KiBps throughput per provisioned GiB of volume capacity.
  * **Premium** : 64 KiBps throughput per provisioned GiB of volume capacity. You can optionally use auto-tiering with this service level.
  * **Extreme** : 128 KiBps throughput per provisioned GiB of volume capacity. You can optionally use auto-tiering with this service level.



For more information about capability differences, see [Google Cloud NetApp Volumes service levels](https://cloud.google.com/netapp/volumes/docs/discover/service-levels).

**Note:** The module doesn't support [Flex service levels](https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels). However, you can connect to existing Flex volumes by using the [`pre-existing-network-storage` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/pre-existing-network-storage).

## Configure the network

To provision a NetApp Volumes storage pool, add the `netapp-storage-pool` module to your blueprint. You must connect the storage pool to a VPC network that has private service access configured. For more information, see [Configure private services access](https://docs.cloud.google.com/vpc/docs/configure-private-services-access).

### Use a new VPC network

The following example creates a new VPC network and configures private service access. Both resources are passed to the `netapp_pool` module to help ensure the correct build order and network configuration.
    
    
    deployment_groups:
    - group: primary
      modules:
      - id: network
        source: modules/network/vpc
        settings:
          region: REGION
    
      - id: private_service_access
        source: modules/network/private-service-access
        use: [network]
        settings:
          prefix_length: 24
          service_name: "netapp.servicenetworking.goog"
          deletion_policy: "ABANDON"
    
      - id: netapp_pool
        source: modules/file-system/netapp-storage-pool
        use: [network, private_service_access]
        settings:
          pool_name: POOL_NAME
          capacity_gib: 20000
          service_level: "EXTREME"
          region: REGION
    
    

Replace the following:

  * `REGION`: the Google Cloud region for your network and storage pool
  * `POOL_NAME`: the name for your storage pool



### Use an existing VPC network

The following example creates a storage pool by using an existing network that is already configured with private service access for NetApp Volumes.
    
    
    deployment_groups:
    - group: primary
      modules:
      - id: network
        source: modules/network/pre-existing-vpc
        settings:
          project_id: PROJECT_ID
          region: REGION
          network_name: NETWORK_NAME
    
      - id: netapp_pool
        source: modules/file-system/netapp-storage-pool
        use: [network]
        settings:
          pool_name: POOL_NAME
          capacity_gib: 20000
          service_level: "EXTREME"
          region: REGION
    
    

Replace the following:

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `REGION`: the Google Cloud region where your network is located.
  * `NETWORK_NAME`: the name of your existing VPC network.
  * `POOL_NAME`: the name for your storage pool.



## Storage pool example

The following example demonstrates a storage pool configuration that defines all available settings.
    
    
      - id: netapp_pool
        source: modules/file-system/netapp-storage-pool
        use: [network, private_service_access]
        settings:
          pool_name: "mypool"
          region: "us-west4"
          capacity_gib: 2048
          service_level: "EXTREME"
          active_directory_policy: "projects/PROJECT_ID/locations/us-east4/activeDirectories/my-ad"
          cmek_policy: "projects/PROJECT_ID/locations/us-east4/kmsConfigs/my-cmek-policy"
          ldap_enabled: false
          allow_auto_tiering: false
          description: "Demo storage pool"
          labels:
            owner: bob
    
    

## What's next

  * For the complete list of inputs and outputs for this module, see the [`netapp-storage-pool` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/file-system/netapp-storage-pool#inputs) page in the Cluster Toolkit GitHub repository.
  * For a complete list of supported modules, see the [compatibility matrix](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/docs/network_storage.md#compatibility-matrix) on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
