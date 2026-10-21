---
url: https://docs.cloud.google.com/data-studio/cancel-a-pro-subscription/
title: Cancel a Data Studio Pro subscription \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:16.482669+00:00
---

# Cancel a Data Studio Pro subscription  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/cancel-a-pro-subscription/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Cancel a Data Studio Pro subscription Stay organized with collections  Save and categorize content based on your preferences. 

This page is for Data Studio Pro project owners who want to terminate a self-service Pro subscription. This page also describes the process of canceling or changing a Monthly Active User (MAU) subscription.

If you set up the Data Studio Pro subscription as part of a Google Workspace subscription you will find additional important details in the [Google Workspace Admin Help Center documentation](https://support.google.com/a/answer/16698551).

## Before you begin

Before you cancel a Data Studio Pro subscription, we highly recommend that you have a plan for moving your Pro content out of team workspaces. [Learn more about moving team workspace content](https://docs.cloud.google.com/data-studio/manage-team-workspace-assets).

  * To perform the steps on this page, you must have either the [Owner role](https://docs.cloud.google.com/iam/docs/understanding-roles#owner) on the Google Cloud project that's associated with your Data Studio Pro subscription or the [Workspace Services Admin role](https://support.google.com/a/answer/2405986#services_admin).
  * If the original project owner has left the organization, assign another user the Owner or Looker Studio Pro Manager role on the project to manage or cancel the subscription. Contact an administrator who has the Organization Administrator role (`roles/resourcemanager.organizationAdmin`) to update IAM permissions if needed. Without one of these roles, the option to cancel the subscription isn't visible.



## How to cancel a Data Studio Pro subscription

How you cancel a subscription depends on where that subscription was originally set up:

  * For subscriptions that were set up directly from the no-cost version of Data Studio, or that were set up from the Google Cloud console, you can cancel by using either the Data Studio Pro interface or the Google Cloud console. This includes subscriptions that were set up by using Data Studio Pro licenses associated with your Looker account.
  * For subscriptions that were set up in Google Workspace, you must cancel by using the Google Workspace Admin console.



## Cancel a subscription by using Data Studio Pro

Follow these steps to cancel a Data Studio Pro subscription by using the Data Studio Pro interface. If you want to cancel multiple subscriptions, you must cancel each one individually.

  1. [Sign in to Data Studio Pro](https://datastudio.google.com/).
  2. In the left navigation, click **Pro subscription**.
  3. Locate the Google Cloud project for the Data Studio Pro subscription that you want to cancel and then click ![Cancel.](https://docs.cloud.google.com/static/data-studio/images/cancelbaselinep900fill0wght400grad0opsz24-2023-09-22.png)**Cancel**.
  4. In the dialog that appears, enter `Cancel`.

**Note:** You must enter the word exactly as shown, in English and with a capital **C**.

  1. Click **Cancel subscription**. It may take a few minutes before your subscription is canceled.



## Cancel a subscription by using the Google Cloud console

Follow these steps to cancel a Data Studio Pro subscription using the Google Cloud console. If you want to cancel multiple subscriptions, you must cancel each one individually.

  1. Sign into the Google Cloud console using an account that has the [Data Studio Pro Manager role](https://docs.cloud.google.com/iam/docs/roles-permissions/datastudio#lookerstudio.proManager) (`roles/lookerstudio.proManager`) or the [Owner role](https://docs.cloud.google.com/iam/docs/understanding-roles#owner) (`roles/owner`) on the Cloud project that is associated with your Data Studio Pro subscription. We recommend using the Data Studio Pro Manager role to follow the principle of least privilege.
  2. Visit the [Data Studio product page](https://console.cloud.google.com/looker-studio/home).
  3. Click **Cancel Subscription**.
  4. In the dialog that appears, enter `cancel`.

**Note:** You must enter the word exactly as shown, in English and with a lowercase **c**.

  1. Click **Confirm**. It may take a few minutes before your subscription is canceled.



## Cancel a subscription by using the Google Workspace Admin console

To cancel a Data Studio Pro subscription in Google Workspace, follow the steps outlined in [Cancel your Data Studio Pro subscription](https://support.google.com/a/answer/16698551).

Canceling a Data Studio Pro subscription in Google Workspace has some important differences from the information provided on this page, including:

  * Data Studio Pro subscriptions in Google Workspace **don't have a cancelation grace period**. Google Workspace cancels your subscription immediately upon submission of the cancelation request.
  * Users will lose access to Pro assets stored in team workspaces immediately. We recommend that users transfer assets that you want to keep to out of team workspaces that belong to the canceled project and into their [Owned by me](https://docs.cloud.google.com/data-studio/owned-by-me) location in the no-cost version of Data Studio before canceling the subscription.
  * Although Data Studio Pro subscriptions in Google Workspace don't have a cancelation grace period, Pro assets remain in the canceled project for 30 days. If you start a new subscription within 30 days and use the same Google Cloud project that you used for your previously canceled subscription, your content will be accessible in your new subscription without any additional migration steps. After 30 days, the team workspace folders will be permanently deleted.



For additional details, see [Cancel your Data Studio Pro subscription](https://support.google.com/a/answer/16698551).

## What happens when you cancel your subscription?

Canceling a Data Studio Pro subscription by using the Data Studio Pro interface or the Google Cloud console has the following effects:

  * Users can continue to use the no-cost version of Data Studio.
  * Pro features in reports that you moved to or created in a [team workspace](https://docs.cloud.google.com/data-studio/about-team-workspaces) or [Sandbox](https://docs.cloud.google.com/data-studio/sandbox) that belongs to the canceled Pro project will continue to work for 30 days.
  * All [alerts](https://docs.cloud.google.com/data-studio/create-alerts-on-a-chart) will be deactivated.
  * Any users or groups to whom you've granted the [Can create schedules permission](https://docs.cloud.google.com/data-studio/invite-others-to-your-reports) will retain the permission. You can't grant the permission to any other users.
  * Users have a 30-day grace period to move their content out of the canceled Pro project and into the no-cost version of Data Studio.
  * You won't be billed for Data Studio Pro usage on the canceled Pro project.



### 30-day grace period

**Warning:** Canceling a Data Studio Pro subscription in Google Workspace **does not** have a grace period. Your subscription is canceled and team workspaces and folders may become immediately unavailable. We recommend that you bookmark links to important reports to ensure their continued availability. Data Studio Pro content may not be recoverable if your subscription is canceled for more than 30 days.

Users have 30 days to move their content out of the Data Studio Pro project and into Data Studio. To do this, users should move any content that they want to keep out of team workspaces that belong to the canceled project and into their [Owned by me](https://docs.cloud.google.com/data-studio/owned-by-me) location in the no-cost version of Data Studio.

During the 30-day grace period, the owner of the canceled Pro project can reassign ownership of the content. [Learn more about transferring ownership of Data Studio content](https://docs.cloud.google.com/data-studio/transfer-ownership).

At the end of the 30-day grace period, the following will occur:

  * All team workspaces that belong to the canceled Pro project are permanently deleted.
  * If the canceled Pro project has content in a team workspace and there are managers of that workspace with active accounts, then that content's ownership is transferred to a workspace manager. The workspace manager can locate this transferred content: 
    * In their [Sandbox](https://docs.cloud.google.com/data-studio/sandbox), if they have an active Data Studio Pro license.
    * In their [Owned by me](https://docs.cloud.google.com/data-studio/owned-by-me) section, if they are using the no-cost version of Data Studio.
  * If no active team workspace manager accounts exist, the content will have no owner and will remain in the canceled Pro project.
  * If the canceled Pro project has content in a Sandbox, and that Sandbox owner's account is still active, then that content moves back to the owner's **Owned by me** location in Data Studio.
  * If the Sandbox owner's account no longer exists, the content will have no owner and will remain in the canceled Pro project.
  * If a new owner can't be assigned according to the preceding points, the content will reside in the canceled Pro project. The project owner can [assign a new content owner](https://docs.cloud.google.com/data-studio/transfer-ownership).

**Important:** If the canceled project is deleted, any content that remains in that project will also be **permanently deleted**.

## Renew a canceled subscription

You can renew your subscription at any time before the 30-day grace period expires. When you renew a subscription, reports and data sources in team workspaces become editable again, and you can resume using Pro features with those content. Billing will resume as before.

You must move any content that was moved to a user's **Owned by me** folder back to team workspaces before that content can use Pro features again.

### To renew a subscription

  1. [Sign in to Data Studio Pro](https://datastudio.google.com/).
  2. In the left navigation, select **Pro subscription.**
  3. Locate the canceled Data Studio Pro project that you want to renew. You'll see the days remaining in the grace period.
  4. Click **Renew**.
  5. Review the project information, and then click **Renew subscription**.

**Important:** Once the 30-day grace period has expired, you can't renew a canceled subscription. After the 30-day grace period has expired, you'll need to create a new subscription to resume using your previous project for Data Studio Pro.

## Cancel or change a Monthly Active User (MAU) subscription

If you have a Data Studio [Monthly Active User (MAU) subscription](https://docs.cloud.google.com/data-studio/pro-subscription-overview#subscription_type), [contact a Google Cloud sales specialist](https://cloud.google.com/contact) to cancel your subscription.

If you want to change your MAU subscription to a self-service subscription, first you need to cancel the MAU subscription. Then, [start a new Pro subscription](https://docs.cloud.google.com/data-studio/start-a-new-pro-subscription) after the cancellation is complete. When selecting a [Google Cloud project](https://docs.cloud.google.com/data-studio/step-1-select-a-google-cloud-project), use the same project as your canceled MAU subscription. This way, your content will be accessible in your new subscription without any additional migration steps.

### Things to consider during the subscription migration

Keep the following considerations in mind during the downtime between canceling your MAU subscription and starting your new Pro self-service subscription:

  * **Pro features will be unavailable:** While your subscription is canceled, Pro features will be disabled on your Data Studio content.
  * **Workspaces and folders may be unavailable:** While your subscription is canceled, team workspaces and folders may be inaccessible. Store the URLs of important reports as bookmarks to ensure their availability.
  * **Switch within 30 days:** Pro content may not be recoverable if your subscription is canceled for more than 30 days.



## Troubleshoot missing cancellation option

This section explains why you may not be able to cancel a Pro subscription and what to do about it.

**Symptom**

The option to cancel the Data Studio Pro subscription is not visible in the Data Studio UI or the Google Cloud console.

**Cause**

This situation usually occurs if you don't have the required IAM permissions for the Google Cloud project. This situation often arises if the person who originally set up the subscription has left the organization.

**Resolution**

To resolve this issue, follow these steps:

  1. **Identify the project:** Confirm the Google Cloud project ID that's linked to the Data Studio Pro subscription.
  2. **Verify IAM roles:** Ensure that an active user has either the **Owner** role or the **Looker Studio Pro Manager** role on that project. If you don't have these roles, contact your Google Cloud Organization Administrator to request them.
  3. **Cancel the subscription:** Once the roles are assigned, the cancellation option should appear. Follow the steps that are in outlined previously on this page.
  4. **Contact Support:** If the cancellation option is still missing after you've verified the roles, contact [Google Cloud Support](https://cloud.google.com/support) with the Project ID and the details of the steps that you've taken.



## Related resources

  * [Change your Data Studio Pro billing account](https://docs.cloud.google.com/data-studio/change-billing-account)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
