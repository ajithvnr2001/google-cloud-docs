---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/trend-micro-vision-one/
title: Trend Micro Vision One \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:29:57.646331+00:00
---

# Trend Micro Vision One  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/trend-micro-vision-one/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Trend Micro Vision One

**Deprecated:** This integration is deprecated and no longer supported. We recommend that you use the [Trend Vision One](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/trend-vision-one) integration instead.

## Configure Trend Micro Vision One integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration configuration parameters

Use the following parameters to configure the integration:

Parameter name | Type | Default value | Required | Description  
---|---|---|---|---  
API Root | String | https://{instance} | Yes | API root of the Trend Micro Vision One instance.  
API Token | String | N/A | Yes | API Key of the Trend Micro Vision One account.  
Verify SSL | Checkbox | Checked | No | If enabled, the integration verifies that the SSL certificate for the connection to the Trend Micro Vision One server is valid.  
  
### How to generate API Token

For more information about how to generate API Token, see [Obtain the Authentication Token of an Account](https://automation.trendmicro.com/xdr/Guides/First-Steps-Toward-Using-the-APIs#Obtain-the-Authentication-Token-of-an--------Account).

## Actions

### Enrich Entities

#### Action description

Enrich entities using information from Trend Micro Vision One. Supported entities: Hostname, IP Address.

#### Action configuration parameters

This action doesn't have any configuration parameters.

#### Run on

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
               "agentGuid": "3b3ff9df-d588-45a2-bb90-d73904accf46",
               "osName": "Windows",
               "osVersion": "6.1.7601",
               "osDescription": "Windows 7 Professional (64 bit) build 7601",
               "productCode": "xes",
               "loginAccount": {
                   "value": [
                       "WINDOWS7\\devs"
                   ],
                   "updatedDateTime": "2022-12-26T17:28:51.000Z"
               },
               "endpointName": {
                   "value": "WINDOWS7",
                   "updatedDateTime": "2022-12-27T17:47:17.000Z"
               },
               "macAddress": {
                   "value": [
                       "00:50:56:b6:3e:a1",
                       "00:00:00:00:00:00:00:e0"
                   ],
                   "updatedDateTime": "2022-12-27T17:47:17.000Z"
               },
               "ip": {
                   "value": [
                       "172.30.201.12"
                   ],
                   "updatedDateTime": "2022-12-27T17:47:17.000Z"
               },
               "installedProductCodes": [
                   "xes"
               ]
    }
    

##### Entity enrichment

Prefix TrendMicroVisionOne_

Enrichment Field Name | Source (JSON key) | Logic - When to apply  
---|---|---  
os | osDescription | When available in JSON  
login_account | Csv of loginAccount.value | When available in JSON  
endpoint_name | endpointName.value | When available in JSON  
ip | Csv ip.value | When available in JSON  
installedProductCodes | Csv of installedProductCodes | When available in JSON  
  
##### Case wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available for one entity (is_success=true):_ "Successfully enriched the following entities using information from Trend Micro Vision One: {entity.identifier}" _If data is not available for all entities (is_success=false):_ "None of the provided entities were enriched." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Title:** {entity.identifier} Columns Key Value | Entity  
  
### Execute Custom Script

#### Action description

Execute custom script on the endpoint in Trend Micro Vision One. Supported entities: Hostname, IP Address. The action runs asynchronously, adjust the script timeout value in the Google SecOps SOAR IDE for the action as needed.

#### Action configuration parameters

Parameter name | Type | Default value | Required | Description  
---|---|---|---|---  
Script Name | String | N/A | Yes | Specify the name of the script that needs to be executed on the endpoints.  
Script Parameters | String | N/A | No | Specify the parameters for the script.  
  
#### Run on

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result

The JSON result is shown even if the action fails.
    
    
    {
       "Entity": "qweqwe",
       "EntityResult": {
        "task_id": "{task id}"
           "status": "{task status}"
       }
    }
    

##### Case wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available for one endpoint (is_success=true only if all were successful else false):_ "Successfully executed custom script "{script name}" on the following endpoints in Trend Micro Vision One: {entity.identifier}" _If data is not available for one endpoint or asset is not found (is_success=false):_ "Action wasn't able to execute custom script "{scrip name}" on the following endpoints using in Trend Micro Vision One: {entity.identifier}" _If data is not available for all endpoints (is_success=false):_ "Scripts were not executed on the provided endpoints." _Asynchronous message:_ "Pending endpoints: {entities}" **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Execute Custom Script". Reason: {0}''.format(error.Stacktrace)" _If a custom script is not found:_ "Error executing action "Execute Custom Script". Reason: script with name "{script name} wasn't found." _If the action ran into a timeout:_ "Error executing action "Execute Custom Script". Reason: action ran into a timeout during execution. Pending endpoints: {endpoints that are still in progress}. Please increase the timeout in IDE. Note: action will run the custom script again." | General  
  
### Isolate Endpoint

#### Action description

Isolate endpoints in Trend Micro Vision One. Supported entities: IP Address, Hostname. The action runs asynchronously, adjust the script timeout value in the Google SecOps SOAR IDE for action as needed.

#### Action configuration parameters

Parameter name | Type | Default value | Required | Description  
---|---|---|---|---  
Description | String | N/A | No | Specify the reasoning for the isolation of the endpoints.  
  
#### Run on

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result

The JSON result is shown even if the action fails.
    
    
    {
       "Entity": "qweqwe",
       "EntityResult": {
           "status": "{task status}"
       }
    }
    

##### Case wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available for one endpoint (is_success=true only if all endpoints were successfully isolated else false):_ "Successfully isolated the following endpoints in Trend Micro Vision One: {entity.identifier}" _If data is not available for one endpoint or asset is not found (is_success=false):_ "Action wasn't able to isolate the following endpoints using in Trend Micro Vision One: {entity.identifier}" _If data is not available for all endpoints (is_success=false):_ "None of the provided endpoints were isolated." _Asynchronous message:_ "Pending endpoints: {entities}" **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Isolate Endpoints". Reason: {0}''.format(error.Stacktrace)" _If the action ran into a timeout:_ "Error executing action "Isolate Endpoints". Reason: action ran into a timeout during execution. Pending endpoints: {endpoints that are still in progress}. Please increase the timeout in IDE." | General  
  
### Unisolate Endpoint

#### Action description

Unisolate endpoints in Trend Micro Vision One. Supported entities: IP Address, Hostname. The action runs asynchronously, adjust the script timeout value in the Google SecOps SOAR IDE for action as needed.

#### Action configuration parameters

Parameter name | Type | Default value | Required | Description  
---|---|---|---|---  
Description | String | N/A | No | Specify the reasoning for the isolation of the endpoints.  
  
#### Run on

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action Results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result

The JSON result is shown even if the action fails.
    
    
    {
       "Entity": "qweqwe",
       "EntityResult": {
           "status": "{task status}"
       }
    }
    

##### Case wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available for one endpoint (is_success=true only if all endpoints were successfully isolated else false):_ "Successfully unisolated the following endpoints in Trend Micro Vision One: {entity.identifier}" _If data is not available for one endpoint or asset is not found (is_success=false):_ "Action wasn't able to unisolate the following endpoints using in Trend Micro Vision One: {entity.identifier}" _If data is not available for all endpoints (is_success=false):_ "None of the provided endpoints were unisolated." _Asynchronous message:_ "Pending endpoints: {entities}" **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Unisolate Endpoints". Reason: {0}''.format(error.Stacktrace)" _If the action ran into a timeout:_ "Error executing action "Unisolate Endpoints". Reason: action ran into a timeout during execution. Pending endpoints: {endpoints that are still in progress}. Please increase the timeout in IDE." | General  
  
### Update Workbench Alert

#### Action description

Update a workbench alert in Trend Micro Vision One.

#### Action configuration parameters

Parameter name | Type | Default value | Required | Description  
---|---|---|---|---  
Alert ID | String | N/A | Yes | Specify the ID of the alert that needs to be updated.  
Status | DDL | Select One Possible value:

  * Select One
  * New
  * In Progress
  * True Positive
  * False Positive

| Yes | Specify the status to be set for the alert.  
  
#### Run on

This action doesn't run on entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
          "artifacts": [],
          "assignedTo": "tip.labops",
          "assignee": {
              "displayName": "tip.labops@siemplify.co",
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
              "id": "_ip-172.30.202.30",
              "macAddress": null,
              "name": "172.30.202.30",
              "sensorZone": "",
              "value": "172.30.202.30"
          },
          "id": "dbc30c20-6d99-4f6f-8580-157ce70368a5",
          "lastUpdated": "2022-03-23T11:04:33.740470",
          "lastUpdatedBy": null,
          "name": "Initial Access",
          "orgId": "siemplify",
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
                          "device_ip": "172.30.202.30",
                          "device_ip_ipv4IntValue": 2887698974,
                          "device_ip_isInternal": true,
                          "device_ip_version": 4,
                          "fieldTags": {},
                          "fields": {
                              "auth_method": "ssh2",
                              "endpoint_ip": "172.30.202.30",
                              "endpoint_username": "1ewk0XJn",
                              "event_message": "Failed password for invalid user",
                              "src_port": "59088"
                          },
                          "friendlyName": "record",
                          "hour": 8,
                          "http_requestHeaders": {},
                          "listMatches": [],
                          "matchedItems": [],
                          "metadata_deviceEventId": "citrix_xenserver_auth_message",
                          "metadata_mapperName": "Citrix Xenserver Auth Message",
                          "metadata_mapperUid": "bcc62402-2870-49ad-ba8d-64ddf22fd342",
                          "metadata_parseTime": 1646987453926,
                          "metadata_product": "Hypervisor",
                          "metadata_productGuid": "6751ee25-4ef9-4f9f-9c8b-c39668856994",
                          "metadata_receiptTime": 1646987443,
                          "metadata_relayHostname": "centos-002",
                          "metadata_schemaVersion": 3,
                          "metadata_sensorId": "0b52e838-2dbd-4fc0-a2b5-7135a5dc72b7",
                          "metadata_sensorInformation": {},
                          "metadata_sensorZone": "default",
                          "metadata_vendor": "Citrix",
                          "month": 3,
                          "normalizedAction": "logon",
                          "objectType": "Authentication",
                          "srcDevice_ip": "172.30.202.30",
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

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If the 200 status code is reported (is_success=true):_ "Successfully updated workbench alert with ID "{id}" in Trend Micro Vision One." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Update Workbench Alert". Reason: {0}''.format(error.Stacktrace)" _If an error is reported in the response:_ "Error executing action "Update Workbench Alert". Reason: {message}.'" | General  
  
## Connectors

### Trend Micro Vision One - Workbench Alerts Connector

#### Connector description

Pull information about workbench alerts from Trend Micro Vision One.

**Note:** The dynamic list filter works with the **model** parameter.

#### Configure the connector

For instructions about how to create and configure the connector in Chronicle SOAR, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

#### Connector configuration parameters

Use the following parameters to configure the connector:

Parameter name | Type | Default value | Required | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | indicators_field | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the Environment Field Name field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://{instance} | Yes | API root of the Trend Micro Vision One instance.  
API Token | String |  | Yes | API Key of the Trend Micro Vision One account.  
Lowest Severity To Fetch | String | N/A | No | The lowest severity that needs to be used to fetch alerts. Possible values: Low, Medium, High, Critical. If nothing is specified, the connector ingests alerts with all severity types.  
Max Hours Backwards | Integer | 1 | No | The number of hours from where to fetch alerts.  
Max Alerts To Fetch | Integer | 10 | No | The number of alerts to process per one connector iteration.  
Use dynamic list as a blocklist | Checkbox | Unchecked | Yes | If enabled, dynamic lists is used as a blocklist.  
Verify SSL | Checkbox | Checked | No | If enabled, the integration verifies that the SSL certificate for the connection to the Trend Micro Vision One server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
