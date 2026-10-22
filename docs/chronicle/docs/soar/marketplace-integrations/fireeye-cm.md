---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fireeye-cm/
title: FireEye CM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:22.999494+00:00
---

# FireEye CM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/fireeye-cm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# FireEye CM

**Important:** FireEye and McAfee Enterprise merged and became Trelix. FireEye CM was renamed to Trellix Central Management.

This document describes how to integrate FireEye CM with Google Security Operations.

## Use Cases

  1. Ingest Trellix Central Management alerts to use them to create Google Security Operations alerts. Next, in Google SecOps, alerts can be used to perform orchestrations with playbooks or manual analysis.
  2. Perform active actions - download alert artifacts using Trellix Central Management agent from Google SecOps, create a rule, IOC feeds



## Configure FireEye CM integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
API Root | String | https://: | Yes | API root of the Trellix Central Management server.  
Username | String | N/A | Yes | Username of the Trellix Central Management account.  
Password | Password | N/A | Yes | The password of the Trellix Central Management account.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Trellix Central Management server is valid.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to Trellix Central Management with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail or stop a playbook execution:**_if successful:_  
Print "Successfully connected to the Trellix Central Management server with the provided connection parameters!"  
**The action should fail and stop a playbook execution:**_if not successful:_ Print "Failed to connect to the Trellix Central Management server! Error is {0}".format(exception.stacktrace) | General  
  
### Add IOC Feed

#### Description

Add IOC feed in Trellix Central Management based on entities. Only MD5 and SHA256 hashes are supported.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Action | DDL | AlertPossible ValueAlertBlock | Yes | Specify what should be the action for the new feed.  
Comment | String | N/A | No | Specify additional comments for the feed.  
Extract Domain | Checkbox | N/A | Yes | If enabled, action will extract the domain part out of the URL and use it to create IOC feed.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * URL
  * HASH (MD5/SHA256)



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail or stop a playbook execution:**_if status code 200 for at least one entity type(is_success = true):_  
Print "Successfully added new IOC feeds to Trellix Central Management based on the following entities: \n".format(entity.identifier)  
_if some of the entity types were not used properly (is_success =true) :_  
Print "Action wasn't able to create new IOC feeds in Trellix Central Management based on the following entities:\n).format(entity.identifier)_iIf none of the entities were successfully used for feed creation: (is_success=false)_  
Print "No IOC feeds were created in Trellix Central Management!"**The action should fail and stop a playbook execution:**_if fatal error, like wrong credentials, no connection to server, other:_ Print "Error executing action "Add IOC Feed". Reason: {0}''.format(error.Stacktrace) | General  
  
### Delete IOC Feed

#### Description

Delete IOC feed in Trellix Central Management.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Feed Name | String | N/A | Yes | Specify the name of the feed that needs to be deleted.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if status code 200 and feedName was not found in the list (is_success = true):** "Successfully deleted feed '{0}' in Trellix Central Management !".  
******if status code 200 and feedName was found in the list for last request (is_success = false):** "Action wasn't able to delete feed '{0}' in Trellix Central Management.  
******If initially the feed name is not existing** "Action wasn't able to delete IOC feed in Trellix Central Management". Reason: Feed "{feed_name}" was not found.  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Delete IOC Feed". Reason: {0}''.format(error.Stacktrace) | General  
  
### List Quarantined Emails

#### Description

List quarantined emails. Requires FireEye EX connected to Trellix Central Management.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Start Time | String | N/A | No | If specified, only emails that were created after start time will be returned. If Start Time and End Time are not specified, action returns quarantined emails from the last 24 hours. Format: YYYY-MM-DD'T'HH:MM:SS.SSS-HHMM  
End Time | String | N/A | No | If specified, only emails that were created before end time will be returned. If Start Time and End Time are not specified, action returns quarantined emails from the last 24 hours. Format: YYYY-MM-DD'T'HH:MM:SS.SSS-HHMM  
Sender Filter | String | N/A | No | If specified, returns all of the quarantined emails only from this sender.  
Subject Filter | String | N/A | No | If specified, returns all of the quarantined emails only with this subject.  
Max Email to Return | String | 50 | No | Specify how many emails to return. Limit is 10000. This is Trellix Central Management limitation.  
**Note:** If End time is not specified, action returns quarantined emails from the specified Start time up to the execution moment.

##### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    [
        {
            "completed_at": "2020-06-09T08:21:17",
            "email_uuid": "x-x-x-x-x",
            "quarantine_path": "/data/email-analysis/quarantine2/2020-06-09/08/49h33n3HZczxNgc",
            "subject": "qwe",
            "message_id": "ec7d161d-c0f5-7e32-8f53-468393ccc9b6@fex2-lab.local",
            "from": "xxxx.xxxx2@xxxx-xxx.xxxx",
            "queue_id": "49h33n3HZczxNgc"
        },
        {
            "completed_at": "2020-06-09T08:21:42",
            "email_uuid": "58800022-51f7-4b07-b6b1-c5d88434283f",
            "quarantine_path": "/data/email-analysis/quarantine2/2020-06-09/08/49h34G5TVczxNgg",
            "subject": "rew",
            "message_id": "625607a6-a99d-004a-4ad6-69c3ec795168@fex2-lab.local",
            "from": "xxxx.xxxx2@xxxx-xxx.xxxx",
            "queue_id": "49h34G5TVczxNgg"
        }
    ]
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if data is available (is_success = true):** "Successfully listed Trellix Central Management quarantined emails!"  
******if no data is available (is_success = true):** "No quarantined emails were found in Trellix Central Management!"  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Quarantined Emails". Reason: {0}''.format(error.Stacktrace) | General  
Case wall table | **Name:** Quarantined Emails******Columns:**

  * Sender 
  * Subject 
  * Completed At 
  * Email UUID
  * Message ID 
  * Queue ID 

|   
  
### Release Quarantined Email

#### Description

Releases quarantined email. Requires FireEye EX connected to Trellix Central Management.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Queue ID | String | N/A | Yes | Specify the queue id of the email that needs to be released.  
Sensor Name | String | N/A | No | Specify the name of the sensor, where you want to release a quarantined email. If nothing is specified here, action will try to find the sensor automatically.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if status code 200 and response is empty (is_success = true):** "Successfully released Trellix Central Management quarantined email with queue id {0}!".  
******if status code 200 and response is not empty (is_success = false):** "Email with queue id {0} was not released. Reason: {1}".  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Release Quarantined Email". Reason: {0}''.format(error.Stacktrace)  
******If Sensor not found automatically:** "Error executing action "Release Quarantined Email". Reason: Sensor for FireEye EX appliance was not found. Please provide it manually in the 'Sensor Name' parameter.''.format(error.Stacktrace)  
******If Invalid sensor is provided:** "Error executing action "Release Quarantined Email". Reason: Sensor with name {0} for FireEye EX appliance was not found. Please check the spelling.''.format(error.Stacktrace) | General  
  
### Download Quarantined Email

#### Description

Download quarantined email. Requires FireEye EX connected to Trellix Central Management.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Queue ID | String | N/A | Yes | Specify the queue id of the email that needs to be downloaded.  
Download Folder Path | String | N/A | Yes | Specify the absolute path to the folder where the action should save the files.  
Overwrite | Checkbox | Yes | Yes | If enabled, action will overwrite the existing file with the same path.  
Sensor Name | String | N/A | No | Specify the name of the sensor, where you want to download a quarantined email. If nothing is specified here, action will try to find the sensor automatically.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    file_path = {absolute file path to the file}
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if status code 200 and no xml (is_success = true):** "Successfully downloaded Trellix Central Management quarantined email with queue id {0}!".  
******if status code 200 and xml in the response (is_success = false):** "Email with queue id {0} was not downloaded. Reason: {1}".  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Download Quarantined Email". Reason: {0}''.format(error.Stacktrace)  
******If Sensor not found automatically:** "Error executing action "Download Quarantined Email". Reason: Sensor for FireEye EX appliance was not found. Please provide it manually in the 'Sensor Name' parameter.''.format(error.Stacktrace)  
******If Invalid sensor is provided:** "Error executing action "Download Quarantined Email". Reason: Sensor with name {0} for FireEye EX appliance was not found. Please check the spelling.''.format(error.Stacktrace) | General  
  
### Delete Quarantined Email

#### Description

Delete quarantined email. Requires FireEye EX connected to Trellix Central Management.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Queue ID | String | N/A | Yes | Specify the queue id of the email that needs to be deleted.  
Sensor Name | String | N/A | No | Specify the name of the sensor, where you want to delete a quarantined email. If nothing is specified here, action will try to find the sensor automatically.  
  
#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if status code 200 and response is empty (is_success = true):** "Successfully deleted Trellix Central Management quarantined email with queue id {0}!".  
****  
**The action should fail and stop a playbook execution:****if status code 200 and response is not empty:** "Email with queue id {0} was not deleted. Reason: {1}".  
******if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Delete Quarantined Email". Reason: {0}''.format(error.Stacktrace)******If Sensor not found automatically:** "Error executing action "Delete Quarantined Email". Reason: Sensor for FireEye EX appliance was not found. Please provide it manually in the 'Sensor Name' parameter.''.format(error.Stacktrace)  
******If Invalid sensor is provided:** "Error executing action "Delete Quarantined Email". Reason: Sensor with name {0} for FireEye EX appliance was not found. Please check the spelling.''.format(error.Stacktrace) | General  
  
### Download Alert Artifacts

#### Description

Download alert artifacts from Trellix Central Management.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Alert UUID | String | N/A | Yes | Specify the alert uuid from where we need to download artifacts.  
Download Folder Path | String | N/A | Yes | Specify the absolute path to the folder where the action should save the files.  
Overwrite | Checkbox | Checked | Yes | If enabled, action will overwrite the existing file with the same path.  
  
#### Run On

The action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    file_path = {absolute file path to the file}
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if status code 200 (is_success = true):** "Successfully downloaded Trellix Central Management alert artifacts with alert id {0}!".******If file with that path already exists (is_success = false):** "Action wasn't able to download Trellix Central Management alert artifacts with alert id {0}. Reason: File with that path already exists."  
******if status code 404 (is_success = false):** "Artifacts for alert with uuid {0} were not found. ".  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Download Alert Artifacts". Reason: {0}''.format(error.Stacktrace) | General  
  
### List IOC Feeds

#### Description

List available IOC feeds in Trellix Central Management.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Max IOC Feeds To Return | String | 50 | No | Specify how many IOC feeds to return. Default is 50.  
  
#### Run On

The action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "customFeedInfo": [
            {
                "feedName": "ad",
                "status": "Feed processed",
                "feedType": "url",
                "uploadDate": "2020/10/13 10:32:28",
                "feedAction": "alert",
                "feedSource": "",
                "contentMeta": [
                    {
                        "contentType": "ip",
                        "feedCount": 0
                    },
                    {
                        "contentType": "domain",
                        "feedCount": 0
                    },
                    {
                        "contentType": "url",
                        "feedCount": 3
                    },
                    {
                        "contentType": "hash",
                        "feedCount": 0
                    }
                ]
            },
            {
                "feedName": "adasdasdas",
                "status": "Feed processed",
                "feedType": "domain",
                "uploadDate": "2020/10/13 10:34:29",
                "feedAction": "alert",
                "feedSource": "",
                "contentMeta": [
                    {
                        "contentType": "ip",
                        "feedCount": 0
                    },
                    {
                        "contentType": "domain",
                        "feedCount": 3
                    },
                    {
                        "contentType": "url",
                        "feedCount": 0
                    },
                    {
                        "contentType": "hash",
                        "feedCount": 0
                    }
                ]
            },
            {
                "feedName": "qweqwe",
                "status": "Feed processed",
                "feedType": "ip",
                "uploadDate": "2020/10/13 10:16:31",
                "feedAction": "alert",
                "feedSource": "",
                "contentMeta": [
                    {
                        "contentType": "ip",
                        "feedCount": 3
                    },
                    {
                        "contentType": "domain",
                        "feedCount": 0
                    },
                    {
                        "contentType": "url",
                        "feedCount": 0
                    },
                    {
                        "contentType": "hash",
                        "feedCount": 0
                    }
                ]
            }
        ]
    }
    

##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if status code 200 (is_success = true):** "Successfully listed available IOC feeds in Trellix Central Management!".  
******If no entries were found:** "No IOC feeds were found in Trellix Central Management"  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List IOC Feeds". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall table | **Table Name:** Available IOC Feeds******Table Columns:** Name Status Type Action Comment IP Count URL Count Domain Count Hash Count Uploaded At  | General  
  
### Add Rule To Custom Rules File

#### Description

Add new rule to custom rule file in Trellix Central Management.

**Note:** The custom rules file should exist already.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Rule | String | N/A | Yes | Specify the rule that needs to be added to the custom rules file.  
Sensor Name | String | N/A | No | Specify the name of the sensor, where you want to add a new rule. If nothing is specified here, action will try to find the sensor automatically.  
  
#### Run On

The action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if status code 200 and file was updated (is_success = true):** "Successfully added rule to custom rules file in '{0}' appliance in Trellix Central Management !".  
****  
**if status code 500 (is_success = false):** "Action wasn't able to add a rule to the custom rules file in Trellix Central Management. Reason: {0}).  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Add Rule To Custom Rules". Reason: {0}''.format(error.Stacktrace)  
******If Sensor not found automatically:** "Error executing action "Add Rule To Custom Rules File". Reason: Sensor for FireEye NX appliance was not found. Please provide it manually in the 'Sensor Name' parameter.''.format(error.Stacktrace)  
******If Invalid sensor is provided:** "Error executing action "Add Rule To Custom Rules File". Reason: Sensor with name {0} for FireEye NX appliance was not found. Please check the spelling.''.format(error.Stacktrace)  
| General  
  
### Acknowledge Alert

#### Description

Acknowledge alert in Trellix Central Management.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Alert UUID | String | N/A | Yes | Specify the alert uuid, which needs to be acknowledged.  
Annotation | String | N/A | Yes | Specify the annotation that explains the reason for acknowledgment.  
  
#### Run On

The action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if status code 200 (is_success = true):** "Successfully acknowledged Trellix Central Management alert with ID {0}!".  
******if status code 404 (is_success = false):** "Action wasn't able to acknowledge Trellix Central Management alert with ID {0}. Reason: Alert with ID {0} wasn't found. ".  
******If status code 400 (is_success = false):** "Action wasn't able to acknowledge Trellix Central Management alert with ID {0}. Reason: {1} ".  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Acknowledge Alert". Reason: {0}''.format(error.Stacktrace) | General  
  
### Download Custom Rules File

#### Description

Download custom rules file from Trellix Central Management.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Sensor Name | String | N/A | No | Specify the name of the sensor, where you want to add a new rule. If nothing is specified here, action will try to find the sensor automatically.  
Download Folder Path | String | N/A | Yes | Specify the absolute path to the folder, where the file should be downloaded to.  
Overwrite | Checkbox | Checked | Yes | If enabled, action will overwrite the existing file with the same path.  
  
#### Run On

The action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    File Path = "absolute path to the file"
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if status code 200 (is_success = true):** "Successfully downloaded custom rules file from appliance '{0}' in Trellix Central Management !".  
******If status code 500 or 400 (is_success = false):** "Action wasn't able to download custom rules file from appliance '{0}' in Trellix Central Management. Reason: {1}".  
****  
**The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Download Custom Rules File". Reason: {0}''.format(error.Stacktrace)  
******If Sensor not found automatically:** "Error executing action "Download Custom Rules File". Reason: Sensor for FireEye NX appliance was not found. Please provide it manually in the 'Sensor Name' parameter.''.format(error.Stacktrace)  
******If Invalid sensor is provided:** "Error executing action "Download Custom Rules File". Reason: Sensor with name {0} for FireEye NX appliance was not found. Please check the spelling.''.format(error.Stacktrace) | General  
  
## Connectors

## FireEye CM - Alerts Connector

#### Description

Connector ingests Trellix Central Management alerts into Google SecOps. This includes alerts generated by FireEye NX and EX appliances.

#### Configure FireEye CM - Alerts Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | sensor | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | eventType | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name  
| String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern  
| String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged.Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https://x.x.x.x:x | Yes | API root of Trellix Central Management server.  
Username | String | N/A | Yes | Username of the Trellix Central Management account.  
Password | Password | N/A | Yes | Password of the Trellix Central Management account.  
Fetch Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch alerts.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Trellix Central Management server is valid.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist will be used as a blacklist.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
