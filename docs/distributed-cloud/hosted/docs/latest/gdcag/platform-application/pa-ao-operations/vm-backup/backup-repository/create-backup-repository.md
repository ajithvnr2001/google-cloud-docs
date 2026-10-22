---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-repository/create-backup-repository/
title: Create a backup repository \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:11.550968+00:00
---

# Create a backup repository  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-repository/create-backup-repository/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a backup repository Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create a backup repository for virtual machines (VMs) in Google Distributed Cloud (GDC) air-gapped.

Before creating backups or snapshots, you must define at least one backup repository that can be shared among several backups or snapshots. A backup repository tells the backup system where to store or retrieve backups. Backup repositories for VMs are restricted to the Management API server.

This document is for developers in platform administrator or application operator groups that manage VM Backup and restore operations. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

Before you create a backup repository, you must provision the underlying storage with the following:

  * [An object storage bucket](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-storage-buckets) and an S3-compatible endpoint.
  * [A service account with granted access to the bucket, and its S3 credentials](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/grant-obtain-storage-access).



### Request IAM roles

To create VM backup repositories, ask your IAM Org Admin to grant you the following roles:

  * **Organization Backup Admin** (`organization-backup-admin`): creates, gets, lists, watches, updates, patches, and deletes VM backup repositories, VM backup plan templates, VM backup requests, and VM restore requests.

  * **Secret Viewer** (`secret-viewer`): gets, lists, and watches Kubernetes secrets in projects. 




## Create a backup repository

Create a repository using the GDC console or the API.

### Console

  1. Sign into the GDC console.
  2. In the navigation menu, click **Backup for Virtual Machines > Repositories**.
  3. Click **Create repository**.
  4. Enter a repository name and an optional description. 
  5. In the **S3 URI endpoint** field, enter an endpoint with the fully-qualified domain name of your object storage site. 
  6. In the **Bucket name** field, enter the name of the bucket.
  7. In the **Bucket region** field, enter the region where the bucket was created.
  8. In the **Access Key ID** list, enter the access key ID.
  9. In the **Access key** field, enter the access key.
  10. Click **Create**.



### API

Create a `BackupRepository` custom resource using your credentials. 

  1. Get the name of the secret that contains S3 credentials:
         
         export PROJECT_NAME=PROJECT_NAME
         export SA_NAME=SA_NAME
         kubectl get secrets --namespace $PROJECT_NAME -o json | jq -r --arg USER_NAME "${SA_NAME:?}" '.items[] | select( (.metadata.annotations."object.gdc.goog/subject"==$USER_NAME)) | .metadata.name'
         

Make sure you record the secret name returned by the command and use it as the `SECRET_NAME` value when creating your `BackupRepository` resource.

Replace the following:

     * `PROJECT_NAME`: the name of your project.
     * `SA_NAME`: the name of the service account used to access object storage.
  2. To get bucket details like FQDN and endpoints, extract the `fullyQualifiedName` and `zonalEndpoints` values from the output:
         
         kubectl get buckets -n PROJECT_NAME BUCKET_NAME -o yaml
         

  3. Create a `BackupRepository` within the Management API server:
         
         apiVersion: backup.gdc.goog/v1
         kind: BackupRepository
         metadata:
           name: REPOSITORY_NAME
         spec:
           secretReference:
             namespace: PROJECT_NAME
             name: SECRET_NAME
           endpoint: ENDPOINT
           type: "S3"
           s3Options:
             bucket: BUCKET_FQDN
             region: REGION
             forcePathStyle: FORCE_PATH_STYLE
           importPolicy: IMPORT_POLICY
         

Replace the following:

     * `REPOSITORY_NAME`: the name of the backup repository.
     * `PROJECT_NAME`: the name of your project.
     * `SA_NAME`: the name of the service account used to access object storage.
     * `SECRET_NAME`: the name of the secret returned from the `kubectl get secrets` command.
     * `ENDPOINT`: the fully qualified domain name for the storage system, for example, `https://objectstorage.google.gdch.test`. For the `type` field, only a value of `S3` is supported.
     * `BUCKET_FQDN`: the fully qualified name of the bucket.
     * `REGION`: the region where the bucket was created.
     * `FORCE_PATH_STYLE`: use the `forcePathStyle` field to force path style URLs for objects. This field must have a value of `true` or `false`.
     * `IMPORT_POLICY`: set to one of the following: 
       * `ReadWrite`: This repository can be used to schedule or create backups, backup plans, and restores.
       * `ReadOnly`: This repository can only be used to import and view backups. No new backups or resources can be created in this repository, but restores can use and reference read-only backups for restoration. There is no restriction on how often a backup repository can be used as ReadOnly.

The `BackupRepository` creates a read-write enabled `BackupRepository` resource in the Management API server that has the same name.




## What's next

  * [Manage a backup repository](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/vm-backup/backup-repository/manage-backup-repository)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
