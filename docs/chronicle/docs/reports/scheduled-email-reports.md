---
url: https://docs.cloud.google.com/chronicle/docs/reports/scheduled-email-reports/
title: Configure scheduled reports \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:00.752120+00:00
---

# Configure scheduled reports  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/scheduled-email-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure scheduled reports

Supported in:

Google SecOps 

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

This document describes the Google Security Operations scheduled reports feature, which lets you create, manage, and distribute reports generated from your existing Google SecOps dashboards. You can use scheduled reports to share key security insights by sending them as recurring email reports to stakeholders.

The scheduled reports feature supports several common use cases:

  * Share key security insights with your organization or customers.
  * Share a one-time snapshot of a dashboard with a manager after an investigation.
  * Send an email to your team with a recurring periodic summary of key security metrics.



## Key features

  * **Flexible scheduling** : Define the delivery frequency (hourly, daily, weekly, and monthly) and the time zone. You can also deliver a single report immediately.
  * **Multiple report formats** : PDF, PNG, and CSV.
  * **Multiple delivery methods** : 
    * **Email attachments** : Sends reports as file attachments directly to recipient inboxes.
    * **Secure GCS delivery** : Uploads reports to a customer-owned Cloud Storage bucket within your Google project and sends email notifications with a secure link to the reports to recipients with the necessary permissions.



## Before you begin

This section contains requirements and prerequisites for the Google Security Operations scheduled reports feature.

### Permissions for view, create, and modify

Role-based access control (RBAC) permissions determine who can view, create, and modify scheduled reports. 

When you create a report, it runs with your RBAC permissions.

The following table lists the permissions required for email reports:

IAM permission | Purpose  
---|---  
`chronicle.googleapis.com/dashboardScheduledReports.get` | View reports.  
`chronicle.googleapis.com/dashboardScheduledReports.list` | View the list of reports.  
`chronicle.googleapis.com/dashboardScheduledReports.fetchHistory` | View the schedule history of reports.  
`chronicle.googleapis.com/dashboardScheduledReports.create` | Create new reports.  
`chronicle.googleapis.com/dashboardScheduledReports.update` | Update reports.  
`chronicle.googleapis.com/dashboardScheduledReports.delete` | Delete reports.  
`chronicle.googleapis.com/dashboardScheduledReports.duplicate` | Make a copy of reports.  
`chronicle.googleapis.com/dashboardScheduledReports.trigger` | Generate reports.  
  
### Allowlist for target email domains

A tenant administrator configures an allowlist of the external email domains to which Google SecOps can send reports. This process helps ensure that Google SecOps sends reports only to approved domains.

To configure the allowlist of external email domains, do the following:

  1. Go to **Settings** > **Email Settings**. The **Email Domains** dialog opens and displays a table with the following columns:

     * **Domain** : The external email domains to which Google SecOps can send reports—that is, either email messages containing a secure link to reports or email messages with a report as an attachment.
     * **Date added** : The date and time that the domain was added to the list.
     * **Added by** : The user who added the domain to the list
     * **Action** : Delete the domain by clicking the trash-can icon 
  2. Click **Add New Domain**. The **Allowlist new domain** dialog opens.

  3. In the **Domain** field, enter the domain and click **Save**. The dialog closes and the domain is displayed in the table.

  4. Repeat the previous two steps as necessary.




## Create a scheduled report

Each Google SecOps tenant can have a maximum of 50 scheduled reports configured on it. 

**Note:** After you create a scheduled report, you can perform various actions on it, for example, to deliver the report immediately. For more information, see Manage existing reports.

To create a scheduled report, complete the following steps:

  1. Go to the **Reports** page and click **Create New Report**. The **Creating new report** dialog opens.

  2. Do the following:

     * In the **Details** panel, do the following:

       * In the **Report Name** box, enter a unique name. 
       * Optional: In the **Report Description** box, enter a description.
     * In the **Data** panel, do the following:

       * From the **Dashboard** list, select the dashboard whose contents the report contains. 
       * Select or clear the **Global Scopes** checkbox. When the **Global Scope** checkbox is selected, the **Data Scopes** list is unavailable, and the report includes all data without any [scope](https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-users#create-manage-scopes)-based restrictions.
       * If the **Global Scope** checkbox is cleared, from the **Data Scopes** list, select at least one RBAC [scope](https://docs.cloud.google.com/chronicle/docs/administration/configure-datarbac-users#create-manage-scopes).

At the bottom of the **Data** panel, the **Filters** box displays the filters and time overrides applicable to the dashboard.

     * In the **Delivery** panel, in the **Schedule Delivery** section, select one of the following **Schedule Type** options:

       * **Basic** : The schedule runs according to the specified **Time** , **Days** , **Months** , and **Timezone** parameters. The sub-parameters and options depend on your configuration. For example, after you choose the **Time** parameter option, **Run at specific time** or **Repeat hourly** , the corresponding, additional parameters change accordingly. 

At the bottom of the **Basic** schedule parameters, the **Executions according to selection** box displays the expected generation times of the first and second reports. 

       * **Advanced** : The schedule runs according to the CRON expression in the **CRON** box and the time zone selected from the **Timezone** list.

At the bottom of the **Advanced** schedule parameters, the **CRON translation** box displays the schedule in human-readable form, for example, `1:35PM, every day`. 

     * In the **Delivery** panel, in the **Email Delivery** section, select one of the following options:

       * **Upload report in GCS and send link in email (More Secured)** : Google SecOps uploads the report to a Cloud Storage bucket within your Google project and sends links over email to recipients with the necessary permissions. Clicking the link allows the recipient to download the report file directly from the Cloud Storage bucket.

If any report with this option has ever been saved in your system, the bucket identifier is displayed (for example, `dsr-999123456789-a1b2c3d4-e5f6-4a5b-8c9d-0123456789ab`).

If this is the first report in your system with this option selected, do the following:

         1. Click **Provision GCS Bucket**. The **GCS Bucket Provision** dialog opens.
         2. Read the text and click **Opt-In & Continue**.
         3. Grant the necessary read permissions to the bucket for users who receive the links to the report.
       * **Send report as file attachments in email** : Google SecOps sends the report over email as a file attachment to the specified recipients. This option is less secure than the **Upload report in GCS...** option.

     * In the **Delivery** panel, in the **Email Delivery** section, configure the following parameters to define how Google SecOps sends email messages for the report:

       * **Subject of Email** : Modify the default text as necessary.
       * **Body of Email** : Modify the default text as necessary.
       * **Recipients** : Enter an email address and click **Add**. The email address is displayed in the **Email IDs of recipients** box. Make sure that the recipient domain is in the allowlist.

The maximum file size for a report is 10 MB.

     * In the **Format** panel, choose the format of the report:

       * **CSV** : Best for printable, read-only versions of the dashboard.
       * **PDF** : Image format suitable for embedding in presentations.
       * **PNG** : Raw data exports from dashboard charts and tables.
  3. Click **Save** to activate the scheduled report.




## Manage existing reports

The **Reports** page displays basic details of all reports that you have access to, letting you monitor the status (Active or Inactive), last run time, last modified time, last run status (Success, Ongoing, or Error).

To perform an action on an existing report, do the following:

  1. Go to the **Reports** page.
  2. Hover over the relevant row and click more_vert **More**. 
  3. Select an action from the following table. Some actions require you to save changes or confirm the action.

Action | Option | Description  
---|---|---  
View details and history | **View Details and History** | Shows the run history and any delivery failure messages.  
Edit a report | **Edit Configuration** | Opens the **Editing report** dialog, where you can modify the settings. For information about the report settings, see Create a scheduled report.  
Deliver the report immediately | **Deliver Now** | Sends the report immediately.  
Pin a report | **Pin** | Keeps the report at the top of the **Reports** page.  
Copy a report | **Duplicate** | Creates a duplicate copy of the report.  
Delete a report | **Delete** | Permanently removes the report after you confirm the action.  
  
## Grant read permissions to the bucket with the report

The first time a report is created with the GCS-delivery option (the **Upload report in GCS and send link in email (More Secured)** option), you must complete a one-time provisioning workflow. This process creates the Cloud Storage bucket within your Bring your own project (BYOP) project, which is linked to your Google Cloud billing account.

After this initial setup, subsequent report configurations will automatically use the existing bucket.

Once the bucket is successfully provisioned, you are responsible for managing access. You must manually grant read access to the bucket for all email recipients who are specified in the configuration of the report. Depending on your security requirements, you can choose between bucket-level or folder-level access.

**Note:** Storing reports on a Cloud Storage bucket in a Bring your own project (BYOP) project will incur additional storage costs.

Do the following to grant the necessary read permissions to the bucket for users who receive the Cloud Storage links:

  1. In the Google Google Cloud console, go to the **Cloud Storage Buckets** page.
  2. In the list of buckets, click the name of the bucket, which starts with the `dsr-` prefix (for example, `dsr-999123456789-a1b2c3d4-e5f6-4a5b-8c9d-0123456789ab`).
  3. Choose an **Access Level**.
  4. Choose the option that best fits your organizational needs:

     * **Bucket-level access** : Use this for the recipients to have access to all reports delivered to the bucket. Using this option is more convenient but grants recipients wider access. To configure this option, do the following:

       1. Select the **Permissions** tab near the top of the page.
       2. Click **Grant Access**.
       3. In the **New principals** field, enter the recipient's identifier (for example, `user:name@example.com` or `serviceAccount:my-service-account@project-id.iam.gserviceaccount.com`).
       4. In the **Assign roles** section, do one of the following:

          * Select **Storage Object Viewer**. (To find the option quickly, you can type `Storage Object Viewer` in the filter box.)
          * For least privilege access at the bucket level, assign a custom role containing only the `storage.objects.get` permission.
       5. Click **Save**.

     * **Folder-level access** : Google SecOps creates a unique folder for each scheduled report. Use this to ensure that recipients only access specific report data. To configure this option, do the following:

       1. In the bucket's object list, locate the folder corresponding to the specific scheduled report.
       2. Click the checkbox next to the folder name.
       3. In the right-hand information panel (click **Show Info Panel** if not visible), select the **Permissions** tab.
       4. Click **Grant Access**.
       5. In the **New principals** field, enter the recipient's identifier (for example, `user:name@example.com` or `serviceAccount:my-service-account@project-id.iam.gserviceaccount.com`).
       6. In the **Assign roles** section, do one of the following:

          * Select **Storage Object Viewer**. (To find the option quickly, you can type `Storage Object Viewer` in the filter box.)
          * For least privilege access at the folder level, assign a custom role containing only the `storage.objects.get` permission.
       7. Click **Save**.




## Data encryption and security compliance

When Google SecOps generates and delivers scheduled reports, it protects your data with standard Google Cloud storage and transmission security controls:

  * **Direct Email Delivery** : Handled using the **Google Message Router (GMR)** service. 
    * **At rest** : All data stored by Google is encrypted at the storage layer using the **Advanced Encryption Standard (AES-256)** algorithm.
    * **In transit** : GMR utilizes **Transport Layer Security (TLS)** to encrypt email traffic and attachments.
  * **GCS Buckets** : For reports delivered to Cloud Storage buckets, Customer-Managed Encryption Keys (CMEK) customers can encrypt the bucket with their own key, ensuring the report attachments are stored with that encryption.



To review detailed compliance information, see the [Google Cloud Compliance Reports Manager](https://cloud.google.com/security/compliance/compliance-reports-manager).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
