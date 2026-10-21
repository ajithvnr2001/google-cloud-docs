---
url: https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/workflow/
title: Set up access to NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:20:17.587688+00:00
---

# Set up access to NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/workflow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Set up access to NetApp Volumes Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the steps you need to complete to set up and configure access for Google Cloud NetApp Volumes.

## Before you begin

NetApp Volumes supports both NFS and SMB protocols.

If you are only testing out NetApp Volumes and don't plan to keep the resources that you create, we recommend that you create a new project instead of selecting an existing project. When you're done testing, you can delete the project, which removes all resources associated with the project.

## Configuration steps

You must complete the following steps to successfully set up NetApp Volumes:

  1. In the Google Cloud console, [select or create a Google Cloud project](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/initiate-console-settings#select-or-create-a-gcp-project).

  2. [Enable billing](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled) on the project.

  3. Enable the [NetApp Volumes API](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/initiate-console-settings#enable-netapp-volumes-api).

  4. Sign up to [receive announcements](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/initiate-console-settings#sign_up_to_receive_maintenance_announcements) for application updates.

  5. Configure Google Cloud tools:

     * Set up the [Google Cloud console](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/tools#set-up-gcp-in-the-console).

     * Install the [Google Cloud CLI](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/tools#install-the-gcloud-cli).

  6. [Configure the network](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/networking).

  7. [Set up IAM permissions](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/iam).

  8. If a customer-managed encryption key is required, create a [CMEK policy](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/cmek/create-cmek-policy).

  9. Create a [storage pool](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/create-storage-pool).

  10. If an Active Directory is required, create an [Active Directory policy](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/create-ad-policy). To check the requirements for an Active Directory, see [use cases](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad#use_cases_for_active_directory). For Standard, Premium, and Extreme service levels: after creating the policy, use the [test Active Directory policy connection](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/test-ad-policy-connection) workflow to attach the policy to the storage pool and test connectivity.

  11. [Create a volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/create-volume).

  12. [Connect your clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-smb-clients) to the volume.

  13. Optional: Monitor your [volume usage](https://docs.cloud.google.com/netapp/volumes/docs/monitor/monitor-volume-usage).

  14. Optional: [Protect your data](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/protect-your-data).




## What's next

[Configure your Google Cloud project and enable Google Cloud components](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/initiate-console-settings)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
