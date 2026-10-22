---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-defender-atp/
title: Microsoft Defender For Endpoint \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:34.117332+00:00
---

# Microsoft Defender For Endpoint  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-defender-atp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Microsoft Defender For Endpoint

**Important:** In the Google SecOps platform, the Microsoft Defender For Endpoint integration is called _Microsoft Defender ATP_.

This document provides guidance on how to integrate Microsoft Defender For Endpoint with Google SecOps.

## Use cases

  1. Use the data gathered in Microsoft Defender for Endpoint for enrichments while investigating a particular case.

Analysts can use the data gathered and stored in Microsoft Defender for Endpoint in investigations—for example, to get information on alerts detected in Microsoft Defender for Endpoint or list machines registered in Microsoft Defender for Endpoint.

  2. Perform active response actions in potential security incidents like isolating a specific host from a network or running an antivirus scan.

  3. Monitor and inspect the Microsoft Defender for Endpoint alerts as Google Security Operations alerts fetched by the respective connector.




## Prerequisites

Before configuring the integration in the Google SecOps platform, make sure to complete the following prerequisite steps:

  1. Create the Microsoft Entra app.

  2. Configure the API permissions for your app.

  3. Create a client secret.




We recommend using Application Context instead of User Context when accessing the Microsoft Defender for Endpoint API.

### Create Microsoft Entra app

  1. Sign in to the [Azure portal](https://portal.azure.com/) as a user administrator or a password administrator.

  2. Select **Microsoft Entra ID**.

  3. Go to **App registrations > New registration**.

  4. Enter the name of the app.

  5. Click **Register**.

**Note:** This document uses a single tenant setup as an example. Redirect URL is not needed for the OAuth flow (client credentials) supported by the integration.
  6. Save the **Application (client) ID** and **Directory (tenant) ID** values to use them later when configuring the integration parameters.




### Configure API permissions

  1. Go to **API Permissions > Add a permission > APIs my organization uses**. The **Request API permissions** dialog opens.

  2. In the **Search** field, enter `WindowsDefenderATP`.

  3. Select the **WindowsDefenderATP > Application permissions**.

  4. Under the **Alert** permission type, select the following permission:

     * `Alert.Read.All`
  5. Click **Add permissions**.

  6. On the **API Permissions** page, click **Add a permission**.

  7. Select **Microsoft Graph > Delegated permissions**.

  8. In the **Select Permissions** section, select the following required permission:

     * `User.Read`
  9. Click **Add permissions**.

  10. On the **API Permissions** page, click **Add a permission**.

  11. Select **WindowsDefenderATP > Application permissions**.

  12. In the **Select Permissions** section, select the following required permissions:

     * `AdvancedQuery.Read.All`
     * `Alert.Read.All`
     * `Alert.ReadWrite.All`
     * `Event.Write`
     * `File.Read.All`
     * `Ip.Read.All`
     * `Machine.Isolate`
     * `Machine.Read.All`
     * `Machine.ReadWrite.All`
     * `Machine.Scan`
     * `Machine.StopAndQuarantine`
     * `Ti.ReadWrite`
     * `Url.Read.All`
     * `User.Read.All`
  13. Click **Grant admin consent for` ORGANIZATION_NAME`**.

When the **Grant admin consent confirmation** dialog appears, click **Yes**.




The example of an API request to get the Defender ATP alerts is as follows (note the `$expand` parameter that is used to fetch data about IP addresses, domains, and files):
    
    
    GET /api/alerts?$expand=files,ips,domains HTTP/1.1
    Host: api.securitycenter.windows.com
    Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJ...
    User-Agent: PostmanRuntime/7.19.0
    Accept: */ *
    Cache-Control: no-cache
    Postman-Token: 2dc0f885-068a-45d4-81a6-2da0d23a58ad,d3dd0e6e-83ab-4d27-94d2-0f3889dff324
    Host: api.securitycenter.windows.com
    Accept-Encoding: gzip, deflate
    Connection: keep-alive
    cache-control: no-cache
    

To learn more about the request parameters and request options like filter or expand, see [Supported Microsoft Defender for Endpoint APIs](https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-atp/exposed-apis-list) in the Microsoft documentation.

### Create client secret

  1. Navigate to **Certificates and secrets > New client secret**.

  2. Provide a description for a client secret and set its expiration deadline.

  3. Click **Add**.

  4. Save the value of the client secret (not the secret ID) to use it as the `Client Secret` parameter value when configuring the integration. The client secret value is only displayed once.




### Enable SIEM integration - Deprecated

**Deprecated:** Microsoft has deprecated the SIEM integration with Microsoft Defender ATP.

  1. In the navigation pane, select **Settings** > **SIEM**.

**Note:** If you encounter an error when trying to enable the SIEM connector application, check the blocking settings of your browser. It might be blocking the new window being opened when you enable the capability.
  2. Select **Enable SIEM integration**.




This activates the SIEM connector access details section with pre-populated values and an application is created under your Azure AD tenant.

**Warning:** The client secret is only displayed once. Make sure you keep a copy of it in a safe place.

  * Choose SIEM type as Generic API.
  * Copy the individual values or select Save details to file to download a file that contains all the values.
  * You will need the values presented on this page to generate a token to access the detections data: Client ID, Client Secret, Resource.



## Integrate Microsoft Defender For Endpoint with Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

**Important:** If you make any changes to the **Application Permissions** or **API Permissions** in your Microsoft Entra ID (Azure AD) App Registration after configuring this integration (for example, adding a new permission for a job to run), you must regenerate and update your credentials in Google SecOps. 

This typically means:

  * Generating a new client secret in your App Registration.
  * Updating the client secret (and regenerating the refresh token, if applicable) in the Google SecOps integration configuration.



Failure to update will prevent new permissions from being applied, causing actions to fail.

### Integration parameters

To configure the integration, use the following parameters:

Parameters  
---  
`Client ID` | _Required_ Client (Application) ID of the Microsoft Entra app to use for the integration.  
`Client Secret` | _Required_ Client secret value of the Microsoft Entra app to use for the integration.  
`Azure Active Directory ID` | _Required_ Microsoft Entra ID (Tenant ID) value.  
`Verify SSL` | _Optional_ If selected, verifies that the SSL certificate for the connection to the Microsoft 365 Defender server is valid. Selected by default.  
`API Root` | _Required_ API root URL to use with integration. For better performance, you can use a server closest to your location:

  * api-us.securitycenter.windows.com
  * api-eu.securitycenter.windows.com
  * api-uk.securitycenter.windows.com

Default value is `https://api.securitycenter.windows.com`.   
  
## Actions

### Delete Entity Indicators

Delete entity indicators in Microsoft Defender for Endpoint.

**Note:** Only the MD5, SHA-1 and SHA256 hashes are supported.

#### Parameters

N/A

#### Run on

This action runs on the following entities:

  * IP Address
  * URL
  * Filehash



#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If the 204 status code is reported (is_success=true):_ "Successfully deleted the following entities as indicators in Microsoft Defender for Endpoint: {entity.identifier}. _If the incident is not found (is_success=true):_ "The following entities don't exist as indicators in Microsoft Defender for Endpoint: {entity.identifier}.**The action should fail and stop a playbook execution:**_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Delete Entity Indicators". Reason: {0}''.format(error.Stacktrace) | General  
  
### Enrich Entities

Enrich Google SecOps Host, IP Address, or File hash entities based on the information from the Microsoft Defender for Endpoint.

#### Parameters

N/A

#### Use cases

The action can be used in the playbooks that investigate activity on devices. If the device has the Microsoft Defender for Endpoint agent installed, then the action pulls information from Defender ATP on a device to enrich Google SecOps entities. The action also can be used to enrich the alert file hashes with the information from the Defender ATP.

#### Run on

This action runs on the following entities:

  * Host
  * IP Address
  * Filehash



#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result

If enrichment works on IP Address or Host:
    
    
    [
        {
            "EntityResult": {
                "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#Machines/$entity",
                "id": "example_id",
                "computerDnsName": "example-name",
                "firstSeen": "2019-11-18T11:13:04.0588699Z",
                "lastSeen": "2019-11-24T18:31:50.581058Z",
                "osPlatform": "Windows10",
                "osVersion": null,
                "osProcessor": "x64",
                "version": "1803",
                "lastIpAddress": "192.0.2.138",
                "lastExternalIpAddress": "203.0.113.28",
                "agentVersion": "10.4860.17134.982",
                "osBuild": 17134,
                "healthStatus": "Active",
                "rbacGroupId": 0,
                "rbacGroupName": null,
                "riskScore": "High",
                "exposureLevel": "Medium",
                "aadDeviceId": null,
                "machineTags": []
            }
        }
    ]
    

If enrichment works on Filehash:
    
    
    [
        {
            "EntityResult": {
                "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#Files/$entity",
                "sha1": "bdd0d38e113a0c7dd6213cf2e89e6cc6d66b5cdb",
                "sha256": "328954033456d5c13e58fb5bcc6c0232f9f62cb6d9185afa51c7913338992491",
                "md5": "9512e1cc66a1d36feb0a290cab09087b",
                "globalPrevalence": 5205000,
                "globalFirstObserved": "2018-06-22T12:59:21.6460311Z",
                "globalLastObserved": "2019-11-21T00:24:01.921338Z",
                "size": 245760,
                "fileType": "APP",
                "isPeFile": true,
                "filePublisher": "Microsoft Corporation",
                "fileProductName": "Microsoft Windows Operating System",
                "signer": "Microsoft Windows",
                "issuer": "Microsoft Windows Production PCA 2011",
                "signerHash": "419e77aed546a1a6cf4dc23c1f977542fe289cf7",
                "isValidCertificate": true
                },
            "EntityResult": {
                "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#microsoft.windowsDefenderATP.api.InOrgFileStats",
                "sha1": "bdd0d38e113a0c7dd6213cf2e89e6cc6d66b5cdb",
                "orgPrevalence": "1",
                "orgFirstSeen": "2019-11-19T03:54:15Z",
                "orgLastSeen": "2019-11-19T04:21:18Z",
                "globalPrevalence": "5205000",
                "globalFirstObserved": "2018-06-22T12:59:21.6460311Z",
                "globalLastObserved": "2019-11-21T00:24:01.921338Z",
                "topFileNames": ["notepad.exe"]
            }
        }
    ]
    

##### Entity enrichment

**IP and Host**

Enrichment Field Name | Logic - When to apply  
---|---  
Defender_ATP.sha1 | Returns if it exists in JSON result  
Defender_ATP.sha256 | Returns if it exists in JSON result  
Defender_ATP.md5 | Returns if it exists in JSON result  
Defender_ATP.globalPrevalence | Returns if it exists in JSON result  
Defender_ATP.globalFirstObserved | Returns if it exists in JSON result  
Defender_ATP.globalLastObserved | Returns if it exists in JSON result  
Defender_ATP.size | Returns if it exists in JSON result  
Defender_ATP.fileType | Returns if it exists in JSON result  
Defender_ATP.isPeFile | Returns if it exists in JSON result  
Defender_ATP.filePublisher | Returns if it exists in JSON result  
Defender_ATP.fileProductName | Returns if it exists in JSON result  
Defender_ATP.signer | Returns if it exists in JSON result  
Defender_ATP.issuer | Returns if it exists in JSON result  
Defender_ATP.signerHash | Returns if it exists in JSON result  
Defender_ATP.isValidCertificate | Returns if it exists in JSON result  
Defender_ATP.orgPrevalence | Returns if it exists in JSON result  
Defender_ATP.orgFirstSeen | Returns if it exists in JSON result  
Defender_ATP.orgLastSeen | Returns if it exists in JSON result  
Defender_ATP.topFileNames | Returns if it exists in JSON result  
  
**File Hash**

Enrichment Field Name | Logic - When to apply  
---|---  
Defender_ATP.sha1 | Returns if it exists in JSON result  
Defender_ATP.sha256 | Returns if it exists in JSON result  
Defender_ATP.md5 | Returns if it exists in JSON result  
Defender_ATP.globalPrevalence | Returns if it exists in JSON result  
Defender_ATP.globalFirstObserved | Returns if it exists in JSON result  
Defender_ATP.globalLastObserved | Returns if it exists in JSON result  
Defender_ATP.size | Returns if it exists in JSON result  
Defender_ATP.fileType | Returns if it exists in JSON result  
Defender_ATP.isPeFile | Returns if it exists in JSON result  
Defender_ATP.filePublisher | Returns if it exists in JSON result  
Defender_ATP.fileProductName | Returns if it exists in JSON result  
Defender_ATP.signer | Returns if it exists in JSON result  
Defender_ATP.issuer | Returns if it exists in JSON result  
Defender_ATP.signerHash | Returns if it exists in JSON result  
Defender_ATP.isValidCertificate | Returns if it exists in JSON result  
Defender_ATP.orgPrevalence | Returns if it exists in JSON result  
Defender_ATP.orgFirstSeen | Returns if it exists in JSON result  
Defender_ATP.orgLastSeen | Returns if it exists in JSON result  
Defender_ATP.topFileNames | Returns if it exists in JSON result  
  
### Execute Live Response Command

Use the **Execute Live Response Command** action to execute a live response command in Microsoft Defender for Endpoint.

**Note:** This is an asynchronous action. Ensure the script timeout value in the Google SecOps IDE is adjusted appropriately to allow for command completion.

#### Action inputs

The **Execute Live Response Command** action requires the following parameters:

Parameter | Description  
---|---  
`Command` | Required. A JSON object representing the command to be executed, including its type and parameters. For more information on supported command structures, see the [Microsoft Defender for Endpoint API documentation](https://learn.microsoft.com/en-us/defender-endpoint/api/run-live-response). Example format:
    
    
    {
        "type": "Command",
        "params": [
            {
                "key": "string",
                "value": "string"
            }
        ]
    }  
  
`Comment` | Optional. A comment or description for the executed command.  
  
#### Action outputs

The **Execute Live Response Command** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Execute Live Response Command** action:
    
    
    {
       "Entity": "",
       "EntityResult": {
           "@odata.context": "https://api.securitycenter.microsoft.com/api/$metadata#MachineActions/$entity",
           "id": "00000000-0000-0000-0000-000000000000",
           "type": "LiveResponse",
           "title": null,
           "requestor": "SEC_OPS_USER",
           "requestorComment": "Execution of live response command",
           "status": "Pending",
           "machineId": "MACHINE_ID_HASH",
           "computerDnsName": "hostname.domain.local",
           "creationDateTimeUtc": "2026-01-04T10:57:33.032Z",
           "lastUpdateDateTimeUtc": "2026-01-04T10:57:33.032Z",
           "cancellationRequestor": null,
           "cancellationComment": null,
           "cancellationDateTimeUtc": null,
           "errorHResult": 0,
           "scope": null,
           "externalId": null,
           "requestSource": "PublicApi",
           "relatedFileInfo": null,
           "commands": [],
           "troubleshootInfo": null,
           "results": {
               "filepath": "",
               "script_name": "remediation_script.ps1",
               "exit_code": 0,
               "script_output": "Script completed successfully",
               "script_errors": ""
           }
       }
    }
    

##### Output messages

The **Execute Live Response Command** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully executed command on the following endpoints in Microsoft Defender for Endpoint: ENTITY_ID.` | The action succeeded.  
`The command didn't complete for the following endpoints in Microsoft Defender for Endpoint: ENTITY_ID. The scan didn't complete for all of the provided endpoints in Microsoft Defender for Endpoint. Error executing action "Execute Live Response Command". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Execute Live Response Command** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Current Task Status

Get the current status of a task.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Task IDs | String | N/A | Yes | Task IDs list as a comma-separated string.  
  
#### Run on

This action runs on all entities.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [
        {
            "status": "Succeeded",
            "creation_date_time_utc": "2020-02-08T03:24:52.8526634Z",
            "cancellation_requestor": null,
            "cancellation_date_time_utc": null,
            "id": "2e39d22e-60a7-4267-899c-a1471e800000",
            "last_update_date_time_utc": "2020-02-08T03:25:35.8345081Z",
            "related_file_info": null,
            "cancellation_comment": null,
            "requestor": "e4fc6454-754d-47f7-bbdb-045fad600000",
            "error_h_result": 0,
            "scope": "Selective",
            "machine_id": "fbc85cf3fbcc8bb14d1a84fcf7bbae4531f00000",
            "type": "Isolate",
            "requestor_comment": "test"
        }
    ]
    

### Get File Related Alerts

Get alerts related to a file from Microsoft Defender for Endpoint based on the file hash.

#### Parameters

**Parameter Display Value** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Status | String | Unknown, New, InProgress, Resolved | No | Specify the statuses of alerts to look for. Parameter accepts multiple values as a comma-separated string.  
Severity | String | UnSpecified, Informational, Low, Medium, High | NO | Specify the severities of the incidents to look for. Parameter accepts multiple values as a comma-separated string.  
Category | String | N/A | No | Specify the alert category to look for.If not provided, the action looks for all categories.Parameter accepts multiple values as a comma-separated string.Possible Values: 'Collection', 'CommandAndControl', 'CredentialAccess', 'DefenseEvasion', 'Discovery', 'Execution', 'Exfiltration', 'Exploit', 'InitialAccess', 'LateralMovement', 'Malware', 'Persistence', 'PrivilegeEscalation', 'Ransomware', 'SuspiciousActivity', 'UnwantedSoftware'.  
Incident ID | Integer | N/A | No | Specify the Microsoft Defender Incident ID for which you want to find related alerts.  
  
#### ‌Use cases

While investigating an alert that came from the Defender ATP connector, this action can be used to gather information if this file is associated with any alerts to get insight on if the file is malicious or not.

#### Run On

This action runs on the Filehash entity.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#Alerts",
        "value": [
            {
                "id": "example_id",
                "incidentId": 2,
                "investigationId": 1,
                "assignedTo": null,
                "severity": "Medium",
                "status": "New",
                "classification": null,
                "determination": null,
                "investigationState": "TerminatedBySystem",
                "detectionSource": "WindowsDefenderAtp",
                "category": "DefenseEvasion",
                "threatFamilyName": null,
                "title": "Suspicious process injection observed",
                "description": "A process abnormally injected code into another process, As a result, unexpected code may be running in the target process memory. Injection is often used to hide malicious code execution within a trusted process. \nAs a result, the target process may exhibit abnormal behaviors such as opening a listening port or connecting to a command and control server.",
                "alertCreationTime": "2019-11-19T03:56:37.7335862Z",
                "firstEventTime": "2019-11-19T03:54:15.7698362Z",
                "lastEventTime": "2019-11-19T03:54:15.7698362Z",
                "lastUpdateTime": "2019-11-20T10:13:31.7266667Z",
                "resolvedTime": null,
                "machineId": "machine-id",
                "alertUser": {
                    "accountName": "example.user",
                    "domainName": "EXAMPLELAB"
                },
                "comments": [],
                "alertFiles": [
                    {
                        "sha1": "1b3b40fbc889fd4c645cc12c85d0805ac36ba254",
                        "sha256": "d3f8fade829d2b7bd596c4504a6dae5c034e789b6a3defbe013bda7d14466677",
                        "filePath": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
                        "fileName": "powershell.exe"
                    },{
                        "sha1": "bdd0d38e113a0c7dd6213cf2e89e6cc6d66b5cdb",
                        "sha256": "328954033456d5c13e58fb5bcc6c0232f9f62cb6d9185afa51c7913338992491",
                        "filePath": "C:\\Windows\\System32\\notepad.exe",
                        "fileName": "notepad.exe"
                    }
                ],
                "alertDomains": [],
                "alertIps": [],
                "alertProcesses": []
            }
        ]
    }
    

### Get File Related Machines

Get machines related to a file from Microsoft Defender for Endpoint based on the file hash.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Machine Name | String | N/A | No | Specify the full machine name to look for.  
Machine IP Address | String | N/A | No | Specify the machine IP address to look for.  
Machine Risk Score | String | N/A | No | Specify the machine risk score to look for.  Parameter accepts multiple values as a comma-separated string.  
Machine Health Status | String | Active, Inactive, ImpairedCommunication, NoSensorData, NoSensorDataImpairedCommunication | No | Specify the machine health status to look for. Parameter accepts multiple values as a comma-separated string.  
Machine OS Platform | String | N/A | No | Specify the machine OS platform to look for.  
RBAC Group ID | String | N/A | No | Specify the RBAC Group ID to look for.  
  
#### Use cases

While investigating an alert that came from the Defender ATP connector, this action can be used to gather information on which machines this file was registered to in Defender ATP.

#### Run on

This action runs on the Filehash entity.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#Machines",
        "value": [
            {
                "id": "example_id",
                "computerDnsName": "example-name",
                "firstSeen": "2019-11-18T11:13:04.0588699Z",
                "lastSeen": "2019-11-20T19:35:36.4619266Z",
                "osPlatform": "Windows10",
                "osVersion": null,
                "osProcessor": "x64",
                "version": "1803",
                "lastIpAddress": "192.0.2.1",
                "lastExternalIpAddress": "203.0.113.121",
                "agentVersion": "10.4860.17134.982",
                "osBuild": 17134,
                "healthStatus": "Active",
                "rbacGroupId": 0,
                "rbacGroupName": null,
                "riskScore": "High",
                "exposureLevel": "Medium",
                "aadDeviceId": null,
                "machineTags": []
            }
        ]
    }
    

### Get Machine Log on Users

Get information on a users logon on a specific machine.

#### Parameters

N/A

#### Use cases

The action can be used for investigation purposes to get specific details on what users logon on a machine in question from the Defender ATP server.

#### Run on

This action runs on the following entities:

  * Host
  * IP Address



#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#Users",
        "value": [
            {
                "id": "example\\example.user",
                "accountName": "example.user",
                "accountDomain": "example",
                "accountSid": null,
                "firstSeen": "2019-11-19T03:50:36Z",
                "lastSeen": "2019-11-19T03:50:36Z",
                "mostPrevalentMachineId": null,
                "leastPrevalentMachineId": null,
                "logonTypes": "Interactive",
                "logOnMachinesCount": 1,
                "isDomainAdmin": false,
                "isOnlyNetworkUser": null
            }
        ]
    }
    

### Get Machine Recommendations

Use the **Get Machine Recommendations** action to retrieve a list of security recommendations for specific machines in Microsoft Defender for Endpoint.

This action runs on the following Google SecOps entities:

  * `Hostname`

  * `IP Address`




#### Action inputs

The **Get Machine Recommendations** action requires the following parameters:

Parameter | Description  
---|---  
`Max Recommendations To Return` | Required. The maximum number of recommendations to retrieve for each entity. The maximum value is `100`. The default value is `100`.  
  
#### Action outputs

The **Get Machine Recommendations** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Machine Recommendations** action:
    
    
    {
       "Entity": "",
       "EntityResult": [
             {
                "id": "va-_-7-zip-_-7-zip",
                "productName": "7-zip",
                "recommendationName": "Update 7-zip to version 25.01.0.0",
                "weaknesses": 12,
                "vendor": "7-zip",
                "recommendedVersion": "25.01.0.0",
                "recommendedVendor": "",
                "recommendedProgram": "",
                "recommendationCategory": "Application",
                "subCategory": "",
                "severityScore": 0.0,
                "publicExploit": true,
                "activeAlert": false,
                "associatedThreats": [],
                "remediationType": "Update",
                "status": "Active",
                "configScoreImpact": 0.0,
                "exposureImpact": 0.0,
                "totalMachineCount": 0,
                "exposedMachinesCount": 1,
                "nonProductivityImpactedAssets": 0,
                "relatedComponent": "7-zip",
                "hasUnpatchableCve": false,
                "tags": [],
                "exposedCriticalDevices": 0
            }
       ]
    }
    

##### Output messages

The **Get Machine Recommendations** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned recommendations for the following endpoints in Microsoft Defender for Endpoint: ENTITY_IDS.` `No recommendations were found for the following endpoints in Microsoft Defender for Endpoint: ENTITY_IDS.` `No recommendations were found for the provided endpoints in Microsoft Defender for Endpoint.` | The action succeeded.  
`Error executing action "Get Machine Recommendations". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Machine Recommendations** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get Machine Related Alerts

Get alerts related to specific machine registered in Defender ATP.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Status | String | Unknown, New, InProgress, Resolved | No | Specify the statuses of alerts to look for.  Parameter accepts multiple values as a comma-separated string.  
Severity | String | UnSpecified, Informational, Low, Medium, High | No | Specify the severities of the incidents to look for. Parameter accepts multiple values as a comma-separated string.  
Category | String | N/A | No | Specify the alert category to look for.If not provided, the action looks for all categories.Parameter accepts multiple values as a comma-separated string.Possible Values: 'Collection', 'CommandAndControl', 'CredentialAccess', 'DefenseEvasion', 'Discovery', 'Execution', 'Exfiltration', 'Exploit', 'InitialAccess', 'LateralMovement', 'Malware', 'Persistence', 'PrivilegeEscalation', 'Ransomware', 'SuspiciousActivity', 'UnwantedSoftware'.  
Incident ID | Integer | N/A | No | Specify the Microsoft Defender Incident ID for which you want to find related alerts.  
  
#### Use cases

The action can be used for investigation purposes to get alerts related to a specific machine in question from the Defender ATP server.

#### Run on

This action runs on the following entities:

  * Host
  * IP Address



#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#Alerts",
        "value": [
            {
                "id": "example-id",
                "incidentId": 1,
                "investigationId": null,
                "assignedTo": "testuser@example.com",
                "severity": "Informational",
                "status": "Resolved",
                "classification": "FalsePositive",
                "determination": "SecurityTesting",
                "investigationState": "UnsupportedAlertType",
                "detectionSource": "WindowsDefenderAtp",
                "category": "Execution",
                "threatFamilyName": null,
                "title": "[Test Alert] Suspicious Powershell commandline",
                "description": "*** This is a test alert ***\nA suspicious Powershell commandline was found on the machine. This commandline might be used during installation, exploration, or in some cases with lateral movement activities which are used by attackers to invoke modules, download external payloads, and get more information about the system. Attackers usually use Powershell to bypass security protection mechanisms by executing their payload in memory without touching the disk and leaving any trace.",
                "alertCreationTime": "2019-11-18T11:17:48.287421Z",
                "firstEventTime": "2019-11-18T11:15:06.5226815Z",
                "lastEventTime": "2019-11-18T11:15:06.5226815Z",
                "lastUpdateTime": "2019-11-20T04:12:03.91Z",
                "resolvedTime": "2019-11-20T04:12:03.4976288Z",
                "machineId": "machine-id",
                "alertUser": {
                    "accountName": "Administrator",
                    "domainName": "US-LT-V13007"
                },
                "comments": [],
                "alertFiles": [
                    {
                        "sha1": "3ce71813199abae99348f61f0caa34e2574f831c",
                        "sha256": "9a7c58bd98d70631aa1473f7b57b426db367d72429a5455b433a05ee251f3236",
                        "filePath": "C:\\Windows\\System32\\cmd.exe",
                        "fileName": "cmd.exe"
                    },
                    {
                        "sha1": "1b3b40fbc889fd4c645cc12c85d0805ac36ba254",
                        "sha256": "d3f8fade829d2b7bd596c4504a6dae5c034e789b6a3defbe013bda7d14466677",
                        "filePath": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
                        "fileName": "powershell.exe"
                    }
                ],
                "alertDomains": [],
                "alertIps": [],
                "alertProcesses": []
            }
        ]
    }
    

### Get Machine Vulnerabilities

Use the **Get Machine Vulnerabilities** action to list vulnerabilities associated with specific machines in Microsoft Defender for Endpoint.

This action runs on the following Google SecOps entities:

  * `Hostname`

  * `IP Address`




#### Action inputs

The **Get Machine Vulnerabilities** action requires the following parameters:

Parameter | Description  
---|---  
`Severity Filter` | Optional. The severity levels used to filter the returned vulnerabilities. The possible values are as follows:

  * `Critical`
  * `High`
  * `Medium`
  * `Low`

The default value is `Critical`.  
`Threat Filter` | Optional. The threat intelligence criteria used to filter the returned vulnerabilities. The possible values are as follows:

  * `Associated Active Alert`
  * `Exploit is available`
  * `Exploit is verified`
  * `This exploit is part of an exploit kit`

  
`Sort By` | Optional. The field used to sort the returned vulnerabilities. The possible values are as follows:

  * `First Detection Time`
  * `Severity`
  * `Update Time`

The default value is `Severity`.  
`Sort Order` | Optional. The order in which the sorted results are displayed. The possible values are as follows:

  * `ASC`
  * `DESC`

The default value is `ASC`.  
`Max Vulnerabilities To Return` | Required. The maximum number of vulnerabilities to return for each entity. The maximum value is `100`. The default value is `100`.  
  
#### Action outputs

The **Get Machine Vulnerabilities** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get Machine Vulnerabilities** action:
    
    
    {
       "Entity": "",
       "EntityResult": [
           {
               "@odata.type": "#microsoft.windowsDefenderATP.api.PublicVulnerabilityDto",
               "id": "CVE-2025-21266",
               "name": "CVE-2025-21266",
               "description": "Summary: The Windows Telephony Service in Microsoft Windows is vulnerable to remote code execution. An attacker can exploit this vulnerability by tricking a user into visiting a malicious website, which would allow them to execute arbitrary code on the system. Impact: If successfully exploited, this vulnerability could allow an attacker to execute arbitrary code on the affected system. This could lead to a complete compromise of the system, enabling the attacker to gain unauthorized access, steal sensitive information, or perform other malicious activities. Remediation: Apply the latest patches and updates provided by the respective vendors. Generated by AI",
               "severity": "High",
               "cvssV3": 8.8,
               "cvssVector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C",
               "exposedMachines": 1,
               "publishedOn": "2025-01-14T08:00:00Z",
               "updatedOn": "2025-09-09T23:45:43.5Z",
               "firstDetected": "2025-01-14T18:31:29Z",
               "patchFirstAvailable": null,
               "publicExploit": false,
               "exploitVerified": false,
               "exploitInKit": false,
               "exploitTypes": [],
               "exploitUris": [],
               "cveSupportability": "Supported",
               "tags": [],
               "epss": 0.01391,
               "status": "RemediationRequired"
           }
       ]
    }
    

##### Output messages

The **Get Machine Vulnerabilities** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned vulnerabilities for the following endpoints in Microsoft Defender for Endpoint: ENTITY_IDS.` `The action wasn't able to return vulnerabilities for the following endpoints in Microsoft Defender for Endpoint: ENTITY_IDS.` `The action wasn't able to return vulnerabilities for the provided endpoints in Microsoft Defender for Endpoint.` `No vulnerabilities were found for the following endpoints in Microsoft Defender for Endpoint: ENTITY_IDS.` `No vulnerabilities were found for the provided endpoints in Microsoft Defender for Endpoint.` | The action succeeded.  
`Error executing action "Get Machine Vulnerabilities". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Machine Vulnerabilities** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Get User Related Alerts

Use the **Get User Related Alerts** action to list alerts associated with specific users in Microsoft Defender for Endpoint.

This action runs on the Google SecOps `User` entity.

#### Action inputs

The **Get User Related Alerts** action requires the following parameters:

Parameter | Description  
---|---  
`Max Alerts To Return` | Required. The maximum number of alerts to retrieve for each user. The maximum value is `100`. The default value is `100`.  
  
#### Action outputs

The **Get User Related Alerts** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Get User Related Alerts** action:
    
    
    [
        {
            "Entity": "User@domain.local",
            "EntityResult": [
                {
                    "id": "da06788650-4d45-4dcf-ae23-d1071ad426ec_1",
                    "incident_id": 864492,
                    "investigation_id": 1778,
                    "assigned_to": "API-Automated Investigation and Response",
                    "severity": "Low",
                    "status": "Resolved",
                    "classification": null,
                    "determination": null,
                    "investigation_state": "Benign",
                    "detection_source": "WindowsDefenderAv",
                    "category": "Malware",
                    "threat_family_name": "Ceprolad",
                    "title": "An active '' malware ",
                    "description": "Malware and unwanted software are undesirable applications that perform annoying, disruptive, or harmful actions on affected machines. Some of these undesirable applications can replicate and spread from one machine to another. Others are able to receive commands from remote attackers and perform activities associated with cyber attacks.\n\nA malware is considered active if it is found running on the machine or it already has persistence mechanisms in place. Active malware detections are assigned higher severity ratings.\n\nBecause this malware was active, take precautionary measures and check for residual signs of infection.",
                    "alert_creation_time": "2026-02-27T06:58:08.1366667Z",
                    "first_event_time": "2026-02-27T06:55:51.021546Z",
                    "last_event_time": "2026-02-27T06:55:51.021546Z",
                    "last_update_time": "2026-02-27T07:13:46.2333333Z",
                    "resolved_time": "2026-02-27T07:13:44.3513463Z",
                    "machine_id": "4f683b2d393afc3149b0de4149acc5449acdf07e",
                    "alert_user": null,
                    "alert_files": [],
                    "comments": [],
                    "alert_domains": null,
                    "alert_ips": null,
                    "alert_processes": null
                },
                {
                    "id": "da0b1f334d-b5e5-4618-8a2a-d3675e62a93b_1",
                    "incident_id": 864492,
                    "investigation_id": null,
                    "assigned_to": null,
                    "severity": "Low",
                    "status": "New",
                    "classification": null,
                    "determination": null,
                    "investigation_state": "UnsupportedAlertType",
                    "detection_source": "WindowsDefenderAtp",
                    "category": "Execution",
                    "threat_family_name": null,
                    "title": "Suspicious JavaScript process",
                    "description": "A suspicious JavaScript process was observed on this device. Attackers typically use JavaScript to download secondary payloads, run additional commands, and perform other malicious activities on the target device.",
                    "alert_creation_time": "2026-02-27T06:58:38.5533333Z",
                    "first_event_time": "2026-02-27T06:55:32.6699867Z",
                    "last_event_time": "2026-03-05T07:24:52.7415066Z",
                    "last_update_time": "2026-03-05T07:28:04.67Z",
                    "resolved_time": null,
                    "machine_id": "4f683b2d393afc3149b0de4149acc5449acdf07e",
                    "alert_user": null,
                    "alert_files": [],
                    "comments": [],
                    "alert_domains": null,
                    "alert_ips": null,
                    "alert_processes": null
                },
                {
                    "id": "da0cfbb355-b5a5-43a5-adb6-d0879d0b0917_1",
                    "incident_id": 690846,
                    "investigation_id": null,
                    "assigned_to": "analyst@company.onmicrosoft.com",
                    "severity": "Medium",
                    "status": "InProgress",
                    "classification": null,
                    "determination": null,
                    "investigation_state": "UnsupportedAlertType",
                    "detection_source": "WindowsDefenderAtp",
                    "category": "Execution",
                    "threat_family_name": null,
                    "title": "Suspicious behavior by cmd.exe was observed",
                    "description": "A suspicious behavior by cmd.exe was observed. This behavior may indicate malware installation or other malicious activities on the machine.",
                    "alert_creation_time": "2025-10-13T10:26:21.3333333Z",
                    "first_event_time": "2025-10-13T10:23:58.1472359Z",
                    "last_event_time": "2025-10-13T10:25:22.714708Z",
                    "last_update_time": "2026-02-13T08:14:22.61Z",
                    "resolved_time": null,
                    "machine_id": "4f683b2d393afc3149b0de4149acc5449acdf07e",
                    "alert_user": null,
                    "alert_files": [],
                    "comments": [
                        {
                            "comment": "\ud83d\udfe6 Intezer Automated Triage\n===================================\n\u26a0\ufe0f Suspicious - Not Mitigated - Follow Up Required\n===================================\n\n- Title: Suspicious behavior by cmd.exe was observed\n- Source: Microsoft Defender for Endpoint\n- Creation time: 13 Oct 25 | 10:26 UTC\n- External severity: Medium\n- Hosts: \n  * workstation-01 (Windows10)\n- Description: A suspicious behavior by cmd.exe was observed. This behavior may indicate malware installation or other malicious activities on the machine.\n- TTPs:\n  * Command and Control: Application Layer Protocol [T1071]\n  * Defense Evasion: MMC [T1218.014]\n  * Execution: Windows Command Shell [T1059.003]\n- Recommended actions: Ensure Device is Patched, Run Intezer Endpoint Scan (https://docs.intezer.com/docs/live-endpoint-analysis), Validate Activity with User\n- Malicious files: APTSimulator_scheduler.bat\n\nView alert: \ud83d\udc49 https://analyze.intezer.com/alerts/da0cfbb355-b5a5-43a5-adb6-d0879d0b0917_1?environment=mde",
                            "createdBy": "API Action",
                            "createdTime": "2025-10-13T10:40:32.4733451Z"
                        }
                    ],
                    "alert_domains": null,
                    "alert_ips": null,
                    "alert_processes": null
                },
                {
                    "id": "da0e3de096-1789-43ff-bb2e-6cc22e5037ad_1",
                    "incident_id": 864492,
                    "investigation_id": null,
                    "assigned_to": null,
                    "severity": "Low",
                    "status": "New",
                    "classification": null,
                    "determination": null,
                    "investigation_state": "UnsupportedAlertType",
                    "detection_source": "WindowsDefenderAtp",
                    "category": "DefenseEvasion",
                    "threat_family_name": null,
                    "title": "Suspicious registry modification",
                    "description": "A suspicious process modified the registry on this device. Registry entries can be added, modified, or removed to change various settings of the system or behavior of a program. Attackers leverage this technique to gain persistence, escalate privileges, launch malicious codes, or to tamper with security products.",
                    "alert_creation_time": "2026-02-27T06:58:38.7266667Z",
                    "first_event_time": "2026-02-27T06:56:11.3416006Z",
                    "last_event_time": "2026-03-05T07:25:30.6007486Z",
                    "last_update_time": "2026-03-05T07:28:07.39Z",
                    "resolved_time": null,
                    "machine_id": "4f683b2d393afc3149b0de4149acc5449acdf07e",
                    "alert_user": null,
                    "alert_files": [],
                    "comments": [],
                    "alert_domains": null,
                    "alert_ips": null,
                    "alert_processes": null
                },
                {
                    "id": "da13c4af0a-bd35-4cb2-a556-fa972f3b80da_1",
                    "incident_id": 864492,
                    "investigation_id": 1779,
                    "assigned_to": "API-Automated Investigation and Response",
                    "severity": "Low",
                    "status": "Resolved",
                    "classification": null,
                    "determination": null,
                    "investigation_state": "Benign",
                    "detection_source": "WindowsDefenderAv",
                    "category": "Malware",
                    "threat_family_name": "Ceprolad",
                    "title": "An active '' malware ",
                    "description": "Malware and unwanted software are undesirable applications that perform annoying, disruptive, or harmful actions on affected machines. Some of these undesirable applications can replicate and spread from one machine to another. Others are able to receive commands from remote attackers and perform activities associated with cyber attacks.\n\nA malware is considered active if it is found running on the machine or it already has persistence mechanisms in place. Active malware detections are assigned higher severity ratings.\n\nBecause this malware was active, take precautionary measures and check for residual signs of infection.",
                    "alert_creation_time": "2026-03-02T07:26:21.22Z",
                    "first_event_time": "2026-03-02T07:25:05.4166175Z",
                    "last_event_time": "2026-03-02T07:25:05.4166175Z",
                    "last_update_time": "2026-03-02T07:37:19.2666667Z",
                    "resolved_time": "2026-03-02T07:37:19.1231428Z",
                    "machine_id": "4f683b2d393afc3149b0de4149acc5449acdf07e",
                    "alert_user": null,
                    "alert_files": [],
                    "comments": [],
                    "alert_domains": null,
                    "alert_ips": null,
                    "alert_processes": null
                },
                {
                    "id": "da2052972f-7cc3-42c8-8abf-8ac490d63c35_1",
                    "incident_id": 690846,
                    "investigation_id": null,
                    "assigned_to": "analyst@company.onmicrosoft.com",
                    "severity": "Medium",
                    "status": "InProgress",
                    "classification": null,
                    "determination": null,
                    "investigation_state": "UnsupportedAlertType",
                    "detection_source": "WindowsDefenderAtp",
                    "category": "Execution",
                    "threat_family_name": null,
                    "title": "Suspicious behavior by cmd.exe was observed",
                    "description": "A suspicious behavior by cmd.exe was observed. This behavior may indicate malware installation or other malicious activities on the machine.",
                    "alert_creation_time": "2025-10-07T10:25:41.1666667Z",
                    "first_event_time": "2025-10-07T10:23:44.5677721Z",
                    "last_event_time": "2025-10-07T10:25:10.6581007Z",
                    "last_update_time": "2026-02-13T08:14:22.61Z",
                    "resolved_time": null,
                    "machine_id": "4f683b2d393afc3149b0de4149acc5449acdf07e",
                    "alert_user": null,
                    "alert_files": [],
                    "comments": [
                        {
                            "comment": "\ud83d\udfe6 Intezer Automated Triage\n===================================\n\ud83e\udde8 Generic Threat - APTSimulator_schedu... - Not Mitigated - Escalated\n===================================\n\n- Title: Suspicious behavior by cmd.exe was observed\n- Source: Microsoft Defender for Endpoint\n- Creation time: 07 Oct 25 | 10:25 UTC\n- External severity: Medium\n- Hosts: \n  * workstation-01 (Windows10)\n- Description: A suspicious behavior by cmd.exe was observed. This behavior may indicate malware installation or other malicious activities on the machine.\n- TTPs:\n  * Command and Control: Application Layer Protocol [T1071]\n  * Defense Evasion: MMC [T1218.014]\n  * Execution: Windows Command Shell [T1059.003]\n- Recommended actions: Isolation, Stop and Quarantine File, Run Intezer Endpoint Scan (https://docs.intezer.com/docs/live-endpoint-analysis)\n- Malicious files: APTSimulator_scheduler.bat\n\nView alert: \ud83d\udc49 https://analyze.intezer.com/alerts/da2052972f-7cc3-42c8-8abf-8ac490d63c35_1?environment=mde",
                            "createdBy": "API Action",
                            "createdTime": "2025-10-07T10:27:41.3867936Z"
                        },
                        {
                            "comment": "\ud83d\udfe6 Intezer Automated Triage (\ud83d\udca1Triage updated \u2192 Risk Deescalated)\n===================================\n\u26a0\ufe0f Suspicious - Not Mitigated - Follow Up Required\n===================================\n\n- Title: Suspicious behavior by cmd.exe was observed\n- Source: Microsoft Defender for Endpoint\n- Creation time: 07 Oct 25 | 10:25 UTC\n- External severity: Medium\n- Hosts: \n  * workstation-01 (Windows10)\n- Description: A suspicious behavior by cmd.exe was observed. This behavior may indicate malware installation or other malicious activities on the machine.\n- TTPs:\n  * Command and Control: Application Layer Protocol [T1071]\n  * Defense Evasion: MMC [T1218.014]\n  * Execution: Windows Command Shell [T1059.003]\n- Recommended actions: Ensure Device is Patched, Run Intezer Endpoint Scan (https://docs.intezer.com/docs/live-endpoint-analysis), Validate Activity with User\n- Malicious files: APTSimulator_scheduler.bat\n\nView alert: \ud83d\udc49 https://analyze.intezer.com/alerts/da2052972f-7cc3-42c8-8abf-8ac490d63c35_1?environment=mde",
                            "createdBy": "API Action",
                            "createdTime": "2025-10-07T10:32:21.417826Z"
                        }
                    ],
                    "alert_domains": null,
                    "alert_ips": null,
                    "alert_processes": null
                },
                {
                    "id": "da2068d331-0335-4479-9f96-e8f33db81aa9_1",
                    "incident_id": 864492,
                    "investigation_id": 1780,
                    "assigned_to": "API-Automated Investigation and Response",
                    "severity": "Low",
                    "status": "Resolved",
                    "classification": null,
                    "determination": null,
                    "investigation_state": "Benign",
                    "detection_source": "WindowsDefenderAv",
                    "category": "Malware",
                    "threat_family_name": "Ceprolad",
                    "title": "An active 'Ceprolad' malware in a command line was prevented from executing",
                    "description": "Malware and unwanted software are undesirable applications that perform annoying, disruptive, or harmful actions on affected machines. Some of these undesirable applications can replicate and spread from one machine to another. Others are able to receive commands from remote attackers and perform activities associated with cyber attacks.\n\nA malware is considered active if it is found running on the machine or it already has persistence mechanisms in place. Active malware detections are assigned higher severity ratings.\n\nBecause this malware was active, take precautionary measures and check for residual signs of infection.",
                    "alert_creation_time": "2026-03-05T07:26:09.89Z",
                    "first_event_time": "2026-03-05T07:25:08.6889036Z",
                    "last_event_time": "2026-03-05T07:25:08.6889036Z",
                    "last_update_time": "2026-03-05T07:37:44.9066667Z",
                    "resolved_time": "2026-03-05T07:37:44.65021Z",
                    "machine_id": "4f683b2d393afc3149b0de4149acc5449acdf07e",
                    "alert_user": null,
                    "alert_files": [],
                    "comments": [],
                    "alert_domains": null,
                    "alert_ips": null,
                    "alert_processes": null
                },
                {
                    "id": "da29243e25-be1e-47b7-9d40-e626df36345c_1",
                    "incident_id": 688299,
                    "investigation_id": null,
                    "assigned_to": null,
                    "severity": "Medium",
                    "status": "InProgress",
                    "classification": null,
                    "determination": null,
                    "investigation_state": "UnsupportedAlertType",
                    "detection_source": "WindowsDefenderAtp",
                    "category": "Persistence",
                    "threat_family_name": null,
                    "title": "New group added suspiciously",
                    "description": "A new group was added after suspicious activities were detected. An attacker might add new users to the group in an attempt to gain a better foothold on the machine or network.",
                    "alert_creation_time": "2025-09-18T14:59:47.52Z",
                    "first_event_time": "2025-09-18T14:53:30.7348596Z",
                    "last_event_time": "2025-09-21T14:53:43.8093531Z",
                    "last_update_time": "2025-09-21T14:56:44.5166667Z",
                    "resolved_time": null,
                    "machine_id": "4f683b2d393afc3149b0de4149acc5449acdf07e",
                    "alert_user": null,
                    "alert_files": [],
                    "comments": [
                        {
                            "comment": "\ud83d\udfe6 Intezer Automated Triage\n===================================\n\u26a0\ufe0f Suspicious - APTSimulator_schedu... - Not Mitigated - Follow Up Required\n===================================\n\n- Title: New group added suspiciously\n- Source: Microsoft Defender for Endpoint\n- Creation time: 18 Sep 25 | 14:59 UTC\n- External severity: Medium\n- Hosts: \n  * workstation-01 (Windows10)\n- Description: A new group was added after suspicious activities were detected. An attacker might add new users to the group in an attempt to gain a better foothold on the machine or network.\n- TTPs:\n  * Command and Control: Application Layer Protocol [T1071]\n  * Discovery: Local Groups [T1069.001]\n  * Persistence: Account Manipulation [T1098]\n- Recommended actions: Ensure Device is Patched, Run Intezer Endpoint Scan (https://docs.intezer.com/docs/live-endpoint-analysis), Validate Activity with User\n\nView alert: \ud83d\udc49 https://analyze.intezer.com/alerts/da29243e25-be1e-47b7-9d40-e626df36345c_1?environment=mde",
                            "createdBy": "API Action",
                            "createdTime": "2025-09-18T15:03:43.2796289Z"
                        }
                    ],
                    "alert_domains": null,
                    "alert_ips": null,
                    "alert_processes": null
                },
                {
                    "id": "da2be6df1c-2401-4545-8111-5f75d0fd0223_1",
                    "incident_id": 690846,
                    "investigation_id": null,
                    "assigned_to": "analyst@company.onmicrosoft.com",
                    "severity": "Low",
                    "status": "InProgress",
                    "classification": null,
                    "determination": null,
                    "investigation_state": "UnsupportedAlertType",
                    "detection_source": "WindowsDefenderAtp",
                    "category": "Execution",
                    "threat_family_name": null,
                    "title": "Suspicious JavaScript process",
                    "description": "A suspicious JavaScript process was observed on this device. Attackers typically use JavaScript to download secondary payloads, run additional commands, and perform other malicious activities on the target device.",
                    "alert_creation_time": "2025-10-01T10:26:20.6566667Z",
                    "first_event_time": "2025-10-01T10:24:19.1071611Z",
                    "last_event_time": "2025-10-07T10:24:27.1065475Z",
                    "last_update_time": "2026-02-13T08:14:22.61Z",
                    "resolved_time": null,
                    "machine_id": "4f683b2d393afc3149b0de4149acc5449acdf07e",
                    "alert_user": null,
                    "alert_files": [],
                    "comments": [
                        {
                            "comment": "\ud83d\udfe6 Intezer Automated Triage\n===================================\n\u26a0\ufe0f Suspicious - en-US.js - Not Mitigated - Follow Up Required\n===================================\n\n- Title: Suspicious JavaScript process\n- Source: Microsoft Defender for Endpoint\n- Creation time: 01 Oct 25 | 10:26 UTC\n- External severity: Low\n- Hosts: \n  * workstation-01 (Windows10)\n- Description: A suspicious JavaScript process was observed on this device. Attackers typically use JavaScript to download secondary payloads, run additional commands, and perform other malicious activities on the target device.\n- TTPs:\n  * Command and Control: Application Layer Protocol [T1071]\n  * Defense Evasion: Indicator Removal on Host [T1070]\n  * Defense Evasion: Indicator Removal on Host: Timestomp [T1070.006]\n- Recommended actions: Ensure Device is Patched, Run Intezer Endpoint Scan (https://docs.intezer.com/docs/live-endpoint-analysis), Validate Activity with User\n\nView alert: \ud83d\udc49 https://analyze.intezer.com/alerts/da2be6df1c-2401-4545-8111-5f75d0fd0223_1?environment=mde",
                            "createdBy": "API Action",
                            "createdTime": "2025-10-01T10:30:36.462226Z"
                        }
                    ],
                    "alert_domains": null,
                    "alert_ips": null,
                    "alert_processes": null
                },
                {
                    "id": "da37252b75-0446-4a7b-99b4-e64886557bd3_1",
                    "incident_id": 688299,
                    "investigation_id": null,
                    "assigned_to": null,
                    "severity": "Low",
                    "status": "InProgress",
                    "classification": null,
                    "determination": null,
                    "investigation_state": "UnsupportedAlertType",
                    "detection_source": "WindowsDefenderAtp",
                    "category": "Execution",
                    "threat_family_name": null,
                    "title": "Suspicious JavaScript process",
                    "description": "A suspicious JavaScript process was observed on this device. Attackers typically use JavaScript to download secondary payloads, run additional commands, and perform other malicious activities on the target device.",
                    "alert_creation_time": "2025-09-18T14:59:46.57Z",
                    "first_event_time": "2025-09-18T14:54:11.4061419Z",
                    "last_event_time": "2025-09-21T14:54:00.575478Z",
                    "last_update_time": "2025-09-21T14:56:36.6533333Z",
                    "resolved_time": null,
                    "machine_id": "4f683b2d393afc3149b0de4149acc5449acdf07e",
                    "alert_user": null,
                    "alert_files": [],
                    "comments": [
                        {
                            "comment": "\ud83d\udfe6 Intezer Automated Triage\n===================================\n\u26a0\ufe0f Suspicious - wscript.exe - Not Mitigated - Follow Up Required\n===================================\n\n- Title: Suspicious JavaScript process\n- Source: Microsoft Defender for Endpoint\n- Creation time: 18 Sep 25 | 14:59 UTC\n- External severity: Low\n- Hosts: \n  * workstation-01 (Windows10)\n- Description: A suspicious JavaScript process was observed on this device. Attackers typically use JavaScript to download secondary payloads, run additional commands, and perform other malicious activities on the target device.\n- TTPs:\n  * Command and Control: Application Layer Protocol [T1071]\n  * Defense Evasion: Indicator Removal on Host [T1070]\n  * Defense Evasion: Indicator Removal on Host: Timestomp [T1070.006]\n- Recommended actions: Ensure Device is Patched, Run Intezer Endpoint Scan (https://docs.intezer.com/docs/live-endpoint-analysis), Validate Activity with User\n\nView alert: \ud83d\udc49 https://analyze.intezer.com/alerts/da37252b75-0446-4a7b-99b4-e64886557bd3_1?environment=mde",
                            "createdBy": "API Action",
                            "createdTime": "2025-09-18T15:06:13.2743521Z"
                        }
                    ],
                    "alert_domains": null,
                    "alert_ips": null,
                    "alert_processes": null
                }
            ]
        }
    ]
    

##### Output messages

The **Get User Related Alerts** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully returned alerts related to the following users in Microsoft Defender for Endpoint: ENTITY_IDS.` `No alerts were related to the following users in Microsoft Defender for Endpoint: ENTITY_IDS.` `No alerts were related to the provided users in Microsoft Defender for Endpoint.` | The action succeeded.  
`Error executing action "Get User Related Alerts". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get User Related Alerts** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Isolate Machine

Isolate a machine using Microsoft Defender for Endpoint. The Machine can be set under full isolation, or selective isolation. Outlook, Skype for Business, and Teams applications continue to work on a machine under isolation.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Isolation Type | DDL | FullPossible Values:

  * Full
  * Selective

| Yes | Specify the isolation type.  
Comment | String | N/A | Yes | Specify a comment as to why the machine needs to be isolated.  
Create an Insight? | Checkbox | Checked |  | If enabled, the action creates a Google SecOps Insight with related information if executed successfully.  
  
#### Use cases

Isolate a machine that is considered to be infected. For example, Defender ATP connector alert was ingested to the Google SecOps server, and during an alert analysis it was discovered that related to the alert machine (Case entity), it can be infected and needs to be isolated.

#### Run on

This action runs on the following actions:

  * Host
  * IP Address



#### Action results

##### Script result

True if the API Endpoint returned for **every** provided entity it ran on, **status 201** , in JSON Response "status": "Pending", which indicates that the API request executed successfully. If at least for one of the entities the action fails, the final result should be fail (False).

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity",
        "id": "example-id",
        "type": "Isolate",
        "requestor": "requestor-id",
        "requestorComment": "Machine Isolation due to alert ...",
        "status": "Pending",
        "machineId": "machine-id",
        "creationDateTimeUtc": "2019-11-21T03:55:59.5419077Z",
        "lastUpdateDateTimeUtc": "2019-11-21T03:55:59.5419077Z",
        "cancellationRequestor": null,
        "cancellationComment": null,
        "cancellationDateTimeUtc": null,
        "errorHResult": 0,
        "scope": null,
        "relatedFileInfo": null
    }
    

##### Insights

  * **Insight Logic:** If machine was isolated using Defender ATP agent, create an insight to indicate this.
  * **Type:** Entity.
  * **Title (String):** entity.
  * **IdentifierMessage:** "Host was isolated using Microsoft Defender for Endpoint."



### List Alerts

List Microsoft Defender for Endpoint alerts based on provided search criteria. The action returns information on found alerts in a table and JSON view form as an action output, along with raw alert data that is stored in and attached to the action output JSON file.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Time Frame | Integer | 3 | No | Specify a timeframe in hours for which to fetch alerts.  
Status | String | Unknown, New, InProgress, Resolved | No | Specify the statuses of alerts to look for. Parameter accepts multiple values as a comma-separated string.  
Severity | String | N/A | No | Specify the severity of the incidents to look for. If not provided, the action looks for all severities. Parameter accepts multiple values as a comma-separated string. Possible Values: UnSpecified, Informational, Low, Medium, and High  
Category | String | N/A | No | Specify the alert category to look for.If not provided, the actions looks for all categories. Parameter accepts multiple values as a comma-separated string. Possible Values: 'Collection', 'CommandAndControl', 'CredentialAccess', 'DefenseEvasion', 'Discovery', 'Execution', 'Exfiltration', 'Exploit', 'InitialAccess', 'LateralMovement', 'Malware', 'Persistence', 'PrivilegeEscalation', 'Ransomware', 'SuspiciousActivity', 'UnwantedSoftware'.  
Incident ID | Integer | N/A | No | Specify the Microsoft Defender Incident ID for which you want to find related alerts.  
  
#### Use cases

The action may be used to review Defender ATP warnings to Google SecOps server for an end-user. For example, when dealing with the warning that came from the Defender ATP connector, the user configures the "List Warnings" action to accept processed alert IncidentId as the input parameter to pull details from the Defender ATP server-there are any other warnings that are part of a single Defender ATP Incident.

#### Run on

This action runs on all entities.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#Alerts",
        "value": [
            {
                "id": "example_id",
                "incidentId": 2,
                "investigationId": null,
                "assignedTo": null,
                "severity": "Medium",
                "status": "New",
                "classification": null,
                "determination": null,
                "investigationState": "UnsupportedAlertType",
                "detectionSource": "WindowsDefenderAtp",
                "category": "Execution",
                "threatFamilyName": null,
                "title": "Unexpected behavior observed by a process run with no command line arguments",
                "description": "The legitimate process by this name does not normally exhibit this behavior when run with no command line arguments. \nSuch unexpected behavior may be a result of extraneous code injected into a legitimate process, or a malicious executable masquerading as the legitimate one by name.",
                "alertCreationTime": "2019-11-19T03:56:35.3007009Z",
                "firstEventTime": "2019-11-19T03:54:16.0441057Z",
                "lastEventTime": "2019-11-19T03:54:16.0441057Z",
                "lastUpdateTime": "2019-11-19T03:56:38.45Z",
                "resolvedTime": null,
                "machineId": "machine-id",
                "alertUser": null,
                "comments": [],
                "alertFiles": [],
                "alertDomains": [],
                "alertIps": [],
                "alertProcesses": []
                }
        ]
    }
    

### List Indicators

List indicators in Microsoft Defender for Endpoint.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Indicators | CSV | N/A | No | Specify a comma-separated list of indicators that you would like to retrieve.  
Indicator Types | CSV | FileSha1,FileSha256,FileMd5,CertificateThumbprint,IpAddress,DomainName, Url | No | Specify a comma-separated list of indicator types that you want to retrieve.Possible values: FileSha1, FileSha256, FileMd5, CertificateThumbprint, IpAddress,DomainName, Url.  
Actions | CSV | Warn,Block,Audit,Alert,AlertAndBlock,BlockAndRemediate,Allowed | No | Specify a comma-separated list of indicator actions that you want to use for filtering.Possible values: Warn,Block,Audit,Alert, AlertAndBlock,BlockAndRemediate,Allowed  
Severity | CSV | Informational,Low,Medium,High | No | Specify a comma-separated list of severities that you want to use for filtering.Possible values: Informational,Low,Medium,High  
Max Results To Return | Integer | 50 | No | Specify the number of indicators to return.  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "id": "18",
        "indicatorValue": "110e7d15b011d7fac48f2bd61114db1022197f7a",
        "indicatorType": "FileSha1",
        "action": "Audit",
        "createdBy": "45e9773c-100e-4a9f-ad37-d8e182e9ed26",
        "severity": "Informational",
        "category": 1,
        "application": "demo-test",
        "educateUrl": null,
        "bypassDurationHours": null,
        "title": "test",
        "description": "test",
        "recommendedActions": "nothing",
        "creationTimeDateTimeUtc": "2022-02-08T14:20:34.9071582Z",
        "expirationTime": null,
        "lastUpdateTime": "2022-02-08T14:20:34.9151307Z",
        "lastUpdatedBy": null,
        "rbacGroupNames": [],
        "rbacGroupIds": [],
        "notificationId": null,
        "notificationBody": null,
        "version": null,
        "mitreTechniques": [],
        "historicalDetection": false,
        "lookBackPeriod": null,
        "generateAlert": true,
        "additionalInfo": null,
        "createdByDisplayName": "Example Defender ATP",
        "externalId": null,
        "createdBySource": "PublicApi",
        "certificateInfo": null
    }
    

##### Case wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If data is available (is_success=true):_ "Successfully found indicators for the provided criteria in Microsoft Defender for Endpoint."._If data is not available (is_success=false):_ "No indicators were found for the provided criteria in Microsoft Defender for Endpoint."  **The action should fail and stop a playbook execution:** _If a fatal error, like wrong_ _credentials, no connection to the server, other is reported:_ "Error executing action "List Indicators". Reason: {0}''.format(error.Stacktrace)_If an invalid "Indicator types" parameter is provided:_ "Error executing action "List Indicators". Reason: invalid value for the parameter "Indicator Types". Possible values: FileSha1, FileSha256, FileMd5, CertificateThumbprint, IpAddress, DomainName, Url._If an invalid "Actions" parameter is provided:_ "Error executing action "List Indicators". Reason: invalid value for the parameter "Actions". Possible values: Warn, Block, Audit, Alert, AlertAndBlock, BlockAndRemediate, Allowed._If an invalid "Severity" parameter is provided:_ "Error executing action "List Indicators". Reason: invalid value for the parameter "Actions". Possible values: Informational, Low, Medium, High. | General  
Case Wall Table | **Found Indicators** Type: indicatorType Action: action Severity: severity Description: description Title: title Recommendation: recommendedActions | Entity  
  
### List Machines

Get information about machines registered with the Microsoft Defender for Endpoint server based on the parameters given for the search.

**Note:** This action returns data from a period of 30 days, and data up to 3 MB. Exceeding data is truncated. The action output is displayed in a table view and a JSON viewer. The output is also attached in the JSON format as a file to the Case wall.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Last Seen Time Frame | Integer | N/A | No | Specify the last seen timeframe to look for in hours.  
Machine Name | String | N/A | No | Specify the full machine name to look for.  
Machine IP Address | String | N/A | No | Specify the machine IP address to look for.  
Machine Risk Score | String | None, Low, Medium, High | No | Specify the machine risk score to look for.  Parameter accepts multiple values as a comma-separated string.  
Machine Health Status | String | Active, Inactive, ImpairedCommunication, NoSensorData, NoSensorDataImpairedCommunication | No | Specify the machine health status to look for.  Parameter accepts multiple values as a comma-separated string.  
Machine OS Platform | String | N/A | No | Specify the machine OS platform to look for.  
RBAC Group ID | String | N/A | No | Specify the RBAC Group ID to look for.  
  
#### Use cases

The action can be used for investigation purposes to get information on devices registered on the Defender ATP server. This action is mostly used as manual action, for the user to not have to switch back to Defender ATP console and look for which machines Defender ATP agent is working on.

#### Run on

This action runs on all entities.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#Machines",
        "value": [
            {
                "id": "example-id",
                "computerDnsName": "example-name",
                "firstSeen": "2019-11-18T11:13:04.0588699Z",
                "lastSeen": "2019-11-20T09:59:28.0646303Z",
                "osPlatform": "Windows10",
                "osVersion": null,
                "osProcessor": "x64",
                "version": "1803",
                "lastIpAddress": "192.0.2.138",
                "lastExternalIpAddress": "203.0.113.35",
                "agentVersion": "10.4860.17134.982",
                "osBuild": 17134,
                "healthStatus": "Active",
                "rbacGroupId": 0,
                "rbacGroupName": null,
                "riskScore": "High",
                "exposureLevel": "Medium",
                "aadDeviceId": null,
                "machineTags": []
            },{
                "id": "example-id",
                "computerDnsName": "example-name",
                "firstSeen": "2019-11-20T08:36:16.2721384Z",
                "lastSeen": "2019-11-20T08:36:52.7182837Z",
                "osPlatform": "Windows10",
                "osVersion": null,
                "osProcessor": "x64",
                "version": "1803",
                "lastIpAddress": "192.0.2.141",
                "lastExternalIpAddress": "203.0.113.35",
                "agentVersion": "10.4850.17134.191",
                "osBuild": 17134,
                "healthStatus": "Active",
                "rbacGroupId": 0,
                "rbacGroupName": null,
                "riskScore": "None",
                "exposureLevel": "Medium",
                "aadDeviceId": null,
                "machineTags": []
            }
        ]
    }
    

### Ping

Test connectivity to Microsoft Defender for Endpoint instance with parameters provided at the integration configuration page.

#### Parameters

N/A

#### Use cases

The action is used to test the connectivity and can be executed as manual action, which is not a part of playbooks.

#### Run on

This action runs on all entities.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### Run Advanced Hunting Query

Run Microsoft Defender for Endpoint advanced hunting query. Note that quotes, new lines, or other special symbols need to be escaped, for example, use the backslash for escaping quotes.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
Query | String | N/A | Yes | Advanced hunting query to execute.  
  
#### Use cases

The user can have hunting queries that they want to use to query data gathered in Defender ATP during the processing of a specific Defender Alert, with this action the user can run those advanced hunting queries.

#### Run on

This action runs on all entities.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "Stats": {
            "ExecutionTime": 0.0156652,
            "resource_usage": {
                "cache": {
                    "memory": {
                        "hits": 13,
                        "misses": 0,
                        "total": 13
                    },
                    "disk": {
                        "hits": 0,
                        "misses": 0,
                        "total": 0
                    }
                },
                "cpu": {
                    "user": "00:00:00.0156250",
                    "kernel": "00:00:00",
                    "total cpu": "00:00:00.0156250"
                },
                "memory": {
                    "peak_per_node": 33554624
                }
            },
            "dataset_statistics": [
                {
                    "table_row_count": 2,
                    "table_size": 60
                }
            ]
        },
        "Schema": [
            {
                "Name": "EventTime",
                "Type": "DateTime"
            },
            {
                "Name": "FileName",
                "Type": "String"
            },
            {
                "Name": "InitiatingProcessFileName",
                "Type": "String"
            }
        ],
        "Results": [
            {
                "EventTime": "2019-11-18T11:13:07.043128Z",
                "FileName": "csc.exe",
                "InitiatingProcessFileName": "powershell.exe"
            },
            {
                "EventTime": "2019-11-19T03:54:14.4256361Z",
                "FileName": "csc.exe",
                "InitiatingProcessFileName": "powershell.exe"
            }
        ]
    }
    

**Warning:** The JSON Results depend on Query. Different queries yield different results, therefore example that matches all cannot be provided. Also, as the JSON example can't match the actual results, you need to manually write the placeholders according to the query.

### Run Antivirus Scan

Start an antivirus scan on a host using Microsoft Defender for Endpoint. Two types of Defender ATP scans are available: Full or Quick.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Antivirus Scan Type | DDL | FullPossible Values:

  * Full
  * Quick

| Yes | Specify whether to start Full or Quick antivirus scan on machine.  
Comment | String | N/A | Yes | Specify a comment as to why an antivirus scan needs to be executed on the machine.  
  
#### Use cases

An alert came from the Defender ATP connector, during the alert processing indicators of malware compromises were found on the machine related to the Google SecOps case entity, and because of that the user decided to run an antivirus scan on the machine to try to find malware on the host.

#### Run on

This action runs on the following entities:

  * Host
  * IP Address



#### Action results

##### Script result

True if the API Endpoint returned for **every** provided entity it ran on, **status 201** , in JSON Response "status": "Pending", which indicates that the API request executed successfully. If at least for one of the entities the action fails, the final result should be fail (False).

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity",
        "id": "example-id",
        "type": "RunAntiVirusScan",
        "requestor": "requestor_id",
        "requestorComment": "Run antivirus scan on suspect",
        "status": "Pending",
        "machineId": "machine-id",
        "creationDateTimeUtc": "2019-11-21T11:07:06.611628Z",
        "lastUpdateDateTimeUtc": "2019-11-21T11:07:06.611628Z",
        "cancellationRequestor": null,
        "cancellationComment": null,
        "cancellationDateTimeUtc": null,
        "errorHResult": 0,
        "scope": null,
        "relatedFileInfo": null
    }
    

### Stop and Quarantine a File on Specific Machine

Stop execution of a file on a specific machine and quarantine it using Microsoft Defender For Endpoint agent. Action works with either Host or IP Google SecOps entities.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
SHA1 File Hash to Quarantine | String | N/A | Yes | Specify SHA-1 file hash of the file to stop and quarantine.  **Note:** The SHA-1 hash needs to be in the lower register for the action to find matching file.  
Comment | String | N/A | Yes | Specify a comment as to why an antivirus scan needs to be executed on the machine.  
Create an Insight? | Checkbox | Checked |  | If enabled, action will create a Google SecOps Insight with related information if executed successfully.  
  
#### Use cases

During processing of the alert that came from the Defender ATP connector, the "Stop and Quarantine File" action can be used to block the specific file from execution to prevent compromise of the machine. The need for this action might come from the advanced hunting, and the user might discover some potentially malicious files that at the moment the user wants to block on a single machine.

#### Run on

This action runs on the following entities:

  * Host
  * IP Address



#### Action results

##### Script result

Can be True or False. True if the API Endpoint returned for **every** provided entity it ran on, **status 201** , in JSON Response "status": "Pending", which indicates that API request executed successfully. If at least for one of the entities action fail - final result should be fail (False).

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity",
        "id": "example-id",
        "type": "StopAndQuarantineFile",
        "requestor": "requestor-id",
        "requestorComment": "Stopping and quarantining putty",
        "status": "Pending",
        "machineId": "machine-id",
        "creationDateTimeUtc": "2019-11-25T10:05:21.3641296Z",
        "lastUpdateDateTimeUtc": "2019-11-25T10:05:21.3641296Z",
        "cancellationRequestor": null,
        "cancellationComment": null,
        "cancellationDateTimeUtc": null,
        "errorHResult": 0,
        "scope": null,
        "relatedFileInfo": {
            "fileIdentifier": "d932604ab8e9debe475415851fd26929a0c0dcd1",
            "fileIdentifierType": "Sha1"
        }
    }
    

##### Insights

  * **Type:** Entity.
  * **Title (String):** entity.
  * **IdentifierMessage (String):** "File with SHA-1 Filehash {0} was stopped and quarantined on {1}". format (filehash,entity.Identifier).



### Submit Entity Indicators

Submit entities as indicators in Microsoft Defender for Endpoint.

**Note:** Only the MD5, SHA-1 and SHA256 hashes are supported.

#### Parameters

**Parameter Display** **Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Action | DDL | Block Possible Values:

  * Block
  * Audit
  * Block And Remediate
  * Allow

| Yes | Specify the action that needs to be applied to the entities. **Note:** The "Block And Remediate" value is supported only for the filehash entities.  
Severity | DDL | High Possible Values: 

  * High
  * Medium
  * Low
  * Informational

| Yes | Specify the severity for the found entities.  
Application | String | N/A | No | Specify an application that is related to the entities.  
Indicator Alert Title | String | N/A | Yes | Specify the title for the alert, if they are identified in the environment.  
Description | String | Google SecOps Remediation | Yes | Specify the description for the entities.  
Recommended Action | String | N/A | No | Specify the recommended actions for the handling of the entities.  
  
#### Run on

This action runs on the following entities:

  * IP Address
  * URL
  * Filehash



#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available for one entity (is_success = true):_ "Successfully submitted the following entities as indicators to Microsoft Defender for Endpoint: {entity.identifier}"._If data is not available for one entity (is_success=true):_ "Action wasn't able to submit the following entities as indicators to Microsoft Defender for Endpoint: {entity.identifier}". _If the 403 status code is reported for one entity:_ "Instance doesn't have enough permissions to submit for the following entities: {entity.identifier}If data is not available for all entities (is_success=false): "None of the provided entities were submitted as indicators to Microsoft Defender for Endpoint."If an entity is already an indicator: "The following entities are already indicators in Microsoft Defender for Endpoint: {entity.identifier}"**The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other:_ "Error executing action "Submit Entity Indicators". Reason: {0}''.format(error.Stacktrace)_If the 403 status code is reported for all entities:_ "Error executing action "Submit Entity Indicators". Reason: none of the indicators were created due to instance permissions, please check the configuration.''. | General  
  
### Unisolate Machine

Unisolate a machine that was previously isolated using Microsoft Defender for Endpoint.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Comment | String | N/A | Yes | Specify a comment for why the machine needs to be unisolated.  
Create an Insight? | Checkbox | Checked |  | If enabled, the action creates a Google SecOps Insight with related information if executed successfully.  
  
#### Use cases

The action can be used for situations where the machine was already isolated, but with the new data gathered during playbook processing (for example, first machine was isolated, next we created a threat indicator for a suspicious file, and ran the "Stop and Quarantine" action to remove this file from the affected machine) we can consider it safe to remove the affected machine from isolation.

#### Run on

This action runs on the following entities:

  * Host
  * IP Address



#### Action results

##### Script result

True if the API Endpoint returned for **every** provided entity it ran on, **status 201** , in JSON Response "status": "Pending", which indicates that the API request executed successfully. If at least for one of the entities the action fails, the final result should be fail (False).

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#MachineActions/$entity",
        "id": "example-id",
        "type": "Unisolate",
        "requestor": "requestor-id",
        "requestorComment": "Unisolate machine due to the following remediation measures taken...",
        "status": "Pending",
        "machineId": "machine-id",
        "creationDateTimeUtc": "2019-11-21T03:59:34.7389352Z",
        "lastUpdateDateTimeUtc": "2019-11-21T03:59:34.7389352Z",
        "cancellationRequestor": null,
        "cancellationComment": null,
        "cancellationDateTimeUtc": null,
        "errorHResult": 0,
        "scope": null,
        "relatedFileInfo": null
    }
    

##### Insights

  * **Type:** Entity
  * **Title:** entity.
  * **IdentifierMessage:** Microsoft Defender for Endpoint isolation was removed.



### Update Alert

Update a specific Microsoft Defender for Endpoint Alert. The action can be used to close an alert in Microsoft Defender for Endpoint.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Alert ID | String | N/A | Yes | Specify the Microsoft Defender for Endpoint Alert ID to update.  
Status | DDL | NewPossible Values:

  * New
  * InProgress
  * Resolved

| No | Specify the status of the alert to update to.  
Assigned To | String | N/A | No | Specify the user info if you want to update this field.  
Classification | DDL | UnknownPossible Values:

  * Unknown
  * FalsePositive
  * TruePositive

| No | Specify the classification to update the alert with.  
Determination | DDL | NotAvailablePossible Values:

  * NotAvailable
  * Apt
  * Malware
  * SecurityPersonnel
  * SecurityTesting
  * UnwantedSoftware
  * Other

| No | Specify the determination to update the alert with.  
  
#### Use cases

  * Use the action to update a Defender ATP warning.

  * Use the action to intervene in a workflow involving Defender ATP warning analysis.

After the alert has been processed in Google SecOps, you can ignore the Defender ATP alert to keep the Defender ATP and Google SecOps alert lists aligned. Also, you can change the alert to show the progress of the alert analysis (for example, set the `assignedTo` attribute or set the alert status to `inProgress`).




#### Run on

This action runs on all entities.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "@odata.context": "https://api.securitycenter.windows.com/api/$metadata#Alerts/$entity",
        "id": "example-id",
        "incidentId": 1,
        "investigationId": null,
        "assignedTo": null,
        "severity": "Informational",
        "status": "Resolved",
        "classification": null,
        "determination": null,
        "investigationState": "UnsupportedAlertType",
        "detectionSource": "WindowsDefenderAtp",
        "category": "Execution",
        "threatFamilyName": null,
        "title": "[Test Alert] Suspicious Powershell commandline",
        "description": "*** This is a test alert ***\nA suspicious Powershell commandline was found on the machine. This commandline might be used during installation, exploration, or in some cases with lateral movement activities which are used by attackers to invoke modules, download external payloads, and get more information about the system. Attackers usually use Powershell to bypass security protection mechanisms by executing their payload in memory without touching the disk and leaving any trace.",
        "alertCreationTime": "2019-11-18T11:17:48.287421Z",
        "firstEventTime": "2019-11-18T11:15:06.5226815Z",
        "lastEventTime": "2019-11-18T11:15:06.5226815Z",
        "lastUpdateTime": "2019-11-20T04:12:03.6066667Z",
        "resolvedTime": "2019-11-20T04:12:03.4976288Z",
        "machineId": "machine-id",
        "alertUser": {
            "accountName": "Administrator",
            "domainName": "example-domain"
        },
        "comments": [],
        "alertFiles": [
            {
                "sha1": "3ce71813199abae99348f61f0caa34e2574f831c",
                "sha256": "9a7c58bd98d70631aa1473f7b57b426db367d72429a5455b433a05ee251f3236",
                "filePath": "C:\\Windows\\System32\\cmd.exe",
                "fileName": "cmd.exe"
            },
            {
                "sha1": "1b3b40fbc889fd4c645cc12c85d0805ac36ba254",
                "sha256": "d3f8fade829d2b7bd596c4504a6dae5c034e789b6a3defbe013bda7d14466677",
                "filePath": "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe",
                "fileName": "powershell.exe"
            }
        ],
        "alertDomains": [],
        "alertIps": [],
        "alertProcesses": []
    }
    

### Wait for Task Status

Wait for the status of a task.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Task IDs | String | N/A | Yes | Task IDs list as a comma-separated string.  
  
#### Run on

This action runs on all entities.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    [
        {
            "status": "Succeeded",
            "creation_date_time_utc": "2020-02-08T03:24:52.8526634Z",
            "cancellation_requestor": null,
            "cancellation_date_time_utc": null,
            "id": "2e39d22e-60a7-4267-899c-a1471e800000",
            "last_update_date_time_utc": "2020-02-08T03:25:35.8345081Z",
            "related_file_info": null,
            "cancellation_comment": null,
            "requestor": "e4fc6454-754d-47f7-bbdb-045fad600000",
            "error_h_result": 0,
            "scope": "Selective",
            "machine_id": "fbc85cf3fbcc8bb14d1a84fcf7bbae4531f00000",
            "type": "Isolate",
            "requestor_comment": "test"
        }
    ]
    

## Connectors

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

To configure the selected connector use the connector-specific parameters listed in the following tables:

  * Microsoft Defender ATP Connector configuration parameters
  * Microsoft Defender ATP Connector v2 configuration parameters



### Microsoft Defender ATP Connector

**Important:** This connector will be fully deprecated on March 30, 2027. Until then, support is limited to critical bug fixes for ingestion issues; no new feature updates will be provided. Use the [Microsoft 365 Defender – Incidents Connector](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-365-defender#microsoft_365_defender_incidents_connector) instead. Note that migrating may require changes to your playbooks.

The Defender ATP SIEM API used in the Microsoft Defender ATP Connector for events is deprecated as of March 1, 2022.

The connector periodically connects to the Defender ATP API endpoint and pulls a list of alerts generated for a specific time period. For the alerts processed, the connector in a separate request pulls the information on the detections from the Defender ATP. Detections have an `AlertId` field that can be used to associate the detections with specific alerts.

#### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | ProductName | Yes | Describes the name of the field where the product name is stored.  
Event Field Name | String | AlertName | Yes | Describes the name of the field where the event name is stored.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored.  If environment field isn't found, environment is "".  
Environment Regex Pattern | String | .* | No | A regular expression pattern to run on the value found in the `Environment Field Name` field. Default is .* to catch all and return value unchanged. Used to allow the user to manipulate the environment field using the regular expression logic. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is "".  
API Root | String | https://api.securitycenter.windows.com | Yes | API root URL to use with integration.  For better performance, you can use a server closest to your location:

  * api-us.securitycenter.windows.com
  * api-eu.securitycenter.windows.com
  * api-uk.securitycenter.windows.com

  
Azure Active Directory ID | String | N/A | Yes | Microsoft Entra Tenant ID, can be viewed in Active Directory > App Registration > Your application > Directory (tenant) ID.  
Integration Client ID | String | N/A | Yes | Client (Application) ID that is added for app registration in Microsoft Entra for the integration.  
Integration Client Secret | Password | N/A | Yes | Secret that is entered for Azure AD app registration for the integration.  
SIEM Client ID | String | N/A | Yes | Client (Application) ID for the enabled SIEM integration in Microsoft Defender for Endpoint.  
SIEM Client Secret | Password | N/A | Yes | Secret for the enabled SIEM integration in Microsoft Defender for Endpoint.  
Offset Time In Hours | Integer | 24 | Yes | Fetch alerts from X hours backwards.  
Max Alerts Per Cycle | Integer | 100 | Yes | Number of alerts that are processed during one connector run.  
Alert Statuses to fetch | String | Unknown, New, InProgress, Resolved | Yes | Specify the statuses of the Defender ATP alerts that should be fetched by the Google SecOps server. Parameter can take multiple values as a comma-separated string.  
Alert Severities to fetch | String | UnSpecified, Informational, Low, Medium, High | Yes | Specify the severities of the Defender ATP alerts that should be fetched by the Google SecOps server. Parameter can take multiple values as a comma-separated string.  
Proxy Server Address | IP_OR_HOST | N/A | No | Proxy server to use for connection.  
Proxy Server Username | String | N/A | No | Proxy server username.  
Proxy Server Password | Password | N/A | No | Proxy server password.  
  
#### Connector rules

  * The connector doesn't support blocklist or dynamic list rules.

  * The connector supports proxies.




### Microsoft Defender ATP Connector V2

**Important:** This connector will be fully deprecated on March 30, 2027. Until then, support is limited to critical bug fixes for ingestion issues; no new feature updates will be provided. Use the [Microsoft 365 Defender – Incidents Connector](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-365-defender#microsoft_365_defender_incidents_connector) instead. Note that migrating may require changes to your playbooks.

Fetch the Defender ATP alerts using the 365 Defender incident API to get the event data. Use the connector dynamic list to ingest only specific types of alerts based on the alert `detectionSource` attribute value.

The connector `SourceGroupIdentifier` attribute can be used to group alerts based on the Defender ATP incident ID.

#### Prerequisites

Before configuring the connector, make sure to grant additional permissions to your Microsoft Entra application:

  1. Sign in to the [Azure portal](https://portal.azure.com/) as a user administrator or a password administrator.

  2. Select **Microsoft Entra ID**.

  3. Go to **API Permissions > Add a permission > APIs my organization uses**.

  4. Select **Microsoft Threat Protection > Application permissions**.

  5. In the **Select Permissions** section, select the following required permissions:

     * `Incident.Read.All`
     * `Incident.ReadWrite.All`
  6. Click **Add permissions**.

  7. Click **Grant admin consent for` YOUR_ORGANIZATION_NAME`**.




#### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | :: | Yes | Describes the name of the field where the product name is stored.  
Event Field Name | String | EventName | Yes | Describes the name of the field where the event name is stored.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If environment field isn't found, environment is "".  
Environment Regex Pattern | String | .* | No | A regular expression pattern to run on the value found in the `Environment Field Name` field. Default is .* to catch all and return value unchanged. Used to allow the user to manipulate the environment field using the regular expression logic. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is "".  
Defender ATP API Root | String | https://api.securitycenter.windows.com | Yes | API root URL to use with integration For better performance, you can use a server closest to your location:

  * api-us.securitycenter.windows.com
  * api-eu.securitycenter.windows.com
  * api-uk.securitycenter.windows.com

  
365 Defender API Root | String | https://api.security.microsoft.com | Yes | API root of the Microsoft 365 Defender instance used to get the Google SecOps events data.  
Azure Active Directory ID | String | N/A | Yes | Microsoft Entra Tenant ID that can be found in Microsoft Entra > App Registration > Your application > Directory (tenant) ID.  
Integration Client ID | String | N/A | Yes | Client (Application) ID that is added for app registration in Microsoft Entra for the integration.  
Integration Client Secret | Password | N/A | Yes | Secret that is entered for Azure AD app registration for the integration.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Microsoft 365 Defender server is valid.  
Offset Time In Hours | Integer | 24 | Yes | Fetch alerts from X hours backwards.  
Max Alerts Per Cycle | Integer | 10 | Yes | Number of alerts that are processed during one connector run.  
Alert Statuses to fetch | String | Unknown, New, InProgress, Resolved | Yes | Specify the statuses of the Defender ATP alerts that should be fetched by the Google SecOps server. Parameter can take multiple values as a comma-separated string.  
Alert Severities to fetch | String | UnSpecified, Informational, Low, Medium, High | Yes | Specify the severities of the Defender ATP alerts that should be fetched by the Google SecOps server. Parameter can take multiple values as a comma-separated string.  
Disable Overflow | Checkbox | Unchecked | No | If enabled, the connector ignores the overflow mechanism.  
Script Timeout | Integer | 300 | Yes | Specify the timeout for connector to run.  
Use whitelist as a blacklist | Checkbox | Unchecked | No | If enabled, dynamic list is used as a blocklist.  
Proxy Server Address | IP_OR_HOST | N/A | No | Proxy server to use for connection.  
Proxy Server Username | String | N/A | No | Proxy server username.  
Proxy Server Password | Password | N/A | No | Proxy server password.  
  
#### Connector rules

The connector supports a dynamic list logic based on the `detectionSource` Defender ATP alert field value.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
