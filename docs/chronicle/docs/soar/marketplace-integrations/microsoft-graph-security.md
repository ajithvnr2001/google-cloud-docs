---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-graph-security/
title: Microsoft Graph Security \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:35:28.742118+00:00
---

# Microsoft Graph Security  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-graph-security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Microsoft Graph Security

This document provides guidance on how to integrate the Microsoft Graph security API with Google Security Operations (Google SecOps).

This document refers to the Microsoft Graph security API. In the Google SecOps platform, the integration for Microsoft Graph security API is called _Microsoft Graph Security_.

## ‌Before you begin

Before configuring the integration in the Google SecOps platform, complete the following steps:

  1. Create the Microsoft Entra app.

  2. Configure the API permissions for your application.

  3. Create a client secret.




### Create Microsoft Entra application

To create the Microsoft Entra application, complete the following steps:

  1. Sign in to the [Azure portal](https://portal.azure.com/) as a user administrator or a password administrator.

  2. Select **Microsoft Entra ID**.

  3. Go to **App registrations > New registration**.

  4. Enter the name of the application.

  5. In the **Redirect URI** field, enter `http://localhost/`.

  6. Click **Register**.

  7. Save the **Application (client) ID** and **Directory (tenant) ID** values to use them later for configuring the integration parameters.




### Configure API permissions

To configure the API permissions for the integration, complete the following steps:

  1. In Azure portal, go to **API Permissions > Add a permission**.

  2. Select **Microsoft Graph > Application permissions**.

  3. In the **Select Permissions** section, select the following required permissions:

     * `User.ReadWrite.All`
     * `Mail.Read`
     * `Directory.ReadWrite.All`
     * `Directory.AccessAsUser.All`
     * `SecurityEvents.ReadWrite.All`
     * `SecurityEvents.Read.All`
  4. Click **Add permissions**.

  5. Click **Grant admin consent for` YOUR_ORGANIZATION_NAME`**.

When the **Grant admin consent confirmation** dialog appears, click **Yes**.




### Create client secret

To create a client secret, complete the following steps:

  1. Navigate to **Certificates and secrets > New client secret**.

  2. Provide a description for a client secret and set its expiration deadline.

  3. Click **Add**.

  4. Save the value of the client secret (not the secret ID) to use it as the **Secret ID** parameter value for configuring the integration. The client secret value is only displayed once.




## Integrate the Microsoft Graph security API with Google SecOps

**Important:** If you make any changes to the **Application Permissions** or **API Permissions** in your Microsoft Entra ID (Azure AD) App Registration after configuring this integration (for example, adding a new permission for a job to run), you must regenerate and update your credentials in Google SecOps. 

This typically means:

  * Generating a new client secret in your App Registration.
  * Updating the client secret (and regenerating the refresh token, if applicable) in the Google SecOps integration configuration.



Failure to update will prevent new permissions from being applied, causing actions to fail.

The integration requires the following parameters:

Parameter | Description  
---|---  
`Client ID` | _Required_ The client (application) ID of the Microsoft Entra application to use in the integration.  
`Secret ID` | _Optional_ The client secret value of the Microsoft Entra application to use in the integration.  
`Certificate Path` | _Optional_ If you use authentication based on certificates instead of the client secret, enter the path to the certificate on the Google SecOps server.  
`Certificate Password` | _Optional_ If the authentication certificate that you use is password-protected, specify the password to open the certificate file.  
`Tenant` | _Required_ The Microsoft Entra ID (tenant ID) value.  
`Use V2 API` | _Optional_ If enabled, the connector will use V2 API endpoints. Note: the structure of the alerts and events will change.  
  
For instructions about configuring an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage if needed. After you configure an integration instance, you can use it in playbooks. For more information about configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [Respond to pending actions from your workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action).

### Add Alert Comment

Use the **Add Alert Comment** action to add a comment to the alert in Microsoft Graph.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Add Alert Comment** action requires the following parameters:

Parameter | Description  
---|---  
`Alert ID` | _Required_ The ID of the alert to update.  
`Comment` | _Required_ The comment for the alert.  
  
#### Action outputs

The **Add Alert Comment** action provides the following outputs:

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

The **Add Alert Comment** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added comment to the alert ALERT_ID in Microsoft Graph.` | The action succeeded.  
`Error executing action "Add Alert Comment". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add Alert Comment** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Administrator Consent

Use the **Get Administrator Consent** action to grant your application the permissions at the Azure portal.

This action runs on all Google SecOps entities.

#### Action inputs

The **Get Administrator Consent** action requires the following parameters:

Parameter | Description  
---|---  
`Redirect URL` | _Required_ The redirect URL that you used when you registered in Azure portal.  
  
#### Action outputs

The **Get Administrator Consent** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Get Administrator Consent** action:

Script result name | Value  
---|---  
`is_connected` | `True` or `False`  
  
### Get Alert

Use the **Get Alert** action to retrieve the properties and relationships of an alert using the alert ID.

This action runs on all Google SecOps entities.

#### Action inputs

The **Get Alert** action requires the following parameters:

Parameter | Description  
---|---  
`Alert ID` | _Required_ The ID of the alert to retrieve details for.  
  
#### Action outputs

The **Get Alert** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Get Alert** action:
    
    
    {
      "feedback": "@odata.type: microsoft.graph.alertFeedback",
      "recommendedActions": ["String"],
      "networkConnections":
        [{
          "applicationName": "String",
          "natDestinationPort": "String",
          "destinationAddress": "String",
          "localDnsName": "String",
          "natDestinationAddress": "String",
          "destinationUrl": "String",
          "natSourceAddress": "String",
          "sourceAddress": "String",
          "direction": "@odata.type: microsoft.graph.connectionDirection",
          "domainRegisteredDateTime": "String (timestamp)",
          "status": "@odata.type: microsoft.graph.connectionStatus",
          "destinationDomain": "String",
          "destinationPort": "String",
          "sourcePort": "String",
          "protocol": "@odata.type: microsoft.graph.securityNetworkProtocol",
          "natSourcePort": "String",
          "riskScore": "String",
          "urlParameters": "String"
         }],
      "cloudAppStates":
        [{
          "destinationServiceIp": "String",
          "riskScore": "String",
          "destinationServiceName": "String"
         }],
      "detectionIds": ["String"],
      "id": "String (identifier)",
      "category": "String",
      "fileStates":
        [{
          "path": "String",
          "riskScore": "String",
          "name": "String",
          "fileHash":
            {
              "hashType": "@odata.type: microsoft.graph.fileHashType",
              "hashValue": "String"
             }
         }],
      "severity": "@odata.type: microsoft.graph.alertSeverity",
      "title": "String",
      "sourceMaterials": ["String"],
      "comments": ["String"],
      "assignedTo": "String",
      "eventDateTime": "String (timestamp)",
      "activityGroupName": "String",
      "status": "@odata.type: microsoft.graph.alertStatus",
      "description": "String",
      "tags": ["String"],
      "confidence": 1024,
      "vendorInformation":
          {
            "providerVersion": "String",
            "vendor": "String",
            "subProvider": "String",
            "provider": "String"
          },
      "userStates":
          [{
            "emailRole": "@odata.type: microsoft.graph.emailRole",
            "logonId": "String",
            "domainName": "String",
            "onPremisesSecurityIdentifier": "String",
            "userPrincipalName": "String",
            "userAccountType": "@odata.type: microsoft.graph.userAccountSecurityType",
            "logonIp": "String",
            "logonDateTime": "String (timestamp)",
            "logonType": "@odata.type: microsoft.graph.logonType",
            "logonLocation": "String",
            "aadUserId": "String",
            "accountName": "String",
            "riskScore": "String",
            "isVpn": "true"
            }],
     "malwareStates":
          [{
            "category": "String",
            "wasRunning": "true",
            "name": "String",
            "family": "String",
            "severity": "String"
           }],
      "processes":
          [{
            "processId": 1024,
            "integrityLevel": "@odata.type: microsoft.graph.processIntegrityLevel",
            "name": "String",
            "fileHash":
                {
                  "hashType": "@odata.type: microsoft.graph.fileHashType",
                  "hashValue": "String"
                },
           "parentProcessId": 1024,
           "createdDateTime": "String (timestamp)",
           "commandLine": "String",
           "parentProcessName": "String",
           "accountName": "String",
           "isElevated": "true",
           "path": "String",
           "parentProcessCreatedDateTime": "String (timestamp)"
          }],
      "azureTenantId": "String",
      "triggers":
         [{
           "type": "String",
           "name": "String",
           "value": "String"
          }],
      "createdDateTime": "String (timestamp)",
      "vulnerabilityStates":
         [{
           "cve": "String",
           "severity": "String",
           "wasRunning": "true"
         }],
      "hostStates":
         [{
           "isAzureAadRegistered": "true",
           "riskScore": "String",
           "fqdn": "String",
           "isHybridAzureDomainJoined": "true",
           "netBiosName": "String",
           "publicIpAddress": "String",
            "isAzureAadJoined": "true",
            "os": "String",
            "privateIpAddress": "String"
          }],
      "lastModifiedDateTime": "String (timestamp)",
      "registryKeyStates":
          [{
            "processId": 1024,
            "oldKey": "String",
            "oldValueName": "String",
             "valueType": "@odata.type: microsoft.graph.registryValueType",
            "oldValueData": "String",
            "hive": "@odata.type: microsoft.graph.registryHive",
            "valueData": "String",
            "key": "String",
            "valueName": "String",
            "operation": "@odata.type: microsoft.graph.registryOperation"
           }],
      "closedDateTime": "String (timestamp)",
      "azureSubscriptionId": "String"
    }
    

##### Script result

The following table lists the value for the script result output when using the **Get Alert** action:

Script result name | Value  
---|---  
`alert_details` | `True` or `False`  
  
### Get Incident

Use the **Get Incident** action to obtain details of a security incident using the incident ID.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Get Incident** action requires the following parameters:

Parameter | Description  
---|---  
`Incident ID` | _Required_ The ID of the incident to obtain the details for.   
  
#### Action outputs

The **Get Incident** action provides the following outputs:

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

The **Get Incident** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned information about the incident INCIDENT_ID.` `` `` | The action succeeded.  
`Error executing action "Get Incident". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Incident** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Kill User Session

Use the **Kill User Session** action to invalidate all refresh tokens issued to applications for a user by resetting the `signInSessionsValidFromDateTime` user property to the current date and time.

This action runs on all Google SecOps entities.

#### Action inputs

The **Kill User Session** action requires the following parameters:

Parameter | Description  
---|---  
`userPrincipalName| ID` | _Required_ The username or the user **Unique ID** value used in Microsoft Entra ID.  
  
#### Action outputs

The **Kill User Session** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Kill User Session** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List Alerts

Use the **List Alerts** action to list available alerts in Microsoft Graph.

This action runs on all Google SecOps entities.

The filtering process happens on the Microsoft Graph API side. For products that publish alerts to Microsoft Graph and don't support filtering, Microsoft Graph adds all alerts to the response as if the alerts have passed the filter.

#### Action inputs

The **List Alerts** action requires the following parameters:

Parameter | Description  
---|---  
`Filter Key` | _Optional_ Specify the key that needs to be used to filter alerts. Note: "Title" option is not supported in the V2 API.  
`Filter Logic` | _Optional_ The filter logic to apply.The filter logic is based on the `Filter Key` parameter value. The possible values are as follows:

  * `Not Specified`
  * `Equal`
  * `Contains`

The default value is `Not Specified`.  
`Filter Value` | _Optional_ The value to use in the filter.If you select `Equal`, the action attempts to find the exact match among results.If you select `Contains`, the action attempts to find results that contain the selected substring.If don't set a value, the filter doesn't apply.The filter logic is based on the `Filter Key` parameter value.  
`Max Records To Return` | _Optional_ The number of records to return for every action run.The default value is 50.  
  
#### Action outputs

The **List Alerts** action provides the following outputs:

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

The following example shows the JSON result output received when using the **List Alerts** action:
    
    
    {
                "id": "ID",
                "azureTenantId": "TENANT_ID",
                "azureSubscriptionId": null,
                "riskScore": null,
                "tags": [],
                "activityGroupName": null,
                "assignedTo": null,
                "category": "ImpossibleTravel",
                "closedDateTime": null,
                "comments": [],
                "confidence": null,
                "createdDateTime": "2022-04-29T13:10:59.705Z",
                "description": "Sign-in from an atypical location based on the user's recent sign-ins",
                "detectionIds": [],
                "eventDateTime": "2022-04-29T11:36:59.1520667Z",
                "feedback": null,
                "incidentIds": [],
                "lastEventDateTime": null,
                "lastModifiedDateTime": "2022-04-30T14:44:43.4742002Z",
                "recommendedActions": [],
                "severity": "medium",
                "sourceMaterials": [],
                "status": "newAlert",
                "title": "Atypical travel",
                "vendorInformation": {
                    "provider": "IPC",
                    "providerVersion": null,
                    "subProvider": null,
                    "vendor": "Microsoft"
                },
                "alertDetections": [],
                "cloudAppStates": [],
                "fileStates": [],
                "hostStates": [],
                "historyStates": [],
                "investigationSecurityStates": [],
                "malwareStates": [],
                "messageSecurityStates": [],
                "networkConnections": [],
                "processes": [],
                "registryKeyStates": [],
                "securityResources": [],
                "triggers": [],
                "userStates": [
                    {
                        "aadUserId": "b786d3cf-e97d-4511-b61c-0559e9f4da75",
                        "accountName": "example.user",
                        "domainName": "example.com",
                        "emailRole": "unknown",
                        "isVpn": null,
                        "logonDateTime": "2022-04-29T11:36:59.1520667Z",
                        "logonId": null,
                        "logonIp": "203.0.113.194",
                        "logonLocation": "1800 Amphibious Blvd, Mountain View, CA 94045",
                        "logonType": null,
                        "onPremisesSecurityIdentifier": null,
                        "riskScore": null,
                        "userAccountType": null,
                        "userPrincipalName": "example.user@example.com"
                    },
                    {
                        "aadUserId": "b786d3cf-e97d-4511-b61c-0559e9f4da75",
                        "accountName": "example.user",
                        "domainName": "example.com",
                        "emailRole": "unknown",
                        "isVpn": null,
                        "logonDateTime": "2022-04-29T11:15:00Z",
                        "logonId": null,
                        "logonIp": "192.0.2.160",
                        "logonLocation": "ES",
                        "logonType": null,
                        "onPremisesSecurityIdentifier": null,
                        "riskScore": null,
                        "userAccountType": null,
                        "userPrincipalName": "example.user@example.com"
                    }
                ],
                "uriClickSecurityStates": [],
                "vulnerabilityStates": []
    }
    

##### Output messages

The **List Alerts** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully found alerts for the provided criteria in Microsoft Graph.` `No alerts were found for the provided criteria in Microsoft Graph.` `The filter was not applied because the "Filter Value" parameter has an empty value.` | The action succeeded.  
`Error executing action "List Alerts". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List Alerts** action:

Script result name | Value  
---|---  
`alerts_details` | `ALERT_DETAILS`  
  
### List Incidents

Use the **List Incidents** action to list the security incidents from Microsoft Graph based on the criteria provided.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **List Incidents** action requires the following parameters:

Parameter | Description  
---|---  
`Filter Key` | _Optional_ Specify the key that needs to be used to filter alerts. Note: "Title" option is not supported in the V2 API.  
`Filter Logic` | _Optional_ The filter logic to apply.The filter logic is based on the `Filter Key` parameter value. The possible values are as follows:

  * `Not Specified`
  * `Equal`
  * `Contains`

The default value is `Not Specified`.  
`Filter Value` | _Optional_ The value to use in the filter.If you select `Equal`, the action attempts to find the exact match among results.If you select `Contains`, the action attempts to find results that contain the selected substring.If don't set a value, the filter doesn't apply.The filter logic is based on the `Filter Key` parameter value.  
`Max Records To Return` | _Optional_ The number of records to return for every action run.The default value is 50.  
  
#### Action outputs

The **List Incidents** action provides the following outputs:

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

The **List Incidents** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully found incidents for the provided criteria in Microsoft Graph.` `No incidents were found for the provided criteria in Microsoft Graph.` `The filter was not applied because the "Filter Value" parameter has an empty value.` | The action succeeded.  
`Error executing action "List Incidents". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List Incidents** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test the connectivity to Microsoft Graph.

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
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Update Alert

Use the **Update Alert** action to update an editable alert property.

This action runs on all Google SecOps entities.

#### Action inputs

The **Update Alert** action requires the following parameters:

Parameter | Description  
---|---  
`Alert ID` | _Required_ The ID of the alert to update.  
`Assigned To` | _Optional_ The name of the analyst the alert is assigned to for triage, investigation, or remediation.  
`Closed Date Time` | _Optional_ Time at which the alert was closed. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Note: this parameter is not supported in the V2 version of API.  
`Comments` | _Optional_ Analyst comments on the alert (for customer alert management), separated by comma. This method can update the comments field with the following values only: Closed in IPC, Closed in MCAS. Note: in V2 version of API this parameter works as a string and a single comment will be added to the Alert.  
`Feedback` | _Optional_ Analyst feedback on the alert. Possible values are: unknown, truePositive, falsePositive, benignPositive. Note: in V2 version of API this parameter is mapped to "classification" and has the following possible values: unknown, falsePositive, truePositive, informationalExpectedActivity, unknownFutureValue.  
`Status` | _Optional_ The alert lifecycle status.The possible values are as follows:

  * `unknown`
  * `newAlert`
  * `inProgress`
  * `resolved`

  
`Tags` | _Optional_ User-definable labels that can be applied to an alert. Separated by comma. Note: this parameter is not supported in the V2 version of API.  
  
#### Action outputs

The **Update Alert** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Update Alert** action:

Script result name | Value  
---|---  
`is_updated` | `True` or `False`  
  
## Connectors

For detailed instructions on how to configure a connector in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

### Microsoft Graph Security Connector

**Important:** This connector will be fully deprecated on March 30, 2027. Until then, support is limited to critical bug fixes for ingestion issues; no new feature updates will be provided. Use the [Microsoft 365 Defender – Incidents Connector](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-365-defender#microsoft_365_defender_incidents_connector) instead. Note that migrating may require changes to your playbooks.

Use the **Microsoft Graph Security Connector** to ingest alerts that are published in the Microsoft Graph security API as Google SecOps alerts. The connector periodically connects to the Microsoft Graph security endpoint and pulls a list of incidents that are generated for a specific period.

The **Microsoft Graph Security Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | _Required_ The name of the field where the product name is stored.The default value is `ProductFieldName`.  
`Event Field Name` | _Required_ The field name used to determine the event name (subtype).The default value is `AlertName`.  
`Script Timeout (Seconds)` | _Required_ The timeout limit (in seconds) for the Python process running the current script.The default value is 30 seconds.   
`Environment Field Name` | _Optional_ The name of the field where the environment name is stored.If the environment field isn't found, the environment is set to `""`.   
`Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is `""`.  
`Client ID` | _Required_ The client (application) ID of the Microsoft Entra application to use in the integration.  
`Client Secret` | _Optional_ The client secret value of the Microsoft Entra application to use in the integration.  
`Certificate Path` | _Optional_ If you use authentication based on certificates instead of the client secret, enter the path to the certificate on the Google SecOps server.  
`Certificate Password` | _Optional_ If the authentication certificate that you use is password-protected, specify the password to open the certificate file.  
`Azure Active Directory ID` | _Required_ The Microsoft Entra ID (tenant ID) value.  
`Offset Time In Hours` | _Required_ The number of hours before now to fetch alerts from.The default value is 120 hours.  
`Fetch Alerts only from` | _Optional_ A comma-separated list of providers to pull alerts from Microsoft Graph. If you set the 'Fetch Alerts only from' parameter to Office 365 Security and Compliance, the connector doesn't support multiple values in the Alert Statuses to fetch or Alert Severities to fetch parameters. If 'Use V2 API' is enabled, then this parameter will work with 'serviceSource' property of the alert.  
`Alert Statuses to fetch` | _Required_ A comma-separated list of alert statuses for the Google SecOps server to retrieve.The possible values are as follows: `unknown`, `newAlert`, `inProgress`, `resolved`.  
`Alert Severities to fetch` | _Required_ A comma-separated list of alert severities for the Google SecOps server to retrieve. The possible values are as follows: `high`, `medium`, `low`, `informational`, `unknown`.  
`Max Alerts Per Cycle` | _Optional_ The maximum number of alerts to process in a one-connector iteration. The default value is 50.  
`Proxy Server Address` | _Optional_ The address of the proxy server to use.  
`Proxy Username` | _Optional_ The proxy username to authenticate with.  
`Proxy Password` | _Optional_ The proxy password to authenticate with.  
`Use V2 API` | _Optional_ If enabled, the connector will use V2 API endpoints. Note: the structure of the alerts and events will change. Additionally, the 'Fetch Alerts only from' parameter will require different values to be provided.  
  
#### Connector rules

The connector doesn't support the dynamic list or blocklist rules.

The connector supports proxies.

### Microsoft Graph Office 365 Security and Compliance Connector

**Important:** This connector will be fully deprecated on March 30, 2027. Until then, support is limited to critical bug fixes for ingestion issues; no new feature updates will be provided. Use the [Microsoft 365 Defender – Incidents Connector](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-365-defender#microsoft_365_defender_incidents_connector) instead. Note that migrating may require changes to your playbooks.

Use the **Microsoft Graph Office 365 Security and Compliance Connector** to ingest the Office 365 Security and Compliance alerts using the Microsoft Graph API.

The **Microsoft Graph Office 365 Security and Compliance Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | _Required_ The name of the field where the product name is stored.The default value is `ProductFieldName`.  
`Event Field Name` | _Required_ The field name used to determine the event name (subtype).The default value is `event_class`.  
`Script Timeout (Seconds)` | _Required_ The timeout limit (in seconds) for the Python process running the current script.The default value is 30 seconds.   
`Environment Field Name` | _Optional_ The name of the field where the environment name is stored.If the environment field isn't found, the environment is set to `""`.   
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is `""`.  
`Client ID` | _Required_ The client (application) ID of the Microsoft Entra application to use in the integration.  
`Client Secret` | _Optional_ The client secret value of the Microsoft Entra application to use in the integration.  
`Certificate Path` | _Optional_ If you use authentication based on certificates instead of the client secret, enter the path to the certificate on the Google SecOps server.  
`Certificate Password` | _Optional_ If the authentication certificate that you use is password-protected, specify the password to open the certificate file.  
`Azure Active Directory ID` | _Required_ The Microsoft Entra ID (tenant ID) value.  
`Verify SSL` | _Optional_ If selected, the integration verifies that the SSL certificate for the connection to the Microsoft Graph server is valid. Selected by default.  
`Offset Time In Hours` | _Required_ The number of hours before now to fetch alerts.The default value is 120 hours.  
`Alert Statuses to fetch` | _Optional_ A comma-separated list of alert statuses for the Google SecOps server to retrieve.The possible values are as follows: `Dismissed`, `Active`, `Investigating`, `Resolved`.  
`Alert Severities to fetch` | _Optional_ A comma-separated list of alert severities for the Google SecOps server to retrieve. The possible values are as follows: `high`, `medium`, `low`, `informational`, `unknown`.  
`Max Alerts Per Cycle` | _Required_ The maximum number of alerts to process in a one-connector iteration. The default value is 50.  
`Proxy Server Address` | _Optional_ The address of the proxy server to use.  
`Proxy Username` | _Optional_ The proxy username to authenticate with.  
`Proxy Password` | _Optional_ The proxy password to authenticate with.  
  
#### Connector rules

The connector doesn't support the dynamic list or blocklist rules.

The connector supports proxies.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
