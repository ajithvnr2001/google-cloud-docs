---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/attivo/
title: Integrate Attivo with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:38:21.012772+00:00
---

# Integrate Attivo with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/attivo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Attivo with Google SecOps 

This document describes how to integrate Attivo with Google Security Operations (Google SecOps).

**Important:** Attivo Networks was acquired by SentinelOne and became part of SentinelOne Singularity XD.

## Integration parameters

Use the following parameters to configure the integration:

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
API Root | String | https:/{{ip address}} | Yes | API root of the Attivo instance.  
Username | String | N/A | Yes | Attivo API Username.  
Password | Password | N/A | Yes | Attivo API Password.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Attivo server is valid.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Ping

Test the connectivity to Attivo.

#### Parameters

N/A

#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | _If successful:_ Successfully connected to the Attivo server with the provided connection parameters! _If not successful:_ Failed to connect to the Attivo server! Error: {0}".format(exception.stacktrace) | General  
  
### Enrich Entities

Enrich entities using information from Attivo. Supported entities: Hostname, IP Address.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Include ThreatPaths | Checkbox | Checked | No | If enabled, the action returns information about ThreatPaths related to the entity.  
Include Vulnerabilities | Checkbox | Checked | No | If enabled, the action returns information about vulnerabilities related to the entity.  
Include Credential Info | Checkbox | Checked | No | If enabled, the action returns information about credential information related to the entity.  
Create Insight | Checkbox | Checked | No | If enabled, the action creates an insight containing all of the retrieved information about the entity.  
Max ThreatPaths To Return | Integration | 50 | No | Specify the number of ThreatPaths to return per entity.  
Max Vulnerabilities To Return | Integration | 50 | No | Specify the number of vulnerabilities to return per entity.  
Max Credentials To Return | Integration | 50 | No | Specify the number of credentials to return per entity.  
  
#### Run on

This action runs on the Hostname and IP Address entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON result
    
    
    {
        "upgradeToVersion": null,
        "quarantineStatus": 0,
        "acmId": -1,
        "tostatus": 0,
        "systemtype": "VM",
        "adsErrorMessage": "",
        "accessprotection": false,
        "functionalId": {
            "templateName": null,
            "usersid": null,
            "errorCode": 0,
            "debugInfo": "",
            "userName": "example\\Administrator",
            "status": null,
            "timestamp": 1636558715000
        },
        "ondAssigned": false,
        "usersInfo": [
            {
                "templateName": "Default_ThreatStrike_Profile:2",
                "usersid": "S-1-5-21-2143737273-3756110848-2070699859-500",
                "errorCode": 0,
                "debugInfo": "Error:0 lsass UnInstallation\\nError:0 webftp UnInstallation\\nError:0 cookies UnInstallation\\nError:0 mstsc UnInstallation\\nError:0 SMB UnInstallation\\nError:0 Web Credential UnInstallation\\nError:0 outlook UnInstallation\\nError:0 iexplorer UnInstallation\\nError:0 Putty UnInstallation\\nError:0 Mozilla UnInstallation\\nError:0 Chrome UnInstallation\\nError:0 FileZilla UnInstallation\\nError:0 lsass UnInstallation\\nError:0 AWS UnInstallation\\nError:0 Telnet UnInstallation\\nError:0 OracleDBClient UnInstallation\\nError:0 IEFavorite UnInstallation\\nError:0 WindowsDNS UnInstallation\\nError:0 RasVPN UnInstallation",
                "userName": "exlab.local\\Administrator",
                "status": "INSTALLED",
                "timestamp": 1636558727000
            }
        ],
        "id": 101,
        "epVersion": "5.0.1.25",
        "activeDirectory": {
            "groups": [
                "Domain Computers"
            ],
            "organizationalUnit": "Computers"
        },
        "installMode": 2,
        "processor_arch": " 64-bit",
        "tdDeflectMessage": "",
        "clientGroupId": "ThreatStrike-Default-Client",
        "deployMode": 0,
        "latestExecutableStatus": "INSTALLED",
        "subscriberId": 1,
        "botsinkDocumentId": 0,
        "executableStatus": [
            {
                "timestamp": 1636558715000,
                "status": "INSTALLED"
            }
        ],
        "processor_cpuSpeed": "2300 MHz",
        "guid": "27f018b6-47c8-4b20-ab62-545c672ddf7cexample",
        "ondMessage": "",
        "debugCollect": false,
        "ondInActive": false,
        "adsstatus": 1,
        "upgradeRequired": false,
        "ondstatus": 0,
        "hostName": "example",
        "memory": "8190 MB",
        "lastModifiedTime": "2021-11-11T15:41:16.254Z",
        "arstatus": 1,
        "dnsName": "example.example",
        "botsinkDeviceId": 0,
        "endpoint_os_type": 1,
        "disabledInClientGroup": false,
        "tddstatus": 1,
        "adsenabled": false,
        "tdDeflectStatus": 0,
        "osType": "Non-Server",
        "featuresstatusforusers": [
            {
                "tddstatus": 1,
                "tsstatus": 1,
                "tostatus": 0,
                "usersid": "user-id",
                "adsstatus": 1,
                "logIn": 1636558717,
                "ondstatus": 0,
                "logOut": 0,
                "tpstatus": 1,
                "live": true,
                "username": "example\\Administrator"
            }
        ],
        "interfaces": [
            {
                "subnet": "192.0.2.0/24",
                "score": 1400.133919820602,
                "macAddress": "01:23:45:AB:CD:EF",
                "ipAddress": "192.0.2.198",
                "name": "Intel(R) 82574L Gigabit Network Connection",
                "type": "Wired",
                "timestamp": 1636645218000
            }
        ],
        "migrateCL": false,
        "debugStatus": false,
        "osName": "Windows 10 64-bit",
        "uptime": "134836",
        "tsstatus": 1,
        "processor_numOfCpu": 4,
        "newClientGroup": null,
        "tpstatus": 1,
        "threatPaths": [
            {
                "destIp": "192.0.2.198",
                "permissionId": -1,
                "reason": null,
                "srcHostName": "Unmanaged host",
                "acmId": -1,
                "source": null,
                "type": "Paths",
                "permScore": "Medium",
                "cancellable": false,
                "targetScore": "Medium",
                "crRuleName": "System Default: Domain Admin Pilferage",
                "credOuPath": "CN=Users,DC=example,DC=example",
                "submissionId": -1,
                "credAcctStatus": "Enabled",
                "credential": "example\\administrator",
                "srcId": "dummy-endpoint-1SUB1"
            }
        ],
        "vulnerabilities": [
            "More than two Administrators were found on this computer",
            "Presence of local administrative privileges for domain user account"
        ],
        "credentials": [
            {
                "isDeceptive": true,
                "service": "putty",
                "domain": "EXAMPLE-W10H66.example\\accessDBuser",
                "serverIp": "EXAMPLE-W10H66.example",
                "isShortcut": false
            },
            {
                "isDeceptive": true,
                "service": "putty",
                "domain": "EXAMPLE-W10H77.example\\accessDBadm",
                "serverIp": "EXAMPLE-W10H77.example",
                "isShortcut": false
            }
        ]
    }
    

##### Enrichment Table

Enrichment field name | Logic - When to apply  
---|---  
os | When available in JSON  
ip | When available in JSON  
mac | When available in JSON  
hostname | When available in JSON  
users | When available in JSON  
type | When available in JSON  
uptime | When available in JSON  
num_threatpaths | When available in JSON  
num_vulnerabilities | When available in JSON  
num_deceptive_creds | When available in JSON  
num_real_creds | When available in JSON  
  
##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** >_If data is available for one entity (is_success=true):_ "Successfully enriched the following entities using information from Attivo: {entity.identifier}". _If data is not available for one entity (is_success=true):_ "Action wasn't able to enrich the following entities using information from Attivo: {entity.identifier}". _If data is not available for all entities (is_success=false):_ "None of the provided entities were enriched." **The action should fail and stop a playbook execution:** >_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Title:** {entity.identifier} **Table Columns:**

  * Key
  * Value

| Entity  
Case Wall Table (If vulnerabilities are available) | **Table Name:** {entity identifier} Vulnerabilities **Table Column:** Name | General  
Case Wall Table(If threatpaths are available) | **Table Name:** {entity identifier} ThreatPaths **Table Columns:**

  * Dest IP
  * Src Ip 
  * Src Host
  * Dest Host
  * Name
  * Credential
  * Description
  * Critical
  * Severity
  * Service
  * Category

| General  
Case Wall Table (If credentials are available) | **Table Name:** {entity identifier} Credentials **Table Columns:**

  * Deceptive
  * Service 
  * Domain
  * Server IP
  * Shortcut

| General  
  
### List Critical ThreatPath

List available critical threat paths in Attivo.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Filter Key | DDL | Select One Possible Values:

  * Rule Name
  * Service
  * Severity
  * Description
  * Category

| No | Specify the key that needs to be used to filter critical paths.  
Filter Logic | DDL | Not Specified Possible Values:

  * Not Specified
  * Equal
  * Contains

| No | Specify the filter logic that should be applied. Filtering logic works based on the value provided in the "Filter Key" parameter.  
Filter Value | N/a | N/A | No | Specify the value that should be used in the filter. If "Equal" is selected, the action tries to find the exact match among results. If "Contains" is selected, the action tries to find results that contain the provided substring. If nothing is provided in this parameter, the filter is not applied. Filtering logic works based on the value provided in the "Filter Key" parameter.  
Max Records To Return | Integrations | 50 | No | Specify the number of records to return. If nothing is provided, action will return 50 records.  
  
#### Runs on

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "criticalPaths": [
            {
                "destIp": "192.0.2.198",
                "permissionId": -1,
                "reason": null,
                "srcHostName": "Unmanaged host",
                "acmId": -1,
                "source": null,
                "type": "Paths",
                "permScore": "Medium",
                "cancellable": false,
                "targetScore": "Medium",
                "crRuleName": "System Default: Domain Admin Pilferage",
                "credOuPath": "CN=Users,DC=example",
                "submissionId": -1,
                "credAcctStatus": "Enabled",
                "credential": "example\\administrator",
                "srcId": "example-endpoint-1SUB1",
                "destHostName": "example",
                "cid2": "rdp1",
                "id": "Unmanaged host192.0.2.5example192.0.2.198RDP Memory Credentialexample\\administratorPaths",
                "srcIp": "192.0.2.5",
                "firstSeen": 1636667535105,
                "credDept": null,
                "subscriberId": 1,
                "remediable": false,
                "credLastPswResetTime": 1620201383000,
                "credLastLogonTime": 1636729127000,
                "moretarget": false,
                "destId": "27f018b6-47c8-4b20-ab62-545c672ddf7cHOST02SMIME:S-1-5-21-2143737273-3756110848-2070699859-500",
                "shareName": null,
                "desc": "rdp Active logon session for exlab.local\\administrator at Unmanaged OU/192.0.2.5 (unmanaged host). Potential movement to Computers/HOST02SMIME.",
                "cid": "rdp0",
                "permissionName": "",
                "destOu": "Computers",
                "critical": true,
                "isgrouppath": false,
                "credUpn": "Administrator@example.com",
                "credCreatedTime": 1610374114000,
                "memberList": null,
                "memberOf": null,
                "remediateStatus": null,
                "severity": "High",
                "srcOu": "Unmanaged",
                "target": "example(192.0.2.198)",
                "loggedOn": false,
                "credSamAcctName": "Administrator",
                "service": "RDP Memory Credential",
                "credDisplayName": null,
                "ukey": null,
                "category": "Saved credential"
            }
        ]
    }
    

##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available (is_success=true):_ "Successfully found critical ThreatPaths for the provided criteria in Attivo". _If data is not available (is_success=false):_ "No ThreatPaths were found for the provided criteria in Attivo" _If the "Filter Value" parameter is empty (is_success=true):_ The filter was not applied, because parameter "Filter Value" has an empty value. **The action should fail and stop a playbook execution:** _If the "Filter Key" parameter is set to "Select One" and the "Filter Logic" parameter is set to "Equal" or "Contains":_ "Error executing action "{action name}". Reason: you need to select a field from the "Filter Key" parameter." _If an invalid value is provided for the "Max Records to Return" parameter:_ "Error executing action "{action name}". Reason: "Invalid value was provided for "Max Records to Return": . Positive number should be provided"." _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "{action name}". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** {entity identifier} ThreatPaths **Table Columns:**

  * Dest IP
  * Src Ip
  * Src Host
  * Dest Host
  * Name
  * Credential
  * Description
  * Critical
  * Severity
  * Service
  * Category

| Entity  
  
### List Vulnerability Hosts

List hosts related to the vulnerability in Attivo.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Vulnerabilities | CSV | N/A | Yes | Specify a comma-separated list of vulnerabilities for which action needs to return hostnames.  
Max Hosts To Return | Integer | 50 | No | Specify the number of hosts to return. If nothing is provided, action will return 50 hosts.  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON result
    
    
    [
        {
            "vulnerability": "Presence of local administrative privileges for domain user account",
            "hostNames": [
                "EXAMPLE"
            ]
        }
    ]
    

##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available for one vulnerability (is_success=true):_ "Successfully retrieved hosts for the following vulnerabilities: {vulnerabilities}". _If no hosts are related for one vulnerability (is_success=true):_ "No hosts were found for the following vulnerabilities: {vulnerabilities}" _If no hosts are related for all vulnerabilities (is_success=false)_ : "No hosts were found for the provided vulnerabilities." _If the response is "{}" for one vulnerability (is_success=true):_ "Action wasn't able to retrieve information about hosts for the following vulnerabilities: {vulnerabilities}" _If the response is "{}" for one vulnerabilities (is_success=false):_ "Action wasn't able to retrieve information about hosts for the provided vulnerabilities." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "{action name}". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** {Vulnerability Name i} **Table Columns:** Name | Entity  
  
### List Service ThreatPaths

List ThreatPaths related to services in Attivo.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Services | CSV | N/A | Yes | Specify a comma-separated list of services for which action needs to return ThreatPaths  
Max ThreatPaths To Return | Integer | 50 | No | Specify the number of threat paths to return. If nothing is provided, the action returns 50 ThreatPaths.  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON result
    
    
    [
        {
            "service": "Web",
            "paths": [
                "EXAMPLE"
            ]
        }
    ]
    

##### Case wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available (is_success=true):_ "Successfully retrieved ThreatPaths for the following services in Attivo: {services}. _If no data is available for one service:_ "No ThreatPaths were found for the following services in Attivo: {services}. _If no data available for all services:_ "No ThreatPaths were found for the provided services in Attivo. **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "{action name}". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** {entity identifier} ThreatPaths **Table Columns:**

  * Dest IP
  * Src Ip
  * Src Host
  * Dest Host
  * Name
  * Credential
  * Description
  * Severity 
  * Service
<
  * Category

| Entity  
  
### Update Event

Update event in Attivo.

**Note:** The API of Attivo returns successful status, even if invalid event ID is provided.

#### Parameters

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Event ID | String | N/A | Yes | Specify the ID of the event, which needs to be updated.  
Status | DDL | Select One Possible Values:

  * Acknowledge
  * Unacknowledge

| No | Specify the status for the event.  
Comment | String | N/A | No | Specify a comment that needs to be added to the event.  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### Case Wall

Result type | Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If the 200 status code is reported (is_success=true):_ "Successfully updated the event with ID "{event_id}" in Attivo.". **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Update Event". Reason: {0}''.format(error.Stacktrace) _If "Select One" is selected and the "Comment" is not provided:_ "Error executing action "Update Event". Reason: at least one of the parameters "Status" or "Comment" should have a value.'' | General  
  
## Connector

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### Attivo - Events Connector

Pull events from Attivo into Google SecOps.

The dynamic list works with the `attackName` parameter.

##### Connector parameters

Use the following parameters to configure the connector:

Parameter name | Type | Default value | Is mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes |  The name of the field where the product name is stored. The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default. The default value is `Product Name`.  
Event Field Name | String | attackName | Yes | The name of the field that determines the event name (subtype).  
Environment Field Name | String | "" | No | The name of the field where the environment name is stored.If the environment field is missing, the connector uses the default value.  
`Environment Regex Pattern` | String | .* | No |  A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | The timeout limit, in seconds, for the Python process that runs the current script.  
API Root | String | https://IP_ADDRESS | Yes | API root of the Attivo instance.  
Username | String | N/A | Yes | Attivo API Username.  
Password | Password | N/A |  | Attivo API Password.  
Status Filter | String | All | Yes | Status filter for the connector. Possible values: unacknowledged, acknowledged, all.  
Lowest Severity To Fetch | String | Medium | No | Severity level to use for fetching events. If none is specified, the action will ingest all events. Possible values: `System Activity`, `Very Low`, `Low`, `Medium`, `High`, `Very High`.  
Max Hours Backwards | Integer | 1 | No | The number of hours before the first connector iteration to retrieve the events. This parameter can apply to the initial connector iteration after you enable the connector for the first time, or the fallback value for an expired connector timestamp.  
Max Events To Fetch | Integer | 100 | No | How many events to process per one connector iteration. Maximum is 1000.  
`Use whitelist as a blacklist` | Checkbox | Unchecked | Yes | If selected, the connector uses the dynamic list as a blocklist.  
Verify SSL | Checkbox | Checked | Yes | If selected, the integration validates the SSL certificate when connecting to the Attivo server.  
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
