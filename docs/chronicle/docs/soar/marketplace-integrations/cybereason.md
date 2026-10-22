---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cybereason/
title: Cybereason \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:51.517654+00:00
---

# Cybereason  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cybereason/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cybereason

This document describes how to integrate Cybereason with Google Security Operations.

**Note:** This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [storage bucket](https://storage.googleapis.com/csoar_public_integrations/Cybereason.zip).

## Before you begin

Before you configure the Cybereason integration in Google SecOps, make sure you have the following:

  * **Cybereason Server URL** : The URL for your Cybereason instance (for example, `https://[hostname]:[port]`).

  * **Cybereason Account** : A user account with the required permissions in your Cybereason environment.

**Note:** This account requires the **L3 analyst** and **System Admin** roles for full integration functionality. For details about roles and associated permissions, refer to the [Cybereason documentation portal](https://nest.cybereason.com/documentation/api-documentation/all-versions/required-permissions).
  * **Account Credentials** : The username and password for the Cybereason account.




## Configure the integration

To configure the Cybereason integration, follow the steps to [configure an integration in Google SecOps](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations). When configuring the instance, use the parameters described in Integration parameters.

## Integration parameters

The Cybereason integration requires the following parameters:

Parameter | Description  
---|---  
`API Root` | Required. The full URL of your Cybereason instance to connect to.  
`Username` | Required. The username for the account used to connect to Cybereason.  
`Password` | Required. The password for the account used to connect to Cybereason.  
`Verify SSL` | Optional.If selected, the integration validates the SSL certificate when connecting to the Cybereason server.Enabled by default.  
`CA Certificate Base64` | Optional. The Base64 encoded string of the trusted root CA certificate. This is required for validating the server's identity when connecting over SSL/TLS (LDAPS) to systems that use internal or self-signed certificates.   
  
### How authentication works

The Cybereason integration authenticates with the Cybereason server by sending a `POST` request to the `/login.html` endpoint. This request uses the `Login` (username) and `Password` values provided in the integration parameters. 

If authentication is successful, the Cybereason server returns a session cookie (`JSESSIONID`). The integration automatically stores and uses this cookie for all subsequent API requests within the session.

Make sure your machine uses **TLS 1.2** to securely communicate with the Cybereason server.

## Actions

### Ping

#### Description

Test connectivity to Cybereason with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Use cases

The action is used to test connectivity at the integration configuration page in the Google SecOps Content Hub page. It can be executed as a manual action, and not used in playbooks.

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | _If successful:_ "Successfully connected to the Cybereason server with the provided connection parameters!"_If not successful:_ "Failed to connect to the Cybereason server! Error is related to invalid credentials. Please check the spelling".format(exception.stacktrace) | General  
  
### Add Comment to Malop

#### Description

Add a comment to an existing malop in Cybereason.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Malop ID | String | N/A | Yes | Specify the ID of the malop to which you want to add a comment.  
Comment to Add | String | N/A | Yes | Specify the comment for the malop.  
  
#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | _If successfully added a comment (is_success=true):_ **"** Successfully added comment to a malop with ID {ID} in Cybereason."_If a critical_ _error is reported (fail):_ **"** Error executing action "{action name}". Reason: {traceback}"_If the malop is not found (fail):_ **"** Error executing action "{action name}". Reason: malop with ID {ID} was not found in Cybereason." | General  
  
### Allow File

#### Description

Remove hash from a blocklist in Cybereason. Supported entities: File Hash.

**Note:** Only the MD5 hashes are supported.

#### Parameters

N/A

#### Run On

This action runs on the File Hash entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | _If successfully removed hashes from the blocklist (is_success=true):_ **"** Successfully removed the following hashes from the blacklist in Cybereason: {entity.identifier}"_If isn't able to remove hashes from the blocklist (is_success=true):_ **"** Action wasn't able to remove the following hashes from the blacklist in Cybereason: {entity.identifier}"_If none of the hashes are blocked: "_ No hashes were removed from the blacklist in Cybereason."_If a critical error is reported: "_ Error executing action "Allow File". Reason: {traceback}" | General  
  
### Clear Reputation

#### Description

Clear the reputation of the entity in Cybereason. Supported entities: File Hash, IP Address, URL.

**Note:** This action strips the domain part from the URL entity. Only the MD5 and SHA1 hashes are supported.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * File Hash
  * IP Address
  * URL



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | _If successful for one entity (is_success=true): "_ Successfully cleared reputation for the following entities: {entity.identifier}"_If one entity is not found (is_success=true):_ **"** The following entities were not found: {entity.identifier}"_If no entities are found (is_success=false):_ **"** None of the provided entities were found in Cybereason."_If a critical error is reported (fail):_ **"** Error executing action "{action name}". Reason: {traceback}." | General  
  
### Enrich Entities

#### Description

Enrich entities using information from Cybereason. Supported entities: Hostname, IP Address, File Hash, URL.

**Note:** This action strips the domain part from the URL entity. IP Address for this action refers to external IP addresses. Only the MD5 and SHA-1 hashes are supported.

#### Parameters

Parameter Name | Type | Default | Is Mandatory | Description  
---|---|---|---|---  
Create Insight | Checkbox | Checked | Yes | If enabled, the action creates an insight for each enriched entity.  
Only Malicious Entity Insight | Checkbox | Checked | Yes | If enabled, the action creates an insight only for entities that have type: ransomware, maltool, unwanted, malware, blacklist. **Note:** This affects only the IP Address, File Hash and URL entities. For the Hostname entity, the action still creates an insight.  
  
#### Run On

This action runs on the following entities:

  * Hostname
  * IP Address
  * File Hash
  * URL



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
#### Enrichment Table - for hash

**Name**  
---  
type  
path  
md5  
signed  
verified_signature  
display_name  
affected_machines  
sha1  
size  
  
#### Enrichment Table - IP, URL

**Name**  
---  
type  
  
##### JSON Result
    
    
    {
        "tables": [
            {
                "rows": [
                    ["d5986926-d3dd-41ff-830f-e90345f1adb6",
                     "2019-10-22T06:54:03Z",
                     "Failed logon attempts within 10 mins",
                     "Failed logon attempts within 10 mins",
                     "Low",
                     "Identifies when failed logon attempts are 6 or higher during a 10 minute period.",
                     "ASI Scheduled Alerts",
                     "Microsoft",
                     "3bbdd11a-d490-4248-b1e1-aa31a7dd3123",
                     "c3f18986-eda6-4778-8c02-43e38bbc89e2",
                     " ",
                     " ",
                     "d5986926-d3dd-41ff-830f-e90345f1adb6_f50e7236-7236-4a75-9e9b-68e9dfea7a65",
                     "Unknown",
                     null,
                     false,
                     "2019-10-22T06:28:57Z",
                     "2019-10-22T06:48:57Z",
                     "2019-10-22T06:54:03Z",
                     " ",
                     "{r\\n  \\\"Query\\\": \\\"//In order to view the events that triggered this alert, please add filtering for the original alert\\u2019s time-frame for any table used in this query.\\\\n//This only happens for queries containing conditions on the TimeGenerated column of one or more tables.\\\\n//The original alert's time-frame filter, which should be added to each table in the query is:\\\\n//\\\\\\\"where TimeGenerated between (datetime(10/22/2019 6:28:57 AM)..datetime(10/22/2019 6:48:57 AM))\\\\\\\"\\\\nlet timeframe = 10m;\\\\nSecurityEvent \\\\n| where TimeGenerated > (datetime(10/22/2019 6:48:57 AM)-(2*timeframe)) \\\\n| where EventID == \\\\\\\"4625\\\\\\\"\\\\n| where AccountType == \\\\\\\"User\\\\\\\"\\\\n| summarize min(TimeGenerated), max(TimeGenerated), FailedLogonCount = count() by EventID, Activity, WorkstationName, Account, TargetAccount, TargetUserName, TargetDomainName, LogonType, LogonTypeName, LogonProcessName, Status, SubStatus\\\\n| where FailedLogonCount >= 6\\\\n| project StartTimeUtc = min_TimeGenerated, EndTimeUtc = max_TimeGenerated, FailedLogonCount, EventID, Activity, WorkstationName, Account, TargetAccount, TargetUserName, TargetDomainName, LogonType, LogonTypeName, LogonProcessName, Status, SubStatus\\\\n| extend timestamp = StartTimeUtc, AccountCustomEntity = Account, HostCustomEntity = WorkstationName\\\",\\r\\n  \\\"Query Period\\\": \\\"00:20:00\\\",\\r\\n  \\\"Trigger Operator\\\": \\\"GreaterThan\\\",\\r\\n  \\\"Trigger Threshold\\\": \\\"0\\\",\\r\\n  \\\"Search Query Results Overall Count\\\": \\\"3\\\",\\r\\n  \\\"Total Account Entities\\\": \\\"1\\\",\\r\\n  \\\"Total Host Entities\\\": \\\"1\\\"\\r\\n}\", \"[\\r\\n  {\\r\\n    \\\"$id\\\": \\\"3\\\",\\r\\n    \\\"HostName\\\": \\\"US-DC-V01001\\\",\\r\\n    \\\"Type\\\": \\\"host\\\"\\r\\n  },\\r\\n  {\\r\\n    \\\"$id\\\": \\\"4\\\",\\r\\n    \\\"Name\\\": \\\"administrator\\\",\\r\\n    \\\"NTDomain\\\": \\\"\\\",\\r\\n    \\\"IsDomainJoined\\\": false,\\r\\n    \\\"Type\\\": \\\"account\\\"\\r\\n  }\\r\\n]",
                     "Detection",
                     "a052d33b-b7c4-4dc7-9e17-5c89ea594669",
                     "Sentinel-Check",
                     " ",
                     "Azure Sentinel",
                     "Scheduled Alerts",
                     "SecurityAlert"
                    ], [
                     "d5986926-d3dd-41ff-830f-e90345f1adb6",
                     "2019-10-23T15:24:15Z",
                     "Failed logon attempts within 10 mins",
                     "Failed logon attempts within 10 mins",
                     "Low",
                     "Identifies when failed logon attempts are 6 or higher during a 10 minute period.",
                     "ASI Scheduled Alerts",
                     "Microsoft",
                     "4f1ac995-f232-4d32-b31c-642e86ef8a3f",
                     "d424e7c0-0d99-45fd-a634-36bd87a6f1ce",
                     " ",
                     " ",
                     "d5986926-d3dd-41ff-830f-e90345f1adb6_f50e7236-7236-4a75-9e9b-68e9dfea7a65",
                     "Unknown",
                     null,
                     false,
                     "2019-10-23T14:59:07Z",
                     "2019-10-23T15:19:07Z",
                     "2019-10-23T15:24:15Z",
                     " ",
                     "{\\r\\n  \\\"Query\\\": \\\"//In order to view the events that triggered this alert, please add filtering for the original alert\\u2019s time-frame for any table used in this query.\\\\n//This only happens for queries containing conditions on the TimeGenerated column of one or more tables.\\\\n//The original alert's time-frame filter, which should be added to each table in the query is:\\\\n//\\\\\\\"where TimeGenerated between (datetime(10/23/2019 2:59:07 PM)..datetime(10/23/2019 3:19:07 PM))\\\\\\\"\\\\nlet timeframe = 10m;\\\\nSecurityEvent \\\\n| where TimeGenerated > (datetime(10/23/2019 3:19:07 PM)-(2*timeframe)) \\\\n| where EventID == \\\\\\\"4625\\\\\\\"\\\\n| where AccountType == \\\\\\\"User\\\\\\\"\\\\n| summarize min(TimeGenerated), max(TimeGenerated), FailedLogonCount = count() by EventID, Activity, WorkstationName, Account, TargetAccount, TargetUserName, TargetDomainName, LogonType, LogonTypeName, LogonProcessName, Status, SubStatus\\\\n| where FailedLogonCount >= 6\\\\n| project StartTimeUtc = min_TimeGenerated, EndTimeUtc = max_TimeGenerated, FailedLogonCount, EventID, Activity, WorkstationName, Account, TargetAccount, TargetUserName, TargetDomainName, LogonType, LogonTypeName, LogonProcessName, Status, SubStatus\\\\n| extend timestamp = StartTimeUtc, AccountCustomEntity = Account, HostCustomEntity = WorkstationName\\\",\\r\\n  \\\"Query Period\\\": \\\"00:20:00\\\",\\r\\n  \\\"Trigger Operator\\\": \\\"GreaterThan\\\",\\r\\n  \\\"Trigger Threshold\\\": \\\"0\\\",\\r\\n  \\\"Search Query Results Overall Count\\\": \\\"1\\\",\\r\\n  \\\"Total Account Entities\\\": \\\"1\\\",\\r\\n  \\\"Total Host Entities\\\": \\\"1\\\"\\r\\n}\", \"[\\r\\n  {\\r\\n    \\\"$id\\\": \\\"3\\\",\\r\\n    \\\"HostName\\\": \\\"DESKTOP-45ISRTV\\\",\\r\\n    \\\"Type\\\": \\\"host\\\"\\r\\n  },\\r\\n  {\\r\\n    \\\"$id\\\": \\\"4\\\",\\r\\n    \\\"Name\\\": \\\"avmilen\\\",\\r\\n    \\\"NTDomain\\\": \\\"DESKTOP-45ISRTV\\\",\\r\\n    \\\"Type\\\": \\\"account\\\"\\r\\n  }\\r\\n]",
                     "Detection",
                     "a052d33b-b7c4-4dc7-9e17-5c89ea594669",
                     "Sentinel-Check",
                     " ",
                     "Azure Sentinel",
                     "Scheduled Alerts",
                     "SecurityAlert"]],
                "name": "PrimaryResult",
                "columns": [
                    {
                        "type": "string",
                        "name": "TenantId"
                    }, {
                        "type": "datetime",
                        "name": "TimeGenerated"
                    }, {
                        "type": "string",
                        "name": "DisplayName"
                    }, {
                        "type": "string",
                        "name": "AlertName"
                    }, {
                        "type": "string",
                        "name": "AlertSeverity"
                    }, {
                        "type": "string",
                        "name": "Description"
                    }, {
                        "type": "string",
                        "name": "ProviderName"
                    }, {
                        "type": "string",
                        "name": "VendorName"
                    }, {
                        "type": "string",
                        "name": "VendorOriginalId"
                    }, {
                        "type": "string",
                        "name": "SystemAlertId"
                    }, {
                        "type": "string",
                        "name": "ResourceId"
                    }, {
                        "type": "string",
                        "name": "SourceComputerId"
                    }, {
                        "type": "string",
                        "name": "AlertType"
                    }, {
                        "type": "string",
                        "name": "ConfidenceLevel"
                    }, {
                        "type": "real",
                        "name": "ConfidenceScore"
                    }, {
                        "type": "bool",
                        "name": "IsIncident"
                    }, {
                        "type": "datetime",
                        "name": "StartTime"
                    }, {
                        "type": "datetime",
                        "name": "EndTime"
                    }, {
                        "type": "datetime",
                        "name": "ProcessingEndTime"
                    }, {
                        "type": "string",
                        "name": "RemediationSteps"
                    }, {
                        "type": "string",
                        "name": "ExtendedProperties"
                    }, {
                        "type": "string",
                        "name": "Entities"
                    }, {
                        "type": "string",
                        "name": "SourceSystem"
                    }, {
                        "type": "string",
                        "name": "WorkspaceSubscriptionId"
                    }, {
                        "type": "string",
                        "name": "WorkspaceResourceGroup"
                    }, {
                        "type": "string",
                        "name": "ExtendedLinks"
                    }, {
                        "type": "string",
                        "name": "ProductName"
                    }, {
                        "type": "string",
                        "name": "ProductComponentName"
                    }, {
                        "type": "string",
                        "name": "Type"
                    }
                ]
            }
        ]
    }
    

##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | _If successful for one entity (is_success=true): "_ Successfully enriched the following entities in Cybereason: {entity.identifier}"_If not successful for one entity (is_success=true):_ **"** Action wasn't able to enrich the following entities in Cybereason: {entity.identifier}"_If no entities are enriched (is_success=false): "_ None of the entities were enriched."_If a critical error is reported (fail):_ "Error executing action "{action name}". Reason: {traceback}" | General  
  
### Get Malop

#### Description

Retrieve detailed information about a malop in Cybereason.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Malop ID | String | N/A | Yes | Specify the ID of the malop for which you want to return details.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | _If the malop is found (is_success=true):_ "Successfully retrieved details for the malop with ID {ID}: {entity.identifier}"_If the malop is not found (fail):_ "Error executing action "Get Malop". Reason: malop with ID {id} was not found in Cybereason."_If a critical error is reported:_ **"** Error executing action "Get Malop". Reason: {traceback}" | General  
Case Wall Table | **Table Name:** Malop Details**Table Columns:**

  * Element Name
  * Detection Type
  * Malop Activity Types  
Affected Machines
  * Affected Users
  * Root Cause Elements

|   
  
### Is Probe Connected

#### Description

Check the connectivity of the endpoint to Cybereason. Supported entities: Hostname.

#### Parameters

N/A

#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "tables": [
            {
                "rows": [
                    ["d5986926-d3dd-41ff-830f-e90345f1adb6",
                     "2019-10-22T06:54:03Z",
                     "Failed logon attempts within 10 mins",
                     "Failed logon attempts within 10 mins",
                     "Low",
                     "Identifies when failed logon attempts are 6 or higher during a 10 minute period.",
                     "ASI Scheduled Alerts",
                     "Microsoft",
                     "3bbdd11a-d490-4248-b1e1-aa31a7dd3123",
                     "c3f18986-eda6-4778-8c02-43e38bbc89e2",
                     " ",
                     " ",
                     "d5986926-d3dd-41ff-830f-e90345f1adb6_f50e7236-7236-4a75-9e9b-68e9dfea7a65",
                     "Unknown",
                     null,
                     false,
                     "2019-10-22T06:28:57Z",
                     "2019-10-22T06:48:57Z",
                     "2019-10-22T06:54:03Z",
                     " ",
                     "{r\\n  \\\"Query\\\": \\\"//In order to view the events that triggered this alert, please add filtering for the original alert\\u2019s time-frame for any table used in this query.\\\\n//This only happens for queries containing conditions on the TimeGenerated column of one or more tables.\\\\n//The original alert's time-frame filter, which should be added to each table in the query is:\\\\n//\\\\\\\"where TimeGenerated between (datetime(10/22/2019 6:28:57 AM)..datetime(10/22/2019 6:48:57 AM))\\\\\\\"\\\\nlet timeframe = 10m;\\\\nSecurityEvent \\\\n| where TimeGenerated > (datetime(10/22/2019 6:48:57 AM)-(2*timeframe)) \\\\n| where EventID == \\\\\\\"4625\\\\\\\"\\\\n| where AccountType == \\\\\\\"User\\\\\\\"\\\\n| summarize min(TimeGenerated), max(TimeGenerated), FailedLogonCount = count() by EventID, Activity, WorkstationName, Account, TargetAccount, TargetUserName, TargetDomainName, LogonType, LogonTypeName, LogonProcessName, Status, SubStatus\\\\n| where FailedLogonCount >= 6\\\\n| project StartTimeUtc = min_TimeGenerated, EndTimeUtc = max_TimeGenerated, FailedLogonCount, EventID, Activity, WorkstationName, Account, TargetAccount, TargetUserName, TargetDomainName, LogonType, LogonTypeName, LogonProcessName, Status, SubStatus\\\\n| extend timestamp = StartTimeUtc, AccountCustomEntity = Account, HostCustomEntity = WorkstationName\\\",\\r\\n  \\\"Query Period\\\": \\\"00:20:00\\\",\\r\\n  \\\"Trigger Operator\\\": \\\"GreaterThan\\\",\\r\\n  \\\"Trigger Threshold\\\": \\\"0\\\",\\r\\n  \\\"Search Query Results Overall Count\\\": \\\"3\\\",\\r\\n  \\\"Total Account Entities\\\": \\\"1\\\",\\r\\n  \\\"Total Host Entities\\\": \\\"1\\\"\\r\\n}\", \"[\\r\\n  {\\r\\n    \\\"$id\\\": \\\"3\\\",\\r\\n    \\\"HostName\\\": \\\"US-DC-V01001\\\",\\r\\n    \\\"Type\\\": \\\"host\\\"\\r\\n  },\\r\\n  {\\r\\n    \\\"$id\\\": \\\"4\\\",\\r\\n    \\\"Name\\\": \\\"administrator\\\",\\r\\n    \\\"NTDomain\\\": \\\"\\\",\\r\\n    \\\"IsDomainJoined\\\": false,\\r\\n    \\\"Type\\\": \\\"account\\\"\\r\\n  }\\r\\n]",
                     "Detection",
                     "a052d33b-b7c4-4dc7-9e17-5c89ea594669",
                     "Sentinel-Check",
                     " ",
                     "Azure Sentinel",
                     "Scheduled Alerts",
                     "SecurityAlert"
                    ], [
                     "d5986926-d3dd-41ff-830f-e90345f1adb6",
                     "2019-10-23T15:24:15Z",
                     "Failed logon attempts within 10 mins",
                     "Failed logon attempts within 10 mins",
                     "Low",
                     "Identifies when failed logon attempts are 6 or higher during a 10 minute period.",
                     "ASI Scheduled Alerts",
                     "Microsoft",
                     "4f1ac995-f232-4d32-b31c-642e86ef8a3f",
                     "d424e7c0-0d99-45fd-a634-36bd87a6f1ce",
                     " ",
                     " ",
                     "d5986926-d3dd-41ff-830f-e90345f1adb6_f50e7236-7236-4a75-9e9b-68e9dfea7a65",
                     "Unknown",
                     null,
                     false,
                     "2019-10-23T14:59:07Z",
                     "2019-10-23T15:19:07Z",
                     "2019-10-23T15:24:15Z",
                     " ",
                     "{\\r\\n  \\\"Query\\\": \\\"//In order to view the events that triggered this alert, please add filtering for the original alert\\u2019s time-frame for any table used in this query.\\\\n//This only happens for queries containing conditions on the TimeGenerated column of one or more tables.\\\\n//The original alert's time-frame filter, which should be added to each table in the query is:\\\\n//\\\\\\\"where TimeGenerated between (datetime(10/23/2019 2:59:07 PM)..datetime(10/23/2019 3:19:07 PM))\\\\\\\"\\\\nlet timeframe = 10m;\\\\nSecurityEvent \\\\n| where TimeGenerated > (datetime(10/23/2019 3:19:07 PM)-(2*timeframe)) \\\\n| where EventID == \\\\\\\"4625\\\\\\\"\\\\n| where AccountType == \\\\\\\"User\\\\\\\"\\\\n| summarize min(TimeGenerated), max(TimeGenerated), FailedLogonCount = count() by EventID, Activity, WorkstationName, Account, TargetAccount, TargetUserName, TargetDomainName, LogonType, LogonTypeName, LogonProcessName, Status, SubStatus\\\\n| where FailedLogonCount >= 6\\\\n| project StartTimeUtc = min_TimeGenerated, EndTimeUtc = max_TimeGenerated, FailedLogonCount, EventID, Activity, WorkstationName, Account, TargetAccount, TargetUserName, TargetDomainName, LogonType, LogonTypeName, LogonProcessName, Status, SubStatus\\\\n| extend timestamp = StartTimeUtc, AccountCustomEntity = Account, HostCustomEntity = WorkstationName\\\",\\r\\n  \\\"Query Period\\\": \\\"00:20:00\\\",\\r\\n  \\\"Trigger Operator\\\": \\\"GreaterThan\\\",\\r\\n  \\\"Trigger Threshold\\\": \\\"0\\\",\\r\\n  \\\"Search Query Results Overall Count\\\": \\\"1\\\",\\r\\n  \\\"Total Account Entities\\\": \\\"1\\\",\\r\\n  \\\"Total Host Entities\\\": \\\"1\\\"\\r\\n}\", \"[\\r\\n  {\\r\\n    \\\"$id\\\": \\\"3\\\",\\r\\n    \\\"HostName\\\": \\\"DESKTOP-45ISRTV\\\",\\r\\n    \\\"Type\\\": \\\"host\\\"\\r\\n  },\\r\\n  {\\r\\n    \\\"$id\\\": \\\"4\\\",\\r\\n    \\\"Name\\\": \\\"avmilen\\\",\\r\\n    \\\"NTDomain\\\": \\\"DESKTOP-45ISRTV\\\",\\r\\n    \\\"Type\\\": \\\"account\\\"\\r\\n  }\\r\\n]",
                     "Detection",
                     "a052d33b-b7c4-4dc7-9e17-5c89ea594669",
                     "Sentinel-Check",
                     " ",
                     "Azure Sentinel",
                     "Scheduled Alerts",
                     "SecurityAlert"]],
                "name": "PrimaryResult",
                "columns": [
                    {
                        "type": "string",
                        "name": "TenantId"
                    }, {
                        "type": "datetime",
                        "name": "TimeGenerated"
                    }, {
                        "type": "string",
                        "name": "DisplayName"
                    }, {
                        "type": "string",
                        "name": "AlertName"
                    }, {
                        "type": "string",
                        "name": "AlertSeverity"
                    }, {
                        "type": "string",
                        "name": "Description"
                    }, {
                        "type": "string",
                        "name": "ProviderName"
                    }, {
                        "type": "string",
                        "name": "VendorName"
                    }, {
                        "type": "string",
                        "name": "VendorOriginalId"
                    }, {
                        "type": "string",
                        "name": "SystemAlertId"
                    }, {
                        "type": "string",
                        "name": "ResourceId"
                    }, {
                        "type": "string",
                        "name": "SourceComputerId"
                    }, {
                        "type": "string",
                        "name": "AlertType"
                    }, {
                        "type": "string",
                        "name": "ConfidenceLevel"
                    }, {
                        "type": "real",
                        "name": "ConfidenceScore"
                    }, {
                        "type": "bool",
                        "name": "IsIncident"
                    }, {
                        "type": "datetime",
                        "name": "StartTime"
                    }, {
                        "type": "datetime",
                        "name": "EndTime"
                    }, {
                        "type": "datetime",
                        "name": "ProcessingEndTime"
                    }, {
                        "type": "string",
                        "name": "RemediationSteps"
                    }, {
                        "type": "string",
                        "name": "ExtendedProperties"
                    }, {
                        "type": "string",
                        "name": "Entities"
                    }, {
                        "type": "string",
                        "name": "SourceSystem"
                    }, {
                        "type": "string",
                        "name": "WorkspaceSubscriptionId"
                    }, {
                        "type": "string",
                        "name": "WorkspaceResourceGroup"
                    }, {
                        "type": "string",
                        "name": "ExtendedLinks"
                    }, {
                        "type": "string",
                        "name": "ProductName"
                    }, {
                        "type": "string",
                        "name": "ProductComponentName"
                    }, {
                        "type": "string",
                        "name": "Type"
                    }
                ]
            }
        ]
    }
    

##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | _If successful for one entity (is_success=true):_ "Successfully retrieved information about connectivity for the following entities: {entity.identifier}"_If not successful for one entity (is_success=true): "_ Action wasn't able to retrieve information about connectivity for the following entities: {entity.identifier}"_If not successful for all entities (is_success=false):_ **"** No information about connectivity was retrieved for the provided entities."_If a critical error is reported (fail):_ **"** Error executing action "{action name}". Reason: {traceback}" | General  
  
### Isolate Machine

#### Description

Isolate a machine in Cybereason. Supported entities: Hostname.

#### Parameters

N/A

#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "tables": [
            {
                "rows": [
                    ["d5986926-d3dd-41ff-830f-e90345f1adb6",
                     "2019-10-22T06:54:03Z",
                     "Failed logon attempts within 10 mins",
                     "Failed logon attempts within 10 mins",
                     "Low",
                     "Identifies when failed logon attempts are 6 or higher during a 10 minute period.",
                     "ASI Scheduled Alerts",
                     "Microsoft",
                     "3bbdd11a-d490-4248-b1e1-aa31a7dd3123",
                     "c3f18986-eda6-4778-8c02-43e38bbc89e2",
                     " ",
                     " ",
                     "d5986926-d3dd-41ff-830f-e90345f1adb6_f50e7236-7236-4a75-9e9b-68e9dfea7a65",
                     "Unknown",
                     null,
                     false,
                     "2019-10-22T06:28:57Z",
                     "2019-10-22T06:48:57Z",
                     "2019-10-22T06:54:03Z",
                     " ",
                     "{r\\n  \\\"Query\\\": \\\"//In order to view the events that triggered this alert, please add filtering for the original alert\\u2019s time-frame for any table used in this query.\\\\n//This only happens for queries containing conditions on the TimeGenerated column of one or more tables.\\\\n//The original alert's time-frame filter, which should be added to each table in the query is:\\\\n//\\\\\\\"where TimeGenerated between (datetime(10/22/2019 6:28:57 AM)..datetime(10/22/2019 6:48:57 AM))\\\\\\\"\\\\nlet timeframe = 10m;\\\\nSecurityEvent \\\\n| where TimeGenerated > (datetime(10/22/2019 6:48:57 AM)-(2*timeframe)) \\\\n| where EventID == \\\\\\\"4625\\\\\\\"\\\\n| where AccountType == \\\\\\\"User\\\\\\\"\\\\n| summarize min(TimeGenerated), max(TimeGenerated), FailedLogonCount = count() by EventID, Activity, WorkstationName, Account, TargetAccount, TargetUserName, TargetDomainName, LogonType, LogonTypeName, LogonProcessName, Status, SubStatus\\\\n| where FailedLogonCount >= 6\\\\n| project StartTimeUtc = min_TimeGenerated, EndTimeUtc = max_TimeGenerated, FailedLogonCount, EventID, Activity, WorkstationName, Account, TargetAccount, TargetUserName, TargetDomainName, LogonType, LogonTypeName, LogonProcessName, Status, SubStatus\\\\n| extend timestamp = StartTimeUtc, AccountCustomEntity = Account, HostCustomEntity = WorkstationName\\\",\\r\\n  \\\"Query Period\\\": \\\"00:20:00\\\",\\r\\n  \\\"Trigger Operator\\\": \\\"GreaterThan\\\",\\r\\n  \\\"Trigger Threshold\\\": \\\"0\\\",\\r\\n  \\\"Search Query Results Overall Count\\\": \\\"3\\\",\\r\\n  \\\"Total Account Entities\\\": \\\"1\\\",\\r\\n  \\\"Total Host Entities\\\": \\\"1\\\"\\r\\n}\", \"[\\r\\n  {\\r\\n    \\\"$id\\\": \\\"3\\\",\\r\\n    \\\"HostName\\\": \\\"US-DC-V01001\\\",\\r\\n    \\\"Type\\\": \\\"host\\\"\\r\\n  },\\r\\n  {\\r\\n    \\\"$id\\\": \\\"4\\\",\\r\\n    \\\"Name\\\": \\\"administrator\\\",\\r\\n    \\\"NTDomain\\\": \\\"\\\",\\r\\n    \\\"IsDomainJoined\\\": false,\\r\\n    \\\"Type\\\": \\\"account\\\"\\r\\n  }\\r\\n]",
                     "Detection",
                     "a052d33b-b7c4-4dc7-9e17-5c89ea594669",
                     "Sentinel-Check",
                     " ",
                     "Azure Sentinel",
                     "Scheduled Alerts",
                     "SecurityAlert"
                    ], [
                     "d5986926-d3dd-41ff-830f-e90345f1adb6",
                     "2019-10-23T15:24:15Z",
                     "Failed logon attempts within 10 mins",
                     "Failed logon attempts within 10 mins",
                     "Low",
                     "Identifies when failed logon attempts are 6 or higher during a 10 minute period.",
                     "ASI Scheduled Alerts",
                     "Microsoft",
                     "4f1ac995-f232-4d32-b31c-642e86ef8a3f",
                     "d424e7c0-0d99-45fd-a634-36bd87a6f1ce",
                     " ",
                     " ",
                     "d5986926-d3dd-41ff-830f-e90345f1adb6_f50e7236-7236-4a75-9e9b-68e9dfea7a65",
                     "Unknown",
                     null,
                     false,
                     "2019-10-23T14:59:07Z",
                     "2019-10-23T15:19:07Z",
                     "2019-10-23T15:24:15Z",
                     " ",
                     "{\\r\\n  \\\"Query\\\": \\\"//In order to view the events that triggered this alert, please add filtering for the original alert\\u2019s time-frame for any table used in this query.\\\\n//This only happens for queries containing conditions on the TimeGenerated column of one or more tables.\\\\n//The original alert's time-frame filter, which should be added to each table in the query is:\\\\n//\\\\\\\"where TimeGenerated between (datetime(10/23/2019 2:59:07 PM)..datetime(10/23/2019 3:19:07 PM))\\\\\\\"\\\\nlet timeframe = 10m;\\\\nSecurityEvent \\\\n| where TimeGenerated > (datetime(10/23/2019 3:19:07 PM)-(2*timeframe)) \\\\n| where EventID == \\\\\\\"4625\\\\\\\"\\\\n| where AccountType == \\\\\\\"User\\\\\\\"\\\\n| summarize min(TimeGenerated), max(TimeGenerated), FailedLogonCount = count() by EventID, Activity, WorkstationName, Account, TargetAccount, TargetUserName, TargetDomainName, LogonType, LogonTypeName, LogonProcessName, Status, SubStatus\\\\n| where FailedLogonCount >= 6\\\\n| project StartTimeUtc = min_TimeGenerated, EndTimeUtc = max_TimeGenerated, FailedLogonCount, EventID, Activity, WorkstationName, Account, TargetAccount, TargetUserName, TargetDomainName, LogonType, LogonTypeName, LogonProcessName, Status, SubStatus\\\\n| extend timestamp = StartTimeUtc, AccountCustomEntity = Account, HostCustomEntity = WorkstationName\\\",\\r\\n  \\\"Query Period\\\": \\\"00:20:00\\\",\\r\\n  \\\"Trigger Operator\\\": \\\"GreaterThan\\\",\\r\\n  \\\"Trigger Threshold\\\": \\\"0\\\",\\r\\n  \\\"Search Query Results Overall Count\\\": \\\"1\\\",\\r\\n  \\\"Total Account Entities\\\": \\\"1\\\",\\r\\n  \\\"Total Host Entities\\\": \\\"1\\\"\\r\\n}\", \"[\\r\\n  {\\r\\n    \\\"$id\\\": \\\"3\\\",\\r\\n    \\\"HostName\\\": \\\"DESKTOP-45ISRTV\\\",\\r\\n    \\\"Type\\\": \\\"host\\\"\\r\\n  },\\r\\n  {\\r\\n    \\\"$id\\\": \\\"4\\\",\\r\\n    \\\"Name\\\": \\\"avmilen\\\",\\r\\n    \\\"NTDomain\\\": \\\"DESKTOP-45ISRTV\\\",\\r\\n    \\\"Type\\\": \\\"account\\\"\\r\\n  }\\r\\n]",
                     "Detection",
                     "a052d33b-b7c4-4dc7-9e17-5c89ea594669",
                     "Sentinel-Check",
                     " ",
                     "Azure Sentinel",
                     "Scheduled Alerts",
                     "SecurityAlert"]],
                "name": "PrimaryResult",
                "columns": [
                    {
                        "type": "string",
                        "name": "TenantId"
                    }, {
                        "type": "datetime",
                        "name": "TimeGenerated"
                    }, {
                        "type": "string",
                        "name": "DisplayName"
                    }, {
                        "type": "string",
                        "name": "AlertName"
                    }, {
                        "type": "string",
                        "name": "AlertSeverity"
                    }, {
                        "type": "string",
                        "name": "Description"
                    }, {
                        "type": "string",
                        "name": "ProviderName"
                    }, {
                        "type": "string",
                        "name": "VendorName"
                    }, {
                        "type": "string",
                        "name": "VendorOriginalId"
                    }, {
                        "type": "string",
                        "name": "SystemAlertId"
                    }, {
                        "type": "string",
                        "name": "ResourceId"
                    }, {
                        "type": "string",
                        "name": "SourceComputerId"
                    }, {
                        "type": "string",
                        "name": "AlertType"
                    }, {
                        "type": "string",
                        "name": "ConfidenceLevel"
                    }, {
                        "type": "real",
                        "name": "ConfidenceScore"
                    }, {
                        "type": "bool",
                        "name": "IsIncident"
                    }, {
                        "type": "datetime",
                        "name": "StartTime"
                    }, {
                        "type": "datetime",
                        "name": "EndTime"
                    }, {
                        "type": "datetime",
                        "name": "ProcessingEndTime"
                    }, {
                        "type": "string",
                        "name": "RemediationSteps"
                    }, {
                        "type": "string",
                        "name": "ExtendedProperties"
                    }, {
                        "type": "string",
                        "name": "Entities"
                    }, {
                        "type": "string",
                        "name": "SourceSystem"
                    }, {
                        "type": "string",
                        "name": "WorkspaceSubscriptionId"
                    }, {
                        "type": "string",
                        "name": "WorkspaceResourceGroup"
                    }, {
                        "type": "string",
                        "name": "ExtendedLinks"
                    }, {
                        "type": "string",
                        "name": "ProductName"
                    }, {
                        "type": "string",
                        "name": "ProductComponentName"
                    }, {
                        "type": "string",
                        "name": "Type"
                    }
                ]
            }
        ]
    }
    

##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | _If successful for one machine (is_success = true):_ **"** Successfully isolated the following machines in Cybereason: {entity.identifier}"_If some machines are not found (is_success=true): "_ The following machines were not found in Cybereason: {entity.identifier}"****_Async message:_ **"** Waiting for isolation to finish on the following entities: {entity.identifier}"_For machines that run into a timeout:_ "Isolation was initiated on the following entities, but wasn't finished: {entity.identifier}. Please execute the action again with bigger timeout."_If none of the machines are found (is_success=false): "_ None of the machines were found in Cybereason."_If a critical error is reported (fail):_ ****"Error executing action "Isolate Machine". Reason: {traceback}" | General  
  
### List Files

#### Description

Get information about files from Cybereason.

#### Known limitation

Cybereason API has a bug. If you make the "totalResults" request in the API, it returns "totalResults + 1". This means that when you provide "Results Limit" == 1, it returns 2 results.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
File Hash | String | N/A | No | Specify a comma-separated list of file hashes for which you want to return data.**Note:** This action only supports the SHA-1 and MD5 hashes. If you provide values for this parameter, then the "Results Limit" parameter is ignored. Action tries to find information about all provided hashes.  
Results Limit | String | 100 | Yes | Specify the number of files to return.  
Fields To Return | CSV | N/A | No | Specify a comma-separated list of fields that you want to return.  
If nothing is provided, the action works with predefined fields.  
Possible values: md5String,ownerMachine,avRemediationStatus,  
isSigned,signatureVerified,  
sha1String,maliciousClassificationType,createdTime,  
modifiedTime,size,correctedPath,productName,productVersion,  
companyName,internalName,elementDisplayName.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
num_of_files | N/A | N/A  
  
##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | _If at least one hash is returned (is_success=true): "_ Successfully retrieved information about hashes from Cybereason."_If no data is found (is_success=false):_ "No information about hashes was found."_If some fields are not correct (is_success=true):_ ****"The following fields are invalid: {invalid fields}."_If a critical error is reported (fail):_ **"** Error executing action "{action name}". Reason: {traceback}"_If none of the fields are correct (fail):_ "Error executing action {}. Reason: none of the provided fields are valid. Please check the spelling." | General  
  
### List Malop Affected Machines

#### Description

List machines affected by the malop in Cybereason.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Malop ID | String | N/A | Yes | Specify the ID of the malop for which you want to return affected machines.  
Results Limit | String | 100 | Yes | Specify how many results to return.  
Create Hostname Entity | Checkbox | Unchecked | No | If enabled, the action creates an entity based on machines name.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
num_of_machines | N/A | N/A  
  
##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | _If executed successfully:_ ****"Successfully retrieved affected machines for the malop with ID {ID} in Cybereason."_If the malop is not found: (fail):_ "Error executing action "{action name}". Reason: malop with ID {ID} wasn't found in Cybereason."_If a critical error is reported (fail):_ ****"Error executing action "{action name}". Reason: {traceback}" | General  
  
### List Malop Processes

#### Description

List processes related to the malop in Cybereason.

#### Known Limitation

Case Wall Tables for processes from the two different Malop Types look differently due to differences in the API responses.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Malop ID | String | N/A | Yes | Specify the ID of the malop for which you want to return related processes.  
Results Limit | String | 100 | Yes | Specify the number of results to return.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
num_of_processes | N/A | N/A  
  
##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | _If some processes are found:_ "Successfully retrieved related processes for the malop with ID {ID} in Cybereason."_If no processes are found:_ "No processes were related to the malop with ID {ID} in Cybereason."_If the malop is not found: (fail):_ ****"Error executing action "{action name}". Reason: malop with ID {ID} wasn't found in Cybereason."_If a critical error is reported (fail):_ "Error executing action "{action name}". Reason: {traceback}" | General  
Case Wall Table | **Table Name:** First Malop Type**Table Columns:**

  * Signed And Verified  
PID
  * User
  * Owner Machine
  * End Time
  * Product Type
  * Creation Time
  * MD5
  * Element Name
  * Command

|   
Case Wall Table | **Table Name:** Second Malop Type**Table Columns:**

  * PID
  * Owner Machine
  * Creation Time
  * End Time
  * Command
  * User
  * Element Name

| CSV  
  
### List Malop Remediations

#### Description

List available remediations for a malop in Cybereason.

#### Parameters

Parameter name | Type | Default value  | Is mandatory | Description  
---|---|---|---|---  
Malop ID | String | N/A | True | ID of the malop for which you want to list available remediations.   
  
#### Run on

N/A

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
If the action runs successfully (no errors returned, server response is **200 OK**) on at least one of the entities, `is_success` should be set to `True`.

##### JSON result
    
    
    [
        {
            "uniqueId": "QUARANTINE_FILE::Q127xR36N9FSGZlV",
            "remediationType": "QUARANTINE_FILE",
            "targetName": "lockless.exe",
            "targetId": "Q127xR36N9FSGZlV",
            "machineName": "desktop-v22rbe5",
            "machineId": "Q127xRCi55eyTiwX",
            "machinesCount": 1,
            "malopId": "AAAA1qdkdM5jUoWK",
            "metaData": null,
            "malopType": "MalopDetectionEvents",
            "machineConnected": false
        }
    ]
    

##### Case wall

Result type | Value/Description | Type (Entity/General)  
---|---|---  
Output message* | **The action should neither fail nor stop a playbook execution:**

  * _If something found (is_success=true):_
Successfully found remediation actions for the malop {malop id} in Cybereason.
  * _If nothing found (is_success=false):_
No remediation actions for the malop {malop id} were found in Cybereason.
**The action should fail and stop a playbook execution:**

  * _If there's a fatal error, such as wrong credentials, no connection to server, or other:_
print "Error executing action "List Malop Remediations". Reason: {0}''.format(error.Stacktrace)
| General  
  
### List Processes

#### Description

List processes based on provided criteria in Cybereason.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Process Name | String | N/A | No | Specify a comma-separated list of process names for which you want to return data.  
Machine Name | String | N/A | No | Specify a comma-separated list of machine names on which you want to search for processes.  
Has Suspicions | Checkbox | Unchecked | No | If enabled, the action only returns processes that are labeled as suspicious.  
Has Incoming Connection | Checkbox | Unchecked | No | If enabled, the action only returns processes that have incoming connections..  
Has Outgoing Connection | Checkbox | Unchecked | No | If enabled, the action only returns processes that have outgoing connections.  
Has External Connection | Checkbox | Unchecked | No | If enabled, the action only returns processes that have external connections.  
Unsigned process with unknown reputation | Checkbox | Unchecked | No | If enabled, the action only returns unsigned processes with unknown reputation.  
Running from temporary folder | Checkbox | Unchecked | No | If enabled, the action only returns processes running from a temporary folder.  
Privilege Escalation | Checkbox | Unchecked | No | If enabled, the action only returns processes with escalated privileges.  
Malicious use of PsExec | Checkbox | Unchecked | No | If enabled, the action only returns processes related to malicious use of PsExec.  
Results Limit | String | 100 | Yes | Specify the number of processes to return.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
num_of_processes | N/A | N/A  
  
##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | _If some processes are found:_ "Successfully retrieved information about processes based on provided criteria in Cybereason."_I_ f no processes are found: "No processes were found based on provided criteria in Cybereason."_If a critical error is reported:_ "Error executing action "{action name}". Reason: {traceback}" | General  
  
### Prevent File

#### Description

Add hash to a blocklist in Cybereason. Supported entities: File Hash.

**Note:** Only the MD5 hashes are supported.

#### Parameters

N/A

#### Run On

This action runs on the File Hash entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "tables": [
            {
                "rows": [
                    ["d5986926-d3dd-41ff-830f-e90345f1adb6",
                     "2019-10-22T06:54:03Z",
                     "Failed logon attempts within 10 mins",
                     "Failed logon attempts within 10 mins",
                     "Low",
                     "Identifies when failed logon attempts are 6 or higher during a 10 minute period.",
                     "ASI Scheduled Alerts",
                     "Microsoft",
                     "3bbdd11a-d490-4248-b1e1-aa31a7dd3123",
                     "c3f18986-eda6-4778-8c02-43e38bbc89e2",
                     " ",
                     " ",
                     "d5986926-d3dd-41ff-830f-e90345f1adb6_f50e7236-7236-4a75-9e9b-68e9dfea7a65",
                     "Unknown",
                     null,
                     false,
                     "2019-10-22T06:28:57Z",
                     "2019-10-22T06:48:57Z",
                     "2019-10-22T06:54:03Z",
                     " ",
                     "{r\\n  \\\"Query\\\": \\\"//In order to view the events that triggered this alert, please add filtering for the original alert\\u2019s time-frame for any table used in this query.\\\\n//This only happens for queries containing conditions on the TimeGenerated column of one or more tables.\\\\n//The original alert's time-frame filter, which should be added to each table in the query is:\\\\n//\\\\\\\"where TimeGenerated between (datetime(10/22/2019 6:28:57 AM)..datetime(10/22/2019 6:48:57 AM))\\\\\\\"\\\\nlet timeframe = 10m;\\\\nSecurityEvent \\\\n| where TimeGenerated > (datetime(10/22/2019 6:48:57 AM)-(2*timeframe)) \\\\n| where EventID == \\\\\\\"4625\\\\\\\"\\\\n| where AccountType == \\\\\\\"User\\\\\\\"\\\\n| summarize min(TimeGenerated), max(TimeGenerated), FailedLogonCount = count() by EventID, Activity, WorkstationName, Account, TargetAccount, TargetUserName, TargetDomainName, LogonType, LogonTypeName, LogonProcessName, Status, SubStatus\\\\n| where FailedLogonCount >= 6\\\\n| project StartTimeUtc = min_TimeGenerated, EndTimeUtc = max_TimeGenerated, FailedLogonCount, EventID, Activity, WorkstationName, Account, TargetAccount, TargetUserName, TargetDomainName, LogonType, LogonTypeName, LogonProcessName, Status, SubStatus\\\\n| extend timestamp = StartTimeUtc, AccountCustomEntity = Account, HostCustomEntity = WorkstationName\\\",\\r\\n  \\\"Query Period\\\": \\\"00:20:00\\\",\\r\\n  \\\"Trigger Operator\\\": \\\"GreaterThan\\\",\\r\\n  \\\"Trigger Threshold\\\": \\\"0\\\",\\r\\n  \\\"Search Query Results Overall Count\\\": \\\"3\\\",\\r\\n  \\\"Total Account Entities\\\": \\\"1\\\",\\r\\n  \\\"Total Host Entities\\\": \\\"1\\\"\\r\\n}\", \"[\\r\\n  {\\r\\n    \\\"$id\\\": \\\"3\\\",\\r\\n    \\\"HostName\\\": \\\"US-DC-V01001\\\",\\r\\n    \\\"Type\\\": \\\"host\\\"\\r\\n  },\\r\\n  {\\r\\n    \\\"$id\\\": \\\"4\\\",\\r\\n    \\\"Name\\\": \\\"administrator\\\",\\r\\n    \\\"NTDomain\\\": \\\"\\\",\\r\\n    \\\"IsDomainJoined\\\": false,\\r\\n    \\\"Type\\\": \\\"account\\\"\\r\\n  }\\r\\n]",
                     "Detection",
                     "a052d33b-b7c4-4dc7-9e17-5c89ea594669",
                     "Sentinel-Check",
                     " ",
                     "Azure Sentinel",
                     "Scheduled Alerts",
                     "SecurityAlert"
                    ], [
                     "d5986926-d3dd-41ff-830f-e90345f1adb6",
                     "2019-10-23T15:24:15Z",
                     "Failed logon attempts within 10 mins",
                     "Failed logon attempts within 10 mins",
                     "Low",
                     "Identifies when failed logon attempts are 6 or higher during a 10 minute period.",
                     "ASI Scheduled Alerts",
                     "Microsoft",
                     "4f1ac995-f232-4d32-b31c-642e86ef8a3f",
                     "d424e7c0-0d99-45fd-a634-36bd87a6f1ce",
                     " ",
                     " ",
                     "d5986926-d3dd-41ff-830f-e90345f1adb6_f50e7236-7236-4a75-9e9b-68e9dfea7a65",
                     "Unknown",
                     null,
                     false,
                     "2019-10-23T14:59:07Z",
                     "2019-10-23T15:19:07Z",
                     "2019-10-23T15:24:15Z",
                     " ",
                     "{\\r\\n  \\\"Query\\\": \\\"//In order to view the events that triggered this alert, please add filtering for the original alert\\u2019s time-frame for any table used in this query.\\\\n//This only happens for queries containing conditions on the TimeGenerated column of one or more tables.\\\\n//The original alert's time-frame filter, which should be added to each table in the query is:\\\\n//\\\\\\\"where TimeGenerated between (datetime(10/23/2019 2:59:07 PM)..datetime(10/23/2019 3:19:07 PM))\\\\\\\"\\\\nlet timeframe = 10m;\\\\nSecurityEvent \\\\n| where TimeGenerated > (datetime(10/23/2019 3:19:07 PM)-(2*timeframe)) \\\\n| where EventID == \\\\\\\"4625\\\\\\\"\\\\n| where AccountType == \\\\\\\"User\\\\\\\"\\\\n| summarize min(TimeGenerated), max(TimeGenerated), FailedLogonCount = count() by EventID, Activity, WorkstationName, Account, TargetAccount, TargetUserName, TargetDomainName, LogonType, LogonTypeName, LogonProcessName, Status, SubStatus\\\\n| where FailedLogonCount >= 6\\\\n| project StartTimeUtc = min_TimeGenerated, EndTimeUtc = max_TimeGenerated, FailedLogonCount, EventID, Activity, WorkstationName, Account, TargetAccount, TargetUserName, TargetDomainName, LogonType, LogonTypeName, LogonProcessName, Status, SubStatus\\\\n| extend timestamp = StartTimeUtc, AccountCustomEntity = Account, HostCustomEntity = WorkstationName\\\",\\r\\n  \\\"Query Period\\\": \\\"00:20:00\\\",\\r\\n  \\\"Trigger Operator\\\": \\\"GreaterThan\\\",\\r\\n  \\\"Trigger Threshold\\\": \\\"0\\\",\\r\\n  \\\"Search Query Results Overall Count\\\": \\\"1\\\",\\r\\n  \\\"Total Account Entities\\\": \\\"1\\\",\\r\\n  \\\"Total Host Entities\\\": \\\"1\\\"\\r\\n}\", \"[\\r\\n  {\\r\\n    \\\"$id\\\": \\\"3\\\",\\r\\n    \\\"HostName\\\": \\\"DESKTOP-45ISRTV\\\",\\r\\n    \\\"Type\\\": \\\"host\\\"\\r\\n  },\\r\\n  {\\r\\n    \\\"$id\\\": \\\"4\\\",\\r\\n    \\\"Name\\\": \\\"avmilen\\\",\\r\\n    \\\"NTDomain\\\": \\\"DESKTOP-45ISRTV\\\",\\r\\n    \\\"Type\\\": \\\"account\\\"\\r\\n  }\\r\\n]",
                     "Detection",
                     "a052d33b-b7c4-4dc7-9e17-5c89ea594669",
                     "Sentinel-Check",
                     " ",
                     "Azure Sentinel",
                     "Scheduled Alerts",
                     "SecurityAlert"]],
                "name": "PrimaryResult",
                "columns": [
                    {
                        "type": "string",
                        "name": "TenantId"
                    }, {
                        "type": "datetime",
                        "name": "TimeGenerated"
                    }, {
                        "type": "string",
                        "name": "DisplayName"
                    }, {
                        "type": "string",
                        "name": "AlertName"
                    }, {
                        "type": "string",
                        "name": "AlertSeverity"
                    }, {
                        "type": "string",
                        "name": "Description"
                    }, {
                        "type": "string",
                        "name": "ProviderName"
                    }, {
                        "type": "string",
                        "name": "VendorName"
                    }, {
                        "type": "string",
                        "name": "VendorOriginalId"
                    }, {
                        "type": "string",
                        "name": "SystemAlertId"
                    }, {
                        "type": "string",
                        "name": "ResourceId"
                    }, {
                        "type": "string",
                        "name": "SourceComputerId"
                    }, {
                        "type": "string",
                        "name": "AlertType"
                    }, {
                        "type": "string",
                        "name": "ConfidenceLevel"
                    }, {
                        "type": "real",
                        "name": "ConfidenceScore"
                    }, {
                        "type": "bool",
                        "name": "IsIncident"
                    }, {
                        "type": "datetime",
                        "name": "StartTime"
                    }, {
                        "type": "datetime",
                        "name": "EndTime"
                    }, {
                        "type": "datetime",
                        "name": "ProcessingEndTime"
                    }, {
                        "type": "string",
                        "name": "RemediationSteps"
                    }, {
                        "type": "string",
                        "name": "ExtendedProperties"
                    }, {
                        "type": "string",
                        "name": "Entities"
                    }, {
                        "type": "string",
                        "name": "SourceSystem"
                    }, {
                        "type": "string",
                        "name": "WorkspaceSubscriptionId"
                    }, {
                        "type": "string",
                        "name": "WorkspaceResourceGroup"
                    }, {
                        "type": "string",
                        "name": "ExtendedLinks"
                    }, {
                        "type": "string",
                        "name": "ProductName"
                    }, {
                        "type": "string",
                        "name": "ProductComponentName"
                    }, {
                        "type": "string",
                        "name": "Type"
                    }
                ]
            }
        ]
    }
    

##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | _If successfully added a single hash to the blocklist (is_success=true):_ ****"Successfully added the following hashes to the blacklist in Cybereason: {entity.identifier}"_If isn't able to add a single hash to the blocklist (is_success=true):_ ****"Action wasn't able to add the following hashes to the blacklist in Cybereason: {entity.identifier}"_If none of the hashes are blocked:_ ****"No hashes were added to the blacklist in Cybereason."_If a critical error is reported:_ "Error executing action "Prevent File". Reason: {traceback}" | General  
  
### Remediate Malop

#### Description

Perform the malop remediation action on endpoints in Cybereason.

**Note:** This action is running asynchronously. Adjust the script timeout value for the action in the Google SecOps IDE, if necessary.

#### Parameters

Parameter name | Type | Default value  | Is mandatory | Description  
---|---|---|---|---  
Malop ID | String | N/A | True | Specify the ID of the malop that contains the necessary file/process.  
Action | DDL | Kill Process DDL possible values:

  * Kill Process
  * Quarantine File
  * Block File

| False | Specify the remediation action.  
Identifier | DDL | SHA256 Supported values:

  * Name
  * MD5
  * SHA1
  * SHA256

| False | Specify the identifier for the process. **Note:** For better precision, it is recommended to work with GUID that Cybereason assigns to all processes.  
Values | CSV | N/A | True | Specify a comma-separated list of values that will be used to search for the correct file/process.  
  
#### Run on

IP address, Hostname.

#### Action results

##### Script result

Script result name | Value options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
If the action runs successfully (no errors returned, server response is **200 OK**) on at least one of the entities, `is_success` should be set to `True`.

##### JSON result
    
    
    {
       "malopId": "NOMALOP",
       "remediationId": "75e6e05c-99be-4c64-92c5-a237f1c1177a",
       "start": 1684176792584,
       "end": null,
       "initiatingUser": "string",
       "final_status": {taken from last status from 'statusLog'| PROCESS_NOT_FOUND},
       "process_identifier": {name of the process that was killed}
       "statusLog": [
           {
               "machineId": "ClfZtxCi55eyTiwX",
               "targetId": "ClfZt5Hmhmiu6g-U",
               "status": "PENDING",
               "actionType": "KILL_PROCESS",
               "error": null,
               "timestamp": 1684176793876,
               "empty": false
           },
           {
               "machineId": "ClfZtxCi55eyTiwX",
               "targetId": "ClfZt5Hmhmiu6g-U",
               "status": "IN_PROGRESS",
               "actionType": "KILL_PROCESS",
               "error": null,
               "timestamp": 1684176793981,
               "empty": false
           },
           {
               "machineId": "ClfZtxCi55eyTiwX",
               "targetId": "ClfZt5Hmhmiu6g-U",
               "status": "PENDING",
               "actionType": "KILL_PROCESS",
               "error": null,
               "timestamp": 1684176794006,
               "empty": false
           }
       ],
       "empty": false
    }
    

##### Case wall

Result type | Value/Description | Type (Entity/General)  
---|---|---  
Output message* | **The action should neither fail nor stop a playbook execution:**  


  * _If at least one endpoint was found, and a process or a file was also found on the same endpoint, and the status is "SUCCESS" (`is_success=true`):_

Successfully initiated "{action}" remediation for "{value}" on the following endpoints in Cybereason: {entity identifier}  


  * _If at least one endpoint was found, and a process or a file was also found on the same endpoint, and the status is "FAILURE" or "ABORTED" (`is_success=false`):_

Action initiated "action" remediation for "{values}", but wasn't able to finish successfully on the following endpoints in Cybereason: {entity identifier}  


  * _If none of the endpoints were found (`is_success=false`):_

No endpoints were found in Cybereason.  


  * _If a process or a file is not found in the scope of a malop (`is_success` is not impacted by this):_

The following processes or files were not found in malop {malopid}: {values}. Please check the spelling.  


  * _If all processes are not found in a malop (`is_success=false`):_

None of the provided processes/files were found in the malop {id}. Please check the spelling.  


  * _Async message:_

Pending endpoints: {entities}  
  
**The action should fail and stop a playbook execution:**  


  * _If there is a fatal error, such as wrong credentials, or no connection to server, or other:_

print: "Error executing action "Remediate Malop". Reason: {0}''.format(error.Stacktrace)  


  * _If timeout:_

print: "Error executing action "Remediate Malop". Reason: action ran into a timeout during execution. Pending endpoints: {endpoints that are still in progress}. Please increase the timeout in IDE. | General  
  
### Set Reputation

#### Description

Set a reputation for an entity in Cybereason. Supported entities: File Hash, IP Address, URL.

**Note:** This action extracts the domain part out of the URL entity. Only the MD5 and SHA1 hashes are supported.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Reputation List Type | List | N/A | Yes | Specify the reputation that needs to be applied to an entity.  
  
#### Use cases

N/A

#### Run On

This action runs on the following entities:

  * File Hash
  * IP Address
  * URL



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | _If successful for one entity:_ ****"Successfully set "{reputation list type}" reputation for the following entities: {entity.identifier}"_If not successful for one entity:_ "Action wasn't able to set reputation for the following entities: {entity.identifier}"_If not successful for all_ _entities:_ "Reputation was not set for the provided entities." | General  
  
### Unisolate Machine

#### Description

Unisolate a machine in Cybereason. Supported entities: Hostname.

#### Parameters

N/A

#### Run On

This action runs on the Hostname entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "tables": [
            {
                "rows": [
                    ["d5986926-d3dd-41ff-830f-e90345f1adb6",
                     "2019-10-22T06:54:03Z",
                     "Failed logon attempts within 10 mins",
                     "Failed logon attempts within 10 mins",
                     "Low",
                     "Identifies when failed logon attempts are 6 or higher during a 10 minute period.",
                     "ASI Scheduled Alerts",
                     "Microsoft",
                     "3bbdd11a-d490-4248-b1e1-aa31a7dd3123",
                     "c3f18986-eda6-4778-8c02-43e38bbc89e2",
                     " ",
                     " ",
                     "d5986926-d3dd-41ff-830f-e90345f1adb6_f50e7236-7236-4a75-9e9b-68e9dfea7a65",
                     "Unknown",
                     null,
                     false,
                     "2019-10-22T06:28:57Z",
                     "2019-10-22T06:48:57Z",
                     "2019-10-22T06:54:03Z",
                     " ",
                     "{r\\n  \\\"Query\\\": \\\"//In order to view the events that triggered this alert, please add filtering for the original alert\\u2019s time-frame for any table used in this query.\\\\n//This only happens for queries containing conditions on the TimeGenerated column of one or more tables.\\\\n//The original alert's time-frame filter, which should be added to each table in the query is:\\\\n//\\\\\\\"where TimeGenerated between (datetime(10/22/2019 6:28:57 AM)..datetime(10/22/2019 6:48:57 AM))\\\\\\\"\\\\nlet timeframe = 10m;\\\\nSecurityEvent \\\\n| where TimeGenerated > (datetime(10/22/2019 6:48:57 AM)-(2*timeframe)) \\\\n| where EventID == \\\\\\\"4625\\\\\\\"\\\\n| where AccountType == \\\\\\\"User\\\\\\\"\\\\n| summarize min(TimeGenerated), max(TimeGenerated), FailedLogonCount = count() by EventID, Activity, WorkstationName, Account, TargetAccount, TargetUserName, TargetDomainName, LogonType, LogonTypeName, LogonProcessName, Status, SubStatus\\\\n| where FailedLogonCount >= 6\\\\n| project StartTimeUtc = min_TimeGenerated, EndTimeUtc = max_TimeGenerated, FailedLogonCount, EventID, Activity, WorkstationName, Account, TargetAccount, TargetUserName, TargetDomainName, LogonType, LogonTypeName, LogonProcessName, Status, SubStatus\\\\n| extend timestamp = StartTimeUtc, AccountCustomEntity = Account, HostCustomEntity = WorkstationName\\\",\\r\\n  \\\"Query Period\\\": \\\"00:20:00\\\",\\r\\n  \\\"Trigger Operator\\\": \\\"GreaterThan\\\",\\r\\n  \\\"Trigger Threshold\\\": \\\"0\\\",\\r\\n  \\\"Search Query Results Overall Count\\\": \\\"3\\\",\\r\\n  \\\"Total Account Entities\\\": \\\"1\\\",\\r\\n  \\\"Total Host Entities\\\": \\\"1\\\"\\r\\n}\", \"[\\r\\n  {\\r\\n    \\\"$id\\\": \\\"3\\\",\\r\\n    \\\"HostName\\\": \\\"US-DC-V01001\\\",\\r\\n    \\\"Type\\\": \\\"host\\\"\\r\\n  },\\r\\n  {\\r\\n    \\\"$id\\\": \\\"4\\\",\\r\\n    \\\"Name\\\": \\\"administrator\\\",\\r\\n    \\\"NTDomain\\\": \\\"\\\",\\r\\n    \\\"IsDomainJoined\\\": false,\\r\\n    \\\"Type\\\": \\\"account\\\"\\r\\n  }\\r\\n]",
                     "Detection",
                     "a052d33b-b7c4-4dc7-9e17-5c89ea594669",
                     "Sentinel-Check",
                     " ",
                     "Azure Sentinel",
                     "Scheduled Alerts",
                     "SecurityAlert"
                    ], [
                     "d5986926-d3dd-41ff-830f-e90345f1adb6",
                     "2019-10-23T15:24:15Z",
                     "Failed logon attempts within 10 mins",
                     "Failed logon attempts within 10 mins",
                     "Low",
                     "Identifies when failed logon attempts are 6 or higher during a 10 minute period.",
                     "ASI Scheduled Alerts",
                     "Microsoft",
                     "4f1ac995-f232-4d32-b31c-642e86ef8a3f",
                     "d424e7c0-0d99-45fd-a634-36bd87a6f1ce",
                     " ",
                     " ",
                     "d5986926-d3dd-41ff-830f-e90345f1adb6_f50e7236-7236-4a75-9e9b-68e9dfea7a65",
                     "Unknown",
                     null,
                     false,
                     "2019-10-23T14:59:07Z",
                     "2019-10-23T15:19:07Z",
                     "2019-10-23T15:24:15Z",
                     " ",
                     "{\\r\\n  \\\"Query\\\": \\\"//In order to view the events that triggered this alert, please add filtering for the original alert\\u2019s time-frame for any table used in this query.\\\\n//This only happens for queries containing conditions on the TimeGenerated column of one or more tables.\\\\n//The original alert's time-frame filter, which should be added to each table in the query is:\\\\n//\\\\\\\"where TimeGenerated between (datetime(10/23/2019 2:59:07 PM)..datetime(10/23/2019 3:19:07 PM))\\\\\\\"\\\\nlet timeframe = 10m;\\\\nSecurityEvent \\\\n| where TimeGenerated > (datetime(10/23/2019 3:19:07 PM)-(2*timeframe)) \\\\n| where EventID == \\\\\\\"4625\\\\\\\"\\\\n| where AccountType == \\\\\\\"User\\\\\\\"\\\\n| summarize min(TimeGenerated), max(TimeGenerated), FailedLogonCount = count() by EventID, Activity, WorkstationName, Account, TargetAccount, TargetUserName, TargetDomainName, LogonType, LogonTypeName, LogonProcessName, Status, SubStatus\\\\n| where FailedLogonCount >= 6\\\\n| project StartTimeUtc = min_TimeGenerated, EndTimeUtc = max_TimeGenerated, FailedLogonCount, EventID, Activity, WorkstationName, Account, TargetAccount, TargetUserName, TargetDomainName, LogonType, LogonTypeName, LogonProcessName, Status, SubStatus\\\\n| extend timestamp = StartTimeUtc, AccountCustomEntity = Account, HostCustomEntity = WorkstationName\\\",\\r\\n  \\\"Query Period\\\": \\\"00:20:00\\\",\\r\\n  \\\"Trigger Operator\\\": \\\"GreaterThan\\\",\\r\\n  \\\"Trigger Threshold\\\": \\\"0\\\",\\r\\n  \\\"Search Query Results Overall Count\\\": \\\"1\\\",\\r\\n  \\\"Total Account Entities\\\": \\\"1\\\",\\r\\n  \\\"Total Host Entities\\\": \\\"1\\\"\\r\\n}\", \"[\\r\\n  {\\r\\n    \\\"$id\\\": \\\"3\\\",\\r\\n    \\\"HostName\\\": \\\"DESKTOP-45ISRTV\\\",\\r\\n    \\\"Type\\\": \\\"host\\\"\\r\\n  },\\r\\n  {\\r\\n    \\\"$id\\\": \\\"4\\\",\\r\\n    \\\"Name\\\": \\\"avmilen\\\",\\r\\n    \\\"NTDomain\\\": \\\"DESKTOP-45ISRTV\\\",\\r\\n    \\\"Type\\\": \\\"account\\\"\\r\\n  }\\r\\n]",
                     "Detection",
                     "a052d33b-b7c4-4dc7-9e17-5c89ea594669",
                     "Sentinel-Check",
                     " ",
                     "Azure Sentinel",
                     "Scheduled Alerts",
                     "SecurityAlert"]],
                "name": "PrimaryResult",
                "columns": [
                    {
                        "type": "string",
                        "name": "TenantId"
                    }, {
                        "type": "datetime",
                        "name": "TimeGenerated"
                    }, {
                        "type": "string",
                        "name": "DisplayName"
                    }, {
                        "type": "string",
                        "name": "AlertName"
                    }, {
                        "type": "string",
                        "name": "AlertSeverity"
                    }, {
                        "type": "string",
                        "name": "Description"
                    }, {
                        "type": "string",
                        "name": "ProviderName"
                    }, {
                        "type": "string",
                        "name": "VendorName"
                    }, {
                        "type": "string",
                        "name": "VendorOriginalId"
                    }, {
                        "type": "string",
                        "name": "SystemAlertId"
                    }, {
                        "type": "string",
                        "name": "ResourceId"
                    }, {
                        "type": "string",
                        "name": "SourceComputerId"
                    }, {
                        "type": "string",
                        "name": "AlertType"
                    }, {
                        "type": "string",
                        "name": "ConfidenceLevel"
                    }, {
                        "type": "real",
                        "name": "ConfidenceScore"
                    }, {
                        "type": "bool",
                        "name": "IsIncident"
                    }, {
                        "type": "datetime",
                        "name": "StartTime"
                    }, {
                        "type": "datetime",
                        "name": "EndTime"
                    }, {
                        "type": "datetime",
                        "name": "ProcessingEndTime"
                    }, {
                        "type": "string",
                        "name": "RemediationSteps"
                    }, {
                        "type": "string",
                        "name": "ExtendedProperties"
                    }, {
                        "type": "string",
                        "name": "Entities"
                    }, {
                        "type": "string",
                        "name": "SourceSystem"
                    }, {
                        "type": "string",
                        "name": "WorkspaceSubscriptionId"
                    }, {
                        "type": "string",
                        "name": "WorkspaceResourceGroup"
                    }, {
                        "type": "string",
                        "name": "ExtendedLinks"
                    }, {
                        "type": "string",
                        "name": "ProductName"
                    }, {
                        "type": "string",
                        "name": "ProductComponentName"
                    }, {
                        "type": "string",
                        "name": "Type"
                    }
                ]
            }
        ]
    }
    

##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | _If successful for one machine (is_success = true):_ ****"Successfully unisolated the following machines in Cybereason: {entity.identifier}"_If some machines are not found (is_success=true):_ ****"The following machines were not found in Cybereason: {entity.identifier}"_If none of the machines are found (is_success=false):_ ****"None of the machines were found in Cybereason."_If unisolation is not finished and run into timeout:_ "Unisolation was initiated on the following entities, but wasn't finished: {entity.identifier}. Please execute the action again with bigger timeout."_If a critical error is reported:_ ****"Error executing action "Unisolate Machine". Reason: {traceback}" | General  
  
### Update Malop Status

#### Description

Update status for the malop in Cybereason.

**Note:** Detection malops supports only the "Remediated", "Not Relevant" or "Open" statuses.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Malop ID | String | N/A | Yes | Specify the ID of the malop that needs to be updated.  
Status | List | N/A | Yes | Specify the new status for the malop.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Case Wall

**Result Type** | **Value / Description** | **Type**  
---|---|---  
Output message* | _If successful:_ **"** Successfully updated status for malop with ID {ID} in Cybereason."_If the malop is not found (fail):_ "Error executing action "{action name}". Reason: malop with ID {ID} was not found in Cybereason."_If a critical error is reported:_ "Error executing action "{action name}". Reason: {traceback}" | General  
  
### List Reputation Items

#### Description

List information about items with reputation in Cybereason.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Filter Logic | DDL | EqualPossible Values:

  * Equal
  * Contains

| No | Specify what filter logic should be applied.  
Filter Value | String | N/A | No | Specify the value that should be used in the filter. If "Equal" is selected, the action tries to find the exact match among results.If "Contains" is selected, the action tries to find results that contain the specified substring.If nothing is provided in this parameter, the filter is not applied.  
Max Results To Return | Integer | 50 | No | Specify the number of results to return.  
  
#### Run On

This action doesn't use any of the Google SecOps entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "key": "8cc79ae4d27210976a5bd50a60ec99f4",
        "reputation": "blacklist",
        "prevent_execution": "false",
        "comment": "null",
        "remove": "false"
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If data is available (is_success=true):_ "Successfully found reputation items for the provided criteria in Cybereason".  
****_If data is not available (is_success=false):_ "No reputation items were found for the provided criteria in Cybereason"  
******The action should fail and stop a playbook execution:******  
****_If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "List Reputation Items". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table  
****| **Table Name:** Available Reputation Items**Table Columns:** The action creates a separate column for each key included in the response. | General  
  
### Execute Simple Investigation Search

#### Description

Execute investigation search based on parameters in Cybereason.

**Note:** This action doesn't support nested queries. Only one type of data, for example, machines or users can be queried at once. For nested queries refer to the "Execute Custom Investigation Search" action.

#### How to prepare a query

This action supports a query that looks slightly different than what you enter in the UI. The general structure of the query is: {key} {operator} {values}

For this action you need to provide specific API fields. For example, in the UI you can see "Platform architecture", but the corresponding API field is "platformArchitecture". A list of all available API fields is provided [here](https://nest.cybereason.com/documentation/api-documentation/all-versions/query-elements-and-features).

**Note:** The "array" type fields are not supported.

Operators also differ between UI and API. The action supports the following operators:

  * Equals
  * NotEquals
  * ContainsIgnoreCase
  * NotContainsIgnoreCase
  * LessThan
  * LessOrEqualsTo
  * GreaterThan
  * GreaterOrEqualsTo
  * Between
  * Includes
  * NotIncludes



To provide multiple values for the same key you need to separate them using the "OR" key. For example: platformArchitecture Equals ARCH_X86 OR ARCH_ARM

Each additional filter should be a separate line. Keep in mind that this action only supports one type of request. This means that you can only query either machines or users, but you can't find all users that are in the machine with the ARM architecture. For more complex cases, see the "Execute Custom Investigation Search" action.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Query Filters JSON | List of JSON | [{ "request_type": "{request type 1}", "queries": ["Query 1", "Query 2"], "connection": "{connection feature}" }, { "request_type": "{request type 2}", "queries": ["Query 3"] }] | Yes | Specify the query that needs to be executed. **Note:** The query should follow a strict pattern of "{API field } {Operator} {Value}". For multiple values you need to provide an "OR" key. Each new filter needs to be a separate item in the list. Each key represents the request type, for example, machine or user. Possible operators: 

  * Equals 
  * NotEquals
  * ContainsIgnoreCase
  * NotContainsIgnoreCase 
  * LessThan
  * LessOrEqualsTo
  * GreaterThan
  * GreaterOrEqualsTo
  * Between
  * Includes
  * NotIncludes

  
Fields To Return | CSV | N/A | Yes | Specify a comma-separated list of fields that need to be returned. **Note:** You need to provide API field names.  
Max Results To Return | Integer | 50 | No | Specify the number of results to return.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "simpleValues": {
                "isActiveProbeConnected": {
                    "totalValues": 1,
                    "values": [
                        "false"
                    ]
                },
                "osVersionType": {
                    "totalValues": 1,
                    "values": [
                        "Windows_7"
                    ]
                }
            }
        },
        {
            "simpleValues": {
                "isActiveProbeConnected": {
                    "totalValues": 1,
                    "values": [
                        "false"
                    ]
                }
            }
        }
    ]
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available (is_success = true):_ "Successfully executed query in Cybereason"._If data is not available (is_success=true):_ "No data was found for the provided query in Cybereason.".**The action should fail and stop a playbook execution:**_If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "Execute Simple Investigation Search". Reason: {0}''.format(error.Stacktrace)_If the 400 or 200 status code with the "Failure" status is reported:_ "Error executing action "Execute Simple Investigation Search". Reason: Invalid query provided. Please double check the structure and syntax.'' | General  
Case Wall Table  
****| **Table Name:** Search Results**Table Columns:** The action creates a separate column for each key included in the "simpleValues" JSON object. | General  
  
### Execute Custom Investigation Search

#### Description

Execute investigation search based on parameters in Cybereason. This action supports nested queries for different item types.

#### How to prepare a query

This action supports a query that looks slightly different than what you enter in the UI. The general structure of the query is as follows:
    
    
    [
        {
            "request_type": "REQUEST_TYPE",
            "queries": [
                "KEY OPERATOR VALUES"
            ]
        }
    ]
    

For this action, you need to provide specific API fields.

In the following example, the UI displays the **Platform architecture** field that corresponds to the `platformArchitecture` API field:
    
    
    [
        {
            "request_type": "Machine",
            "queries": [
                "platformArchitecture Equals ARCH_X86 OR ARCH_ARM",
            ]
        }
    ]
    

If you send the same query without any filters, the result is as follows:
    
    
    [
        {
            "request_type": "Machine",
            "queries": [
    
            ]
        }
    ]
    

A list of all available API fields is provided [here](https://nest.cybereason.com/documentation/api-documentation/all-versions/query-elements-and-features).

**Note:** The `array` type fields are not supported.

Operators also differ between UI and API. The action supports the following operators:

  * Equals
  * NotEquals
  * ContainsIgnoreCase
  * NotContainsIgnoreCase
  * LessThan
  * LessOrEqualsTo
  * GreaterThan
  * GreaterOrEqualsTo
  * Between
  * Includes
  * NotIncludes



To provide multiple values for the same key you need to separate them using the "OR" key. For example: platformArchitecture Equals ARCH_X86 OR ARCH_ARM

Each additional filter should be a separate line. For example:
    
    
    [
        {
            "request_type": "Machine",
            "queries": [
                "platformArchitecture Equals ARCH_X86 OR ARCH_ARM",
                "osVersionType Equals Windows_10"
            ]
        }
    ]
    

This query looks like this in the UI:

![Query in UI](https://docs.cloud.google.com/static/chronicle/images/integrations/cybereason-query-ui-example1.png)

To find all users that are on the provided machines, you can use the following query:
    
    
    [
        {
            "request_type": "Machine",
            "queries": [
                "platformArchitecture Equals ARCH_X86 OR ARCH_ARM",
                "osVersionType Equals Windows_10"
            ],
            "connection": "users"
        },
        {
            "request_type": "User",
            "queries": [
                "emailAddress ContainsIgnoreCase administrator"
            ]
        }
    ]
    

**Key** | **Description**  
---|---  
"request_type" | Key that contains the name of the object that needs to be queried.  
"queries" | Key that contains a list of all query filters.  
"connection" | Key that contains the connection feature. This key is mandatory when multiple resource types are queried. A list of all possible connection features is available [here](https://nest.cybereason.com/documentation/api-documentation/all-versions/use-multiple-elements-query#connection-features).  
  
This query looks like this in the UI:

![Query in UI](https://docs.cloud.google.com/static/chronicle/images/integrations/cybereason-query-ui-example2.png)

Keep in mind that the order of the fields provided in the JSON file matters. If you provide multiple resource types, then all objects except for the last one should have "connection" keys with valid value. If only one resource type is provided then this parameter is not needed.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Query Filters JSON | List of JSON | [{ "request_type": "{request type 1}", "queries": ["Query 1", "Query 2"], "connection": "{connection feature}" }, { "request_type": "{request type 2}", "queries": ["Query 3"] }] | Yes | Specify the query that needs to be executed. **Note:** The query should follow a strict pattern of "{API field } {Operator} {Value}". For multiple values you need to provide an "OR" key. Each new filter needs to be a separate item in the list. Each key represents the request type, for example, machine or user.Possible operators: 

  * Equals 
  * NotEquals 
  * ContainsIgnoreCase
  * NotContainsIgnoreCase
  * LessThan
  * LessOrEqualsTo
  * GreaterThan
  * GreaterOrEqualsTo
  * Between
  * Includes
  * NotIncludes

  
Fields To Return | CSV | N/A | Yes | Specify a comma-separated list of fields that need to be returned. **Note:** You need to provide API field names.  
Max Results To Return | Integer | 50 | No | Specify the number of results to return.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "simpleValues": {
                "isActiveProbeConnected": {
                    "totalValues": 1,
                    "values": [
                        "false"
                    ]
                },
                "osVersionType": {
                    "totalValues": 1,
                    "values": [
                        "Windows_7"
                    ]
                }
            }
        },
        {
            "simpleValues": {
                "isActiveProbeConnected": {
                    "totalValues": 1,
                    "values": [
                        "false"
                    ]
                }
            }
        }
    "user"
    
    ]
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available (is_success = true):_ "Successfully executed query in Cybereason"._If data is not available (is_success=true):_ "No data was found for the provided query in Cybereason.".**The action should fail and stop a playbook execution:**_If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "Execute Simple Investigation Search". Reason: {0}''.format(error.Stacktrace)_If the 400 or 200 status code with the "Failure" status is reported:_ "Error executing action "Execute Simple Investigation Search". Reason: Invalid query provided. Please double check the structure and syntax.'' | General  
Case Wall Table  
****| **Table Name:** Search Results **Table Columns:** The action creates a separate column for each key included in the "simpleValues" JSON object. | General  
  
### Get Sensor Details

#### Description

Get sensor details of entities in Cybereason.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
**Parameter** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
Create Insight | Checkbox | Checked | No | If enabled, the action creates an insight containing information about the sensor.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
      "sensorId": "5e77883de4b0575ddcf824ef:PYLUMCLIENT_INTEGRATION_CYBEREASON-WINS_000C29D6CBF7",
      "pylumId": "PYLUMCLIENT_INTEGRATION_CYBEREASON-WINS_000C29D6CBF7",
      "guid": "-257627486.1198775089551518743",
      "fqdn": "cybereason-wins",
      "machineName": "cybereason-wins",
      "internalIpAddress": "10.10.253.213",
      "externalIpAddress": "65.155.239.27",
      "siteName": "Default",
      "siteId": 0,
      "ransomwareStatus": "DETECT_SUSPEND_PREVENT",
      "preventionStatus": "DISABLED",
      "isolated": false,
      "disconnectionTime": 1636125851418,
      "lastPylumInfoMsgUpdateTime": 1636125550769,
      "status": "Offline",
      "serviceStatus": "Down",
      "onlineTimeMS": 0,
      "offlineTimeMS": 0,
      "staleTimeMS": 0,
      "archiveTimeMs": null,
      "statusTimeMS": 0,
      "lastStatusAction": "None",
      "archivedOrUnarchiveComment": "",
      "sensorArchivedByUser": "",
      "serverName": "integration-1-t",
      "serverId": "5e77883de4b0575ddcf824ef",
      "serverIp": "10.203.17.16",
      "privateServerIp": "10.203.17.16",
      "collectiveUuid": null,
      "osType": "WINDOWS",
      "osVersionType": "Windows_20H2",
      "collectionStatus": "ADVANCED",
      "version": "20.2.244.0",
      "consoleVersion": null,
      "firstSeenTime": 1619187651379,
      "upTime": 540984407,
      "cpuUsage": 0.0,
      "memoryUsage": 0,
      "outdated": false,
      "amStatus": "AM_DETECT_ONLY",
      "amModeOrigin": null,
      "avDbVersion": "86106",
      "avDbLastUpdateTime": 1636124994000,
      "powerShellStatus": "PS_DISABLED",
      "remoteShellStatus": "AC_ENABLED",
      "usbStatus": "DISABLED",
      "fwStatus": "DISABLED",
      "antiExploitStatus": "AE_DISABLED",
      "documentProtectionStatus": "DS_UNKNOWN",
      "documentProtectionMode": "DM_UNKNOWN",
      "organizationalUnit": "",
      "antiMalwareStatus": "AM_ENABLED",
      "antiMalwareModeOrigin": null,
      "organization": "integration",
      "proxyAddress": "",
      "preventionError": "BLOCKI_GENERAL_ERROR",
      "exitReason": "STOP_REQUEST_FROM_PYLUM",
      "actionsInProgress": 0,
      "pendingActions": [],
      "lastUpgradeResult": "None",
      "department": null,
      "location": null,
      "criticalAsset": null,
      "deviceType": null,
      "customTags": null,
      "lastUpgradeSteps": [],
      "disconnected": true,
      "staticAnalysisDetectMode": "DISABLED",
      "staticAnalysisDetectModeOrigin": null,
      "staticAnalysisPreventMode": "DISABLED",
      "staticAnalysisPreventModeOrigin": null,
      "collectionComponents": [
        "DPI",
        "Metadata",
        "File Events",
        "Registry Events"
      ],
      "sensorLastUpdate": 0,
      "fullScanStatus": "IDLE",
      "quickScanStatus": "IDLE",
      "lastFullScheduleScanSuccessTime": 0,
      "lastQuickScheduleScanSuccessTime": 1636103116000,
      "policyName": "Default",
      "deliveryTime": 1628671127981,
      "policyId": "be944da9-89e9-48e0-8c84-80000a6f2b29",
      "compliance": true,
      "groupId": null,
      "groupName": "Unassigned"
    }
    

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
sensor_status | Returns if it exists in JSON result  
sensor_groupName | Returns if it exists in JSON result  
sensor_policyName | Returns if it exists in JSON result  
sensor_isolated | Returns if it exists in JSON result  
sensor_internalIpAddress | Returns if it exists in JSON result  
sensor_machineName | Returns if it exists in JSON result  
sensor_fqdn | Returns if it exists in JSON result  
sensor_serviceStatus | Returns if it exists in JSON result  
sensor_osType | Returns if it exists in JSON result  
sensor_site | Returns if it exists in JSON result  
sensor_upTime | Returns if it exists in JSON result  
  
##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
****_If data is available (is_success = true):_ "Successfully found sensor information in Cybereason for the following entities: {entity identifier}"._If data is not available for one entity (is_success=false):_ "Action wasn't able to find sensor information in Cybereason for the following entities: {entity identifier}". _If data is not available for all entities (is_success=false):_ "No sensor information was found for the provided entities in Cybereason".  
******The action should fail and stop a playbook execution:******  
****_If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "Get Sensor Details". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table  
****| **Table Name:** {entity.identifier}**Table Columns:**

  * FQDN - fqdn
  * Name - machineName
  * IP Address - internalIpAddress
  * Site - siteName
  * Isolated - isolated
  * Uptime - upTime
  * Policy - policyName
  * Group - groupName
  * Status - status
  * Service Status - serviceStatus

| General  
  
## Connector

### Cybereason - Malops Inbox Connector

Pull alerts from Malops Inbox in Cybereason.

#### Configure Cybereason - Malops Inbox Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | malopDetectionType | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | Yes | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | Yes | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Cybereason server URL | String | https:/{{api root}} | Yes | The full URL of your Cybereason instance to connect to.  
Login | String | N/A | Yes | The username for the account used to connect to Cybereason.  
Password | Password | N/A | Yes | The password for the account used to connect to Cybereason.  
Script Timeout (Seconds) | Integer | 120 | Yes | Timeout limit for the python process running the current script.  
Offset Time In Hours | Integer | 24 | Yes | The number of hours preceding the current time from which to fetch alerts.  
Max malops per cycle | Integer | 100 | Yes | The amount of MalOps to process for every connector iteration.  
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
