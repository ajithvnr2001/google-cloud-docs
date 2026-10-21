---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-alert-center/
title: Integrate Google Alert Center with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:48:08.103615+00:00
---

# Integrate Google Alert Center with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-alert-center/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Google Alert Center with Google SecOps

This document explains how to integrate the Google Workspace Alert Center with Google Security Operations.

**Important:** In the Google SecOps platform, the integration for the alert center is called _Google Alert Center_.

## Use cases

The **Google Alert Center** integration uses Google SecOps capabilities to support the following use cases:

  * **Phishing campaign response** : Ingest Alert Center notifications regarding potential phishing targeting your organization. Trigger automated workflows to investigate emails, block malicious URLs, and quarantine affected accounts.

  * **Data exfiltration containment** : Trigger automated incident response when suspicious data movement is detected. Isolate affected systems and initiate forensic analysis.

  * **Automated malware remediation** : Quarantine infected devices identified by Google Workspace alerts and initiate mandatory malware scans or patch deployments.

  * **Vulnerability management** : Automatically process alerts about newly discovered vulnerabilities affecting your Google Workspace environment to prioritize patching and inform relevant teams.




## Before you begin

Before you configure the Google Alert Center integration in Google SecOps, complete the following prerequisite steps:

  1. Enable the Google Workspace Alert Center API.

  2. Create a service account.

  3. Configure a JSON key.

  4. Delegate domain-wide authority.




### Enable the Google Workspace Alert Center API

Enabling the API lets Google SecOps communicate with your Google Workspace security data.

  1. In the Google Cloud console, go to the **Library** page.

[Go to Library](https://console.cloud.google.com/apis/library/alertcenter.googleapis.com)

  2. Click **Enable**.




### Create a service account

A service account serves as the secure identity for the integration to access your Google Workspace data.

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click **add Create service account**.

  3. Provide a name (such as "SecOps Alert Center Integration") and description.

  4. Click **Create and continue**. 

  5. Skip the optional role assignment steps and click **Done**.

  6. Locate the service account in the list and copy its **Client ID** (Unique ID) and **Email address**.




### Configure a JSON key

This integration uses a static JSON key file for authentication.

  1. Select your service account in the Google Cloud console and go to the **Keys** tab.

  2. Click **Add key > Create new key**.

  3. Select **JSON** and click **Create**. The key file automatically downloads to your computer.

  4. Copy the full content of this file and paste it into `Service Account JSON Secret` during integration configuration.




### Delegate domain-wide authority

Granting domain-wide authority lets the service account access your users' alerts by impersonating an administrator.

  1. From your domain's Google Admin console, go to **Main menu > Security > Access and data control > API controls**.

  2. In the **Domain wide delegation** pane, select **Manage Domain Wide Delegation**.

  3. Click **Add new**.

  4. In the **Client ID** field, enter the **Unique ID** (client ID) you copied from the service account.

  5. In the **OAuth Scopes** field, enter the following scope:
         
         https://www.googleapis.com/auth/apps.alerts
         

  6. Click **Authorize**.




## Integration parameters

The **Google Alert Center** integration requires the following parameters:

Parameter | Description  
---|---  
`Service Account JSON Secret` |  Required. The full content of the service account key JSON file you downloaded.  
`Impersonation Email Address` |  Required. The email address of a user with administrator privileges in your Google Workspace domain. The integration uses domain-wide delegation to impersonate this user and retrieve alerts.  
`Verify SSL` |  Optional. If selected, the integration validates the SSL certificate when connecting to the Google Alert Center server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Delete Alert

Use the **Delete Alert** action to delete an alert in the alert center.

After deleting an alert, you can recover it for 30 following days. You can't recover an alert that you deleted more than 30 days ago.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Delete Alert** action requires the following parameters:

Parameter | Description  
---|---  
`Alert ID` | _Required_ The ID of the alert to delete.  
  
#### Action outputs

The **Delete Alert** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Delete Alert** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully deleted alert with ID RECORD_ID in the alert center.` `Alert with ID RECORD_ID doesn't exist in the alert center.` | The action succeeded.  
`Error executing action "Delete Alert". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Delete Alert** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test the connectivity to the alert center.

This action doesn't run on Google SecOps entities.

#### Action inputs

None.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the alert center server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the alert center server! Error is ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### Google Alert Center – Alerts Connector

Use the **Google Alert Center – Alerts Connector** to retrieve information about alerts from the alert center.

**Important:** **Data ingestion limitations**

The data ingested into Google SecOps is limited by the fields provided by the underlying [Google Workspace Alert Center API](https://developers.google.com/admin-sdk/alertcenter/reference/rest/v1beta1/alerts).

Some fields visible in the Google Alert Center UI (such as **Username**) aren't returned by the API and won't be present in the ingested cases. This is intended behavior. See Sample event JSON to verify available fields.

The dynamic list filter works with the `type` parameter.

#### Connector inputs

The **Google Alert Center – Alerts Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | _Required_ The name of the field where the product name is stored.The default value is `source`.  
`Event Field Name` | _Required_ The field name used to determine the event name (subtype).The default value is `type`.  
`Environment Field Name` | _Optional_ The name of the field where the environment name is stored.If the environment field isn't found, the environment is set to the default environment.The default value is `""`.  
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`PythonProcessTimeout` | _Required_ The timeout limit in seconds for the Python process that runs the current script.The default value is `180`.  
`Service Account JSON Secret` | _Required_ The full JSON content of the service account file that you used for authentication to the alert center.  
`Impersonation Email Address` | _Required_ The email address to impersonate a user with access to the alert center. To configure this parameter, enter the administrator email address. The data from the alert center is available only to administrators.  
`Verify SSL` | _Optional_ If selected, the integration verifies that the SSL certificate for connecting to the alert center is valid. Selected by default.  
`Max Hours Backwards` | _Optional_ A number of hours before the first connector iteration to retrieve responses from. This parameter applies either to the initial connector iteration after you enable the connector for the first time or the fallback value for an expired connector timestamp. The default value is 1 hour.  
`Max Alerts To Fetch` | _Optional_ The maximum number of alerts to retrieve for every connector iteration.The maximum number is 100.  
`Lowest Severity To Fetch` | _Optional_ The lowest severity of alerts to retrieve.  
`Use whitelist as a blacklist` | _Optional_ If selected, the connector uses the dynamic list as a blocklist. Not selected by default.  
`Proxy Server Address` | _Optional_ The address of the proxy server to use.  
`Proxy Username` | _Optional_ The proxy username to authenticate with.  
`Proxy Password` | _Optional_ The proxy password to authenticate with.  
  
#### Connector Rules

The following rules define the operational logic, data processing behavior, and safety mechanisms of the connector.

  * **Proxies** : The connector supports proxies.

  * **Event creation** : If an alert contains a `data/messages` key (a list of JSON objects), the connector creates a separate event for each object in the list.

  * **Safety timeout** : If the connector reaches 90% of its execution timeout (based on `PythonProcessTimeout`), it stops and doesn't create a new alert for that iteration to prevent partial data ingestion.

  * **Watermark management** : The connector tracks processed alerts using `alertId`. It stores up to 1000 IDs in `ids.json`. When the limit is exceeded, it removes the oldest 100 IDs.




#### Sample event JSON

The following JSON sample represents the typical response structure from the Google Alert Center API, illustrating the specific data fields available for ingestion.
    
    
    {
        "customerId": "038judqw",
        "alertId": "e37415f1-7c39-44a5-b43c-4f8159638a2a",
        "createTime": "2020-07-22T11:50:08.353Z",
        "startTime": "2020-07-22T10:54:54.059475Z",
        "endTime": "2020-07-22T11:46:51.020063Z",
        "type": "User reported phishing",
        "source": "Gmail phishing",
        "data": {
            "@type": "[type.googleapis.com/google.apps.alertcenter.type.MailPhishing](https://type.googleapis.com/google.apps.alertcenter.type.MailPhishing)",
            "domainId": {
                "customerPrimaryDomain": "smplylab.com"
            },
            "maliciousEntity": {
                "fromHeader": "crazywiz7@abv.bg"
            },
            "messages": [
                {
                    "messageId": "1753474999.350456.1595412914645@nm22.abv.bg",
                    "messageBodySnippet": " eicar com http malware wicar org data ms14_064_ole_not_xp html",
                    "md5HashSubject": "c93d4454877e844fdfcb4401472204f2",
                    "subjectText": "Re: App Store - Support.      17/07/2020 12:50:36",
                    "attachmentsSha256Hash": [
                        "77c2aed70c3b20c50dbf071f8688580e02463c213e7a65ccab1acc2f8a9769a3",
                        "f5e1b1bf12b71c54f68a719e0c45df5806a8b8d57bf3967d9bd4a071cfc5abbe"
                    ],
                    "recipient": "lab3@smplylab.com",
                    "date": "2020-07-22T10:54:54.059475Z"
                }
            ]
        },
        "securityInvestigationToolLink": "[admin.google.com/ac/ac/investigate?alert=CiRlMzc0MTVmMS03YzM5LTQ0YTUtYjQzYy00ZjgxNTk2MzhhMmE](https://admin.google.com/ac/ac/investigate?alert=CiRlMzc0MTVmMS03YzM5LTQ0YTUtYjQzYy00ZjgxNTk2MzhhMmE)",
        "metadata": {
            "customerId": "038judqw",
            "alertId": "e37415f1-7c39-44a5-b43c-4f8159638a2a",
            "status": "NOT_STARTED",
            "updateTime": "2020-07-22T11:50:08.353Z",
            "severity": "HIGH",
            "etag": "rrXycg7VpUA="
        },
        "updateTime": "2020-07-22T11:50:08.353Z",
        "etag": "rrXycg7VpUA="
    }
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
