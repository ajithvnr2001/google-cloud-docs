---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/raw-data-export/
title: Raw data export \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:26.758452+00:00
---

# Raw data export  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/raw-data-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Raw data export Stay organized with collections  Save and categorize content based on your preferences. 

Contact Center AI Platform (CCAI Platform) lets you export session data to a Cloud Storage bucket or an external server. With this data, you can get insights into calls, chats, emails, queues, agent performance, virtual agents, and more.

## Before you begin

To set up session data export, you must have the following:

  * A Google Cloud [service account](https://docs.cloud.google.com/iam/docs/service-account-overview) with the `Storage Object Admin` role. For more information, see [Create service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create). 
  * A JSON service account key. You use this key in [Set up external storage with Cloud Storage](https://docs.cloud.google.com/contact-center/ccai-platform/docs/external-storage#set-up-cloud-storage). For more information, see [Create a service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating). **Important:** Follow Google Cloud's [Best practices for managing service account keys.](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys)



## Export session data

To export session data, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Session Data Export** pane, and then click **Manage Data Export Settings**. The **Session Data Export** page appears.

  3. Click the **Raw Data Export** toggle to the on position.

  4. Select **Google Cloud**.

  5. In the **Bucket Name** field, enter the name of the Cloud Storage bucket where you want to export your session data.

  6. Under **Service Account Key (JSON File)** , click **Upload key** to upload your JSON service account key for authentication. For more informatoion, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts) and [Create and delete service account keys](https://docs.cloud.google.com/iam/docs/keys-create-delete).

**Note:** If you've already uploaded a service account key, you can skip this step.
  7. In the **Folder Path** field, enter the path to the subfolder where you want to store your session data, and then click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
