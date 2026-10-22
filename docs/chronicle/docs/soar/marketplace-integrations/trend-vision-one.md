---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/trend-vision-one/
title: Integrate Trend Vision One with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:59.660653+00:00
---

# Integrate Trend Vision One with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/trend-vision-one/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Trend Vision One with Google SecOps 

This document provides guidance on how to integrate Trend Vision One with Google Security Operations.

## Integrate Trend Vision One with Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration inputs

To configure the integration, use the following parameters:

Parameters  
---  
API Root | **Required** API root of the Trend Vision One instance. Default value is `https://INSTANCE`  
API Token | **Required** API Key of the Trend Vision One account.  
Verify SSL | If checked, the integration verifies if the SSL certificate for the connection to the Trend Vision One server is valid. Checked by default  
  
### How to generate API Token

For more information about how to generate API Token, see [Obtain the Authentication Token of an Account](https://automation.trendmicro.com/xdr/Guides/First-Steps-Toward-Using-the-APIs#Obtain-the-Authentication-Token-of-an--------Account).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Enrich Entities

Enrich entities using information from Trend Vision One.

#### Entities

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action inputs

To configure the action, use the following parameters:

Parameters   
---  
`Agent UUID` | **Optional.** A comma-separated list of UUIDs to specify the endpoints to process. The action runs on these endpoints in addition to any entities found in the alert.  
  
#### Action outputs

Action output type   
---  
Case wall attachment  | N/A   
Case wall link  | N/A   
Case wall table  | Available   
Enrichment table  | N/A   
Entity insight  | N/A   
Insight  | N/A   
JSON result  | Available   
OOTB widget  | N/A   
Script result  | Available   
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### JSON result
    
    
    {
               "agentGuid": "3b3ff9df-d588-45a2-bb90-d73904accf46",
               "osName": "Example OS",
               "osVersion": "6.1.1111",
               "osDescription": "Example OS Professional (64 bit) build 1111",
               "productCode": "xes",
               "loginAccount": {
                   "value": [
                       "EXAMPLE\\devs"
                   ],
                   "updatedDateTime": "2022-12-26T17:28:51.000Z"
               },
               "endpointName": {
                   "value": "EXAMPLE",
                   "updatedDateTime": "2022-12-27T17:47:17.000Z"
               },
               "macAddress": {
                   "value": [
                       "01:23:45:ab:cd:ef",
                       "01:23:45:67:ab:cd:ef:gh"
                   ],
                   "updatedDateTime": "2022-12-27T17:47:17.000Z"
               },
               "ip": {
                   "value": [
                       "198.51.100.1"
                   ],
                   "updatedDateTime": "2022-12-27T17:47:17.000Z"
               },
               "installedProductCodes": [
                   "xes"
               ]
    }
    

##### Entity enrichment – Prefix: TrendMicroVisionOne_

Enrichment Field Name | Source (JSON key) | Logic - When to apply  
---|---|---  
os | osDescription | When available in JSON  
login_account | Csv of loginAccount.value | When available in JSON  
endpoint_name | endpointName.value | When available in JSON  
ip | Csv ip.value | When available in JSON  
installedProductCodes | Csv of installedProductCodes | When available in JSON  
  
##### Case wall

The action provides the following output messages:

Output message  | Message description   
---|---  
Successfully enriched the following entities using information from Trend Micro Vision One: ENTITY_IDENTIFIER | Action is successful.   
Error executing action "Enrich Entities". Reason: ERROR_REASON | Action returned an error. Check connection to the server, input parameters, or credentials.  
  
##### Case wall table

**Name:** ENTITY_IDENTIFIER

**Columns:**

  * Key
  * Value



### Execute Custom Script

Execute custom script on the endpoint in Trend Vision One.

**Note:** The action runs asynchronously. Adjust the script timeout value in Google SecOps IDE for the action as required.

#### Entities

This action runs on the following entities:

  * Hostname
  * IP Address.



#### Action inputs

To configure the action, use the following parameters:

Parameters   
---  
`Agent UUID` | **Optional.** A comma-separated list of UUIDs to specify the endpoints to process. The action runs on these endpoints in addition to any entities found in the alert.  
`Script Name` | **Required** Name of the script that needs to be executed on the endpoints.  
`Script Parameters` | Parameters for the script.   
  
#### Action outputs

Action output type   
---  
Case wall attachment  | N/A   
Case wall link  | N/A   
Case wall table  | Available   
Enrichment table  | N/A   
Entity insight  | N/A   
Insight  | N/A   
JSON result  | Available   
OOTB widget  | N/A   
Script result  | Available   
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### JSON result

The JSON result is available even if the action fails.
    
    
    {
       "Entity": "qweqwe",
       "EntityResult": {
        "task_id": "{task id}"
           "status": "{task status}"
       }
    }
    

##### Case wall

The action provides the following output messages:

Output message  | Message description   
---|---  
Successfully executed custom script "SCRIPT_NAME" on the following endpoints in Trend Micro Vision One: ENTITY_IDENTIFIER | Action is successful.   
Error executing action "Execute Custom Script". Reason: ERROR_REASON | Action returned an error. Check connection to the server, input parameters, or credentials.  
Error executing action "Execute Custom Script". Reason: script with name "SCRIPT_NAME" wasn't found. | Action returned an error. Check the script name.  
Error executing action "Execute Custom Script". Reason: action ran into a timeout during execution. Please increase the timeout in IDE.  | Action returned an error. Increase the timeout value in IDE.   
  
### Execute Email Action

Execute email action on the endpoint in Trend Vision One.

**Note:** The action is running asynchronously. Adjust the script timeout value in Google SecOps IDE for action as required.

#### Entities

The action does not run on entities.

#### Action inputs

To configure the action, use the following parameters:

Parameters   
---  
`Action` | The action for the email.Default value is `Delete`. Possible values are:

  * Delete
  * Quarantine
  * Restore

  
`Message ID` | **Required** ID of the message used in the action.  
`Mailbox` | The mailbox related to the message.  
`Description` | A description for the performed action.  
  
#### Action outputs

Action output type   
---  
Case wall attachment  | N/A   
Case wall link  | N/A   
Case wall table  | N/A   
Enrichment table  | N/A   
Entity insight  | N/A   
Insight  | N/A   
JSON result  | Available   
OOTB widget  | N/A   
Script result  | Available   
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### JSON result
    
    
    {
        "id": "RM-20231017-00001",
        "status": "running",
        "createdDateTime": "2023-10-17T05:25:37Z",
        "lastActionDateTime": "2023-10-17T05:25:37Z",
        "description": "task description",
        "action": "quarantineMessage",
        "account": "API key",
        "tasks": [
            {
                "messageId": "<64e32256-fae1-4652-9f7a-8e514ec86d5a@example.com>",
                "mailBox": "example.user@example.com",
                "messageSubject": "Example Service has merged the incidents detected in your environment",
                "uniqueId": "AAkALgAAAAAAHYQDEapmEc2byACqAC-EWg0A28vWY1XUyUyUUvI8a3APqAADxR_EPAAA",
                "organizationId": "40c52b8c-062a-4095-bd74-e46a5eb48308",
                "status": "running",
                "lastActionDateTime": "2023-10-17T05:25:38Z"
            }
        ]
    }
    

##### Case wall

The action provides the following output messages:

Output message  | Message description   
---|---  
Successfully executed action on the message ID in Trend Micro Vision One.  | Action is successful.   
Error executing action "Execute Email Action". Reason: ERROR_REASON | Action returned an error. Check connection to the server, input parameters, or credentials.  
Error executing action "Execute Email Action". Reason: action ran into a timeout during execution. Please increase the timeout in IDE.  | Action returned an error. Increase the timeout value in IDE.   
  
### Isolate Endpoint

Isolate endpoints in Trend Vision One.

**Note:** The action runs asynchronously. Adjust the script timeout value in Google SecOps IDE for action as required.

#### Entities

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action inputs

To configure the action, use the following parameters:

Parameters   
---  
`Agent UUID` | A comma-separated list of UUIDs to specify the endpoints to process. The action runs on these endpoints in addition to any entities found in the alert.  
`Description` | **Required.** The reasoning for the isolation of the endpoints. The default value is `Isolating endpoint from Google SecOps Playbook`.  
  
#### Action outputs

Action output type   
---  
Case wall attachment  | N/A   
Case wall link  | N/A   
Case wall table  | N/A   
Enrichment table  | N/A   
Entity insight  | N/A   
Insight  | N/A   
JSON result  | Available   
OOTB widget  | N/A   
Script result  | Available   
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### JSON result

The JSON result is shown even if the action fails.
    
    
    [
      {
        "Entity": "172.yy.yyy.yyy",
        "EntityResult": {
          "status": "succeeded",
          "task_id": "1"
        }
      }
    ]
    

##### Case wall

The action provides the following output messages:

Output message  | Message description   
---|---  
Successfully isolated the following endpoints in Trend Micro Vision One: ENTITY_IDENTIFIER | Action is successful.   
Error executing action "Isolate Endpoints". Reason: ERROR_REASON | Action returned an error. Check connection to the server, input parameters, or credentials.  
Error executing action "Isolate Endpoints". Reason: action ran into a timeout during execution. Pending endpoints: PENDING_ENDPOINTS. Please increase the timeout in IDE.  | Action returned an error. Increase the timeout value in IDE.   
  
### Submit File

Submit file in Trend Vision One.

**Note:** This action is running asynchronously. Adjust the script timeout value in Google SecOps IDE for action as required.

#### Entities

The action does not run on entities.

#### Action inputs

To configure the action, use the following parameters:

Parameters   
---  
`File Paths` | **Required** A comma-separated list of paths for the files to submit.  
`Archive Password` | The password for the archive.  
`Document Password` | The password for the document.  
`Arguments` | Arguments for the submitted file.  
  
#### Action outputs

Action output type   
---  
Case wall attachment  | N/A   
Case wall link  | N/A   
Case wall table  | N/A   
Enrichment table  | N/A   
Entity insight  | N/A   
Insight  | N/A   
JSON result  | Available   
OOTB widget  | N/A   
Script result  | Available   
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### JSON result
    
    
    {
       "Entity": "file path",
       "EntityResult": {
        "id": "3daefed8-466f-46c6-849a-4dd46edb94b4",
        "type": "file",
        "digest": {
            "md5": "f90a614c2ec8f72c55c2f50c0af923f3",
            "sha1": "d3f75803673b19c0c736efbaf6a8d3891ae18a10",
            "sha256": "3ba41b6e5c2ee4e9a2710976b177cf0db1080eb0277c554aa7d6ef1f0b04b33f"
        },
        "analysisCompletionDateTime": "2023-10-16T17:38:21Z",
        "riskLevel": "noRisk",
        "detectionNames": [],
        "threatTypes": [],
        "trueFileType": "Shell Script"
    }
    }
    

##### Case wall

The action provides the following output messages:

Output message  | Message description   
---|---  
Successfully submitted the following files in Trend Micro Vision One: FILE_PATHS | Action is successful.   
Error executing action "Submit file". Reason: ERROR_REASON | Action returned an error. Check connection to the server, input parameters, or credentials.  
Error executing action "Submit File". Reason: the following files weren't found or not accessible: LIST_OF_FILE_PATHS | Action returned an error.Check the file paths.  
  
### Submit URL

Submit URL in Trend Vision One.

**Note:** The action is running asynchronously. Adjust the script timeout value in Google SecOps IDE for action as required.

#### Entities

This action runs on a URL entity.

#### Action inputs

To configure the action, use the following parameters:

Parameters   
---  
`Action` | The action for the email.Default value is `Delete`. Possible values are:

  * Delete
  * Quarantine
  * Restore

  
`Message ID` | **Required** ID of the message used in the action.  
`Mailbox` | The mailbox related to the message.  
`Description` | A description for the performed action.  
  
#### Action outputs

Action output type   
---  
Case wall attachment  | N/A   
Case wall link  | N/A   
Case wall table  | N/A   
Enrichment table  | N/A   
Entity insight  | N/A   
Insight  | N/A   
JSON result  | Available   
OOTB widget  | N/A   
Script result  | Available   
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### JSON result
    
    
    {
       "Entity": "url",
       "EntityResult": {
        "id": "3daefed8-466f-46c6-849a-4dd46edb94b4",
        "type": "file",
        "digest": {
            "md5": "f90a614c2ec8f72c55c2f50c0af923f3",
            "sha1": "d3f75803673b19c0c736efbaf6a8d3891ae18a10",
            "sha256": "3ba41b6e5c2ee4e9a2710976b177cf0db1080eb0277c554aa7d6ef1f0b04b33f"
        },
        "analysisCompletionDateTime": "2023-10-16T17:38:21Z",
        "riskLevel": "noRisk",
        "detectionNames": [],
        "threatTypes": [],
        "trueFileType": "Shell Script"
    }
    }
    

##### Case wall

The action provides the following output messages:

Output message  | Message description   
---|---  
Successfully submitted the following URLs in Trend Micro Vision One: LIST_OF_URLS | Action is successful.   
Error executing action "Submit URL". Reason: ERROR_REASON | Action returned an error. Check connection to the server, input parameters, or credentials.  
Error executing action "Submit URL". Reason: action ran into a timeout during execution. Pending files: FILES_STILL_IN_PROGRESS. Please increase the timeout in IDE.  | Action returned an error. Increase the timeout value in IDE.   
  
### Unisolate Endpoint

Unisolate endpoints in Trend Vision One.

**Note:** The action runs asynchronously. Adjust the script timeout value in Google SecOps IDE for action as required.

#### Entities

The action runs on the following entities:

  * IP Address
  * Hostname



#### Action inputs

To configure the action, use the following parameters:

Parameters   
---  
`Agent UUID` | A comma-separated list of UUIDs to specify the endpoints to process. The action runs on these endpoints in addition to any entities found in the alert.  
`Description` | **Required.** The reason to unisolate the endpoints. The default value is `Unisolating endpoint from Google SecOps Playbook`.  
  
#### Action outputs

Action output type   
---  
Case wall attachment  | N/A   
Case wall link  | N/A   
Case wall table  | N/A   
Enrichment table  | N/A   
Entity insight  | N/A   
Insight  | N/A   
JSON result  | Available   
OOTB widget  | N/A   
Script result  | Available   
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### JSON result

The JSON result is shown even if the action fails.
    
    
    {
       "Entity": "qweqwe",
       "EntityResult": {
           "status": "{task status}"
       }
    }
    

##### Case wall

The action provides the following output messages:

Output message  | Message description   
---|---  
Successfully unisolated the following endpoints in Trend Micro Vision One: ENTITY_IDENTIFIER | Action is successful.   
Error executing action "Unisolate Endpoints". Reason: ERROR_REASON | Action returned an error. Check connection to the server, input parameters, or credentials.  
Error executing action "Unisolate Endpoints". Reason: action ran into a timeout during execution. Pending endpoints: PENDING_ENDPOINTS. Please increase the timeout in IDE.  | Action returned an error. Increase the timeout value in IDE.   
  
### Update Workbench Alert

Update a workbench alert in Trend Vision One.

#### Entities

The action doesn't run on entities.

#### Action inputs

To configure the action, use the following parameters:

Parameters   
---  
`Alert ID` | **Required** ID of the alert that needs to be updated.  
`Status` | **Required** The status to be set for the alert.Default value is `Select One`. Possible values are:

  * `New`
  * `In Progress`
  * `True Positive`
  * `False Positive`

  
  
#### Action outputs

Action output type   
---  
Case wall attachment  | N/A   
Case wall link  | N/A   
Case wall table  | N/A   
Enrichment table  | N/A   
Entity insight  | N/A   
Insight  | N/A   
JSON result  | Available   
OOTB widget  | N/A   
Script result  | Available   
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
##### JSON result
    
    
    {
          "artifacts": [],
          "assignedTo": "tip.labops",
          "assignee": {
              "displayName": "tip.labops@example.com",
              "username": "tip.labops"
          },
          "closed": "2022-03-23T11:04:33.731971",
          "closedBy": "tip.labops",
          "confidence": 0.1,
          "created": "2022-03-11T08:48:26.030204",
          "description": "Detects multiple failed login attempts from a single source with unique usernames over a 24 hour timeframe. This is designed to catch both slow and quick password spray type attacks. The threshold and time frame can be adjusted based on the customer's environment.",
          "entity": {
              "entityType": "_ip",
              "hostname": null,
              "id": "_ip-198.51.100.1",
              "macAddress": null,
              "name": "198.51.100.1",
              "sensorZone": "",
              "value": "198.51.100.1"
          },
          "id": "dbc30c20-6d99-4f6f-8580-157ce70368a5",
          "lastUpdated": "2022-03-23T11:04:33.740470",
          "lastUpdatedBy": null,
          "name": "Initial Access",
          "orgId": "example",
          "readableId": "INSIGHT-13927",
          "recordSummaryFields": [],
          "resolution": "False Positive",
          "severity": "CRITICAL",
          "signals": [
              {
                  "allRecords": [
                      {
                          "action": "failed password attempt",
                          "bro_dns_answers": [],
                          "bro_file_bytes": {},
                          "bro_file_connUids": [],
                          "bro_flow_service": [],
                          "bro_ftp_pendingCommands": [],
                          "bro_http_cookieVars": [],
                          "bro_http_origFuids": [],
                          "bro_http_origMimeTypes": [],
                          "bro_http_request_headers": {},
                          "bro_http_request_proxied": [],
                          "bro_http_response_headers": {},
                          "bro_http_response_respFuids": [],
                          "bro_http_response_respMimeTypes": [],
                          "bro_http_tags": [],
                          "bro_http_uriVars": [],
                          "bro_kerberos_clientCert": {},
                          "bro_kerberos_serverCert": {},
                          "bro_sip_headers": {},
                          "bro_sip_requestPath": [],
                          "bro_sip_responsePath": [],
                          "bro_ssl_certChainFuids": [],
                          "bro_ssl_clientCertChainFuids": [],
                          "cseSignal": {},
                          "day": 11,
                          "device_ip": "198.51.100.1",
                          "device_ip_ipv4IntValue": 2887698974,
                          "device_ip_isInternal": true,
                          "device_ip_version": 4,
                          "fieldTags": {},
                          "fields": {
                              "auth_method": "ssh2",
                              "endpoint_ip": "198.51.100.1",
                              "endpoint_username": "1ewk0XJn",
                              "event_message": "Failed password for invalid user",
                              "src_port": "59088"
                          },
                          "friendlyName": "record",
                          "hour": 8,
                          "http_requestHeaders": {},
                          "listMatches": [],
                          "matchedItems": [],
                          "metadata_deviceEventId": "Example_server_auth_message",
                          "metadata_mapperName": "Example Server Auth Message",
                          "metadata_mapperUid": "bcc62402-2870-49ad-ba8d-64ddf22fd342",
                          "metadata_parseTime": 1646987453926,
                          "metadata_product": "Example Product",
                          "metadata_productGuid": "6751ee25-4ef9-4f9f-9c8b-c39668856994",
                          "metadata_receiptTime": 1646987443,
                          "metadata_relayHostname": "centos-002",
                          "metadata_schemaVersion": 3,
                          "metadata_sensorId": "0b52e838-2dbd-4fc0-a2b5-7135a5dc72b7",
                          "metadata_sensorInformation": {},
                          "metadata_sensorZone": "default",
                          "metadata_vendor": "Example Vendor",
                          "month": 3,
                          "normalizedAction": "logon",
                          "objectType": "Authentication",
                          "srcDevice_ip": "198.51.100.1",
                          "srcDevice_ip_ipv4IntValue": 2887698974,
                          "srcDevice_ip_isInternal": true,
                          "srcDevice_ip_version": 4,
                          "success": false,
                          "timestamp": 1646987443000,
                          "uid": "c2e6188b-202c-5736-9b4d-248ab6ba88dd",
                          "user_username": "1ewk0XJn",
                          "user_username_raw": "1ewk0XJn",
                          "year": 2022
                      }
                  ],
                  "artifacts": [],
                  "contentType": "ANOMALY",
                  "description": "Detects multiple failed login attempts from a single source with unique usernames over a 24 hour timeframe. This is designed to catch both slow and quick password spray type attacks. The threshold and time frame can be adjusted based on the customer's environment.",
                  "id": "b4adb0dc-1340-56ec-87aa-c6f1fc0fa247",
                  "name": "Password Attack",
                  "recordCount": 10,
                  "recordTypes": [],
                  "ruleId": "THRESHOLD-S00095",
                  "severity": 4,
                  "stage": "Initial Access",
                  "tags": [
                      "_mitreAttackTactic:TA0001"
                  ],
                  "timestamp": "2022-03-11T08:31:28"
              }
          ],
          "source": "USER",
          "status": {
              "displayName": "Closed",
              "name": "closed"
          },
          "subResolution": null,
          "tags": [
              "aaa3"
          ],
          "teamAssignedTo": null,
          "timeToDetection": 1271.030204,
          "timeToRemediation": 1044967.701767,
          "timeToResponse": 21.186055,
          "timestamp": "2022-03-11T08:31:28"
      }
    

##### Case wall

The action provides the following output messages:

Output message  | Message description   
---|---  
Successfully updated workbench alert with ID ID in Trend Micro Vision One. | Action is successful.   
Error executing action "Update Workbench Alert". Reason: ERROR_REASON | Action returned an error. Check connection to the server, input parameters, or credentials.  
  
## Connectors

For instructions about how to create and configure the Trend Vision One connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

### Trend Vision One Workbench Alerts Connector

Pull information about workbench alerts from Trend Vision One.

**Note:** The dynamic list filter works with the `model` parameter.

#### Connector parameters

To configure the connector, use the following parameters:

Parameters  
---  
`Product Field Name` | **Required** Enter the source field name in order to retrieve the Product Field name. Default value is `Product Name`.  
`Event Field Name` | **Required** Enter the source field name in order to retrieve the Event Field name. Default value is `indicators_field`.  
`Environment Field Name` | _Optional_ Describes the name of the field where the environment name is stored.  If the environment field isn't found, the environment is the default environment. Default value is `""`.  
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. Default value `.*` catches all and returns the value unchanged. The parameter allows the user to manipulate the environment field using the regular expression logic. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is the default environment.   
`Script Timeout (Seconds)` | **Required** Timeout limit for the python process running the current script. Default value is 180.  
`API Root` | **Required** API root of the Trend Vision One instance. Default value is `https://INSTANCE`.  
`API Key` | **Required** API Key of the Trend Vision One account.  
`Lowest Severity Score To Fetch` | _Optional_ Lowest severity score of the incidents to fetch. If nothing is provided, the connector ingests incidents with all severities. Possible values are:

  * Low
  * Medium
  * High
  * Critical

  
`Max Hours Backwards` | _Optional_ Amount of hours from where to fetch incidents. Default value is 1 hour.  
`Max Alerts To Fetch` | _Optional_ The number of alerts to process per one connector iteration. Default value is 10.  
`Use dynamic list as a blocklist` | **Required** If checked, the dynamic list is used as a blocklist. Unchecked by default.  
`Verify SSL` | **Required** If checked, verifies that the SSL certificate for the connection to the Trend Vision One server is valid. Checked by default.  
`Proxy Server Address` | _Optional_ The address of the proxy server to use.  
`Proxy Username` | _Optional_ The proxy username to authenticate with.  
`Proxy Password` | _Optional_ The proxy password to authenticate with.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
