---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-mvision-epo/
title: McAfee MVISION ePO \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:08.716237+00:00
---

# McAfee MVISION ePO  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/mcafee-mvision-epo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# McAfee MVISION ePO

**Important:** McAfee MVISION ePO became part of the Trellix product portfolio and is known as MVISION ePO.

This document provides guidance on how to integrate McAfee MVISION ePO with Google SecOps.

## Product Use Cases

Malware Attack on an endpoint

  1. Malware attacks a computer in your McAfee ePO managed network.
  2. McAfee product software, for example, McAfee Endpoint Security cleans or deletes the malware file.
  3. McAfee Agent notifies McAfee ePO of the attack.
  4. McAfee ePO stores the attack information.



## Configure McAfee MVISION ePO integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

#### Integration Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
API Root | String | https://api.mvision.mcafee.com | Yes | McAfee MVISION ePO API Root.  
Client ID | String | N/A | Yes | Client ID of the McAfee MVISION ePO account.  
Client Secret | Password | N/A | Yes | Client Secret of the McAfee MVISION ePO account.  
Scopes | Comma-separated values | epo.device.r, epo.device.w,epo.grps.r, epo.grps.w, epo.sftw.r, epo.tags.r, epo.tags.w | Yes | Scopes of the McAfee MVISION ePO account.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify the SSL certificate for the connection to the McAfee MVISION ePO public cloud server is valid.  
Group Name | String | N/A | No | Group name that will be used to search for endpoints. If nothing is specified. All of the groups will be used.  
  
## Actions

### Ping

#### Description

Test connectivity to McAfee MVISION ePO with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Playbook Use Cases Examples

The action is used to test connectivity at the integration configuration page in the Google SecOps Content Hub page, and it can be executed as a manual action, not used in playbooks.

#### Run On

The action doesn't run on entities, nor has mandatory input parameters.

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
    

### Enrich Endpoint

#### Description

Fetch endpoint's system information by its hostname or IP address.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * IP Address
  * Hostname



#### Action Results

##### Entity Enrichment

Enrichment Field Name | Source (JSON Key) | Logic - When to apply  
---|---|---  
MMV_EPO_id | id | When available in JSON  
MMV_EPO_uuid | uuid | When available in JSON  
MMV_EPO_lastcommunicated | lastcommunicated | When available in JSON  
MMV_EPO_managedState | managedState | When available in JSON  
MMV_EPO_ipaddress | properties/ipaddress | When available in JSON  
MMV_EPO_osplatform | properties/osplatform | When available in JSON  
MMV_EPO_operatingsystem | properties/operatingsystem | When available in JSON  
MMV_EPO_hostname | properties/hostname | When available in JSON  
MMV_EPO_windowsdomain | properties/windowsdomain | When available in JSON  
MMV_EPO_dnsname | properties/dnsname | When available in JSON  
MMV_EPO_datversion | properties/datversion | When available in JSON  
MMV_EPO_username | properties/username | When available in JSON  
MMV_EPO_groups | space separated list of group/name | When available in JSON  
MMV_EPO_tags | space separated list of tags/tagName | When available in JSON  
  
##### Insights

N/A

##### Script Result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
        "data": {
            "totalItems": 8,
            "startIndex": 1,
            "currentItemCount": 1,
            "items": [
                {
                    "id": 227568,
                    "uuid": "fef3d9aa-e58e-ea11-87c6-005056a2196c",
                    "lastcommunicated": "2020-05-31T12:34:13.500+0000",
                    "managedState": "managed",
                    "properties": {
                        "cpuspeed": 2299,
                        "ipaddress": "172.30.202.30",
                        "osplatform": "Workstation",
                        "operatingsystem": "Linux",
                        "cputype": "Intel(R) Xeon(R) CPU E5-2698 v3 @ 2.30GHz",
                        "type": "non-portable",
                        "numofcpu": 2,
                        "hostname": "Centos7-001",
                        "windowsdomain": "(none)",
                        "dnsname": "Centos7-001",
                        "totalphysicalmemory": 2096254976,
                        "macaddress": "005056A2196C",
                        "datversion": "4253.0",
                        "amcorecontentdate": "2020-05-30 00:00:00.0",
                        "username": "root"
                    },
                    "group": {
                        "groupId": 372690,
                        "name": "Linux",
                        "path": "My Organization\\Linux",
                        "link": {
                            "rel": "group",
                            "href": "../groups/372690"
                        }
                    },
                    "tags": [
                        {
                            "tagId": 24751,
                            "tagName": "Workstation",
                            "link": {
                                "rel": "tag",
                                "href": "../tags/24751"
                            }
                        }
                    ],
                    "productsInstalled": [
                        {
                            "product": "Agent",
                            "version": "5.6.5.165"
                        },
                        {
                            "product": "MVISION EDR",
                            "version": "3.1.0.482"
                        },
                        {
                            "product": "Endpoint Security Platform",
                            "version": "10.7.0.130"
                        },
                        {
                            "product": "McAfee DXL Client",
                            "version": "6.0.0.218"
                        },
                        {
                            "product": "Endpoint Security Threat Prevention",
                            "version": "10.7.0.351"
                        }
                    ]
                }
            ]
        }
    }
    

### Add Tag

#### Description

Add tag to the endpoint in McAfee MVISION ePO.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Tag Name | String | N/A | True | Specify what tag you want to add to endpoint.  
  
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
    

### Remove Tag

#### Description

Remove tag from the endpoint in McAfee MVISION ePO.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Tag Name | String | N/A | True | Specify what tag you want to remove from endpoint.  
  
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
    

#### List Tags

#### Description

List tags that are available in McAfee MVISION ePO.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Max Tags to Return | Integer | 100 | False | Specify how many tags to return.  
  
#### Run On

This action doesn't run on entities.

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
    
    
    {
        "data": {
            "totalItems": 4,
            "startIndex": 0,
            "currentItemCount": 4,
            "items": [
                {
                    "id": 24752,
                    "name": "Escalated",
                    "description": "Protection Workspace tag for escalated systems",
                    "links": [
                        {
                            "rel": "self",
                            "href": "24752"
                        }
                    ]
                },
                {
                    "id": 24753,
                    "name": "Excluded from Compliance Check",
                    "description": "Protection Workspace tag for systems to be excluded from the compliance check",
                    "links": [
                        {
                            "rel": "self",
                            "href": "24753"
                        }
                    ]
                },
                {
                    "id": 24750,
                    "name": "Server",
                    "description": "Default tag for systems identified as a Server",
                    "links": [
                        {
                            "rel": "self",
                            "href": "24750"
                        }
                    ]
                },
                {
                    "id": 24751,
                    "name": "Workstation",
                    "description": "Default tag for systems identified as a Workstation",
                    "links": [
                        {
                            "rel": "self",
                            "href": "24751"
                        }
                    ]
                }
            ]
        }
    }
    

### List Groups

#### Description

List groups that are available in McAfee MVISION ePO.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Max Groups to Return | Integer | 100 | False | Specify how many groups to return.  
  
#### Run On

This action doesn't run on entities.

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
    
    
    {
        "data": {
            "totalItems": 12,
            "startIndex": 0,
            "currentItemCount": 1,
            "items": [
                {
                    "id": 1,
                    "name": "GlobalRoot",
                    "userFriendlyName": "Global Root",
                    "type": 7,
                    "parentId": 0,
                    "description": "",
                    "textPath": "GlobalRoot",
                    "links": [
                        {
                            "rel": "self",
                            "href": "1"
                        },
                        {
                            "rel": "parent",
                            "href": "0"
                        }
                    ]
                }
            ]
        }
    }
    

### List Endpoints In Group

#### Description

List endpoints that are in the same group in McAfee MVISION ePO.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Group Name | String | N/A | True | Specify in which groups to search for endpoints  
Max Endpoints to Return | Integer | 100 | False | Specify how many endpoints to return.  
  
#### Run On

The action doesn't run on entities.

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
    
    
    {
        "data": {
            "totalItems": 1,
            "startIndex": 0,
            "currentItemCount": 1,
            "items": [
                {
                    "id": 227568,
                    "uuid": "fef3d9aa-e58e-ea11-87c6-005056a2196c",
                    "lastcommunicated": "2020-05-31T13:34:13.327+0000",
                    "managedState": "managed",
                    "properties": {
                        "cpuspeed": 2299,
                        "ipaddress": "172.30.202.30",
                        "osplatform": "Workstation",
                        "operatingsystem": "Linux",
                        "cputype": "Intel(R) Xeon(R) CPU E5-2698 v3 @ 2.30GHz",
                        "type": "non-portable",
                        "numofcpu": 2,
                        "hostname": "Centos7-001",
                        "windows domain": "(none)",
                        "dnsname": "Centos7-001",
                        "totalphysicalmemory": 2096254976,
                        "macaddress": "005056A2196C",
                        "datversion": "4253.0",
                        "amcorecontentdate": "2020-05-30 00:00:00.0",
                        "username": "root"
                    },
                    "group": {
                        "groupId": 372690,
                        "name": "Linux",
                        "path": "My Organization\\Linux",
                        "link": {
                            "rel": "group",
                            "href": "../groups/372690"
                        }
                    },
                    "tags": [
                        {
                            "tagId": 24751,
                            "tagName": "Workstation",
                            "link": {
                                "rel": "tag",
                                "href": "../tags/24751"
                            }
                        }
                    ],
                    "productsInstalled": [
                        {
                            "product": "Agent",
                            "version": "5.6.5.165"
                        },
                        {
                            "product": "MVISION EDR",
                            "version": "3.1.0.482"
                        },
                        {
                            "product": "Endpoint Security Platform",
                            "version": "10.7.0.130"
                        },
                        {
                            "product": "McAfee DXL Client",
                            "version": "6.0.0.218"
                        },
                        {
                            "product": "Endpoint Security Threat Prevention",
                            "version": "10.7.0.351"
                        }
                    ]
                }
            ]
        }
    }
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
