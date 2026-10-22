---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cisco-amp/
title: Cisco AMP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:01.595939+00:00
---

# Cisco AMP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cisco-amp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cisco AMP

**Important:** Cisco AMP was renamed to Cisco Secure Endpoint.

This document describes how to integrate Cisco Secure Endpoint with Google Security Operations.

## Configure Cisco Secure Endpoint to work with Google Security Operations

### Generating Client ID and API Key:

  1. Log into [Cisco Secure Endpoint](https://console.amp.cisco.com/) console for North America or [Cisco Secure Endpoint](https://console.eu.amp.cisco.com/) console for Europe.

  2. Go to **Accounts > Business** and click **Edit**.

  3. Under features, click **Regenerate** to generate the **Client ID** and secure **API Key**.




Once you have the API client ID and API key, you can make the API calls as follows: `https://<your_client_id>:<your_api_key>@<api_endpoint>`

Alternatively, you can use Basic HTTP Authentication. Base64 encode the string ":", and send that prefixed with the string "Basic" as the authorization header. For instance, if your client_id was 1234, and your api_key was "atest", then it would be base64 encoded to `MTIzNDphdGVzdA==`, and your header would be:

**Authorization:** `Basic MTIzNDphdGVzdA==`

### Base64 encoding

The client ID, API key can be encoded through [Base64 Decode and Encode](https://www.base64encode.org/).

Type the client ID and API key in the format Client_ID:API key and encode it to generate a Basic HTTP Authentication.

### Network

Function | Default Port | Direction | Protocol  
---|---|---|---  
API | Multivalues | Outbound | apikey  
  
## Configure Cisco AMP integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Instance Name | String | N/A | No | Name of the Instance you intend to configure integration for.  
Description | String | N/A | No | Description of the Instance.  
API Root | String | `https://api.amp.cisco.com` | Yes | Specify the Cisco Secure Endpoint API root URl.  
Client ID | String | N/A | Yes | Specify the Client ID.  
API Key | Password | N/A | Yes | Specify the Cisco Secure Endpoint API key.  
Use SSL | Checkbox | Unchecked | No | If enabled, verifies that the SSL certificate for the connection to the Cisco Secure Endpoint server is valid.  
Run Remotely | Checkbox | Unchecked | No | Check the field in order to run the configured integration remotely. Once checked, the option appears to select the remote user (agent).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Add File to File List

#### Description

Add a SHA-256 for a specific file list.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
File Name List | String | N/A | Yes | File Blacklist.  
Description | String | N/A | Yes | Description of the file.  
  
#### Run On

This action runs on the File entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
### Create Group

#### Description

Create a new group.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Group Name | String | N/A | Yes | The name of the new group.  
Group Description | String | N/A | Yes | The description of the new group.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
group_name | True/False | group_name:False  
  
##### JSON Result
    
    
    {
       "source": "CreatedviaAPI",
       "guid": "c5e2099d-3aeb-4dc2-add4-42fb01d05c51",
       "name": "test", "policies":
           [{
              "product": "windows",
              "description": "ThispolicyputstheAMPforEndpointsConnectorinamodethatwillonlydetectmaliciousfilesbutnotquarantinethem.Maliciousnetworktrafficisalsodetectedbutnotblocked.",
              links":
                     {
                       "policy": "https: //api.amp.cisco.com/v1/policies/a8ba7d10-de10-42a6-a6e4-8d679f5b1ec2", "policy_xml": "https: //api.amp.cisco.com/v1/policies/a8ba7d10-de10-42a6-a6e4-8d679f5b1ec2.xml"
                    },
                "default": true,
                "File_lists":
                      [{
                        "guid": "cef9b12e-4a25-4f1a-93f4-3836ebd97ed5",
                        "type": "simple_custom_detections",
                        "name": "FileBlacklist"
                       },
                      {
                        "guid": "38c1a9eb-0389-4f12-8084-96f5ee62d72e",
                        "type": "application_blocking",
                        "name": "ExecutionBlacklist"
                       },
                       {
                        "guid": "3133128e-5455-4e74-82c5-1ff3c816c414",
                        "type": "application_whitelist",
                        "name": "FileWhitelist"
                       }],
                "ip_lists": [],
                "Used_in_groups":
                      [{
                        "guid": "d3f8be3c-e53b-4b31-a8b7-a78a69b74ea1",
                        "name": "Audit",
                        "description": "AuditGroupforPartner-Siemplify"
                      }],
               "inherited": false,
               "serial_number": 28,
               "guid": "a8ba7d10-de10-42a6-a6e4-8d679f5b1ec2",
               "Exclusion_sets":
                     [{
                        "guid": "43fc08b5-c603-4c24-9b4d-501d342f443c",
                        "name": "WorkstationExclusions"
                      }],
               "name": "Audit"
            }],
       "description": "added by siemplify!"
    }
    

### Get Computer Info

#### Description

Get details about a computer.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

Entities are marked as Suspicious (True) if they exceed threshold. Else: False.

**Enrichment Field Name** | **Logic - When to apply**  
---|---  
Demo_AMP | Returns if it exists in JSON result  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    {
       "Demo_AMP":
             {
               "operating_system": "Windows 7, SP 1.0",
               "connector_guid": "f719857b-5474-467f-803c-00393616cdcf",
               "network_addresses":
                  [{
                     "ip": "1.1.1.1",
                     "mac": "18:ac:08:1f:49:13"
                   }],
               "faults": [],
               "external_ip": "1.1.1.1",
               "group_guid": "bcaafdfb-bf15-4f65-81e0-58b14624ff26",
               "hostname": "Demo_AMP",
               "install_date": "2018-05-09T14:51:04Z",
               "connector_version": "1.1.1.1",
               "internal_ips": ["92.168.133.146"],
               "Policy":
                   {
                     "guid": "d04fbbc0-fc5d-45d9-94f6-9e53f5079c2f",
                     "name": "Triage"
                   },
               "active": true,
               "last_seen": "2018-05-09T14:51:04Z"
               }
    }
    

### Get Computers by File Hash

#### Description

Fetch a list of computers that have observed files with the given SHA-256 value.

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

Entities are marked as Suspicious (True) if they exceed threshold. Else: False.

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [{
       "EntityResult":
           {
            "0":
               {
                "connector_guid": "abfe956e-8b67-4d5c-9353-1b490cdad8b2",
                "links":
                   {
                    "trajectory": "https://api.amp.cisco.com/v1/computers/abfe956e-8b67-4d5c-9353-1b490cdad8b2/trajectory",
                    "computer": "https://api.amp.cisco.com/v1/computers/abfe956e-8b67-4d5c-9353-1b490cdad8b2",
                    "group": "https://api.amp.cisco.com/v1/groups/1d7e90f6-b6b6-49ba-90ab-a8fe13d8f3d4"
                    },
                "group_guid": "1d7e90f6-b6b6-49ba-90ab-a8fe13d8f3d4",
                "active": "True",
                "operating_system": "Windows Server 2012 R2, SP 0.0",
                "network_addresses":
                   [{
                      "ip": "10.0.0.4",
                      "mac": "00:0d:3a:4e:fc:6e"
                     },
                     {
                       "ip": "10.212.134.201",
                       "mac": "00:09:0f:aa:00:01"
                     }],
                "faults": [],
                "external_ip": "13.72.107.194",
                "hostname": "poc-JuanV",
                "install_date": "2019-04-29T19:37:06Z",
                "connector_version": "6.2.9.10881",
                "internal_ips": ["10.0.0.4", " 10.212.134.201"],
                "policy":
                    {
                       "guid": "9d8be508-fbec-457a-a0eb-c0cb82be482c",
                       "name": "Server"
                    },
                "last_seen": "2019-05-28T11:46:32Z"
                }
           },
      "Entity": "entityIdentifier"
     }]
    

### Get Computers by File Name

#### Description

Fetch a list of computers that have observed files with the given file name.

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [{
       "EntityResult":
         {
          "0":
            {
             "connector_guid": "abfe956e-8b67-4d5c-9353-1b490cdad8b2",
              "Links":
                 {
                  "trajectory": "https://api.amp.cisco.com/v1/computers/abfe956e-8b67-4d5c-9353-1b490cdad8b2/trajectory",
                  "computer": "https://api.amp.cisco.com/v1/computers/abfe956e-8b67-4d5c-9353-1b490cdad8b2",
                  "group": "https://api.amp.cisco.com/v1/groups/1d7e90f6-b6b6-49ba-90ab-a8fe13d8f3d4"
                  },
              "group_guid": "1d7e90f6-b6b6-49ba-90ab-a8fe13d8f3d4",
              "active": "True",
              "operating_system": "Windows Server 2012 R2, SP 0.0",
               "network_addresses":
                  [{
                     "ip": "10.0.0.4",
                     "mac": "00:0d:3a:4e:fc:6e"
                   },
                   {
                     "ip": "10.212.134.201",
                     "mac": "00:09:0f:aa:00:01"
                   }],
               "faults": [],
               "external_ip": "13.72.107.194",
               "hostname": "poc-JuanV",
               "install_date": "2019-04-29T19:37:06Z",
               "connector_version": "6.2.9.10881",
               "internal_ips": ["10.0.0.4", " 10.212.134.201"],
               "policy":
                   {
                      "guid": "9d8be508-fbec-457a-a0eb-c0cb82be482c",
                      "name": "Server"
                   },
               "last_seen": "2019-05-28T11:46:32Z"
              }
         },
       "Entity": "entityIdentifier"
     }]
    

### Get Computers by Network Activity (IP)

#### Description

Fetch a list of computers that have connected to the given IP address.

#### Parameter

N/A

#### Run On

This action runs on the IP Address entity.

#### Action Results

##### Entity Enrichment

Entities are marked as Suspicious (True) if they exceed threshold. Else: False.

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [{
      "EntityResult":
        {
         "0":
           {
            "connector_guid": "abfe956e-8b67-4d5c-9353-1b490cdad8b2",
            "links":
               {
                 "trajectory": "https://api.amp.cisco.com/v1/computers/abfe956e-8b67-4d5c-9353-1b490cdad8b2/trajectory",
                 "computer": "https://api.amp.cisco.com/v1/computers/abfe956e-8b67-4d5c-9353-1b490cdad8b2",
                 "group":
     "https://api.amp.cisco.com/v1/groups/1d7e90f6-b6b6-49ba-90ab-a8fe13d8f3d4"
                },
            "group_guid": "1d7e90f6-b6b6-49ba-90ab-a8fe13d8f3d4",
            "active": "True",
            "operating_system": "Windows Server 2012 R2, SP 0.0",
           "network_addresses":
                [{
                   "ip": "10.0.0.4",
                   "mac": "00:0d:3a:4e:fc:6e"
                 },
                 {
                   "ip": "10.212.134.201",
                   "mac": "00:09:0f:aa:00:01"
                }],
           "faults": [],
           "external_ip": "13.72.107.194",
           "hostname": "poc-JuanV",
           "install_date": "2019-04-29T19:37:06Z",
           "connector_version": "6.2.9.10881",
           "internal_ips": ["10.0.0.4", " 10.212.134.201"],
           "policy":
               {
                  "guid": "9d8be508-fbec-457a-a0eb-c0cb82be482c",
                  "name": "Server"
               },
           "last_seen": "2019-05-28T11:46:32Z"
          }
        },
     "Entity": "entityIdentifier"
    }]
    

### Get Computers by Network Activity (URL)

#### Description

Fetch a list of computers that have connected to the given hostname or URL.

#### Run On

This action runs on the following entities:

  * Hostname
  * URL



#### Action Results

##### Entity Enrichment

Entities are marked as Suspicious (True) if they exceed threshold. Else: False.

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
##### JSON Result
    
    
    [{
      "EntityResult":
         {
          "0":
             {
              "connector_guid": "abfe956e-8b67-4d5c-9353-1b490cdad8b2",
              "links":
                 {
                  "trajectory": "https://api.amp.cisco.com/v1/computers/abfe956e-8b67-4d5c-9353-1b490cdad8b2/trajectory",
                  "computer": "https://api.amp.cisco.com/v1/computers/abfe956e-8b67-4d5c-9353-1b490cdad8b2",
                  "group": "https://api.amp.cisco.com/v1/groups/1d7e90f6-b6b6-49ba-90ab-a8fe13d8f3d4"
                 },
             "group_guid": "1d7e90f6-b6b6-49ba-90ab-a8fe13d8f3d4",
             "active": "True",
             "operating_system": "Windows Server 2012 R2, SP 0.0",
             "Network_addresses":
                 [{
                   "ip": "10.0.0.4",
                   "mac": "00:0d:3a:4e:fc:6e"
                  },
                  {
                   "ip": "10.212.134.201",
                   "mac": "00:09:0f:aa:00:01"
                 }],
            "faults": [],
            "external_ip": "13.72.107.194",
            "hostname": "poc-JuanV",
            "install_date": "2019-04-29T19:37:06Z",
            "connector_version": "6.2.9.10881",
            "internal_ips": ["10.0.0.4", " 10.212.134.201"],
            "policy":
                {
                  "guid": "9d8be508-fbec-457a-a0eb-c0cb82be482c",
                  "name": "Server"
                },
           "last_seen": "2019-05-28T11:46:32Z"
           }
        },
     "Entity": "entityIdentifier"
    }]
    

### File List Items

#### Description

Get the items listed in a given file list.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
File List Name | String | N/A | Yes | Example: File Blacklist  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
Items | True/False | items:False  
  
##### JSON Result
    
    
    {
      "Items":
        [{
          "source": "Created by uploading 1_Credit Card Magnetic Tracks - Notepad (2).TXT via Web from 1.1.1.1.",
          "sha256": "640e9583763fa553069a4984f8df5e81d6890897a6eb0f5de881218e3ed409c8", "description": ""
          },
         {
          "source": "Created by entering SHA-256 via Public api.",
          "sha256": "5fd924625f6ab16a19cc9807c7c506ae1813490e4ba675f843d5a10e0baacdb8",
          "description": "Added by Siemplify"
         },
         {
          "source": "Created by entering SHA-256 via Public api.",
          "sha256": "1248712441dbbf43bb37f91d626a020e7e0f4486f050142034b8a267b06a2f0c",
          "description": "Added by Siemplify"
       }],
     "guid": "cef9b12e-4a25-4f1a-93f4-3836ebd97ed5",
     "name": "File Blacklist"
    }
    

### Get File Lists by Policy

#### Description

Get the file lists that are assigned in a policy.

#### Parameters

**Parameter Display Name** | **Type** | **Default Value** | Is Mandatory | **Description**  
---|---|---|---|---  
Policy Name | String | N/A | Yes | The name of the policy e.g. Triage.  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
File_Lists | N/A | N/A  
  
##### JSON Result
    
    
    {
      "1":
        {
         "guid": "38c1a9eb-0389-4f12-8084-96f5ee62d72e",
         "type": "application_blocking",
         "name": "Execution Blacklist"},
         "0":
           {
             "guid": "cef9b12e-4a25-4f1a-93f4-3836ebd97ed5",
             "type": "simple_custom_detections",
             "name": "File Blacklist"
           },
        "2":
          {
             "guid": "3133128e-5455-4e74-82c5-1ff3c816c414",
             "type": "application_whitelist",
             "name": "File Whitelist"
        }
    }
    

### Get Groups

#### Description

Get group details.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
Groups | N/A | N/A  
  
##### JSON Result
    
    
    {
      "1":
        {
         "source": "CreatedviaAPI",
         "guid": "1111111111111111111111",
         "name": "TestGroup",
         "description": "GroupcreatedbySiemplify"
        },
      "0":
        {
         "source": null,
         "guid": "1111111111111111111111",
         "name": "Audit",
         "description": "AuditGroupforPartner-Siemplify"
        }
    }
    

### Get Policies

#### Description

Get policy details.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
Policies | N/A | N/A  
  
##### JSON Result
    
    
    {
      "1":
        {
         "product": "ios",
         "name": "Audit",
         "default": true,
         "serial_number": 38,
         "guid": "1111111111111111",
         "description": "ThispolicyputsClarityinamodethatwilllogandalertonconvictionsbutnotblocktraffic."
        },
      "0":
        {
         "product": "android",
         "name": "Protect",
         "default": true,
         "serial_number": 11,
         "guid": "1111111111111111",
         "description": "ThisisthestandardpolicyfortheAMPforEndpointsConnectorthatwillquarantinemaliciousfilesandblockmaliciousnetworkconnections."
       }
    }
    

### Ping

#### Description

Test connectivity to Cisco Secure Endpoint.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
success | True/False | success:False  
  
### Isolate Machine

#### Description

Isolate a host so it will stop network traffic to and from the isolated host.

#### Parameters

N/A

#### Use Cases

**Ransomware Detected on a host:**

  1. Stop ransomware process.
  2. Delete ransomware if possible.
  3. Isolate host.



#### Run On

This action runs on the following entities:

  * Host
  * Internal IP
  * External IP



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    "data": {
            "available": true,
            "status": "isolated",
            "unlock_code": "kzhduj",
            "comment": "Host pending investigation",
            "isolated_by": "Meny Har"
        }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:** _If successful:_ 'Target Host was isolated successfully:{host}/{Internal IP}/{External IP} _If unsuccessful:_ 'Target Host was not isolated successfully' **The action should fail and stop a playbook execution:** _If critical error, like wrong credentials or lost connectivity:_ 'Some errors occurred. Please check log.' | General  
  
### Unisolate Machine

#### Description

Stop isolation on a host to allow network traffic to and from the previously isolated host.

#### Run On

This action runs on the following entities:

  * Host
  * Internal IP
  * External IP



#### Action Results

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    "data": {
            "available": true,
            "status": "isolated",
            "unlock_code": "kzhduj",
            "comment": "Host confirmed:Infection free",
            "isolated_by": "Meny Har"
        }
    

##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If successful:_ print 'Target Host was unisolated successfully:{host}/{Internal IP}/{external IP}_If unsuccessful:_ print ****'Target Host was not unisolated successfully'**The action should fail and stop a playbook execution:**_If critical error, like wrong credentials or lost connectivity:_ 'Some errors occurred. Please check log.' | General  
  
## Connector

### Cisco AMP - Security Events Connector

#### Description

Pull security events from Cisco Secure Endpoint into Google SecOps.

**Note:** whitelist works with eventType parameter.

### Configure Cisco AMP - Security Events Connector on Google SecOps

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

##### Connector parameters

Use the following parameters to configure the connector:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Product Field Name | String | Product Name | Yes | Enter the source field name in order to retrieve the Product Field name.  
Event Field Name | String | eventType | Yes | Enter the source field name in order to retrieve the Event Field name.  
Environment Field Name | String | "" | No | Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.  
Environment Regex Pattern | String | .* | No | A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.  
Script Timeout (Seconds) | Integer | 180 | Yes | Timeout limit for the python process running the current script.  
API Root | String | https:/{{ip address}} | Yes | API root of the Cisco Secure Endpoint instance.  
Client ID | String |  | Yes | Cisco Secure Endpoint Client ID.  
API Key | Password |  | Yes | Cisco Secure Endpoint API Key.  
Lowest Severity To Fetch | String |  | No | Severity that will be used to fetch events. If nothing is specified, connector will ingest events with all severities. Events without severity data are handled by the "Fetch Events Without Severity" parameter. Possible values: Low, Medium, High, Critical.  
Fetch Events Without Severity | Checkbox |  | No | If enabled, the connector will fetch events that don't have severity. Those events will be assigned "Informational" severity.  
Max Hours Backwards | Integer | 1 | No | Amount of hours from where to fetch events.  
Max Events To Fetch | Integer | 100 | No | How many alerts to process per one connector iteration. Maximum is 1000. Default: 100.  
Use whitelist as a blacklist | Checkbox | Unchecked | Yes | If enabled, whitelist will be used as a blacklist.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the Cisco Secure Endpoint server is valid.  
Proxy Server Address | String |  | No | The address of the proxy server to use.  
Proxy Username | String |  | No | The proxy username to authenticate with.  
Proxy Password | Password |  | No | The proxy password to authenticate with.  
  
#### Connector Rules

##### Proxy Support

The connector supports Proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
