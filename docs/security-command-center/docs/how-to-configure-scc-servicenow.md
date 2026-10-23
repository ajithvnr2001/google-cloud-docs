---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-servicenow/
title: Send Security Command Center data to ServiceNow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:31:34.646241+00:00
---

# Send Security Command Center data to ServiceNow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-configure-scc-servicenow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Send Security Command Center data to ServiceNow Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document explains how to automatically send Security Command Center data to [ServiceNow](https://www.servicenow.com/) and provides guidance on how to manage the exported data. You can export the following data types:

  * [Findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings)
  * [Assets](https://docs.cloud.google.com/security-command-center/docs/assets-resources-overview)
  * [Audit logs](https://docs.cloud.google.com/logging/docs/audit)
  * [Security sources](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources)



ServiceNow provides technical management support, including helpdesk functionality. Its management system helps automate task-intensive IT processes and events using digital workflows and employee service portals.

## Supported versions

You can send Security Command Center information to ServiceNow IT Service Management (ITSM) or ServiceNow Security Incident Response (SIR).

Security Command Center supports integrations with the following ServiceNow versions:

  * Australia
  * Zurich
  * Yokohama



If you use an earlier version (such as Rome, San Diego, or Tokyo), you should migrate to the latest supported version.

To get started with ServiceNow, see the [ServiceNow contact page](https://www.servicenow.com/contact-us.html).

## Limitations

This section describes the limitations of this integration.

  * You can fetch a combined maximum of 1,000 assets, findings, sources, or audit logs per API call.
  * If the Findings API call response is `429` or `5xx`, the application retries after 60 seconds for 3 attempts. If it still fails, the process fails. To change the response time, see Application cannot reconnect after three attempts.



## Before you begin

Before integrating with ServiceNow, complete the Google Cloud configuration steps in the following section. To complete some tasks in this guide, such as the user creation steps, you must be a ServiceNow system administrator.

### Google Cloud configuration

Before you can connect to ServiceNow, you need to create an Identity and Access Management (IAM) [service account](https://docs.cloud.google.com/iam/docs/service-account-overview) and grant the account the organization-level and project-level [ IAM roles](https://docs.cloud.google.com/iam/docs/understanding-roles) required by the Google Security Command Center SIR app or Google Security Command Center ITSM app.

For more information about these roles, see Create a service account and grant IAM roles.

#### Create a service account and grant IAM roles

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



#### Provide the credentials to ServiceNow

To provide IAM credentials to ServiceNow, [create a service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys). To complete this guide, you need the service account key in JSON format.

If you use multiple Google Cloud organizations, add this service account to the other organizations and grant it the necessary IAM roles, as described in Create a service account and grant IAM roles in the preceding section.

**Note:** Service account keys are a security risk if not managed correctly. You are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

#### Configure notifications

Complete these steps for each Google Cloud organization that you want to import Security Command Center data from.

  1. [Set up finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications) as follows:

     1. Enable the [Security Command Center API](https://console.cloud.google.com/apis/library/securitycenter.googleapis.com).
     2. Create a [filter](https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications) to export findings and assets.
  2. [Enable the Cloud Asset API](https://console.cloud.google.com/apis/library/cloudasset.googleapis.com) for your project.

  3. [Create feeds for your assets](https://docs.cloud.google.com/asset-inventory/docs/monitoring-asset-changes#creating_a_feed). Create two feeds in the same [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) topic: one for your resources and one for your [IAM policies](https://docs.cloud.google.com/iam/docs/policies).

     * Use a different [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/publish-message-overview#about-topics) for assets from the topic you use for findings.
     * For the feed for your resources, use the following filter:

`content-type=resource`

     * For the IAM policies feed, use the following filter:

`content-type=iam-policy --asset-types="cloudresourcemanager.googleapis.com/Project"`

  4. [Create a destination sink](https://docs.cloud.google.com/logging/docs/export/configure_export_v2) for the audit logs. This integration uses a Pub/Sub topic as the destination.




To configure ServiceNow, you need your [organization IDs](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id) and [Pub/Sub subscription](https://docs.cloud.google.com/pubsub/docs/subscriber) names.

## Set up ServiceNow

This section explains how to install the app, create users, configure connectivity, and set up ServiceNow to retrieve Security Command Center data.

### Install the ServiceNow app

To complete this task, you must be a ServiceNow system administrator.

  1. Go to the [ServiceNow Store](https://store.servicenow.com/) and search for one of the following apps:

     * If you are running ServiceNow ITSM, search _Google Security Command Center ITSM_.

     * If you are running ServiceNow SIR, search _Google Security Command Center SIR_.

  2. Click the app and click **Get**.

  3. Enter your ServiceNow ID credentials and proceed through the authentication process.

  4. In the ServiceNow console **All** tab, search for **System Applications** and click **All Available Applications > All**.

  5. Select **Not installed**. The console displays a list of applications.

  6. Select the _Google Security Command Center ITSM_ or _Google Security Command Center SIR_ app and click **Install**.




### Create users for the app

Create two users for the Google Security Command Center ITSM or Google Security Command Center SIR app and assign them the appropriate roles.

To complete this task, you must be a ServiceNow system administrator.

#### Create the user accounts

  1. In the ServiceNow console, search for **Organization**.

  2. Click **Organization > Users**.

  3. Click **New**.

  4. Enter the information for the administrator account for the Google Security Command Center ITSM app or Google Security Command Center SIR app. For example, in the **User ID** field, enter `google_scc_itsm_admin` for Google Security Command Center ITSM or `google_scc_sir_admin` for Google Security Command Center SIR.

  5. Click **Submit**.

  6. To create a user account for the Google Security Command Center ITSM app or Google Security Command Center SIR app, repeat the steps in Create the user accounts. For example, in the **User ID** field, enter `google_scc_itsm_user` for Google Security Command Center ITSM or `google_scc_sir_user` for Google Security Command Center SIR.




#### Assign roles to the accounts

  1. In the **Users** list, click the name of one of the new accounts.

  2. Under **Roles** , click **Edit**.

  3. Add the roles that apply to the account:

Username| Roles  
---|---  
Google Security Command Center ITSM admin (google_scc_itsm_admin) | 
     * x_goog_scc_itsm.Google_SCC_ITSM_Admin
     * itil
     * itil_admin
     * personalize_dictionary
     * oauth_admin  
Google Security Command Center ITSM User (google_scc_itsm_user) | 
     * x_goog_scc_itsm.Google_SCC_ITSM_User
     * itil  
Google Security Command Center SIR admin (google_scc_sir_admin)| 
     * x_goog_scc_sir.Google_SCC_SIR_Admin
     * sn_si.admin
     * oauth_admin  
Google Security Command Center SIR user (google_scc_sir_user)| 
     * x_goog_scc_sir.Google_SCC_SIR_User
     * sn_si.analyst  
  4. Click **Save**.

  5. To assign roles to the other account, repeat steps 1 through 4.

  6. Sign out and sign in with the new accounts to verify the passwords.




### Configure authentication with Security Command Center

Set up connectivity between Security Command Center and ServiceNow. If you support multiple organizations, complete these steps for each organization.

To complete this task, you must be a ServiceNow system administrator.

#### Prepare the Java KeyStore certificate

  1. Create a Java KeyStore certificate from the JSON file that contains your service account key. For instructions, see [Create a Java KeyStore certificate](https://www.servicenow.com/docs/r/platform-administration/dynamic-translation/create-jks-google.html).

  2. In the ServiceNow console **All** tab, search for **Google SCC ITSM** or **Google SCC SIR** and click **Guided Setup**.

  3. Click **Get Started**.

  4. In **Authentication Configuration** , click **Get Started**.




#### Create the X.509 certificate

  1. On the tasks page, in **Create X.509 Certificate** , click **Configure**.

  2. Enter the following information:

     * **Name** : a unique name for this certificate

     * **Format** : `PEM`

     * **Type** : **Java Key Store**

  3. Click the **Manage Attachments** icon and add the Java KeyStore certificate (`.jks` format) that you generated in Prepare the Java KeyStore certificate.

  4. Click the **Close** icon.

  5. Click **Submit**.

  6. On the tasks page, in **Create X.509 Certificate** , click **Mark as Complete**.




#### Create the JWT key

  1. On the tasks page, in **Create JWT Key** , click **Configure**.

  2. Enter the following information:

     * **Name** : a unique name for this key

     * **Signing Keystore** : the certificate name specified in Create the X.509 certificate

     * **Signing Algorithm** : `RSA 256`

     * **Signing Key** : the password for the `.jks` file created in Prepare the Java KeyStore certificate

  3. Click **Submit**.

  4. On the tasks page, in **Create JWT Key** , click **Mark as Complete**.




#### Create the JWT provider

  1. On the tasks page, in **Create JWT Provider** , click **Configure**.

  2. Enter the following information:

     * **Name** : a unique name for this provider

     * **Expiry Interval (sec)** : `60`

     * **Signing Configuration** : the JWT key name specified in Create the JWT key

  3. Click **Submit**.

  4. On the tasks page, in **Create JWT Provider** , click **Mark as Complete**.




#### Create the authentication configuration

  1. On the tasks page, in **Create Authentication Configuration** , click **Configure**.

  2. Enter the following information:

     * **Name** : a unique name for this configuration

     * **Organization ID** : the ID for your [organization](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization) in Google Cloud

     * **Base URL** : the URL for the [Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/reference/rest), typically `https://securitycenter.googleapis.com`

     * **Client Email** : the email address for the [IAM credentials](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys)

     * **JWT Provider** : the JWT provider name specified in Create the JWT provider

  3. Click **Submit**. An _Authentication Successful_ message appears.

  4. Close the **Create Authentication Configuration** window.

  5. On the tasks page, in **Create Authentication Configuration** , click **Mark as Complete**.




### Configure incident management for Security Command Center

To enable data collection from Security Command Center, complete the following steps. To support multiple organizations, complete this section for each organization.

To complete this task, you must be a ServiceNow system administrator.

#### Configure CI lookup rules

  1. In the ServiceNow console **All** tab, search for **Google SCC ITSM** or **Google SCC SIR** and click **Guided Setup**.

  2. Click **Get Started**.

  3. In **Incident Configuration** , click **Get Started**.

  4. To identify configuration items (such as assets) to add to incidents created from Security Command Center findings, use configure item (CI) lookup rules. For more information, see [CI Lookup Rules](https://docs.servicenow.com/bundle/sandiego-security-management/page/product/security-operations-common/concept/ci-identifier-rules.html).

Complete the following steps:

     1. On the tasks page, in **CI Lookup Rule** , click **Configure**.

     2. Click **New**.

     3. Enter the following information:

        * **Name** : a unique name for this lookup rule

        * **Lookup method** : either **Field Matching** or **Script**

        * **Order** : the order that the app evaluates this rule in, relative to other rules

        * **Source Field** : the field in the [findings data](https://docs.cloud.google.com/security-command-center/docs/reference/rest/v2/organizations.sources.findings#resource:-finding) that serves as input for this rule

        * **Search On Table** : if matching on a field, the table to find the field

        * **Search On Field** : if matching on a field, the field to match with the **Source Field**

        * **Script** : if using a script, enter the script

        * **Active** : select to enable this lookup rule

     4. Click **Submit**.

     5. Repeat this step for additional configuration items, as required.

     6. On the tasks page, in **CI Lookup Rule** , click **Mark as Complete**.




#### Create the ingestion configuration

  1. On the tasks page, in **Ingestion Configuration** , click **Configure**.

  2. Click **New**.

  3. Enter the following information:

Field  | Description   
---|---  
**Name** | A unique name for this record  
**Google SCC Configuration** | The authentication configuration that you created in Configure authentication with Security Command Center. You require one ingestion configuration for each authentication that you configured.  
**Recurring Data Collection** | Select to allow regular data ingestion from Security Command Center  
**Interval(second)** | The time interval between data updates from Security Command Center  
**One Time Data Collection** | Select to allow data ingestion from Security Command Center. One-time data collection doesn't support audit logs.  
**Collection Start Time** | The date to start data ingestion from Security Command Center  
  
Don't select **Active** until you have completed the remaining steps in this section.

  4. To add findings, complete these steps:

     1. In the **Findings** tab, select **Enabled**. When you enable findings, you also enable assets and sources automatically.

     2. Enter the following information:

Field | Description  
---|---  
**Findings Subscription Id** | For recurring data collections, the name of the Pub/Sub subscription for findings  
**Google SCC Finding Name** | The name of the incident field to populate with the finding name (for example, Description)  
**Google SCC Finding State** | The name of the incident field to populate with the finding state (for example, Description)  
**Google SCC Finding Indicator** | The name of the incident field to populate with the finding indicator (for example, Description)  
**Google SCC Finding Resource Name** | The name of the incident field to populate with the resource name for the finding (for example, Description)  
**Google SCC Finding External URI** | The name of the incident field to populate with the URL pointing to an external web page with more information about the finding, if available.  
**Apply Filters** | Available for one-time data collection, select to specify which projects, state, severity, or categories to include   
**Project Name** | The name of the project to retrieve findings from when **Apply Filters** is selected  
**State** | Whether the findings are active or inactive, when **Apply Filters** is selected  
**Severity** | The severity of the findings, when **Apply Filters** is selected  
**Category** | The category that you want to retrieve findings from, when **Apply Filters** is selected  
  5. To add assets, complete these steps:

     1. In the **Assets** tab, select **Enabled**.

     2. In the **Asset Subscription Id** field, for recurring data collections, enter the name of the Pub/Sub subscription for assets.

  6. To add security sources, in the **Sources** tab, select **Enabled**.

  7. To add audit logs, complete these steps:

     1. In the **Audit Logs** tab, select **Enabled**.

     2. In the **Audit Logs Subscription Id** field, for recurring data collections, enter the name of the Pub/Sub subscription for audit logs.

  8. Click **Submit**.

  9. If you get the message that the configuration is inactive, click **OK**. You activate the configuration in Activate the ingestion configuration.

  10. On the tasks page, in **Ingestion Configuration** , click **Mark as Complete**.




#### Define incident creation criteria

To create incidents from findings, complete these steps:

  1. On the tasks page, in **Incident Creation Criteria** (for Google Security Command Center ITSM) or **Security Incident Creation Criteria** (for Google Security Command Center SIR), click **Configure**.

  2. Click the name of the incident configuration that you created.

  3. In the **Ingestion Configuration** page, click the **Incident Creation Criteria List** (for Google Security Command Center ITSM) or **Security Incident Creation Criteria** (for Google Security Command Center SIR) tab.

  4. Click **New**.

  5. Enter the following information:

     * **Condition** : the dynamic condition under which an incident is created, based on field. For example, you can create incidents for findings with the **Severity** field set to **High**.

     * **Order** : the order for this condition, relative to other conditions.

  6. Click **Submit**.

  7. Repeat steps 4 through 6 for each condition that triggers incident creation.

  8. Close the **Ingestion Configuration** page.

  9. On the tasks page, in **Incident Creation Criteria** (for Google Security Command Center ITSM) or **Security Incident Creation Criteria** (for Google Security Command Center SIR), click **Mark as Complete**.




#### Define assignment group criteria

To assign incidents to a group, complete these steps:

  1. On the tasks page, in **Assignment Group Criteria** , click **Configure**.

  2. Click the name of the incident configuration that you created.

  3. In the **Ingestion Configuration** page, click the **Assignment Group Criteria List** tab.

  4. Click **New**.

  5. Enter the following information:

     * **Assignment Group** : the group that the incidents will be assigned to.

     * **Condition** : the dynamic condition that triggers incident assignment, based on a specified field. For example, you can assign incidents for findings with the **Finding Class** field set to **Misconfiguration**.

     * **Order** : the order for this condition, relative to other conditions.

  6. Click **Submit**.

  7. Repeat steps 4 through 6 for each group to assign incidents to.

  8. Close the **Ingestion Configuration** page.

  9. On the tasks page, in **Assignment Group Criteria** , click **Mark as complete**.




#### Activate the ingestion configuration

  1. On the tasks page, in **Activate Ingestion Configuration** , click **Configure**.

  2. Click the name of the incident configuration that you created.

  3. Select **Active**.

  4. To start collecting data, click **Collect Data**.

  5. Click **Update**.

  6. On the tasks page, in **Activate Ingestion Configuration** , click **Mark as Complete**.




## Verify data retrieval

To verify that ServiceNow retrieves data from Security Command Center, complete these steps.

To complete this task, you must be a ServiceNow system administrator.

  1. In the ServiceNow console, click the **All** tab.

  2. Search for **Google SCC ITSM** or **Google SCC SIR** and click **Ingestion Configuration**.

  3. Check the state to verify that the app collects data.

  4. Search for **Google SCC ITSM** or **Google SCC SIR** and click one of **Assets** , **Findings** , **Sources** , or **Audit Logs**. Verify that the app adds records for each enabled data type. If you configured automatic incident creation in the Findings configuration, verify that ServiceNow creates incidents related to each finding that matches your specified criteria.




## View the dashboards

The Google Security Command Center ITSM app lets you visualize the data from Security Command Center. It includes five dashboards: **Overview** , **Sources** , **Findings** , **Assets** , and **Audit Logs**.

You can access these dashboards in the ServiceNow console, from the **All > Google SCC ITSM > Dashboards** or the **All > Google SCC SIR > Dashboards** page.

### Overview dashboard

The **Overview** dashboard contains charts that display the total number of findings in your organization by severity level, category, and state. Security Command Center compiles findings from built-in services, such as [ Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics), [ Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview), [ Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview), and [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview) and any integrated services you enable.

To filter content, you can set the time range and organization ID.

Additional charts show which categories, projects, and assets are generating the most findings.

**Note:** You must be a [Security Command Center Premium](https://docs.cloud.google.com/security-command-center/docs/service-tiers) customer to receive findings from certain Security Command Center services, such as Event Threat Detection and Container Threat Detection.

### Assets dashboard

The **Assets** dashboard displays a chart of Google Cloud assets, categorized by asset type.

You can filter asset data by organization ID.

### Audit logs dashboard

The **Audit logs** dashboard displays a series of charts and tables that show [audit log](https://docs.cloud.google.com/logging/docs/audit) information. The dashboard includes administration activity, data access, system events, and policy-denied audit logs. The table includes the time, log name, severity, service name, resource name, and resource type.

You can filter the data by time range and organization ID.

### Findings dashboard

The **Findings** dashboard includes a table of the 1,000 most recent findings. The table columns include items such as category, asset name, source name, [security marks](https://docs.cloud.google.com/security-command-center/docs/how-to-security-marks-findings), [finding class](https://docs.cloud.google.com/security-command-center/docs/finding-classes), and [severity](https://docs.cloud.google.com/security-command-center/docs/finding-severity-classifications).

You can filter the data by time range, organization ID, severity, state, or finding class. If you set up automatic incident creation, the dashboard includes a link to the incident.

### Sources dashboard

The **Sources** dashboard shows a table of all your security sources. Table columns include name, display name, and description.

To filter content, you can set the organization ID.

## Create an incident manually

  1. Sign in to the ServiceNow console as the Google Security Command Center ITSM or Google Security Command Center SIR administrator.

  2. In the **All** tab, search for **Google SCC ITSM** or **Google SCC SIR** and click **Findings**.

  3. Click the finding that you want to create an incident for.

  4. On the findings page, for Google Security Command Center ITSM, click **Create Incident** and for Google Security Command Center SIR, click **Create Security Incident**.




## Mute or unmute findings

The Google Security Command Center SIR app provides mute and unmute functionality for findings.

**Role required:** `x_goog_scc_sir.Google_SCC_SIR_Admin` or `x_goog_scc_sir.Google_SCC_SIR_User`

To mute or unmute findings, complete the following steps:

  1. Sign in to the ServiceNow instance.
  2. Navigate to **Google SCC SIR > Findings**.
  3. Open a finding to change its mute status. 
     * If the finding mute state is **Undefined** or **Unmuted** , the **Mute Finding** button is visible.
     * If the finding mute state is **Muted** , the **Unmute Finding** button is visible.
  4. Click **Mute Finding** or **Unmute Finding**. A dialog appears.
  5. Enter a description for muting or unmuting the finding. 
     * If you select multiple findings from the list view, the description applies to all selected findings.
  6. Click **OK**. The mute state of the finding changes in Security Command Center. 
     * The description is visible in the security marks of the finding in the Google Cloud console and includes the ServiceNow username.
     * If the mute state is changed in Security Command Center, the new state is reflected in ServiceNow after the next data collection.



## Create a mute rule

The Google Security Command Center SIR app lets you create mute rules. If you create a mute rule in ServiceNow, future findings that match the criteria are muted. If you delete the rule in ServiceNow, it is also deleted in Security Command Center.

**Role required:** `x_goog_scc_sir.Google_SCC_SIR_Admin` or `x_goog_scc_sir.Google_SCC_SIR_User`

To create a mute rule, complete the following steps:

  1. Sign in to the ServiceNow instance.
  2. Navigate to **Google SCC SIR > Mute Rule**.
  3. Click **New**.
  4. Configure the following fields:

     * **Name** : A name for the mute rule. When you submit the mute rule, the name is prefixed with `servicenow-USER_NAME`, where `USER_NAME` is the username of the user who created the mute rule.

     * **Description** : A description of the mute rule.

     * **Authentication Configuration** : Select an authentication configuration to connect to Security Command Center.

     * **Query** : Enter a filter query for the mute rule.

     * **Type** : Select one of the following:

       * **Static** : Mutes only future findings.
       * **Dynamic** : Mutes both existing and future findings.
  5. Click **Create Mute Rule**. An informational message and application log entry are created based on the response (success or failure).




## Create a CI lookup rule manually

The Google Security Command Center SIR app lets you create configuration item (CI) lookup rules manually.

**Role required:** `x_goog_scc_sir.Google_SCC_SIR_Admin`

To create a CI lookup rule, complete the following steps:

  1. Sign in to the ServiceNow instance.
  2. Navigate to **Google SCC SIR > CI Lookup Rules**.
  3. Click **New**.
  4. Fill the **Name** and **Order** fields.
  5. Select the **Active** checkbox.
  6. For **Lookup method** , select either **Field Matching** or **Script**.
  7. For **Source Field** , enter the field in the findings data to use as input.
  8. In the **Search On Field** and **Search On Table** fields, enter the values to use for the lookup.
  9. For **Description** , enter a description for the rule.
  10. Define the rule details: 
     * For field matching rules, specify the table and field to search in the Configuration Management Database (CMDB). The field must be a string or a number.
     * For script rules, implement the script using the template comments. The script must return the system ID (`sys_id`) of the matched configuration item.
  11. Click **Submit**.



## View the action log

The Google Security Command Center SIR app provides an action log that records user actions related to muting or unmuting findings and updates to mute rules.

**Role required:** `x_goog_scc_sir.Google_SCC_SIR_Admin`

To view the action log, navigate to **Google SCC SIR > Action Log**. The log displays the following information:

  * **Action** : The action performed (for example, creating, updating, or deleting a mute rule, or muting or unmuting findings)
  * **User** : The username of the person who performed the action
  * **Record** : A reference to the affected record
  * **Date** : The date and time when the action was performed



## Change a finding state

You can change a finding state from active to inactive or from inactive to active.

  1. In the ServiceNow console, on the **All** tab, search for **Google SCC ITSM** or **Google SCC SIR** and click **Findings**.

  2. Click the finding that you want to change the state for.

  3. In the findings page, click **Active Finding** or **Inactive Finding**.

  4. Click **OK**.




## Uninstall the apps

To complete this task, you must be a ServiceNow system administrator.

  1. In the ServiceNow console **All** tab, search for **System Applications** and click **All Available Applications > All**.

  2. Select **Installed**.

  3. Select **Google Security Command Center ITSM** or **Google Security Command Center SIR** and click **Uninstall**.




## View application logs

To view the logs for the app, complete the following steps:

  1. Sign in to the ServiceNow console as the Google Security Command Center ITSM or Google Security Command Center SIR administrator.

  2. In the **All** tab, search for **Google SCC ITSM** or **Google SCC SIR** and click **Administration > Application Logs**.




## Troubleshooting

This section covers how to resolve common issues that you might encounter when configuring or using the ServiceNow integration.

### Application cannot reconnect after three attempts

If the findings API call returns an HTTP `429` or `5xx` status code, the application retries three times, waiting 60 seconds between attempts. If the third retry fails, the process fails. To change the response time, complete the following steps:

  1. Sign in to the ServiceNow console as the Google Security Command Center ITSM or Google Security Command Center SIR administrator. For more information about these accounts, see Create users for the app.

  2. In the **All** tab, search for **Google SCC ITSM** or **Google SCC SIR** and click **System Properties**.

  3. Set the **Number of max retries for an invalid response from Google SCC (in numbers)** field to a number that is greater than 3.

  4. Click **Save**.




### Attachment isn't supported

  1. Sign in to the ServiceNow console as a system administrator.

  2. In the **All** tab, search for **System Applications** and click **Security**.

  3. In the **Security System Properties** page, verify that the **List of file extensions (comma-separated) that can be attached to documents via the attachment dialog** field includes the extension that you want to attach without a leading dot—for example, `xlsx,docx`. If the field is blank, all extensions are allowed.




### Cannot add more than 250 work notes or activities to an incident

  1. Sign in to the ServiceNow console as a system administrator.

  2. In the navigation bar, search for **sys_properties.list**.

  3. In the **System Properties** window, create a filter **Name is glide.history.max_entries**.

  4. Click **Run**.

  5. In the property window, set **Value** to a number that is greater than 250.

  6. Click **Update**.




### Cannot create a new user

If you use the Rome release version, see [Create a user](https://docs.servicenow.com/bundle/rome-platform-administration/page/administer/users-and-groups/task/t_CreateAUser.html) for instructions.

### Cannot fetch data

This issue can occur when fetching findings, assets, sources, or audit logs if the "Starting data ingestion for profile: `PROFILE_NAME`" message appears.

  1. Sign in to the ServiceNow console as the Google Security Command Center ITSM or Google Security Command Center SIR administrator.

  2. In the **All** tab, search for **Google SCC ITSM** or **Google SCC SIR** and click **Administration > System Properties**.

  3. Verify that the following fields aren't empty:

     * **Number of max retries for an invalid response from Google SCC (in numbers)**

     * **Time window to wait before making another request after reaching request limit (in milliseconds)**

  4. If the fields are empty, set the values as follows:

     * Set **Number of max retries for an invalid response from Google SCC (in numbers)** field to `3`.

     * Set **Time window to wait before making another request after reaching request limit (in milliseconds)** to `60000`.

  5. Click **Save**.




### Cannot install the app from the ServiceNow Store

  1. Verify that you are logged in as the ServiceNow system administrator.

  2. In the **All** tab, search for **System Applications** and click **All Available Applications > All**.

  3. Check whether the app appears in the **Installed** tab.




### `ECC Queue Timeout Error` message in Application Logs

**Role required:** `admin`

**Prerequisites:**

  * You must be signed in as a system administrator.
  * You must be in the **Global** scope of ServiceNow.



To resolve this issue, complete the following steps:

  1. Switch the **Application Scope** to **Global**.
  2. Navigate to the **System Property** table by entering `sys_properties.list` in the navigation filter.
  3. Click **New** to create a system property.
  4. Enter the following values: 
     * **Name** : `com.glide.ecc.agent_response_timeout`
     * **Value** : `3600` (or higher if needed)
     * **Type** : `integer`
  5. Click **Submit**.



### `Maximum execution time exceeded` message on dashboard widgets

If you see this message on dashboard widgets, you might need to increase the transaction quota. For more information, see the ServiceNow knowledge base article [Widget cancelled - Maximum execution time exceeded](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0715793) (requires ServiceNow authentication).

### Unable to collect data

If you encounter errors during data collection, verify the system properties.

**Role required:** `x_goog_scc_sir.Google_SCC_SIR_Admin`

  1. Sign in to the ServiceNow instance.
  2. Navigate to **Google SCC SIR > System Properties**.
  3. Verify that the following fields aren't empty: 
     * **Number of max retries for invalid response from Google SCC (in numbers)**
     * **Time window to wait before making another request after reaching request limit (in milliseconds)**
  4. If the fields are empty, set the values as follows: 
     * Set **Number of max retries...** to `3`.
     * Set **Time window to wait...** to `60000`.
  5. Click **Save**.



## What's next

  * Learn more about setting up [finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications) in Security Command Center.

  * Read about [filtering finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-api-filter-notifications) in Security Command Center.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
