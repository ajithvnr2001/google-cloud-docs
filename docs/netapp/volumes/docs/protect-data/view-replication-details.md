---
url: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/view-replication-details/
title: View replication details \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:00:04.859692+00:00
---

# View replication details  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/view-replication-details/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)



Send feedback 

#  View replication details Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for how to view your replication details.

## View replication details

Use the following instructions to view replication details of the source or destination volume using either the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to **NetApp Volumes page** in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes**.

  3. Click the name of the source or destination volume.

  4. Select the **Replication tab**.

If the volume is part of a replication, details of the replication appear.

The status of the volume replication appears in the **Replication status** and **Transfer status** fields:

Transfer status | Overall state  
---|---  
Preparing | The volume replication is created and the initial replication operation begins and is in progress.   
  
The amount of transferred data displays in Google Cloud console. Status updates occur in five minute increments.  
Mirrored | The volume replication is created and the volume replication operation is completed.  
Transferring | The volume replication is created and an incremental replication operation is in progress. The amount of transferred data displays in Google Cloud console. Status updates are provided in five-minute increments.  
Stopped | The volume replication is stopped by the user, which allows the destination volume to become writeable.   
  
The size of the destination volume is set independent of the source volume. This state is required if you want to permanently delete a volume replication relationship.  



### gcloud

View the details of a replication using the following command:
    
    
       gcloud netapp volumes replications list VOLUME_NAME \
          --location=LOCATION

Replace the following information:

  * `VOLUME_NAME`: the name of the source or destination volume.

  * `LOCATION`: the location in which to list volume replications.




For more options, see [Google Cloud SDK documentation on volume replication](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications).

## What's next

[Edit or stop replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/edit-or-stop-replication).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
