---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/add-backup-repository/
title: Add a backup repository \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:13.885436+00:00
---

# Add a backup repository  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/add-backup-repository/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Add a backup repository Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a backup repository for cluster workloads in Google Distributed Cloud (GDC) air-gapped.

**Deprecated:** The `ClusterBackupRepository` resource is deprecated in release 1.18. We recommend using the generic `BackupRepository` resource instead. Existing `ClusterBackupRepository` resources remain supported, but you cannot create new ones. For more information on `BackupRepository`, see [Create a backup repository](/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-repository/create-backup-repository). 

A backup repository represents a compatible storage location for your backups. A backup repository is also used to store records of backups, backup plans, restore plans, and restores.

## Before you begin

To create a backup repository, you must have the following: 

  * Compatible endpoint: The fully qualified domain name of your object storage site.
  * Bucket name: The name of the [bucket](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-storage-buckets), found in the status of the GDC bucket custom resource.
  * Bucket [access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/grant-obtain-storage-access): Configured permissions for the object storage bucket.
  * Service identity: A [service account](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/service-identities) to manage API interactions. Replace the variable `SA_NAME` in these instructions with the name of the service account you use to access object storage.



### Request IAM roles

Contact your IAM Org Admin to request the following role on your project:

  * **Organization Cluster Backup Admin** (`organization-cluster-backup-admin`): create, get, list, watch and delete backup resources such as backup and restore plans in user clusters.



## Create a repository

Create a repository by using the GDC console or the API.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for Clusters**. Ensure no project is selected in the project selector.
  3. Click **Repository** > **Create Repository**.
  4. Enter a repository name. The description is optional. 
  5. In the **S3 URI endpoint** field, enter an endpoint containing the fully qualified domain name of your object storage site. For example, `https://storagegrid.zone.DOMAIN.SUFFIX:PORT`. 
  6. In the **Bucket name** field, enter the name of the fully qualified name of the bucket, found from the status of the GDC bucket custom resource.
  7. In the **Bucket region** field, enter the region where the bucket was created.
  8. In the **Access Key ID** list, enter the access key ID from the [bucket Secret](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/grant-obtain-storage-access#getting_bucket_access_credentials).
  9. In the **Access key** field, enter the access key from the [bucket Secret](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/grant-obtain-storage-access#getting_bucket_access_credentials).
  10. Click **Create**.



### API

To use the backup and restore APIs, you must configure a valid `ClusterBackupRepository` custom resource and supply the required credentials. You must also use a service identity, often referred to as a _service account_ to create repositories with the API. 

  1. Get the name of the secret that contains S3 credentials:
         
         export PROJECT_NAME=PROJECT_NAME
         export SA_NAME=SA_NAME
         kubectl get secrets --namespace $PROJECT_NAME -o json | jq -r --arg USER_NAME "${SA_NAME:?}" '.items[] | select( (.metadata.annotations."object.gdc.goog/subject"==$USER_NAME)) | .metadata.name'
         

Make sure to record the secret name returned by the command and use it as the `SECRET_NAME` value when you create your `ClusterBackupRepository` custom resource.

Replace the following:

     * `PROJECT_NAME`: the name of your project.
     * `SA_NAME`: the name of the service account used to access object storage.
  2. To get bucket details like FQDN and endpoints, extract the `fullyQualifiedName` and `zonalEndpoints` values from the output:
         
         kubectl get buckets -n PROJECT_NAME BUCKET_NAME -o yaml
         

  3. Add a `ClusterBackupRepository` custom resource to use these credentials and apply the new resource to the Management API server. Backup repositories are cluster-scoped:
         
         apiVersion: backup.gdc.goog/v1
         kind: ClusterBackupRepository
         metadata:
           name: CLUSTER_BACKUP_REPOSITORY
           namespace: PROJECT_NAME
         spec:
           secretReference:
             namespace: PROJECT_NAME
             name: SECRET_NAME
           endpoint: END_POINT
           type: "S3"
           s3Options:
             bucket: BUCKET_FQDN
             region: REGION
             forcePathStyle: FORCE_PATH_STYLE
           importPolicy: IMPORT_POLICY
         

Replace the following:

     * `CLUSTER_BACKUP_REPOSITORY`: the name of the cluster backup repository.
     * `PROJECT_NAME`: the name of your project.
     * `SA_NAME`: the name of the service account used to access object storage.
     * `SECRET_NAME`: the name of the secret returned from the `kubectl get secrets` command.
     * `ENDPOINT`: the fully qualified domain name for the storage system, for example, `https://objectstorage.google.gdch.test`. For the `type` field, only a value of `S3` is supported.
     * `BUCKET_FQDN`: the fully qualified name of the bucket.
     * `REGION`: the region where the bucket was created.
     * `FORCE_PATH_STYLE`: use the `forcePathStyle` field to force path style URLs for objects. This field must have a value of `true` or `false`.
     * `IMPORT_POLICY`: set to one of the following: 
       * `ReadWrite`: This repository can be used to schedule or create backups, backup plans, and restores.
       * `ReadOnly`: This repository can only be used to import and view backups. You can't create new backups or resources in this repository, but restores can use and reference read-only backups for restoration. There is no restriction on how often you can use a backup repository as `ReadOnly`.



## Backup repository import policies

All clusters must have at least one `ReadWrite` repository to successfully use backup and restore features. `ReadOnly` repositories are optional, have no limit, and are used to gain visibility into other cluster backups for cross-cluster restores.

`ReadOnly` repositories cannot be used as storage locations for additional backups or for backup plans within the cluster they were imported.

Importing a repository as `ReadWrite` claims the repository for that cluster, preventing other clusters from importing the same repository as `ReadWrite`. After importing a `ReadWrite` repository, all records of previous backups, backup plans, and restores in that repository are imported into the target cluster as local custom resources.

Importing a repository as `ReadOnly` does not claim the repository, it only imports the backups, backup plans, restores, and restore plans. Backup plans in read-only repositories don't schedule backups, they exist to provide visibility into what backup plans exist in the cluster you are importing from. Removing a `ReadOnly` repository cleans up any imported resources from the cluster and has no effect on the resources in the storage location as no write operations occur to object storage for read-only repositories.

When a `ReadWrite` repository is removed from the cluster:

  * All local custom resources associated with that repository, such as backups and restores, are removed from the current cluster.
  * That cluster's claim on the repository is removed, allowing the repository to be used as `ReadWrite` by another cluster. However, these resources are not removed from the storage endpoint.



## What's next

  * [Customize backup and restore for an application](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/customize-backup-restore)
  * [Plan a set of backups](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/plan-backups)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
