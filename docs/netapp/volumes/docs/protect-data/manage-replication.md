---
url: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/manage-replication/
title: Manage volume replication \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:53.881213+00:00
---

# Manage volume replication  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/manage-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Manage volume replication Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage a [volume replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-replication#about_volume_replication).

## View replication details

The following table describes the different states in a volume replication:

Transfer status (mirrorState) | Overall state  
---|---  
Preparing | The volume replication is created and the initial replication operation begins and is in progress.   
  
The amount of transferred data displays in Google Cloud console. Status updates occur in five minute increments.  
Mirrored | The volume replication is created and the volume replication operation is completed.  
Transferring | The volume replication is created and an incremental replication operation is in progress. The amount of transferred data displays in Google Cloud console. Status updates are provided in five-minute increments.  
Stopped | The volume replication was stopped by the user, which allows the destination volume to become writeable.   
  
The size of the destination volume is set independent of the source volume. This state is required if you want to permanently delete a volume replication relationship.  
  
Use the following instructions to view replication details of the source or destination volume using either the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to **NetApp Volumes page** in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes**.

  3. Click the name of the source or destination volume.

  4. Select the **Replication tab**.

If the volume is part of a replication, details of the replication appear.




Google Cloud console displays the names of the source and destination volumes. The partner volume's name appears as a clickable link which directs you to its volume details page. For cross-project replication, the link to the partner volume doesn't work. You need to navigate to the partner volume manually.

### gcloud

View the details of a replication using the following command:
    
    
       gcloud netapp volumes replications list \
          --project=PROJECT_ID \
          --location=LOCATION \
          --volume=VOLUME_NAME

Replace the following information:

  * `PROJECT_ID`: the name of the project your volume is in.

  * `LOCATION`: the location of the source or destination volume.

  * `VOLUME_NAME`: the name of the source or destination volume.




For more options, see [Google Cloud SDK documentation on volume replication](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications).

## Edit a volume replication

You can change the replication schedule of the source volume in a replication relationship.

Use the following instructions to edit replication details in the Google Cloud console:

  1. Go to **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes**.

  3. Click the source volume. The **Details page** appears.

  4. Select the **Replication tab**.

  5. Select **Edit replication**.

  6. In the **Edit replication** dialog, update the **replication schedule** field.

  7. Click **Save**.




## Delete a volume replication

When you delete a replication, it removes the replication relationship between the source and destination volume. After the replication deletes, both volumes continue to exist independently with the current data they contain.

### Considerations

When you delete a replication, NetApp Volumes also deletes the common replication snapshots of source and destination volume. You can't resume a replication relationship for the two volumes again but you can create a new replication with either of them. When you create a new replication, it creates a new destination volume as part of the process.

### Delete a replication

Use the following instructions to delete a replication using the Google Cloud console:

  1. Go to **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes**.

  3. Click the name of the volume you want to delete.

The **Details** page appears.

  4. Select the **Replication** tab.

  5. Make sure that the **Replication status** is set to **Stopped**. For instructions about how to stop a replication, see [Stop a replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/stop-or-resume-replication#stop_a_replication).

  6. Click **Delete volume replication**.

  7. In the **Delete volume replication** dialog, enter the name of the destination volume.

  8. Click **Delete**.




## What's next

[Stop or resume a replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/stop-or-resume-replication).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
