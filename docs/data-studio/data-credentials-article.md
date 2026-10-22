---
url: https://docs.cloud.google.com/data-studio/data-credentials-article/
title: Data credentials \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:25.939157+00:00
---

# Data credentials  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/data-credentials-article/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Data credentials Stay organized with collections  Save and categorize content based on your preferences. 

_Credentials_ determine who can see the data that is provided by a data source. Data Studio uses three types of data credentials:

  * _Owner's Credentials_ let other users access the data by using the credential owner's authorization. Data sources that use this credential type have a credential owner who may be be a different user than the data source owner. The credential owner's data credentials are used to determine access to the data source's underlying data.
  * _Viewer's Credentials_ rely on each individual report viewer's credentials to access the data.
  * _Service Account Credentials_ rely on a special type of Google Account that represents a non-human user, which can be authenticated and authorized to access data.



## Set credentials for a data source

You can set data credentials for Data Studio reports and for [Looker reports](https://docs.cloud.google.com/looker/docs/glossary#reports).

  1. Add data to your report.
  2. After you select a data source but before you click **Add** , click **Data credentials**.
  3. Select the credential type. If a data source supports Owner's Credentials, then **Owner's Credentials** is selected and you are the data credential owner by default.
  4. Click **Add**.



You can also update the data credentials as needed after creating the data source.

## Types of credentials

Click the headers of the following sections to learn more about each type of data credential.

### Owner's Credentials

Select this option if you want to let other people view or create reports that use this data without requiring them to have their own access to the dataset. Owner's Credentials uses the credentials of a specific person to authorize access to the dataset. By default, you are the credential owner if you created the data source, but another editor of the data source can become the credential owner.

Owner's Credentials may not work correctly when you query BigQuery external tables that are linked to Google Drive, such as Google Sheets. We recommend using Service Account Credentials in these scenarios to avoid potential access issues. To allow access, share the underlying Google Sheets with the Service Account email address as a Viewer, and ensure that the Data Studio Service Agent has the Service Account Token Creator role.

**Note:** Using the Owner's Credentials option does not grant other people the right to access the dataset directly. The Owner's Credentials are never displayed or transmitted "in the clear."

#### Example

You've created a Google Analytics data source that connects to your company's All Website Traffic view. You selected **Owner's Credentials** in the data source **Configuration** tab. You've shared this data source with Nikhil and Betsy. Nikhil has his own Google Analytics login and permission to access the All Website Traffic view. Betsy does not have access to this view. However, both Nikhil and Betsy can view reports based on this data source, because it uses your credentials, not theirs.

### Viewer's Credentials

This option requires each user of the data source (or reports that are built using the data source) to provide their own credentials to access the dataset. If they don't have access to the dataset, they won't be able to view the data in reports or to edit the data source fields.

When a viewer runs a report that is based on a BigQuery data source, Data Studio displays a dialog that asks for consent to collect their email address as part of [audit logging](https://docs.cloud.google.com/bigquery/docs/reference/auditlogs). Users can deny this consent when prompted, or revoke email logging at any time.

**Warning:** When you enable Viewer's Credentials for a data source, Data Studio won't render [hyperlinks](https://docs.cloud.google.com/data-studio/hyperlink) or [images](https://docs.cloud.google.com/data-studio/image) in dimensions from that data source.

#### Example

It's the same scenario as described previously in the "Owner's Credentials" section, only this time you've selected the **Viewer's Credentials** option. You've shared a report that was built using this data source with the same people, but only Nikhil, who has his own credentials to the All Website Traffic view in Google Analytics, will be able to see the data. When Betsy views the report, she won't see this data.

### Service Account Credentials

Instead of delegating access using the **Owner's Credentials** option, or requiring individual report viewers to have access to the data using the **Viewer's Credentials** option, Data Studio can use a service account to authenticate and get authorization to access your data. 

You can use Service Account Credentials as a workaround if your organization restricts the use of Owner's Credentials through Google Workspace policy, which can prevent you from sharing reports that are based on static files like CSV uploads. To share such reports, upload the static file to a BigQuery table, create a Service Account with access to that table, and then connect Data Studio to the BigQuery table by using Service Account Credentials.

Note the following limitations and requirements:

  * The **Service Account Credentials** option is available only for Google Workspace or Cloud Identity managed organizations.
  * Service Account Credentials are available only for BigQuery data sources.
  * Service accounts must be set up by a Google Workspace or Cloud Identity administrator. If that's you, [learn how to set up a service account](https://docs.cloud.google.com/data-studio/set-up-a-google-cloud-service-account).



If a service account has already been set up, you can use it to connect a data source to BigQuery data by providing the service account's email address in the data source credentials dialog. Follow these steps:

  1. [Create or edit a BigQuery data source](https://docs.cloud.google.com/data-studio/connect-to-google-bigquery).
  2. In the toolbar, click **Data Credentials**.
  3. Select **Service Account Credentials**.
  4. Enter your **Service account** email address in the box.
  5. Click **Update**.



#### How to find your service account

The simplest way to know which service account to use is to ask your Google Cloud administrator. Your organization may have multiple service accounts set up, so it's important to use the correct one.

If you have access to the Google Cloud console, you can use it to list the available service accounts in one of two ways:

**Use Google Cloud console**

  1. Navigate to the Google [Cloud Platform > IAM & Admin > Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) page.
  2. Select a project, if necessary.
  3. In the **Service accounts for project** page, locate the service account that Data Studio will use to access your BigQuery data.
  4. Copy the email address for that account.



**Use Cloud shell**

  1. [Open the Cloud shell](https://console.cloud.google.com/home/dashboard?cloudShell=true).
  2. Select a project, if necessary.
  3. To list the service accounts to which you have access, run the [Google Cloud CLI iam service-accounts list](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/list) command:

`gcloud iam service-accounts list`




## Troubleshoot credential errors

If you see an error in the credentials dialog or in your reports, check the following troubleshooting steps.

### Incomplete or incorrect service account setup

If you see an error while trying to use a service account, it is most likely caused by an incomplete or incorrect service account setup. For possible solutions, see [Set up a Google Cloud service account for Data Studio](https://docs.cloud.google.com/data-studio/set-up-a-google-cloud-service-account).

### Credential errors caused by Context-Aware Access

When a user's Google Workspace account is subject to Context-Aware Access (CAA) restrictions, such as IP address allowlists, requests from Data Studio to data sources like BigQuery or Google Sheets might be blocked. This can result in a "Credential settings are incorrect" error or a blank interface when you connect to Google Sheets.

To resolve this issue, a Google Workspace administrator must exempt Data Studio from Context-Aware Access enforcement:

  1. In the Google Admin console, go to **Security** > **Access and data control** > **API controls**.
  2. In the **App access control** section, add Data Studio and configure it to be exempt from Context-Aware Access enforcement.
  3. Go to **Security** > **Access and data control** > **Context-Aware Access**.
  4. Select the access level that is blocking access.
  5. Select the **Enable the CAA for APIs allowlist** checkbox.



For more information about Context-Aware Access, see [Protect your business with Context-Aware Access](https://support.google.com/a/answer/9275380).

## Update credentials

Editors of a data source can update its credentials:

  * Editors can change the type of credentials that are used by the data source.
  * Editors can become the new credential owner.



To update a data source's credentials, follow these steps:

  1. [Edit the data source](https://docs.cloud.google.com/data-studio/edit-a-data-source-article).
  2. At the top of the screen, click **Data credentials**.
  3. Select the new credential type.



To become a data source's credential owner, follow these steps:

  1. [Edit the data source](https://docs.cloud.google.com/data-studio/edit-a-data-source-article).
  2. At the top of the screen, click **Data credentials**.
  3. Select **Make me the owner**.

**Important:** Changing data source credentials may cause people who don't have access to the underlying dataset to see errors in reports.

## Revoke your data credentials

Data sources that use your credentials continue to retrieve data even if you can no longer edit the data source. Revoking your credentials stops the data source from accessing the data "as you."

For example, if you create a data source for your company and then leave that company, you can stop that data source from retrieving data. You can do this for an individual data source, or you can revoke your credentials from all data sources to which you no longer have access.

### Revoke your credentials from a single data source

  1. [Sign in to Data Studio](https://datastudio.google.com).
  2. At the top, select **Data Sources**.
  3. Browse or search for the file that you want to stop sharing; then, on the right, click **More** ![More options.](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png).
  4. Click **Revoke data source**.



### Revoke your credentials from all data that sources you no longer own

  1. [Sign in to Data Studio](https://datastudio.google.com).
  2. At the top right, click **Settings** ![Settings](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--settings.png).
  3. Select **Revoke Data Source**.
  4. A list of all data sources that you created but no longer own appears.
  5. Click **Revoke all**.



### Revoke email logging

To stop providing your email address to reports that request it, you can revoke your consent by following these steps:

  1. [Sign in to Data Studio](https://datastudio.google.com).
  2. In the upper right, click **Settings** ![Settings.](https://docs.cloud.google.com/static/data-studio/images/icsettingsgrey6002xweb48dp-2019-12-03.png).
  3. On the left, select **Revoke Consent**.
  4. Under **Revoke audit logging consent** , click **Revoke all**.



After you revoke your consent, you'll need to grant it again before you can see personalized data in reports.

## Data credential administration

Data Studio administrators can control whether users in their organization can set data credentials for data sources that they have permission to edit. [Learn more about managing data credentials for your organization](https://support.google.com/a/answer/14340218).

## Related resources

  * [Ways to share your reports](https://docs.cloud.google.com/data-studio/ways-to-share-your-reports)
  * [Set up a Google Cloud service account for Data Studio](https://docs.cloud.google.com/data-studio/set-up-a-google-cloud-service-account)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
