---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/rapid7-insightidr/
title: Rapid7 InsightIDR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:28.667708+00:00
---

# Rapid7 InsightIDR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/rapid7-insightidr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Rapid7 InsightIDR

This document provides guidance on how to integrate Rapid7 InsightIDR with Google SecOps.

## Use Cases

Use InsightIDR data for enrichment of processed Google Security Operations alert.

## Configure Rapid7 InsightIDR integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://[region].api.insight.rapid7.com | Yes | Specify API Root to use for connection.  
API Key | Password | N/A | Yes | Specify API Key to use for connection.  
Verify SSL | Checkbox | Checked | No | Specify if certificate that is configured on the api root should be validated.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to the Rapid7 InsightIDR service with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:****if successful:** print "Successfully connected to the Rapid7 InsightIDR service with the provided connection parameters!"******The action should fail and stop a playbook execution:****if critical error, like wrong credentials or lost connectivity:** print "Failed to connect to the Rapid7 InsightIDR service! Error is {0}".format(exception.stacktrace) | General  
  
### List Investigations

#### Description

List Rapid7 InsightIDR investigations based on the specified action input parameters.

**Note:** Action is not working with Google SecOps entities, only with action input parameters.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Time Frame | Integer | 4 | No | Specify a time frame in hours for which to fetch findings.  
Record limit | Integer | 20 | No | Specify how many records can be returned by the action.  
Include Closed Investigations? | Checkbox | Unchecked | No | Specify whether to include closed investigations in results or not.  
  
#### Run On

This action doesn't run on entities.

##### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "data": [
            {
                "id": "8ec8e324-4522-4a6e-9838-81496a0cadb0",
                "title": "Process reported as malicious ran on asset hw-srv2016-rpd7.rapid7.local",
                "status": "OPEN",
                "source": "ALERT",
                "assignee": {
                    "name": "Tip Labops",
                    "email": "tip.labops@siemplify.co"
                },
                "alerts": [
                    {
                        "type": "Malicious Hash On Asset",
                        "type_description": "A malicious hash was found on an asset.",
                        "first_event_time": "2020-12-02T13:16:14.197Z"
                    }
                ],
                "created_time": "2020-12-02T13:18:16.758Z"
            },
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Action should not fail and not stop playbook execution:****if successful:** print "Rapid7 InsightIDR investigations found"**if is_success=False, for example no investigations were found:** print "No investigations were returned."****  
**Action should fail and stop playbook execution:**  
**if critical error, like wrong credentials or lost connectivity:** print "Failed to connect to the Rapid7 InsightIDR service! Error is {0}".format(exception.stacktrace) | General  
CSV | **Table Name:** Rapid7 InsightIDR Investigations**Table Columns:** TitleStatusSourceAssignee (Assignee.email)Alerts (CSV list of alerts.type values)Created Time | General  
  
### Set Investigation Status

#### Description

Set the status for the specific Rapid7 InsightIDR investigation.

**Note:** Action is not working with Google SecOps entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Investigation ID | String | N/A | Yes | ID of investigation to update status for. ID should be in the format like 8ec8e324-4522-4a6e-9838-81496a0cadb0  
Status | DDL | " " | Yes | New Status of investigation.  
  
#### Run On

This action doesn't run on entities.

##### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "id": "8ec8e324-4522-4a6e-9838-81496a0cadb0",
        "title": "Process reported as malicious ran on asset hw-srv2016-rpd7.rapid7.local",
        "status": "CLOSED",
        "source": "ALERT",
        "assignee": {
            "name": "Tip Labops",
            "email": "tip.labops@siemplify.co"
        },
        "alerts": [
            {
                "type": "Malicious Hash On Asset",
                "type_description": "A malicious hash was found on an asset.",
                "first_event_time": "2020-12-02T13:16:14.197Z"
            }
        ],
        "created_time": "2020-12-02T13:18:16.758Z"
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Action should not fail and not stop playbook execution:****if successful:** print "Rapid7 InsightIDR Investigation {0} status changed to {1}".format(investigation_id, status)**if is_success=False, for example investigation with provided id was not found:** print "Failed to update Rapid7 InsightIDR investigation status. Error is: {0}".format(error from response)****  
**Action should fail and stop playbook execution:**  
**if critical error, like wrong credentials or lost connectivity:** print "Failed to connect to the Rapid7 InsightIDR service! Error is {0}".format(exception.stacktrace) | General  
  
### Set Investigation Assignee

#### Description

Set the assignee for the specific Rapid7 InsightIDR investigation.

**Note:** Action is not working with Google SecOps entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Investigation ID | String | N/A | Yes | ID of investigation to update status for. ID should be in the format like 8ec8e324-4522-4a6e-9838-81496a0cadb0.  
Assignee email | String | N/A | Yes | Email of a new assignee of investigation.  
  
#### Run On

This action doesn't run on entities.

##### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "id": "8ec8e324-4522-4a6e-9838-81496a0cadb0",
        "title": "Process reported as malicious ran on asset hw-srv2016-rpd7.rapid7.local",
        "status": "OPEN",
        "source": "ALERT",
        "assignee": {
            "name": "Tip Labops",
            "email": "tip.labops@siemplify.co"
        },
        "alerts": [
            {
                "type": "Malicious Hash On Asset",
                "type_description": "A malicious hash was found on an asset.",
                "first_event_time": "2020-12-02T13:16:14.197Z"
            }
        ],
        "created_time": "2020-12-02T13:18:16.758Z"
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Action should not fail and not stop playbook execution:****if successful:** print "Rapid7 InsightIDR Investigation {0} assignee changed to {1}".format(investigation_id, assignee)**if is_success=False, for example investigation with provided id was not found:** print "Failed to update Rapid7 InsightIDR investigation assignee. Error is: {0}".format(error from response)****  
**Action should fail and stop playbook execution:**  
**if critical error, like wrong credentials or lost connectivity:** print "Failed to connect to the Rapid7 InsightIDR service! Error is {0}".format(exception.stacktrace) | General  
  
### List Saved Queries

#### Description

List Rapid7 InsightIDR saved queries.

**Note:** Action is not working with Google SecOps entities, only with action input parameters.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Record limit | Integer | 20 | No | Specify how many records can be returned by the action.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "saved_queries": [
            {
                "id": "00000000-0003-71fd-0000-000000000000",
                "name": "test3",
                "leql": {
                    "statement": "where(destination_asset = \"hw-srv2016-rpd7.rapid7.local\" AND destination_user = \"administrator\")",
                    "during": {
                        "time_range": "Last 1 Hour",
                        "to": null,
                        "from": null
                    }
                },
                "logs": [
                    "a2ba0890-8ddd-444a-9e15-2dc488f0c398",
                    "043584c7-113e-4ffc-a6b8-ea0be1a4f501",
                    "3c0fc9f7-a7c4-4ff3-b221-d60d260bab22",
                    "9eedf8cd-cf85-4ca3-9ac5-e329b523cc12",
                    "3e251f54-71a3-4d19-84dd-b56d8ad8c49c"
                ]
            },
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Action should not fail and not stop playbook execution:****if successful:** print "Rapid7 InsightIDR saved queries found"**if is_success=True, but no saved queries were found:** print "No saved queries were returned."****  
**Action should fail and stop playbook execution:**  
**if critical error, like wrong credentials or lost connectivity:** print "Failed to connect to the Rapid7 InsightIDR service! Error is {0}".format(exception.stacktrace) | General  
CSV | **Table Name:** Rapid7 InsightIDR Saved Queries**Table Columns:** ID  
NameStatementTime RangeStart TimeEnd TimeLogs | General  
  
### Create Saved Query

#### Description

Create Rapid7 InsightIDR saved query based on the specified action input parameters.

**Note:** Action is not working with Google SecOps entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Name | String | N/A | Yes | Name for the new saved query.  
Statement | String | N/A | Yes | A statement to execute in query, should follow LEQL syntax, for example: where(foo=bar).  
Time Frame | Integer | 4 | Yes | Specify a time frame in hours for which query should fetch data.  
Logs | String | N/A | No | Log names query should execute against. Parameter accepts multiple values as a comma separated string.  
  
##### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "saved_query": {
            "id": "00000000-0003-7216-0000-000000000000",
            "name": "MySearch4",
            "leql": {
                "statement": "where(bar=foo)",
                "during": {
                    "time_range": null,
                    "to": 1450557608000,
                    "from": 1450557604000
                }
            },
            "logs": [
                "a2ba0890-8ddd-444a-9e15-2dc488f0c398",
                "043584c7-113e-4ffc-a6b8-ea0be1a4f501"
            ]
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* |  **Action should not fail and not stop playbook execution:****if successful:** print "New Rapid7 InsightIDR saved query created: {0}".format(new query id from response)**if is_success=False, for example syntax of query was incorrect:** print "Failed to create Rapid7 InsightID saved query. Error is: {0}".format(error from response)****  
**Action should fail and stop playbook execution:**  
**if critical error, like wrong credentials or lost connectivity:** print "Failed to connect to the Rapid7 InsightIDR service! Error is {0}".format(exception.stacktrace) | General  
  
### Delete Saved Query

#### Description

Delete Rapid7 InsightIDR saved query.

**Note:** Action is not working with Google SecOps entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Saved Query ID | String | N/A | Yes | ID of the saved query to delete in the format 00000000-0003-7218-0000-000000000000  
  
##### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* |  **Action should not fail and not stop playbook execution:****if successful:** print "Rapid7 InsightIDR saved query {0} was deleted successfully".format(query id)**if is_success=False, for example wrong query id was provided:** print "Failed to delete Rapid7 InsightID saved query. Error is: {0}".format(error from response)****  
**Action should fail and stop playbook execution:**  
**if critical error, like wrong credentials or lost connectivity:** print "Failed to connect to the Rapid7 InsightIDR service! Error is {0}".format(exception.stacktrace) | General  
  
### Run Saved Query

#### Description

Run a Rapid7 InsightIDR saved query.

**Note:** Action is not working with Google SecOps entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Saved Query ID | String | N/A | Yes | ID of the saved query to delete in the format 00000000-0003-7218-0000-000000000000  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "logs": [
            "a2ba0890-8ddd-444a-9e15-2dc488f0c398",
            "043584c7-113e-4ffc-a6b8-ea0be1a4f501",
            "3c0fc9f7-a7c4-4ff3-b221-d60d260bab22",
            "9eedf8cd-cf85-4ca3-9ac5-e329b523cc12",
            "3e251f54-71a3-4d19-84dd-b56d8ad8c49c"
        ],
        "events": [
            {
                "sequence_number": 3237167368573841408,
                "timestamp": 1607411688338,
                "labels": [],
                "log_id": "3e251f54-71a3-4d19-84dd-b56d8ad8c49c",
                "message": "{\"timestamp\":\"2020-12-08T07:14:32.408Z\",\"source_asset\":\"hw-srv2016-rpd7.rapid7.local\",\"destination_asset\":\"hw-srv2016-rpd7.rapid7.local\",\"source_asset_address\":\"172.30.202.20\",\"destination_asset_address\":\"172.30.202.20\",\"destination_user\":\"administrator\",\"destination_account\":\"administrator\",\"destination_domain\":\"rapid7\",\"destination_account_sid\":\"S-1-5-21-3325036707-3113295233-4269388844-500\",\"logon_type\":\"NETWORK\",\"result\":\"SUCCESS\",\"new_authentication\":\"false\",\"service\":\"ntlmssp\",\"source_json\":{\"eventCode\":4624,\"computerName\":\"HW-SRV2016-RPD7.rapid7.local\",\"insertionStrings\":[\"S-1-0-0\",\"-\",\"-\",\"0x0\",\"S-1-5-21-3325036707-3113295233-4269388844-500\",\"Administrator\",\"RAPID7\",\"0xd071a3b\",\"3\",\"NtLmSsp \",\"NTLM\",\"NEXPOSE\",\"{00000000-0000-0000-0000-000000000000}\",\"-\",\"NTLM V2\",\"128\",\"0x0\",\"-\",\"172.30.202.20\",\"61228\",\"%%1833\",\"-\",\"-\",\"-\",\"%%1843\",\"0x0\",\"%%1842\"],\"timeGenerated\":\"20201208071432.408008-000\"}}",
                "links": [
                    {
                        "rel": "Context",
                        "href": "https://eu.api.insight.rapid7.com/log_search/query/context/3237167368573841408?per_page=50&timestamp=1607411688338&log_keys=a2ba0890-8ddd-444a-9e15-2dc488f0c398%3A043584c7-113e-4ffc-a6b8-ea0be1a4f501%3A3c0fc9f7-a7c4-4ff3-b221-d60d260bab22%3A9eedf8cd-cf85-4ca3-9ac5-e329b523cc12%3A3e251f54-71a3-4d19-84dd-b56d8ad8c49c&context_type=SURROUND"
                    }
                ],
                "sequence_number_str": "3237167368573841408"
            },
            {
                "sequence_number": 3237167368573845504,
                "timestamp": 1607411688338,
                "labels": [],
                "log_id": "3e251f54-71a3-4d19-84dd-b56d8ad8c49c",
                "message": "{\"timestamp\":\"2020-12-08T07:14:31.433Z\",\"source_asset\":\"hw-srv2016-rpd7.rapid7.local\",\"destination_asset\":\"hw-srv2016-rpd7.rapid7.local\",\"source_asset_address\":\"172.30.202.20\",\"destination_asset_address\":\"172.30.202.20\",\"destination_user\":\"administrator\",\"destination_account\":\"administrator\",\"destination_domain\":\"rapid7\",\"destination_account_sid\":\"S-1-5-21-3325036707-3113295233-4269388844-500\",\"logon_type\":\"NETWORK\",\"result\":\"SUCCESS\",\"new_authentication\":\"false\",\"service\":\"ntlmssp\",\"source_json\":{\"eventCode\":4624,\"computerName\":\"HW-SRV2016-RPD7.rapid7.local\",\"insertionStrings\":[\"S-1-0-0\",\"-\",\"-\",\"0x0\",\"S-1-5-21-3325036707-3113295233-4269388844-500\",\"Administrator\",\"RAPID7\",\"0xd071708\",\"3\",\"NtLmSsp \",\"NTLM\",\"NEXPOSE\",\"{00000000-0000-0000-0000-000000000000}\",\"-\",\"NTLM V2\",\"128\",\"0x0\",\"-\",\"172.30.202.20\",\"61226\",\"%%1833\",\"-\",\"-\",\"-\",\"%%1843\",\"0x0\",\"%%1842\"],\"timeGenerated\":\"20201208071431.433772-000\"}}",
                "links": [
                    {
                        "rel": "Context",
                        "href": "https://eu.api.insight.rapid7.com/log_search/query/context/3237167368573845504?per_page=50&timestamp=1607411688338&log_keys=a2ba0890-8ddd-444a-9e15-2dc488f0c398%3A043584c7-113e-4ffc-a6b8-ea0be1a4f501%3A3c0fc9f7-a7c4-4ff3-b221-d60d260bab22%3A9eedf8cd-cf85-4ca3-9ac5-e329b523cc12%3A3e251f54-71a3-4d19-84dd-b56d8ad8c49c&context_type=SURROUND"
                    }
                ],
                "sequence_number_str": "3237167368573845504"
            },
            {
                "sequence_number": 3237167368573849600,
                "timestamp": 1607411688338,
                "labels": [],
                "log_id": "3e251f54-71a3-4d19-84dd-b56d8ad8c49c",
                "message": "{\"timestamp\":\"2020-12-08T07:14:31.430Z\",\"source_asset\":\"hw-srv2016-rpd7.rapid7.local\",\"destination_asset\":\"hw-srv2016-rpd7.rapid7.local\",\"source_asset_address\":\"172.30.202.20\",\"destination_asset_address\":\"172.30.202.20\",\"destination_user\":\"administrator\",\"destination_account\":\"administrator\",\"destination_domain\":\"rapid7\",\"destination_account_sid\":\"S-1-5-21-3325036707-3113295233-4269388844-500\",\"logon_type\":\"NETWORK\",\"result\":\"SUCCESS\",\"new_authentication\":\"false\",\"service\":\"ntlmssp\",\"source_json\":{\"eventCode\":4624,\"computerName\":\"HW-SRV2016-RPD7.rapid7.local\",\"insertionStrings\":[\"S-1-0-0\",\"-\",\"-\",\"0x0\",\"S-1-5-21-3325036707-3113295233-4269388844-500\",\"Administrator\",\"RAPID7\",\"0xd0716eb\",\"3\",\"NtLmSsp \",\"NTLM\",\"NEXPOSE\",\"{00000000-0000-0000-0000-000000000000}\",\"-\",\"NTLM V2\",\"128\",\"0x0\",\"-\",\"172.30.202.20\",\"61225\",\"%%1833\",\"-\",\"-\",\"-\",\"%%1843\",\"0x0\",\"%%1842\"],\"timeGenerated\":\"20201208071431.430750-000\"}}",
                "links": [
                    {
                        "rel": "Context",
                        "href": "https://eu.api.insight.rapid7.com/log_search/query/context/3237167368573849600?per_page=50&timestamp=1607411688338&log_keys=a2ba0890-8ddd-444a-9e15-2dc488f0c398%3A043584c7-113e-4ffc-a6b8-ea0be1a4f501%3A3c0fc9f7-a7c4-4ff3-b221-d60d260bab22%3A9eedf8cd-cf85-4ca3-9ac5-e329b523cc12%3A3e251f54-71a3-4d19-84dd-b56d8ad8c49c&context_type=SURROUND"
                    }
                ],
                "sequence_number_str": "3237167368573849600"
            },
            {
                "sequence_number": 3237167368573853696,
                "timestamp": 1607411688338,
                "labels": [],
                "log_id": "3e251f54-71a3-4d19-84dd-b56d8ad8c49c",
                "message": "{\"timestamp\":\"2020-12-08T07:14:31.427Z\",\"source_asset\":\"hw-srv2016-rpd7.rapid7.local\",\"destination_asset\":\"hw-srv2016-rpd7.rapid7.local\",\"source_asset_address\":\"172.30.202.20\",\"destination_asset_address\":\"172.30.202.20\",\"destination_user\":\"administrator\",\"destination_account\":\"administrator\",\"destination_domain\":\"rapid7\",\"destination_account_sid\":\"S-1-5-21-3325036707-3113295233-4269388844-500\",\"logon_type\":\"NETWORK\",\"result\":\"SUCCESS\",\"new_authentication\":\"false\",\"service\":\"ntlmssp\",\"source_json\":{\"eventCode\":4624,\"computerName\":\"HW-SRV2016-RPD7.rapid7.local\",\"insertionStrings\":[\"S-1-0-0\",\"-\",\"-\",\"0x0\",\"S-1-5-21-3325036707-3113295233-4269388844-500\",\"Administrator\",\"RAPID7\",\"0xd0716d1\",\"3\",\"NtLmSsp \",\"NTLM\",\"NEXPOSE\",\"{00000000-0000-0000-0000-000000000000}\",\"-\",\"NTLM V2\",\"128\",\"0x0\",\"-\",\"172.30.202.20\",\"61224\",\"%%1833\",\"-\",\"-\",\"-\",\"%%1843\",\"0x0\",\"%%1842\"],\"timeGenerated\":\"20201208071431.427604-000\"}}",
                "links": [
                    {
                        "rel": "Context",
                        "href": "https://eu.api.insight.rapid7.com/log_search/query/context/3237167368573853696?per_page=50&timestamp=1607411688338&log_keys=a2ba0890-8ddd-444a-9e15-2dc488f0c398%3A043584c7-113e-4ffc-a6b8-ea0be1a4f501%3A3c0fc9f7-a7c4-4ff3-b221-d60d260bab22%3A9eedf8cd-cf85-4ca3-9ac5-e329b523cc12%3A3e251f54-71a3-4d19-84dd-b56d8ad8c49c&context_type=SURROUND"
                    }
                ],
                "sequence_number_str": "3237167368573853696"
            },
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Action should not fail and not stop playbook execution:****if successful:** print "Rapid7 InsightIDR saved query {0} executed successfully".format(query id)**if is_success=False, for example wrong query id was provided:** print "Failed to delete Rapid7 InsightID saved query. Error is: {0}".format(error from response)******Action should fail and stop playbook execution:**  
**if critical error, like wrong credentials or lost connectivity:** print "Failed to connect to the Rapid7 InsightIDR service! Error is {0}".format(exception.stacktrace) | General  
  
### Update Investigation

#### Description

Update investigation in Rapid7 InsightIDR.

**Note:** This action is built using API endpoints that are in preview release.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Investigation ID | String | NA | Yes | Specify the ID of the investigation that needs to be updated.  
Status | DDL | Select One Possible Values:

  * Open
  * Investigating
  * Closed

| No | Specify the status for the investigation.  
Saved Query ID | String | Select One Possible Values:

  * Benign
  * Malicious
  * Not Applicable

| No | Specify the disposition for the investigation.  
  
##### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "rrn": "rrn:investigation:eu:d16635a5-8a81-410c-8c33-67a4fbf26eb4:investigation:PAQBBKR4941D",
        "organization_id": "d16635a5-8a81-410c-8c33-67a4fbf26eb4",
        "title": "Suspicious Process - Malicious Hash On Asset",
        "source": "ALERT",
        "status": "OPEN",
        "priority": "HIGH",
        "last_accessed": "2022-10-12T13:08:37.650Z",
        "created_time": "2022-10-12T13:08:37.650Z",
        "disposition": "NOT_APPLICABLE",
        "assignee": null,
        "first_alert_time": "2022-10-12T13:08:37.643Z",
        "latest_alert_time": "2022-10-12T13:11:43.018Z"
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* |  **Action should not fail and not stop playbook execution:** **If returned information (is_success=true):** "Successfully updated investigation with ID {investigation id} in Rapid7 InsightIDR." **Action should fail and stop playbook execution:** **If a critical error, like wrong credentials, no connection to the server, other is reported:** "Error executing action "Update Investigation". Reason: {0}''.format(error.Stacktrace)" **If alert not found:** Error executing action "Update Investigation". Reason: investigation with ID {investigation id} wasn't found in Rapid7 InsightIDR. Please check the spelling." **If "Status" and"Disposition" is "Select One":** "Error executing action "Update Investigation". Reason: at least one of the "Status" or "Disposition" parameters should have a value ." | General  
  
## Connectors

### Rapid7 InsightIDR - Investigations Connector

#### Description

This connector is built using API endpoints that are in preview release. Pull information about investigation from Rapid7 InsightIDR.

**Note:** Dynamic list filter works with the "title" parameter.

#### Connector parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | data_type | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | source | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name  
| String | "" | No | Describes the name of the field where the environment name is stored.If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern  
| String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field.Default is .* to catch all and return the value unchanged.Used to allow the user to manipulate the environment field via regex logic.If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://{instance}.api.insight.rapid7.com | Yes | API root of the Rapid7 InsightIDR instance.  
API Key | String | N/A | Yes | API Key of the Rapid7 InsightIDR account.   
Sources | CSV | ALERT,USER | No | Sources that are used to fetch investigations. Possible values: User, Alert. If nothing is provided, the connector ingests investigations from both sources.  
Lowest Priority To Fetch | String | Medium | No | The lowest priority that needs to be used to fetch investigations. Possible values: Low, Medium, High, Critical. If nothing is specified, the connector ingests alerts with all severities.  
Max Hours Backwards | Integer | 1 | No | Number of hours from where to fetch investigations.  
Max Alerts To Fetch | Integer | 20 | No | Number of alerts to process per one connector iteration. Default: 20.  
Use dynamic list as a blacklist | Checkbox | Checked | Yes | If enabled, dynamic list is used as a blacklist.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Darktrace server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

The connector supports Proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
