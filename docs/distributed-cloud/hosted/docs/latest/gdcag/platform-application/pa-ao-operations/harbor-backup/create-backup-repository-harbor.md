---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-backup-repository-harbor/
title: Create a backup repository \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:49:36.858948+00:00
---

# Create a backup repository  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-backup-repository-harbor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a backup repository Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of Harbor backup repositories and how to create backup repositories in Google Distributed Cloud (GDC) air-gapped.

A backup repository represents an S3-compatible storage location for your backups.

## Before you begin

To create a Harbor backup repository, you must have an S3-compatible endpoint available and a storage bucket to use as the backup repository.

### Required IAM roles

Request the necessary permissions from your Project IAM Admin. Enforce least privilege access by requesting only the roles required for your specific tasks:

  * **Secret Admin** (`secret-admin`): get, list, create, update, patch, and delete all Kubernetes secrets within the project namespace. This is a project-level permission that includes the sensitive authentication credentials needed by the backup repository.
  * **Harbor Instance Admin** (`harbor-instance-admin`): get, list, watch, create, update, patch, and delete Harbor instances, backup repositories, backup plans, backups, and restores within the project namespace.



## Create a backup repository

Create a repository in the GDC console or the API.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for harbor instance**.
  3. Click **Repositories**.
  4. Click **Create repository**.
  5. In the **Zone** menu, select the zone where the backup repository is created.
  6. In the **Repository name** field, enter a repository name.
  7. Optional: In the **Repository description** field, enter a description to distinguish this backup repository.
  8. In the **S3 URI endpoint** field, enter an endpoint containing the fully qualified domain name of your object storage site. For example, `https://storagegrid.zone.DOMAIN.SUFFIX:PORT`.
  9. In the **Bucket FQN** field, enter a fully qualified name (FQN) for the bucket.
  10. In the **Access Key ID** field, enter the access key ID for your bucket.
  11. In the **Access key** field, enter the access key for your bucket.
  12. Click **Create**.



### API
    
    
    apiVersion: artifactregistry.gdc.goog/v1
    kind: HarborInstanceBackupRepository
    metadata:
      name: BACKUP_REPO_NAME
      namespace: INSTANCE_NAMESPACE
    spec:
      secretReference:
        namespace: INSTANCE_NAMESPACE
        name: BUCKET_SECRET_NAME
      endpoint: BUCKET_ENDPOINT
      region: BUCKET_REGION
      bucket: BUCKET_NAME
      description: REPORSITORY_DESCRIPTION
    

Replace the following:

  * `BACKUP_REPO_NAME`: the name of the backup repository. The repository must be in the same namespace with the Harbor instance to backup.
  * `INSTANCE_NAMESPACE`: the namespace of the Harbor instance that is created in [Create a Harbor registry instance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/create-harbor-instances#create-a-harbor-registry-instance). The backup repository must be in the same namespace as the Harbor instance being backed up.
  * `BUCKET_SECRET_NAME`: the name of the secret that contains access credentials for the endpoint. The secret must be placed in the same namespace as the Harbor instance repository. The secret must contain the fields `access-key-id` and `access-key`. For more information on getting access to buckets, see [Grant and obtain storage bucket access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/grant-obtain-storage-access).
  * `BUCKET_ENDPOINT`: the fully qualified domain name for the storage system, such as `https://storagegrid.zone.DOMAIN.SUFFIX:PORT`.
  * `BUCKET REGION`: the region containing the bucket, such as `us-east1`. The region is storage system specific.
  * `BUCKET_NAME`: the name of the storage bucket. The bucket name is found in the status of the GDC bucket custom resource.
  * `REPORSITORY_DESCRIPTION`: a text description of the backup repository.



## What's next

  * [Create a backup plan](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/harbor-backup/create-backup-plan-harbor)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
