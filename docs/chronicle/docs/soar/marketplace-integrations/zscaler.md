---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/zscaler/
title: Zscaler \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:49.224487+00:00
---

# Zscaler  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/zscaler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Zscaler

This document provides guidance on how to integrate Zscaler with Google SecOps.

## Use cases

The **Zscaler** integration uses Google SecOps capabilities to support the following use cases:

  * **Manage URL filtering** : Automatically update URL categories and filtering rules to block malicious domains identified during investigations.

  * **Automate user lifecycle management** : Dynamically manage user access and group memberships in Zscaler based on security risk levels.

  * **Enrich network alerts** : Retrieve detailed information about users, departments, and locations associated with blocked traffic.

  * **Synchronize security policies** : Instantly deploy security changes across your Zscaler environment to respond to active threats.




## Before you begin

Before you configure the integration in Google SecOps, verify that your Zscaler environment meets the following requirements:

  * **Authentication method** : Determine whether your organization uses OAuth 2.0 or legacy credential-based authentication. The integration uses these credentials to establish a session and retrieve a temporary token for API requests:

    * **OAuth 2.0 (recommended)** : This method uses the ZSLogin service for centralized identity management. You must register an OAuth 2.0 client in your identity provider and add the authorization server to the ZIA Admin Portal. For details, see [Securing ZIA APIs with OAuth 2.0](https://help.zscaler.com/zia/securing-zia-apis-oauth-2.0).

    * **Legacy credential** : This method uses an API Key and ZIA administrator credentials. For details, see [Managing Cloud Service API Key](https://help.zscaler.com/zia/managing-cloud-service-api-key).

  * **Account permissions** : Ensure the client or administrator account has the correct roles assigned:

    * **OAuth 2.0** : Requires an API role. For details, see [Adding API Roles](https://help.zscaler.com/zia/adding-api-roles).

    * **Legacy credential** : Requires an administrator role with API access permissions enabled. For details, see [Adding Admin Roles](https://help.zscaler.com/zia/adding-admin-roles).

  * **Network access** : Ensure your network configuration allows outbound HTTPS connections from your Google SecOps environment to the Zscaler API endpoints, for example, `zsapi.{your_cloud_name}`.




## Integration parameters

The **Zscaler** integration requires the following parameters:

Parameter | Description  
---|---  
`Api Root` |  Required. The base URL of the Zscaler instance, for example, `https://admin.zscalertwo.net` or `https://api.zsapi.net`.  
`Login ID` |  Optional. The username or email address associated with the Zscaler administrator account used for authentication. This parameter is mandatory for legacy authentication. If both legacy and OAuth 2.0 credentials are provided, OAuth 2.0 takes precedence.  
`Api Key` |  Optional. The unique API key generated in the Zscaler portal to authorize API requests. This parameter is mandatory for legacy authentication. If both legacy and OAuth 2.0 credentials are provided, OAuth 2.0 takes precedence.  
`Password` |  Optional. The password associated with the Zscaler administrator account used for authentication. This parameter is mandatory for legacy authentication. If both legacy and OAuth 2.0 credentials are provided, OAuth 2.0 takes precedence.  
`Verify SSL` |  Optional. If selected, the integration validates the SSL certificate when connecting to the Zscaler server. Enabled by default.  
`Client ID` |  Optional. The unique identifier for the OAuth 2.0 client used for authentication using the ZSLogin service. This parameter is mandatory for OAuth 2.0 configuration and takes precedence over legacy authentication.  
`Client Secret` |  Optional. The secret key associated with the client ID used to authenticate the OAuth 2.0 client. This parameter is mandatory for OAuth 2.0 configuration and takes precedence over legacy authentication.  
`Login API Root` |  Optional. The base URL for the ZSLogin service used for centralized identity and access management. This parameter is mandatory for OAuth 2.0 configuration and takes precedence over legacy authentication. The default value is `https://{instance}.zslogin.net`.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add to Blacklist

Adds a URL/Domain/IP to the blocklist.

**Note:** If the submitted URL begins with `http://` or `https://`, the action blocks the entire domain instead of the specific URL.

#### Action inputs

This action requires the following parameters:

Parameter | Description  
---|---  
`IOCs` | Optional. A comma-separated list of IOCs (IP addresses, URLs, or domains) to add to the blocklist, for example, `10.1.1.1, google.com, http://example.net`.  
  
#### Run On

This action runs on the following entities:

  * URL
  * Hostname
  * IP Address



##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Add to Whitelist

Adds a URL/Domain/IP to the allowlist.

#### Action inputs

This action requires the following parameters:

Parameter | Description  
---|---  
`IOCs` | Optional. A comma-separated list of IOCs (IP addresses, URLs, or domains) to add to the allowlist, for example, `10.1.1.1, google.com, http://example.net`.  
  
#### Run On

This action runs on the following entities:

  * URL
  * Hostname
  * Domain



##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Get Blacklist

Gets a list of black-listed URLs.

#### Parameters

N/A

#### Run On

This action runs on all entities.

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Get Sandbox Report

Get a full report for an MD5 hash of a file that was analyzed by Sandbox.

#### Parameters

N/A

#### Run On

This action runs on the Filehash entity.

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "EntityResult":
            {
                "Full Details":
                {
                  "SystemSummary": [
                        {
                            "SignatureSources": [
                                "",
                                "76CD0000 page execute and read and write",
                                "76DD0000 page execute and read and write"
                               ],
                            "Risk": "LOW",
                            "Signature": "Allocates memory within range which is reserved for system DLLs"
                        },{
                         "SignatureSources": [
                                "",
                                "wow64.pdb source: loaddll32.exe",
                                "wow64.pdbH source: loaddll32.exe",
                                "wow64cpu.pdb source: loaddll32.exe",
                                "wow64win.pdb source: loaddll32.exe",
                                "wow64win.pdbH source: loaddll32.exe"
                            ],
                            "Risk": "LOW",
                            "Signature": "Binary contains paths to debug symbols"
                        },{
                            "SignatureSources": [
                                "",
                                "clean0.winDLL@1/1@0/0"
                            ],
                            "Risk": "LOW",
                            "Signature": "Classification label"
                        }, {
                            "SignatureSources":[
                                "",
                                "More than 502 > 100 exports found"
                            ],
                         "Risk": "LOW",
                         "Signature": "PE file exports many functions"
                       }, {
                         "SignatureSources": [
                                 "",
                                 "Virtual size of .text is bigger than: 0x100000"
                                ],
                         "Risk": "LOW",
                         "Signature": "PE file has a big code size"
                        },{
                         "SignatureSources": [
                                 "",
                                 "Raw size of .text is bigger than: 0x100000 < 0x176000"
                         ],
                            "Risk": "LOW",
                            "Signature": "PE file has a big raw section"
                        }, {
                         "SignatureSources": [
                             "",
                             "Image base 0x704c0000 > 0x60000000"
                         ],
                            "Risk": "LOW",
                            "Signature": "PE file has a high image base. often used for DLLs"
                        }, {
                            "SignatureSources": [
                                "",
                                "Section: .text IMAGE_SCN_ALIGN_MASK, IMAGE_SCN_ALIGN_256BYTES, IMAGE_SCN_ALIGN_16BYTES, IMAGE_SCN_ALIGN_64BYTES, IMAGE_SCN_ALIGN_1BYTES, IMAGE_SCN_MEM_EXECUTE, IMAGE_SCN_CNT_INITIALIZED_DATA, IMAGE_SCN_ALIGN_2048BYTES, IMAGE_SCN_ALIGN_1024BYTES, IMAGE_SCN"
                            ],
                            "Risk": "LOW",
                            "Signature": "PE file has an executable .text section and no other executable section"
                        }, {
                          "SignatureSources": [
                              "", "HKEY_USERS\\\\Software\\\\Policies\\\\Microsoft\\\\Windows\\\\Safer\\\\CodeIdentifiers"
                          ],
                            "Risk": "LOW",
                            "Signature": "Reads software policies"
                        },{
                          "SignatureSources": [
                              "",
                              "File size 1710606 > 1048576"
                          ],
                            "Risk": "LOW",
                            "Signature": "Submission file is bigger than most known malware samples"
                        },{
                           "SignatureSources": [
                               "",
                               "no activity detected"
                           ],
                            "Risk": "MODERATE",
                            "Signature": "Program does not show much activity"
                        }
                    ],
                    "Summary":
                    {
                        "Status": "COMPLETED",
                        "Category": "EXECS",
                        "FileType": "DLL",
                        "Duration": 499618,
                        "StartTime": 1553130306
                    },
                    "Classification":
                    {
                        "Category": "BENIGN",
                        "Type": "BENIGN",
                        "Score": 0,
                        "DetectedMalware": ""
                    },
                    "Persistence":[
                        {
                            "SignatureSources": [
                                "",
                                "section name: /4"
                            ],
                            "Risk": "LOW",
                            "Signature": "PE file contains sections with non-standard names"
                        }
                    ],
                    "FileProperties":
                    {
                        "SHA1": "b0aa7eecfa6c0066504bf79efe1bc057ac61e9b8",
                        "FileSize": 1710606,
                        "RootCA": "",
                        "Issuer": "",
                        "FileType": "DLL",
                        "Sha256": "a39180232ae6a689650f5df566bb4e81b94d9d19a53363ce17d7a12fd21f78cf",
                        "DigitalCerificate": "",
                        "SSDeep": "24576:3LnYQhDtnNgQe42lcCZNj4I/MmaOdb+Y+mmY5Gc3nGkh2sQginrgGGQCTQIMGNdd:zYQlEpIE/p3nFhckZF7oU",
                        "MD5": "1803c2c0f0ec61c98b3630d7e4b1cd5d"
                    }
                }
            },
            "Entity": "1803C2C0F0EC61C98B3630D7E4B1CD5D"
        }
    ]
    

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
Full Details | Returns if it exists in JSON result  
  
##### Insights

N/A

### Get URL Categories

Gets information about all URL categories.

#### Parameters

N/A

#### Run On

This action runs on all entities.

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
            "description": "OTHER_ADULT_MATERIAL_DESC",
            "val": 1,
            "dbCategorizedUrls": [],
            "editable": true,
            "urls": [],
            "customCategory": false,
            "id": "OTHER_ADULT_MATERIAL"
        }, {
            "description": "ADULT_THEMES_DESC",
            "val": 2,
            "dbCategorizedUrls": [],
            "editable": true,
            "urls": [],
            "customCategory": false,
            "id": "ADULT_THEMES"
        }
    ]
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Get Whitelist

Gets a list of white-listed URLs.

#### Parameters

N/A

#### Run On

This action runs on all entities.

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Lookup Entity

Look up the categorization of a URL/Domain/IP.

#### Parameters

N/A

#### Run On

This action runs on the following entities:

  * URL
  * Hostname
  * Domain



##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
        {
       "EntityResult": {
           "url": "markossolomon.com/f1q7qx.php",
           "urlClassificationsWithSecurityAlert": ["MALWARE_SITE"],
           "urlClassifications": []
       },
            "Entity": "HTTP://MARKOSSOLOMON.COM/F1Q7QX.PHP"
        }
    ]
    

##### Entity Enrichment

Enrichment Field Name | Logic - When to apply  
---|---  
url | Returns if it exists in JSON result  
urlClassificationsWithSecurityAlert | Returns if it exists in JSON result  
urlClassifications | Returns if it exists in JSON result  
  
##### Insights

N/A

### Ping

Check connectivity.

#### Parameters

N/A

#### Run On

This action runs on all entities.

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Remove From Blacklist

Removes a URL/Domain/IP from the blocklist.

#### Action inputs

This action requires the following parameters:

Parameter | Description  
---|---  
`IOCs` | Optional. A comma-separated list of IOCs (IP addresses, URLs, or domains) to remove from the blocklist, for example, `10.1.1.1, google.com, http://example.net`.  
  
#### Run On

This action runs on the following entities:

  * URL
  * Hostname
  * IP Address



##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

### Remove From Whitelist

Removes a URL/Domain/IP from the allowlist.

#### Action inputs

This action requires the following parameters:

Parameter | Description  
---|---  
`IOCs` | Optional. A comma-separated list of IOCs (IP addresses, URLs, or domains) to remove from the allowlist, for example, `10.1.1.1, google.com, http://example.net`.  
  
#### Run On

This action runs on the following entities:

  * URL
  * Hostname
  * IP Address



##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Entity Enrichment

N/A

##### Insights

N/A

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
