---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/azure-ad-identity-protection/
title: Integrate Microsoft 365 Identity Protection with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:00:29.275151+00:00
---

# Integrate Microsoft 365 Identity Protection with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/azure-ad-identity-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Microsoft 365 Identity Protection with Google SecOps

**Important:** In the Google SecOps platform, the Microsoft 365 Identity Protection integration is called _Azure AD Identity Protection_.

This document describes how to integrate Microsoft 365 Identity Protection with Google Security Operations (Google SecOps).

## Prerequisites

Before you configure the integration in the Google SecOps platform, complete the following prerequisite steps:

  1. Create the Microsoft Entra app.

  2. Configure the API permissions for your app.

  3. Create a client secret.




### Create Microsoft Entra app

  1. Sign in to the [Azure portal](https://portal.azure.com/) as a user administrator or a password administrator.

  2. Select **Microsoft Entra ID**.

  3. Go to **App registrations > New registration**.

  4. Enter the name of the app.

  5. Click **Register**.

  6. Save the **Application (client) ID** and **Directory (tenant) ID** values to use them later when configuring the integration parameters.




### Configure API permissions

  1. Go to **API Permissions > Add a permission**.

  2. Select **Microsoft Graph**.

  3. In the **Select Permissions** section, select the following permissions: 

     * `IdentityRiskEvent.Read.All`
     * `IdentityRiskyUser.ReadWrite.All`
  4. Click **Add permissions**.

  5. Click **Grant admin consent for` YOUR_ORGANIZATION_NAME`**.

When the **Grant admin consent confirmation** dialog appears, click **Yes**.




### Create client secret

  1. Navigate to **Certificates and secrets > New client secret**.

  2. Provide a description for a client secret and set its expiration deadline.

  3. Click **Add**.

  4. Save the value of the client secret (not the secret ID) to use it as the `Client Secret` parameter value when configuring the integration. The client secret value is only displayed once.




## Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Login API Root | String | https://login.microsoftonline.com | No | API root used to authenticate with the Microsoft identity platform.  
API Root | String | https://graph.microsoft.com | Yes | API root of the Microsoft 365 Identity Protection instance.  
Tenant ID | String | N/A | Yes | Tenant ID of the Microsoft 365 Identity Protection account.  
Client ID | String | N/A | Yes | Client ID of the Microsoft 365 Identity Protection account.  
Client Secret | Password | N/A | Yes | Client Secret of the Microsoft 365 Identity Protection account.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Microsoft 365 Identity Protection server is valid.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Test the connectivity to Microsoft 365 Identity Protection.

#### Parameters

N/A

#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful:_ "Successfully connected to the Azure AD Identity Protection server with the provided connection parameters!" **The action should fail and stop a playbook execution:** _If not successful:_ "Failed to connect to the Azure AD Identity Protection server! Error is {0}".format(exception.stacktrace) | General  
  
### Enrich Entities

Enrich entities using information from Microsoft 365 Identity Protection. Supported entities: Username, Email Address (user entity that matches email regular expression pattern).

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Create Insight | Checkbox | Checked | No | If enabled, the action creates an insight containing all of the retrieved information about the entity.  
  
#### Run On

This action runs on the Username entity.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "id": "2600d017-84a1-444f-94ba-4bebed30b09e",
        "isDeleted": false,
        "isProcessing": false,
        "riskLevel": "none",
        "riskState": "remediated",
        "riskDetail": "userPerformedSecuredPasswordChange",
        "riskLastUpdatedDateTime": "2021-09-02T14:10:48Z",
        "userDisplayName": "user_1",
        "userPrincipalName": "user_1@example.com"
    }
    

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
is_deleted | When available in JSON  
is_processing | When available in JSON  
risk_level | When available in JSON  
risk_state | When available in JSON  
risk_detail | When available in JSON  
risk_updated | When available in JSON  
display_name | When available in JSON  
principal_name | When available in JSON  
  
##### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available for one entity (is_success=true):_ "Successfully enriched the following entities using information from Azure AD Identity Protection: {entity.identifier}". _If data is not available for one entity (is_success=true):_ "Action wasn't able to enrich the following entities using information from Azure AD Identity Protection: {entity.identifier}". _If data is not available for all entities (is_success=false): "_ None of the provided entities were enriched." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** {entity.identifier} **Table Columns:**

  * Key
  * Value

| Entity  
  
### Update User State

Update state of the user in Microsoft 365 Identity Protection. Supported entities: Username, Email Address (user entity that matches email regular expression pattern).

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
State | DDL | Compromised Possible Values:

  * Compromised
  * Dismissed

| No | Specify the state for the users.  
  
#### Run On

This action runs on the Username entity.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If the 204 status code is reported for one user (is_success=true):_ "Successfully updated the state of the following users in Azure AD Identity Protection: {entity identifier}". _If one user is not found (is_success=true): "_ The following users were not found in Azure AD Identity Protection:"{entity.identifier}" _If all users are not found (is_success=true):_ "None of the provided users were not found in Azure AD Identity Protection." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Update User State". Reason: {0}''.format(error.Stacktrace)' | General  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### Azure AD Identity Protection - Risk Detections Connector

Pull information about risk detections from Microsoft 365 Identity Protection.

The dynamic list filter works with the `riskEventType` parameter.

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Login API Root | String | https://login.microsoftonline.com | No | API root used to authenticate with the Microsoft identity platform.  
API Root | String | https://graph.microsoft.com | Yes | API root of the Microsoft 365 Identity Protection instance.  
Product Field Name | String | Product Name | Yes |  The name of the field where the product name is stored. The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default. The default value is `Product Name`.  
Event Field Name | String | riskEventType | Yes | The name of the field that determines the event name (subtype).  
Environment Field Name | String | "" | No | The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value.  
`Environment Regex Pattern` | String | .* | No |  A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
PythonProcessTimeout | Integer | 180 | Yes | The timeout limit, in seconds, for the Python process that runs the current script.  
API Root | String | https://graph.microsoft.com | Yes | API root of the Microsoft 365 Identity Protection instance.  
Tenant ID | String | N/A | Yes | Tenant ID of the Microsoft 365 Identity Protection account.  
Client ID | String | N/A | Yes | Client ID of the Microsoft 365 Identity Protection account.  
Client Secret | Password | N/A | Yes | Client Secret of the Microsoft 365 Identity Protection account.  
Lowest Risk Level To Fetch | String | N/A | No | The lowest risk that needs to be used to fetch alerts. Possible values: `Low`, `Medium`, `High`. If no value is specified, the connector ingests risk detections with all risk levels.  
Max Hours Backwards | Integer | 1 | No | The number of hours for which risk detections should be fetched.  
Max Alerts To Fetch | Integer | 100 | No | The number of alerts to process per one connector iteration.  
`Use whitelist as a blacklist` | Checkbox | Unchecked | Yes | If selected, the connector uses the dynamic list as a blocklist.  
Verify SSL | Checkbox | Checked | Yes | If selected, the integration validates the SSL certificate when connecting to the Microsoft 365 Identity Protection server.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector rules

The connector supports proxies.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
