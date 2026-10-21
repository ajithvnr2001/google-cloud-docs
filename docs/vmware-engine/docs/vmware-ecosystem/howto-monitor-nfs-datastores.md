---
url: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-monitor-nfs-datastores/
title: Monitor NFS Datastores \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:58.232973+00:00
---

# Monitor NFS Datastores  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/howto-monitor-nfs-datastores/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor NFS Datastores

You can monitor NFS Datastore performance in vCenter and in Cloud Monitoring:

  * **vCenter:** Provides performance metrics as observed by the ESXi hosts and cluster on which the NFS Datastore is mounted.
  * **Cloud Monitoring:** Provides performance metrics for NFS volumes from Filestore and Google Cloud NetApp Volumes, as observed by the respective service. We recommend using Cloud Monitoring metrics to monitor the performance of your file shares, track latency, and set up alerts based on your workload's needs.



VMware Engine automatically monitors your NFS Datastores for potential issues. When a condition requires your attention or indicates a problem, VMware Engine generates an alert. You receive these alerts as emails sent to the essential contacts for your project and as entries in Cloud Logging.

The following sections describe the alerts you might receive.

## High storage usage

**Alert name:** `vmware_nfs_datastore_storage_usage_high`

This alert triggers when the used space on an NFS Datastore exceeds 80% of its total capacity.

**Recommended action:** To resolve the issue, increase the size of the underlying NFS volume to avoid running out of space.

**Example notification:**
    
    
    The private cloud `{.PCName}` in project `{.ProjectNumber}` can be affected because
    the used space for the NFS Datastore `{.NFS_Datastore}` has exceeded
    80%. Increase the size of your NFS volume and Datastore to avoid an out-of-space
    condition and disruption to your applications. If you have any questions,
    contact Cloud Customer Care.
    

## Datastore inaccessibility

**Alert name:** `vmware_host_datastore_nfs_mount_inaccessible`

This alert triggers when one or more ESXi hosts in a cluster cannot access a mounted NFS Datastore.

**Recommended action:** This alert indicates an issue that the VMware Engine team is actively working to resolve. If you have questions, contact [Cloud Customer Care](https://docs.cloud.google.com/support).

**Example notification:**
    
    
    The NFS Datastore `{.NFS_Datastore}` in private cloud `{.PCName}`
    mounted to cluster `{.cluster}` is inaccessible from one or more hosts in
    cluster `{.cluster}`. The VMware Engine team is aware of the issue and is working on a
    resolution. If you have any questions, contact Cloud Customer Care.
    

## Unmanaged Datastore detected

**Alert name:** `vmware_nfs_datastore_not_allowed`

This alert triggers when VMware Engine detects an NFS Datastore that you mounted manually, without using the VMware Engine API. These unmanaged Datastores aren't supported going forward.

**Recommended action:** To ensure proper integration and support, contact [Cloud Customer Care](https://docs.cloud.google.com/support) to schedule a migration of the unmanaged Datastore to a fully managed VMware Engine Datastore.

**Example notification:**
    
    
    Google Cloud VMware Engine Service identified an NFS volume within your Google Cloud project `{.ProjectNumber}` as a mounted NFS Datastore in your private cloud `{.PCName}` but is not managed by VMware Engine. To ensure seamless operation and proper integration, contact Cloud Customer Care to arrange its no-data-copy migration.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
