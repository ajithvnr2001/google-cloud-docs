---
url: https://docs.cloud.google.com/compute/docs/disks/manage-recycle-bin/
title: Manage snapshots in the recycle bin \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:48.315613+00:00
---

# Manage snapshots in the recycle bin  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/manage-recycle-bin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manage snapshots in the recycle bin Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Recycle bin for Compute Engine snapshots**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To prevent a _recoverable snapshot_ , that is, a deleted standard snapshot that's in the recycle bin, from being permanently erased, recover the snapshot from the recycle bin before its retention period expires. When you recover a snapshot, it becomes a usable standard snapshot that you can use to create a new disk.

This document describes how to list, recover, and delete recoverable snapshots.

To learn more about the recycle bin, see [Retain deleted resources in the recycle bin](https://docs.cloud.google.com/compute/docs/disks/retain-deleted-resources).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles and permissions

To get the permissions that you need to manage recoverable snapshots, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin) (`roles/compute.instanceAdmin`)
  * To connect to a VM that can run as a service account: [Service Account User (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage recoverable snapshots. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage recoverable snapshots:

  * To recover a recoverable snapshot: `compute.recoverableSnapshots.recover` on the snapshot 
  * To view information about a recoverable snapshot: `compute.recoverableSnapshots.get` on the snapshot 
  * To permanently delete a recoverable snapshot: `compute.recoverableSnapshots.delete` on the snapshot 
  * To list the recoverable snapshots in a project: `compute.recoverableSnapshots.list` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

  * **Supported resources** : Only standard snapshots are supported. Archive snapshots, instant snapshots, disks, and images are immediately permanently erased upon deletion. 
  * **Name conflicts** : Recovering a snapshot will fail if a standard snapshot that has the same name already exists and you don't provide a new name for the recovered snapshot. To recover such a snapshot, you must use the Google Cloud CLI or REST to specify a new name. 
  * **Tag persistence** : Tags that are attached to a snapshot before it is deleted are not retained if the snapshot is recovered from the recycle bin. You must [add the tags back](https://docs.cloud.google.com/compute/docs/tag-resources#adding_tags_to_a_resource) to the snapshot after you recover it from the recycle bin. 
  * **Retention policy changes** : Changes to the recycle bin retention policy don't apply to existing recoverable snapshots, that is, existing deleted standard snapshots that are in the recycle bin. 
  * **Scheduled snapshots** : If you recover a snapshot that was originally created on a schedule, then the snapshot is no longer part of the schedule and isn't automatically deleted after the duration specified by the schedule. Instead, Compute Engine retains the snapshot indefinitely until you manually delete the snapshot. 
  * **Customer-managed encryption keys (CMEKs)** : If you revoke the CMEK that protects a recoverable snapshot, and you then recover the snapshot, you can't use the recovered snapshot to create a disk until you restore the key. If you don't recover the snapshot before the retention period expires, then Compute Engine permanently erases the snapshot. 
  * **Recovery required before use** : Recoverable snapshots are read-only. To use a recoverable snapshot to create a disk, you must first recover the standard snapshot from the recycle bin. 



## List recoverable snapshots

To view the recoverable snapshots that are in a project, use the Google Cloud console, the gcloud CLI, or REST.

###  Google Cloud console 

  1. In the Google Cloud console, go to the **Snapshots** page.

[Go to the Snapshots page](https://console.cloud.google.com/compute/snapshots)

  2. Click **Recycle bin**.

  3. Click the **Deleted Snapshots** tab. The list of recoverable snapshots appears.




Each column lists details about the recoverable snapshots, including the following:

  * **Name** : the name of the recoverable snapshot.
  * **Original snapshot name** : the name of the original standard snapshot.
  * **Snapshot deletion time** : the time when the original standard snapshot was deleted.
  * **Permanent deletion time** : the time in the future when Compute Engine will permanently delete the recoverable snapshot.



###  gcloud CLI 

To list all the snapshots in a project's recycle bin, use the [`gcloud beta compute recoverable-snapshots list` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/recoverable-snapshots/list). To include additional information about each recoverable snapshot, use the `--format` flag.

For example, the following command lists each recoverable snapshot in a project and includes details about each recoverable snapshot:
    
    
    gcloud beta compute recoverable-snapshots list \
      --project=PROJECT_ID \
      --format="yaml(name, creationTimestamp, purgeTimestamp, originalResource)"
    

Replace `PROJECT_ID` with the ID of the project.

The output is a list of the recoverable snapshots in the project, similar to the following:
    
    
    creationTimestamp: '2026-09-01T11:13:50.716-07:00'
    name: data-disk-snapshot-20260805-qlb6lyqw
    purgeTimestamp: '2026-09-06T11:13:50.609-07:00'
    originalResource:
      ...
      name: data-disk-snapshot-20260805
      ...
      sourceDisk: projects/my-project/global/disks/data-disk
    ---
    creationTimestamp: '2026-09-01T12:13:50.229-07:00'
    name: disk-snapshot-20260901191347-s0c24h1m
    purgeTimestamp: '2026-09-06T12:13:50.070-07:00'
    originalResource:
      ...
      name: disk-snapshot-20260901191347
      ...
      sourceDisk: projects/my-project/global/disks/my-disk
    ---
    

The output lists the following key properties of each recoverable snapshot: 

  * `name`: the name of the recoverable snapshot. To recover the snapshot, you must specify this name if you use the gcloud CLI or REST.
  * `creationTimestamp`: the time when the original standard snapshot was deleted.
  * `purgeTimestamp`: the time in the future when Compute Engine will permanently delete the recoverable snapshot.
  * `originalResource`: an object that contains details about the original snapshot, including its name and source disk. 



###  REST 

Construct a `GET` request to the [`recoverableSnapshots list` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/recoverableSnapshots/list).
    
    
        GET https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/global/recoverableSnapshots/
    

Replace `PROJECT_ID` with the ID of the project.

The JSON response body contains a list of the recoverable snapshots in the project, similar to the following:
    
    
    {
      "kind": "compute#recoverableSnapshotList",
      "id": "projects/PROJECT_ID/global/recoverableSnapshots/",
      "items": [
        {
          "name": "prod-test-snapshot-20260905053732-uj731vz4",
          "creationTimestamp": "2026-09-05T22:37:34.164-07:00",
          "purgeTimestamp": "2026-09-12T22:37:32.918-07:00",
          ...
          "originalResource": {
            "id": "3004584137782651782",
            "creationTimestamp": "2025-10-05T22:36:41.868-07:00",
            "name": "prod-test-snapshot"
            ...
          }
        },
        {
          "kind": "compute#recoverableSnapshot",
          "id": "8914891425536994162",
          "name": "my-test-snapshot-20260906053732-uj731vz5",
          "creationTimestamp": "2026-09-05T22:37:34.164-07:00",
          "purgeTimestamp": "2026-09-12T22:37:32.918-07:00",
          ...
          "originalResource": {
            "id": "39904584137782651782",
            "creationTimestamp": "2026-08-05T22:36:41.868-07:00",
            "name": "my-test-snapshot"
            ...
          }
        }
      ]
    }
    

The output lists the following key properties of each recoverable snapshot: 

  * `name`: the name of the recoverable snapshot. To recover the snapshot, you must specify this name if you use the gcloud CLI or REST.
  * `creationTimestamp`: the time when the original standard snapshot was deleted.
  * `purgeTimestamp`: the time in the future when Compute Engine will permanently delete the recoverable snapshot.
  * `originalResource`: an object that contains details about the original snapshot, including its name and source disk. 



## Find a recoverable snapshot by the name of the original snapshot

To find a recoverable snapshot so that you can recover it, you can use the name of the original snapshot. Recoverable snapshots have a unique name that Compute Engine generates when you delete the original snapshot.

To find the name of the recoverable snapshot, list the recoverable snapshots and filter by the original snapshot name.

You can use the Google Cloud console, the gcloud CLI, or REST.

###  Google Cloud console 

  1. In the Google Cloud console, go to the **Snapshots** page.

[Go to the Snapshots page](https://console.cloud.google.com/compute/snapshots)

  2. Click **Recycle bin**.

  3. Click the **Deleted Snapshots** tab. The list of recoverable snapshots appears.

  4. In the **filter_list Filter** field, click **Enter property name or value**. Select **Original snapshot name** from the list of properties.

  5. Enter the original snapshot name in the **Value** field, and press **Enter**.




The Google Cloud console displays a list of recoverable snapshots that have an original snapshot with a name that matches the name you entered.

###  gcloud CLI 

To find a recoverable snapshot by original snapshot name, use the [`gcloud beta compute recoverable-snapshots list` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/recoverable-snapshots/list). To filter by the original snapshot name, use the `--filter` flag for the `originalResource.name` property.
    
    
    gcloud beta compute recoverable-snapshots list \
    --project=PROJECT_ID \
    --filter="originalResource.name:ORIGINAL_SNAPSHOT_NAME" \
    --format="yaml(name, creationTimestamp, purgeTimestamp)"
    

Replace the following with the corresponding values:

  * `PROJECT_ID`: the ID of the project.
  * `ORIGINAL_SNAPSHOT_NAME`: the original name of the snapshot.



The output is a list of the recoverable snapshots that have an original snapshot with a name that matches the original snapshot name you entered, similar to the following:
    
    
    creationTimestamp: '2026-09-01T11:13:50.716-07:00'
    name: disk-20260805-09550-us-central1-a-202-20260901181348-qlb6lyqw
    purgeTimestamp: '2026-09-06T11:13:50.609-07:00'
    ---
    creationTimestamp: '2026-09-01T12:13:50.229-07:00'
    name: disk-20260805-09550-us-central1-a-202-20260901191347-s0c24h1m
    purgeTimestamp: '2026-09-06T12:13:50.070-07:00'
    ---
    creationTimestamp: '2026-09-01T13:13:51.060-07:00'
    name: disk-20260805-09550-us-central1-a-202-20260901201348-ogybudsu
    purgeTimestamp: '2026-09-06T13:13:50.904-07:00'
    

To filter by the creation or deletion time of the original snapshot, extend the `--filter` expression:

  * To filter by the original snapshot's creation time, add a condition for `originalResource.creationTimestamp` to the `--filter` expression. For example, to find the recoverable snapshots for an original snapshot that was created on or after a specific time:


    
    
      --filter="**originalResource.creationTimestamp >= 'CREATION_FILTER_TIMESTAMP'** AND originalResource.name:ORIGINAL_SNAPSHOT_NAME"
    

Replace the following:

  * `ORIGINAL_SNAPSHOT_NAME`: the name of the original snapshot.
  * `CREATION_FILTER_TIMESTAMP`: the timestamp for the filter, for example, `2026-09-01T10:00:00`. The timestamp is in local time.

  * To filter by when the original snapshot was deleted, add a condition for `creationTimestamp` to the `--filter` expression. For example, to find the recoverable snapshots for a specific original snapshot that was deleted on or after a specific time:



    
    
      --filter="**creationTimestamp >= 'DELETION_FILTER_TIMESTAMP'** AND originalResource.name:ORIGINAL_SNAPSHOT_NAME"
    

Replace the following:

  * `ORIGINAL_SNAPSHOT_NAME`: the name of the original snapshot.
  * `DELETION_FILTER_TIMESTAMP`: the timestamp for the filter, for example, `2026-09-01T10:00:00`. The timestamp is in local time.



###  REST 

Construct a `GET` request to the [`recoverableSnapshots.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/recoverableSnapshots/list) using the `filter` query parameter.
    
    
    GET 'https://compute.googleapis.com/compute/beta/projects/
    PROJECT_ID/global/recoverableSnapshots?filter=originalResource.name:ORIGINAL_SNAPSHOT_NAME'
    

Replace the following with the corresponding values:

  * `PROJECT_ID`: the ID of the project.
  * `ORIGINAL_SNAPSHOT_NAME`: the original name of the snapshot.



The response body is a list of the recoverable snapshots whose original snapshot name matches the original snapshot name you entered, similar to the following:
    
    
    {
      "kind": "compute#recoverableSnapshotList",
      "id": "projects/PROJECT_ID/global/recoverableSnapshots/",
      "items": [
        {
          "kind": "compute#recoverableSnapshot",
          "id": "8914891425536994161",
          "name": "prod-test-snapshot-20261006053732-uj731vz4",
          "creationTimestamp": "2026-10-05T22:37:34.164-07:00",
          "purgeTimestamp": "2026-10-12T22:37:32.918-07:00",
          ...
          "originalResource": {
            "name": "prod-test-snapshot",
            ...
          }
        }
      ]
    }
    

Each object in the `items` array represents a recoverable snapshot and has the following properties:

  * `name`: the name of the recoverable snapshot. To recover the snapshot, you must specify this name if you use the gcloud CLI or REST.
  * `creationTimestamp`: the time when the original standard snapshot was deleted.
  * `purgeTimestamp`: the time in the future when Compute Engine will permanently delete the recoverable snapshot.
  * `originalResource`: an object that contains details about the original snapshot, including its name and source disk. 



## View information about a recoverable snapshot

To retrieve detailed information about a recoverable snapshot, such as its source snapshot or creation time, use the Google Cloud console, the gcloud CLI, or REST.

To find the name of a recoverable snapshot if you only have the original snapshot name, see Find the name of a recoverable snapshot.

###  Google Cloud console 

  1. In the Google Cloud console, go to the **Snapshots** page.

[Go to the Snapshots page](https://console.cloud.google.com/compute/snapshots)

  2. Click **Recycle bin**.

  3. On the **Deleted Snapshots** tab, view the list of recoverable snapshots.

  4. Each column lists details about a recoverable snapshot, including the following:

     * **Name** : the name of the recoverable snapshot.
     * **Original snapshot name** : the name of the original standard snapshot.
     * **Snapshot deletion time** : the time when the original standard snapshot was deleted.
     * **Permanent deletion time** : the time in the future when Compute Engine will permanently delete the recoverable snapshot.



###  gcloud CLI 

To view information about a recoverable snapshot, use the [`gcloud beta compute recoverable-snapshots describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/recoverable-snapshots/describe).
    
    
    gcloud beta compute recoverable-snapshots describe RECOVERABLE_SNAPSHOT_NAME \
    --project=PROJECT_ID
    

Replace the following with the corresponding values:

  * `RECOVERABLE_SNAPSHOT_NAME`: the name of the recoverable snapshot.
  * `PROJECT_ID`: the ID of the project.



The output is a description of the recoverable snapshot, similar to the following:
    
    
      creationTimestamp: '2026-09-01T13:13:51.626-07:00'
      id: '2573728532034916112'
      kind: compute#recoverableSnapshot
      name: prod-test-snapshot-uj731vz4
      originalResource:
          name: prod-test-snapshot
          ...
          storageBytesStatus: UP_TO_DATE
          storageLocations:
          - us
      purgeTimestamp: '2026-09-06T13:13:51.493-07:00'
      selfLink: ..
      status: READY
    

The output includes the following key properties of the recoverable snapshot: 

  * `name`: the name of the recoverable snapshot. To recover the snapshot, you must specify this name if you use the gcloud CLI or REST.
  * `creationTimestamp`: the time when the original standard snapshot was deleted.
  * `purgeTimestamp`: the time in the future when Compute Engine will permanently delete the recoverable snapshot.
  * `originalResource`: an object that contains details about the original snapshot, including its name and source disk. 



###  REST 

To view information about a recoverable snapshot, make a `GET` request to the [`recoverableSnapshots.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/recoverableSnapshots).
    
    
    GET 'https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/global/recoverableSnapshots/RECOVERABLE_SNAPSHOT_NAME'
    

Replace the following with the corresponding values:

  * `PROJECT_ID`: the ID of the project that contains the recoverable snapshot.
  * `RECOVERABLE_SNAPSHOT_NAME`: the name of the recoverable snapshot.



The response is similar to the following:
    
    
      {
        "name": "prod-test-snapshot-uj731vz4",
        "creationTimestamp": "2026-09-05T22:37:34.164-07:00",
        "purgeTimestamp": "2026-09-12T22:37:32.918-07:00",
        ...
        "originalResource": {
            "name": "prod-test-snapshot",
            ...
        }
      }
    

The response body includes the following key properties of the recoverable snapshot: 

  * `name`: the name of the recoverable snapshot. To recover the snapshot, you must specify this name if you use the gcloud CLI or REST.
  * `creationTimestamp`: the time when the original standard snapshot was deleted.
  * `purgeTimestamp`: the time in the future when Compute Engine will permanently delete the recoverable snapshot.
  * `originalResource`: an object that contains details about the original snapshot, including its name and source disk. 



## Recover deleted snapshots

Before you recover a snapshot, consider the following:

  * **Tag persistence** : Tags that are attached to a snapshot before it is deleted are not retained if the snapshot is recovered from the recycle bin. You must [add the tags back](https://docs.cloud.google.com/compute/docs/tag-resources#adding_tags_to_a_resource) to the snapshot after you recover it from the recycle bin. 
  * **Scheduled snapshots** : If you recover a snapshot that was originally created on a schedule, then the snapshot is no longer part of the schedule and isn't automatically deleted after the duration specified by the schedule. Instead, Compute Engine retains the snapshot indefinitely until you manually delete the snapshot. 
  * **Name conflicts** : Recovering a snapshot will fail if a standard snapshot that has the same name already exists and you don't provide a new name for the recovered snapshot. To recover such a snapshot, you must use the Google Cloud CLI or REST to specify a new name. 
  * **Recoverable snapshots persist after recovery** : recovering a snapshot doesn't delete the recoverable snapshot from the recycle bin. The recoverable snapshot persists in the recycle bin until the retention period expires.
  * **New creation time for the recovered snapshot** : when you recover a snapshot, the creation time for the standard snapshot is the time you recovered it from the recycle bin and not the time when the snapshot was originally created.



### Recover a snapshot from the recycle bin

To recover a deleted snapshot so that you can use it to create a new disk, you must first find the name of the recoverable snapshot. To do so, follow the instructions in Find the name of a recoverable snapshot.

When you know the name of the recoverable snapshot, use the Google Cloud console, gcloud CLI, or REST to recover the snapshot.

###  Google Cloud console 

  1. In the Google Cloud console, go to the **Snapshots** page.

[Go to the Snapshots page](https://console.cloud.google.com/compute/snapshots)

  2. Click **Recycle bin**.

  3. Click the **Deleted Snapshots** tab. The list of recoverable snapshots appears.

  4. Select the snapshot that you want to recover.

  5. Click **restore_from_trash Recover**.




###  gcloud CLI 

To recover a snapshot, use the [`gcloud beta compute recoverable-snapshots recover` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/recoverable-snapshots/recover).

  * To recover a snapshot and keep its original name:
        
        gcloud beta compute recoverable-snapshots recover \
          RECOVERABLE_SNAPSHOT_NAME \
          --project=PROJECT_ID
        

Replace the following with the corresponding values:

    * `RECOVERABLE_SNAPSHOT_NAME`: the name of the recoverable snapshot.
    * `PROJECT_ID`: the ID of the project.
  * To recover a snapshot and specify a new name for the recovered snapshot, specify the new name with the `--snapshot-name` flag.
        
        gcloud beta compute recoverable-snapshots recover \
        RECOVERABLE_SNAPSHOT_NAME \
        --project=PROJECT_ID \
        **--snapshot-name= NEW_SNAPSHOT_NAME**
        

Replace the following with the corresponding values:

    * `RECOVERABLE_SNAPSHOT_NAME`: the name of the recoverable snapshot.
    * `PROJECT_ID`: the ID of the project.
    * `NEW_SNAPSHOT_NAME`: the new name for the recovered snapshot.



###  REST 

To recover a snapshot, make a `POST` request to the [`recoverableSnapshots.recover` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/recoverableSnapshots/recover).
    
    
    POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/global/recoverableSnapshots/RECOVERABLE_SNAPSHOT_NAME/recover
    

Replace the following with the corresponding values:

  * `PROJECT_ID`: the ID of the project.
  * `RECOVERABLE_SNAPSHOT_NAME`: the name of the recoverable snapshot.



To recover a snapshot and specify a new name for the recovered snapshot, specify the new name with the `snapshotName` field in the request body:
    
    
    {
      "snapshotName": "NEW_SNAPSHOT_NAME"
    }
    

Replace `NEW_SNAPSHOT_NAME` with the new name for the recovered snapshot.

To create a disk from the recovered snapshot, see [Create a disk from a snapshot](https://docs.cloud.google.com/compute/docs/disks/restore-snapshot).

To add tags that were attached to the original standard snapshot, see [Adding tags to a resource](https://docs.cloud.google.com/compute/docs/tag-resources#adding_tags_to_a_resource).

## Delete a recoverable snapshot

You can permanently delete a snapshot from the recycle bin before its retention period expires with the Google Cloud console, gcloud CLI, or REST.

**Warning:** Deleting a recoverable snapshot is irreversible. You can't recover deleted recoverable snapshots.

###  Google Cloud console 

  1. In the Google Cloud console, go to the **Snapshots** page.

[Go to the Snapshots page](https://console.cloud.google.com/compute/snapshots)

  2. Click **Recycle bin**.

  3. In the **Deleted snapshots** tab, select the snapshot you want to permanently delete.

  4. Click **delete Delete permanently**.




###  gcloud CLI 

To permanently delete a recoverable snapshot, use the [`gcloud beta compute recoverable-snapshots delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/recoverable-snapshots/delete).
    
    
    gcloud beta compute recoverable-snapshots delete RECOVERABLE_SNAPSHOT_NAME \
      --project=PROJECT_ID
    

Replace the following with the corresponding values:

  * `RECOVERABLE_SNAPSHOT_NAME`: the name of the recoverable snapshot.
  * `PROJECT_ID`: the ID of the project.



###  REST 

To permanently delete a recoverable snapshot, make a `DELETE` request to the [`recoverableSnapshots.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/recoverableSnapshots/delete).
    
    
      DELETE https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/global/recoverableSnapshots/RECOVERABLE_SNAPSHOT_NAME
    

Replace the following with the corresponding values:

  * `PROJECT_ID`: the ID of the project.
  * `RECOVERABLE_SNAPSHOT_NAME`: the name of the recoverable snapshot.



## What's next

  * [Create a disk from a snapshot](https://docs.cloud.google.com/compute/docs/disks/restore-snapshot)
  * [Configure the recycle bin retention policy](https://docs.cloud.google.com/compute/docs/disks/configure-recycle-bin)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
