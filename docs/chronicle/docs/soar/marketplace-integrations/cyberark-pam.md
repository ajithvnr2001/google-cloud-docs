---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cyberark-pam/
title: Integrate CyberArk PAM with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:34:32.842243+00:00
---

# Integrate CyberArk PAM with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cyberark-pam/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate CyberArk PAM with Google SecOps

This document provides guidance on how to integrate CyberArk Privileged Access Manager with Google Security Operations.

## Before you begin

To configure CyberArk PAM to work with the integration you need to create a user for the integration and provide that user with the permissions to access needed CyberArk PAM vaults.

### Create a user

Complete the following steps to create a user for the integration:

  1. Sign in to the PrivateArk Client as an administrator.
  2. Go to **Tools > Administrative Tools > Users and Groups**.
  3. In the **Users and Groups** dialog, select the user location, click **New** , and select **User**.
  4. In the different tabs of the **New User** dialog, fill in the information as needed. The **General** and the **Authentication** tabs are mandatory.



For more information about creating a user, see [Add a user to a Vault](https://docs.cyberark.com/pam-self-hosted/13.0/en/Content/PASIMP/Managing-Users.htm?TocPath=Administrator%7CUser%20Management%7C_____4#AddausertoaVault).

### Grant permissions to the created user

Complete the following steps to add access to a vault to a newly created user:

  1. Sign in to the PrivateArk Client as an administrator.
  2. Select the vault you want to provide access to and sign in to it (double-click it).
  3. From the top menu, click **Owners**.
  4. To add a new user, click **Add**.
  5. In the dialog, select the user.
  6. In the **Authorized to** section, select at least the following permissions: 
     * `Monitor Safe`
     * `Retrieve files from Safe`
     * `Store files in Safe`
     * `Admisiter Safe`
  7. To save changes, click **OK**.
  8. To exit the dialog window, click **Close**.



### Optional: Configure client certificate

You can use existing or make a new client certificate for secure communications between the CyberArk PAM instance and Google SecOps SOAR. For more information about how to configure the client certificate, see [Central Credential Provider web service configuration](https://docs.cyberark.com/credential-providers/Latest/en/Content/CCP/Configure_CCPWindows.htm?tocpath=Administration%7CCentral%20Credential%20Provider%20\(CCP\)%7CCentral%20Credential%20Provider%20web%20service%20configuration%7C_____0).

## Integrate CyberArk PAM and Google SecOps

The integration requires the following parameters:

Parameters | Description  
---|---  
`API Root` | _Required_ The API root URL.Provide the value in the following format: `https://IP_ADDRESS :PORT`.  
`Username` | _Required_ The username to connect with.  
`Password` | _Required_ The password to connect with.  
`Verify SSL` | _Optional_ If selected, the integration verifies that the SSL certificate for the connection to the CyberArk server is valid. Selected by default.  
`CA Certificate` | _Required_ The CA certificate to use for validating the secure connection to the API root.This parameter accepts the CA certificate in a form of the Base64 encoded string.  
`Client Certificate` | _Optional_ If configured for CyberArk PAM, specify the CyberArk client certificate to use for establishing a connection to the API root. Provide the certificate as the PFX file (in the PKCS #12 format).  
`Client Certificate Passphrase` | _Optional_ The passphrase required for the client certificate.   
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Get Account Password Value

Use the **Get Account Password Value** action to get the account password value from CyberArk.

With this action, you can retrieve both the password and SSH key.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Get Account Password Value** action requires the following parameters:

Parameters | Description  
---|---  
`Account` | _Required_ The account ID for which to retrieve the password value. Note: The account ID can be retrieved from the **List Accounts** action.  
`Reason` | _Required_ The reason to access the account password value. The default value is automatically retrieved from Google SecOps SOAR.  
`Ticketing System Name` | _Optional_ The name of the ticketing system.  
`Ticket ID` | _Optional_ The ticketing system ticket ID.  
`Version` | _Optional_ The account password value version to retrieve.  
  
#### Action outputs

The **Get Account Password Value** action provides the following outputs:

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

The following example describes the JSON result output received when using the **Get Account Password Value** action:
    
    
    {
     "content": "PASSWORD_VALUE"
    }
    

##### Output messages

The **Get Account Password Value** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully fetched password value for account ID ACCOUNT_ID` `Password value for account with ID ACCOUNT_ID and supplied version VERSION was not found in the CyberArk PAM.` | Action succeeded.  
`Error executing action "Get Account Password Value". Reason: ERROR_REASON` | Action failed.Check the connection to the server, the input parameters, or the credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Get Account Password Value** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List Accounts

Use the **List Accounts** action to list accounts available in CyberArk PAM based on the criteria provided.

This action doesn't run on Google SecOps SOAR entities.

#### Action inputs

The **List Accounts** action requires the following parameters:

Parameters | Description  
---|---  
`Search Query` | _Required_ The search query to use.  
`Search operator` | _Required_ The search operator to use for running a search based on the provided search query.Possible values are as follows: 

  * `contains`
  * `startswith`

. The default value is `contains`.  
`Max Records To Return` | _Required_ The number of records to return. If you provide no value, the action returns 50 records (API default).  
`Records Offset` | _Required_ The offset for the action to return the values.  
`Filter Query` | _Required_ The filter query to use. You can base the filter on the `safeName` or `modificationTime` parameters.  
`Saved Filter` | _Required_ The saved filter query to use.This parameter takes priority over the `Filter Query` parameter.  
  
#### Action outputs

The **List Accounts** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall Table

On a Case Wall, the **List Accounts** action provides the following table:

Table name: **Available PAM Accounts**

Table columns:

  * **ID**
  * **Safe Name**
  * **User Name**
  * **Secret Type**



##### JSON result

The following example describes the JSON result output received when using the **List Accounts** action:
    
    
    {
       "value": [
           {
               "categoryModificationTime": 1672051160,
               "platformId": "WinDomain",
               "safeName": "UserTestSafe",
               "id": "33_3",
               "name": "user@example.com",
               "address": "user@example.com",
               "userName": "user",
               "secretType": "password",
               "platformAccountProperties": {},
               "secretManagement": {
                   "automaticManagementEnabled": true,
                   "lastModifiedTime": 1672051160
               },
               "createdTime": 1672051160
           }
       ],
       "count": 1
    }
    

##### Output messages

The **List Accounts** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully found accounts for the criteria provided in CyberArk PAM.` `No accounts were found for the criteria provided in CyberArk PAM.` `Both the Filter Query and Saved Filter parameters are provided, Saved Filter takes priority.` | Action succeeded.  
`Error executing action "List Accounts". Reason: ERROR_REASON` | Action failed.Check the connection to the server, the input parameters, or the credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **List Accounts** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the * **Ping** action to test connectivity to CyberArk.

This action doesn't run on Google SecOps entities.

#### Integration inputs

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

The **Ping** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the CyberArk PAM installation with the provided connection parameters!` | Action succeeded.  
`Failed to connect to the CyberArk PAM installation! Error is ERROR_REASON` | Action failed.Check the connection to the server, the input parameters, or the credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Change Account Password

Use the **Change Account Password** action to queue an immediate password change task in CyberArk PAM. 

**Note:** There is a localized processing delay between the task being queued and it being executed by the Central Policy Manager (CPM).

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Change Account Password** action requires the following parameters:

Parameters | Description  
---|---  
`Account ID` | _Required_ A comma-separated list of the account IDs to queue for an immediate password change task. Note: You can retrieve target account ID strings directly from the output parameters of the **List Accounts** action.  
  
#### Action outputs

The **Change Account Password** action provides the following outputs:

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

The following example describes the JSON result output received when using the **Change Account Password** action:
    
    
    {
      "successful_accounts": [
        "28_12"
      ],
      "failed_accounts": [
        {
          "account_id": "36_4",
          "error": "The account is not managed by the CPM"
        }
      ]
    }
    

##### Output messages

The **Change Account Password** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully queued immediate password change task for the following accounts: ACCOUNT_IDS` | Action succeeded.  
`Error executing action "Change Account Password". Reason: ERROR_REASON` | Action failed.Check the connection to the server, target account ID values, or administrative CPM configuration settings.  
  
##### Script result

The following table describes the values for the script result output when using the **Change Account Password** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
## Jobs

For more information on jobs, see [ Configure a new job](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#configure-a-new-job) and [ Advanced scheduling](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#advanced-scheduling). 

### CyberArk PAM - Sync Integration Credentials Job

Use the **CyberArk PAM - Sync Integration Credentials Job** to automatically fetch account credentials and secrets from CyberArk PAM and synchronize them into Google SecOps SOAR by dynamically updating configurations for integration instances, connectors, and scheduled jobs.

**Note:** The job only updates Google SecOps SOAR configurations when an account's version changes in CyberArk PAM. 

Credential retrieval requests are logged in CyberArk PAM with the reason `Google SecOps SOAR automated credential synchronization`.

#### Job parameters

The **CyberArk PAM - Sync Integration Credentials Job** requires the following parameters:

Parameter | Description  
---|---  
`API Root` | Required. The API root URL of CyberArk PAM. If no value is provided, the job refers to the value provided in the integration configuration.  
`Username` | Required. The username used to connect to CyberArk PAM. If no value is provided, the job refers to the value provided in the integration configuration.  
`Password` | Required. The password used to connect to CyberArk PAM. If no value is provided, the job refers to the value provided in the integration configuration.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the CyberArk PAM server. Enabled by default.  
`CA Certificate` | Optional. The Base64-encoded CA certificate used to validate the SSL connection to the API root.  
`Client Certificate` | Optional. The Base64-encoded client certificate used for mutual TLS authentication.  
`Client Certificate Passphrase` | Optional. The passphrase required for the client certificate (if encrypted).  
`Environment Name` | Required. The name of the Google SecOps SOAR environment in which to look up and update integration instances, connectors, and jobs. For shared environments, supply `*`. The default value is `Default Environment`.  
`Credential Mapping` | Required. The JSON or YAML mapping string that maps SOAR integration instances, connectors, and jobs to their CyberArk PAM account paths. Values must use the `accounts/<account_id>` or `accounts/<account_id>/versions/<version_id>` format. The default value is `{"integration_instances": {"Integration_Instance_Name": {"Parameter_Name": "accounts/Account_ID"}}}`.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
