---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/illusive-networks/
title: Illusive Networks \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:37.322801+00:00
---

# Illusive Networks  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/illusive-networks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Illusive Networks

**Important:** Illusive Networks was acquired by Proofpoint and became Proofpoint Identity Threat Defense.

This document provides guidance on how to integrate Illusive Networks with Google SecOps.

### Product Use Cases

  1. Perform active actions - run forensic scans, enrich entities, add/remove deception users/servers.
  2. Ingest Incidents into Simplify.



## Configure Illusive Networks integration on Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
API Root | String | http://x.x.x.x | Yes | API root of the Illusive Networks instance.  
API Key | Password | N/A | Yes | API Key of the Illusive Networks.   
Note: string "Basic" shouldn't be a part of the value.  
CA Certificate File | String |  | False | Base 64 encoded CA certificate file.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Illusive Networks server is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## How to generate API Key

  1. Navigate to "Settings" section in Illusive Networks Console
  2. In the "General" section, scroll down to the "API Keys" part.
  3. Press on the "Add Key" button.
  4. It is recommended to add all permissions to the API Key.
  5. From the provided string you need to copy everything except for the "Basic" string.
  6. Put that value into the "API Key" parameter of the Google SecOps integration.



**How to update the rate limit**

There is a rate limit for certain endpoints in Illusive Networks. For the connector it is crucial that the limit will be high enough, so that all of the incidents were ingested. In order to update the rate limit, you need to login into the management server and navigate to: `C:\Program Files\illusive-Management-Server-3.1.XXX.XXXX\conf\general.properties.txt`

**In the file, you look for the following properties:**

  * api.incident.rate.limit.maximum.num.requests
  * api.rate.limit.windows.duration.minutes



**It is recommended that the setup will be the following:**

  * api.incident.rate.limit.maximum.num.requests=100
  * api.rate.limit.windows.duration.minutes=1
  * api.monitoring.rate.limit.maximum.num.requests = 100
  * api.forensics.rate.limit.maximum.num.requests = 100



## Actions

### Ping

#### Description

Test connectivity to Illusive Networks with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **if successful:** "Successfully connected to the Illusive Networks server with the provided connection parameters!"**Not successful: (fail)** \- Failed to connect to the Illusive Networks server! Error is {0}".format(exception.stacktrace) | General  
  
### Enrich Entities

#### Description

Enrich entities using information from Illusive Networks. Supported entities: Hostname.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
N/A |  |  |  |   
  
#### Run On

This action runs on the Host entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "machineId": "00428a29-0343-4e13-aa97-3b624739c509",
        "machineName": "HELLO",
        "isHealthy": false,
        "lastDeploymentMethodType": "WMI",
        "distinguishedName": "CN=HELLO,CN=Computers,dc=iln,dc=local",
        "groupName": null,
        "sourceDiscoveryName": "iln.local",
        "collectData": true,
        "policyName": null,
        "assignmentStatus": "ANALYSIS",
        "operatingSystemType": "Windows",
        "operatingSystemName": "Windows Server 2016 Standard Evaluation",
        "operatingSystemVersion": "10.0 (14393)",
        "agentVersion": null,
        "bitness": null,
        "loggedInUserName": null,
        "lastLogonTime": 1613078764501,
        "succeededDeceptionFamilies": 0,
        "shouldBeUninstalledDeceptionFamilies": 0,
        "desiredDeceptionFamilies": 0,
        "deceptionFamiliesPercentages": null,
        "lastExecutionType": "AGENT",
        "machineLastExecutionPhaseType": "CONNECTION",
        "machineLastExecutionPhaseStatus": "FAILURE",
        "machineLastExecutionPhaseErrorMessage": "Unreachable - no ping",
        "mitigationStatusType": null,
        "machineExecutionUnifiedStatus": "FAILURE_CONNECTION",
        "machineLastExecutionPhaseFinishDate": "2021-02-12T10:17:30.623Z",
        "endpointTrapHealthCheckHostStatus": "NotTested",
        "endpointTrapHealthCheckHostStatusLastUpdated": null,
        "failedDeceptionFamilies": 0,
        "inProgressDeceptionFamilies": 0,
        "notDeployedDeceptionFamilies": 0,
        "policyId": null,
        "ghost": false
    }
    

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
ILLNET_machineName | When available in JSON (Host Info)  
ILLNET_isHealthy | When available in JSON (Host Info)  
ILLNET_host | When available in JSON (Host Info)  
ILLNET_distinguishedName | When available in JSON (Host Info)  
ILLNET_sourceDiscoveryName | When available in JSON (Host Info)  
ILLNET_policyName | When available in JSON (Host Info)  
ILLNET_operatingSystemName | When available in JSON (Host Info)  
ILLNET_agentVersion | When available in JSON (Host Info)  
ILLNET_loggedInUserName | When available in JSON (Host Info)  
ILLNET_machineExecutionUnifiedStatus | When available in JSON (Host Info)  
ILLNET_bitness | When available in JSON (Host Info)  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if data is available for at least one (is_success = true):** "Successfully enriched the following entities using Illusive Networks: \n {entity.identifier}".  
******if data is not available for at least one (is_success = true):** "Action wasn't able to enrich the following entities using Illusive Networks: \n {entity.identifier}".  
******if data not available for all (is_success = false):** "No entities were enriched".  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Enrich Entities". Reason: {0}''.format(error.Stacktrace)  
******If 429 status code:** "Error executing action "Enrich Entities". Reason: Rate limit error. Please refer to the documentation on how to increase the rate limit". | General  
Case Wall Table | **Name:** {entity.identifier}**There will be only 2 columns:** Key and Value. | Entity  
  
### Run Forensic Scan

#### Description

Run forensic scan on the endpoint in the Illusive Networks. Works with IP and Hostname entities.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Include System Information | Checkbox | Checked | Yes | If enabled, action will return system information.  
Include Prefetch Files Information | Checkbox | Checked | Yes | If enabled, action will return information about prefetch files.  
Include Add-Remove Programs Information | Checkbox | Checked | Yes | If enabled, action will return information about add-remove programs.  
Include Startup Processes Information | Checkbox | Checked | Yes | If enabled, action will return information about startup processes.  
Include Running Processes Information | Checkbox | Checked | Yes | If enabled, action will return information about running processes.  
Include User-Assist Programs Information | Checkbox | Checked | Yes | If enabled, action will return information about user-assist programs.  
Include Powershell History Information | Checkbox | Checked | Yes | If enabled, action will return information about powershell history.  
Max Items To Return  
| Integer | 50 | No | Specify how many items to return. If nothing is provided, action will return everything.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Host



#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "Entity.identifier": {
            "host_info": "{Host_info part}",
            "prefetch_info": "{prefetch_info}",
            "installed_programs_info": "{installed_programs_info}",
            "startup_processes": "{startup_processes}",
            "running_processes": "{running_processes}",
            "user_assist_info": "{user_assist_info}",
            "powershell_history": "{powershell history}"
        }
    }
    

##### Entity Enrichment

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
ILLNET_osName | When available in JSON (Host Info)  
ILLNET_machineType | When available in JSON (Host Info)  
ILLNET_host | When available in JSON (Host Info)  
ILLNET_loggedInUser | When available in JSON (Host Info)  
ILLNET_userProfiles | When available in JSON (Host Info)  
ILLNET_operatingSystemType | When available in JSON (Host Info)  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if successfully executed for at least one (is_success = true):** "Successfully ran forensic scan on the following endpoints in Illusive Networks: {entity.identifier}"  
******If not success for at least one:** "Action wasn't able to get any information from forensic scan on the following endpoints: {entity.identifier}"  
******If no success for all:** "No forensic information was found on the provided endpoints."  
******Async message:** "Started the forensic scan on the following endpoints: {entity identifier}. \nFinished forensic scan on the following endpoints."  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "Run Forensic Scan". Reason: {0}''.format(error.Stacktrace)  
******If none of the "include ..." parameters are enabled:** "Error executing action "Run Forensic Scan". Reason: you need to enable at least one of the "Include ..." parameters" | General  
Case Wall Table Host Info | **Name:** {entity.identifier}**There will be only 2 columns:** Key and Value. | Entity  
Case Wall Table Prefetch_Info | **Name:** "{entity.identifier}: Prefetch Files Information"**Columns:** File Name Last Execution Time File Modification TimePrefetch File Name  | General  
Case Wall TableINSTALLED_PROGRAMS_INFO | **Name:** "{entity.identifier}: Add-Remove Programs Information"**Columns:** Display Name File Name | General  
Case Wall TableSTARTUP_PROCESSES | **Name:** "{entity.identifier}: Startup Processes"**Columns:** Name Command Location User  | General  
Case Wall TableRUNNING_PROCESSES | **Name:** "{entity.identifier}: Running Processes"**Columns:** User Admin Privileges Command Process ID Process Name Start Time  | General  
Case Wall TableUSER_ASSIST_INFO | **Name:** "{entity.identifier}: User-Assist Programs Information"**Columns:** File Name Username Last Used Date  | ****  
Case Wall TablePOWER_SHELL_HISTORY | **Name:** "{entity.identifier}: Powershell History"**Columns:** Username Command  |   
  
### List Deceptive Items

#### Description

List available deceptive items in Illusive Networks.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Deceptive Type | DDL | AllPossible Values:AllOnly UsersOnly Servers | Yes | Specify what kind of deceptive items should be returned.  
Deceptive State | DDL | AllPossible Values:AllOnly Approved, Only Suggested  | Yes | Specify what kind of deceptive items should be returned based on state.  
Max Items To Return | Integer | 50 | No | Specify how many items to return. Default: 50. If nothing is specified, action will return all items.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### JSON Result
    
    
    {
        "users": [
            {
                "username": "backupad",
                "password": "5437niwY",
                "domainName": "intw-lab.local",
                "policyNames": [
                    "Full Protection"
                ],
                "adUser": false,
                "activeUser": false,
                "deceptiveState": "APPROVED"
            },
            {
                "username": "jvillar",
                "password": "ritA1102",
                "domainName": "intw-lab.local",
                "policyNames": [],
                "adUser": true,
                "activeUser": false,
                "deceptiveState": "SUGGESTED"
            },
            {
                "username": "gaccess.user",
                "password": "psUiS01",
                "domainName": "intw-lab.local",
                "policyNames": [],
                "adUser": true,
                "activeUser": false,
                "deceptiveState": "SUGGESTED"
            },
            {
                "username": "service.user",
                "password": "mAkaYe4",
                "domainName": "intw-lab.local",
                "policyNames": [],
                "adUser": true,
                "activeUser": false,
                "deceptiveState": "SUGGESTED"
            }
        ],
        "servers": [
            {
                "host": "10.0.0.2",
                "serviceTypes": [
                    "DB"
                ],
                "policyNames": [
                    "Full Protection"
                ],
                "adHost": false,
                "deceptiveState": "APPROVED"
            },
            {
                "host": "10.0.0.1",
                "serviceTypes": [
                    "DB"
                ],
                "policyNames": [
                    "Full Protection"
                ],
                "adHost": false,
                "deceptiveState": "APPROVED"
            }
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
**if 200 and data is available (is_success = true):** "Successfully returned available deceptive items from Illusive Networks".  
******If 200 and no data is available (is_success=false)** "No data was found regarding deceptive items based on the provided criteria in Illusive Networks."  
******The action should fail and stop a playbook execution:**  
**if fatal error, like wrong credentials, no connection to server, other:** "Error executing action "List Deceptive Items". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Name:** "Deceptive Users"**Column:** Username Password Domain Policies AD User Active State  | General  
Case Wall Table | **Name:** "Deceptive Servers"**Column:** HostServicesPolicies AD Server State  | General  
|  |   
  
### Add Deceptive User

#### Description

Add deceptive users in Illusive Networks.

#### Parameters

**Name** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---  
Username | N/A | Yes | Specify the username for the new deceptive user.  
Password | N/A | Yes | Specify the password for the new deceptive user.  
DNS Domain | N/A | No | Specify the domain name for the new deceptive user.  
Policy Names | N/A | No | Specify a comma-separated list of policies that need to be applied to the new deceptive user. If nothing is provided action will use by default all policies.  
  
#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Success (is_success=true)** → Successfully added deceptive user in Illusive networks.******Case 1. User Already Exists (fail)** \- Error executing action "{action name}". Reason: Deceptive user "{username}" already exists.**Case 2. 400 status code (fail)** \- Error executing action "{action name}". Reason: {error message}.**Case 3. General Error (fail)** \- Error executing action "{action name}". Reason: {error traceback}. | General  
  
### Remove Deceptive User

#### Description

Remove deceptive user from Illusive Networks.

#### Parameters

**Name** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---  
Username | N/A | Yes | Specify the username of the deceptive user that needs to be removed.  
  
#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Success →** Successfully removed deceptive user in Illusive networks.**Case 1. User doesn't exist (is_success=false) -** Action wasn't able to remove deceptive user "{username}". Reason: Deceptive user "{username}" doesn't exist.**Case 2. General Error (fail) -** Error executing action "{action name}". Reason: {error traceback}. | General  
  
### Add Deceptive Server

#### Description

Add deceptive servers in Illusive Networks.

#### Parameters

**Name** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---  
Server Name | N/A | Yes | Specify the name for the new deceptive server.  
Service Types | DB | Yes | Specify a comma-separated list of service types for new deceptive server.  
Policy Names |  | No | Specify a comma-separated list of policies that need to be applied to the new deceptive server. If nothing is provided action will use by default all policies.  
  
#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Success (is_success=true)** → Successfully added deceptive server in Illusive networks.**Case 1. Server Already Exists (fail) -** Error executing action "{action name}". Reason: Deceptive server "{server name}" already exists.**Case 2. 400 status (fail) -** Error executing action "{action name}". Reason: {error message}.**Case 3. General Error -** Error executing action "{action name}". Reason: {error traceback}. | General  
  
### Remove Deceptive Server

#### Description

Remove deceptive server from Illusive Networks.

#### Parameters

**Name** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---  
Server Name | N/A | Yes | Specify the name of the deceptive server that needs to be removed.  
  
#### Action Results

##### Script Result

**Script Result Name** | **Value Options**  
---|---  
is_success | is_success=False  
is_success | is_success=True  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **Success →** Successfully removed deceptive server in Illusive networks.**Case 1. Server doesn't exist (is_success=false) -** Action wasn't able to remove deceptive server "{server name}". Reason: Deceptive server "{server name}" doesn't exist.**Case 2. General Error -** Error executing action "{action name}". Reason: {error traceback}. | General  
  
## Connectors

### Illusive Networks - Incidents Connector

#### Description

Pull incidents with related forensic timeline from Illusive Networks.

**Note:** This connector requires changes to the rate limiting on the Illusive Networks server. Default rate limit is too small. All of the steps are available in the documentation. Whitelisting and Blacklisting is done via type of the incident.

#### Configure Illusive Networks - Incidents Connector in Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type> | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | details_serviceType | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | http://x.x.x.x | Yes | API root of the Illusive Networks instance.  
API Key | String | N/A | Yes | API Key of the Illusive Networks. Note: string "Basic" shouldn't be a part of the value.  
Alert Severity | String | Medium | Yes | Severity of the Google SecOps alert that will be created based on the incidents from Illusive Networks. Possible values: Informational Low Medium High Critical  
Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch incidents.  
Max Incidents To Fetch | Integer | 10 | No | How many incidents to process per one connector iteration. Maximum is 1000.  
Use whitelist as a blacklist | Checkbox | Checked | Yes | If enabled, whitelist will be used as a blacklist.  
Verify SSL | Checkbox | Unchecked | Yes | If enabled, verify the SSL certificate for the connection to the Illusive Networks server is valid.  
CA Certificate File | String | N/A | No | Base 64 encoded CA certificate file.  
Proxy Server Address | String | N/A | No | The address of the proxy server to use.  
Proxy Username | String | N/A | No | The proxy username to authenticate with.  
Proxy Password | Password | N/A | No | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

The connector supports proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
