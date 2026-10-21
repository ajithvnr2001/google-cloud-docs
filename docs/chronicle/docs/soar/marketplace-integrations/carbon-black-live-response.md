---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/carbon-black-live-response/
title: VMware Carbon Black Endpoint Standard Live Response \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:10.312473+00:00
---

# VMware Carbon Black Endpoint Standard Live Response  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/carbon-black-live-response/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# VMware Carbon Black Endpoint Standard Live Response

This document describes how to integrate Carbon Black Endpoint Standard Live Response with Google Security Operations.

## Use Case

Perform real-time investigation and remediation on the hosts that have CB Endpoint Standard agent running.

## Configure VMware Carbon Black Endpoint Standard Live Response to work with Google Security Operations

### Product Permission

The Carbon Black Live Response feature is authenticated via API Key. Users can view API Key settings within the Carbon Black Cloud Console under Settings > API Keys.

### Service Hostnames

There are two Carbon Black Cloud hostnames:

  * `https://defense-<environment>.conferdeploy.net`
  * `https://api-<environment>.conferdeploy.net`



In addition, we have multiple environments such as (not a complete list):

  * prod02
  * prod04
  * prod05



For Carbon Black Live Response API, the following hostnames will be used: `https://defense-about:blank)<environment>.conferdeploy.net`

### API Keys

API keys include two parts:

  * API Secret Key (previously API Key).
  * API ID (previously Connector ID).



Authentication is passed to the API via the X-Auth-Token HTTP header.

  1. To generate the appropriate header, concatenate the API Secret Key with the API ID with a forward slash in between.
  2. For example, if the API Secret Key is ABCD and the API ID is 1234, the corresponding X-Auth-Token HTTP header will be: X-Auth-Token: ABCD/1234



All API requests must be authenticated by using an API Secret Key and an API ID. Unauthenticated requests return an HTTP 401 error.

### How to obtain an API Secret Key and API ID

  1. Log into your Carbon Black Cloud Organization.
  2. Navigate to Settings > API Keys.
  3. Click "Add API Key".
  4. Select Access Level = Live Response, configure other parameters.
  5. Obtain your API Secret Key and API ID pair.



### Network

Function | Default Port | Direction | Protocol  
---|---|---|---  
API | Multivalues | Outbound | apikey  
  
## Product Permission for CB Live Response v6 API version

**Concepts required to access Carbon Black Cloud APIs:**

  1. Service Hostname
  2. API Keys
  3. RBAC
  4. Organization Keys



**Service Hostnames:**

For CarbonBlack Live Response API the following hostnames will be used: `https://defense-<environment>.conferdeploy.net`

**API Keys**

Carbon Black Cloud APIs and Services are authenticated via API Keys. Users can view API Key settings within the Carbon Black Cloud Console under Settings > API Keys.

**API keys include two parts:**

  * API Secret Key (previously API Key).
  * API ID (previously Connector ID).



**How to obtain an API Secret Key and API ID**

  1. Log into your Carbon Black Cloud Organization.
  2. Navigate to Settings > API Keys.
  3. Click "Add API Key".
  4. Configure Name, Access Level, etc.
  5. Obtain your API Secret Key and API ID pair.



This allows an organization administrator to define an API Key and get access to the API Secret Key and API ID that will be required to authenticate the API request. In addition, administrators can restrict use of this API key to a specific set of IP addresses for security reasons.

**Organization Keys**

In addition to API Keys, many Carbon Black Cloud APIs or Services require an org_key in the API request path. This is to support customers that manage multiple orgs. You can find your org_key in the Carbon Black Cloud Console under Settings > API Keys.

**Configure API Access for CB Live Response Google SecOps integration**

To configure API Access for CB Live Response Google SecOps integration the following steps needs to be taken:

  1. Login Carbon Black Cloud Console, go to **Settings > API Access.**
  2. On the API Access page, go to **Access Levels**.
  3. On Access Levels page, click **\+ Add Access Level**.
  4. In the opened window, provide a name and description for the new Access Level and select permissions like on the screenshot below:

![List of required
permissions](https://docs.cloud.google.com/static/chronicle/images/integrations/vmware-carbon-black-endpoint-standard-live-response-permissions.png)

  5. Go back to API Access tab.

  6. Click **\+ Add API Key** to create a new API key.

  7. In the opened tab fill mandatory field and select the Access Level you configured on step 4:

![Edit API key
settings](https://docs.cloud.google.com/static/chronicle/images/integrations/vmware-carbon-black-endpoint-standard-live-response-api-key.png)

  8. Once you will click Save, you will be shown API ID and API Secret Key. Please save those values, you will need them to configure the integration.

  9. Once the API ID and API Secret key are saved, the API Access for CB Live Response v6 API is done.




## Configure VMware Carbon Black Endpoint Standard Live Response integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
API Root | String | https://defense-{environment}.conferdeploy.net | Yes | Endpoint Standard Live Response API Root URL.  
Organization Key | String | N/A | Yes | Vmware Carbon Black Cloud Organization Key.  
Carbon Black Cloud API ID | String | N/A | Yes | Vmware Carbon Black Cloud API ID (Custom API Key ID that allows to read devices data).  
Carbon Black Cloud API Secret Key | String | N/A | Yes | Vmware Carbon Black Cloud API Secret Key (Custom API Key ID that allows to read devices data).  
Live Response API ID | String | N/A | Yes | Endpoint Standard Live Response API key API ID.  
Live Response API Secret Key | Password | N/A | Yes | Live Response API key API Secret Key.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
Use Live Response V6 API  | Checkbox | Unchecked | No | If enabled, integration will use the Live Response API version 6 that is a part of CB Cloud (Platform) APIs.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to VMware Carbon Black Endpoint Standard Live Response with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Use Case

The action is used to test connectivity at the integration configuration page on the Google SecOps Content Hub page, and it can be executed as a manual action, not used in playbooks.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type |  |   
---|---|---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * if successful: print "Successfully connected to the VMware Carbon Black Endpoint Standard Live Response service with the provided connection parameters!"

**The action should fail and stop a playbook execution:**

  * if critical error, like wrong credentials or lost connectivity: print "Failed to connect to the VMware Carbon Black Endpoint Standard Live Response service! Error is {0}".format(exception.stacktrace)

| General |  |   
  
### Kill Process

#### Description

Kill process on a host based on the Google SecOps Host or IP entity.

**Note:** The Process name can be provided either as a Google SecOps entity (artifact) or as an action input parameter. If the Process name is passed to action both as an entity (process) and input parameter - action will be executed on the input parameter. Process name is case insensitive.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Process Name | String | N/A | No | Process name to search PID for. Process name is case insensitive.  
Check for active session x times | Integer | 20 | Yes | How many attempts action should make to get active session for the entity. Check is made every 2 seconds.  
  
#### Use Case

Kills the malicious process on the affected device.

#### Run On

This action runs on the following entities:

  1. IP Address
  2. Hostname



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result

Action should return JSON result.

Action should return the information about the executed kill process task and those results should be grouped according to the entities action ran on, to use later with expression builder. See JSON example for reference.
    
    
    {
        "entity1":[
      {
        "obj": {
            "name": "kill",
            "object": 2224
        },
        "id": 1,
        "name": "kill",
        "username": null,
        "creation_time": 1602161475,
        "completion_time": 1602161475,
        "result_code": 0,
        "result_type": "WinHresult",
        "result_desc": "",
        "status": "complete"
    }]
    }
    

### List Processes

#### Description

List processes running on endpoint based on the provided Google SecOps Host or IP entity.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Process Name | String | N/A | No | Process name to search for on the host. Process name is case insensitive.  
How Many Records To Return | Integer | 25 | No | How many records per entity action should return.  
Check for active session x times | Integer | 20 | Yes | How many attempts action should make to get active session for the entity. Check is made every 2 seconds.  
  
#### Use cases

Get a process list from the specific host for investigation.

#### Run On

This action runs on the following entities:

  1. IP Address
  2. Hostname



#### Action Results

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
cb_defense_deviceId | N/A  
cb_defense_policy | N/A  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result

Action should return JSON result.

Action should return the information about processes from the get command result and those results should be grouped according to the entities action ran on, to use later with expression builder. See JSON example for reference.
    
    
    {
        "entity1":[
      {
        "pid": 4,
        "create_time": 132463818889511,
        "path": "SYSTEM",
        "command_line": "",
        "sid": "S-1-5-18",
        "username": "NT AUTHORITY\\SYSTEM",
        "parent": 0,
        "parent_create_time": 0
      }]
    }
    

### Download File

#### Description

Download a file from a host running VMware CB Cloud Agent based on the Google SecOps Host or IP entity.

**Note:** The File name can be provided either as a Google SecOps File entity (artifact) or as an action input parameter. If the File name is passed to action both as an entity and input parameter - action will be executed on the input parameter. File name is case insensitive. File name will be appended to both Local Directory Path and Remote Directory Path to get the resulting file paths that CB Cloud API accepts. If action is executed against multiple Host or IP entities, to not overwrite the file downloaded from multiple entities, the downloaded file name is appended with Hostname or IP address, example format: hostname_filename.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
File Name | String | N/A | No | Specify the file name to download. File name is case insensitive.  
Remote Directory Path | String | N/A | Yes | Specify the remote directory path action should take to download the file. Example: C:\\\TMP\\\  
Local Directory Path | String | N/A | Yes | Specify the local directory path action should save the file to. Example: /tmp/  
Check for active session x times | Integer | 20 | Yes | How many attempts action should make to get active session for the entity. Check is made every 2 seconds.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Host
  * File (optional, if provided)



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "values": [],
        "file_details": {
            "offset": 0,
            "count": 0,
            "file_id": "55173d88-b4a8-4410-870c-8d3a0acf1cc9"
        },
        "id": 1,
        "name": "get file",
        "result_code": 0,
        "result_type": "WinHresult",
        "result_desc": "",
        "status": "complete",
        "sub_keys": [],
        "files": [],
        "input": {
            "name": "get file",
            "object": "C:\\TMP\\127.0.0.1.txt"
        },
        "create_time": "2021-06-16T11:46:41Z",
        "finish_time": "2021-06-16T11:46:42Z"
    }
    

### List Files

#### Description

List files on a host running VMware CB Cloud Agent based on the Google SecOps Host or IP entity.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Remote Directory Path | String | N/A | Yes | Specify the target directory path action should list. Example: C:\\\TMP\\\ or /tmp/  
Max Rows to Return | Integer | 50 | No | Specify how many rows action should return.  
Start from Row | Integer | 0 | No | Specify from which row action should start to return data.  
Check for active session x times | Integer | 20 | Yes | How many attempts action should make to get active session for the entity. Check is made every 2 seconds.  
  
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
        "values": [],
        "id": 0,
        "name": "directory list",
        "result_code": 0,
        "result_type": "WinHresult",
        "result_desc": "",
        "status": "complete",
        "sub_keys": [],
        "files": [
            {
                "size": 0,
                "attributes": [
                    "DIRECTORY"
                ],
                "filename": ".",
                "alternate_name": "",
                "create_time": "2021-01-27T19:06:19Z",
                "last_access_time": "2021-06-16T07:51:39Z",
                "last_write_time": "2021-06-16T07:51:40Z"
            },
            {
                "size": 0,
                "attributes": [
                    "DIRECTORY"
                ],
                "filename": "..",
                "alternate_name": "",
                "create_time": "2021-01-27T19:06:19Z",
                "last_access_time": "2021-06-16T07:51:39Z",
                "last_write_time": "2021-06-16T07:51:40Z"
            },
            {
                "size": 341,
                "attributes": [
                    "ARCHIVE"
                ],
                "filename": "127.0.0.1.txt",
                "alternate_name": "127001~1.TXT",
                "create_time": "2021-01-27T19:18:44Z",
                "last_access_time": "2021-03-18T12:34:04Z",
                "last_write_time": "2021-01-27T19:03:27Z"
            },
    

### Put File

#### Description

Put a file on a host running VMware CB Cloud Agent based on the Google SecOps Host or IP entity.

**Note:** The File name can be provided either as a Google SecOps File entity (artifact) or as an action input parameter. If the File name is passed to action both as an entity and input parameter - action will be executed on the input parameter. File name is case insensitive. File name will be appended to both Source Directory Path and Destination Directory Path to get the resulting file paths that CB Cloud API accepts.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
File Name | String | N/A | No | Specify the file name to upload. File name is case insensitive.  
Source Directory Path | String | N/A | Yes | Specify the source directory path action should take to get the file to upload. Example: /tmp/  
Destination Directory Path | String | N/A | Yes | Specify the target directory path action should upload the file to. Example: C:\\\TMP\\\  
Check for active session x times | Integer | 20 | Yes | How many attempts action should make to get active session for the entity. Check is made every 2 seconds.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Host
  * File (optional, if provided)



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "values": [],
        "id": 0,
        "name": "put file",
        "result_code": 0,
        "result_type": "WinHresult",
        "result_desc": "",
        "status": "complete",
        "sub_keys": [],
        "files": [],
        "input": {
            "chunkNumber": 0,
            "file_id": "a3623dc4-a1cc-4d29-8cde-2d36d605b1a5",
            "name": "put file",
            "object": "C:\\TMP\\test_file.txt"
        },
        "create_time": "2021-06-16T07:51:40Z",
        "finish_time": "2021-06-16T07:51:41Z"
    }
    

### Execute File

#### Description

Execute file on a host running VMware CB Cloud Agent based on the Google SecOps Host or IP entity.

**Note:** The File name can be provided either as a Google SecOps File entity (artifact) or as an action input parameter. If the File name is passed to action both as an entity and input parameter - action will be executed on the input parameter. File name is case insensitive. File name will be appended to Remote Directory Path to get the resulting file paths that CB Cloud API accepts.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
File Name | String | N/A | No | Specify the file name to execute. File name is case insensitive.  
Remote Directory Path | String | N/A | Yes | Specify the remote directory path for the file to execute. Example: C:\\\TMP\\\  
Output Log File on Remote Host | String | N/A | No | Specify the output log file action should save the redirected output to. Example: C:\\\TMP\\\cmdoutput.log  
Command Arguments to Pass to File | String | N/A | No | Specify the command arguments to pass for executing the file.Example, here we specify "/C whoami" to execute whoami command with cmd: C:\Windows\system32\cmd.exe /C whoami  
Wait for the Result | Boolean | Checkbox unchecked | No | If enabled, action will wait for the command to complete.  
Check for active session x times | Integer | 20 | Yes | How many attempts action should make to get active session for the entity. Check is made every 2 seconds.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Host
  * File (optional, if provided)



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "values": [],
        "process_details": {
            "pid": 0,
            "return_code": -1
        },
        "id": 0,
        "name": "create process",
        "result_code": 0,
        "result_desc": "",
        "status": "pending",
        "sub_keys": [],
        "files": [],
        "input": {
            "wait": false,
            "name": "create process",
            "object": "C:\\Windows\\system32\\cmd.exe /C whoami"
        },
        "create_time": "2021-06-16T12:14:25Z",
        "finish_time": "2021-06-16T12:14:25.690Z"
    }
    

### Create Memdump

#### Description

Create memdump on a host running VMware CB Cloud Agent based on the Google SecOps Host or IP entity.

**Note:** The File name for the memdump to create can be provided either as a Google SecOps File entity (artifact) or as an action input parameter. If the File name is passed to action both as an entity and input parameter - action will be executed on the input parameter. File name is case insensitive. File name will be appended to Remote Directory Path to get the resulting file paths that CB Cloud API accepts.

Additionally, note that VMware CB API does not provide an error message if an invalid Remote Directory Path is provided for the created memory dump.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
File Name | String | N/A | No | Specify the file name for memdump creation. File name is case insensitive.  
Remote Directory Path | String | N/A | Yes | Specify the directory file path to store the memdump. Example: C:\\\TMP\\\  
Check for active session x times | Integer | 20 | Yes | How many attempts action should make to get active session for the entity. Check is made every 2 seconds.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Host
  * File (optional, if provided)



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "values": [],
        "mem_dump": {
            "compressing": false,
            "complete": true,
            "dumping": false,
            "return_code": 1627,
            "percentdone": 0
        },
        "id": 0,
        "name": "memdump",
        "result_code": 0,
        "result_type": "WinHresult",
        "result_desc": "",
        "status": "complete",
        "sub_keys": [],
        "files": [],
        "input": {
            "name": "memdump",
            "object": "C:\\TMP\\cb-session-dump2.dmp"
        },
        "create_time": "2021-06-16T13:06:26Z",
        "finish_time": "+53427-09-21T04:18:52Z"
    }
    

### Delete File

#### Description

Delete a file from a host running VMware CB Cloud Agent based on the Google SecOps Host or IP entity.

**Note:** The File name can be provided either as a Google SecOps File entity (artifact) or as an action input parameter. If the File name is passed to action both as an entity and input parameter - action will be executed on the input parameter. File name is case insensitive. File name will be appended to Remote Directory Path to get the resulting file paths that CB Cloud API accepts.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
File Name | String | N/A | No | Specify the file name to delete. File name is case insensitive.  
Remote Directory Path | String | N/A | Yes | Specify the remote directory path to file to delete. Example: C:\\\TMP\\\  
Check for active session x times | Integer | 20 | Yes | How many attempts action should make to get active session for the entity. Check is made every 2 seconds.  
  
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
        "values": [],
        "id": 0,
        "name": "delete file",
        "result_code": 0,
        "result_desc": "",
        "status": "pending",
        "sub_keys": [],
        "files": [],
        "input": {
            "name": "delete file",
            "object": "C:\\TMP\\test_file.txt"
        },
        "create_time": "2021-06-16T13:43:45Z",
        "finish_time": "2021-06-16T13:43:45.796Z"
    }
    

### List Files in Cloud Storage

#### Description

List files in the VMware Carbon Black Cloud file storage for an existing live response session based on the Google SecOps Host or IP entity.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Max Rows to Return | Integer | 50 | No | Specify how many rows action should return.  
Start from Row | Integer | 0 | No | Specify from which row action should start to return data.  
Check for active session x times | Integer | 20 | Yes | How many attempts action should make to get active session for the entity. Check is made every 2 seconds.  
  
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
    
    
    [
        {
            "id": "97200931-cca6-4eed-8952-c47d529de103",
            "size": 32,
            "file_name": "test_file.txt",
            "size_uploaded": 0,
            "upload_url": null
        }
    ]
    

### Delete File from Cloud Storage

#### Description

Delete a file from the VMware Carbon Black Cloud file storage for an existing live response session based on the Google SecOps Host or IP entity.

**Note:** This action is not supported in Carbon Black Live Response API v3, API v6 should be used to run this action. The File name can be provided either as a Google SecOps File entity (artifact) or as an action input parameter. If the File name is passed to action both as an entity and input parameter - action will be executed on the input parameter. File name is case insensitive.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
File Name | String | N/A | No | Specify the file name to delete. File name is case insensitive.  
Check for active session x times | Integer | 20 | Yes | How many attempts action should make to get active session for the entity. Check is made every 2 seconds.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Host
  * File (optional, if provided)



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
