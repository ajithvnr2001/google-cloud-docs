---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/f5-big-ip-access-policy-manager/
title: F5 BIG-IP Access Policy Manager \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:12.967960+00:00
---

# F5 BIG-IP Access Policy Manager  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/f5-big-ip-access-policy-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# F5 BIG-IP Access Policy Manager

This document describes how to integrate F5 BIG-IP Access Policy Manager with Google Security Operations.

## Configure F5 BIG-IP Access Policy Manager integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
BIG-IP APM Address | String | https://{IP-Address} | Yes | API Root of the F5 BIG-IP Access Policy Manager instance.  
User Name | String |  | Yes | User Name of F5 BIG-IP Access Policy Manager.  
Password | Password |  | Yes | Password of the user  
Token Timeout (in Seconds) | String | 36000 | No | Specify the timeout in seconds you would like the generated tokens to be valid for. If you want the default F5 BIG-IP timeout to take place - please leave this field empty  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verify the SSL certificate for the connection to the F5 BIG-IP Access Policy Manager server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to F5 BIG-IP Access Policy Manager with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if successful:** "Successfully connected to the F5 BIG-IP Access Policy Manager server with the provided connection parameters!" **The action should fail and stop a playbook execution:**   
**if not successful:** "Failed to connect to the F5 BIG-IP Access Policy Manager! Error is {0}".format(exception.stacktrace) | General  
  
### List Active Sessions

#### Description

The action will list all the currently active sessions in the F5 BIG-IP Access Policy Manager.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Limit | String | N/A | No | Specify the maximum number of entries you would like to get in the action.  
  
#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
     0: {
       "sessionID" : "fee20d24",
              "nestedStats": {
                    "entries": {
                        "clientIp": {
                            "description": "10.0.150.45"
                        },
                        "logonUser": {
                            "description": "n/a"
                        }
                    }
                }
            }
        }
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**   
**if successful:** "Successfully listed active sessions." **If successful and no active sessions found on the F5 instance: (result=false)** "No active sessions found in F5 BIG Access Policy Manager." **The action should fail and stop a playbook execution:**   
**if not successful:** "Failed to perform action "List Active Sessions" {0}".format(exception.stacktrace) | General  
  
### Disconnect Sessions

#### Description

The action will disconnect the specified sessions from the F5 BIG-IP instance. Action can work using entities or using parameters, according to the "Use Case Entities" parameter's value. Supported entities are "Address" and "User Name".

**Note:** Filters will be used with an "OR" logic, so that every session that even one of the parameters, or entities, will be matched in - will be disconnected.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Use Case Entities | Checkbox | unchecked | No | Specify whether the action should disconnect sessions using "Address" and "Client IP" entities found in the case, or work on the provided parameters only. NOTE - once checked, action will ignore all other parameters in the action  
Session IDs | String | N/A | No | Specify specific session IDs you would like to disconnect, in a comma separated list.  
Logon User Names | String | N/A | No | Specify Logon User Names you would like to disconnect sessions for,in a comma separated list, so only sessions for these Logon User Names will be disconnected.  
Client IPs | String | N/A | No | Specify Client IPs you would like to disconnect the sessions for,in a comma separated list, so only sessions for these Client IPs will be disconnected.  
  
#### Action Results

##### Script Result

Script Result Name | Value Options  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** **If successfully disconnected session for Session IDs parameter:** "Successfully disconnected sessions for the following provided Session IDs: "+{successfulsession_ids} **If successfully disconnected session for Logon User name (or User name entity):** "Successfully disconnected sessions for the following Logon User names: "+{successful_logon_user_names} **If successfully disconnected session for Client IPs (or Address entity):** "Successfully disconnected sessions for the following Client IPs: "+{successfulclient_ips} **If Logon User name (or User name entity) was not found in active session:** "Couldn't find the following Logon User Names in any of the active sessions: "+{failed_logon_user_names} **If Client IP (or address entity) was not found in active session:** "Couldn't find the following Clients IP in any of the active sessions: "{failed_clientips} **If one of the Session IDs was not found in the active Sessions list:** "Couldn't find the following Session IDs in any of the active sessions: "{failed_session_IDs} **The action should fail and stop a playbook execution:** **If Use Case Entities = false, and none of the inputs (session ids, user logon names, client IPS) were not found in the active Sessions list:** "Could not find any of the provided inputs in the Active Sessions List, please check the inputs you have provided and try again" **If Use Case Entities = true, and no relevant entities were found in the active Sessions list (Addresses or User Names):** "Could not find any of the provided entities in the Active Sessions List, please check the inputs you have provided and try again" **In any other case of failure:** "Failed to perform action "Disconnect Sessions".format(exception.stacktrace) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
