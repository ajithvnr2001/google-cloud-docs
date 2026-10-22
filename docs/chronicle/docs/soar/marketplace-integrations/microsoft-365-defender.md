---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-365-defender/
title: Microsoft 365 Defender \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:38.248528+00:00
---

# Microsoft 365 Defender  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-365-defender/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Microsoft 365 Defender

**Important:** In the Google SecOps platform, the Microsoft Defender For XDR integration is called _Microsoft 365 Defender_.

This document describes how to integrate Microsoft Defender For XDR with Google Security Operations.

## Use cases

Integrating Microsoft Defender For XDR with Google SecOps can help you solve the following use cases:

  * **Automated incident response:** use the Google SecOps capabilities to automatically isolate the affected endpoint and initiate a scan for further compromise.

  * **Phishing investigation and remediation:** use the Google SecOps capabilities to automatically extract relevant information, such as the sender, subject, and attachments, and enrich it with threat intelligence data.

  * **Vulnerability management:** use the Google SecOps capabilities to automate vulnerability scanning and remediation workflows.

  * **Compliance reporting and auditing:** use the Google SecOps capabilities to automate the collecting and reporting of security data from Microsoft Defender For XDR, simplifying compliance audits, and demonstrating adherence to security standards.

  * **Alert prioritization and triage:** use the Google SecOps capabilities to analyze alerts from Microsoft Defender For XDR and prioritize them based on severity and potential impact.

  * **Automated malware analysis:** use the Google SecOps capabilities to automatically submit the sample of a malware that Microsoft 365 Defender has detected to a sandbox environment for dynamic analysis.




## Before you begin

Before configuring the integration in the Google SecOps platform, complete the following steps:

  1. Create the Microsoft Entra application.

  2. Configure the API permissions for your app.

  3. Create a client secret.




### Create the Microsoft Entra application

To create the Microsoft Entra application, complete the following steps:

  1. Sign in to the [Azure portal](https://portal.azure.com/) as a user administrator or a password administrator.

  2. Select **Microsoft Entra ID**.

  3. Go to **App registrations > New registration**.

  4. Enter the name of the application.

  5. Click **Register**.

  6. Save the **Application (client) ID** and **Directory (tenant) ID** values to use them later when configuring the integration parameters.




### Configure the API permissions

To configure the API permissions for the integration, complete the following steps:

  1. In the Azure portal, go to **Manage > API Permissions > Add a permission**.

  2. In the **Request API permissions** window, select **APIs my organization uses**.

  3. Select **Microsoft Graph > Application permissions**.

  4. Select the following permissions:

     * `SecurityAlert.Read.All`
     * `SecurityIncident.ReadWrite.All`
  5. Click **Add permissions**.

  6. In the **Request API permissions** window, select **APIs my organization uses**.

  7. Select **Microsoft Threat Protection > Application permissions**.

  8. Select the following permission:

     * `ThreatHunting.Read.All`
  9. Click **Add permissions**.

  10. Click **Grant admin consent for` YOUR_ORGANIZATION_NAME`**.

When the **Grant admin consent confirmation** dialog appears, click **Yes**.




### Create a client secret

To create a client secret, complete the following steps:

  1. Navigate to **Certificates and secrets > New client secret**.

  2. Provide a description for a client secret and set its expiration deadline.

  3. Click **Add**.

  4. Save the value of the client secret (not the secret ID) to use it as the `Client Secret` parameter value when configuring the integration.

The client secret value is only displayed once.




## Integrate Microsoft Defender For XDR with Google SecOps

**Important:** If you make any changes to the **Application Permissions** or **API Permissions** in your Microsoft Entra ID (Azure AD) App Registration after configuring this integration (for example, adding a new permission for a job to run), you must regenerate and update your credentials in Google SecOps. 

This typically means:

  * Generating a new client secret in your App Registration.
  * Updating the client secret (and regenerating the refresh token, if applicable) in the Google SecOps integration configuration.



Failure to update will prevent new permissions from being applied, causing actions to fail.

The Microsoft Defender For XDR integration requires the following parameters:

Parameter | Description  
---|---  
`Login API Root` | _Required_ The login API root of the Microsoft Defender For XDR instance.The default value is `https://login.microsoftonline.com`.  
`Graph API Root` | _Required_ The API root of the Microsoft Graph service. The default value is `https://graph.microsoft.com`.  
`API Root` | _Required_ The API root of the Microsoft Defender For XDR instance. The default value is `https://api.security.microsoft.com`.  
`Tenant ID` | _Required_ The Microsoft Entra ID (tenant ID) value of your Microsoft Entra ID account.  
`Client ID` | _Required_ The application (client) ID value of your Microsoft Entra ID account.  
`Client Secret` | _Required_ The client secret value of the Microsoft Entra ID application.  
`Verify SSL` | _Optional_ If selected, the integration verifies that the SSL certificate for connecting to the Microsoft Defender For XDR server is valid. Selected by default.  
  
For instructions about configuring an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage if needed. After you configure an integration instance, you can use it in playbooks. For more information about configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [Respond to pending actions from your workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action).

### Add Comment To Incident

Use the **Add Comment To Incident** action to add a comment to an incident in Microsoft Defender For XDR.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Add Comment To Incident** action requires the following parameters:

Parameter | Description  
---|---  
`Incident ID` | _Required_ The ID of the incident to add the comment to.  
`Comment` | _Required_ The comment to add to the incident.  
  
#### Action outputs

The **Add Comment To Incident** action provides the following outputs:

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

The **Add Comment To Incident** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added comment to incident INCIDENT_ID in Microsoft Defender XDR.` | The action succeeded.  
`Error executing action "Add Comment To Incident". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Comment To Incident** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Execute Custom Query

Use the **Execute Custom Query** action to execute a custom hunting query in Microsoft Defender For XDR.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Execute Custom Query** action requires the following parameters:

Parameter | Description  
---|---  
`Query` | _Required_ The query to execute in Microsoft Defender For XDR for result filtering.  
`Max Results To Return` | _Optional_ The maximum number of results to return from the query. The default value is `50`.  
  
#### Action outputs

The **Execute Custom Query** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Execute Custom Query** action:
    
    
    {"Results": [
        {
            "Timestamp": "2021-04-12T07:25:00Z",
            "AlertId": "fa7a318954-6c4c-eaab-3200-08d8fd82af35",
            "Title": "CC_Sensitive information",
            "Category": "InitialAccess",
            "Severity": "Medium",
            "ServiceSource": "Microsoft Defender for Office 365",
            "DetectionSource": "Microsoft Defender for Office 365",
            "AttackTechniques": ""
        }
    ]}
    

##### Output messages

The **Execute Custom Query** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully executed query "QUERY" in Microsoft 365 Defender.` `No data was found for the query "QUERY" in Microsoft 365 Defender.` | The action succeeded.  
`Error executing action "Execute Custom Query". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Execute Custom Query** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Execute Entity Query

Use the **Execute Entity Query** action to execute a hunting query that is based on entities in Microsoft Defender For XDR.

This action uses a `where` filter that is based on entities.

This action runs on the following Google SecOps entities:

  * `IP Address`
  * `Host`
  * `User`
  * `Hash`
  * `URL`



You can use the **Execute Entity Query** action to retrieve information that is related to entities, such as retrieve the results from a table and filter the results based on entities.

Unlike the **Execute Query** action that requires you to use specific formatting, the **Execute Entity Query** action doesn't use the query input.

When using the **Execute Query** action to retrieve the alerts that are related to an endpoint, format the `| where` clause as follows:
    
    
    AlertInfo | where DeviceName == "Host-1" or IPAddress == "192.0.2.1" | top 100
    by Timestamp desc
    

To retrieve the alerts that are related to an endpoint, the **Execute Entity Query** action requires you to configure the `Table`, `IP Entity Key`, `Hostname Entity Key`, and `Cross Entity Operator` parameters as follows:

Parameter | `AlertInfo` value  
---|---  
`IP Entity Key` | `IPAddress`  
`Hostname Entity Key` | `DeviceName`  
`Cross Entity Operator` | `OR`  
  
To check how many endpoints the provided hashes affect, the **Execute Entity Query** action requires you to enter the `SHA1` value for the `File Hash Entity Key` parameter.

The `Cross Entity Operator` only impacts the query when you configure multiple values for the `Entity Keys` parameter.

#### Action inputs

The **Execute Entity Query** action requires the following parameters:

Parameter | Description  
---|---  
`Table Names` | _Required_ A comma-separated list of tables to query in Microsoft Defender For XDR.  
`Time Frame` | _Optional_ The time period for the query results. The default value is `Last Hour`. The possible values are as follows:

  * `Last Hour`
  * `Last 6 Hours`
  * `Last 24 Hours`
  * `Last Week`
  * `Last Month`
  * `Custom`

  
`Start Time` | _Optional_ The start time for the query results.If you set the `Time Frame` parameter to `Custom`, this parameter is required.  
`End Time` | _Optional_ The end time for the query results.If you don't set a value and set the `Time Frame` parameter to `Custom`, the action sets this parameter to the current time value by default.  
`Fields To Return` | _Optional_ A comma-separated list of fields to include in the results.  
`Sort Field` | _Optional_ The field to sort the results by. The default value is `Timestamp`.  
`Sort Order` | _Optional_ The order to sort the results (ascending or descending). The default value is `ASC`. The possible values are as follows:

  * `ASC`
  * `DESC`

  
`Max Results To Return` | _Optional_ The maximum number of results to return. The default value is `50`.  
`IP Entity Key` | _Optional_ The key to use for filtering by the `IP Address` entity.  
`Hostname Entity Key` | _Optional_ The key to use for filtering by the `Hostname` entity.  
`File Hash Entity Key` | _Optional_ The key to use for filtering by the `File Hash` entity.  
`User Entity Key` | _Optional_ The key to use for filtering by the `User` entity.  
`URL Entity Key` | _Optional_ The key to use for filtering by the `URL` entity.  
`Email Address Entity Key` | _Optional_ The key to use for filtering by the `Email Address` entity. The action accepts the `User` entity that matches the email regular expression.  
`Stop If Not Enough Entities` | _Optional_ If selected, the action runs if all specified entity types are present. Selected by default.  
`Cross Entity Operator` | _Required_ The logical operator to use between different entity types in the query.The default value is `OR`. The possible values are as follows:

  * `OR`
  * `AND`

  
  
#### Action outputs

The **Execute Entity Query** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Execute Entity Query** action:
    
    
     {
            "Timestamp": "2021-04-12T07:25:00Z",
            "AlertId": "fa7a318954-6c4c-eaab-3200-08d8fd82af35",
            "Title": "CC_Sensitive information",
            "Category": "InitialAccess",
            "Severity": "Medium",
            "ServiceSource": "Microsoft Defender for Office 365",
            "DetectionSource": "Microsoft Defender for Office 365",
            "AttackTechniques": ""
      }
    

##### Output messages

The **Execute Entity Query** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully executed query "QUERY" in Microsoft 365 Defender.` `Action wasn't able to build the query, because not enough entity types were supplied for the specified "ENTITY_KEYS". Please disable the "Stop If Not Enough Entities" parameter or provide at least one entity for each specified ENTITY_KEY.` `No data was found for the query "QUERY" in Microsoft 365 Defender."` | The action succeeded.  
`Error executing action "Execute Entity Query". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Execute Entity Query** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Execute Query

Use the **Execute Query** action to execute hunting queries in Microsoft 365 Defender.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Execute Query** action requires the following parameters:

Parameter | Description  
---|---  
`Table Names` | _Required_ A comma-separated list of table names to query in Microsoft 365 Defender.  
`Query` | _Optional_ A query to execute.Use this parameter to provide the `| where` clause. The time filter, limiting, and sorting are optional.  
`Time Frame` | _Optional_ The time period for the query results. The default value is `Last Hour`. The possible values are as follows:

  * `Last Hour`
  * `Last 6 Hours`
  * `Last 24 Hours`
  * `Last Week`
  * `Last Month`
  * `Custom`

  
`Start Time` | _Optional_ The start time for the query results in the ISO 8601 format.If you set the `Time Frame` parameter to `Custom`, this parameter is required.  
`End Time` | _Optional_ The end time for the query results in the ISO 8601 format.If you don't set a value and set the `Time Frame` parameter to `Custom`, the action sets this parameter to the current time value by default.  
`Fields To Return` | _Optional_ A comma-separated list of fields to include in the results.  
`Sort Field` | _Optional_ The field to sort the results by. The default value is `Timestamp`.  
`Sort Order` | _Optional_ The order to sort the results (ascending or descending). The default value is `ASC`. The possible values are as follows:

  * `ASC`
  * `DESC`

  
`Max Results To Return` | _Optional_ The maximum number of results to return. The default value is `50`.  
  
#### Action outputs

The **Execute Query** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Execute Query** action:
    
    
    {"Results": [
        {
            "Timestamp": "2021-04-12T07:25:00Z",
            "AlertId": "fa7a318954-6c4c-eaab-3200-08d8fd82af35",
            "Title": "CC_Sensitive information",
            "Category": "InitialAccess",
            "Severity": "Medium",
            "ServiceSource": "Microsoft Defender for Office 365",
            "DetectionSource": "Microsoft Defender for Office 365",
            "AttackTechniques": ""
        }
    ]}
    

##### Output messages

The **Execute Query** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully executed query "QUERY" in Microsoft 365 Defender.` `No data was found for the query "QUERY" in Microsoft 365 Defender."` | The action succeeded.  
`Error executing action "Execute Query". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Execute Query** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test the connectivity to Microsoft Defender For XDR.

The action doesn't run on Google SecOps entities.

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
  
##### JSON result

The following example shows the JSON result output received when using the **Ping** action:

##### Output messages

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Microsoft 365 Defender server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Microsoft 365 Defender server! Error is ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Update Incident

Use the **Update Incident** action to update incidents in Microsoft Defender For XDR.

Following the API limitations, this action doesn't fail even if you set an invalid username value to the `Assign To` parameter.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Update Incident** action requires the following parameters:

Parameter | Description  
---|---  
`Incident ID` | _Required_ The ID of the incident to update in Microsoft Defender For XDR.  
`Status` | _Optional_ The status to set for the incident in Microsoft Defender For XDR. The default value is `Select One`. The possible values are as follows:

  * `Select One`
  * `Active`
  * `Resolved`

  
`Classification` | _Optional_ The classification to set for the incident in Microsoft Defender For XDR. The default value is `Select One`. The possible values are as follows:

  * `Select One`
  * `False Positive`
  * `True Positive`

  
`Determination` | _Optional_ The determination to set for the incident in Microsoft Defender For XDR. This parameter only applies if the `Classification` parameter value is `True Positive`. The default value is `Select One`. The possible values are as follows:

  * `Select One`
  * `Not Available`
  * `Apt`
  * `Malware`
  * `Security Personnel`
  * `Security Testing`
  * `Unwanted Software`
  * `Other`

  
`Assign To` | _Optional_ The user to assign the incident to in Microsoft Defender For XDR.  
  
#### Action outputs

The **Update Incident** action provides the following outputs:

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

The **Update Incident** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully updated incident INCIDENT_ID in Microsoft 365 Defender.` | The action succeeded.  
`Error executing action "Update Incident". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
## Connectors

For detailed instructions on how to configure a connector in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

### Microsoft 365 Defender – Incidents Connector

Use the **Microsoft 365 Defender – Incidents Connector** to pull information about incidents and their related alerts from Microsoft Defender XDR.

The dynamic list works with an incident name.

#### Connector limitations

The **Microsoft 365 Defender – Incidents Connector** uses the API requests with strict API limits. To stabilize the connector, set the `Max Incidents To Fetch` parameter to `10` and the `Run Every` parameter to `1 minute`. You can still reach the rate limit because the Microsoft Graph API endpoint that is used to fetch alerts only allows 20 requests for every minute.

To prevent data loss at reaching the rate limit, the connector stops processing the current incident and waits for 90 seconds before processing any other incident. In 90 seconds, the rate limit returns to its maximum value and the connector reprocesses the incident that was not properly processed in the previous iteration.

##### Connector inputs

The **Microsoft 365 Defender – Incidents Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | _Required_ The name of the field where the product name is stored.The default value is `event_type`.  
`Event Field Name` | _Required_ The field name used to determine the event name (subtype).The default value is `@odata.type`.  
`Login API Root` | _Required_ The login API root of the Microsoft Defender For XDR instance. Update this parameter if using a GCC High tenant.The default value is `https://login.microsoftonline.com`.  
`Graph API Root` | _Required_ The API root of the Microsoft Graph service. Update this parameter if using a GCC High tenant. The default value is `https://graph.microsoft.com`.  
`API Root` | _Required_ The API root of the Microsoft Defender XDR instance. Update this parameter if using a GCC High tenant. The default value is `https://api.security.microsoft.com`.  
`Tenant ID` | _Required_ The Microsoft Entra ID (tenant ID) value of your Microsoft Entra ID account.  
`Client ID` | _Required_ The application (client) ID value of your Microsoft Entra ID account.  
`Client Secret` | _Required_ The client secret value of the Microsoft Entra ID application.  
`Verify SSL` | _Optional_ If selected, the integration verifies that the SSL certificate for connecting to the Microsoft Defender For XDR server is valid. Selected by default.  
`Lowest Severity To Fetch` | _Optional_ The lowest severity of incidents to fetch.  
`Max Hours Backwards` | _Optional_ The number of hours before the first connector iteration to retrieve incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time or the fallback value for an expired connector timestamp. The default value is `1`.  
`Max Incidents To Fetch` | _Optional_ The maximum number of incidents to fetch for every connector iteration.The default value is `10`.  
`Incident Status Filter` | _Optional_ A comma-separated list of incident statuses to ingest. The default value is `active, inProgress`. The possible values are as follows:

  * `active`
  * `inProgress`
  * `resolved`
  * `redirected`

Redirected incidents can be empty in most cases.  
`Assigned To` | _Optional_ A comma-separated list of assigned user accounts or email addresses used to filter incidents during ingestion via the Microsoft Graph API.  
`Tags` | _Optional_ A comma-separated list of tags used to filter incidents fetched from Microsoft 365 Defender.  
`Use whitelist as a blacklist` | _Optional_ If selected, the connector uses the dynamic list as a blocklist. Not selected by default.  
`Lowest Alert Severity To Fetch` | _Optional_ The lowest severity of alerts to fetch.  
`Disable Alert Tracking` | _Optional_ If enabled, the connector stops tracking updates for alerts. Disabled by default.  
`Environment Field Name` | _Optional_ The name of the field containing the environment name.  
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`PythonProcessTimeout` | _Required_ The timeout limit in seconds for the Python process that runs the current script.The default value is `180`.  
`Dynamic List Field` | _Optional_ The value that the dynamic list uses for filtering.The possible values are `Incident Name` and `Alert Name`. The default value is `Incident Name`.  
`Alert Detection Source Filter` | _Optional_ A comma-separated list of alert detection sources to ingest, such as `antivirus, microsoftDefenderForEndpoint`.  
`Alert Service Source Filter` | _Optional_ A comma-separated list of alert service sources to ingest, such as `antivirus, microsoftDefenderForEndpoint`.  
`Disable Overflow` | _Optional_ If selected, the connector ignores the Google SecOps overflow mechanism during alert creation. Enabled by default.  
`Proxy Server Address` | _Optional_ The address of the proxy server to use.  
`Proxy Username` | _Optional_ The proxy username to authenticate with.  
`Proxy Password` | _Optional_ The proxy password to authenticate with.  
  
#### Connector rules

  * The connector supports proxies.
  * The connector supports the dynamic lists and blocklists.
  * The connector supports GCC High tenants.



## Jobs

For more information on jobs, see [ Configure a new job](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#configure-a-new-job) and [ Advanced scheduling](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#advanced-scheduling). 

### Microsoft 365 Defender - Sync Alerts

Use the **Microsoft 365 Defender - Sync Alerts** job to synchronize alerts, comments, and statuses bi-directionally between Google SecOps and Microsoft Defender XDR.

#### Job requirements

To ensure the job identifies and synchronizes the correct data, the following conditions must be met:

  * The Google SecOps case must contain the `Microsoft Defender XDR Alert` tag.

  * If the alert didn't originate from the **Microsoft 365 Defender - Incidents Connector** , you must add an `Alert_ID` context value to the alert.

  * Assignee synchronization occurs exclusively from Microsoft Defender XDR to Google SecOps.




#### Job parameters

The **Microsoft 365 Defender - Sync Alerts** job requires the following parameters:

Parameter | Description  
---|---  
`Environment Name` | Required. The name of the environment from which to synchronize alerts. The default value is `Default Environment`.  
`Login API Root` | Required. The Login API root of the Microsoft Defender XDR instance. The default value is `https://login.microsoftonline.com`.  
`Graph API Root` | Required. The API root of the Microsoft Graph service. The default value is `https://graph.microsoft.com`.  
`API Root` | Required. The API root of the Microsoft Defender XDR instance. The default value is `https://api.security.microsoft.com`.  
`Tenant ID` | Required. The Microsoft Defender XDR account tenant ID.  
`Client ID` | Required. The Microsoft Defender XDR account client ID.  
`Client Secret` | Required. The Microsoft Defender XDR account client secret.  
`Max Hours Backwards` | Required. The number of hours to synchronize alerts prior to the current time during the first job iteration. The default value is `24`.  
`Sync Assignee` | Optional. If selected, the action synchronizes the assignee from Microsoft Defender XDR to Google SecOps.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Microsoft Defender XDR server. Enabled by default.  
`Sync Direction` | Optional. The JSON mapping used to control the synchronization direction for each feature. The supported keys are `Status` and `Comments`. The possible values are as follows:

  * `Bidirectional`
  * `toXDR`
  * `toSecOps`
  * `None`

If a key is set to `None` or an invalid value, synchronization is disabled for that feature. If no value is provided, both status and comments synchronize bidirectionally. Unspecified keys default to `Bidirectional`. For example:

  * `{"Status": "toXDR"}`: Synchronizes status from Google SecOps to Microsoft Defender XDR, while comments continue to synchronize bidirectionally.
  * `{"Comments": "toSecOps"}`: Synchronizes comments from Microsoft Defender XDR to Google SecOps, while status continues to synchronize bidirectionally.

The default value is `{"Status": "Bidirectional", "Comments": "Bidirectional"}`.  
`Closed Reason Mapping` | Optional. The JSON mapping of Google SecOps `Closure Reason|RootCause` pairs to the Microsoft Defender XDR classification and determination. This parameter applies only to custom closure reason synchronization from Google SecOps to Microsoft Defender XDR. **Default or empty behavior:** If this parameter is left empty or uses the default mapping, the job maps closure reasons as follows:

  * `Malicious` → `truePositive`, `maliciousUserActivity`
  * `Not Malicious` → `falsePositive`, `notMalicious`
  * `Maintenance` or `Inconclusive` → `unknownFutureValue`, `other` (corresponds to _Unclassified_ in Microsoft Defender)

**Lookup order:** When an alert is closed in Google SecOps, the job evaluates closure details in the following order:

  1. **Exact pair match (`"{Reason} | {Root Cause}"`):** Checks for an exact pair match (such as `"{Malicious} | {Misconfigured system}"`).
  2. **Single reason match (`"Reason"`):** If no exact pair matches, checks for a single reason key match (such as `"Malicious"`).
  3. **Fallback:** If neither matches, or if the specified `classification` or `determination` value isn't accepted by the Microsoft Defender API, the job uses the `Fallback` entry.

**Note:**

  * The `Fallback` entry is mandatory. If omitted, the job fails.
  * The `classification` and `determination` values must be provided in `camelCase` as required by the Microsoft Defender API.

The default value is `{"{reason} | {root cause}": {"classification": "unknownFutureValue", "determination": "other"}, "Malicious": {"classification": "truePositive", "determination": "maliciousUserActivity"}, "NotMalicious": {"classification": "falsePositive", "determination": "notMalicious"}, "Fallback": {"classification": "unknownFutureValue", "determination": "other"}}`.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
