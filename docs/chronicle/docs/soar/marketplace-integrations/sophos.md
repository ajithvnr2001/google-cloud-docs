---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sophos/
title: Sophos \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:09.292655+00:00
---

# Sophos  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sophos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Sophos

This document provides guidance on how to integrate Sophos with Google SecOps.

## Configure Sophos integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://api.central.sophos.com | Yes | API root of the Sophos instance.  
Client ID | String | N/A | Yes | Client ID of the Sophos account.  
Client Secret | Secret | N/A | Yes | Client Secret of the Sophos account.  
SIEM API Root | String | N/A | No | SIEM API root of the Sophos instance. Required for the "Get Events Log" action.  
API Key | Password | N/A | No | Sophos API key. Required for the "Get Events Log" action.  
Base 64 Auth Payload | Password | N/A | No | Sophos Base 64 Auth Payload. **Note:** "Basic" shouldn't be a part of it. Required for the "Get Events Log" parameter.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Sophos server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Where to find SIEM API Root, API Key, and Base64 Auth Payload

To get the API credentials from Sophos Central, use the following **Credentials Management** process:

  1. Sign in to Sophos Central and navigate to **Global Settings > Integration Credential Manager**.

  2. Click **Create Credential** and provide a name and description.

  3. In the newly created credential, copy the API Access URL and paste it into **SIEM API Root** in the connector configuration.

  4. Copy the x-api-key value and paste it into **API Key** in the connector configuration.

  5. Copy the Authorization header value, excluding the Basic string, and paste it into **Base64 Auth Payload** .




Example: `"MzNiYjEyN2ItYzaaYS00MzI5LWFjZWQtOTNjZGEwNTVhMDIyOk41WkpXU1pXUUlFVVJQQ1JJRUM1WFlUTEJXNURNUFYzK1R6MnpyZGhqUW85V2xsMktta3N3ZDN4cDY4R2FvTk40OVJ2UDaaUjk="`

## Where to find Client ID and Client Secret

  1. Navigate to **Global Settings" - > "API Credentials Management**.
  2. Click **Add Credential** and provide a token name.
  3. Provide "Credential name" and select "Service Principal Super Admin" role.
  4. Copy "Client ID" and "Client Secret".



## Product Use Cases

Enrich entities.

## Actions

### Ping

#### Description

Test connectivity to Sophos with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

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
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ "Successfully connected to the Sophos server with the provided connection parameters!"**The action should fail and stop a playbook execution:******_If not successful:_ "Failed to connect to the Sophos server! Error is {0}".format(exception.stacktrace) | General  
  
### Get Service Status

#### Description

Retrieve information about services on endpoints in Sophos. Supported entities: IP Address, Hostname.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
                    "services": {
                        "status": "good",
                        "serviceDetails": [
                            {
                                "name": "HitmanPro.Alert service",
                                "status": "running"
                            },
                            {
                                "name": "Sophos Anti-Virus",
                                "status": "running"
                            },
                            {
                                "name": "Sophos Anti-Virus Status Reporter",
                                "status": "running"
                            },
                            {
                                "name": "Sophos AutoUpdate Service",
                                "status": "running"
                            },
                            {
                                "name": "Sophos Clean",
                                "status": "running"
                            },
                            {
                                "name": "Sophos Clean Service",
                                "status": "running"
                            },
                            {
                                "name": "Sophos Device Control Service",
                                "status": "running"
                            },
                            {
                                "name": "Sophos Endpoint Defense",
                                "status": "running"
                            },
                            {
                                "name": "Sophos Endpoint Defense Service",
                                "status": "running"
                            },
                            {
                                "name": "Sophos File Scanner",
                                "status": "running"
                            },
                            {
                                "name": "Sophos File Scanner Service",
                                "status": "running"
                            },
                            {
                                "name": "Sophos IPS",
                                "status": "running"
                            },
                            {
                                "name": "Sophos MCS Agent",
                                "status": "running"
                            },
                            {
                                "name": "Sophos MCS Client",
                                "status": "running"
                            },
                            {
                                "name": "Sophos Network Threat Protection",
                                "status": "running"
                            },
                            {
                                "name": "Sophos Safestore",
                                "status": "running"
                            },
                            {
                                "name": "Sophos Safestore Service",
                                "status": "running"
                            },
                            {
                                "name": "Sophos System Protection Service",
                                "status": "running"
                            },
                            {
                                "name": "Sophos Web Control Service",
                                "status": "running"
                            },
                            {
                                "name": "Sophos Web Intelligence Filter Service",
                                "status": "running"
                            },
                            {
                                "name": "Sophos Web Intelligence Service",
                                "status": "running"
                            }
                        ]
                    }
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available for one entity (is_success=true):_ "Successfully retrieved service information from the following entities in Sophos: {entity.identifier}."_If not found one entity (is_success=true): "_ The following entities were not found in Sophos: {entity.identifier}."_If not found all entities (is_success=false): "_ None of the provided entities were found in Sophos."**The action should fail and stop a playbook execution:******_If_ a ****_fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Get Service Status". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Title:** {entity.identifier}**Table Columns:**

  * Name - "serviceDetails/name"
  * Status - Capitalized (serviceDetails/status)

| Entity  
  
### Scan Endpoints

#### Description

Initiate a scan on endpoints in Sophos. Supported entities: IP Address, Hostname.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



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
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available for one entity (is_success=true):_ "Successfully initiated scan on the following entities in Sophos: {entity.identifier}."_If not found one (is_success = true):_ The following entities were not found in Sophos: {entity.identifier}_If not found all (is_success = false):_ None of the provided entities were found in Sophos.**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Scan Endpoints". Reason: {0}''.format(error.Stacktrace) | General  
  
### Get Events Log

#### Description

Retrieve logs related to the endpoints in Sophos. Supported entities: IP Address, Hostname.

**Note:** Events are accessible from API only for 24 hours. Requires valid "SIEM API Root", "API Key" and "Base 64 Auth Payload" parameters provided in the integration configuration.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Timeframe | Integer | 12 | Yes | Specify the number of hours backwards events should be retrieved.**Note:** If the user provides more than 24 hours, the action still uses 24.  
Max Events To Return | Integer | 50 | Yes | Specify the number events to return per entity.Maximum: 1000  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "events": [
            {
                "when": "2021-08-25T12:11:59.959Z",
                "appSha256": "7282879dee5b483f07e05e81c610e352f146d29390c7a4bbf6d8bc3335cfeeec",
                "appCerts": [
                    {
                        "signer": "KnowBe4 Inc.",
                        "thumbprint": "20f1ff543d8b5cbe14398a440ddd8c8ec63373f6271d796387b414214ccd9a50"
                    }
                ],
                "threat": "KnowBe4 Ransomware Simulator",
                "created_at": "2021-08-25T12:12:11.432Z",
                "source_info": {
                    "ip": "172.30.201.180"
                },
                "customer_id": "dfb85412-db6e-4289-b5a1-03523a0178b8",
                "severity": "medium",
                "endpoint_id": "5fc739f3-dcab-4a1a-a4cc-d77902621e3b",
                "endpoint_type": "computer",
                "user_id": "61238d60b382960e83de9f54",
                "origin": "SAV",
                "core_remedy_items": null,
                "source": "SOPHOS-H01\\Admin",
                "type": "Event::Endpoint::CorePuaDetection",
                "name": "PUA detected: 'KnowBe4 Ransomware Simulator' at 'C:\\Users\\Admin\\Desktop\\SimulatorSetup.exe'",
                "location": "Sophos-H01",
                "id": "18e3b4a6-86af-4ca1-87ce-5d7a8f29c438",
                "group": "PUA"
            }
        ]
    }
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available for one_ ****entity****_(is_success=true):_ "Successfully retrieved events related to the following endpoints in Sophos: {entity.identifier}."_If not found one entity (is_success=true): "_ The following entities were not found in Sophos: {entity.identifier}."_If not found all entities (is_success=false): "_ None of the provided entities were found in Sophos."_If no events for one endpoint (is_success=true): "_ No events were found for the following endpoints in Sophos: {entity.identifier}."_If no events for all endpoints (is_success=true): "_ No events were found for the provided endpoints in Sophos."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Get Events Logs". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** {entity.identifier}**Table Columns:**

  * Name
  * Type
  * Source
  * Threat
  * Severity
  * Timestamp

| Entity  
  
### Isolate Endpoint

#### Description

Isolate endpoints in Sophos. Supported entities: IP Address, Hostname.

**Note:** This action runs as async. Adjust the script timeout value in the Google SecOps IDE for the action as needed.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Comment | String | N/A | Yes | Specify the comment explaining why the isolation is needed.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



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
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available for one entity (is_success=true):_ "Successfully isolated the following endpoints in Sophos: {entity.identifier}."_If not found one entity (is_success=true): "_ The following entities were not found in Sophos: {entity.identifier}."_If not found all entities (is_success=false): "_ None of the provided entities were found in Sophos."_Async Message: "_ Waiting for isolation to finish on the following entities: {pending entities}."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Isolate Endpoint". Reason: {0}''.format(error.Stacktrace)"_If ran into a timeout: "_ Error executing action "Isolate Endpoint". Reason: action ran into a timeout. Pending entities: {pending entities}. Please increase the timeout in the IDE." | General  
  
### Unisolate Endpoint

#### Description

Unisolate endpoints in Sophos. Supported entities: IP Address, Hostname.

**Note:** This action runs as async. Adjust the script timeout value in the Google SecOps IDE for the action as needed.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Comment | String | N/A | Yes | Specify the comment explaining why the unisolation is needed.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



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
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available for one entity (is_success=true):_ "Successfully unisolated the following endpoints in Sophos: {entity.identifier}."_If not found one entity (is_success=true): "_ The following entities were not found in Sophos: {entity.identifier}."_If not found all entities (is_success=false): "_ None of the provided entities were found in Sophos."_Async Message: "_ Waiting for unisolation to finish on the following entities: {pending entities}."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Unisolate Endpoint". Reason: {0}''.format(error.Stacktrace)"_If ran into a timeout: "_ Error executing action "Unisolate Endpoint". Reason: action ran into a timeout. Pending entities: {pending entities}. Please increase the timeout in the IDE." | General  
  
### List Alert Actions

#### Description

Retrieve actions that can be executed on the alert in Sophos.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert ID | String | N/A | Yes | Specify the ID of the alert for which you want to retrieve details.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    {
        "allowedActions": [
            "clearThreat"
        ]
    }
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available for one alert (is_success=true):_ "Successfully retrieved available actions for the Alert with ID {alert_id} in Sophos."_If no actions are available for the alert (is_success=false):_ "No actions are available for the alert with ID {alert_id} in Sophos."**The action should fail and stop a playbook execution:**___If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "List Alert Actions". Reason: {0}''.format(error.Stacktrace)_If the 400 status code is reported:_ "Error executing action "List Alert Actions". Reason: {0}''.format(message)_If the 404 status code is reported:_ "Error executing action "List Alert Actions". Reason: alert with ID {alert_id} was not found in Sophos.'' | General  
  
### Execute Alert Action

#### Description

Initiate action execution on the alert in Sophos. Use the "List Alert Actions" action to get a list of available actions for the alert.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Alert ID | String | N/A | Yes | Specify the ID of the alert on which you want to execute the action.  
Action | DDL | AcknowledgePossible Values:

  * Acknowledge
  * Clean PUA
  * Clean Virus
  * Auth PUA
  * Clear Threat
  * Clear HMPA
  * Send Message PUA
  * Send Message Threats

| Yes | Specify the action that should be executed on the alert.  
Message | String | N/A | No | Specify a message explaining why the action was executed.  
  
#### Run On

This action doesn't run on entities.

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
Output message* | **The action should not fail nor stop a playbook execution:******_If the 201 status code is reported for one action (is_success=true):_ "Successfully initiated execution of the action "{action name}" for the Alert with ID {alert_id} in Sophos."**The action should fail and stop a playbook execution:**___If a fatal error, like wrong credentials, no connection to server, other:_ "Error executing action "Execute Alert Actions". Reason: {0}''.format(error.Stacktrace)_If the 404 status code is reported:_ "Error executing action "Execute Alert Actions". Reason: alert with ID {alert_id} was not found in Sophos.''_If the 400 status code is reported (is_success=false):_ "Error executing action "Execute Alert Action". Reason: Invalid action was provided for the alert. Please check what actions are available for the provided alert with action "List Alert Actions"." | General  
  
### Add Entities To Blocklist

#### Description

Add entities to blocklist in Sophos. Supported entities: Filehash.

**Note:** Only the SHA-256 hashes are supported.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Comment | String | N/A | Yes | Specify the comment explaining why the hash was sent to blocklist.  
  
#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A ##### Insights

N/A

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If the 201 status code is reported (is_success=true):_ "Successfully added the following entities to blocklist in Sophos: {entity.identifier}."_If the 409 status code is reported (is_success=true):_ "The following entities are already a part of the blocklist in Sophos: {entity.identifier}."_If one hash is invalid (is_success=true):_ "Action wasn't able to add the following entities to blocklist in Sophos: {entity.identifier}"._If all hashes are invalid (is_success=false):_ "None of the provided entities were added to the blocklist in Sophos."**The action should fail and stop a playbook execution:**___If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Add Entities To Blocklist". Reason: {0}''.format(error.Stacktrace) | General  
  
### Add Entities To Allowlist

#### Description

Add entities to allowlist in Sophos. Supported entities: Filehash.

**Note:** Only the SHA-256 hashes are supported.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Comment | String | N/A | Yes | Specify the comment explaining why the hash was sent to allowlist.  
  
#### Run on

This action runs on the Filehash entity.

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
Output message* | **The action should not fail nor stop a playbook execution:******_If the 201 status code is reported (is_success=true):_ "Successfully added the following entities to allowlist in Sophos: {entity.identifier}."_If the 409 status code is reported (is_success=true):_ "The following entities are already a part of the allowlist in Sophos: {entity.identifier}."_If one hash is invalid (is_success=true):_ "Action wasn't able to add the following entities to allowlist in Sophos: {entity.identifier}."_If all hashes are invalid (is_success=false):_ "None of the provided entities were added to the allowlist in Sophos."**The action should fail and stop a playbook execution:******_If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Add Entities To Allowlist". Reason: {0}''.format(error.Stacktrace) | General  
  
### Case Enrich Entities

#### Description

Enrich entities using information from Sophos. Supported entities: Hostname, IP Address, Filehash.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Create Insight | Checkbox | Checked | No | If enabled, the action creates an insight containing all of the retrieved information about the entity.  
  
#### Run On

This action runs on the following entities:

  * Hostname
  * IP Address
  * Filehash



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result for Host
    
    
    {
        "id": "5fc739f3-dcab-4a1a-a4cc-d77902621e3b",
        "type": "computer",
        "tenant": {
            "id": "dfb85412-db6e-4289-b5a1-03523a0178b8"
        },
        "hostname": "Sophos-H01",
        "health": {
            "overall": "suspicious",
            "threats": {
                "status": "suspicious"
            },
            "services": {
                "status": "good",
                "serviceDetails": [
                    {
                        "name": "HitmanPro.Alert service",
                        "status": "running"
                    }
                ]
            }
        },
        "os": {
            "isServer": false,
            "platform": "windows",
            "name": "Windows 10 Enterprise Evaluation",
            "majorVersion": 10,
            "minorVersion": 0,
            "build": 19043
        },
        "ipv4Addresses": [
            "172.30.201.180"
        ],
        "macAddresses": [
            "00:50:56:A2:73:E8"
        ],
        "associatedPerson": {
            "name": "SOPHOS-H01\\Admin",
            "viaLogin": "SOPHOS-H01\\Admin",
            "id": "3d5b16cc-cc1c-4adc-97fb-b57adc9b16d8"
        },
        "tamperProtectionEnabled": true,
        "assignedProducts": [
            {
                "code": "endpointProtection",
                "version": "10.8.11.1",
                "status": "installed"
            },
            {
                "code": "interceptX",
                "version": "2.0.22",
                "status": "installed"
            },
            {
                "code": "coreAgent",
                "version": "2.19.6",
                "status": "installed"
            }
        ],
        "lastSeenAt": "2021-09-09T11:02:22.259Z"
    }
    

##### JSON Result
    
    
    {
        "id": "2c43575d-7b8c-4b8a-a65c-4248662ef369",
        "createdAt": "2021-09-01T12:50:34.879Z",
        "properties": {
            "sha256": "ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48ba"
        },
        "comment": "asdasda",
        "type": "sha256"
    }
    

##### Entity Enrichment

##### Enrichment Table for Host

Enrichment Field Name | Logic - When to apply  
---|---  
health | When available in JSON  
threat\\_status | When available in JSON  
services\\_status | When available in JSON  
type | When available in JSON  
hostname | When available in JSON  
os | When available in JSON  
os\\_build | When available in JSON  
ipv4 | When available in JSON  
mac\\_address | When available in JSON  
associated\\_person | When available in JSON  
is\\_server | When available in JSON  
last\\_seen | When available in JSON  
isolated | When available in JSON  
  
##### Enrichment Table for Hash

Enrichment Field Name | Logic - When to apply  
---|---  
type | When available in JSON  
comment | When available in JSON  
createdAt | When available in JSON  
  
##### Insights

N/A

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available for one entity (is_success=true):_ "Successfully enriched the following entities using information from Sophos: {entity.identifier}."_If data is not available for one entity (is_success=true):_ "Action wasn't able to enrich the following entities using information from Sophos: {entity.identifier}".  
_If data is not available for all entities (is_success=false): "_ None of the provided entities were enriched."**The action should fail and stop a playbook execution:**___If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Title:** {entity.identifier}**Table Columns:**

  * Key
  * Value

| Entity  
  
## Connectors

### Sophos Central - Alerts Connector

#### Description

Pull alerts from Sophos Central into Google SecOps.

**Note:** Alerts are available to API only for 24 hours.

#### Configure Sophos Central - Alerts Connector in Google SecOps

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
API Root | String | https:/{{api root}} | Yes | API root of the Sophos instance.  
Client ID | String | N/A | No | Client ID of the Sophos instance.  
Client Secret | Password | N/A | No | Client Secret of the Sophos instance.  
API Key | Password | N/A | Yes | Sophos API key.  
Base 64 Auth Payload | Password | N/A | Yes | Sophos Base 64 Auth Payload. **Note:** "Basic" shouldn't be a part of it.  
Lowest Severity To Fetch | String | N/A | No | Severity that is used to fetch alerts. If nothing is specified, the action ingests all alerts. Possible values: Low, Medium, High.  
Max Hours Backwards | Integer | 1 | No | Number of hours from where to fetch alerts.  Maximum: 24 hours  
Max Alerts To Fetch | Integer | 10 | No | Number of alerts to process per one connector iteration. Maximum: 1000  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist is used as a blacklist.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verifies that the SSL certificate for the connection to the Sophos Central server is valid.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector rules

##### Proxy support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
