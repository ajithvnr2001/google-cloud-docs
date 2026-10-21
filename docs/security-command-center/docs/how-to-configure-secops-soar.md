---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-configure-secops-soar/
title: Send Security Command Center data to Google Security Operations SOAR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:09.144978+00:00
---

# Send Security Command Center data to Google Security Operations SOAR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-configure-secops-soar/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Send Security Command Center data to Google Security Operations SOAR Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, and Premium [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

This page explains how to automatically send Security Command Center findings, assets, audit logs, and security sources to Google Security Operations SOAR. It also describes how to manage the exported data.

**Note:** These instructions are for customers that have a [Google SecOps package](https://cloud.google.com/security/products/security-operations#pricing). If you use Google SecOps SOAR as part of the Enterprise (Deprecated) service tier of Security Command Center, then you don't need to complete these steps.

Before you begin, ensure that the required Security Command Center and Google Cloud services are properly configured and enable Google SecOps SOAR to access findings, audit logs, and assets in your Security Command Center environment. For more information on the Security Command Center integration for Google SecOps SOAR, see [Security Command Center](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-security-command-center) in the Google Security Operations documentation.

## Configure authentication and authorization

Before connecting to Google SecOps SOAR, you need to create an Identity and Access Management service account and grant to it IAM roles at both the organization and project levels.

### Create a service account and grant IAM roles

In this document, this service account is also called the _user service account_. The following steps use the Google Cloud console. For other methods, see the links at the end of this section.

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

        * **Security Center Admin Viewer** (`roles/securitycenter.adminViewer`) 
        * **Security Center Notification Configurations Editor** (`roles/securitycenter.notificationConfigEditor`)
        * **Organization Viewer** (`roles/resourcemanager.organizationViewer`)
        * **Cloud Asset Viewer** (`roles/cloudasset.viewer`) 
     3. Click **Save**. The service account appears on the **Permissions** tab of the **IAM** page under **View by principals**.

By inheritance, the service account also becomes a principal in all child projects of the organization. The roles that are applicable at the project level are listed as inherited roles.




For more information about creating service accounts and granting roles, see the following topics:

  * [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts)
  * [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access)



### Create a service account for impersonation

In this document, this service account is also called the _SOAR service account_. Create a service account to impersonate the user service account and its permissions.

  1. In the Google SecOps SOAR console, navigate to **Response** , and then click **Integrations setup**.

  2. In the **Integrations setup** page, click **Create a new instance**. The **Add instance** dialog opens.

  3. In the **Integrations** list, select **Google Security Command Center** and click **Save**. The **Google Security Command Center - Configure Instance** dialog opens.

  4. In the **Workload Identity Email** field, specify the service account email ID.

  5. Click **Save**.




### Provide the credentials to Google SecOps SOAR

Depending on where you are hosting Google SecOps SOAR, how you provide the IAM credentials to Google SecOps SOAR differs.

  * If you are hosting Google SecOps SOAR in Google Cloud, the user service account that you created and the organization level roles that you granted to it are available automatically by inheritance from the parent organization.
  * If you are hosting Google SecOps SOAR in your on-premises environment, [create a key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) for the user service account that you created. You need the service account key JSON file to complete this task. To learn about best practices for storing your service account keys securely, see [Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).



## Configure notifications

Complete these steps for each Google Cloud organization that you want to import Security Command Center data from.

  1. [Set up finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications) as follows:

     1. Enable the Security Command Center API.
     2. Create a [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) topic for findings.
     3. Create a `NotificationConfig` object that contains the filter for findings that you want to export. The `NotificationConfig` must use the Pub/Sub topic you created for findings.
  2. [Enable the Cloud Asset API](https://console.cloud.google.com/apis/library/cloudasset.googleapis.com) for your project.




You need your organization ID, project ID, and the Pub/Sub subscription ID from this task to configure Google SecOps SOAR. To retrieve your organization ID and project ID, see [Retrieving your organization ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id) and [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects), respectively.

## Configure Google SecOps SOAR

Google SecOps SOAR enables enterprises and managed security service providers (MSSPs) to gather data and security alerts from different sources by combining orchestration and automation, threat intelligence, and incident response.

To use Security Command Center with Google SecOps SOAR, complete the following steps:

  1. In the Google SecOps SOAR console, navigate to **Marketplace** , and then click **Integrations**.

  2. Search for `Google Security Command Center`, and install the Security Command Center integration that appears in the search results.

  3. On the **Google Security Command Center** integration, click **Configure**. The **Google Google Security Command Center - Configure Instance** dialog opens.

  4. Optional: To create a new environment or to edit the environment configuration, click **Settings screen**. The **Environments** page opens in a new tab.

  5. On the **Environments** page, select the environment for which you want to configure the integration instance.

  6. In the selected environment, click **Create a new instance**. The **Add instance** dialog opens.

  7. In the **Integrations** list, select **Google Security Command Center** and click **Save**. The **Google Security Command Center - Configure Instance** dialog opens.

  8. Specify the configuration parameters and click **Save**.

**Parameter** | **Description** | **Required**  
---|---|---  
API Root | API root of the Security Command Center instance. For example, `securitycenter.googleapis.com`. | Yes  
Organization ID | ID of the organization whose findings you want to export. | No  
Project ID | ID of the project to be used in the Security Command Center integration. | No  
Quota Project ID | ID of your Google Cloud project for Google Cloud API usage and billing. | No  
Location ID | ID of the location to be used in the Security Command Center integration. Default location ID is global. | No  
User's Service Account |  Service account that you created in Create a service account and grant IAM roles. If you are hosting Google SecOps SOAR in your on-premises environment, then provide the service account key ID and all the content of the service account JSON file.  | Yes  
Workload Identity Email | Email that you created in Create a service account for impersonation. It is a service account client email to replace the usage of the user service account that can be used for impersonation. The SOAR service account must be granted the `Service Account Token Creator` IAM role on the user service account. | Yes  
Verify SSL | Enable to verify that the SSL certificate used for the connection to the Security Command Center server is valid. | Yes  
  9. To verify that the integration is configured correctly, click **Test**.

  10. After successful verification, click **Save**.




## Upgrade the Google Security Command Center integration

To upgrade the Google Security Command Center integration, complete the following steps:

  1. In the Google SecOps SOAR console, navigate to **Marketplace** , and then click **Integrations**.

  2. Search for the **Google Security Command Center** integration and click **Upgrade to VERSION_NUMBER**.


**Note:** If the integration has a connector configured, the connector needs to be manually updated after the integration is upgraded. To update the connector, go to **Settings** > **Ingestion** > **Connectors** , select the connector that you want to update, and click **Update**.

## Work with findings and assets

Google SecOps SOAR uses connectors to ingest alerts from a variety of data sources into the platform.

### Fetch Security Command Center alerts for analysis in Google SecOps SOAR

You need to configure a connector to pull information about findings from Security Command Center. To configure the connector, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

Set the following parameters in Google SecOps SOAR to configure the Google Security Command Center - Findings connector.

Parameter | Type | Default value | Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Source field name to retrieve the product field name.  
Event Field Name | String | type | Yes | Source field name to retrieve the event field name.  
Environment Field Name | String | Empty | No | Name of the field where the environment name is stored. If the environment field name isn't specified, the default environment is selected.  
Environment Regex Pattern | String | .* | No | A regular expression pattern to run on the value found in the **Environment Field Name** field. Default is .* to catch all and return the value unchanged. This parameter is used to allow the user to manipulate the environment field through regular expression logic. If the regular expression pattern is null or empty, or the environment value is null, the default environment is selected.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String |  | Yes | API root of the Security Command Center instance. For example, `securitycenter.googleapis.com`.  
Organization ID | String |  | No | ID of the organization that should be used in Google Security Command Center integration.  
User's Service Account | Password |  | Yes | Service account that you created in Create a service account and grant IAM roles. If you are hosting Google SecOps SOAR in your on-premises environment, then provide the service account key ID and all the content of the service account JSON file.  
Finding Class Filter | CSV | Threat, Vulnerability, Misconfiguration, SCC_Error, Observation | No |  Finding classes that should be ingested. Possible values are: 

  * Threat
  * Vulnerability
  * Misconfiguration
  * SCC_Error
  * Observation

If nothing is provided, findings from all classes are ingested.   
Lowest Severity To Fetch | String | High | No |  The lowest severity that is used to fetch findings. Possible values are: 

  * Low
  * Medium
  * High
  * Critical

Note: If finding with undefined severity is ingested, it has the medium severity. If nothing is provided, findings with all severities are ingested.   
Max Hours Backwards | Integer | 1 | No | Number of hours from where to fetch findings. Maximum limit is 24.  
Max Findings To Fetch | Integer | 100 | No | Number of findings to process per one connector iteration. Maximum limit is 1000.  
Use dynamic list as an exclude list | Checkbox | Disabled | Yes | Enable the dynamic list as an exclude list.  
Verify SSL | Checkbox | Disabled | Yes | Enable to verify that the SSL certificate for the connection to the Security Command Center server is valid.  
Proxy Server Address | String |  | No | The address of the proxy server to use.  
Proxy Username | String |  | No | The proxy username to authenticate with.  
Proxy Password | Password |  | No | The proxy password to authenticate with.  
  
### Enrich assets

To enable a security investigation, Google Security Operations ingests contextual data from different sources, performs analysis on the data, and provides additional context about artifacts in a customer environment.

To enrich assets using information from Security Command Center, add the enrich assets action to a playbook in Google SecOps SOAR and run the playbook. For more information, see [Adding an action](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-actions-in-playbooks#adding-an-action).

To configure this action, set the following parameters:

Parameter | Type | Default value | Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name to retrieve the product field name.  
  
### List alert vulnerabilities

To list vulnerabilities related to the entities in Security Command Center, add the list asset vulnerabilities action to a playbook in Google Security Operations SOAR and run the playbook. For more information, see [Adding an action](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-actions-in-playbooks#adding-an-action).

To configure this action, set the following parameters:

Parameter | Type | Default value | Mandatory | Description  
---|---|---|---|---  
Asset Resource Names | CSV |  | Yes | Specify a comma-separated list of resource names of the assets for which you want to return data.  
Timeframe | DDL | All Time | No |  Specify the timeframe for the vulnerabilities or misconfiguration search. Possible values are: 

  * Last Week
  * Last Month
  * Last Year
  * All Time

  
Record Types | DDL | Vulnerabilities + Misconfigurations | No |  Specify the type of record that should be returned. Possible values are: 

  * Vulnerabilities
  * Misconfigurations
  * Vulnerabilities + Misconfigurations

  
Output Type | DDL | Statistics | No |  Specify the type of output that should be returned in the JSON result for the asset. Possible values are: 

  * Statistics
  * Data
  * Statistics + Data

  
Max Records To Return | String | 100 | No | Specify the number of records to return per record type per assets.  
  
### Update findings

To update findings in Security Command Center, add the update findings action to a playbook in Google SecOps SOAR and run the playbook. For more information, see [Adding an action](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-actions-in-playbooks#adding-an-action).

To configure this action, set the following parameters:

Parameter | Type | Default value | Mandatory | Description  
---|---|---|---|---  
Finding Name | CSV | `organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID` | Yes | Specify a comma-separated list of finding names that you want to update.  
Mute Status | DDL |  | No |  Specify the mute status for the finding. Possible values are: 

  * Mute
  * Unmute

  
State Status | DDL |  | No |  Specify the state status for the finding. Possible values are: 

  * Active
  * Inactive

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
