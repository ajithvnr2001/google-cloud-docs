---
url: https://cloud.google.com/asset-inventory/docs/overview/
title: Cloud Asset Inventory overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:16.714459+00:00
---

# Cloud Asset Inventory overview  |  Google Cloud Documentation

> Source: https://cloud.google.com/asset-inventory/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Guides ](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview)



Send feedback 

#  Cloud Asset Inventory overview Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Asset Inventory is a global metadata inventory service that lets you view, search, export, monitor, and analyze your Google Cloud asset metadata. It's designed for tasks like compliance tracking, scheduled audits, and analytics.

**Note:** Cloud Asset Inventory isn't designed for real time querying of assets, where missing or stale asset data could break production availability or security enforcement. For live querying of data, call a service's API directly instead. To learn more, see Consistency model.

Tasks that you might use Cloud Asset Inventory for include the following:

  * **Resource discovery and management** : filter by metadata properties such as location, time created, tags, and status. 
  * **Resource monitoring** : track changes to a resource over time to create an audit trail, debug problems, and manage compliance drift. 
  * **Security and cost audits** : find resources that are over-permissioned, publicly exposed, or unused to minimize attack surface and optimize costs.



Create, update, and delete history for assets is kept for up to 35 days. Assets that haven't changed in the past 35 days return their latest status.

## Work with assets in Google Cloud

Here's how you can work with your assets:

  * [**List** your assets](https://cloud.google.com/asset-inventory/docs/list-assets) and their relationships in a particular project, folder, or organization, and [get asset history up to 35 days in the past](https://cloud.google.com/asset-inventory/docs/get-asset-history).

  * [**Search** for your resources](https://cloud.google.com/asset-inventory/docs/search-resources) and their [IAM allow policies](https://cloud.google.com/asset-inventory/docs/search-allow-policies) using a custom query language, or [query your assets with BigQuery SQL](https://cloud.google.com/asset-inventory/docs/query-assets-with-sql).

  * **Export** your asset metadata to [BigQuery](https://cloud.google.com/asset-inventory/docs/export-bigquery) or [Cloud Storage](https://cloud.google.com/asset-inventory/docs/export-cloud-storage). 

  * [**Analyze** what would happen if a resource was moved to another project](https://cloud.google.com/resource-manager/docs/analyze-move).

  * [**Analyze** your IAM and organization policies](https://cloud.google.com/asset-inventory/docs/view-resource-policies) on resources, and [**View** your effective IAM policies](https://cloud.google.com/asset-inventory/docs/view-resource-policies#view-effective-policies) on resources to see who has access to what. 

  * **Monitor** your assets for changes by [setting up and subscribing to a feed](https://cloud.google.com/asset-inventory/docs/monitor-asset-changes). 

  * [**Generate insights** from your assets](https://cloud.google.com/asset-inventory/docs/asset-insights) to help improve your security posture.




## Asset metadata sources

Asset metadata can come from the following places:

  * **Google Cloud resources** , such as Compute Engine VM instances, Cloud Storage buckets, and App Engine instances.

  * **Policies** set on Google Cloud resources, such as IAM policies, organization policies, and Access Context Manager policies.

  * **Runtime information** from [OS inventory management](https://cloud.google.com/compute/docs/instances/os-inventory-management).




## Asset types, asset names, and content types

Cloud Asset Inventory offers multiple methods to interact with your assets. Depending on the method you use and the response detail you want, you might need to specify asset types, asset names, and content types in your requests.

### Asset types

Some Cloud Asset Inventory methods return results based on asset types. Asset types include Google Cloud resources, policies, OS inventory runtime information, and relationships. The available asset types and the Cloud Asset Inventory methods that support them are detailed in [Asset types](https://cloud.google.com/asset-inventory/docs/asset-types).

### Asset names

Some Cloud Asset Inventory methods return results based on asset names. When specifying an asset name, you must use its full resource name. See [Asset names](https://cloud.google.com/asset-inventory/docs/asset-names) for a list of full resource names.

### Content types

You can request additional metadata on a resource by specifying a metadata content type. If you don't specify a content type, then only a basic response is returned, which contains information such as the asset name, the last time it was updated, and the projects, folders, and organizations it belongs to.

Content type names differ depending on how you interact with Cloud Asset Inventory. The RPC and REST API names are the same. However, the gcloud CLI content type names follow a different pattern. For consistency and ease of explanation, the rest of this documentation refers to content types by their RPC and REST names.

The following table details the content types and their descriptions:

Content type | Description  
---|---  
RPC and REST name | gcloud CLI name |   
`ACCESS_POLICY` | `access-policy` | The [ Access Context Manager](https://cloud.google.com/access-context-manager/docs/overview) policy set on an asset.  
`IAM_POLICY` | `iam-policy` | The IAM policy metadata binding to the resource.  
`ORG_POLICY` | `org-policy` |  The organization policy metadata set on an asset. This content type outputs legacy organization policy v1. For organization policy v2, try the `resource` content type and a resource type of `orgpolicy.googleapis.com/Policy`.   
`OS_INVENTORY` | `os-inventory` |  The runtime OS inventory information. To enable OS inventory, complete the relevant steps in [Set up VM Manager](https://cloud.google.com/compute/docs/manage-os).   
`RELATIONSHIP` | `relationship` |  Requires access to the [ Security Command Center Premium or Enterprise tier](https://cloud.google.com/security-command-center/pricing#tier-pricing). Many Google Cloud assets are connected to each other by relationships. For example, a [Compute instance group](https://cloud.google.com/compute/docs/instance-groups) can contain a [ Compute instance](https://cloud.google.com/compute/docs/instances), or a [ GKE cluster](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture) can contain a [ node](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#cp_node).  Relationship data is available from May 30th, 2022. A relationship might have its own update timestamp, because it might be inferred at a different time than the source asset updates. See [ Relationship types](https://cloud.google.com/asset-inventory/docs/relationship-types) for a list of the supported relationships.  
`RESOURCE` | `resource` | The resource's metadata.  
**Note:** The `ancestors` field in the response to some requests can be inconsistent across content types. This is because there are different data ingestion schedules for each content type, and their update times might not align. Check the `update_time` field to ensure that the asset has the most up-to-date information. [Contact Cloud Customer Care](https://cloud.google.com/asset-inventory/docs/get-support) if the inconsistency lasts for more than 24 hours.

### How responses change with content type

The following examples show how responses change when listing VM instances in a project through Cloud Asset Inventory with different content types.

#### No content type

If you specify no content type when listing VM instances, you receive only the instance names, the last time they were updated, and what projects, folders, and organizations they belong to.

Expand for response example
    
    
    ---
    ancestors:
    - projects/PROJECT_NUMBER
    - folders/FOLDER_NUMBER
    - organizations/ORGANIZATION_ID
    assetType: compute.googleapis.com/Instance
    name: //compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
    updateTime: '2023-11-15T12:28:30.087825Z'

#### IAM_POLICY content type

If you specify the `IAM_POLICY` content type, you also receive the IAM bindings on the VM, if there are any.

Expand for response example
    
    
    ---
    ancestors:
    - projects/PROJECT_NUMBER
    - folders/FOLDER_NUMBER
    - organizations/ORGANIZATION_ID
    assetType: compute.googleapis.com/Instance
    **iamPolicy:
      bindings:
      - members:
        - user: USER_EMAIL_ADDRESS
        role: roles/compute.securityAdmin
      etag: ETAG**
    name: //compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
    updateTime: '2023-12-19T23:35:42.673842Z'

#### RELATIONSHIP content type

Relationships require access to the [Security Command Center Premium or Enterprise tier](https://cloud.google.com/security-command-center/pricing#tier-pricing).

If you specify the `RELATIONSHIP` content type, you also receive metadata associated with the VM instance's related assets.

Expand for response example
    
    
    ---
    ancestors:
    - projects/PROJECT_NUMBER
    - folders/FOLDER_NUMBER
    - organizations/ORGANIZATION_ID
    assetType: compute.googleapis.com/Instance
    name: //compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
    **relatedAsset:
      ancestors:
      - projects/ PROJECT_NUMBER
      - folders/FOLDER_NUMBER
      - organizations/ORGANIZATION_ID
      asset: //compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/disks/INSTANCE_NAME
      assetType: compute.googleapis.com/Disk
      relationshipType: COMPUTE_INSTANCE_USE_DISK**
    updateTime: '2023-12-19T23:35:42.673842Z'

When using the `RELATIONSHIP` content type, instead of requesting all relationships, you can request specific [relationship types](https://cloud.google.com/asset-inventory/docs/relationship-types). 

#### RESOURCE content type

If you specify the `RESOURCE` content type, you also receive all the metadata associated with the VM.

Expand for response example
    
    
    ---
    ancestors:
    - projects/PROJECT_NUMBER
    - folders/FOLDER_NUMBER
    - organizations/ORGANIZATION_ID
    assetType: compute.googleapis.com/Instance
    name: //compute.googleapis.com/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
    **resource:
      data:
        allocationAffinity:
          consumeAllocationType: ANY_ALLOCATION
        canIpForward: false
        confidentialInstanceConfig:
          enableConfidentialCompute: true
        cpuPlatform: AMD Rome
        creationTimestamp: '2023-11-14T14:35:37.059-08:00'
        deletionProtection: false
        description: ''
        disks:
        - architecture: X86_64
          autoDelete: true
          boot: true
          deviceName: INSTANCE_NAME
          diskSizeGb: '10'
          guestOsFeatures:
          - type: VIRTIO_SCSI_MULTIQUEUE
          - type: SEV_CAPABLE
          - type: SEV_SNP_CAPABLE
          - type: SEV_LIVE_MIGRATABLE
          - type: UEFI_COMPATIBLE
          - type: GVNIC
          index: 0
          interface: NVME
          licenses:
          - https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-2004-lts
          mode: READ_WRITE
          shieldedInstanceInitialState:
            dbx:
            - content: DATA
              fileType: BIN
            dbxs:
            - content: DATA
              fileType: BIN
          source: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/INSTANCE_NAME
          type: PERSISTENT
        displayDevice:
          enableDisplay: false
        fingerprint: FINGERPRINT
        id: 'ID'
        keyRevocationActionType: NONE_ON_KEY_REVOCATION
        labelFingerprint: LABEL_FINGERPRINT
        lastStartTimestamp: '2023-11-15T04:28:30.005-08:00'
        machineType: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/machineTypes/n2d-standard-2
        name: INSTANCE_NAME
        networkInterfaces:
        - accessConfigs:
          - name: External NAT
            natIP: 34.27.105.222
            networkTier: PREMIUM
            type: ONE_TO_ONE_NAT
          fingerprint: jKU51FdTluk=
          name: nic0
          network: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/default
          networkIP: 10.128.15.212
          nicType: GVNIC
          stackType: IPV4_ONLY
          subnetwork: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks/default
        reservationAffinity:
          consumeReservationType: ANY_ALLOCATION
        resourceStatus: {}
        scheduling:
          automaticRestart: true
          onHostMaintenance: TERMINATE
          preemptible: false
          provisioningModel: STANDARD
        selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME
        serviceAccounts:
        - email: PROJECT_NUMBER-compute@developer.gserviceaccount.com
          scopes:
          - https://www.googleapis.com/auth/devstorage.read_only
          - https://www.googleapis.com/auth/logging.write
          - https://www.googleapis.com/auth/monitoring.write
          - https://www.googleapis.com/auth/servicecontrol
          - https://www.googleapis.com/auth/service.management.readonly
          - https://www.googleapis.com/auth/trace.append
        shieldedInstanceConfig:
          enableIntegrityMonitoring: true
          enableSecureBoot: false
          enableVtpm: true
        shieldedInstanceIntegrityPolicy:
          updateAutoLearnPolicy: true
        startRestricted: false
        status: RUNNING
        tags:
          fingerprint: FINGERPRINT
        zone: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE
      discoveryDocumentUri: https://www.googleapis.com/discovery/v1/apis/compute/v1/rest
      discoveryName: Instance
      location: ZONE
      parent: //cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER
      version: v1**
    updateTime: '2023-11-15T12:28:30.087825Z'

## Consistency model

Before architecting solutions involving Cloud Asset Inventory, it helps to understand its consistency model so you can build robust software:

  * **Eventual consistency** : Cloud Asset Inventory uses periodic data synchronization. Because of this, newly provisioned or modified resources might not be immediately queryable. Indexing delays are possible; as a result, state changes can take time to propagate across search queries, feeds, and exports.

  * **Potential for data/event loss** : When receiving information from other Google Cloud services, there might be temporary drops, lag, or out-of-order deliveries.




See the Cloud Asset Inventory [best practices](https://cloud.google.com/asset-inventory/docs/best-practice) for more information on designing services that consume Cloud Asset Inventory data.

## What's next

  * [View your assets](https://cloud.google.com/asset-inventory/docs/view-assets)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
