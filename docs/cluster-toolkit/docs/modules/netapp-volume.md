---
url: https://docs.cloud.google.com/cluster-toolkit/docs/modules/netapp-volume/
title: Create a NetApp Volumes volume \u00a0|\u00a0 Cluster Toolkit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:23.837012+00:00
---

# Create a NetApp Volumes volume  |  Cluster Toolkit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-toolkit/docs/modules/netapp-volume/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Toolkit ](https://docs.cloud.google.com/cluster-toolkit/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-toolkit/docs/overview)



Send feedback 

#  Create a NetApp Volumes volume Stay organized with collections  Save and categorize content based on your preferences. 

Use the `netapp-volume` module to create a [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview) volume.

NetApp Volumes is a managed Google Cloud service that provides Network File System (NFS) and Server Message Block (SMB) shared file systems to Compute Engine instances. It offers advanced data management capabilities and highly scalable capacity and performance. For more information, see [NetApp Volumes overview](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview).

To support NetApp Volumes, Cluster Toolkit uses two modules:

  * **`netapp-storage-pool`** : Provisions a storage pool. Storage pools are pre-provisioned storage capacity containers that host volumes. A pool also defines fundamental properties for all its volumes, such as the region, attached network, service level, Customer-Managed Encryption Key (CMEK) encryption, and Active Directory or Lightweight Directory Access Protocol (LDAP) settings.
  * **`netapp-volume`** : Provisions a volume inside an existing storage pool. A volume is a file-system container that you share by using NFS or SMB.



For the complete list of inputs and outputs for this module, see the [`netapp-volume` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/file-system/netapp-volume#inputs) page in the Cluster Toolkit GitHub repository.

## Before you begin

Before you begin, verify that you meet the following requirements:

  * You have installed and configured Cluster Toolkit. For installation instructions, see [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).
  * You have an existing cluster blueprint. You can use and modify an existing blueprint or create one from scratch.
  * You have created a NetApp Volumes storage pool by using the `netapp-storage-pool` module. You must create volumes inside a storage pool and consume capacity from that pool.
  * For a detailed example of this module, see [examples/netapp-volumes.yaml](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/examples/netapp-volumes.yaml).

**Warning:** The `netapp-volume` module does not implement volume deletion protection. Volumes created with this module are not persistent. If you run the [`gcluster destroy` command](https://docs.cloud.google.com/cluster-toolkit/docs/reference/gcluster-destroy), then Cluster Toolkit permanently deletes the volume and all its data. If you want to retain the volume, then we recommend that you create the volume manually and use the [`pre-existing-network-storage` module](https://docs.cloud.google.com/cluster-toolkit/docs/modules/pre-existing-network-storage) instead.

### Required roles

To get the permissions that you need to create and mount NetApp Volumes volumes, ask your administrator to grant you the following IAM roles on your project: 

  * [NetApp Volumes Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/netapp#netapp.admin) (`roles/netapp.admin`)
  * [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a volume

The following examples show how to configure the `netapp-volume` module. Both examples require an existing storage pool.

### Minimal configuration

The following example provisions a 1,024 GiB volume by using a minimal set of parameters. By default, the module exports to the `10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16` IP address ranges with the `no_root_squash` option.
    
    
      - id: home_volume
        source: modules/file-system/netapp-volume
        use: [netapp_pool]
        settings:
          volume_name: "eda-home"
          capacity_gib: 1024
          local_mount: "/eda-home"
          protocols: ["NFSV3"]
          region: REGION
    
    

Replace `REGION` with the Google Cloud region where your storage pool is located.

### Advanced configuration

The following example defines all available parameters, including custom mount options, export policies, and auto-tiering.
    
    
      - id: shared_volume
        source: modules/file-system/netapp-volume
        use: [netapp_pool]
        settings:
          volume_name: "eda-shared"
          capacity_gib: 25000
          large_capacity: true
          local_mount: "/shared"
          mount_options: "rw"
          protocols: ["NFSV3","NFSV4"]
          region: REGION
          unix_permissions: "0777"
          export_policy:
          - allowed_clients: "10.10.20.8,10.10.20.9"
            has_root_access: true
            access_type: "READ_WRITE"
            nfsv3: false
            nfsv4: true
          - allowed_clients: "10.0.0.0/8"
            has_root_access: false
            access_type: "READ_WRITE"
            nfsv3: true
            nfsv4: false
          tiering_policy:
            tier_action: "ENABLED"
            cooling_threshold_days: 31
          description: "Shared volume for EDA job"
          labels:
            owner: bob
    
    

## Protocol support

Because Cluster Toolkit provisions Linux-based compute clusters, the `netapp-volume` module supports only NFSv3 and NFSv4.1. Server Message Block (SMB) is not supported.

## Large volumes

You can create volumes larger than 15 TiB as Large Volumes. Large volumes can grow up to 3 PiB and scale read performance up to 29 GiBps.

Large volumes provide six IP addresses, which the module exports using the `server_ips` output. When you connect to a large volume to a client by using the `use` keyword, Cluster Toolkit uses only the first IP address to mount the volume on clients.

**Note:** This feature is in allow-listed General Availability (GA). To request access, see [Large capacity volumes](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/overview#large-capacity-volumes).

## Auto-tiering support

If your storage pool has auto-tiering enabled, then you can enable auto-tiering on the individual volume by configuring the `tiering_policy`.
    
    
    tiering_policy:
      tier_action: "ENABLED"
      cooling_threshold_days: 31
    

For more information, see [Manage auto-tiering](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-auto-tiering).

## Use existing volumes

NetApp Volumes volumes are standard NFS exports. If you want to use an existing volume that you did not create with Cluster Toolkit, then use the `pre-existing-network-storage` module.
    
    
    - id: homefs
      source: modules/file-system/pre-existing-network-storage
      settings:
        server_ip: SERVER_IP
        remote_mount: nfsshare
        local_mount: /home
        fs_type: nfs
    
    

Replace `SERVER_IP` with the IP address of your NFS server.

**Note:** You must know the `server_ip` before deployment. The `pre-existing-network-storage` module doesn't support specifying a list of multiple IP addresses for large volumes.

## FlexCache support

FlexCache technology accelerates data access, reduces WAN latency, and lowers WAN bandwidth costs for read-intensive workloads. When you create a FlexCache volume, you create a remote cache of an existing origin volume that contains only the actively accessed data. For more information, see [About FlexCache](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/overview#about_flexcache).

Deploying FlexCache volumes requires manual steps on the ONTAP origin side, which Cluster Toolkit does not automate. Therefore, the `netapp-volume` module does not support deploying FlexCache volumes directly. To use FlexCache, deploy the volumes manually and then integrate them by using the `pre-existing-network-storage` module.

## What's next

  * For the complete list of inputs and outputs for this module, see the [`netapp-volume` module](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/modules/file-system/netapp-volume#inputs) page in the Cluster Toolkit GitHub repository.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
