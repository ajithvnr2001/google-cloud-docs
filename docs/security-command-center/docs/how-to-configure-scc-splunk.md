---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-splunk/
title: Send Security Command Center data to Splunk \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:29.181861+00:00
---

# Send Security Command Center data to Splunk  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-splunk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Send Security Command Center data to Splunk Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page explains how to automatically send [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) findings, assets, audit logs, and security sources to [Splunk](https://www.splunk.com/). It also describes how to manage the exported data. Splunk is a security information and event management (SIEM) platform that ingests security data from one or more sources and lets security teams manage responses to incidents and perform real-time analytics.

In this guide, you ensure that required Security Command Center and Google Cloud services are properly configured and enable Splunk to access findings, audit logs, and asset information in your Security Command Center environment.

## Before you begin

This guide assumes you are using one of the following:

  * [Splunk Enterprise](https://www.splunk.com/en_us/download/splunk-enterprise.html) version 8.1, 8.2, or 9.0

  * [Splunk Cloud](https://www.splunk.com/en_us/download/splunk-cloud.html)

  * Hosting Splunk in [Google Cloud](https://cloud.google.com/splunk), Amazon Web Services, or Microsoft Azure




## Configure authentication and authorization

Before connecting to Splunk, you need to create an Identity and Access Management (IAM) service account in each Google Cloud organization that you want to connect and grant the account both the organization-level and project-level IAM roles that the Google SCC Add-on for Splunk needs.

### Create a service account and grant roles

The following steps use the Google Cloud console. For other methods, see the links at the end of this section.

Complete these steps for each Google Cloud organization that you want to import Security Command Center data from.

  1. In the same project in which you create your Pub/Sub topics, use the **Service Accounts** page in the Google Cloud console to create a service account. For instructions, see [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts). 
  2. Grant the service account the following role:

     * **Pub/Sub Editor** (`roles/pubsub.editor`) 
  3. Copy the name of the service account that you just created.

  4. Use the project selector in the Google Cloud console to switch to the organization level.

  5. Open the **IAM** page for the organization:

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  6. On the IAM page, click **Grant access**. The grant access panel opens.

  7. In the **Grant access** panel, complete the following steps:

     1. In the **Add principals** section in the **New principals** field, paste the name of the service account.
     2. In the **Assign roles** section, use the **Role** field to grant the following IAM roles to the service account: 

     3. **Security Center Admin Editor** (`roles/securitycenter.adminEditor`) 
     4. **Security Center Notification Configurations Editor** (`roles/securitycenter.notificationConfigEditor`)
     5. **Organization Viewer** (`roles/resourcemanager.organizationViewer`)
     6. **Cloud Asset Viewer** (`roles/cloudasset.viewer`) 
  8. Click **Save**. The service account appears on the **Permissions** tab of the **IAM** page under **View by principals**.

By inheritance, the service account also becomes a principal in all child projects of the organization. The roles that are applicable at the project level are listed as inherited roles.




For more information about creating service accounts and granting roles, see the following topics:

  * [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts)
  * [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access)



### Provide the credentials to Splunk

Depending on where you are hosting Splunk, how you provide the IAM credentials to Splunk differs.

  * If you are hosting [Splunk in Google Cloud](https://cloud.google.com/splunk), consider the following:

    * The service account that you created and the organization-level roles that you granted to it are available automatically by inheritance from the parent organization. If you are using multiple Google Cloud organizations, add this service account to the other organizations and grant it the organization-level IAM roles described in Create a service account and grant IAM roles.

    * If you deploy Splunk in a service perimeter, create the ingress and egress rules. For instructions, see [Granting perimeter access in VPC Service Controls](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications#grant-perimeter-access).

  * If you are hosting [Splunk Enterprise](https://www.splunk.com/en_us/software/splunk-enterprise.html) in your on-premises environment, [create a service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) for each Google Cloud organization. You need the service account keys in JSON format to complete this guide.

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  * If you are hosting Splunk in another cloud, [configure workload identity federation](https://docs.cloud.google.com/iam/docs/configuring-workload-identity-federation) and [download the credentials configuration files](https://docs.cloud.google.com/iam/docs/using-workload-identity-federation). If you are using multiple Google Cloud organizations, add this service account to the other organizations and grant it the organization-level IAM roles described in Create a service account and grant IAM roles.




## Configure notifications

Complete these steps for each Google Cloud organization that you want to import Security Command Center data from.

To configure Splunk, you need your organization IDs, Pub/Sub topic names, and Pub/Sub subscription names from this task

### Create topics and subscriptions

To enable Splunk to retrieve the data, you must create three Pub/Sub topics and a corresponding pull subscription for each topic.

  1. Create a topic and subscription for findings.
  2. Create a topic and subscription for assets.
  3. Create a topic and subscription for audit logs.



For instructions on creating topics and subscriptions, see [Managing topics and subscriptions](https://docs.cloud.google.com/pubsub/docs/admin).

### Set up finding notifications

  1. Enable the Security Command Center API.
  2. To export Security Command Center findings to the findings Pub/Sub topic based on filters that you specify, [create a `notificationConfig`](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications)



### Set up asset feeds

  1. [Enable the Cloud Asset API](https://console.cloud.google.com/apis/library/cloudasset.googleapis.com) for your project.
  2. To send asset change notifications to the assets Pub/Sub topic, [create feeds for your assets](https://docs.cloud.google.com/asset-inventory/docs/monitoring-asset-changes#creating_a_feed). You must create two feeds in the same topic: 
     * For resources, use the filter `content-type=resource`.
     * For IAM policies, use the filter `content-type=iam-policy AND asset-types="cloudresourcemanager.googleapis.com/Project"`.



### Set up audit logs export

  1. [Create a destination sink](https://docs.cloud.google.com/logging/docs/export/configure_export_v2) for your audit logs. Use the audit logs Pub/Sub topic as the destination.
  2. To export only relevant audit logs, use a filter that includes the supported audit log types:

     * Admin Activity
     * Data Access
     * System Events
     * Policy Denied

For example, you can use the following filter for your sink:
    
    log_id("cloudaudit.googleapis.com/activity") OR
    log_id("cloudaudit.googleapis.com/data_access") OR
    log_id("cloudaudit.googleapis.com/system_event") OR
    log_id("cloudaudit.googleapis.com/policy")
    




## Install the apps

In this section, you install the Google SCC App for Splunk and the Google SCC Add-on for Splunk. These apps, which are maintained by Security Command Center, automate the process of scheduling Security Command Center API calls, regularly retrieve Security Command Center data for use in Splunk, and set up the dashboards that allow you to view Security Command Center data in Splunk.

App installation requires access to the Splunk web interface.

If you have a distributed Splunk deployment, install the apps as follows:

  * Install the Google SCC App for Splunk on the Splunk [heavy forwarder](https://docs.splunk.com/Splexicon:Heavyforwarder) and the Splunk [search heads](https://docs.splunk.com/Splexicon:Searchhead).
  * Install the Google SCC Add-on for Splunk on the Splunk search heads.



To complete the installation, do the following:

  1. In the Splunk web interface, go to the **Apps** gear icon.

  2. Select **Manage Apps > Browse more apps**.

  3. Search for and install the following apps:

     * Google SCC Add-on for Splunk
     * Google SCC App for Splunk



Both apps appear in your Apps list. Continue to Connect Splunk to Google Cloud to configure the apps.

## Upgrade the apps

  1. Disable all existing inputs:

     1. In the Splunk web interface, click **Apps > Google SCC Add-on for Splunk**.

     2. Select the **Inputs** tab.

     3. For each input, click **Action > Disable**.

  2. Remove the Security Command Center indexed data. You can use the [Splunk CLI clean command](https://docs.splunk.com/Documentation/Splunk/8.2.5/Indexer/RemovedatafromSplunk#Remove_data_from_indexes_with_the_CLI_clean_command) to remove indexed data from an app before deleting the app.

  3. Perform the upgrade:

     1. In the Splunk web interface, go to the **Apps** gear icon.

     2. Select **Manage Apps > Browse more apps**.

     3. Search for and upgrade the following apps:

        * Google SCC Add-on for Splunk
        * Google SCC App for Splunk
     4. If prompted, restart Splunk.

  4. For each new Google Cloud organization, complete the Connect Splunk to Google Cloud section.

  5. Create the new inputs, as described in Add the Security Command Center data inputs.




## Connect Splunk to Google Cloud

You must have the [`admin_all_objects` capability](https://docs.splunk.com/Documentation/Splunk/8.2.5/Security/Rolesandcapabilities) in Splunk to complete this task.

### Prerequisites for AWS or Azure deployments

If you installed Splunk on Amazon Web Services or Microsoft Azure, complete the following steps before configuring your account in the Splunk web interface:

  1. Open a terminal window.

  2. Navigate to the Google SCC App for Splunk directory:
         
         cd $SPLUNK_HOME/etc/apps/TA_GoogleSCC/local/
         

  3. Open `ta_googlescc_settings.conf` in a text editor:
         
         sudo vim ta_googlescc_settings.conf
         

  4. Add the following lines to the end of the file:
         
         [additional_parameters]
         scheme = http
         

  5. Save and close the file.

  6. Restart the Splunk platform.




### Add your Google SCC account in Splunk

  1. In the Splunk web interface, go to **Apps > Google SCC Add-on for Splunk > Configuration**, select the **Configuration** tab, and click **Add**.

  2. In the Add Account dialog, provide your credentials by doing one of the following, depending on the field that appears:

     * If the **Service Account JSON** field is displayed, browse to the JSON file that includes the service account key.

     * If the **Credential Configuration** field is displayed, browse to the credential configuration file that you downloaded when you set up workload identity federation.

If you deployed Splunk in Google Cloud or completed the prerequisites for AWS or Azure deployments, the service account configuration is automatically detected.

  3. In the **Organization** field, add your Google Cloud organization ID.

  4. If you are using a proxy server to connect Splunk with Google Cloud, do the following:

     1. Click the **Proxy** tab.
     2. Select **Enable**.
     3. Select your proxy type (HTTPS, SOCKS4, or SOCKS5).
     4. Add your proxy hostname, port, and optionally, the username and password.
  5. In the **Logging** tab, select the logging level for the add-on.

  6. Click **Save**.


**Note:** To integrate multiple Google Cloud organizations, repeat the steps in this section for each organization.

Create data inputs for your Google Cloud organizations, as described in Add the Security Command Center data inputs.

### Add the Security Command Center data inputs

  1. In the Splunk web interface, click **Apps > Google SCC Add-on for Splunk**.

  2. Select the **Inputs** tab.

  3. Click **Create New Input**.

  4. Select one of the inputs:

     * Source Input
     * Findings Input
     * Asset Input
     * Audit Logs Input
  5. Click the **Edit** icon.

  6. Enter the following information: 

Field  | Description   
---|---  
Input name | The default name for your data input  
Interval | The time (in seconds) to wait between calls for data  
Index | The Splunk index that the Security Command Center data goes to  
Assets Subscription Id | For asset inputs only, the name of the Pub/Sub subscription for resources  
Audit Logs Subscription Id | For audit logs input only, the name of the Pub/Sub subscription for audit logs  
Findings Subscription Id | For findings input only, the name of the Pub/Sub subscription for findings  
Maximum Fetching | The maximum number of assets to fetch in one call  
  7. Click **Update**.

  8. Repeat steps 3 through 7 for each input that you want to add.

  9. Repeat steps 3 through 8 for each Google Cloud organization that you want to integrate.

  10. In the **Status** row, enable the data inputs that you want to forward to Splunk.




### Update the Splunk index

Complete this task if you don't use the main Splunk index:

  1. In the Splunk web interface, click **Settings > Advanced Search > Search macros**.
  2. Select **Google SCC App for Splunk**.
  3. Select **googlescc_index**.
  4. Update `index=main` to use your index.
  5. Click **Save**.



### View Security Command Center data in Splunk

  1. In the Splunk web interface, click **Apps > Google SCC Add-on for Splunk**.

  2. Select the **Search** tab.

  3. Set your search query, for example `index="main"`.

  4. Select the time range.

  5. Click the **Search** icon.

  6. Filter data by source type (one of sources, assets, auditlogs, IAM assets, or findings), as required.




## View the dashboards

The Google SCC App for Splunk lets you visualize the data from Security Command Center. It includes five dashboards: **Overview** , **Sources** , **Findings** , **Assets** , **Audit Logs** , and **Search**.

You can access these dashboards in the Splunk web interface, from the **Apps > Google SCC App for Splunk** page.

### Overview dashboard

The **Overview** dashboard contains a series of charts that displays the total number of findings in your organization by severity level, category, and state. Findings are compiled from Security Command Center's built-in services, such as [Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics), [Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview), [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview), and [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview) and any integrated services you enable.

To filter content, you can set the time range and organization ID.

Additional charts show which categories, projects, and assets are generating the most findings.

**Note:** You must be a [Security Command Center Premium](https://docs.cloud.google.com/security-command-center/docs/service-tiers) customer to receive findings from certain Security Command Center services, such as Event Threat Detection and Container Threat Detection.

### Assets dashboard

The **Assets** dashboard displays a table of the 1000 most recently created or modified Google Cloud assets. The table shows asset name, asset type, resource owner, and last update time.

You can filter asset data by time range, organization ID, and asset type. If you click **View** in the **Redirect To SCC** column, you are redirected to Security Command Center's **Assets** page in the Google Cloud console and shown details for the selected asset.

### Audit logs dashboard

The **Audit logs** dashboard displays a series of charts and tables that show audit log information. The audit logs that are included in the dashboard are the administrator activity, data access, system events, and policy denied audit logs. The table includes the time, log name, severity, service name, resource name, and resource type.

You can filter the data by time range, organization ID, and log name.

### Findings dashboard

The **Findings** dashboard includes a table of the 1000 most recent findings. The table column includes items such as category, asset name, source name, security marks, finding class, and severity.

You can filter the data by time range, organization ID, category, severity, source name, asset name, project name, or finding class. In addition, in the **Update Status** column, you can update the state of a finding. To indicate that you are actively reviewing a finding, click **Mark as ACTIVE**. If you are not actively reviewing a finding, click **Mark as INACTIVE**.

If you click a finding name, you are redirected to Security Command Center's **Findings** page in the Google Cloud console and shown details for the selected finding.

### Sources dashboard

The **Sources** dashboard shows a table of all your security sources. Table columns include name, display name, and description.

To filter content, you can set the time range.

## Uninstall the apps

Uninstall the apps when you no longer want to retrieve Security Command Center data for Splunk.

  1. In the Splunk web interface, go to **Apps > Manage Apps**.

  2. Search for `Google SCC App for Splunk`.

  3. In the **Status** column, click **Disable**.

  4. Search for `Google SCC Add-on for Splunk`.

  5. In the **Status** column, click **Disable**.

  6. Optionally, remove the Security Command Center indexed data. You can use the [Splunk CLI clean command](https://docs.splunk.com/Documentation/Splunk/8.2.5/Indexer/RemovedatafromSplunk#Remove_data_from_indexes_with_the_CLI_clean_command) to remove indexed data from an app before deleting the app.

  7. In a Splunk standalone environment, do the following:

     1. Open a terminal and sign in to Splunk.

     2. Delete the apps and their directories in `$SPLUNK_HOME/etc/apps/APPNAME`:
            
            ./splunk remove app APPNAME -auth USERNAME:PASSWORD
            

Replace APPNAME with `GoogleSCCAppforSplunk` or `TA_GoogleSCC`.

     3. Repeat step b for the other app.

     4. Optionally, remove the user-specific directories by deleting any files found in `$SPLUNK_HOME/etc/users/*/GoogleSCCAppforSplunk` and `$SPLUNK_HOME/etc/users/*/TA_GoogleSCC`.

     5. Restart the Splunk platform.

  8. In a distributed Splunk environment, do the following:

     1. Sign in to the [deployer manager](https://docs.splunk.com/Documentation/Splunk/latest/DistSearch/PropagateSHCconfigurationchanges).
     2. Delete the apps and their directories in `$SPLUNK_HOME/etc/apps/APPNAME`:
            
            ./splunk remove app APPNAME -auth USERNAME:PASSWORD
            

Replace APPNAME with `GoogleSCCAppforSplunk` or `TA_GoogleSCC`.

     3. Repeat step b for the other app.

     4. Run the `splunk apply shcluster-bundle` command:
            
            splunk apply shcluster-bundle -target URI:MANAGEMENT_PORT -auth USERNAME:PASSWORD
            




## Troubleshooting

This section describes how to resolve common issues with the Splunk integration.

### Configuration or input page doesn't load

If the configuration or input page doesn't load, check the Splunk daemon log for errors: `$SPLUNK_HOME/var/log/splunk/splunkd.log`

### Data doesn't appear in Splunk or dashboards

If you configured the account and inputs but data doesn't appear in Splunk, try the following:

  * **Check the logs:** Check the log file for the specific input that is failing: `$SPLUNK_HOME/var/log/splunk/ta_googlescc_INPUT_NAME.log`

Replace `INPUT_NAME` with `findings`, `assets`, or `audit_logs`.

  * **Enable debug logging:** To get more verbose logs, go to **Google SCC Add-on for Splunk > Configuration > Logging**, and set the log level to **DEBUG**. Then, to recollect data, disable and re-enable the input.

  * **Verify Pub/Sub data:** Verify that data is reaching your Pub/Sub subscriptions in Google Cloud. You can try pulling messages manually from the subscription in the Google Cloud console.

  * **Update the index macro:** If you use a custom Splunk index, update the `googlescc_index` search macro. Go to **Settings > Advanced Search > Search macros**, and then select **Google SCC App for Splunk**. To point to your index, update `googlescc_index`.

  * **Enable saved searches:** Go to **Settings > Searches, Reports and Alerts**, and then select **Google SCC App for Splunk**. Enable `googlescc_finding_state_lookup` and `googlescc_update_owner_lookup_from_index` if they are disabled.




### Finding state doesn't update

If clicking **Mark as ACTIVE** or **Mark as INACTIVE** doesn't update the finding state, try the following:

  * Check the user action log: `$SPLUNK_HOME/var/log/splunk/ta_googlescc_update_findings_status.log`

  * Confirm that you enabled the KV Store in Splunk. The integration relies on the KV Store to maintain finding states.




### Splunk doesn't detect cloud instances

If you host Splunk on AWS or Azure and the add-on UI doesn't auto-detect the instance, verify the configuration:

  1. Edit the following file: `$SPLUNK_HOME/etc/apps/TA_GoogleSCC/local/ta_googlescc_settings.conf`.
  2. Ensure that the following lines are present:
         
         [additional_parameters]
         scheme = http
         

  3. Restart Splunk.

  4. Verify that you enabled the KV Store.




## What's next

  * Learn more about setting up [finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications) in Security Command Center.

  * Read about [filtering finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications) in Security Command Center.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
