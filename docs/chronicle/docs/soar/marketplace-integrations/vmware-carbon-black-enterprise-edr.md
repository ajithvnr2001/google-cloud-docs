---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/vmware-carbon-black-enterprise-edr/
title: VMware Carbon Black Enterprise EDR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:49.118731+00:00
---

# VMware Carbon Black Enterprise EDR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/vmware-carbon-black-enterprise-edr/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# VMware Carbon Black Enterprise EDR

This document provides guidance on how to integrate VMware Carbon Black Enterprise EDR with Google SecOps.

## Product Use Cases

  1. Perform investigative actions - get data from CB Enterprise EDR as part of an alert analysis in Google Security Operations.
  2. Perform configuration actions - configure CB Enterprise EDR feeds/watchlists from Google SecOps.



## Product Permission

Concepts required to access Carbon Black Enterprise EDR (ThreatHunter) APIs:

  1. Service Hostname
  2. API Keys
  3. RBAC
  4. Organization Keys

**Note:** How to Configure API Access for Carbon Black Enterprise EDR (ThreatHunter) Google SecOps integration will be described in the section "Configure API Access for Carbon Black Enterprise EDR (ThreatHunter) Google SecOps integration" below.

### Service Hostnames

There are two Carbon Black Cloud hostnames:

  * https://defense-<environment>.conferdeploy.net/
  * https://api-<environment>.conferdeploy.net/



In addition, we have multiple environments such as (not a complete list):

  * prod02
  * prod04
  * prod05



For Carbon Black Enterprise EDR (ThreatHunter) API the following hostnames will be used: https://defense-<environment>.conferdeploy.net/

### API Keys

Carbon Black Enterprise EDR (ThreatHunter) APIs and Services are authenticated via API Keys. Users can view API Key settings within the Carbon Black Cloud Console under **Settings** > **API Keys**.

API keys include two parts:

  * API Secret Key (previously API Key).
  * API ID (previously Connector ID).



Authentication is passed to the API via the X-Auth-Token HTTP header.

  1. To generate the appropriate header, concatenate the API Secret Key with the API ID with a forward slash in between.
  2. For example, if the API Secret Key is ABCD and the API ID is 1234, the corresponding X-Auth-Token HTTP header will be: X-Auth-Token: ABCD/1234



All API requests must be authenticated by using an API Secret Key and an API ID. Unauthenticated requests return an HTTP 401 error.

### How to obtain an API Secret Key and API ID

  1. Log into your Carbon Black Cloud Organization.
  2. Navigate to **Settings** > **API Keys**.
  3. Click "**Add API Key** ".
  4. Configure Name, Access Level, etc.
  5. Obtain your API Secret Key and API ID pair.



This allows an organization administrator to define an API Key and get access to the API Secret Key and API ID that will be required to authenticate the API request. In addition, administrators can restrict the use of this API key to a specific set of IP addresses for security reasons.

### API Key Access Levels

Currently there are four major access levels for API Keys available in the API Keys page. Each access level provides different access levels to API routes:

  1. Custom Key Access Level: provides customizable authorization.

     * Custom API Keys are a result of our role based access control efforts (RBAC).
     * Allows customers to apply access controls and create least-privileged API keys.
     * Custom API Keys can be assigned User Roles or Access Levels.
  2. API Key Access Level: provides access to all APIs except for the Notifications API and the Live Response API.

  3. SIEM Key Access Level: provides access to the Notifications API.

  4. Live Response Key Access Level: provides access to all APIs available to (1) above plus the Live Response API.




_Carbon Black Enterprise EDR (ThreatHunter) Service to API Access Level Correlation_ _Platform API is bolded_

API/Service Category | API Key Access Level(s) Permitted  
---|---  
PSC /appservices/* | Custom (with appropriate permissions)  
CB-TH /threathunter/* | Custom (with appropriate permissions)API  
CB-LO /livequery/* | Custom (with appropriate permissions)  
CB-D /integrationServices/v3/notification/ | SIEM  
CB-D /integrationServices/* | APILive Response  
  
### Organization Keys

In addition to API Keys, many Carbon Black Cloud APIs or Services require an org_key in the API request path. This is to support customers that manage multiple orgs.

You can find your org_key in the Carbon Black Cloud Console under Settings > API Keys.

## Configure API Access for Carbon Black Enterprise EDR (ThreatHunter) Google SecOps integration

To configure API Access for Carbon Black Enterprise EDR (ThreatHunter) Google SecOps integration the following steps needs to be taken:

  1. Login Carbon Black Cloud Console, go to **Settings** > **API Access**.
  2. On the API Access page, go to Access Levels.
  3. On Access Levels page, click **\+ Add Access Level**.
  4. In the opened window, provide a name and description for the new Access Level, and select permissions like on the screenshot below:

![List of required
permissions](https://docs.cloud.google.com/static/chronicle/images/integrations/vmware-carbon-black-enterprise-edre-permissions.png)

  5. Go back to API Access tab.

  6. Click "**\+ Add API Key** " to create a new API key.

  7. In the opened tab fill mandatory field and select the Access Level you configured on step 4:

![Edit API key
settings](https://docs.cloud.google.com/static/chronicle/images/integrations/vmware-carbon-black-enterprise-edre-edit-api-key.png)

  8. Once you click **Save** , you will be shown API ID and API Secret Key. **Please save those values, because they will be shown once.**

  9. Once the API ID and API Secret key are saved, the API Access in Carbon Black Enterprise EDR (ThreatHunter) is done.




## Configure VMware Carbon Black Enterprise EDR (Threat Hunter) integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Dexcription | String | N/A | No | Description of the Instance.  
API Root | String | N/A | Yes | Vmware Carbon Black Cloud API Root URL.  
Organization Key | String | N/A | Yes | Vmware Carbon Black Cloud Organization Key.  
API ID | String | N/A | Yes | Vmware Carbon Black Cloud API ID (Custom API Key ID).  
API Secret Key | String | N/A | Yes | Vmware Carbon Black Cloud API Secret Key (Custom API Secret Key).  
Run Remotely | Checkbox | N/A | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, please see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to the VMware Carbon Black Enterprise EDR with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Playbook Use Cases Examples

The action is used to test connectivity at the integration configuration page on the Google SecOps Content Hub page, and it can be executed as a manual action, not used in playbooks.

#### Run On

This action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value/Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * If successful: print "Successfully connected to the VMware Carbon Black Enterprise EDR server with the provided connection parameters!"

**The action should fail and stop a playbook execution:**

  * If not successful: print "Failed to connect to the VMware Carbon Black Enterprise EDR server! Error is {0}".format(exception.stacktrace)

| General  
  
### Process Search

#### Description

Search information about process activity on the host with CB sensor based on the provided search parameters. The action accepts Host Google SecOps entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Query | String | N/A | No | Query to execute in process search. For example, process_name:svchost.exe - to search based by process name, process_hash:9520a99e77d6196d0d09833146424113 - to search based by process hash.  
Time Frame | Integer | 4 | No | Specify a time frame in hours for which to fetch alerts.  
Record limit | Integer | 20 | Yes | Specify how many records can be returned by the action.  
Sort by | String | N/A | No | Specify a parameter for sorting the data.  
Sort order | DDL | ASC | No | Sort order.  
  
#### Playbook Use Cases Examples

**Search for events caused by processes based on the provided search parameters.**

During the analysis of an alert, that is related to a specific host that is managed by CB Platform, the user wants to investigate the host - search for particular events caused by processes running based on the provided search parameters. Users can run this action for threat hunting activity - proactively search if there are any suspicious processes/events on the host in question.

#### Run On

This action runs on the Host entity.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
    "results": [
        {
            "alert_id": [
                "null/WSD2CQMT"
            ],
            "backend_timestamp": "2020-03-04T21:42:45.080Z",
            "device_id": 3078944,
            "device_name": "qaam\\manticorewin864",
            "device_policy_id": 6525,
            "device_timestamp": "2020-03-04T21:39:33.180Z",
            "enriched": true,
            "enriched_event_type": "CREATE_PROCESS",
            "event_description": "The script \"<share><link hash=\"74fcbbb574bfd505cf0680575a1c025f6cead071fce78ee0cc2c7bac7dd24ce9\">C:\\programdata\\wmirepair.bat</link></share>\" invoked the application \"<share><link hash=\"7eadc73f8aa77148ca289d5ce5c2632f3a157d313079583454c0421bb97d5646\">C:\\windows\\syswow64\\regsvr32.exe</link></share>\". ",
            "event_id": "ecc6954f5e6011eaa0de89cc027330db",
            "event_type": "childproc",
            "ingress_time": 1583358118950,
            "legacy": true,
            "org_id": "7DESJ9GN",
            "parent_guid": "7DESJ9GN-002efb20-00001604-00000000-1d5f26cab1067fe",
            "parent_pid": 5636,
            "process_guid": "7DESJ9GN-002efb20-00000d58-00000000-1d5f26d6615c568",
            "process_hash": [
                "629ae017d28848b68485bd2aeede9129",
                "74fcbbb574bfd505cf0680575a1c025f6cead071fce78ee0cc2c7bac7dd24ce9"
            ],
            "process_name": "c:\\programdata\\wmirepair.bat",
            "process_pid": [
                3416
            ],
            "process_username": [
                "NT AUTHORITY\\SYSTEM"
            ]
        },
        ...
    ]  }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * If successful: print "Found process information for the following entities:\n {0}".format( entity.Identifiers list)
  * If is_success=False for all of the provided entities: print "No search results were returned."
  * If is_success=False for some of the provided entities because it can't find results for specified search parameters: print "Action was not able to find process information for the following entities:\n {0}".format(entity.Identifiers list)
  * If is_success=False for some of the provided entities because there was an error running the search (for example timeout): print "Failed to get results because of the errors running search for the following entities:/n {0}".format(entity.identifiers list)

**The action should fail and stop a playbook execution:**

  * If fatal error, like wrong credentials, no connection to server, other: print "Failed to execute action! Error is {0}".format(exception.stacktrace)

| Both  
Table | **Table Name:** Process search results for {entityIdentifier} **Columns:**

  * Event id (event_id)
  * Event Type ("enriched_event_type")
  * Process Name (process_name)
  * Process GUID (process_guid)
  * Process PID (process_pid)
  * Process Parent GUID (parent_guid)
  * Process Parent PID (parent_pid)
  * Process File Hash (process_hash)
  * Process Run As ("process_username")
  * Created Time ("device_timestamp")
  * Event Description (event_description)
  * Local ipv4 address (event_network_local_ipv4)
  * Network Protocol (event_network_protocol)
  * Remote IPv4 Address (event_network_remote_ipv4)
  * Remote Port (event_network_remote_port)

| Entity  
  
### Get Events Associated With Process by Process Guid

#### Description

Get events associated with specific processes based on the information from the VMware Carbon Black Enterprise EDR. This action can get more detailed results on specific process activity than "Process Search" action. Note for the action to work, Google SecOps processed artifact passed to the action should be a process guid type.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Search criteria | String | N/A | No | Specify a search criteria for the request. Currently, only "event_type" values are accepted as the search criteria, for example, netconn. Multiple values are accepted as a comma separated string.  
Query | Search | N/A | Yes | Query to execute in process search.For example, "netconn_action:ACTION_CONNECTION_CREATE OR netconn_action:ACTION_CONNECTION_ESTABLISHED"  
Time Frame | Integer | 4 | No | Specify a time frame in hours for which to fetch alerts.  
Record limit | Integer | 20 | No | Specify how many records can be returned by the action.  
Sort by | String | N/A | No | Specify a parameter for sorting the data.  
Sort order | DDL | ASC | No | Sort order  
  
#### Playbook Use Cases Examples

**Investigate specific process activity.**

During the analysis of an alert, that is related to a specific host that is managed by CB Platform, it was discovered that the host has a suspicious process running. The Google SecOps user needs an action that will use CB Enterprise EDR functionality to get events, associated with a given process from Google SecOps.

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "results": [
            {
                "backend_timestamp": "2020-04-26T18:38:50.128Z",
                "created_timestamp": "2020-05-19T03:56:53.483Z",
                "event_guid": "ufzid3pPQs-yrRlPBe8-ww",
                "event_hash": "ce6a949bcd3879897c9eac258ec6a091",
                "event_timestamp": "2020-04-26T18:34:16.258Z",
                "event_type": "netconn",
                "legacy": false,
                "netconn_action": "ACTION_CONNECTION_CREATE",
                "netconn_inbound": true,
                "netconn_local_ipv6": "FF020000000000000000000000010003",
                "netconn_local_port": 5355,
                "netconn_protocol": "PROTO_UDP",
                "netconn_remote_ipv6": "FE800000000000000000000000000000",
                "netconn_remote_port": 58994,
                "process_guid": "7DESJ9GN-002efb20-000003ec-00000000-1d5fb6d63ba535c",
                "process_pid": 1004
            },
            ...
        ]
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * If successful: print "Found events for the following process guids:\n {0}".format( process guid list)
  * If is_success=False for all of the provided process guids: print "No search results were returned."
  * If is_success=False for some of the provided entities because it can't find specified process guid: print "Action was not able to find information for the following processes:\n {0}".format(process guids list).
  * If is_success=False for some of the provided entities because there was an error running the search (for example timeout): print "Failed to get results because of errors running search for the following process guids:/n {0}".format(entity.identifiers list)

**The action should fail and stop a playbook execution:**

  * If fatal error, like wrong credentials, no connection to server, other: print "Failed to execute action! Error is {0}".format(exception.stacktrace)

| General  
Table | **Table Name:** Found events for process {process artifact identifier} **Columns:** Should be generated automatically based on the returned results. | Entity  
  
### Enrich Hash

#### Description

Enrich Google SecOps File hash entity based on the information from the VMware Carbon Black Enterprise EDR.

**Warning:** The action accepts file hashes only in SHA256 format!

#### Playbook Use Cases Examples

**Enrich Google SecOps filehash entity with information from CB Enterprise EDR.**

During the processing of a possible malware infection alert that is associated with a host that have CB Platform sensor, the user needs to have enrichment data from CB Enterprise EDR (part of platform) about particular filehashes that are associated with the alert in question for investigative reasons. For example, as part of enrichment, the user can get related filehash metadata, when this filehash was first detected in Organization, and on which host.

#### Run On

This action runs on the Filehash entity in the Sha256 format.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Source (JSON Key) | Logic - When to apply  
---|---|---  
CB_ENT_EDR.sha256 | sha256 | always  
CB_ENT_EDR.md5 | md5 | always  
CB_ENT_EDR.architecture | architecture | always  
CB_ENT_EDR.available_file_size | available_file_size | always  
CB_ENT_EDR.charset_id | charset_id | always  
CB_ENT_EDR.comments | comments | If not null  
CB_ENT_EDR.company_name | company_name | always  
CB_ENT_EDR.copyright | copyright | always  
CB_ENT_EDR.file_available | file_available | always  
CB_ENT_EDR.file_description | file_description | always  
CB_ENT_EDR.file_size | file_size | always  
CB_ENT_EDR.file_version | file_version | always  
CB_ENT_EDR.internal_name | internal_name | always  
CB_ENT_EDR.lang_id | lang_id | If not null  
CB_ENT_EDR.original_filename | original_filename | always  
CB_ENT_EDR.os_type | os_type | always  
CB_ENT_EDR.private_build | private_build | If not null  
CB_ENT_EDR.product_description | product_description | If not null  
CB_ENT_EDR.product_name | product_name | always  
CB_ENT_EDR.product_version | product_version | always  
CB_ENT_EDR.special_build | special_build | If not null  
CB_ENT_EDR.trademark | trademark | If not null  
CB_ENT_EDR.found_times | num_devices | always  
CB_ENT_EDR.first_seen_device_timestamp | first_seen_device_timestamp | always  
CB_ENT_EDR.first_seen_device_id | first_seen_device_id | always  
CB_ENT_EDR.first_seen_device_name | first_seen_device_name | always  
CB_ENT_EDR.last_seen_device_timestamp | last_seen_device_timestamp | always  
CB_ENT_EDR.last_seen_device_id | last_seen_device_id | always  
CB_ENT_EDR.last_seen_device_name | last_seen_device_name | always  
  
##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "sha256": "e24dd278cec867486b68418c9066ffa9bd4f394dac3ba94125d58415f677f0f4",
        "architecture": [
            "amd64"
        ],
        "available_file_size": 207800,
        "charset_id": 1200,
        "comments": null,
        "company_name": "Example Organization",
        "copyright": "Copyright  © 2019",
        "file_available": true,
        "file_description": "OpenJDK Platform binary",
        "file_size": 207800,
        "file_version": "8.0.2320.9",
        "internal_name": "java",
        "lang_id": null,
        "md5": "afede6f64ed8878bc0cac57e1831a3bc",
        "original_filename": "java.exe",
        "os_type": "WINDOWS",
        "private_build": null,
        "product_description": null,
        "product_name": "OpenJDK Platform 8",
        "product_version": "8.0.2320.9",
        "special_build": null,
        "trademark": null
    }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**

  * If successful and at least one of the provided entities were enriched: print "Successfully enriched entities: {0}".format([entity.Identifier]).
  * If fail to enrich all of the provided entities: print "No entities were enriched."
  * If fail to find data in VMware Carbon Black Enterprise EDR to enrich specific entities: print "Action was not able to find VMware Carbon Black Enterprise EDR info to enrich the following entities: {0}".format([entity.identifier])
  * If fail to run one of the enrich queries, for example error 500 when getting one response, but the other one is ok - is_success should be False, but action should enrich with data it got from other response and print: "The following entities were partially enriched because of the errors getting entity data:/n {0}".format(entityIdentifier list)

**The action should fail and stop a playbook execution:**

  * If fatal error, like wrong credentials, no connection to server, other: print "Failed to execute Enrich Entities action! Error is {0}".format(exception.stacktrace)

| General  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
