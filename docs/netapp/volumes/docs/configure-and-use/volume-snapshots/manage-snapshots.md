---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/manage-snapshots/
title: Manage your snapshots \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:26.926047+00:00
---

# Manage your snapshots  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/manage-snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Manage your snapshots Stay organized with collections  Save and categorize content based on your preferences. 

This page provides details on how to perform the following actions:

  * Make changes to existing settings

  * View snapshot details

  * Delete a snapshot




## Make changes to an existing snapshot

Use the following instructions to edit, revert, or delete a volume using the Google Cloud console or ONTAP-mode.

### Console

  1. Go to **NetApp Volumes page** in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Select **Volumes**.

  3. Click the volume's name.

  4. Click the **Snapshots** tab.

  5. Select the snapshot you want to modify. You can revert, edit, or delete the snapshot.




### ONTAP-mode

Identify the required ONTAP commands in the [ONTAP documentation](https://docs.netapp.com/us-en/ontap/).

For example, see [Volume snapshot modify](https://docs.netapp.com/us-en/ontap-cli/volume-snapshot-modify.html).

After you identify the required commands, see [ONTAP-mode](https://docs.cloud.google.com/netapp/volumes/docs/ontap/overview) for instructions about how to submit ONTAP commands to the storage pool.

## View snapshot details

Use the following instructions to see a detailed view of your snapshots using the Google Cloud console or ONTAP-mode.

### Console

  1. Go to **NetApp Volumes page** in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Select **Volumes**.

  3. Click the volume name.

  4. Use the following features to manage your volumes:

     * **Overview tab** : shows details about the volume.

     * **Snapshots tab** : the **Snapshots** tab lets you see the following details:

       * Provides the **Create snapshot** feature

       * Shows the number of snapshots in the volume out of a maximum of 255 and the amount of storage they consume

       * Lists all of the snapshots of the volume

       * Lists the name, creation date, and state of the volume

       * For the Flex Unified service level volumes, if you view details for a snapshot used to create other volumes, the **Associated clone volumes** section lists clones created from that snapshot that depend on the source volume.




### ONTAP-mode

When using the CLI proxy, run the following command:
    
    
    gcloud netapp storage-pools execute POOL_NAME "volume snapshot show -volume VOLUME_NAME"
    

Replace the following information:

  * `POOL_NAME`: the name of the storage pool.

  * VOLUME_NAME the name of your volume.




For more information, see [Volume snapshot show](https://docs.netapp.com/us-en/ontap-cli/volume-snapshot-show.html) and [ONTAP-mode](https://docs.cloud.google.com/netapp/volumes/docs/ontap/overview) for instructions about how to submit ONTAP commands to the storage pool.

Alternatively, you can use the proxy API as follows:

  1. Follow the instructions in [List all volumes of a storage pool](https://docs.cloud.google.com/netapp/volumes/docs/ontap/manage-ontap#list_all_volumes_of_a_storage_pool) to identify the volume UUID.

  2. Run the following API call:
         
         TOKEN=$(gcloud auth print-access-token)
         curl --location 'https://netapp.googleapis.com/v1/projects/PROJECT/locations/LOCATION/storagePools/POOL_NAME/ontap/api/storage/volumes/VOLUME_UUID/snapshots' \
         --header "Authorization: Bearer $TOKEN" \
         --header "Content-Type: application/json"
         

Replace the following information:

     * `PROJECT`: your project ID or number.

     * `LOCATION`: the location of the storage pool.

     * `POOL_NAME`: the name of your storage pool.

     * `VOLUME_UUID`: the universally unique identifier (UUID) of your volume.




## What's next

[Delete a snapshot](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/delete-snapshot).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
