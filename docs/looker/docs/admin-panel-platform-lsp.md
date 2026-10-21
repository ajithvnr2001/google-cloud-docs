---
url: https://docs.cloud.google.com/looker/docs/admin-panel-platform-lsp/
title: Admin settings - Data Studio Pro \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:48:39.658190+00:00
---

# Admin settings - Data Studio Pro  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-platform-lsp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - Data Studio Pro Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Complimentary Data Studio Pro licenses are also available for Looker (Google Cloud core) instances. See the [Accept complimentary Data Studio Pro licenses for a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-lsp) documentation page.**Important:** Complimentary Data Studio Pro licenses and this admin page are not available for Looker (original) instances that are are affiliated with Looker contracts that were signed after **August 1, 2026**.

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

Complimentary Data Studio Pro licenses are available for Looker instances that fulfill the following requirements:

  * The instance is hosted by Looker.
  * If hosted in the Google Cloud, the instance must be running Looker 22.16 or later.
  * If hosted by a cloud provider other than Google Cloud, the instance must be running Looker 23.4 or later.



Each Looker user who will use Data Studio must also be a Google Workspace or Cloud Identity user with a [Managed Google account](https://support.google.com/work/android/answer/6371476).

A Looker account, as defined in your Looker agreement, can be associated with only one Data Studio Pro subscription.

### Required roles

To get the permission that you need to accept complimentary Data Studio Pro licenses, ask your Looker admin to grant you the [Admin](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) Looker role.

To get the permission that you need to set up a self-service subscription to Data Studio Pro, ask your IAM administrator to grant you a role containing the `lookerstudio.pro.manage` permission for the Google Cloud project that hosts your Data Studio Pro content. The [Looker Studio Pro Manager](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.proManager) (`roles/lookerstudio.proManager`) and [Owner](https://docs.cloud.google.com/iam/docs/understanding-roles#owner) (`roles/owner`) contain this permission by default, but you may be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

For more information about granting Identity and Access Management roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## AcceptData Studio Pro licenses

To accept your complimentary Data Studio Pro licenses, follow these steps:

  1. In the **Admin** panel of your Looker instance, navigate to the **Platform** section and select the **Data StudioPro** page. If your Looker account uses multiple instances, you can accept your complimentary licenses in any instance.
  2. Enable the **AcceptData Studio Pro licenses** setting.



## Select a Google Cloud project

After you have accepted the complimentary Data Studio Pro licenses, you must associate your Looker instance with the Google Cloud project that yourData Studio Pro subscription uses. To specify yourData Studio Pro Google Cloud project, follow these steps:

  1. In the **Admin** panel of your Looker instance, navigate to the **Platform** section and select the **Data Studio Pro** page.
  2. In the **Google Cloud Project Number** field, enter the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) for the Google Cloud project that hosts yourData Studio Pro content. Note that the project number is distinct from the project ID.
  3. Click **Save**.

**Warning:** Once you have saved your project, note the following effects: 

If you disable the **AcceptData Studio Pro licenses** setting, your complimentary Data Studio Pro licenses become paid licenses, subject to [Data StudioPro pricing](https://cloud.google.com/data-studio#pricing). This conversion typically happens within 24 hours. If you no longer want to use your complimentary licenses, we recommend that you cancel the associatedData Studio Pro subscription. To learn more about what happens when you cancel a Data Studiosubscription, see Effects of canceling a Data Studiosubscription.

Just changing the project number won't transfer your complimentary licenses to another project. Instead, you must transfer your licenses in yourData Studio Pro subscription settings.

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

  1. In the **Admin** panel of your Looker instance, navigate to the **Platform** section and select the **Data Studio Pro** page.
  2. In the **Google Cloud Project Number** field, enter the [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) for the new Google Cloud project. Note that the project number is distinct from the project ID.
  3. Click **Save**.

**Important:** The complimentary licenses will be applied automatically to the users in the new Data Studio Pro subscription. If there are fewer users in the new subscription than in the old subscription, there will be some unused complimentary licenses still attached to the old Data Studio Pro subscription. These unused licenses will be converted to paid licenses, subject to [Data Studio Pro pricing](https://cloud.google.com/data-studio#pricing). **To avoid being charged for these licenses, you must cancel the old subscription.**

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

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
