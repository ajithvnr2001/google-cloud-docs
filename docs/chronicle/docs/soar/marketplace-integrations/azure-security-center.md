---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/azure-security-center/
title: Microsoft Defender for Cloud \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:39.025250+00:00
---

# Microsoft Defender for Cloud  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/azure-security-center/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Microsoft Defender for Cloud

**Important:** In the Google SecOps platform, the Microsoft Defender For Cloud integration is called _Azure Security Center_.

This document describes how to integrate Microsoft Defender For Cloud with Google Security Operations.

## Use cases

  1. Ingest security alerts into Google SecOps for investigation.

  2. Update alerts.

  3. Retrieve information about standard compliance.




## Prerequisites

Before configuring the integration in the Google SecOps platform, make sure to grant required permissions to the Azure user account and configure either a password authentication or an OAuth authentication.

### Configure permissions

This integration requires delegated access to the Azure resources. Make sure to grant the following required permissions to the Azure user account used to configure the integration:

  1. User account must be an **active** member for the following Azure roles:

     * `Security Reader`
     * `Security Admin`
  2. On the Azure subscription level, make sure to grant the user the following IAM role: `Management Group Reader`.




### Configure password authentication

To configure the password authentication for Microsoft Defender for Cloud, complete the following steps:

  1. Create the Microsoft Entra app.

  2. Configure the API permissions for your app.

  3. Create a client secret.

  4. Use your Azure subscription ID as a value for the corresponding integration parameter.




#### Create Microsoft Entra app

  1. Sign in to the [Azure portal](https://portal.azure.com/) as a user administrator or a password administrator.

  2. Select **Microsoft Entra ID**.

  3. Go to **App registrations > New registration**.

  4. Enter the name of the app.

  5. Click **Register**.

  6. Save the **Application (client) ID** and **Directory (tenant) ID** values to use them later when configuring the integration parameters.




#### Configure API permissions

  1. Go to **API Permissions > Add a permission**.

  2. Select **Azure Service Management > Delegated permissions**.

  3. In the **Select Permissions** section, select the following permission: 

     * `user_impersonation`
  4. Select **Microsoft Graph > Delegated permissions**.

  5. In the **Select Permissions** section, select the following permissions: 

     * `SecurityEvents.Read.All`
     * `SecurityEvents.ReadWrite.All`
     * `User.Read`
  6. Select **Microsoft Graph > Application permissions**.

  7. In the **Select Permissions** section, select the following permissions: 

     * `SecurityEvents.Read.All`
     * `SecurityEvents.ReadWrite.All`
  8. Click **Add permissions**.

  9. Click **Grant admin consent for` YOUR_ORGANIZATION_NAME`**.

When the **Grant admin consent confirmation** dialog appears, click **Yes**.




#### Create client secret

  1. Navigate to **Certificates and secrets > New client secret**.

  2. Provide a description for a client secret and set its expiration deadline.

  3. Click **Add**.

  4. Save the value of the client secret (not the secret ID) to use it as the `Client Secret` parameter value when configuring the integration. The client secret value is only displayed once.




#### Configure integration with Azure subscription ID

  1. In Microsoft Defender for Cloud, go the **Overview** tab.

  2. Click **Azure subscriptions**.

  3. Copy the Azure subscription ID value and input it in the `Subscription ID` parameter when configuring the integration parameters.




### Configure OAuth authentication

To configure the OAuth authentication for Microsoft Defender for Cloud, complete the following steps:

  1. Create the Microsoft Entra app.

  2. Configure the API permissions for your app.

  3. Create a client secret.

  4. Use your Azure subscription ID as a value for the corresponding integration parameter.




#### Create Microsoft Entra app

To create an application and impersonate the chosen user, follow these steps:

  1. Sign in to the [Azure portal](https://portal.azure.com/) as a user administrator or a password administrator.

  2. Select **Microsoft Entra ID**.

  3. Go to **App registrations > New registration**.

  4. Enter the name of the app.

  5. Select suitable **Supported account types**.

  6. For the **Redirect URL** , provide the following value: `http://localhost`.

  7. Click **Register**.

  8. Save the **Application (client) ID** and **Directory (tenant) ID** values to use them later to configure the integration.




#### Configure API permissions

  1. Go to **API Permissions > Add a permission**.

  2. Select **Azure Service Management > Delegated permissions**.

  3. In the **Select Permissions** section, select the following permission: 

     * `user_impersonation`
  4. Select **Microsoft Graph > Delegated permissions**.

  5. In the **Select Permissions** section, select the following permissions: 

     * `SecurityEvents.Read.All`
     * `SecurityEvents.ReadWrite.All`
     * `User.Read`
  6. Select **Microsoft Graph > Application permissions**.

  7. In the **Select Permissions** section, select the following permissions: 

     * `SecurityEvents.Read.All`
     * `SecurityEvents.ReadWrite.All`
  8. Click **Add permissions**.

  9. Click **Grant admin consent for` YOUR_ORGANIZATION_NAME`**.

When the **Grant admin consent confirmation** dialog appears, click **Yes**.




#### Create client secret

  1. Navigate to **Certificates and secrets > New client secret**.

  2. Provide a description for a client secret and set its expiration deadline.

  3. Click **Add**.

  4. Save the value of the client secret (not the secret ID) to use it as the `Client Secret` parameter value when configuring the integration. The client secret value is only displayed once.




#### Configure integration with Azure subscription ID

  1. In Microsoft Defender for Cloud, go the **Overview** tab.

  2. Click **Azure subscriptions**.

  3. Copy the Azure subscription ID value and input it in the `Subscription ID` parameter when configuring the integration.




#### Configure OAuth authentication in Google SecOps

To configure the OAuth authentication for Microsoft Defender for Cloud in Google SecOps platform, complete the following steps:

  1. Configure the integration parameters and save them.

  2. Generate a refresh token:

     * Optional: Simulate a case in Google SecOps.

     * Manually run the _Get OAuth Authorization Code_ action.

     * Manually run the _Generate Token_ action.

  3. Input the obtained refresh token as the `Refresh Token` parameter value and save the configuration.




##### Configure integration parameters

In Google SecOps, configure the integration parameters with Client ID, Client secret, Tenant ID, and Subscription ID values that you've obtained in previous steps.

##### Generate refresh token

Generating a refresh token requires running manual actions on any existing case. If your Google SecOps instance is new and has no existing cases, simulate one.

###### Simulate case

To simulate a case in Google SecOps, follow these steps:

  1. In the left navigation, select **Cases**.

  2. On the Cases page, click **add > Simulate Cases**.

  3. Select any of the default cases and click **Create**. It doesn't matter what case you choose to simulate.

  4. Click **Simulate**.

If you have an environment other than default and would like to use it, select the correct environment and click **Simulate**.

  5. In the **Cases** tab, click **Refresh**. The case you have simulated appears in the case list.




###### Run the Get OAuth Authorization Code action

Use the Google SecOps case you've simulated or any existing one to run the Get OAuth Authorization Code action manually.

  1. In the **Cases** tab, select your simulated case to open a Case View.

  2. Click **Manual Action**.

  3. In the Manual Action **Search** field, input `Azure Security Center`.

  4. In the results under the Azure Security Center integration, select **Get OAuth Authorization Code**. This action returns an authorization link used to interactively sign in to the Microsoft Entra app.

  5. In the `Redirect URL` parameter field, input the URL that you've used when creating the Microsoft Entra app.

  6. Click **Execute**.

  7. After the action is executed, navigate to the Case Wall of your simulated case. In the _Azure Security Center_Get OAuth Authorization Code_ action record, click **View More** and copy the authorization link.

  8. Open a new browser window in the incognito mode and paste the generated authorization URL. The Azure sign-in page opens.

  9. Sign in with the user credentials you selected for the integration. After signing in, your browser should be redirected with a code in the address bar.

An example of the resulting URL with the code is as follows:
         
         http://localhost/?code=0.ATwAylKP1BpbCEeO0Ou5iiakalBV.......nIAA&state=12345&session_state=28084547-3dea-449a-8b4c-c1671342a39d#
         

  10. From the URL, copy the access code part that comes after `http://localhost/?code=`. You need this access code to run the _Get OAuth Refresh Token_ action. 




###### Run the Get OAuth Refresh Token action

Use a the Google SecOps case you've simulated to run the Get OAuth Refresh Token  action manually.

  1. In the **Cases** tab, select your simulated case to open a Case View.

  2. Click **Manual Action**.

  3. In the Manual Action **Search** field, type in `Azure Security Center`.

  4. In the results under the Azure Security Center integration, select **Get OAuth Refresh Token**.

  5. In the `Authorization Code` parameter field, input the access code that you've obtained after running the _Get OAuth Authorization Code_ action.

  6. Click **Execute**.

  7. After the action is executed, navigate to the Case Wall of your simulated case. In the _Azure Security Center_Get OAuth Refresh Token_ action record, click **View More**.

  8. Copy the entire value of the generated refresh token.




###### Configure the Refresh Token parameter

  1. Navigate to the configuration dialog for the Azure Security Center integration.

  2. Input the refresh token value from the previous step into the **Refresh Token** field.

  3. Click **Save**.




## Integrate Microsoft Defender For Cloud with Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration inputs

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Client ID | String | N/A | Yes | Client ID of the Microsoft Entra application.  
Client Secret | Password | N/A | Yes | Client Secret of the Microsoft Entra application.  
Username | String | N/A | No | Username of the Microsoft Entra account.  
Password | Password | N/A | No | Password of the Microsoft Entra account.  
Subscription ID | String | N/A | Yes | The ID of the subscription for which you want to query information. Note: If subscription ID is provided at the integration level and action level, priority is given to the action configuration.  
Tenant ID | String | N/A | Yes | Tenant ID of the Microsoft Entra application.  
Refresh Token | Password | N/A | Yes | Refresh token for the OAuth authorization.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verifies that the SSL certificate for the connection to the Microsoft Defender for Cloud server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Get OAuth Authorization Code

Generate an OAuth authorization code to obtain a refresh token.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Redirect URL | String | https://localhost | Yes | Specify the redirect URL that was used when the Microsoft Entra app was created.  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case wall

**Result type** | **Value/Description** | **Type (Entity \ General)**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** "Successfully generated Authorization code URL in Azure Security Center. Please copy paste it in the browser. After that, copy the "code" part from the URL. This authorization code is used in action "Get OAuth Refresh Token". ". | General  
Link | **Name:** Authorization Code Link  
**URL:** {generated link} |   
  
### Get OAuth Refresh Token

Generate the refresh token that is needed for the integration configuration. Authorization code can be generated using the _Get OAuth Authorization Code_ action.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Redirect URL | String | https://localhost | Yes | Specify the redirect URL that was used when the app was created.  
Authorization Code | String |  | Yes | Specify the authorization code from action "Get OAuth Authorization Code"  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON result
    
    
    {
        "token_type": "Bearer",
        "scope": "user_impersonation",
        "expires_in": "3599",
        "ext_expires_in": "3599",
        "expires_on": "1628514482",
        "not_before": "1628510582",
        "resource": "https://management.azure.com",
        "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Im5PbzNaRH",
        "refresh_token": "0.ATwAylKP1BpbCEeO0Ou5iiakalBVs4hy5YpMhS4OVguFb9Y8AGw",
        "id_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdWQiOiI4OGIzNTU1MC1"
    }
    

##### Case wall

**Result type** | **Value/Description** | **Type (Entity \ General)**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If the 200 status code is reported (is_success = true):** "Successfully generated refresh token in Azure Security Center.". **The action should fail and stop a playbook execution:** **if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Get OAuth Refresh Token". Reason: {0}''.format(error.Stacktrace) **If non 200 status code:** "Error executing action "Get OAuth Refresh Token". Reason: {0}''.format(error_description) | General  
  
### List Regulatory Standards

List available regulatory standards in Microsoft Defender for Cloud.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Subscription ID | String | N/A | No | Specify the ID of the subscription for which you want to query information.Note: If subscription ID is provided at the integration level and action level, priority is given to the action configuration.  
State Filter | CSV | Failed | No | Specify the comma-separated list of states. Example: Failed, Skipped. Only standards with the matching state will be returned. For example, if you specify "Failed", action will only return failed standards. Possible values: Passed,Failed,Unsupported,Skipped  
Max Standards To Return | String | 50 | No | Specify how many standards to return.  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON result
    
    
    {
        "value": [
            {
                "id": "/subscriptions/a052d33b-b7c4-4dc7-9e17-5c89ea594669/providers/Microsoft.Security/regulatoryComplianceStandards/Azure-CIS-1.1.0",
                "name": "Azure-CIS-1.1.0",
                "type": "Microsoft.Security/regulatoryComplianceStandards",
                "properties": {
                    "state": "Failed",
                    "passedControls": 21,
                    "failedControls": 3,
                    "skippedControls": 0,
                    "unsupportedControls": 87
                }
            }
        ]
    }
    

##### Case wall

**Result type** | **Value/Description** | **Type (Entity \ General)**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If status code 200 and after filtering we have data :** "Successfully retrieved regulatory controls for the provided standards in Microsoft Azure Security Center" **If status code 200 and after filtering we have no data :** "No regulatory standards were found in Microsoft Azure Security Center" **The action should fail and stop a playbook execution:** **If a fatal error, SDK error, like wrong credentials, no connection to the server, other is reported:** "Error executing action "List Regulatory Standards". Reason: {0}''.format(error.Stacktrace) **If State Filter contains invalid values:** "Error executing action "List Regulatory Standards". Reason: 'State Filter' parameter should only contain the following values: 'Passed', 'Failed', 'Skipped', 'Unsupported'.'' | General  
Case Wall Table | **Name:** Regulatory Standards **Column:**

  * Name 
  * State 
  * Passed Controls
  * Failed Controls
  * Skipped Controls
  * Unsupported Controls

| General  
  
### List Regulatory Standard Controls

List available controls related to standards in Microsoft Defender for Cloud.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Subscription ID | String | N/A | No | Specify the ID of the subscription for which you want to query information.Note: If subscription ID is provided at the integration level and action level, priority is given to the action configuration.  
Standard Names | CSV |  | Yes | Specify a comma-separated list of standard names for which you want to retrieve details. Example: Azure-CIS-1.1.0  
State Filter | CSV | Failed | No | Specify the comma-separated list of states. Example: Failed, Skipped. Only controls with the matching state will be returned. For example, if you specify "Failed", action will only return failed controls. Possible values: Passed,Failed,Unsupported,Skipped  
Max Controls To Return | String | 50 | No | Specify how many controls to return per standard.  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON result
    
    
    {
        "results": [
          "Name": "{Standard_name}",
          "Controls":
    [
            {
                "id": "/subscriptions/a052d33b-b7c4-4dc7-9e17-5c89ea594669/providers/Microsoft.Security/regulatoryComplianceStandards/Azure-CIS-1.1.0",
                "name": "Azure-CIS-1.1.0",
                "type": "Microsoft.Security/regulatoryComplianceStandards",
                "properties": {
                    "state": "Failed",
                    "passedControls": 21,
                    "failedControls": 3,
                    "skippedControls": 0,
                    "unsupportedControls": 87
                }
            }
        ]
    }
    

##### Case wall

Result type | Value/Description | Type (Entity \ General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If status code 200 and after filtering we have data for at least one standard(is_success = true) :** "Successfully retrieved regulatory controls for the following standards in Microsoft Azure Security Center:\n {0}".format(standard) **If fail for standard(is_success = true) :** "Action wasn't able to retrieve regulatory controls for the following standards in Microsoft Azure Security Center:\n {0}".format(standard) **If no data is found for some standards after filter (is_success=true):** "No regulatory controls were found for the following standards in Microsoft Azure Security Center:\n {0}".format(standard) **If no data is found for all standards based on filters:** "No regulatory controls were found for the provided standards." **The action should fail and stop a playbook execution:** **If a fatal error, SDK error, like wrong credentials, no connection to the server, other is reported:** "Error executing action "List Regulatory Standard Controls". Reason: {0}''.format(error.Stacktrace) **If State Filter contains invalid values:** "Error executing action "List Regulatory Standard Controls". Reason: 'State Filter' parameter should only contain the following values: 'Passed', 'Failed', 'Skipped', 'Unsupported'.'' | General  
Case Wall Table | **Table Name:** "Regulatory Controls: {0}".format(Standard) **Column:**

  * Name 
  * State 
  * Description
  * Passed Assessments
  * Failed Assessments
  * Skipped Assessments

| General  
  
### Ping

Test connectivity to Microsoft Defender for Cloud with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If successful:** "Successfully connected to the Azure Security Center server with the provided connection parameters!" **The action should fail and stop a playbook execution:** **If not successful:** "Failed to connect to the Azure Security Center server! Error is {0}".format(exception.stacktrace) | General  
  
### Update Alert Status

Update status of the alert in Microsoft Defender for Cloud.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Subscription ID | String | N/A | No | Specify the ID of the subscription for which you want to query information.Note: If subscription ID is provided at the integration level and action level, priority is given to the action configuration.  
Alert ID | String | N/A | Yes | Specify an ID of the alert, where you want to update status.  
Location | String | N/A | Yes | Specify the location of the alert. Example: centralus.  
Status | DDL | Resolve Possible values:

  * Dismiss
  * Reactivate
  * Resolve

| Yes | Specify the status for the alert.  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If status code 204 (is_success = true) :** "Successfully {0} alert with ID {1} in Microsoft Azure Security Center:\n {0}".format(dismissed/resolved/reactivated, alert_id) **If "errors" in the response (is_success = false) :** "Action wasn't able to {0} alert with ID {1} in Microsoft Azure Security Center. Reason: {2}".format(dismiss/resolve/reactivate, alert_id, errors/message) **The action should fail and stop a playbook execution:** **If a fatal error, SDK error, like wrong credentials, no connection to the server, other is reported:** "Error executing action "Update Alert Status". Reason: {0}''.format(error.Stacktrace) | General  
  
## Connectors

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

### Azure Security Center - Security Alerts Connector

**Important:** This connector will be fully deprecated on March 30, 2027. Until then, support is limited to critical bug fixes for ingestion issues; no new feature updates will be provided. Use the [Microsoft 365 Defender – Incidents Connector](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-365-defender#microsoft_365_defender_incidents_connector) instead. Note that migrating may require changes to your playbooks.

Pull security alerts from Microsoft Defender for Cloud.

**Note:** Dynamic list works with the `alertType` field.

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | resourceType | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
Client ID | String | N/A | True | Client ID of the Microsoft Entra application.  
Client Secret | Password | N/A | True | Client Secret of the Microsoft Entra application.  
Username | String | N/A | True | Username of the Microsoft Entra account.  
Password | Password | N/A | True | Password of the Microsoft Entra account.  
Subscription ID | String | N/A | True | Subscription ID of the Microsoft Entra application  
Tenant ID | String | N/A | True | Tenant ID of the Microsoft Entra application.  
Lowest Severity To Fetch | String | Low |  | Lowest severity that will be used to fetch Alert. Possible values: Low, Medium, High  
Max Alerts To Fetch | Integer | 50 | No | How many alerts to process per one connector iteration.  
Max Hours Backwards | Integer | 1 | No | How many hours backwards to fetch alerts.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, dynamic list will be used as a blocklist.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verify the SSL certificate for the connection to the Microsoft Defender for Cloud server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
Refresh Token | Password | N/A | No | Refresh token for the OAuth authorization.  
  
#### Connector rules

##### Proxy support

The connector supports proxy.

## Jobs

To configure jobs in Google SecOps, go to **Response > Job Scheduler**.

### Refresh Token Renewal Job

The goal of the Refresh Token Renewal Job is to periodically update the refresh token used in the integration. 

By default, the refresh token expires every 90 days, thus making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that the refresh token is up to date.

#### Job inputs

To configure the job, use the following parameters:

Parameters  
---  
Integration Environments | _Optional_ Integration environments which the job updates the refresh tokens for. This parameter accepts multiple values as a comma-separated string. Enclose individual values in quotation marks (`" "`).  
Connector Names | _Optional_ Connector names which the job updates the refresh tokens for. This parameter accepts multiple values as a comma-separated string. Enclose individual values in quotation marks (`" "`).  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
