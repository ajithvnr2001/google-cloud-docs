---
url: https://docs.cloud.google.com/alloydb/docs/user-grant-access/
title: Grant access to other users \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:44.194227+00:00
---

# Grant access to other users  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/user-grant-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Grant access to other users Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to grant a Google Cloud user account or service account access to all AlloyDB resources in a project.

Depending on the scope of control you want the account to have, you grant it one of these predefined IAM roles:

  * `roles/alloydb.admin` (Cloud AlloyDB Admin) to grant full control for all AlloyDB resources
  * `roles/alloydb.client` (Cloud AlloyDB Client) and `roles/serviceusage.serviceUsageConsumer` (Service Usage Consumer) to grant connectivity access to AlloyDB instances from clients connecting with the AlloyDB Auth proxy
  * `roles/alloydb.databaseUser` (Cloud AlloyDB Database User) to grant database-user authentication to AlloyDB instances
  * `roles/alloydb.viewer` (Cloud AlloyDB Viewer) to grant read-only access to all AlloyDB resources



For detailed information about the specific IAM permissions these roles provide, see [Predefined AlloyDB IAM roles](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions#roles).

## Before you begin

  * The Google Cloud project you are using must have been [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#before-you-begin). 
  * You must have the `roles/owner` (Owner) basic IAM role in the Google Cloud project you are using, or a role that grants these permissions: 
    * `resourcemanager.projects.get`
    * `resourcemanager.projects.getIamPolicy`
    * `resourcemanager.projects.setIamPolicy`

To gain these permissions while following the principle of least privilege, ask your administrator to grant you the `roles/resourcemanager.projectIamAdmin` (Project IAM Admin) role.

  * Enable the Cloud Resource Manager API in the Google Cloud project you are using.

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudresourcemanager.googleapis.com)




## Procedure

### Console

  1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select the project enabled to access AlloyDB.
  3. Select a principal (user or service account) to grant access to: 
     * To grant a role to a principal who already has other roles on the project, find the row containing the principal's email address, click edit **Edit principal** in that row, and click add **Add another role**. 
     * To grant a role to a principal who does not already have other roles on the project, click person_add **Add** , then enter the principal's email address. 
  4. From the drop-down list, select one of these roles: 
     * **Cloud AlloyDB Admin**
     * **Cloud AlloyDB Viewer**
     * **Cloud AlloyDB Client** and **Service Usage Consumer**
     * **Cloud AlloyDB Database User**
  5. Click **Save**. The principal is granted the role.

**Note:** In general, the policy changes will take effect within 60 seconds. However, under certain circumstances, it can take up to 7 minutes for such changes to fully propagate across the system. 

### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the `add-iam-policy-binding` command to grant an AlloyDB predefined role to an IAM principal (user account or service account).
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member=PRINCIPAL \
        --role=ALLOYDB_ROLE
    

  * `PROJECT_ID`: The ID of the project enabled to access AlloyDB.
  * `PRINCIPAL`: The type and email ID (email address) of the principal: 
    * For user accounts: `user:EMAIL_ID`
    * For service accounts: `serviceAccount:EMAIL_ID`
  * `ALLOYDB_ROLE`: The role you want to grant the principal. The value must be one of the following: 

    * `roles/alloydb.admin`
    * `roles/alloydb.viewer`
    * `roles/alloydb.client` and `roles/serviceusage.serviceUsageConsumer`
    * `roles/alloydb.databaseUser`

For details about the permissions these roles grant, see [Predefined AlloyDB IAM roles](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions#roles).


**Note:** In general, the policy changes will take effect within 60 seconds. However, under certain circumstances, it can take up to 7 minutes for such changes to fully propagate across the system. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


