---
url: https://docs.cloud.google.com/billing/docs/how-to/budgets-notification-recipients/
title: Customize budget alert email recipients \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:14.663503+00:00
---

# Customize budget alert email recipients  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/budgets-notification-recipients/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Customize budget alert email recipients Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

You can specify the email recipients of budget alerts in these ways:

![Diagram of budget alert notifications](https://docs.cloud.google.com/static/billing/docs/images/budget-alert-diagram-cbar.png)**Figure 1** : Illustrates the default email feature for budget alert notifications and the optional method to customize the email recipients using Cloud Monitoring. 

![Diagram of budget alert notifications](https://docs.cloud.google.com/static/billing/docs/images/budget-alert-diagram-cbar.png)

  * **Role-based** : For budgets scoped to a Cloud Billing account (or to more than one project within the billing account), you can send email alerts to Billing Account Administrators and Billing Account Users on the target Cloud Billing account when the [budget alert threshold rules](https://docs.cloud.google.com/billing/docs/how-to/budgets#alert-thresholds) trigger an email notification. Use this option if Billing Account Administrators and Billing Account Users can take cost control actions based on the alert emails.

For budgets scoped to a _single_ project, you can also send email alerts to Project Owners of the budget's project ([Preview](https://cloud.google.com/products/#product-launch-stages)), when the [budget alert threshold rules](https://docs.cloud.google.com/billing/docs/how-to/budgets#alert-thresholds) trigger an email notification. Use this option if Project Owners can take cost control actions on their projects based on the alert emails.

  * **Using Cloud Monitoring (described on this page)** : You can specify other people in your organization (for example, project managers) to receive budget alert emails.

Use this option if your organization's Billing Account Administrators, Billing Account Users, and Project Owners aren't the best recipients to take cost control actions based on the alerts. For example, you want to send an email alert to a developer or a system administrator who is not a Project Owner or a Billing Account Administrator.




To customize who receives the budget alert emails for a specific budget, link Monitoring email notifications to the budget, and select up to five email notification channels.

### Permissions required for this task

To set up Cloud Monitoring notification channels and link them to a Cloud Billing budget, you need the following roles:

  * To [create](https://docs.cloud.google.com/billing/docs/how-to/budgets#create-budget) or [modify](https://docs.cloud.google.com/billing/docs/how-to/budgets#edit-or-delete-budget) a budget for your _Cloud Billing account_ , you need the [Billing Account Costs Manager role](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam) or the [Billing Account Administrator role](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam) on the Cloud Billing account.

To [create](https://docs.cloud.google.com/billing/docs/how-to/budgets#permissions-project) or [modify](https://docs.cloud.google.com/billing/docs/how-to/budgets#project_level_access_to_manage_budgets) a budget scoped for a _project_ that you own (this feature is in [Preview](https://cloud.google.com/products/#product-launch-stages)), you need the [Project Owner role](https://docs.cloud.google.com/resource-manager/docs/access-control-proj) or the [Project Editor role](https://docs.cloud.google.com/resource-manager/docs/access-control-proj) on the Google Cloud project.

  * To create or modify Cloud Monitoring notification channels, you must have the [Monitoring Editor role](https://docs.cloud.google.com/monitoring/access-control) on the project where you create the notification channel.




#### Permissions when using custom roles

If you're using custom roles to grant access, your role must have the following permissions to set up Cloud Monitoring notification channels and link them to a Cloud Billing budget:

#### For billing-account-level access

To create a new Cloud Billing budget to link it to new Cloud Monitoring notification channels, you need these specific permissions:

  * [`billing.budgets.create`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budget_alerts) on the Cloud Billing account, to create a new budget for a Cloud Billing account.
  * [`billing.budgets.get` and `billing.budgets.list`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budget_alerts) on the Cloud Billing account, to view all budgets for the Cloud Billing account.
  * [`billing.budgets.update`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budget_alerts) on the Cloud Billing account, to modify an existing budget for a Cloud Billing account.
  * [`roles/monitoring.editor`](https://docs.cloud.google.com/monitoring/access-control) on the project where you want to create notification channels.



To edit an _existing_ Cloud Billing budget to link it to _existing_ Cloud Monitoring notification channels, you need these specific permissions:

  * [`billing.budgets.get` and `billing.budgets.list`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budget_alerts) on the Cloud Billing account, to view all budgets for the Cloud Billing account.
  * [`billing.budgets.update`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budget_alerts) on the Cloud Billing account, to modify an existing budget.
  * [`roles/monitoring.viewer`](https://docs.cloud.google.com/monitoring/access-control#predefined_roles) on the project that stores the notification channels.



#### For project-level access to manage budgets

If you have limited or no access to a Cloud Billing account, you can still create or modify a budget that is scoped only to the projects that you own, one project at a time.

To manage budgets for a project and customize the email recipients of budget alerts, you need a role that includes these specific permissions:

  * [`resourcemanager.projects.get`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budget_alerts) on your project, to view the projects associations (such as the linked billing account) for your project.
  * [`billing.resourceCosts.get`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budget_alerts) on your project (optional), to view costs and usage for your project.
  * [`billing.resourcebudgets.read`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budget_alerts) on your project, to view a billing account's _single-project_ budgets that are scoped to your project.
  * [`billing.resourcebudgets.write`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budget_alerts) on your project, to create or modify _single-project_ budgets that are scoped to your project.
  * [`roles/monitoring.editor`](https://docs.cloud.google.com/monitoring/access-control) on the project where you want to create notification channels, or [`roles/monitoring.viewer`](https://docs.cloud.google.com/monitoring/access-control#predefined_roles) on the project that stores the notification channels.



#### Permissions required for the recipients of budget alert emails

When you select Cloud Monitoring email notification channels to customize who receives alert emails (in addition to Billing Account Administrators, Billing Account Users, or Project Owners), the email addresses you specify are sent the budget alert emails when the [threshold rules](https://docs.cloud.google.com/billing/docs/how-to/budgets#alert-thresholds) trigger an alert.

The budget alert emails contain helpful links to the budget, so that you can quickly view it and take any appropriate actions. The people you specify to receive alert emails using _email notification channels_ might not have the correct permissions to view the Cloud Billing budgets in the Google Cloud console.

If you want the recipients of the alert emails to be able to view the budget, email recipients need [permissions on the Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/budgets#permissions_required_for_viewing_a_list_of_budgets) (to view billing-account-level budgets) or on the [budget's project](https://docs.cloud.google.com/billing/docs/how-to/budgets#project_level_access_to_view_budgets) (for single-project-scoped budgets).

  * For billing-account-level budgets, at a minimum, ensure email recipients are added to the [Billing Account Viewer role](https://docs.cloud.google.com/billing/docs/how-to/budgets#permissions_required_for_viewing_a_list_of_budgets) on the Cloud Billing account that owns the budget.
  * For single-project-scoped budgets, at a minimum, ensure email recipients are added to the [Project Viewer role](https://docs.cloud.google.com/billing/docs/how-to/budgets#project_level_access_to_view_budgets) on the budget's project ([Preview](https://cloud.google.com/products/#product-launch-stages)).



See [View a list of budgets](https://docs.cloud.google.com/billing/docs/how-to/budgets#view-budgets) for additional information.

#### About Google Cloud permissions

For more information about Cloud Billing permissions, see:

  * [Overview of Cloud Billing access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access)
  * [Create custom roles for Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#budget_alerts)
  * [Understanding predefined Identity and Access Management roles for Cloud Billing](https://docs.cloud.google.com/iam/docs/roles-permissions/billing)



For more information about Google Cloud project permissions, see:

  * [Access control for projects with IAM](https://docs.cloud.google.com/resource-manager/docs/access-control-proj)
  * [IAM basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/roles-overview#basic)



## Set up and enable Cloud Monitoring email notifications

To customize the email addresses that will receive budget alert notifications, link notification channels to your budget.

### Before you begin: create an email notification channel

You must [create an email notification channel in Cloud Monitoring](https://docs.cloud.google.com/monitoring/support/notification-options#creating_channels).

For Cloud Billing budget alerts, you must configure Email notification channels. Other types of notification channels aren't supported.

If you already set up email notification channels that you want to use, skip this step and link the notification channel to your budget.

**Tip:** If you want to [send notifications to Slack](https://docs.cloud.google.com/billing/docs/how-to/notify#send_notifications_to_slack), you can configure [programmatic notifications](https://docs.cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications).

### Link your budget to email notification channels

After you create an email notification channel, follow these steps to link your budget to it:

  1. Using the procedure that fits your level of access to Cloud Billing accounts, sign in to the **Budgets & alerts** page in the Billing section of the Google Cloud console:

Users with Cloud Billing account permissions | Users with project-level permissions only ([Preview](https://cloud.google.com/products/#product-launch-stages))  
---|---  
If you have Cloud Billing account permissions, you can select from a list of billing accounts that you have permissions to access.
     1. Sign in to the **Budgets & alerts** page in the Google Cloud console. [ Open Budgets & alerts](https://console.cloud.google.com/billing/budgets)
     2. At the prompt, **choose the Cloud Billing account** for which you'd like to manage budgets. The **Budgets & alerts** page opens for the selected billing account.
|  If you only have project permissions, but don't have any permissions on your project's Cloud Billing account, you need to select your project before you navigate to the Billing section.
     1. Sign in to the Google Cloud console dashboard and select a project. [ Open Google Cloud console](https://console.cloud.google.com/projectselector2/home/dashboard?project=_)
     2. **Select the project** for which you want to manage budgets.
     3. Next, **navigate to Billing** : Open the Google Cloud console **Navigation menu** menu, and then select **Billing**. If you're prompted to choose which billing account you want to view and manage, click **Go to linked billing account** to view the billing account that is linked to your selected project. The **Billing Overview** page opens for the selected billing account.
     4. In the **Cost management** section of the **Billing navigation menu** , select **Budgets & alerts**.   
  2. If necessary, [create a budget](https://docs.cloud.google.com/billing/docs/how-to/budgets#create-budget) and set [alert threshold rules](https://docs.cloud.google.com/billing/docs/how-to/budgets#alert-thresholds). Or, to edit an existing budget and alert rules, click a _budget name_.

  3. In the **Actions** section, under **Manage notifications** , select **Link Monitoring email notifications to this budget**.

  4. From the **Select project** menu, select the project that contains the email notification channels.

  5. Under **Notification Channels** , select up to five _existing_ notification channels, or click **Manage notification channels** to edit or create email notification channels on demand.

     * If you're editing a budget, you can link new notification channels or unlink previously selected email channels by using the checkboxes next to the channel names.
     * While editing a budget, if you can no longer see an email notification channel that you previously linked to the budget, this might be because the notification channel was deleted from the project. To learn more about viewing, editing, or deleting notification channels, visit [Notification options](https://docs.cloud.google.com/monitoring/support/notification-options).
  6. Click **Save**.




## Delivery guarantees for Cloud Monitoring notifications

After you create a budget and link it to Cloud Monitoring email notification channels, you can expect emails to be sent as described here:

  * It may take several hours before receiving the first alert email.
  * Email alerts are sent only when triggered by the threshold rules.
  * If the Cloud Billing account has no usage, no email notification is sent.
  * If delivery fails due to notification channel misconfiguration, you will _not_ be notified.
  * Delivery will fail if the notification channel no longer exists.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
