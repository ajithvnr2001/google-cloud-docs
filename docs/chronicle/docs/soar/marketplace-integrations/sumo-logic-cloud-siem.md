---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sumo-logic-cloud-siem/
title: Sumo Logic Cloud SIEM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:34.914035+00:00
---

# Sumo Logic Cloud SIEM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sumo-logic-cloud-siem/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Sumo Logic Cloud SIEM

This document provides guidance on how to integrate Sumo Logic Cloud SIEM with Google SecOps.

## Configure Sumo Logic Cloud SIEM integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://{instance} | Yes | API root of the Sumo Logic Cloud SIEM instance.  
API Key | String | N/A | No | API Key of the Sumo Logic Cloud SIEM account. **Note:** API key has priority over other authentication method.  
Access ID | String | N/A | No | Access ID of the Sumo Logic Cloud SIEM account. **Note:** Both Access ID and Access Key are required for this type of authentication.  
Access Key | String | N/A | No | Access Key of the Sumo Logic Cloud SIEM account. **Note:** Both Access ID and Access Key are required for this type of authentication.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verify that the SSL certificate for the connection to the Sumo Logic Cloud SIEM server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Use Cases

Ingest alerts.

## Actions

### Ping

#### Description

Test connectivity to Sumo Logic Cloud SIEM with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

This action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ "Successfully connected to the Sumo Logic Cloud SIEM server with the provided connection parameters!"**The action should fail and stop a playbook execution:******_If not successful:_ "Failed to connect to the Sumo Logic Cloud SIEM server! Error is {0}".format(exception.stacktrace) | General  
  
### Search Entity Signals

#### Description

Search signals related to entities in Sumo Logic Cloud SIEM. Supported entities: IP Address, Hostname, Username.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Lowest Severity To Return | Integer | 5 | No | Specify the lowest severity number that is used to return signals.Maximum: 10  
Time Frame | DDL | Last HourPossible Values:

  * Last Hour
  * Last 6 Hours
  * Last 24 Hours
  * Last Week
  * Last Month
  * 5 Minutes Around Alert Time
  * 30 Minutes Around Alert Time
  * 1 Hour Around Alert Time
  * Custom

| No | Specify a time frame for the results.If "Custom" is selected, you also need to provide "Start Time".If "Alert Time Till Now" is selected, the action uses start time of the alert as start time for the search and end time is current time.If "30 Minutes Around Alert Time" is selected, the action searches the alerts 30 minutes before the alert happened till the 30 minutes after the alert has happened. Same idea applies to "1 Hour Around Alert Time" and "5 Minutes Around Alert Time"  
Start Time | String | N/A | No | Specify the start time for the results.This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter.Format: ISO 8601  
End Time | String | N/A | No | Specify the end time for the results.If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter uses current time.Format: ISO 8601  
Max Signals To Return | Integer | 50 | No | Specify the number of signals to return per entity.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname
  * Username



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    [
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
                        "endpoint_username": "bL0ofHLH",
                        "event_message": "Failed password for invalid user",
                        "src_port": "39788"
                    },
                    "friendlyName": "record",
                    "hour": 10,
                    "http_requestHeaders": {},
                    "listMatches": [],
                    "matchedItems": [],
                    "metadata_deviceEventId": "citrix_xenserver_auth_message",
                    "metadata_mapperName": "Citrix Xenserver Auth Message",
                    "metadata_mapperUid": "bcc62402-2870-49ad-ba8d-64ddf22fd342",
                    "metadata_parseTime": 1646994593976,
                    "metadata_product": "Hypervisor",
                    "metadata_productGuid": "6751ee25-4ef9-4f9f-9c8b-c39668856994",
                    "metadata_receiptTime": 1646994592,
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
                    "timestamp": 1646994592000,
                    "uid": "7a89ebd4-3346-59fe-839a-9fc9bf99f51a",
                    "user_username": "bL0ofHLH",
                    "user_username_raw": "bL0ofHLH",
                    "year": 2022
                }
            ],
            "artifacts": [],
            "contentType": "ANOMALY",
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
            "id": "a9288779-354c-5a61-b492-f617d302c5ed",
            "name": "Password Attack",
            "recordCount": 10,
            "recordTypes": [],
            "ruleId": "THRESHOLD-S00095",
            "severity": 4,
            "stage": "Initial Access",
            "suppressed": true,
            "tags": [
                "_mitreAttackTactic:TA0001",
                "_mitreAttackTactic:TA0006",
                "_mitreAttackTechnique:T1110",
                "_mitreAttackTechnique:T1078",
                "_mitreAttackTechnique:T1078.001",
                "_mitreAttackTechnique:T1078.002",
                "_mitreAttackTechnique:T1078.003",
                "_mitreAttackTechnique:T1078.004",
                "_mitreAttackTechnique:T1586",
                "_mitreAttackTechnique:T1586.001",
                "_mitreAttackTechnique:T1586.002",
                "_mitreAttackTactic:TA0008",
                "_mitreAttackTechnique:T1110.003",
                "_mitreAttackTechnique:T1110.002",
                "_mitreAttackTechnique:T1110.001"
            ],
            "timestamp": "2022-03-11T10:29:52"
        }
    ]
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If found at least one signal (is_success=true):_ "Successfully returned signals for the following entities in Sumo Logic Cloud SIEM: {entities}."_If nothing was found for one entity (is_success=true):_ "No signals were found for the following entities in Sumo Logic Cloud SIEM: {entities}."_If nothing is found for all entities (is_success=true):_ "No signals were found for the provided entities in Sumo Logic Cloud SIEM."_If the 500 status code is reported for one entity (is_success=true):_ "Action wasn't able to retrieve signals for the following entities in Sumo Logic Cloud SIEM: {entities}."_If the 500 status code is reported for all entities (is_success=false):_ "Action wasn't able to retrieve signals for the provided entities in Sumo Logic Cloud SIEM."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Search Entity Signals". Reason: {0}''.format(error.Stacktrace) | General  
  
### Update Insight

#### Description

Update insight status in Sumo Logic Cloud SIEM.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Insight ID | String | N/A | Yes | Specify the ID of the insight needs to be updated.  
Status | DDL | Select OnePossible Values:

  * Select One
  * New In Progress
  * Closed

| Yes | Specify the status to set for the insight.  
Assignee Type | DDL | UserPossible Values:

  * User
  * Team

| Yes | Specify the assignee type for the "Assignee" parameter.  
Assignee | String | N/A | No | Specify the assignee identifier.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
      "data": {
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
      },
      "errors": []
    }
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If the 200 status code is reported (is_success=true):_ "Successfully updated insight with ID "{id}" in Sumo Logic Cloud SIEM."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Update Insight". Reason: {0}''.format(error.Stacktrace)_If errors are reported:_ "Error executing action "Update Insight". Reason: {message}.'_If "Select One" is selected for the "Status" parameter and no assignee is provided:_ "Error executing action "Update Insight". Reason: either status or assignee needs to be provided." | General  
  
### Add Comment To Insight

#### Description

Add a comment to an insight in Sumo Logic Cloud SIEM.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Insight ID | String | N/A | Yes | Specify the ID of the insight to which action needs to add a comment.  
Comment | String | N/A | Yes | Specify the comment that needs to be added to the insight.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "data": {
            "author": {
                "username": "tip.labops"
            },
            "body": "In Progress",
            "id": "1",
            "timestamp": "2022-03-16T12:03:56.472109"
        },
        "errors": []
    }
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If the 200 status code is reported (is_success=true):_ "Successfully added a comment to an insight with ID "{id}" in Sumo Logic Cloud SIEM."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Add Comment To Insight". Reason: {0}''.format(error.Stacktrace)_If errors are reported:_ "Error executing action "Add Comment To Insight". Reason: {message}. | General  
  
### Add Tags To Insight

#### Description

Add tags to an insight in Sumo Logic Cloud SIEM.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Insight ID | String | N/A | Yes | Specify the ID of the insight to which action needs to add tags.  
Tags | CSV | N/A | Yes | Specify a comma-separated list of tags that needs to be added to the insight.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "data": {
            "author": {
                "username": "tip.labops"
            },
            "body": "In Progress",
            "id": "1",
            "timestamp": "2022-03-16T12:03:56.472109"
        },
        "errors": []
    }
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If the 200 status code is reported (is_success=true):_ "Successfully added tags to an insight with ID "{id}" in Sumo Logic Cloud SIEM."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Add Tags To Insight". Reason: {0}''.format(error.Stacktrace)_If errors are reported:_ "Error executing action "Add Tags To Insight". Reason: {message}. | General  
  
### Enrich Entities

#### Description

Enrich entities using information from Sumo Logic Cloud SIEM. Supported entities: Hostname, User, IP Address.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Create Insight | Checkbox | Checked | No | If enabled, the action creates an insight containing all of the retrieved information about the entity.  
  
#### Run On

This action runs on the following entities:

  * Hostname
  * User
  * IP Address



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "activityScore": 8,
        "criticality": null,
        "entityType": "_ip",
        "firstSeen": null,
        "hostname": null,
        "id": "_ip-172.30.202.30",
        "inventory": [],
        "isSuppressed": false,
        "isWhitelisted": false,
        "lastSeen": "2022-03-11T09:44:53",
        "macAddress": null,
        "name": "172.30.202.30",
        "sensorZone": null,
        "tags": [],
        "value": "172.30.202.30"
    }
    

#### Entity Enrichment - Prefix SumoLogicCloudSIEM_

Enrichment Field Name | Source (JSON Key) | Logic - When to apply  
---|---|---  
isSuppressed | isSuppressed | When available in JSON  
isWhitelisted | isWhitelisted | When available in JSON  
tags | CSV of tags | When available in JSON  
firstSeen | firstSeen | When available in JSON  
lastSeen | lastSeen | When available in JSON  
criticality | criticality | When available in JSON  
activityScore | activityScore | When available in JSON  
  
##### Insights

N/A

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available for one entity (is_success=true):_ "Successfully enriched the following entities using information from Harmony Mobile: {entity.identifier}"._If data is not available for one entity (is_success=true):_ "Action wasn't able to enrich the following entities using information from Sumo Logic Cloud SIEM: {entity.identifier}"_If data is not available for all entities (is_success=false):_ "None of the provided entities were enriched."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Title:** {entity.identifier}**Table Columns:**

  * Key
  * Value

| Entity  
  
## Connectors

### Sumo Logic Cloud SIEM - Insights Connector

#### Description

Pull information about insights from Sumo Logic Cloud SIEM.

**Note:** The dynamic list filter works with the "name" parameter.

#### Configure Sumo Logic Cloud SIEM - Insights Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | N/A | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | generalized_data_name | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://{instance} | Yes | API root of the Sumo Logic Cloud SIEM instance.  
API Key | String | N/A | No | API Key of the Sumo Logic Cloud SIEM account. **Note:** API key has priority over other authentication method.  
Access ID | String | N/A | No | Access ID of the Sumo Logic Cloud SIEM account. **Note:** Both Access ID and Access Key are required for this type of authentication.  
Access Key | Secret | N/A | No | Access Key of the Sumo Logic Cloud SIEM account. **Note:** Both Access ID and Access Key are required for this type of authentication.  
Lowest Severity To Fetch | String | N/A | No | The lowest priority that needs to be used to fetch cases. Possible values: Low, Medium, High, Critical. If nothing is specified, the connector will ingest insights with all severities.  
Max Hours Backwards | Integer | 1 | No | Number of hours from where to fetch insights.  
Max Insights To Fetch | Integer | 20 | No | Number of insights to process per one connector iteration.  
Use dynamic list as a blacklist | Checkbox | Unchecked | Yes | If enabled, dynamic list is used as a blacklist.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verify that the SSL certificate for the connection to the Sumo Logic Cloud SIEM server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector rules

##### Proxy support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
