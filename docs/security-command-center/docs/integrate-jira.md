---
url: https://docs.cloud.google.com/security-command-center/docs/integrate-jira/
title: Integrate Security Command Center with Atlassian Jira \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:38.564398+00:00
---

# Integrate Security Command Center with Atlassian Jira  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/integrate-jira/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Integrate Security Command Center with Atlassian Jira Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

Security Command Center for Jira Cloud lets you automatically create Jira issues from Security Command Center findings. When you configure [Security Command Center for Jira Cloud](https://marketplace.atlassian.com/apps/1922340779/security-command-center-for-jira-cloud) in Jira, you specify the project, state, severity, and category of findings to import from an organization where Security Command Center is activated.

You can set an automatic sync interval or manually sync Jira and Security Command Center at any time.

During the sync process, Jira creates issues from new or updated Security Command Center findings that match the Security Command Center for Jira Cloud configuration. If you update the mute status or finding state in Jira, Security Command Center for Jira Cloud syncs those changes back to the corresponding finding in Security Command Center.

After you set up Security Command Center for Jira Cloud, you can manually refresh Jira issues to display the latest finding details, finding state, and mute status from Security Command Center.

## Before you begin

Before you integrate Jira Cloud with Security Command Center, you need the following:

  * A [Jira Cloud](https://developer.atlassian.com/cloud/jira/platform/) instance.
  * A Google Cloud project with Security Command Center enabled.
  * The service account. You will grant the service account roles and use the key to configure the connection.  
Service account keys are a security risk if not managed correctly. You are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 




### Required roles

To ensure that your service account has the necessary permissions to integrate Security Command Center findings with Jira, ask your administrator to grant the [Security Center Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securitycenter#securitycenter.admin) (`roles/securitycenter.admin`) IAM role to your service account on your organization. **Important:** You must grant this role to your service account, _not_ to your user account. Failure to grant the role to the correct principal might result in permission errors.  For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give your service account the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Configure policies for service perimeters

If you use Security Command Center with a service perimeter, you must configure ingress and egress policies. To configure ingress and egress policies, see [Configuring ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).

## Use the Security Command Center for Jira Cloud application

To use the Security Command Center for Jira Cloud application, do the following:

  1. Install the Security Command Center for Jira Cloud application in Jira.
  2. Configure the Security Command Center for Jira Cloud application in Jira.
  3. Add Security Command Center finding source details to Jira issues.
  4. Get mute status and finding state information for Jira issues.



After you configure Security Command Center and get data from it, Security Command Center for Jira Cloud syncs issues between Jira and Security Command Center.

### Install the Security Command Center for Jira Cloud application in Jira

To install the Security Command Center for Jira Cloud application in Jira, do the following:

  1. Sign in to your Atlassian Jira account as a Jira administrator.
  2. In Jira, click **Apps** and then select **Explore More Apps**.
  3. Search for **Security Command Center for Jira Cloud**.
  4. Click the application, and then click **Get App** to open the installation dialog.
  5. Click **Get it now**. When the installation completes, Jira displays a confirmation message.
  6. Click **Apps** , and then select **Manage your Apps**.
  7. Confirm that **Security Command Center for Jira Cloud** appears in the **User-Installed Apps** section.



### Configure the Security Command Center for Jira Cloud application in Jira

  1. In Jira, click **Apps** and then **Manage your Apps**.
  2. Go to **Apps > Security Command Center for Jira Cloud**.
  3. If prompted to allow access, click **Allow Access > Accept**. The configuration page displays.
  4. For **Authentication Information** , specify the following:

     * For **User's Service Account JSON** , enter the service account key in JSON format. For information about getting the key, see [Create and delete service account keys](https://docs.cloud.google.com/iam/docs/keys-create-delete#iam-service-account-keys-get-console).
     * For **Enter Base URL** , enter the regional endpoint base URL for the Google Cloud API services. The default value is `https://securitycenter.googleapis.com`. For more information, see [Security Command Center regional service endpoint](https://docs.cloud.google.com/security-command-center/docs/reference/rest?rep_location=global#regional-service-endpoint).

     * For **Enter Organization ID** , enter the ID of your Security Command Center organization. Security Command Center for Jira Cloud creates issues for Security Command Center findings for all projects and folders in that organization.

  5. For **Scheduler Configurations** , specify the following:

     * For **Run** , select how often you want Security Command Center and Jira to sync. You can choose from `Hourly`, `Daily`, `Weekly`, and `Custom` intervals. If you select `Custom`, specify the time between syncs, in hours.

     * For **Number of days of historical findings to fetch initially** , enter a time range, in days, that identifies the findings that are collected by Jira. By default, Jira collects Security Command Center findings from the last 7 days.

**Note:** We recommend setting this field to 7 days or fewer. Setting a larger value will cause Jira to take longer and use more resources to create issues.
  6. For **Projects & Users**, specify the following:

     * For **Select Project** , select the Jira project to create issues in.

**Note:** The list displays only company-managed projects; Jira team-managed projects don't appear.
     * For **Default Assignee** , select the Jira user to assign the Jira issues to. If you don't select a Jira user, Jira sets the **Default assignee** field to `Unassigned`.

  7. For **Findings Configuration** , specify the following:

     * For **GCP Project ID** , enter a comma-separated list of Security Command Center project IDs to get findings from.

     * For **State** , select the findings that you want to import from Security Command Center based on their current state. Valid values are `active`, `inactive`, or `all`. By default, Jira imports findings in an active state.

     * For **Severity** , select which severity of findings Jira imports. By default, Jira imports findings of all severity levels.

     * For **Category** , enter a comma-separated list of finding categories that you want to import into Jira.

  8. To authenticate your credentials and save the configuration, click **Validate and Save**.




After you save the configuration, Security Command Center for Jira Cloud creates issues from Security Command Center findings within one hour. For each Jira issue, the **Description** field contains finding and asset details, the **Details** field contains Security Command Center information, and the **Finding URL** field contains a link to the Security Command Center finding details.

After you configure Security Command Center for Jira Cloud, Jira displays Security Command Center findings as issues in your Jira project.

### Add Security Command Center finding source details to Jira issues

Security Command Center for Jira Cloud doesn't automatically populate Security Command Center source details during a sync. To see Security Command Center finding source details for Jira issues, do the following:

  1. Open a Jira issue created by the Security Command Center for Jira Cloud application.
  2. Click the gear icon, then click **Google SCC Enrichment**.
  3. Click **Confirm**.



Jira updates the **Source Details** field with the source details.

### Get mute status and finding state for Jira issues

After you configure Security Command Center for Jira Cloud, the application doesn't automatically populate the mute status and finding state from Security Command Center. To view these values in Jira issues created from Security Command Center findings, you must manually update them. To update the mute status and finding state, do the following:

  1. Open a Jira issue created by the Security Command Center for Jira Cloud application.
  2. Click the gear icon, then click **Update mute status and finding state**.
  3. Click **Confirm**.



When Security Command Center for Jira Cloud successfully updates the finding state or mute status, the application adds a comment to the Jira issue. If the update fails, Security Command Center for Jira Cloud adds a comment about the failure and reverts both properties to their previous state.

When you change the finding state or mute status in Jira, Security Command Center for Jira Cloud updates the corresponding finding in Security Command Center, and Security Command Center adds a description to the finding's **Security marks** field.

## Manually start or stop a sync process

To sync Security Command Center findings and Jira issues immediately, do the following:

  1. In Jira, click **Apps** and then **Manage your Apps**.
  2. Go to **Apps > Security Command Center for Jira Cloud**.
  3. If prompted to allow access, click **Allow Access > Accept**. The configuration page opens.
  4. Click **Manual Sync**.

**Note:** You can't manually sync Jira and Security Command Center while a sync process is running.

To stop a sync process between Jira and Security Command Center, do the following:

  1. In Jira, click **Apps** and then **Manage your Apps**.
  2. Go to **Apps > Security Command Center for Jira Cloud**.
  3. If prompted to allow access, click **Allow Access > Accept**. The configuration page opens.
  4. Click **Stop Sync**.



## Reset the Security Command Center for Jira Cloud application

After you save and validate your configuration, you can't change the selected Jira project or the time range that you set for getting Security Command Center findings. To modify these settings, you must reset and reconfigure the application.

When you reset and reconfigure the application, any Jira issues that Security Command Center for Jira Cloud already created remain in Jira. If your new configuration imports the same findings, Jira checks for duplicate issues and doesn't create new issues for those findings.

To remove all saved credentials and configurations, do the following:

  1. In Jira, click **Apps** and then **Manage your Apps**.
  2. Go to **Apps > Security Command Center for Jira Cloud**.
  3. Click **Reset**.



Jira removes your existing configuration. To configure Security Command Center for Jira Cloud again, see Configure the Security Command Center for Jira Cloud application in Jira.

## View log files for Security Command Center for Jira Cloud

To see errors and troubleshoot the Security Command Center for Jira Cloud application, you can view its log files.

**Note:** To view log files for Security Command Center for Jira Cloud, you must have a Jira system administrator role. For more information about users, groups, permissions, and roles in Jira Cloud, see [Manage users, groups, permissions, and roles in Jira Cloud](https://support.atlassian.com/jira-cloud-administration/docs/manage-users-groups-permissions-and-roles-in-jira-cloud).

To view log files in Jira for Security Command Center for Jira Cloud, do the following:

  1. Go to [Atlassian Administration](https://admin.atlassian.com/).
  2. Click **Products**.
  3. For **SITES AND PRODUCTS** , select your site.
  4. Click **Connected Apps**.
  5. Find **Security Command Center for Jira Cloud** from the installed apps list and click **View app details**.
  6. Click **Download Logs**.
  7. Choose a time interval and click **Apply**.
  8. Click **Download** to download the log file.



## Troubleshoot Security Command Center for Jira Cloud

Jira typically enables Security Command Center for Jira Cloud within two minutes. After Jira enables the application and Security Command Center generates a new finding, Security Command Center for Jira Cloud typically creates a Jira issue for the finding within a few seconds.

If a sync process fails, Security Command Center for Jira Cloud logs an error and retries the sync. If a sync process fails four times, the process stops and Security Command Center for Jira Cloud displays an error message. To view these errors, see View log files for Security Command Center for Jira Cloud.

When a sync process fails, Security Command Center for Jira Cloud saves your configuration and progress. The next time Security Command Center for Jira Cloud runs, it resumes using the saved data. If you change the configuration before Security Command Center for Jira Cloud runs again, the application uses the new configuration.

If you encounter an authentication error, check the error message and reset your configuration.

If Security Command Center for Jira Cloud doesn't create issues or creates issues incorrectly, check the error messages and reset your configuration.

## What's next

  * Learn more about [Security Command Center for Jira Cloud](https://marketplace.atlassian.com/apps/1922340779/security-command-center-for-jira-cloud).
  * To learn more about installing apps in Jira, see [Installing Marketplace apps](https://confluence.atlassian.com/upm/installing-marketplace-apps-273875715.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
