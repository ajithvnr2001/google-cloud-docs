---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fortinet-fortisiem/
title: Fortinet FortiSIEM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:25.010697+00:00
---

# Fortinet FortiSIEM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fortinet-fortisiem/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Fortinet FortiSIEM

This document describes how to integrate Fortinet FortiSIEM with Google Security Operations.

## Configure Fortinet FortiSIEM integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root | String | https://x.x.x.x:port | Yes | Specify the API root for the target FortiSIEM installation.  
Username | String | N/A | Yes | Specify the username to use for the target FortiSIEM installation.  
Password | Password | N/A | Yes | Specify the password to use for the target FortiSIEM installation.  
Verify SSL | Checkbox | Checked | No | If enabled, the Google SecOps server checks that the certificate is configured for API root.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Product Use Cases

  1. Ingest alerts from SIEM to Google SecOps.
  2. Use data from SIEM for Google SecOps alert enrichment.
  3. Synchronize statuses of processed with Google SecOps alerts back at SIEM side.



## Actions

### Ping

#### Description

Test connectivity to FortiSIEM with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

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
Output message* | **The action should not fail nor stop a playbook execution:** _If successful:_ "Successfully connected to the FortiSIEM installation with the provided connection parameters!" **The action should fail and stop a playbook execution:** >_If not successful:_ "Failed to connect to the FortiSIEM installation! Error is {0}".format(exception.stacktrace)" | General  
  
### Enrich Entities

#### Description

Enrich entities using information from Fortinet FortiSIEM CMDB. Supported entities: Hostname, IP Address.

**Note:** The Hostname entity should contain the "name" of the device.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Target Organization | String | N/A | No | Specify the optional target organization name to look for enrichment information in this organization only.  
  
#### Run On

This action runs on the following entities:

  * Hostname
  * IP Address



#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    [
      {
        "Entity": "centos-xxx",
        "EntityResult": {
          "device": {
            "organization": {
              "@id": "1xx",
              "@name": "Super"
            },
            "accessIp": "172.30.xxx.xxx",
            "approved": "true",
            "components": null,
            "creationMethod": "LOG",
            "deviceType": {
              "accessProtocols": "TELNET,SSH",
              "jobWeight": "10",
              "model": "Unix",
              "vendor": "Generic",
              "version": "ANY"
            },
            "discoverMethod": "LOG",
            "discoverTime": "1640008485000",
            "eventParserList": null,
            "interfaces": null,
            "ipToHostNames": null,
            "luns": null,
            "name": "centos-xxx",
            "naturalId": "centos%2dxxx",
            "processors": null,
            "properties": {
              "customproperty": [
                {
                  "matched": "false",
                  "propertyDef": {
                    "displayInCMDB": "false",
                    "displayName": "Importance",
                    "groupKey": "false",
                    "propertyName": "importance",
                    "subValueType": "STRING",
                    "valueType": "STRING"
                  },
                  "propertyName": "importance",
                  "propertyValue": "Normal",
                  "updated": "false"
                },
                {
                  "matched": "false",
                  "propertyDef": {
                    "displayInCMDB": "false",
                    "displayName": "Location Name",
                    "groupKey": "false",
                    "propertyName": "locationName",
                    "subValueType": "STRING",
                    "valueType": "STRING"
                  },
                  "propertyName": "locationName",
                  "updated": "false"
                }
              ]
            },
            "raidGroups": null,
            "sanControllerPorts": null,
            "softwarePatches": null,
            "softwareServices": null,
            "status": "2",
            "storageGroups": null,
            "storages": null,
            "unmanaged": "false",
            "updateMethod": "LOG",
            "version": "ANY",
            "winMachineGuid": null
          }
        }
      },
      {
        "Entity": "172.30.xxx.xxx",
        "EntityResult": {
          "device": {
            "organization": {
              "@id": "1xx",
              "@name": "Super"
            },
            "accessIp": "172.30.xxx.xxx",
            "applications": null,
            "approved": "true",
            "components": null,
            "creationMethod": "LOG",
            "deviceType": {
              "accessProtocols": "TELNET,SSH",
              "jobWeight": "10",
              "model": "Unix",
              "vendor": "Generic",
              "version": "ANY"
            },
            "discoverMethod": "LOG",
            "discoverTime": "1640070721000",
            "eventParserList": {
              "eventparser": {
                "deviceType": {
                  "category": "Appliance",
                  "jobWeight": "10",
                  "model": "Generic",
                  "vendor": "Generic",
                  "version": "ANY"
                },
                "enabled": "true",
                "name": "SyslogNGParser",
                "parserXml": "<patternDefinitions><pattern>..."
              }
            },
            "interfaces": null,
            "ipToHostNames": null,
            "luns": null,
            "name": "centos-xxx",
            "naturalId": "centos",
            "primaryContactUser": "0",
            "processors": null,
            "properties": {
              "customproperty": [
                {
                  "matched": "false",
                  "propertyDef": {
                    "displayInCMDB": "false",
                    "displayName": "Importance",
                    "groupKey": "false",
                    "propertyName": "importance",
                    "subValueType": "STRING",
                    "valueType": "STRING"
                  },
                  "propertyName": "importance",
                  "propertyValue": "Mission Critical",
                  "updated": "false"
                },
                {
                  "matched": "false",
                  "propertyDef": {
                    "displayInCMDB": "false",
                    "displayName": "Location Name",
                    "groupKey": "false",
                    "propertyName": "locationName",
                    "subValueType": "STRING",
                    "valueType": "STRING"
                  },
                  "propertyName": "locationName",
                  "updated": "false"
                }
              ]
            },
            "raidGroups": null,
            "sanControllerPorts": null,
            "secondaryContactUser": "0",
            "softwarePatches": null,
            "softwareServices": null,
            "status": "2",
            "storageGroups": null,
            "storages": null,
            "unmanaged": "false",
            "updateMethod": "MANUAL",
            "version": "ANY",
            "winMachineGuid": null
          }
        }
      }
    ]
    

##### Entity Enrichment

Enrichment Field Name | Source (JSON Key) | Logic - When to apply  
---|---|---  
accessIp | accessIp | When available in XML  
name | name | When available in XML  
applications | CSV of "applications/name" | When available in XML  
creationMethod | creationMethod | When available in XML  
deviceType_model | deviceType_model | When available in XML  
deviceType_accessProtocolsdeviceType_vendor | deviceType_accessProtocolsdeviceType_vendor | When available in XML  
discoverMethod | discoverMethod | When available in XML  
discoverTime | discoverTime | When available in XML  
  
##### Insights

N/A

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If data is available for one entity (is_success=true):_ "Successfully enriched the following entities using information from FortiSIEM: {entity.identifier}." _If data is not available for one entity (is_success=true):_ "Action wasn't able to enrich the following entities using information from FortiSIEM: {entity.identifier}." _If data is not available for all entities (is_success=false):_ "None of the provided entities were enriched." **The action should fail and stop a playbook execution:** If a fatal error, like wrong credentials, no connection to the server, other is reported: "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Title:** {entity.identifier} **Table Columns:**

  * Key
  * Value

| Entity  
  
### Execute Simple Query

#### Description

Execute FortiSIEM events query based on the provided parameters.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Event Types | CSV | N/A | No | Specify the event types query should fetch. Parameter accepts multiple values as a comma-separated string.  
Minimum Severity to Fetch | Integer | N/A | No | Specify the minimum event severity to fetch to Google SecOps in numbers.Example: 5 or 7  
Event Category | CSV | N/A | No | Specify the event category query should fetch. Parameter accepts multiple values as a comma-separated string.  
Event IDs | CSV | N/A | No | Specify optionally exact event ids query should fetch. Parameter accepts multiple values as a comma-separated string.  
Fields To Return | CSV | N/A | No | Specify the fields to return.If nothing is provided, the action returns all fields.  
Sort Field | String | phRecvTime | No | Specify the parameter that should be used for sorting.  
Sort Order | DDL | DESCPossible Values:

  * ASC
  * DESC

| No | Specify the order of sorting.  
Time Frame | DDL | Last HourPossible Values:

  * Last Hour
  * Last 6 Hours
  * Last 24 Hours
  * Last Week
  * Last Month
  * Custom

| No | Specify a time frame for the results.If "Custom" is selected, you also need to provide the "Start Time" parameter.  
Start Time | String | N/A | No | Specify the start time for the results.This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter.Format: ISO 8601Example: 2021-04-23T12:38Z  
End Time | String | N/A | No | Specify the end time for the results.If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter uses current time.Format: ISO 8601  
Max Results To Return | Integer | 50 | No | Specify the number of results to return.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    [
      {
        "custId": "1",
        "attributes": {
          "eventType": "Unknown_EventType",
          "eventSeverity": "3",
          "eventAction": "0 (Permit)",
          "phRecvTime": "Wed Dec 29 00:36:55 IST 2021",
          "relayDevIpAddr": "172.30.20xxx",
          "reptDevIpAddr": "172.30.20xxx",
          "destIpAddr": "172.30.20xxx",
          "destName": "HOST-172.30.20xxx",
          "reptDevName": "centos-xxx",
          "reptVendor": "Unknown",
          "customer": "Super",
          "reptModel": "Unknown",
          "rawEventMsg": "<27>Dec 29 00:36:47 centos-xxx aella_flow[5074]: 1902195|aos_afix_json|ERR|Failed to send message: Couldn't connect to server/7",
          "collectorId": "1",
          "eventId": "4242813061460978xxx",
          "phEventCategory": "0 (External)",
          "count": "1",
          "eventName": "Unknown event type",
          "eventParsedOk": "0",
          "parserName": "SyslogNGParser"
        },
        "dataStr": null,
        "eventType": "Unknown_EventType",
        "id": "4242813061460978xxx",
        "index": "0",
        "nid": "4242813061460978xxx",
        "receiveTime": "2021-12-29T00:36:55+02:00"
      }
    ]
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If found at least some data (is_success=true):_ "Successfully retrieved results for the constructed query "{query}" in FortiSIEM.". _If no results are found (is_success=false):_ "No results were found for the constructed query "{Query}" in FortiSIEM." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Simple Query". Reason: {0}''.format(error.Stacktrace) _If the "Start Time" parameter is empty and the "Time Frame" parameter is set to "Custom" (fail):_ "Error executing action "". Reason: "Start Time" should be provided, when "Custom" is selected in the "Time Frame" parameter." _If value of the "Start Time" is greater than value of the "End Time" parameter (fail):_ "Error executing action "". Reason: "End Time" should be later than "Start Time". | General  
Table | **Table Name:** Simple Query Results **Table Columns:** All of the columns from response | General  
  
### Execute Custom Query

#### Description

Execute a custom query in FortiSIEM.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Query | String multi line input field | (Attribute = Value OR Value) AND (Attribute Value OR Value) | Yes | Specify a query that is used to retrieve information about the events. Example: (relayDevIpAddr = 172.30.202.1 OR 172.30.202.2) AND (reptDevName = HOST1)  
Fields To Return | CSV |  | No | Specify the fields to return.If nothing is provided, the action returns all fields.  
Sort Field | String | phRecvTime | No | Specify the parameter that should be used for sorting.  
Sort Order | DDL | DESCPossible Values:

  * ASC
  * DESC

| No | Specify the order of sorting.  
Time Frame | DDL | Last HourPossible Values:

  * Last Hour
  * Last 6 Hours
  * Last 24 Hours
  * Last Week
  * Last Month
  * Custom

| No | Specify a time frame for the results.If "Custom" is selected, you also need to provide the "Start Time" parameter.  
Start Time | String | N/A | No | Specify the start time for the results.This parameter is mandatory, if "Custom" is selected for the "Time Frame" parameter.Format: ISO 8601 Example: 2021-04-23T12:38Z  
End Time | String | N/A | No | Specify the end time for the results.If nothing is provided and "Custom" is selected for the "Time Frame" parameter then this parameter uses current time.  
Max Results To Return | Integer | 50 | No | Specify the number of results to return.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success=False  
  
##### JSON Result
    
    
    [
      {
        "custId": "1",
        "attributes": {
          "eventType": "Unknown_EventType",
          "eventSeverity": "3",
          "eventAction": "0 (Permit)",
          "phRecvTime": "Wed Dec 29 00:36:55 IST 2021",
          "relayDevIpAddr": "172.30.20xxx",
          "reptDevIpAddr": "172.30.20xxx",
          "destIpAddr": "172.30.20xxx",
          "destName": "HOST-172.30.20xxx",
          "reptDevName": "centos-xxx",
          "reptVendor": "Unknown",
          "customer": "Super",
          "reptModel": "Unknown",
          "rawEventMsg": "<27>Dec 29 00:36:47 centos-xxx aella_flow[5074]: 1902195|aos_afix_json|ERR|Failed to send message: Couldn't connect to server/7",
          "collectorId": "1",
          "eventId": "4242813061460978xxx",
          "phEventCategory": "0 (External)",
          "count": "1",
          "eventName": "Unknown event type",
          "eventParsedOk": "0",
          "parserName": "SyslogNGParser"
        },
        "dataStr": null,
        "eventType": "Unknown_EventType",
        "id": "4242813061460978xxx",
        "index": "0",
        "nid": "4242813061460978xxx",
        "receiveTime": "2021-12-29T00:36:55+02:00"
      }
    ]
    

##### Entity Enrichment

N/A

##### Insights

N/A

##### Case Wall

Result type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If found at least some data (is_success=true):_ "Successfully retrieved results for the provided query "{query}" in FortiSIEM." _If no results are found (is_success=false):_ "No results were found for the provided query "{Query}" in FortiSIEM." **The action should fail and stop a playbook execution:** _If a fatal error, like wrong credentials, no connection to the server, other is reported:_ "Error executing action "Simple Query". Reason: {0}''.format(error.Stacktrace) _If the "Start Time" parameter is empty and the "Time Frame" parameter is set to "Custom" (fail):_ "Error executing action "". Reason: "Start Time" should be provided, when "Custom" is selected in the "Time Frame" parameter." _If value of the "Start Time" is grater than value of the "End Time" parameter (fail):_ "Error executing action "". Reason: "End Time" should be later than "Start Time". | General  
Table | **Table Name:** Custom Query Results ******Table Columns:** All of the columns from response | General  
  
## Connectors

### FortiSIEM Incidents Connector

#### Connector Description

Connector can be used to fetch FortiSIEM incidents. Connector whitelist can be used to ingest only specific types of incidents based on the incident's "eventType" attribute value. SourceGroupIdentifier of the connector can be used to group Google SecOps alerts based on the incident ID. Connector requires FortiSIEM version 6.3 or newer.

#### Connector Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | deviceProduct | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | eventType | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String |  | No | Describes the name of the field where the environment name is stored.If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field.Default is .* to catch all and return the value unchanged.Used to allow the user to manipulate the environment field via regex logic.If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout | Integer | 300 | Yes | Specify the timeout for connector to run.  
API Root | String | https:/x.x.x.x:port | Yes | Specify the API root for the target FortiSIEM installation.  
Username | String | N/A | Yes | Specify the username to use for the target FortiSIEM installation.  
Password | Password | N/A | Yes | Specify the password to use for the target FortiSIEM installation.  
Verify SSL | Checkbox | Checked | No | If enabled, the Google SecOps server checks the certificate configured for API root.  
Target Organization | CSV | N/A | No | Specify organizations the connector should fetch incidents for. Parameters accepts multiple values as a comma separated string.  
Max hours backwards | Integer | 24 | Yes | Specify the time frame to fetch incidents from X hours backwards.  
Max Incidents Per Cycle | Integer | 10 | Yes | Specify the number of incidents should be processed during one connector run.  
Max Events Per Incidents | Integer | 100 | Yes | Specify the maximum number of events the connector should track for the incident.Once the limit is reached, new events are not added to Google SecOps.  
Incident Statuses to Fetch | CSV | 0 | No | Specify incident's statuses to fetch to Google SecOps.Parameter accepts multiple values as a comma-separated string.0 stands for incidents in open status.  
Minimum Severity to Fetch | Integer | N/A | No | Specify the minimum incident's event severity to fetch to Google SecOps in numbers, for example 5 or 7.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist is used as a blacklist.  
Track New Events Added to Already Ingested Incidents | Checkbox | Checked | Yes | If enabled, if new events are added to already ingested FortiSIEM incident, additional new alert is created in Google SecOps that has those new events.  
Track New Events Threshold (hours) | Integer | 24 | Yes | If "Track New Events Added to Already Ingested Incidents" checkbox is checked, specify the maximum number of hours connector should track already ingested incidents for new events.Once the limit is reached, new events are not added to Google SecOps.  
Proxy Server Address | String | N/A | No | Specify the address of the proxy server to use.  
Proxy Username | String | N/A | No | Specify the proxy username to authenticate with.  
Proxy Password | Password | N/A | No | Specify the proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

Connector supports Proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
