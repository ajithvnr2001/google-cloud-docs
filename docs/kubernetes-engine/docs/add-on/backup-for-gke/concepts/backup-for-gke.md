---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke/
title: Backup for GKE overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:38.410166+00:00
---

# Backup for GKE overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Backup for GKE overview Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

Backup for GKE is a managed service for backing up and restoring workloads and persistent data in GKE clusters. Protecting your workloads with Backup for GKE helps you satisfy disaster recovery requirements, support continuous integration and continuous deployment (CI/CD) pipelines, clone workloads, and achieve recovery point objectives (RPO).

The service consists of two primary architectural components:

  * **A control plane API** : A Google Cloud REST API that manages backup and restore cloud resources.
  * **An in-cluster agent** : A GKE add-on that runs in each cluster where you back up or restore workloads.

**Note:** Backup for GKE is a separate service from GKE, with independent compliance certifications and accreditations. For more information, see Service architecture on this page.

## Workload backup and restore capabilities

When enabled, Backup for GKE integrates with the GKE console, the Google Cloud CLI CLI, and REST APIs to provide unified workflows for development and operations.

A workload backup captures two forms of data:

  * **Configuration backup** : A collection of Kubernetes resource manifests extracted from the cluster API server that records the state of your Kubernetes resources.
  * **Volume backup** : A collection of volume snapshots that correspond to `PersistentVolumeClaim` resources referenced in the configuration backup.



You can back up all workloads in a cluster or select specific workloads to protect by namespace or by application. You can back up workloads from one cluster and restore them into another cluster. You can also schedule automated backups to run on recurring schedules so that you can recover workloads quickly during an outage.

Backup for GKE supports both intra-project and cross-project operations. You can create backup plans and restore plans within the same Google Cloud project as your cluster, or coordinate backups and restores across multiple projects to isolate environments or meet compliance requirements.

Restoring a workload re-creates Kubernetes resources and persistent volumes in the target cluster. After Backup for GKE creates the resource manifests, GKE reconciles the workload by scheduling Pods to nodes and starting containers.

During a restore operation, you can apply optional transformation rules to modify resource configurations before they are created in the target cluster. Transformation rules match specified Kubernetes resources and replace attribute values, such as updating storage classes or modifying namespace references.

### Supported backup and restore scenarios

You can combine selective backup scopes, restore scopes, and transformation rules to support scenarios such as the following:

  * **Disaster recovery** : Back up all workloads in a cluster and restore them into a separate cluster in another region.
  * **Selective rollback** : Back up all workloads, but selectively roll back a single corrupted or misconfigured workload in the source cluster.
  * **Namespace cloning** : Back up resources in one namespace and restore them into a new namespace within the same cluster or a different cluster.
  * **Workload migration** : Migrate or clone application workloads from one GKE cluster to another.
  * **Storage configuration updates** : Update storage parameters during restore, such as moving a workload from a zonal persistent disk to a regional persistent disk.



To back up workloads, the source cluster must have the Backup for GKE agent enabled. To restore workloads, the target cluster must already exist and have the Backup for GKE agent enabled.

## Service architecture

Backup for GKE divides responsibilities between a Google Cloud control plane service and an in-cluster agent:

  * **The Backup for GKE service** : Runs in Google Cloud infrastructure and serves as the centralized control plane. The service provides a resource-based REST API and powers the Backup for GKE interface in the Google Cloud console.
  * **The Backup for GKE agent** : Runs as a workload in each GKE cluster where backup or restore operations occur. The agent communicates with the Backup for GKE service to execute backup and restore tasks.



The following architecture diagram illustrates the interactions between user tools, the Backup for GKE service, and the in-cluster agent:

![Architectural diagram showing user clients interacting with the Backup for GKE service, which coordinates with an in-cluster agent to back up and restore Kubernetes resources and persistent volumes.](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/images/bfg_arch.svg)

As shown in the diagram:

  1. **Clients submit requests** : Users manage backups and restores through the Google Cloud console, the Google Cloud CLI CLI, or `kubectl`. These requests target the Consumer API (`v1`).
  2. **Control plane orchestrates jobs** : The Backup for GKE service processes requests and coordinates with the in-cluster agent through the internal Agent API (`v1agent`).
  3. **Agent executes operations** : The Backup for GKE agent interacts with the local Kubernetes API server to capture configuration manifests or apply restored resources.
  4. **Data is stored securely** : Configuration manifests and Persistent Disk volume snapshots are stored in a dedicated, Google-managed tenant project isolated from cluster compute resources.



### Control plane service and cloud resources

The Backup for GKE service exposes a REST API that manages resources in the [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). You interact with four primary resource types:

#### Operational resources

Operational resources represent individual backup and restore executions:

  * **`Backup`** : Represents the point-in-time backup of a GKE cluster or a subset of workloads. Creating a `Backup` resource initiates the backup process, which extracts Kubernetes configuration manifests and initiates Persistent Disk volume snapshots. Deleting a `Backup` resource permanently deletes the stored configuration artifacts and volume snapshots.
  * **`Restore`** : Represents the restoration of data and configurations from a specific `Backup` resource into a target GKE cluster. Creating a `Restore` resource triggers the restore workflow. Deleting a `Restore` resource removes the restore execution history from the database without affecting the resources running in the cluster.



#### Configuration resources

Configuration resources define reusable policies for creating backups and running restores:

  * **`BackupPlan`** : A configuration template that defines when and how to create a chain of `Backup` resources. A backup plan specifies the source cluster, the backup scope (all workloads, selected namespaces, or specific protected applications), the schedule, retention settings, and the storage region. If you store backups in a region different from the source cluster, outbound network data transfer charges apply. For more information, see [Backup for GKE pricing](https://cloud.google.com/kubernetes-engine/pricing#backup-for-gke). 
  * **`RestorePlan`** : A configuration template that defines how to execute restorations from a specified backup plan into a target cluster. A restore plan specifies the target cluster, the restore scope, resource conflict handling rules, volume data restore policies, and optional transformation rules. The target cluster must exist before you can create a restore plan.



### In-cluster agent operations

The Backup for GKE agent runs as a workload inside each GKE cluster where you enable data protection. The agent performs the following tasks:

  * **Backup orchestration** : 
    * Queries the Kubernetes API server for workload manifests matching the backup plan scope.
    * Serializes resource manifests into an encrypted archive and uploads the archive to Google-managed storage.
    * Triggers volume snapshots for persistent volumes associated with `PersistentVolumeClaim` resources.
  * **Restore orchestration** : 
    * Retrieves the resource archive from storage.
    * Applies configured transformation rules and conflict resolution policies.
    * Re-creates Kubernetes resources in the target cluster.
    * Provisions persistent volumes from snapshots and binds them to workloads in the target cluster.



You don't directly interact with the agent pods. When you create a `Backup` or `Restore` cloud resource, the Backup for GKE service automatically creates corresponding custom resources (`BackupJob` or `RestoreJob`) in the cluster, which the agent detects and executes.

To define custom backup and restore logic (such as pausing database writes or executing pre-backup scripts), you can define [`ProtectedApplication`](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/protected-application) custom resources in your cluster.

For historical information about the preview agent for GKE clusters earlier than version 1.24, see [Preview agent deprecation](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-preview).

## Zonal redundancy and high availability

Backup for GKE provides regional high availability by replicating service components and backup data across multiple zones within a Google Cloud region:

  * **Control plane resilience** : The Backup for GKE control plane service is deployed across at least three zones in each supported region, ensuring that API operations continue without interruption if an individual zone experiences an outage.
  * **Storage replication** : Backup configuration archives and Persistent Disk volume snapshots are stored with regional redundancy across multiple zones.
  * **Managed replication** : The service relies on regional Google Cloud storage infrastructure to handle replication automatically, without requiring manual zone-level configuration.



## Limitations

Backup for GKE protects Kubernetes workloads and persistent disk volumes, but excludes cluster infrastructure and external services.

Backup for GKE does not back up the following resources:

  * **Cluster infrastructure configurations** : Cluster-level settings such as node pools, machine types, node count, networking configuration, and enabled cluster features. To reproduce cluster configurations, use infrastructure as code tools like Terraform.
  * **Container image binaries** : The container images referenced by Pod manifests. Backup for GKE backs up the YAML manifests that point to container images, but does not store the image layers. You must maintain the container images in an artifact registry such as [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs).
  * **External services and databases** : The state or configuration of services located outside the Kubernetes cluster, such as Cloud SQL instances, Cloud Storage buckets, or external load balancers.
  * **Non-Persistent Disk volume types** : Storage volume types other than Persistent Disk persistent volumes, such as NFS shares or Google Cloud NetApp Volumes instances. However, you can protect workloads backed by Filestore instances by using custom backup hooks; to learn more, see [Handle Filestore volumes with Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/handle-filestore-volumes).



## What's next

  * [Enable the Backup for GKE API](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/install)
  * [Enable Backup for GKE for a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/enable-gke-cluster)
  * [Create a backup plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan)
  * [Back up workloads](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup)
  * [Restore a backup](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
