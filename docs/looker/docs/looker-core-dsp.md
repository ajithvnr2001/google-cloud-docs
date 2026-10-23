---
url: https://docs.cloud.google.com/looker/docs/looker-core-dsp/
title: Accept complimentary Data Studio Pro licenses for a Looker (Google Cloud core) instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:27.233794+00:00
---

# Accept complimentary Data Studio Pro licenses for a Looker (Google Cloud core) instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-dsp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Accept complimentary Data Studio Pro licenses for a Looker (Google Cloud core) instance Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Complimentary Data Studio Pro licenses are also available for Looker (original) instances. For instructions about accepting complimentary Data Studio Pro licenses for a Looker (original) instance, see [Admin settings - Data Studio Pro](https://docs.cloud.google.com/looker/docs/admin-panel-platform-lsp).**Important:** Complimentary Data Studio Pro licenses are not available for Looker (Google Cloud core) instances that are created after **August 1, 2026**.

As a Looker customer, you can get complimentary Data Studio Pro licenses as part of your Looker agreement. To start using Data Studio Pro, you must set up a subscription, accept the complimentary licenses, and assign them to users.

Your Looker agreement determines the number of complimentary Data Studio Pro licenses that are allocated to your Looker account. For more information about the terms of this offer, see [Complimentary Data Studio Pro licenses offer details](https://docs.cloud.google.com/looker/docs/studio/complimentary-looker-studio-pro-licenses-offer-details).

This document describes how to perform the following tasks for a Looker instance:

  1. Accept the complimentary Data Studio Pro licenses
  2. Select a Google Cloud project to host your subscription
  3. Add users to your Data Studio Pro subscription
  4. Transfer the complimentary licenses to a different subscription



## Before you begin

**Important:** A Looker account is associated with a Data Studio Pro subscription through the Google Cloud project that hosts Data Studio Pro content. We recommend that you devote a specific Google Cloud project to hosting just Data Studio Pro content and that you indicate this project when you are accepting your complimentary licenses.

If you don't already have a Data Studio Pro subscription, we recommend that you [set up the Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) for your Data Studio content _before_ you accept your account's allotted complimentary licenses. For more information about Google Cloud project requirements and setting a new Data Studio Pro subscription, see the [Start a new Pro subscription](https://docs.cloud.google.com/looker/docs/studio/start-a-new-pro-subscription) documentation page.

Each user with a [Looker Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.viewer) (`roles/looker.viewer`) role who uses Data Studio Pro must also be a Google Workspace or Cloud Identity user with a [Managed Google account](https://support.google.com/work/android/answer/6371476).

You can associate each Looker (Google Cloud core) instance with only one Data Studio Pro subscription.

### Required roles

You need different permissions to perform the following tasks:

  * Accept complimentary Data Studio Pro licenses
  * Set up a self-service subscription to Data Studio Pro



To get the permission to accept complimentary Data Studio Pro licenses and update Looker (Google Cloud core) instance information, ask your administrator to grant you an IAM role containing the `looker.instances.update` permission for the Google Cloud project that your Looker (Google Cloud core) instance resides in. The [Looker Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`) IAM role contains this permission by default, but you can get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles). To get the permission to set up a self-service subscription to Data Studio Pro, ask your administrator to grant you an IAM role containing the `lookerstudio.pro.manage` permission for the Google Cloud project that your Looker (Google Cloud core) instance resides in. The [Looker Studio Pro Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.proManager) (`roles/lookerstudio.proManager`) and [Owner](https://docs.cloud.google.com/iam/docs/understanding-roles#owner) (`roles/owner`) IAM roles contain this permission by default, but you can get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

## Accept Data Studio Pro licenses

By default, Looker (Google Cloud core) instances include 50 complimentary Data Studio Pro licenses.

To accept these licenses, follow these steps in the Google Cloud console or the Google Cloud CLI:

### console

  1. Navigate to the [**Instances**](https://docs.cloud.google.com/looker/docs/looker-core-view-console#the_instances_page) page for the Google Cloud project in which your Looker (Google Cloud core) instance resides.
  2. Select the name of the Looker (Google Cloud core) instance that you want to use with Data Studio Pro.
  3. Select the **Data Studio Pro** tab. This tab is not visible if your Looker (Google Cloud core) instance was created after August 1, 2026.
  4. Select **Accept Data Studio Pro licenses**.



### gcloud

With the Google Cloud CLI, you accept complimentary Data Studio Pro licenses and link your Data Studio Pro Google Cloud project in a single step using the `--linked-lsp-project-number` flag. Proceed to Select a Google Cloud project and follow the **gcloud** instructions.

By accepting these complimentary licenses, you agree to the [Google Cloud Terms of Service](https://cloud.google.com/terms). Use of Data Studio Pro (even when it's connected to Looker) is subject to the agreement under which you use Google Cloud, not your Looker agreement.

## Select a Google Cloud project

After you accept the complimentary Data Studio Pro licenses, you must associate your Looker (Google Cloud core) instance with the Google Cloud project that your Data Studio Pro subscription uses. You can specify your Data Studio Pro Google Cloud project by using the Google Cloud console or the Google Cloud CLI:

### console

Follow these steps in the [**Data Studio Pro** tab](https://docs.cloud.google.com/looker/docs/looker-core-view-console#tabs) of your Looker (Google Cloud core) instance settings:

  1. Click **Select project**.
  2. In the **Select a resource** dialog, select your project from the list, and click **Select project**.
  3. In the **Data Studio Pro** tab of your Looker (Google Cloud core) instance settings, click **Save**.



The **Project name** field now displays the selected Google Cloud project ID.

### gcloud

  1. Get the project number of the Google Cloud project that hosts your Data Studio Pro subscription:
         
         gcloud projects describe DSP_PROJECT_ID \
             --format="value(projectNumber)"
         

Replace `DSP_PROJECT_ID` with the project ID of the Google Cloud project that hosts your Data Studio Pro subscription. This project must belong to the same Google Cloud organization as your Looker (Google Cloud core) instance.

  2. Accept the complimentary licenses and link the Data Studio Pro project to your Looker (Google Cloud core) instance:
         
         gcloud looker instances update INSTANCE_NAME \
             --project=PROJECT_ID \
             --region=REGION \
             --linked-lsp-project-number=DSP_PROJECT_NUMBER
         

Replace the following:

     * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
     * `PROJECT_ID`: the project ID of the Google Cloud project that hosts your Looker (Google Cloud core) instance.
     * `REGION`: the region where your Looker (Google Cloud core) instance is located.
     * `DSP_PROJECT_NUMBER`: the project number of your Data Studio Pro Google Cloud project.
  3. Verify that your Looker (Google Cloud core) instance is linked to the Data Studio Pro project:
         
         gcloud looker instances describe INSTANCE_NAME \
             --project=PROJECT_ID \
             --region=REGION \
             --format="value(linkedLspProjectNumber)"
         




**Caution:** Once you have saved your project, note the following effects: 

  * Just changing the project number won't transfer your complimentary licenses to another project. Instead, you must transfer your licenses in your Data Studio Pro subscription settings.
  * If you no longer want to link your Looker (Google Cloud core) instance to your Data Studio Pro project, see Unlink complimentary Data Studio Pro licenses from your instance.



## Add users to your Data Studio Pro subscription

To finish setting up your new Data Studio Pro subscription, add users to your subscription and assign their licenses. You can complete these steps in either the Google Cloud console or Data Studio. If you had already completed the setup for your Data Studio Pro subscription before you accepted your complimentary licenses, your licenses have been applied automatically to your existing Data Studio Pro users.

### Console

To finish setting up your new Data Studio Pro subscription in the Google Cloud console, follow these steps:

  1. Open the Data Studio Pro homepage within the Google Cloud console by either clicking **Add users** on the **Data Studio Pro** page or tab for your Looker instance, or navigating directly to the **Data Studio** page in the Google Cloud console for your linked Google Cloud project.
  2. Click **Subscribe** to open the **Buy Data Studio Pro licenses** panel:

![The Buy Data Studio Pro licenses panel.](https://docs.cloud.google.com/static/looker/docs/images/lsp-licenses-looker.png)
     * The **Current no-cost Pro licenses** line item displays the number of complimentary Data Studio Pro licenses that have been allocated to your Looker (Google Cloud core) instance.
  3. In the **Add users / groups** field, add the email addresses of users or groups to your subscription. 
     * The **Total licenses** field displays the total number of licenses that are required to support the number of users that you have added.
     * Select **Auto-assign licenses to new users added to a group** to assign available licenses to users who are added to Google Groups under the Data Studio subscription.
  4. Click **Buy**.

**Note:** If the number of users that you have added exceeds the number of complimentary Data Studio Pro licenses that are allocated to your Looker instance, the **Total monthly cost** line item displays the cost of the additional licenses that you are purchasing. 

### Data Studio

To finish setting up your new Data Studio Pro subscription in Data Studio, follow these steps:

  1. Open [Data Studio](https://datastudio.google.com/) (or click **add users in Data Studio Pro** on the **Data Studio Pro** page or tab for your Looker instance).
  2. Add users to your subscription by following the steps described on the [Add people to the subscription](https://docs.cloud.google.com/data-studio/step-2-add-people-to-the-subscription) documentation page.



### Remove licenses or users

Each Data Studio Pro user requires a Data Studio Pro license. If you need to decrease the number of licenses that are used with your Data Studio Pro subscription, you will also need to remove the corresponding number of users.

To remove licenses and users from your Data Studio Pro subscription in the Google Cloud console, follow these steps:

  1. In the Google Cloud project that hosts your Data Studio Pro subscription content, navigate to the **Data Studio** page.
  2. Select **Manage access**.
  3. Select the user or group that you want to remove from the subscription.
  4. Select delete **Delete**. In the resulting dialog, select **Delete** again.
  5. Close the **Manage access** window.
  6. Select **Add / remove licenses**.
  7. Next to the **Total licenses** field, select remove **Decrement license count** to decrease the number of licenses under the Data Studio Pro subscription.
  8. Select **Confirm**.



For more information, see [Remove users from a Pro subscription](https://docs.cloud.google.com/looker/docs/studio/edit-a-looker-studio-pro-subscription#remove_users_or_groups_from_the_subscription).

## Transfer complimentary Data Studio Pro licenses to a different subscription

After you have saved the project that you selected for your Data Studio Pro licenses in your Looker instance, we strongly recommend that you don't modify the project selection. Your complimentary licenses must be associated with the same Google Cloud project as your Data Studio Pro subscription. If you need to transfer your licenses from one Data Studio Pro subscription to another, follow these steps:

  1. [Set up a new Data Studio Pro subscription](https://docs.cloud.google.com/looker/docs/studio/start-a-new-pro-subscription) based on a different project.
  2. [Add users to your new subscription](https://docs.cloud.google.com/looker/docs/studio/step-2-add-people-to-the-subscription).
  3. [Transfer ownership](https://docs.cloud.google.com/looker/docs/studio/transfer-ownership) for any "ownerless" content that resides in team workspaces that are associated with the old subscription.
  4. [Cancel the old subscription](https://docs.cloud.google.com/looker/docs/studio/cancel-a-looker-studio-pro-subscription).



Next, to associate your complimentary Data Studio Pro licenses with the new Data Studio Pro subscription, follow these steps:

### console

  1. Navigate to the **Data Studio Pro** tab of your Looker (Google Cloud core) instance settings.
  2. Click **Select project**.
  3. In the **Select a resource** dialog, choose your new selection from the list, and click **Select project**.
  4. Select a Google Cloud project that is associated with the new Data Studio Pro subscription.
  5. In the **Data Studio Pro** tab of your Looker (Google Cloud core) instance settings, click **Save**.



The **Project name** field now displays the Google Cloud project ID that is associated with the new Data Studio Pro subscription.

### gcloud

  1. Get the project number of the Google Cloud project that is associated with the new Data Studio Pro subscription:
         
         gcloud projects describe NEW_DSP_PROJECT_ID \
             --format="value(projectNumber)"
         

Replace `NEW_DSP_PROJECT_ID` with the project ID of the Google Cloud project that hosts your new Data Studio Pro subscription.

  2. Update your Looker (Google Cloud core) instance to link the new project:
         
         gcloud looker instances update INSTANCE_NAME \
             --project=PROJECT_ID \
             --region=REGION \
             --linked-lsp-project-number=NEW_DSP_PROJECT_NUMBER
         

Replace the following:

     * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
     * `PROJECT_ID`: the project ID of the Google Cloud project that hosts your Looker (Google Cloud core) instance.
     * `REGION`: the region where your Looker (Google Cloud core) instance is located.
     * `NEW_DSP_PROJECT_NUMBER`: the project number from the previous step.
  3. Verify that your Looker (Google Cloud core) instance is linked to the new project:
         
         gcloud looker instances describe INSTANCE_NAME \
             --project=PROJECT_ID \
             --region=REGION \
             --format="value(linkedLspProjectNumber)"
         




**Important:** Google Cloud automatically applies the complimentary licenses to the users in the new Data Studio Pro subscription. If there are fewer users in the new subscription than in the old subscription, some unused complimentary licenses remain attached to the old Data Studio Pro subscription. Google Cloud converts these unused licenses to paid licenses, subject to [Data Studio Pro pricing](https://cloud.google.com/data-studio#pricing). **To avoid charges, cancel the old subscription.**

## Unlink complimentary Data Studio Pro licenses from your instance

If you no longer want to link your Looker (Google Cloud core) instance to your Data Studio Pro Google Cloud project, you can unlink the project using the Google Cloud console or the Google Cloud CLI.

**Warning:** If you unlink your Data Studio Pro project from your Looker (Google Cloud core) instance, your complimentary Data Studio Pro licenses become paid licenses, subject to [ Data Studio Pro pricing](https://cloud.google.com/data-studio#pricing). This conversion typically happens within 24 hours. If you no longer want to use your complimentary licenses, we recommend that you cancel the associated Data Studio Pro subscription. To learn more about what happens when you cancel a Data Studio subscription, see Effects of canceling a Data Studio Pro subscription. 

### console

  1. In the [**Data Studio Pro** tab](https://docs.cloud.google.com/looker/docs/looker-core-view-console#tabs) of your Looker (Google Cloud core) instance settings, disable the **Accept Data Studio Pro licenses** toggle.
  2. Click **Save**.



### gcloud

  1. Unlink the Data Studio Pro project from your Looker (Google Cloud core) instance by setting the `--linked-lsp-project-number` flag to `0`:
         
         gcloud looker instances update INSTANCE_NAME \
             --project=PROJECT_ID \
             --region=REGION \
             --linked-lsp-project-number=0
         

Replace the following:

     * `INSTANCE_NAME`: the name of your Looker (Google Cloud core) instance.
     * `PROJECT_ID`: the project ID of the Google Cloud project that hosts your Looker (Google Cloud core) instance.
     * `REGION`: the region where your Looker (Google Cloud core) instance is located.
  2. Verify that the Data Studio Pro project is unlinked:
         
         gcloud looker instances describe INSTANCE_NAME \
             --project=PROJECT_ID \
             --region=REGION \
             --format="value(linkedLspProjectNumber)"
         

When the project is unlinked, the command returns empty output.




## Effects of canceling a Data Studio Pro subscription

If the Data Studio Pro subscription is canceled, Looker will no longer recognize the subscription. Although the Google Cloud console will continue to reflect that the Looker instance and the Data Studio Pro subscription are linked, you will no longer be billed for Data Studio Pro usage on the Google Cloud project. Your Looker instance's Data Studio Pro licenses are still available if you reinstate your subscription (within the [30-day grace period](https://docs.cloud.google.com/looker/docs/studio/cancel-a-looker-studio-pro-subscription#30-day_grace_period)) or if you initiate a new subscription. The no-cost version of Data Studio is also available for use.

For more information about the effects of canceling a Data Studio Pro subscription or deleting a Google Cloud project that is associated with a canceled subscription, see [Cancel a Data Studio Pro subscription](https://docs.cloud.google.com/looker/docs/studio/cancel-a-looker-studio-pro-subscription).

## Troubleshooting complimentary licenses

**Note:** Manual license count adjustments that are requested through the Support team typically take 7 to 10 working days to fully reflect in your Data Studio Pro subscription.

Errors may occur when you accept complimentary Data Studio Pro licenses or add users to a Data Studio Pro subscription. See the following table for steps on how to troubleshoot errors that are related to accepting licenses.

Error message | Steps to resolve | Example | `You have reached your license limit. To add more users, either delete some existing users/groups or purchase additional licenses.` | 

  1. In Data Studio, select **Pro subscriptions** from the left navigation to open the list of Data Studio Pro subscriptions.
  2. Data Studio displays the number of complimentary licenses that are available for the Google Cloud project that hosts your Looker (Google Cloud core) instance. For that project, under **Actions** , select **Manage subscription**.
  3. Navigate to the **Review and confirm Data Studio Pro licenses** step, and review the number of licenses in the **Number of licenses to buy** field.
  4. Enter the total number of licenses that you want to use, _including_ the number of complimentary licenses that are available for the subscription.

| If there are 10 complimentary licenses available, add 10 users to your subscription to use all licenses. If you add 11 users, you will be charged for 1 additional license. If you increase the **Number of licenses to buy** field to 11, you will be charged for 1 additional license, which you can assign at a later date.   
---|---|---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
