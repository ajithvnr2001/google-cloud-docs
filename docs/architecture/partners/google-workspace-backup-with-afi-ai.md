---
url: https://docs.cloud.google.com/architecture/partners/google-workspace-backup-with-afi-ai/
title: Google Workspace Backup with Afi.ai \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:47.946274+00:00
---

# Google Workspace Backup with Afi.ai  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/partners/google-workspace-backup-with-afi-ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Google Workspace Backup with Afi.ai Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-04-01 UTC

By [Afi.ai](https://afi.ai/google-workspace-backup)

This document describes how to set up an automated Google Workspace backup using Afi.ai.

In order to install the application in your Google Workspace domain, system administrators must have domain administrator rights. The initial setup takes approximately 5 minutes; up to 24 hours might be required in order for all settings to take full effect.

You can use any Super Admin account from your Google Workspace to install the Afi Google Workspace Backup application. Afi continues to work even if the Super Admin account that you used for the install is deleted from your Google Workspace account. All Super Admin accounts are granted the same unlimited access to the Afi application by default, but you can configure and limit their access. For more information, see Backup access control.

## Objectives

  * Install and configure [Afi Google Workspace Backup](https://afi.ai/google-workspace-backup).
  * Configure Afi data protection settings.
  * Preview, export, and recover data using Afi.
  * Add your Afi customer account to the Afi partner management portal.



## Afi Google Workspace Backup and recovery options

The Afi Google Workspace Backup tools enable versioning of Google Docs files, [recovery of permanently deleted items](https://support.google.com/a/answer/6052340) through the Admin console, and unlimited data retention as part of the [Google Vault](https://support.google.com/a/answer/2462365) data retention and eDiscovery solution.

With the Afi Google Workspace Backup policy, you typically use third-party software in addition to the native Google capabilities in order to extend the timeframe and scope of protected Google Workspace data, and to automate the recovery process.

| Google Workspace Admin console | Google Vault | Third-party Google Workspace backup  
---|---|---|---  
Permanently deleted data | Data deleted within 25 days can be restored. | Google Vault doesn't restore data. However, administrators can access and download user-deleted data that's protected by Vault retention rules for existing, licensed user accounts. | Yes, infinite data retention.  
Configurable retention rules.  
Deletion of user account | Removes retained data in 20 days after account deletion. | Removes retained data. | Data is retained.  
Folder structure | Yes. | No. | Yes.  
Gmail label structure | Yes. | No. | Yes.  
Metadata, rights, and permissions | Authorship and created/modified dates are restored. Share permissions are not preserved. | Export functionality allows downloading files with authorship and created/modified dates. Sharing permissions are not preserved. | Document ID, authorship, created/modified dates are restored.  
Sharing permissions are restored.  
Individual emails and files | No, only full Google Workspace account. | Can be retained and downloaded using export functionality. | Yes.  
Email drafts and trash | Cannot be restored. | Can be retained and downloaded using export functionality. | Yes.  
Full user account | Only the last state and within 20 days after deletion can be restored. | No. | Yes, point in time with infinite versions.  
Contacts | Only the full contact list within 30 days after deletion can be restored.  | No. | Yes, granular Google Workspace Contacts backup, offline export and recovery.  
Calendar events | Events deleted within the last 30 days can be restored. | No. | Yes, granular Google Workspace Calendar backup, offline export, and recovery.  
Apps Scripts and Jamboard data | No. | No. | Yes.  
Point-in-time recovery | No, only deleted files within the selected period. | Partial data export for the selected period is available, no restore back to Google Workspace. | Yes.  
Real-time data preview | No. | Yes. | Yes.  
Admin involvement | Data restore can only be performed by a Google Workspace administrator. | Export and data download can only be performed by a Google Workspace administrator. | Self-service recovery is available for end users.  
Shared Drive self-service recovery is available for end users.  
  
## Afi Google Workspace Backup capabilities

As one of the third-party Google Workspace Backup solutions, Afi enables automated [Google Workspace data backup](https://support.afi.ai/hc/en-us/articles/5678240535442-supported-workloads-in-the-afi-google-workspace-g-suite-backup) to a secondary cloud storage location. In addition to doing scheduled backups, Afi uses AI technology to detect security events—like ransomware attacks, mass data changes, deleting data, and others—perform preemptive backups, and accelerate recovery.

### Cloud Storage backup

Afi Google Workspace Backup data is stored in the Cloud Storage location that you select during initial setup. The data is encrypted and stored in an immutable format. Any deletions, modifications, or other operations in the Google Workspace domain produce new versions of the data, but have no impact on the old recovery points.

Afi also offers a Bring Your Own Encryption capability that supports Cloud Key Management Service and enables customers to control and maintain the encryption keys they use to encrypt backup data.

### Artificial intelligence backup engine

The artificial intelligence (AI) backup engine monitors Google Workspace data changes and external data sources that include weather forecasts and major antivirus RSS feeds, to detect high-risk events (for example, massive changes to Google Drive files or outbreaks of new types of malware). The AI backup engine activates the protection by doing the following:

  * Performing high-frequency shared drives and Google Workspace user data backups to maximize the number of recovery points before the potential event.
  * Auto-labeling the recovery points. This feature analyzes the changes between the versions and helps you recover to the latest version that is unaffected by a malware attack or by data corruption.



### Backup access control

Afi relies on Identity Platform to authenticate administrators and users. Afi also implements role-based access control in order to limit access to backup contents within the application. The Afi application supports very granular access configuration via access groups:

  * **Google Workspace Super Admin:** Assigned by default to all Google Workspace Super Admin users in Google Workspace domains, granting them the right to view and export the data of all domain users. You can configure Google Workspace Super Admin access to user data by limiting access to user backup data within Afi. You can also disable access to the Afi application altogether by [creating a support ticket with the Afi help desk](https://support.afi.ai/hc/en-us/requests/new).
  * **Backup Operator:** Assigned to selected users to let them perform backup and restore operations for other users, with custom configurable data preview, download, and export permissions.
  * **Self Service:** Assigned to users who need to perform a limited set of data recovery and export operations for their own accounts.
  * **Custom Access Group:** Defines users who will have access. Uses a set of allowed operations and data scope that can be as granular as a single user or a shared drive backup.



The following screenshot shows the **Access Group** settings.

![Roles and self-service settings.](https://docs.cloud.google.com/static/architecture/images/partners/afi_access_group.png)

## Setting up Afi Google Workspace Backup

### Install Google Cloud Marketplace

  1. Sign in to the Google Admin panel as a Super Admin and open the Afi [application](https://workspace.google.com/marketplace/app/afi_g_suite_backup/429019162995) in Cloud Marketplace.

![Cloud Marketplace.](https://docs.cloud.google.com/static/architecture/images/partners/afi_install.png)

  2. Click **Admin install** (the **Individual install** option is not supported). You can install the application to your entire domain or limit the installation to specific organizational units (OUs).




### Initial configuration and storage selection

  1. Go to <https://app.afi.ai/> to access the application.
  2. Use your Google Workspace administrator account to sign in. Upon first signing in, you need to set the following:

     * **Region to store backup data:** When selecting a storage region, consider your data residency requirements. You cannot change your selection later.

     * **Time zone:** Affects the timing of automated backups.

![Afi welcome screen.](https://docs.cloud.google.com/static/architecture/images/partners/afi_install_region.png)

After you confirm the settings, Afi will initiate a discovery process for the whole domain. For large domains with more than 5,000 users, this process might take up to a few minutes.




#### Google Cloud storage options

By default, you can select one of the [Google Cloud regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) during the initial configuration. There are no additional storage costs because all storage costs are already included in Afi subscription fees. The default regions are:

  * `eu-west4` (Eemshaven, Netherlands)
  * `eu-west2` (London, England)
  * `us-central1` (Council Bluffs, Iowa, USA)
  * `northamerica-northeast1` (Montreal, Canada)
  * `australia-southeast1` (Sydney, Australia)



Afi supports multi-region backup storage. You can choose to keep different users and shared drives backups in different geographical regions to comply with local data residency laws. For more information, see [Multi-geo support in Afi Backup](https://support.afi.ai/hc/en-us/articles/4411298074898-multi-geo-support-in-afi-backup).

## Backup and recovery operations

### Customize protection policies

Afi protection is based on Service Level Agreement (SLA) policies, which define how often backups are performed and what Google Workspace applications are protected. By default, Afi provides policies for user accounts and shared drives protection:

  * Gold (backups occur three times a day, all applications)
  * Sliver (backups occur twice a day, all applications)
  * Bronze (backups occur once a day–excluding weekends–all applications)
  * Manual (on-demand backups, no automated backups, all applications)



End users can modify pre-set policies—as well as create additional policies (with required settings)—by clicking **Add new SLA**.

![Afi service level agreement screen.](https://docs.cloud.google.com/static/architecture/images/partners/afi_sla.png)

Each SLA policy can be customized to include the selected applications (or to exclude the unselected applications).

  1. Go to the **Configuration** screen and make sure the **SLA** tab is selected.
  2. Select or clear the required applications to include or exclude in the SLA.

![Selecting or clearing required applications in the SLA tab.](https://docs.cloud.google.com/static/architecture/images/partners/afi_edit_sla.png)

The **Computers** checkbox refers to the data uploaded to Google Workspace by the Google Backup and Sync application. Users can configure that application to sync their computers to their Google Drives.




## Retention and archiving policies

You can configure **Data retention and data archiving policies** as a part of an SLA.

**Retention policy:** A set of rules that defines how long different kinds of data should be stored. These rules also define how and when data should be cleaned up after the retention period ends.

Retention policies help organizations to accomplish different goals including:

  * Complying with various legal or other requirements for data storage (HIPAA, FINRA, SOX)
  * Removing obsolete or stale data that occupies significant storage space and makes navigation across company data unnecessarily complex



To support these requirements, Afi Backup offers item-level and backup version retention policies that clean up data after it reaches the age defined by the policy. For more information about how to configure retention rules, see [Data retention policies in Afi Backup](https://support.afi.ai/hc/en-us/articles/360021017079-data-retention-policies-in-afi-backup).

**Archiving policy:** A set of rules used to configure how long backup data is stored after the corresponding user or other resource (drive, site, and so on) is deleted or becomes inactive in Google Workspace. By default, Afi will keep archived data indefinitely. For more information about Afi's archiving policies, see [Retention polices for archived backups.](https://support.afi.ai/hc/en-us/articles/4406009027474-retention-polices-for-archived-backups).

### Assign protection policies

You can assign protection policies to individual users and shared drives, OUs, or entire domains. Click **Automatically protect new resources** to enable auto-protection for added shared drives and user accounts.

To apply protection using the OU view, follow these steps:

  1. In the **Protection** section of the Afi application, click **Organizational units**.
  2. Select the OUs you want to protect.
  3. Click **Assign SLA**.
  4. In the pop-up window, select which SLA to apply.
  5. Click the checkbox in the top-left corner to protect all resources in the domain.

![Applying protection to all resources in the domain.](https://docs.cloud.google.com/static/architecture/images/partners/afi-assign_sla.png)




### Recover data

In the **Protection** section of the Afi application, select **Recover** to search, preview, and recover the data.

To download data from a selected recovery point, do the following:

  1. Under the **Backup version** label, browse the recovery points in the drop-down calendar.
  2. Click the selected recovery point.
  3. Use **Search** to find email messages or files.
  4. Click **Download** or **Recover** to export data offline.
  5. Select the export format from the available email options (MBOX, EML, or PST) and then click **Download**.

![Overwriting existing content in Google Workspace.](https://docs.cloud.google.com/static/architecture/images/partners/afi_data_export.png)




To restore data to the same user or to a different user of a shared drive in Google Workspace:

  1. Click **Recover**.
  2. Click **Recover to another account** and select a resource from the drop-down menu if you want to restore data to a different user or shared drive.
  3. Click **Overwrite existing content** if you want to replace existing data in the Google Workspace account.

![Exporting data offline or restoring it to Google Workspace.](https://docs.cloud.google.com/static/architecture/images/partners/afi_data_restore.png)




You can perform export and restore operations for the following:

  * Whole user accounts or shared drives
  * Specific services–for example, restore user data only from Google Workspace email backup)
  * Separate items–for example, specific email messages, labels, or Google Drive folders



## Scope of ransomware protection

Ransomware can infect your users' machines and encrypt the information stored on their computers, including Google Drive files and other Google Workspace data. Afi has a built-in ransomware protection engine that helps detect Google Workspace ransomware attacks and initiates preemptive backup runs before ransomware spreads in your infrastructure. The recovery points resulting from the backup runs are immutable and cannot be encrypted or otherwise modified. This lets you recover Google Workspace data after an attack.

### What Afi can do

  * Detect ransomware and notify your Google Workspace administrator
  * Take preemptive Google Workspace backups before the data is affected
  * Add labels to recovery points to indicate changes between versions and to indicate the last unaffected version of Google Workspace data before encryption
  * Recover Google Workspace data from the last or any previous recovery points before ransomware attacks



### What Afi Google Workspace Backup cannot do

  * Remove ransomware from infected machines
  * Prevent ransomware from spreading
  * Recover Google Workspace data if no recovery points exist (if backups were not running before the ransomware attack)
  * Recover non–Google Workspace data from your users' computers



## Protection status monitoring

In the **Overview** section of the Afi application, Google Workspace administrators can view the protection summary and activity log.

The most recent backup and restore operations are summarized in the **Activity** table. Out-of-schedule backup operations triggered by AI in response to a security event have the **preemptive backup** activity type, while regular backup operations per SLA policies have the **scheduled backup** activity type.

To view details for security events that triggered preemptive backups, and all other activities within the Afi application, go to the **Audit** section.

### Afi Google Workspace Backup audit trail

System administrators can review the activity in the **Audit** section of the Afi application.

  1. Click **Tasks** to review backup and restore operations and their progress.
  2. Go to the **Audit** tab to view the complete list of Afi Google Workspace Backup events, including the following:

     1. User sign-in to Afi applications
     2. Backup data access operations
     3. Backup and restore operations
     4. Detected security threats
     5. The IP address of the actor



The **Audit** tab reflects all activity in the application, including actions performed by partners on behalf of their customers, licensing changes, and Afi configuration changes.

## Partner management portal

Afi provides a [partner management portal](https://portal.afi.ai) for managed service providers (MSPs) that manage Google Workspace Backup for their customers. The portal enables MSPs to create Afi subscriptions, manage Google Workspace Backup policies, and execute data recovery operations for multiple customers.

### Adding customers to the partner management portal

  1. Install Afi Google Workspace Backup in your customer's domain.
  2. In the **Configuration** section, go to the **Service** tab, and copy your customer's Afi customer ID.
  3. Sign in to the partner management portal.
  4. In the **Customers** section, click **\+ Add customer**.

The customer's name appears in the list of customers.




In the **Billing** section of the partner management portal, partners can activate Afi Google Workspace Backup licenses for their customers. Afi sends the invoices and payment receipts to the partner's email address.

## Partner access revocation

Customers can configure and revoke partner access to their Afi Google Workspace Backup account at any time.

  1. Sign in to the Afi Google Workspace Backup application.
  2. In the **Configuration** section, go to the **Roles & Self-Service** tab.
  3. Select the required partner role privileges, or click **Revoke partner access**.



## What's next

  * Sign up for an Afi Google Workspace Backup [trial](http://afi.ai/register).
  * [Install](https://workspace.google.com/marketplace/app/afi_g_suite_backup/429019162995) the application from Cloud Marketplace.
  * Review Afi Google Workspace Backup [pricing](https://afi.ai/pricing).
  * Find out more about [built-in Google Workspace recovery](https://support.google.com/a/answer/6052340) capabilities.
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-01 UTC."],[],[]] 
