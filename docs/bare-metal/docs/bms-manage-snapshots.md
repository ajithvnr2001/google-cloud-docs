---
url: https://docs.cloud.google.com/bare-metal/docs/bms-manage-snapshots/
title: Manage boot volume snapshots \u00a0|\u00a0 Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:53:38.732157+00:00
---

# Manage boot volume snapshots  |  Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/bms-manage-snapshots/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage boot volume snapshots

You can create, delete, view, and restore a boot volume snapshot.

## View boot volume snapshot details

You can view the list of snapshots of a boot volume and their details, including the following:

  * ID
  * Name
  * Description
  * Create time
  * Associated volume
  * Type




###  Console 

  1. Go to the [**Compute Engine** > **Bare Metal Solution** > **Volumes**](https://console.cloud.google.com/compute/bareMetalSolution/volumes) page.
  2. Click the volume name.
  3. On the **Volume details** page, in the **Snapshots** section, you can view the list of snapshots and their details.



###  gcloud 

To list all the snapshots for a boot volume, issue the `gcloud bms volumes snapshots list` command.
    
    
    gcloud bms volumes snapshots list --project=PROJECT_ID --region=REGION --volume=VOLUME_NAME
    

To view details of a specific boot volume snapshot, issue the `gcloud bms volumes snapshots describe` command.
    
    
    gcloud bms volumes snapshots describe --project=PROJECT_ID --region=REGION --volume=VOLUME_NAME --snapshot=SNAPSHOT_NAME
    

###  API 

To list all boot volume snapshots, enter your project ID, region, and volume name into the following `curl` command. Copy the command, paste it into the Cloud Shell prompt, and press the **Enter** or **Return** key.
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "X-Goog-User-Project: PROJECT_ID" \
    -H "Content-Type: application/json" \
    "https://baremetalsolution.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/volumes/VOLUME_NAME/snapshots"
    

To view details of a boot volume snapshot, enter your project ID, region, volume name, and snapshot name into the following `curl` command. Copy the command, paste it into the Cloud Shell prompt, and press the **Enter** or **Return** key.
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "X-Goog-User-Project: PROJECT_ID" \
    -H "Content-Type: application/json" \
    "https://baremetalsolution.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/volumes/VOLUME_NAME/snapshots/SNAPSHOT_NAME"
    

## Create a boot volume snapshot

You can create snapshots for boot volumes.

###  Console 

  1. Go to the [**Compute Engine** > **Bare Metal Solution** > **Volumes**](https://console.cloud.google.com/compute/bareMetalSolution/volumes) page.
  2. Click the volume name.
  3. On the **Volume details** page, in the **Snapshots** section, click **Create**.
  4. On the **Create a new volume snapshot** page: 
     1. In the **Name** field, enter a unique name for the snapshot.
     2. In the **Description** field, enter a description for the snapshot.
  5. Click **Create**.



###  gcloud 

To create a boot volume snapshot, issue the `gcloud bms volumes snapshot` command.
    
    
    gcloud bms volumes snapshot --project=PROJECT_ID --region=REGION --volume=VOLUME_NAME --snapshot=SNAPSHOT_NAME --description=DESCRIPTION
    

###  API 

To create a boot volume snapshot, enter your project ID, region, volume name, snapshot name, and snapshot description into the following `curl` command. Copy the command, paste it into the Cloud Shell prompt, and press the **Enter** or **Return** key.
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "X-Goog-User-Project: PROJECT_ID" \
    -H "Content-Type: application/json" \
    "https://baremetalsolution.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/volumes/VOLUME_NAME/snapshots"
     -d \
    '{\''name\'':
    \''projects/PROJECT_ID/locations/REGION/volumes/VOLUME_NAME/snapshots/SNAPSHOT_NAME\'', \''description\'': \''DESCRIPTION\''}' \
    

## Delete a boot volume snapshot

You can delete boot volume snapshots.

**Note:** Because you might need to restore the boot volume from a snapshot taken on a specific day for recovery purposes, we do not recommend deleting scheduled daily snapshots.

###  Console 

  1. Go to the [**Compute Engine** > **Bare Metal Solution** > **Volumes**](https://console.cloud.google.com/compute/bareMetalSolution/volumes) page.
  2. Click the volume name.
  3. On the **Volume details** page, in the **Snapshots** section, select the snapshot that you want to delete.
  4. Click **Delete**.
  5. When prompted, click **Confirm**.



###  gcloud 

To delete a boot volume snapshot, issue the `gcloud bms volumes snapshots delete` command.
    
    
    gcloud bms volumes snapshots delete --project=PROJECT_ID --region=REGION --volume=VOLUME_NAME --snapshot=SNAPSHOT_NAME
    

When prompted, type "Y" and press the **Enter** or **Return** key.

###  API 

To delete a boot volume snapshot, enter your project ID, region, volume name, and snapshot name into the following `curl` command. Copy the command, paste it into the Cloud Shell prompt, and press the **Enter** or **Return** key.
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "X-Goog-User-Project: PROJECT_ID" \
    -H "Content-Type: application/json" \
    "https://baremetalsolution.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/volumes/VOLUME_NAME/snapshots/SNAPSHOT_NAME"
    

## Restore a boot volume snapshot

You can restore a boot volume from a snapshot.

**Caution:** Restoring a volume from a snapshot will delete all the snapshots created after it. 

###  Console 

  1. Go to the [**Compute Engine** > **Bare Metal Solution** > **Servers**](https://console.cloud.google.com/compute/bareMetalSolution/servers) page.
  2. Stop the server attached to the volume that you want to restore. See [Operate your Bare Metal Solution server](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#restart_a_bare_metal_solution_server).

Wait for the shutdown to complete before moving to the next step.

  3. Go to the [**Compute Engine** > **Bare Metal Solution** > **Volumes**](https://console.cloud.google.com/compute/bareMetalSolution/volumes) page.

  4. For the volume that you want to restore, click the volume name.

  5. On the **Volume details** page:

     1. For the snapshot that you want to restore, click more_vert.
     2. Click **Restore**.
     3. When prompted, click **Confirm**.



###  gcloud 

To restore a boot volume snapshot, issue the `gcloud bms volumes restore` command.
    
    
    gcloud bms volumes restore --project=PROJECT_ID --region=REGION VOLUME_NAME --snapshot=SNAPSHOT_NAME
    

###  API 

To restore a boot volume snapshot, enter your project ID, region, volume name, and snapshot name into the following `curl` command. Copy the command, paste it into the Cloud Shell prompt, and press the **Enter** or **Return** key.
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "X-Goog-User-Project: PROJECT_ID" \
    -H "Content-Type: application/json" \
    -H "Content-Length:0" \
    "https://baremetalsolution.googleapis.com/v2/projects/PROJECT_ID/locations/REGION/volumes/VOLUME_NAME/snapshots/SNAPSHOT_NAME:restoreVolumeSnapshot"
    

Because restoring a boot volume takes a while to complete, you can check the status by following the steps in [View the status of a long-running operation](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance#view_the_status_of_a_long-running_operation).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
