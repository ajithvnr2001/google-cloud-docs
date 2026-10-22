---
url: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/reverse-and-resume-replication/
title: Reverse and resume a replication \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:15.084447+00:00
---

# Reverse and resume a replication  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/reverse-and-resume-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Reverse and resume a replication Stay organized with collections  Save and categorize content based on your preferences. 

This page provides details about how to reverse and resume a replication.

## About the reverse and resume operation

When you reverse and resume a replication, it switches the source and destination roles of your volumes; the destination volume becomes the new source volume and the source volume becomes the new destination volume. This operation is immediately followed by a resume operation, which overwrites the contents of the new destination volume with the contents of the new source volume. If you reverse and resume a replication twice, the original replication direction re-establishes.

## Reverse and resume operation use case

After you stop replication and make changes to the destination volume, you can replicate those changes back to the source volume. This process is common in a disaster recovery scenario in which you operate on the destination volume for a period of time and want to switch roles of the volumes.

## Considerations

Consider the following before you use reverse and resume operation:

  * If you use reverse and resume operations incorrectly, you might experience unintended data loss. Make sure that you know the current and future roles of your source and destination volumes because changes on the new destination volume are overwritten with the new source volume.

  * While you can use a destination volume to take manual backups, the service doesn't support the scheduled backups from a destination volume. Before you reverse a volume replication, make sure to remove any backup policy from the volume that becomes new destination volume.

  * If you plan to continuously operate with reversed replication direction, it's recommended to set up a backup for the new source volume. If you intend to revert replication back to the original source and switch directions again, make sure to enable scheduled backups on the source volume after completion.




## Reverse and resume a replication

Use the following instructions to reverse and resume a replication using the Google Cloud console or Google Cloud CLI:

### Console

  1. Go to **NetApp Volumes page** in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes**.

  3. Click the name of the volume. The **Details page** for the volume appears.

  4. Select the **Replication tab**.

  5. Ensure that the replication status is set to **Stopped**.

  6. Click **Reverse and resume replication**.

  7. In the **Reverse volume replication and resume dialog** , enter the **new destination volume** that you want to overwrite to confirm the reverse and resume action.

  8. Click **Reverse and resume** to initiate the operation.

In the overview of the volume, note that the role, either source or destination, changes and names of source and destination volume change as well. An incremental transfer operation to update the new destination volume triggers immediately after you initiate the reverse and resume operation.




### gcloud

Run the following command to reverse and resume a volume replication:
    
    
      gcloud netapp volumes replications reverse \
       --project=PROJECT_ID \
       --location=LOCATION \
       --volume=VOLUME \

Replace the following information:

  * `PROJECT_ID`: the name of the project your volume is in.

  * `LOCATION`: the location of the source or destination volume.

  * `VOLUME`: the name of the source or destination volume.




For more options, see [Google Cloud SDK documentation on volume replication](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/replications).

## What's next

[Integrate Active Directory](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
