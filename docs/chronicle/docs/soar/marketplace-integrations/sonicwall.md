---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sonicwall/
title: SonicWall-Beta \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:12.562276+00:00
---

# SonicWall-Beta  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/sonicwall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SonicWall-Beta

**Beta:** This integration refers to SonicWall and is in beta stage.

This document provides guidance on how to integrate SonicWall-Beta with Google SecOps.

## Product Use Cases

Perform management actions - add or remove IP from SonicWall Group, add URL to URI Lists/Groups.

## Authentication

You cannot authenticate to both the API and the Web UI at the same time. Make sure you have logged out of the Web UI before using the integration.

## Configure SonicWall integration in Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Ping

#### Description

Test connectivity to the SonicWall with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Playbook Use Cases Examples

The action is used to test connectivity at the integration configuration page in the Google SecOps Content Hub page, and it can be executed as a manual action, not used in playbooks.

#### Run On

The action doesn't run on entities, and does not have mandatory input parameters.

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
    

### Add IP to Address Group

#### Description

Add an IP address to specific SonicWall Address Group. Note that successful action execution commits all uncommitted changes.

**Note:** To get consistent results it is recommended to have two different Address Groups for different types of IP addresses.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Group Name | String | N/A | True | Specify to which group you want to add IP address. Groups that contain unicode characters are not supported.  
IP Zone | String | N/A | True | Specify the zone of the IP address that you want to add.  
  
#### Run On

This action runs on the IP Address entity.

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
    

### Remove IP from Address Group

#### Description

Remove IP address from specific SonicWall Address Group. Note that successful action execution commits all uncommitted changes.

**Note:** To get consistent results it is recommended to have two different Address Groups for different types of IP addresses.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Group Name | String | N/A | True | Specify from which group you want to remove the IP address. Groups that contain unicode characters are not supported.  
  
#### Run On

This action runs on the IP Address entity.

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
    

### List Address Groups

#### Description

List SonicWall Address Groups.

**Note:** To get consistent results it is recommended to have two different Address Groups for different types of IP addresses.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Address Type | Dropdown  
| IPv4Possible values:  
IPv4IPv6All | False | Specify which address type should be used for address groups.  
Max Address Groups To Return | Int | 100 | False | Specify how many address groups to return.  
  
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
      "address_groups": [
          {
              "ipv4": {
                  "name": "Public Mail Server Address Group",
                  "uuid": "601b29f9-6c3b-18c3-0200-00401038b139"
              }
          },
          {
              "ipv4": {
                  "name": "Default Trusted Relay Agent List",
                  "uuid": "d4590e52-b145-5835-0200-00401038b139"
              }
          },
          {
              "ipv4": {
                  "name": "McAfee Client AV Enforcement List",
                  "uuid": "4f555370-3660-3aee-0200-00401038b139"
              }
          },
          {
              "ipv4": {
                  "name": "Excluded from McAfee Client AV Enforcement List",
                  "uuid": "3d7ead85-d36b-51de-0200-00401038b139"
              }
          },
          {
              "ipv4": {
                  "name": "Kaspersky Client AV Enforcement List",
                  "uuid": "5d7701ac-4247-ffb4-0200-00401038b139"
              }
          },
          {
              "ipv4": {
                  "name": "Excluded from Kaspersky Client AV Enforcement List",
                  "uuid": "98ea70c8-d3e0-7584-0200-00401038b139"
              }
          },
          {
              "ipv4": {
                  "name": "Excluded from Client AV Enforcement List",
                  "uuid": "fe0a4372-936f-1747-0200-00401038b139"
              }
          },
          {
              "ipv4": {
                  "name": "Capture Client Enforcement List",
                  "uuid": "6878046d-34a8-deda-0200-00401038b139"
              }
          },
          {
              "ipv4": {
                  "name": "Excluded from DPI-SSL Enforcement List",
                  "uuid": "354a69f3-0ee5-7d6c-0200-00401038b139"
              }
          },
          {
              "ipv4": {
                  "name": "All X4 Management IP",
                  "uuid": "e3413593-7f84-9e36-0200-00401038b139",
                  "address_object": {
                      "ipv4": [
                          {
                              "name": "X4 IP"
                          }
                      ]
                  }
              }
          },
          {
              "ipv4": {
                  "name": "All X5 Management IP",
                  "uuid": "8e9df420-5e71-37f7-0200-00401038b139",
                  "address_object": {
                      "ipv4": [
                          {
                              "name": "X5 IP"
                          }
                      ]
                  }
              }
          },
          {
              "ipv4": {
                  "name": "All X6 Management IP",
                  "uuid": "a28cfb77-fe27-892e-0200-00401038b139",
                  "address_object": {
                      "ipv4": [
                          {
                              "name": "X6 IP"
                          }
                      ]
                  }
              }
          },
          {
              "ipv4": {
                  "name": "Siemplify Block List",
                  "uuid": "00000000-0000-0003-0200-00401038b139",
                  "address_object": {
                      "ipv4": [
                          {
                              "name": "Siemplify 192.168.168.168 DMZ"
                          },
                          {
                              "name": "Dogo"
                          },
                          {
                              "name": "X0 IP"
                          }
                      ]
                  }
              }
          }
      ]
    }
    

#### Add URL to URI List

#### Description

Add URL to specific SonicWall URI List.

**Note:** SonicWall API doesn't support URLs that contain Unicode characters.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
URI List Name | String | N/A | True | Specify to which URI List you want to add the URL. URI Lists that contain unicode characters are not supported.  
  
#### Run On

This action runs on the URL entity.

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
    

### Remove URL from URI List

#### Description

Remove URL from specific SonicWall URI List.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
URI List Name | String | N/A | True | Specify to which URI List you want to add the URL. URI lists that contain unicode characters are not supported.  
  
#### Run On

This action runs on the URL entity.

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
    

### Add URI List to URI Group

#### Description

Add URI List to SonicWall URI Group.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
URI List Name | String | N/A | True | Specify which URI List you want to add the URI Group. URI Lists that contain unicode characters are not supported.  
URI Group Name | String | N/A | True | Specify to which URI Group you want to add the URI List. URI Groups that contain unicode characters are not supported.  
  
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
    
    
    N/A
    

### List URI Lists

#### Description

List SonicWall URI Lists. Requires SonicOS 6.5.3 or higher.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Max URI Lists To Return | Int | 100 | False | Specify how many URI Lists to return.  
  
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
      "content_filter": {
          "uri_list_object": [
              {
                  "name": "Block List",
                  "uri": [
                      {
                          "uri": "example.com"
                      },
                      {
                          "uri": "example.com/news/123.html"
                      },
                      {
                          "uri": "string.com"
                      },
                      {
                          "uri": "string"
                      }
                  ]
              },
              {
                  "name": "Test",
                  "uri": [
                      {
                          "uri": "qweewq"
                      }
                  ]
              }
          ]
      }
    }
    

### List URI Groups

#### Description

List SonicWall URI Groups.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Max URI Groups To Return | Int | 100 | False | Specify how many URI Groups to return.  
  
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
      "content_filter": {
          "uri_list_group": [
              {
                  "name": "URI TEst",
                  "uri_list_object": [
                      {
                          "name": "Block List"
                      }
                  ]
              },
              {
                  "name": "asd",
                  "uri_list_group": [
                      {
                          "name": "URI TEst"
                      }
                  ],
                  "uri_list_object": [
                      {
                          "name": "Block List"
                      }
                  ]
              }
          ]
      }
    }
    

### Create CFS Profile

#### Description

Create SonicWall CFS Profile. Requires SonicOS 6.5.3 or higher.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Name | String |  | True | Specify the name of the CFS Profile. Unicode characters are not supported.  
Allowed URI List or Group | String |  | False | Specify the allowed URI list or group for the CFS Profile. URI List with unicode characters is not supported.  
Forbidden URI List or Group | String |  | False | Specify the forbidden URI list or group for the CFS Profile. Unicode characters are not supported.  
Search Order | DDL | Allowed URI First  
Possible values:  
Forbidden URI First | True | Specify the search order for the CFS Profile.  
Operation for Forbidden URI | DDL | Block  
Possible values:  
BlockConfirmPassphrase | True | Specify the operation for forbidden URI for the CFS Profile.  
Enable Smart Filter | Checkbox | Checked | True | Enable Smart Filter.  
Enable Google Safe Search | Checkbox | Checked | True | Enable Google Safe Search.  
Enable Youtube Restricted Mode | Checkbox | Checked | True | Enable Youtube Restricted Mode.  
Enable Bing Safe Search | Checkbox | Checked | True | Enable Bing Safe Search.  
  
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
    
    
    N/A
    

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
