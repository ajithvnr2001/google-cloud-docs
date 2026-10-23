---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-qradar/
title: Send Security Command Center data to IBM QRadar \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:30:43.114353+00:00
---

# Send Security Command Center data to IBM QRadar  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-qradar/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Send Security Command Center data to IBM QRadar Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page explains how to automatically send [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview) findings, assets, audit logs, and security sources to [IBM QRadar](https://www.ibm.com/qradar). It also describes how to manage the exported data. QRadar is a security information and event management (SIEM) platform that ingests security data from one or more sources and lets security teams manage responses to incidents and perform real-time analytics.

In this guide, you ensure that required Security Command Center and Google Cloud services are properly configured and enable QRadar to access findings, audit logs, and assets in your Security Command Center environment.

## Before you begin

This guide assumes you are using QRadar ([v7.4.1 Fix Pack 2 or later](https://www.ibm.com/support/pages/release-qradar-741-fix-pack-2-sfs-741qradarfixpack220203220201112005343)). To get started with QRadar, see [Sign up for QRadar](https://www.ibm.com/account/reg/us-en/signup?formid=urx-30209).

## Configure authentication and authorization

Before connecting to QRadar, you need to create an Identity and Access Management (IAM) service account in each Google Cloud organization that you want to connect and grant the account both the organization-level and project-level IAM roles that the Google SCC App for QRadar needs.

### Create a service account and grant IAM roles

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



### Provide the credentials to QRadar

Depending on where you are hosting QRadar, how you provide the IAM credentials to QRadar differs.

  * If you are hosting the [QRadar deployment in Google Cloud](https://www.ibm.com/docs/en/qsip/7.4?topic=images-configuring-qradar-console-google-cloud-platform), consider the following:

    * The service account that you created and the organization-level roles that you granted to it are available automatically by inheritance from the parent organization. If you are using multiple Google Cloud organizations, add this service account to the other organizations and grant it the IAM roles that are described in steps 5 to 7 of Create a service account and grant IAM roles.

    * If you deploy QRadar in a service perimeter, create the ingress and egress rules. For instructions, see [Granting perimeter access in VPC Service Controls](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications#grant-perimeter-access).

  * If you are hosting [QRadar](https://www.ibm.com/docs/en/qsip/7.4?topic=installations-qradar) in your on-premises environment or on IBM Cloud, [create a service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) for each Google Cloud organization. You will need the service account keys in JSON format to complete this guide.

**Note:** Service account keys are a security risk if not managed correctly. You are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  * If you are hosting QRadar in Microsoft Azure or Amazon Web Services, [configure workload identity federation](https://docs.cloud.google.com/iam/docs/configuring-workload-identity-federation) and [download the credentials configuration files](https://docs.cloud.google.com/iam/docs/using-workload-identity-federation). If you are using multiple Google Cloud organizations, add this service account to the other organizations and grant it the IAM roles that are described in steps 5 to 7 of Create a service account and grant IAM roles.




## Configure notifications

Complete these steps for each Google Cloud organization that you want to import Security Command Center data from.

  1. [Set up finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications) as follows: 
     1. Enable the Security Command Center API.
     2. Create a filter to export desired findings and assets.
     3. Create three [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) topics: one each for findings, audit logs, and assets. The `NotificationConfig` must use the Pub/Sub topic that you create for findings.
  2. Create a [sink](https://docs.cloud.google.com/logging/docs/export/configure_export_v2) for the audit logs, as described in [Collate and route organization-level logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks#gcloud). The sink must use the Pub/Sub topic that you created for audit logs. For example:
         
         gcloud logging sinks create SINK_NAME SINK_DESTINATION \
           --include-children \
           --organization=ORGANIZATION_ID \
           --log-filter=FILTER
         

Replace the following:

     * SINK_NAME with the name for the audit log sink.

     * SINK_DESTINATION with `pubsub.googleapis.com/projects/PROJECT_ID/topics/TOPIC_ID`

     * ORGANIZATION_ID with your organization's ID.

     * FILTER with `logName:activity`, `logName:data_access`, `logName:system_event`, or `logName:policy`.

  3. Grant the Pub/Sub Publisher (`roles/pubsub.publisher`) role to the sink's service account.

  4. [Enable the Cloud Asset API](https://console.cloud.google.com/apis/library/cloudasset.googleapis.com) for your project.

  5. [Create feeds for your assets](https://docs.cloud.google.com/asset-inventory/docs/monitoring-asset-changes#creating_a_feed). You must create two feeds in the same Pub/Sub topic, one for your resources and another for your Identity and Access Management (IAM) policies.

     * The Pub/Sub topic for assets must be different than the one used for findings.
     * For the feed for your resources, use the following filter: `content-type=resource`.
     * For the IAM policies feed, you must use the following filter: `content-type=iam-policy --asset-types="cloudresourcemanager.googleapis.com/Project"`.



You will need your organization IDs and Pub/Sub subscription names to configure QRadar.

## Install Google SCC App for QRadar - QRadar v7.4.1FP2+

In this section, you install the Google SCC App for QRadar - QRadar v7.4.1FP2+ (v3.0.0). The app, which is maintained by Security Command Center, automates the process of scheduling Security Command Center API calls, and regularly retrieves Security Command Center data for use in QRadar.

App installation requires access to the QRadar console machine through a web interface.

To complete the installation, do the following:

  1. Download the Google SCC App for QRadar from [IBM App Exchange](https://exchange.xforce.ibmcloud.com/hub).
  2. Log into your QRadar console at https://QRadar_Console_IP.
  3. In the console menu, click **Admin** , and then select **Extension Management**.
  4. To select the download zip file, click **Add**. Follow the prompts as the install is prepared.
  5. Select **Start a default instance for each app**.
  6. Click **Install**. After installation completes successfully, you see a list of application components.
  7. Click the **Admin** tab, and then click **Deploy changes**.
  8. Clear the browser's cache and refresh the browser window.
  9. Navigate to **Extension Management**. You should see **Google SCC App For QRadar** with a status of **Installed**.



## Configure the Google SCC app

In this section, you configure the Google SCC App. To complete the configuration, do the following:

  1. Navigate to the **Admin** tab in QRadar.
  2. Click **Google SCC App Settings**.
  3. Click **Add Google SCC Organization**.
  4. Enter the following variables as needed:

     * **Service Account JSON** : the JSON file that includes the service account key

If you are hosting the QRadar deployment in Google Cloud, this field is not available. Ensure that you provide the service account that is linked to the VM with the IAM permissions for each Google Cloud organization. For more information, see Provide the credentials to QRadar.

     * **Credential Configuration** : the credential configuration file that you downloaded when you set up workload identity federation

     * **Organization ID** : the ID for your organization

     * **Findings Subscription Name** : Pub/Sub subscription name for your finding notifications

     * **Assets Subscription Name** : Pub/Sub subscription name for your assets feed

     * **Enable Audit Logs Collection** : select to send audit logs to your QRadar instance

       * **Audit Logs Subscription Name** : Pub/Sub subscription name for your audit logs sink
     * **Interval** : the number of seconds between Pub/Sub calls during real-time data collection

     * **QRadar Authorization Token** : the token for your QRadar instance. To retrieve a token, do the following:

       1. Navigate to the **Admin** tab in QRadar.
       2. Under **User Management** , click **Authorized Service**.
       3. Copy your authorization token with **Admin** as a user role and **Admin** as Security Profile. If you don't have a token, create one by clicking **Add Authorized Service**.
       4. Click **Deploy changes** , and then refresh the browser window.
  5. To enter optional proxy configuration details, click the **Enable/Disable Proxy** toggle, and then enter your proxy settings:

     * **IP/Hostname** : the IP address or hostname of your proxy server (don't include the HTTP/HTTPS prefix)
     * **Port** : the port of your proxy server
     * **Username** : the username used for the authentication proxy
     * **Password** : the password used for the authentication proxy
  6. Click **Save**.

  7. Repeat these steps for each Google Cloud organization that you want to integrate.




The app configuration is stored and your organizations are added to the app configuration page. The following sections explain how to view and manage Security Command Center data in the service.

## Upgrade the Google SCC app

In this section, you upgrade an existing Google SCC App for QRadar to the latest version.

To complete the upgrade, do the following:

  1. Download the latest version of the Google SCC App from the [IBM App Exchange](https://exchange.xforce.ibmcloud.com/hub).
  2. Log into your QRadar console at https://QRadar_Console_IP.
  3. In the console menu, click **Admin** , and then select **Extension Management**.
  4. To select the download zip file, click **Add**. Follow the prompts as the upgrade is prepared.
  5. Select **Replace Existing Items** and **Start a default instance for each app**.
  6. Click **Install**. After the upgrade process completes successfully, you see a list of application components.
  7. Click the **Admin** tab, and then click **Deploy changes**.
  8. Clear the browser's cache and refresh the browser window.
  9. Navigate to **Extension Management**. You should see **Google SCC App For QRadar** with a status of **Installed**.
  10. Remove application logs from users who access the application from QRadar using SSH:

     1. Download the latest version of the Reference Data Management app from the [IBM App Exchange](https://exchange.xforce.ibmcloud.com/hub/extension/074f919060a2f2dea33e365fc0c5e039).

     2. Log into your QRadar console at https://QRadar_Console_IP.

     3. In the console menu, click **Admin** , and then select **Extension Management**.

     4. To select the download ZIP file, click **Add**. Follow the prompts to install the application.

     5. In the console, navigate to the **Reference Data Management** dashboard.

     6. Click **Reference Map**.

     7. Select **asset_owners** and click **Clear Data**.




## View the exported data in QRadar

This section describes relevant functionality available in QRadar, including searching for findings, audit logs, and assets, viewing IAM policies, and viewing custom dashboards.

### Search for data

To search Security Command Center data in QRadar, you use the **Log Activity** panel. You can see ingested findings, assets, audit logs, and security sources and apply SQL-style filters to refine the data.

### View IAM policy data

To view IAM policy data for your assets, do the following:

  1. Download and install the **Reference Data Management** application from the [IBM App Exchange Portal](https://exchange.xforce.ibmcloud.com/hub/extension/074f919060a2f2dea33e365fc0c5e039).
  2. Click on the **Reference Data Management** dashboard in QRadar.
  3. In the navigation panel, click **Reference Map**.
  4. Select **asset_owners**. The dashboard is populated with your IAM policy data.



### Custom dashboards

You can use custom dashboards in QRadar to visualize and analyze your findings, assets, and security sources.

#### Overview

The **Overview** dashboard displays the total number of findings, threats, and vulnerabilties in your Google Cloud organizations. Findings are compiled from Security Command Center's built-in services, such as [Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics), [Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview), [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview), and [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview) and any integrated services you enable.

You can filter data to update visualizations, specify Google Cloud organization, and fetch new data on-demand.

**Note:** You must be a [Security Command Center Premium](https://docs.cloud.google.com/security-command-center/docs/service-tiers) customer to receive findings from certain Security Command Center services, such as Event Threat Detection and Container Threat Detection.

#### Assets

The **Assets** tab displays a table of your Google Cloud assets. Table data includes asset name, asset type, resource owners, last update time, and links to Security Command Center's **Assets** page in the Google Cloud console.

You can search and filter asset data by organization, time range, and asset type, and drill down to findings for specific assets.

#### Sources

The **Sources** tab displays a table of your security sources, including source name, source display name, and description. By clicking a source name, you can view findings for that source.

#### Findings

The **Findings** tab displays a table of your organization's findings. You can search the table and filter the list by time range, category, severity, security source, asset, and project name.

Table columns includes finding name, category, asset name, security source name, security marks, severity, project name, event time, event time, finding class, and update status. If you click a finding name, you are redirected to Security Command Center's **Findings** page in the Google Cloud console and shown details for the selected finding.

In the **Update Status** column, you can update the state of a finding. To indicate that you are actively reviewing a finding, click **Mark as ACTIVE**. If you are not actively reviewing a finding, click **Mark as INACTIVE**.

### Audit logs

The **Audit logs** dashboard displays a series of charts and tables that show audit log information. The audit logs that are included in the dashboard are the administrator activity, data access, system events, and policy denied audit logs. The table includes the time, log name, severity, service name, resource name, and resource type.

### Check application logs

  1. Log in to QRadar through SSH.
  2. List all installed applications and their `App-ID` values:
         
         /opt/qradar/support/recon ps
         

The output is similar to the following. Take note of the `App-ID` of the `Google SCC` app.
         
         App-ID  Name                                    Managed Host ID Workload ID             Service Name    AB       Container Name          CDEGH          Port          IJKL
         1101    QRadar Log Source Management            53              apps                    qapp-1101       ++           qapp-1101           +++++          5000          ++++
         1104    QRadar Assistant                        53              apps                    qapp-1104       ++           qapp-1104           +++++          5000          ++++
         1105    QRadar Use Case Manager                 53              apps                    qapp-1105       ++           qapp-1105           +++++          5000          ++++
         1163    IBM QRadar Pre-Validation App Service   53              apps                    qapp-1163       ++           qapp-1163           +++++          5000          ++++
         1164    IBM QRadar Pre-Validation App UI        53              apps                    qapp-1164       ++           qapp-1164           +++++          5000          ++++
         1170    Google SCC                              53              apps                    qapp-1170       ++           qapp-1170           +++++          5000          ++++
         

  3. Connect to the `Google SCC` app container:
         
         /opt/qradar/support/recon connect APP_ID
         

Replace APP_ID with the `App-ID` of the `Google SCC` app.

  4. Go to the log directory:
         
         cd /opt/app-root/store/log
         

  5. List all files in the directory:
         
         ls
         

  6. View the contents of a file:
         
         cat FILENAME
         

Replace FILENAME with the name of the file.




## Uninstall Google SCC App

To uninstall the Google SCC App, do the following:

  1. Go to the **Admin** tab.
  2. Select **Extension Management**.
  3. Select **Google SCC App For QRadar - QRadar v7.4.1FP2+**.
  4. Click **Uninstall**.



If you uninstall the application, custom event properties, reference maps, dashboards, and log sources provided by the Google SCC App are removed.

## Known issues

This section lists known issues with the Google SCC App and QRadar dashboards.

### v1.0.0

  * In the **Overview** dashboard, the panel **Findings By Severity Over Time** displays a technical error for data greater than 250,000 findings and the flask process, which populates the dashboards, is restarted in the backend. To avoid this issue, select a smaller time range for the dashboard.

This issue is resolved in v2.0.0.

  * Deleted assets might appear on the **Assets** dashboard because of unexpected behavior from the `GROUP BY` AQL function.




### v2.0.0

  * Deleted assets might appear on the **Assets** dashboard because of unexpected behavior from the `GROUP BY` AQL function.
  * The **Findings** dashboard might not display the latest finding data after you update the Google SCC app because of unexpected behavior from the `GROUP BY` AQL function.



### v3.0.0

  * The dashboard might not display the latest events when multiple events are available with the same unique key because of unexpected behavior from the `GROUP BY` AQL function.
  * For data already ingested using v2, the **Organization ID** filter isn't applicable. You can view the data by selecting the **All** value in the **Organization ID** filter.



## Troubleshoot

This section describes solutions for some common problems.

### Google SCC events are shown as Google SCC messages

**Problem** : Security Command Center events will show up as Security Command Center messages rather than getting identified as the right QRadar category. Messages are seen in the **Log Activity** tab in QRadar when a user searches for an event from a Google Cloud log source.

This issue is occurs when a required field is not present in a raw log event, or if the event payload size is more than the default 4,096 bytes, which can cause events to be truncated.

**Solution** : If payloads are truncated, perform the following steps to increase the maximum payload size:

  1. Navigate to **Admin** tab and select **System settings**.
  2. Under **Switch to** , click **Advanced**.
  3. In the settings list, do the following: 
     1. Select **Max TCP Syslog Payload Length** and increase its value; the recommended value is 32,000.
     2. Select **Max UDP Syslog Payload Length** and increase its value; the recommended value is 32,000.
  4. Click **Deploy changes** and use the **Full Deploy** option.



### Google SCC events listed as unknown events

**Problem** : Security Command Center events are listed as **Unknown**. This issue occurs when the event ID and category from the payload are not mapped in QRadar.

**Solution** : Perform the following steps to fix this issue:

  1. Navigate to **Log Activity** , and then click **Add Filter**.
  2. Select **Parameter** , and then select **Log Source Type (Indexed)**.
  3. Select **Operator** , and then select **Equals**.
  4. Select **Log Source Type** , and then select **Google SCC**.
  5. In the **Views** filter drop-down menu, seelect **Last 7 days**.
  6. If events are displayed as **Unknown** , perform the following steps: 
     1. Right click on the event, and select **View in DSM editor**.
     2. Under **Log Activity Preview** , check the values of **Event ID** and **Event Category**.
     3. If the values are unknown, contact [Cloud Support](https://cloud.google.com/support-hub).



### App configuration fails with error messages

If you get an app configuration error, follow these steps to fix the issue.

Error | Description | Solution  
---|---|---  
"Please enter valid Service Account JSON." | This error occurs if a properly formatted JSON is provided but authentication fails when attempting to save the configuration. | Enter a valid JSON with the correct account credentials.  
"Service Account JSON should be JSON string." | This error occurs if an improperly formatted JSON is provided or the file is in a format other than JSON. | Enter a valid JSON file.  
"Please enter valid Organization ID". | This error occurs when an incorrect or incomplete organization ID is entered. | Verify your organization ID and re-enter it.  
"Please enter valid Project ID or Findings Subscription ID." | This error occurs when an incorrect or invalid project ID or subscription ID is entered. | Verify your project ID and organization ID, and re-enter them.  
"Please enter valid Assets Subscription ID." | This error occurs when an incorrect or invalid asset subscription ID is entered. | Verify your asset subscription ID, and re-enter it.  
"Error while validating authorization token." | This error when an incorrect or invalid QRadar Authorization Token is provided. | Verify your QRadar Authorization Token, and re-enter it. It must have **Admin** as the user role and security profile. The token must also not be expired.  
  
### Error while initiating socket connection with QRadar

**Problem** : An error message, "Error while initiating socket connection with IBM QRadar" is observed in data collection log files. This issue might be observed in the QRadar v2 app framework (< v7.4.2 P2).

**Solution** : Perform the following steps to fix this issue:

  1. Review [support note regarding QRadar deploy changes](https://www.ibm.com/support/pages/node/6395080).
  2. Upgrade QRadar.



### Interface issues

**Problem** : A dashboard panel or configuration page shows errors or unintended behavior.

**Solution** : Perform the following steps to fix this issue:

  1. Clear the browser cache and reload the webpage.
  2. Reduce the time range of the filter. QRadar queries might expire if the number of responses is too large.
  3. If the issue is not resolved, contact [Cloud Support](https://cloud.google.com/support-hub).



### Dashboard panels fail to load and flask process gets killed

**Problem** : The flask process times out and some dashboard panels fail to load.

**Solution** : Perform the following steps to fix this issue:

  1. Clear the browser cache and reload the webpage.
  2. Reduce the time range of the filter. QRadar queries might expire if the number of responses is too large.
  3. If the issue is not resolved, please contact [Cloud Support](https://cloud.google.com/support-hub).



### All other performance issues

If your issue is not resolved by following instructions in this guide, do the following:

  1. Navigate to the **Admin** tab, and then click on **System and License Management**.
  2. Select the host on which **Google SCC App For QRadar - QRadar v7.4.1FP2+** is installed.
  3. Click **Action** , and then select **Collect Log Files**.
  4. In the dialog, click on **Advance Options**.
  5. Select the checkboxes next to **Include Debug Logs** , **Application Extension Logs** , and **Setup Logs (Current Version)**.
  6. Select two days as data input, and then click on **Collect Log Files**.
  7. Select **Click here to download files**.

Log files will be downloaded in a zip file. Contact [Cloud Support](https://docs.cloud.google.com/support-hub) and share the log files.




## What's next

  * Learn more about setting up [finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications) in Security Command Center.

  * Read about [filtering finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications) in Security Command Center.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
