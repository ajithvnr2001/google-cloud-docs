---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-azure-sentinel/
title: Microsoft Sentinel \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:54.847607+00:00
---

# Microsoft Sentinel  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-azure-sentinel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Microsoft Sentinel

**Important:** In the Google SecOps platform, the Microsoft Sentinel integration is called _Microsoft Azure Sentinel_.

This document provides guidance on how to integrate Microsoft Sentinel with Google SecOps.

This integration uses one or more open source components. You can download a zipped copy of the full source code of this integration from the [Cloud Storage bucket](https://storage.googleapis.com/csoar_public_integrations/MicrosoftAzureSentinel.zip).

## Use cases

  1. Monitor and inspect alerts created in Sentinel based on events flowing from both on-premise hosts and cloud-based Microsoft services like Microsoft 365 and Microsoft 365 Cloud App Security.
  2. Use data gathered and correlated in Sentinel for enrichments, while investigating a particular incident. Analysts can use the data that was gathered and stored in Sentinel in investigations, for example, to "drill down" to particular information (inspect alert data, for example, inspect Syslog logs) or query for activity in specific time period or from particular hosts.



## Prerequisites

You need authorization in Microsoft Entra ID to configure it first in order to execute requests against the Microsoft Security Insights API. You will need to configure permissions:

  * Create the Microsoft Entra app.
  * Create a client secret.
  * Grant the registered Microsoft Entra app access to the Microsoft Sentinel Workspace.
  * Use the Microsoft Entra application to get an access token.

**Note:** Microsoft Security Insights API supports Microsoft Entra authentication with three different OAuth2 flows: client credentials, authorization flow, and implicit. If you are unfamiliar with OAuth2, take a moment to familiarize yourself with [Microsoft identity platform and OAuth 2.0 authorization code flow](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-protocols-oauth-code).

### Create Microsoft Entra app

  1. Sign in to the [Azure portal](https://portal.azure.com/) as a user administrator or a password administrator.

  2. Select **Microsoft Entra ID**.

  3. Go to **App registrations > New registration**.

  4. Enter the name of the app.

  5. Select applicable **Supported account type**.

  6. Click **Register**.

  7. Save the **Application (client) ID** and **Directory (tenant) ID** values to use them later when configuring the integration parameters.




### Create client secret

  1. Navigate to **Certificates and secrets > New client secret**.

  2. Provide a description for a client secret and set its expiration deadline.

  3. Click **Add**.

  4. Save the value of the client secret (not the secret ID) to use it as the `Client Secret` parameter value when configuring the integration. The client secret value is only displayed once.




### Give registered Microsoft Entra access to the Microsoft Sentinel Workspace

  1. Go to the Microsoft Sentinel Overview page.

  2. Click **Settings**.

  3. Click **Access control (IAM)**.

  4. In the **Add a role assignment** section, click **Add**.

  5. Configure the following parameters:

     * Role = `Azure Sentinel Contributor`.

     * Assign access to = `default, Microsoft Entra ID user group, or service principal`.

  6. In the **Select** section, provide a search condition to find your app and add a role assignment for your app.

  7. Go to the Microsoft Sentinel workspaces page. Find and configure the following parameters:

     * `Azure Resource Group`
     * `Azure Sentinel Workspace Name`



## Integrate Microsoft Sentinel with Google SecOps SOAR

For detailed instructions on how to configure an integration in Google Security Operations, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

**Important:** If you make any changes to the **Application Permissions** or **API Permissions** in your Microsoft Entra ID (Azure AD) App Registration after configuring this integration (for example, adding a new permission for a job to run), you must regenerate and update your credentials in Google SecOps. 

This typically means:

  * Generating a new client secret in your App Registration.
  * Updating the client secret (and regenerating the refresh token, if applicable) in the Google SecOps integration configuration.



Failure to update will prevent new permissions from being applied, causing actions to fail.

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Azure Subscription ID | String | N/A | Yes | Microsoft Azure Subscription ID, can be viewed in Azure Portal > Subscriptions > <Your Subscription> Subscription ID.  
Azure Active Directory ID | String | N/A | Yes | Microsoft Entra Tenant ID, can be viewed in Microsoft Entra > App Registration > <Application you configured for your integration> Directory (tenant) ID.  
Api Root | String | https://management.azure.com | Yes | Management.azure.com API root URL to use with integration.  
Azure Resource Group | String | N/A | Yes | Name of Azure Resource Group where Microsoft Sentinel is located.  
Azure Sentinel Workspace Name | String | N/A | Yes | Name of the Microsoft Sentinel workspace to work with. Can be viewed in Azure portal > Microsoft Sentinel > Microsoft Sentinel Workspaces.  
Client ID | String | N/A | Yes | Client (Application) ID that was added for the app registration in Microsoft Entra for this integration.  
Client Secret | Password | N/A | Yes | A secret that was entered for Azure Sentinel app registration.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

Test connectivity to Microsoft Sentinel workspace with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Use cases

Action is used to test the connectivity at the integration configuration page in the Google SecOps Content Hub page, and it can be executed as a manual action, which is not used in playbooks.

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output Message* | **If successful:** print "Successfully connected to the Microsoft Sentinel Workspace with the provided connection parameters!".  
**If not successful:** print "Failed to connect to the Microsoft Sentinel Workspace! Error is {0}".format(exception.stacktrace). | General  
  
### List Incidents

List Microsoft Sentinel incidents based on the provided search criteria.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Time Frame | Integer | 3 | No | Specify a timeframe in hours for which to fetch incidents.  
Status | String | New, Active, Closed | No | Specify the statuses of the incidents to look for. Parameter accepts multiple values as a comma-separated string.  
Severity | String | Informational, Low, Medium, High | No | Specify the severities of the incidents to look for. Parameter accepts multiple values as a comma-separated string.  
How Many Incidents to Fetch | Integer | 200 | No | How many incidents to fetch. By default, latest 200 incidents are returned.   
  
#### Use cases

The action can be used to list Microsoft Sentinel incidents from the Google SecOps playbook.

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "value": [
            {
                "id": "/subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP/providers/Microsoft.OperationalInsights/workspaces/WORKSPACE/providers/Microsoft.SecurityInsights/Cases/323032be-5b0d-4661-944f-ff9557597e50",
                "name": "323032be-5b0d-4661-944f-ff9557597e50",
                "etag": "\"2100e65a-0000-0d00-0000-5de3b1bf0000\"",
                "type": "Microsoft.SecurityInsights/Cases",
                "properties": {
                    "title": "Suspicious process injection observed",
                    "description": "A process abnormally injected code into another process, As a result, unexpected code may be running in the target process memory. Injection is often used to hide malicious code execution within a trusted process. \nAs a result, the target process may exhibit abnormal behaviors such as opening a listening port or connecting to a command and control server.",
                    "severity": "Medium",
                    "status": "New",
                    "labels": ["add_tag"],
                    "endTimeUtc": "2019-11-29T03:42:05Z",
                    "startTimeUtc": "2019-11-29T03:42:05Z",
                    "owner": {
                        "objectId": null
                    },
                    "lastUpdatedTimeUtc": "2019-12-01T12:27:43Z",
                    "createdTimeUtc": "2019-11-29T07:13:32.0266519Z",
                    "relatedAlertIds": ["2462474c-b6d9-6937-17ee-c2a62671c2f8"],
                    "relatedAlertProductNames": ["Microsoft Defender Advanced Threat Protection"],
                    "caseNumber": 2276,
                    "totalComments": 0,
                    "metrics": {
                        "SecurityAlert": 1
                    },
                    "firstAlertTimeGenerated": "2019-11-29T07:13:31.961602Z",
                    "lastAlertTimeGenerated": "2019-11-29T07:13:31.961602Z"
                }
            },{
                "id": "/subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP/providers/Microsoft.OperationalInsights/workspaces/WORKSPACE/providers/Microsoft.SecurityInsights/Cases/c7939be8-32fb-415c-9f7c-c13325d6c48b",
                "name": "c7939be8-32fb-415c-9f7c-c13325d6c48b",
                "etag": "\"1900f5e2-0000-0d00-0000-5de0c5110000\"",
                "type": "Microsoft.SecurityInsights/Cases",
                "properties": {
                    "title": "Suspicious Power Shell command line",
                    "description": "A suspicious PowerShell activity was observed on the machine. \nThis behavior may indicate that PowerShell was used during installation, exploration, or in some cases in lateral movement activities which are used by attackers to invoke modules, download external payloads, or get more information about the system. Attackers usually use PowerShell to bypass security protection mechanisms by executing their payload in memory without touching the disk and leaving any trace.\r\nOur algorithms found the behaviors of this process to be suspicious due to the following factors:\nSuspicious memory activity\nExecutes suspicious PowerShell commands",
                    "severity": "Medium",
                    "status": "New",
                    "labels": [],
                    "endTimeUtc": "2019-11-29T03:42:04.9552017Z",
                    "startTimeUtc": "2019-11-29T03:42:04.9552017Z",
                    "owner": {
                        "objectId": null
                    },
                    "lastUpdatedTimeUtc": "2019-11-29T07:13:21Z",
                    "createdTimeUtc": "2019-11-29T07:13:21.6858164Z",
                    "relatedAlertIds": [
                        "d053f17e-6153-d171-9f4d-82389442aa35"
                    ],
                    "relatedAlertProductNames": [
                        "Microsoft Defender Advanced Threat Protection"
                    ],
                    "caseNumber": 2275,
                    "totalComments": 0,
                    "metrics": {
                        "SecurityAlert": 1
                    },
                    "firstAlertTimeGenerated": "2019-11-29T07:13:21.5885314Z",
                    "lastAlertTimeGenerated": "2019-11-29T07:13:21.5885314Z"
                }
            }
        ],
        "nextLink": "https://management.azure.com:443/subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP/providers/Microsoft.OperationalInsights/workspaces/WORKSPACE/providers/Microsoft.SecurityInsights/Cases?api-version=2019-01-01-preview&$skipToken=H4sIAAAAAAAEAE1VTVMiSxD8MR45LIstukbsIbvnqxmGcRgR2xsiFqA44soiHt5vf1nzfOwaQUg31fWRlVnVGfvo8p-Jf5jhavBejW1_jQvon5OfP0_G15ffT67H7rLX7fIQXQ4P64vB583efZqXUSo7zGaRvS4-inWzK9Z-V3ze3RSfxfko8ufFdfy7jIpu8Snd8vkXTnx9c9k78XF52T87O-2fJFdXlxCZfMUDItN-zflJ2m9o-EmRx13Efi52cvw9Fnf2LBmvkW0-aBJwK8kUSYPp0R88pm_m9s-5gg2uKx9y9PMMu1yuOqgNaklrOGPfBDtMAu4FfawNZpJ2EDXWChZYGCwl2iBt7EpQovKARD1k3pb6u_Vqt4ELdqy_nw7mhSQ7pN5e6RnGbQQ9PDUYSNpHEnAjaQzUtiM2x71HLoMNoXCVoMZMz4wHg6FkueaXCrZYBHiJWYG3tEuRVke8Dog69ccs9uJ2wNxaJJ55OsASmmDvBB3F7VaQoarQ0XzjyiKOe4gDluo0laO_HN752wa_5a6-Ow3x_R88BYU_yOt7b1B6PPyN-_Ps6fHv8_ez7vLv876R1fFs2fftaLqsFjgPUV9GNevPzqRc4D1EvyXvYGPYN2yHfv9_XnYBt7A77ddgh-fgSin6tM_mEh3sqcFaHrb4HqI7sStrGvcm-RafjTMy7GHl7d262WDR2B-Sl9g27pcMD3gI2TfGsYx_LqMF3kJUSdnjO2QyP-DdR5EMd1gaPB3zT0E_5Uz9PjXsc1TiNtieDDroBdr73AafXMg0tXUTL-Wxr_cdGfUYN5qITzEPvXu51fjOyjDFKkSPks6Ytw1S9e0oJE4ea4xDZsgje9bikdqdd-eS7zA49p_0Sxb-1KdP4nd4CW4pfoVNg0TmM-JD-0GNZXAHGXbw4l0jWY1n40T9rIx7krRXLrwbiZ_ixdAuW9A-Wio-pyZKJT_gYNyH5n0d0ldJOuxnJFLMGMd2xYWjvgbChG5XSWPcWP3Q316GW5SGOEe5fQxJLVXqbkzcl3pnfcjexP3R5w9KvfkgPw3GcLHyc6p-Jh5d1ZElXwUrXDX4IW6hI8SL7ek82JIHuDKq4xWyVrf6X_WZwXueaVc2eBe3Jf8hjufU41yiVOPYPa9UD3oeNvgU6sex7-JKeMN41OWQI-br_lTiKUaN6qqGb_W9UOndq95co_lu4APIx43ml4lVnmMjrsbIMB5lmhvOA94XBhOxrBfVs7gp-45X9RMFjj47o36t0zmVCGXrVVH4T5AxgmAILdDZVOfUTmTl8yM_CNLryj4aFzSfNGgczolf0FkQZ4orpcU4HIZWtVqJc_qSw3elcWDhUATOI-LP_DPBTOvjHDogC4j2joOWqei7rFGdMNv2HVxpiBftaB8RX1bIy2SF2qOnOHLOpWKd4hjEliyWzxolAeMRp0x5gIHmfa15JgbcC6nyICiuxOmpzXdOXPh-oPOSc5D2Y62F9U2UF8OAR84FjRfpPGU_K-0reVBVbqV822nfuU_4Tir2s5R4q3lM27447gX6rwxG4gqlJhQh8uWXuI32nfypHPMrxXW03y-ijPb8nXhfeRjtq9V-sq_s00RxoX2u8xzKD3fQep-Ur2xFrf1ivE_pLLJXk1SSpyga9bsD56KNW9nJN9UBeeR4pa2qFNdE9wd5ETOBmPyhXu7b-i-YpDYV1VL3j2_76cA7r3WQ13eKD_F0MXk58Lj6wtdXxD1S3nP_MQ-397E2vmr3o2e-xIlbhfEP2s_f4mbah1jrJL573a_EdSRc2eTDWnXoW35wL7X17rT-i5YXc8ut1Oqzrzrm3nRfOA0Vp6TlH3kvvrUbNHhWnCOv_c25l6lL8iXlnod6t1i1um9QtHwMzIP99OrHFvTrFBTV1rnyKt4zb8VJ9cX6klYPFR2pJJzydy12q3ik6geqa-ojbeeItbTnHnfUVfXzX2qVoX91CQAA"
    }
    

##### Case wall

Result Type | Value/ Description | Type  
---|---|---  
Output Message* | if successful and obtains data: print "Successfully returned Microsoft Sentinel incidents".  
If nothing found: print "Action was not able to find any incidents".  
if error: print "Failed to list Microsoft Sentinel incidents! Error is {0}".format(exception.stacktrace). | General  
Table | **Table title:** Microsoft Sentinel incidents found**:****Columns:** incident_number, incident_id, title, description, severity, status, labels, assigned to, alert product names, created time, last updated time | General  
Attachments | List_Incidents.json - contains returned by the action technical JSON data.  | General  
JSON Viewer  
(Only if the table is not optional) | Show the JSON viewer for the query result. | General  
  
### Update Incident Details

Update a Microsoft Sentinel incident.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Incident Case Number | Integer | N/A | Yes | Specify Azure Sentinel incident number to update.  
Title | String | N/A | No | Specify new title for the Azure Sentinel incident.  
Severity | DDL | Not Updated (possible values: Not Updated, Informational, Low, Medium, High) | No | Specify new severity for the Azure Sentinel incident.  
Description | String | N/A | No | Specify new description for the Azure Sentinel incident.  
Assigned To | String | N/A | No | Specify the user to assign the incident to.  
Status | DDL | Not Updated (possible values: Not Updated, New, Active, Closed) | No | Specify new status status for the Azure Sentinel incident.  
Closed Reason | DDL | Not Updated (possible values:   
Not Updated, True Positive - suspicious activity, Benign Positive - suspicious but expected,   
False Positive - incorrect alert logic, False Positive - inaccurate data, Undetermined) | No | If status of the incident is set to Closed, provide a Closed Reason for the incident.  
Closing Comment | String | N/A | No | Optional closing comment to provide for the closed Azure Sentinel Incident.  
Number of retries | Integer | 1 | Yes | Specify the number of retry attempts the action should make if the incident update was unsuccessful.  
Retry Every | Integer | 20 | Yes | Specify the time period for the action to wait between incident update retries.  
  
#### Use cases

The action can be used to update a Microsoft Sentinel incident from the Google SecOps playbook. It an be used as a resulting action in a workflow that involves analysis of a Microsoft Sentinel incident, once incidents were processed in Google SecOps, incidents can then be updated to indicate the progress of the analysis of the incident (e.g. set assignedTo, set Status as inProgress, etc).

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result

JSON result is returned for the Request 2, and contains the following updated incident details:
    
    
    {
      "id": "/subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP/providers/Microsoft.OperationalInsights/workspaces/WORKSPACE/providers/Microsoft.SecurityInsights/Cases/9e5c0afc-b7a6-4eac-8164-9242ad710a66",
      "name": "9e5c0afc-b7a6-4eac-8164-9242ad710a66",
      "etag": "\"12002b5c-0000-0d00-0000-5dde83730000\"",
      "type": "Microsoft.SecurityInsights/Cases",
      "properties": {
          "title": "Activity from a Tor IP address",
          "description": "A failed sign in was detected from a Tor IP addressThe Tor IP address 203.0.113.200 was used by Example User - Test User Spec (user@example.com).",
          "severity": "Informational",
          "status": "InProgress",
          "assignedTo": "test@example.com",
          "labels": [],
          "closeReason": "Resolved",
          "endTimeUtc": "2019-11-27T01:56:03.4651258Z",
          "startTimeUtc": "2019-11-27T01:56:03.4651258Z",
          "owner": {
              "objectId": null,
              "email": "test@example.com"
          },
          "lastUpdatedTimeUtc": "2019-11-27T14:08:51Z",
          "createdTimeUtc": "2019-11-27T05:01:11.1139394Z",
          "relatedAlertIds": [
              "2a96343c-e551-4529-96f1-18d6f734470d"
          ],
          "relatedAlertProductNames": [
              "Azure Sentinel"
          ],
          "caseNumber": 2274,
          "totalComments": 0,
          "metrics": {
              "SecurityAlert": 1
          },
          "firstAlertTimeGenerated": "2019-11-27T05:01:10.2574659Z",
          "lastAlertTimeGenerated": "2019-11-27T05:01:10.2574659Z"
      }
    }
    

##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output Message* | **If successful:** print "Successfully updated Microsoft Sentinel incident {0}".format(IncidentID).  
**If can't find the incident by the provided incident case number:** print "Microsoft Sentinel Incident with case number {0} was not found!".format(incident_case_number).  
**If error:** print "Failed to update Microsoft Sentinel incident! Error is {0}".format(exception.stacktrace). | General  
  
### Update Incident Labels

Update labels on a specific Microsoft Sentinel incident.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Incident Case Number | Integer | 2273 | Yes | Specify Azure Sentinel incident number to update with new labels.  
Labels | String | malware | Yes | Specify new labels that should be appended to the Incident. Parameter accepts multiple values as a comma-separated string.  
Number of retries | Integer | 1 | Yes | Specify the number of retry attempts the action should make if the incident update was unsuccessful.  
Retry Every | Integer | 20 | Yes | Specify what time period action should wait between incident update retries.   
  
#### Use cases

The action can be used to update Microsoft Sentinel incident labels from the Google SecOps playbook. User can use this action to assign specific tags (labels) to specific incidents if it is needed. For example, if specific hosts are part of this incident there should be a specific label.

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result

JSON result is returned for the Request 2, and contains updated incident details:
    
    
    {
      "id": "/subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP/providers/Microsoft.OperationalInsights/workspaces/WORKSPACE/providers/Microsoft.SecurityInsights/Cases/9e5c0afc-b7a6-4eac-8164-9242ad710a66",
      "name": "9e5c0afc-b7a6-4eac-8164-9242ad710a66",
      "etag": "\"12002b5c-0000-0d00-0000-5dde83730000\"",
      "type": "Microsoft.SecurityInsights/Cases",
      "properties": {
          "title": "Activity from a Tor IP address",
          "severity": "Informational",
          "status": "InProgress",
          "labels": [
     "malware",
     "trojan"
       ],
          "endTimeUtc": "2019-11-27T01:56:03.4651258Z",
          "startTimeUtc": "2019-11-27T01:56:03.4651258Z",
          "owner": {
              "objectId": null,
          },
          "lastUpdatedTimeUtc": "2019-11-27T14:08:51Z",
          "createdTimeUtc": "2019-11-27T05:01:11.1139394Z",
          "relatedAlertIds": [
              "2a96343c-e551-4529-96f1-18d6f734470d"
          ],
          "relatedAlertProductNames": [
              "Azure Sentinel"
          ],
          "caseNumber": 2274,
          "totalComments": 0,
          "metrics": {
              "SecurityAlert": 1
          },
          "firstAlertTimeGenerated": "2019-11-27T05:01:10.2574659Z",
          "lastAlertTimeGenerated": "2019-11-27T05:01:10.2574659Z"
      }
    }
    

##### Case wall

Result Type | Value/ Description | Type  
---|---|---  
Output Message* | **if successful:** "Successfully updated Microsoft Sentinel incident {0} with the following labels: {1}".format(IncidentID, [labels_list]).   
**If can't find the incident by the provided incident case number:** "Microsoft Sentinel incident with case number {0} was not found!".format(incident_case_number).**If user have provided a label that already exists in the incident** (isSuccess=False): "The following labels were not added to the Microsoft Sentinel labels for incident {0} because they already exist: {1}".format(IncidentID, [labels_list])  
**If error:** "Failed to update Microsoft Sentinel incident labels! Error is {0}".format(exception.stacktrace). | General  
  
### Get Incident Statistics

Get Azure Sentinel incident statistics.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Time Frame | Integer | 3 | No | Specify the timeframe for which to show the statistics.  
  
#### Use cases

The action can be used for showing Google SecOps Playbook reports for Microsoft Sentinel events. This action will form part of the playbook in which a user interacts with Microsoft Sentinel's alarm created when, for example, a warning was processed and removed, this action could be implemented to view an outcome of Microsoft Sentinel incidents on the "lessons learned" page.

Conversely, it can be a user's interface method, instead of using the Windows Sentinel app, to remain in Google SecOps.

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "id": "/subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP/providers/Microsoft.OperationalInsights/workspaces/WORKSPACE/providers/Microsoft.SecurityInsights/Aggregations/Cases",
        "name": "Cases",
        "type": "Microsoft.SecurityInsights/Aggregations",
        "kind": "CasesAggregation",
        "properties": {
            "aggregationBySeverity": {
                "totalCriticalSeverity": 1,
                "totalHighSeverity": 2,
                "totalMediumSeverity": 554,
                "totalLowSeverity": 1714,
                "totalInformationalSeverity": 1
            },
            "aggregationByStatus": {
                "totalNewStatus": 2268,
                "totalInProgressStatus": 4,
                "totalResolvedStatus": 1,
                "totalDismissedStatus": 0,
                "totalTruePositiveStatus": 2,
                "totalFalsePositiveStatus": 1
            }
        }
    }
    

##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output Message* | **If successful and obtains data:** print "Successfully returned Microsoft Sentinel incident statistics".  
**If error:** print "Failed to get Microsoft Sentinel incident statistics! Error is {0}".format(exception.stacktrace). | General  
Table #1 | **Table title:** Microsoft Sentinel Incident statistics by Severity:**Columns:** Critical (mapped to totalCriticalSeverity), High (mapped to totalHighSeverity), Medium (mapped to totalMediumSeverity), Low(mapped to totalLowSeverity) , Informational(mapped to totalInformationalSeverity)  | General  
Table #2 | **Table title:** Microsoft Sentinel Incident statistics by Status:**Columns:** New(mapped to totalNewStatus), InProgress(mapped to totalInProgressStatus), Resolved(mapped to totalResolvedStatus), Dismissed(mapped to totalDismissedStatus) , TruePositive(mapped to totalTruePositiveStatus),FalsePositive(mapped to totaFalsePositiveStatus)  | General  
JSON Viewer  
(Only if table is not optional) | Show the JSON viewer for the query result. | General  
  
### List Alert Rules

Get Azure Sentinel scheduled rules list.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert Rule Severity | String | Informational, Low, Medium, High, Critical | No | Specify the severities of the alert rules to look for. The parameter accepts multiple values as a comma-separated string.  
Fetch Specific Alert Rule Types | String | N/A | No | Specify what alert types action should return. Parameter accepts multiple values as a comma-separated string.If value is not provided - return all possible alert types.  
Fetch Specific Alert Rule Tactics | String | N/A | No | Specify what alert rule tactics action should return. The parameter accepts multiple values as a comma-separated string. If the value is not provided - return all possible alert types.  
Fetch only Enabled Alert Rules? | Checkbox | Unchecked | No | Specify if action should return only enabled alert rules.  
Max rules to return | Integer | N/A | No | How many scheduled alert rules the action should return, for example, 50.  
  
#### Use cases

The action can be used to list Microsoft Sentinel alert rules from the Google SecOps playbook. You can list alert rules to make sure that you have prepared an alert rule for each type of threat and anomalies that are suspicious in your environment. If you see that some situations are not handled properly, you can immediately update an existing alert rules or create a new one. The Microsoft Sentinel alert rule makes sure that you are notified right away, so that you can triage, investigate, and remediate the threats.

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "value": [
            {
                "id": "/subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP/providers/Microsoft.OperationalInsights/workspaces/WORKSPACE/providers/Microsoft.SecurityInsights/alertRules/4bdce24d-7837-4f02-9f7a-10824f376517",
                "name": "4bdce24d-7837-4f02-9f7a-10824f376517",
                "etag": "\"00002f05-0000-0d00-0000-5d9db9970000\"",
                "type": "Microsoft.SecurityInsights/alertRules",
                "kind": "MicrosoftSecurityIncidentCreation",
                "properties": {
                    "productFilter": "Azure Active Directory Identity Protection",
                    "severitiesFilter": null,
                    "displayNamesFilter": null,
                    "displayName": "Create incidents based on Azure Active Directory Identity Protection alerts",
                    "enabled": true,
                    "description": "Create incidents based on all alerts generated in Azure Active Directory Identity Protection",
                    "tactics": null,
                    "alertRuleTemplateName": "532c1811-79ee-4d9f-8d4d-6304c840daa1",
                    "lastModifiedUtc": "2019-10-09T10:42:31.5264376Z"
                }
            },
            {
                "id": "/subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP/providers/Microsoft.OperationalInsights/workspaces/WORKSPACE/providers/Microsoft.SecurityInsights/alertRules/540f68c9-9397-49c7-8953-8efce08d6e62",
                "name": "540f68c9-9397-49c7-8953-8efce08d6e62",
                "etag": "\"00003105-0000-0d00-0000-5d9db9ad0000\"",
                "type": "Microsoft.SecurityInsights/alertRules",
                "kind": "MicrosoftSecurityIncidentCreation",
                "properties": {
                    "productFilter": "Azure Security Center",
                    "severitiesFilter": null,
                    "displayNamesFilter": null,
                    "displayName": "Create incidents based on Azure Security Center alerts",
                    "enabled": true,
                    "description": "Create incidents based on all alerts generated in Azure Security Center",
                    "tactics": null,
                    "alertRuleTemplateName": "90586451-7ba8-4c1e-9904-7d1b7c3cc4d6",
                    "lastModifiedUtc": "2019-10-09T10:42:53.9014288Z"
                }
            }
        ]
    }
    

##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output Message* | **If successful:** print "Successfully listed Microsoft Sentinel alert rules configured".  
**If error:** print "Failed to list Microsoft Sentinel alert rules! Error is {0}".format(exception.stacktrace). | General  
Table | **Table title:** Microsoft Sentinel Alert Rules found: **Columns:** AlertID (mapped to name), Name (mapped to displayName), Enabled, Description, Tactics, Last Modification Time (mapped to lastModificationUtc) | General  
Attachments | List_AlertRules.json - contains returned by the action technical JSON data.  | General  
JSON Viewer  
(Only if table is not optional) | Show the JSON viewer for the query result. | General  
  
### Get Alert Rule Details

Get details of the Azure Sentinel scheduled alert rule.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
AlertRuleID | String | N/A | Yes | Specify the ID of the alert rule.  
  
#### Use cases

The action can be used to get details about Microsoft Sentinel alert rule from the Google SecOps playbook. If you see, for example, that some alerts are becoming more frequent and most of them are false positives, or if one alert rule handles too many situations and you want to separate them, so that it is easier to identify the threat, you can use this action to properly understand the configuration of the alert rule. Based on the results of the alert rule, you can decide whether to update it, delete it, or leave it unchanged.

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "id": "/subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP/providers/Microsoft.OperationalInsights/workspaces/WORKSPACE/providers/Microsoft.SecurityInsights/alertRules/8dce4dbd-0ba6-4c93-943a-8da49f7d0aa4",
        "name": "8dce4dbd-0ba6-4c93-943a-8da49f7d0aa4",
        "etag": "\"0200c767-0000-0d00-0000-5ddf3b160000\"",
        "type": "Microsoft.SecurityInsights/alertRules",
        "kind": "Scheduled",
        "properties": {
            "severity": "High",
            "query": "SecurityEvent\r\n| where Activity startswith \"4625\"\r\n| summarize count() by IpAddress, Computer\r\n| where count_ >3\r\n| extend HostCustomEntity = Computer\r\n| extend IPCustomEntity = IpAddress",
            "queryFrequency": "PT1H",
            "queryPeriod": "P5D",
            "triggerOperator": "GreaterThan",
            "triggerThreshold": 0,
            "suppressionDuration": "PT5H",
            "suppressionEnabled": false,
            "displayName": "Multiple failed login attempts from the same IP",
            "enabled": false,
            "description": "",
            "tactics": [
                "InitialAccess"
            ],
            "alertRuleTemplateName": null,
            "lastModifiedUtc": "2019-11-28T03:12:21.9276927Z"
        }
    }
    

##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output Message* | **If successful and obtains data:** print "Successfully returned Microsoft Sentinel alert rule {0} details".format(AlertRuleID).  
**If can't find the alert rule by the provided AlertID:** print "Microsoft Sentinel alert rule with ID "{0}" was not found!".format(AlertRuleID).   
**If error:** print "Failed to get details about Microsoft Sentinel alert rule! Error is {0}".format(exception.stacktrace). | General  
Table | **Table title:** Microsoft Sentinel Alert Rule Details: **Columns:** AlertID (mapped to name), Name (mapped to displayName), Enabled, Description, Query, Frequency(mapped to queryFrequency), Period of Lookup data(mapped queryPeriod), Trigger (mapped as combination of triggerOperator and triggerThreshold) Tactics, Enable Suppression(mapped as "suppressionEnabled"), Suppression Duration(mapped as suppressionDuration )Last Modification Time (mapped to lastModificationUtc) | General  
JSON Viewer  
(Only if the table is not optional) | Show the JSON viewer for the query result. | General  
  
### Create Alert Rule

Create Azure Sentinel scheduled alert rule.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Enable Alert Rule | DDL | N/A | Yes | Specify whether you want to disable or enable this alert rule.  
Name | String | N/A | Yes | Specify the display name of the alert rule.  
Severity | DDL | N/A | Yes | Specify the severity of this alert rule.  
Query | String | N/A | Yes | Specify the query of this alert rule.  
  
  
Frequency | String | N/A | Yes | Specify how frequently to run the query, use the following format: PT + number + (M, H, D),where M - minutes, H - hours, D - days.Minimum is 5 minutes, maximum is 14 days.   
Period of Lookup Data | String | N/A | Yes | Specify the time of the last lookup data, use the following format: P + number + (M, H, D),where M - minutes, H - hours, D - days. Minimum is 5 minutes, maximum is 14 days.  
  
Trigger Operator | DDL | N/A | Yes | Specify the trigger operator for this alert rule.  
Trigger Threshold | Integer | N/A | Yes | Specify the trigger threshold for this alert rule.  
Enable Suppression | DDL | N/A | Yes | Specify whether you want to stop running query after alert is generated.  
Suppression Duration | String | N/A | Yes | Specify for how long you want to stop running query after alert is generated, use the following format: PT + number + (M, H, D),where M - minutes, H - hours, D - days Examples:P1M - 1 minute P10H - 10 hoursP2D - 2 days.Minimum is 5 minutes, maximum is 14 days.  
Description | String | N/A | No | Specify the description for this alert rule.  
Tactics | String | N/A | No | Specify tactics for this alert rule.Parameter can take multiple comma-separated values.  
  
#### Use cases

The action can be used to create Microsoft Sentinel alert rules from the Google SecOps playbook. You can create a custom alert rules to help you search for the types of threats and anomalies that are suspicious in your environment. The Microsoft Sentinel alert rule makes sure that you are notified right away, so that you can triage, investigate, and remediate the threats.

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
#### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output Message* | **If successful:** print "Successfully created Microsoft Sentinel alert rule!".  
**If error:** print "Failed to create Microsoft Sentinel alert rule! Error is {0}".format(exception.stacktrace).  | General  
  
### Update Alert Rule

Update Azure Sentinel scheduled alert rule.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
AlertRuleID | String | N/A | Yes | Specify the AlertRuleID of the alert rule.  
Name | String | N/A | No | Specify the display name of the alert rule.  
Enable Alert Rule | DDL | N/A | No | Specify whether you want to disable or enable this alert rule.  
Severity | DDL | N/A | No | Specify the severity of this alert rule.  
Query | String | N/A | No | Specify the query of this alert rule.  
Frequency | String | N/A | No | Specify how frequently to run the query, use the following format: PT + number + (M, H, D),where M - minutes, H - hours, D - days. Examples: PT1M - run query every minutePT10H - run query every 10 hours PT2D - Run query every 2 days.Minimum is 5 minutes, maximum is 14 days.  
Period of Lookup Data | String | N/A | No | Specify the time of the last lookup data, use the following format: P + number + (M, H, D),where M - minutes, H - hours, D - days. . Examples:P1M - 1 minuteP10H - 10 hoursP2D - 2 days. Minimum is 5 minutes, maximum is 14 days.  
Trigger Operator | DDL | N/A | No | Specify the trigger operator for this alert rule.  
Trigger Threshold | Integer | N/A | No | Specify the trigger threshold for this alert rule.  
Enable Suppression | DDL | N/A | No | Specify whether you want to stop running query after alert is generated.  
Suppression Duration | String | N/A | No | Specify for how long you want to stop running query after alert is generated, use the following format: PT + number + (M, H, D),where M - minutes, H - hours, D - days Examples:P1M - 1 minute P10H - 10 hoursP2D - 2 days.Minimum is 5 minutes, maximum is 14 days.  
Description | String | N/A | No | Specify the description for this alert rule.  
Tactics | String | None | No | Specify tactics for this alert rule.Parameter accepts multiple comma-separated values.  
  
#### Use cases

The action can be used to update Microsoft Sentinel alert rules from the Google SecOps playbook. If you see, for example, that some alerts are becoming more frequent and most of them are false positives, you can use this action to update the configuration of the alert rule to match your needs and desires. The Microsoft Sentinel alert rule makes sure that you are notified right away, so that you can triage, investigate, and remediate the threats.

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output Message* | **If successful:** print "Successfully updated Microsoft Sentinel alert rule with ID {0}".format(AlertRuleID).  
**If can't find an alert rule by the provided AlertID:** print "Microsoft Sentinel alert rule with ID "{0}" was not found!".format(AlertRuleID).  
**If error:** print "Failed to update Microsoft Sentinel alert rule! Error is {0}".format(exception.stacktrace). | General  
  
### Delete Alert Rule

Delete Azure Sentinel scheduled alert rule.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
AlertRuleID | String | N/A | Yes | Specify the ID of the alert rule to delete.  
  
#### Use cases

The action can be used to delete Microsoft Sentinel alert rule from the Google SecOps. If an alert rule is very outdated and it does not serve its purpose or if a rule creates only false positives, you can delete it with this action.

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output Message* | **If successful:** print "Successfully deleted Microsoft Sentinel alert rule {0}".format(AlertRuleID).  
**If can't find alert rule by the provided AlertID:** print "Microsoft Sentinel alert rule with ID "{0}" was not found!".format(AlertRuleID).  
**If error:** print "Failed to delete Microsoft Sentinel alert rule! Error is {0}".format(exception.stacktrace). | General  
  
### List Custom Hunting Rules

Get Azure Sentinel custom hunting rules list.

**Note:** Default Microsoft-provided hunting rules aren't displayed. To display a Microsoft rule, mark this rule as a favorite or clone the rule to a new custom rule.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Hunting Rule Names to Return | String | N/A | No | Specify names for the hunting rules action should return. The parameter accepts multiple values as a comma-separated string.If the value is not provided - return all possible alert types.  
Fetch Specific Hunting Rule Tactics | String | N/A | No | Specify what hunting rule tactics action should return. The parameter accepts multiple values as a comma-separated string. If the value is not provided - return all possible alert types.  
Max rules to return | Integer | N/A | No | How many scheduled alert rules the action should return, for example, 50.  
  
#### Use cases

The action can be used to list custom and favorite hunting rules of the Google SecOps playbook for Microsoft Sentinel. To ensure you have established all hunting rules for data concerning the rarest but very critical processes that operate on your network, you should mention custom and preferred hunting rules. You can immediately update and create existing hunting rules if you see that some situations are not handled correctly.

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "__metadata": {},
        "value": [
            {
                "id": "subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP/providers/Microsoft.OperationalInsights/workspaces/WORKSPACE/savedSearches/0c5bd7e1-0e13-4e7d-9e32-88baf9589192",
                "etag": "W/\"datetime'2019-12-02T10%3A14%3A10.5299491Z'\"",
                "properties": {
                    "Category": "Hunting Queries",
                    "DisplayName": "Hunting Query 1",
                    "Query": "\r\nlet timeframe = 7d;\r\nAWSCloudTrail\r\n| where TimeGenerated >= ago(timeframe)\r\n| where  EventName in~ (\"AttachGroupPolicy\", \"AttachRolePolicy\", \"AttachUserPolicy\", \"CreatePolicy\",\r\n\"DeleteGroupPolicy\", \"DeletePolicy\", \"DeleteRolePolicy\", \"DeleteUserPolicy\", \"DetachGroupPolicy\",\r\n\"PutUserPolicy\", \"PutGroupPolicy\", \"CreatePolicyVersion\", \"DeletePolicyVersion\", \"DetachRolePolicy\", \"CreatePolicy\")\r\n| project TimeGenerated, EventName, EventTypeName, UserIdentityAccountId, UserIdentityPrincipalid, UserAgent, \r\nUserIdentityUserName, SessionMfaAuthenticated, SourceIpAddress, AWSRegion, EventSource, AdditionalEventData, ResponseElements\r\n| extend timestamp = TimeGenerated, IPCustomEntity = SourceIpAddress, AccountCustomEntity = UserIdentityAccountId\r\n",
                    "Tags": [
                        {
                            "Name": "description",
                            "Value": "1234"
                        },
                        {
                            "Name": "tactics",
                            "Value": "DefenseEvasion"
                        },
                        {
                            "Name": "createdTimeUtc",
                            "Value": "12/02/2019 09:21:18"
                        }
                    ],
                    "Version": 2
                },
                "name": "0c5bd7e1-0e13-4e7d-9e32-88baf9589192"
            },
            {
                "id": "subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP/providers/Microsoft.OperationalInsights/workspaces/WORKSPACE/savedSearches/30a94796-a573-4e6e-9385-fb96d0aa5ea2",
                "etag": "W/\"datetime'2019-12-02T10%3A10%3A18.4761379Z'\"",
                "properties": {
                    "Category": "Hunting Queries",
                    "DisplayName": "Hunting Query 1",
                    "Query": "\r\nlet timeframe = 7d;\r\nAWSCloudTrail\r\n| where TimeGenerated >= ago(timeframe)\r\n| where  EventName in~ (\"AttachGroupPolicy\", \"AttachRolePolicy\", \"AttachUserPolicy\", \"CreatePolicy\",\r\n\"DeleteGroupPolicy\", \"DeletePolicy\", \"DeleteRolePolicy\", \"DeleteUserPolicy\", \"DetachGroupPolicy\",\r\n\"PutUserPolicy\", \"PutGroupPolicy\", \"CreatePolicyVersion\", \"DeletePolicyVersion\", \"DetachRolePolicy\", \"CreatePolicy\")\r\n| project TimeGenerated, EventName, EventTypeName, UserIdentityAccountId, UserIdentityPrincipalid, UserAgent, \r\nUserIdentityUserName, SessionMfaAuthenticated, SourceIpAddress, AWSRegion, EventSource, AdditionalEventData, ResponseElements\r\n| extend timestamp = TimeGenerated, IPCustomEntity = SourceIpAddress, AccountCustomEntity = UserIdentityAccountId\r\n",
                    "Tags": [
                        {
                            "Name": "description",
                            "Value": "1234"
                        },
                        {
                            "Name": "tactics",
                            "Value": "DefenseEvasion"
                        },
                        {
                            "Name": "createdTimeUtc",
                            "Value": "12/02/2019 09:21:18"
                        }
                    ],
                    "Version": 2
                },
                "name": "30a94796-a573-4e6e-9385-fb96d0aa5ea2"
            }
        ]
    }
    

##### Case wall

Result type | Value/Description | Type  
---|---|---  
Output Message* | **If successful:** print "Successfully returned Microsoft Sentinel hunting rules".   
**If error:** print "Failed to list Microsoft Sentinel hunting rules! Error is {0}".format(exception.stacktrace).  | General  
Table | **Table title:** Microsoft Sentinel hunting rules found: **Columns:** HuntingRuleID(mapped to name), title (mapped to displayName), category, description (mapped to description parameter in tags dict), tactics(mapped to tactics parameter in tags dict), query, creation time (mapped to CreatedTimeUtc parameter in tags dict) | General  
Attachments | List_HuntingRules.json - contains returned by the action technical JSON data.  | General  
JSON Viewer  
(Only if the table is not optional) | Show the JSON viewer for the query result. | General  
  
### Get Custom Hunting Rule Details

Get details of the Azure Sentinel custom hunting rule.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
HuntingRuleID | String | N/A | Yes | Specify the ID of the hunting rule.  
  
#### Use cases

Information on Microsoft Sentinel standard or preferred hunting rules can be accessed using the Google SecOps playbook. Use this tool, for example, if you see details you receive from hunting rules which are not appropriate for analysis, or you want to see if your hunting rule is correctly configured. You will evaluate whether to edit, remove, or leave it unchanged based on the results.

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
       "id": "subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP/providers/Microsoft.OperationalInsights/workspaces/WORKSPACE/savedSearches/30a94796-a573-4e6e-9385-fb96d0aa5ea2",
        "etag": "W/\"datetime'2019-12-02T10%3A14%3A10.5299491Z'\"",
        "properties": {
            "Category": "Log Management",
            "DisplayName": "Multiple Password Reset by user",
            "Query": "\nlet timeframe = 7d;\nAWSCloudTrail\n| where TimeGenerated >= ago(timeframe)\n| where  EventName in~ (\"AttachGroupPolicy\", \"AttachRolePolicy\", \"AttachUserPolicy\", \"CreatePolicy\",\n\"DeleteGroupPolicy\", \"DeletePolicy\", \"DeleteRolePolicy\", \"DeleteUserPolicy\", \"DetachGroupPolicy\",\n\"PutUserPolicy\", \"PutGroupPolicy\", \"CreatePolicyVersion\", \"DeletePolicyVersion\", \"DetachRolePolicy\", \"CreatePolicy\")\n| project TimeGenerated, EventName, EventTypeName, UserIdentityAccountId, UserIdentityPrincipalid, UserAgent, \nUserIdentityUserName, SessionMfaAuthenticated, SourceIpAddress, AWSRegion, EventSource, AdditionalEventData, ResponseElements\n| extend timestamp = TimeGenerated, IPCustomEntity = SourceIpAddress, AccountCustomEntity = UserIdentityAccountId\n",
            "Tags": [
                {
                    "Name": "description",
                    "Value": "Identity and Access Management (IAM) securely manages access to AWS services and resources."
                },
                {
                    "Name": "tactics",
                    "Value": "DefenseEvasion"
                },
                {
                    "Name": "createdTimeUtc",
                    "Value": "12/02/2019 09:21:18"
                }
            ],
            "Version": 2
        }
    }
    

##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output Message* | **If successful:** print "Successfully returned Microsoft Sentinel hunting rule {0} details".format(HuntingRuleID).  
**If can't find alert rule by the provided AlertID:** print "Microsoft Sentinel hunting rule with ID "{0}" was not found!".format(HuntingRuleID).  
**If error:** print "Failed to get details about Microsoft Sentinel hunting rule! Error is {0}".format(exception.stacktrace). | General  
Table | **Table title:** Microsoft Sentinel Hunting Rule Details: **Columns:** HuntingRuleID (mapped to name), Name (mapped to displayName), Description, Query, Tactic,Creation TIme | General  
Attachments | List_HuntingRules.json - contains returned by the action technical JSON data.  | General  
JSON Viewer  
(Only if the table is not optional) | Show the JSON viewer for the query result. | General  
  
### Create Custom Hunting Rule

Create Azure Sentinel custom hunting rule.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Query | String | N/A | Yes | Specify query to execute in this hunting rule.  
Display Name | String | N/A | Yes | Specify display name for hunting rule.  
Description | String | N/A | No | Specify description for the hunting rule.  
Tactics | String | N/A | No | Specify tactics for this hunting rule. The parameter accepts multiple comma-separated values.  
  
#### Use cases

The action can be used to create a new Microsoft Sentinel hunting rule from the Google SecOps playbook. For example, hunting rules contain a query, which can provide data about the most uncommon processes running on your infrastructure - you wouldn't want an alert about each time they are run, they could be entirely innocent, but you might want to take a look at the query on occasion to see if there's anything unusual. This means they can be used to gather more information from your network environment.

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output Message* | **If successful:** print "Successfully created Microsoft Sentinel hunting rule".  
**If error:** print "Failed to create Microsoft Sentinel hunting rule! Error is {0}".format(exception.stacktrace).  | General  
  
### Update Custom Hunting Rule

Update Azure Sentinel custom hunting rule.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
HuntingRuleID | String | N/A | Yes | Specify the ID of the hunting rule.  
Display Name | String | N/A | No | Specify display name for hunting rule.  
Query | String | N/A | No | Specify query to execute in this hunting rule.  
Description | String | N/A | No | Specify description.  
Tactics | String | N/A | No | Specify tactics for this hunting rule.The parameter can take multiple comma-separated values.  
  
  
#### Use cases

The action can be used to update a custom Microsoft Sentinel hunting rule from the Google SecOps playbook. Use this action if you think, for example, that a hunting rule is very outdated and you want to update several parameters like a query or description. Information is key when doing the investigation of incidents, so every hunting rule should be updated to show relevant information.

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output Message* | **If successful:** print "Successfully updated Microsoft Sentinel hunting rule with ID {0}".format(HuntingRuleID).  
**If can't find hunting rule by the provided HuntingRuleID:** print "Microsoft Sentinel hunting rule with ID "{0}" was not found!".format(HuntingRuleID).  
**If error:** print "Failed to update Microsoft Sentinel hunting rule! Error is {0}".format(exception.stacktrace). | General  
  
### Delete Custom Hunting Rule

Delete Azure Sentinel custom hunting rule.

**Warning:** Predefined Microsoft Azure hunting rules cannot be deleted, even if they were set to favorites.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
HuntingRuleID | String | N/A | Yes | Specify the ID of the hunting rule to delete.  
  
#### Use cases

The action can be used to delete a custom Microsoft Sentinel hunting rule from Google SecOps. If you think, for example, that a hunting rule is very outdated and it is not needed for the investigation process, then it's best to delete it.

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output Message* | **If successful:** print "Successfully deleted Microsoft Sentinel hunting rule with ID {0}".format(HuntingRuleID).  
**If can't find hunting rule by the provided HuntingRuleID:** print "Microsoft Sentinel hunting rule with ID "{0}" was not found!".format(HuntingRuleID).  
**If error:** print "Failed to delete Microsoft Sentinel hunting rule! Error is {0}".format(exception.stacktrace). | General  
  
### Run a Custom Hunting Rule

Execute a custom or favorite Microsoft Sentinel hunting rule.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
HuntingRuleID | String | N/A | Yes | Specify the ID of the hunting rule.  
Timeout | Integer | N/A | No | The parameter that is used to specify a timeout value for the Azure Sentinel hunting rule API call.  
  
#### Use cases

The action can be used to run a Microsoft Sentinel hunting rules from the Google SecOps playbook. Running a hunting rule query provides data about the most uncommon processes running on your infrastructure - you wouldn't want an alert about each time they are run, they could be entirely innocent, but you might want to take a look at the query on occasion to see if there's anything unusual. This means, it can be used to gather more information from your network environment, which will help investigators to figure out all nuances regarding an incident and help make further decisions.

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "tables": [
            {
                "name": "PrimaryResult",
                "columns": [
                    {
                        "name": "timerange",
                        "type": "datetime"
                    },
                    {
                        "name": "AppDisplayName",
                        "type": "string"
                    },
                    {
                        "name": "UserPrincipalName",
                        "type": "string"
                    },
                    {
                        "name": "threeDayWindowLocationCount",
                        "type": "long"
                    },
                    {
                        "name": "locationList",
                        "type": "dynamic"
                    },
                    {
                        "name": "timestamp",
                        "type": "datetime"
                    },
                    {
                        "name": "AccountCustomEntity",
                        "type": "string"
                    }
                ],
                "rows": [
                    [
                        "2019-11-29T00:00:00Z",
                        "WindowsDefenderATP Portal",
                        "user@example.com",
                        2,
                        "[\"US/Florida/Miami;\",\"AM/Kotayk'/Abovyan;\"]",
                        "2019-11-29T00:00:00Z",
                        "user@example.com"
                    ],
                    [
                        "2019-12-02T00:00:00Z",
                        "WindowsDefenderATP Portal",
                        "user@example.com",
                        1,
                        "[\"US/Florida/Miami;\"]",
                        "2019-12-02T00:00:00Z",
                        "user@example.com"
                    ],
                    [
                        "2019-11-29T00:00:00Z",
                        "Azure Portal",
                        "example@example.com",
                        1,
                        "[\"UA/Kyiv Misto/Kyiv;\"]",
                        "2019-11-29T00:00:00Z",
                        "example@example.com"
                    ],
                    [
                        "2019-12-02T00:00:00Z",
                        "Azure Portal",
                        "example@example.com",
                        2,
                        "[\"UA/Kyiv Misto/Kyiv;\",\"UA/Kyivs'ka Oblast'/Boryspil';\"]",
                        "2019-12-02T00:00:00Z",
                        "example@example.com"
                    ],
                    [
                        "2019-11-29T00:00:00Z",
                        "Azure Portal",
                        "user@example.com",
                        1,
                        "[\"RU/Sverdlovskaya Oblast'/Yekaterinburg;\"]",
                        "2019-11-29T00:00:00Z",
                        "user@example.com"
                    ],
                    [
                        "2019-12-02T00:00:00Z",
                        "Azure Portal",
                        "user@example.com",
                        1,
                        "[\"RU/Sverdlovskaya Oblast'/Yekaterinburg;\"]",
                        "2019-12-02T00:00:00Z",
                        "user@example.com"
                    ]
                ]
            }
        ]
    }
    

##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output Message* | **If successful:** print "Hunting rule executed successfully".  
If can't find hunting rule by the provided HuntingRuleID: print "Microsoft Sentinel hunting rule with ID "{0}" was not found!".format(HuntingRuleID)  
**if nothing found:** print "Hunting rule executed successfully, but did not return any results."  
**if error:** print "Hunting rule didn't completed due to error: {0}".format(exception.stacktrace)  
**If timeout:** print "Hunting rule didn't completed due to timeout: {0}".format(exception.stacktrace)   
**If query results were truncated:** print "Hunting rule results exceeded limits and were truncated, please rewrite your query!" | General  
Table | **Table title:** Microsoft Sentinel hunting rule results Columns: dynamically generate columns based on the query result | General  
Attachments | Run_Hunting_rule_{HuntingRuleID}_response.json - contains returned by the action technical JSON data. | General  
JSON Viewer  
(Only if the table is not optional) | Show the JSON viewer for the query result. | General  
  
### Run a KQL Query

Run Azure Sentinel KQL query based on the provided action input parameters.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
KQL Query | String | N/A | Yes | A KQL Query to execute in Azure Sentinel. For example, to get security alerts available in Sentinel, query will be \"SecurityAlert\". Use other action input parameters (time span, limit) to filter the query results. For the examples of KQL queries consider Sentinel \"Logs\" Web page".  
Time Span | String | N/A | No | Specify THE time span to look for. The time value should be ISO 8601 compliant, and for example, can be used to specify to search for the last 10 hours or time interval to search for. Use the following format: PT + number + (M, H, D),where M - minutes, H - hours, D - days.  
Query Timeout | Integer | 180 | No | Timeout value for the Azure Sentinel hunting rule API call. Note that Google SecOps action python process timeout should be adjusted accordingly for this parameter, to not timeout action sooner than specified value because of the python process timeout.  
Record Limit | Integer | 100 | No | How many records should be fetched. Optional parameter, if set, adds a \"| limit x\" to the kql query where x is the value set for the record limit. Can be removed if \"limit\" is already set in kql query or not needed.  
  
#### Use cases

Running advances queries during the investigation on the Case.

#### Run on

This action runs on all entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "tables": [
            {
                "name": "PrimaryResult",
                "columns": [
                    {
                        "name": "Reason",
                        "type": "string"
                    },
                    {
                        "name": "StartTimeUtc",
                        "type": "datetime"
                    },
                    {
                        "name": "EndTimeUtc",
                        "type": "datetime"
                    },
                    {
                        "name": "count_",
                        "type": "long"
                    },
                    {
                        "name": "timestamp",
                        "type": "datetime"
                    }
                ],
                "rows": [
                    [
                        "Incorrect password",
                        "2019-10-22T06:38:30.837Z",
                        "2019-10-22T11:57:00.003Z",
                        28,
                        "2019-10-22T06:38:30.837Z"
                    ],
                    [
                        "Account name does not exist",
                        "2019-10-21T15:19:33.727Z",
                        "2019-10-22T06:40:13.51Z",
                        3,
                        "2019-10-21T15:19:33.727Z"
                    ]
                ]
            }
        ]
    }
    

##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output Message* | **If successful:** print "Query executed successfully".  
**If nothing found:** print "Query executed successfully, but did not return any results.".  
**If error:** print "Query didn't completed due to error: {0}".format(exception.stacktrace).  
**If timeout:** print "Query didn't completed due to timeout: {0}".format(exception.stacktrace).  
**If query results were truncated:** print "Query results exceeded limits and were truncated, please rewrite your query!". |   
Table | **Table title:** KQL Query results**Columns:** dynamically generate columns based on the query result | General  
Attachments | Run_KQL_query_response.json - contains returned by the action technical JSON data. | General  
JSON Viewer  
(Only if the table is not optional) | Show the JSON viewer for the query result. | General  
  
### Add Comment to Incident

Add a comment to Azure Sentinel incident.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Incident Number | Integer | N/A | Yes | Specify Incident number to add comment to.  
Comment to Add | String | N/A | Yes | Specify comment to add to Incident  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "id": "/subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP/providers/Microsoft.OperationalInsights/workspaces/WORKSPACE/providers/Microsoft.SecurityInsights/Incidents/00cfebdc-c677-463f-8355-cb7f23472c06/Comments/f0f31d1a-d32b-4774-a21d-3279240c7c33",
        "name": "f0f31d1a-d32b-4774-a21d-3279240c7c33",
        "etag": "\"7e000812-0000-0c00-0000-606fc83f0000\"",
        "type": "Microsoft.SecurityInsights/Incidents/Comments",
        "properties": {
            "message": "Some message",
            "createdTimeUtc": "2021-04-09T03:21:35.0894288Z",
            "lastModifiedTimeUtc": "2021-04-09T03:21:35.0894288Z",
            "author": {
                "objectId": "f6ce2f43-6f77-4b30-9a4a-de1a069b2560",
                "email": null,
                "name": "Comment created from external application - log_analytics_rest_api_for_sentinel",
                "userPrincipalName": null
            }
        }
    }
    

##### Case wall

Result Type | Value / Description | Type  
---|---|---  
Output Message* | **The action should not fail nor stop a playbook execution:**

  * **if successful:** "Successfully added a comment to Microsoft Sentinel incident {0}".format(Incident number).

****

  * **If can't find incident by the provided incident case number:** "Microsoft Sentinel incident {0} was not found!". format(incident_case_number).

******The action should fail and stop a playbook execution:**

  * **if fatal error, like wrong credentials:** "Failed to add a comment to Microsoft Sentinel incident! Error is {0}".format(exception.stacktrace).

| General  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### Microsoft Azure Sentinel Incidents Connector – Deprecated

**Deprecated:** This connector is deprecated. For the integration to function properly, use the Microsoft Azure Sentinel Incident Connector v2.

In Google SecOps SOAR, Microsoft Azure Sentinel Incidents Connector ingests incidents from the specific Microsoft Sentinel workspace as alerts using the Azure Security Insights API.

The connector uses capabilities similar to the **List Incidents** and **Get Incident Details** actions, and connects to the Azure Security Insights endpoint to pull a list of incidents generated during a specified period.

#### Connector use case

Use the connector to monitor Microsoft Sentinel workspaces for new incidents and ingest them into the Google SecOps SOAR server.

To ensure the flow of specific event types, add the data connector to Microsoft Sentinel. For example, to add security events from Windows hosts as one of the data connectors, install a Microsoft Sentinel agent on a Windows host, and configure what types of events to ingest: security events, firewall events, DNS events, or other.

To generate alerts based on specific conditions, define alert rules using rule queries. When alert rules create warnings, it triggers Microsoft Sentinel to generate events, store data accidents, and display incidents on the portal incidents page.

To read and write incident data programmatically, use the Security Insights REST API.

#### Connector parameters

To configure the connector, use the following parameters:

Parameters  
---  
`Product Field Name` | _Required_ Name of the field where the product name is stored. Default value is `ProductName`.  
`Event Field Name` | _Required_ Name of the field where the event name is stored. Default value is `AlertName`.  
`Environment Field Name` | _Optional_ Name of the field where the environment name is stored. If the environment field isn't found, the default environment is used. Default value is `""`.  
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. The default value `.*` catches all and returns the value unchanged.The parameter lets you manipulate the environment field using the regular expression logic.If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Azure Subscription ID` | _Required_ Azure subscription ID.  
`Azure Active Directory ID` | _Required_ Microsoft Entra tenant ID.  
`Api Root` | _Required_ The management.azure.com API root URL to use with the integration. Default value is `https://management.azure.com`.  
`Azure Resource Group` | _Required_ Name of the Azure resource group where Microsoft Sentinel is located.  
`Azure Sentinel Workspace Name` | _Required_ Name of the Microsoft Sentinel workspace to work with.  
`Client ID` | _Required_ Microsoft Entra application (client) ID used for this integration.  
`Client Secret` | _Required_ Microsoft Entra client secret value.  
`Script Timeout (Seconds)` | _Required_ Timeout limit for the python process running the current script. Default value is 180 seconds.  
`Offset Time In Hours` | _Required_ Number of hours before now to retrieve incidents from. Default value is 24 hours.  
`Incident Statuses to Fetch` | _Required_ Statuses of the incidents to fetch. This parameter accepts multiple values as a comma-separated string. Default value is `Active, New, Closed`.  
`Incident Severities to Fetch` | _Required_ Severities of the incidents to fetch. This parameter accepts multiple values as a comma-separated string. Default value is `Informational, Low, Medium, High`.  
`Max Incidents per Cycle` | _Required_ Number of incidents to process during one connector run. This parameter accepts multiple values as a comma-separated string. Default value is 10.  
`Proxy Server Address` | _Optional_ Address of the proxy server to use.  
`Proxy Server Username` | _Optional_ Proxy username to authenticate with.  
`Proxy Server Password` | _Optional_ Proxy password to authenticate with.  
  
#### Connector rules

  * The connector doesn't support blocklists and dynamic lists.

  * The connector supports proxies.




### Microsoft Azure Sentinel Incident Connector v2

**Important:** This connector will be fully deprecated on March 30, 2027. Until then, support is limited to critical bug fixes for ingestion issues; no new feature updates will be provided. Use the [Microsoft 365 Defender – Incidents Connector](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-365-defender#microsoft_365_defender_incidents_connector) instead. Note that migrating may require changes to your playbooks.

**Microsoft Azure Sentinel Incidents Connector v2** is a recommended connector to use when working with Microsoft Sentinel. Major changes include moving to the new incident endpoints in the Microsoft Sentinel API and introducing the connector entities handling and parsing logic. To filter specific Microsoft Sentinel incidents and fetch them based on incident names, use the dynamic list.

It is possible that the Microsoft Sentinel UI displays the incident entities but the API doesn't return them (the entity list is empty). As a result, the connector requires more time to ingest such incidents and queries them in the backlog for the following connector runs. Once the entities information is available in the API response, the connector ingests the incidents.

#### Processing of Scheduled and Non-Scheduled Sentinel Alerts

To resolve an issue in the **Microsoft Azure Sentinel Incidents Connector** when it erroneously displayed entities for all alerts other than the Azure Sentinel scheduled alerts, the **Microsoft Azure Sentinel Incidents Connector v2** adds an additional event for every entity.

This means that if the connector receives an **IP** , **Account** , or **Hostname** entity in the Google SecOps event, it adds an additional Google SecOps event for every found entity. The newly created event can be used to create entities and map entity properties in Google SecOps SOAR. The initial events remain intact. New events are only added to the Google SecOps alert. Other entity types are not affected by this logic and remain in the initial event with no additional events created for them.

To enable creating additional events, the connector uses the `entity` Sentinel API endpoint to fetch the data. Both scheduled and NRT alerts are by default ingested using the log analytics KQL queries to get alert and event data. If selected, the **Use the same approach with event creation for all alert types?** parameter in the connector configuration uses the same entity-based approach to all alerts, including scheduled and non-scheduled. We recommend to use this option with caution.

#### Connector parameters

To configure the connector, use the following parameters:

Parameters  
---  
`Product Field Name` | _Required_ Name of the field where the product name is stored. Default value is `product_type`.  
`Event Field Name` | _Required_ Name of the field where the event name is stored. Default value is `event_type`.  
`Environment Field Name` | _Optional_ Name of the field where the environment name is stored. If the environment field isn't found, the default environment is used. Default value is `""`.  
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. The default value `.*` catches all and returns the value unchanged.The parameter lets you manipulate the environment field using the regular expression logic.If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Azure Subscription ID` | _Required_ Azure subscription ID.  
`Azure Active Directory ID` | _Required_ Microsoft Entra tenant ID.  
`Api Root` | _Required_ The API root URL to use with the integration. Default value is `https://management.azure.com`.  
`OAUTH2 Login Endpoint Url` | _Required_ Endpoint URL to use for the OAuth 2.0 authentication.  
`Azure Resource Group` | _Required_ Name of the Azure resource group where Microsoft Sentinel is located.  
`Azure Sentinel Workspace Name` | _Required_ Name of the Microsoft Sentinel workspace to work with.  
`Client ID` | _Required_ Microsoft Entra application (client) ID used for this integration.  
`Client Secret` | _Required_ Microsoft Entra client secret value.  
`Script Timeout (Seconds)` | _Required_ Timeout limit for the python process running the current script. Default value is 180 seconds.  
`Offset Time In Hours` | _Required_ Number of hours before now to retrieve incidents from. Default value is 24 hours.  
`Incident Statuses to Fetch` | _Required_ Statuses of the incidents to fetch. This parameter accepts multiple values as a comma-separated string. Default value is `Active, New, Closed`.  
`Incident Severities to Fetch` | _Required_ Severities of the incidents to fetch. This parameter accepts multiple values as a comma-separated string. Default value is `Informational, Low, Medium, High`.  
`Use the same approach with event creation for all alert types? ` | _Optional_ When checked, the connector uses the same approach for all alert types. When unchecked, the connector uses a different approach for the Azure Sentinel scheduled alert type and tries to fetch events that caused the alert by running the query specified in alert details. Unchecked by default.  
`Use whitelist as a blacklist` | _Required_ If checked, the dynamic list is used as a blocklist.Unchecked by default.  
`Proxy Server Address` | _Optional_ Address of the proxy server to use.  
`Proxy Server Username` | _Optional_ Proxy username to authenticate with.  
`Proxy Server Password` | _Optional_ Proxy password to authenticate with.  
`Max Backlog Incidents per Cycle` | _Required_ Number of incidents to fetch from the backlog during one connector run.  Default value is 10.  
`StartTimeFallback` | _Required_ Comma-separated list of incident or alert attributes to use as a fallback for the `Start Time` alert field in descending order. Additionally, a new `Siemplify_Start_Time` attribute is added to created events. First attribute has the highest priority. The next attribute, if not present or empty in the event, falls back to the next priority value from the list. If none of the fallback fields are found, the connector uses the `createdTimeUTC` attribute. If there is no `createdTimeUTC` attribute, the connector uses the time that the alert was ingested into Google SecOps SOAR. Default value is `properties_firstActivityTimeGenerated, properties_startTimeUtc,properties_createdTimeUtc, properties_firstAlertTimeGenerated`.  
`EndTimeFallback` | _Required_ Comma-separated list of incident or alert attributes to use as a fallback for the `End Time` alert field in descending order. Additionally, a new `Siemplify_End_Time` attribute is added to created events. First attribute has the highest priority. The next attribute, if not present or empty in the event, falls back to the next priority value from the list. If none of the fallback fields are found, the connector uses the `createdTimeUTC` attribute. If there is no `createdTimeUTC` attribute, the connector uses the time that the alert was ingested into Google SecOps SOAR. Default value is `properties_lastActivityTimeGenerated, properties_endTimeUtc,properties_createdTimeUtc, properties_lastAlertTimeGenerated`.  
`Enable Fallback Logic Debug?` | _Optional_ If checked, the connector adds debug fields containing the values used for fallback to the created events.Unchecked by default.  
`VendorFieldFallback` | _Required_ Comma-separated list of incident attributes to use as a fallback for the `DeviceVendor` field in descending order. First attribute has the highest priority. The next attribute, if not present or empty in the event, falls back to the next priority value from the list. Default value is `vendorName`.  
`ProductFieldFallback` | _Required_ Comma-separated list of incident attributes to use as a fallback for the `DeviceVendor` field in descending order. First attribute has the highest priority. The next attribute, if not present or empty in the event, falls back to the next priority value from the list. Default value is `ProductName`.  
`EventFieldFallback` | _Required_ Comma-separated list of incident attributes to use as a fallback for the `Event Field Name` parameter in descending order. First attribute has the highest priority. The next attribute, if not present or empty in the event, falls back to the next priority value from the list. Default value is `kind`.  
`Max New Incidents per cycle` | _Required_ Number of incidents to process in one connector run.Default value is 10.  
`Wait For Scheduled/NRT Alert Object` | _Optional_ If enabled, the connector waits until a Scheduled/NRT alert object is available.  
`Scheduled Alerts Events Limit to Ingest` | _Optional_ Maximum number of events to ingest for a single Azure Sentinel scheduled alert or NRT alert.Default value is 100.  
`Incidents Padding Period (minutes)` | _Optional_ Time period in minutes for the connector to fetch incidents and return them. These incidents are not in chronological order.  
`Create Siemplify Alerts for Sentinel incidents that do not have entities?` | _Optional_ If checked, the connector creates Google SecOps alerts from Microsoft Sentinel incidents that don't have entities. Otherwise, the connector creates Google SecOps alerts only for scheduled and NRT alerts and skips all other Microsoft Sentinel incident types. Unchecked by default.  
`Incident's Alerts Limit to Ingest` | _Optional_ Maximum number of alerts to ingest for every Microsoft Sentinel incident.   
`Alert Name Template` | _Optional_ If specified, the connector uses this value from the incident data returned in the Microsoft Sentinel API response to populate the `Siemplify Alert Name` field. You can provide a placeholder in the following format: `[name of the field]`, for example, `Sentinel incident - [title]`.The maximum length for the field is 256 characters.If no value is provided or you provide an invalid template, the connector uses the default alert name.  
`Rule Generator Template` | _Optional_ If specified, the connector uses this value from the incident data returned in the Microsoft Sentinel API response to populate the `Siemplify Rule Generator` field. You can provide a placeholder in the following format: `[name of the field]`, for example, `Sentinel incident - [severity]`.The maximum length for the field is 256 characters.If no value is provided or you provide an invalid template, the connector uses the default rule generator value.  
  
#### Customize the Alert Name and Rule Generator fields

The connector lets you customize the **Siemplify Alert Name** and **Rule Generator** field values using the **Alert Name Template** and **Rule Generator Template** parameters. For templates, the connector gets information from the Microsoft Sentinel incidents data returned by the API. 

The following example displays the incident data as it is returned from the API to reference the fields that are available in the alert and can be used for templates:
    
    
    {
                "id": "/subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP/providers/Microsoft.OperationalInsights/workspaces/WORKSPACE/providers/Microsoft.SecurityInsights/Incidents/d4f632be-0689-93f7-57a6-f27bfabbbad1",
                "name": "d4f632be-0689-93f7-57a6-f27bfabbbad1",
                "etag": "\"79004534-0000-0d00-0000-63590d610000\"",
                "type": "Microsoft.SecurityInsights/Incidents",
                "properties": {
                    "title": "Incident title",
                    "description": "",
                    "severity": "Low",
                    "status": "New",
                    "owner": {
                        "objectId": null,
                        "email": null,
                        "assignedTo": null,
                        "userPrincipalName": null
                    },
                    "labels": [],
                    "firstActivityTimeUtc": "2022-10-26T07:00:09.3857965Z",
                    "lastActivityTimeUtc": "2022-10-26T09:07:02.1083312Z",
                    "lastModifiedTimeUtc": "2022-10-26T10:35:13.0254798Z",
                    "createdTimeUtc": "2022-10-26T10:34:55.7454638Z",
                    "incidentNumber": 380925,
                    "additionalData": {
                        "alertsCount": 102,
                        "bookmarksCount": 0,
                        "commentsCount": 0,
                        "alertProductNames": [
                            "Azure Sentinel"
                        ],
                        "tactics": [
                            "InitialAccess",
                            "Persistence"
                        ]
                    },
                    "relatedAnalyticRuleIds": [
                        "/subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP/providers/Microsoft.OperationalInsights/workspaces/WORKSPACE/Microsoft.SecurityInsights/alertRules/8a3ca5c5-7875-466e-accd-3bcb2881cdb0"
                    ],
                    "incidentUrl": "https://portal.azure.com/#asset/Microsoft_Azure_Security_Insights/Incident/subscriptions/SUBSCRIPTION_ID/resourceGroups/RESOURCE_GROUP/providers/Microsoft.OperationalInsights/workspaces/WORKSPACE/Microsoft.SecurityInsights/Incidents/d4f632be-0689-93f7-57a6-f27bfabbbad1",
                    "providerName": "Azure Sentinel",
                    "providerIncidentId": "380925"
                }
            }
    

#### Connector rules

  * The connector supports the blocklist and the dynamic list.

  * The connector supports proxies.




### Microsoft Sentinel Incident Tracking Connector

**Important:** This connector will be fully deprecated on March 30, 2027. Until then, support is limited to critical bug fixes for ingestion issues; no new feature updates will be provided. Use the [Microsoft 365 Defender – Incidents Connector](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-365-defender#microsoft_365_defender_incidents_connector) instead. Note that migrating may require changes to your playbooks.

Use the **Microsoft Sentinel Incident Tracking Connector** to work with Microsoft Sentinel incidents and retrieve updates to the Sentinel incidents as new Google SecOps alerts. You can use the dynamic list to specify the incident names to retrieve. For this connector, we recommend you configure the Google SecOps alerts grouping based on the `SourceGroupIdentifier` parameter.

#### Connector inputs

To configure the connector, use the following parameters:

Parameters  
---  
`Product Field Name` | _Required_ Name of the field where the product name is stored. Default value is `product_type`.  
`Event Field Name` | _Required_ Name of the field where the event name is stored. Default value is `event_type`.  
`Environment Field Name` | _Optional_ Name of the field where the environment name is stored. If the environment field isn't found, the default environment is used. Default value is `""`.  
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. The default value `.*` catches all and returns the value unchanged.The parameter lets you manipulate the environment field using the regular expression logic.If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
`Azure Subscription ID` | _Required_ Azure subscription ID.  
`Entra ID Directory ID` | _Required_ Microsoft Entra tenant ID.  
`Api Root` | _Required_ The API root URL to use with the integration. Default value is `https://management.azure.com`.  
`OAUTH2 Login Endpoint Url` | _Required_ Endpoint URL to use for OAuth 2.0 authentication.  
`Azure Resource Group` | _Required_ Name of the Azure resource group where Microsoft Sentinel is located.  
`Azure Sentinel Workspace Name` | _Required_ Name of the Microsoft Sentinel workspace to work with.  
`Client ID` | _Required_ Microsoft Entra application (client) ID used for this integration.  
`Client Secret` | _Required_ Microsoft Entra client secret value.  
`Script Timeout (Seconds)` | _Required_ Timeout limit for the Python process running the current script. Default value is 480 seconds.  
`Verify SSL` | _Optional_ If selected, the integration verifies that the SSL certificate for the connection to the Microsoft server is valid. Selected by default.  
`Max Hours Backwards` | _Required_ The number of hours before the first connector iteration to retrieve the incidents from. This parameter applies only once to the initial connector iteration after you enable the connector for the first time. The default value is 24 hours.  
`Incident Statuses to Fetch` | _Required_ Statuses of the incidents to fetch. This parameter accepts multiple values as a comma-separated string. Default value is `Active, New, Closed`.  
`Incident Severities to Fetch` | _Required_ Severities of the incidents to fetch. This parameter accepts multiple values as a comma-separated string. Default value is `Informational, Low, Medium, High`.  
`Max Incidents per Cycle` | _Required_ The number of incidents to fetch from the backlog during one connector run. The default value is 10.  
`Use the same approach with event creation for all alert types? ` | _Optional_ If selected, the connector uses the same approach for all alert types.If not selected, the connector uses a different approach for the Microsoft Sentinel scheduled alert type and attempts to fetch events that caused the alert by running the query specified in the alert details.Not selected by default.  
`Incidents Tags To Ingest` | _Optional_ A comma-separated list of incident tags to ingest. The connector ignores incidents that don't possess the tags from this list.  
`Use whitelist as a blacklist` | _Required_ If selected, the dynamic list is used as a blocklist.Not selected by default.  
`Backlog Expiration Timer` | _Required_ A period in minutes for the connector to keep the incidents in a backlog. The default value is 60 minutes.  
`StartTimeFallback` | _Required_ A comma-separated list of incident or alert attributes to use as a fallback for the `Start Time` alert field in descending order. Additionally, a new `SecOps_Start_Time` attribute applies to created events. The first attribute has the highest priority. The following attribute, if not present or empty in the event, falls back to the next priority value from the list. If none of the fallback fields are found, the connector uses the `createdTimeUTC` attribute. If there is no `createdTimeUTC` attribute, the connector uses the time that the alert was ingested into Google SecOps SOAR. The default value is `properties_firstActivityTimeGenerated, properties_startTimeUtc,properties_createdTimeUtc, properties_firstAlertTimeGenerated`.  
`EndTimeFallback` | _Required_ A comma-separated list of incident or alert attributes to use as a fallback for the `End Time` alert field in descending order. Additionally, a new `SecOps_End_Time` attribute is added to created events. The first attribute has the highest priority. The next attribute, if not present or empty in the event, falls back to the next priority value from the list. If none of the fallback fields are found, the connector uses the `createdTimeUTC` attribute. If there is no `createdTimeUTC` attribute, the connector uses the time that the alert was ingested into Google SecOps SOAR. The default value is `properties_lastActivityTimeGenerated, properties_endTimeUtc,properties_createdTimeUtc, properties_lastAlertTimeGenerated`.  
`Enable Fallback Logic Debug?` | _Optional_ If selected, the connector adds debug fields containing the values used for fallback to the created events.Not selected by default.  
`VendorFieldFallback` | _Required_ A comma-separated list of incident attributes to use as a fallback for the `DeviceVendor` field in a descending order. The first attribute has the highest priority. The following attribute, if not present or empty in the event, falls back to the next priority value from the list.  The default value is `vendorName`.  
`ProductFieldFallback` | _Required_ A comma-separated list of incident attributes to use as a fallback for the `DeviceVendor` field in descending order. The first attribute has the highest priority. The following attribute, if not present or empty in the event, falls back to the next priority value from the list. The default value is `ProductName`.  
`EventFieldFallback` | _Required_ A comma-separated list of incident attributes to use as a fallback for the `Event Field Name` parameter in a descending order. The first attribute has the highest priority. The next attribute, if not present or empty in the event, falls back to the next priority value from the list. The default value is `kind`.  
`Max Backlog Incidents per cycle` | _Required_ The number of incidents to retrieve from the backlog in a one connector run.The default value is 10.  
`Disable Overflow` | _Optional_ if selected, the connector disables an event overflow. Not selected by default.  
`Total Number of Scheduled Alerts Events Limit to Ingest` | _Optional_ The maximum number of events to ingest for a single Microsoft Sentinel scheduled alert or an NRT alert.The default value is 100.  
`Create Chronicle SOAR Alerts for Sentinel incidents that do not have entities?` | _Optional_ If selected, the connector creates Google SecOps alerts from Microsoft Sentinel incidents that don't have entities. Otherwise, the connector creates Google SecOps alerts only for scheduled and NRT alerts and skips all other Microsoft Sentinel incident types. Not selected by default.  
`Incident's Alerts Limit to Ingest` | _Optional_ The maximum number of alerts to ingest for every Microsoft Sentinel incident.  
`Incidents Padding Period (minutes)` | _Optional_ Period in minutes before now for the connector to fetch incidents and return them. The connector doesn't return incidents in a chronological order.  
`Alert Name Template` | _Optional_ If specified, the connector uses this value from the incident data returned in the Microsoft Sentinel API response to for a Google SecOps SOAR alert name. You can provide a placeholder in the following format: `[name of the field]`, for example, `Sentinel incident - [title]`.The maximum length for the field is 256 characters.If no value is provided or you provide an invalid template, the connector uses the default alert name.  
`Rule Generator Template` | _Optional_ If specified, the connector uses this value from the incident data returned in the Microsoft Sentinel API response for a Google SecOps SOAR rule generator. You can provide a placeholder in the following format: `[name of the field]`, for example, `Sentinel incident - [severity]`.The maximum length for the field is 256 characters.If no value is provided or you provide an invalid template, the connector uses the default rule generator value.  
`How many hours to track ingested incident for updates` | _Required_ A period for the connector to track the already ingested Sentinel incidents for updates like the addition of new events or entities or incident details.The default value is 24 hours.  
`Wait For Scheduled/NRT Alert Object` | _Optional_ If enabled, the connector waits until a Scheduled/NRT alert object is available.  
`Proxy Server Address` | _Optional_ Address of the proxy server to use.  
`Proxy Server Username` | _Optional_ Proxy username to authenticate with.  
`Proxy Server Password` | _Optional_ Proxy password to authenticate with.  
`Incident Creation Time Filter (days)` | _Optional_ The number of days before the current time to fetch incidents. If specified, the connector only fetches incidents created within this timeframe. This value must be a valid positive integer. This is an advanced parameter.  
  
#### Connector rules

The **Microsoft Sentinel Incident Tracking Connector** supports blocklists and dynamic lists.

## Jobs

For more information on jobs, see [ Configure a new job](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#configure-a-new-job) and [ Advanced scheduling](https://cloud.google.com/chronicle/docs/soar/respond/jobs-scheduler/writing-jobs#advanced-scheduling). 

### Deprecated: Microsoft Sentinel - Sync Incidents

**Deprecated:** This job is deprecated. Use the Microsoft Sentinel - Sync Incidents V2 job instead.

Use the **Microsoft Sentinel - Sync Incidents** job to synchronize Google SecOps alerts with Microsoft Sentinel incidents. It ensures that comments, status, and tags are kept in sync between the two systems.

For the job to identify the correct information, the Google SecOps case must have the `Microsoft Sentinel Incident` tag. If an alert did not originate from the `Microsoft Azure Sentinel Incident Connector v2`, you must add an `Incident_ID` context value to the case for the job to find the correct information.

#### Job behavior

This job consists of two main parts:

  1. The job synchronizes alert statuses, comments, and tags from Microsoft Sentinel to Google SecOps.
  2. The job synchronizes any updates from Google SecOps back to Microsoft Sentinel.



The job processes a maximum number of cases per iteration to ensure stable performance. It relies on the last modification time of a case to ensure no updates are missed.

When an alert is closed in either system, the job synchronizes the closure. The status mapping is as follows:

  * `Malicious` maps to a Microsoft Sentinel status of `Closed` with a `True Positive` reason.
  * `Not Malicious` maps to a Microsoft Sentinel status of `Closed` with a `False Positive` reason.
  * Any other closure value maps to a Microsoft Sentinel status of `Closed` with an `Unknown` reason.



#### Important notes on API Rate Limiting

This job leverages the Microsoft Graph API to manage incidents, which has a rate limit of 20 requests per minute. To reduce the risk of reaching this limit, it is highly recommended that you set up a separate Microsoft Entra ID App specifically for this job with the `SecurityIncident.ReadWrite.All` permission.

#### Job parameters

The **Microsoft Sentinel - Sync Incidents** job requires the following parameters:

Parameter | Description  
---|---  
`Environment Name` | Required. The name of the environment from which to sync incidents. The default value is `Default Environment`.  
`Azure Active Directory ID` | Required. Your unique directory ID in Azure (Tenant ID).   
`OAUTH2 Login Endpoint Url` | Required. The URL for the OAuth 2.0 endpoint. The default value is `https://login.microsoftonline.com`.  
`API Root` | Required. The base URL for the Graph API. The default value is `https://graph.microsoft.com`.  
`Client ID` | Required. The unique ID of the application registered in Azure Active Directory.   
`Client Secret` | Required. The confidential key used with the `Client ID`.   
`Max Hours Backwards` | Required. The number of hours in the past to synchronize incidents. The default value is `24`.  
`Verify SSL` | Required. Verifies the SSL certificate for the Microsoft Sentinel server. Enabled by default.  
  
### Microsoft Sentinel - Sync Incidents V2

Use the **Sync Incidents V2** job to synchronize Google SecOps alerts with Microsoft Sentinel incidents. This job ensures that comments, statuses, and tags are synchronized bi-directionally between both systems.

**Note:** Assignee and severity synchronization occurs exclusively from Microsoft Sentinel to Google SecOps.

#### Job behavior

  * **Prerequisites:** For the job to identify the correct information, the Google SecOps case must have the `Microsoft Sentinel Incident` tag. This job only works on alerts from the **Microsoft Azure Sentinel Incident Connector v2**.

  * **Initial logic:** The first iteration relies on `Max Hours Backwards` to query alerts where the start time is greater than or equal to the current time minus the specified hours. Subsequent runs use the `start_time` of the last processed alert.

  * **Status synchronization:** The job monitors both systems for status changes. When an incident is closed in Microsoft Sentinel, the Google SecOps case and alert status updates automatically.

    * If the Microsoft Sentinel Reason is `True positive - Suspicious activity`, the Google SecOps reason for closing is set to `Malicious`.

    * If the Microsoft Sentinel Reason is either `False Positive - Incorrect Alert Logic` or `False Positive - Inaccurate Data`, the Google SecOps reason for closing is set to `Not Malicious`.

    * All other values result in a Google SecOps closing reason of `Inconclusive`.

This synchronization also works from Google SecOps to Microsoft Sentinel.

  * **Comment synchronization:** Comments from Sentinel to Google SecOps use the structure: `Microsoft Sentinel Incident` INCIDENT_NUMBER`:` COMMENT.

Comments from Google SecOps to Sentinel use the structure: `Google SecOps Case` CASE_ID`:` COMMENT.

  * **Tag synchronization:** Tags synchronize using specific prefixes to maintain source clarity.

    * Google SecOps tags: `Google SecOps:` TAG`.`
    * Microsoft Sentinel tags: `Microsoft Sentinel:` TAG`.`
  * **Severity and assignee synchronization:** Microsoft Sentinel acts as the source of truth for these fields. Severity and assignee synchronization occurs exclusively from Microsoft Sentinel to Google SecOps.

  * **Assignee synchronization control:** If `Sync Assignee` is disabled, the assignee doesn't synchronize from Microsoft Sentinel to Google SecOps.


**Note:** We recommend disabling Alert Grouping for these alerts to ensure the job functions correctly.

#### Job parameters

The **Sync Incidents V2** job requires the following parameters:

Parameter | Description  
---|---  
`Environment Name` | Required. The name of the environment from which to sync incidents. The default value is `Default Environment`.  
`Azure Subscription ID` | Required. The ID of the Azure subscription containing the Sentinel workspace.  
`Azure Active Directory ID` | Required. Your unique directory ID in Azure, also known as your tenant ID.  
`OAUTH2 Login Endpoint Url` | Required. The URL for the OAuth 2.0 endpoint where the job requests an authentication token. The default value is `https://login.microsoftonline.com`.  
`Management API Root` | Required. The base URL for the Management API. The job appends specific API calls to this root URL to retrieve data. The default value is `https://management.azure.com`.  
`Azure Resource Group` | Required. The name of the Azure Resource Group where the Sentinel workspace is located.  
`Azure Sentinel Workspace Name` | Required. The name of the Microsoft Sentinel workspace.  
`Client ID` | Required. The unique ID of the application registered in Azure Active Directory that is granted permissions to access Microsoft Sentinel.  
`Client Secret` | Required. The confidential key for the application, used in conjunction with `Client ID` to authenticate and authorize the job.  
`Max Hours Backwards` | Required. The number of hours to synchronize incidents prior to the current time. The default value is `24`.  
`Sync Assignee` | Optional. If selected, the job syncs the assignee from Microsoft Sentinel to Google SecOps.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Enabled by default.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
