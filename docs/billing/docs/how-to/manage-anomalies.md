---
url: https://docs.cloud.google.com/billing/docs/how-to/manage-anomalies/
title: View and manage cost anomalies \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:18.832192+00:00
---

# View and manage cost anomalies  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/manage-anomalies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  View and manage cost anomalies Stay organized with collections  Save and categorize content based on your preferences. 

Anomaly detection helps you manage unexpected costs across your [billing account's projects](https://docs.cloud.google.com/billing/docs/how-to/view-linked). These anomalies are spikes or deviations in usage costs that differ from your expected spend, when compared to historical spending patterns. Usage costs are calculated using the on-demand rates that are applicable to your billing account. On-demand rates include publicly available list prices and any contracted, negotiated, or discounted pricing that's available for your Cloud Billing account. Usage cost totals are gross costs that include [spend-based CUD discounts](https://docs.cloud.google.com/docs/cuds-multiprice), but exclude [legacy spend-based CUD credits](https://docs.cloud.google.com/docs/cuds-spend-based#legacy-cuds), [resource-based CUD credits](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) and [other savings](https://docs.cloud.google.com/billing/docs/how-to/reports#other_savings), such as promotional credits, and sustained use discounts.

For AI workloads (such as Gemini API and Vertex AI), you can also view **early anomalies**. Early anomalies use near real-time cost estimates to provide daily, service-level insights before finalized billing occurs.

The **Anomalies** dashboard displays all cost anomalies associated with your projects, within the linked billing account. You can use the **Anomalies** dashboard to do the following:

  * Investigate the root causes of anomalies.
  * View early anomalies for AI workloads [Preview](https://cloud.google.com/products#product-launch-stages).
  * Customize your view by setting thresholds for cost impact amount and percent of deviation (applies to standard anomalies only).
  * Manage automated alerts and notifications for detected anomalies.
  * Provide feedback on detected anomalies to improve the tool's accuracy.



For reseller accounts and subaccounts, this feature is only available if you enable project-based cost visibility. Resellers can only view anomalies for their projects. To view anomalies for a subaccount, you must switch to the subaccount. To enable project-based cost visibility, contact [Cloud Billing Support](https://docs.cloud.google.com/billing/docs/support).

## Permissions required for this task

You can view and manage anomalies for all projects on a Cloud Billing account or for individual projects. To manage anomalies for all projects on a Cloud Billing account, you need permissions on the billing account. To view anomalies for a specific project, you need billing-specific permissions on the project.

### Full billing account permissions

Cloud Billing account permissions are granted using roles on the billing account. To view the cost anomalies for your Cloud Billing account, including viewing the cost information for _all_ of the Google Cloud projects that are linked to the billing account, you need a role on your _Cloud Billing account_ that includes the following [ permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/billing): 

  * `billing.accounts.get`
  * `billing.accounts.getIamPolicy`
  * `billing.anomalies.get`
  * `billing.anomalies.list`



To gain these permissions using a predefined role, ask your administrator to grant you one of the following [Cloud Billing IAM](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam) roles on your Cloud Billing account: 

  * [Billing Account Costs Manager](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview_of_billing_roles_in)
  * [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview_of_billing_roles_in)
  * [Billing Account Viewer (view only)](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview_of_billing_roles_in)



To set up Pub/Sub notifications for anomalies, you need additional permissions. 

To gain the necessary permissions using a predefined role, ask your administrator to grant you the following role on the _target project_ that contains the Pub/Sub topics: 

  * [Pub/Sub Admin](https://docs.cloud.google.com/pubsub/docs/access-control)



If your organization uses [custom roles](https://docs.cloud.google.com/billing/docs/how-to/custom-roles) for authentication, you need the following permissions on the _target project_ : 

  * `pubsub.topics.setIamPolicy`
  * `pubsub.topics.list`
  * `pubsub.subscriptions.consume`



### Project-scoped billing permissions

Depending on your level of Cloud Billing access for project costs, by using billing-specific permissions on a project, you can view anomalies that are scoped to the projects that you own, one project at a time.

For more information about project-limited permissions for viewing costs and anomalies in Cloud Billing accounts, see [ project-scoped access to Cloud Billing accounts](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access#project-permissions).

Access a billing account for _multiple_ Google Cloud projects  | Access billing for an _individual_ Google Cloud project  
---|---  
You can view cost anomalies for your authorized Google Cloud projects, one project at a time. When you have multi-project-scoped access to a Cloud Billing account through a _combination_ of project and billing account permissions, on the Anomalies page, you can use a project selector to switch between your billing-authorized projects.

  * **Projects** : you need billing-specific cost view permissions on _each Google Cloud project_. Project permissions are granted with roles on the _Google Cloud project or folder_. At a minimum, you need the following permissions on each project:
    * `resourcemanager.projects.get`
    * `billing.anomalies.get`
    * `billing.anomalies.list`
  * **Cloud Billing account** : you need project-scoped billing permissions on the _Cloud Billing account_ that is [ linked to your authorized projects](https://docs.cloud.google.com/billing/docs/how-to/view-linked). Billing account permissions are granted using roles on the _Cloud Billing account_. For multi-project-scoped access to the billing account, you need the following role on the _Cloud Billing account_ :
    * [ Project Billing Costs Manager](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.projectCostsManager)

Learn more about the [ permissions required for _multi-project-scoped access_ to Cloud Billing accounts](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access#required-permissions). |  To access Cloud Billing to view costs anomalies for an _individual_ Google Cloud project, one project at a time, you only need _billing-specific_ permissions on the _Google Cloud project_.

  * **Projects** : you need billing-specific cost view permissions on _each Google Cloud project_ you want to view. Project permissions are granted with roles on the _Google Cloud project or folder_. At a minimum, you need the following permissions on each project:
    * `resourcemanager.projects.get`
    * `billing.anomalies.get`
    * `billing.anomalies.list`
  * **Cloud Billing account permissions aren't required** : If you are viewing billing information for one project at a time, you don't need permissions on the Cloud Billing account that is [ linked to your authorized Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/view-linked). 

Learn more about the [ _project_ permissions required for _single-project-scoped access_ to Cloud Billing accounts](https://docs.cloud.google.com/billing/docs/how-to/project-owners/setup-multi-project-access#project-permissions).  
  
For more information about _Cloud Billing permissions_ , see:

  * [ Overview of Cloud Billing access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access)
  * [ Create custom roles for Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/custom-roles)
  * [ Understanding predefined Identity and Access Management roles for Cloud Billing](https://docs.cloud.google.com/iam/docs/choose-predefined-roles)

|  For more information about Google Cloud _project permissions_ , see:

  * [ Access control for projects with IAM](https://docs.cloud.google.com/resource-manager/docs/access-control-proj)
  * [ IAM basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/roles-overview#basic)

  
---|---  
  
## Access the Anomalies dashboard

To view the cost anomalies for your Cloud Billing account or projects, follow the procedure that fits your level of access to Cloud Billing accounts. Cost anomalies for a Cloud Billing account are accessible in the Billing section of the Google Cloud console.

### Full billing account permissions

If you have full Cloud Billing account permissions, you can select from a list of billing accounts that you have permissions to access.

  1. In the Google Cloud console, go to your Cloud Billing account.

[ Go to your Cloud Billing account](https://console.cloud.google.com/billing/overview)
  2. At the prompt, select the Cloud Billing account that you want to view anomalies for.

The Billing **Overview** page opens for the selected billing account.

  3. In the **Cost management** section of the **Billing navigation menu** ,select **Anomalies**.



When you access cost anomalies with full _billing-account-level permissions_ , you can see anomalies for _all_ of the projects that are linked to the Cloud Billing account.

### Project-scoped billing permissions

You can access the tools in Cloud Billing to view cost anomaly information for individual projects, one project at a time.

Depending on your level of Cloud Billing access for project costs, you might have a project selector on the anomalies page that you can use to switch between projects that you want to view.

View costs in a billing account for _multiple_ Google Cloud projects | View costs for an _individual_ Google Cloud project  
---|---  
When you have _project-scoped_ access to view billing data and cost anomalies, you can see costs anomalies for _one project_ at a time.

  1. In the Google Cloud console, go to the Billing / Anomalies page. [ Go to Anomalies](https://console.cloud.google.com/billing/anomalies)
  2. In the **Billing account** selector, **choose the Cloud Billing account** for which you'd like to view cost anomalies, then click **Go to Anomalies**. **Tip** : If you have access to multiple billing accounts and you aren't sure which Cloud Billing to select, you can use the **project selector** to choose the project for which you want to view cost anomalies. For the selected project, its linked billing account is automatically selected for you, or you can select a different billing account before continuing to the anomalies page.
  3. The **Anomalies** page opens for the selected billing account. The Anomalies page displays anomalies for one project at a time. With multi-project access to Cloud Billing accounts, the active project appears in the project selector at the top of the Anomalies page.
  4. If you want to view cost anomalies for a different project, use the project selector on the Anomalies page to choose a different project.

![Example of the anomalies page, showing the project picker available for users with multi-project access to the billing account.](https://docs.cloud.google.com/static/billing/docs/images/anomalies-multi-project.png)Click image to view an enlarged version. ![](https://docs.cloud.google.com/static/billing/docs/images/anomalies-multi-project.png) |  **Important** : If you only have project permissions, but don't have any permissions on your project's Cloud Billing account, you'll need to select your project _before_ you navigate to the Billing section.

  1. Sign in to the Google Cloud console. [ Open Google Cloud console](https://console.cloud.google.com/projectselector2/home/dashboard?project=_)
  2. Select the project that you want to view anomalies for. This project must be one that you own.
  3. Next, **navigate to Billing** : Open the Google Cloud console **Navigation menu** menu, and then select **Billing**. If you're prompted to choose which billing account you want to view and manage, click **Go to linked billing account** to view the billing account that's linked to your selected project. The Billing **Reports** page opens for the selected billing account.
  4. In the **Cost management** section of the **Billing navigation** menu, select **Anomalies**.

As a project user accessing the Cloud Billing account using _project-level permissions only_ , you can see costs anomalies for a _single_ project — the project that you selected in the Google Cloud console _before_ you accessed the Billing section. To view cost anomalies for a different project, exit Billing, repeat the steps above to select a project on the Google Cloud console dashboard, and then navigate back to Billing.  
  
## View early anomalies for AI workloads (preview)

The early signals feature helps you identify cost anomalies for AI workloads daily to support cost control and help detect potential fraud or system abuse. This feature is available for the Gemini API and Vertex AI services.

Early anomalies use near real-time cost estimates. Estimated costs are not finalized and don't appear on [cost reports](https://docs.cloud.google.com/billing/docs/how-to/reports). The system delivers alerts with an expected latency of 20 to 40 minutes from the time of usage.

In the Google Cloud console, early signal alerts appear exclusively on the **By service (Early signals)** tab. Broad, project-level anomalies continue to be reported using standard next-day channels.

To view early anomalies, follow these steps:

  1. Following the procedure that fits your level of access to Cloud Billing accounts, access the **Anomalies** dashboard in the **Billing** section of the Google Cloud console.
  2. Click the **By service (Early signals)** tab.



You must have the same permissions required to view standard project-level anomalies. For more information, see Permissions required for this task.

## Analyze root causes of anomalies

Each anomaly includes a granular **Root cause analysis** panel that helps pinpoint the source of the cost spike. To open the panel and view the details of an anomaly, click the anomaly date.

For standard anomalies, the **Root cause analysis** panel shows the top services, regions, and SKUs that contributed to the spike in spend. If the anomaly is equally spread across services, regions, or SKUs, you won't see any top contributors in the **Root cause analysis** panel.

For early anomalies, the **Root cause analysis** panel displays the project details and the top three SKUs driving the spike. The panel also shows that the costs are estimated and not finalized. Feedback options are hidden for early anomalies.

Click any of the links in the **Root cause analysis** panel to open a Billing Report that's filtered by the project you're viewing, and also by service, region, or SKU, depending on the link you select.

In the **Root cause analysis** panel, you can also share feedback about the anomaly to help optimize anomaly detection.

## Manage anomalies

Billing Account Administrators can set threshold and notification preferences for all anomalies. On the **Anomalies** page, click settings **Manage anomalies** to customize thresholds and notifications.

### Manage anomaly thresholds

**Note** : User-configured thresholds apply only to standard project-level anomalies. Thresholds for early anomalies are system-defined and can't be configured.

A cost impact and deviation percentage threshold will automatically be set based on your usage patterns.

To focus on cost anomalies that are significant to you, you can configure a different cost impact and deviation percentage anomaly threshold. The threshold amount filters your view to show only anomalies exceeding a certain cost deviation (for example, $200) and deviation percentage (for example, 20%). If you set up notifications, you will also receive alerts when a cost anomaly crosses the defined threshold values.

The cost impact threshold value is in your billing account's local currency and can only contain positive numeric values, including up to two decimal places. You can't use negative or non-numeric values.

For users with billing-account-level access, the threshold amount automatically sets a `Cost impact` and `Deviation percentage` filter on the anomalies list, showing only anomalies that cross these thresholds. You can remove both filters to see all anomalies, but the filter is reapplied the next time you visit the page.

Users with project-level access can view these detected anomalies set by the Billing Account Administrator for their project. However, only users with the [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin) (roles/billing.admin) role can update the notification thresholds.

**Note:** The threshold value applies to all notifications (email and Pub/Sub), regardless of the IAM roles of the recipients.

### Manage notifications

On the **Manage anomalies** page, you can set how you want to be notified about anomalies. You can configure email or [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/publish-receive-messages-console) notifications. Notification settings apply to both standard and early anomalies.

For standard anomalies, notifications are triggered when they exceed your configured cost impact and percent of deviation thresholds. Early anomalies use system-defined thresholds.

By default, Cloud Billing admins receive email notifications for every individual anomaly. You can change this setting in the **Notifications** section on the **Manage anomalies** page.

You can change your notification settings at any time. Notification configurations apply to all projects on your billing account. You can't set up notifications for a subset of projects.

#### Set up email notifications

To set up email notifications, complete the following steps:

  1. From the **Anomalies** dashboard, click settings **Manage anomalies**.
  2. If you haven't already, enter an **Anomaly threshold** value for **Cost impact** and **Deviation %**. This amount is the threshold value that triggers notifications.
  3. In the **Email notifications** section, set the email recipients (**Billing admins** , **Essential contacts** , or **Project owners**) and the frequency of emails for each recipient (every **Individual anomaly** or a **Daily summary**).

     * For **Essential contacts** , selecting **Individual anomaly** sends notifications to the [designated Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts), in the _Billing_ category, for the _project_.
     * For **Essential contacts** , selecting **Daily summary** sends notifications to the [designated Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts), in the _Billing_ category, for the _organization_.
     * **Project owners** can receive notifications only for individual anomalies on projects that they own.
     1. Click **Save**.



#### Email notifications behavior for early anomalies

If you configure email notifications, the system handles early anomalies as follows:

  * **Individual alerts** : You receive separate emails for project-level and service-level anomalies.
  * **Daily summaries** : The daily summary email aggregates both project-level and service-level anomalies into a single daily digest email.



#### Set up Pub/Sub notifications

To set up Pub/Sub notifications for anomalies, complete the steps in [Set up programmatic notifications](https://docs.cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications).

**Note:** When you configure Pub/Sub notifications, the project hosting the Pub/Sub topic must allow resource sharing with external domains. If your organization enforces the `iam.allowedPolicyMemberDomains` constraint, then you must exempt the project containing the topic from the policy. If you don't exempt the project, then you might encounter an error because Cloud Billing cannot publish to the topic.

For details about the JSON schema of Pub/Sub notifications for anomalies, see [Notification format](https://docs.cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications#anomaly-notifications_2).

## Optimize anomaly detection

**Note** : You can only submit feedback for standard anomalies. Feedback options aren't available for early anomalies.

The AI-powered anomaly detection algorithm constantly learns and improves, but your feedback helps it adapt faster to your business needs. To provide feedback, complete the following steps:

  1. In the list of anomalies, click the date of an anomaly to open its **Root cause analysis** panel.
  2. For **Is this an anomaly?** , select one of the following options: 
     1. **Yes, it's an unexpected cost increase** : Select this option if the anomaly is unexpected and an unintended cost increase.
     2. **Yes, but it's an expected cost increase** : Select this option if the anomaly is an expected cost increase to meet your business needs. To help Google's anomaly detection models adapt, you can provide more context around the specific business reason for the anomaly (for example, if you have active migrations underway, are using new Google Cloud resources, or if the cost increase is temporary).
     3. **No, the cost impact is insignificant** : Select this option if the anomaly has a cost impact that you don't consider to be significant.
  3. Click **Submit feedback**.

**Note:** To submit feedback, you must have [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin) `(roles/billing.admin)` role on the Cloud Billing account.



After you submit your feedback, it's recorded with a timestamp.

To change previously submitted feedback, complete the following steps:

  1. Open the **Root cause analysis** panel.
  2. Change your selection using the provided options.
  3. Click **Submit feedback**.



## Related topics

  * [Set up programmatic notifications](https://docs.cloud.google.com/billing/docs/how-to/budgets-programmatic-notifications)
  * [Analyze billing data and cost trends with Reports](https://docs.cloud.google.com/billing/docs/how-to/reports)
  * [Create, edit, or delete budgets and budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
