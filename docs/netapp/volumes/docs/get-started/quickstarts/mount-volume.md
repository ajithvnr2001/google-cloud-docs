---
url: https://docs.cloud.google.com/netapp/volumes/docs/get-started/quickstarts/mount-volume/
title: Mount a volume quickstart \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:40.464116+00:00
---

# Mount a volume quickstart  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/get-started/quickstarts/mount-volume/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Mount a volume quickstart Stay organized with collections  Save and categorize content based on your preferences. 

This page provides quickstart instructions for how to mount the volume on a client.

## Mount your volume on a client

After you create a volume, you can create a Linux Compute Engine VM and mount the volume.

  1. Go to the NetApp Volumes page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes**.

  3. Identify the volume you want to mount.

  4. Click the more_vert **More options icon**.

  5. Click **Mount instructions**.

  6. Open an `ssh` client and connect to your instance. Install the NFS client on your instance. Based on your instance type, run one of the following commands:

### Red Hat
         
         sudo yum install -y nfs-utils

### SuSE
         
         sudo yum install -y nfs-utils

### Ubuntu
         
         sudo apt-get install nfs-common

### Debian
         
         sudo apt-get install nfs-common

  7. Create a new directory on your instance.

  8. Mount your volume.




## Clean up

Use the following instructions to delete your Google Cloud project.

### Before you begin

When you delete a project, the following actions take place:

  * **All contents in the project are deleted.** If you used an existing project to get started using NetApp Volumes, you delete any other work completed in the project.

  * **Custom project IDs are lost.** When you created the project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project.




### Delete the Google Cloud project

Use the following instructions to delete a Google Cloud project:

  1. Go to **Manage resources** in the Google Cloud console.

  2. In the project list, select the project that you want to delete and then click **Delete**.

  3. In the dialog, enter the **project ID** and then click **Shut down** to delete the project.




## What's next

Review [customer-managed encryption key policies](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/cmek-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
