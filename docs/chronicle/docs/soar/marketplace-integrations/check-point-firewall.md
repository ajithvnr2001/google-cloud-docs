---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/check-point-firewall/
title: Check Point Firewall \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:48:47.865767+00:00
---

# Check Point Firewall  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/check-point-firewall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Check Point Firewall

This document describes how to integrate Check Point Firewall with Google Security Operations.

## Configure Check Point Firewall integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
Server Address | String | xx.xx.xx.xx:443 | Yes | The IP address of the Check Point Firewall server.  
Username | String | N/A | Yes | The email address of the user which should be used to connect to the Check Point Firewall.  
Domain | String | N/A | No | The domain of the user. E.g. if the email address of the user is `user@example.com`, the domain will be `example.com`  
Password | Password | N/A | Yes | The password of the according user.  
Policy Name | String | standard | Yes | Name of the policy.  
Verify SSL | Checkbox | Unchecked | No | Use this checkbox, if your Check Point Firewall connection requires an SSL verification.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Add a SAM Rule

#### Description

Add a SAM (suspicious activity monitoring) rule for Check Point Firewall. Please refer to the [Check Point fw_sam command criteria](https://sc1.checkpoint.com/documents/R81/WebAdminGuides/EN/CP_R81_CLI_ReferenceGuide/Topics-CLIG/MDSG/fw-sam.htm) section documentation for available IP, netmask, port, and protocol combinations.

**Warning:** Please note that this action publishes the changes.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Security Gateway to Create SAM Rule on | String | N/A | Yes | Specify the name of Security Gateway to create a rule for.  
  
Source IP | String | N/A | No | Specify the source IP to be added to the rule.  
Source Netmask | String | N/A | No | Specify the source netmask to be added to the rule.  
Destination IP | String | N/A | No | Specify the destination IP to be added to the rule.  
Destination Netmask | String | N/A | No | Specify the destination netmask to be added to the rule.  
Port | Integer | N/A | No | Specify the port number to be added to the rule, for example, 5005.  
Protocol | String | N/A | No | Specify the protocol name to be added to the rule, for example, TCP.  
Expiration | Seconds | N/A | No | Specify for how long in seconds the newly added SAM rule should be active, for example, 4. If nothing is specified - then the rule never expires.  
Action for the Matching Connections | DDL | Drop | Yes | Specify the action that should be executed for the matching connections.  
How to Track Matching Connections | DDL | Log | Yes | Specify how to track matching connections.  
Close Connections | Checkbox | Checked | No | Specify if the existing matching connections should be closed.  
  
#### Run On

The action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "tasks": [
            {
                "uid": "8163c4f0-a269-4628-9bb3-0ba597e9694c",
                "name": "gaia80.10 - CW Test fw sam",
                "type": "CdmTaskNotification",
                "domain": {
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                    "domain-type": "domain"
                },
                "task-id": "4ca124e5-c9ce-45cf-8275-4b119e535d3e",
                "task-name": "gaia80.10 - CW Test fw sam",
                "status": "succeeded",
                "progress-percentage": 100,
                "start-time": {
                    "posix": 1594959450832,
                    "iso-8601": "2020-07-17T07:17+0300"
                },
                "last-update-time": {
                    "posix": 1594959453264,
                    "iso-8601": "2020-07-17T07:17+0300"
                },
                "suppressed": false,
                "task-details": [
                    {
                        "uid": "94108666-b9d6-4165-80ab-13078c03395b",
                        "name": null,
                        "domain": {
                            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                            "name": "SMC User",
                            "domain-type": "domain"
                        },
                        "color": "black",
                        "statusCode": "succeeded",
                        "statusDescription": "sam: request for 'Inhibit Drop Close src ip 8.9.10.11 on All' acknowledged, sam: gaia80.10 (0/1) successfully completed 'Inhibit Drop Close src ip 8.9.10.11 on All' processing, ...",
                        "taskNotification": "8163c4f0-a269-4628-9bb3-0ba597e9694c",
                        "gatewayId": "8f36a0de-e0d5-6347-ae51-6fb22d573f04",
                        "gatewayName": "",
                        "transactionId": 552194328,
                        "responseMessage": "",
                        "responseError": "c2FtOiByZXF1ZXN0IGZvciAnSW5oaWJpdCBEcm9wIENsb3NlIHNyYyBpcCA4LjkuMTAuMTEgb24gQWxsJyBhY2tub3dsZWRnZWQKc2FtOiBnYWlhODAuMTAgKDAvMSkgc3VjY2Vzc2Z1bGx5IGNvbXBsZXRlZCAnSW5oaWJpdCBEcm9wIENsb3NlIHNyYyBpcCA4LjkuMTAuMTEgb24gQWxsJyBwcm9jZXNzaW5nCnNhbTogcmVxdWVzdCBmb3IgJ0luaGliaXQgRHJvcCBDbG9zZSBzcmMgaXAgOC45LjEwLjExIG9uIEFsbCcgZG9uZQo=",
                        "meta-info": {
                            "validation-state": "ok",
                            "last-modify-time": {
                                "posix": 1594959453332,
                                "iso-8601": "2020-07-17T07:17+0300"
                            },
                            "last-modifier": "admin",
                            "creation-time": {
                                "posix": 1594959451003,
                                "iso-8601": "2020-07-17T07:17+0300"
                            },
                            "creator": "admin"
                        },
                        "tags": [],
                        "icon": "General/globalsNa",
                        "comments": "",
                        "display-name": "",
                        "customFields": null
                    }
                ],
                "comments": "Completed",
                "color": "black",
                "icon": "General/globalsNa",
                "tags": [],
                "meta-info": {
                    "lock": "unlocked",
                    "validation-state": "ok",
                    "last-modify-time": {
                        "posix": 1594959453299,
                        "iso-8601": "2020-07-17T07:17+0300"
                    },
                    "last-modifier": "admin",
                    "creation-time": {
                        "posix": 1594959450933,
                        "iso-8601": "2020-07-17T07:17+0300"
                    },
                    "creator": "admin"
                },
                "read-only": false
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * if successful: print "Successfully added SAM rule with the following command: {0}".format(script_text_from_run-script). If show-task return base64 encoded status message in responseError (or responseMessage) param - add it fo the response too: "fw sam command output: {0}".format(responseError.text)
  * If show-task returns "partially succeeded" status: "SAM rule addition with the following fw sam command partially succeededsucceded: {0}".format(script_text_from_run-script). If show-task return base64 encoded status message in responseError (or responseMessage) param - add it fo the response too: "fw sam command output: {0}".format(responseError.text)
  * If fail to add SAM rule, show-task returns failed: print "Failed to add SAM rule with the following command: {0}".format(script_text_from_run-script). If show-task return base64 encoded status message in responseError (or responseMessage) param - add it fo the response too: "fw sam command output: {0}".format(responseError.text)
  * If Google SecOps action hit timeout waiting for show-task response or waiting for status to change from "in progress": print "Timeout waiting for addition of the following SAM rule: {0}".format(script_text_from_run-script).

******The action should fail and stop a playbook execution:**

  * If fatal error, like wrong credentials, no connection to server, other: print "Failed to execute Add SAM Rule action! Error is {0}".format(exception.stacktrace)

| General  
  
### Remove SAM Rule

#### Description

Remove a SAM (suspicious activity monitoring) rule from Check Point Firewall.

**Note:** You need to match the current rule in order to remove it. Please refer to the [Check Point fw_sam command criteria](https://sc1.checkpoint.com/documents/R81/WebAdminGuides/EN/CP_R81_CLI_ReferenceGuide/Topics-CLIG/MDSG/fw-sam.htm) section documentation for available ip, netmask, port and protocol combinations.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Security Gateway | String | N/A | Yes | Specify the name of Security Gateway from where to remove SAM Rule.  
Source IP | String | N/A | No | Specify the source IP to be added to the rule.  
Source Netmask | String | N/A | No | Specify the source netmask to be added to the rule.  
Destination IP | String | N/A | No | Specify the destination IP to be added to the rule.  
Destination Netmask | String | N/A | No | Specify the destination netmask to be added to the rule.  
Port | Integer | N/A | No | Specify the port number to be added to the rule, for example, 5005.  
Protocol | String | N/A | No | Specify the protocol name to be added to the rule, for example, TCP.  
Action for the Matching Connections | DDL | DropPossible Values:DropRejectNotify | Yes | Specify the action that should be executed for the matching connections.  
How to Track Matching Connections | DDL | LogPossible Values:No LogLogAlert | Yes | Specify how to track matching connections.  
Close Connections | Checkbox | Checked | No | Specify if the existing matching connections should be closed.  
  
#### Run On

The action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "tasks": [
            {
                "uid": "6966d094-c7d9-4e46-a824-d4948be71b3e",
                "name": "gaia80.10 - Siemplify-generated-script",
                "type": "CdmTaskNotification",
                "domain": {
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User",
                    "domain-type": "domain"
                },
                "task-id": "77318892-48aa-4a38-ad94-b9322695c2c8",
                "task-name": "gaia80.10 - Siemplify-generated-script",
                "status": "succeeded",
                "progress-percentage": 100,
                "start-time": {
                    "posix": 1608120786139,
                    "iso-8601": "2020-12-16T14:13+0200"
                },
                "last-update-time": {
                    "posix": 1608120788465,
                    "iso-8601": "2020-12-16T14:13+0200"
                },
                "suppressed": false,
                "task-details": [
                    {
                        "uid": "c40132ac-547f-4fbf-b4bb-5c7efb7ed76b",
                        "name": null,
                        "domain": {
                            "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                            "name": "SMC User",
                            "domain-type": "domain"
                        },
                        "color": "black",
                        "statusCode": "succeeded",
                        "statusDescription": "",
                        "taskNotification": "6966d094-c7d9-4e46-a824-d4948be71b3e",
                        "gatewayId": "8f36a0de-e0d5-6347-ae51-6fb22d573f04",
                        "gatewayName": "",
                        "transactionId": 194990168,
                        "responseMessage": "",
                        "responseError": "",
                        "meta-info": {
                            "validation-state": "ok",
                            "last-modify-time": {
                                "posix": 1608120788509,
                                "iso-8601": "2020-12-16T14:13+0200"
                            },
                            "last-modifier": "admin",
                            "creation-time": {
                                "posix": 1608120786199,
                                "iso-8601": "2020-12-16T14:13+0200"
                            },
                            "creator": "admin"
                        },
                        "tags": [],
                        "icon": "General/globalsNa",
                        "comments": "",
                        "display-name": "",
                        "customFields": null
                    }
                ],
                "comments": "Completed",
                "color": "black",
                "icon": "General/globalsNa",
                "tags": [],
                "meta-info": {
                    "lock": "unlocked",
                    "validation-state": "ok",
                    "last-modify-time": {
                        "posix": 1608120788491,
                        "iso-8601": "2020-12-16T14:13+0200"
                    },
                    "last-modifier": "admin",
                    "creation-time": {
                        "posix": 1608120786184,
                        "iso-8601": "2020-12-16T14:13+0200"
                    },
                    "creator": "admin"
                },
                "read-only": false
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:****If status="succeeded" (is_success = true):** "Successfully removed SAM rule from the Check Point Firewall using the command: {0}".format(command)******If status code != 200,401 in the first response(is_success=false):** "Action wasn't able to remove the SAM rule using the command "{0}" in Check Point FireWall. Reason: {1}".format(command,message)******If in the second response statusCode == failed and base64 responseError is not available (is_success=false):** "Action wasn't able to remove the SAM rule using the command "{0}" in Check Point FireWall."******If in the second response statusCode == failed and base64 responseError is available (is_success=false):** "Action wasn't able to remove the SAM rule using the command "{0}" in Check Point FireWall. Reason: {1}".format(command, base64 decoded responseError)******If timeout(is_success=false):** "Action reached timeout, while waiting to remove SAM Rule. Command used: {0}".format(command)******Async message:** Waiting for a task to remove the SAM rule to finish.  
******The action should fail and stop a playbook execution:****if fatal error, SDK error, like wrong credentials, no connection to server, other:** "Error executing action "Update Alert Status". Reason: {0}''.format(error.Stacktrace) | General  
  
### Add IP to Group

#### Description

Updates the Google SecOps Blacklist group with new IP addresses.

#### Parameters

Parameters | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Blacklist Group Name | String | N/A | Yes | Name of the group.  
  
#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_blocked | True/False | is_blocked:False  
  
### Add URL to Group

#### Description

Updates the group with the URL.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
URLs Group Name | String | N/A | Yes | Name of the group.  
  
#### Run On

This action runs on the URL entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_blocked | True/False | is_blocked:False  
  
### List Layers on Site

#### Description

Retrieve all existing layers.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### List Policies on Site

#### Description

Retrieve all existing policies.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### Ping

#### Description

Test Connectivity.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### Remove IP From Group

#### Description

Updates the Google SecOps Blacklist group to NOT include the IP addresses.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Blacklist Group Name | String | N/A | Yes | Name of the group to remove the address range object from.  
  
#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_unblocked | True/False | is_unblocked:False  
  
### Remove URL From Group

#### Description

Updates the group to NOT include the URL.

#### Parameters

Parameter | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
URLs Group Name | String | N/A | Yes | Name of the group to remove the URL object from.  
  
#### Run On

This action runs on the URL entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_unblocked | True/False | is_unblocked:False  
  
### Run Script

#### Description

Run the arbitrary script with Check Point run-script API call.

**Note:** This action doesn't use Google SecOps entities to operate.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Script text | String | N/A | Yes | Script to execute. For example, fw sam command: fw sam -t 600 -I src 8.9.10.12  
Target | String | N/A | Yes | Specify Check Point device to execute the script on, for example, gaia80.10 The parameter accepts multiple values as a comma-separated list.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "tasks": [{
            "task-id": "867fef24-647e-40ea-91ef-9b5f8ae83d07",
            "status": "succeeded",
            "domain": {
                "domain-type": "domain",
                "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                "name": "SMC User"
            },
            "start-time": {
                "posix": 1597737649683,
                "iso-8601": "2020-08-18T11:00+0300"
            },
            "uid": "bb5c4640-9774-45cd-8631-8e80518f4e18",
            "tags": [],
            "last-update-time": {
                "posix": 1597737651783,
                "iso-8601": "2020-08-18T11:00+0300"
            },
            "suppressed": false,
            "progress-percentage": 100,
            "comments": "Completed",
            "task-name": "gaia80.10 - Siemplify-generated-script",
            "color": "black",
            "meta-info": {
                "creation-time": {
                    "posix": 1597737649720,
                    "iso-8601": "2020-08-18T11:00+0300"
                },
                "validation-state": "ok",
                "creator": "admin",
                "lock": "unlocked",
                "last-modifier": "admin",
                "last-modify-time": {
                    "posix": 1597737651810,
                    "iso-8601": "2020-08-18T11:00+0300"
                }},
            "task-details": [{
                "display-name": "",
                "domain": {
                    "domain-type": "domain",
                    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
                    "name": "SMC User"
                }, "gatewayName": "",
                "uid": "b4a71da3-60fc-4785-a379-3bb9f7a0ff2f",
                "icon": "General/globalsNa",
                "tags": [],
                "color": "black",
                "comments": "",
                "name": null,
                "responseError": "",
                "taskNotification": "bb5c4640-9774-45cd-8631-8e80518f4e18",
                "responseMessage": "",
                "gatewayId": "8f36a0de-e0d5-6347-ae51-6fb22d573f04",
                "transactionId": 931053033,
                "meta-info": {
                    "creation-time": {
                        "posix": 1597737649735,
                        "iso-8601": "2020-08-18T11:00+0300"
                    },
                    "last-modify-time": {
                        "posix": 1597737651840,
                        "iso-8601": "2020-08-18T11:00+0300"
                    },
                    "creator": "admin",
                    "validation-state": "ok",
                    "last-modifier": "admin"
                },
                "customFields": null,
                "statusDescription": "",
                "statusCode": "succeeded"
            }],
            "icon": "General/globalsNa",
            "type": "CdmTaskNotification",
            "read-only": false,
            "name": "gaia80.10 - Siemplify-generated-script"
        }]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * If successful run: print "Script executed successfully."   
If show-task return base64 encoded status message in responseError (or responseMessage) param - add it fo the response too: "Script output: {0}".format(responseError.text)
  * If script returns other status rather than succeeded: print "Failed to execute provided script"   
If show-task return base64 encoded status message in responseError (or responseMessage) param - add it fo the response too: "Script output: {0}".format(responseError.text)"

******The action should fail and stop a playbook execution:**

  * _If fatal error, like wrong credentials, no connection to server, other_ : print "Failed to execute action! Error is {0}".format(exception.stacktrace)

| General  
  
### Show Logs

#### Description

Retrieve logs from Check Point FireWall based on the filter.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Query Filter | String | N/A | No | Specify the query filter that will be used to return logs.  
Time Frame | DDL | Last Hour Possible Values: Today Yesterday Last Hour Last 24 Hours Last 30 Days This Week This Month All Time | Yes | Specify what time frame should be used for log retrieval.  
Log Type | DDL | Log Possible Values: Log Audit | Yes | Specify what type of logs should be returned.  
Max Logs To Return | Integer | 50 | No | Specify how many logs to return. Maximum is 100. This is Check Point FireWall limitation.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "logs": [
            {
                "subject": "Object Manipulation",
                "confidence_level": "N/A",
                "description": "Engine mode: changed from 'by_policy' to 'detect_only' ",
                "type": "System Alert",
                "orig_log_server_attr": [
                    {
                        "isCHKPObject": "true",
                        "uuid": "8f36a0de-e0d5-6347-ae51-6fb22d573f04",
                        "resolved": "gaia80.10"
                    }
                ],
                "cb_log_type": "Security Alert",
                "user_field": "admin",
                "administrator": "admin",
                "index_time": "2020-10-14T21:35:45Z",
                "d_name": "Check that each Gateway's Anti-Bot configuration is activated according to the policy",
                "violation_date": "3/6/2020 15:03",
                "id": "ac1eca60-81b3-d219-5f87-6f2f000105e8",
                "rounded_received_bytes": "0",
                "cb_title": "Best Practice AB104 status decreased. New Status: Medium",
                "cb_old_status": "Secure",
                "lastUpdateSeqNum": "1513",
                "severity": "Critical",
                "product_family": "Network",
                "product": "Compliance Blade",
                "sequencenum": "1513",
                "rounded_sent_bytes": "0",
                "cb_scan_id": "Thu Oct 15 00:35:39 2020",
                "orig_log_server": "172.30.202.96",
                "cb_changed_objects": "ABSettings_8F36A0DE-E0D5-6347-AE51-6FB22D573F04",
                "additional_info": "Security Alert: Best Practice status was reduced",
                "cb_status": "Medium",
                "orig": "gaia80.10",
                "marker": "@A@@B@1602709200@C@1513",
                "rounded_bytes": "0",
                "orig_log_server_ip": "172.30.202.96",
                "stored": "true",
                "calc_desc": "Best Practice AB104 status decreased. New Status: Medium",
                "logid": "134283267",
                "time": "2020-10-14T21:35:43Z",
                "cb_recommendation": "Each Gateway should be configured to work according to the profiles defined in the Anti-Bot policy. The Activation Mode should be set to 'According to Policy' and not 'Detect Only'.",
                "best_practice_id": "AB104",
                "lastUpdateTime": "1602711343000"
            }
        ],
        "logs-count": 1,
        "query-id": "admin_6e9fce3a-4cd7-48b9-a3e7-14b701fb204c"
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If status code 200 (is_success = true):_ Print "Successfully retrieved logs from Check Point FireWall!"  
_If status code 400 (is_success =false):_ Print "Action wasn't able to retrieve logs from Check Point FireWall! Reason: {0}. Code: {1}".format(message, code)******The action should fail and stop a playbook execution:**_If fatal error, like wrong credentials, no connection to server, other_ : Print "Error executing action "Show Logs". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table Log type = Log | **Case Wall Name:** Results **Case Wall Columns:** ID (mapped as id) Title (mapped as cb_title) Severity (mapped as severity) Subject (mapped as subject) Index Time (mapped as index_time) | General  
Case Wall Table Log type = Audit | **Case Wall Name:** Results **Case Wall Columns:** ID (mapped as id)Title (mapped as calc_desc) Severity (mapped as severity) Subject (mapped as subject) Time (mapped as time) | General  
  
### Download Log Attachment

#### Description

Download log attachments from Check Point FireWall.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Log IDs | String | N/A | Yes | Specify the comma-separated list of log IDs from which you want to download attachments.  
Download Folder Path | String | N/A | Yes | Specify the absolute path for the folder where the action should store the attachments.  
Create Case Wall Attachment | Checkbox | N/A | No | If enabled, action will create a case wall attachment for each successfully downloaded file. Note: that attachment will only be created if it"s size is less than 3 MB.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "tasks": [
            {
                "task-id": "01234567-89ab-cdef-8273-cee81a82701c",
                "task-name": "Packet Capture operation",
                "status": "succeeded",
                "progress-percentage": 100,
                "suppressed": false,
                "task-details": [
                    {
                        "attachments": [
                            {
                                "base64-data": "...",
                                "file-name": "Anti-Virus-blob-time1602759307.id5a5b7500.blade05.cap"
                            }
                        ]
                    }
                ]
    "absolute_path": "{folder_path}"
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If "status" == "succeeded" for at least one log (is_success = true):_ Print "Successfully retrieved attachments in Check Point FireWall from the following logs:{0}".format(log ids)  
_If "status" != "succeeded" for at least one log (is_success = true):_ Print "Action wasn't able to retrieve attachments in Check Point FireWall from the following logs:{0}".format(log ids)****_If "status" != "succeeded" for all logs (is_success = true):_ Print "No attachments were downloaded"******The action should fail and stop a playbook execution:**_if fatal error, like wrong credentials, no connection to server, other:_ Print "Error executing action "Download Log Attachment". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Attachment | If it"s not reaching the size limit. For each successful attachment download. "{0}".format(task-details/attachment/file-name) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
