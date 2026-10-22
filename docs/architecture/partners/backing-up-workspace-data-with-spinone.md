---
url: https://docs.cloud.google.com/architecture/partners/backing-up-workspace-data-with-spinone/
title: Configuring SaaS data protection for Google Workspace data with Spin.AI \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:48.649344+00:00
---

# Configuring SaaS data protection for Google Workspace data with Spin.AI  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/partners/backing-up-workspace-data-with-spinone/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Configuring SaaS data protection for Google Workspace data with Spin.AI Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2023-07-12 UTC

By: [Spin.AI](https://spin.ai/)

This document describes how to configure SpinOne - All-in-One SaaS Data Protection with [Cloud Storage](https://docs.cloud.google.com/storage). When you configure SpinOne, including its cybersecurity features, you can store SpinOne for Google Workspace backup data in Google Cloud and restore data from Cloud Storage. The following steps are completed automatically as part of the SpinOne configuration and account creation process:

  * Configures the required Google Cloud infrastructure and services such as Cloud Storage accounts, services, and API hooks.
  * Integrates with Cloud Storage during the SpinOne registration process.
  * Creates new Cloud Storage buckets to store data in Google Cloud.



In this document, you complete the following:

  * Set up SpinOne for Google Workspace.
  * Back up and restore Google Workspace data using SpinOne.
  * Perform a risk assessment of applications in your organization.
  * View and configure ransomware monitoring and response.
  * Enable data loss prevention (DLP) with data audit.



## SpinOne for Google Workspace

SpinOne is a comprehensive SaaS data protection platform for your mission-critical Google Workspace data. SpinOne provides the following four core solutions:

  * SaaS Apps Risk Assessment for Google Workspace
  * SaaS Ransomware Protection for Google Workspace
  * SaaS DLP for Google Workspace
  * SaaS Backup & Recovery for Google Workspace



## Installing SpinOne for Google Workspace

  1. Go to the Google Workspace Marketplace to install [SpinOne – Security & Backup](https://gapps.spinbackup.com/signup/) and click **Install**.
  2. Sign in with your Google Workspace administrator account (make sure you are a [Super Admin](https://support.google.com/a/answer/2405986)), and then click **Next**.
  3. In the **Choose a secure cloud storage** window, click a data center location for Google Cloud, and then click **Get Started**.

Select a data center location based on your business policies or needs. These needs can include keeping data close to the source for performance reasons or keeping your backup data geographically separated from your production data. For more information, see [Geography and Regions](https://docs.cloud.google.com/docs/geography-and-regions).

![Screenshot of SpinOne selection window.](https://docs.cloud.google.com/static/architecture/images/partners/backing-up-g-suite-data-with-spinbackup-spinone.png)

  4. Complete the registration process.




## Perform a risk assessment of the applications in your organization

SpinOne lets you assess the risk of the applications that are installed in your organization. It provides an automated way to assess third-party applications' business, security, and compliance risks. SpinOne includes the following features:

  * **Continuous risk level analysis of applications:** SpinAudit detects when new applications are installed or uninstalled. Then, it automatically reviews the application and identifies applications that have been blocked. After SpinAudit has blocked an application, its access is revoked whenever a user attempts to install it in the cloud SaaS environment.
  * **Implement security policies:** Use granular policies to customize applications, data audits, and domain audit-related policies. It allows for specific rule scopes, exceptions, and notification settings on a per- rule basis.



To view the applications in use in your organization, complete the following:

  1. In the Web Direct console, navigate to **Risk Assessment > All Apps**.
  2. Change the status to **Active**. It displays the scores, applications, states, types, users, and when access was last granted. By reviewing the score, you can determine the level of risks that were introduced in the environment by the applications. SpinOne automatically and continuously performs the risk assessment of third-party applications in Google Workspace Marketplace and browser plugins.



![Screenshot of Risk Assessment window.](https://docs.cloud.google.com/static/architecture/images/partners/backing-up-g-suite-data-with-spinbackup-risk-assessment.png)

## Create a security policy to blocklist risky applications

The risk assessment displays the risk score of applications that are installed in the environment. You can take that information and enforce governance policies based on risk score levels.

Using the SpinOne security policies, you can create granular security policies to block applications based on their security score, among other factors.

  1. In the Web Direct console, navigate to **Security Policies > Policies**.

  2. Click the add icon (+) next to **Create Policy**.

![Screenshot of Security policies window.](https://docs.cloud.google.com/static/architecture/images/partners/backing-up-g-suite-data-with-spinbackup-security-policies.png)

  3. Select **Apps Policy**.

  4. Choose from several conditions, including the following:

     * Application name
     * Application category
     * Application ID
     * Developer
     * Scope of permissions
     * Application risk score

You can choose to apply the policy to OAuth applications or Google Chrome extensions.

![Screenshot of Policy Conditions window.](https://docs.cloud.google.com/static/architecture/images/partners/backing-up-g-suite-data-with-spinbackup-policy-conditions.png)

  5. After defining the conditions of the security policy, define the actions that you want to take. The following screenshot shows how to set the Blocklist action and the alert for each event.

![Screenshot of Blocklist actions window.](https://docs.cloud.google.com/static/architecture/images/partners/backing-up-g-suite-data-with-spinbackup-policy-blocklist.png)

  6. Click **Next step**.

  7. (Optional) In **Scope and Exceptions** , set the scope for the policy to specific users and enter user exceptions for the policy.

![Screenshot of Scope and Exceptions window.](https://docs.cloud.google.com/static/architecture/images/partners/backing-up-g-suite-data-with-spinbackup-scope-exceptions.png)

  8. Click **Next step**. The **Preview** screen appears.

  9. Click **Create policy**.

![Screenshot of Create policy window.](https://docs.cloud.google.com/static/architecture/images/partners/backing-up-g-suite-data-with-spinbackup-create-policy.png)




## View and configure ransomware monitoring and response

You can view and configure ransomware protection in SpinOne. The ransomware protection dashboard provides visibility into malicious activity in the organization and proactive recovery of file resources.

The ransomware protection dashboard gives visibility to the following information:

  * Affected user
  * Service affected
  * Number of encrypted files
  * Number of files recovered
  * Unrecovered files
  * When the attack started
  * When the attack was stopped
  * The type of ransomware


  1. In the Web Direct console, navigate to **Ransomware protection**.

![Screenshot of Ransomware protection window.](https://docs.cloud.google.com/static/architecture/images/partners/backing-up-g-suite-data-with-spinbackup-ransomware-protection.png)

  2. Click **Settings** to view the ransomware protection policy settings. If you have multiple policies configured for ransomware protection, you can change the priority of the policies.

![Screenshot of Change priorities window.](https://docs.cloud.google.com/static/architecture/images/partners/backing-up-g-suite-data-with-spinbackup-change-priorities.png)

  3. To launch the configuration settings for a ransomware protection policy, click the policy. The configuration for the ransomware protection policy includes:

     * Policy type
     * Description
     * Scope
     * Restore encrypted files automatically
     * Revoke an access
     * Restore file sharing permissions
     * Send notification

![Screenshot of Policy configuration window.](https://docs.cloud.google.com/static/architecture/images/partners/backing-up-g-suite-data-with-spinbackup-policy-configuration.png)




## DLP with data audit

SpinOne data audit lets you see the data that is shared internally and externally in your organization. It includes filtering the shared data reports to view sharing information. In addition, administrators can see personally identifiable information (PII) data in the form of transmitted credit card numbers (CCNs).

Using data audit, administrators can create data policies in the security policy settings to enforce data governance and compliance requirements.

  1. In the Web Direct console, click **Data audit > Shared data** to view the shared data dashboard. Use the **Owner** , **Shared to** , **Security Policies** , and **Date** filters to filter data.

![Screenshot of Shared data window.](https://docs.cloud.google.com/static/architecture/images/partners/backing-up-g-suite-data-with-spinbackup-shared-data.png)

  2. To view the PII data, including the CCNs, click **PII data**.

![Screenshot of PII window.](https://docs.cloud.google.com/static/architecture/images/partners/backing-up-g-suite-data-with-spinbackup-pii.png)

  3. To create a new data policy, complete the following tasks:

     1. Go to **Security policies > Policies**.

     2. Click **Create New > Data Policy**.

     3. Configure the following conditions for the new data policy:

        * Filename
        * Check external domains
        * Check domains, users, or groups
        * Check shared by link
        * Allowlist for domains, users, or groups
        * Check for non-owner file sharing

![Screenshot of Policy conditions window.](https://docs.cloud.google.com/static/architecture/images/partners/backing-up-g-suite-data-with-spinbackup-policy-conditions2.png)

     4. Click **Next step**.

     5. Configure the following actions for the new data policy:

        * Revoke sharing permissions
        * Send notification
        * Send notification to owner
        * Change the owner
        * Suspend user

![Screenshot of Policy actions window.](https://docs.cloud.google.com/static/architecture/images/partners/backing-up-g-suite-data-with-spinbackup-policy-actions.png)

     6. Click **Next step**.

     7. (Optional) In **Scope and Exceptions** , set the scope for the data policy to specific users and enter any exceptions for the policy.

![Screenshot of Policy actions window.](https://docs.cloud.google.com/static/architecture/images/partners/backing-up-g-suite-data-with-spinbackup-policy-scope.png)

     8. Click **Next step**. The **Preview** screen appears.

     9. Click **Create policy**.

![Screenshot of Create data policy window.](https://docs.cloud.google.com/static/architecture/images/partners/backing-up-g-suite-data-with-spinbackup-create-data-policy.png)




## Configuring Google Workspace backup

In your SpinOne Dashboard, you can configure the following settings for your Google Workspace backup:

  * Choose which Google Workspace services to back up.
  * Configure backup frequency.
  * Configure backup retention.



### Choose which Google Workspace services to back up

During the initial installation and setup process for SpinOne, you can indicate which of the global Google Workspace services to include in the SpinOne backup of Google Workspace. You can change these preferences after the initial setup wizard or on a per-Google Workspace-user basis. For the purposes of this document, you configure your Google Workspace backup for all users.

  1. In the SpinOne Dashboard, in the **Backup & Recovery** section, click **Users**.

  2. To configure which of the following services are available for backup, expand the **Users** menu:

     * Gmail
     * Google Drive
     * Google Calendar
     * Google Contacts
  3. In **Autobackup** , select the services to back up.

![Screenshot of backed up services.](https://docs.cloud.google.com/static/architecture/images/partners/backing-up-g-suite-data-with-spinbackup-services-backed-up.png)




### Configure automatic backup settings

By default, the automatic backup settings are set up during the initial setup wizard. You can change the automatic backup settings for all users or a specific organization unit. Organizational units are configured in the Google Workspace environment and allow configuring different settings for different users. SpinOne automatically pulls the list of organizational units from your Google Workspace environment.

  1. In the SpinOne Dashboard, in the **Backup & Recovery** section, click **Users**.
  2. In the **Update autobackup setting** window, click **Update all users** , and then turn on the following services for backup:

     * Gmail
     * Google Drive
     * Google Calendar
     * Google Contacts
  3. Click **Update**.

![Screenshot of auto backup settings.](https://docs.cloud.google.com/static/architecture/images/partners/backing-up-g-suite-data-with-spinbackup-update-autobackup-setting.png)




### Configure backup frequency

You can also configure your automatic backup frequency. You can choose to back up the environment either once or three times per day. The backups are fully automated. The backup times are set by our system. You may also trigger a manual backup at any time.

  1. In the SpinOne Dashboard, in the **Backup & Recovery** section, click **Settings**.
  2. In the **Automated Backup Frequency** section, click **3x/day** , and then click **Update**.



### Configure backup retention

By configuring the retention policy, you can choose to keep data indefinitely or to prune data after a specific number of months. Organizations may choose not to retain data due to business policies or other compliance regulations. The default is to keep backups indefinitely, but you can change the duration.

  1. In the SpinOne Dashboard, in the **Backup & Recovery** section, click **Settings**.
  2. In the **Retention policy** section, in the **months from when data was backed up** enter `12`, and then click **Update**.

![Screenshot of Spinbackup retention policy setting.](https://docs.cloud.google.com/static/architecture/images/partners/backing-up-g-suite-data-with-spinbackup-retention-policy.png)




## What's next

  * [Install the application](https://workspace.google.com/marketplace/app/spinone_security_and_backup_spinbackup/829029953048) from Google Workspace Marketplace.

  * Sign up for a free trial of [SpinOne for Google Workspace](https://spin.ai/free-trial/).

  * Find the right solution for you: [SpinOne for Google Workspace](https://spin.ai/platform/google-workspace/).

  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2023-07-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2023-07-12 UTC."],[],[]] 
