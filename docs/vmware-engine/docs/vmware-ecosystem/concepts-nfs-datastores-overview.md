---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/concepts-nfs-datastores-overview/
title: NFS Datastores overview \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:51.298480+00:00
---

# NFS Datastores overview  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/concepts-nfs-datastores-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# NFS Datastores overview

As your data grows, you might need to scale storage for your VMware workloads independently from compute resources. While the default vSAN storage in VMware Engine provides high performance for your most demanding applications, adding capacity requires adding a full node, including compute and networking resources that you might not need.

To give you more flexibility, VMware Engine supports external Network File System (NFS) Datastores from services like Filestore and Google Cloud NetApp Volumes. Using an external NFS Datastore is a cost-effective way to scale storage for Tier-2 and Tier-3 applications, backups, and archival workloads that don't require the high performance of vSAN.

## Supported NFS storage services

You can use external NFS Datastores with the following Google Cloud services:

  * **Filestore:** For details on Filestore specific prerequisites, limitations and mounting instructions, see [Use Filestore Volumes as vSphere Datastores](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-filestore-storage-for-vmware-engine-datastores).
  * **Google Cloud NetApp Volumes:** For details on GCNV specific prerequisites, limitations and mounting instructions, see [Use Google Cloud NetApp Volumes as vSphere Datastores](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-cloud-volumes-datastores-vmware-engine).



## General prerequisites to using NFS Datastores with VMware Engine

Before you mount an external NFS volume as a Datastore, you must meet the following prerequisites:

### NFS Volume requirements

NFS volumes must meet the following requirements:

  * **Location:** The NFS volume (Filestore instance or Google Cloud NetApp Volumes volume) and the VMware Engine cluster must reside in the same Google Cloud region. VMware Engine doesn't support mounting Datastores across different regions. For stretched private clouds, only regional Datastores are supported.
  * **Protocol:** VMware Engine supports only NFS version 3 (NFSv3) for use as a VMware Engine Datastore. NFSv4.1 is not supported.
  * **Delete protection:** If using Filestore or Google Cloud NetApp Volumes, you must enable delete protection on the volume to prevent accidental deletion and data loss.



### VMware Engine service account permissions

To create and mount a Datastore backed by Filestore or Google Cloud NetApp Volumes, VMware Engine uses a Google-managed service account to access NFS resources. Grant the following IAM roles to the service account (`service-PROJECT_NUMBER@gcp-sa-vmwareengine.iam.gserviceaccount.com`):

  * **`roles/compute.networkViewer`:** Required for all Datastore types to view network peerings. Grant this role on the project where the NFS volume resides. If you use Shared VPC, grant this role on the host project instead.
  * **`roles/file.viewer`:** Required for Datastores backed by Filestore to access Filestore instances. Grant this role on the project where Filestore resides.
  * **`roles/netapp.viewer`:** Required for Datastores backed by Google Cloud NetApp Volumes to access Google Cloud NetApp Volumes volumes. Grant this role on the project where Google Cloud NetApp Volumes resides.



Use the following commands to grant these roles:

When granting the `roles/compute.networkViewer` role for a Shared VPC configuration, make sure to replace the project ID in the example with your host project ID.

**For Filestore:**
    
    
    gcloud projects add-iam-policy-binding FILESTORE_PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-vmwareengine.iam.gserviceaccount.com \
        --role=roles/file.viewer
    
    gcloud projects add-iam-policy-binding FILESTORE_PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-vmwareengine.iam.gserviceaccount.com \
        --role=roles/compute.networkViewer
    

**For Google Cloud NetApp Volumes:**
    
    
    gcloud projects add-iam-policy-binding NETAPP_PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-vmwareengine.iam.gserviceaccount.com \
        --role=roles/netapp.viewer
    
    gcloud projects add-iam-policy-binding NETAPP_PROJECT_ID \
        --member=serviceAccount:service-PROJECT_NUMBER@gcp-sa-vmwareengine.iam.gserviceaccount.com \
        --role=roles/compute.networkViewer
    

Replace the following:

  * `FILESTORE_PROJECT_ID`: The project ID where your Filestore instance resides.
  * `NETAPP_PROJECT_ID`: The project ID where your Google Cloud NetApp Volumes volume resides.
  * `PROJECT_NUMBER`: The project number where VMware Engine is enabled.



### Service subnet requirements

You must have a dedicated service subnet with a unique CIDR range allocated for NFS traffic between ESXi hosts and the NFS volume. You configure the service subnet as follows:

  * You must configure a CIDR range for the service subnet that has enough IP addresses to assign one to each node in the private cloud.
  * You can only use the service subnet for NFS Datastore traffic, but you can connect the same subnet to multiple different NFS Datastores.
  * You must add the reserved CIDR allocation for the service subnet to the allowed clients list or export policy of your NFS volume. For Filestore, add an access control rule for the service subnet CIDR range. For Google Cloud NetApp Volumes, add the CIDR to the **Allowed Clients** section of the volume's export rules.



NSX-T gateway and distributed firewall rules don't apply to service subnets.

### Network connection requirements

An active connection must exist between the NFS volume's VPC network and the VMware Engine network (VEN) of the private cloud where you will mount the Datastore. Network charges resulting from storage access within a region don't apply when using Filestore with Private Service Access (PSA).

When connecting to network file services, use one of the following connection methods, depending on your private cloud's VEN type:

  * **Standard VEN:** Private clouds created in a standard VEN use VPC Network Peering to connect to network file services like Filestore (using PSA) or Google Cloud NetApp Volumes.
  * **Legacy VEN:** Private clouds that operate on a legacy VEN require a private connection to connect with network file services. If you delete a private connection while an NFS Datastore is in use, it will disrupt access to the Datastore. Therefore, ensure you don't delete a private connection while an NFS Datastore is mounted and in use.



## Interoperability with private cloud Lifecycle

NFS Datastores managed by the VMware Engine API remain persistent across private cloud lifecycle events in the following ways:

  * **Cluster expansion and contraction:** If you add nodes to a cluster with mounted NFS Datastores, VMware Engine automatically mounts those Datastores on the new nodes. If you remove nodes when contracting a cluster, their vmknic IP addresses are released.
  * **Node reboot:** The NFS Datastore configuration on a node is persistent and remains intact after a node reboot.
  * **Software upgrades:** NFS Datastores mounted on hosts are unaffected by ESXi, vCenter, and NSX-T component upgrades.



## Migration from legacy NFS Datastore mounts

If you created NFS Datastores in VMware Engine before January 1, 2026, you're using the legacy model. To transition to the supported and recommended model, contact Cloud Customer Care to begin the migration process.

## Known issues

The following are known issues with external NFS Datastores:

  * During private cloud soft deletion, the network path to the Datastore is severed.
  * After VPC Network Peering is established, route propagation to vSphere nodes can take up to 20 minutes.



## What's next

  * To mount a Filestore volume, see [Use Filestore Volumes as vSphere Datastores](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-filestore-storage-for-vmware-engine-datastores).
  * To mount a Google Cloud NetApp Volumes volume, see [Use Google Cloud NetApp Volumes as vSphere Datastores](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-netapp-volumes-for-vmware-engine-datastores).
  * To manage Datastores using the API or Google Cloud CLI, see [Manage NFS Datastores](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-manage-nfs-datastores).
  * To monitor NFS Datastores, see [Monitor NFS Datastores](https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-monitor-nfs-datastores).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
