---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/solar-winds-orion/
title: SolarWinds Orion \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:45.441593+00:00
---

# SolarWinds Orion  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/solar-winds-orion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SolarWinds Orion

This document provides guidance on how to integrate SolarWinds Orion with Google SecOps.

### Use Cases

Perform active actions - execute SQL queries to get more information about the endpoint.

## Configure SolarWinds Orion integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
IP Address | String | x.x.x.x:17778 | Yes | IP address of the SolarWinds Orion instance.  
Username | String | N/A | Yes | Username of the SolarWinds Orion account.  
Password | Password | N/A | Yes | Password of the SolarWinds Orion account.  
Verify SSL | Checkbox | Unchecked | No | If enabled, verify the SSL certificate for the connection to the SolarWinds Orion server is valid.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

‌Test connectivity to the SolarWinds Orion with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Run On

This action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_succeed:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If successful:_ Print "Successfully connected to the SolarWinds Orion server with the provided connection parameters!"  
******The action should fail and stop a playbook execution:**  
****_If not successful:_ Print "Failed to connect to the SolarWinds Orion server! Error is {0}".format(exception.stacktrace) | General  
  
### Execute Query

#### Description‌

Execute query in SolarWinds Orion.

#### Parameters

Parameter Display Name | Type | Default Value | Is **M** andatory | Description  
---|---|---|---|---  
Query | String | N/A | Yes | Specify the query that needs to be executed. Note: SolarWind queries don't support "*" notation.  
Max Results To Return | Integer | 100 | No | Specify how many results should be returned.  
  
#### Run On

This action doesn't run on entities, nor has mandatory input parameters.

‌Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
##### JSON Result
    
    
    {
        "results": [
            {
                "DisplayName": "orion"
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If not status code 400 (is_success = true):_ Print "Successfully executed query and retrieved results from SolarWinds Orion".****_If status code 400 (is_success = false):_ Print "Action wasn't able to successfully execute query and retrieve results from SolarWinds Orion. Reason: {0}".format(message)  
******The action should fail and stop a playbook execution:**  
****_If fatal error, like wrong credentials, no connection to server, other:_ Print "Error executing action "Execute Query". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** "Results" All of the columns from the response will be used as table columns. | General  
  
### Execute Entity Query

#### Description

Execute query in SolarWinds Orion based on the IP and Hostname entities.

#### How to work with action parameters

This action gives an ability to easily retrieve information about the endpoints based on the IP and Hostname entities.

Imagine a situation where you want to retrieve the uptime of the endpoints. First endpoint has IP '172.30.230.130' and the second endpoint has hostname 'DC001'. In this case our query would need to look like this:

`SELECT IpAddress, DisplayName, SystemUpTime FROM Orion.Nodes WHERE IpAddress='172.30.203.130' OR DisplayName='DC001'`

In order to create the same query using "Execute Entity Query" action, you need to fill out the action parameters in the following way:

Query | SELECT IpAddress, DisplayName, SystemUpTime FROM Orion.Nodes  
---|---  
IP Entity Key | IpAddress  
Hostname Entity Key | DisplayName  
  
WHERE clause will be prepared automatically.

#### Table Schema Documentation

http://solarwinds.github.io/OrionSDK/2020.2/schema/Orion.Nodes.html

**Note:** Users are expected to provide limitations in the query itself, but we can't rely on that, so we would also perform manual restriction of results on our side.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Query | String | N/A | Yes | Specify the query that needs to be executed. Note: SolarWind queries don't support "*" notation and you shouldn't have a WHERE clause in the query, because it is added by the action. Please refer to the action documentation for details.  
IP Entity Key | String | IpAddress | No | Specify what key should be used with IP entities in the WHERE clause of the query. Please refer to the action documentation for details. Default:IpAddress  
Hostname Entity Key | String | Hostname | No | Specify what key should be used with Hostname entities in the WHERE clause of the query. Please refer to the action documentation for details. Default:Hostname  
Max Results To Return | Integer | 100 | No | Specify how many results should be returned.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Host



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "results": [
            {
                "DisplayName": "orion"
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If not status code 400 (is_success = true):_ Print "Successfully executed query and retrieved results from SolarWinds Orion".****_If status code 400 (is_success = false):_ Print "Action wasn't able to successfully execute query and retrieve results from SolarWinds Orion. Reason: {0}".format(message)****_If no entities in the scope (is_success = false)_ Print "No entities were found in the scope."   
******The action should fail and stop a playbook execution:**  
****_If fatal error, like wrong credentials, no connection to server, other:_ Print "Error executing action "Execute Entity Query". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** "Results"All of the columns from the response will be used as table columns. | General  
  
### Enrich Endpoint

#### Description

Fetch endpoint's system information by its hostname or IP address.

#### Run On

This action runs on the following entities:

  * IP Address
  * Host



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Entity Enrichment

For entity enrichment, every field from the response will be used. The prefix will be SLRW _ORION_

For example, SLRW_ORION_CPULoad is mapped from CPULoad

##### JSON Result
    
    
    {
        "results": [
            {
                "IpAddress": "172.30.203.130",
                "DisplayName": "orion",
                "NodeDescription": "Hardware: Intel64 Family 6 Model 63 Stepping 2 AT/AT COMPATIBLE - Software: Windows Version 10.0 (Build 17763 Multiprocessor Free)",
                "ObjectSubType": "Agent",
                "Description": "Windows 2019 Server",
                "SysName": "ORION",
                "Caption": "orion",
                "DNS": "orion",
                "Contact": "",
                "Status": 1,
                "StatusDescription": "Node status is Up.",
                "IOSImage": "",
                "IOSVersion": "10.0 (Build 17763 Multiprocessor Free)",
                "GroupStatus": "Up.gif                                  ",
                "LastBoot": "2020-10-26T11:06:00.0000000",
                "SystemUpTime": 76135.1171875,
                "AvgResponseTime": 4,
                "CPULoad": 0,
                "PercentMemoryUsed": 76,
                "MemoryAvailable": 3.08503347E+09,
                "Severity": 0,
                "Category": 2,
                "EntityType": "Orion.Nodes",
                "IsServer": true,
                "IsOrionServer": false
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If successful and at least one of the provided entities were enriched (is_success = true):_ Print "Successfully enriched the following endpoints from SolarWinds Orion: \n {0}".format(entity.identifier list)****_If fail to enrich specific entities(is_success = true):_ Print "Action was not able to enrich the following endpoints from SolarWinds Orion \n: {0}".format([entity.identifier])****_If fail to enrich for all entities (is_success = false):_ Print "No entities were enriched."  
******The action should fail and stop a playbook execution:**  
****_If fatal error, like wrong credentials, no connection to server, other:_ Print "Error executing action "Enrich Endpoint". Reason: {0}''.format(error.Stacktrace) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
