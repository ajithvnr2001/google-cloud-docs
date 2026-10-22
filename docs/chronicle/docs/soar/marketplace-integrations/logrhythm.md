---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/logrhythm/
title: LogRhythm \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:17.971815+00:00
---

# LogRhythm  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/logrhythm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# LogRhythm

This document provides guidance on how to integrate LogRhythm with Google SecOps.

Starting from version 10 of this integration, there will no longer be an Alarms Connector. This connector is deprecated, since the SOAP API is deprecated from LogRhythm side. Now the whole integration is using the REST API, that was introduced in the LogRhythm 7.9 Release.

For more information, see [SOAP API (LogRhythm 7.x.x)](https://docs.logrhythm.com/docs/lrapi/soap-api-logrhythm-7-x-x).

In addition, the integration is updated to Python version 3, so keeping this connector (from version 9) with the newer version of the integration (version 10) is not supported and causes unexpected behaviors.

Follow the recommended flow for this update:

  1. Before updating the integration to version 10, migrate every "LogRhythm Alarms Connector" to the "LogRhythm - Rest API Alarms Connector"' using version 9 of the integration.

  2. Update the integration to version 10.


**Note:** This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [storage bucket](https://storage.googleapis.com/csoar_public_integrations/LogRhythm.zip).

## Configure LogRhythm integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
API Root | String | https://{IP}:8501 | Yes | API root of the LogRhythm instance.  
API Token | Password | N/A | No | API Token of the LogRhythm instance.  
CA Certificate File | String | N/A | No | Base 64 encoded CA certificate file.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verify that the SSL certificate for the connection to the LogRhythm server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to LogRhythm with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Use cases

N/A

#### Run On

This action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ "Successfully connected to the LogRhythm server with the provided connection parameters!"**The action should fail and stop a playbook execution:******_If not successful:_ "Failed to connect to the LogRhythm server! Error is {0}".format(exception.stacktrace) | General  
  
### Enrich Entities

#### Description

Enrich entities using information from LogRhythm. Supported entities: Hostname, IP Address.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Create Insight | Checkbox | Checked | No | If enabled, the action creates an insight containing all of the retrieved information about the entity.  
  
#### Run on

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "id": 2,
        "entity": {
            "id": 2,
            "name": "EchoTestEntity"
        },
        "name": "EchoTestHost",
        "shortDesc": "LogRhythm ECHO",
        "riskLevel": "None",
        "threatLevel": "None",
        "threatLevelComments": "",
        "recordStatusName": "Active",
        "hostZone": "Internal",
        "location": {
            "id": -1
        },
        "os": "Windows",
        "osVersion": "Microsoft Windows NT 6.2.9200.0",
        "useEventlogCredentials": false,
        "osType": "Server",
        "dateUpdated": "2021-04-14T09:18:17.677Z",
        "hostRoles": [],
        "hostIdentifiers": [
            {
                "type": "IPAddress",
                "value": "10.1.2.50",
                "dateAssigned": "2021-04-14T09:17:31Z"
            },
            {
                "type": "WindowsName",
                "value": "EchoTestHost",
                "dateAssigned": "2021-04-14T09:17:31Z"
            }
        ]
    }
    

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
description | When available in JSON  
risk_level | When available in JSON  
threat_level | When available in JSON  
status | When available in JSON  
host_zone | When available in JSON  
os | When available in JSON  
type | When available in JSON  
ips | When available in JSON  
  
##### Insights

N/A

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******I _f data is available for one entity (is_success=true):_ "Successfully enriched the following entities using information from LogRhythm: {entity.identifier}"._If data is not available for one entity (is_success=true):_ "Action wasn't able to enrich the following entities using information from LogRhythm: {entity.identifier}"._If data is not available for all entities (is_success=false): "_ None of the provided entities were enriched."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Title:** {entity.identifier} | Entity  
  
### Update Alarm

#### Description

Update an alarm in LogRhythm.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Alarm ID | String | N/A | Yes | Specify the ID of the alarm that needs to be updated in LogRhythm.  
Status | DDL | Select OnePossible Values:

  * Select One
  * New
  * Open
  * Working
  * Escalated
  * Closed
  * False Alarm
  * Resolved
  * Unresolved
  * Reported
  * Monitor

| No | Specify the status for the alarm.  
Risk Score | Integer | N/A | No | Specify a new risk score for the alarm. Maximum: 100  
  
#### Run on

This action runs on the following entities:

  * URL
  * IP Address



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If the_ ****_200 status code is reported (is_success=true):_ "Successfully updated alarm with ID {ID} in LogRhythm."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Update Alarm". Reason: {0}''.format(error.Stacktrace)_If the status code is not 200:_ "Error executing action "Update Alarm". Reason: {0}''.format(responseMessage)"_If the "Status" parameter is set to "Select One" and none of the other values are provided:_ "Error executing action "Update Alarm". Reason: at least one of the action parameters should have a provided value." | General  
  
### Get Alarm Details

#### Description

Get alarm details in LogRhythm. This action allows you to get details from the LogRhythm Advanced Intelligence Engine (AIE) events and ingest this data into Google SecOps.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Alarm IDs | CSV | N/A | Yes | Specify a comma-separated list of alarm IDs for which we need to retrieve details.  
Max Events To Fetch | Integer | 50 | No | Specify the number of events to return.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    [
      {
        "alarmRuleID": 98,
        "alarmId": 18755,
        "personId": -100,
        "alarmDate": "2021-08-17T13:36:39.78",
        "alarmStatus": 0,
        "alarmStatusName": "New",
        "entityId": 2,
        "entityName": "EchoTestEntity",
        "alarmRuleName": "LogRhythm Agent Heartbeat Missed",
        "lastUpdatedID": -100,
        "lastUpdatedName": "LogRhythm Administrator",
        "dateInserted": "2021-08-17T13:36:39.807",
        "dateUpdated": "2021-08-17T13:36:39.86",
        "associatedCases": [],
        "lastPersonID": null,
        "eventCount": 1,
        "eventDateFirst": "2021-08-17T13:36:37.057",
        "eventDateLast": "2021-08-17T13:36:37.057",
        "rbpMax": 39,
        "rbpAvg": 39,
        "smartResponseActions": null,
        "alarmDataCached": "N",
        "alarmEventsDetails": [
          {
            "account": "admin5",
            "action": "",
            "amount": null,
            "bytesIn": null,
            "bytesOut": null,
            "classificationId": 2600,
            "classificationName": "Compromise",
            "classificationTypeName": "Security",
            "command": "",
            "commonEventId": 1031412,
            "cve": "",
            "commonEventName": "AIE: CSC: Disabled Account Auth Success",
            "count": 1,
            "directionId": 0,
            "directionName": "Unknown",
            "domain": "",
            "duration": 0,
            "entityId": -1000001,
            "entityName": "",
            "group": "",
            "impactedEntityId": -100,
            "impactedEntityName": "Global Entity",
            "impactedHostId": -1,
            "impactedHostName": "",
            "impactedInterface": "",
            "impactedIP": null,
            "impactedLocation": {
              "countryCode": "",
              "name": "",
              "latitude": 0,
              "locationId": 0,
              "locationKey": "",
              "longitude": 0,
              "parentLocationId": 0,
              "recordStatus": "Deleted",
              "regionCode": "",
              "type": "NULL",
              "dateUpdated": "0001-01-01T00:00:00"
            },
            "impactedMAC": "",
            "impactedName": "",
            "impactedNATIP": "",
            "impactedNATPort": null,
            "impactedNetwork": {
              "beginIPRange": {
                "value": ""
              },
              "dateUpdated": "0001-01-01T00:00:00",
              "riskThreshold": "",
              "endIPRange": {
                "value": ""
              },
              "entityId": 0,
              "hostZone": "Unknown",
              "locationId": 0,
              "longDesc": "",
              "name": "",
              "networkId": 0,
              "recordStatus": "Deleted",
              "shortDesc": ""
            },
            "impactedPort": -1,
            "impactedZone": "Unknown",
            "itemsPacketsIn": 0,
            "itemsPacketsOut": 0,
            "logDate": "2021-08-16T09:51:16.993",
            "login": "admin5",
            "logMessage": "",
            "logSourceHostId": -1000001,
            "logSourceHostName": "AI Engine Server",
            "logSourceName": "AI Engine",
            "logSourceTypeName": "LogRhythm AI Engine",
            "messageId": 173885,
            "mpeRuleId": -1,
            "mpeRuleName": "",
            "normalDateMax": "0001-01-01T00:00:00",
            "objectName": "",
            "objectType": "",
            "originEntityId": -100,
            "originEntityName": "Global Entity",
            "originHostId": -1,
            "originHostName": "",
            "originInterface": "",
            "originIP": null,
            "originLocation": {
              "countryCode": "",
              "name": "",
              "latitude": 0,
              "locationId": 0,
              "locationKey": "",
              "longitude": 0,
              "parentLocationId": 0,
              "recordStatus": "Deleted",
              "regionCode": "",
              "type": "NULL",
              "dateUpdated": "0001-01-01T00:00:00"
            },
            "originMAC": "",
            "originName": "",
            "originNATIP": "",
            "originNATPort": null,
            "originNetwork": {
              "beginIPRange": {
                "value": ""
              },
              "dateUpdated": "0001-01-01T00:00:00",
              "riskThreshold": "",
              "endIPRange": {
                "value": ""
              },
              "entityId": 0,
              "hostZone": "Unknown",
              "locationId": 0,
              "longDesc": "",
              "name": "",
              "networkId": 0,
              "recordStatus": "Deleted",
              "shortDesc": ""
            },
            "originPort": -1,
            "originZone": "Unknown",
            "parentProcessId": "",
            "parentProcessName": "",
            "parentProcessPath": "",
            "policy": "",
            "priority": 91,
            "process": "",
            "processId": -1,
            "protocolId": -1,
            "protocolName": "",
            "quantity": 0,
            "rate": 0,
            "reason": "",
            "recipient": "",
            "result": "",
            "responseCode": "",
            "sender": "",
            "session": "",
            "recipientIdentityId": null,
            "recipientIdentityName": ""
          }
        ]
      }
    ]
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If the_ ****_200 status code for one entity is reported (is_success=true):_ "Successfully retrieved details for the following alarms in LogRhythm: {IDs}"_If not found one alarm (is_success=true):_ "The following alarms were not found in LogRhythm: {IDs}"_If not found all alarms (is_success=false):_ "None of the provided alarms were found in LogRhythm."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Get Alarm Details". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** Alarm {ID} Events**Table Columns:**

  * Classification Name
  * Classification Type
  * Name
  * Priority
  * Account
  * Hostname

| General  
  
### Add Comment To Alarm

#### Description

Add a comment to the alarm in LogRhythm.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Alarm ID | String | N/A | Yes | Specify the ID of the alarm to which you need to add a comment in LogRhythm.  
Comment | String | N/A | Yes | Specify a comment that needs to be added to the alarm.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If_ the ****_200 status code is reported (is_success=true):_ "Successfully added comment to the alarm with ID {ID} in LogRhythm."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Add Comment To Alarm". Reason: {0}''.format(error.Stacktrace)_If the status code is not 200:_ "Error executing action "Add Comment To Alarm". Reason: {0}''.format(responseMessage) | General  
  
### List Case Evidence

#### Description

List case evidence in LogRhythm.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Case ID | String | N/A | Yes | Specify the ID of the case for which you want to return a list of evidence.  
Status Filter | CSV | N/A | No | Specify a comma-separated list of status filters for the evidence.Possible values: pending, completed, failed.If nothing is provided, the action return evidence from all statuses.  
Type Filter | CSV | N/A | No | Specify a comma-separated list of type filters for the evidence.Possible values: alarm, userEvents, log, note, file.If nothing is provided, the action returns evidence from all types.  
Max Evidences To Return | Integer | 50 | No | Specify the number of evidence to return.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    [
        {
            "number": 4,
            "dateCreated": "2021-07-31T11:00:40.2433333Z",
            "dateUpdated": "2021-07-31T11:00:40.2433333Z",
            "createdBy": {
                "number": -100,
                "name": "LogRhythm Administrator",
                "disabled": false
            },
            "lastUpdatedBy": {
                "number": -100,
                "name": "LogRhythm Administrator",
                "disabled": false
            },
            "type": "file",
            "status": "completed",
            "statusMessage": null,
            "text": "test",
            "pinned": false,
            "datePinned": null,
            "file": {
                "name": "UploadCustomListTemplate .csv",
                "size": 161
            }
        }
    ]
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If the_ ****_200 status code is reported (is_success=true):_ "Successfully listed evidence related to the case with ID {ID} in LogRhythm."If no evidence is available (is_success=false): "No evidence was found for the case with ID {ID} in LogRhythm."**The action should fail and stop a playbook execution:**___If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "List Case Evidence". Reason: {0}''.format(error.Stacktrace)_If the 404 status code is reported:_ "Error executing action "List Case Evidence". Reason: {0}''.format(message)_If an invalid value is provided for the "Status" parameter:_ "Error executing action "List Case Evidence". Reason: invalid values provided in the parameter "Status Filter": {invalid value}. Possible values: pending, completed, failed._If an invalid value is provided for the "Type" parameter:_ "Error executing action "List Case Evidence". Reason: invalid values provided in the parameter "Type": {invalid value}. Possible values: alarm, userEvents, log, note, file. | General  
Case Wall | **Case {case id} Evidence** TypeStatusContext |   
  
### Add Alarm To Case

#### Description

Add an alarm to the case in LogRhythm.

#### Parameter

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Case ID | String | N/A | Yes | Specify the ID of the case to which you want to add alarms.  
Alarm IDs | CSV | N/A | Yes | Specify a comma-separated list of alarms that need to be added to the case.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    [
        {
            "number": 23,
            "dateCreated": "2021-08-11T09:02:17.0066667Z",
            "dateUpdated": "2021-08-11T09:02:17.0066667Z",
            "createdBy": {
                "number": -100,
                "name": "LogRhythm Administrator",
                "disabled": false
            },
            "lastUpdatedBy": {
                "number": -100,
                "name": "LogRhythm Administrator",
                "disabled": false
            },
            "type": "alarm",
            "status": "completed",
            "statusMessage": null,
            "text": "",
            "pinned": false,
            "datePinned": null,
            "alarm": {
                "alarmId": 15298,
                "alarmDate": "2021-07-30T02:07:29.813+03:00",
                "alarmRuleId": 1000,
                "alarmRuleName": "AIE: ISO-27001: File Monitoring Event-File Changes",
                "dateInserted": "2021-07-30T02:07:29.82+03:00",
                "entityId": -100,
                "entityName": "Global Entity",
                "riskBasedPriorityMax": 1
            }
        },
        {
            "number": 24,
            "dateCreated": "2021-08-11T09:03:18.65Z",
            "dateUpdated": "2021-08-11T09:03:18.65Z",
            "createdBy": {
                "number": -100,
                "name": "LogRhythm Administrator",
                "disabled": false
            },
            "lastUpdatedBy": {
                "number": -100,
                "name": "LogRhythm Administrator",
                "disabled": false
            },
            "type": "alarm",
            "status": "completed",
            "statusMessage": null,
            "text": "",
            "pinned": false,
            "datePinned": null,
            "alarm": {
                "alarmId": 15297,
                "alarmDate": "2021-07-30T02:07:28.353+03:00",
                "alarmRuleId": 1419,
                "alarmRuleName": "AIE: CCF: FIM General Activity",
                "dateInserted": "2021-07-30T02:07:29.82+03:00",
                "entityId": 1,
                "entityName": "Primary Site",
                "riskBasedPriorityMax": 0
            }
        }
    ]
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If the_ ****_201 status code is reported (is_success=true):_ "Successfully added alarm evidence related to the case with ID {ID} in LogRhythm."_If the 200 status code is reported (is_success=true):_ "All of the provided alarm evidence was already a part of the case with ID {ID} in LogRhythm."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Add Alarm To Case". Reason: {0}''.format(error.Stacktrace)_If the 404 status code is reported:_ "Error executing action "Add Alarm To Case". Reason: {0}''.format(message or details) | General  
  
### Attach File To Case

#### Description

Attach a file to the case in LogRhythm.

**Note:** This action runs as async. Adjust the script timeout value in the Google SecOps IDE for the action as needed.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Case ID | String | N/A | Yes | Specify the ID of the case to which you want to attach files.  
File Paths | CSV | N/A | Yes | Specify a comma-separate list of absolute file paths.  
Note | String | N/A | No | Specify a note that should be added to the case alongside the file.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    [
        {
            "number": 26,
            "dateCreated": "2021-08-11T09:17:33.91Z",
            "dateUpdated": "2021-08-11T09:17:33.91Z",
            "createdBy": {
                "number": -100,
                "name": "LogRhythm Administrator",
                "disabled": false
            },
            "lastUpdatedBy": {
                "number": -100,
                "name": "LogRhythm Administrator",
                "disabled": false
            },
            "type": "file",
            "status": "completed",
            "statusMessage": null,
            "text": "",
            "pinned": false,
            "datePinned": null,
            "file": {
                "name": "Get Deep Visibility Query Result_JsonResultSample.json",
                "size": 4979
            }
        }
    ]
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If completed for one file_ ****_path (is_success=true):_ "Successfully added the following files to the case with ID {ID} in LogRhythm."___If failed for one filepath (is_success= true):_ "Action wasn't able to add the following files to the case with ID {ID} in LogRhythm: {failed file paths}".___If failed for all file paths (is_success=false): "_ No files were added to the case with ID {ID} in LogRhythm."**The action should fail and stop a playbook execution:**___If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Attach File To Case". Reason: {0}''.format(error.Stacktrace)_If the 404 status code is reported:_ "Error executing action "Attach File To Case". Reason: {0}''.format(message)_If ran into a timeout:_ "Error executing action "Attach File To Case". Reason: action ran into a timeout. The following files are still processing: {pending files}. Please increase the timeout in IDE. Note: adding the same file will create a separate entry in LogRhythm. | General  
  
### Add Note To Case

#### Description

Add a note to the case in LogRhythm.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Case ID | String | N/A | Yes | Specify the ID of the case to which you want to add a note.  
Note | String | N/A | Yes | Specify a note that should be added to the case.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "number": 29,
        "dateCreated": "2021-08-11T12:21:11.5547306Z",
        "dateUpdated": "2021-08-11T12:21:11.5547306Z",
        "createdBy": {
            "number": -100,
            "name": "LogRhythm Administrator",
            "disabled": false
        },
        "lastUpdatedBy": {
            "number": -100,
            "name": "LogRhythm Administrator",
            "disabled": false
        },
        "type": "note",
        "status": "completed",
        "statusMessage": null,
        "text": "asdasd",
        "pinned": false,
        "datePinned": null
    }
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If the 201 status code is reported (is_success=true):_ "Successfully added a note to the case with ID {ID} in LogRhythm."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Add Note To Case". Reason: {0}''.format(error.Stacktrace)_If the 404 status code is reported:_ "Error executing action "Add Note To Case". Reason: {0}''.format(message) | General  
  
### Create Case

#### Description

Create a case in LogRhythm.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Name | String | N/A | Yes | Specify the name for the case.  
Priority | DDL | 1Possible Values:

  * 1
  * 2
  * 3
  * 4
  * 5

| Yes | Specify the priority for the case.  
Due Date | String | N/A | No | Specify the due date for the case. Format: ISO 8601Example: 2021-04-23T12:38Z  
Description | String | N/A | No | Specify a description for the case.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "id": "BA210B5A-0E4F-4E07-A770-8C24FB82747A",
        "number": 2,
        "externalId": "",
        "dateCreated": "2021-08-11T12:37:42.8942168Z",
        "dateUpdated": "2021-08-11T12:37:42.8942168Z",
        "dateClosed": null,
        "owner": {
            "number": -100,
            "name": "LogRhythm Administrator",
            "disabled": false
        },
        "lastUpdatedBy": {
            "number": -100,
            "name": "LogRhythm Administrator",
            "disabled": false
        },
        "name": "System Compromise",
        "status": {
            "name": "Created",
            "number": 1
        },
        "priority": 1,
        "dueDate": "2019-08-24T14:15:22Z",
        "resolution": null,
        "resolutionDateUpdated": null,
        "resolutionLastUpdatedBy": null,
        "summary": "Investigated a potential system compromise. More details at http://example.com/.",
        "entity": {
            "number": -100,
            "name": "Global Entity",
            "fullName": "Global Entity"
        },
        "collaborators": [
            {
                "number": -100,
                "name": "LogRhythm Administrator",
                "disabled": false
            }
        ],
        "tags": []
    }
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**___If the 201 status code is reported (is_success=true):_ "Successfully created case {number} in LogRhythm."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Create Case". Reason: {0}''.format(error.Stacktrace)_If the 404 status code is reported:_ "Error executing action "Create Case". Reason: {0}''.format(message) | General  
  
### Update Case

#### Description

Update a case in LogRhythm.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Case ID | String | N/A | Yes | Specify the ID of the case that needs to be updated.  
Name | String | N/A | No | Specify a new name for the case.  
Priority | DDL | Select OnePossible Values:

  * 1
  * 2
  * 3
  * 4
  * 5

| No | Specify a new priority for the case.  
Due Date | String | N/A | No | Specify a new due date for the case. Format: ISO 8601 Example: 2021-04-23T12:38Z  
Description | String | N/A | No | Specify a new description for the case.  
Resolution | String | N/A | No | Specify how the case is resolved.  
Status | DDL | Select OnePossible Values:

  * Created
  * Completed
  * Incident
  * Mitigated
  * Resolved

| No | Specify the new status for the case.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "id": "BA210B5A-0E4F-4E07-A770-8C24FB82747A",
        "number": 2,
        "externalId": "",
        "dateCreated": "2021-08-11T12:37:42.8942168Z",
        "dateUpdated": "2021-08-11T12:48:52.9765558Z",
        "dateClosed": null,
        "owner": {
            "number": -100,
            "name": "LogRhythm Administrator",
            "disabled": false
        },
        "lastUpdatedBy": {
            "number": -100,
            "name": "LogRhythm Administrator",
            "disabled": false
        },
        "name": "System Compromise",
        "status": {
            "name": "Created",
            "number": 1
        },
        "priority": 1,
        "dueDate": "2019-08-24T14:15:22Z",
        "resolution": null,
        "resolutionDateUpdated": null,
        "resolutionLastUpdatedBy": null,
        "summary": "Investigated a potential system compromise. More details at http://example.com/.",
        "entity": {
            "number": -100,
            "name": "Global Entity",
            "fullName": "Global Entity"
        },
        "collaborators": [
            {
                "number": -100,
                "name": "LogRhythm Administrator",
                "disabled": false
            }
        ],
        "tags": []
    }
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If_ ****_the 201 status code is reported (is_success=true):_ "Successfully updated case {ID} in LogRhythm."**The action should fail and stop a playbook execution:******_If_ ****_a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Update Case". Reason: {0}''.format(error.Stacktrace)"_If the 404 status code is reported:_ "Error executing action "Update Case". Reason: {0}''.format(message)_If status code is 400:_ "Error executing action "Update Case". Reason: {0}''.format(validationErrors)"_If the "Status" or "Priority" parameter is set to "Select One" and none of the other values are provided:_ "Error executing action "Update Case". Reason: at least one of the action parameters should have a provided value." | General  
  
### Download Case Files

#### Description

Download files related to the case in LogRhythm.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Case ID | String | N/A | Yes | Specify the ID of the case from which you want to download files.  
Download Folder Path | String | N/A | Yes | Specify the path to the folder, where you want to store the case files.  
Overwrite | Bool | False | Yes | If enabled, the action overwrites the file with the same name.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {"absolute_file_paths": ["file_path_1","file_path_2"]}
    ``` ##### Entity
    Enrichment
    
    N/A
    
    #####  Insights
    
    N/A
    
    #####  Case Wall
    
    <table>
    <thead>
    <tr>
    <th><strong>Result type</strong></th>
    <th><strong>Value/Description</strong></th>
    <th><strong>Type</strong></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>Output message*</td>
    <td><p><strong>The action should not fail nor stop a playbook execution:</strong></p><p><strong></strong></p><p><em>If the</em> <strong></strong> <em>200 status code for all cases is reported (is_success=true):</em> "Successfully downloaded files related to case with ID {ID} in LogRhythm."</p><p></p><p><em>If no files are found (is_success=true): "</em>No related files were found for the case with ID {ID} in LogRhythm."</p><p></p><p><strong>The action should fail and stop a playbook execution:</strong></p><p><strong></strong></p><p><em>If a</em> <strong></strong> <em>fatal error, like wrong credentials, no connection to the server, other is reported:</em> "Error executing action "Download Case Files". Reason: {0}''.format(error.Stacktrace)"</p><p></p><p><em>If the 404 status code is reported:</em> "Error executing action "Download Case Files". Reason: {0}''.format(message)"</p><p></p><p><em>If a file with the same name already exists, but "Overwrite" is set to false:</em> "Error executing action "Download Case Files". Reason: files with path {0} already exist. Please delete the files or set "Overwrite" to true."</p></td>
    <td>General</td>
    </tr>
    </tbody>
    </table>
    
    ### List Entity Events
    
    #### Description
    
    List events related to entities in LogRhythm. Supported entities: Hostname, IP
    Address, User, CVE, Hash, URL.
    
    Note: This action runs as async. Adjust the script timeout value in the
    Google SecOps IDE for the action as needed.
    
    #### Parameters
    
    <table>
    <thead>
    <tr>
    <th><strong>Parameter Display Name</strong></th>
    <th><strong>Type</strong></th>
    <th><strong>Default Value</strong></th>
    <th><strong>Is Mandatory</strong></th>
    <th><strong>Description</strong></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>Time Frame</td>
    <td>DDL</td>
    <td><p>Last Hour</p><p><strong></strong></p><p>Possible Values: </p><ul><li>Last Hour</li><li>Last 6 Hours</li><li>Last 24 Hours</li><li>Last Week</li><li>Last Month</li><li>Custom</li></ul></td>
    <td>No</td>
    <td>Name of the watchlist from which you want to remove values.</td>
    </tr>
    <tr>
    <td>Start Time</td>
    <td>String</td>
    <td>N/A</td>
    <td>No</td>
    <td><p>Specify the start time for the results.</p><p></p><p>This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter. </p><p></p><p>Format: ISO 8601</p><p></p><p>Example: 2021-04-23T12:38Z</p></td>
    </tr>
    <tr>
    <td>End Time</td>
    <td>String</td>
    <td>N/A</td>
    <td>No</td>
    <td><p>Specify the end time for the results. </p><p></p><p>If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter uses current time.</p><p></p><p>Format: ISO 8601</p></td>
    </tr>
    <tr>
    <td>Sort Order</td>
    <td>DDL</td>
    <td><p>Datetime ASC <strong></strong> </p><p></p><p>Possible values:</p><ul><li>Datetime ASC</li><li>Datetime DESC</li><li>Risk ASC</li><li>RiskDESC</li></ul></td>
    <td>No</td>
    <td>Specify the sorting logic for the query.</td>
    </tr>
    <tr>
    <td>Max Events To Return</td>
    <td>Integer</td>
    <td>50</td>
    <td>No</td>
    <td>Specify the number of events to return.</td>
    </tr>
    </tbody>
    </table>
    
    #### Run On
    
    This action runs on the following entities:
    
    *   Hostname
    *   IP Address
    *   User
    *   CVE
    *   Hash
    *   URL
    
    #### Action Results
    
    #####  Script Result
    
    <table>
    <thead>
    <tr>
    <th><strong>Script Result Name</strong></th>
    <th><strong>Value Options</strong></th>
    <th><strong>Example</strong></th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td>is_success</td>
    <td>True/False</td>
    <td>is_success:False</td>
    </tr>
    </tbody>
    </table>
    
    #####  JSON Result
    
    ```json
    {
        "kBytes": 2521.025390625,
        "kBytesIn": 2500.0,
        "kBytesOut": 21.025390625,
        "outboundKBytes": 21.025390625,
        "impactedHostTotalKBytes": 2521.025390625,
        "keyField": "messageId",
        "count": 1,
        "classificationId": 3200,
        "classificationName": "Error",
        "classificationTypeName": "Operations",
        "commonEventName": "HTTP 504 : Server Error - Gateway Time-Out",
        "commonEventId": 8938,
        "direction": 3,
        "directionName": "External",
        "entityId": 2,
        "entityName": "EchoTestEntity",
        "rootEntityId": 2,
        "rootEntityName": "EchoTestEntity",
        "impactedEntityId": -100,
        "impactedEntityName": "Global Entity",
        "impactedHost": "192.0.2.11",
        "impactedInterface": "0",
        "impactedIp": "192.0.2.11",
        "impactedPort": 80,
        "impactedZoneName": "External",
        "indexedDate": 1629460029041,
        "insertedDate": 1629123439811,
        "logDate": 1629134239789,
        "logMessage": "CISCONGFW EVENT Ev_Id=436 Ev",
        "logSourceHost": "EchoTestHost",
        "logSourceHostId": 2,
        "logSourceHostName": "EchoTestHost",
        "logSourceId": 15,
        "logSourceName": "Echo_2_1000107",
        "logSourceType": 1000107,
        "logSourceTypeName": "Flat File - Cisco NGFW",
        "messageId": "23066",
        "messageTypeEnum": 2,
        "mpeRuleId": 1176829,
        "mpeRuleName": "HTTP 504 : Server Error : Gateway Timeout",
        "normalDate": 1629123439791,
        "normalDateMin": 1629123439791,
        "normalMsgDateMax": 1629123439791,
        "normalDateHour": 1629122400000,
        "originEntityId": -100,
        "originEntityName": "Global Entity",
        "originHostId": -1,
        "originHost": "192.0.2.12",
        "originInterface": "0",
        "originIp": "192.0.2.12",
        "originPort": 14042,
        "originZone": 3,
        "originZoneName": "External",
        "priority": 38,
        "process": "5",
        "processId": 300003,
        "protocolId": 6,
        "protocolName": "TCP",
        "serviceId": 1388,
        "serviceName": "HTTP",
        "portProtocol": "HTTP",
        "session": "436",
        "severity": "57",
        "url": "http://www.google.com/",
        "vendorMessageId": "504",
        "version": "2",
        "status": "504"
    }
    
    

##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If found data for one entity (is_success=true):_ "Successfully retrieved events for the following entities in LogRhythm: {entity.identifier}." _If failed for one entity (is_success=true):_ "Action wasn't able to retrieve events for the following entities in LogRhythm: {entity.identifier}."_If failed for all entities (is_success=false):_ "Action wasn't able to retrieve events for the provided entities in LogRhythm."_If no data for at least one entity (is_success=true):_ "No events were found for the following entities in LogRhythm: {entity.identifier}."_If no data for all entities (is_success=false):_ "No events were found for the provided entities in LogRhythm."_If ran into a timeout for one entity (is_success=true):_ "Action ran into a timeout during execution. Pending entities: {entities that didn't return data}. Please increase the action timeout in the IDE."_Async Message:_ "Waiting for events information for the following entities: {entity.identifier}"**The action should fail and stop a playbook execution:**_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "List Entity Events". Reason: {0}''.format(error.Stacktrace)"_If ran into a timeout for all entities (is_success=false):_ "Error executing action "List Entity Events". Reason: Action ran into a timeout during execution. No information about the events was retrieved for the provided entities. Please increase the action timeout in the IDE."_If the "Start Time" parameter is empty, when the "Time Frame" parameter is set to "Custom" (fail):_ "Error executing action "". Reason: "Start Time" should be provided, when "Custom" is selected in the "Time Frame" parameter."_If the "Start Time" parameter has greater value than the "End Time" parameter (fail):_ "Error executing action "". Reason: "End Time" should be later than "Start Time"._If max items to return is not greater than 0:_ "Error executing action "". Reason: "Max Events To Return" should be greater than 0. | General  
Case Wall Table | **Table Name:** {entity.identifier}**Table Columns:**

  * Classification: "classificationName" 
  * Event Name: "commonEventName" Date: Converted to ISO (insertedDate) 
  * Impacted Host: impactedHost 
  * Impacted IP: impactedIP Login: login Hash: hash URL: url 
  * Priority: priority CVE: CVE Origin 
  * Host: originHost
  * Origin IP: originIP 

**Note:** This column will be visible if there is at least one record with value. | Entity  
  
## Connectors

### LogRhythm Cases Connector

#### Description

Pull cases from LogRhythm.

#### Connector Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Product Field Name | String | N/A | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | event_type | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | **""** | No | Describes the name of the field where the environment name is stored.If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field.Default is .* to catch all and return the value unchanged.Used to allow the user to manipulate the environment field via regex logic.If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
Api Root | String | https://{IP}:8501 | Yes | API root of the LogRhythm instance.  
Api Token | Password | N/A | Yes | LogRhythm API token.  
Max Days Backwards | Integer | 1 | Yes | Number of days from where to fetch cases.  
Lowest Priority To Fetch | Integer | N/A | No | The lowest priority that needs to be used to fetch cases.If nothing is provided, cases with all priorities are ingested.Possible values: from 1 to 5.  
Alerts Count Limit | Integer | 10 | Yes | Number of cases to process per one connector iteration.  
CA Certificate File | String | N/A | No | Base 64 encoded CA certificate file.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist is used as a blacklist.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verify that the SSL certificate for the connection to the LogRhythm server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

Connector supports Proxy.

### LogRhythm - Rest API Alarms Connector

#### Description

Pull alarms from LogRhythm using Rest API.

**Note:** This connector is only supported for Logrhythm version 7.7+. The "alarmRuleName" parameter is used in the whitelist.

#### Configure LogRhythm - Rest API Alarms Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | classificationTypeName | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field through regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://{IP}:8501 | Yes | API root of the LogRhythm instance.  
API Token | Password | N/A | Yes | LogRhythm API token.  
Max Hours Backwards | Integer | 1 | No | Number of hours from where to fetch alerts.  
Max Alarms To Fetch | Integer | 10 | No | Number of alerts to process per one connector iteration.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist is used as a blacklist.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verify that the SSL certificate for the connection to the LogRhythm server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

The Connector supports Proxy.

## Jobs

### Sync Case Comments

#### Description

This job synchronizes comments in LogRhythm cases and Google SecOps cases.

**Note:** The job only synchronizes the LogRhythm cases with the "Created", "Incident" and "Mitigated" statuses.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Api Root | String | https://{IP}:8501 | Yes | API root of the LogRhythm instance.  
Api Token | Password | N/A | Yes | LogRhythm API token.  
CA Certificate File | String | N/A | No | Base 64 encoded CA certificate file.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify that the SSL certificate for the connection to the LogRhythm server is valid.  
  
### Sync Closed Cases

#### Description

This job synchronizes closed LogRhythm cases and Google SecOps alerts.

**Note:** In LogRhythm, the "Completed" and "Resolved" statuses are treated as closed.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Api Root | String | https://{IP}:8501 | Yes | API root of the LogRhythm instance.  
Api Token | Password | N/A | Yes | LogRhythm API token.  
CA Certificate File | String | N/A | No | Base 64 encoded CA certificate file.  
Max Hours Backwards | Integer | 24 | No | Specify the number of hours backwards to synchronize statuses.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify that the SSL certificate for the connection to the LogRhythm server is valid.  
  
### Sync Alarm Comments

#### Description

This job synchronizes comments in LogRhythm alarms and Google SecOps cases.

**Note:** The job only synchronizes the LogRhythm alarms with the "New", "Open", "Working" and "Escalated" statuses.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Api Root | String | https://{IP}:8501 | Yes | API root of the LogRhythm instance.  
Api Token | Password | N/A | Yes | LogRhythm API token.  
CA Certificate File | String | N/A | No | Base 64 encoded CA certificate file.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify that the SSL certificate for the connection to the LogRhythm server is valid.  
  
### Sync Closed Alarms

#### Description

This job synchronizes closed LogRhythm alarms and Google SecOps alerts.

**Note:** In LogRhythm, the "Closed", "Closed False Alarm", "Closed Resolved", "Closed Unresolved", "Closed Reported", "Closed Monitor" statuses are treated as closed.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Api Root | String | https://{IP}:8501 | Yes | API root of the LogRhythm instance.  
Api Token | Password | N/A | Yes | LogRhythm API token.  
CA Certificate File | String | N/A | No | Base 64 encoded CA certificate file.  
Max Hours Backwards | Integer | 24 | No | Specify the number of hours backwards to synchronize statuses.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify that that the SSL certificate for the connection to the LogRhythm server is valid.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
