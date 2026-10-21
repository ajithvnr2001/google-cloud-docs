---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cylance/
title: Cylance \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:39:28.997180+00:00
---

# Cylance  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/cylance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cylance

**Important:** Cylance was acquired by BlackBerry and became part of BlackBerry Cybersecurity.

This document describes how to integrate Cylance with Google Security Operations.

## Configure Cylance integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Add to Global List

#### Description

Add a hash to one of the two global lists: GlobalSafe or GlobalQuarantine.

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
List Type | String | N/A | The list to add the hash to. Example: GlobalSafe  
Category | String | N/A | The category of the hash.  
Reason | String | N/A | The reason for adding the hash to the list.  
  
#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Change Policy

#### Description

Change the policy of an endpoint to an existing policy.

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
Policy Name | String | N/A | The new policy name.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Change Zone

#### Description

Change the zone for an endpoint (group of endpoints).

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
Zones to Add | String | N/A | The new Zone to Add. Comma separated.  
Zones to Remove | String | N/A | The Zone to be removed. Comma separated.  
  
#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Delete From Global List

#### Description

Remove a hash for the specified global list (GlobalSafe or GlobalQuarantine).

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
**Parameter** | **Type** | **Default Value** | **Description**  
List Type | String | N/A | The list to delete the hash from. Example: GlobalSafe  
  
#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

### Enrich Entities

#### Description

Enrich the hostname and IP addresses with extra Cylance data.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
update_available | Returns if it exists in JSON result  
date_last_modified | Returns if it exists in JSON result  
distinguished_name | Returns if it exists in JSON result  
policy | Returns if it exists in JSON result  
date_offline | Returns if it exists in JSON result  
ip_addresses | Returns if it exists in JSON result  
mac_addresses | Returns if it exists in JSON result  
last_logged_in_user | Returns if it exists in JSON result  
agent_version | Returns if it exists in JSON result  
os_version | Returns if it exists in JSON result  
state | Returns if it exists in JSON result  
update_type | Returns if it exists in JSON result  
date_first_registered | Returns if it exists in JSON result  
host_name | Returns if it exists in JSON result  
is_safe | Returns if it exists in JSON result  
background_detection | Returns if it exists in JSON result  
id | Returns if it exists in JSON result  
name | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    ​[{
       "EntityResult":
         {
           "update_available": false,
           "date_last_modified": "2012-01-16T10:04:27",
           "distinguished_name": "CN=PC-01,CN=Computers,DC=DOMAIN,DC=COM",
           "policy":
             {
               "id": "1413b00e-50bc-4438-base-04935713aabf",
               "name": "A_policy"
             },
          "date_offline": null,
          "ip_addresses": ["1.92.168.0.3"],
          "mac_addresses": ["AB-CD-C4-12-A2-73"],
          "last_logged_in_user": "DOMAIN\\\\user",
          "agent_version": "2.0.1510",
          "os_version": "Microsoft Windows 10 Pro",
          "state": "Online",
          "update_type": null,
          "date_first_registered": "2012-03-27T11:35:12",
          "host_name": "PC-01.DOMAIN.COM",
          "is_safe": true,
          "background_detection": false,
          "id": "8e501f3b-d3c3-4549-94af-5b3335af247d",
          "name": "PC-01"
         },
       "Entity": "PC-01"
    }]
    

### Get Global List

#### Description

Retrieve a list of all the hashes in the specified global list (GlobalSafe or GlobalQuarantine).

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
List Type | String | N/A | Name of the global list. Example: GlobalSafe  
  
#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "category": "Drivers",
            "added": "2018-04-01T16:14:01",
            "name": "MaliciousFile.exe",
            "classification": "",
            "sub_classification": "",
            "av_industry": null,
            "reason": "Testing actions",
            "list_type": "GlobalSafe",
            "sha256": "9890B2F415D096B3E5B259C414166C7E0C7C2BE7AB7FBE0C30ACC67AA78D7BC6",
            "cylance_score": -0.999,
            "added_by": "a4366b76-669e-46ac-acb8-67d1d8e2c5ed",
            "md5": "F0D291E88A11CCCF31BC358DCB83ACC2"
        },{
            "category": "Drivers",
            "added": "2018-04-01T13:13:03",
            "name":"ThisWillDestroyYourComputer.exe",
            "classification": "",
            "sub_classification": "",
            "av_industry": null,
            "reason": "Testing actions",
            "list_type": "GlobalSafe",
            "sha256": "EB83B77112874E1082BBD529182DD22C5C0BFD2390E4C1584CBE1C50CBB3FD03",
            "cylance_score": -0.999,
            "added_by": "a4366b76-669e-46ac-acb8-67d1d8e2c5ed",
            "md5": "8A1B7AF7A850493D3683C6EC660CA454"
        }
    ]
    

### Get Threat

#### Description

Enrich a hash with data from Cylance.

#### Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
Threshold | String | 0 | Mark entity as suspicious if the threat Cylance score pass the given threshold. Example: 3  
  
#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

Entities are marked as Suspicious (True) if they exceed the threshold. Else: False.

Enrichment Field Name | Logic - When to apply  
---|---  
cylance_score | Returns if it exists in JSON result  
name | Returns if it exists in JSON result  
classification | Returns if it exists in JSON result  
last_found | Returns if it exists in JSON result  
av_industry | Returns if it exists in JSON result  
unique_to_cylance | Returns if it exists in JSON result  
global_quarantined | Returns if it exists in JSON result  
file_size | Returns if it exists in JSON result  
safelisted | Returns if it exists in JSON result  
sha256 | Returns if it exists in JSON result  
md5 | Returns if it exists in JSON result  
sub_classification | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [{
       "EntityResult":
        {
          "cylance_score": -1.0,
          "name": "mpress.exe",
          "classification": "Trusted",
          "last_found": "2018-03-28T20:34:44",
          "av_industry": null,
          "unique_to_cylance": true,
          "global_quarantined": false,
          "file_size": 103424,
          "safelisted": false,
          "sha256": "2852680C94A9D68CDAB285012D9328A1CECA290DB60C9E35155C2BB3E46A41B4",
          "md5": "8B632BFC3FE653A510CBA277C2D699D1",
          "sub_classification": "Local"
        },
      "Entity": "8B632BFC3FE653A510CBA277C2D699D1"
    }]
    

### Get Threat Devices

#### Description

Get threats associated to a particular hostname or an IP address.

#### Parameters

N/A

#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
name | Returns if it exists in JSON result  
ip_addresses | Returns if it exists in JSON result  
mac_addresses | Returns if it exists in JSON result  
id | Returns if it exists in JSON result  
state | Returns if it exists in JSON result  
date_found | Returns if it exists in JSON result  
file_status | Returns if it exists in JSON result  
agent_version | Returns if it exists in JSON result  
file_path | Returns if it exists in JSON result  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [{
       "EntityResult":
         [{
           "name": "DESKTOP-CL0OJIN",
           "ip_addresses": ["169.254.195.84", "192.168.2.100"],
           "mac_addresses": ["02-00-4C-4F-4F-50", "CC-2F-71-24-2D-59"],
           "id": "0805c701-009b-4d2a-8d52-142e3af38c33",
           "state": "OffLine",
           "date_found": "2018-03-28T20:34:44",
           "file_status": "Quarantined",
           "agent_version": "2.0.1480",
           "file_path": "C:\\\\Users\\\\Daniel\\\\Downloads\\\\mpress.219\\\\mpress.exe", "policy_id": "1429b00e-50bc-4038-bcae-04935713aabf"
         }],
       "Entity": "2852680c94a9d68cdab285012d9328a1ceca290db60c9e35155c2bb3e46a41b4"
    }]
    

### Get Threat Download Link

#### Description

Get the download link of a threat file for further use and sandboxing from Cylance to Google SecOps.

#### Parameters

Parameter Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Threat SHA256 Hash | String  
| N/A | No  
| Threat SHA256 hashes, in a comma separated list. Note: If parameter value will be left empty, action will use file hash entities as input.  
  
#### Run On

This action runs on the Filehash entity.

#### Action Results

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
Clyance_dl | When available in JSON  
  
##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:****if successful:** print "Successfully fetched download link for following hashes: {file_hash_list}"**If file hash not found:** print "Action could not fetch download link for following hashes: {file_hash_list}"  
  
If none of the file hashes was found: print "No Download links were fetched"****  
**The action should fail and stop a playbook execution:****if not successful: (400 - bad request, 401- unauthorized, 403 forbidden, 500 internal server error):** print "Error executing action "Get Threat Download Link". Reason: {0}''.format(error.Stacktrace) | General  
  
### Get Threats

#### Description

Retrieve a list of all the available threats in the system.

#### Parameters

N/A

#### Run On

This action runs on all entities.

#### Action Results

##### Entity Enrichment

N/A

##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "cylance_score": -0.999,
            "name": "BADguyFILE.exe",
            "classification": "",
            "last_found": "2018-03-29T14:26:56",
            "av_industry": null,
            "unique_to_cylance": false,
            "global_quarantined": false,
            "sub_classification": "",
            "file_size": 31246,
            "safelisted": false,
            "sha256": "19D51872FEC52363589C46E869B9A7A7EC567CB2AED6DBF9B206FC04AE7361DA",
            "md5": "859214628259F59A1DD3ABE8C3201346"
        },{
            "cylance_score": -1.0,
            "name": "mpress.exe",
            "classification": "Trusted",
            "last_found": "2018-03-28T20:34:44",
            "av_industry": null,
            "unique_to_cylance": true,
            "global_quarantined": false,
            "sub_classification": "Local",
            "file_size": 103424,
            "safelisted": false,
            "sha256":"2852680C94A9D68CDAB285012D9328A1CECA290DB60C9E35155C2BB3E46A41B4",
            md5": "8B632BFC3FE653A510CBA277C2D699D1"
        }
    ]
    

## Connectors

### Cylance Connector

#### Description

N/A

#### Connector Parameters

Parameter Name | Type | Default Value | Description  
---|---|---|---  
DeviceProductField | 2 | device_product | The field name used to determine the device product.  
EventClassId | 2 | N/A | The field name used to determine the event name (sub-type).  
PythonProcessTimeout | 2 | 60 | The timeout limit (in seconds) for the python process running current script.  
API Root | 2 | N/A | https://protectapi.cylance.com/  
Application Secret | 3 | N/A | Used to sign the Application ID.  
Application ID | 2 | N/A | Used to indicate the token requested.  
Tenant Identifier | 2 | N/A | ID number of tenant information being queried.  
Proxy Server Address | 2 | N/A | The address of the proxy server to use.  
Proxy Username | 2 | N/A | The proxy username to authenticate with.  
Proxy Password | 3 | N/A | The proxy password to authenticate with.  
  
#### Connector Rules

##### Blacklist/Whitelist

Connector doesn't support Blacklist/Whitelist rule.

##### Proxy support

Connector supports Proxy.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
