---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/rsa-netwitness-platform/
title: RSA NetWitness Platform \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:41.387665+00:00
---

# RSA NetWitness Platform  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/rsa-netwitness-platform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# RSA NetWitness Platform

This document provides guidance on how to integrate RSA NetWitness Platform with Google SecOps.

## Configure RSA NetWitness Platform integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Broker API Root | String | http://x.x.x.x:50103 | No | API Root of the Broker API.  
Broker API Username | String | N/A | No | Username for the Broker API.  
Broker API Password | Password | N/A | No | Password for the Broker API.  
Concentrator API Root | String | http://x.x.x.x:50105 | No | API Root of the Concentrator API.  
Concentrator API Username | String | N/A | No | Username for the Concentrator API.  
Concentrator API Password | Password | N/A | No | Password for the Concentrator API.  
Web API Root | String | https://{ip}/rest/api/ | No | API Root of the Netwitness Platform Instance.  
Web Username | String | N/A | No | Username for the Netwitness Platform Instance.  
Web Password | Password | N/A | No | Password for the Netwitness Platform Instance.  
Verify SSL | Checkbox | Unchecked | No | If enabled, verifies that the SSL certificate for the connection to the RSA Netwitness Platform server is valid.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to RSA Netwitness Platform.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action is doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### Enrich Endpoint

#### Description

Fetch endpoint's system information by its hostname or IP address. Requires RSA Netwitness Respond license, endpoint server service running in the background, configured Web Username and Web Password in the integration configuration.

#### Parameters

Parameter Display Name | Type | Default Value | Is **M** andatory | Description  
---|---|---|---|---  
Risk Score Threshold | Integer | 50 | False | Specify risk threshold for the endpoint. If the endpoint exceeds the threshold, the related entity will be marked as suspicious. If nothing is specified, action won't check the risk score.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Host



#### Action Results

##### Entity Enrichment

Enrichment Field Name | Source (JSON Key) | Logic - When to apply  
---|---|---  
RSA_NTW_agentId | agentId | When available in JSON  
RSA_NTW_hostName | hostName | When available in JSON  
RSA_NTW_riskScore | riskScore | When available in JSON  
RSA_NTW_networkInterfaces_{id}_name | networkInterfaces/name | When available in JSON  
RSA_NTW_networkInterfaces_{id}_macAddress | networkInterfaces/macAddress | When available in JSON  
RSA_NTW_networkInterfaces_{id}_ipv4 | Space separated list networkInterfaces/ipv4 | When available in JSON  
RSA_NTW_networkInterfaces_{id}_ipv6 | Space separated list networkInterfaces/ipv6 | When available in JSON  
RSA_NTW_networkInterfaces_{id}_networkIdv6 | Space separated list networkInterfaces/networkIdv6 | When available in JSON  
RSA_NTW_networkInterfaces_{id}_gateway | Space separated list networkInterfaces/gateway | When available in JSON  
RSA_NTW_networkInterfaces_{id}_dns | Space separated list networkInterfaces/dns | When available in JSON  
RSA_NTW_networkInterfaces_{id}_promiscuous | networkInterfaces/promiscuous | When available in JSON  
RSA_NTW_lastSeenTime | lastSeenTime | When available in JSON  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "items": [
            {
                "agentId": "575EDC44-BDF9-6D00-FFCD-D354FB641E27",
                "hostName": "RSA-HOST-1",
                "riskScore": 100,
                "networkInterfaces": [
                    {
                        "name": "Intel(R) 82574L Gigabit Network Connection",
                        "macAddress": "00:50:56:A2:30:03",
                        "ipv4": [
                            "172.30.203.145"
                        ],
                        "ipv6": [
                            "fe80::dce6:5825:454a:968d"
                        ],
                        "networkIdv6": [
                            "fe80::"
                        ],
                        "gateway": [
                            "172.30.203.1"
                        ],
                        "dns": [
                            "8.8.8.8"
                        ],
                        "promiscuous": false
                    }
                ],
                "lastSeenTime": "2020-08-23T12:32:33.107Z"
            }
        ],
        "pageNumber": 0,
        "pageSize": 100,
        "totalPages": 1,
        "totalItems": 1,
        "hasNext": false,
        "hasPrevious": false
    }
    

##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If successful and at least one of the provided entities were enriched (is_success = true):_ Print "Successfully enriched the following endpoints from RSA Netwitness: \n {0}".format(entity.identifier list)  
****_If fail to enrich specific entities(is_success = true):_ Print "Action was not able to enrich the following endpoints from RSA Netwitness \n: {0}".format([entity.identifier])****_If fail to enrich for all entities (is_success = false):_ Print: "No entities were enriched."******The action should fail and stop a playbook execution:**  
****_If fatal error, like wrong credentials, no connection to server, other:_ Print "Error executing action "Enrich Endpoint". Reason: {0}''.format(error.Stacktrace)_If endpoint service was not found:_ Print "Error executing action "Enrich Endpoint". Reason: Endpoint server wasn't found." | General  
  
### Enrich File

#### Description

Fetch information about the file using hashes or file names. Only MD5 and SHA256 are supported. Requires RSA Netwitness Respond license, endpoint server service running in the background, configured Web Username and Web Password in the integration configuration.

#### Parameters

Parameter Display Name | Type | Default Value | Is **M** andatory | Description  
---|---|---|---|---  
Risk Score Threshold | Integer | 50 | No | Specify risk threshold for the file. If the file exceeds the threshold, the related entity will be marked as suspicious. If nothing is specified, action won't check the risk score.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Source (JSON Key) | Logic - When to apply  
---|---|---  
RSA_NTW_filename | firstFileName | When available in JSON  
RSA_NTW_reputationStatus | reputationStatus | When available in JSON  
RSA_NTW_globalRiskScore | globalRiskScore | When available in JSON  
RSA_NTW_machineOsType | machineOsType | When available in JSON  
RSA_NTW_size | size | When available in JSON  
RSA_NTW_checksumMd5 | checksumMd5 | When available in JSON  
RSA_NTW_checksumSha1 | checksumSha1 | When available in JSON  
RSA_NTW_checksumSha256 | checksumSha256 | When available in JSON  
RSA_NTW_entropy | entropy | When available in JSON  
RSA_NTW_format | pe | When available in JSON  
RSA_NTW_fileStatus | Neutral | When available in JSON  
RSA_NTW_remediationAction | Unblock | When available in JSON  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "items": [
            {
                "firstFileName": "AM_Delta_Patch_1.321.1947.0.exe",
                "reputationStatus": "Known Good",
                "globalRiskScore": 0,
                "firstSeenTime": "2020-08-23T00:46:25.288Z",
                "machineOsType": "windows",
                "signature": {
                    "timeStamp": "2020-08-22T21:01:55.552Z",
                    "thumbprint": "c6573d9ba5efc55b1ad1c59b9cafc33d232b13cc",
                    "context": [
                        "microsoft",
                        "signed",
                        "valid"
                    ],
                    "signer": "Microsoft Corporation"
                },
                "size": 441280,
                "checksumMd5": "40d93a5ed9d2d55e35857c1f1de162db",
                "checksumSha1": "3096e9e4ac4cc46dcfa11a053583c2d3e14b14b8",
                "checksumSha256": "34261adf58ac3c8e38724d5fbfba21037d868a2c0b6291e2a61e5a023b55c3f9",
                "pe": {
                    "timeStamp": "2020-08-22T20:57:28.000Z",
                    "imageSize": 454656,
                    "numberOfExportedFunctions": 0,
                    "numberOfNamesExported": 0,
                    "numberOfExecuteWriteSections": 0,
                    "context": [
                        "file.exe",
                        "file.arch64",
                        "file.versionInfoPresent",
                        "file.resourceDirectoryPresent",
                        "file.relocationDirectoryPresent",
                        "file.debugDirectoryPresent",
                        "file.tlsDirectoryPresent",
                        "file.richSignaturePresent",
                        "file.companyNameContainsText",
                        "file.descriptionContainsText",
                        "file.versionContainsText",
                        "file.internalNameContainsText",
                        "file.legalCopyrightContainsText",
                        "file.originalFilenameContainsText",
                        "file.productNameContainsText",
                        "file.productVersionContainsText",
                        "file.standardVersionMetaPresent"
                    ],
                    "resources": {
                        "originalFileName": "AM_Delta_Patch_1.321.1947.0.exe",
                        "company": "Microsoft Corporation",
                        "description": "Microsoft Antimalware WU Stub",
                        "version": null
                    },
                    "sectionNames": [
                        ".text",
                        ".rdata",
                        ".data",
                        ".pdata",
                        ".rsrc",
                        ".reloc"
                    ],
                    "importedLibraries": [
                        "ADVAPI32.dll",
                        "KERNEL32.dll",
                        "RPCRT4.dll",
                        "ntdll.dll"
                    ]
                },
                "elf": null,
                "macho": null,
                "entropy": 7.378079119412321,
                "format": "pe",
                "fileStatus": "Neutral",
                "remediationAction": "Unblock"
            }
        ],
        "pageNumber": 0,
        "pageSize": 100,
        "totalPages": 1,
        "totalItems": 1,
        "hasNext": false,
        "hasPrevious": false
    }
    

##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If successful and at least one of the provided entities were enriched (is_success = true):_  
****Print "Successfully enriched the following files from RSA Netwitness: \n {0}".format(entity.identifier list)****_If fail to enrich specific entities(is_success = true):_  
****Print "Action was not able to enrich the following files from RSA Netwitness \n: {0}".format([entity.identifier])****_If fail to enrich for all entities (is_success = false):_  
****Print: "No entities were enriched."  
******The action should fail and stop a playbook execution:**_If_ ****_fatal error, like wrong credentials, no connection to server, other:_ Print "Error executing action "Enrich File". Reason: {0}''.format(error.Stacktrace)__  
_If_ ****_fatal error, like wrong credentials, no connection to server, other:_ Print "Error executing action "Enrich File". Reason: Endpoint server wasn't found." | General  
  
### Isolate Endpoint

#### Description

Request endpoint isolation in RSA Netwitness. Requires RSA Netwitness Respond license, endpoint server service running in the background, configured Web Username and Web Password in the integration configuration.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Comment | String | N/A | Yes | Add comment, which describes the reason behind the isolation request.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Host



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If successful for all of the provided entities(is_success = true):_  
****Print "Successfully requested isolation for the following endpoints from RSA Netwitness: \n {0}".format(entity.identifier list)****_If fail to isolate at least one of the provided entities(is_success = false):_  
****Print "Action was not able to request isolation for the following endpoints from RSA Netwitness \n: {0}".format([entity.identifier])  
******The action should fail and stop a playbook execution:**_If_ ****_fatal error, like wrong credentials, no connection to server, other:_ Print "Error executing action "Isolate Endpoint". Reason: {0}''.format(error.Stacktrace)_If endpoint service was not found:_ Print "Error executing action "Isolate Endpoint". Reason: Endpoint server wasn't found." | General  
  
### Unisolate Endpoint

#### Description

Request endpoint unisolation in RSA Netwitness. Requires RSA Netwitness Respond license, endpoint server service running in the background, configured Web Username and Web Password in the integration configuration.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Comment | String | N/A | Yes | Add comment, which describes the reason behind the isolation request.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Host



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If successful for all of the provided entities(is_success = true):_  
****Print "Successfully requested unisolation for the following endpoints from RSA Netwitness: \n {0}".format(entity.identifier list)****_If fail to isolate at least one of the provided entities(is_success = false):_  
****Print "Action was not able to request unisolation for the following endpoints from RSA Netwitness \n: {0}".format([entity.identifier])  
******The action should fail and stop a playbook execution:**_If_ ****_fatal error, like wrong credentials, no connection to server, other:_ Print "Error executing action "Unisolate Endpoint". Reason: {0}''.format(error.Stacktrace)_If endpoint service was not found:_ Print "Error executing action "Unisolate Endpoint". Reason: Endpoint server wasn't found." | General  
  
### Update Incident

#### Description

Update Incident in RSA Netwitness. Requires RSA Netwitness Respond license, configured Web Username and Web Password in the integration configuration.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Incident ID | String | N/A | Yes | Specify ID of the incident that needs to be updated.  
Status | DDL | N/A | No | Specify new status for the incident.  
Assignee | String | N/A | No | Specify new assignee for the incident.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "id": "INC-128",
        "title": "High Risk Alerts: NetWitness Endpoint for RSA-HOST-1",
        "summary": "",
        "priority": "High",
        "riskScore": 72,
        "status": "RemediationRequested",
        "alertCount": 136,
        "averageAlertRiskScore": 72,
        "sealed": true,
        "totalRemediationTaskCount": 0,
        "openRemediationTaskCount": 0,
        "created": "2020-08-26T12:56:57.867Z",
        "lastUpdated": "2020-08-26T15:31:27.953Z",
        "lastUpdatedBy": null,
        "assignee": "admin",
        "sources": [
            "ECAT"
        ],
        "ruleId": "5ef1b33614c0552a2884c590",
        "firstAlertTime": "2020-08-26T12:56:56.097Z",
        "categories": [],
        "journalEntries": null,
        "createdBy": "High Risk Alerts: NetWitness Endpoint",
        "deletedAlertCount": 0,
        "eventCount": 136,
        "alertMeta": {
            "SourceIp": [
                ""
            ],
            "DestinationIp": [
                ""
            ]
        }
    }
    

##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If status code == 200 (is_success = true):_ Print "Successfully updated incident with ID {0} in RSA Netwitness".format(incident_id).  
****_If status code 400 (is_success=false):_ Print "Action wasn't able to update incident with ID {0} in RSA Netwitness. Reason: {1}".format(incident_id, errors/message).  
******The action should fail and stop a playbook execution:**_If fatal error, like wrong credentials, no connection to server, other:_ Print "Error executing action "Update Incident". Reason: {0}''.format(error.Stacktrace)  
| General  
  
### Add Note to Incident

#### Description

Add Note to Incident in RSA Netwitness. Requires RSA Netwitness Respond license, configured Web Username and Web Password in the integration configuration..

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Incident ID | String | N/A | Yes | Specify ID of the incident that needs to be updated.  
Note | String | N/A | Yes | Specify which note should be added to.  
Author | String | N/A | Yes | Specify the author of the note.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If status code == 200 (is_success = true):_ Print "Successfully added note to incident with ID {0} in RSA Netwitness".format(incident_id).  
****_If status code 400 (is_success=false):_ Print "Action wasn't able to add note to incident with ID {0} in RSA Netwitness. Reason: {1}".format(incident_id, errors/message).  
******The action should fail and stop a playbook execution:**_If fatal error, like wrong credentials, no connection to server, other:_ Print "Error executing action "Add Note to Incident". Reason: {0}''.format(error.Stacktrace)  
| General  
  
## Connector

### RSA Netwitness Platform - Incidents Connector

#### Description

Pull incidents from RSA Netwitness Platform.

#### How to work with Credential JSON Object

Credential JSON object provides a more flexible way of authenticating to the data sources. The most basic configuration of the JSON will look like this:
    
    
    {
        "default_username": "username",
        "default_password": "password"
    }
    

Without "default_username" and "default_password" connector will throw an error. This configuration is suitable for environments, where all data sources share the same username and password. If you need to provide specific credentials for the data sources then the structure of the JSON will look like this:
    
    
    {
        "default_username": "username",
        "default_password": "password",
        "dataSources": [
            {
                "api_root": "172.30.203.151:50102",
                "username": "username",
                "password": "password"
            },
            {
                "api_root": "172.30.203.151:50105",
                "username": "username",
                "password": "password"
            },
            {
                "api_root": "172.30.203.151:50103",
                "username": "username",
                "password": "password"
            }
        ]
    }
    

Connector will scan the events for the source api root and then compare it with what is available in the Credential JSON Object. If the match is found, then the connector will take the username + password from "dataSources" list, if there is no match, it will use "default_username" and default_password. Additionally, you don't need to provide both username and password in the "dataSources" list. If, for example, only username is provided, then the connector will take username from "dataSource" list and password from "default_password".

#### Configure RSA Netwitness Platform - Incidents Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | type | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
Web API Root | String | https://{ip}/rest/api/ | Yes | Web API Root of the RSA Netwitness Platform instance.  
Web Username | String | N/A | Yes | Username of the RSA Netwitness Platform account.  
Web Password | Password | N/A | Yes | Password of the RSA Netwitness Platform account.  
Fetch Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch incidents. Note: connector will wait for the provided time for the updates to incidents.  
Lowest Risk Score To Fetch | Integer | N/A | No | Lowest risk score of the incidents to fetch. By default, the connector will ingest all of the incidents.Maximum is 100.  
Severity Fallback | String | Informational | Yes | Specify what should be the fallback severity for the Google SecOps alert, when risk score is not available. Possible Values: Informational, Low, Medium, High, Critical.  
Max Incidents To Fetch | Integer | 10 | No | How many incidents to process per one connector iteration. Maximum is 100.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist will be used as a blacklist.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verify the SSL certificate for the connection to the RSA Netwitness Platform server is valid.  
Proxy Server Address | String |  | No | The address of the proxy server to use.  
Proxy Username | String |  | No | The proxy username to authenticate with.  
Proxy Password | Password |  | No | The proxy password to authenticate with.  
Credential JSON Object | Password | N/A | No | This parameter is needed for storing the data source credentials. This parameter has priority over "Broker API Root", "Broker API Username", "Broker API Password", "Concentrator API Root", "Concentrator API Username", "Concentrator API Password". Please refer to the documentation portal for more details.  
  
#### Connector rules

##### Proxy support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
